---
name: animating-classical-paintings
description: Standard for bringing classical paintings to life with AI video (living paintings). Two modes, license check, take selection, anti-stuck protocol, eight acceptance rules, prompt template and numeric frame-by-frame QA. Use for any living painting, museum loop or immersive art series.
---

# Animating classical paintings

A production standard built on real series work: a portfolio showreel and loops meant to hang in a room for hours. It exists because mixing up the two modes once stopped the work for two days.

## 1. Decide the mode first. There are two

**Mode A, portfolio.** Showreel, social, a link in a message. About 8 seconds, loud motion across the whole frame, people may walk, no loop needed. The eight rules below do NOT apply.

**Mode B, licensed series.** A loop that hangs on a wall for hours. About 2 minutes, seamless loop, quiet motion in one zone. All eight rules apply.

Never judge a piece of one mode by the other mode's rules. If the mode is not stated, ask in one line before starting.

## 2. Rights: check every file before you generate

Search anywhere (museum catalogues, Wikimedia Commons, Europeana, Artvee), but open the file page and read the license before taking it into work. Twenty seconds per painting.

- Commons is a warehouse, not a license. The uploader sets the license, and it differs file by file.
- OK: CC0, PD-old-100, PD-Art when the Source field points to a museum with an open collection.
- NOT OK: CC BY-SA (share-alike poisons a commercial derivative), "PD-US only", anything NC.
- Safe default collections: Rijksmuseum (CC0, commercial use explicitly allowed), The Met Open Access (CC0, has an API), Smithsonian Open Access.
- Do not download from Google Arts & Culture, it breaks their ToS.
- 20th century: public domain depends on the author's death date and differs by country. Check each author. When unclear, pick another painting. We are not lawyers.

## 3. Method: select, don't steer

- 4 to 5 takes on a short prompt beat one take on a perfect prompt.
- A bad take means the next take, not a one-word prompt edit.
- Keeper seconds: a rejected take almost always has 2 or 3 clean seconds. The final can be cut from pieces of different takes.
- A long descriptive prompt plus first/last frame makes the generator repaint the canvas from text. Formula: "REFERENCE = FINAL RESULT, video = how the light arrives".
- Simple motion (breathing zoom, moving light patches, shadow) is cheaper and cleaner done in Python from the scan: zero credits, brushwork intact. Call the generator only for real physics: water, smoke, clouds, fabric.

## 4. Anti-stuck protocol

An argument about one failing painting should take two minutes, not two days.

1. Bench of 15 to 20 candidates for a series of eight.
2. Ceiling of three takes per painting. No fourth.
3. Change the moving zone once. Usually the zone is wrong, not the painting: you chose water, the sky works. Three more takes.
4. Then the painting goes to the back of the queue. Take the next one from the bench. No more discussion.
5. The series closes on the eighth ACCEPTED piece, not when all chosen pieces are forced through.
6. Order from easy to hard: big skies, storms, smoke, open water first. Interiors and large faces last.

A series theme passes three checks: one physical phenomenon across all eight works, one rights source, not done by anyone or done badly. "Nature" and "animals" are shelves, not themes.

## 5. The taste line, one sentence (mode B)

Animation reveals what is already on the canvas and adds nothing the artist did not paint. It is almost always crossed the moment a human face comes alive.

## 6. Eight acceptance rules (mode B only)

1. Museum scan only, at maximum resolution.
2. One moving zone per work. Water OR smoke OR fabric. Everything else is dead still.
3. Motion follows the brushstroke: displacement along a flow map, not a global fractal noise shift.
4. No face comes alive. No blink, no turn, no breath. Hands, jugs, bread stay solid.
5. Nothing that is not on the canvas. No added objects, no recomposition, no outpainted edges.
6. No element completes a visible cycle faster than eight seconds. The camera is slower than feels right.
7. The loop is seamless and verified by a number. Encode all-intra with a constant quantizer.
8. The person who did not make the piece accepts it, with an explicit instruction to hunt for defects.

## 7. Move / don't touch (mode B)

Move: environment and elements (sky, clouds, water, rain, snow, smoke), what already moves in the stroke, light and time of day, dust in a beam, reflections, fabric in a soft sway, scale without recomposition, parallax without inventing hidden areas.

Don't touch: faces, gazes, expressions, figure actions, new objects, composition geometry, speech, clip tempo instead of painting tempo.

## 8. Prompt: forbid by name, not by description

The generator adds effects on its own. Forbid each one by name.

```
Static camera, absolutely no zoom, no pan, no push-in.
The painting is a still object: canvas edges must never move.
ONLY [one zone] changes, returning exactly to the starting state.
Period 8 seconds, seamless loop.
No faces move. No figures move. No heads turn. No eyes move. No hands.
No light shafts, no god rays, no volumetric beams, no dust, no sparkles,
no glitter, no smoke, no added objects.
Do not repaint any surface: preserve original brushwork and craquelure.
Amplitude at the threshold of perception.
```

If the generator crops the painting to 16:9 and cuts the frame, feed first/last already letterboxed to 16:9 with black bars.

## 9. Frame-by-frame QA by numbers

Use the companion skill `frame-by-frame-video-qa`. Report one line per broken rule with its number, then the next prompt version as a block.

Reference numbers from two 8-second 1280x720 clips:

- mean difference between neighbour frames: accepted mode A piece 6.43, rejected mode B take 1.51
- cells with motion out of 36: 32 vs 36
- liveliest zone energy: 17.37 vs 3.26
- first vs last frame difference: 53 vs 44

The mode A reference breaks the eight rules harder than the rejected mode B take. That is fine. Never apply one mode's rules to the other.

## 10. Industry numbers

- Immersive programme 35 to 52 minutes; a single work stays on screen 6 to 7 seconds on average.
- Masters in ProRes or uncompressed (media servers like Modulo Kinetic, Hive Player).
- Specs talk about brightness, not resolution: 9 to 10 foot-lamberts for 2D.
- A show takes about 8 weeks to produce.

## 11. References

Genre: B E A U T Y by Rino Stefano Tagliafierro. Brushstroke life: Loving Vincent. Rhythm: the animated Qingming scroll, Expo 2010.
Research on amplitudes: Animating Pictures with Stochastic Motion Textures (SIGGRAPH 2005); Generative Image Dynamics (CVPR 2024).
