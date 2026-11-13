#!/usr/bin/env python3
"""Anonymous booth blocks for the full-floor map (Venetian Expo, Level 2, Halls A-D).

Source: the Freeman "Target Freight Move-In" plan of Halls A-D (revision 11/3/2026, private repo
events/ces-2027/manual/). Every booth there is filled with a move-in colour, so booths are easy to
separate from aisles. The plan is shifted and scaled against the 10/5/2026 floor plan that
v2/map_data.py uses; the transform below was fitted on 440 booth numbers present in both PDFs
(pdftotext -bbox), median error 0.016 units, max 0.075. Output is in v2 map units.

No names, no booth numbers: only rectangles. Usage:
  python3 extract_booths.py /path/to/venetian-halls-a-d-target-move-in.pdf  ->  booths_full.json
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

DPI = 288                      # 4 px per plan unit
A_X, B_X = 1.00362293, -107.397439   # x_v2 = A_X * x_movein + B_X
A_Y, B_Y = 1.00364164, -6.393361     # y_v2 = A_Y * y_movein + B_Y
BOOTH_RGB = [(0, 165, 124), (127, 191, 255), (214, 214, 214), (152, 88, 253), (255, 168, 233),
             (255, 127, 0)]
CROP = (150, 30, 1010, 700)    # v2 units: the hall, without the legend and title block
RES = 0.5                      # output grid, units


def dilate(m, r):
    out = m.copy()
    for d in range(1, r + 1):
        out[d:, :] |= m[:-d, :]; out[:-d, :] |= m[d:, :]
    m2 = out.copy()
    for d in range(1, r + 1):
        out[:, d:] |= m2[:, :-d]; out[:, :-d] |= m2[:, d:]
    return out


def erode(m, r):
    return ~dilate(~m, r)


def main(pdf):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-png", "-singlefile", pdf, f"{td}/p"], check=True)
        rgb = np.asarray(Image.open(f"{td}/p.png").convert("RGB")).astype(np.int16)
    mask = np.zeros(rgb.shape[:2], bool)
    for c in BOOTH_RGB:
        mask |= (np.abs(rgb - np.array(c)).sum(axis=2) < 40)
    # seal booth outlines and text, fill the holes, then restore the size
    m = dilate(mask, 3)
    inv = Image.fromarray(((~m) * 255).astype(np.uint8)).copy()  # writable, floodfill is a no-op otherwise
    # the plan has a frame, so the outside is not one region: flood the aisle network and the
    # margins from several seeds (v2 units); whatever stays unreached is a hole inside a booth
    seeds = [(750, 452), (450, 330), (450, 162), (300, 330), (200, 447), (600, 600), (705, 560),
             (-60, 20), (-60, 760), (1100, 20), (1100, 760), (980, 300), (300, 760)]
    for sx, sy in seeds:
        px = int((sx - B_X) / A_X * DPI / 72); py = int((sy - B_Y) / A_Y * DPI / 72)
        if 0 <= px < inv.width and 0 <= py < inv.height and inv.getpixel((px, py)) == 255:
            ImageDraw.floodfill(inv, (px, py), 128)
    holes = np.asarray(inv) == 255
    m = erode(m | holes, 3)
    # resample onto the v2 grid
    x0, y0, x1, y1 = CROP
    xs = np.arange(x0, x1, RES) + RES / 2
    ys = np.arange(y0, y1, RES) + RES / 2
    px = np.clip(((xs - B_X) / A_X * DPI / 72).astype(int), 0, m.shape[1] - 1)
    py = np.clip(((ys - B_Y) / A_Y * DPI / 72).astype(int), 0, m.shape[0] - 1)
    g = m[np.ix_(py, px)]
    # rectangles: merge identical horizontal runs of consecutive rows
    rects, open_ = [], {}
    for j in range(g.shape[0] + 1):
        runs = set()
        if j < g.shape[0]:
            row = np.concatenate([[0], g[j].astype(np.int8), [0]])
            d = np.diff(row)
            runs = set(zip(np.where(d == 1)[0], np.where(d == -1)[0]))
        for k in list(open_):
            if k not in runs:
                a, b = k; jj = open_.pop(k)
                rects.append((x0 + a * RES, y0 + jj * RES, (b - a) * RES, (j - jj) * RES))
        for k in runs:
            open_.setdefault(k, j)
    rects = [r for r in rects if r[2] * r[3] >= 4]
    out = Path(__file__).with_name("booths_full.json")
    out.write_text(json.dumps([[round(v, 2) for v in r] for r in rects]))
    print(out, len(rects), "rects")


if __name__ == "__main__":
    main(sys.argv[1])
