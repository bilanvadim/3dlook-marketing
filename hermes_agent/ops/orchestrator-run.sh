#!/usr/bin/env bash
# orchestrator-run.sh — start the Hermes Orchestrator orchestrator worker.
# State is SQLite/libSQL (no Postgres, no docker dependency). Used as ExecStart of
# hermes-orchestrator.service; also runnable by hand.
#
# Portable: paths come from env with defaults derived from this script's location.
#   HERMES_REPO_ROOT  repo checkout root  (default: auto from script path)
#   ORCHESTRATOR_DIR     orchestrator app dir   (default: $HERMES_REPO_ROOT/claude_code/DEV/full_stack_sm/orchestrator)
#   HO_STATE_DIR      dir for the SQLite file  (default: $HOME/.hermes)
#   DATABASE_URL      libSQL URL           (default: file:$HO_STATE_DIR/ho.db;
#                                           set libsql://…/Turso for a networked DB)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"   # hermes_agent/ops -> repo root

HERMES_REPO_ROOT="${HERMES_REPO_ROOT:-$DEFAULT_ROOT}"
ORCHESTRATOR_DIR="${ORCHESTRATOR_DIR:-$HERMES_REPO_ROOT/claude_code/DEV/full_stack_sm/orchestrator}"
HO_STATE_DIR="${HO_STATE_DIR:-$HOME/.hermes}"

[ -d "$ORCHESTRATOR_DIR" ] || { echo "orchestrator-run: ORCHESTRATOR_DIR not found: $ORCHESTRATOR_DIR" >&2; exit 1; }
mkdir -p "$HO_STATE_DIR"
cd "$ORCHESTRATOR_DIR"

export DATABASE_URL="${DATABASE_URL:-file:$HO_STATE_DIR/ho.db}"

# For a local file DB, ensure the schema exists (idempotent; create tables if missing).
case "$DATABASE_URL" in
  file:*)
    dbfile="${DATABASE_URL#file:}"
    if command -v sqlite3 >/dev/null 2>&1; then
      sqlite3 "$dbfile" < "$ORCHESTRATOR_DIR/sql/schema.sql" || true
    fi
    echo "orchestrator-run: DATABASE_URL → file:$dbfile"
    ;;
  *)
    echo "orchestrator-run: DATABASE_URL → ${DATABASE_URL%%\?*} (networked libSQL/Turso)"
    ;;
esac

exec /usr/bin/npm start
