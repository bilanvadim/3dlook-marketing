#!/usr/bin/env bash
# diff.sh [profile] [--full|--porcelain] — what differs between this tree and the repo. Read-only.
#
# Local modifications are NORMAL here: render.sh rewrites tracked files with this profile's
# paths, so `git status` in a deployed tree is never clean and cannot be read as "drift". That
# is precisely why a dedicated script is needed — it splits the modifications into
#
#   RENDER   — explained entirely by this profile's substitutions. Expected. Disposable.
#   DRIFT    — someone (or something) edited the deployed tree. This is what you want to see.
#   BEHIND   — tracked files the upstream has changed since this checkout.
#
# Without that split you get one undifferentiated pile of ~30 modified files and learn nothing.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_profile "${1:-}"
FULL=0; PORCELAIN=0
for a in "$@"; do case "$a" in --full) FULL=1;; --porcelain) PORCELAIN=1;; esac; done
# --porcelain exists because parsing the human output is a trap: update.sh grepped for "drift:"
# and matched the SUCCESS line "no drift: every local modification is explained by the render",
# so a clean tree was reported as drifting. Machine callers read the counters, not the prose.
if [ "$PORCELAIN" = 1 ]; then
  say(){ :; }; hdr(){ :; }; ok(){ :; }; warn(){ :; }; bad(){ :; }; info(){ :; }
fi

git -C "$PROFILE_DEST" rev-parse --git-dir >/dev/null 2>&1 \
  || die "$PROFILE_DEST is not a git checkout — nothing to diff against (see deploy.sh)"

hdr "checkout"
info "commit  $(git_head) $(git -C "$PROFILE_DEST" log -1 --format=%s | cut -c1-56)"
info "branch  $(git -C "$PROFILE_DEST" rev-parse --abbrev-ref HEAD)"

# Classify each modified tracked file: re-render the PRISTINE version from git and see whether
# the working copy matches it. If it does, the only change is the render.
hdr "local modifications"
render_n=0; drift_n=0
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
# The same table render.sh uses — from lib.sh, not a second copy of it.
sed_script="$(render_sed_script)"
while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  if ! git -C "$PROFILE_DEST" show "HEAD:$rel" > "$tmp/pristine" 2>/dev/null; then
    drift_n=$((drift_n+1)); bad "untracked-or-new: $rel"; continue
  fi
  if sed "$sed_script" "$tmp/pristine" | cmp -s - "$PROFILE_DEST/$rel"; then
    render_n=$((render_n+1))
    [ "$FULL" = 1 ] && info "render: $rel"
  else
    drift_n=$((drift_n+1))
    bad "drift:  $rel"
    [ "$FULL" = 1 ] && git -C "$PROFILE_DEST" diff -- "$rel" | sed -n '5,25p' | sed 's/^/        /'
  fi
done < <(git -C "$PROFILE_DEST" diff --name-only HEAD 2>/dev/null)

[ "$render_n" -gt 0 ] && ok "$render_n file(s) differ ONLY by this profile's render — expected"
[ "$drift_n" = 0 ] && ok "no drift: every local modification is explained by the render"
[ "$FULL" = 0 ] && [ "$render_n" -gt 0 ] && info "(--full lists them and shows drift hunks)"

hdr "untracked files"
untracked="$(git -C "$PROFILE_DEST" ls-files --others --exclude-standard 2>/dev/null)"
untracked_n=0
[ -n "$untracked" ] && untracked_n="$(printf '%s\n' "$untracked" | wc -l | tr -d ' ')"
if [ -z "$untracked" ]; then ok "none"
else
  n="$(printf '%s\n' "$untracked" | wc -l)"
  # .env and node_modules are gitignored, so anything listed here is genuinely unexpected.
  warn "$n untracked file(s) not covered by .gitignore:"
  printf '%s\n' "$untracked" | head -15 | sed 's/^/      /'
fi

hdr "upstream"
if git -C "$PROFILE_DEST" fetch -q origin 2>/dev/null; then
  behind="$(git -C "$PROFILE_DEST" rev-list --count HEAD..@{u} 2>/dev/null || echo 0)"
  ahead="$(git -C "$PROFILE_DEST" rev-list --count @{u}..HEAD 2>/dev/null || echo 0)"
  if [ "${behind:-0}" = 0 ] && [ "${ahead:-0}" = 0 ]; then ok "up to date with origin"
  else
    [ "${behind:-0}" -gt 0 ] && warn "$behind commit(s) BEHIND origin — run update.sh"
    # Whether "ahead" is a fault depends on the profile's ROLE. A consumer tree is a read-only
    # clone: commits there are invisible to the other runtime and get lost by the next
    # reset-and-render in update.sh. The author's tree is also the development repo, so being
    # ahead is simply unpushed work.
    if [ "${ahead:-0}" -gt 0 ]; then
      if [ "${PROFILE_ROLE:-consumer}" = author ]; then
        info "$ahead unpushed commit(s) — expected for the author tree"
      else
        bad "$ahead local commit(s) AHEAD of origin — a consumer tree must not carry commits"
      fi
    fi
  fi
  [ "${behind:-0}" -gt 0 ] && git -C "$PROFILE_DEST" log --oneline HEAD..@{u} | head -10 | sed 's/^/      /'
else
  warn "cannot reach origin (no network, or no read access with this key)"
fi

if [ "$PORCELAIN" = 1 ]; then
  printf 'RENDER=%s DRIFT=%s UNTRACKED=%s BEHIND=%s AHEAD=%s\n' \
    "$render_n" "$drift_n" "$untracked_n" \
    "${behind:-0}" "${ahead:-0}"
  exit 0
fi
finish
