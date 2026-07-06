#!/usr/bin/env bash
# conductor-run.sh — start the Hermes conductor worker.
# Resolves the Postgres (Supabase) IP + password FRESH at each start so the
# service survives container IP changes and keeps no secret on disk.
# Used as ExecStart of hermes-conductor.service; also runnable by hand.
#
# Portable: machine-specific paths come from env vars with sane defaults derived
# from this script's location. Set these in the conductor .env or the systemd
# unit's Environment= (see hermes_agent/INSTALL.md):
#
#   HERMES_REPO_ROOT  repo checkout root  (default: auto from script path)
#   CONDUCTOR_DIR     conductor app dir   (default: $HERMES_REPO_ROOT/claude_code/DEV/full_stack_sm/conductor)
#   STACK_ENV         path to Supabase stack .env holding POSTGRES_PASSWORD  (REQUIRED unless DATABASE_URL set)
#   PG_CONTAINER      Postgres docker container name  (default: supabase-db)
#   PG_NETWORK        docker network name             (default: supabase_default)
#   DATABASE_URL      if set, used as-is and IP/password resolution is skipped
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"   # hermes_agent/ops -> repo root

HERMES_REPO_ROOT="${HERMES_REPO_ROOT:-$DEFAULT_ROOT}"
CONDUCTOR_DIR="${CONDUCTOR_DIR:-$HERMES_REPO_ROOT/claude_code/DEV/full_stack_sm/conductor}"
PG_CONTAINER="${PG_CONTAINER:-supabase-db}"
PG_NETWORK="${PG_NETWORK:-supabase_default}"

[ -d "$CONDUCTOR_DIR" ] || { echo "conductor-run: CONDUCTOR_DIR not found: $CONDUCTOR_DIR" >&2; exit 1; }
cd "$CONDUCTOR_DIR"

if [ -z "${DATABASE_URL:-}" ]; then
  : "${STACK_ENV:?conductor-run: set STACK_ENV to the Supabase stack .env (holds POSTGRES_PASSWORD), or export DATABASE_URL directly}"
  ip=$(docker inspect -f "{{.NetworkSettings.Networks.${PG_NETWORK}.IPAddress}}" "$PG_CONTAINER" 2>/dev/null || true)
  [ -n "$ip" ] || { echo "conductor-run: cannot resolve ${PG_CONTAINER} IP on ${PG_NETWORK}" >&2; exit 1; }
  pw=$(grep -hE '^POSTGRES_PASSWORD=' "$STACK_ENV" | sed -E 's/^POSTGRES_PASSWORD=//')
  [ -n "$pw" ] || { echo "conductor-run: POSTGRES_PASSWORD not found in $STACK_ENV" >&2; exit 1; }
  enc=$(PW="$pw" python3 -c 'import urllib.parse,os;print(urllib.parse.quote(os.environ["PW"],safe=""))')
  export DATABASE_URL="postgresql://postgres:${enc}@${ip}:5432/postgres"
  echo "conductor-run: DATABASE_URL → postgres:***@${ip}:5432/postgres"
else
  echo "conductor-run: using preset DATABASE_URL"
fi

exec /usr/bin/npm start
