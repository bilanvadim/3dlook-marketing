#!/usr/bin/env python3
"""Sound for the social pack's video: a cue list → one 48 kHz stereo WAV.

Added 2026-11-16 (Vadim: «вивчи це і додай що корисно», about earshot). Runs under
earshot's own venv, not the system python: `social_video.py sound` calls it with
EARSHOT_PYTHON (default ~/.local/share/earshot-venv/bin/python) and a JSON job file.

earshot (github.com/Leonxlnx/earshot, MIT, pinned 4ac3d2a = 0.4.1) is installed
WITHOUT torch and without its two listening models (~1.1 GB); this script only uses
the parts that need neither:
  - the sound bank: 252 effects stored as synthesis code (no recorded audio, nothing
    licensed inside), rendered by id, aimed with `dur` / `apex` (a whoosh's loudest
    moment lands within 5 ms of the target), and audited model-free on every render
    (clicks, cut tails, clipping, DC, ring); a take that fails is re-rolled on a new seed;
  - pyloudnorm for integrated loudness.

Job (JSON):
    {"total": 19.4, "out": "/path/mix.wav",
     "cues": [{"role": "pop", "sound": "pro_pop_in/round", "at": 7.43,
               "align": "onset" | "peak", "level_db": -7.0, "dur": null, "apex": null}],
     "bed": null | {"path": "/path/bed.wav", "lufs": -24.0, "fade_in": 0.4, "fade_out": 1.2},
     "target_lufs": -14.0, "true_peak_db": -1.0}

`at` is where the cue's aligned point (onset or peak) lands on the film. Without a
bed the mix is peak-normalised only: effects alone integrate around -30 LUFS, and
pushing that to a platform target would make every pop shout. With a bed the
whole mix goes to `target_lufs`, capped by the true-peak ceiling.

Prints one JSON object: per-cue placements and audit, the mix's peak / true peak /
integrated loudness, and earshot's version.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

SR = 48000
MAX_REROLLS = 6


def _stereo(y):
    y = np.asarray(y, np.float64)
    return np.stack([y, y], axis=1) if y.ndim == 1 else y[:, :2]


def _true_peak_db(x):
    """4x oversampled peak, the way a limiter would see it (dBTP)."""
    up = resample_poly(x, 4, 1, axis=0)
    pk = float(np.abs(up).max()) if len(up) else 0.0
    return 20 * np.log10(pk) if pk > 0 else -240.0


def _lufs(x):
    import pyloudnorm as pyln
    try:
        v = float(pyln.Meter(SR).integrated_loudness(x))
    except ValueError:                       # shorter than one 400 ms block
        return None
    return round(v, 1) if np.isfinite(v) else None


def render_cue(c, i):
    """One take of a bank sound; a take the audit flags is re-rolled on the next seed."""
    from earshot.forge import bank
    entry = bank.get(c["sound"])
    base = int(entry.get("seed") or 0)
    last = None
    for k in range(MAX_REROLLS):
        # every repeat of a role gets its own seed, so a run of pops is not a machine gun
        seed = None if (i == 0 and k == 0) else base + 7919 * (i + 1) + 104729 * k
        y, meta = bank.render(c["sound"], seed=seed, dur=c.get("dur"), apex=c.get("apex"), peak_db=-1.0)
        last = (y, meta, seed)
        if (meta.get("checks") or {}).get("ok", True):
            break
    return last


def main(job_path: str) -> int:
    job = json.load(open(job_path, encoding="utf-8"))
    total = float(job["total"])
    n = int(round(total * SR))
    mix = np.zeros((n, 2), np.float64)
    placed, seen = [], {}
    for c in job["cues"]:
        i = seen.get(c["role"], 0)
        seen[c["role"]] = i + 1
        y, meta, seed = render_cue(c, i)
        y = _stereo(y) * 10 ** (float(c.get("level_db") or 0.0) / 20)
        anchor = float(meta["peak_s"] if c.get("align") == "peak" else meta["onset_s"])
        start = float(c["at"]) - anchor
        s = int(round(start * SR))
        a, b = max(0, s), min(n, s + len(y))
        if b > a:
            mix[a:b] += y[a - s:b - s]
        ck = meta.get("checks") or {}
        placed.append({"role": c["role"], "sound": c["sound"], "at": round(float(c["at"]), 3),
                       "start": round(start, 3), "seed": seed if seed is not None else meta.get("seed"),
                       "level_db": c.get("level_db"), "clean": bool(ck.get("ok", True)),
                       "warnings": [w.get("code") for w in ck.get("warnings") or []]})

    fx_peak = float(np.abs(mix).max())
    if fx_peak > 0:                          # the loudest effect sits at the ceiling; the rest keep their levels
        mix *= 10 ** (float(job.get("true_peak_db", -1.0)) / 20) / fx_peak

    bed = job.get("bed")
    if bed:
        import pyloudnorm as pyln
        b, sr = sf.read(bed["path"], always_2d=True)
        if sr != SR:
            raise SystemExit(f"bed must be {SR} Hz (social_video.py converts it), got {sr}")
        b = _stereo(b)[:n]
        if len(b) < n:
            b = np.pad(b, ((0, n - len(b)), (0, 0)))
        lv = pyln.Meter(SR).integrated_loudness(b)
        if np.isfinite(lv):
            b *= 10 ** ((float(bed.get("lufs", -20.0)) - lv) / 20)
        fi, fo = int(float(bed.get("fade_in", 0.4)) * SR), int(float(bed.get("fade_out", 1.2)) * SR)
        if fi:
            b[:fi] *= np.linspace(0, 1, fi)[:, None]
        if fo:
            b[-fo:] *= np.linspace(1, 0, fo)[:, None]
        mix += b
        lufs_now = _lufs(mix)
        gain = (float(job.get("target_lufs", -14.0)) - lufs_now) if lufs_now is not None else 0.0
        tp = _true_peak_db(mix)
        gain = min(gain, float(job.get("true_peak_db", -1.0)) - tp)
        mix *= 10 ** (gain / 20)

    tp = _true_peak_db(mix)
    if tp > float(job.get("true_peak_db", -1.0)) + 0.05:        # inter-sample overs after summing
        mix *= 10 ** ((float(job.get("true_peak_db", -1.0)) - tp) / 20)
        tp = _true_peak_db(mix)
    sf.write(job["out"], mix.astype(np.float32), SR, subtype="PCM_24")

    import earshot
    print(json.dumps({
        "out": job["out"], "duration": round(n / SR, 3), "cues": placed,
        "peak_dbfs": round(20 * np.log10(max(float(np.abs(mix).max()), 1e-12)), 2),
        "true_peak_dbtp": round(tp, 2), "lufs_i": _lufs(mix),
        "bed": bool(bed), "earshot": getattr(earshot, "__version__", "?"),
        "unclean": [p["sound"] for p in placed if not p["clean"]],
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
