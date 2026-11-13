#!/usr/bin/env python3
"""Full-floor "find us" map for /meet-us/ (CES 2027, booth 55630), v3.

Vadim, 2026-11-13: redraw the map in our design system, show the whole floor instead of a zoomed
window, loop the route, no replay button, no total distance, only the numbered steps.

Inputs
  booths_full.json      anonymous booth blocks of Halls A-D (extract_booths.py, Freeman plan 11/3/2026)
  ../v2/map_data.py     routes, step copy, our island, doors, escalators (units of the 10/5/2026 plan)
Outputs (out/, git-ignored)
  map-{route}.html      seekable animation page: window.__frame(t), window.__duration
  preview.html          all three loops playing in the browser (for review)
  *.mp4 / *.gif / *.png rendered by render.sh

Geometry below the routes is our own schematic: hall outline, walkways and labels traced by hand from
the CTA/Freeman plan; booths are blocks without names or numbers (CES contract section 37c).
"""
import base64
import html
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "v2"))
import map_data as M  # noqa: E402

FONT_DIR = Path.home() / ".local/share/fonts/satoshi"
OUT = HERE / "out"

# ------------------------------------------------------------------ geometry (v2 units, 1 u = 0.416 m)
VIEW = (150, 40, 870, 690)          # whole floor incl. ballroom, foyer and west concourse

HALL = [(165, 57), (737, 57), (737, 192), (912, 192), (912, 478), (716, 478), (716, 487), (696, 487),
        (696, 624), (597, 624), (560, 630), (500, 600), (440, 576), (360, 546), (300, 524), (240, 508),
        (196, 503), (174, 498), (165, 488)]

WALKWAY = [  # west concourse along the curved wall, corridor to Hall D, Venetian Foyer
    (300, 528), (360, 550), (440, 580), (500, 604), (559, 634), (598, 628), (698, 628), (698, 505),
    (709, 505), (709, 662), (1000, 662), (1000, 682), (879, 682), (879, 712), (803, 712), (803, 682),
    (660, 680), (600, 672), (500, 652), (440, 628), (360, 598), (300, 576), (262, 560)]

BALLROOM = (712, 505, 288, 152)
HUB = (636.5, 387, 58, 57.5)
ISLAND_BBOX = (789.4, 386.9, 804.0, 401.4)

ZONES = [  # label, x, y, highlighted
    ("HEALTH", 905, 330, True),
    ("SMART HOME", 449, 332, False),
    ("LIFESTYLE", 675, 186, False),
    ("GLOBAL PAVILIONS", 232, 334, False),
]
AREA_LABELS = [
    ("Venetian Ballroom", 856, 584, "area", 0),
    ("Venetian Foyer", 760, 679, "walk", 0),
    ("West concourse", 392, 590, "walk", 21),
    ("Health Hub", 665.5, 418.5, "hub", 0),
]
ENTRANCES = [  # label, door x, y, label x, y, anchor
    ("Hall D entrance", 707, 487, 721, 497.5, "start"),
    ("Hall C entrance", 578, 627, 572, 619, "end"),
]
ESC_LABELS = [("Escalators", 647.5, 671, "middle"), ("Escalators", 838, 700, "end")]

ROUTE_KEYS = ["foyer", "west"]
# the 11/3 plan has the booth column west of this aisle at 564-578, so the aisle centre is 581.7
ROUTE_POINTS = {
    "foyer": M.ROUTES["foyer"]["points"],
    "west": [(566, 646), (577.5, 628), (581.7, 576), (581.7, 452.6), (807.6, 452.6), (807.6, 393)],
}


def point_in_poly(x, y, poly):
    inside = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            inside = not inside
    return inside


def booths():
    out = []
    for x, y, w, h in json.loads((HERE / "booths_full.json").read_text()):
        cx, cy = x + w / 2, y + h / 2
        if not point_in_poly(cx, cy, HALL):
            continue
        if x < ISLAND_BBOX[2] and x + w > ISLAND_BBOX[0] and y < ISLAND_BBOX[3] and y + h > ISLAND_BBOX[1]:
            continue
        if abs(x - HUB[0]) < 1 and abs(y - HUB[1]) < 1:
            continue
        if min(w, h) < 2.5 or w * h < 14:     # slivers left by freight lines and wall hatching
            continue
        out.append((x, y, w, h))
    return out


# ------------------------------------------------------------------ helpers
def pts(poly):
    return " ".join(f"{x:g},{y:g}" for x, y in poly)


def cum(points):
    o = [0.0]
    for i in range(len(points) - 1):
        o.append(o[-1] + math.dist(points[i], points[i + 1]))
    return o


def chevrons(points, step=13.0, start=8.0):
    cl, res, s = cum(points), [], start
    while s < cl[-1] - 7:
        for i in range(len(points) - 1):
            if cl[i] <= s <= cl[i + 1]:
                (x0, y0), (x1, y1) = points[i], points[i + 1]
                f = (s - cl[i]) / (cl[i + 1] - cl[i])
                res.append((x0 + (x1 - x0) * f, y0 + (y1 - y0) * f,
                            math.degrees(math.atan2(y1 - y0, x1 - x0)), s))
                break
        s += step
    return res


def font_faces():
    faces = []
    for w, f in [(500, "Satoshi-Medium.otf"), (700, "Satoshi-Bold.otf"), (900, "Satoshi-Black.otf")]:
        b64 = base64.b64encode((FONT_DIR / f).read_bytes()).decode()
        faces.append(f"@font-face{{font-family:'Satoshi';font-weight:{w};font-style:normal;font-display:block;"
                     f"src:url(data:font/otf;base64,{b64}) format('opentype')}}")
    return "\n".join(faces)


CSS = """
:root{--blue:#143DFF;--blue-50:#ECEFFF;--blue-100:#D8DEFF;--blue-200:#B1BDFF;--blue-300:#8A9CFF;
  --blue-400:#4F6DFF;--blue-700:#0B2299;--navy:#050F40;--g500:#808080;--g600:#666666;--g700:#4C4C4C}
html,body{margin:0;background:#EEF0F6}
svg{display:block}
.f-bg{fill:#EEF0F6}
.f-walk{fill:#FFFFFF;stroke:#D5D8E2;stroke-width:.8;stroke-linejoin:round}
.f-hall{fill:#FFFFFF;stroke:#B9BCC8;stroke-width:1.2;stroke-linejoin:round}
.f-door{fill:#FFFFFF}
.f-health{fill:#ECEFFF;stroke:#8A9CFF;stroke-width:.9;stroke-dasharray:4 3}
.f-ballroom{fill:#E8EAF0}
.f-booth{fill:#DDE1EC}
.f-hub{fill:#D8DEFF}
.f-island{fill:#C9CFE0}
.f-esc{fill:#C9CDDA}.f-esc-l{stroke:#FFFFFF;stroke-width:.7}
.t{font-family:'Satoshi',sans-serif;font-weight:500}
.t-zone{font-size:9px;font-weight:700;letter-spacing:1.6px;fill:#A3A8B8;text-anchor:middle}
.t-zone.is-on{fill:#4F6DFF;text-anchor:end}
.t-area{font-size:10px;fill:#808080;text-anchor:middle}
.t-walk{font-size:9px;fill:#666666;text-anchor:middle}
.t-hub{font-size:8px;font-weight:700;fill:#0B2299;text-anchor:middle}
.t-door{font-size:8.5px;font-weight:700;fill:#050F40}
.t-small{font-size:7.5px;fill:#666666}
.f-door-dot{fill:#050F40}
.r-ghost{fill:none;stroke:#143DFF;stroke-opacity:.22;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:.1 5.5}
.r-line{fill:none;stroke:#143DFF;stroke-width:4.2;stroke-linecap:round;stroke-linejoin:round}
.r-chev{fill:none;stroke:#FFFFFF;stroke-width:1.3;stroke-linecap:round;stroke-linejoin:round}
.r-step circle{fill:#050F40;stroke:#FFFFFF;stroke-width:1.6}
.r-step text{font-family:'Satoshi',sans-serif;font-weight:700;font-size:9.5px;fill:#FFFFFF;text-anchor:middle}
.our{fill:#143DFF}
.ring{fill:none;stroke:#143DFF;stroke-width:1.4}
.callout rect{fill:#050F40}.callout path{fill:#050F40}
.callout text{font-family:'Satoshi',sans-serif;font-weight:700;font-size:9.5px;fill:#FFFFFF;text-anchor:middle}
.walker{fill:#143DFF;stroke:#FFFFFF;stroke-width:1.8}.walker-halo{fill:#143DFF;fill-opacity:.18}
.chip rect{fill:#FFFFFF;stroke:#E1E4EC;stroke-width:.8}
.chip text{font-family:'Satoshi',sans-serif;font-weight:700;font-size:10px;fill:#050F40}
.chip circle{fill:#143DFF}
"""


def base_svg(idp):
    vx, vy, vw, vh = VIEW
    o = [f'<svg viewBox="{vx} {vy} {vw} {vh}" xmlns="http://www.w3.org/2000/svg" role="img" '
         f'aria-labelledby="{idp}-t {idp}-d" preserveAspectRatio="xMidYMid meet">',
         f'<title id="{idp}-t">Route to 3DLOOK booth 55630, Venetian Expo, Level 2, Halls A-D</title>',
         f'<desc id="{idp}-d">Schematic map of Level 2 of the Venetian Expo, Halls A-D, with the walking route '
         f'to booth 55630 in the Health area. The numbered steps next to the map give the route in words.</desc>',
         f'<rect class="f-bg" x="{vx - 50}" y="{vy - 50}" width="{vw + 100}" height="{vh + 100}"/>',
         f'<polygon class="f-walk" points="{pts(WALKWAY)}"/>',
         f'<polygon class="f-hall" points="{pts(HALL)}"/>']
    for d in M.DOORS.values():
        o.append(f'<polygon class="f-door" points="{pts(d)}"/>')
    o.append(f'<polygon class="f-health" points="{pts(M.HEALTH)}"/>')
    x, y, w, h = BALLROOM
    o.append(f'<rect class="f-ballroom" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>')
    # booth blocks: grown by .25 u so strips of one block overlap and never show a seam
    o.append('<g class="f-booth">' + "".join(
        f'<rect x="{bx - .25:g}" y="{by - .25:g}" width="{bw + .5:g}" height="{bh + .5:g}"/>'
        for bx, by, bw, bh in booths()) + '</g>')
    x, y, w, h = HUB
    o.append(f'<rect class="f-hub" x="{x}" y="{y}" width="{w}" height="{h}" rx="2"/>')
    for bx, by, bw, bh in M.ISLAND_OTHERS:
        o.append(f'<rect class="f-island" x="{bx}" y="{by}" width="{bw}" height="{bh}"/>')
    for (x, y, w, h) in M.ESCALATORS.values():
        o.append(f'<rect class="f-esc" x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5"/>')
        for i in range(1, 6):
            xx = x + w * i / 6
            o.append(f'<line class="f-esc-l" x1="{xx:.1f}" y1="{y + 2}" x2="{xx:.1f}" y2="{y + h - 2}"/>')
    for text, x, y, on in ZONES:
        o.append(f'<text class="t t-zone{" is-on" if on else ""}" x="{x}" y="{y}">{text}</text>')
    for text, x, y, kind, rot in AREA_LABELS:
        tr = f' transform="rotate({rot} {x} {y})"' if rot else ""
        o.append(f'<text class="t t-{kind}" x="{x}" y="{y}"{tr}>{html.escape(text)}</text>')
    for text, x, y, anchor in ESC_LABELS:
        o.append(f'<text class="t t-small" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>')
    for text, dx, dy, lx, ly, anchor in ENTRANCES:
        if text.startswith("Hall C"):
            o.append(f'<circle class="f-door-dot" cx="{dx}" cy="{dy}" r="2.6"/>')
        o.append(f'<text class="t t-door" x="{lx}" y="{ly}" text-anchor="{anchor}">{text}</text>')
    # title chip, top left
    o.append(f'<g class="chip" transform="translate({vx + 18} {vy + 14})"><rect width="196" height="24" rx="12"/>'
             f'<circle cx="13" cy="12" r="3.6"/><text x="24" y="15.6">Venetian Expo · Level 2 · Halls A-D</text></g>')
    return o


def route_group(key, color="#143DFF", idx=0):
    r = M.ROUTES[key]
    p = ROUTE_POINTS[key]
    d = "M" + " L".join(f"{x:g},{y:g}" for x, y in p)
    cl = cum(p)
    starts = [0] + r["step_ends"][:-1]           # marker k sits where step k begins
    o = [f'<g class="route" data-route="{key}" data-len="{cl[-1]:.2f}">',
         f'<path class="r-ghost" d="{d}"/>',
         f'<path class="r-line" d="{d}" style="stroke:{color}"/>']
    for x, y, a, at in chevrons(p):
        o.append(f'<path class="r-chev" data-at="{at:.1f}" transform="translate({x:.2f} {y:.2f}) rotate({a:.0f})" '
                 f'd="M-1.8,-2.3 L1.1,0 L-1.8,2.3"/>')
    for n, vi in enumerate(starts, 1):
        x, y = p[vi]
        o.append(f'<g class="r-step" data-at="{cl[vi]:.1f}" transform="translate({x:g} {y:g})">'
                 f'<circle r="7.2"/><text y="3.4">{n}</text></g>')
    o.append(f'<g class="walker-g"><circle class="walker-halo" r="9"/><circle class="walker" r="4"/></g>')
    o.append('</g>')
    return "".join(o)


def booth_marker():
    bx, by = M.OUR_BOOTH_CENTER
    x, y, w, h = M.OUR_BOOTH
    return (f'<circle class="ring" cx="{bx}" cy="{by}" r="7"/>'
            f'<rect class="our" x="{x}" y="{y}" width="{w}" height="{h}" rx=".8"/>'
            f'<g class="callout" data-base="translate({bx} {by - 10})" transform="translate({bx} {by - 10})">'
            f'<rect x="-46" y="-19" width="92" height="16.5" rx="8.25"/><path d="M-4,-2.6 L4,-2.6 L0,2 Z"/>'
            f'<text y="-7.6">3DLOOK · 55630</text></g>')


JS = r"""
var T={intro:.6,travel:7.2,arrive:1.6,hold:1.2,fade:.8};
window.__duration=T.intro+T.travel+T.arrive+T.hold+T.fade;
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function ease(x){return x<.5?2*x*x:1-Math.pow(-2*x+2,2)/2}
function setup(svg){
  var routes=[].map.call(svg.querySelectorAll('.route'),function(g){
    var p=g.querySelector('.r-line'),L=p.getTotalLength();p.style.strokeDasharray=L+' '+L;
    return {p:p,L:L,w:g.querySelector('.walker-g'),
      ch:[].map.call(g.querySelectorAll('.r-chev'),function(c){return {el:c,at:+c.getAttribute('data-at')}}),
      st:[].map.call(g.querySelectorAll('.r-step'),function(c){return {el:c,at:+c.getAttribute('data-at'),base:c.getAttribute('transform')}})};
  });
  var ring=svg.querySelector('.ring'),call=svg.querySelector('.callout'),C0=call.getAttribute('data-base');
  return function(t){
    var t1=T.intro,t2=t1+T.travel,t3=t2+T.arrive+T.hold;
    var k=ease(clamp((t-t1)/T.travel,0,1)),fade=1-clamp((t-t3)/T.fade,0,1);
    routes.forEach(function(r){
      var len=r.L*k; r.p.style.strokeDashoffset=r.L-len; r.p.style.opacity=fade;
      r.ch.forEach(function(c){c.el.style.opacity=(c.at<=len?1:0)*fade});
      r.st.forEach(function(s,i){var on=i===0||s.at<=len+.01,age=clamp((len-s.at)/14,0,1);
        var sc=on?(i===0&&t<t1?1:.75+.25*Math.min(1,age*1.4)+(age>0&&age<.6?Math.sin(age/.6*Math.PI)*.18:0)):0;
        s.el.setAttribute('transform',s.base+' scale('+sc.toFixed(3)+')');s.el.style.opacity=(on?1:0)*(i===0?1:fade)});
      var pt=r.p.getPointAtLength(len); r.w.setAttribute('transform','translate('+pt.x+' '+pt.y+')');
      r.w.style.opacity=(t>=t1-.2?1:0)*fade;
    });
    var a=t>=t2&&t<t3?((t-t2)%1.2)/1.2:0;
    ring.setAttribute('r',7+a*13); ring.style.opacity=t>=t2&&t<t3?(1-a)*.9:.55;
    var pop=t>=t2&&t<t2+.5?Math.sin((t-t2)/.5*Math.PI)*.14:0;
    call.setAttribute('transform',C0+' scale('+(1+pop)+')');
  };
}
"""


def map_page(key, w=1600, h=1270):
    svg = base_svg(f"fm-{key}")
    svg.append(route_group(key))
    svg.append(booth_marker())
    svg.append("</svg>")
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Booth 55630 · {key}</title>
<style>{font_faces()}{CSS}
html,body{{width:{w}px;height:{h}px;overflow:hidden}} svg{{width:{w}px;height:{h}px}}</style></head><body>
{"".join(svg)}
<script>{JS}
var F=setup(document.querySelector('svg')); window.__frame=F; F(0);
if(!/render/.test(location.hash)){{var s=performance.now();(function loop(n){{F(((n-s)/1000)%__duration);requestAnimationFrame(loop)}})(s)}}
</script></body></html>"""


def main():
    OUT.mkdir(exist_ok=True)
    for k in ROUTE_KEYS:
        (OUT / f"map-{k}.html").write_text(map_page(k))
    print("booth blocks:", len(booths()))
    for k in ROUTE_KEYS:
        print(OUT / f"map-{k}.html")


if __name__ == "__main__":
    main()
