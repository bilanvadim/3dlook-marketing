#!/usr/bin/env bash
# doctor.sh [profile] — look for the failure modes that produce NO error message. Read-only.
#
# status.sh reports; this judges. Every check below exists because the corresponding failure
# actually happened on this box and was invisible: nothing logged, both halves believing they
# were fine. That is the selection criterion — if a problem announces itself in a log, it does
# not need a check here.
#
# Exit: 0 clean, 1 something is broken, 2 warnings only.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_profile "${1:-}"

# ── 1. the two halves must agree on ONE conductor database ───────────────────
# THE quietest bug found so far. The gateway resolves its own copy of the path
# (HO_DB or ~/.hermes/ho.db) and the conductor resolves its own (unit drop-in
# Environment, then its .env, then conductor-run.sh's default). On vadim_prod they
# disagreed for weeks: every Telegram Approve/Deny wrote "approved" into an empty
# schema while the conductor sat out its timeout against a different file. Neither
# side ever logged anything — both were working perfectly, on different databases.
hdr "conductor ↔ gateway: one database?"
cond_db=""
dropin_db="$(sc hermes-conductor show -p Environment 2>/dev/null | tr ' ' '\n' | sed -n 's/^DATABASE_URL=//p' | tail -1)"
envfile_db="$(env_get "$CONDUCTOR_DIR/.env" DATABASE_URL || true)"
cond_db="${envfile_db:-$dropin_db}"
cond_db="${cond_db#file:}"
[ -n "$cond_db" ] || cond_db="$HERMES_HOME/ho.db"   # conductor-run.sh's own default

gw_sw="$HERMES_HOME/hermes-agent/gateway/claude_switcher.py"
gw_db="$HERMES_HOME/ho.db"                          # HO_DB or ~/.hermes/ho.db
gw_override="$(env_get "$HERMES_HOME/.env" HO_DB || true)"
[ -n "$gw_override" ] && gw_db="$gw_override"

info "conductor → $cond_db"
info "gateway   → $gw_db"
if [ ! -f "$gw_sw" ]; then
  warn "gateway claude_switcher.py not found — cannot confirm the gateway side"
elif [ "$(readlink -f "$cond_db" 2>/dev/null)" = "$(readlink -f "$gw_db" 2>/dev/null)" ]; then
  ok "both resolve to the same file"
else
  bad "DIFFERENT FILES — escalation buttons write where nothing reads them"
fi
# Both sides must have their `file:` prefix stripped BEFORE comparing, and the stripping has to
# be a real expansion. Written as "$envfile_db#file:" it was string concatenation, not a prefix
# removal, so this warned that two identical paths differed — on a runtime where they matched.
dropin_path="${dropin_db#file:}"
envfile_path="${envfile_db#file:}"
if [ -n "$envfile_path" ] && [ -n "$dropin_path" ] \
   && [ "$(readlink -f "$dropin_path" 2>/dev/null)" != "$(readlink -f "$envfile_path" 2>/dev/null)" ]; then
  warn "unit drop-in says $dropin_path but conductor/.env says $envfile_path — the unit wins"
fi

# ── 2. the unit and the process must agree on WHICH TREE ──────────────────────
# A unit pointing at one tree while the live process runs from another is a delayed
# fault, not a curiosity: everything looks fine until a restart, and then the box
# resolves the disagreement itself, silently, possibly onto a tree that cannot start.
# vadim_prod ran a full day in exactly that state.
hdr "conductor: unit tree == running tree?"
unit_wd="$(sc hermes-conductor show -p WorkingDirectory 2>/dev/null | sed 's/^WorkingDirectory=//')"
run_cmd="$(pgrep -u "$PROFILE_USER" -f 'src/core/conductor\.ts' 2>/dev/null | while read -r p; do tr '\0' ' ' < "/proc/$p/cmdline" 2>/dev/null; echo; done | grep -m1 'node_modules/tsx')"
info "unit WorkingDirectory  ${unit_wd:-<unset>}"
if [ -z "$run_cmd" ]; then
  warn "no conductor process found — cannot compare (is it meant to be running?)"
elif [ -n "$unit_wd" ] && printf '%s' "$run_cmd" | grep -qF -- "$unit_wd"; then
  ok "the running process comes from the unit's tree"
else
  bad "running process is NOT from $unit_wd — a restart will change what runs"
  info "running: $(printf '%s' "$run_cmd" | grep -oE '/[^ ]*/conductor' | head -1)"
fi

# ── 3. one unit per service, in one scope ────────────────────────────────────
# A leftover unit file for a service that runs in the other scope is a loaded gun:
# enable it and two conductors claim jobs from one SQLite queue. sergiy_prod has a
# disabled user unit sitting next to the active system one right now.
hdr "duplicate unit files"
dupes=0
# A system-scope unit is GLOBAL: on a shared box it may well belong to the other account, and
# its mere existence says nothing about this profile. Checking only "does the file exist in the
# other scope" reported that vadim_prod had an enabled duplicate — when the file in question was
# sergiy_prod's system unit, running sergiy_prod's tree. So establish OWNERSHIP first: a unit
# counts as this profile's only if it points into this profile's tree or home.
unit_is_ours(){
  local file="$1" body
  body="$(cat "$file" 2>/dev/null)" || return 1
  case "$body" in
    *"$PROFILE_DEST"*|*"HOME=$PROFILE_HOME"*|*"User=$PROFILE_USER"*) return 0;;
  esac
  return 1
}
for u in "${ALL_SERVICES[@]}"; do
  sys="/etc/systemd/system/$u.service"; usr="$PROFILE_HOME/.config/systemd/user/$u.service"
  [ -f "$sys" ] && [ -f "$usr" ] || continue
  # Only the unit in the OTHER scope matters here, and only if it is ours.
  if [ "$(unit_scope "$u")" = system ]; then other_file="$usr"; other_enabled="$(systemctl --user is-enabled "$u" 2>&1)"
  else other_file="$sys"; other_enabled="$(systemctl is-enabled "$u" 2>&1)"; fi
  if ! unit_is_ours "$other_file"; then
    info "$u also exists in the other scope, but that unit is not this profile's — ignoring"
    continue
  fi
  if [ "$other_enabled" = enabled ]; then
    bad "$u: this profile has an ENABLED unit in both scopes — two instances will claim one queue"
  else
    warn "$u has a leftover unit file of ours in the other scope (disabled). Remove it, don't keep it as a spare."
  fi
  dupes=$((dupes+1))
done
# A local counter, not the global FAILS/WARNS: those already carry findings from the sections
# above, so testing them here printed "no duplicates" or stayed silent depending on unrelated
# checks — a status line that lies whenever anything earlier failed.
[ "${dupes:-0}" = 0 ] && ok "no service has unit files in two scopes"

# ── 4. ports: assigned, listening, and nobody else's ─────────────────────────
# Ports are the reason profiles exist. A shared value does not error — the second
# binder just loses, and its half of the system goes quiet (this is what happened to
# the escalation webhook while both profiles defaulted to 3001).
hdr "ports"
for pair in "webhook:$PROFILE_HO_WEBHOOK_PORT" "qdrant-http:${PROFILE_QDRANT_HTTP_PORT:-}" \
            "qdrant-grpc:${PROFILE_QDRANT_GRPC_PORT:-}" "proxy-agentic:${PROFILE_PROXY_AGENTIC_PORT:-}" \
            "proxy-strong:${PROFILE_PROXY_STRONG_PORT:-}"; do
  name="${pair%%:*}"; port="${pair##*:}"; [ -n "$port" ] || continue
  owner="$(ss -ltnp 2>/dev/null | awk -v p=":$port" '$4 ~ p"$" {print $NF}' | head -1)"
  if [ -z "$owner" ]; then bad "$name :$port not listening"; continue; fi
  # Whose process is it? A port this profile claims must be held by this profile's user.
  pid="$(printf '%s' "$owner" | grep -oE 'pid=[0-9]+' | head -1 | cut -d= -f2)"
  puser="$(ps -o user= -p "${pid:-0}" 2>/dev/null | tr -d ' ')"
  if [ -n "$puser" ] && [ "$puser" != "$PROFILE_USER" ]; then
    bad "$name :$port is held by $puser, not $PROFILE_USER — port assignment collision"
  else
    ok "$name :$port held by ${puser:-$PROFILE_USER}"
  fi
done
# Cross-profile collision, statically: two profiles must never name one port.
for other in "$REPO_ROOT"/config/profiles/*.vars; do
  o="$(basename "$other" .vars)"; [ "$o" = "$PROFILE_NAME" ] && continue
  for k in PROFILE_HO_WEBHOOK_PORT PROFILE_QDRANT_HTTP_PORT PROFILE_QDRANT_GRPC_PORT \
           PROFILE_PROXY_AGENTIC_PORT PROFILE_PROXY_STRONG_PORT; do
    mine="${!k:-}"; [ -n "$mine" ] || continue
    theirs="$(sed -n "s/^$k=//p" "$other" | tr -d '"')"
    [ "$mine" = "$theirs" ] && bad "$k=$mine is also claimed by profile $o"
  done
done

# ── 5. secrets: present, private, and NOT the other account's ────────────────
# A cross-user credential copy is the one mistake in this setup that cannot be undone by
# editing a file — it has to be rotated. It happened: one Google key ended up serving as
# another user's proxy gate. So compare, never trust.
hdr "secrets"
# The canonical location is ~/.config/ai-agent-stack/secrets.env, which is what install.sh
# reads. It is NOT the only place they can be: sergiy_prod predates that mechanism and holds
# its keys directly in ~/.hermes/.env. Flagging that as "no secrets" is wrong — the file is
# there, with the right mode. So check WHEREVER they live, and say plainly which layout is in
# use, because the two accounts differing here is a convergence task, not a fault.
SECRET_STORES=()
[ -f "$SECRETS_FILE" ] && SECRET_STORES+=("$SECRETS_FILE")
[ -f "$HERMES_HOME/.env" ] && SECRET_STORES+=("$HERMES_HOME/.env")
if [ "${#SECRET_STORES[@]}" -eq 0 ]; then
  bad "no secret store found (looked in $SECRETS_FILE and $HERMES_HOME/.env)"
else
  if [ -f "$SECRETS_FILE" ]; then
    ok "canonical store present: $SECRETS_FILE"
  else
    warn "no $SECRETS_FILE — keys live in $HERMES_HOME/.env instead (install.sh reads the canonical path; converge these)"
  fi
  for f in "${SECRET_STORES[@]}"; do
    perm="$(stat -c '%a' "$f")"
    [ "$perm" = 600 ] && ok "$(basename "$f") mode $perm" || bad "$f mode $perm — must be 600"
    dperm="$(stat -c '%a' "$(dirname "$f")")"
    case "$dperm" in 700|750|755) : ;; *) warn "$(dirname "$f") mode $dperm — unexpectedly open";; esac
  done
  for other in "$REPO_ROOT"/config/profiles/*.vars; do
    o="$(basename "$other" .vars)"; [ "$o" = "$PROFILE_NAME" ] && continue
    ohome="$(sed -n 's/^PROFILE_HOME=//p' "$other" | tr -d '"')"
    theirs=(); for c in "$ohome/.config/ai-agent-stack/secrets.env" "$ohome/.hermes/.env"; do
      [ -r "$c" ] && theirs+=("$c")
    done
    if [ "${#theirs[@]}" -eq 0 ]; then
      info "cannot read $o's secrets (correct — accounts are isolated; run doctor as each user)"
      continue
    fi
    shared=0
    for k in TELEGRAM_BOT_TOKEN OPENROUTER_API_KEY GEMINI_API_KEY GOOGLE_API_KEY GROQ_API_KEY \
             NVIDIA_API_KEY OPENCODE_ZEN_API_KEY GITHUB_PERSONAL_ACCESS_TOKEN TG_API_HASH \
             OPENAI_API_KEY QDRANT_API_KEY; do
      for mine_f in "${SECRET_STORES[@]}"; do
        a="$(env_get "$mine_f" "$k" || true)"; [ -n "$a" ] || continue
        for their_f in "${theirs[@]}"; do
          b="$(env_get "$their_f" "$k" || true)"
          # Compare by hash so a match can be reported without ever printing the value.
          [ -n "$b" ] && [ "$(hash8 "$a")" = "$(hash8 "$b")" ] && {
            bad "$k is IDENTICAL to $o's (sha $(hash8 "$a")) — rotate it, do not just edit one side"; shared=1; }
        done
      done
    done
    [ "$shared" = 0 ] && ok "no secret shared with $o"
  done
fi

# ── 5b. the source and the distributed copies must still agree ───────────────
# secrets.env is the SOURCE; install.sh distributes it into ~/.hermes/.env, ai-models.env,
# mtproto/creds.env, telegram-userbot/.env and conductor-bridge/bridge.env. Those are generated.
#
# Nothing stops someone editing a generated copy directly — that is exactly how this account
# ended up with keys in ~/.hermes/.env and no source file at all. When they diverge, the running
# system keeps using the copy while the source says something else, and the next install.sh run
# silently reverts the live value. No error either way.
if [ -f "$SECRETS_FILE" ]; then
  hdr "secrets.env vs the copies it generates"
  diverged=0; compared=0
  for copy in "$HERMES_HOME/.env" "$HERMES_HOME/ai-models.env" "$HERMES_HOME/mtproto/creds.env" \
              "$HERMES_HOME/telegram-userbot/.env" "$HERMES_HOME/conductor-bridge/bridge.env"; do
    [ -f "$copy" ] || continue
    while IFS= read -r k; do
      a="$(env_get "$SECRETS_FILE" "$k" || true)"; [ -n "$a" ] || continue
      b="$(env_get "$copy" "$k" || true)";        [ -n "$b" ] || continue
      compared=$((compared+1))
      if [ "$(hash8 "$a")" != "$(hash8 "$b")" ]; then
        bad "$k differs between secrets.env ($(hash8 "$a")) and $(basename "$copy") ($(hash8 "$b"))"
        diverged=$((diverged+1))
      fi
    # Plain ERE: grep -E has no lookahead, so the `(?==)` form silently failed and only the
    # fallback ever ran. One way of listing the names is enough.
    done < <(grep -E '^[A-Z][A-Z0-9_]*=' "$SECRETS_FILE" | cut -d= -f1 | sort -u)
  done
  [ "$diverged" = 0 ] && ok "$compared shared value(s) identical across source and copies"
fi

# ── 6. render state ──────────────────────────────────────────────────────────
hdr "render"
if [ -x "$REPO_ROOT/scripts/render.sh" ]; then
  out="$("$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$PROFILE_DEST" --check 2>&1)"
  if [ $? -eq 0 ]; then ok "tree is fully rendered for $PROFILE_NAME"
  else bad "$(printf '%s' "$out" | head -1)"; info "run: scripts/render.sh $PROFILE_NAME"; fi
else
  warn "render.sh missing"
fi

# ── 7. the snapshot safety net has to actually be wired ──────────────────────
# The pre-run snapshot is the only rollback an autonomous run has (autocommit skips
# main, and these repos work on main). If HO_SNAPSHOT_SH is unset or unreadable the
# conductor logs one warning at job start and runs anyway — easy to never notice.
hdr "pre-run snapshot"
snap="$(env_get "$CONDUCTOR_DIR/.env" HO_SNAPSHOT_SH || true)"
if [ -z "$snap" ]; then
  repo_root_env="$(env_get "$CONDUCTOR_DIR/.env" HERMES_REPO_ROOT || true)"
  [ -n "$repo_root_env" ] && snap="$repo_root_env/agents-ai/telegram-bot-agent/hermes-agent/ops/conductor-snapshot.sh"
fi
if [ -z "$snap" ]; then bad "neither HO_SNAPSHOT_SH nor HERMES_REPO_ROOT is set — runs have no rollback point"
elif [ ! -x "$snap" ]; then bad "snapshot script not executable: $snap"
else ok "snapshot script ready: $snap"; fi

# ── 7b. the LIVE database must accept the profiles that exist ────────────────
# validate.sh checks the schema FILE against the shipped profiles, and the file was correct — while
# sergiy_prod's live ho_jobs still carried the PRE-RENAME constraint
# check (profile in ('dev-sm','seo-sm',…)) and therefore rejected every job submitted under the
# names the system actually uses. `create table if not exists` never alters an existing table, so a
# schema change lands in git and nowhere else, and the only symptom is a bare "CHECK constraint
# failed" at enqueue time. The live database is the thing that decides, so check IT.
hdr "live schema vs shipped profiles"
if [ -f "$CONDUCTOR_DB_FILE" ] && [ -d "$PROFILES_DIR" ]; then
  live_pc="$(sqlite_q "$CONDUCTOR_DB_FILE" "select sql from sqlite_master where name='ho_jobs';" \
    | tr -d '\n' | grep -oE "profile in \([^)]*\)" || true)"
  rejected=()
  for f in "$PROFILES_DIR"/*.json; do
    [ -e "$f" ] || continue
    p="$(basename "$f" .json)"
    case "$live_pc" in *"'$p'"*) : ;; *) rejected+=("$p");; esac
  done
  if [ "${#rejected[@]}" -eq 0 ]; then
    ok "ho_jobs accepts every shipped profile"
  else
    bad "ho_jobs REJECTS ${#rejected[@]} shipped profile(s): ${rejected[*]}"
    info "fix with: scripts/migrate-db.sh $PROFILE_NAME   (rehearse first: --db /tmp/copy.db)"
  fi
else
  info "no queue db or profiles dir — skipped"
fi

# ── 7b2. the escalation endpoint must not be open ─────────────────────────────
# It decides gated actions — approve, deny, ABORT — for any escalation id. It used to trust any POST
# that reached the port, with loopback as the only control, and loopback does not separate the other
# accounts on this box: a forged callback was accepted with {"ok":true}, forging decided_by too.
# Verified against the running service. Tested live here rather than by reading the config, because
# what matters is what the LISTENER does, not what a file says.
hdr "escalation endpoint is authenticated"
secret="$(env_get "$CONDUCTOR_DIR/.env" HO_WEBHOOK_SECRET || true)"
if [ -z "$secret" ]; then
  bad "HO_WEBHOOK_SECRET is not set — every callback is refused, so Telegram buttons cannot work"
  info "generate one: scripts/deploy.sh $PROFILE_NAME (writes it into a fresh .env), then restart"
elif [ "${#secret}" -lt 16 ]; then
  bad "HO_WEBHOOK_SECRET is only ${#secret} chars — use 32+ random characters"
else
  ok "HO_WEBHOOK_SECRET set (${#secret} chars)"
fi
if port_listening "$PROFILE_HO_WEBHOOK_PORT"; then
  code_no="$(curl -s -o /dev/null -w '%{http_code}' -m 4 -X POST \
    "http://127.0.0.1:$PROFILE_HO_WEBHOOK_PORT/telegram-webhook" \
    -H 'Content-Type: application/json' -d '{}' 2>/dev/null)"
  if [ "$code_no" = 401 ]; then ok "an unauthenticated callback is rejected (401)"
  elif [ "$code_no" = 200 ]; then bad "an unauthenticated callback was ACCEPTED (200) — anyone local can approve a gated action"
  else warn "unauthenticated callback answered HTTP $code_no (expected 401)"; fi
  if [ -n "$secret" ]; then
    code_yes="$(curl -s -o /dev/null -w '%{http_code}' -m 4 -X POST \
      "http://127.0.0.1:$PROFILE_HO_WEBHOOK_PORT/telegram-webhook" \
      -H 'Content-Type: application/json' -H "X-Telegram-Bot-Api-Secret-Token: $secret" \
      -d '{}' 2>/dev/null)"
    # A correct secret must still be accepted, or the fix has simply broken the button.
    [ "$code_yes" = 200 ] && ok "a correctly signed callback is accepted (200)" \
      || bad "a correctly signed callback answered HTTP $code_yes — the escalation path is broken"
  fi
else
  warn "webhook not listening on :$PROFILE_HO_WEBHOOK_PORT — cannot test it"
fi

# ── 7c. every work_dir the queue has used must have a baseline ────────────────
# This is where the protection actually applies. The conductor sets cwd=work_dir and
# settingSources:['project'], so a job's deny list and PreToolUse hook come from
# <work_dir>/.claude/ — the system's own baseline is never read. A work_dir without one runs an
# autonomous agent with edit and Bash access and nothing in front of it, and NOTHING reports that:
# the job succeeds, the log is clean, and the guard simply was not there.
#
# Checked against the work_dirs the queue has ACTUALLY used, because that is the knowable set — a
# static list would go stale the first time someone enqueues against a new directory.
hdr "work_dir safety baseline"
if [ -f "$CONDUCTOR_DB_FILE" ]; then
  nowd=0; unguarded=0; checked=0
  while IFS= read -r wd; do
    [ -n "$wd" ] || continue
    case "$wd" in .|'') continue;; esac
    [ -d "$wd" ] || { info "work_dir no longer exists: $wd"; continue; }
    checked=$((checked+1))
    if [ ! -f "$wd/.claude/settings.json" ]; then
      bad "no baseline in $wd — an autonomous run there has no deny list and no guard"
      nowd=$((nowd+1))
    elif [ ! -x "$wd/.claude/hooks/guard.py" ]; then
      # Present but not executable fails OPEN: the hook errors and the command proceeds.
      bad "guard.py in $wd is missing or not executable — the hook fails open"
      unguarded=$((unguarded+1))
    fi
  done < <(sqlite_q "$CONDUCTOR_DB_FILE" "select distinct work_dir from ho_jobs;")
  if [ "$checked" = 0 ]; then info "no existing work_dir in the queue history"
  elif [ "$((nowd+unguarded))" = 0 ]; then ok "$checked work_dir(s) from the queue all carry a working baseline"
  else info "fix with: scripts/prepare-workdir.sh <dir>"; fi
else
  info "no queue db — skipped"
fi

# ── 8. escalation hygiene ────────────────────────────────────────────────────
# An escalation whose run is long dead can never be answered by the conductor that
# raised it, and it keeps a job flagged 'escalated' forever.
hdr "escalations"
if [ -f "$CONDUCTOR_DB_FILE" ]; then
  orphans="$(sqlite_q "$CONDUCTOR_DB_FILE" \
    "select count(*) from ho_escalations e where e.status='open' and not exists
       (select 1 from ho_jobs j where j.id=e.job_id and j.status in
        ('queued','deferred','claimed','running','planning','verifying','awaiting-input','escalated'));")"
  if [ "${orphans:-0}" -gt 0 ]; then warn "$orphans open escalation(s) whose job is already terminal — orphaned"
  else ok "no orphaned open escalations"; fi
  ok "queue db readable ($(sqlite_q "$CONDUCTOR_DB_FILE" 'select count(*) from ho_jobs;') jobs)"
else
  bad "queue db missing: $CONDUCTOR_DB_FILE"
fi

finish
