#!/usr/bin/env bash
# install-skill.sh — security-gated installer for Claude Code skills.
#
# The pipeline Hermes uses to give Claude Code a new skill WITHOUT a human
# vetting each one:  fetch → AgentShield (config surface) → content scan
# (SKILL.md/scripts) → [optional Claude semantic review] → install.
#
# Usage:
#   install-skill.sh <name> --source <src> [--force] [--strict]
#
#   <src> forms:
#     /abs/path/to/skilldir        local directory (must contain SKILL.md)
#     https://github.com/o/r.git    git repo whose root (or skills/<name>/) is the skill
#     ecc:<name>                    fetch skills/<name>/ from affaan-m/ECC
#
#   --force    reinstall even if ~/.claude/skills/<name> already exists
#   --strict   also require the optional Claude semantic review to return SAFE
#              (default: Claude review is advisory — only a hard UNSAFE blocks)
#
# Installs to $CLAUDE_CONFIG_DIR/skills/<name>/ (default ~/.claude/skills).
# Exit 0 = installed; 3 = rejected by a gate; 2 = fetch/usage error.

set -uo pipefail

# Pull TELEGRAM_* etc. if a Hermes/OA env file is around (optional).
for ef in "${SKILL_GUARD_ENV_FILE:-}" "$HOME/.hermes/.env"; do
  [[ -n "$ef" && -f "$ef" ]] && { set -a; # shellcheck disable=SC1090
    source "$ef"; set +a; break; }
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck disable=SC1091
source "$script_dir/lib-skill-guard.sh"

CLAUDE_CONFIG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
ECC_REPO="${ECC_REPO:-https://github.com/affaan-m/ECC.git}"

name="${1:?usage: install-skill.sh <name> --source <src> [--force] [--strict]}"; shift
# The name lands in `dest="$CLAUDE_CONFIG_DIR/skills/$name"`, and line ~117 runs
# `rm -rf "$dest"`. Hermes composes this call unattended from a third-party
# catalog (see skills/vps-orchestration), so the name is untrusted input to a
# recursive delete: `install-skill.sh '../../.hermes' --force` would have taken
# out the whole runtime — .env, the encrypted MTProto session, qdrant storage.
# One flat path component, nothing else.
case "$name" in
  ""|.|..|*/*|*'\'*|-*) echo "ERR: недопустимое имя скилла: '$name'" >&2; exit 2 ;;
esac
[[ "$name" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]] || {
  echo "ERR: имя скилла может содержать только A-Z a-z 0-9 . _ - и начинаться с буквы или цифры: '$name'" >&2
  exit 2
}
source_spec=""; force=0; strict=0
while (( $# )); do
  case "$1" in
    --source) source_spec="${2:?}"; shift 2 ;;
    --force)  force=1; shift ;;
    --strict) strict=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done
[[ -n "$source_spec" ]] || { echo "ERR: --source required" >&2; exit 2; }

dest="$CLAUDE_CONFIG_DIR/skills/$name"
if [[ -e "$dest" && $force -eq 0 ]]; then
  echo "[install-skill] $name already installed at $dest (use --force)" ; exit 0
fi

stage="$(mktemp -d)"; trap 'rm -rf "$stage"' EXIT
skilldir=""   # will point at the dir that holds SKILL.md

echo "[install-skill] fetching '$name' from: $source_spec"
case "$source_spec" in
  ecc:*)
    want="${source_spec#ecc:}"
    tmp_repo="$stage/ecc"; mkdir -p "$tmp_repo"
    ( cd "$tmp_repo" && git init -q && git remote add origin "$ECC_REPO" \
      && git config core.sparseCheckout true \
      && echo "skills/$want/*" > .git/info/sparse-checkout \
      && git pull -q --depth=1 origin main ) >/dev/null 2>&1 \
      || { echo "ERR: ECC sparse fetch failed for skills/$want" >&2; exit 2; }
    skilldir="$tmp_repo/skills/$want"
    ;;
  http*://*|git@*)
    ( git clone -q --depth=1 "$source_spec" "$stage/repo" ) >/dev/null 2>&1 \
      || { echo "ERR: git clone failed" >&2; exit 2; }
    if [[ -f "$stage/repo/SKILL.md" ]]; then skilldir="$stage/repo"
    elif [[ -f "$stage/repo/skills/$name/SKILL.md" ]]; then skilldir="$stage/repo/skills/$name"
    else skilldir="$(dirname "$(find "$stage/repo" -name SKILL.md | head -1)")"; fi
    ;;
  *)
    [[ -d "$source_spec" ]] || { echo "ERR: local source not a dir: $source_spec" >&2; exit 2; }
    cp -a "$source_spec" "$stage/local"; skilldir="$stage/local"
    ;;
esac

[[ -n "$skilldir" && -f "$skilldir/SKILL.md" ]] \
  || { echo "ERR: no SKILL.md found in fetched source" >&2; exit 2; }
echo "[install-skill] staged at: $skilldir"

# ── Gate 1: AgentShield (config surface) ─────────────────────────────────────
as_json="$stage/agentshield.json"
sg_agentshield "$skilldir" "$as_json"; as_rc=$?
if (( as_rc == 1 )); then
  echo "[install-skill] REJECTED by AgentShield (critical/high findings)" >&2
  sg_notify "🛑 skill <b>$name</b> отклонён: AgentShield нашёл critical/high"
  exit 3
fi
(( as_rc == 2 )) && echo "[install-skill] WARN: AgentShield unavailable — relying on content scan" >&2

# ── Gate 2: deterministic content scan (SKILL.md + scripts) ───────────────────
if ! sg_content_scan "$skilldir"; then
  echo "[install-skill] REJECTED by content scan" >&2
  sg_notify "🛑 skill <b>$name</b> отклонён: content-scan нашёл опасные паттерны"
  exit 3
fi

# ── Gate 3 (optional): Claude semantic review ────────────────────────────────
sg_claude_review "$skilldir"; cr_rc=$?
if (( cr_rc == 1 )); then
  echo "[install-skill] REJECTED by Claude review (UNSAFE)" >&2
  sg_notify "🛑 skill <b>$name</b> отклонён: Claude признал UNSAFE"
  exit 3
fi
if (( strict && cr_rc != 0 )); then
  echo "[install-skill] REJECTED: --strict requires a SAFE Claude review (got rc=$cr_rc)" >&2
  exit 3
fi

# ── Install ──────────────────────────────────────────────────────────────────
rm -rf "$dest"; mkdir -p "$(dirname "$dest")"; cp -a "$skilldir" "$dest"
echo "[install-skill] INSTALLED → $dest"
sg_notify "✅ skill <b>$name</b> установлен в Claude Code (AgentShield+content-scan прошли)"
