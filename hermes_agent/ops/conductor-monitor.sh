#!/usr/bin/env bash
# conductor-monitor.sh — Hermes-side PUSH notifier for the conductor.
#
# Reads the conductor's Postgres state (hc_questions / hc_escalations / hc_jobs)
# and Telegram-pushes anything NEW that needs the human: open interview questions,
# open ASK-escalations, and newly-terminal jobs. Dedups via a state file so it
# never re-notifies the same item. Runs from cron every ~5 min.
#
# It only PUSHES. The RESPONSE loop (answering a question via hc_answer_question,
# deciding an escalation via hc_escalations) goes THROUGH Hermes the bot per the
# vps-orchestration skill — a human reply to the bot, not this script.
#
# Modes:
#   (default)   notify — send Telegram for new items, record them as seen
#   --init      mark the CURRENT state as already-seen (no sends) — run once at install
#   --dry-run   print what it WOULD send, send nothing
set -uo pipefail

ENVF="${HERMES_ENV_FILE:-$HOME/.hermes/.env}"
STATE="${CONDUCTOR_MONITOR_STATE:-$HOME/.hermes/.conductor-monitor-state}"
PG_CONTAINER="${HC_PG_CONTAINER:-supabase-db}"
MODE="${1:-notify}"

BOT=$(grep -hE '^TELEGRAM_BOT_TOKEN=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_BOT_TOKEN=//')
CHAT=$(grep -hE '^TELEGRAM_ALLOWED_USERS=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_ALLOWED_USERS=//' | cut -d, -f1)

PSQL() { docker exec -i "$PG_CONTAINER" psql -U postgres -d postgres -tAc "$1" 2>/dev/null; }
touch "$STATE" 2>/dev/null || true
seen() { grep -qxF "$1" "$STATE" 2>/dev/null; }
mark() { printf '%s\n' "$1" >> "$STATE"; }

send() { # $1 = text
  if [ "$MODE" = "--dry-run" ]; then printf '[dry-run] would send:\n%s\n---\n' "$1"; return 0; fi
  if [ -z "$BOT" ] || [ -z "$CHAT" ]; then echo "monitor: missing TELEGRAM creds in $ENVF" >&2; return 1; fi
  curl -s -m 15 "https://api.telegram.org/bot${BOT}/sendMessage" \
    --data-urlencode "chat_id=${CHAT}" \
    --data-urlencode "text=$1" >/dev/null
}

emit() { # $1 = dedup key, $2 = text
  seen "$1" && return 0
  if [ "$MODE" = "--init" ]; then mark "$1"; return 0; fi
  if send "$2"; then mark "$1"; fi
}

# 1) open interview questions
PSQL "select id||E'\t'||job_id||E'\t'||coalesce(step_no::text,'-')||E'\t'||replace(replace(question,E'\n',' '),E'\t',' ') from hc_questions where status='open' order by id" |
while IFS=$'\t' read -r qid job step q; do
  [ -n "${qid:-}" ] || continue
  title=$(PSQL "select title from hc_jobs where id=$job")
  emit "q:$qid" "❓ ${title} (job ${job}, шаг ${step}) ждёт ответа:
${q}

Ответь мне — я передам дирижёру."
done

# 2) open ASK-escalations
PSQL "select id||E'\t'||job_id||E'\t'||reason||E'\t'||replace(replace(coalesce(question,''),E'\n',' '),E'\t',' ') from hc_escalations where status='open' order by id" |
while IFS=$'\t' read -r eid job reason q; do
  [ -n "${eid:-}" ] || continue
  title=$(PSQL "select title from hc_jobs where id=$job")
  emit "e:$eid" "⚠️ ${title} (job ${job}) — нужно решение [${reason}]:
${q}

Ответь: approve / deny / abort."
done

# 3) newly terminal jobs
PSQL "select id||E'\t'||status||E'\t'||title||E'\t'||replace(replace(coalesce(result_summary,''),E'\n',' '),E'\t',' ') from hc_jobs where status in ('done','failed','escalated','aborted') order by id" |
while IFS=$'\t' read -r id st title summary; do
  [ -n "${id:-}" ] || continue
  case "$st" in done) ic="✅";; failed) ic="❌";; aborted) ic="🛑";; *) ic="🟡";; esac
  emit "term:${id}:${st}" "${ic} ${title} (job ${id}): ${st}. ${summary}"
done

[ "$MODE" = "--init" ] && echo "monitor: initialized — $(wc -l < "$STATE" 2>/dev/null || echo 0) keys marked seen"
exit 0
