#!/usr/bin/env bash
# rollback.sh [profile] [--from DIR|--to COMMIT] [--config] [--queue] [--memory] [--yes]
#
# Two different things get called "rollback", and conflating them is how a bad afternoon becomes
# a bad week:
#
#   CODE     — put the tree back on an earlier commit and re-render. Cheap, reversible, and
#              what you want 95% of the time. This is the DEFAULT.
#   STATE    — restore secrets/config, the conductor queue, or the vector memory from a backup.
#              This OVERWRITES live data, so each part is opt-in: --config / --queue / --memory.
#
# Restoring state is not symmetric with restoring code: putting yesterday's ho.db back discards
# every job that ran since, and putting yesterday's qdrant snapshot back discards everything the
# agent learned since. So nothing here touches state unless you name it.
#
#   rollback.sh                       → previous commit, re-render, restart
#   rollback.sh --to 834197b          → that commit
#   rollback.sh --from <backup> --queue --config
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

PROFILE_ARG=""; FROM=""; TO=""; DO_CONFIG=0; DO_QUEUE=0; DO_MEM=0; YES=0
while [ $# -gt 0 ]; do
  case "$1" in
    --from) FROM="${2:-}"; shift 2;;
    --to) TO="${2:-}"; shift 2;;
    --config) DO_CONFIG=1; shift;;
    --queue) DO_QUEUE=1; shift;;
    --memory) DO_MEM=1; shift;;
    --yes|-y) YES=1; shift;;
    -*) die "unknown option: $1";;
    *) PROFILE_ARG="$1"; shift;;
  esac
done
load_profile "$PROFILE_ARG"
require_own_profile

confirm(){
  [ "$YES" = 1 ] && return 0
  printf '  %s%s%s [type yes to proceed] ' "$_C_Y" "$1" "$_C_0"
  read -r a; [ "$a" = yes ]
}

# ── resolve the backup, if state is being restored ───────────────────────────
if [ "$DO_CONFIG$DO_QUEUE$DO_MEM" != "000" ]; then
  [ -n "$FROM" ] || FROM="$(cat "$HERMES_HOME/backups/.last" 2>/dev/null)"
  [ -n "$FROM" ] && [ -d "$FROM" ] || die "state restore needs a backup: --from DIR (none recorded in $HERMES_HOME/backups/.last)"
  hdr "backup"
  [ -f "$FROM/MANIFEST.txt" ] && sed 's/^/  /' "$FROM/MANIFEST.txt" | head -8 || warn "no MANIFEST.txt in $FROM"
fi

# ── code ─────────────────────────────────────────────────────────────────────
if [ "$DO_CONFIG$DO_QUEUE$DO_MEM" = "000" ] || [ -n "$TO" ]; then
  git -C "$PROFILE_DEST" rev-parse --git-dir >/dev/null 2>&1 || die "$PROFILE_DEST is not a git checkout"
  target="$TO"
  if [ -z "$target" ]; then
    # The previous commit of THIS tree, not of origin: that is what "roll back the update" means.
    target="$(git -C "$PROFILE_DEST" rev-parse HEAD~1 2>/dev/null)" || die "no previous commit to go back to"
  fi
  git -C "$PROFILE_DEST" rev-parse --verify -q "$target" >/dev/null || die "unknown commit: $target"

  hdr "code"
  info "from  $(git_head) $(git -C "$PROFILE_DEST" log -1 --format=%s | cut -c1-50)"
  info "to    $(git -C "$PROFILE_DEST" rev-parse --short "$target") $(git -C "$PROFILE_DEST" log -1 --format=%s "$target" | cut -c1-50)"
  confirm "reset the tree to $(git -C "$PROFILE_DEST" rev-parse --short "$target")?" || die "aborted"

  # Same reasoning as update.sh: reset --hard discards render output (regenerable) and leaves
  # untracked files (conductor/.env, node_modules) alone. No git clean, ever.
  git -C "$PROFILE_DEST" reset -q --hard "$target" || die "reset failed"
  ok "tree at $(git_head)"
  "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$PROFILE_DEST" >/dev/null && ok "re-rendered"

  # Dependencies must match the code we just went back to, or the tests below pass against a
  # node_modules from a different commit.
  if [ -d "$CONDUCTOR_DIR/node_modules" ]; then
    ( cd "$CONDUCTOR_DIR" && npm ci --silent ) && ok "dependencies reinstalled for this commit" \
      || warn "npm ci failed — node_modules may not match this commit"
    ( cd "$CONDUCTOR_DIR" && npx --no-install tsc --noEmit ) && ok "typecheck clean" || bad "typecheck FAILS at this commit"
  fi
fi

# ── config / secrets ─────────────────────────────────────────────────────────
if [ "$DO_CONFIG" = 1 ]; then
  hdr "config + secrets"
  warn "this overwrites the LIVE config and secrets with the backup's copies"
  confirm "restore config/secrets from $FROM?" || die "aborted"
  restore(){ # src-name → dest-path
    [ -f "$FROM/$1" ] || { info "not in backup: $1"; return; }
    cp -p "$FROM/$1" "$2" && chmod 600 "$2" && ok "$1 → $2"
  }
  restore secrets.env            "$SECRETS_FILE"
  restore hermes-.env            "$HERMES_HOME/.env"
  restore hermes-config.yaml     "$HERMES_HOME/config.yaml"
  restore hermes-mem0.json       "$HERMES_HOME/mem0.json"
  restore hermes-SOUL.md         "$HERMES_HOME/SOUL.md"
  restore hermes-auth.json       "$HERMES_HOME/auth.json"
  restore hermes-ai-models.env   "$HERMES_HOME/ai-models.env"
  restore conductor.env          "$CONDUCTOR_DIR/.env"
  [ -d "$FROM/llm-failover-proxy" ] && {
    cp -p "$FROM/llm-failover-proxy/"*.json "$PROFILE_HOME/.config/llm-failover-proxy/" 2>/dev/null \
      && ok "llm-failover-proxy config restored"; }
  # The vault is restored ALONGSIDE, not over: overwriting a knowledge store with an older copy
  # silently deletes whatever was written since, and unlike the queue there is no delta to report.
  if [ -f "$FROM/AI-Second-Brain.tar.gz" ]; then
    aside="$HERMES_HOME/AI-Second-Brain.restored-$(date -u +%Y%m%d-%H%M%S)"
    mkdir -p "$aside" && tar -C "$aside" -xzf "$FROM/AI-Second-Brain.tar.gz" 2>/dev/null \
      && ok "vault extracted to $aside — merge what you need, nothing was overwritten" \
      || warn "could not extract the vault"
  fi
fi

# ── queue ────────────────────────────────────────────────────────────────────
if [ "$DO_QUEUE" = 1 ]; then
  hdr "conductor queue"
  [ -f "$FROM/ho.db" ] || die "no ho.db in $FROM"
  now_jobs="$(sqlite_q "$CONDUCTOR_DB_FILE" 'select count(*) from ho_jobs;')"
  bk_jobs="$(sqlite_q "$FROM/ho.db" 'select count(*) from ho_jobs;')"
  info "live: ${now_jobs:-0} jobs   backup: ${bk_jobs:-0} jobs"
  bad_delta=$(( ${now_jobs:-0} - ${bk_jobs:-0} ))
  [ "$bad_delta" -gt 0 ] && warn "$bad_delta job(s) recorded since the backup will be LOST"
  warn "the conductor must be stopped for this — a live writer and a file swap do not mix"
  confirm "stop the conductor and replace the queue?" || die "aborted"
  sc hermes-conductor stop >/dev/null && ok "conductor stopped"
  # Keep the live one aside: "restore the backup" is itself an action someone may want to undo.
  aside="$CONDUCTOR_DB_FILE.replaced-$(date -u +%Y%m%d-%H%M%S)"
  cp -p "$CONDUCTOR_DB_FILE" "$aside" 2>/dev/null && info "current queue kept at $aside"
  rm -f "$CONDUCTOR_DB_FILE-wal" "$CONDUCTOR_DB_FILE-shm"
  cp -p "$FROM/ho.db" "$CONDUCTOR_DB_FILE" && chmod 600 "$CONDUCTOR_DB_FILE" && ok "queue restored"
  [ "$(sqlite_q "$CONDUCTOR_DB_FILE" 'pragma integrity_check;')" = ok ] && ok "integrity ok" || bad "restored queue fails integrity_check"
  sc hermes-conductor start >/dev/null; sleep 10
  svc_active hermes-conductor && ok "conductor back up" || bad "conductor did not start"
fi

# ── memory ───────────────────────────────────────────────────────────────────
if [ "$DO_MEM" = 1 ]; then
  hdr "mem0 / qdrant"
  [ -f "$FROM/hermes_mem0.snapshot" ] || die "no hermes_mem0.snapshot in $FROM"
  qport="${PROFILE_QDRANT_HTTP_PORT:-}"; [ -n "$qport" ] || die "no qdrant port in this profile"
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
  live_pts="$(curl -s -m 10 -H "api-key: $key" "http://127.0.0.1:$qport/collections/hermes_mem0" 2>/dev/null \
    | python3 -c "import sys,json;print(json.load(sys.stdin).get('result',{}).get('points_count','?'))" 2>/dev/null)"
  info "live collection holds $live_pts point(s)"
  warn "restoring REPLACES the collection — everything learned since the snapshot is gone"
  confirm "restore hermes_mem0 from the snapshot?" || die "aborted"
  out="$(curl -s -m 300 -X POST -H "api-key: $key" \
    -F "snapshot=@$FROM/hermes_mem0.snapshot" \
    "http://127.0.0.1:$qport/collections/hermes_mem0/snapshots/upload?priority=snapshot" 2>&1)"
  if printf '%s' "$out" | grep -q '"status":"ok"'; then
    ok "snapshot uploaded and applied"
    sleep 3
    now="$(curl -s -m 10 -H "api-key: $key" "http://127.0.0.1:$qport/collections/hermes_mem0" 2>/dev/null \
      | python3 -c "import sys,json;r=json.load(sys.stdin).get('result',{});print(r.get('status'),r.get('points_count'))" 2>/dev/null)"
    ok "collection now: $now"
  else
    bad "snapshot restore failed: $(printf '%s' "$out" | head -c 200)"
  fi
fi

hdr "restart"
if [ "$DO_QUEUE" = 0 ]; then
  for u in hermes-conductor hermes-gateway; do
    sc "$u" restart >/dev/null && info "$u restarting"
  done
  sleep 12
  for u in hermes-conductor hermes-gateway; do
    svc_active "$u" && ok "$u active" || bad "$u did not come back"
  done
fi

finish
