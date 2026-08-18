#!/usr/bin/env bash
# Auto-sync the AI Second Brain vault to git. The vault now lives INSIDE the
# ai-agents-config repo on the single `main` branch, at agents-ai/telegram-bot-agent/hermes-agent/AI-Second-Brain.
# Commits ONLY that subfolder, so unrelated repo changes are untouched. $0 cost.
set -uo pipefail

REPO="@DEST@"
SUBDIR="agents-ai/telegram-bot-agent/hermes-agent/AI-Second-Brain"
BRANCH="main"
cd "$REPO" 2>/dev/null || { echo "repo not found: $REPO" >&2; exit 1; }
[ -d .git ] || { echo "not a git repo: $REPO" >&2; exit 1; }

# NO PULL HERE. It used to run `git pull --rebase --autostash`, and on a rendered tree that is a
# wrecking ball: the ~30 files carrying this profile's paths are RENDER OUTPUT, autostash treats
# them as user work, and reapplying them over a pulled template leaves CONFLICT MARKERS in the
# working tree. That is not theoretical — it happened on vadim_prod, where every profiles/*.json
# ended up with "<<<<<<< Updated upstream" and stopped being valid JSON, so Claude Code resolved no
# plugin marketplaces at all. The timer fires every 30 minutes, so it was a 48-times-a-day fuse.
#
# Pulling was never needed for this script's job either: it PUSHES a subdirectory. If the push is
# rejected because origin moved, the next run retries — after scripts/update.sh has pulled properly,
# with a reset and a re-render.
#
# And a runtime replica must not commit at all. This script is the one legitimate exception (the
# vault is content produced at run time, not render output), so it says so explicitly rather than
# quietly bypassing the guard.
if [ -f .git/hooks/pre-commit ] && grep -q 'runtime replica' .git/hooks/pre-commit 2>/dev/null; then
  echo "vault-sync: $REPO is a runtime replica — the vault cannot be pushed from here." >&2
  echo "vault-sync: the vault is runtime CONTENT living inside a template repo, which is the real" >&2
  echo "vault-sync: problem; it belongs outside the tree, like ~/.hermes/ho.db. Not syncing." >&2
  exit 0
fi
git add "$SUBDIR"
if git diff --cached --quiet -- "$SUBDIR"; then
  exit 0   # vault unchanged
fi
git commit -q -m "vault sync $(date '+%Y-%m-%d %H:%M')" -- "$SUBDIR" || exit 0
git push -q origin "$BRANCH" 2>/dev/null || echo "push failed (will retry next run)" >&2
