#!/usr/bin/env python3
"""
batch_color_correct.py - Batch image color correction tool

Applies white balance, brightness/exposure, and contrast/levels adjustments
to all JPEG, PNG, and TIFF images in a folder.

Requirements:
    pip install Pillow numpy

Usage examples:
    # Fully automatic (all corrections, defaults):
    python batch_color_correct.py photos/ output/

    # Manual brightness boost, no auto white balance:
    python batch_color_correct.py photos/ output/ --no-wb --brightness 1.3

    # Manual white balance (R/G/B multipliers) + stronger contrast:
    python batch_color_correct.py photos/ output/ --wb 1.1 1.0 0.85 --contrast 1.2

    # Tighter auto-levels clipping (clips top/bottom 0.5% instead of 1%):
    python batch_color_correct.py photos/ output/ --clip 0.5

    # Save without a suffix (overwrite originals in output folder):
    python batch_color_correct.py photos/ output/ --suffix "" --overwrite
"""

import argparse
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}


# ---------------------------------------------------------------------------
# Core correction functions
# ---------------------------------------------------------------------------

def auto_white_balance(arr: np.ndarray) -> np.ndarray:
    """
    Gray World white balance: scale each channel so all channel averages
    become equal to the overall mean luminance.
    """
    result = arr.astype(np.float32)
    per_channel_avg = result.mean(axis=(0, 1))   # shape (3,)
    gray = per_channel_avg.mean()
    scale = gray / (per_channel_avg + 1e-6)
    result *= scale
    return np.clip(result, 0, 255).astype(np.uint8)


def manual_white_balance(arr: np.ndarray, r: float, g: float, b: float) -> np.ndarray:
    """Scale individual R, G, B channels by the provided multipliers."""
    result = arr.astype(np.float32)
    result[:, :, 0] *= r
    result[:, :, 1] *= g
    result[:, :, 2] *= b
    return np.clip(result, 0, 255).astype(np.uint8)


def auto_levels(arr: np.ndarray, clip_percent: float = 1.0) -> np.ndarray:
    """
    Per-channel histogram stretch: clip the darkest and brightest `clip_percent`
    of pixels, then remap to 0–255.  Improves dynamic range without the
    colour shift of a luminance-only stretch.
    """
    result = arr.astype(np.float32)
    for ch in range(result.shape[2]):
        lo = np.percentile(result[:, :, ch], clip_percent)
        hi = np.percentile(result[:, :, ch], 100.0 - clip_percent)
        if hi > lo:
            result[:, :, ch] = (result[:, :, ch] - lo) / (hi - lo) * 255.0
    return np.clip(result, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def process_image(
    img: Image.Image,
    auto_wb: bool,
    wb_r: float,
    wb_g: float,
    wb_b: float,
    do_levels: bool,
    clip_percent: float,
    brightness: float,
    contrast: float,
) -> Image.Image:
    """Run the full correction pipeline on a single PIL Image."""
    # Preserve alpha channel if present; process RGB only.
    original_mode = img.mode
    has_alpha = original_mode in ("RGBA", "LA", "PA")

    alpha = None
    if has_alpha:
        alpha = img.split()[-1]

    rgb = img.convert("RGB")
    arr = np.array(rgb, dtype=np.uint8)

    # 1. White balance
    if auto_wb:
        arr = auto_white_balance(arr)
    elif not (wb_r == 1.0 and wb_g == 1.0 and wb_b == 1.0):
        arr = manual_white_balance(arr, wb_r, wb_g, wb_b)

    # 2. Auto levels / contrast stretch
    if do_levels:
        arr = auto_levels(arr, clip_percent)

    out = Image.fromarray(arr, mode="RGB")

    # 3. Brightness (PIL enhancer works on the full image in perceptual space)
    if brightness != 1.0:
        out = ImageEnhance.Brightness(out).enhance(brightness)

    # 4. Contrast
    if contrast != 1.0:
        out = ImageEnhance.Contrast(out).enhance(contrast)

    # Reattach alpha
    if has_alpha and alpha is not None:
        out = out.convert("RGBA")
        out.putalpha(alpha)

    return out


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Batch color correction: white balance, auto-levels, brightness, contrast.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    p.add_argument("input",  help="Input folder containing images")
    p.add_argument("output", help="Output folder for corrected images")

    # --- White balance ---
    wb = p.add_mutually_exclusive_group()
    wb.add_argument(
        "--no-wb", action="store_true",
        help="Disable white balance correction entirely",
    )
    wb.add_argument(
        "--wb", nargs=3, metavar=("R", "G", "B"), type=float,
        help="Manual white balance multipliers, e.g. --wb 1.1 1.0 0.85",
    )

    # --- Levels ---
    p.add_argument(
        "--no-levels", action="store_true",
        help="Disable automatic levels/contrast stretch",
    )
    p.add_argument(
        "--clip", type=float, default=1.0, metavar="PCT",
        help="Percentile to clip at each end during auto-levels (default: 1.0)",
    )

    # --- Tone ---
    p.add_argument(
        "--brightness", type=float, default=1.0,
        help="Brightness multiplier: 1.2 = 20%% brighter, 0.8 = 20%% darker (default: 1.0)",
    )
    p.add_argument(
        "--contrast", type=float, default=1.0,
        help="Contrast multiplier: 1.3 = 30%% more contrast (default: 1.0)",
    )

    # --- Output ---
    p.add_argument(
        "--suffix", default="_corrected",
        help='Suffix appended to output filenames (default: "_corrected")',
    )
    p.add_argument(
        "--overwrite", action="store_true",
        help="Overwrite existing output files instead of skipping them",
    )

    return p


def main() -> None:
    args = build_parser().parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)

    if not input_path.is_dir():
        print(f"Error: input folder not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    output_path.mkdir(parents=True, exist_ok=True)

    # Resolve WB settings
    auto_wb = not args.no_wb and args.wb is None
    wb_r = wb_g = wb_b = 1.0
    if args.wb:
        wb_r, wb_g, wb_b = args.wb

    # Gather supported images
    images = sorted(
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        print(f"No supported images found in {input_path}")
        sys.exit(0)

    print(f"Found {len(images)} image(s) in '{input_path}'")
    print(f"Settings:")
    if auto_wb:
        print(f"  White balance : auto (gray world)")
    elif args.wb:
        print(f"  White balance : manual  R={wb_r}  G={wb_g}  B={wb_b}")
    else:
        print(f"  White balance : disabled")
    print(f"  Auto levels   : {'on  (clip={args.clip}%)' if not args.no_levels else 'off'}")
    print(f"  Brightness    : {args.brightness}")
    print(f"  Contrast      : {args.contrast}")
    print()

    processed = skipped = errors = 0

    for img_path in images:
        out_name = f"{img_path.stem}{args.suffix}{img_path.suffix}"
        out_path = output_path / out_name

        if out_path.exists() and not args.overwrite:
            print(f"  [skip]  {img_path.name}  →  {out_name}  (already exists)")
            skipped += 1
            continue

        try:
            with Image.open(img_path) as img:
                # Keep EXIF if available
                exif = img.info.get("exif", b"")

                corrected = process_image(
                    img,
                    auto_wb=auto_wb,
                    wb_r=wb_r, wb_g=wb_g, wb_b=wb_b,
                    do_levels=not args.no_levels,
                    clip_percent=args.clip,
                    brightness=args.brightness,
                    contrast=args.contrast,
                )

                save_kwargs: dict = {}
                ext = img_path.suffix.lower()
                if ext in (".jpg", ".jpeg"):
                    save_kwargs["quality"]     = 95
                    save_kwargs["subsampling"] = 0
                    if exif:
                        save_kwargs["exif"] = exif
                elif ext in (".tif", ".tiff"):
                    save_kwargs["compression"] = "tiff_lzw"

                corrected.save(out_path, **save_kwargs)
                print(f"  [ok]    {img_path.name}  →  {out_name}")
                processed += 1

        except Exception as exc:
            print(f"  [error] {img_path.name}: {exc}", file=sys.stderr)
            errors += 1

    print(f"\nFinished — processed: {processed}, skipped: {skipped}, errors: {errors}")


if __name__ == "__main__":
    main()
