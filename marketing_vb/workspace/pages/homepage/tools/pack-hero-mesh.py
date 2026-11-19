#!/usr/bin/env python3
"""Pack hero-v3-body.json into a compact gzip binary for the homepage (v4.1).

Layout (little-endian, then gzip):
  b'HB01' · u32 metaLen · meta JSON (min, max, count, nIdx, nNoDot, loops, anchors, source)
  positions: 3 planes (x, y, z) of u16 deltas (wrapping) of u = q + 32768, each plane byte-shuffled (low bytes, then high bytes)
  indices:   nIdx i16 deltas from the previous index, byte-shuffled
  noDot:     nNoDot u16 deltas of the sorted list, byte-shuffled
The page decodes it with DecompressionStream('gzip').
"""
import base64, gzip, json, struct, sys
import numpy as np

src = sys.argv[1] if len(sys.argv) > 1 else 'hero-v3-body.json'
dst = sys.argv[2] if len(sys.argv) > 2 else 'hero-body-v3.bin'
d = json.load(open(src))
q = np.frombuffer(base64.b64decode(d['pos']), dtype='<i2').reshape(-1, 3).astype(np.int32)
idx = np.frombuffer(base64.b64decode(d['idx']), dtype='<u2').astype(np.int32)
no_dot = np.array(sorted(d.get('noDot') or []), dtype=np.int32)

def shuffle16(a):
    b = a.astype('<u2').view(np.uint8).reshape(-1, 2)
    return b[:, 0].tobytes() + b[:, 1].tobytes()

def rnd(o):
    if isinstance(o, float): return round(o, 5)
    if isinstance(o, list): return [rnd(x) for x in o]
    if isinstance(o, dict): return {k: rnd(v) for k, v in o.items()}
    return o

u = q + 32768
planes = b''
for k in range(3):
    dk = np.diff(np.concatenate([[0], u[:, k]])) & 0xFFFF
    planes += shuffle16(dk)
di = np.diff(np.concatenate([[0], idx]))
assert di.min() >= -32768 and di.max() <= 32767
dn = np.diff(np.concatenate([[0], no_dot])) if len(no_dot) else np.zeros(0, np.int32)
assert len(dn) == 0 or (dn.min() >= 0 and dn.max() <= 65535)
meta = {'min': d['min'], 'max': d['max'], 'count': int(len(q)), 'nIdx': int(len(idx)), 'nNoDot': int(len(no_dot)),
        'loops': rnd(d['loops']), 'anchors': rnd(d['anchors']), 'source': d.get('source', '')}
mj = json.dumps(meta, separators=(',', ':')).encode()
raw = b'HB01' + struct.pack('<I', len(mj)) + mj + planes + shuffle16(di & 0xFFFF) + shuffle16(dn)
open(dst, 'wb').write(gzip.compress(raw, 9, mtime=0))
print(f'{dst}: {len(raw):,} bytes raw, {len(gzip.compress(raw, 9)):,} gzip')
