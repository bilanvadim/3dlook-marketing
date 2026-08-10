#!/usr/bin/env bash
#
# weekly-posts.sh — простой runner для еженедельного контентного пайплайна.
#
# Вызывает Claude Code в headless mode: запуск slash-command /weekly-posts,
# который внутри прогоняет post-drafter по всем профилям.
#
# Использование:
#   ./weekly-posts.sh           # текущая ISO-неделя
#   ./weekly-posts.sh 17        # неделя 17

set -euo pipefail

WEEK="${1:-$(date +%V)}"
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BOT_DIR="$PROJECT_ROOT/telegram-bot"

cd "$PROJECT_ROOT"

echo "[$(date)] Starting weekly posts pipeline for week $WEEK"

# Запускаем slash-command в headless mode.
# --output-format json для парсинга, --max-turns 50 — лимит на пайплайн,
# --dangerously-skip-permissions потому что это серверный запуск.
claude -p "/weekly-posts $WEEK" \
  --output-format json \
  --max-turns 50 \
  --dangerously-skip-permissions \
  > "/tmp/claude-weekly-posts-$WEEK.json"

echo "[$(date)] Pipeline finished, posting summary to Telegram"

# После того, как пайплайн отработал, найти манифест и пинговать Вадима
WEEK_DIR="$PROJECT_ROOT/workspace/social/$(date +%G)-W${WEEK}"
MANIFEST="$WEEK_DIR/manifest.json"

if [[ ! -f "$MANIFEST" ]]; then
  echo "[ERROR] Manifest not found: $MANIFEST" >&2
  exit 1
fi

# Для каждого драфта — отправить Vадиму уведомление с кнопками
python3 <<EOF
import json, subprocess
from pathlib import Path

manifest = json.loads(Path("$MANIFEST").read_text())
notify = "$BOT_DIR/notify.py"

for draft in manifest["drafts"]:
    if draft["status"] != "draft":
        continue
    artifact_rel = draft["file"]  # e.g. "social/2026-W17/linkedin-company/post-1.md"
    summary = f"Profile: {draft['profile']}\nPost: {draft['post']}\n\nReview required."
    subprocess.run([
        "python3", notify,
        "--track", "social",
        "--artifact", artifact_rel,
        "--summary", summary,
    ], check=True)

print(f"Notified Vadim for {len(manifest['drafts'])} drafts")
EOF

echo "[$(date)] Done"
