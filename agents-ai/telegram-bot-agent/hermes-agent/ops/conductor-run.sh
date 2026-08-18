#!/usr/bin/env bash
# conductor-run.sh — start the Hermes Orchestrator conductor worker.
# State is SQLite/libSQL (no Postgres, no docker dependency). Used as ExecStart of
# hermes-conductor.service; also runnable by hand.
#
# Portable: paths come from env with defaults derived from this script's location.
#   HERMES_REPO_ROOT  repo checkout root  (default: auto from script path)
#   CONDUCTOR_DIR     conductor app dir   (default: $HERMES_REPO_ROOT/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor)
#   HO_STATE_DIR      dir for the SQLite file  (default: $HOME/.hermes)
#   DATABASE_URL      libSQL URL           (default: file:$HO_STATE_DIR/ho.db;
#                                           set libsql://…/Turso for a networked DB)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"   # …/agents-ai/telegram-bot-agent/hermes-agent/ops -> repo root (4 up)

HERMES_REPO_ROOT="${HERMES_REPO_ROOT:-$DEFAULT_ROOT}"
CONDUCTOR_DIR="${CONDUCTOR_DIR:-$HERMES_REPO_ROOT/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor}"
HO_STATE_DIR="${HO_STATE_DIR:-$HOME/.hermes}"

[ -d "$CONDUCTOR_DIR" ] || { echo "conductor-run: CONDUCTOR_DIR not found: $CONDUCTOR_DIR" >&2; exit 1; }
mkdir -p "$HO_STATE_DIR"
cd "$CONDUCTOR_DIR"

export DATABASE_URL="${DATABASE_URL:-file:$HO_STATE_DIR/ho.db}"
# Run several conductor workers so multiple A→Z projects (Dev/SEO/…) run in parallel,
# not one-at-a-time. Each claims jobs atomically; a heartbeat keeps live jobs from being
# stale-recovered. Tune per box resources (each worker = one Claude Agent SDK session).
export CONDUCTOR_WORKERS="${CONDUCTOR_WORKERS:-3}"

# For a local file DB, ensure the schema exists (idempotent; create tables if missing).
case "$DATABASE_URL" in
  file:*)
    dbfile="${DATABASE_URL#file:}"
    if command -v sqlite3 >/dev/null 2>&1; then
      sqlite3 "$dbfile" < "$CONDUCTOR_DIR/sql/schema.sql" || true
    fi
    echo "conductor-run: DATABASE_URL → file:$dbfile"
    ;;
  *)
    echo "conductor-run: DATABASE_URL → ${DATABASE_URL%%\?*} (networked libSQL/Turso)"
    ;;
esac

exec /usr/bin/npm start
