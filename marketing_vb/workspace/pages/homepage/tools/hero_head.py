"""Sculpted mannequin head for the homepage hero v3 (used by make-hero-v3-mesh.py).

A display-mannequin head of the kind couture windows use: the source face blurred into a smooth sculpt
(nose, brow, cheekbones, lips and chin stay as soft forms; eyes, ears and skin detail go), sculpted
slicked-back hair with a clean hairline and a low chignon, a slim neck, the chin slightly up.
It is a signed distance field: the source head's distance (sign from vertex normals) on a grid, Gaussian
blurred, plus hair shell, chignon and neck. Meshed as a ring lattice that starts on the body's open neck
loop, ray-cast from inside the head, then relaxed on the surface (Laplacian step + projection) so the
triangles stay even. Normalized body space: feet y=0, head y~2, facing +z.
"""
import math
import numpy as np

PITCH = math.radians(-5.0)          # chin slightly up
HC = np.array([0.0, 1.888, -0.060])  # head frame origin (raised: a long, slim neck)
O1 = np.array([0.0, 1.860, -0.064])  # the same point on the source head (local coords = source - O1)
BLUR = 0.0050                        # Gaussian sigma of the face sculpt, source units
CELL = 0.0020
SCALE = 0.965                        # display mannequins carry a slightly small head


def _ell(p, c, r):
    q = (p - c) / r
    k0 = np.linalg.norm(q, axis=-1)
    k1 = np.linalg.norm((p - c) / (r * r), axis=-1)
    return k0 * (k0 - 1.0) / np.maximum(k1, 1e-9)


def _cap(p, a, b, ra, rb):
    pa = p - a; ba = b - a
    t = np.clip((pa @ ba) / (ba @ ba), 0.0, 1.0)
    return np.linalg.norm(pa - t[:, None] * ba, axis=-1) - (ra + (rb - ra) * t)


def _smin(a, b, k):
    h = np.clip(0.5 + 0.5 * (b - a) / k, 0.0, 1.0)
    return b + (a - b) * h - k * h * (1.0 - h)


def _smax(a, b, k):
    return -_smin(-a, -b, k)


def _blur1(a, sig, axis):
    r = int(math.ceil(3 * sig)); x = np.arange(-r, r + 1); w = np.exp(-0.5 * (x / sig) ** 2); w /= w.sum()
    pad = [(0, 0)] * 3; pad[axis] = (r, r)
    b = np.pad(a, pad, mode="edge"); out = np.zeros_like(a)
    n = a.shape[axis]
    for i, wi in enumerate(w):
        sl = [slice(None)] * 3; sl[axis] = slice(i, i + n)
        out += wi * b[tuple(sl)]
    return out


def _grow(m, k):
    """k steps of 6-neighbour dilation (a diamond of radius k cells)."""
    for _ in range(k):
        g = m.copy()
        g[1:] |= m[:-1]; g[:-1] |= m[1:]; g[:, 1:] |= m[:, :-1]; g[:, :-1] |= m[:, 1:]
        g[:, :, 1:] |= m[:, :, :-1]; g[:, :, :-1] |= m[:, :, 1:]
        m = g
    return m


def _grow26(m):
    """one step of 26-neighbour dilation (3x3x3 cube), separable."""
    g = m.copy(); g[1:] |= m[:-1]; g[:-1] |= m[1:]
    h = g.copy(); h[:, 1:] |= g[:, :-1]; h[:, :-1] |= g[:, 1:]
    k = h.copy(); k[:, :, 1:] |= h[:, :, :-1]; k[:, :, :-1] |= h[:, :, 1:]
    return k


def _steps(seed, iters):
    """cells to reach from seed, alternating 6- and 26-neighbour steps (close to Euclidean)."""
    d = np.full(seed.shape, iters + 1, np.float32); d[seed] = 0; cur = seed.copy()
    for k in range(1, iters + 1):
        nxt = _grow26(cur) if k % 2 == 0 else _grow(cur, 1)
        d[nxt & ~cur] = k; cur = nxt
    return d


class Field:
    """Smoothed occupancy of the source head (local coords), sampled trilinearly as an approximate SDF.
    The triangles are rasterized into voxels, closed morphologically (fills the lip line and eyelid folds,
    the air cannot get into the mouth or eye pockets), then Gaussian blurred: a softly sculpted head."""
    CLOSE = 4                                  # closing radius, cells

    def __init__(self, V, Fc, neck_xz, neck_y):
        lo = V.min(0) - 0.03; hi = V.max(0) + 0.03
        self.lo = lo; self.n = np.ceil((hi - lo) / CELL).astype(int) + 1
        wall = np.zeros(self.n, bool)
        T = V[np.array(Fc)]                                  # faces x 3 x 3
        emax = np.max(np.linalg.norm(T - np.roll(T, 1, axis=1), axis=2), axis=1)
        steps = np.maximum(1, np.ceil(emax / (CELL * 0.4)).astype(int))
        for m in np.unique(steps):
            tri = T[steps == m]
            uv = np.array([(i / m, j / m) for i in range(m + 1) for j in range(m + 1 - i)])
            pts = tri[:, 0][:, None] + uv[None, :, :1] * (tri[:, 1] - tri[:, 0])[:, None] + uv[None, :, 1:] * (tri[:, 2] - tri[:, 0])[:, None]
            ij = np.floor((pts.reshape(-1, 3) - lo) / CELL).astype(int)
            wall[ij[:, 0], ij[:, 1], ij[:, 2]] = True
        g = [lo[k] + CELL * np.arange(self.n[k]) for k in range(3)]
        GY = g[1][None, :, None]
        (cx, cz), (ex, ez) = neck_xz
        GE = ((g[0][:, None, None] - cx) / (ex + 0.014)) ** 2 + ((g[2][None, None, :] - cz) / (ez + 0.014)) ** 2
        plug = (GY < neck_y + 0.012) & (GE < 1)                           # seal the neck opening
        GX = g[0][:, None, None]; GZ = g[2][None, None, :]
        mouth = ((GX / 0.034) ** 2 + ((GY + 0.070) / 0.016) ** 2 + ((GZ - 0.100) / 0.026) ** 2) < 1   # the lips are parted
        blocked = _grow(wall, self.CLOSE) | plug | mouth
        O = np.zeros(self.n, bool)
        O[0], O[-1], O[:, 0], O[:, -1], O[:, :, 0], O[:, :, -1] = True, True, True, True, True, True
        O &= ~blocked
        while True:
            N2 = _grow(O, 1) & ~blocked
            if N2.sum() == O.sum():
                break
            O = N2
        self.blocked, self.O = blocked, O                                    # kept for debugging
        solid = ~_grow(O, self.CLOSE)                                        # closing: back onto the surface
        # signed distance (cells) from the closed solid, then blurred: smooth, and a true distance far out,
        # so offsets (the hair shell) and unions (the chignon) behave
        f = np.where(solid, -(_steps(~solid, 48) - 0.5), _steps(solid, 48) - 0.5).astype(float) * CELL
        sig = BLUR / CELL
        for ax in range(3):
            f = _blur1(f, sig, ax)
        self.f = f

    def __call__(self, l):
        u = (l - self.lo) / CELL
        i = np.floor(u).astype(int)
        inside = np.all((i >= 0) & (i < self.n - 1), axis=1)
        i = np.clip(i, 0, self.n - 2); t = np.clip(u - i, 0, 1)
        f = self.f; out = 0.0
        for dx in (0, 1):
            for dy in (0, 1):
                for dz in (0, 1):
                    w = (t[:, 0] if dx else 1 - t[:, 0]) * (t[:, 1] if dy else 1 - t[:, 1]) * (t[:, 2] if dz else 1 - t[:, 2])
                    out = out + w * f[i[:, 0] + dx, i[:, 1] + dy, i[:, 2] + dz]
        return np.where(inside, out, 0.10)


class Head:
    def __init__(self, neck_c, neck_rx, neck_rz, field):
        self.field = field
        self.c0 = np.array(neck_c, float)     # neck loop centre at the cut
        self.rx0, self.rz0 = neck_rx, neck_rz
        tilt = math.radians(14.0)             # the neck leans forward a little
        self.na = np.array([0.0, math.cos(tilt), math.sin(tilt)])
        self.nw = np.array([0.0, -math.sin(tilt), math.cos(tilt)])
        cp, sp = math.cos(PITCH), math.sin(PITCH)
        self.R = np.array([[1, 0, 0], [0, cp, -sp], [0, sp, cp]])   # world -> head-local rotation about x

    def neck(self, p):
        d = p - self.c0
        t = d @ self.na
        s = np.clip(t / 0.11, 0.0, 1.0); s = s * s * (3 - 2 * s)
        rx = self.rx0 + (self.rx0 * 0.84 - self.rx0) * s
        rz = self.rz0 + (self.rz0 * 0.90 - self.rz0) * s
        qx = d[:, 0]; qz = d @ self.nw
        side = (np.sqrt((qx / rx) ** 2 + (qz / rz) ** 2) - 1.0) * np.minimum(rx, rz)
        return _smax(side, t - 0.19, 0.02)               # capped inside the skull

    def head(self, p):
        l = ((p - HC) @ self.R.T) / SCALE
        V = np.array
        f = self.field(l)
        # below the jaw the neck primitive takes over: cut the source neck away under a tilted plane
        cut = (l - V([0, -.135, .020])) @ V([0, -.919, -.394])
        face = _smax(f, cut, .010)
        # sculpted hair, as on couture window mannequins: slicked back over the ears into a low chignon. The shell
        # grows from nothing at the hairline to ~5 mm, so the hairline reads as a soft edge, not a helmet rim.
        # Hairline: across the forehead, down the temple, over the (absent) ear, down to the nape.
        top = (l - V([0, .070, .104])) @ V([0.0, .958, -.287])                  # forehead line, dipping at the temples
        temple = .020 - l[:, 2] - .30 * (l[:, 1] - .03)                          # behind the temple line
        nape = (l[:, 1] - .60 * l[:, 2] + .018) / 1.166                          # above a line rising from nape (y -.078) to temple (y -.008)
        side = _smin(temple, nape, .020)
        sm = lambda x: x * x * (3 - 2 * x)
        rt = np.clip((top + .002) / .018, 0.0, 1.0)                              # crisp-ish edge on the forehead
        rs = np.clip((side + .010) / .050, 0.0, 1.0)                             # fades out over the ear and nape
        hair = face - .0052 * sm(rt) * sm(rs)                                    # face already carries the jaw cut
        bun = _ell(l, V([0, -.046, -.106]), V([.050, .036, .033]))               # chignon, set into the nape
        d = _smin(hair, bun, .014)
        d = d * SCALE
        return d

    def sdf(self, p):
        p = np.atleast_2d(p)
        return _smin(self.head(p), self.neck(p), 0.024)

    def grad(self, p, e=4e-4):
        g = np.zeros_like(p)
        for k in range(3):
            o = np.zeros(3); o[k] = e
            g[:, k] = (self.sdf(p + o) - self.sdf(p - o)) / (2 * e)
        return g

    def project(self, p, steps=3):
        for _ in range(steps):
            d = self.sdf(p); g = self.grad(p)
            p = p - (d / np.maximum((g * g).sum(1), 1e-9))[:, None] * g
        return p

    def raycast(self, o, dirs, tmax=0.32, n=320):
        """First exit of rays from o (inside) along dirs."""
        ts = np.linspace(0.0, tmax, n)
        hit = np.full(len(dirs), tmax)
        prev = self.sdf(np.repeat(o[None], len(dirs), 0))
        done = np.zeros(len(dirs), bool)
        for i in range(1, n):
            cur = self.sdf(o + dirs * ts[i])
            cross = (~done) & (prev < 0) & (cur >= 0)
            # linear interpolation of the zero crossing
            f = prev[cross] / (prev[cross] - cur[cross])
            hit[cross] = ts[i - 1] + (ts[i] - ts[i - 1]) * f
            done |= cross
            prev = cur
        return o + dirs * hit[:, None]


def source_field(P, F):
    """Smoothed field of the source head (call before the head faces are dropped). Ears are pressed flat
    onto the side of the skull first (abstract mannequins have none)."""
    A = np.array(P, float)
    keep = A[:, 1] > 1.70
    ids = np.nonzero(keep)[0]; remap = -np.ones(len(A), int); remap[ids] = np.arange(len(ids))
    Fc = [[remap[v] for v in f] for f in F if all(keep[v] for v in f)]
    A = A[keep]
    ear = (A[:, 1] > 1.775) & (A[:, 1] < 1.895) & (A[:, 2] < 0.0)
    A[ear, 0] = np.sign(A[ear, 0]) * np.minimum(np.abs(A[ear, 0]), 0.074)
    # the open neck loop of the source head (edges used by one face only) gives the plug's shape and height
    cnt = {}
    for f in Fc:
        for a, b in ((f[0], f[1]), (f[1], f[2]), (f[2], f[0])):
            k = (min(a, b), max(a, b)); cnt[k] = cnt.get(k, 0) + 1
    rim = A[sorted({v for k, c in cnt.items() if c == 1 for v in k})]
    lo_, hi_ = rim.min(0), rim.max(0)
    neck = ([float((lo_[0] + hi_[0]) / 2 - O1[0]), float((lo_[2] + hi_[2]) / 2 - O1[2])],
            [float((hi_[0] - lo_[0]) / 2), float((hi_[2] - lo_[2]) / 2)])
    return Field(A - O1, Fc, neck, float(hi_[1] - O1[1]))


def build(P, F, ring0, field, M=208, K=96, relax=70):
    """Grow the head from the open neck loop ring0 (vertex ids into P, boundary order).
    Returns (new_vertices, new_faces, head_ids, head) with ids continuing after len(P)."""
    loop = np.array([P[v] for v in ring0])
    c0 = [0.0, float(loop[:, 1].mean()), float((loop[:, 2].min() + loop[:, 2].max()) / 2)]
    rx0 = float((loop[:, 0].max() - loop[:, 0].min()) / 2)
    rz0 = float((loop[:, 2].max() - loop[:, 2].min()) / 2)
    H = Head(c0, rx0, rz0, field)
    o = np.array([0.0, 1.875, -0.070])            # ray origin, inside the skull above the neck

    # spherical angles of the loop as seen from o; azimuth direction follows the loop order
    d = loop - o
    th_loop = np.arccos(np.clip(d[:, 1] / np.linalg.norm(d, axis=1), -1, 1))
    ph_loop = np.unwrap(np.arctan2(d[:, 2], d[:, 0]))
    sgn = 1.0 if ph_loop[-1] > ph_loop[0] else -1.0
    ph0 = ph_loop[0]
    rel = (ph_loop - ph0) * sgn                    # 0 .. ~2pi, increasing
    order = np.argsort(rel)
    if not (np.all(np.diff(rel) > 0)):
        raise SystemExit('neck loop azimuth is not monotonic as seen from the ray origin')
    rel_s = np.concatenate([rel[order] - 2 * np.pi, rel[order], rel[order] + 2 * np.pi])
    th_s = np.concatenate([th_loop[order]] * 3)

    base = len(P)
    a = 2 * np.pi * np.arange(M) / M
    th_ring = np.interp(a, rel_s, th_s)
    dirs = []
    for k in range(1, K):
        th = th_ring * (1.0 - k / K)
        ph = ph0 + sgn * a
        dirs.append(np.stack([np.sin(th) * np.cos(ph), np.cos(th), np.sin(th) * np.sin(ph)], 1))
    dirs.append(np.array([[0.0, 1.0, 0.0]]))
    pts = H.raycast(o, np.vstack(dirs))
    verts = pts.tolist()
    rings = [list(range(base + (k - 1) * M, base + k * M)) for k in range(1, K)]
    pole = base + len(verts) - 1

    faces = []
    # zip ring0 (body loop, n0 vertices) to ring 1 (M vertices) by azimuth
    n0 = len(ring0)
    r0 = [ring0[i] for i in order]                 # sorted by azimuth (same as boundary order, rotated)
    a0 = list(rel[order]); a1 = [2 * np.pi * j / M for j in range(M)]
    r1 = rings[0]
    i = j = 0
    while i < n0 or j < M:
        na = a0[i + 1] if i + 1 < n0 else a0[0] + 2 * np.pi
        nb = a1[j + 1] if j + 1 < M else 2 * np.pi
        if j >= M or (i < n0 and na <= nb):
            faces.append((r0[(i + 1) % n0], r0[i % n0], r1[j % M])); i += 1
        else:
            faces.append((r0[i % n0], r1[j % M], r1[(j + 1) % M])); j += 1
    for k in range(len(rings) - 1):
        a, b = rings[k], rings[k + 1]
        for j in range(M):
            a0_, a1_, b0, b1 = a[j], a[(j + 1) % M], b[j], b[(j + 1) % M]
            faces += [(a1_, a0_, b0), (a1_, b0, b1)]
    last = rings[-1]
    faces += [(last[(j + 1) % M], last[j], pole) for j in range(M)]

    # relax on the surface: umbrella step, then project back onto the SDF; the body loop stays fixed
    nv = len(verts)
    allp = np.vstack([np.array(P, float), np.array(verts)])
    nbrs = [set() for _ in range(len(allp))]
    for f in faces:
        for x in f:
            nbrs[x].update(y for y in f if y != x)
    ids = np.arange(base, base + nv)
    src, dst = [], []
    for v in ids:
        for u in nbrs[v]:
            src.append(v); dst.append(u)
    src = np.array(src); dst = np.array(dst)
    deg = np.bincount(src - base, minlength=nv).astype(float)
    for it in range(relax):
        cur = allp[ids]
        acc = np.zeros((nv, 3))
        np.add.at(acc, src - base, allp[dst])
        avg = acc / deg[:, None]
        g = H.grad(cur); nrm = g / np.maximum(np.linalg.norm(g, axis=1), 1e-9)[:, None]
        step = avg - cur
        step -= (step * nrm).sum(1)[:, None] * nrm                 # tangential only: vertices do not slide off bumps
        allp[ids] = H.project(cur + 0.55 * step, steps=2)
    # the seam: body loop and first head rings meet with a small step and thin zip triangles; a Taubin pass
    # over a band around the loop (body side + head side) blends them into one smooth neck
    adj = [set() for _ in range(len(allp))]
    for f in list(F) + faces:
        for x in f:
            adj[x].update(y for y in f if y != x)
    cxz = np.array([c0[0], c0[2]])
    band = [v for v in range(base) if abs(allp[v][1] - c0[1]) < 0.045
            and np.linalg.norm(allp[v][[0, 2]] - cxz) < max(rx0, rz0) * 1.45 and adj[v]]
    band += [v for k in range(min(7, len(rings))) for v in rings[k]]
    w = {v: 1.0 for v in band}
    for v in band[:]:
        if v < base and abs(allp[v][1] - c0[1]) > 0.03:
            w[v] = 0.5
    for _ in range(25):
        for lam in (0.5, -0.53):
            upd = {}
            for v in band:
                nb = list(adj[v])
                avg = allp[nb].mean(0)
                upd[v] = allp[v] + lam * w[v] * (avg - allp[v])
            for v, q in upd.items():
                allp[v] = q
    for v in band:
        if v < base:
            P[v] = allp[v].tolist()
    out = allp[ids]
    return out.tolist(), faces, list(ids), H
