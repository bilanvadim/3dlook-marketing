import sys
from PIL import Image
import numpy as np
src, out = sys.argv[1], sys.argv[2]
im = np.array(Image.open(src).convert('RGB')).astype(float)
L = im.sum(2)

def interp_rows(x0, x1, y0, y1, xl, xr):
    """per row: linear between clean columns xl and xr"""
    for y in range(y0, y1):
        a, b = im[y, xl], im[y, xr]
        for x in range(x0, x1):
            t = (x - xl) / (xr - xl); im[y, x] = a * (1 - t) + b * t

def interp_cols(x0, x1, y0, y1):
    """per column: linear between clean rows y0-1 and y1 (band [y0,y1) replaced)"""
    ya, yb = y0 - 1, y1
    for y in range(y0, y1):
        t = (y - ya) / (yb - ya)
        im[y, x0:x1] = im[ya, x0:x1] * (1 - t) + im[yb, x0:x1] * t

# logo on the left gradient
interp_rows(84, 202, 52, 152, 80, 206)
# BMI card text (rows 246-278)
interp_cols(1188, 1272, 243, 282)
# metabolic card text (rows 370-405)
interp_cols(1186, 1278, 366, 409)
# transformation card: band by band, gaps between bands stay original glass
for a, b in [(503, 525), (535, 553), (569, 587), (595, 609), (624, 640), (650, 665), (680, 720)]:
    interp_cols(1040, 1270, a, b)
# body fat header value
interp_cols(298, 357, 636, 661)

# phone headline: rebuild the grid (flat navy + 1px lines)
rowprof = im[205, :].copy()   # clean row: vertical lines only
colprof = im[:, 1420].copy()  # clean column: horizontal lines only
for y in range(218, 358):
    if y < 300:
        edge = 1600
    else:
        xs = np.where(L[y, 1590:1630] > 300)[0]
        edge = 1590 + xs.min() if len(xs) else 1600
    for x in range(1426, edge - 3):
        im[y, x] = np.maximum(rowprof[x], colprof[y])
Image.fromarray(np.clip(im, 0, 255).astype('uint8')).save(out)
