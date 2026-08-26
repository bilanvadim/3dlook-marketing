#!/usr/bin/env bash
# conductor-monitor.sh — Hermes-side PUSH notifier for the Hermes Orchestrator conductor.
#
# Reads the conductor's SQLite/libSQL state (ho_questions / ho_escalations / ho_jobs)
# and Telegram-pushes anything NEW that needs the human: open interview questions,
# open ASK-escalations, and newly-terminal jobs. Dedups via a state file so it
# never re-notifies the same item. Runs from cron every ~5 min.
#
# It only PUSHES. The RESPONSE loop (answering a question, deciding an escalation)
# goes THROUGH Hermes the bot per the vps-orchestration skill — a human reply to
# the bot, not this script.
#
# State DB: local SQLite file. Resolve order:
#   $HO_DB  →  file: part of $DATABASE_URL  →  $HO_STATE_DIR/ho.db  →  $HOME/.hermes/ho.db
# (A remote libsql://…/Turso DB needs a different reader — use the turso CLI.)
#
# Modes:
#   (default)   notify — send Telegram for new items, record them as seen
#   --init      mark the CURRENT state as already-seen (no sends) — run once at install
#   --dry-run   print what it WOULD send, send nothing
set -uo pipefail

ENVF="${HERMES_ENV_FILE:-$HOME/.hermes/.env}"
STATE="${CONDUCTOR_MONITOR_STATE:-$HOME/.hermes/.conductor-monitor-state}"
HO_STATE_DIR="${HO_STATE_DIR:-$HOME/.hermes}"
MODE="${1:-notify}"

# resolve the SQLite file path
DB="${HO_DB:-}"
if [ -z "$DB" ] && [ -n "${DATABASE_URL:-}" ]; then
  case "$DATABASE_URL" in file:*) DB="${DATABASE_URL#file:}";; esac
fi
DB="${DB:-$HO_STATE_DIR/ho.db}"

BOT=$(grep -hE '^TELEGRAM_BOT_TOKEN=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_BOT_TOKEN=//')
CHAT=$(grep -hE '^TELEGRAM_ALLOWED_USERS=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_ALLOWED_USERS=//' | cut -d, -f1)

SQL() { sqlite3 -noheader -separator "$(printf '\t')" "$DB" "$1" 2>/dev/null; }

# Strip markdown so pushes render as clean plain text (Telegram sendMessage here
# has no parse_mode; raw #/##, **bold**, `code`, |tables| would show literally).
plain() { printf '%s' "$1" | sed -E 's/#{1,6} ?//g; s/\*\*//g; s/`//g; s/ *\| */ · /g; s/\|//g; s/  +/ /g'; }
touch "$STATE" 2>/dev/null || true
seen() { grep -qxF "$1" "$STATE" 2>/dev/null; }
mark() { printf '%s\n' "$1" >> "$STATE"; }

send() { # $1 = text
  if [ "$MODE" = "--dry-run" ]; then printf '[dry-run] would send:\n%s\n%s\n---\n' "$1" "${2:+[buttons] $2}"; return 0; fi
  if [ -z "$BOT" ] || [ -z "$CHAT" ]; then echo "monitor: missing TELEGRAM creds in $ENVF" >&2; return 1; fi
  # Two changes from the obvious form, both load-bearing:
  #
  #  -f (--fail): without it curl exits 0 on an HTTP 400/429, emit() calls mark()
  #  and the item is never retried. The realistic trigger is a long escalation
  #  body — Telegram rejects over 4096 chars — so an open escalation WAITING FOR A
  #  HUMAN DECISION was being dropped forever, with the dedup file guaranteeing it
  #  could not come back.
  #
  #  --config -: the bot token used to sit in the URL, i.e. in argv, readable by
  #  every local account via `ps` — and this runs from cron every 5 minutes, so
  #  the window was permanent. curl reads the URL from stdin instead.
  local rc
  if [ -n "${2:-}" ]; then
    printf 'url = "https://api.telegram.org/bot%s/sendMessage"\n' "$BOT" | \
      curl -sf -m 15 --config - \
        --data-urlencode "chat_id=${CHAT}" \
        --data-urlencode "text=$1" \
        --data-urlencode "reply_markup=$2" >/dev/null
    rc=$?
  else
    printf 'url = "https://api.telegram.org/bot%s/sendMessage"\n' "$BOT" | \
      curl -sf -m 15 --config - \
        --data-urlencode "chat_id=${CHAT}" \
        --data-urlencode "text=$1" >/dev/null
    rc=$?
  fi
  [ "$rc" -ne 0 ] && echo "monitor: telegram send FAILED (curl rc=$rc) — не помечаю доставленным" >&2
  return "$rc"
}

emit() { # $1 = dedup key, $2 = text, $3 = optional reply_markup JSON
  seen "$1" && return 0
  if [ "$MODE" = "--init" ]; then mark "$1"; return 0; fi
  if send "$2" "${3:-}"; then mark "$1"; fi
}

[ -f "$DB" ] || { [ "$MODE" = "--dry-run" ] && echo "monitor: no DB at $DB (nothing to do)"; exit 0; }

# 1) open interview questions
SQL "select id, job_id, coalesce(step_no,'-'), replace(replace(question,char(10),' '),char(9),' ') from ho_questions where status='open' order by id" |
while IFS=$'\t' read -r qid job step q; do
  [ -n "${qid:-}" ] || continue
  title=$(SQL "select title from ho_jobs where id=$job")
  emit "q:$qid" "❓ $(plain "$title") (job ${job}, шаг ${step}) ждёт ответа:
$(plain "$q")

Ответь мне — я передам дирижёру."
done

# 2) open ASK-escalations
SQL "select id, job_id, reason, replace(replace(coalesce(question,''),char(10),' '),char(9),' ') from ho_escalations where status='open' order by id" |
while IFS=$'\t' read -r eid job reason q; do
  [ -n "${eid:-}" ] || continue
  title=$(SQL "select title from ho_jobs where id=$job")
  kb='{"inline_keyboard":[[{"text":"✅ Approve","callback_data":"ho:approve:'"$eid"'"},{"text":"⛔ Deny","callback_data":"ho:deny:'"$eid"'"},{"text":"⏹ Abort","callback_data":"ho:abort:'"$eid"'"}]]}'
  emit "e:$eid" "⚠️ $(plain "$title") (job ${job}) — нужно решение [${reason}]:
$(plain "$q")

Реши кнопкой ниже (или ответь approve / deny / abort)." "$kb"
done

# 3) newly terminal jobs
SQL "select id, status, title, replace(replace(coalesce(result_summary,''),char(10),' '),char(9),' ') from ho_jobs where status in ('done','failed','escalated','aborted') order by id" |
while IFS=$'\t' read -r id st title summary; do
  [ -n "${id:-}" ] || continue
  case "$st" in done) ic="✅";; failed) ic="❌";; aborted) ic="🛑";; *) ic="🟡";; esac
  emit "term:${id}:${st}" "${ic} $(plain "$title") (job ${id}): ${st}. $(plain "$summary")"
done

# 4) jobs parked on a backoff — the silent failure mode this script was missing.
#
# From Telegram a rate-limited run is INDISTINGUISHABLE from a working one: blocks
# 1-3 push questions, escalations and terminal jobs, so a job that is merely
# waiting produces nothing. On 2026-08-25 job 95 sat here for 2.5 hours — ladder
# 59s → 249 → 756 → 1459 → 2007 → 2101 → 2044, two turns per resume — and the only
# signal Вадим got was his own "Статус" question three hours in.
#
# Short rungs stay silent on purpose: under 10 minutes a retry is noise, not news.
# Each longer rung pushes exactly once, keyed on its own not_before, so a long
# stall reports progress (~25 мин → ~34 мин) instead of repeating every 5 minutes.
SQL "select id, status, replace(replace(title,char(10),' '),char(9),' '),
            cast((julianday(not_before) - julianday('now')) * 1440 as int),
            replace(not_before,' ','_')
     from ho_jobs
     where status in ('deferred','paused') and not_before is not null
       and julianday(not_before) - julianday('now') > 10.0/1440
     order by id" |
while IFS=$'\t' read -r id st title mins key; do
  [ -n "${id:-}" ] || continue
  emit "defer:${id}:${key}" "⏳ $(plain "$title") (job ${id}): ${st}, повтор через ~${mins} мин.
Прогон не упал — он ждёт окно Claude (conductor делит его с интерактивными сессиями Вадима). Делать ничего не надо: когда доработает, придёт ✅.
Подробности: mvb-run.py status ${id}"
done

[ "$MODE" = "--init" ] && echo "monitor: initialized — $(wc -l < "$STATE" 2>/dev/null || echo 0) keys marked seen"
exit 0
