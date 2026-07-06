#!/usr/bin/env bash
# Auto-sync the AI Second Brain vault to git. The vault now lives INSIDE the
# ai-agents-config repo on the single `main` branch, at hermes_agent/AI-Second-Brain.
# Commits ONLY that subfolder, so unrelated repo changes are untouched. $0 cost.
set -uo pipefail

# Portable: REPO defaults to the checkout root inferred from this script's path
# (hermes_agent/ops/vault-sync.sh -> repo root). Override with $VAULT_REPO.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${VAULT_REPO:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
SUBDIR="hermes_agent/AI-Second-Brain"
BRANCH="${VAULT_BRANCH:-main}"
cd "$REPO" 2>/dev/null || { echo "repo not found: $REPO" >&2; exit 1; }
[ -d .git ] || { echo "not a git repo: $REPO" >&2; exit 1; }

git pull --rebase --autostash -q origin "$BRANCH" 2>/dev/null || true
git add "$SUBDIR"
if git diff --cached --quiet -- "$SUBDIR"; then
  exit 0   # vault unchanged
fi
git commit -q -m "vault sync $(date '+%Y-%m-%d %H:%M')" -- "$SUBDIR" || exit 0
git push -q origin "$BRANCH" 2>/dev/null || echo "push failed (will retry next run)" >&2
