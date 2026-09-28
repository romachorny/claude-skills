#!/usr/bin/env python3
"""Numeric QA for a generated video clip.

Usage: python qa.py clip.mp4 [--size 320]
Writes <clip>_sheet.jpg and <clip>_motion.png next to the clip and prints a JSON report.
Requires ffmpeg on PATH, numpy and Pillow.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
         "-show_entries", "stream=width,height,r_frame_rate,nb_read_frames:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True, check=True).stdout
    j = json.loads(out)
    s = j["streams"][0]
    num, den = s["r_frame_rate"].split("/")
    return {
        "width": s["width"], "height": s["height"],
        "fps": round(int(num) / int(den), 3),
        "frames": int(s.get("nb_read_frames", 0)),
        "duration": float(j["format"]["duration"]),
    }


def frames(path, width):
    info = probe(path)
    h = int(round(info["height"] * width / info["width"] / 2) * 2)
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-vf", f"scale={width}:{h}",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
        capture_output=True, check=True).stdout
    arr = np.frombuffer(raw, np.uint8).reshape(-1, h, width, 3)
    return info, arr


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    width = int(sys.argv[sys.argv.index("--size") + 1]) if "--size" in sys.argv else 320
    info, f = frames(path, width)
    g = f.astype(np.float32).mean(axis=3)

    diffs = np.abs(np.diff(g, axis=0))
    motion = diffs.sum(axis=0)
    per_step = diffs.mean(axis=(1, 2))

    H, W = motion.shape
    grid = [[float(motion[r * H // 6:(r + 1) * H // 6, c * W // 6:(c + 1) * W // 6].mean() / len(diffs))
             for c in range(6)] for r in range(6)]
    flat = [v for row in grid for v in row]
    thr = 0.25 * max(flat) if max(flat) > 0 else 0

    brightness = g.mean(axis=(1, 2))
    slope = float(np.polyfit(np.arange(len(brightness)), brightness, 1)[0]) if len(brightness) > 1 else 0.0

    report = {
        "file": path.name,
        **info,
        "mean_neighbour_diff": round(float(per_step.mean()), 2),
        "cells_with_motion": int(sum(v > thr for v in flat)),
        "liveliest_cell": round(max(flat), 2),
        "grid_6x6": [[round(v, 2) for v in row] for row in grid],
        "loop_seam": round(float(np.abs(g[0] - g[-1]).mean()), 2),
        "brightness_trend_per_frame": round(slope, 4),
    }

    m = motion / motion.max() * 255 if motion.max() > 0 else motion
    Image.fromarray(m.astype(np.uint8)).save(path.with_name(path.stem + "_motion.png"))

    idx = np.linspace(0, len(f) - 1, 16).astype(int)
    fh, fw = f.shape[1:3]
    sheet = Image.new("RGB", (fw * 4, fh * 4))
    for k, i in enumerate(idx):
        sheet.paste(Image.fromarray(f[i]), ((k % 4) * fw, (k // 4) * fh))
    sheet.save(path.with_name(path.stem + "_sheet.jpg"), quality=88)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
