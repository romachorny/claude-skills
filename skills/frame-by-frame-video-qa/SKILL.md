---
name: frame-by-frame-video-qa
description: Accept or reject an AI-generated video clip by numbers instead of by eye - probe, contact sheet, motion map with a 6x6 energy grid, loop seam check, brightness drift and face crops. Use before sending any generated clip to a client or into an edit.
---

# Frame-by-frame video QA

Generated video looks fine at a glance and fails on the tenth watch. This skill turns "looks ok" into numbers you can compare between takes and between versions of a prompt.

## When to use

- Before a clip leaves the studio (client, edit, social).
- When choosing between several takes of the same shot.
- When a loop must be seamless (museum screens, backgrounds, product turntables).

## Steps

1. `ffprobe` the file: duration, fps, frame count, resolution. Wrong fps or a dropped frame is the first thing to catch.
2. Run `scripts/qa.py <clip.mp4>` (needs `ffmpeg`, `numpy`, `Pillow`). It writes next to the clip:
   - `*_sheet.jpg` a 4x4 contact sheet across the clip
   - `*_motion.png` accumulated `abs(frame[i] - frame[i-1])`, brighter means more motion
   - a JSON report on stdout
3. Read the report:
   - `mean_neighbour_diff` how alive the clip is overall
   - `grid_6x6` motion energy per cell, and `cells_with_motion` out of 36. A "one moving zone" shot should light up a few cells, not all of them
   - `loop_seam` difference between first and last frame, compare it with `mean_neighbour_diff`. A seamless loop has a seam close to a normal neighbour step
   - `brightness_trend` slope of mean brightness over time. A steady climb means exposure drift, not a cycle
4. If faces must stay still, crop the faces from 8 evenly spaced frames and put them in a row. Any change you can see there is a defect.
5. Write the verdict: one line per broken rule with its number, then what changes in the next take.

## Rules of thumb

- Compare takes of the same shot with each other, not with an absolute threshold.
- The accepter is not the maker. Ask a fresh reviewer, or a fresh agent, explicitly to hunt for defects.
- Keep the numbers with the take name. Next week they tell you which prompt worked.
