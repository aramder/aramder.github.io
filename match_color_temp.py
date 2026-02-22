#!/usr/bin/env python3
"""
match_color_temp.py - Match all images in a folder to a reference image's
color temperature/white balance.

Analyzes the reference image's per-channel statistics and forces every other
image to match, producing visually consistent color temperature across
the batch.

Requirements:
    pip install Pillow numpy

Usage:
    python match_color_temp.py <folder> --ref <reference_image> [--suffix _processed]
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}


def get_channel_stats(arr: np.ndarray):
    """Return per-channel (mean, std) for an RGB array, ignoring near-black
    and near-white pixels to avoid skewing from clipped regions."""
    mask = (arr.min(axis=2) > 15) & (arr.max(axis=2) < 240)
    if mask.sum() < 100:
        # Fallback: use all pixels
        mask = np.ones(arr.shape[:2], dtype=bool)
    pixels = arr[mask].astype(np.float64)
    means = pixels.mean(axis=0)   # shape (3,)
    stds  = pixels.std(axis=0)    # shape (3,)
    return means, stds


def match_to_reference(arr: np.ndarray, ref_means, ref_stds, src_means, src_stds):
    """
    Reinhard-style color transfer: for each channel, shift and scale so that
    the source image's mean and std match the reference image's.

    pixel_out = (pixel_in - src_mean) * (ref_std / src_std) + ref_mean
    """
    result = arr.astype(np.float64)
    for ch in range(3):
        scale = ref_stds[ch] / (src_stds[ch] + 1e-6)
        result[:, :, ch] = (result[:, :, ch] - src_means[ch]) * scale + ref_means[ch]
    return np.clip(result, 0, 255).astype(np.uint8)


def process_image(img: Image.Image, ref_means, ref_stds) -> Image.Image:
    """Match a single image to the reference color profile."""
    original_mode = img.mode
    has_alpha = original_mode in ("RGBA", "LA", "PA")
    alpha = None
    if has_alpha:
        alpha = img.split()[-1]

    rgb = img.convert("RGB")
    arr = np.array(rgb, dtype=np.uint8)

    src_means, src_stds = get_channel_stats(arr)
    matched = match_to_reference(arr, ref_means, ref_stds, src_means, src_stds)

    out = Image.fromarray(matched)

    if has_alpha and alpha is not None:
        out = out.convert("RGBA")
        out.putalpha(alpha)

    return out


def main():
    p = argparse.ArgumentParser(
        description="Match all images to a reference image's color temperature.",
    )
    p.add_argument("folder", help="Folder containing images")
    p.add_argument("--ref", required=True, help="Reference image filename (inside the folder)")
    p.add_argument("--suffix", default="_processed", help="Output filename suffix (default: _processed)")
    p.add_argument("--output", default=None, help="Output folder (default: same as input)")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs")
    args = p.parse_args()

    folder = Path(args.folder)
    output = Path(args.output) if args.output else folder
    output.mkdir(parents=True, exist_ok=True)

    ref_path = folder / args.ref
    if not ref_path.exists():
        print(f"Error: reference image not found: {ref_path}", file=sys.stderr)
        sys.exit(1)

    # Analyze reference
    print(f"Reference image: {ref_path.name}")
    with Image.open(ref_path) as ref_img:
        ref_arr = np.array(ref_img.convert("RGB"), dtype=np.uint8)
        ref_means, ref_stds = get_channel_stats(ref_arr)

    print(f"  Channel means (R, G, B): {ref_means[0]:.1f}, {ref_means[1]:.1f}, {ref_means[2]:.1f}")
    print(f"  Channel stds  (R, G, B): {ref_stds[0]:.1f}, {ref_stds[1]:.1f}, {ref_stds[2]:.1f}")
    print()

    # Gather images
    images = sorted(
        f for f in folder.iterdir()
        if f.is_file()
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
        and args.suffix not in f.stem  # skip previously processed
    )

    if not images:
        print("No images found.")
        sys.exit(0)

    print(f"Processing {len(images)} image(s)...\n")

    log_entries = []
    processed = errors = 0
    for img_path in images:
        out_name = f"{img_path.stem}{args.suffix}{img_path.suffix}"
        out_path = output / out_name

        if out_path.exists() and not args.overwrite:
            print(f"  [skip]  {img_path.name} (output exists)")
            continue

        try:
            with Image.open(img_path) as img:
                exif = img.info.get("exif", b"")

                # Show before stats
                src_arr = np.array(img.convert("RGB"), dtype=np.uint8)
                src_means, src_stds = get_channel_stats(src_arr)

                corrected = process_image(img, ref_means, ref_stds)

                save_kwargs = {}
                ext = img_path.suffix.lower()
                if ext in (".jpg", ".jpeg"):
                    save_kwargs["quality"] = 95
                    save_kwargs["subsampling"] = 0
                    if exif:
                        save_kwargs["exif"] = exif

                corrected.save(out_path, **save_kwargs)

                print(f"  [ok]    {img_path.name}")
                print(f"          before  R={src_means[0]:.1f}  G={src_means[1]:.1f}  B={src_means[2]:.1f}")
                print(f"          target  R={ref_means[0]:.1f}  G={ref_means[1]:.1f}  B={ref_means[2]:.1f}")
                processed += 1

                log_entries.append({
                    "source": img_path.name,
                    "output": out_name,
                    "before_means": (src_means[0], src_means[1], src_means[2]),
                    "before_stds":  (src_stds[0],  src_stds[1],  src_stds[2]),
                })

        except Exception as exc:
            print(f"  [error] {img_path.name}: {exc}", file=sys.stderr)
            errors += 1

    print(f"\nFinished — processed: {processed}, errors: {errors}")

    # Write processing log
    log_path = output / "processing_log.txt"
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("Color Temperature Matching — Processing Log\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Date:       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Tool:       match_color_temp.py\n")
        f.write(f"Method:     Reinhard color transfer (per-channel mean/std matching)\n\n")
        f.write(f"Command:    {' '.join(sys.argv)}\n\n")
        f.write(f"Input folder:  {folder.resolve()}\n")
        f.write(f"Output folder: {output.resolve()}\n")
        f.write(f"Suffix:        {args.suffix}\n\n")
        f.write(f"Reference image: {args.ref}\n")
        f.write(f"  Channel means (R, G, B): {ref_means[0]:.2f}, {ref_means[1]:.2f}, {ref_means[2]:.2f}\n")
        f.write(f"  Channel stds  (R, G, B): {ref_stds[0]:.2f}, {ref_stds[1]:.2f}, {ref_stds[2]:.2f}\n")
        f.write(f"  (Stats computed on pixels with min > 15, max < 240 to exclude clipped regions)\n\n")
        f.write("-" * 50 + "\n")
        f.write(f"Images processed: {processed}  |  Errors: {errors}\n")
        f.write("-" * 50 + "\n\n")
        for entry in log_entries:
            bm = entry["before_means"]
            bs = entry["before_stds"]
            f.write(f"  {entry['source']}\n")
            f.write(f"    -> {entry['output']}\n")
            f.write(f"    Original means  R={bm[0]:.2f}  G={bm[1]:.2f}  B={bm[2]:.2f}\n")
            f.write(f"    Original stds   R={bs[0]:.2f}  G={bs[1]:.2f}  B={bs[2]:.2f}\n")
            f.write(f"    Matched to ref  R={ref_means[0]:.2f}  G={ref_means[1]:.2f}  B={ref_means[2]:.2f}\n\n")

    print(f"Log written to {log_path}")


if __name__ == "__main__":
    main()
