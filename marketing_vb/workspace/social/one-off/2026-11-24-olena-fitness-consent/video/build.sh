#!/usr/bin/env bash
# Rebuild the one-off video: copy composition + real product imagery into a build dir
# outside the repo (Satoshi resolves via local()), lint the layout, render 4:5.
# Usage: bash build.sh [draft|looks|delivery]   (default: delivery)
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
MVB="$(cd "$HERE/../../../../.." && pwd)"                 # …/marketing_vb
OUT="${XDG_CACHE_HOME:-$HOME/.cache}/mvb-social-video/oneoff-2026-11-24-olena-fitness-consent/feed"
Q="${1:-delivery}"
mkdir -p "$OUT/assets"
cp "$HERE/composition/index.html" "$OUT/index.html"
cp \
   "$MVB/brand-assets/product-imagery/fitxpress/capture-person-and-phone.webp" \
   "$MVB/brand-assets/video/3dlook-logo-white.svg" "$OUT/assets/"
export HYPERFRAMES_NO_TELEMETRY=1 NPM_CONFIG_UPDATE_NOTIFIER=false NO_UPDATE_NOTIFIER=1
cd "$OUT"
npx --yes hyperframes@0.9.1 check --json > check.json || { cat check.json; exit 1; }
npx --yes hyperframes@0.9.1 render --quality "$Q" -o out.mp4
PRIV="${MVB_PRIVATE_REPO:-$HOME/3dlook-marketing-private}/social-video/2026-11-24-olena-fitness-consent"
mkdir -p "$PRIV"
cp out.mp4 "$PRIV/2026-11-24-olena-fitness-consent-feed.mp4"
ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 "$PRIV/2026-11-24-olena-fitness-consent-feed.mp4"
