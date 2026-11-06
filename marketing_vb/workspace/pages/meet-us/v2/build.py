#!/usr/bin/env python3
"""Build /meet-us/ v2: responsive prototype with the animated "find us" map, static per-breakpoint
pages for the Figma import, and the seekable page used to render the route videos.

    python3 build.py            -> out/page-v2.html, out/figma/*.html, out/video.html

One source for every output: the copy and map geometry live here and in map_data.py.
"""
import base64
import html
import json
import math
import re
from pathlib import Path

import map_data as M

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
FONT_DIR = Path.home() / ".local/share/fonts/satoshi"
LOGO_SVG = (Path.home() / "3dlook-marketing/marketing_vb/brand-assets/video/3dlook-logo-white.svg").read_text()

BREAKPOINTS = [1920, 1440, 744, 375]
FINAL_MOBILE = (700, 336, 170, 194.3)   # camera window at the end of the route on narrow screens

# ---------------------------------------------------------------- copy (variant A and B)
COPY = {
    "topbar": "Meet 3DLOOK at CES 2027 · Booth 55630, Venetian Expo",
    "topbar_short": "CES 2027 · Booth 55630",
    "topbar_cta": "Book a meeting →",
    "A": {
        "eyebrow": "CES 2027 · Las Vegas · January 6-9",
        "h1": "Meet 3DLOOK at CES 2027, booth 55630",
        "lede": "Step up for a live body scan on a smartphone. Two photos give 80+ body measurements and "
                "body composition estimates, in under 45 seconds from the photos to structured results.",
        "cta": "Book a meeting at the booth",
        "cta2": "How to find booth 55630",
        "micro": "30 minutes at the booth with our CEO or our sales team, January 6-9.",
        "cards_h": "What can you see at booth 55630?",
        "book_h": "Book a meeting",
        "book_p": "Pick a 30-minute slot between January 6 and 9. The calendar invite carries the booth "
                  "number and the hall.",
        "embed": "[PLACEHOLDER: HubSpot Meetings embed. One team link (round robin, CEO and sales) or two host links]",
    },
    "B": {
        "eyebrow": "CES 2027 · Las Vegas",
        "h1": "Missed us at CES 2027?",
        "lede": "At booth 55630 we ran live body scans on a phone. The online demo shows the same scan: two "
                "photos, 80+ body measurements and body composition estimates, in under 45 seconds from "
                "the photos to structured results.",
        "cta": "Book an online demo",
        "cards_h": "What does the demo show?",
        "book_h": "Book a demo",
        "book_p": "Pick a 30-minute slot. The invite carries the video link.",
        "embed": "[PLACEHOLDER: HubSpot Meetings embed: the sales demo link, not the booth link]",
    },
    "cards": [
        ("A live body scan", "A guided capture on a phone, then the 80+ body measurements and body "
                             "composition estimates on the screen next to you."),
        ("Where the data goes", "Structured results reach a health, insurance, fitness or apparel platform "
                                "through our software development kit (SDK) or application programming "
                                "interface (API)."),
        ("What is new", "Wrist sizing is now part of the 3DLOOK platform, and more body areas are in "
                        "development."),
    ],
    "cards_B_first": ("A live body scan", "A guided capture on a phone, then the 80+ body measurements and "
                                          "body composition estimates."),
    "find_h": "How do you find booth 55630?",
    "find_lede": "Booth 55630 is a corner booth in the Health area of Halls A-D, on Level 2 of the Venetian "
                 "Expo. Pick where you come from and follow the route.",
    "find_note": "Drawn from the official floor plan of October 2026. Layouts can change before the show, "
                 "and the CES app shows the current plan.",
    "find_dir": "[PLACEHOLDER: link to the 3DLOOK listing in the CES exhibitor directory]",
    "replay": "Replay the route",
    "pass_h": "No CES badge yet?",
    "pass_p": "Our guests register for CES free with the code <code>[PLACEHOLDER: customer promo code]</code> "
              "at [PLACEHOLDER: CES registration link]. Register before you fly.",
    "soft": 'Not going to Las Vegas? <a href="https://3dlook.ai/contact-us/" data-mu-event="soft_online_demo">'
            'Request an online demo</a> instead.',
    "about": "3DLOOK builds smartphone body measurement technology for enterprises and has worked with 100+ "
             "clients since 2016.",
}
ENTRANCE_SUB = {"foyer": "Hall D entrance · about 230 m", "west": "Hall C entrance · about 200 m"}


# ---------------------------------------------------------------- map svg
def pts(poly):
    return " ".join(f"{x:g},{y:g}" for x, y in poly)


def rect(r, cls, rx=1.2):
    x, y, w, h = r
    return f'<rect class="{cls}" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{rx:g}"/>'


def cum_lengths(points):
    out = [0.0]
    for i in range(len(points) - 1):
        out.append(out[-1] + math.dist(points[i], points[i + 1]))
    return out


def chevrons(points, step=11.0, start=7.0):
    """positions (x, y, angle, at) every `step` units along the polyline"""
    cl = cum_lengths(points)
    total = cl[-1]
    res = []
    s = start
    while s < total - 6:
        for i in range(len(points) - 1):
            if cl[i] <= s <= cl[i + 1]:
                (x0, y0), (x1, y1) = points[i], points[i + 1]
                f = (s - cl[i]) / (cl[i + 1] - cl[i])
                ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
                res.append((x0 + (x1 - x0) * f, y0 + (y1 - y0) * f, ang, s))
                break
        s += step
    return res


def map_svg(active="foyer", view=None, idp="mu"):
    vx, vy, vw, vh = view or M.VIEW
    o = [f'<svg class="mu-map" viewBox="{vx:g} {vy:g} {vw:g} {vh:g}" preserveAspectRatio="xMidYMid slice" '
         f'role="img" aria-labelledby="{idp}-map-t {idp}-map-d" xmlns="http://www.w3.org/2000/svg">',
         f'<title id="{idp}-map-t">Route to 3DLOOK booth 55630, Venetian Expo, Level 2</title>',
         f'<desc id="{idp}-map-d">Schematic map of the Health area in Halls A-D with the walking route from the '
         f'chosen entrance to booth 55630. The numbered steps next to the map give the same route in words.</desc>',
         f'<rect class="m-bg" x="{M.VIEW[0] - 200:g}" y="{M.VIEW[1] - 200:g}" width="{M.VIEW[2] + 400:g}" height="{M.VIEW[3] + 400:g}"/>',
         f'<polygon class="m-walk" points="{pts(M.WALKWAY)}"/>',
         f'<polygon class="m-hall" points="{pts(M.HALL)}"/>']
    for d in M.DOORS.values():
        o.append(f'<polygon class="m-door" points="{pts(d)}"/>')
    o.append(f'<polygon class="m-health" points="{pts(M.HEALTH)}"/>')
    o.append(rect(M.BALLROOM, "m-ballroom", 3))
    for b in M.BOOTHS:
        o.append(rect(b, "m-booth", 1))
    for b in M.ISLAND_OTHERS:
        o.append(rect(b, "m-booth", 0.6))
    o.append(rect(M.HEALTH_HUB, "m-hub", 2))
    for k, (x, y, w, h) in M.ESCALATORS.items():
        o.append(rect((x, y, w, h), "m-esc", 1.5))
        n = 6
        for i in range(1, n):
            xx = x + w * i / n
            o.append(f'<line class="m-esc-l" x1="{xx:.1f}" y1="{y + 2:g}" x2="{xx:.1f}" y2="{y + h - 2:g}"/>')
    for text, x, y, kind in M.LABELS:
        o.append(f'<text class="m-t m-t-{kind}" x="{x:g}" y="{y:g}">{html.escape(text)}</text>')
    for text, x, y, anchor in M.ESCALATOR_LABELS:
        o.append(f'<text class="m-t m-t-small" x="{x:g}" y="{y:g}" text-anchor="{anchor}">{html.escape(text)}</text>')
    for k, e in M.ENTRANCES.items():
        dx, dy = e["door"]
        lx, ly = e["label_at"]
        o.append(f'<circle class="m-door-dot" cx="{dx:g}" cy="{dy:g}" r="2.2"/>')
        o.append(f'<text class="m-t m-t-door" x="{lx:g}" y="{ly:g}" text-anchor="{e["anchor"]}">{html.escape(e["label"])}</text>')
    # routes
    for k, r in M.ROUTES.items():
        p = r["points"]
        d = "M" + " L".join(f"{x:g},{y:g}" for x, y in p)
        cl = cum_lengths(p)
        ends = [round(cl[i], 2) for i in r["step_ends"]]
        hidden = "" if k == active else ' style="display:none"'
        o.append(f'<g class="mu-route" data-route="{k}" data-step-ends="{json.dumps(ends)}"{hidden}>')
        o.append(f'<path class="m-ghost" d="{d}"/>')
        o.append(f'<path class="mu-route-line m-line" d="{d}"/>')
        for x, y, a, at in chevrons(p):
            o.append(f'<path class="mu-chev m-chev" data-at="{at:.1f}" '
                     f'transform="translate({x:.2f} {y:.2f}) rotate({a:.0f})" d="M-1.5,-1.9 L0.9,0 L-1.5,1.9"/>')
        sx, sy = p[0]
        o.append(f'<circle class="m-start" cx="{sx:g}" cy="{sy:g}" r="3.4"/>')
        o.append('</g>')
    # our booth + callout + walker
    bx, by = M.OUR_BOOTH_CENTER
    o.append(f'<circle class="mu-booth-ring m-ring" cx="{bx:g}" cy="{by:g}" r="6"/>')
    o.append(rect(M.OUR_BOOTH, "m-our", 0.8))
    o.append(f'<g class="m-callout" transform="translate({bx:g} {by - 9:g})">'
             f'<rect x="-31" y="-15.5" width="62" height="13.5" rx="3"/>'
             f'<path d="M-3.5,-2.2 L3.5,-2.2 L0,1.8 Z"/>'
             f'<text x="0" y="-6.4" text-anchor="middle">3DLOOK · 55630</text></g>')
    fx, fy = M.ROUTES[active]["points"][-1]
    o.append(f'<g class="mu-walker" transform="translate({fx:g} {fy:g})" style="display:none">'
             f'<circle class="m-walker-halo" r="7"/><circle class="m-walker" r="3.3"/></g>')
    o.append('</svg>')
    return "\n".join(o)


# ---------------------------------------------------------------- css
def font_faces():
    faces = []
    for w, f in [(400, "Satoshi-Regular.otf"), (500, "Satoshi-Medium.otf"), (700, "Satoshi-Bold.otf"),
                 (900, "Satoshi-Black.otf")]:
        b64 = base64.b64encode((FONT_DIR / f).read_bytes()).decode()
        faces.append(f"@font-face{{font-family:'Satoshi';font-weight:{w};font-style:normal;font-display:block;"
                     f"src:url(data:font/otf;base64,{b64}) format('opentype')}}")
    return "\n".join(faces)


CSS = r"""
:root{
  --white:#fff; --blue:#143DFF;
  --blue-50:#ECEFFF; --blue-100:#D8DEFF; --blue-200:#B1BDFF; --blue-300:#8A9CFF;
  --blue-400:#4F6DFF; --blue-600:#0F2ECD; --blue-700:#0B2299; --blue-800:#08186B; --navy:#050F40;
  --g50:#F9F9F9; --g100:#F2F2F2; --g200:#E5E5E5; --g300:#D1D1D1; --g400:#A8A8A8;
  --g500:#808080; --g600:#666666; --g700:#4C4C4C; --g800:#333333; --g900:#1A1A1A; --ink:#1A1A1A;
  --font:'Satoshi','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
}
*{box-sizing:border-box}
body{margin:0;font-family:var(--font);color:var(--ink);background:var(--white);line-height:1.5;
  -webkit-font-smoothing:antialiased}
.mu-wrap{max-width:1110px;margin:0 auto}
.mu a:focus-visible,.mu button:focus-visible,.mu-topbar a:focus-visible{outline:3px solid var(--blue-200);outline-offset:2px}

/* ---------- top bar (site-wide, Dec 1 - Jan 9) */
.mu-topbar{background:var(--blue-800);color:var(--white);font-size:15px;font-weight:500;text-align:center;
  padding:12px 24px;line-height:20px}
.mu-topbar a{color:var(--white);font-weight:700;text-decoration:underline;text-underline-offset:3px;margin-left:12px}
.mu-topbar .is-short{display:none}

/* ---------- prototype chrome: the theme supplies header and footer */
.proto-header{background:var(--white);border-bottom:1px solid var(--g200)}
.proto-header .mu-wrap{display:flex;align-items:center;justify-content:space-between;height:80px}
.proto-logo{width:150px;height:22px;display:block}
.proto-logo path{fill:#0B0B0C}
.proto-nav{display:flex;gap:32px;font-size:16px;font-weight:500;color:var(--ink)}
.proto-demo{background:var(--blue);color:var(--white);font-weight:700;font-size:16px;border-radius:5px;padding:12px 22px}
.proto-burger{display:none;width:24px;height:16px;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink);position:relative}
.proto-burger:after{content:"";position:absolute;left:0;right:0;top:5px;border-top:2px solid var(--ink)}
.proto-footer{margin-top:0;background:radial-gradient(60% 120% at 50% 0%,#0B2299 0%,#08186B 45%,#050F40 100%);
  color:var(--blue-200);border-radius:30px 30px 0 0;padding:60px 0;font-size:15px}
.proto-footer .mu-wrap{display:flex;justify-content:space-between;align-items:center;gap:24px}
.proto-footer .proto-logo path{fill:var(--white)}

/* ---------- hero */
.mu-hero{position:relative;overflow:hidden;color:var(--white);background:
  radial-gradient(60% 80% at 85% 10%,rgba(20,61,255,.55),rgba(5,15,64,0) 70%),
  linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px) 0 0/40px 40px,
  linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px) 0 0/40px 40px,
  var(--navy);
  padding:96px 0 144px;border-radius:0 0 30px 30px}
.mu-hero-grid{display:grid;grid-template-columns:7fr 5fr;gap:30px;align-items:center}
.mu-eyebrow{display:inline-block;font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--blue-200);border:1px solid rgba(177,189,255,.4);border-radius:15px;padding:8px 12px;margin:0 0 24px}
.mu h1{font-size:60px;line-height:1.08;font-weight:700;margin:0 0 24px;letter-spacing:-.02em}
.mu-lede{font-size:20px;color:var(--blue-100);max-width:36em;margin:0 0 32px}
.mu-actions{display:flex;align-items:center;gap:32px;flex-wrap:wrap}
.mu-btn{display:inline-flex;align-items:center;justify-content:center;font-family:var(--font);font-weight:700;font-size:16px;
  text-decoration:none;border-radius:5px;padding:14px 26px;min-height:52px;border:0;cursor:pointer;
  transition:transform .15s ease,background .15s ease}
.mu-btn:hover{transform:translateY(-1px)}
.mu-btn-light{background:var(--white);color:var(--navy)}
.mu-btn-light:hover{background:var(--blue-50)}
.mu-textlink{color:var(--white);font-weight:500;font-size:16px;text-decoration:underline;text-underline-offset:4px}
.mu-micro{font-size:15px;color:var(--blue-200);margin:16px 0 0}
.mu-hero-visual{width:270px;height:560px;margin-left:auto;margin-right:40px;border-radius:44px;
  border:2px solid rgba(177,189,255,.45);background:linear-gradient(180deg,rgba(20,61,255,.18),rgba(5,15,64,.2));
  display:flex;align-items:center;justify-content:center;text-align:center;padding:32px;font-size:14px;color:var(--blue-200)}

/* ---------- facts */
.mu-facts{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;margin:-56px 0 0;position:relative;padding:0}
.mu-fact{background:var(--white);border:1px solid var(--g200);border-radius:20px;padding:24px;
  box-shadow:0 12px 32px rgba(5,15,64,.08)}
.mu-fact dt{font-size:13px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--g600);margin:0 0 8px}
.mu-fact dd{margin:0;font-size:17px;font-weight:500}
.mu-fact .mu-num{font-size:44px;font-weight:900;line-height:1;color:var(--navy);display:block;margin-bottom:8px}
.mu-fact a{color:var(--blue-600);font-weight:500}

/* ---------- sections */
.mu-section{padding:96px 0 0}
.mu h2{font-size:44px;line-height:1.1;font-weight:700;margin:0 0 16px;letter-spacing:-.02em}
.mu-sub{font-size:20px;color:var(--g700);margin:0;max-width:720px}
.mu-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:30px;list-style:none;margin:40px 0 0;padding:0}
.mu-card{background:var(--g50);border-radius:20px;padding:32px}
.mu-card h3{font-size:20px;line-height:1.3;margin:0 0 12px}
.mu-card p{margin:0;color:var(--g800);font-size:17px}

/* ---------- find us: map block */
.mu-find-grid{display:grid;grid-template-columns:380px 1fr;column-gap:30px;row-gap:24px;margin-top:40px;
  grid-template-areas:"tabs map" "steps map" "meta map";grid-template-rows:auto auto 1fr;align-items:start}
.mu-tabs{grid-area:tabs;display:grid;grid-template-columns:1fr;gap:12px}
.mu-tab{display:flex;flex-direction:column;align-items:flex-start;gap:2px;text-align:left;font-family:var(--font);
  background:var(--white);color:var(--ink);border:1px solid var(--g300);border-radius:15px;padding:14px 18px;
  cursor:pointer;transition:border-color .15s ease,background .15s ease}
.mu-tab:hover{border-color:var(--g500)}
.mu-tab b{font-size:17px;font-weight:700}
.mu-tab span{font-size:14px;font-weight:500;color:var(--g600)}
.mu-tab[aria-selected="true"]{background:var(--navy);border-color:var(--navy);color:var(--white)}
.mu-tab[aria-selected="true"] span{color:var(--blue-200)}
.mu-steps{grid-area:steps;list-style:none;margin:0;padding:0;display:grid;gap:14px}
.mu-steps[hidden]{display:none}
.mu-step{display:grid;grid-template-columns:28px 1fr;gap:12px;align-items:start;font-size:16px;color:var(--g800);
  transition:color .2s ease}
.mu-step i{font-style:normal;width:28px;height:28px;border-radius:9999px;display:flex;align-items:center;justify-content:center;
  font-size:14px;font-weight:700;background:var(--blue-50);color:var(--navy);transition:background .2s ease,color .2s ease}
.mu-step.is-current{color:var(--ink);font-weight:500}
.mu-step.is-current i{background:var(--blue);color:var(--white)}
.mu-step.is-done i{background:var(--navy);color:var(--white)}
.mu-step.is-upcoming{color:var(--g500)}
.mu-step.is-upcoming i{background:var(--g100);color:var(--g500)}
.mu-find-meta{grid-area:meta;display:flex;flex-direction:column;align-items:flex-start;gap:16px}
.mu-find-meta p{margin:0;font-size:15px;color:var(--g700)}
.mu-replay{display:inline-flex;align-items:center;gap:8px;font-family:var(--font);font-size:16px;font-weight:700;
  color:var(--navy);background:var(--white);border:1px solid var(--navy);border-radius:9999px;padding:10px 20px;cursor:pointer}
.mu-replay:hover{background:var(--blue-50)}
.mu-replay svg{width:16px;height:16px}
.mu-mapbox{grid-area:map;position:relative;margin:0;border-radius:20px;overflow:hidden;background:#EEF0F6;
  aspect-ratio:410/364;border:1px solid var(--g200)}
.mu-mapbox svg{display:block;width:100%;height:100%}
.mu-map-badge{position:absolute;left:16px;top:16px;background:var(--white);border-radius:9999px;padding:8px 14px;
  font-size:14px;font-weight:700;color:var(--navy);box-shadow:0 4px 16px rgba(5,15,64,.12)}
.mu-map-legend{position:absolute;left:16px;bottom:16px;display:flex;gap:16px;background:rgba(255,255,255,.92);
  border-radius:12px;padding:8px 12px;font-size:13px;font-weight:500;color:var(--g800)}
.mu-map-legend span{display:inline-flex;align-items:center;gap:6px}
.mu-map-legend i{display:inline-block;width:18px;height:4px;border-radius:2px;background:var(--blue)}
.mu-map-legend i.b{width:11px;height:11px;border-radius:2px}
.mu-find-foot{margin:20px 0 0;font-size:14px;color:var(--g600);max-width:760px}
.mu-find-foot a{color:var(--blue-600)}

/* map drawing */
.m-bg{fill:#EEF0F6}
.m-walk{fill:#FFFFFF;stroke:#D1D1D1;stroke-width:.6}
.m-hall{fill:#FFFFFF;stroke:#B9BCC8;stroke-width:.9}
.m-door{fill:#FFFFFF}
.m-health{fill:#ECEFFF;fill-opacity:.75;stroke:#8A9CFF;stroke-width:.7;stroke-dasharray:3 2}
.m-ballroom{fill:#E3E5EC}
.m-booth{fill:#DCE0EC}
.m-hub{fill:#D8DEFF;stroke:#B1BDFF;stroke-width:.6}
.m-esc{fill:#C9CDDA}
.m-esc-l{stroke:#FFFFFF;stroke-width:.6}
.m-t{font-family:var(--font);font-size:7px;font-weight:500;fill:#4C4C4C}
.m-t-area{font-size:8px;fill:#808080;text-anchor:middle}
.m-t-walk{font-size:7.5px;fill:#666666;text-anchor:middle}
.m-t-walkl{font-size:7.5px;fill:#666666}
.m-t-hub{font-size:7px;font-weight:700;fill:#0B2299;text-anchor:middle}
.m-t-zone{font-size:7px;font-weight:700;letter-spacing:1.2px;fill:#4F6DFF}
.m-t-aisle{font-size:6px;fill:#808080;text-anchor:middle}
.m-t-small{font-size:6px;fill:#666666}
.m-t-door{font-size:6.5px;font-weight:700;fill:#050F40}
.m-door-dot{fill:#050F40}
.m-ghost{fill:none;stroke:#143DFF;stroke-opacity:.28;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:.1 4}
.m-line{fill:none;stroke:#143DFF;stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round}
.m-chev{fill:none;stroke:#FFFFFF;stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round}
.m-start{fill:#FFFFFF;stroke:#050F40;stroke-width:1.6}
.m-our{fill:#143DFF}
.m-ring{fill:none;stroke:#143DFF;stroke-width:1.1;opacity:.6}
.m-callout rect,.m-callout path{fill:#050F40}
.m-callout text{font-family:var(--font);font-size:7px;font-weight:700;fill:#FFFFFF}
.m-walker{fill:#050F40;stroke:#FFFFFF;stroke-width:1.4}
.m-walker-halo{fill:#143DFF;fill-opacity:.2}
.is-anim .mu-booth-ring{transform-box:fill-box;transform-origin:center;animation:muPulse 1.6s ease-out infinite}
@keyframes muPulse{0%{transform:scale(.6);opacity:.9}100%{transform:scale(2.2);opacity:0}}

/* ---------- booking */
.mu-book{display:grid;grid-template-columns:5fr 7fr;grid-template-areas:"intro embed" "extra embed";
  column-gap:30px;row-gap:24px;align-items:start;grid-template-rows:auto 1fr}
.mu-book-intro{grid-area:intro}.mu-embed{grid-area:embed}.mu-book-extra{grid-area:extra}
.mu-book-intro p{font-size:20px;color:var(--g800);margin:0}
.mu-embed{min-height:640px;border:2px dashed var(--blue-300);border-radius:20px;background:var(--blue-50);
  display:flex;align-items:center;justify-content:center;text-align:center;padding:32px;color:var(--blue-700);font-weight:500}
.mu-pass{background:var(--white);border:1px solid var(--g200);border-left:4px solid var(--blue);border-radius:15px;padding:20px 24px}
.mu-pass h3{font-size:18px;margin:0 0 8px}
.mu-pass p{font-size:16px;margin:0}
.mu-pass code{font-family:var(--font);font-weight:700;background:var(--blue-50);padding:2px 8px;border-radius:4px}
.mu-soft{margin:24px 0 0;font-size:16px}
.mu-soft a{color:var(--blue-600);font-weight:500}
.mu-about{padding:96px 0 120px;color:var(--g600);font-size:16px;margin:0}

@media (prefers-reduced-motion:reduce){
  .mu-btn,.mu-tab,.mu-step,.mu-step i{transition:none}
  .is-anim .mu-booth-ring{animation:none}
}

/* ---------- 1920 */
@media (min-width:1600px){
  .mu-wrap{max-width:1180px}
  .mu-hero{padding:120px 0 160px}
  .mu h1{font-size:65px}
  .mu-lede{font-size:21px}
  .mu h2{font-size:50px}
  .mu-section{padding-top:120px}
  .mu-find-grid{grid-template-columns:400px 1fr;column-gap:40px}
  .mu-hero-visual{width:290px;height:600px}
}
/* ---------- small desktop */
@media (max-width:1279px){
  .mu-wrap{max-width:none;margin:0 48px}
}
/* ---------- tablet (iPad mini 744) */
@media (max-width:1023px){
  .proto-nav,.proto-demo{display:none}
  .proto-burger{display:block}
  .proto-header .mu-wrap{height:72px}
  .mu-hero{padding:80px 0 120px}
  .mu-hero-grid{grid-template-columns:1fr}
  .mu-hero-visual{display:none}
  .mu h1{font-size:48px}
  .mu-lede{font-size:19px}
  .mu h2{font-size:36px}
  .mu-sub{font-size:18px}
  .mu-section{padding-top:80px}
  .mu-facts{gap:16px;margin-top:-48px}
  .mu-fact{padding:20px}
  .mu-fact dd{font-size:16px}
  .mu-fact .mu-num{font-size:36px}
  .mu-find-grid{grid-template-columns:1fr;grid-template-areas:"tabs" "map" "steps" "meta";margin-top:32px}
  .mu-tabs{grid-template-columns:1fr 1fr}
  .mu-cards{grid-template-columns:1fr;gap:16px;margin-top:32px}
  .mu-card{padding:24px}
  .mu-book{grid-template-columns:1fr;grid-template-areas:"intro" "embed" "extra"}
  .mu-book-intro p{font-size:18px}
  .mu-embed{min-height:560px}
  .mu-about{padding:80px 0 96px}
  .proto-footer .mu-wrap{flex-direction:column;align-items:flex-start}
}
/* ---------- mobile (iPhone 13, 375) */
@media (max-width:599px){
  .mu-wrap{margin:0 30px}
  .mu-topbar{font-size:14px;padding:10px 16px}
  .mu-topbar .is-long{display:none}
  .mu-topbar .is-short{display:inline}
  .proto-header .mu-wrap{height:64px}
  .proto-logo{width:120px;height:18px}
  .mu-hero{padding:56px 0 104px;border-radius:0 0 20px 20px}
  .mu-eyebrow{font-size:12px;letter-spacing:.1em}
  .mu h1{font-size:36px}
  .mu-lede{font-size:18px;margin-bottom:24px}
  .mu-actions{flex-direction:column;align-items:stretch;gap:20px}
  .mu-btn{width:100%}
  .mu-textlink{text-align:center}
  .mu h2{font-size:30px}
  .mu-sub{font-size:17px}
  .mu-section{padding-top:60px}
  .mu-facts{grid-template-columns:1fr;gap:12px;margin-top:-56px}
  .mu-fact{padding:18px 20px}
  .mu-find-grid{margin-top:24px;row-gap:20px}
  .mu-tabs{grid-template-columns:1fr;gap:8px}
  .mu-tab{padding:12px 16px}
  .mu-mapbox{aspect-ratio:7/8;border-radius:15px}
  .mu-map-badge{left:12px;top:12px;font-size:13px;padding:6px 12px}
  .mu-map-legend{display:none}
  .mu-card{padding:24px 20px}
  .mu-card p{font-size:16px}
  .mu-book-intro p{font-size:17px}
  .mu-embed{min-height:520px;padding:24px}
  .mu-about{padding:60px 0 80px}
  .proto-footer{border-radius:20px 20px 0 0;padding:48px 0}
}
"""


# ---------------------------------------------------------------- js (animation)
JS = r"""
(function(){
  var root=document.querySelector('[data-mu-find]'); if(!root) return;
  var svg=root.querySelector('svg.mu-map'), box=root.querySelector('.mu-mapbox');
  var VIEW=__VIEW__, CAM=__CAM__, FINAL=__FINAL__;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  var D={intro:.7,travel:7.5,arrive:1.4};
  var routes={};
  [].forEach.call(svg.querySelectorAll('.mu-route'),function(g){
    var p=g.querySelector('.mu-route-line'); var L=p.getTotalLength();
    routes[g.getAttribute('data-route')]={g:g,p:p,L:L,ends:JSON.parse(g.getAttribute('data-step-ends')),
      chev:[].map.call(g.querySelectorAll('.mu-chev'),function(c){return {el:c,at:+c.getAttribute('data-at')}})};
    p.style.strokeDasharray=L+' '+L;
  });
  var walker=svg.querySelector('.mu-walker');
  var tabs=[].slice.call(root.querySelectorAll('.mu-tab'));
  var cur=(tabs.filter(function(t){return t.getAttribute('aria-selected')==='true'})[0]||tabs[0]).getAttribute('data-route');
  var raf=0,start=0,played=false;
  function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
  function ease(x){return x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2}
  function mode(){return box.clientWidth<600?'follow':'fixed'}
  function camWindow(cx,cy,w){var h=w*box.clientHeight/box.clientWidth;
    return [clamp(cx-w/2,CAM[0],CAM[0]+CAM[2]-w),clamp(cy-h/2,CAM[1],CAM[1]+CAM[3]-h),w,h]}
  function finalWindow(){var w=FINAL[2],h=w*box.clientHeight/box.clientWidth;return [FINAL[0],FINAL[1]+(FINAL[3]-h)/2,w,h]}
  function lerpV(a,b,k){return a.map(function(v,i){return v+(b[i]-v)*k})}
  function setView(v){svg.setAttribute('viewBox',v.map(function(n){return n.toFixed(2)}).join(' '))}
  function steps(){return [].slice.call(root.querySelectorAll('.mu-steps[data-route="'+cur+'"] .mu-step'))}
  function render(t){
    var r=routes[cur], k=clamp((t-D.intro)/D.travel,0,1), len=r.L*k;
    r.p.style.strokeDashoffset=(r.L-len);
    r.chev.forEach(function(c){c.el.style.opacity=c.at<=len?1:0});
    var pt=r.p.getPointAtLength(len);
    walker.style.display=''; walker.setAttribute('transform','translate('+pt.x+' '+pt.y+')');
    var idx=0; while(idx<r.ends.length-1&&len>r.ends[idx]+.01) idx++;
    var arrived=t>=D.intro+D.travel;
    steps().forEach(function(li,i){li.className='mu-step '+(arrived||i<idx?'is-done':i===idx?'is-current':'is-upcoming')});
    if(mode()==='follow'){
      var w=150, follow=camWindow(pt.x,pt.y,w);
      var a=clamp((t-D.intro-D.travel)/D.arrive,0,1);
      setView(a>0?lerpV(follow,finalWindow(),ease(a)):follow);
    } else setView(VIEW);
    return t<D.intro+D.travel+D.arrive;
  }
  function finalState(){
    var r=routes[cur]; r.p.style.strokeDashoffset=0; r.chev.forEach(function(c){c.el.style.opacity=1});
    walker.style.display='none';
    steps().forEach(function(li){li.className='mu-step'});
    setView(mode()==='follow'?finalWindow():VIEW);
  }
  function play(){
    cancelAnimationFrame(raf); played=true;
    if(reduce){finalState();return}
    root.classList.add('is-anim'); start=performance.now();
    (function tick(now){ if(render((now-start)/1000)) raf=requestAnimationFrame(tick); })(start);
  }
  function select(key,focus){
    cur=key;
    tabs.forEach(function(t){var on=t.getAttribute('data-route')===key;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;if(on&&focus)t.focus()});
    [].forEach.call(root.querySelectorAll('.mu-steps'),function(o){o.hidden=o.getAttribute('data-route')!==key});
    Object.keys(routes).forEach(function(k){routes[k].g.style.display=k===key?'':'none'});
    play();
    if(window.dataLayer) dataLayer.push({event:'map_route_select',route:key});
  }
  tabs.forEach(function(t,i){
    t.addEventListener('click',function(){select(t.getAttribute('data-route'))});
    t.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'||e.key==='ArrowDown'?1:e.key==='ArrowLeft'||e.key==='ArrowUp'?-1:0;
      if(d){e.preventDefault();select(tabs[(i+d+tabs.length)%tabs.length].getAttribute('data-route'),true)}});
  });
  root.querySelector('.mu-replay').addEventListener('click',function(){play();if(window.dataLayer)dataLayer.push({event:'map_replay',route:cur})});
  window.addEventListener('resize',function(){if(!raf||reduce)finalState()});
  // seek API for video rendering and design review: ?t=4.2 freezes the frame
  window.__muSeek=function(t,key){if(key&&key!==cur){cur=key;Object.keys(routes).forEach(function(k){routes[k].g.style.display=k===key?'':'none'})}
    played=true;cancelAnimationFrame(raf);root.classList.add('is-anim');render(t)};
  if(reduce){finalState();return}
  // reset to the start until the block scrolls into view
  render(0); walker.style.display='none';
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!played){play();io.disconnect()}})},{threshold:.35});
    io.observe(box);
  } else play();
})();
"""


# ---------------------------------------------------------------- html parts
def topbar():
    return (f'<div class="mu-topbar"><span class="is-long">{COPY["topbar"]}</span>'
            f'<span class="is-short">{COPY["topbar_short"]}</span>'
            f'<a href="/meet-us/#book">{COPY["topbar_cta"]}</a></div>')


def logo():
    return re.sub(r'<svg[^>]*>', '<svg class="proto-logo" viewBox="0 0 248 36" xmlns="http://www.w3.org/2000/svg" aria-label="3DLOOK">', LOGO_SVG, 1)


def header():
    nav = "".join(f"<span>{n}</span>" for n in ["Products", "Industries", "Pricing", "Resources", "Company"])
    return (f'<header class="proto-header" data-prototype-chrome><div class="mu-wrap">{logo()}'
            f'<nav class="proto-nav">{nav}</nav><span class="proto-demo">Book a demo</span>'
            f'<span class="proto-burger" aria-hidden="true"></span></div></header>')


def footer():
    return (f'<footer class="proto-footer" data-prototype-chrome><div class="mu-wrap">{logo()}'
            f'<span>Theme footer (existing, not part of this page)</span></div></footer>')


def hero(v):
    c = COPY[v]
    if v == "A":
        actions = (f'<a class="mu-btn mu-btn-light" href="#book" data-mu-event="cta_book_hero">{c["cta"]}</a>'
                   f'<a class="mu-textlink" href="#find" data-mu-event="cta_find_hero">{c["cta2"]} ↓</a>')
        micro = f'<p class="mu-micro">{c["micro"]}</p>'
    else:
        actions = f'<a class="mu-btn mu-btn-light" href="#book" data-mu-event="cta_book_hero">{c["cta"]}</a>'
        micro = ""
    return (f'<section class="mu-hero"><div class="mu-wrap mu-hero-grid"><div>'
            f'<p class="mu-eyebrow">{c["eyebrow"]}</p><h1>{c["h1"]}</h1><p class="mu-lede">{c["lede"]}</p>'
            f'<div class="mu-actions">{actions}</div>{micro}</div>'
            f'<div class="mu-hero-visual" role="img" aria-label="Guided body scan on a phone">'
            f'[PLACEHOLDER: hero visual, guided-capture phone UI, still from the booth video (Kristina, B7)]</div>'
            f'</div></section>')


def facts():
    return ('<div class="mu-wrap"><dl class="mu-facts">'
            '<div class="mu-fact"><dt>When</dt><dd>January 6-9, 2027<br><a href="https://www.ces.tech/">Exhibit hours on ces.tech</a></dd></div>'
            '<div class="mu-fact"><dt>Where</dt><dd>Venetian Expo, Level 2, Halls A-D, Health area<br><a href="#find">See the route</a></dd></div>'
            '<div class="mu-fact"><dt>Booth</dt><dd><span class="mu-num">55630</span>A corner booth</dd></div>'
            '</dl></div>')


REPLAY_ICON = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5 8a5.5 5.5 0 1 1-1.6-3.9" fill="none" '
               'stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M12.6 1.6v3.1H9.5" fill="none" '
               'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def find_block(active="foyer", view=None, step_state=None):
    """step_state: None (plain list) or dict route -> index of current step (for storyboard frames)"""
    tabs = []
    for k, r in M.ROUTES.items():
        on = "true" if k == active else "false"
        tabs.append(f'<button class="mu-tab" role="tab" type="button" id="mu-tab-{k}" aria-controls="mu-steps-{k}" '
                    f'aria-selected="{on}" tabindex="{0 if k == active else -1}" data-route="{k}">'
                    f'<b>{r["tab"]}</b><span>{ENTRANCE_SUB[k]}</span></button>')
    lists = []
    for k, r in M.ROUTES.items():
        hidden = "" if k == active else " hidden"
        items = []
        for i, s in enumerate(r["steps"]):
            cls = "mu-step"
            if step_state and k in step_state:
                cur = step_state[k]
                cls += " is-done" if i < cur else " is-current" if i == cur else " is-upcoming"
            items.append(f'<li class="{cls}"><i>{i + 1}</i><span>{html.escape(s)}</span></li>')
        lists.append(f'<ol class="mu-steps" id="mu-steps-{k}" role="tabpanel" aria-labelledby="mu-tab-{k}" '
                     f'data-route="{k}"{hidden}>{"".join(items)}</ol>')
    meta = {k: r["meta"] for k, r in M.ROUTES.items()}
    return (f'<section class="mu-section mu-find" id="find" aria-labelledby="mu-find-h" data-mu-find>'
            f'<div class="mu-wrap"><h2 id="mu-find-h">{COPY["find_h"]}</h2><p class="mu-sub">{COPY["find_lede"]}</p>'
            f'<div class="mu-find-grid">'
            f'<div class="mu-tabs" role="tablist" aria-label="Where do you come from?">{"".join(tabs)}</div>'
            f'{"".join(lists)}'
            f'<div class="mu-find-meta"><p class="mu-find-dist" data-route-meta=\'{html.escape(json.dumps(meta))}\'>{meta[active]}</p>'
            f'<button class="mu-replay" type="button">{REPLAY_ICON}{COPY["replay"]}</button></div>'
            f'<figure class="mu-mapbox">{map_svg(active, view)}'
            f'<figcaption class="mu-map-badge">Venetian Expo · Level 2</figcaption>'
            f'<div class="mu-map-legend" aria-hidden="true"><span><i></i>Your route</span><span><i class="b"></i>Booth 55630</span></div>'
            f'</figure></div>'
            f'<p class="mu-find-foot">{COPY["find_note"]} {COPY["find_dir"]}</p>'
            f'</div></section>')


def cards(v):
    items = list(COPY["cards"])
    if v == "B":
        items[0] = COPY["cards_B_first"]
    lis = "".join(f'<li class="mu-card"><h3>{h}</h3><p>{p}</p></li>' for h, p in items)
    h = COPY[v]["cards_h"]
    return (f'<section class="mu-section" aria-labelledby="mu-see"><div class="mu-wrap">'
            f'<h2 id="mu-see">{h}</h2><ul class="mu-cards">{lis}</ul></div></section>')


def book(v):
    c = COPY[v]
    extra = ""
    if v == "A":
        extra = (f'<div class="mu-pass"><h3>{COPY["pass_h"]}</h3><p>{COPY["pass_p"]}</p></div>'
                 f'<p class="mu-soft">{COPY["soft"]}</p>')
    return (f'<section class="mu-section" id="book" aria-labelledby="mu-book"><div class="mu-wrap"><div class="mu-book">'
            f'<div class="mu-book-intro"><h2 id="mu-book">{c["book_h"]}</h2><p>{c["book_p"]}</p></div>'
            f'<div class="mu-embed">{c["embed"]}</div><div class="mu-book-extra">{extra}</div>'
            f'</div></div></section>')


def page(v="A", *, js=True, fonts="embed", view=None, step_state=None, chrome=True, title_suffix=""):
    body = []
    if chrome and v == "A":
        body.append(topbar())
    if chrome:
        body.append(header())
    body.append('<main class="mu">')
    body.append(hero(v))
    if v == "A":
        body.append(facts())
        body.append(find_block("foyer", view, step_state))
    body.append(cards(v))
    body.append(book(v))
    body.append(f'<div class="mu-wrap"><p class="mu-about">{COPY["about"]}</p></div>')
    body.append('</main>')
    if chrome:
        body.append(footer())
    font_css = font_faces() if fonts == "embed" else ""
    font_link = ('<link rel="preconnect" href="https://api.fontshare.com">'
                 '<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&display=swap">'
                 if fonts == "link" else "")
    script = ""
    if js and v == "A":
        script = "<script>" + JS.replace("__VIEW__", json.dumps(M.VIEW)).replace("__FINAL__", json.dumps(FINAL_MOBILE)).replace("__CAM__", json.dumps(M.CAM_BOUNDS)) + "</script>"
    meta_js = """<script>(function(){var p=document.querySelector('.mu-find-dist');if(!p)return;var m=JSON.parse(p.getAttribute('data-route-meta'));
document.querySelectorAll('.mu-tab').forEach(function(t){t.addEventListener('click',function(){p.textContent=m[t.getAttribute('data-route')]})})})();</script>""" if js and v == "A" else ""
    title = "Meet 3DLOOK at CES 2027 · Booth 55630" if v == "A" else "Missed us at CES 2027? · 3DLOOK"
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}{title_suffix}</title><meta name="robots" content="noindex, follow">'
            f'{font_link}<style>{font_css}\n{CSS}</style></head><body>{"".join(body)}{script}{meta_js}</body></html>')


# ---------------------------------------------------------------- static export for Figma
MEDIA_RE = re.compile(r"@media \((min|max)-width:(\d+)px\)\{")


def unwrap_media(css, width):
    """Keep base rules, then append the bodies of width media blocks that match `width`.
    Drops prefers-reduced-motion. Works because the blocks above hold flat rules only."""
    out, i = [], 0
    while True:
        m = re.search(r"@media [^{]+\{", css[i:])
        if not m:
            out.append(css[i:])
            break
        s = i + m.start()
        out.append(css[i:s])
        depth, j = 0, i + m.end() - 1
        while True:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        head = css[s:i + m.end()]
        inner = css[i + m.end():j]
        mm = MEDIA_RE.match(head)
        if mm:
            kind, px = mm.group(1), int(mm.group(2))
            if (kind == "min" and width >= px) or (kind == "max" and width <= px):
                out.append(inner)
        i = j + 1
    return "".join(out)


def static_page(v, width, step_state=None):
    view = None
    if width < 600 and v == "A":
        h = FINAL_MOBILE[2] * 8 / 7
        view = (FINAL_MOBILE[0], FINAL_MOBILE[1] + (FINAL_MOBILE[3] - h) / 2, FINAL_MOBILE[2], h)
    doc = page(v, js=False, fonts="embed", view=view, step_state=step_state)
    css_block = re.search(r"<style>(.*?)</style>", doc, re.S).group(1)
    # font faces have no media queries, safe to unwrap whole block
    doc = doc.replace(css_block, unwrap_media(css_block, width) + f"\nhtml,body{{width:{width}px}}")
    # aspect-ratio is not reliable in the importer: give the map box a fixed height
    return doc


def video_page(route):
    """1080 x 1080 page that renders one frame per __muSeek call (see render_video.py)"""
    svg = map_svg(route, M.VIEW, idp="v")
    steps = json.dumps(M.ROUTES[route]["steps"])
    ends = json.dumps([round(cum_lengths(M.ROUTES[route]["points"])[i], 2) for i in M.ROUTES[route]["step_ends"]])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_faces()}
{CSS}
html,body{{margin:0;width:1080px;height:1080px;overflow:hidden;background:#EEF0F6}}
.v-map{{position:absolute;inset:0}} .v-map svg{{width:1080px;height:1080px;display:block}}
.v-top{{position:absolute;left:48px;right:48px;top:44px;display:flex;justify-content:space-between;align-items:center}}
.v-brand{{display:flex;align-items:center;gap:16px;background:#050F40;color:#fff;border-radius:9999px;padding:14px 26px 14px 22px;font:700 26px var(--font)}}
.v-brand svg{{width:150px;height:22px}} .v-brand svg path{{fill:#fff}}
.v-lvl{{background:#fff;color:#050F40;border-radius:9999px;padding:14px 24px;font:700 24px var(--font);box-shadow:0 6px 24px rgba(5,15,64,.15)}}
.v-cap{{position:absolute;left:48px;right:48px;bottom:48px;background:#fff;border-radius:24px;padding:26px 30px;display:grid;
  grid-template-columns:56px 1fr;gap:22px;align-items:center;box-shadow:0 10px 40px rgba(5,15,64,.18);font:500 31px/1.3 var(--font);color:#1A1A1A}}
.v-cap i{{font-style:normal;width:56px;height:56px;border-radius:9999px;background:#143DFF;color:#fff;display:flex;align-items:center;justify-content:center;font:700 26px var(--font)}}
.v-end{{position:absolute;inset:0;background:radial-gradient(60% 80% at 80% 10%,rgba(20,61,255,.55),rgba(5,15,64,0) 70%),#050F40;color:#fff;
  display:flex;flex-direction:column;justify-content:center;padding:0 90px;opacity:0}}
.v-end small{{font:700 24px var(--font);letter-spacing:.14em;text-transform:uppercase;color:#B1BDFF}}
.v-end h1{{font:700 84px/1.05 var(--font);margin:22px 0 26px;letter-spacing:-.02em}}
.v-end p{{font:500 32px/1.35 var(--font);color:#D8DEFF;margin:0}}
.m-t{{font-size:7.5px}} .m-callout text{{font-size:7px}}
</style></head><body>
<div class="v-map" data-mu-find><div class="mu-mapbox" style="border:0;border-radius:0;aspect-ratio:auto;width:1080px;height:1080px">{svg}</div></div>
<div class="v-top"><div class="v-brand">{logo().replace('class="proto-logo"', '')}<span>· 55630</span></div><div class="v-lvl">Venetian Expo · Level 2</div></div>
<div class="v-cap"><i>1</i><span></span></div>
<div class="v-end"><small>CES 2027 · Las Vegas · January 6-9</small><h1>See you at<br>booth 55630</h1><p>Venetian Expo, Level 2, Halls A-D, Health area. A corner booth.</p></div>
<script>
var VIEW={json.dumps(M.VIEW)}, STEPS={steps}, ENDS={ends};
var svg=document.querySelector('svg.mu-map'), r=svg.querySelector('.mu-route[data-route="{route}"]'), p=r.querySelector('.mu-route-line');
var L=p.getTotalLength(); p.style.strokeDasharray=L+' '+L;
var chev=[].map.call(r.querySelectorAll('.mu-chev'),function(c){{return {{el:c,at:+c.getAttribute('data-at')}}}});
var walker=svg.querySelector('.mu-walker'), ring=svg.querySelector('.mu-booth-ring');
var cap=document.querySelector('.v-cap'), capN=cap.querySelector('i'), capT=cap.querySelector('span'), end=document.querySelector('.v-end');
var T={{over:1.2,zoomIn:1.0,travel:8.5,arrive:1.5,zoomOut:1.4,endIn:.6}};
function clamp(v,a,b){{return Math.max(a,Math.min(b,v))}}
function ease(x){{return x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2}}
function lerp(a,b,k){{return a.map(function(v,i){{return v+(b[i]-v)*k}})}}
var OVER=[VIEW[0]-10,VIEW[1]-30,VIEW[2]+20,VIEW[2]+20];
function win(x,y,w){{return [clamp(x-w/2,VIEW[0],VIEW[0]+VIEW[2]-w),clamp(y-w/2,VIEW[1]-10,VIEW[1]+VIEW[3]-w+40),w,w]}}
function setV(v){{svg.setAttribute('viewBox',v.map(function(n){{return n.toFixed(2)}}).join(' '))}}
window.__frame=function(t){{
  var t1=T.over,t2=t1+T.zoomIn,t3=t2+T.travel,t4=t3+T.arrive,t5=t4+T.zoomOut;
  var k=clamp((t-t2)/T.travel,0,1), len=L*k;
  p.style.strokeDashoffset=L-len; chev.forEach(function(c){{c.el.style.opacity=c.at<=len?1:0}});
  var pt=p.getPointAtLength(len); walker.style.display=t>=t1?'':'none'; walker.setAttribute('transform','translate('+pt.x+' '+pt.y+')');
  var W=200, fw=win(pt.x,pt.y,W), st=p.getPointAtLength(0);
  var v;
  if(t<t1) v=OVER;
  else if(t<t2) v=lerp(OVER,win(st.x,st.y,W),ease((t-t1)/T.zoomIn));
  else if(t<t3) v=fw;
  else if(t<t4) v=lerp(fw,win(pt.x,pt.y,150),ease((t-t3)/T.arrive));
  else v=lerp(win(pt.x,pt.y,150),OVER,ease(clamp((t-t4)/T.zoomOut,0,1)));
  setV(v);
  var idx=0; while(idx<ENDS.length-1&&len>ENDS[idx]+.01) idx++;
  capN.textContent=idx+1; capT.textContent=STEPS[idx];
  cap.style.opacity=(t>=t1&&t<t5)?1:0;
  var pulse=t>=t3?((t-t3)%1.6)/1.6:0; ring.setAttribute('r',6+pulse*9); ring.style.opacity=t>=t3?(1-pulse)*.9:.6;
  end.style.opacity=clamp((t-t5-.6)/T.endIn,0,1);
}};
window.__duration=1.2+1.0+8.5+1.5+1.4+0.6+2.2;
__frame(0);
</script></body></html>"""


def artifact_page():
    """same page for the claude.ai artifact preview: the host adds doctype/head/body"""
    doc = page("A")
    head_style = re.search(r"<style>.*?</style>", doc, re.S).group(0)
    body = re.search(r"<body>(.*)</body>", doc, re.S).group(1)
    return f"<title>CES 2027 Meet-us Page</title>\n{head_style}\n{body}"


def main():
    OUT.mkdir(exist_ok=True)
    (HERE / "page-v2.html").write_text(page("A", fonts="link"))
    (HERE / "page-v2-variant-b.html").write_text(page("B", fonts="link"))
    (OUT / "artifact-preview.html").write_text(artifact_page())
    (OUT / "figma").mkdir(exist_ok=True)
    (OUT / "page-v2.html").write_text(page("A"))
    (OUT / "page-v2-variant-b.html").write_text(page("B"))
    for v in ["A", "B"]:
        for w in BREAKPOINTS:
            (OUT / "figma" / f"{v}-{w}.html").write_text(static_page(v, w))
    for k in M.ROUTES:
        (OUT / f"video-{k}.html").write_text(video_page(k))
    print("ok", sorted(p.name for p in OUT.rglob("*.html")))


if __name__ == "__main__":
    main()
