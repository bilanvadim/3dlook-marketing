import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os
F = os.environ.get('JOST_TTF', 'Jost-var.ttf')
def font(size, wght):
    f = ImageFont.truetype(F, size); f.set_variation_by_axes([wght]); return f

W, H = 1080, 1350
src = Image.open(sys.argv[2] if len(sys.argv) > 2 else 'fitxpress-post-1800x942.png').convert('RGB')
# the old subtitle's tail ("…ness", x 580-662) would leak into the crop: erase it per column
a = np.array(src).astype(float)
for y in range(421, 470):
    t = (y - 420) / (470 - 420)
    a[y, 575:672] = a[420, 575:672] * (1 - t) + a[470, 575:672] * t
src = Image.fromarray(a.clip(0, 255).astype('uint8'))
X0, X1 = 580, 1745
s = W / (X1 - X0)
crop = src.crop((X0, 0, X1, 942)).resize((W, round(942 * s)), Image.LANCZOS)
CY = H - crop.height

# header background: continue the crop's top row upward (hair columns bridged, smoothed)
top = np.array(crop).astype(float)[2]
hx0, hx1 = int((790 - X0) * s), int((1260 - X0) * s)   # hair + shoulders at the top edge
for x in range(hx0, hx1):
    t = (x - hx0) / (hx1 - hx0); top[x] = top[hx0 - 1] * (1 - t) + top[hx1] * t
k = 41; pad = np.pad(top, ((k, k), (0, 0)), mode='edge')
top = np.array([pad[i:i + 2 * k + 1].mean(0) for i in range(W)])
bg = np.repeat(top[None, :, :], H, axis=0)
canvas = Image.fromarray(bg.clip(0, 255).astype('uint8')).convert('RGBA')

# crop with a soft top fade into the header
FADE = 110
alpha = np.full((crop.height, W), 255, np.uint8)
alpha[:FADE] = (np.linspace(0, 1, FADE) ** 1.4 * 255).astype(np.uint8)[:, None]
c = crop.convert('RGBA'); c.putalpha(Image.fromarray(alpha))
canvas.alpha_composite(c, (0, CY))

d = ImageDraw.Draw(canvas)
WHITE = (255, 255, 255, 255)
# logo
logo = Image.open('logo_big.png').convert('RGBA')
LW = 210; logo = logo.resize((LW, round(logo.height * LW / logo.width)), Image.LANCZOS)
canvas.alpha_composite(logo, (64, 64))
# title + subtitle
ft = font(92, 400); b = ft.getbbox('FitXpress')
d.text((64 - b[0], 150 - b[1]), 'FitXpress', font=ft, fill=WHITE)
fs = font(38, 400)
for i, line in enumerate(['AI-powered body scanning', 'technology for next-level', 'fitness progress tracking']):
    b = fs.getbbox('A'); d.text((64, 290 + 48 * i - b[1]), line, font=fs, fill=WHITE)

# body fat card, lifted from the fixed banner, top-right of the header
card = src.crop((88, 615, 368, 879)).convert('RGBA')
m = Image.new('L', card.size, 0)
ImageDraw.Draw(m).rounded_rectangle((1, 1, card.width - 2, card.height - 2), radius=17, fill=255)
card.putalpha(m)
canvas.alpha_composite(card, (W - 64 - card.width, 120))

canvas.convert('RGB').save(sys.argv[1])
