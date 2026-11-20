import sys
from PIL import Image, ImageDraw, ImageFont
import os
F = os.environ.get('JOST_TTF', 'Jost-var.ttf')
def font(size, wght):
    f = ImageFont.truetype(F, size); f.set_variation_by_axes([wght]); return f

im = Image.open('base_clean.png').convert('RGBA')
d = ImageDraw.Draw(im)
WHITE = (255, 255, 255, 255)
CYAN = (19, 224, 242, 255)
BLUE_TXT = (28, 110, 255, 255)
NEUTRAL = (196, 201, 224, 255)

def text_top(x, top, t, f, fill, anchor_right=False):
    """draw t so its ink top sits at `top` (left x, or right edge x if anchor_right)"""
    b = f.getbbox(t)
    ox = x - b[2] if anchor_right else x - b[0]
    d.text((ox, top - b[1]), t, font=f, fill=fill)

# logo: white horizontal lockup, replaces the light-blue symbol
logo = Image.open('logo_big.png').convert('RGBA')
LW = 230; logo = logo.resize((LW, round(logo.height * LW / logo.width)), Image.LANCZOS)
im.alpha_composite(logo, (92, 101 - logo.height // 2))

# BMI card (metric, Vadim/AU 2026-11-20): 168 cm, 63.5 kg -> BMI 22.5
text_top(1193, 246, 'Your BMI', font(12, 500), WHITE)
text_top(1193, 265, '22.5', font(17, 500), WHITE)

# BMR card: Katch-McArdle at 23% body fat, 63.5 kg -> ~1,420 kcal/day
text_top(1191, 370, 'Your BMR', font(12, 500), WHITE)
fv, fu = font(25, 500), font(11, 500)
bv = fv.getbbox('1,420')
d.text((1191 - bv[0], 389 - bv[1]), '1,420', font=fv, fill=WHITE)
digit_bottom = 389 + (fv.getbbox('1')[3] - fv.getbbox('1')[1])
bu = fu.getbbox('kcal')
d.text((1191 + (bv[2] - bv[0]) + 2 - bu[0], digit_bottom - bu[3]), 'kcal', font=fu, fill=WHITE)

# progress card: the post's story — scale barely moves, waist and body fat do
text_top(1048, 507, 'Your progress', font(20, 500), WHITE)
text_top(1047, 539, '3 MONTHS', font(14, 400), BLUE_TXT)
rows = [  # label, value, value colour, fill end x, gradient
    ('Weight',   '−0.3 kg', NEUTRAL, 1064, ((110, 116, 160), (170, 176, 205))),
    ('Waist',    '−2.5 cm', CYAN,    1168, ((20, 61, 255), (19, 224, 242))),
    ('Body fat', '−2%',     CYAN,    1140, ((20, 61, 255), (19, 224, 242))),
]
for i, (lab, val, vc, fend, (c0, c1)) in enumerate(rows):
    ly, by = 573 + 55 * i, 599 + 55 * i
    text_top(1049, ly, lab, font(12, 500), WHITE)
    text_top(1259, ly, val, font(12, 500), vc, anchor_right=True)
    # track
    d.rounded_rectangle((1046, by, 1258, by + 6), radius=3, fill=(75, 76, 108, 255))
    # gradient fill
    bar = Image.new('RGBA', (fend - 1046 + 1, 7))
    bd = ImageDraw.Draw(bar)
    for x in range(bar.width):
        t = x / max(1, bar.width - 1)
        bd.line([(x, 0), (x, 6)], fill=tuple(round(c0[k] * (1 - t) + c1[k] * t) for k in range(3)) + (255,))
    mask = Image.new('L', bar.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, bar.width - 1, 6), radius=3, fill=255)
    im.paste(bar, (1046, by), mask)

# body fat card header: current = 23% (the May tooltip 25% stays, the line keeps falling)
text_top(347, 640, '23%', font(20, 500), WHITE, anchor_right=True)

# phone headline: no "Instant, accurate"
fh = font(40, 400)
for i, t in enumerate(['Scan,', 'measure,', 'compare']):
    d.text((1435, 212 + 40 * i), t, font=fh, fill=WHITE)

im.convert('RGB').save(sys.argv[1])
