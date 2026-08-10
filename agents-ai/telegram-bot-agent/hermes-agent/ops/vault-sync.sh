#!/usr/bin/env bash
# Auto-sync the AI Second Brain vault to git. The vault now lives INSIDE the
# ai-agents-config repo on the single `main` branch, at agents-ai/telegram-bot-agent/hermes-agent/AI-Second-Brain.
# Commits ONLY that subfolder, so unrelated repo changes are untouched. $0 cost.
set -uo pipefail

REPO="/srv/sergiy_prod/ai-agents-config"
SUBDIR="agents-ai/telegram-bot-agent/hermes-agent/AI-Second-Brain"
BRANCH="main"
cd "$REPO" 2>/dev/null || { echo "repo not found: $REPO" >&2; exit 1; }
[ -d .git ] || { echo "not a git repo: $REPO" >&2; exit 1; }

git pull --rebase --autostash -q origin "$BRANCH" 2>/dev/null || true
git add "$SUBDIR"
if git diff --cached --quiet -- "$SUBDIR"; then
  exit 0   # vault unchanged
fi
git commit -q -m "vault sync $(date '+%Y-%m-%d %H:%M')" -- "$SUBDIR" || exit 0
git push -q origin "$BRANCH" 2>/dev/null || echo "push failed (will retry next run)" >&2
