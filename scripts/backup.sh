#!/usr/bin/env bash
# backup.sh [profile] [--label TEXT] — snapshot everything that is NOT in git.
#
# Git already has the config. What git does NOT have is the entire reason a restore is hard:
# the secrets, the live Hermes config, the conductor queue with its job history, the systemd
# unit files (including drop-ins, which is where the deployment paths actually live), and the
# vector memory. Those are what this captures.
#
# Writes ~/.hermes/backups/<stamp>[-label]/ and prints the path. update.sh calls it before
# touching anything, and rollback.sh restores from it.
#
# SECRETS ARE INCLUDED, so the archive is created 0700/0600 and never leaves the account. It is
# not encrypted — encrypting to a key stored on the same box buys nothing. Do not copy it off
# the machine without encrypting it there and then.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_profile "${1:-}"
require_own_profile

LABEL=""
case "${2:-}" in --label) LABEL="-${3:-}";; esac
STAMP="$(date -u +%Y%m%d-%H%M%S)"
DEST="$HERMES_HOME/backups/$STAMP$LABEL"

mkdir -p "$DEST" || die "cannot create $DEST"
chmod 700 "$DEST"
umask 077

hdr "backup → $DEST"

# ── 1. the conductor queue ───────────────────────────────────────────────────
# `.backup` rather than cp: a live conductor is writing, and copying a SQLite file mid-write
# yields a torn database whose WAL you no longer have. This takes a consistent snapshot with
# the writers running.
if [ -f "$CONDUCTOR_DB_FILE" ]; then
  if sqlite3 "$CONDUCTOR_DB_FILE" ".backup '$DEST/ho.db'" 2>/dev/null; then
    jobs="$(sqlite_q "$DEST/ho.db" 'select count(*) from ho_jobs;')"
    runs="$(sqlite_q "$DEST/ho.db" 'select count(*) from ho_runs;')"
    integrity="$(sqlite_q "$DEST/ho.db" 'pragma integrity_check;')"
    if [ "$integrity" = ok ]; then ok "ho.db  $jobs jobs / $runs runs (integrity ok)"
    else bad "ho.db snapshot failed integrity_check: $integrity"; fi
  else
    bad "could not snapshot $CONDUCTOR_DB_FILE"
  fi
else
  warn "no conductor db at $CONDUCTOR_DB_FILE"
fi

# ── 2. secrets and live config ───────────────────────────────────────────────
hdr "config + secrets"
copied=0
for f in "$SECRETS_FILE" "$HERMES_HOME/.env" "$HERMES_HOME/config.yaml" "$HERMES_HOME/mem0.json" \
         "$HERMES_HOME/SOUL.md" "$HERMES_HOME/auth.json" "$HERMES_HOME/ai-models.env" \
         "$CONDUCTOR_DIR/.env"; do
  [ -f "$f" ] || continue
  # Flatten with a name that says where it came from, so a restore cannot put it back wrong.
  case "$f" in
    "$CONDUCTOR_DIR/.env") name="conductor.env";;
    "$SECRETS_FILE")       name="secrets.env";;
    *)                     name="hermes-$(basename "$f")";;
  esac
  cp -p "$f" "$DEST/$name" && { chmod 600 "$DEST/$name"; copied=$((copied+1)); }
done
ok "$copied config/secret file(s)"
[ -d "$PROFILE_HOME/.config/llm-failover-proxy" ] && {
  mkdir -p "$DEST/llm-failover-proxy"
  cp -p "$PROFILE_HOME/.config/llm-failover-proxy/"*.json "$DEST/llm-failover-proxy/" 2>/dev/null
  chmod 600 "$DEST/llm-failover-proxy/"* 2>/dev/null
  ok "llm-failover-proxy config(s)"
}

# ── 3. unit files, INCLUDING drop-ins ────────────────────────────────────────
# The drop-ins matter more than the units: that is where a deployment's real paths live
# (WorkingDirectory, CONDUCTOR_DIR, DATABASE_URL). A backup without them restores a system
# that points somewhere else.
hdr "systemd"
mkdir -p "$DEST/systemd/user" "$DEST/systemd/system"
n=0
for u in "${ALL_SERVICES[@]}" hermes-conductor-guard; do
  for src in "$PROFILE_HOME/.config/systemd/user/$u.service" "$PROFILE_HOME/.config/systemd/user/$u.timer"; do
    [ -f "$src" ] && { cp -p "$src" "$DEST/systemd/user/"; n=$((n+1)); }
  done
  [ -d "$PROFILE_HOME/.config/systemd/user/$u.service.d" ] && {
    cp -rp "$PROFILE_HOME/.config/systemd/user/$u.service.d" "$DEST/systemd/user/"; n=$((n+1)); }
  if [ "$(unit_scope "$u")" = system ] && [ -f "/etc/systemd/system/$u.service" ]; then
    cp -p "/etc/systemd/system/$u.service" "$DEST/systemd/system/" 2>/dev/null && n=$((n+1))
    [ -d "/etc/systemd/system/$u.service.d" ] && cp -rp "/etc/systemd/system/$u.service.d" "$DEST/systemd/system/" 2>/dev/null
  fi
done
ok "$n unit file(s)/drop-in dir(s)"

# ── 3b. the knowledge vault ──────────────────────────────────────────────────
# Runtime content since the vault moved out of the config tree, so git no longer holds anything
# resembling what the agent has written. If it is not here, it is nowhere.
hdr "vault"
if [ -d "$HERMES_HOME/AI-Second-Brain" ]; then
  if tar -C "$HERMES_HOME" -czf "$DEST/AI-Second-Brain.tar.gz" AI-Second-Brain 2>/dev/null; then
    chmod 600 "$DEST/AI-Second-Brain.tar.gz"
    ok "AI-Second-Brain ($(find "$HERMES_HOME/AI-Second-Brain" -type f | wc -l) file(s), $(du -h "$DEST/AI-Second-Brain.tar.gz" | cut -f1))"
  else bad "could not archive the vault"; fi
else
  info "no vault at $HERMES_HOME/AI-Second-Brain — skipped"
fi

# ── 4. vector memory ─────────────────────────────────────────────────────────
# A qdrant SNAPSHOT, not a copy of the storage dir: the process holds the segment files open
# and a filesystem copy of a live collection restores as a corrupt one.
hdr "mem0 / qdrant"
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
  resp="$(curl -s -m 60 -X POST -H "api-key: $key" "http://127.0.0.1:$qport/collections/hermes_mem0/snapshots" 2>/dev/null)"
  sname="$(printf '%s' "$resp" | python3 -c "import sys,json;print(json.load(sys.stdin).get('result',{}).get('name',''))" 2>/dev/null)"
  if [ -n "$sname" ]; then
    if curl -s -m 300 -H "api-key: $key" \
        "http://127.0.0.1:$qport/collections/hermes_mem0/snapshots/$sname" -o "$DEST/hermes_mem0.snapshot" 2>/dev/null; then
      ok "qdrant snapshot $(du -h "$DEST/hermes_mem0.snapshot" | cut -f1) ($sname)"
      # Don't leave it on the server too — the point is having it HERE.
      curl -s -m 30 -X DELETE -H "api-key: $key" \
        "http://127.0.0.1:$qport/collections/hermes_mem0/snapshots/$sname" >/dev/null 2>&1
    else
      warn "snapshot created on the server but could not be downloaded"
    fi
  else
    warn "qdrant snapshot request failed — memory NOT backed up"
  fi
else
  info "no qdrant in this profile — skipped"
fi

# ── 5. manifest ──────────────────────────────────────────────────────────────
{
  echo "profile:   $PROFILE_NAME ($PROFILE_USER)"
  echo "taken:     $(date -u '+%F %T') UTC"
  echo "host:      $(hostname)"
  echo "tree:      $PROFILE_DEST"
  echo "commit:    $(git_head 2>/dev/null || echo '<not a git checkout>')"
  echo "conductor: $CONDUCTOR_DB_FILE"
  [ -f "$REPO_ROOT/VERSION" ] && echo "version:   $(cat "$REPO_ROOT/VERSION")"
  echo
  echo "restore with: scripts/rollback.sh $PROFILE_NAME --from $DEST"
  echo
  echo "CONTAINS SECRETS — 0700/0600, do not copy off this machine unencrypted."
} > "$DEST/MANIFEST.txt"
chmod 600 "$DEST/MANIFEST.txt"

# ── 6. prune ─────────────────────────────────────────────────────────────────
KEEP="${AI_BACKUP_KEEP:-10}"
mapfile -t olds < <(ls -1dt "$HERMES_HOME/backups"/*/ 2>/dev/null | tail -n +$((KEEP+1)))
if [ "${#olds[@]}" -gt 0 ]; then
  for d in "${olds[@]}"; do rm -rf "$d"; done
  info "pruned ${#olds[@]} backup(s) older than the last $KEEP"
fi

hdr "done"
info "$DEST  ($(du -sh "$DEST" | cut -f1))"
printf '%s\n' "$DEST" > "$HERMES_HOME/backups/.last"
finish
