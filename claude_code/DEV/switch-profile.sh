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

# ── SERIALISE THE SWITCH ──────────────────────────────────────────────────────
# settings.json is a single GLOBAL file, so a profile switch is a read-modify-write on
# shared mutable state. Two concurrent switches interleave and the loser's plugin set
# silently survives — and a headless `claude -p` started in between loads whichever set
# happened to land.
#
# The lock used to live only in dispatch-in-profile.sh. But this script is what
# install.sh runs, what INSTALL.md and REPRODUCE.md tell a human to run, and what every
# doc example calls — i.e. the guarded path was the one nobody uses.
#
# HERMES_PROFILE_LOCK_HELD lets dispatch-in-profile.sh keep holding the lock across its
# wider switch+verify+run window without deadlocking against this one: flock on a second
# descriptor would block on the parent's own lock forever.
LOCK="${TMPDIR:-/tmp}/hermes-profile-switch.lock"
if [ "${HERMES_PROFILE_LOCK_HELD:-0}" != "1" ]; then
  exec 9>"$LOCK"
  if ! flock -w 900 9; then
    die "could not acquire the profile lock within 900s ($LOCK) — another switch is in progress"
  fi
fi

PROFILE="$1"
MANIFEST="$PROFILES_DIR/$PROFILE.json"
[ -f "$MANIFEST" ] || die "unknown profile '$PROFILE' (see: $0 --list)"
[ -f "$SETTINGS" ] || die "settings not found: $SETTINGS"

echo "→ Switching to profile: $PROFILE"

# 0) PRE-FLIGHT, BEFORE TOUCHING ANYTHING GLOBAL.
#
# `claude plugin install --scope user` writes to ~/.claude/settings.json ITSELF. So
# validating after the install loop is too late: a profile naming one bad plugin among
# several good ones still leaves the good ones enabled in global settings, and the caller
# gets an error while the machine is in a third state that is neither the old profile nor
# the new one. Measured 2026-08-28 with a deliberately broken profile: settings.json
# gained a plugin from a switch that had "failed".
#
# So resolve every plugin OFFLINE first — the manifest names a directory, the directory
# declares its marketplace name, and the plugin has a .claude-plugin/plugin.json — and
# refuse before the first side effect.
python3 - "$MANIFEST" "$SCRIPT_DIR" <<'PYPRE' || die "profile '$PROFILE' does not resolve — nothing was changed"
import json, os, sys
manifest, base = sys.argv[1], sys.argv[2]
m = json.load(open(manifest))
mkts = m.get("marketplaces") or {}
bad = []
for key, rel in mkts.items():
    d = rel if os.path.isabs(rel) else os.path.normpath(os.path.join(base, rel))
    mp = os.path.join(d, ".claude-plugin", "marketplace.json")
    if not os.path.isfile(mp):
        bad.append(f"marketplace '{key}' -> {d} has no .claude-plugin/marketplace.json")
        continue
    declared = (json.load(open(mp)) or {}).get("name")
    if declared != key:
        bad.append(f"marketplace '{key}' -> {d} declares itself '{declared}' — "
                   f"plugins named @{key} cannot resolve")
for ep in m.get("enabledPlugins") or []:
    plug, _, key = ep.partition("@")
    rel = mkts.get(key)
    if rel is None:
        bad.append(f"plugin '{ep}' names marketplace '{key}', which this profile does not register")
        continue
    d = rel if os.path.isabs(rel) else os.path.normpath(os.path.join(base, rel))
    pj = os.path.join(d, "plugins", plug, ".claude-plugin", "plugin.json")
    if not os.path.isfile(pj):
        bad.append(f"plugin '{ep}' has no {os.path.relpath(pj, base)}")
for b in bad:
    print("  ! " + b, file=sys.stderr)
sys.exit(1 if bad else 0)
PYPRE
echo "  pre-flight ok: every marketplace and plugin resolves on disk"

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

# 2) Ensure each target plugin is installed, then ASSERT THE END STATE.
#
# `|| true` used to swallow every failure here, and step 3 wrote the plugin into
# enabledPlugins regardless — so settings.json claimed a plugin that was not installed and
# the script printed success. That is how profiles/sandbox_sm.json shipped for weeks with
# sbx-probe@ai-agents-sbx unresolvable (the marketplace declared itself 'sandbox_sm'): a
# sandbox whose whole purpose is to make a non-loading candidate obvious, reporting green.
#
# The exit code of `plugin install` is not a reliable signal on its own — an
# already-installed plugin is a normal, non-failing no-op with varying output — so the
# check is on what is actually installed AFTERWARDS.
TARGETS=()
while read -r plug; do
  [ -z "$plug" ] && continue
  TARGETS+=("$plug")
  out="$(claude plugin install "$plug" --scope user 2>&1)" || true
  case "$out" in *[Ee]rror*|*"not found"*|*"Unknown"*) echo "  ! install reported: $(printf '%s' "$out" | head -2 | tr '\n' ' ')" ;; esac
done < <(python3 -c "
import json,sys
m=json.load(open(sys.argv[1]))
for p in m.get('enabledPlugins',[]): print(p)
" "$MANIFEST")

installed="$(claude plugin list 2>/dev/null || true)"
missing=()
for plug in "${TARGETS[@]:-}"; do
  [ -z "$plug" ] && continue
  case "$installed" in *"$plug"*) : ;; *) missing+=("$plug") ;; esac
done
if [ "${#missing[@]}" -gt 0 ]; then
  die "profile '$PROFILE' names plugin(s) that are NOT installed after the attempt: ${missing[*]}
       settings.json has NOT been changed. Usually the marketplace directory declares a
       different name than the profile's key — compare profiles/$PROFILE.json against
       <dir>/.claude-plugin/marketplace.json."
fi

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

# 4) A profile may be BOUND to one directory (`runFrom` in its manifest). Systems
#    whose agents read context by relative path — marketing_vb reads brand-assets/,
#    workspace/, about-me.md that way — only work when the session starts there.
#    Record the resolved directory so the Telegram switcher uses it as a tab's
#    default cwd, and clear it for profiles that are not bound, otherwise the
#    previous system's directory would leak into the next one.
#    Relative runFrom is resolved against this script's dir, like the marketplaces.
RUN_FROM="$(python3 -c "
import json,os,sys
v = json.load(open(sys.argv[1])).get('runFrom') or ''
print(v if (not v or os.path.isabs(v)) else os.path.normpath(os.path.join(sys.argv[2], v)))
" "$MANIFEST" "$SCRIPT_DIR")"
CWD_FILE="$CONFIG_DIR/.active-profile-cwd"
if [ -n "$RUN_FROM" ]; then
  if [ -d "$RUN_FROM" ]; then
    printf '%s\n' "$RUN_FROM" > "$CWD_FILE"
    echo "  runFrom: $RUN_FROM  (recorded → $CWD_FILE)"
  else
    # Loud, not fatal: the profile is still switched, but say plainly what will
    # break. Silently falling back to the projects root is how a brand-driven
    # system ends up producing confidently generic output.
    rm -f "$CWD_FILE"
    echo "  ⚠  runFrom '$RUN_FROM' does not exist on this machine."
    echo "     '$PROFILE' expects to run FROM that directory — its agents read"
    echo "     context by relative path and will see none of it from anywhere else."
    echo "     Fix the 'runFrom' path in $MANIFEST, then switch again."
  fi
else
  rm -f "$CWD_FILE"
fi

echo "  enabled plugins now:"
python3 -c "
import json,sys
print('\n'.join('    - '+k for k in json.load(open(sys.argv[1]))['enabledPlugins']))
" "$SETTINGS"

echo
echo "✔ Profile '$PROFILE' is active in $SETTINGS"
echo "⚠  RESTART Claude Code for it to take effect (plugins load at session start)."
[ -n "$RUN_FROM" ] && [ -d "$RUN_FROM" ] && echo "→  Start it from there:  cd $RUN_FROM && claude"
