#!/usr/bin/env bash
# conductor-run.sh — start the Hermes conductor worker.
# Resolves the supabase-db Postgres IP + password FRESH at each start so the
# service survives container IP changes and keeps no secret on disk.
# Used as ExecStart of hermes-conductor.service; also runnable by hand.
set -euo pipefail

CONDUCTOR_DIR=/srv/sergiy_prod/ai-agents-config/claude_code/DEV/full_stack_sm/conductor
STACK_ENV=/srv/sergiy_prod/dev-home-archive/infra/stacks/supabase/.env
PG_CONTAINER=supabase-db
PG_NETWORK=supabase_default

cd "$CONDUCTOR_DIR"

ip=$(docker inspect -f "{{.NetworkSettings.Networks.${PG_NETWORK}.IPAddress}}" "$PG_CONTAINER" 2>/dev/null || true)
[ -n "$ip" ] || { echo "conductor-run: cannot resolve ${PG_CONTAINER} IP on ${PG_NETWORK}" >&2; exit 1; }

pw=$(grep -hE '^POSTGRES_PASSWORD=' "$STACK_ENV" | sed -E 's/^POSTGRES_PASSWORD=//')
[ -n "$pw" ] || { echo "conductor-run: POSTGRES_PASSWORD not found in $STACK_ENV" >&2; exit 1; }
enc=$(PW="$pw" python3 -c 'import urllib.parse,os;print(urllib.parse.quote(os.environ["PW"],safe=""))')

export DATABASE_URL="postgresql://postgres:${enc}@${ip}:5432/postgres"
echo "conductor-run: DATABASE_URL → postgres:***@${ip}:5432/postgres"
exec /usr/bin/npm start
