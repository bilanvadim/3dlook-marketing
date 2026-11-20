#!/usr/bin/env bash
# Metric (kg / cm / kcal) version of the 2026-11-19 Nick visual, for linkedin-vadim (AU), 2026-11-20.
# Rebuilds both from Hlib's original banner in the Nick folder.
# Needs: python3 + Pillow + numpy, google-chrome (renders the logo SVG), network once for the Jost font.
set -euo pipefail
cd "$(dirname "$0")"
OUT=..; OUT_ABS=$(cd .. && pwd); TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
export JOST_TTF=${JOST_TTF:-$TMP/Jost-var.ttf}
[ -f "$JOST_TTF" ] || curl -sL -o "$JOST_TTF" "https://github.com/google/fonts/raw/main/ofl/jost/Jost%5Bwght%5D.ttf"
LOGO=../../../../../../brand-assets/logos/3dlook-logo-white.svg
printf '<html><body style="margin:0;background:transparent">%s</body></html>' \
  "$(sed 's/width="248" height="36"/width="1240" height="180"/' "$LOGO")" > "$TMP/logo.html"
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --default-background-color=00000000 \
  --window-size=1240,180 --screenshot="$TMP/logo_big.png" "file://$TMP/logo.html" 2>/dev/null
python3 -I clean.py "../../../2026-11-19-nick-fitness-retention/visual/original-hlib-1800x942.png" "$TMP/base_clean.png"
(cd "$TMP" && python3 -I "$OLDPWD/compose.py" "$TMP/fixed.png")
cp "$TMP/fixed.png" "$OUT/fitxpress-post-metric-1800x942.png"
(cd "$TMP" && python3 -I "$OLDPWD/compose45.py" "$OUT_ABS/fitxpress-post-4x5-metric-1080x1350.png" "$TMP/fixed.png")
