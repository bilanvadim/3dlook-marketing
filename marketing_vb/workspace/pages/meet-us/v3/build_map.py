#!/usr/bin/env python3
"""Find-us map v3b: middle zoom, Kristina's visual language, 3DLOOK logo on the booth.

Vadim, 2026-11-13, after the full-floor v3a (build_full.py): "a bit closer, something between the old
window and the whole floor; colour it like Kristina's so it is more interesting; add the 3DLOOK logo".

Geometry comes from build_full.py (booth blocks from the 11/3 Freeman plan, hand-traced hall, walkways,
routes). Kristina's look, from her prototype (Figma «Website», frame 5170:5929): lavender hall, white
booths with a blue outline, solid blue Health Hub, graph-paper walkways, dashed blue route, blue step
dots, white pills with soft shadows, a legend pill at the bottom.

  python3 build_map.py            -> out/find-{foyer,west}.html (seekable, window.__frame(t))
  ./render.sh                     -> MP4, GIF, poster PNG per route
"""
import html
import math
import re
from pathlib import Path

import build_full as F
from build_full import M

HERE = Path(__file__).resolve().parent
OUT = HERE / "out"
LOGOS = HERE.parents[3] / "brand-assets" / "logos"

VIEW = (380, 222, 632, 502)          # Health area, ballroom, foyer, west concourse, east of Smart Home
W, H = 1600, 1272

ZONES = [("HEALTH", 505, 474, True), ("SMART HOME", 449, 336.5, False), ("LIFESTYLE", 742, 330.5, False)]
UPPER_LABELS = [  # text, x, y, anchor, rotate, class
    ("VENETIAN BALLROOM", 856, 584, "middle", 0, "ball"),
    ("VENETIAN FOYER", 790, 678.5, "middle", 0, "walk"),
    ("WEST CONCOURSE", 432, 598, "middle", 21.5, "walk"),
    ("MAIN HEALTH AISLE", 862, 456.2, "middle", 0, "aisle"),
    ("ESCALATORS TO LEVEL 1", 664, 669.5, "end", 0, "walk"),
]
DOORS = [("Hall D entrance", 721, 497.5, "start"), ("Hall C entrance", 571, 620, "end")]
START = {"foyer": ("You are here", "ESCALATORS", 839, 699, "end"),
         "west": ("You are here", "WEST CONCOURSE", 558, 660, "end")}


def svg_inner(path):
    s = path.read_text()
    vb = re.search(r'viewBox="([\d. ]+)"', s).group(1).split()
    body = re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", s, flags=re.S)
    return body, float(vb[2]), float(vb[3])


SYMBOL, SYM_W, SYM_H = svg_inner(LOGOS / "3dlook-symbol-white.svg")
WORDMARK, WM_W, WM_H = svg_inner(LOGOS / "3dlook-logo-black.svg")
WORDMARK = re.sub(r'fill="#[0-9A-Fa-f]{3,6}"', 'fill="#050F40"', WORDMARK)

CSS = """
html,body{margin:0;background:#F6F7FB}
svg{display:block}
.bg{fill:url(#grid-bg)}
.walk{fill:url(#grid-walk);stroke:#D6DAE6;stroke-width:.8;stroke-linejoin:round}
.hall{fill:#EDF0FF;stroke:#B9C3F5;stroke-width:1;stroke-linejoin:round}
.door{fill:#EDF0FF}
.health{fill:#DDE4FF;stroke:#8A9CFF;stroke-width:.8;stroke-dasharray:3.5 2.5}
.ballroom{fill:#EEEFF4;stroke:#D3D6E0;stroke-width:.9}
.booth{fill:#FFFFFF;stroke:#AFBDF6;stroke-width:.65}
.hub{fill:#143DFF}
.island{fill:#FFFFFF;stroke:#AFBDF6;stroke-width:.65}
.esc{fill:#FFFFFF;stroke:#B7BCCB;stroke-width:.7}.esc-l{stroke:#C9CDDA;stroke-width:.6}
.t{font-family:'Satoshi',sans-serif}
.t-zone{font-size:8.5px;font-weight:700;letter-spacing:1.8px;fill:#9AA3C4;paint-order:stroke;stroke:#EDF0FF;stroke-width:3.2px;stroke-linejoin:round}
.t-zone.on{fill:#143DFF;font-size:9.5px;stroke:#DDE4FF}
.t-ball{font-size:8px;font-weight:700;letter-spacing:1.6px;fill:#4F5B93;text-anchor:middle}
.t-walk{font-size:6.2px;font-weight:500;letter-spacing:1px;fill:#7A8099;paint-order:stroke;stroke:#FAFAFC;stroke-width:2.4px;stroke-linejoin:round}
.t-aisle{font-size:5.6px;font-weight:500;letter-spacing:.9px;fill:#7A8099;paint-order:stroke;stroke:#EDF0FF;stroke-width:2.4px;stroke-linejoin:round}
.t-hub{font-size:7.5px;font-weight:700;fill:#FFFFFF;text-anchor:middle}
.t-door{font-size:7.4px;font-weight:700;fill:#050F40;paint-order:stroke;stroke:#EDF0FF;stroke-width:2.6px;stroke-linejoin:round}
.door-mark{fill:#FFFFFF;stroke:#050F40;stroke-width:.9}
.ghost{fill:none;stroke:#143DFF;stroke-opacity:.28;stroke-width:2.4;stroke-dasharray:5 3.6;stroke-linecap:round;stroke-linejoin:round}
.line{fill:none;stroke:#143DFF;stroke-width:2.8;stroke-dasharray:5 3.6;stroke-linecap:round;stroke-linejoin:round}
.reveal{fill:none;stroke:#fff;stroke-width:12;stroke-linecap:round;stroke-linejoin:round}
.step circle{fill:#143DFF;stroke:#FFFFFF;stroke-width:1.6}
.step text{font-family:'Satoshi',sans-serif;font-weight:700;font-size:8px;fill:#FFFFFF;text-anchor:middle}
.walker{fill:#143DFF;stroke:#FFFFFF;stroke-width:1.6}.walker-halo{fill:#143DFF;fill-opacity:.16}
.you .lbl{font-family:'Satoshi',sans-serif;font-weight:700;font-size:7px;fill:#050F40;paint-order:stroke;stroke:#FAFAFC;stroke-width:2.4px}
.you .sub{font-family:'Satoshi',sans-serif;font-weight:500;font-size:5.4px;letter-spacing:.8px;fill:#7A8099}
.ring{fill:none;stroke:#143DFF;stroke-width:1.2}
.pin-bg{fill:#143DFF}.pin-ring{fill:none;stroke:#FFFFFF;stroke-width:1.1;stroke-opacity:.85}
.pill{fill:#FFFFFF}
.pill-t{font-family:'Satoshi',sans-serif;font-weight:700;font-size:8.2px;fill:#050F40}
.pill-s{font-family:'Satoshi',sans-serif;font-weight:500;font-size:8.2px;fill:#5A6180}
.chip-t{font-family:'Satoshi',sans-serif;font-weight:700;font-size:7.6px;fill:#050F40}
.leg-t{font-family:'Satoshi',sans-serif;font-weight:500;font-size:7px;fill:#3A4060}
"""

DEFS = """<defs>
<pattern id="grid-bg" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#F6F7FB"/>
<path d="M8 0H0V8" fill="none" stroke="#E7E9F1" stroke-width=".5"/></pattern>
<pattern id="grid-walk" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#FAFAFC"/>
<path d="M6 0H0V6" fill="none" stroke="#E6E8EF" stroke-width=".45"/></pattern>
<filter id="sh" x="-40%" y="-60%" width="180%" height="220%"><feDropShadow dx="0" dy="1.6" stdDeviation="2.2" flood-color="#0B1A66" flood-opacity=".16"/></filter>
<filter id="sh-blue" x="-60%" y="-60%" width="220%" height="220%"><feDropShadow dx="0" dy="1.4" stdDeviation="2" flood-color="#143DFF" flood-opacity=".35"/></filter>
</defs>"""


def pts(poly):
    return " ".join(f"{x:g},{y:g}" for x, y in poly)


def base(idp):
    vx, vy, vw, vh = VIEW
    o = [f'<svg viewBox="{vx} {vy} {vw} {vh}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-labelledby="{idp}-t {idp}-d" preserveAspectRatio="xMidYMid meet">',
         f'<title id="{idp}-t">Route to the 3DLOOK booth 55630, Venetian Expo, Level 2</title>',
         f'<desc id="{idp}-d">Map of the Health area of Halls A-D on Level 2 of the Venetian Expo with the walking '
         f'route to booth 55630. The numbered steps next to the map give the route in words.</desc>',
         DEFS,
         f'<rect class="bg" x="{vx - 40}" y="{vy - 40}" width="{vw + 80}" height="{vh + 80}"/>',
         f'<polygon class="walk" points="{pts(F.WALKWAY)}"/>',
         f'<polygon class="hall" points="{pts(F.HALL)}"/>']
    for d in M.DOORS.values():
        o.append(f'<polygon class="door" points="{pts(d)}"/>')
    o.append(f'<polygon class="health" points="{pts(M.HEALTH)}"/>')
    x, y, w, h = F.BALLROOM
    o.append(f'<rect class="ballroom" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/>')
    o.append('<g class="booth">' + "".join(
        f'<rect x="{bx:g}" y="{by:g}" width="{bw:g}" height="{bh:g}" rx=".6"/>' for bx, by, bw, bh in F.booths()) + '</g>')
    for bx, by, bw, bh in M.ISLAND_OTHERS:
        o.append(f'<rect class="island" x="{bx}" y="{by}" width="{bw}" height="{bh}" rx=".4"/>')
    x, y, w, h = F.HUB
    o.append(f'<rect class="hub" x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5"/>'
             f'<text class="t t-hub" x="{x + w / 2}" y="{y + h / 2 + 2.6}">Health Hub</text>')
    for (x, y, w, h) in M.ESCALATORS.values():
        o.append(f'<rect class="esc" x="{x}" y="{y}" width="{w}" height="{h}" rx="1.4"/>')
        for i in range(1, 6):
            xx = x + w * i / 6
            o.append(f'<line class="esc-l" x1="{xx:.1f}" y1="{y + 2.5}" x2="{xx:.1f}" y2="{y + h - 2.5}"/>')
    for text, x, y, on in ZONES:
        o.append(f'<text class="t t-zone{" on" if on else ""}" x="{x}" y="{y}">{text}</text>')
    for text, x, y, anchor, rot, cls in UPPER_LABELS:
        tr = f' transform="rotate({rot} {x} {y})"' if rot else ""
        o.append(f'<text class="t t-{cls}" x="{x}" y="{y}" text-anchor="{anchor}"{tr}>{text}</text>')
    for text, x, y, anchor in DOORS:
        o.append(f'<text class="t t-door" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>')
    # top-left chip
    o.append(f'<g filter="url(#sh)" transform="translate({vx + 12} {vy + 11})"><rect class="pill" width="150" height="20" rx="10"/>'
             f'<circle cx="11" cy="10" r="3" fill="#143DFF"/><text class="chip-t" x="19" y="12.8">Venetian Expo · Level 2 · Halls A-D</text></g>')
    return o


def legend():
    vx, vy, vw, vh = VIEW
    return (f'<g filter="url(#sh)" transform="translate({vx + 12} {vy + vh - 31})"><rect class="pill" width="196" height="20" rx="10"/>'
            f'<path d="M10 10H26" stroke="#143DFF" stroke-width="2" stroke-dasharray="4 2.6" stroke-linecap="round"/>'
            f'<text class="leg-t" x="31" y="12.6">Your route</text>'
            f'<g class="step" transform="translate(80 10)"><circle r="5.6"/><text y="2.8" style="font-size:6.6px">1</text></g>'
            f'<text class="leg-t" x="89" y="12.6">Step</text>'
            f'<g transform="translate(120 10)"><circle r="5.6" fill="#143DFF"/>'
            f'<g transform="translate(-3.4 -3) scale({6.8 / SYM_W:.4f})">{SYMBOL}</g></g>'
            f'<text class="leg-t" x="129" y="12.6">3DLOOK booth</text></g>')


def route(key):
    p = F.ROUTE_POINTS[key]
    r = M.ROUTES[key]
    d = "M" + " L".join(f"{x:g},{y:g}" for x, y in p)
    cl = F.cum(p)
    starts = [0] + r["step_ends"][:-1]
    vx, vy, vw, vh = VIEW
    o = [f'<mask id="m-{key}" maskUnits="userSpaceOnUse" x="{vx - 50}" y="{vy - 50}" width="{vw + 100}" height="{vh + 100}">'
         f'<path class="reveal" d="{d}"/></mask>',
         f'<g class="route" data-route="{key}">',
         f'<path class="ghost" d="{d}"/>',
         f'<path class="line" d="{d}" mask="url(#m-{key})"/>']
    lbl, sub, lx, ly, anchor = START[key]
    sx, sy = p[0]
    o.append(f'<g class="you"><text class="lbl" x="{lx}" y="{ly}" text-anchor="{anchor}">{lbl}</text>'
             f'<text class="sub" x="{lx}" y="{ly + 7}" text-anchor="{anchor}">{sub}</text></g>')
    for n, vi in enumerate(starts, 1):
        x, y = p[vi]
        o.append(f'<g class="step" filter="url(#sh-blue)" data-at="{cl[vi]:.1f}" data-base="translate({x:g} {y:g})" '
                 f'transform="translate({x:g} {y:g})"><circle r="6.4"/><text y="2.9">{n}</text></g>')
    o.append('<g class="walker-g"><circle class="walker-halo" r="8"/><circle class="walker" r="3.4"/></g></g>')
    return "".join(o)


def booth():
    bx, by = M.OUR_BOOTH_CENTER
    x, y, w, h = M.OUR_BOOTH
    s = 10.5 / SYM_W                       # symbol 10.5 units wide inside a 9.5 radius pin
    wm_h = 7.4
    wm_w = WM_W * wm_h / WM_H
    pill_w = 10 + wm_w + 5 + 62
    px, py = bx - 15 - pill_w, by - 30       # pill to the upper left, like Kristina's
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#143DFF" rx=".6"/>'
            f'<circle class="ring" cx="{bx}" cy="{by}" r="10"/>'
            f'<g class="pin" data-base="translate({bx} {by})" transform="translate({bx} {by})" filter="url(#sh-blue)">'
            f'<circle class="pin-bg" r="9.5"/><circle class="pin-ring" r="7.6"/>'
            f'<g transform="translate({-SYM_W * s / 2:.2f} {-SYM_H * s / 2 - .3:.2f}) scale({s:.4f})">{SYMBOL}</g></g>'
            f'<g class="callout" data-base="translate({px:.1f} {py:.1f})" transform="translate({px:.1f} {py:.1f})" filter="url(#sh)">'
            f'<rect class="pill" width="{pill_w:.1f}" height="19" rx="9.5"/>'
            f'<g transform="translate(10 {9.5 - wm_h / 2:.2f}) scale({wm_h / WM_H:.4f})">{WORDMARK}</g>'
            f'<text class="pill-s" x="{10 + wm_w + 5:.1f}" y="12.4">· Booth</text>'
            f'<text class="pill-t" x="{10 + wm_w + 33:.1f}" y="12.4">55630</text></g>')


JS = r"""
var T={intro:.6,travel:7.2,arrive:1.6,hold:1.2,fade:.8};
window.__duration=T.intro+T.travel+T.arrive+T.hold+T.fade;
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function ease(x){return x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2}
function setup(svg){
  var g=svg.querySelector('.route'),rev=svg.querySelector('.reveal'),L=rev.getTotalLength();
  rev.style.strokeDasharray=L+' '+L;
  var line=g.querySelector('.line'),w=g.querySelector('.walker-g');
  var st=[].map.call(g.querySelectorAll('.step'),function(c){return {el:c,at:+c.getAttribute('data-at'),base:c.getAttribute('data-base')}});
  var ring=svg.querySelector('.ring'),pin=svg.querySelector('.pin'),P0=pin.getAttribute('data-base'),
      call=svg.querySelector('.callout'),C0=call.getAttribute('data-base');
  return function(t){
    var t1=T.intro,t2=t1+T.travel,t3=t2+T.arrive+T.hold;
    var k=ease(clamp((t-t1)/T.travel,0,1)),fade=1-clamp((t-t3)/T.fade,0,1),len=L*k;
    rev.style.strokeDashoffset=L-len; line.style.opacity=fade;
    st.forEach(function(s,i){var on=i===0||s.at<=len+.01,age=clamp((len-s.at)/12,0,1);
      var sc=on?(i===0?1:.7+.3*Math.min(1,age*1.5)+(age>0&&age<.55?Math.sin(age/.55*Math.PI)*.2:0)):0;
      s.el.setAttribute('transform',s.base+' scale('+sc.toFixed(3)+')');s.el.style.opacity=(on?1:0)*(i===0?1:fade)});
    var pt=rev.getPointAtLength(len); w.setAttribute('transform','translate('+pt.x+' '+pt.y+')');
    w.style.opacity=(t>=t1-.2?1:0)*fade;
    var a=t>=t2&&t<t3?((t-t2)%1.2)/1.2:0;
    ring.setAttribute('r',10+a*14); ring.style.opacity=t>=t2&&t<t3?(1-a)*.9:0;
    var pop=t>=t2&&t<t2+.5?Math.sin((t-t2)/.5*Math.PI):0;
    pin.setAttribute('transform',P0+' scale('+(1+pop*.16)+')');
    call.setAttribute('transform',C0+' translate(0 '+(-pop*1.6)+')');
  };
}
"""


def page(key):
    svg = base(f"fm-{key}") + [route(key), booth(), legend(), "</svg>"]
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Booth 55630 · {key}</title>
<style>{F.font_faces()}{CSS}
html,body{{width:{W}px;height:{H}px;overflow:hidden}} svg{{width:{W}px;height:{H}px}}</style></head><body>
{"".join(svg)}
<script>{JS}
var Fr=setup(document.querySelector('svg')); window.__frame=Fr; Fr(0);
if(!/render/.test(location.hash)){{var s0=performance.now();(function loop(n){{Fr(((n-s0)/1000)%__duration);requestAnimationFrame(loop)}})(s0)}}
</script></body></html>"""


def main():
    OUT.mkdir(exist_ok=True)
    for k in F.ROUTE_KEYS:
        (OUT / f"find-{k}.html").write_text(page(k))
        print(OUT / f"find-{k}.html")


if __name__ == "__main__":
    main()
