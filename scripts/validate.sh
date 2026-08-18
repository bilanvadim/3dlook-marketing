#!/usr/bin/env bash
# validate.sh [profile] — static checks on the REPO. No runtime, no network, no services.
#
# This is the CI entry point, so every check must hold on a bare clone with no deployment
# anywhere: parse what claims to be parseable, prove the profiles are complete and mutually
# consistent, and prove no secret ever entered git. Runtime health is doctor.sh's job.
#
# Exit: 0 clean, 1 broken, 2 warnings only.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

# CI has no profile, so the profile-specific section is skipped rather than fatal.
PROFILE_ARG="${1:-}"
HAVE_PROFILE=0
if [ -n "$PROFILE_ARG" ] || [ -f "$REPO_ROOT/config/profiles/$(id -un).vars" ]; then
  load_profile "$PROFILE_ARG" && HAVE_PROFILE=1
fi

hdr "profiles"
shopt -s nullglob
profiles=("$REPO_ROOT"/config/profiles/*.vars)
[ "${#profiles[@]}" -gt 0 ] || bad "no config/profiles/*.vars found"
REQUIRED=(PROFILE_USER PROFILE_HOME PROFILE_DEST PROFILE_OWNER PROFILE_GH_OWNER
          PROFILE_PROJECT_ROOT PROFILE_HO_WEBHOOK_PORT PROFILE_QDRANT_HTTP_PORT
          PROFILE_QDRANT_GRPC_PORT PROFILE_PROXY_AGENTIC_PORT PROFILE_PROXY_STRONG_PORT
          PROFILE_CONDUCTOR_DB PROFILE_ROLE)
for f in "${profiles[@]}"; do
  name="$(basename "$f" .vars)"
  missing=()
  for k in "${REQUIRED[@]}"; do grep -qE "^$k=" "$f" || missing+=("$k"); done
  if [ "${#missing[@]}" -gt 0 ]; then bad "$name is missing: ${missing[*]}"; else ok "$name has every required value"; fi
  # A two-word value must be quoted: these files are `source`d, so `PROFILE_OWNER=Vadim Bilan`
  # runs `Bilan` as a command and the variable keeps only the first word. Cost me one failed run.
  while IFS= read -r line; do
    case "$line" in
      *=*[[:space:]]*) v="${line#*=}"; case "$v" in \"*\"|\'*\') :;; *) bad "$name: unquoted value with a space → $(printf '%s' "${line%%=*}")";; esac;;
    esac
  done < <(grep -E '^[A-Z_]+=' "$f")
  # Secrets must never appear here, even by accident.
  if grep -qiE '^[A-Z_]*(API_KEY|TOKEN|SECRET|PASSWORD|API_HASH)=.+' "$f"; then
    bad "$name looks like it contains a SECRET — profiles are committed; secrets never are"
  fi
done

hdr "port assignments are unique across profiles"
clash=0
for k in PROFILE_HO_WEBHOOK_PORT PROFILE_QDRANT_HTTP_PORT PROFILE_QDRANT_GRPC_PORT \
         PROFILE_PROXY_AGENTIC_PORT PROFILE_PROXY_STRONG_PORT; do
  vals="$(for f in "${profiles[@]}"; do sed -n "s/^$k=//p" "$f" | tr -d '"'; done)"
  dupe="$(printf '%s\n' "$vals" | sort | uniq -d)"
  [ -n "$dupe" ] && { bad "$k is claimed twice: $dupe"; clash=1; }
done
# Also across DIFFERENT keys: one process cannot bind a port twice, and 6343 for one user's
# qdrant and another user's proxy is the same collision as two identical keys.
allports="$(for f in "${profiles[@]}"; do grep -E '^PROFILE_[A-Z_]*PORT=' "$f" | cut -d= -f2 | tr -d '"'; done)"
dupe_any="$(printf '%s\n' "$allports" | sort | uniq -d)"
[ -n "$dupe_any" ] && { bad "port(s) used more than once anywhere: $(printf '%s' "$dupe_any" | tr '\n' ' ')"; clash=1; }
[ "$clash" = 0 ] && ok "every port in every profile is distinct"

hdr "JSON parses"
jn=0
while IFS= read -r f; do
  python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$f" 2>/dev/null || bad "invalid JSON: ${f#"$REPO_ROOT"/}"
  jn=$((jn+1))
done < <(find "$REPO_ROOT/agents-ai" -name '*.json' -not -path '*/node_modules/*' -not -name 'package-lock.json' 2>/dev/null)
ok "$jn JSON file(s) checked"

hdr "shell scripts parse"
sn=0
while IFS= read -r f; do
  bash -n "$f" 2>/dev/null || bad "syntax error: ${f#"$REPO_ROOT"/}"
  sn=$((sn+1))
done < <(find "$REPO_ROOT/scripts" "$REPO_ROOT/agents-ai" -name '*.sh' -not -path '*/node_modules/*' 2>/dev/null; echo "$REPO_ROOT/install.sh")
ok "$sn shell script(s) checked"

hdr "python compiles"
pn=0
while IFS= read -r f; do
  python3 -m py_compile "$f" 2>/dev/null || bad "does not compile: ${f#"$REPO_ROOT"/}"
  pn=$((pn+1))
done < <(find "$REPO_ROOT/agents-ai" -name '*.py' -not -path '*/node_modules/*' -not -path '*/venv/*' 2>/dev/null)
ok "$pn python file(s) checked"
find "$REPO_ROOT" -name '__pycache__' -path '*/agents-ai/*' -prune -exec rm -rf {} + 2>/dev/null || true

hdr "the substitution table has one meaning"
# render.sh keeps its own copy (it must work standalone) and lib.sh mirrors it for the read-only
# scripts. A mirror that drifts is worse than a duplicate you know about: diff.sh once carried a
# stale copy, classified 30 correctly rendered files as DRIFT, and update.sh refused to run.
rules_render="$(grep -oE 's\|@[A-Z]+@\|\$PROFILE_[A-Z_]+\|g' "$REPO_ROOT/scripts/render.sh" | sort)"
rules_lib="$(grep -oE 's\|@[A-Z]+@\|\$PROFILE_[A-Z_]+\|g' "$REPO_ROOT/scripts/lib.sh" | sort)"
if [ -z "$rules_render" ]; then
  bad "render.sh has no substitution rules at all"
elif [ "$rules_render" = "$rules_lib" ]; then
  ok "render.sh and lib.sh agree on $(printf '%s\n' "$rules_render" | wc -l) rule(s)"
else
  bad "render.sh and lib.sh disagree on the substitution table"
  diff <(printf '%s\n' "$rules_render") <(printf '%s\n' "$rules_lib") | sed 's/^/      /'
fi

# TEMPLATE OR RUNTIME? The invariant to check is the opposite in each, and asserting the template's
# one against a rendered tree produced four confident failures on a perfectly healthy runtime — the
# exact false alarm that teaches people to ignore a check. INSTALL.md tells operators to run this
# script, so it has to be right in both places.
TOKENS_PRESENT=0
for t in '@DEST@' '@HOME@' '@USER@'; do
  [ "$(grep -rlI -F "$t" "$REPO_ROOT/agents-ai" 2>/dev/null | wc -l)" -gt 0 ] && TOKENS_PRESENT=1
done

if [ "$TOKENS_PRESENT" = 1 ]; then
hdr "template: hard-codes nobody's paths"
# THE invariant that keeps §4 from rotting back. The tree used to carry the author's real paths as
# fact, so rendering was a no-op for one profile and a rewrite for the other — the "template" was
# one user's tree that happened to work for him. A single re-introduced absolute path makes one
# profile's render silently incomplete, and the symptom is a runtime loading another account's
# plugin marketplaces by absolute path.
#
# The check is about PATHS, not mentions, and that distinction is load-bearing. Prose sometimes has
# to name the other account on purpose: vps-maintenance/SKILL.md says "do not kill processes owned
# by other users (vadim_prod, root)", and tokenising that would render to "do not kill processes
# owned by <yourself>" — the rule inverted. Test fixtures are excluded for the same reason:
# signature.test.ts asserts that six real 128-char paths share their first 80 characters, which
# only holds for a fixed literal.
leaked=0
for f in "${profiles[@]}"; do
  u="$(sed -n 's/^PROFILE_USER=//p' "$f" | tr -d '"')"
  [ -n "$u" ] || continue
  hits="$(grep -rlIE --exclude-dir=test --exclude-dir=node_modules \
            -e "/srv/$u([/\"' ]|$)" -e "/home/$u([/\"' ]|$)" "$REPO_ROOT/agents-ai" 2>/dev/null || true)"
  if [ -n "$hits" ]; then
    n="$(printf '%s\n' "$hits" | wc -l)"
    bad "$n file(s) hard-code a path under /srv/$u or /home/$u — use @DEST@ / @HOME@ / @USER@"
    printf '%s\n' "$hits" | head -5 | sed "s|$REPO_ROOT/|      |"
    leaked=1
  fi
done
[ "$leaked" = 0 ] && ok "no absolute path names any profile's account"
for t in '@DEST@' '@HOME@' '@USER@'; do
  c="$(grep -rlI -F "$t" "$REPO_ROOT/agents-ai" 2>/dev/null | wc -l || true)"
  if [ "${c:-0}" -gt 0 ]; then ok "$t present in ${c} file(s)"
  else bad "$t appears nowhere — the template cannot render to a working tree"; fi
done

else
hdr "rendered runtime: the paths are THIS profile's"
# A rendered tree must satisfy the mirror image: no token left unsubstituted, and no path belonging
# to a DIFFERENT account — that one is the real danger, because Claude Code resolves plugin
# marketplaces by absolute path and would load somebody else's.
if [ "$HAVE_PROFILE" = 1 ]; then
  own="$(grep -rlI -F "/srv/$PROFILE_USER" "$REPO_ROOT/agents-ai" 2>/dev/null | wc -l)"
  [ "${own:-0}" -gt 0 ] && ok "$own file(s) carry this profile's paths" \
    || bad "no path under /srv/$PROFILE_USER anywhere — this tree was never rendered"
  foreign=0
  for f in "${profiles[@]}"; do
    o="$(sed -n 's/^PROFILE_USER=//p' "$f" | tr -d '"')"
    [ -n "$o" ] && [ "$o" != "$PROFILE_USER" ] || continue
    hits="$(grep -rlIE --exclude-dir=test --exclude-dir=node_modules \
              -e "/srv/$o([/\"' ]|$)" -e "/home/$o([/\"' ]|$)" "$REPO_ROOT/agents-ai" 2>/dev/null || true)"
    if [ -n "$hits" ]; then
      bad "$(printf '%s\n' "$hits" | wc -l) file(s) point at $o's tree — this runtime would load their plugins"
      printf '%s\n' "$hits" | head -5 | sed "s|$REPO_ROOT/|      |"; foreign=1
    fi
  done
  [ "$foreign" = 0 ] && ok "no path belongs to another account"
else
  warn "rendered tree but no profile resolved — cannot say whose paths these should be"
fi
ok "no unsubstituted token remains (that is how this branch was chosen)"
fi

hdr "every system has the safety baseline"
# Only `dev` had a .claude/ baseline. An interactive session opened in any other system directory
# therefore ran with no deny list and no PreToolUse hook — and that is the SAME config an autonomous
# run inherits when its work_dir happens to be a system dir.
#
# guard.py is ONE file with symlinks pointing at it, not five copies. Five copies drift: that is
# exactly how the absolute-path `rm -rf` hole survived on the canonical guard after being fixed on
# the other account, and how diff.sh's private substitution table went stale. A symlink cannot
# silently disagree with its target.
SYSDIR="$REPO_ROOT/agents-ai/telegram-bot-agent/claude-code-agent/DEV"
canon_guard="$SYSDIR/dev/.claude/hooks/guard.py"
[ -f "$canon_guard" ] || bad "the canonical guard is missing: dev/.claude/hooks/guard.py"
missing=0; badlink=0
for pf in "$SYSDIR"/../DEV/profiles/*.json; do
  [ -e "$pf" ] || continue
  sysname="$(basename "$pf" .json)"
  sd="$SYSDIR/$sysname"
  [ -d "$sd" ] || continue                     # a profile may compose marketplaces it does not own
  st="$sd/.claude/settings.json"; gd="$sd/.claude/hooks/guard.py"
  if [ ! -f "$st" ]; then bad "$sysname has no .claude/settings.json"; missing=1; continue; fi
  python3 -c "
import json,sys
d=json.load(open(sys.argv[1]))
p=d.get('permissions',{})
assert p.get('deny'), 'no deny rules'
h=(d.get('hooks') or {}).get('PreToolUse') or []
assert any('guard.py' in x.get('command','') for e in h for x in (e.get('hooks') or [])), 'no guard hook'
" "$st" 2>/dev/null || { bad "$sysname settings.json has no deny list or no guard hook"; missing=1; }
  if [ ! -e "$gd" ]; then bad "$sysname guard.py is missing or a dangling symlink"; badlink=1
  elif [ "$sysname" != dev ]; then
    # It must BE the canonical guard, not a copy that merely looks like it.
    [ "$(readlink -f "$gd")" = "$(readlink -f "$canon_guard")" ] \
      || { bad "$sysname guard.py is not the canonical one ($(readlink "$gd" 2>/dev/null || echo 'a plain copy'))"; badlink=1; }
  fi
done
[ "$missing" = 0 ] && ok "every system directory carries settings.json with a deny list and the guard hook"
[ "$badlink" = 0 ] && ok "every system's guard.py resolves to the one canonical file"

# The guard's own regression harness must pass, and it must actually contain the case that the
# canonical guard used to fail: a recursive delete of a NAMED absolute path.
if [ -f "$SYSDIR/dev/.claude/hooks/test-guard.py" ]; then
  if python3 "$SYSDIR/dev/.claude/hooks/test-guard.py" >/tmp/.vg.$$ 2>&1; then
    ok "guard regression suite passes ($(grep -c '  ok' /tmp/.vg.$$) cases)"
  else
    bad "guard regression suite FAILED"; grep FAIL /tmp/.vg.$$ | head -5 | sed 's/^/      /'
  fi
  rm -f /tmp/.vg.$$
  grep -q 'rm -rf /home/' "$SYSDIR/dev/.claude/hooks/test-guard.py" \
    && ok "the harness covers a named absolute path" \
    || bad "the harness has no case for `rm -rf /<named path>` — the hole it missed once"
else
  warn "no test-guard.py — the guard has no regression suite"
fi

hdr "no secrets in the tree"
# SCANS WHAT GIT TRACKS, not the working directory. The purpose is "no secret ever entered git", and
# a runtime working tree legitimately contains secrets: conductor/.env holds this account's Telegram
# token, gitignored and 0600. Scanning the filesystem flagged that as a leak on vadim_prod — a
# confident failure about a file that is correctly ignored and was never committed.
#
# And it PRINTED PART OF THE TOKEN while doing so. A check that exists to keep secrets out of the
# repo must not put one in a terminal, a log or a CI transcript; SECRETS.md says exactly that. Only
# the file and line are reported now — the matched value never is.
#
# Shapes, not names: a variable called FOO can still hold a bot token.
leak=0
while IFS= read -r hit; do
  case "$hit" in *".example:"*|*"secrets.env.example"*) continue;; esac
  bad "possible secret in a TRACKED file: ${hit}"
  leak=1
done < <(git -C "$REPO_ROOT" ls-files -z 2>/dev/null \
  | xargs -0 -r grep -InIE \
      -e '[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}' \
      -e 'sk-[A-Za-z0-9]{32,}' \
      -e 'gh[pousr]_[A-Za-z0-9]{36,}' \
      -e 'AIza[A-Za-z0-9_-]{30,}' 2>/dev/null \
  | cut -d: -f1,2)
[ "$leak" = 0 ] && ok "no token-shaped string in any tracked file"

# Belt and braces: the runtime files that DO hold secrets must be ignored, not merely absent from
# the index today. `git check-ignore` answers the question that matters — would a careless
# `git add -A` pick this up?
for f in agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor/.env; do
  if [ -e "$REPO_ROOT/$f" ]; then
    if git -C "$REPO_ROOT" check-ignore -q "$f" 2>/dev/null; then ok "$f exists and is ignored"
    else bad "$f exists and is NOT ignored — one `git add -A` from being committed"; fi
  fi
done

hdr ".gitignore actually covers the runtime files"
for pat in '.env' 'config.yaml' 'auth.json' '*.db' '*.session' '*.enc' 'node_modules'; do
  grep -qF -- "$pat" "$REPO_ROOT/.gitignore" 2>/dev/null && ok "ignores $pat" || bad "'.gitignore' does not cover $pat"
done
# The rule that already bit once: *.env is ignored, so anything that MUST be tracked cannot
# use that extension. Profiles are .vars for exactly this reason — assert it stays that way.
if [ -n "$(find "$REPO_ROOT/config/profiles" -name '*.env' 2>/dev/null)" ]; then
  bad "config/profiles contains a *.env file — it is gitignored and would be silently untracked"
else
  ok "profiles use *.vars, so .gitignore cannot swallow them"
fi

hdr "conductor"
CD="$REPO_ROOT/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor"
if [ -d "$CD/node_modules" ]; then
  ( cd "$CD" && npx --no-install tsc --noEmit 2>&1 | head -5 ) && ok "typecheck clean" || bad "typecheck failed"
  if ( cd "$CD" && npm test >/tmp/.validate-tests.$$ 2>&1 ); then
    ok "tests pass ($(grep -cE 'ok  ' /tmp/.validate-tests.$$) assertions)"
  else
    bad "tests FAILED"; grep -E 'FAIL' /tmp/.validate-tests.$$ | head -8 | sed 's/^/      /'
  fi
  rm -f /tmp/.validate-tests.$$
else
  warn "conductor node_modules absent — skipping typecheck/tests (CI must run npm ci first)"
fi
# The schema's profile CHECK has to admit every profile that ships as a file, or enqueueing
# against one fails with a bare constraint error and no hint why.
if [ -f "$CD/sql/schema.sql" ]; then
  allowed="$(sed -n "s/.*check (profile in (\(.*\))).*/\1/p" "$CD/sql/schema.sql" | tr -d "' " | tr '\n' ',')"
  [ -z "$allowed" ] && allowed="$(grep -A2 'check (profile in' "$CD/sql/schema.sql" | tr -d "\n' " )"
  for pf in "$REPO_ROOT"/agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles/*.json; do
    n="$(basename "$pf" .json)"
    case "$allowed" in *"$n"*) :;; *) bad "profile '$n' ships as a file but the ho_jobs CHECK rejects it";; esac
  done
  ok "schema CHECK covers the shipped profiles"
fi

if [ "$HAVE_PROFILE" = 1 ]; then
  hdr "profile $PROFILE_NAME: referenced paths exist"
  for p in "$PROFILE_HOME" "$PROFILE_PROJECT_ROOT"; do
    [ -d "$p" ] && ok "exists: $p" || warn "missing: $p"
  done
fi

finish
