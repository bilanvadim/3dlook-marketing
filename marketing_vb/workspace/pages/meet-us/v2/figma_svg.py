"""Inline-styled SVGs of the map for figma.createNodeFromSvg (no CSS classes). Scale: 2 px per plan unit,
origin = CAM_BOUNDS top-left, so every breakpoint crop is a plain offset + rescale of one component."""
import html, json, math
import map_data as M
from build import chevrons, cum_lengths

S = 2.0
X0, Y0, W, H = M.CAM_BOUNDS


def tx(x): return round((x - X0) * S, 1)
def ty(y): return round((y - Y0) * S, 1)
def P(poly): return " ".join(f"{tx(x)},{ty(y)}" for x, y in poly)
def R(r, fill, rx=1, extra=""):
    x, y, w, h = r
    return f'<rect x="{tx(x)}" y="{ty(y)}" width="{round(w*S,1)}" height="{round(h*S,1)}" rx="{rx*S:g}" fill="{fill}"{extra}/>'
def T(text, x, y, size, fill, weight=500, anchor="start", ls=0):
    return (f'<text x="{tx(x)}" y="{ty(y)}" font-family="Satoshi" font-weight="{weight}" font-size="{size*S:g}" '
            f'fill="{fill}" text-anchor="{anchor}"' + (f' letter-spacing="{ls*S:g}"' if ls else '') + f'>{html.escape(text)}</text>')


def base_svg():
    w, h = W * S, H * S
    o = [f'<svg width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}" xmlns="http://www.w3.org/2000/svg">',
         f'<rect x="0" y="0" width="{w:g}" height="{h:g}" fill="#EEF0F6"/>',
         f'<polygon points="{P(M.WALKWAY)}" fill="#FFFFFF" stroke="#D1D1D1" stroke-width="1.2"/>',
         f'<polygon points="{P(M.HALL)}" fill="#FFFFFF" stroke="#B9BCC8" stroke-width="1.8"/>']
    for d in M.DOORS.values():
        o.append(f'<polygon points="{P(d)}" fill="#FFFFFF"/>')
    o.append(f'<polygon points="{P(M.HEALTH)}" fill="#ECEFFF" fill-opacity="0.75" stroke="#8A9CFF" stroke-width="1.4" stroke-dasharray="6 4"/>')
    o.append(R(M.BALLROOM, "#E3E5EC", 3))
    for b in M.BOOTHS + M.ISLAND_OTHERS:
        o.append(R(b, "#DCE0EC", 1))
    o.append(R(M.HEALTH_HUB, "#D8DEFF", 2, ' stroke="#B1BDFF" stroke-width="1.2"'))
    for (x, y, w_, h_) in M.ESCALATORS.values():
        o.append(R((x, y, w_, h_), "#C9CDDA", 1.5))
        for i in range(1, 6):
            xx = x + w_ * i / 6
            o.append(f'<line x1="{tx(xx)}" y1="{ty(y+2)}" x2="{tx(xx)}" y2="{ty(y+h_-2)}" stroke="#FFFFFF" stroke-width="1.2"/>')
    kinds = {"area": (8, "#808080", 500, "middle", 0), "walk": (7.5, "#666666", 500, "middle", 0),
             "walkl": (7.5, "#666666", 500, "start", 0), "hub": (7, "#0B2299", 700, "middle", 0),
             "zone": (7, "#4F6DFF", 700, "start", 1.2), "aisle": (6, "#808080", 500, "middle", 0)}
    for text, x, y, kind in M.LABELS:
        size, fill, wt, anc, ls = kinds[kind]
        o.append(T(text, x, y, size, fill, wt, anc, ls))
    for text, x, y, anchor in M.ESCALATOR_LABELS:
        o.append(T(text, x, y, 6, "#666666", 500, anchor))
    for e in M.ENTRANCES.values():
        dx, dy = e["door"]; lx, ly = e["label_at"]
        o.append(f'<circle cx="{tx(dx)}" cy="{ty(dy)}" r="{2.2*S:g}" fill="#050F40"/>')
        o.append(T(e["label"], lx, ly, 6.5, "#050F40", 700, e["anchor"]))
    o.append('</svg>')
    return "".join(o)


def booth_svg():
    """our booth + callout as its own layer (sits above the route)"""
    bx, by = M.OUR_BOOTH_CENTER
    w, h = W * S, H * S
    x, y, bw, bh = M.OUR_BOOTH
    o = [f'<svg width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}" xmlns="http://www.w3.org/2000/svg">',
         f'<circle cx="{tx(bx)}" cy="{ty(by)}" r="{6*S:g}" fill="none" stroke="#143DFF" stroke-width="2.2" stroke-opacity="0.6"/>',
         R(M.OUR_BOOTH, "#143DFF", 0.8),
         f'<rect x="{tx(bx-31)}" y="{ty(by-9-15.5)}" width="{62*S:g}" height="{13.5*S:g}" rx="{3*S:g}" fill="#050F40"/>',
         f'<polygon points="{tx(bx-3.5)},{ty(by-11.2)} {tx(bx+3.5)},{ty(by-11.2)} {tx(bx)},{ty(by-7.2)}" fill="#050F40"/>',
         T("3DLOOK · 55630", bx, by - 9 - 6.4, 7, "#FFFFFF", 700, "middle"),
         '</svg>']
    return "".join(o)


def route_svg(key, upto=None, ghost=True):
    r = M.ROUTES[key]; p = r["points"]
    cl = cum_lengths(p); L = cl[-1]
    if upto is None: upto = L
    # partial polyline up to length `upto`
    part = [p[0]]
    for i in range(len(p) - 1):
        if cl[i + 1] <= upto:
            part.append(p[i + 1])
        else:
            f = (upto - cl[i]) / (cl[i + 1] - cl[i])
            part.append((p[i][0] + (p[i + 1][0] - p[i][0]) * f, p[i][1] + (p[i + 1][1] - p[i][1]) * f))
            break
    w, h = W * S, H * S
    d_full = "M" + " L".join(f"{tx(x)},{ty(y)}" for x, y in p)
    d_part = "M" + " L".join(f"{tx(x)},{ty(y)}" for x, y in part)
    o = [f'<svg width="{w:g}" height="{h:g}" viewBox="0 0 {w:g} {h:g}" xmlns="http://www.w3.org/2000/svg">']
    if ghost:
        o.append(f'<path d="{d_full}" fill="none" stroke="#143DFF" stroke-opacity="0.3" stroke-width="{2.4*S:g}" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="0.2 8"/>')
    if upto > 0.5:
        o.append(f'<path d="{d_part}" fill="none" stroke="#143DFF" stroke-width="{3.4*S:g}" stroke-linecap="round" stroke-linejoin="round"/>')
        for x, y, a, at in chevrons(p):
            if at <= upto:
                c, s_ = math.cos(math.radians(a)), math.sin(math.radians(a))
                pts = [(-1.5, -1.9), (0.9, 0), (-1.5, 1.9)]
                q = [(x + px * c - py * s_, y + px * s_ + py * c) for px, py in pts]
                o.append(f'<path d="M{tx(q[0][0])},{ty(q[0][1])} L{tx(q[1][0])},{ty(q[1][1])} L{tx(q[2][0])},{ty(q[2][1])}" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    sx, sy = p[0]
    o.append(f'<circle cx="{tx(sx)}" cy="{ty(sy)}" r="{3.4*S:g}" fill="#FFFFFF" stroke="#050F40" stroke-width="3.2"/>')
    o.append('</svg>')
    walker = part[-1]
    return "".join(o), (tx(walker[0]), ty(walker[1]))


if __name__ == "__main__":
    import sys
    b = base_svg(); bo = booth_svg(); f, _ = route_svg("foyer"); w, _ = route_svg("west")
    print(len(b), len(bo), len(f), len(w))
