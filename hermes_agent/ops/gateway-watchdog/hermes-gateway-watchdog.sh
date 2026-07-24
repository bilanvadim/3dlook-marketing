#!/usr/bin/env bash
# hermes-gateway-watchdog
# ----------------------------------------------------------------------------
# Detects a WEDGED gateway: the systemd unit shows active/running, but its
# Telegram long-poll loop is dead — getUpdates isn't being acked, so
# getWebhookInfo.pending_update_count stays > 0 and the bot goes silent.
# (Observed 2026-07-23: gateway hung after a drain-timeout, process wouldn't
# die, planned-restart wrapper deadlocked, bot silent ~7h.)
# When wedged, force-restart the gateway (systemd's KillMode=mixed guarantees a
# SIGKILL within TimeoutStopSec=3m30s, so even a TERM-ignoring process dies).
# See memory: project_hermes_gateway_wedge_dup_conductor
#
# SAFETY against false restarts (a healthy long-poller keeps pending at ~0
# because it acks within seconds, so any persistent backlog is a real wedge):
#   - only acts if the unit is active/running (else systemd already handling it)
#   - STRIKES: needs pending>0 on STRIKE_THRESHOLD consecutive checks (state
#     persisted across runs) — one transient burst won't trigger
#   - MIN_UPTIME: never restarts a gateway that's been up < 5min (startup drain)
#   - COOLDOWN: at most one restart per 15min (no restart storms if TG is down)
#   - getWebhookInfo is READ-ONLY and does NOT conflict with the poller;
#     the script NEVER calls getUpdates (that would cause a getUpdates conflict)
#   - API/network error or webhook-mode → inconclusive, no strike change
#
# Test:  DRY_RUN=1 WATCHDOG_FAKE_PENDING=5 hermes-gateway-watchdog.sh   (repeat)
# ----------------------------------------------------------------------------
set -uo pipefail

UNIT=hermes-gateway.service
ENV_FILE=/home/vadim_prod/.hermes/.env
STATE_DIR=/home/vadim_prod/.hermes/gateway-watchdog
STATE="$STATE_DIR/state"
STRIKE_THRESHOLD=3      # consecutive pending>0 checks before acting
COOLDOWN=900           # min seconds between force-restarts (15 min)
MIN_UPTIME=300         # don't act on a gateway up < 5 min (legit startup drain)
DRY_RUN="${DRY_RUN:-0}"

ts()  { date -u '+%Y-%m-%dT%H:%M:%SZ'; }
log() { echo "$(ts) gw-watchdog: $*"; }

mkdir -p "$STATE_DIR"
strikes=0; last_restart=0
# shellcheck disable=SC1090
[ -f "$STATE" ] && . "$STATE" 2>/dev/null
case "$strikes"      in ''|*[!0-9]*) strikes=0;; esac
case "$last_restart" in ''|*[!0-9]*) last_restart=0;; esac
now=$(date +%s)
save() { printf 'strikes=%s\nlast_restart=%s\n' "$strikes" "$last_restart" > "$STATE"; }

# (1) unit must be active/running; otherwise systemd is already restarting it
active="$(systemctl --user is-active "$UNIT" 2>/dev/null)"
if [ "$active" != "active" ]; then
  log "unit $active (not active) — systemd handling; reset strikes"; strikes=0; save; exit 0
fi

# (2) pending_update_count — from Telegram (read-only) or a test override
if [ -n "${WATCHDOG_FAKE_PENDING:-}" ]; then
  status=ok; pending="$WATCHDOG_FAKE_PENDING"; url="-"
  log "TEST: using fake pending=$pending"
else
  TOKEN="$(grep -E '^TELEGRAM_BOT_TOKEN=' "$ENV_FILE" 2>/dev/null | head -1 | cut -d= -f2-)"
  TOKEN="${TOKEN%$'\r'}"; TOKEN="${TOKEN%\"}"; TOKEN="${TOKEN#\"}"; TOKEN="${TOKEN%\'}"; TOKEN="${TOKEN#\'}"
  if [ -z "$TOKEN" ]; then log "no TELEGRAM_BOT_TOKEN in $ENV_FILE — cannot check; skip"; exit 0; fi
  resp="$(curl -s --max-time 15 "https://api.telegram.org/bot$TOKEN/getWebhookInfo" 2>/dev/null)"
  read -r status pending url <<EOF
$(printf '%s' "$resp" | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin); r = d.get("result", {})
    print(("ok" if d.get("ok") else "err"), r.get("pending_update_count", -1), (r.get("url") or "-"))
except Exception:
    print("err -1 -")' 2>/dev/null)
EOF
fi

if [ "${status:-err}" != "ok" ] || [ "${pending:--1}" = "-1" ] || [ -z "${pending:-}" ]; then
  log "getWebhookInfo inconclusive (api/network) — no strike change (strikes=$strikes)"; exit 0
fi
if [ "$url" != "-" ] && [ -n "$url" ]; then
  log "webhook url set ($url) — not long-polling; watchdog N/A; reset strikes"; strikes=0; save; exit 0
fi

# (3) gateway uptime (age since it became active), for the startup-drain guard
aem="$(systemctl --user show "$UNIT" -p ActiveEnterTimestampMonotonic --value 2>/dev/null)"
case "$aem" in ''|*[!0-9]*) aem=0;; esac
up="$(cut -d' ' -f1 /proc/uptime 2>/dev/null)"; up="${up%.*}"; case "$up" in ''|*[!0-9]*) up=0;; esac
if [ "$aem" -gt 0 ] && [ "$up" -gt 0 ]; then age=$(( up - aem/1000000 )); else age=999999; fi

# (4) strike accounting
if [ "$pending" -gt 0 ]; then
  strikes=$(( strikes + 1 ))
  log "pending=$pending → strike $strikes/$STRIKE_THRESHOLD (gateway up ${age}s)"
else
  [ "$strikes" -ne 0 ] && log "pending=0 — poller healthy; reset strikes"
  strikes=0; save; exit 0
fi

if [ "$strikes" -lt "$STRIKE_THRESHOLD" ]; then save; exit 0; fi

# (5) threshold reached — apply the last two guards
if [ "$age" -lt "$MIN_UPTIME" ]; then
  log "threshold hit but gateway only ${age}s old — defer (startup drain)"; save; exit 0
fi
if [ $(( now - last_restart )) -lt "$COOLDOWN" ]; then
  log "threshold hit but within cooldown ($(( now - last_restart ))s < ${COOLDOWN}s) — not restarting"; save; exit 0
fi

log "WEDGE: pending=$pending for $strikes checks, gateway active ${age}s, poller not draining → force restart"
if [ "$DRY_RUN" = "1" ]; then
  log "[dry-run] would: stop planned-restart transients; reset-failed; systemctl restart --no-block $UNIT"
  exit 0
fi

# stop any deadlock-prone planned-restart transients (they spin waiting on a PID that won't die)
for u in $(systemctl --user list-units --all --plain --no-legend 'hermes-gateway-planned-restart-*' 2>/dev/null | awk '{print $1}'); do
  log "stopping stale transient $u"; systemctl --user stop "$u" 2>/dev/null
done
systemctl --user reset-failed "$UNIT" 2>/dev/null
if systemctl --user restart --no-block "$UNIT" 2>/dev/null; then
  log "issued restart --no-block for $UNIT"
else
  log "restart command failed"
fi
strikes=0; last_restart="$now"; save
exit 0
