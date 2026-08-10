#!/usr/bin/env bash
# audit-config.sh — AgentShield security audit of a Claude Code config tree.
#
# Usage:  audit-config.sh [path] [--baseline] [--quiet]
#   path        dir to scan (default: $CLAUDE_CONFIG_DIR or ~/.claude)
#   --baseline  save this scan as the baseline for future regression checks
#   --quiet     no Telegram, just stdout + JSON report
#
# Writes a timestamped JSON report under <path>/.agentshield/ and a Telegram
# summary. Exit code mirrors AgentShield: 2 if critical findings.
#
# AgentShield audits the CONFIG surface (settings.json permissions, hooks,
# MCP configs, agent definitions, CLAUDE.md) — not skill prose. Pair it with
# install-skill.sh's content scan for full coverage.

set -uo pipefail

for ef in "$HOME/.hermes/.env"; do
  [[ -f "$ef" ]] && { set -a; # shellcheck disable=SC1090
    source "$ef"; set +a; break; }
done

CLAUDE_CONFIG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
target="$CLAUDE_CONFIG_DIR"; save_baseline=0; quiet=0
while (( $# )); do
  case "$1" in
    --baseline) save_baseline=1; shift ;;
    --quiet)    quiet=1; shift ;;
    -*)         echo "unknown arg: $1" >&2; exit 2 ;;
    *)          target="$1"; shift ;;
  esac
done
[[ -d "$target" ]] || { echo "ERR: not a dir: $target" >&2; exit 2; }

outdir="$target/.agentshield"; mkdir -p "$outdir"
report="$outdir/scan.json"
baseline="$outdir/baseline.json"

extra=()
[[ -f "$baseline" ]] && extra=(--baseline "$baseline")

timeout 300 npx -y ecc-agentshield@latest scan \
  --path "$target" --format json --min-severity low "${extra[@]}" \
  >"$report" 2>/dev/null
as_rc=$?

[[ -s "$report" ]] || { echo "ERR: AgentShield produced no report" >&2; exit 2; }

read -r grade score crit high med low files < <(python3 -c "
import json;d=json.load(open('$report'));s=d['score'];m=d['summary']
print(s['grade'],s['numericScore'],m['critical'],m['high'],m['medium'],m['low'],m['filesScanned'])
")

echo "AgentShield: grade $grade ($score/100) — crit=$crit high=$high med=$med low=$low over $files files"
echo "report: $report"

if (( save_baseline )); then
  cp "$report" "$baseline"; echo "baseline saved: $baseline"
fi

if (( ! quiet )); then
  [[ -n "${TELEGRAM_BOT_TOKEN:-}" && -n "${TELEGRAM_CHAT_ID:-}" ]] && \
  curl -fsS -m 10 -X POST \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=🛡️ AgentShield аудит Claude Code: <b>${grade}</b> (${score}/100) — crit=${crit} high=${high} med=${med} low=${low}" \
    --data-urlencode "parse_mode=HTML" >/dev/null 2>&1 || true
fi

exit "$as_rc"
