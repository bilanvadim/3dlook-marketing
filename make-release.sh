#!/usr/bin/env bash
# =============================================================================
#  make-release.sh — package the deploy kit into a distributable zip.
#
#  Produces dist/ai-agent-bot-<sha>.zip containing everything needed to stand up
#  the bot on a fresh VPS via `./install.sh`. Excludes .git, node_modules,
#  __pycache__, and ANY real secret (*.env except *.example, *.session, *.enc,
#  creds.env, bridge.env, config.yaml, auth.json). Also excludes archive/ and n8n/.
# =============================================================================
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
SHA="$(git rev-parse --short HEAD 2>/dev/null || echo local)"
OUT="$ROOT/dist/ai-agent-bot-$SHA.zip"
STAGE="$(mktemp -d)"; K="$STAGE/ai-agent-bot"
mkdir -p "$K" "$ROOT/dist"

# stage the kit
cp -r "$ROOT/agents-ai" "$K/"
for f in install.sh bootstrap-vps.sh secrets.env.example REPRODUCE.md README.md; do
  [ -e "$ROOT/$f" ] && cp "$ROOT/$f" "$K/"
done

# prune junk + ANY real secret that may exist on disk (untracked/ignored files)
find "$K" -type d \( -name .git -o -name __pycache__ -o -name node_modules -o -name venv \) -prune -exec rm -rf {} + 2>/dev/null || true
find "$K" -type f \( -name '*.pyc' -o -name '*.session' -o -name '*.session-journal' \
  -o -name '*.enc' -o -name creds.env -o -name bridge.env -o -name auth.json \
  -o -name config.yaml -o -name qr.png \) -delete 2>/dev/null || true
find "$K" -type f -name '*.env' ! -name '*.env.example' -delete 2>/dev/null || true
chmod +x "$K/install.sh" "$K/bootstrap-vps.sh" 2>/dev/null || true

# safety: refuse to ship if any secret-looking file slipped through
LEAK="$(find "$K" -type f \( -name '*.session' -o -name '*.enc' -o -name creds.env -o -name '.env' -o -name config.yaml -o -name auth.json \) 2>/dev/null)"
[ -n "$LEAK" ] && { echo "REFUSING TO PACKAGE — secret file present:"; echo "$LEAK"; exit 1; }

# build the zip (python zipfile — no dependency on the `zip` binary)
rm -f "$OUT"
python3 - "$STAGE" "$OUT" <<'PY'
import os,sys,zipfile
stage,out=sys.argv[1],sys.argv[2]
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for root,_,files in os.walk(stage):
        for fn in files:
            p=os.path.join(root,fn)
            z.write(p, os.path.relpath(p,stage))
PY
rm -rf "$STAGE"

N=$(python3 -c "import zipfile,sys;print(len(zipfile.ZipFile(sys.argv[1]).namelist()))" "$OUT")
SZ=$(du -h "$OUT" | cut -f1)
SUM=$(sha256sum "$OUT" | cut -d' ' -f1)
echo "✔ built: $OUT"
echo "  files: $N   size: $SZ"
echo "  sha256: $SUM"
echo
echo "Deploy on a fresh VPS:"
echo "  unzip ai-agent-bot-$SHA.zip && cd ai-agent-bot"
echo "  cp secrets.env.example secrets.env && nano secrets.env   # fill bot token + keys"
echo "  ./install.sh"
