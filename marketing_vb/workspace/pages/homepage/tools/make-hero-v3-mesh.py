#!/usr/bin/env python3
"""Build hero-v3-body.json (homepage hero v3: mannequin + scan lens) from hero-body-mesh.json.

Usage:
    python3 tools/make-hero-v3-mesh.py [arm_drop_degrees] < ../hero-body-mesh.json > ../hero-v3-body.json

Input is the v2 hero mesh (MakeHuman base mesh, body group, CC0 1.0; see make-hero-mesh.py).
What this script adds:
  1. Mannequin head: the source head is cut at the neck and replaced by a sculpted display-mannequin head
     (tools/hero_head.py: the source face blurred into a smooth sculpt, no ears, slicked-back sculpted hair
     with a low chignon, a longer neck, the chin slightly up).
  2. Arms lowered from the scan A-pose (default 32 degrees), blended at the shoulder.
  3. Measurement geometry for the page: bust / waist / hips tape loops (convex hull of the torso slice,
     like a tape), wrist loop, one loop per finger (ring finger flagged), and card anchor points.
Output: the same quantized pos/idx format as v2 plus "loops" and "anchors" (normalized space: feet y=0,
head y=2, facing +z). Stdlib, plus numpy for the head.
"""
import base64, json, math, os, struct, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hero_head  # noqa: E402
from collections import defaultdict

ARM_DROP = math.radians(float(sys.argv[1]) if len(sys.argv) > 1 else 32.0)
Y_CUT = 1.695          # the source head goes above this height; the sculpted head starts on the open neck loop


def decode(j):
    raw = base64.b64decode(j["pos"])
    q = struct.unpack("<%dh" % (len(raw) // 2), raw)
    mn, mx = j["min"], j["max"]
    s = 2 / (mx[1] - mn[1]); cx = (mn[0] + mx[0]) / 2; cz = (mn[2] + mx[2]) / 2
    P = []
    for i in range(0, len(q), 3):
        v = [mn[k] + (q[i + k] + 32768) / 65535 * (mx[k] - mn[k]) for k in range(3)]
        P.append([(v[0] - cx) * s, (v[1] - mn[1]) * s, (v[2] - cz) * s])
    ri = base64.b64decode(j["idx"])
    I = struct.unpack("<%dH" % (len(ri) // 2), ri)
    return P, [tuple(I[i:i + 3]) for i in range(0, len(I), 3)]


def encode(P, F):
    mn = [min(p[k] for p in P) for k in range(3)]
    mx = [max(p[k] for p in P) for k in range(3)]
    q = lambda v, k: max(-32768, min(32767, int(round((v - mn[k]) / (mx[k] - mn[k]) * 65535)) - 32768))
    pos = b"".join(struct.pack("<3h", *(q(p[k], k) for k in range(3))) for p in P)
    idx = b"".join(struct.pack("<3H", *f) for f in F)
    return {"min": mn, "max": mx, "count": len(P),
            "pos": base64.b64encode(pos).decode(), "idx": base64.b64encode(idx).decode()}


def smoothstep(a, b, x):
    t = max(0.0, min(1.0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


def neighbours(F, n):
    nb = [set() for _ in range(n)]
    for a, b, c in F:
        nb[a].update((b, c)); nb[b].update((a, c)); nb[c].update((a, b))
    return [list(s) for s in nb]


def taubin(P, nb, weight, iters=40, lam=0.5, mu=-0.53):
    for _ in range(iters):
        for f in (lam, mu):
            Q = [p[:] for p in P]
            for i, w in enumerate(weight):
                if w <= 0 or not nb[i]:
                    continue
                avg = [sum(P[j][k] for j in nb[i]) / len(nb[i]) for k in range(3)]
                for k in range(3):
                    Q[i][k] = P[i][k] + f * w * (avg[k] - P[i][k])
            P = Q
    return P


# ---- 2D helpers ----
def hull(pts):
    pts = sorted(set((round(x, 6), round(y, 6)) for x, y in pts))
    if len(pts) < 3:
        return pts
    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and (h[-1][0] - h[-2][0]) * (p[1] - h[-2][1]) - (h[-1][1] - h[-2][1]) * (p[0] - h[-2][0]) <= 0:
                h.pop()
            h.append(p)
        return h
    lo, up = half(pts), half(reversed(pts))
    return lo[:-1] + up[:-1]


def perimeter(poly):
    return sum(math.dist(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly)))


def resample(poly, n=96):
    L = perimeter(poly); out = []; seg = 0; acc = 0.0
    for k in range(n):
        target = k * L / n
        while True:
            a, b = poly[seg % len(poly)], poly[(seg + 1) % len(poly)]
            d = math.dist(a, b)
            if acc + d >= target or d == 0:
                t = 0 if d == 0 else (target - acc) / d
                out.append((a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t))
                break
            acc += d; seg += 1
    return out


def inflate(poly, f):
    cx = sum(p[0] for p in poly) / len(poly); cy = sum(p[1] for p in poly) / len(poly)
    return [(cx + (x - cx) * f, cy + (y - cy) * f) for x, y in poly]


# ---- 3D helpers ----
def sub(a, b): return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
def add(a, b): return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
def mul(a, s): return [a[0] * s, a[1] * s, a[2] * s]
def dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def cross(a, b): return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
def norm(a):
    l = math.sqrt(dot(a, a)) or 1.0
    return [a[0] / l, a[1] / l, a[2] / l]
def centroid(pts): return [sum(p[k] for p in pts) / len(pts) for k in range(3)]


def principal_axis(pts):
    c = centroid(pts)
    C = [[0.0] * 3 for _ in range(3)]
    for p in pts:
        d = sub(p, c)
        for i in range(3):
            for j in range(3):
                C[i][j] += d[i] * d[j]
    v = [1.0, 0.3, 0.2]
    for _ in range(60):
        v = norm([sum(C[i][j] * v[j] for j in range(3)) for i in range(3)])
    return c, v


def frame(axis):
    a = norm(axis)
    ref = [0, 1, 0] if abs(a[1]) < 0.9 else [1, 0, 0]
    u = norm(cross(a, ref)); w = cross(a, u)
    return a, u, w


def section_loop(pts, center, axis, half_width, inflate_by=1.03, n=96):
    """Tape loop around the slice of pts perpendicular to axis at center."""
    a, u, w = frame(axis)
    sl = [p for p in pts if abs(dot(sub(p, center), a)) < half_width]
    if len(sl) < 6:
        return None
    t0 = dot(center, a)
    flat = [(dot(sub(p, center), u), dot(sub(p, center), w)) for p in sl]
    poly = inflate(resample(hull(flat), n), inflate_by)
    loop = [add(add(center, mul(u, x)), mul(w, y)) for x, y in poly]
    return loop, perimeter(poly)


def components(vset, F):
    adj = defaultdict(set)
    for a, b, c in F:
        if a in vset and b in vset and c in vset:
            adj[a].update((b, c)); adj[b].update((a, c)); adj[c].update((a, b))
    seen, comps = set(), []
    for v in vset:
        if v in seen or v not in adj:
            continue
        stack, comp = [v], []
        seen.add(v)
        while stack:
            x = stack.pop(); comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        comps.append(comp)
    return sorted(comps, key=len, reverse=True)


def main():
    src = json.load(sys.stdin)
    P, F = decode(src)
    n = len(P)
    nb = neighbours(F, n)

    # 1. the source head (face, ears, mouth) is cut off at the neck later and replaced by a sculpted
    # mannequin head (tools/hero_head.py); here only the neck below the cut gets a light smoothing
    P = taubin(P, nb, [smoothstep(1.60, 1.69, p[1]) * 0.7 for p in P], iters=10)
    # mannequin body: no nipples, navel or genital crease (local Taubin passes), then a light pass everywhere
    def front_near(x, y, r=0.03):
        cand = [p for p in P if abs(p[0] - x) < r and abs(p[1] - y) < r]
        return max(cand, key=lambda p: p[2])
    belly = [p for p in P if abs(p[0]) < 0.015 and 1.10 < p[1] < 1.30 and p[2] > 0]
    def dent(v):
        ring = [q[2] for q in P if 0.008 < math.dist(q, v) < 0.03 and q[2] > 0]
        return (sum(ring) / len(ring) - v[2]) if ring else -1
    navel = max(belly, key=dent)
    nip_r = max((p for p in P if 0.05 < p[0] < 0.13 and 1.38 < p[1] < 1.50), key=lambda p: p[2])
    regions = [(nip_r, 0.055), ([-nip_r[0], nip_r[1], nip_r[2]], 0.055),
               (navel, 0.05), ([0.0, 0.985, 0.04], 0.095)]
    local_w = [max(smoothstep(r, r * 0.35, math.dist(p, c)) for c, r in regions) for p in P]
    no_dot = {i for i, p in enumerate(P) if any(math.dist(p, c) < r * 0.75 for c, r in regions)}
    P = taubin(P, nb, local_w, iters=110)
    # a light pass over the whole body for a moulded, mannequin surface
    P = taubin(P, nb, [0.35] * n, iters=3)

    # 2. measurement geometry is found in the A-pose (arms clear of the torso), then deformed with the arms.
    # Arm weight: above the knees everything past |x| 0.27 is arm (hips never get there; feet do, hence y > 0.8); the armpit band blends.
    xmax = max(p[0] for p in P)
    arm_w = [0.0 if p[1] < 0.8 else 1.0 if abs(p[0]) >= 0.27 else smoothstep(0.16, 0.27, abs(p[0])) * smoothstep(1.30, 1.42, p[1]) for p in P]
    is_arm = [w > 0.001 for w in arm_w]
    pivot = [0.175, 1.575]

    def deform(p, w, side):
        a = -ARM_DROP * side * w
        dx, dy = p[0] - side * pivot[0], p[1] - pivot[1]
        x = dx * math.cos(a) - dy * math.sin(a); y = dx * math.sin(a) + dy * math.cos(a)
        return [side * pivot[0] + x, pivot[1] + y, p[2]]

    def deform_full(p):  # for points that belong to the arm/hand entirely
        return deform(p, 1.0, 1 if p[0] > 0 else -1)

    # torso tape loops (horizontal), only torso vertices
    torso = [p for i, p in enumerate(P) if not is_arm[i]]
    def torso_loop(y):
        sl = [(p[0], p[2]) for p in torso if abs(p[1] - y) < 0.012]
        poly = inflate(resample(hull(sl), 128), 1.025)
        return [[x, y, z] for x, z in poly], perimeter(poly)
    def best(lo, hi, pick):
        ys = [lo + (hi - lo) * k / 30 for k in range(31)]
        return pick(ys, key=lambda y: torso_loop(y)[1])
    y_bust = best(1.38, 1.46, max)
    y_waist = best(1.24, 1.36, min)
    y_hips = best(1.08, 1.24, max)
    loops = {}
    lengths = {}
    for name, y in (("bust", y_bust), ("waist", y_waist), ("hips", y_hips)):
        loops[name], lengths[name] = torso_loop(y)
    y_thigh = 0.86
    sl = [(p[0], p[2]) for p in torso if abs(p[1] - y_thigh) < 0.012 and p[0] > 0.005]
    poly = inflate(resample(hull(sl), 96), 1.03)
    loops["thigh"] = [[x, y_thigh, z] for x, z in poly]; lengths["thigh"] = perimeter(poly)

    # right arm (+x): wrist and fingers, then mirror for the left
    right = [i for i, p in enumerate(P) if p[0] > 0.16 and is_arm[i]]
    def slab(a, b):
        return [P[i] for i in right if a * xmax < P[i][0] < b * xmax]
    elbow_c = centroid(slab(0.55, 0.57))
    wrist_pts = slab(0.70, 0.78)
    fore_axis = norm(sub(centroid(slab(0.73, 0.75)), elbow_c))
    wrist_c = add(centroid(slab(0.73, 0.75)), mul(fore_axis, 0.022))  # the slab sits on the forearm; the wrist bone is just past it
    arm_pts = [P[i] for i in right]
    # the wrist is the narrowest section between the forearm slab and the hand
    best_d = min((d / 1000 for d in range(-20, 61, 4)),
                 key=lambda d: (section_loop(arm_pts, add(wrist_c, mul(fore_axis, d)), fore_axis, 0.006, 1.0) or (None, 9))[1])
    wrist_c = add(wrist_c, mul(fore_axis, best_d))
    wl, wlen = section_loop(arm_pts, wrist_c, fore_axis, 0.010, 1.05)
    loops["wrist"] = wl; lengths["wrist"] = wlen

    # hand = arm vertices past the wrist along the forearm axis
    hand_ids = [i for i in right if dot(sub(P[i], wrist_c), fore_axis) > 0.01]
    hand_c, hand_axis = principal_axis([P[i] for i in hand_ids])
    if dot(hand_axis, sub(hand_c, wrist_c)) < 0:
        hand_axis = mul(hand_axis, -1)
    t_of = lambda i: dot(sub(P[i], wrist_c), hand_axis)
    tmax = max(t_of(i) for i in hand_ids)
    # Fingers: cut the hand across its axis; the thumb splits off first (shorter, points elsewhere),
    # the four fingers split past the webbing. Take the first cut with four big components.
    thumb_c = fingers = None
    for k in range(50, 96):
        cut = tmax * k / 100
        comps = components({i for i in hand_ids if t_of(i) > cut}, F)
        if thumb_c is None and len(comps) >= 2 and len(comps[1]) > 40:
            thumb_c = centroid([P[i] for i in comps[1]])
        big = [c for c in comps if len(c) > 60]
        if len(big) >= 4:
            fingers = big[:4]; break
    if fingers is None or thumb_c is None:
        sys.exit("finger segmentation failed")
    finger_info = []
    for comp in fingers:
        tmin = min(t_of(i) for i in comp)
        base_c = centroid([P[i] for i in comp if t_of(i) < tmin + 0.008])
        tip = max((P[i] for i in comp), key=lambda q: dot(sub(q, base_c), hand_axis))
        ax = norm(sub(tip, base_c)); L = math.dist(tip, base_c)
        ring_c = add(base_c, mul(ax, 0.22 * L))
        lp = section_loop([P[i] for i in comp], ring_c, ax, 0.0032, 1.14, 48)
        finger_info.append({"c": centroid([P[i] for i in comp]), "loop": lp})
    order = sorted(range(4), key=lambda k: math.dist(finger_info[k]["c"], thumb_c))  # index .. little
    loops["fingers"] = []
    for name, k in zip(["index", "middle", "ring", "little"], order):
        lp = finger_info[k]["loop"]
        if lp:
            loops["fingers"].append({"name": name, "pts": lp[0]})
            lengths["finger_" + name] = lp[1]

    # deform: arm vertices of the mesh, then arm/hand loops entirely
    P = [deform(p, arm_w[i], 1 if p[0] > 0 else -1) for i, p in enumerate(P)]
    loops["wrist"] = [deform_full(p) for p in loops["wrist"]]
    for f in loops["fingers"]:
        f["pts"] = [deform_full(p) for p in f["pts"]]

    mirror = lambda pts: [[-p[0], p[1], p[2]] for p in pts]
    loops["wrist_l"] = mirror(loops["wrist"])
    for f in loops["fingers"]:
        f["pts_l"] = mirror(f["pts"])

    # anchors on the surface (front-most vertex near a given x, y), body composition on the left half
    def front_point(x, y, r=0.02):
        cand = [p for i, p in enumerate(P) if not is_arm[i] and abs(p[0] - x) < r and abs(p[1] - y) < r]
        return max(cand, key=lambda p: p[2])
    def loop_front(pts, bias_x):
        return max(pts, key=lambda p: p[2] + bias_x * p[0])
    ring_f = next(f for f in loops["fingers"] if f["name"] == "ring")
    def upper_arm_left(y):
        cand = [p for i, p in enumerate(P) if is_arm[i] and p[0] < -0.16 and abs(p[1] - y) < 0.015]
        return max(cand, key=lambda p: p[2] - 0.3 * p[0])
    # left side of the screen (-x): body composition (torso + upper arm) above the left wrist and ring finger;
    # right side (+x): tape measurements. Anchor heights keep each column in the same order as its cards.
    anchors = {
        "bmi": front_point(-0.045, 1.535),
        "lean": upper_arm_left(1.42),
        "bodyfat": front_point(-0.06, 1.30),
        "wrist": loop_front(loops["wrist_l"], -0.6),
        "finger": loop_front(ring_f["pts_l"], -0.6),
        "bust": loop_front(loops["bust"], 0.9),
        "waist": loop_front(loops["waist"], 0.9),
        "hips": loop_front(loops["hips"], 0.9),
        "thigh": loop_front(loops["thigh"], 0.9),
    }
    # 3. replace the head: drop every face above the neck cut, then grow the sculpted head from the open loop
    field = hero_head.source_field(P, F)
    above = [p[1] > Y_CUT for p in P]
    F = [f for f in F if not all(above[v] for v in f)]
    directed = {(a, b) for f in F for a, b in ((f[0], f[1]), (f[1], f[2]), (f[2], f[0]))}
    nxt = {a: b for a, b in directed if (b, a) not in directed}
    loops_b, left = [], set(nxt)
    while left:
        v0 = min(left); lp = [v0]; left.discard(v0)
        while nxt[lp[-1]] != v0:
            lp.append(nxt[lp[-1]]); left.discard(lp[-1])
        loops_b.append(lp)
    loops_b.sort(key=len, reverse=True)
    ring0 = loops_b[0]
    for lp in loops_b[1:]:                      # stray holes, if any: fan at the centroid
        P.append(centroid([P[v] for v in lp])); tip = len(P) - 1
        F += [(lp[(j + 1) % len(lp)], lp[j], tip) for j in range(len(lp))]
    hv, hf, hids, H = hero_head.build(P, F, ring0, field)
    P += hv; F += hf
    # point mesh on the head: a Poisson-like subset at the body's dot spacing
    body_edge = sorted(math.dist(P[a], P[b]) for a, b, c in F[:4000] if P[a][1] > 1.2 and P[a][1] < 1.5)
    spacing = body_edge[len(body_edge) // 2] * 0.95
    cell = {}
    keep = set()
    for v in hids:
        key = tuple(int(math.floor(P[v][k] / spacing)) for k in range(3))
        near = [u for dx in (-1, 0, 1) for dy in (-1, 0, 1) for dz in (-1, 0, 1) for u in cell.get((key[0] + dx, key[1] + dy, key[2] + dz), [])]
        if all(math.dist(P[v], P[u]) >= spacing for u in near):
            keep.add(v); cell.setdefault(key, []).append(v)
    no_dot |= set(hids) - keep
    # compact: drop vertices no face uses any more
    used = sorted({v for f in F for v in f})
    remap = {o: i for i, o in enumerate(used)}
    P = [P[o] for o in used]
    F = [tuple(remap[v] for v in f) for f in F]
    no_dot = sorted(remap[i] for i in no_dot if i in remap)

    r6 = lambda pts: [[round(c, 4) for c in p] for p in pts]
    out = encode(P, F)
    out.update({
        "source": "MakeHuman base mesh, body group (CC0 1.0) via hero-body-mesh.json; sculpted mannequin head + arms lowered %.0f deg by tools/make-hero-v3-mesh.py" % math.degrees(ARM_DROP),
        "loops": {"bust": r6(loops["bust"]), "waist": r6(loops["waist"]), "hips": r6(loops["hips"]), "thigh": r6(loops["thigh"]),
                  "wrist": r6(loops["wrist"]), "wrist_l": r6(loops["wrist_l"]),
                  "fingers": [{"name": f["name"], "pts": r6(f["pts"]), "pts_l": r6(f["pts_l"])} for f in loops["fingers"]]},
        "anchors": {k: [round(c, 4) for c in v] for k, v in anchors.items()},
        "noDot": no_dot,
        "debug": {"head_vertices": len(hids), "head_dots": len(keep), "dot_spacing": round(spacing, 4), "neck": [round(H.rx0, 4), round(H.rz0, 4)], "wrist_shift": best_d, "y_bust": y_bust, "y_waist": y_waist, "y_hips": y_hips,
                  "lengths_units": {k: round(v, 4) for k, v in lengths.items()}},
    })
    json.dump(out, sys.stdout, separators=(",", ":"))


if __name__ == "__main__":
    main()
