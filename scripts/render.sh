#!/usr/bin/env bash
# render.sh — turn a clean checkout of this repo into ONE user's runtime tree.
#
#   scripts/render.sh <profile> [--tree DIR] [--check] [--verbose]
#
#   <profile>   name of a file in config/profiles/<profile>.vars
#   --tree DIR  tree to render (default: the profile's PROFILE_DEST)
#   --check     report what WOULD change and exit non-zero if anything would; touches nothing
#   --verbose   list every file rendered
#
# WHY THIS EXISTS
#
# The repo is one source of truth for two isolated users, so it cannot contain either user's
# absolute paths as fact. It carries the author's paths, and the per-user values live in
# config/profiles/*.vars. Rendering is what turns that template into a runtime tree — the one
# Claude Code loads plugin marketplaces and profiles from, by absolute path.
#
# It has to be a SEPARATE, RE-RUNNABLE step rather than a stanza inside install.sh, because
# `git pull` overwrites tracked files with the author's paths again and nothing else puts the
# user's values back. Under the clean-clone → render model those local modifications are
# DISPOSABLE by design: an update discards them, pulls, and re-renders.
#
# IDEMPOTENT: after one pass there is nothing left to change, so it is safe to run after every
# update, and `--check` is what doctor/diff use to tell a MISSED RENDER from real drift.
set -uo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SELF_DIR/.." && pwd)"

die(){ echo "render: $*" >&2; exit 1; }

PROFILE=""; TREE=""; CHECK=0; VERBOSE=0
while [ $# -gt 0 ]; do
  case "$1" in
    --tree) TREE="${2:-}"; shift 2;;
    --check) CHECK=1; shift;;
    --verbose|-v) VERBOSE=1; shift;;
    -h|--help) sed -n '2,20p' "$0"; exit 0;;
    -*) die "unknown option: $1";;
    *) [ -z "$PROFILE" ] || die "only one profile at a time"; PROFILE="$1"; shift;;
  esac
done
[ -n "$PROFILE" ] || die "usage: render.sh <profile> [--tree DIR] [--check]"

PROFILE_FILE="$REPO_ROOT/config/profiles/$PROFILE.vars"
[ -f "$PROFILE_FILE" ] || die "no such profile: $PROFILE_FILE"

# shellcheck disable=SC1090
set -a; . "$PROFILE_FILE"; set +a

for v in PROFILE_USER PROFILE_HOME PROFILE_DEST PROFILE_OWNER PROFILE_GH_OWNER PROFILE_PROJECT_ROOT; do
  [ -n "${!v:-}" ] || die "$PROFILE_FILE is missing $v"
done

[ -n "$TREE" ] || TREE="$PROFILE_DEST"
TREE="${TREE%/}"
[ -d "$TREE" ] || die "tree not found: $TREE"
[ -d "$TREE/agents-ai" ] || die "$TREE does not look like this repo (no agents-ai/)"

# SCOPE: the path tokens. NOT the identity tokens.
#
# @DEST@ / @HOME@ / @USER@ are this script's. @OWNER@ / @GH_OWNER@ / @PROJECT_ROOT@ are NOT: they
# are substituted where they belong — when a template is deployed into ~/.hermes, by install.sh
# and then by hermes-update.py's _render_identity() on every update, reading HERMES_OWNER /
# HERMES_GH_OWNER / HERMES_PROJECT_ROOT from ~/.hermes/.env.
#
# Doing identity here as well would be duplicate ownership of one decision, and actively harmful:
# hermes-update.py contains the strings ("@OWNER@", "HERMES_OWNER") as CODE, so a blind tree-wide
# substitution rewrites the renderer's own token table and breaks every future update.
#
# The template used to carry the author's REAL paths instead of tokens, which meant rendering was
# a no-op for one profile and a 30-file rewrite for the other — the template was one user's tree
# that happened to work for him. Now no tree is anyone's flavour: every runtime is produced the
# same way, and a tree that was never rendered is obviously broken rather than subtly wrong.
#
# @DEST@ FIRST: it is the longest token and its expansion contains the others' expansions. Doing
# /srv/@USER@ first would leave @DEST@ half-substituted.
# DEFINED HERE, and lib.sh mirrors it for the read-only scripts.
#
# render.sh does not source lib.sh, deliberately: it must run on a bare clone with nothing else in
# place, and it is the one script whose failure leaves a tree UNUSABLE. Making it call into lib.sh
# proved that the hard way — `render_candidates: command not found`, an empty substitution table,
# and a cheerful "fully rendered — nothing to do" over a live tree that had just been reset to
# template form. 30 files, every profile JSON pointing at a literal "@DEST@/...", and doctor.sh
# reported clean because its render check calls the same broken script.
#
# Two copies of three lines is the lesser evil here. validate.sh asserts they stay identical.
#
# @DEST@ FIRST: it is the longest token and its expansion contains the others' expansions.
SED_SCRIPT="
s|@DEST@|$PROFILE_DEST|g
s|@HOME@|$PROFILE_HOME|g
s|@USER@|$PROFILE_USER|g
"

# A file is a target only if rendering would ACTUALLY CHANGE it — not merely because it
# contains a marker.
#
# Grepping for markers was the obvious approach and it was wrong while the template carried the
# author's real paths: there, `sergiy_prod → sergiy_prod` was a no-op, so a marker scan called all
# 39 files that merely mention the account "unrendered". With tokens a marker scan would in fact
# be equivalent — but comparing bytes stays correct no matter what the substitution table becomes,
# and a --check that cries drift on a correct tree trains you to ignore it.
#
# So: cheap grep to shortlist candidates (-I skips binaries — a stray match inside a .db or
# an image would corrupt it), then compare the rendered bytes to decide.
#
# *.example files are EXCLUDED, and that is not an optimisation. They exist to be copied and
# filled in by a human, so the placeholders inside them are the instructions, not a defect.
# Rendering one bakes in a single user's value and it silently stops being an example — the
# next person copies qdrant.env.example and inherits somebody else's storage path and ports.
mapfile -t CANDIDATES < <(grep -rlI --exclude='*.example' \
  -e '@DEST@' -e '@HOME@' -e '@USER@' "$TREE/agents-ai" 2>/dev/null | sort)

TARGETS=()
for f in "${CANDIDATES[@]}"; do
  sed "$SED_SCRIPT" "$f" 2>/dev/null | cmp -s - "$f" || TARGETS+=("$f")
done

if [ "${#TARGETS[@]}" -eq 0 ]; then
  # "Nothing to render" and "I failed to look" are indistinguishable to a caller, and the second
  # one over a freshly reset tree is how a live runtime ends up full of literal @DEST@ paths while
  # every script reports success. So prove the substitution table is non-empty before claiming it.
  case "$SED_SCRIPT" in
    *'@DEST@'*) : ;;
    *) echo "render: substitution table is EMPTY — refusing to report success" >&2; exit 1;;
  esac
  echo "render: $TREE is fully rendered for $PROFILE ($PROFILE_USER) — nothing to do"
  exit 0
fi

if [ "$CHECK" = 1 ]; then
  echo "render --check: ${#TARGETS[@]} file(s) in $TREE would change under profile $PROFILE:"
  for f in "${TARGETS[@]}"; do echo "  ${f#"$TREE"/}"; done
  exit 1
fi

n=0
for f in "${TARGETS[@]}"; do
  sed -i "$SED_SCRIPT" "$f" || die "sed failed on $f"
  n=$((n+1))
  [ "$VERBOSE" = 1 ] && echo "  rendered ${f#"$TREE"/}"
done

# Unit files live outside agents-ai/ once installed, so they are handled by whoever
# installs them (install.sh) — this pass deliberately covers only the repo tree, which is
# the thing `git pull` overwrites.
echo "render: $n file(s) → user=$PROFILE_USER home=$PROFILE_HOME dest=$PROFILE_DEST"
echo "        owner='$PROFILE_OWNER' ($PROFILE_GH_OWNER) projects=$PROFILE_PROJECT_ROOT"

# Prove it converged twice over: no path token may survive, and a second pass must find nothing
# left to change. The token check is now meaningful — with the author's paths gone from the
# template, a surviving @USER@ is unambiguously a bug rather than a legitimate mention.
left=0
for f in "${TARGETS[@]}"; do
  sed "$SED_SCRIPT" "$f" 2>/dev/null | cmp -s - "$f" || left=$((left+1))
done
tokens_left="$(grep -rlI --exclude='*.example' -e '@DEST@' -e '@HOME@' -e '@USER@' \
  "$TREE/agents-ai" 2>/dev/null | wc -l)"
if [ "$left" != "0" ] || [ "${tokens_left:-0}" != "0" ]; then
  [ "$left" != 0 ] && echo "render: WARNING — $left file(s) would still change on a second pass" >&2
  [ "${tokens_left:-0}" != 0 ] && {
    echo "render: WARNING — $tokens_left file(s) still contain a path token:" >&2
    grep -rlI --exclude='*.example' -e '@DEST@' -e '@HOME@' -e '@USER@' "$TREE/agents-ai" | head -5 >&2; }
  exit 1
fi
exit 0
