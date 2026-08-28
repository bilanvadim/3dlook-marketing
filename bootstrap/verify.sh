#!/usr/bin/env bash
# verify.sh — is this machine's Hermes/Claude-Code ecosystem actually healthy,
# and is it independent of /srv/…/ai-agents-config?
#
# Run it after a bootstrap, after `hermes update`, and any time something feels
# wrong. It only READS: nothing here starts, stops, installs or edits anything, so
# it is safe to run against production at any moment.
#
# WHY THE INDEPENDENCE CHECKS ARE IN A HEALTH SCRIPT AT ALL
# --------------------------------------------------------
# /srv/vadim_prod/ai-agents-config is a different system (Sergiy's). Until
# 2026-08-26 this repo's conductor, its cron monitor and its DAILY UPDATE all
# reached into that tree. The update was the dangerous one: it re-copied SOUL.md,
# the vendored patch appliers and the model-router out of /srv every morning, so
# the dependency came BACK on its own after any manual cleanup. A one-time audit
# cannot hold that; a check that runs regularly can.
#
# Usage: bootstrap/verify.sh [--quiet]
# Exit:  0 all green · 1 at least one FAIL · 2 warnings only.
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# The one place this path is allowed to appear in live code: this script exists to
# assert the ABSENCE of the dependency, so naming it here is the check, not a tie.
LEGACY_TREE="/srv/vadim_prod/ai-agents-config"
QUIET=0; [ "${1:-}" = "--quiet" ] && QUIET=1

fails=0; warns=0
ok()   { [ "$QUIET" = 1 ] || printf '[OK]   %s\n' "$1"; }
warn() { printf '[WARN] %s\n' "$1"; warns=$((warns+1)); }
fail() { printf '[FAIL] %s\n' "$1"; fails=$((fails+1)); }
hdr()  { [ "$QUIET" = 1 ] || printf '\n── %s\n' "$1"; }

# ── 1. services ──────────────────────────────────────────────────────────────
hdr "Services"
for u in hermes-gateway hermes-conductor; do
  if systemctl --user is-active --quiet "$u"; then ok "$u active"
  else fail "$u NOT active (systemctl --user status $u)"; fi
done

# ── 2. the conductor must be OUR conductor ───────────────────────────────────
# Checking the unit file is not enough: a drop-in can override WorkingDirectory,
# which is exactly how the runtime ended up in /srv while the base unit still
# named this repo. Ask the RUNNING process where it actually is.
hdr "Conductor runs from this repo"
CPID="$(systemctl --user show hermes-conductor -p MainPID --value 2>/dev/null)"
if [ -n "${CPID:-}" ] && [ "$CPID" != "0" ] && [ -e "/proc/$CPID/cwd" ]; then
  cwd="$(readlink -f "/proc/$CPID/cwd" 2>/dev/null)"
  case "$cwd" in
    "$REPO"/*) ok "conductor cwd inside repo (${cwd#$REPO/})" ;;
    *)         fail "conductor cwd is OUTSIDE this repo: $cwd" ;;
  esac
else
  fail "conductor has no running main process"
fi

# ── 3. independence from the legacy tree ─────────────────────────────────────
hdr "Independence from ai-agents-config"
if [ -e "$LEGACY_TREE" ]; then
  warn "$LEGACY_TREE still exists — presence alone is fine, the checks below are what matter"
else
  ok "$LEGACY_TREE absent"
fi

# systemd: only LIVE directives count, comments explaining the history are fine.
live_srv=0
for f in "$HOME"/.config/systemd/user/*.service "$HOME"/.config/systemd/user/*.d/*.conf; do
  [ -f "$f" ] || continue
  if [ -n "$(grep -v '^[[:space:]]*#' "$f" 2>/dev/null | grep -F "$LEGACY_TREE" || true)" ]; then
    fail "live systemd directive points at legacy tree: $f"; live_srv=1
  fi
done
[ "$live_srv" = 0 ] && ok "no systemd unit or drop-in points at the legacy tree"

if [ -n "$(crontab -l 2>/dev/null | grep -v '^[[:space:]]*#' | grep -F "$LEGACY_TREE" || true)" ]; then
  fail "crontab still runs something from the legacy tree"
else
  ok "crontab free of the legacy tree"
fi

# The daily update is the one that used to re-acquire the dependency.
if [ -n "$(grep -v '^[[:space:]]*#' "$REPO/hermes_agent/ops/hermes-update.py" 2>/dev/null | grep -F "$LEGACY_TREE" || true)" ]; then
  fail "hermes-update.py still pulls from the legacy tree — it would come back tomorrow 06:01"
else
  ok "hermes-update.py sources everything from this repo"
fi

# grep -q in a pipeline is unsafe under `set -o pipefail`: grep exits at the first
# match, the closed pipe SIGPIPEs the writer, and pipefail then reports the whole
# pipeline as FAILED — so a match takes the else branch. It is input-size dependent,
# so it passes every small test and inverts on real data.
if [ -n "$(find "$HOME" -maxdepth 4 -type l -lname "${LEGACY_TREE}*" 2>/dev/null | head -5 || true)" ]; then
  fail "symlink(s) under \$HOME point into the legacy tree"
else
  ok "no symlinks into the legacy tree"
fi

# ── 4. the pieces the pipelines shell out to ─────────────────────────────────
hdr "Executables the pipelines depend on"
for f in \
  "hermes_agent/ops/mvb-run.py" \
  "hermes_agent/ops/conductor-monitor.sh" \
  "hermes_agent/ops/conductor-run.sh" \
  "hermes_agent/ops/mvb-verify-job.py" \
  "marketing_vb/scripts/ahrefs-keywords.py" \
  "marketing_vb/scripts/check-agent-copies.py" \
  "marketing_vb/brand-assets/style-guides/scripts/detect-ai-tells.py" ; do
  if [ -x "$REPO/$f" ]; then ok "$f"
  elif [ -f "$REPO/$f" ]; then warn "$f present but not executable"
  else fail "$f MISSING"; fi
done

# ── 5. conductor app is installed and buildable ──────────────────────────────
hdr "Conductor application"
CDIR="$REPO/claude_code/DEV/full_stack_sm/conductor"
[ -f "$CDIR/package.json" ] && ok "package.json present" || fail "conductor package.json missing"
[ -d "$CDIR/node_modules" ] && ok "node_modules installed" || fail "node_modules missing — run: (cd $CDIR && npm install)"
if [ -d "$CDIR/node_modules/better-sqlite3" ]; then ok "better-sqlite3 present"
else fail "better-sqlite3 missing — the source needs it (@libsql/client leaked and OOM-killed the box 2026-08-14)"; fi

# ── 6. agent copies must not have drifted ────────────────────────────────────
hdr "Agent definitions"
if [ -x "$REPO/marketing_vb/scripts/check-agent-copies.py" ]; then
  if out="$("$REPO/marketing_vb/scripts/check-agent-copies.py" --quiet 2>&1)"; then
    ok "every agent identical across its copies"
  else
    fail "agent copies have drifted — run marketing_vb/scripts/check-agent-copies.py"
  fi
fi

# ── 7. secrets present but NOT in git ────────────────────────────────────────
hdr "Secrets"
SEC="$HOME/.config/ai-agent-stack/secrets.env"
if [ -f "$SEC" ]; then
  perm="$(stat -c '%a' "$SEC" 2>/dev/null)"
  [ "$perm" = "600" ] && ok "secrets.env present, mode 600" || warn "secrets.env mode is $perm, expected 600"
else
  fail "secrets.env missing — copy config/secrets.env.example and fill it in"
fi
# THE OLD CHECK HERE COULD NEVER FAIL. It ran
#   git ls-files --error-unmatch /home/…/.config/ai-agent-stack/secrets.env
# — an absolute path OUTSIDE the working tree, which git can never match. It printed
# "no secrets file tracked in git" unconditionally, including on a repo that had just
# committed a live key. A check that cannot fail is worse than no check: it is a green
# light with nothing behind it.
#
# What is actually asserted now: no tracked file is a secret STORE by name, and no
# tracked file CONTAINS anything shaped like a live credential. Only paths are ever
# printed — never a value, not even a fragment.
# NOTE ON `grep -q` UNDER `set -o pipefail`: the first version of this check used
#   ... | grep -qiE '<pattern>'
# inside an `if`. grep -q exits the moment it matches, which closes the pipe, which
# sends SIGPIPE upstream, which under pipefail makes the WHOLE PIPELINE non-zero — so a
# MATCH took the else branch and printed "no secret store tracked by name". The check
# was rewritten to fail, and immediately could not fail again for a completely different
# reason. Collect into a variable and test the variable.
STORES="$(git -C "$REPO" ls-files 2>/dev/null \
          | grep -viE '\.(example|sample|template|dist)$' \
          | grep -iE '(^|/)([^/]*\.env|[^/]*\.envrc|auth\.json|\.credentials\.json|id_rsa[^/]*|[^/]*\.pem|[^/]*\.session|[^/]*\.key)$' || true)"
if [ -n "$STORES" ]; then
  fail "secret store(s) TRACKED IN GIT: $(printf '%s' "$STORES" | head -3 | tr '\n' ' ')"
else
  ok "no secret store tracked by name"
fi
SHAPES="$(git -C "$REPO" grep -lIE '(sk-[A-Za-z0-9]{20,}|sk-or-v1-[A-Za-z0-9]{20,}|nvapi-[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{30,}|vfp_[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|gh[pousr]_[A-Za-z0-9]{30,}|[0-9]{8,10}:AA[A-Za-z0-9_-]{30,})' -- . 2>/dev/null \
          | grep -vE '(\.example$|\.md$|/docs/)' || true)"
if [ -n "$SHAPES" ]; then
  fail "credential-shaped content in tracked file(s): $(printf '%s' "$SHAPES" | head -5 | tr '\n' ' ')"
else
  ok "no credential-shaped content in tracked files"
fi

# ═══════════════════════════════════════════════════════════════════════════════
# The six diagnostics the spec makes mandatory.
#
# Each of these exists because something on this machine once broke with NO ERROR
# MESSAGE ANYWHERE. Both halves of the system worked perfectly; they just worked on
# different assumptions. If a problem announces itself in a log, it does not need a
# check here.
# ═══════════════════════════════════════════════════════════════════════════════

# ── D1. both halves of the escalation path must resolve the SAME ho.db ───────
# When they do not, every Approve tap writes 'approved' into one database while the
# conductor times out against another, and NOTHING is logged on either side.
hdr "D1 · one queue, not two"
resolve_db() {  # strip the file: scheme, expand ~, make absolute
  local v="${1#file:}"; v="${v/#\~/$HOME}"
  [ "${v:0:1}" = "/" ] || v="$HOME/$v"
  readlink -f "$v" 2>/dev/null || echo "$v"
}
CONDUCTOR_DB="$(resolve_db "$(systemctl --user show hermes-conductor -p Environment --value 2>/dev/null | tr ' ' '\n' | sed -n 's/^DATABASE_URL=//p' | tail -1)")"
[ -n "$CONDUCTOR_DB" ] || CONDUCTOR_DB="$(resolve_db "$HOME/.hermes/ho.db")"
# claude_switcher.py:851 is  HO_DB = os.environ.get("HO_DB") or <hermes_home>/ho.db
# so ask the GATEWAY PROCESS's environment, not the source text. Scraping the source
# gave a truncated path and a false FAIL — a check that cries wolf gets ignored, which
# is the same outcome as no check.
GPID="$(systemctl --user show hermes-gateway -p MainPID --value 2>/dev/null)"
GATEWAY_DB=""
if [ -n "${GPID:-}" ] && [ "$GPID" != "0" ] && [ -r "/proc/$GPID/environ" ]; then
  GATEWAY_DB="$(tr '\0' '\n' < "/proc/$GPID/environ" 2>/dev/null | sed -n 's/^HO_DB=//p' | tail -1)"
  GHOME="$(tr '\0' '\n' < "/proc/$GPID/environ" 2>/dev/null | sed -n 's/^HERMES_HOME=//p' | tail -1)"
  [ -n "$GATEWAY_DB" ] || GATEWAY_DB="${GHOME:-$HOME/.hermes}/ho.db"
fi
GATEWAY_DB="$(resolve_db "${GATEWAY_DB:-$HOME/.hermes/ho.db}")"
CRON_DB="$(resolve_db "$(crontab -l 2>/dev/null | grep -oE 'HO_DB=[^ ]+' | head -1 | cut -d= -f2-)")"
printf '       conductor : %s\n       gateway   : %s\n       cron      : %s\n' \
       "$CONDUCTOR_DB" "$GATEWAY_DB" "$CRON_DB"
if [ "$CONDUCTOR_DB" = "$GATEWAY_DB" ] && { [ -z "$CRON_DB" ] || [ "$CRON_DB" = "$CONDUCTOR_DB" ]; }; then
  ok "all paths resolve one ho.db"
else
  fail "ho.db paths DISAGREE — Approve/Deny would write to a database the worker never reads"
fi
# A second ho.db anywhere near the runtime is a decoy waiting to be opened.
for decoy in "$REPO/claude_code/DEV/full_stack_sm/conductor/ho.db" "$REPO/ho.db"; do
  [ -e "$decoy" ] && warn "decoy database present: ${decoy#$REPO/} (WorkingDirectory sits here)"
done

# ── D2. the unit must name the tree the process actually runs from ────────────
# Invisible until a restart, which then silently "resolves" it — possibly onto a
# tree that does not start.
hdr "D2 · unit and live process agree"
# The question is NOT "is the binary named the same" — the conductor's unit declares a
# wrapper (conductor-run.sh) that legitimately execs `npm start`, and comparing
# basenames there fails on a system that is perfectly correct. The question the spec
# actually asks is: does the unit name the TREE the process runs from? That is the one
# that stays invisible until a restart silently resolves it — possibly onto a tree that
# will not start.
for u in hermes-conductor hermes-gateway llm-failover-proxy llm-failover-proxy-strong; do
  pid="$(systemctl --user show "$u" -p MainPID --value 2>/dev/null)"
  if [ -z "$pid" ] || [ "$pid" = "0" ]; then warn "$u not running — cannot compare"; continue; fi
  live_cwd="$(readlink -f "/proc/$pid/cwd" 2>/dev/null)"
  want_cwd="$(systemctl --user show "$u" -p WorkingDirectory --value 2>/dev/null)"
  want_cwd="${want_cwd#\!}"; want_cwd="$(readlink -f "${want_cwd:-/}" 2>/dev/null)"
  if [ -n "$want_cwd" ] && [ "$want_cwd" != "/" ]; then
    if [ "$live_cwd" = "$want_cwd" ]; then ok "$u runs from the tree its unit declares (${live_cwd#$HOME/})"
    else fail "$u: unit says WorkingDirectory=$want_cwd but the process is in $live_cwd"; fi
  else
    ok "$u declares no WorkingDirectory (process is in ${live_cwd:-?})"
  fi
  # Additionally: every absolute path in ExecStart must still exist. A unit naming a
  # deleted tree starts fine until the day it is restarted.
  missing=""
  while IFS= read -r p; do
    case "$p" in /*) [ -e "$p" ] || missing="$missing $p" ;; esac
  done < <(systemctl --user show "$u" -p ExecStart --value 2>/dev/null | tr ' ;' '\n\n' | grep -oE '^/[^ ]+')
  [ -z "$missing" ] || fail "$u: ExecStart names path(s) that do not exist:$missing"
done

# ── D3. exactly ONE conductor may consume this queue ─────────────────────────
# A forgotten unit in the other systemd scope is a trap, not a spare: enable it and
# two workers claim from one ho.db.
hdr "D3 · one conductor on the queue"
sys_state="$(systemctl is-enabled hermes-conductor.service 2>/dev/null || echo absent)"
sys_user="$(systemctl show hermes-conductor.service -p User --value 2>/dev/null || true)"
if [ "$sys_state" = "absent" ]; then ok "no system-scope conductor"
elif [ -n "$sys_user" ] && [ "$sys_user" != "$(id -un)" ]; then
  ok "system-scope conductor belongs to $sys_user (not ours) — different HOME, different ho.db"
else
  fail "a system-scope conductor runs as US as well as the user unit — two workers, one queue"
fi
rogue="$(pgrep -u "$(id -un)" -f 'conductor.ts|core/conductor' 2>/dev/null | wc -l)"
managed="$(systemctl --user show hermes-conductor -p MainPID --value 2>/dev/null)"
if [ "${rogue:-0}" -gt 0 ]; then
  bad=0
  for p in $(pgrep -u "$(id -un)" -f 'conductor.ts|core/conductor' 2>/dev/null); do
    cg="$(cat "/proc/$p/cgroup" 2>/dev/null || true)"
    case "$cg" in *hermes-conductor.service*) : ;; *) bad=$((bad+1)); warn "conductor pid $p is NOT in the managed cgroup: ${cg##*:}" ;; esac
  done
  [ "$bad" = 0 ] && ok "every conductor process is inside the managed unit"
fi

# ── D4. no port of ours may be held by anything but our own managed unit ──────
# A busy port raises no error: llmfp simply binds the NEXT free one. That is how an
# orphan took 47832 while the real strong instance moved to 47833 and Hermes' heavy
# mode plus all of OpenCode spoke to old code for 21 hours.
hdr "D4 · ports held by the right process"
port_owner() { ss -tlnpH "sport = :$1" 2>/dev/null | grep -oE 'pid=[0-9]+' | head -1 | cut -d= -f2; }
check_port() { # port  unit  label
  local p="$1" u="$2" label="$3" owner want
  owner="$(port_owner "$p")"
  want="$(systemctl --user show "$u" -p MainPID --value 2>/dev/null)"
  if [ -z "$owner" ]; then fail "$label: nothing listening on :$p"
  elif [ "$owner" = "$want" ]; then ok "$label :$p owned by $u"
  else
    local cg; cg="$(cat "/proc/$owner/cgroup" 2>/dev/null || echo '?')"
    fail "$label :$p held by pid $owner, NOT $u (cgroup ${cg##*/}) — an orphan or the other account"
  fi
}
AGENTIC_PORT="$(python3 -c "import json;print(json.load(open('$HOME/.config/llm-failover-proxy/agentic/config.json'))['server']['port'])" 2>/dev/null || echo 47831)"
STRONG_PORT="$(python3 -c "import json;print(json.load(open('$HOME/.config/llm-failover-proxy/strong/config.json'))['server']['port'])" 2>/dev/null || echo 47832)"
check_port "$AGENTIC_PORT" llm-failover-proxy        "proxy agentic"
check_port "$STRONG_PORT"  llm-failover-proxy-strong "proxy strong"
# Each instance must also REPORT the port it was configured for. A daemon.json whose
# port differs from server.port beside it is the signature of a port fallback.
for inst in agentic strong; do
  d="$HOME/.config/llm-failover-proxy/$inst/daemon.json"
  [ -f "$d" ] || continue
  got="$(python3 -c "import json;print(json.load(open('$d'))['port'])" 2>/dev/null)"
  wantp="$(python3 -c "import json;print(json.load(open('$HOME/.config/llm-failover-proxy/$inst/config.json'))['server']['port'])" 2>/dev/null)"
  [ "$got" = "$wantp" ] && ok "$inst daemon state agrees with its config (:$got)" \
                        || fail "$inst daemon.json says :$got but its config says :$wantp — port fallback happened"
done

# ── D5. secrets: source vs copy, BY VALUE HASH ───────────────────────────────
# A name-based check reports a live credential as missing. That is not academic: it
# is why mem0's llm block was deleted on 2026-08-26 with the note "no Google API key
# exists in this environment" — the key was there, under another name.
hdr "D5 · secrets source vs copies (by hash)"
SRC="$HOME/.config/ai-agent-stack/secrets.env"
if [ ! -f "$SRC" ]; then
  fail "no single source of secrets at $SRC"
else
  [ "$(stat -c %a "$SRC")" = "600" ] && ok "source is 0600" || fail "source is $(stat -c %a "$SRC"), must be 600"
  python3 - "$SRC" "$HOME/.hermes/.env" <<'PYSEC'
import hashlib, sys, os

def load(p):
    out = {}
    try:
        for line in open(p, encoding="utf-8", errors="replace"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    except OSError:
        return None
    return out

def h(v):
    return hashlib.sha256(v.encode()).hexdigest()[:10]

src, cp = load(sys.argv[1]), load(sys.argv[2])
if src is None or cp is None:
    print("[FAIL] cannot read one of the secret files"); sys.exit(0)

# Reverse index by VALUE: the same credential under a different NAME is the failure
# mode a name-based diff cannot see, and it is what happened here.
by_val = {}
for k, v in cp.items():
    if v:
        by_val.setdefault(h(v), []).append(k)

same = renamed = missing = 0
for k, v in sorted(src.items()):
    if not v:
        continue
    if cp.get(k) == v:
        same += 1
    elif h(v) in by_val:
        renamed += 1
        print(f"[WARN] {k} reaches ~/.hermes/.env under a DIFFERENT NAME: {', '.join(by_val[h(v)])}"
              f" — a check that compares names would call this missing")
    elif k in cp:
        print(f"[FAIL] {k} present in both files with DIFFERENT VALUES — the live system runs on"
              f" the copy and the next install silently rolls it back")
        missing += 1
    else:
        print(f"[WARN] {k} is in the source but nowhere in ~/.hermes/.env (by name or by value)")
        missing += 1
orphans = [k for k, v in cp.items()
           if v and k not in src and h(v) not in {h(x) for x in src.values() if x}]
print(f"[OK]   {same} key(s) identical in source and copy"
      + (f", {renamed} renamed" if renamed else "")
      + (f", {missing} unaccounted" if missing else ""))
if orphans:
    print(f"[WARN] {len(orphans)} value(s) exist only in ~/.hermes/.env, generated by nothing: "
          + ", ".join(sorted(orphans)[:8]))
PYSEC
fi
# Cross-account comparison is deliberately NOT attempted: reading the other account's
# secrets would require access we must not have. What CAN be checked is that none of
# our secrets leaked somewhere readable.
leaky=0
while IFS= read -r f; do
  [ -f "$f" ] || continue
  m="$(stat -c %a "$f" 2>/dev/null)"
  case "$m" in 600|400|0) : ;; *) fail "secret-bearing $f is mode $m — must be 600"; leaky=$((leaky+1)) ;; esac
done <<LIST
$HOME/.hermes/.env
$HOME/.config/llm-failover-proxy/.env
$HOME/.hermes/mem0.json
$HOME/.hermes/qdrant-server/qdrant.env
$HOME/.config/llm-failover-proxy/agentic/config.json
$HOME/.config/llm-failover-proxy/strong/config.json
LIST
[ "$leaky" = 0 ] && ok "every secret-bearing file is 0600"

# ── D6. an autonomous run must have a rollback point ─────────────────────────
hdr "D6 · pre-run snapshot wired"
SNAP="$(systemctl --user show hermes-conductor -p Environment --value 2>/dev/null | tr ' ' '\n' | sed -n 's/^HO_SNAPSHOT_SH=//p' | tail -1)"
if [ -z "$SNAP" ]; then fail "HO_SNAPSHOT_SH not set — an autonomous job on main has NO rollback point"
elif [ ! -x "$SNAP" ]; then fail "HO_SNAPSHOT_SH=$SNAP is not executable"
else ok "snapshot hook wired: ${SNAP#$HOME/}"; fi

# ═══════════════════════════════════════════════════════════════════════════════
# Beyond the six: things this machine has actually been bitten by.
# ═══════════════════════════════════════════════════════════════════════════════

# ── the barrier around autonomous execution ──────────────────────────────────
hdr "Barrier · manager is not a coder"
python3 - "$HOME/.hermes/config.yaml" "$REPO" <<'PYBAR'
import sys, yaml, fnmatch
cfg = yaml.safe_load(open(sys.argv[1], encoding="utf-8")) or {}
repo = sys.argv[2]
ap = cfg.get("approvals") or {}
mode = str(ap.get("mode", "")).strip().lower()
print("[OK]   approvals.mode = smart" if mode == "smart"
      else f"[FAIL] approvals.mode = {mode or '(unset)'} — flagged commands no longer reach the judge")
al = cfg.get("command_allowlist") or []
print("[OK]   command_allowlist empty" if not al
      else f"[FAIL] command_allowlist has {len(al)} standing bypass(es): {al[:3]} — written by the 'Always' button")
deny = [str(d) for d in (ap.get("deny") or [])]
# The barrier is only real if it matches the tree that actually holds the code.
probes = [
    (f"cd {repo} && grep -rn x .",              True,  "grep inside the repo"),
    ("cd ~/3dlook-marketing && grep -rn x .",   True,  "grep via the ~ spelling"),
    (f"sed -i 's/a/b/' {repo}/docs/x.md",       True,  "in-place edit of repo docs"),
    (f'claude -p "grep the seo dir and sed it" --max-turns 40', False, "dispatching the coder"),
    (f"cd {repo} && git status",                 False, "git status"),
    (f"echo n > {repo}/.hermes-handoff.md",      False, "writing the handoff note"),
]
bad = 0
for cmd, want_denied, label in probes:
    hit = any(fnmatch.fnmatch(cmd.lower(), g.lower()) for g in deny)
    if hit != want_denied:
        bad += 1
        print(f"[FAIL] {label}: {'should be denied but is not' if want_denied else 'is denied but must be allowed'}")
if not bad:
    print(f"[OK]   {len(deny)} deny globs cover the real code tree and still allow dispatch/git/handoff")
PYBAR

# ── the model selector ───────────────────────────────────────────────────────
hdr "Model selector"
for pair in "agentic:$AGENTIC_PORT" "strong:$STRONG_PORT"; do
  inst="${pair%%:*}"; p="${pair##*:}"
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "http://127.0.0.1:$p/health" 2>/dev/null)"
  [ "$code" = "200" ] && ok "$inst /health 200 on :$p" || fail "$inst /health returned ${code:-no answer} on :$p"
done
for L in Vision Embedding Judge; do
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "http://127.0.0.1:$AGENTIC_PORT/health?list=$L" 2>/dev/null)"
  [ "$code" = "200" ] && ok "list '$L' served (auto - $L)" || fail "list '$L' missing or empty (HTTP ${code:-none}) — vision/memory/judge fall back off-proxy"
done
# Kind isolation: an embedding-only chain must REFUSE chat rather than serve something else.
code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "http://127.0.0.1:$AGENTIC_PORT/health?list=Embedding&kind=chat" 2>/dev/null)"
[ "$code" = "503" ] && ok "Embedding chain refuses chat (503), so kinds cannot cross" \
                    || warn "Embedding chain answered ${code:-none} to a chat probe (expected 503)"
python3 - "$HOME/.hermes/config.yaml" <<'PYMODEL'
import sys, yaml
d = yaml.safe_load(open(sys.argv[1], encoding="utf-8")) or {}
m = d.get("model") or {}
bad = []
if m.get("default") != "auto": bad.append(f"model.default={m.get('default')!r}")
if m.get("provider") != "custom": bad.append(f"model.provider={m.get('provider')!r}")
if "model" in m: bad.append("model.model exists and OVERRIDES model.default")
print("[OK]   model.default=auto, provider=custom, no model.model" if not bad
      else "[FAIL] " + "; ".join(bad) + " — a pinned name bypasses the failover chain (this took the channel down with 503)")
aux = d.get("auxiliary") or {}
for name in ("vision", "approval"):
    a = aux.get(name) or {}
    mdl = str(a.get("model") or "")
    if mdl.startswith("auto"): print(f"[OK]   auxiliary.{name} -> {mdl}")
    elif name == "approval" and not mdl: print(f"[WARN] auxiliary.approval unpinned — a reasoning model returns empty at max_tokens=16 and everything ESCALATEs")
    else: print(f"[WARN] auxiliary.{name} bypasses the proxy: provider={a.get('provider')} model={mdl!r}")
PYMODEL

# ── memory really initialises ───────────────────────────────────────────────
hdr "Memory"
# Scope this to the CURRENT gateway process, not a fixed 24h window. The question is
# "is memory working now", and a 24h window keeps reporting a failure that was fixed
# this morning — a check that cries wolf about the past gets muted, which costs the same
# as having no check. Historical occurrences are still reported, as a WARN.
GW_SINCE="$(systemctl --user show hermes-gateway -p ActiveEnterTimestamp --value 2>/dev/null)"
[ -n "$GW_SINCE" ] || GW_SINCE="-1h"
NOW_BAD="$(journalctl --user -u hermes-gateway --since "$GW_SINCE" --no-pager 2>/dev/null | grep -F 'Mem0 backend failed to initialize' || true)"
PAST_BAD="$(journalctl --user -u hermes-gateway --since '-7d' --no-pager 2>/dev/null | grep -cF 'Mem0 backend failed to initialize' || true)"
if [ -n "$NOW_BAD" ]; then
  fail "mem0 failed to initialize in the RUNNING gateway — store AND search are dead, not degraded"
else
  ok "mem0 initialised in the running gateway (up since ${GW_SINCE})"
  [ "${PAST_BAD:-0}" -gt 0 ] && warn "mem0 did fail to initialise ${PAST_BAD} time(s) in the last 7 days — fixed since, but worth knowing"
fi
QENV="$HOME/.hermes/qdrant-server/qdrant.env"
if [ -f "$QENV" ]; then
  QP="$(sed -n 's/^QDRANT__SERVICE__HTTP_PORT=//p' "$QENV" | tail -1)"; QP="${QP:-6353}"
  QK="$(sed -n 's/^QDRANT__SERVICE__API_KEY=//p' "$QENV" | tail -1)"
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "http://127.0.0.1:$QP/collections" 2>/dev/null)"
  [ "$code" = "401" ] && ok "qdrant :$QP demands a key (401) — healthy" || warn "qdrant :$QP answered ${code:-none} unauthenticated (401 expected)"
  read -r pts dims <<<"$(curl -s --max-time 10 -H "api-key: $QK" "http://127.0.0.1:$QP/collections/hermes_mem0" 2>/dev/null | python3 -c "
import json,sys
try:
  r=json.load(sys.stdin)['result']
  print(r.get('points_count'), (r.get('config',{}).get('params',{}).get('vectors') or {}).get('size'))
except Exception: print('? ?')" 2>/dev/null)"
  want="$(python3 -c "import json;print(json.load(open('$HOME/.hermes/mem0.json'))['oss']['embedder']['config']['embedding_dims'])" 2>/dev/null)"
  if [ "$dims" = "$want" ]; then ok "hermes_mem0: $pts points, $dims dims == mem0.json embedding_dims"
  else fail "collection is $dims dims but mem0.json asks for $want — the backend DELETES a mismatched collection"; fi
fi

# ── live units vs the copies in git ─────────────────────────────────────────
hdr "Units tracked in git"
TRACKED="$REPO/hermes_agent/ops/systemd/vadim-user"
missing=0; drift=0
for f in "$HOME/.config/systemd/user"/*.service "$HOME/.config/systemd/user"/*.timer; do
  b="$(basename "$f")"; case "$b" in *.bak-*|*.replaced-by-*) continue ;; esac
  if [ ! -f "$TRACKED/$b" ]; then warn "live unit not in git: $b"; missing=$((missing+1))
  elif ! diff -q <(grep -v '^#' "$f") <(grep -v '^#' "$TRACKED/$b") >/dev/null 2>&1; then
    # hermes-gateway.service is REGENERATED by `hermes update`; drift there is expected.
    case "$b" in hermes-gateway.service) warn "$b differs from git (upstream regenerates it — expected)" ;;
                 *) warn "$b differs from the copy in git"; drift=$((drift+1)) ;; esac
  fi
done
[ "$missing" = 0 ] && ok "every live unit has a copy in git"
[ "$drift" = 0 ]   && ok "no unexplained drift between live units and git"

# ── a backup exists and is recent ───────────────────────────────────────────
hdr "Backups"
NEW="$(find "$HOME/.hermes/backups" -maxdepth 1 -name 'auto-*' -type d 2>/dev/null | sort | tail -1)"
if [ -z "$NEW" ]; then fail "no automatic backup has ever run (hermes-backup.timer)"
else
  age=$(( ( $(date +%s) - $(stat -c %Y "$NEW") ) / 3600 ))
  [ "$age" -le 48 ] && ok "newest backup $(basename "$NEW") is ${age}h old" || warn "newest backup is ${age}h old"
  for must in ho.db units/systemd-user.tar.gz hermes/config.yaml hermes/SOUL.md secrets/secrets.env; do
    [ -e "$NEW/$must" ] || fail "backup is missing $must"
  done
  n="$(ls "$NEW"/qdrant/*.snapshot 2>/dev/null | wc -l)"
  [ "${n:-0}" -gt 0 ] && ok "backup carries $n Qdrant snapshot(s)" || fail "backup has NO Qdrant snapshot — mem0 vectors exist nowhere else"
  d="$(tar tzf "$NEW/units/systemd-user.tar.gz" 2>/dev/null | grep -c '\.service\.d/.*\.conf$')"
  [ "${d:-0}" -gt 0 ] && ok "backup carries $d unit drop-in(s)" || fail "backup has no drop-ins — the real deployment paths are not captured"
fi

# ── 8. repository shape ──────────────────────────────────────────────────────
hdr "Repository"
br="$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null)"
[ "$br" = "main" ] && ok "on branch main" || warn "on branch '$br', expected main"
# `branch -r` prints "origin/HEAD -> origin/main" as a row; without stripping the
# arrow form it reads as a phantom branch called "origin".
extra="$(git -C "$REPO" branch -r --format='%(refname:short)' 2>/dev/null \
          | grep -vE '^origin/HEAD$|^origin$|^origin/main$' | tr '\n' ' ')"
[ -z "$extra" ] && ok "no extra remote branches" || warn "extra remote branches: $extra"

# ── verdict ──────────────────────────────────────────────────────────────────
echo
if [ "$fails" -gt 0 ]; then
  echo "SYSTEM NOT READY — $fails failure(s), $warns warning(s)"; exit 1
elif [ "$warns" -gt 0 ]; then
  echo "SYSTEM READY (with $warns warning(s))"; exit 2
fi
echo "SYSTEM READY"
