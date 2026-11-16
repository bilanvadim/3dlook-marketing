#!/usr/bin/env python3
"""Sound for the social pack's video: a cue list (+ an optional music bed) → one WAV.

Added 2026-11-16 (Vadim: «вивчи це і додай що корисно», about earshot; the same day
«дозволяю музику і не треба зазначати автора»). Runs under earshot's own venv, not
the system python: `social_video.py sound` calls it with EARSHOT_PYTHON (default
~/.local/share/earshot-venv/bin/python) and a JSON job file.

earshot (github.com/Leonxlnx/earshot, MIT, pinned 4ac3d2a = 0.4.1) is installed
WITHOUT torch and without its two listening models (~1.1 GB); only the parts that
need neither are used:
  - the sound bank: 252 effects stored as synthesis code (no recorded audio, nothing
    licensed inside), rendered by id, aimed with `dur` / `apex` (a whoosh's loudest
    moment lands within 5 ms of the target), audited model-free on every render; a
    take that fails the audit is re-rolled on a new seed;
  - its mixer maths (earshot.forge.kit): `loud_lufs` (a take's loudest 50 ms,
    K-weighted), `bed_level` (the music's median 50 ms level in the second before a
    cue), `over_bed`; and its offline true-peak limiter (earshot.forge.fx.limit).

Job (JSON):
    {"total": 19.4, "out": "/path/mix.wav",
     "cues": [{"role": "pop", "sound": "ui_pop/soft", "at": 7.43, "align": "onset" | "peak",
               "level_db": -8.0, "bed_db": 8.5, "dur": null, "apex": null}],
     "bed": null | {"path": "/path/bed.wav", "fade_in": 0.3, "fade_out": 1.2},
     "target_lufs": -14.0, "true_peak_db": -1.0}

`at` is where the cue's aligned point (onset or peak) lands on the film.

No bed: effects at their `level_db`, the loudest at the true-peak ceiling. Effects
alone integrate around -20 LUFS; pushing that to a platform target would make every
pop shout.

With a bed (earshot's `launch` kit method, numbers measured on pro launch films): each
effect is set so the mix's loudest 50 ms at it sits `bed_db` over the music just before
it; the whole mix then goes to `target_lufs` and through the limiter at the ceiling.
The report measures what each effect actually landed at over the bed, after limiting.

Prints one JSON object: placements, audit, per-cue level over the bed, the mix's
loudness / true peak / limiter reduction, earshot's version.
"""
from __future__ import annotations

import json
import sys

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

SR = 48000
MAX_REROLLS = 6
BED_REF_LUFS = -20.0         # the bed's working level; only relative levels matter before the final gain
LIMIT_ALLOW_DB = 3.0         # an effect may go this far over the ceiling and lean on the limiter
LIMIT_WARN_DB = 4.0          # more reduction than this on an effect squashes its attack


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


def _bed_level(bed, t):
    from earshot.forge import kit
    try:
        return kit.bed_level(bed, max(t, 0.06))
    except Exception:                        # KitError: less than 50 ms of music before t
        return None


def _load_bed(spec, n):
    import pyloudnorm as pyln
    b, sr = sf.read(spec["path"], always_2d=True)
    if sr != SR:
        raise SystemExit(f"bed must be {SR} Hz (social_video.py converts it), got {sr}")
    b = _stereo(b)[:n]
    if len(b) < n:
        b = np.pad(b, ((0, n - len(b)), (0, 0)))
    lv = pyln.Meter(SR).integrated_loudness(b)
    if np.isfinite(lv):
        b *= 10 ** ((BED_REF_LUFS - lv) / 20)
    fi, fo = int(float(spec.get("fade_in", 0.3)) * SR), int(float(spec.get("fade_out", 1.2)) * SR)
    if fi:
        b[:fi] *= np.linspace(0, 1, fi)[:, None]
    if fo:
        b[-fo:] *= np.linspace(1, 0, fo)[:, None]
    return b


def main(job_path: str) -> int:
    from earshot.forge import fx, kit
    job = json.load(open(job_path, encoding="utf-8"))
    total = float(job["total"])
    ceiling = float(job.get("true_peak_db", -1.0))
    n = int(round(total * SR))
    bed = _load_bed(job["bed"], n) if job.get("bed") else None
    takes, placed, seen = [], [], {}
    for c in job["cues"]:
        i = seen.get(c["role"], 0)
        seen[c["role"]] = i + 1
        y, meta, seed = render_cue(c, i)
        y = _stereo(y)
        anchor = float(meta["peak_s"] if c.get("align") == "peak" else meta["onset_s"])
        start = float(c["at"]) - anchor
        if bed is not None and c.get("bed_db") is not None:
            bl = _bed_level(bed, float(c["at"]))
            g = (bl if bl is not None else BED_REF_LUFS) + kit.over_bed(c["bed_db"]) - kit.loud_lufs(y, SR)
        else:
            g = float(c.get("level_db") or 0.0)
        takes.append((y, int(round(start * SR)), _true_peak_db(y)))
        ck = meta.get("checks") or {}
        placed.append({"role": c["role"], "sound": c["sound"], "at": round(float(c["at"]), 3),
                       "start": round(start, 3), "end": round(start + len(y) / SR, 3),
                       "seed": seed if seed is not None else meta.get("seed"),
                       "gain_db": round(g, 2), "bed_db": c.get("bed_db"),
                       "clean": bool(ck.get("ok", True)),
                       "warnings": [w.get("code") for w in ck.get("warnings") or []]})

    def fx_bus():
        out = np.zeros((n, 2), np.float64)
        for (y, s, _), p in zip(takes, placed):
            a, b = max(0, s), min(n, s + len(y))
            if b > a:
                out[a:b] += y[a - s:b - s] * 10 ** (p["gain_db"] / 20)
        return out

    limited_db = 0.0
    if bed is None:
        fxbus = fx_bus()
        pk = float(np.abs(fxbus).max())
        mix = fxbus * (10 ** (ceiling / 20) / pk if pk > 0 else 1.0)
    else:
        target = float(job.get("target_lufs", -14.0))
        for _ in range(4):
            # a short, spiky take (a 39 ms tick has a 23 dB crest) set by its 50 ms loudness
            # can peak far over the ceiling after the final gain, and a take's peak adds to
            # the music's under it; the limiter would flatten the attack. Measure the mix
            # in each take's window and pull the take down to LIMIT_ALLOW_DB over the ceiling.
            mix = fx_bus() + bed
            lv = _lufs(mix)
            g = (target - lv) if lv is not None else 0.0
            capped = False
            for (y, s, _), p in zip(takes, placed):
                a, b = max(0, s), min(n, s + len(y))
                if b - a < 16:
                    continue
                over = _true_peak_db(mix[a:b]) + g - (ceiling + LIMIT_ALLOW_DB)
                if over > 0.1:
                    p["gain_db"] = round(p["gain_db"] - over, 2)
                    p["capped_db"] = round(p.get("capped_db", 0) + over, 1)
                    capped = True
            if not capped:
                break
        mix = fx_bus() + bed
        lv = _lufs(mix)
        g = (target - lv) if lv is not None else 0.0
        mix *= 10 ** (g / 20)
        bed_final = bed * 10 ** (g / 20)
        # the reduction the limiter makes on the effects (the music's own peaks are mastering)
        limited_db = float(max([0.0] + [_true_peak_db(mix[max(0, s):min(n, s + len(y))]) - ceiling
                                        for y, s, _ in takes if min(n, s + len(y)) - max(0, s) >= 16]))
        mix = fx.limit(mix, ceiling_db=ceiling)
        for p in placed:                      # what each effect landed at over the music, after the limiter
            a, b = max(0, int(p["start"] * SR)), min(n, int(p["end"] * SR))
            bl = _bed_level(bed_final, p["at"])
            if p.get("bed_db") is not None and b - a > 2400 and bl is not None:
                p["over_bed_db"] = round(kit.loud_lufs(mix[a:b], SR) - bl, 1)

    tp = _true_peak_db(mix)
    if tp > ceiling + 0.05:                   # the limiter's safety clip should prevent this
        mix *= 10 ** ((ceiling - tp) / 20)
        tp = _true_peak_db(mix)
    sf.write(job["out"], mix.astype(np.float32), SR, subtype="PCM_24")

    import earshot
    print(json.dumps({
        "out": job["out"], "duration": round(n / SR, 3), "cues": placed,
        "peak_dbfs": round(20 * np.log10(max(float(np.abs(mix).max()), 1e-12)), 2),
        "true_peak_dbtp": round(tp, 2), "lufs_i": _lufs(mix),
        "limiter_max_db": round(limited_db, 1),
        "limiter_warning": bool(limited_db > LIMIT_WARN_DB),
        "bed": bed is not None, "earshot": getattr(earshot, "__version__", "?"),
        "unclean": [p["sound"] for p in placed if not p["clean"]],
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
