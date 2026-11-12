#!/usr/bin/env bash
# OpenMontage (OpenMontageInc/OpenMontage, AGPLv3) as a one-off video studio on this VPS.
# Reviewed 2026-11-12 (Vadim: «перевір та встанови що корисно для монтажа відео»).
#
#   bash marketing_vb/docs/vendor/openmontage/setup.sh      # idempotent; safe to re-run
#   cd ~/OpenMontage && claude                              # then describe the video
#
# What it does NOT install, on purpose:
#   - Remotion (remotion-composer/node_modules): 3DLOOK has more than 3 employees, so Remotion needs a paid
#     Company License. OpenMontage falls back to HyperFrames / FFmpeg (captions: `ffmpeg_fallback`).
#   - torch / transformers / GPU extras, and any paid-provider API keys (.env stays empty).
# The local rules live next to this script (CLAUDE.local.md) and are symlinked into the checkout.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DEST="${OPENMONTAGE_DIR:-$HOME/OpenMontage}"

if [ ! -d "$DEST/.git" ]; then
  GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/OpenMontageInc/OpenMontage.git "$DEST"
fi
cd "$DEST"

[ -x .venv/bin/python ] || python3 -m venv .venv
PY=.venv/bin/python
"$PY" -m pip install -q 'pip>=26.2.2'
"$PY" -m pip install -q -r requirements.txt
# Local, keyless tools: TTS, transcription, downloader, audio analysis, face tracking / auto-reframe.
# av<17: faster-whisper 1.2.1 passes metadata_errors= to av.open(), which PyAV 19 removed.
"$PY" -m pip install -q piper-tts faster-whisper yt-dlp librosa soundfile scipy opencv-python-headless mediapipe 'av<17'

# Piper voice used by the free narration path
[ -f "$HOME/.piper/models/en_US-lessac-medium.onnx" ] || \
  "$PY" -m piper.download_voices --download-dir "$HOME/.piper/models" en_US-lessac-medium

# Empty .env (no keys); HyperFrames CLI warm-up (telemetry is off via HYPERFRAMES_NO_TELEMETRY in ~/.claude/settings.json)
[ -f .env ] || cp .env.example .env
HYPERFRAMES_NO_TELEMETRY=1 npx --yes hyperframes --version >/dev/null

# Local rules: symlink so the repo copy stays the single source of truth; keep it out of OpenMontage's git
ln -sfn "$HERE/CLAUDE.local.md" CLAUDE.local.md
grep -qxF 'CLAUDE.local.md' .git/info/exclude || echo 'CLAUDE.local.md' >> .git/info/exclude

echo "OpenMontage ready at $DEST (Remotion intentionally absent). Start with: cd $DEST && claude"
