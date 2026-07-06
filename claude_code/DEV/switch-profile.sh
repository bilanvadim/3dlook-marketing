#!/usr/bin/env bash
# switch-profile.sh — activate exactly one Claude Code "system" (profile).
#
# A profile (profiles/<name>.json) declares which marketplaces to register and
# which plugins to enable. Switching rewrites ~/.claude/settings.json's
# enabledPlugins to EXACTLY that set (mutual exclusion), so only one system's
# agents/skills/commands load. A Claude Code RESTART is required to apply.
#
# Usage:
#   switch-profile.sh <dev|seo|marketing|security|marketing_vb|marketing_vb_sm>   activate a profile
#   switch-profile.sh --list                          list available profiles
#   switch-profile.sh --current                       show the active profile
#
# Honors $CLAUDE_CONFIG_DIR (defaults to ~/.claude).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROFILES_DIR="$SCRIPT_DIR/profiles"
CONFIG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
SETTINGS="$CONFIG_DIR/settings.json"
ACTIVE_FILE="$CONFIG_DIR/.active-profile"

die() { echo "ERROR: $*" >&2; exit 1; }
command -v claude >/dev/null 2>&1 || die "claude CLI not found in PATH"
command -v python3 >/dev/null 2>&1 || die "python3 not found in PATH"

list_profiles() {
  echo "Available profiles ($PROFILES_DIR):"
  for f in "$PROFILES_DIR"/*.json; do
    [ -e "$f" ] || continue
    name="$(basename "$f" .json)"
    desc="$(python3 -c "import json,sys;print(json.load(open(sys.argv[1])).get('description',''))" "$f")"
    printf "  %-10s %s\n" "$name" "$desc"
  done
  [ -f "$ACTIVE_FILE" ] && echo && echo "Active: $(cat "$ACTIVE_FILE")"
}

case "${1:-}" in
  ""|-h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
  --list)       list_profiles; exit 0 ;;
  --current)    [ -f "$ACTIVE_FILE" ] && cat "$ACTIVE_FILE" || echo "(none set)"; exit 0 ;;
esac

PROFILE="$1"
MANIFEST="$PROFILES_DIR/$PROFILE.json"
[ -f "$MANIFEST" ] || die "unknown profile '$PROFILE' (see: $0 --list)"
[ -f "$SETTINGS" ] || die "settings not found: $SETTINGS"

echo "→ Switching to profile: $PROFILE"

# 1) Register any marketplaces this profile needs (idempotent).
existing_mkts="$(claude plugin marketplace list 2>/dev/null || true)"
while IFS=$'\t' read -r mkt_name mkt_path; do
  [ -z "$mkt_name" ] && continue
  if echo "$existing_mkts" | grep -q "\b$mkt_name\b"; then
    echo "  marketplace ok: $mkt_name"
  else
    echo "  + registering marketplace: $mkt_name → $mkt_path"
    claude plugin marketplace add "$mkt_path" >/dev/null
  fi
done < <(python3 -c "
import json,os,sys
m=json.load(open(sys.argv[1])); base=sys.argv[2]
for n,p in m.get('marketplaces',{}).items():
    print(n+'\t'+(p if os.path.isabs(p) else os.path.normpath(os.path.join(base,p))))
" "$MANIFEST" "$SCRIPT_DIR")

# 2) Ensure each target plugin is installed (idempotent).
while read -r plug; do
  [ -z "$plug" ] && continue
  claude plugin install "$plug" --scope user >/dev/null 2>&1 || true
done < <(python3 -c "
import json,sys
m=json.load(open(sys.argv[1]))
for p in m.get('enabledPlugins',[]): print(p)
" "$MANIFEST")

# 3) Rewrite settings.json enabledPlugins to EXACTLY this profile's set,
#    keep extraKnownMarketplaces in sync, preserve everything else.
python3 - "$SETTINGS" "$MANIFEST" "$SCRIPT_DIR" <<'PY'
import json, os, sys
settings_path, manifest_path, base = sys.argv[1], sys.argv[2], sys.argv[3]
with open(settings_path) as f: s = json.load(f)
with open(manifest_path) as f: m = json.load(f)

s["enabledPlugins"] = {p: True for p in m.get("enabledPlugins", [])}

known = s.get("extraKnownMarketplaces", {})
for name, path in m.get("marketplaces", {}).items():
    ap = path if os.path.isabs(path) else os.path.normpath(os.path.join(base, path))
    known[name] = {"source": {"source": "directory", "path": ap}}
s["extraKnownMarketplaces"] = known

with open(settings_path, "w") as f:
    json.dump(s, f, indent=2); f.write("\n")
PY

echo "$PROFILE" > "$ACTIVE_FILE"

echo "  enabled plugins now:"
python3 -c "
import json,sys
print('\n'.join('    - '+k for k in json.load(open(sys.argv[1]))['enabledPlugins']))
" "$SETTINGS"

echo
echo "✔ Profile '$PROFILE' is active in $SETTINGS"
echo "⚠  RESTART Claude Code for it to take effect (plugins load at session start)."
