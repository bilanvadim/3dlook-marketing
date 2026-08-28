#!/usr/bin/env bash
#
# sync-text-guards.sh — weekly autonomous sync of 3DLOOK text-writing guards
# from Vadim's Google Doc into the marketing_vb Claude Code project.
#
# Run by Hermes cron (no_agent=true) every Monday 12:00.
# It switches into the marketing_vb profile, asks Claude Code (via Google Drive
# MCP) to re-read the doc and update the project's guards, then reports.
#
set -uo pipefail

# Ensure cron's restricted PATH can find our toolchain
export PATH="$HOME/.local/bin:$HOME/.hermes/node/bin:$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:$PATH"

DEV_DIR="$HOME/3dlook-marketing/claude_code/DEV"
PROJ_DIR="$HOME/3dlook-marketing/marketing_vb"
PROFILE="marketing_vb"
DOC_ID="1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214"
DOC_URL="https://docs.google.com/document/d/${DOC_ID}/edit?usp=sharing"

# Locate claude binary (npm global may not be on cron PATH)
CLAUDE_BIN="$(command -v claude 2>/dev/null || echo "$HOME/.local/bin/claude")"
if [ ! -x "$CLAUDE_BIN" ]; then
  echo "ERROR: claude binary not found on PATH or $HOME/.npm-global/bin/claude"
  exit 1
fi

PROMPT_FILE="$(mktemp)"
cat > "$PROMPT_FILE" <<EOF
Use your Google Drive MCP tool (claude.ai Google Drive) to read the ENTIRE Google Doc at ${DOC_URL} (doc ID ${DOC_ID}). It is the living guidelines doc "General Approach & Language Guardrails for Corporate Content — 3DLOOK" (owner asselya@3dlook.me). It contains rules on how to write corporate texts: construction rules, word bans, style/voice directives, quality bars.

This is the WEEKLY scheduled sync run. Each week:
1) Re-read the whole document fresh.
2) Diff its current rules against the project's text-writing guards. Determine whether anything is NEW or CHANGED since the last sync.
3) If something changed: update the project's guards consistently across ALL of these targets (do NOT create a second divergent file — the canonical guard file is brand-assets/content-strategy/terminology-guardrails.md):
   - brand-assets/content-strategy/terminology-guardrails.md  (canonical — rewrite/amend here)
   - CLAUDE.md  (§6 canonical bullet + hard-ban table + override block; §15 requirement #7, and correct any stale requirement; §16 non-negotiables; §13 history row if a rule reversed)
   - brand-assets/style-guides/editorial-guardrails.md  (#6, #7, M1, M2, add M3 if needed)
   - brand-assets/style-guides/ai-tells-sweep.md  (add hard-fail paragraphs for new bans)
   - brand-assets/style-guides/scripts/detect-ai-tells.py  (add detector categories for new hard bans)
   - page-builder files (SKILL.md, kit-vertical-page, copy-humanisation, gates-and-scorecard)
   - the 8 agents: seo-writer, seo-editor, seo-publisher, brand-checker, post-drafter, post-brand-checker, message-sequencer, data-lifecycle-writer (reference terminology-guardrails.md by name)
   Keep existing project context; ADD/AMEND. Preserve dated override notes where a doc rule reverses an older project rule (do NOT retro-edit already-published articles).
4) If NOTHING changed: do NOT commit, do NOT push — just report "no changes since last sync".
5) If changed: commit + push:
   git add -A && git commit -m 'chore(guards): weekly sync text-writing guards from Google Doc ${DOC_ID}' && git push origin HEAD
   (no force-push; never commit .env/secrets; if git add -A would sweep unrelated pre-existing work, commit ONLY the guard files explicitly.)
6) Report concisely: did the doc change? what changed? exact file paths updated + commit hash (or "no changes").

All guards in English. Translate the doc's rules into clear English guards.
EOF

cd "$DEV_DIR" || { echo "ERROR: DEV_DIR missing"; exit 1; }
./switch-profile.sh "$PROFILE" >/dev/null 2>&1
cd "$PROJ_DIR" || { echo "ERROR: PROJ_DIR missing"; exit 1; }

run_claude() {
  local extra="${1:-}"
  "$CLAUDE_BIN" -p "$(cat "$PROMPT_FILE")${extra}" --output-format json --max-turns 30 --dangerously-skip-permissions 2>/dev/null
}

OUT="$(run_claude)"

# Resume loop on max_turns (up to 3 more continuations)
for i in 1 2 3; do
  # See the pipefail/grep -q note: $OUT is a full `claude -p` payload, easily large
  # enough for grep to exit before the writer finishes.
  if [ -n "$(printf '%s' "$OUT" | grep -F '"subtype":"error_max_turns"' || true)" ]; then
    SID="$(echo "$OUT" | python3 -c 'import sys,json
try:
    print(json.load(sys.stdin).get("session_id",""))
except Exception:
    print("")' 2>/dev/null)"
    [ -z "$SID" ] && break
    OUT="$(run_claude $'\n\nContinue exactly where you stopped, without restarting. Finish the weekly guard sync: the doc is already read, finish updating guards if changed, then commit and push.')"
  else
    break
  fi
done

rm -f "$PROMPT_FILE"

# Extract result text for delivery
echo "$OUT" | python3 -c '
import sys, json
raw = sys.stdin.read()
try:
    d = json.loads(raw)
except Exception:
    print("SYNC-RESULT (raw, unparsable JSON):")
    print(raw[:3000])
    sys.exit(0)
sub = d.get("subtype","?")
res = d.get("result","(no result field)")
print("SUBTYPE:", sub)
print(res)
'
