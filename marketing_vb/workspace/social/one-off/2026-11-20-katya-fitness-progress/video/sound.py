#!/usr/bin/env python3
"""One-off sound pass for the Katya video: the house sound rules (scripts/social_video.py
sound_cues + pick_bed + beat_fit, earshot mix via social_sound.py) mapped onto this
composition's own scene times. Writes <private>/social-video/<SLUG>/<SLUG>-feed-sound.mp4.
Usage: python3 sound.py   (after build.sh; reads the silent MP4 from the private dir)"""
import json, os, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MVB = HERE.parents[4]
sys.path.insert(0, str(MVB / "scripts"))
import social_video as sv  # noqa: E402

SLUG = "2026-11-20-katya-fitness-progress"
OUTDIR = sv.PRIVATE_ROOT / sv.PRIVATE_VIDEO / SLUG
SILENT = OUTDIR / f"{SLUG}-feed.mp4"
DST = OUTDIR / f"{SLUG}-feed-sound.mp4"
TOTAL = 22.0
# composition/index.html scene starts: s1 0 · s2 3.6 · s3 8.4 · s4 13.6 · s5 18.4
T = {"total": TOTAL,
     "hook": {"start": 0.18},                       # land = +0.32 → 0.5, the squiggle draws
     "stat": {"start": 3.6},                        # whoosh into the scale, tick as the line draws
     "points": {"items": [9.4, 9.85, 10.3, 15.3, 15.72, 16.14]},   # 3 bars, 3 chips
     "close": {"start": 18.4}}                      # whoosh + ding on the CTA (19.2)
cues = sv.sound_cues(T, "music")
pal = sv.SOUND_PALETTES["music"]
for at in (8.4 + 0.15, 13.6 + 0.15):                # whoosh into the measured card and the product
    sid, align, level, offset, bed_db = pal["whoosh"]
    cues.append({"role": "whoosh", "sound": sid, "align": align, "level_db": level, "bed_db": bed_db,
                 "at": round(at + offset, 3), **sv.WHOOSH_SHAPE})
cues.sort(key=lambda c: c["at"])

work = sv.BUILD_ROOT / f"oneoff-{SLUG}" / "sound"
work.mkdir(parents=True, exist_ok=True)
got = sv.pick_bed(SLUG)
if not got:
    sys.exit("no music library")
bed, lic, grid = got
fit = sv.beat_fit(grid, cues, TOTAL) if grid else {}
start = fit.get("start_s", 0.0)
wav = work / "bed.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(start), "-i", bed, "-t", str(TOTAL),
                "-ar", "48000", "-ac", "2", str(wav)], check=True)
job = {"total": TOTAL, "out": str(work / "mix.wav"), "cues": cues,
       "bed": {"path": str(wav), "fade_in": 0.3, "fade_out": 1.2},
       "target_lufs": -14.0, "true_peak_db": -1.0}
(work / "job.json").write_text(json.dumps(job, indent=2))
r = subprocess.run([sv.EARSHOT_PY, "-I", sv.SOUND_SCRIPT, str(work / "job.json")], capture_output=True,
                   text=True, timeout=600, env=dict(os.environ, EARSHOT_OFFLINE="1", HF_HUB_OFFLINE="1"))
mix = sv._json_tail(r.stdout)
if r.returncode or not mix:
    sys.exit("mix failed: " + (r.stdout + r.stderr)[-1500:])
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(SILENT), "-i", job["out"], "-map", "0:v:0",
                "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                "-t", str(TOTAL), "-movflags", "+faststart", str(DST)], check=True)
meta = {"bed": {**lic, "file": os.path.basename(bed), "start_s": start, "beat_fit": fit or None},
        "mix": {k: mix.get(k) for k in ("peak_dbfs", "true_peak_dbtp", "lufs_i", "limiter_max_db")},
        "cues": len(cues), "file": DST.name}
(HERE / "sound.json").write_text(json.dumps(meta, indent=2) + "\n")
print(json.dumps(meta, indent=2))
