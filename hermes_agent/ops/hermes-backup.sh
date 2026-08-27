#!/usr/bin/env bash
# hermes-backup.sh — the recurring backup this box did not have.
#
# WHAT WAS THERE BEFORE (measured 2026-08-27): nothing recurring. The only backups on
# disk were a side effect of `hermes update --backup`, kept two deep — about 48 hours
# of history — and they contained no systemd units, no drop-ins, no Qdrant snapshot, no
# secrets from outside ~/.hermes, and ho.db as a RAW FILE COPY while the database was in
# WAL mode with a 778 KB uncheckpointed write-ahead log beside it. A raw copy of a WAL
# database is not merely stale; it can be torn.
#
# WHAT IS BACKED UP, AND WHY EACH ONE
#   ho.db              via `sqlite3 .backup`, the only way to get a consistent copy of a
#                      live WAL database. `cp` captures the main file and leaves the WAL
#                      behind, so committed transactions silently vanish.
#   systemd user units AND their drop-ins, as a tar. The drop-ins are where the real
#                      deployment paths live (WorkingDirectory, CONDUCTOR_DIR,
#                      DATABASE_URL, HO_PROFILES_DIR, the memory ceiling). A backup
#                      without them restores a system pointing at the wrong tree.
#   Qdrant             via the snapshot API, not by copying storage/. Copying a live
#                      segment directory is the same class of mistake as cp'ing a WAL db.
#                      Memory is dead without this: mem0's vectors exist nowhere else.
#   ~/.hermes config   config.yaml, .env, mem0.json, SOUL.md, MEMORY.md, USER.md,
#                      agent-hooks/ — none of which has a rendered representation in git.
#   secrets            ~/.config/ai-agent-stack/secrets.env (the single source) AND both
#                      llm-failover-proxy configs, which carry provider keys inline and
#                      are the most load-bearing config in the stack.
#   the wiki           ~/.hermes/AI-Second-Brain as a tar: the repo holds only a seed, so
#                      everything the agent has written lives here and nowhere else.
#   switcher state     tab bindings, anchors, task spaces, topic media. Losing anchors
#                      means the bot's replies start escaping into the DM lobby.
#
# NOT backed up on purpose: the hermes-agent checkout (it is a git clone plus vendored
# patches that patchers re-apply), node_modules, caches, and ~/.hermes/backups itself.
#
# Retention is by COUNT, not by age, so a machine that sat idle for a month still has
# history. Everything is 0600/0700: several of these files are secrets.
set -uo pipefail

HOME_DIR="${HOME:-/home/vadim_prod}"
H="$HOME_DIR/.hermes"
DEST_ROOT="${HERMES_BACKUP_DIR:-$H/backups}"
KEEP="${HERMES_BACKUP_KEEP:-14}"
STAMP="$(date -u +%Y%m%d-%H%M%S)"
DEST="$DEST_ROOT/auto-$STAMP"
LOG="$H/logs/hermes-backup.log"
mkdir -p "$(dirname "$LOG")"

say() { printf '%s %s\n' "$(date -u +'%F %T')" "$*" | tee -a "$LOG"; }
warn_count=0
warn() { warn_count=$((warn_count + 1)); say "WARN: $*"; }

mkdir -p "$DEST"/{hermes,units,secrets,qdrant,state} || { say "FATAL: cannot create $DEST"; exit 1; }
say "backup -> $DEST"

# ── ho.db: sqlite3 .backup, then PROVE the copy is usable ─────────────────────────
HO_DB="${HO_DB:-$H/ho.db}"
if [ -f "$HO_DB" ]; then
  if sqlite3 "$HO_DB" ".backup '$DEST/ho.db'" 2>>"$LOG"; then
    ic="$(sqlite3 "$DEST/ho.db" 'pragma integrity_check;' 2>/dev/null | head -1)"
    live_n="$(sqlite3 "$HO_DB" 'select count(*) from ho_jobs;' 2>/dev/null)"
    copy_n="$(sqlite3 "$DEST/ho.db" 'select count(*) from ho_jobs;' 2>/dev/null)"
    if [ "$ic" = "ok" ] && [ -n "$copy_n" ] && [ "$copy_n" -ge "${live_n:-0}" ] 2>/dev/null; then
      say "ho.db: ok ($copy_n jobs, integrity ok)"
    else
      warn "ho.db copy suspect (integrity='$ic' live=$live_n copy=$copy_n)"
    fi
  else
    warn "ho.db .backup failed"
  fi
else
  warn "ho.db not found at $HO_DB"
fi

# ── systemd user units + drop-ins ─────────────────────────────────────────────────
if [ -d "$HOME_DIR/.config/systemd/user" ]; then
  tar czf "$DEST/units/systemd-user.tar.gz" -C "$HOME_DIR/.config/systemd" user 2>>"$LOG" \
    && say "units: $(tar tzf "$DEST/units/systemd-user.tar.gz" | grep -c '\.\(service\|timer\|conf\)$') files" \
    || warn "units tar failed"
  # A drop-in count of zero means the tar is useless even though it succeeded.
  di="$(tar tzf "$DEST/units/systemd-user.tar.gz" 2>/dev/null | grep -c '\.service\.d/.*\.conf$')"
  [ "${di:-0}" -gt 0 ] || warn "units tar contains NO drop-ins — deployment paths not captured"
else
  warn "no systemd user dir"
fi

# ── Qdrant snapshot via the API ───────────────────────────────────────────────────
QENV="$H/qdrant-server/qdrant.env"
if [ -f "$QENV" ]; then
  # shellcheck disable=SC1090
  set -a; . "$QENV"; set +a
  QP="${QDRANT__SERVICE__HTTP_PORT:-6353}"
  QK="${QDRANT__SERVICE__API_KEY:-}"
  cols="$(curl -sS --max-time 20 -H "api-key: $QK" "http://127.0.0.1:$QP/collections" \
          | python3 -c 'import json,sys
try: print(" ".join(c["name"] for c in json.load(sys.stdin)["result"]["collections"]))
except Exception: pass' 2>/dev/null)"
  if [ -z "$cols" ]; then
    warn "Qdrant: could not list collections on :$QP"
  else
    for c in $cols; do
      name="$(curl -sS --max-time 120 -X POST -H "api-key: $QK" \
               "http://127.0.0.1:$QP/collections/$c/snapshots" \
               | python3 -c 'import json,sys
try: print(json.load(sys.stdin)["result"]["name"])
except Exception: pass' 2>/dev/null)"
      if [ -z "$name" ]; then warn "Qdrant: snapshot of $c failed"; continue; fi
      if curl -sS --max-time 300 -H "api-key: $QK" \
           "http://127.0.0.1:$QP/collections/$c/snapshots/$name" \
           -o "$DEST/qdrant/$name" && [ -s "$DEST/qdrant/$name" ]; then
        say "qdrant: $c -> $name ($(du -h "$DEST/qdrant/$name" | cut -f1))"
        # Snapshots accumulate server-side and are large; keep the server tidy.
        curl -sS --max-time 60 -X DELETE -H "api-key: $QK" \
             "http://127.0.0.1:$QP/collections/$c/snapshots/$name" >/dev/null 2>&1
      else
        warn "Qdrant: download of $c/$name failed"
      fi
    done
  fi
else
  warn "no qdrant.env — Qdrant NOT backed up"
fi

# ── ~/.hermes config + persona + hooks ────────────────────────────────────────────
for f in config.yaml .env mem0.json SOUL.md MEMORY.md USER.md; do
  [ -f "$H/$f" ] && cp -a "$H/$f" "$DEST/hermes/" 2>>"$LOG"
done
[ -d "$H/agent-hooks" ] && cp -a "$H/agent-hooks" "$DEST/hermes/" 2>>"$LOG"
[ -f "$H/qdrant-server/qdrant.env" ] && cp -a "$H/qdrant-server/qdrant.env" "$DEST/hermes/" 2>>"$LOG"
n=$(find "$DEST/hermes" -type f | wc -l); say "hermes config: $n files"
for must in config.yaml .env mem0.json SOUL.md; do
  [ -f "$DEST/hermes/$must" ] || warn "MISSING from backup: $must"
done

# ── secrets that live OUTSIDE ~/.hermes ───────────────────────────────────────────
[ -f "$HOME_DIR/.config/ai-agent-stack/secrets.env" ] \
  && cp -a "$HOME_DIR/.config/ai-agent-stack/secrets.env" "$DEST/secrets/" 2>>"$LOG" \
  || warn "secrets.env not captured"
for f in config.json config-strong.json .env; do
  [ -f "$HOME_DIR/.config/llm-failover-proxy/$f" ] \
    && cp -a "$HOME_DIR/.config/llm-failover-proxy/$f" "$DEST/secrets/llmfp-$f" 2>>"$LOG"
done
[ -f "$HOME_DIR/.config/opencode/opencode.jsonc" ] \
  && cp -a "$HOME_DIR/.config/opencode/opencode.jsonc" "$DEST/secrets/" 2>>"$LOG"
[ -f "$HOME_DIR/.local/share/opencode/auth.json" ] \
  && cp -a "$HOME_DIR/.local/share/opencode/auth.json" "$DEST/secrets/opencode-auth.json" 2>>"$LOG"
[ -f "$HOME_DIR/.claude/settings.json" ] \
  && cp -a "$HOME_DIR/.claude/settings.json" "$DEST/secrets/claude-settings.json" 2>>"$LOG"
[ -f "$DEST/secrets/llmfp-config.json" ] || warn "llm-failover-proxy config NOT captured"

# ── the wiki (everything the agent wrote; the repo has only a seed) ───────────────
if [ -d "$H/AI-Second-Brain" ]; then
  tar czf "$DEST/AI-Second-Brain.tar.gz" -C "$H" AI-Second-Brain 2>>"$LOG" \
    && say "wiki: $(tar tzf "$DEST/AI-Second-Brain.tar.gz" | wc -l) entries" \
    || warn "wiki tar failed"
fi

# ── switcher state (tabs, anchors, backlogs, topic media) ────────────────────────
for f in claude-switcher-state.json claude-switcher-anchors.json csw-task-spaces.json \
         csw-topic-media.json gateway_state.json channel_directory.json mtproto-topics.json; do
  [ -f "$H/$f" ] && cp -a "$H/$f" "$DEST/state/" 2>>"$LOG"
done
[ -f "$H/state.db" ] && sqlite3 "$H/state.db" ".backup '$DEST/state/state.db'" 2>>"$LOG" \
  && say "state.db: ok" || true
say "switcher state: $(find "$DEST/state" -type f | wc -l) files"

# ── permissions, manifest, retention ─────────────────────────────────────────────
chmod -R go-rwx "$DEST"
{
  echo "created_utc=$STAMP"
  echo "host=$(hostname)"
  echo "hermes_version=$("$H/hermes-agent/venv/bin/hermes" --version 2>/dev/null | head -1)"
  echo "warnings=$warn_count"
  echo "--- contents ---"
  find "$DEST" -type f -printf '%P\t%s\n' | sort
} > "$DEST/MANIFEST.txt"
chmod 600 "$DEST/MANIFEST.txt"

mapfile -t old < <(find "$DEST_ROOT" -maxdepth 1 -name 'auto-*' -type d | sort | head -n -"$KEEP")
for d in "${old[@]:-}"; do [ -n "$d" ] && rm -rf "$d" && say "pruned $(basename "$d")"; done

say "done: $(du -sh "$DEST" | cut -f1), warnings=$warn_count"
# A backup with warnings is not a backup you can rely on. Exit non-zero so systemd
# marks the unit failed and the failure is visible instead of buried in a log.
[ "$warn_count" -eq 0 ] || exit 1
