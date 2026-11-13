---
product: company
type: readme
vertical: none
status: sent-to-kristina
date: 2026-11-13
---

# /meet-us/ v3: the "find us" map as looping videos

Vadim, 2026-11-13, on Kristina's prototype (Figma «Website», page Conference, frame 5170:5929):
loop the route, no replay button, no total distance, only steps 1-5, no note under the map; then
"redraw it in our design system", "show more of the floor", "colour it like Kristina's", "add the 3DLOOK logo".

The map block on the page becomes a `<video autoplay muted loop playsinline>` with a poster, one file
per route tab (foyer, west). The numbered steps next to it stay HTML text and match the numbers on the map.

## Files

| File | What |
|---|---|
| `extract_booths.py` | Anonymous booth blocks of Halls A-D from the Freeman move-in plan of 11/3/2026 (private repo, `events/ces-2027/manual/`). Booths there are filled with move-in colours, so they separate cleanly from aisles. Transform to v2 map units fitted on 440 booth numbers present in both plans (`pdftotext -bbox`), max error 0.075 units; no booth moved between 10/5 and 11/3. Output: `booths_full.json` (rectangles only, no names, no numbers) |
| `build_full.py` | v3a: the whole floor. Hand-traced hall outline, walkways, ballroom, zone labels; shared geometry and helpers for v3b. Vadim: too far out |
| `build_map.py` | **v3b, the one in use**: middle zoom (Health area, ballroom, foyer, west concourse, edges of Smart Home and Lifestyle), Kristina's visual language, 3DLOOK symbol in the booth pin and the wordmark in the booth pill (`brand-assets/logos/`) |
| `tools/render_video.js`, `tools/frame.js` | MP4 and single-frame render (system Chrome via the Playwright MCP module), `#render` stops the preview loop |

## Rebuild

```
python3 extract_booths.py ~/3dlook-marketing-private/events/ces-2027/manual/venetian-halls-a-d-target-move-in.pdf
python3 build_map.py
for k in foyer west; do
  VW=1600 VH=1272 node tools/render_video.js out/find-$k.html out/ces2027-booth-55630-map-$k-1600.mp4 30
  VH=1272 node tools/frame.js out/find-$k.html out/ces2027-booth-55630-map-$k-poster-1600.png 9.4
done
```

GIF: `ffmpeg -i X.mp4 -vf "fps=15,scale=900:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 X.gif`.
The canvas height must be even (H.264).

## Animation

11.4 s loop: 0.6 s start, 7.2 s walk (dashed route revealed through a mask, the walker dot, step dots pop
when reached), 1.6 s arrival pulse, 1.2 s hold, 0.8 s fade back to the first frame. Step dots sit where
each step begins. The west route runs at x 581.7, the aisle centre on the 11/3 plan.

## Outputs

Drive, «CES 2027 Marketing» → «Find-us map v3 (2026-11-13)»: `ces2027-booth-55630-map-{foyer,west}`
MP4 1600×1272, GIF 900 px, poster PNG. The whole-floor v3a files are in the subfolder «Old · whole floor
(do not use)». Sent to Kristina in Slack on 2026-11-13 together with the other prototype comments.

## Before launch

Re-check both routes against the final floor plan in December (v1 TODO 16), rebuild, re-render.
