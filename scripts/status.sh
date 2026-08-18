#!/usr/bin/env bash
# status.sh [profile] — what is actually running, in one screen. Read-only.
#
# Answers the questions you ask first when something looks wrong: which commit is deployed,
# is every service up, are the ports the ones this profile was assigned, and is the queue
# moving. It reports; doctor.sh judges.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_profile "${1:-}"

hdr "profile"
info "name        $PROFILE_NAME  (owner ${PROFILE_OWNER:-?})"
info "tree        $PROFILE_DEST"
info "runtime     $HERMES_HOME"

hdr "version"
if git -C "$PROFILE_DEST" rev-parse --git-dir >/dev/null 2>&1; then
  info "commit      $(git_head) $(git -C "$PROFILE_DEST" log -1 --format=%s | cut -c1-58)"
  info "branch      $(git -C "$PROFILE_DEST" rev-parse --abbrev-ref HEAD 2>/dev/null)"
  local_mods="$(git -C "$PROFILE_DEST" status --porcelain 2>/dev/null | wc -l)"
  # Local modifications are EXPECTED here: render.sh rewrites tracked files with this
  # profile's paths. diff.sh is what tells those apart from real drift.
  info "local mods  $local_mods (render output + any drift — see diff.sh)"
  [ -f "$REPO_ROOT/VERSION" ] && info "VERSION     $(cat "$REPO_ROOT/VERSION")"
else
  warn "tree is NOT a git checkout — no update path (see deploy.sh)"
fi

hdr "services"
for u in "${ALL_SERVICES[@]}"; do
  st="$(sc "$u" is-active)"; en="$(sc "$u" is-enabled)"
  line="$(printf '%-28s %-9s %-9s scope=%s' "$u" "$st" "$en" "$(unit_scope "$u")")"
  case "$st" in
    active) ok "$line";;
    inactive|failed) bad "$line";;
    *) warn "$line";;
  esac
done

hdr "ports (assigned by this profile)"
for pair in \
  "conductor webhook:$PROFILE_HO_WEBHOOK_PORT" \
  "qdrant http:${PROFILE_QDRANT_HTTP_PORT:-}" \
  "qdrant grpc:${PROFILE_QDRANT_GRPC_PORT:-}" \
  "proxy agentic:${PROFILE_PROXY_AGENTIC_PORT:-}" \
  "proxy strong:${PROFILE_PROXY_STRONG_PORT:-}"; do
  name="${pair%%:*}"; port="${pair##*:}"
  [ -n "$port" ] || continue
  if port_listening "$port"; then ok "$(printf '%-18s %s listening' "$name" "$port")"
  else bad "$(printf '%-18s %s NOT listening' "$name" "$port")"; fi
done

hdr "conductor queue"
if [ -f "$CONDUCTOR_DB_FILE" ]; then
  info "db          $CONDUCTOR_DB_FILE"
  counts="$(sqlite_q "$CONDUCTOR_DB_FILE" "select group_concat(status||'='||n, '  ') from (select status, count(*) n from ho_jobs group by status);")"
  info "jobs        ${counts:-<empty>}"
  info "runs        $(sqlite_q "$CONDUCTOR_DB_FILE" 'select count(*) from ho_runs;')"
  openesc="$(sqlite_q "$CONDUCTOR_DB_FILE" "select count(*) from ho_escalations where status='open';")"
  if [ "${openesc:-0}" -gt 0 ]; then warn "escalations $openesc awaiting a human decision"
  else info "escalations none open"; fi
  last="$(sqlite_q "$CONDUCTOR_DB_FILE" 'select coalesce(max(ended_at), "never") from ho_runs;')"
  info "last run    $last"
else
  bad "conductor db missing: $CONDUCTOR_DB_FILE"
fi

hdr "memory (mem0)"
qport="${PROFILE_QDRANT_HTTP_PORT:-}"
if [ -n "$qport" ] && [ -f "$HERMES_HOME/mem0.json" ]; then
  key="$(python3 - "$HERMES_HOME/mem0.json" <<'PY' 2>/dev/null
import json,sys
def find(o):
    if isinstance(o,dict):
        if o.get('provider')=='qdrant' and 'config' in o: return o['config']
        for v in o.values():
            r=find(v)
            if r: return r
    return None
print((find(json.load(open(sys.argv[1]))) or {}).get('api_key',''))
PY
)"
  body="$(curl -s -m 5 -H "api-key: $key" "http://127.0.0.1:$qport/collections/hermes_mem0" 2>/dev/null)"
  pts="$(printf '%s' "$body" | python3 -c "import sys,json;r=json.load(sys.stdin).get('result',{});print(r.get('status','?'),r.get('points_count','?'))" 2>/dev/null)"
  if [ -n "$pts" ]; then ok "hermes_mem0  $pts (status points)"; else warn "could not read hermes_mem0 on :$qport"; fi
else
  info "no mem0.json / qdrant port in this profile — skipped"
fi

finish
