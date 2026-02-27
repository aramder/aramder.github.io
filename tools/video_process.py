"""
Video processing wrapper for FFmpeg.
Supports stabilization (vid.stab), cropping, and timeline trimming.

Usage:
    python video_process.py <input.mp4> [options]

Examples:
    python video_process.py input.mp4 --stabilize
    python video_process.py input.mp4 --trim 00:01:30 00:03:45
    python video_process.py input.mp4 --crop 1280:720
    python video_process.py input.mp4 --stabilize --trim 00:00:10 00:00:30 --crop 1280:720
"""

import argparse
import subprocess
import shutil
import sys
import os
import json
import tempfile
from pathlib import Path


def ffmpeg_safe_path(path: str) -> str:
    """Convert a Windows path to an FFmpeg filter-safe path.

    FFmpeg filter option parser treats \\ as escape and : as option separator.
    Fix by using forward slashes and escaping the drive-letter colon.
    """
    safe = path.replace("\\", "/")
    # Escape the colon after drive letter, e.g. C: -> C\\:
    if len(safe) >= 2 and safe[1] == ":":
        safe = safe[0] + "\\\\:" + safe[2:]
    return safe


def check_ffmpeg():
    """Verify FFmpeg is installed and has vid.stab support."""
    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg not found in PATH.")
        print("Download from https://www.gyan.dev/ffmpeg/builds/ (full build for vid.stab)")
        sys.exit(1)

    result = subprocess.run(
        ["ffmpeg", "-filters"],
        capture_output=True, text=True
    )
    has_vidstab = "vidstab" in result.stdout
    if not has_vidstab:
        print("WARNING: vid.stab not found in this FFmpeg build.")
        print("Stabilization will not work. Get the 'full' build from gyan.dev.")
    return has_vidstab


def probe_video(input_path: str) -> dict:
    """Get video metadata via ffprobe."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_format", "-show_streams",
        input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ffprobe failed: {result.stderr}")
        sys.exit(1)
    info = json.loads(result.stdout)

    for s in info.get("streams", []):
        if s.get("codec_type") == "video":
            w = int(s.get("width", 0))
            h = int(s.get("height", 0))
            dur = float(info.get("format", {}).get("duration", 0))
            fps = s.get("r_frame_rate", "30/1")
            if "/" in fps:
                num, den = fps.split("/")
                fps_val = float(num) / float(den)
            else:
                fps_val = float(fps)
            print(f"  Resolution : {w}x{h}")
            print(f"  Duration   : {dur:.2f}s")
            print(f"  Frame rate : {fps_val:.2f} fps")
            print(f"  Codec      : {s.get('codec_name', 'unknown')}")
            return {"width": w, "height": h, "duration": dur, "fps": fps_val}

    print("ERROR: No video stream found.")
    sys.exit(1)


def build_output_path(input_path: str, suffix: str, output_dir: str = None) -> str:
    """Generate output filename with suffix, written to output_dir or same dir as input."""
    p = Path(input_path)
    # Clean up bracket artifacts from browser cache filenames like "file[1].mp4"
    stem = p.stem
    for bracket_suffix in ["[1]", "[2]", "[3]", "[4]", "[5]"]:
        stem = stem.replace(bracket_suffix, "")

    out_name = f"{stem}_{suffix}{p.suffix}"

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        return str(Path(output_dir) / out_name)
    else:
        return str(p.with_name(out_name))


def run_cmd(cmd: list, desc: str):
    """Run an FFmpeg command with progress output."""
    print(f"\n{'='*60}")
    print(f"  {desc}")
    print(f"{'='*60}")
    print(f"  CMD: {subprocess.list2cmdline(cmd)}\n")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"\nERROR: {desc} failed (exit code {result.returncode})")
        sys.exit(1)
    print(f"\n  Done: {desc}")


def process_video(
    input_path: str,
    stabilize: bool = False,
    shakiness: int = 8,
    smoothing: int = 20,
    zoom: int = 5,
    crop: str = None,
    trim_start: str = None,
    trim_end: str = None,
    crf: int = 18,
    preset: str = "slow",
    output: str = None,
    output_dir: str = None,
):
    """Main processing pipeline."""
    input_path = os.path.abspath(input_path)
    if not os.path.isfile(input_path):
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    print(f"\nInput: {input_path}")
    meta = probe_video(input_path)

    # Build filter chain
    filters = []

    # Use temp directory for the .trf file to avoid writing into cache dirs etc.
    trf_file = None
    if stabilize:
        trf_file = os.path.join(
            tempfile.gettempdir(),
            Path(input_path).stem + "_transforms.trf"
        )

        # Pass 1: detect motion
        trf_safe = ffmpeg_safe_path(trf_file)
        vf_detect = f"vidstabdetect=stepsize=6:shakiness={shakiness}:accuracy=15:result={trf_safe}"
        cmd1 = ["ffmpeg", "-y"]
        if trim_start:
            cmd1 += ["-ss", trim_start]
        if trim_end:
            cmd1 += ["-to", trim_end]
        cmd1 += ["-i", input_path, "-vf", vf_detect, "-f", "null", "-"]
        run_cmd(cmd1, "Pass 1/2: Analyzing motion")

        filters.append(
            f"vidstabtransform=input={trf_safe}:smoothing={smoothing}:zoom={zoom}"
        )
        filters.append("unsharp=5:5:0.8:3:3:0.4")

    # Crop
    if crop:
        filters.append(f"crop={crop}")

    # Build suffix for auto-naming
    suffix_parts = []
    if stabilize:
        suffix_parts.append("stab")
    if crop:
        suffix_parts.append("crop")
    if trim_start or trim_end:
        suffix_parts.append("trim")
    suffix = "_".join(suffix_parts) if suffix_parts else "processed"

    if output is None:
        output = build_output_path(input_path, suffix, output_dir)

    cmd2 = ["ffmpeg", "-y"]
    if trim_start:
        cmd2 += ["-ss", trim_start]
    if trim_end:
        cmd2 += ["-to", trim_end]
    cmd2 += ["-i", input_path]

    if filters:
        cmd2 += ["-vf", ",".join(filters)]

    cmd2 += [
        "-c:v", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        output,
    ]

    desc = "Pass 2/2: Stabilizing & encoding" if stabilize else "Encoding"
    run_cmd(cmd2, desc)

    # Cleanup transform file
    if trf_file and os.path.exists(trf_file):
        os.remove(trf_file)
        print(f"  Cleaned up: {trf_file}")

    # Report
    in_size = os.path.getsize(input_path) / (1024 * 1024)
    out_size = os.path.getsize(output) / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"  Input  : {in_size:.1f} MB  {input_path}")
    print(f"  Output : {out_size:.1f} MB  {output}")
    print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Video stabilization, cropping, and trimming via FFmpeg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s video.mp4 --stabilize
  %(prog)s video.mp4 --stabilize --shakiness 10 --smoothing 30
  %(prog)s video.mp4 --trim 00:00:05 00:00:30
  %(prog)s video.mp4 --crop 1280:720
  %(prog)s video.mp4 --crop 1280:720:320:180   (w:h:x:y)
  %(prog)s video.mp4 --stabilize --trim 00:00:10 00:01:00 --crop 1280:720
  %(prog)s "path with spaces/file[1].mp4" --stabilize --output-dir ~/Videos
        """,
    )
    parser.add_argument("input", help="Input MP4 file path (any location, no copying needed)")
    parser.add_argument("-o", "--output", help="Output file path (auto-generated if omitted)")
    parser.add_argument("--output-dir", help="Directory for output file (default: same as input, or ~/Videos if input is read-only)")

    # Stabilization
    stab = parser.add_argument_group("Stabilization")
    stab.add_argument("--stabilize", action="store_true", help="Enable video stabilization")
    stab.add_argument("--shakiness", type=int, default=8, help="Source shakiness 1-10 (default: 8)")
    stab.add_argument("--smoothing", type=int, default=20, help="Smoothing frames (default: 20, higher=smoother)")
    stab.add_argument("--zoom", type=int, default=5, help="Zoom %% to hide borders (default: 5)")

    # Crop
    cr = parser.add_argument_group("Cropping")
    cr.add_argument("--crop", help="Crop as w:h or w:h:x:y (e.g. 1280:720 or 1280:720:320:180)")

    # Trim
    tr = parser.add_argument_group("Trimming")
    tr.add_argument("--trim", nargs=2, metavar=("START", "END"),
                    help="Trim timeline: START END as HH:MM:SS or seconds")

    # Encoding
    enc = parser.add_argument_group("Encoding")
    enc.add_argument("--crf", type=int, default=18, help="Quality 0-51 (default: 18, lower=better)")
    enc.add_argument("--preset", default="slow",
                     choices=["ultrafast", "superfast", "veryfast", "faster", "fast",
                              "medium", "slow", "slower", "veryslow"],
                     help="Encoding preset (default: slow)")

    args = parser.parse_args()

    if not args.stabilize and not args.crop and not args.trim:
        parser.error("Specify at least one operation: --stabilize, --crop, or --trim")

    has_vidstab = check_ffmpeg()
    if args.stabilize and not has_vidstab:
        print("ERROR: Stabilization requested but vid.stab is not available.")
        sys.exit(1)

    # If no explicit output dir, check if input dir is writable; if not, fall back to ~/Videos
    output_dir = args.output_dir
    if not args.output and not output_dir:
        input_dir = os.path.dirname(os.path.abspath(args.input))
        if not os.access(input_dir, os.W_OK):
            output_dir = str(Path.home() / "Videos")
            print(f"  Input directory is not writable, writing output to: {output_dir}")

    trim_start = args.trim[0] if args.trim else None
    trim_end = args.trim[1] if args.trim else None

    process_video(
        input_path=args.input,
        stabilize=args.stabilize,
        shakiness=args.shakiness,
        smoothing=args.smoothing,
        zoom=args.zoom,
        crop=args.crop,
        trim_start=trim_start,
        trim_end=trim_end,
        crf=args.crf,
        preset=args.preset,
        output=args.output,
        output_dir=output_dir,
    )


if __name__ == "__main__":
    main()
