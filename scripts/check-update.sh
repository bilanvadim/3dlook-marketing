#!/usr/bin/env bash
# check-update.sh [profile] [--quiet] — is there anything new upstream? Changes NOTHING.
#
# Built for cron and for update.sh's own pre-flight, so the ANSWER IS THE EXIT CODE:
#   0  already up to date
#   3  updates available (deliberately not 1 — 1 must stay "the check itself failed")
#   1  could not determine (no network, no git, no upstream)
#
# It only fetches. Nothing about the working tree is touched, so it is safe to run every
# few minutes from a timer while a job is mid-flight.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
load_profile "${1:-}"
QUIET=0; case "${2:-}" in --quiet|-q) QUIET=1;; esac
say(){ [ "$QUIET" = 1 ] || printf '%s\n' "$*"; }
ok(){   [ "$QUIET" = 1 ] || printf '  %s✓%s %s\n' "$_C_G" "$_C_0" "$*"; }
info(){ [ "$QUIET" = 1 ] || printf '  · %s\n' "$*"; }

git -C "$PROFILE_DEST" rev-parse --git-dir >/dev/null 2>&1 || {
  printf 'check-update: %s is not a git checkout — no update path\n' "$PROFILE_DEST" >&2; exit 1; }

git -C "$PROFILE_DEST" fetch -q origin 2>/dev/null || {
  printf 'check-update: cannot reach origin\n' >&2; exit 1; }

behind="$(git -C "$PROFILE_DEST" rev-list --count HEAD..@{u} 2>/dev/null)" || {
  printf 'check-update: no upstream configured for %s\n' "$(git -C "$PROFILE_DEST" rev-parse --abbrev-ref HEAD)" >&2; exit 1; }

if [ "${behind:-0}" = 0 ]; then
  ok "up to date at $(git_head)"
  exit 0
fi

say ""
say "$_C_B$behind update(s) available for $PROFILE_NAME$_C_0"
info "current $(git_head)"
info "latest  $(git -C "$PROFILE_DEST" rev-parse --short '@{u}')"
[ "$QUIET" = 1 ] || git -C "$PROFILE_DEST" log --oneline HEAD..@{u} | head -15 | sed 's/^/      /'

# Say plainly whether applying it will bounce services, so a human can pick the moment.
touched="$(git -C "$PROFILE_DEST" diff --name-only HEAD..@{u} 2>/dev/null)"
restarts=()
printf '%s\n' "$touched" | grep -q 'DEV/dev/conductor/' && restarts+=(hermes-conductor)
printf '%s\n' "$touched" | grep -qE 'hermes-agent/(SOUL\.md|skills/|ops/)' && restarts+=(hermes-gateway)
if [ "${#restarts[@]}" -gt 0 ]; then
  info "applying this will restart: ${restarts[*]}"
fi
if printf '%s\n' "$touched" | grep -q 'conductor/package-lock.json'; then
  info "dependencies changed — update.sh will run npm ci"
fi
exit 3
