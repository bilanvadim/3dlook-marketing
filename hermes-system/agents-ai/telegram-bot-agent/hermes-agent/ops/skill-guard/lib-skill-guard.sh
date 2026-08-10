# lib-skill-guard.sh — two-layer security gate for installing Claude Code skills.
# Sourced, not executed.
#
# Why two layers: AgentShield (npx ecc-agentshield) audits Claude Code CONFIG
# surface — settings.json permissions, hooks, MCP configs, agent definitions.
# It does NOT read SKILL.md prose (a skill dir with only a SKILL.md scans as
# "0 files, grade A"). So a skill's real danger surface — instructions telling
# an agent to pipe-to-shell, exfiltrate secrets, or grant Bash(*) — needs a
# separate content scan. Both must pass before install.

# ── Layer 2: deterministic content scan of SKILL.md + bundled scripts ────────
# Echoes findings to stderr; returns 0 = clean, 1 = danger found.
sg_content_scan() {
  local dir="$1" hits=0
  # Files a skill can carry that execute or instruct.
  #
  # NUL-delimited into an array, not a newline-joined string. The string form was
  # interpolated unquoted into grep, so a single space in a path word-split it
  # into non-existent fragments, grep matched nothing and the scan reported
  # "clean" — a hostile skill defeated all six patterns at once by naming its
  # folder "My Skill/". Verified before and after this change.
  #
  # The extension list also stopped at six; a payload in .mjs/.cjs/.rb/.yaml or a
  # Makefile was simply never read. Scan every text file instead and let grep's
  # -I skip binaries: a skill bundle is small, and an allowlist of extensions is
  # the wrong shape for "what might contain instructions".
  local files=()
  while IFS= read -r -d '' f; do files+=("$f"); done < <(
    find "$dir" -type f -size -2M -print0 2>/dev/null)
  (( ${#files[@]} )) || { echo "[skill-guard] no scannable files in $dir" >&2; return 1; }

  # Pattern → human label. Any match = block (these are unambiguous red flags
  # for an unattended installer; a legit skill rarely needs them verbatim).
  sg_flag() {  # <regex> <label>
    local m; m=$(grep -rEnI "$1" "${files[@]}" 2>/dev/null | head -3)
    if [[ -n "$m" ]]; then
      echo "[skill-guard] BLOCK: $2" >&2
      echo "$m" | sed 's/^/    /' >&2
      hits=$((hits+1))
    fi
  }

  sg_flag 'curl[^|]*\|[[:space:]]*(ba)?sh|wget[^|]*\|[[:space:]]*(ba)?sh|eval[[:space:]]+"\$\(curl' \
          'pipe remote content to shell (curl|sh / wget|sh / eval $(curl))'
  sg_flag 'rm[[:space:]]+-rf[[:space:]]+(/|~|\$HOME|/\*)|mkfs|dd[[:space:]]+if=|:\(\)[[:space:]]*\{[[:space:]]*:\|:' \
          'destructive command (rm -rf / , mkfs, dd, fork bomb)'
  sg_flag '(id_rsa|\.ssh/|\.aws/credentials|\.env|\.credentials\.json|GITHUB_TOKEN|ANTHROPIC_API_KEY)' \
          'references secret/credential material'
  sg_flag 'AKIA[0-9A-Z]{16}|-----BEGIN[[:space:]].*PRIVATE KEY-----|\bghp_[A-Za-z0-9]{20,}|\bsk-[A-Za-z0-9]{20,}' \
          'hardcoded secret / API key / private key'
  sg_flag 'ignore[[:space:]]+(all[[:space:]]+)?previous[[:space:]]+instructions|disregard[[:space:]]+(your|all|the)[[:space:]]|exfiltrat' \
          'prompt-injection language'
  # Unrestricted Bash in frontmatter allowed-tools.
  sg_flag '^allowed-tools:.*Bash\(\*\)|^allowed-tools:.*Bash[[:space:]]*$|"Bash\(\*\)"' \
          'grants unrestricted Bash(*)'

  if (( hits )); then
    echo "[skill-guard] content scan: $hits danger pattern(s) → FAIL" >&2
    return 1
  fi
  echo "[skill-guard] content scan: clean" >&2
  return 0
}

# ── Layer 1: AgentShield on the staged skill dir (config surface) ────────────
# Writes JSON to <out_json>. Returns 0 if no critical/high findings, 1 otherwise.
# Soft-degrades: if AgentShield can't run (offline), returns 2 (caller decides).
sg_agentshield() {
  local dir="$1" out_json="$2"
  if ! timeout 240 npx -y ecc-agentshield@latest scan \
        --path "$dir" --format json --min-severity high >"$out_json" 2>/dev/null; then
    : # non-zero exit (2 = critical findings) still writes JSON; parse below
  fi
  [[ -s "$out_json" ]] || { echo "[skill-guard] AgentShield produced no output" >&2; return 2; }
  local crit high
  crit=$(python3 -c "import json;print(json.load(open('$out_json'))['summary']['critical'])" 2>/dev/null || echo 0)
  high=$(python3 -c "import json;print(json.load(open('$out_json'))['summary']['high'])" 2>/dev/null || echo 0)
  echo "[skill-guard] AgentShield: critical=$crit high=$high" >&2
  (( crit == 0 && high == 0 )) && return 0
  return 1
}

# ── optional Layer 3: semantic review via Claude Code (best-effort) ───────────
# Only runs if claude is on PATH and not rate-limited. Returns 0=approve,
# 1=reject, 2=unavailable/skipped. Never blocks on its own unless it says reject.
sg_claude_review() {
  local dir="$1"
  command -v claude >/dev/null 2>&1 || return 2
  local verdict
  verdict=$(cd "$dir" && timeout 180 claude -p \
    "Read every file in this directory (a Claude Code skill). Decide if it is safe to install for an autonomous agent with broad permissions. Reply with EXACTLY one word on the first line: SAFE or UNSAFE." \
    --allowedTools "Read,Glob,Grep" --max-turns 8 --output-format text 2>/dev/null \
    | grep -oiE '\b(SAFE|UNSAFE)\b' | head -1 | tr '[:lower:]' '[:upper:]')
  case "$verdict" in
    SAFE)   echo "[skill-guard] Claude review: SAFE" >&2;   return 0 ;;
    UNSAFE) echo "[skill-guard] Claude review: UNSAFE" >&2; return 1 ;;
    *)      echo "[skill-guard] Claude review: unavailable/inconclusive" >&2; return 2 ;;
  esac
}

sg_notify() {  # best-effort Telegram
  [[ -n "${TELEGRAM_BOT_TOKEN:-}" && -n "${TELEGRAM_CHAT_ID:-}" ]] || return 0
  curl -fsS -m 10 -X POST \
    "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=$1" --data-urlencode "parse_mode=HTML" >/dev/null 2>&1 || true
}
