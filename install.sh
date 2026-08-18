#!/usr/bin/env bash
# =============================================================================
#  install.sh — one-command deploy of the Telegram-bot AI agent on a fresh VPS.
#
#  Unzip the kit, then:
#      ./install.sh                     # interactive — prompts for each secret
#      cp secrets.env.example secrets.env && nano secrets.env && ./install.sh
#      ./install.sh --secrets /path/to/secrets.env --yes   # non-interactive (agent)
#
#  Flags:
#    --dest DIR        where to install the repo (default /srv/$USER/ai-agents-config)
#    --secrets FILE    read secrets from FILE instead of prompting
#    --yes             non-interactive (fail if a required secret is missing)
#    --skip-apt        don't apt-install system packages (assume present)
#    --skip-enroll     don't run the interactive MTProto/userbot Telegram login
#    --skip-claude     don't scaffold the Claude Code side
#    --owner NAME      the human this manager serves (default: your GitHub name, else $USER)
#    --gh-owner LOGIN  GitHub account new repos belong to (default: `gh api user`, else $USER)
#    --project-root D  where YOUR projects/content live (default: the kit dir if it
#                      carries content next to the kit, else ~/workspaces). Profiles
#                      bound to one directory (`runFrom`) and the job defaults resolve
#                      against it — the SYSTEM installs under --dest, your content
#                      does not move.
#
#  It does every mechanical step, writes+locks the secrets, binds to YOUR bot,
#  starts the gateway, and verifies "telegram: connected". Steps that truly need
#  a human (upstream OAuth `hermes auth`, receiving the SMS login code) are run
#  interactively or listed at the end.
# =============================================================================
set -uo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="/srv/$USER/ai-agents-config"
# Where the credentials come from, in order: --secrets wins, then the XDG store, then the legacy
# in-kit path.
#
# The XDG location is first because the in-kit default puts a file full of API keys INSIDE a git
# checkout. It is gitignored, but it only survives by that one line, and the tree is something
# update.sh resets and deploy.sh clones-and-swaps. ~/.config/ai-agent-stack/ is outside all of
# that and survives a re-clone of the repo.
#
# It also removes a real trap: with the in-kit path as the only default, an account whose keys
# live in the XDG store gets "no secrets file — will prompt" and install.sh starts asking for
# credentials that are already deployed and working.
XDG_SECRETS="${XDG_CONFIG_HOME:-$HOME/.config}/ai-agent-stack/secrets.env"
if [ -f "$XDG_SECRETS" ]; then SECRETS_FILE="$XDG_SECRETS"; else SECRETS_FILE="$KIT/secrets.env"; fi
ASSUME_YES=0; SKIP_APT=0; SKIP_ENROLL=0; SKIP_CLAUDE=0; PROJECT_ROOT=""; OWNER=""; GH_OWNER=""
while [ $# -gt 0 ]; do case "$1" in
  --dest) DEST="$2"; shift 2;;
  --secrets) SECRETS_FILE="$2"; shift 2;;
  --yes|-y) ASSUME_YES=1; shift;;
  --skip-apt) SKIP_APT=1; shift;;
  --skip-enroll) SKIP_ENROLL=1; shift;;
  --skip-claude) SKIP_CLAUDE=1; shift;;
  --project-root) PROJECT_ROOT="$2"; shift 2;;
  --owner) OWNER="$2"; shift 2;;
  --gh-owner) GH_OWNER="$2"; shift 2;;
  *) echo "unknown flag: $1"; exit 2;;
esac; done

# Strip trailing slashes: `dirname /srv/foo/` is `/srv`, not `/srv/foo`, so
# `--dest /srv/foo/` made the chown below take ownership of the shared /srv — a
# root-owned directory holding other accounts' trees — instead of its parent.
DEST="${DEST%"${DEST##*[!/]}"}"; [ -z "$DEST" ] && die "--dest не может быть /"

# Where the USER's own content lives. Distinct from --dest on purpose: the system
# installs into /srv/<user>/…, while content stays wherever the person keeps it (for
# the 3dlook kit that is the repo itself, which carries marketing_vb/ beside the
# kit). A profile bound to one directory resolves against this, so guessing it wrong
# means those profiles load and see nothing.
if [ -z "$PROJECT_ROOT" ]; then
  if [ -d "$KIT/marketing_vb" ]; then PROJECT_ROOT="$KIT"; else PROJECT_ROOT="$HOME/workspaces"; fi
fi
PROJECT_ROOT="${PROJECT_ROOT%/}"

# WHO this system serves. SOUL.md and the vps-orchestration skill name the owner in
# sentences the agent obeys — "merges are <owner>'s decision", "ask <owner> first" —
# and the skill tells it to create repos under a GitHub account. Shipped with the
# author's name baked in, a fresh install produces a manager that defers to a person
# who is not its user and pushes to an account it cannot write to.
if [ -z "$GH_OWNER" ]; then
  GH_OWNER="$(gh api user --jq .login 2>/dev/null || true)"; : "${GH_OWNER:=$USER}"
fi
if [ -z "$OWNER" ]; then
  OWNER="$(gh api user --jq '.name // .login' 2>/dev/null || true)"; : "${OWNER:=$USER}"
fi

HHOME="${HERMES_HOME:-$HOME/.hermes}"
BOT="$DEST/agents-ai/telegram-bot-agent"
HSRC="$BOT/hermes-agent"; CSRC="$BOT/claude-code-agent"
TODO=()
c(){ printf '\n\033[1;36m▶ %s\033[0m\n' "$*"; }
ok(){ printf '  \033[1;32m✓\033[0m %s\n' "$*"; }
warn(){ printf '  \033[1;33m⚠\033[0m %s\n' "$*"; }
die(){ printf '\033[1;31m✗ %s\033[0m\n' "$*"; exit 1; }
todo(){ TODO+=("$*"); }
gen_fernet(){ python3 -c "from cryptography.fernet import Fernet;print(Fernet.generate_key().decode())" 2>/dev/null || openssl rand -base64 32 | tr '+/' '-_'; }
gen_token(){ python3 -c "import secrets;print(secrets.token_urlsafe(32))" 2>/dev/null || openssl rand -hex 24; }

# ── 0. prereqs ───────────────────────────────────────────────────────────────
c "0/8 Prerequisites"
if [ "$SKIP_APT" = 0 ] && command -v apt-get >/dev/null; then
  if command -v sudo >/dev/null || [ "$(id -u)" = 0 ]; then
    ${SUDO:-sudo} apt-get update -qq && ${SUDO:-sudo} apt-get install -y -qq \
      git python3 python3-venv python3-pip sqlite3 curl jq nodejs npm >/dev/null 2>&1 \
      && ok "system packages installed" || warn "apt install had issues — continuing"
  else warn "no sudo — skipping apt (ensure git/python3/venv/node/npx present)"; fi
fi
for b in git python3; do command -v "$b" >/dev/null || die "missing: $b"; done
python3 -c "import venv" 2>/dev/null || warn "python3-venv missing — hermes install may fail"
command -v npx >/dev/null || { warn "node/npx missing — MCP + Claude Code need it"; todo "install Node.js (npx)"; }
loginctl enable-linger "$USER" >/dev/null 2>&1 || ${SUDO:-sudo} loginctl enable-linger "$USER" >/dev/null 2>&1 || warn "could not enable-linger (services may stop on logout)"
export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
# Append to whichever login file the user ALREADY has. Creating ~/.bash_profile
# where only ~/.profile exists (the Debian/Ubuntu default this script targets)
# makes bash stop reading ~/.profile on login, quietly dropping ~/.bashrc,
# ~/.local/bin from PATH and nvm from every SSH session.
_PROFILE="$HOME/.bash_profile"
[ -e "$_PROFILE" ] || { [ -e "$HOME/.profile" ] && _PROFILE="$HOME/.profile"; }
grep -q 'XDG_RUNTIME_DIR' "$_PROFILE" 2>/dev/null || echo 'export XDG_RUNTIME_DIR=/run/user/$(id -u)' >> "$_PROFILE"
ok "prereqs ok"

# ── 1. place the repo at DEST + make paths portable ──────────────────────────
c "1/8 Install repo → $DEST"
if [ "$KIT" != "$DEST" ]; then
  ${SUDO:-sudo} mkdir -p "$(dirname "$DEST")" 2>/dev/null || mkdir -p "$(dirname "$DEST")"
  [ -w "$(dirname "$DEST")" ] || ${SUDO:-sudo} chown "$USER:$USER" "$(dirname "$DEST")" 2>/dev/null || true
  mkdir -p "$DEST"
  cp -r "$KIT/agents-ai" "$KIT/bootstrap-vps.sh" "$KIT/REPRODUCE.md" "$DEST/" 2>/dev/null
  [ -f "$KIT/README.md" ] && cp "$KIT/README.md" "$DEST/" 2>/dev/null || true
  ok "kit copied to $DEST"
else ok "running in place at $DEST"; fi
# Rewrite the author's canonical paths → this machine's. BOTH roots matter: only
# /srv was rewritten before, so /home/sergiy_prod survived into places that decide
# whether the system runs at all — the conductor unit's Environment=HOME (a home
# the new user cannot even read: 0750), vault-sync's ExecStart, the file-tool
# guard's TARGET (patch silently applies to nothing), and the claude-switcher's
# default WORKDIR, i.e. the project directory of every single tab.
# Most specific first: $DEST before /srv/$USER, or the repo path gets half-rewritten.
# The bare account name is rewritten last, after the paths: it survives in prose
# that the agent READS AS INSTRUCTIONS — SOUL.md tells Hermes "don't touch anything
# outside sergiy_prod", which on a ported box points the new owner's manager at
# someone else's account.
# The template carries @DEST@ / @HOME@ / @USER@ rather than the author's real paths, so this is a
# token substitution — see scripts/render.sh, which does the same job for an already-deployed tree.
# @DEST@ goes FIRST: it is the longest token and its expansion contains the others'.
#
# YOUR_USER is included here and NOT in render.sh, and the difference is deliberate: install.sh
# DEPLOYS config.yaml.example into ~/.hermes/config.yaml, so its human placeholder has to be
# resolved. render.sh only maintains the /srv tree, where an example must stay an example.
grep -rlI -e "@DEST@" -e "@HOME@" -e "@USER@" -e "YOUR_USER" "$DEST/agents-ai" 2>/dev/null \
  | xargs -r sed -i "s|@DEST@|$DEST|g; s|@HOME@|$HOME|g; s|@USER@|$USER|g; s|YOUR_USER|$USER|g"
# @PROJECT_ROOT@ cannot ride the rewrite above: content does not live under /srv with
# the system, so there is no author path to swap — the token carries the answer.
#
# hermes-update.py IS EXCLUDED, and that exclusion is load-bearing. It is the renderer that
# re-applies these same tokens after every `hermes update` (_render_identity), so it holds
# ("@OWNER@", "HERMES_OWNER") as CODE — a table of token→env-var pairs. Substituting into it
# rewrote the table to ("Vadim Bilan", "HERMES_OWNER"), which means the updater no longer
# recognises @OWNER@ at all: the next `hermes update` overwrites SOUL.md with the upstream
# default and the re-render silently leaves a literal "@OWNER@" in the persona the agent is
# handed as its instructions. Found live on vadim_prod, in the /srv copy AND in the deployed
# ~/.hermes/hermes-update.py.
#
# It renders itself for its own file anyway; nothing needs us to do it here.
grep -rlI --exclude='hermes-update.py' -e "@PROJECT_ROOT@" -e "@OWNER@" -e "@GH_OWNER@" "$DEST/agents-ai" 2>/dev/null \
  | xargs -r sed -i "s|@PROJECT_ROOT@|$PROJECT_ROOT|g; s|@GH_OWNER@|$GH_OWNER|g; s|@OWNER@|$OWNER|g"
ok "paths rewritten to $USER / $DEST / $HOME; projects=$PROJECT_ROOT; owner=$OWNER ($GH_OWNER)"

# ── 2. upstream hermes-agent ─────────────────────────────────────────────────
c "2/8 Upstream hermes-agent"
if [ -x "$HHOME/hermes-agent/venv/bin/python" ]; then ok "already installed"
else
  mkdir -p "$HHOME"
  if curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/setup-hermes.sh 2>/dev/null | bash 2>/dev/null && [ -d "$HHOME/hermes-agent" ]; then
    ok "installed via setup-hermes.sh"
  elif git clone --depth 1 https://github.com/NousResearch/hermes-agent.git "$HHOME/hermes-agent" 2>/dev/null; then
    ( cd "$HHOME/hermes-agent" && python3 -m venv venv && ./venv/bin/pip install -q -e . ) && ok "installed manually"
  else warn "could not auto-install hermes-agent"; todo "Install upstream hermes-agent (SETUP.md §2), then re-run"; fi
fi

# ── 3. secrets → config (the bind-to-bot step) ───────────────────────────────
c "3/8 Secrets & bot binding"
declare -A S
load_secret(){ # name required?  → sets S[name]
  # `local` expands all of its arguments BEFORE it assigns any of them, so a
  # v="${!n:-}" written on this same line indirects through an empty name and
  # bash aborts the expansion with "invalid indirect expansion". The env-var path
  # then silently never worked — the grep below covered for it — while every call
  # printed the error twice to stderr. Assign n first, indirect afterwards.
  local n="$1" req="${2:-0}" v=""
  v="${!n:-}"
  [ -z "$v" ] && v="$(grep -E "^$n=" "$SECRETS_FILE" 2>/dev/null | head -1 | cut -d= -f2- | sed 's/[[:space:]]*#.*//;s/[[:space:]]*$//')"
  if [ -z "$v" ] && [ "$ASSUME_YES" = 0 ] && [ -t 0 ]; then
    if [ "$req" = secret ]; then read -rsp "  · $n: " v; echo; else read -rp "  · $n${req:+ (required)}: " v; fi
  fi
  [ -z "$v" ] && [ "$req" = 1 ] && die "required secret missing: $n (fill secrets.env or run interactively)"
  S[$n]="$v"
}
[ -f "$SECRETS_FILE" ] && { set -a; . "$SECRETS_FILE"; set +a; ok "loaded $(basename "$SECRETS_FILE")"; } || warn "no secrets file — will prompt"
load_secret TELEGRAM_BOT_TOKEN 1
load_secret TELEGRAM_ALLOWED_USERS 1
# Model routing goes through llm-failover-proxy only, and its `opencode` provider
# hits the ZEN endpoint (https://opencode.ai/zen/v1) — so ZEN is the key that matters
# and GO is no longer part of the stack. GO stays readable but optional: a secrets.env
# written before the switch carries only GO, and failing an install over a renamed key
# would be gratuitous. Order matters — GO must load before the fallback runs.
load_secret OPENCODE_GO_API_KEY 0
load_secret OPENCODE_ZEN_API_KEY 0
[ -z "${S[OPENCODE_ZEN_API_KEY]}" ] && S[OPENCODE_ZEN_API_KEY]="${S[OPENCODE_GO_API_KEY]}"
[ -z "${S[OPENCODE_ZEN_API_KEY]}" ] && die "required secret missing: OPENCODE_ZEN_API_KEY (fill secrets.env or run interactively)"
# Free-provider keys for the backup coder (optional — the morning report asks
# for whatever is missing, so an empty value is a valid starting state).
# Every provider the router can rotate through must be listed: a key filled into
# secrets.env but not read here is silently dropped, and the morning report then
# asks Telegram for a key the user already provided. ModelScope and Cloudflare
# are two of the top-3 free catalogues, so they were exactly that gap.
for k in OPENROUTER_API_KEY NVIDIA_API_KEY MODELSCOPE_API_KEY \
         CLOUDFLARE_API_KEY CLOUDFLARE_ACCOUNT_ID; do load_secret "$k" 0; done
for k in TG_API_ID TG_API_HASH TG_PHONE TG_PASSWORD GEMINI_API_KEY GROQ_API_KEY \
         GITHUB_PERSONAL_ACCESS_TOKEN POSTGRES_CONNECTION_STRING MAGIC_API_KEY; do load_secret "$k" 0; done
# auto-generate crypto material if absent
: "${MTPROTO_SESSION_KEY:=}"; [ -n "${S[TG_API_ID]:-}" ] && S[MTPROTO_SESSION_KEY]="${MTPROTO_SESSION_KEY:-$(gen_fernet)}"
S[CONDUCTOR_BRIDGE_TOKEN]="${CONDUCTOR_BRIDGE_TOKEN:-$(gen_token)}"

mkdir -p "$HHOME"
# --- ~/.hermes/.env (preserve an existing one — only scaffold if absent, so a
#     re-run on a live box never wipes real keys; _set updates in place below) ---
[ -f "$HHOME/.env" ] || cp "$HSRC/.env.example" "$HHOME/.env"
# A value containing a space MUST be quoted: this file is read back with
# `set -a; . .env`, and an unquoted HERMES_OWNER=Vadim Bilan makes bash set
# HERMES_OWNER=Vadim and then try to RUN `Bilan`. Every consumer that sourced the
# file got a truncated owner name plus "command not found" on stderr. A one-word
# owner (Sergiy) hid it; the first two-word owner surfaced it.
_set(){ local k="$1" v="$2"; [ -z "$v" ] && return
  case "$v" in *[[:space:]]*) v="\"$v\"";; esac
  if grep -qE "^$k=" "$HHOME/.env"; then sed -i "s|^$k=.*|$k=$v|" "$HHOME/.env"; else echo "$k=$v" >> "$HHOME/.env"; fi; }
_set TELEGRAM_BOT_TOKEN "${S[TELEGRAM_BOT_TOKEN]}"; _set TELEGRAM_ALLOWED_USERS "${S[TELEGRAM_ALLOWED_USERS]}"
_set OPENCODE_GO_API_KEY "${S[OPENCODE_GO_API_KEY]}"; _set OPENCODE_ZEN_API_KEY "${S[OPENCODE_ZEN_API_KEY]}"
_set GEMINI_API_KEY "${S[GEMINI_API_KEY]}"; _set OPENAI_API_KEY "${S[GEMINI_API_KEY]}"; _set GROQ_API_KEY "${S[GROQ_API_KEY]}"
# Point at the RUNTIME vault, not the seed in the config tree — see the seeding step below.
_set WIKI_PATH "$HHOME/AI-Second-Brain"; _set OBSIDIAN_VAULT_PATH "$HHOME/AI-Second-Brain"
# The Telegram switcher's projects root, and the fallback for conductor jobs that
# name no work_dir. Without it both fall back to ~/workspaces, which on a box where
# projects live elsewhere is an empty or missing directory.
_set HERMES_CLAUDE_SWITCHER_WORKDIR "$PROJECT_ROOT"
_set HERMES_OWNER "$OWNER"; _set HERMES_GH_OWNER "$GH_OWNER"; _set HERMES_PROJECT_ROOT "$PROJECT_ROOT"
# --- config.yaml / mem0 / SOUL ---
[ -f "$HHOME/config.yaml" ] || cp "$HSRC/config.yaml.example" "$HHOME/config.yaml"
[ -f "$HHOME/mem0.json" ]    || cp "$HSRC/mem0.json.example"    "$HHOME/mem0.json"
cp "$HSRC/SOUL.md" "$HHOME/SOUL.md"
# --- mtproto + userbot creds ---
if [ -n "${S[TG_API_ID]}" ]; then
  mkdir -p "$HHOME/mtproto" "$HHOME/telegram-userbot"
  printf 'TG_API_ID=%s\nTG_API_HASH=%s\nMTPROTO_SESSION_KEY=%s\n' "${S[TG_API_ID]}" "${S[TG_API_HASH]}" "${S[MTPROTO_SESSION_KEY]}" > "$HHOME/mtproto/creds.env"
  printf 'TG_API_ID=%s\nTG_API_HASH=%s\nTG_PHONE=%s\nTG_PASSWORD=%s\n' "${S[TG_API_ID]}" "${S[TG_API_HASH]}" "${S[TG_PHONE]}" "${S[TG_PASSWORD]}" > "$HHOME/telegram-userbot/.env"
fi
mkdir -p "$HHOME/conductor-bridge"
printf 'CONDUCTOR_BRIDGE_TOKEN=%s\nBRIDGE_HOST=172.20.0.1\nBRIDGE_PORT=8790\nBRIDGE_DEFAULT_PROFILE=dev\nBRIDGE_DEFAULT_WORKDIR=%s\nBRIDGE_DEFAULT_MAX_TURNS=40\n' "${S[CONDUCTOR_BRIDGE_TOKEN]}" "$PROJECT_ROOT" > "$HHOME/conductor-bridge/bridge.env"
chmod 600 "$HHOME/.env" "$HHOME/config.yaml" "$HHOME/mem0.json" 2>/dev/null
chmod 600 "$HHOME/mtproto/creds.env" "$HHOME/telegram-userbot/.env" "$HHOME/conductor-bridge/bridge.env" 2>/dev/null
# The source file too. secrets.env.example promises "install.sh chmod 600's
# everything", but the file the user is told to fill in — the one holding the bot
# token, TG api_hash, the PAT and the PG password all at once — sits in the
# unpacked kit at whatever the umask gave it (0664) and was never touched.
[ -e "$SECRETS_FILE" ] && chmod 600 "$SECRETS_FILE" 2>/dev/null || true
ok "secrets written to ~/.hermes (chmod 600); bound to bot ...${S[TELEGRAM_BOT_TOKEN]: -6}"

# ── 4. mechanical scaffolding (ops, skills, patches, units, claude) ──────────
c "4/8 Scaffolding (ops · skills · patches · units)"
# --skip-claude has to reach bootstrap, which scaffolds ~/.mcp.json and the whole
# ~/.claude tree in its section 7. CLAUDE_FLAG was assigned here and then never
# used — the flag documented at the top as "don't scaffold the Claude Code side"
# did nothing at all.
BOOT_ARGS=(); [ "$SKIP_CLAUDE" = 1 ] && BOOT_ARGS+=(--skip-claude)
BOOT_LOG="$(mktemp -t hermes-bootstrap.XXXXXX)"
bash "$DEST/bootstrap-vps.sh" "${BOOT_ARGS[@]}" >"$BOOT_LOG" 2>&1 && ok "bootstrap-vps.sh done" || warn "bootstrap-vps.sh reported issues (see $BOOT_LOG)"

# ── 4b. memory (Qdrant) + backup coder (OpenCode) ────────────────────────────
c "4b/8 Memory store (Qdrant) + backup coding agent (OpenCode)"

# Qdrant: mem0's default embedded mode locks its storage folder, so the SECOND
# process to open it dies with "already accessed by another instance" and memory
# silently stays empty. Run it as a service instead — loopback + API key, because
# Qdrant ships with no auth and the box may be shared.
mkdir -p "$HHOME/bin" "$HHOME/qdrant-server/storage" "$HHOME/qdrant-server/snapshots"
if [ ! -x "$HHOME/bin/qdrant" ]; then
  QV="${QDRANT_VERSION:-1.18.3}"
  QURL="https://github.com/qdrant/qdrant/releases/download/v$QV/qdrant-x86_64-unknown-linux-musl.tar.gz"
  if curl -sSL "$QURL" -o /tmp/qdrant.$$.tgz && tar xzf /tmp/qdrant.$$.tgz -C /tmp; then
    install -m 0755 /tmp/qdrant "$HHOME/bin/qdrant" && ok "qdrant $QV installed (static, no Docker)"
  else warn "qdrant download failed"; todo "Install qdrant: see hermes-agent/ops/systemd/hermes-qdrant.service"; fi
  rm -f /tmp/qdrant.$$.tgz /tmp/qdrant 2>/dev/null || true
fi
# Ports are per-user: 6333/6334 are the defaults, so a second account on the same
# host must move. Override with QDRANT_HTTP_PORT/QDRANT_GRPC_PORT.
QHTTP="${QDRANT_HTTP_PORT:-6343}"; QGRPC="${QDRANT_GRPC_PORT:-6344}"
if [ ! -f "$HHOME/qdrant-server/qdrant.env" ]; then
  QKEY="$(python3 -c 'import secrets;print(secrets.token_urlsafe(32))')"
  umask 077
  cat > "$HHOME/qdrant-server/qdrant.env" <<QENV
QDRANT__SERVICE__HOST=127.0.0.1
QDRANT__SERVICE__HTTP_PORT=$QHTTP
QDRANT__SERVICE__GRPC_PORT=$QGRPC
QDRANT__SERVICE__API_KEY=$QKEY
QDRANT__SERVICE__ENABLE_TLS=false
QDRANT__TELEMETRY_DISABLED=true
QDRANT__STORAGE__STORAGE_PATH=$HHOME/qdrant-server/storage
QDRANT__STORAGE__SNAPSHOTS_PATH=$HHOME/qdrant-server/snapshots
QENV
  chmod 600 "$HHOME/qdrant-server/qdrant.env"
  ok "qdrant.env written (127.0.0.1:$QHTTP, API key generated)"
else
  # A re-run on a box that ALREADY runs Qdrant used to read back only the API key,
  # leaving $QHTTP at the default (or whatever the caller exported) while the live
  # service kept listening on the port inside this file. mem0.json below was then
  # rewired to a port nothing answers on, and long-term memory died silently — the
  # exact outcome for anyone told "pass QDRANT_HTTP_PORT=<free port>" on a machine
  # whose Qdrant is already on another one. The existing file is the truth: it is what
  # the running unit reads.
  QKEY="$(grep '^QDRANT__SERVICE__API_KEY=' "$HHOME/qdrant-server/qdrant.env" | cut -d= -f2-)"
  _QH="$(grep '^QDRANT__SERVICE__HTTP_PORT=' "$HHOME/qdrant-server/qdrant.env" | cut -d= -f2-)"
  _QG="$(grep '^QDRANT__SERVICE__GRPC_PORT=' "$HHOME/qdrant-server/qdrant.env" | cut -d= -f2-)"
  if [ -n "$_QH" ]; then
    if [ -n "${QDRANT_HTTP_PORT:-}" ] && [ "$QDRANT_HTTP_PORT" != "$_QH" ]; then
      warn "QDRANT_HTTP_PORT=$QDRANT_HTTP_PORT ignored — qdrant.env already says $_QH (the running service uses that). Edit qdrant.env + restart hermes-qdrant to actually move it."
    fi
    QHTTP="$_QH"; ok "qdrant already configured on 127.0.0.1:$QHTTP (kept)"
  fi
  [ -n "$_QG" ] && QGRPC="$_QG"
fi
# Point mem0 at the SERVER and pin https:false — qdrant-client silently switches to
# HTTPS as soon as api_key is set, then fails with SSL: WRONG_VERSION_NUMBER.
python3 - "$HHOME/mem0.json" "$QKEY" "$QHTTP" <<'PYMEM' || warn "could not rewire mem0.json"
import json, os, sys
path, key, port = sys.argv[1], sys.argv[2], int(sys.argv[3])
cfg = json.load(open(path))
vs = cfg.setdefault("oss", {}).setdefault("vector_store", {"provider": "qdrant"})
c = vs.setdefault("config", {})
c.pop("path", None)
c.update({"host": "127.0.0.1", "port": port, "api_key": key, "https": False})
c.setdefault("collection_name", "hermes_mem0")
json.dump(cfg, open(path, "w"), indent=2, ensure_ascii=False)
os.chmod(path, 0o600)
print("mem0 -> qdrant server")
PYMEM

# Free-provider keys for the backup coder. The morning router asks in Telegram for
# whatever is missing here, so an empty file is a fine starting state.
if [ ! -f "$HHOME/ai-models.env" ]; then
  cp "$HSRC/ops/ai-models.env.example" "$HHOME/ai-models.env" 2>/dev/null || : > "$HHOME/ai-models.env"
  # The example ships illustrative values (nvapi-YOUR_KEY, ms-YOUR_TOKEN, …) and the
  # router reads "k=v with a non-empty v" as a key it has. Copied verbatim, a fresh
  # box therefore claims keys for every provider, and each one 401s on probe —
  # burning the morning pick's time and hiding the real "no key here, ask for it"
  # state. Comment the placeholders out; real values are appended just below.
  sed -i -E 's/^([A-Z0-9_]+)=(.*YOUR_(KEY|TOKEN).*)$/# \1=\2/' "$HHOME/ai-models.env" 2>/dev/null || true
  chmod 600 "$HHOME/ai-models.env"
fi
for V in OPENROUTER_API_KEY NVIDIA_API_KEY MODELSCOPE_API_KEY \
         CLOUDFLARE_API_KEY CLOUDFLARE_ACCOUNT_ID GEMINI_API_KEY GROQ_API_KEY; do
  [ -n "${S[$V]:-}" ] && { grep -q "^$V=" "$HHOME/ai-models.env" \
      && sed -i "s|^$V=.*|$V=${S[$V]}|" "$HHOME/ai-models.env" \
      || printf '%s=%s\n' "$V" "${S[$V]}" >> "$HHOME/ai-models.env"; }
done
ok "ai-models.env ready (0600)"

# OpenCode CLI = the backup coder. Three things make `opencode run` print NOTHING
# and exit 0: no provider creds, a PAID small_model (its 401 kills the stream), and
# a cwd outside a git repo. The first two are set up here; the router refreshes the
# model ids every morning.
if [ -n "${S[OPENCODE_ZEN_API_KEY]:-}" ]; then
  mkdir -p "$HOME/.config/opencode" "$HOME/.local/share/opencode"
  python3 - "$HOME/.local/share/opencode/auth.json" "${S[OPENCODE_ZEN_API_KEY]}" <<'PYAUTH' || true
import json, os, sys
path, key = sys.argv[1], sys.argv[2]
try: d = json.load(open(path))
except Exception: d = {}
d.setdefault("opencode", {"type": "api", "key": key})     # 'opencode' = free Zen tier
json.dump(d, open(path, "w"), indent=2); os.chmod(path, 0o600)
PYAUTH
  [ -f "$HOME/.config/opencode/opencode.jsonc" ] || \
    cp "$BOT/opencode-agent/opencode.jsonc.example" "$HOME/.config/opencode/opencode.jsonc" 2>/dev/null || true
  ok "OpenCode configured (zen creds + free small_model)"
else
  todo "OpenCode backup coder: add OPENCODE_ZEN_API_KEY, then rerun (see opencode-agent/README.md)"
fi

# ── 5. systemd + cron ────────────────────────────────────────────────────────
c "5/8 Services (systemd + cron)"
mkdir -p "$HOME/.config/systemd/user"
cp "$HSRC/ops/systemd/"*.service "$HSRC/ops/systemd/"*.timer "$HOME/.config/systemd/user/" 2>/dev/null || true
sed -i "s|/srv/sergiy_prod|/srv/$USER|g; s|/home/sergiy_prod|$HOME|g" "$HOME/.config/systemd/user/"*.service 2>/dev/null || true
mkdir -p "$HHOME/model-router/cache"   # BEFORE the copy: the cp silently no-op'd without it
cp "$HSRC/ops/model-router/"*.py "$HSRC/ops/model-router/"*.json "$HHOME/model-router/" 2>/dev/null || true
cp "$HSRC/ops/hermes-update.py" "$HHOME/" 2>/dev/null
# THE VAULT IS RUNTIME CONTENT, so it lives in ~/.hermes — not inside the config tree.
#
# It used to live at $HSRC/AI-Second-Brain, i.e. inside a repo that update.sh resets and
# re-renders. Anything the agent wrote there was one update away from being discarded, and
# vault-sync.sh existed to paper over that by committing and pushing FROM a runtime replica —
# which is how a `git pull --rebase --autostash` every 30 minutes came to leave conflict markers
# in every profiles/*.json on one account.
#
# The repo copy is now purely a SEED (a schema, a README and empty directories). Seeded once,
# never overwritten: a re-run must not touch a vault the owner has since filled.
if [ ! -d "$HHOME/AI-Second-Brain" ]; then
  cp -r "$HSRC/AI-Second-Brain" "$HHOME/AI-Second-Brain" 2>/dev/null \
    && ok "vault seeded → $HHOME/AI-Second-Brain" || warn "could not seed the vault"
else ok "vault already present — left untouched"; fi
# The shared heaviness rule. Both the switcher and the suggest-stronger-model hook
# import it BY PATH and fall back to a weaker built-in copy when it is missing — so a
# fresh install without this line silently runs the looser rule, which is the exact
# drift ops/task-heaviness.py exists to end. Observed on a real install.
cp "$HSRC/ops/task-heaviness.py" "$HHOME/task-heaviness.py" 2>/dev/null && chmod 0644 "$HHOME/task-heaviness.py"
mkdir -p "$HHOME/agent-hooks"
cp "$HSRC/ops/agent-hooks/"*.py "$HHOME/agent-hooks/" 2>/dev/null; chmod +x "$HHOME/agent-hooks/"*.py 2>/dev/null
systemctl --user daemon-reload 2>/dev/null || true
systemctl --user enable --now hermes-qdrant.service 2>/dev/null && ok "hermes-qdrant enabled+started" || warn "hermes-qdrant not started — memory will be dead"
systemctl --user enable --now hermes-gateway.service 2>/dev/null && ok "hermes-gateway enabled+started" || { warn "could not start hermes-gateway via systemctl --user"; todo "systemctl --user enable --now hermes-gateway.service"; }
# vault-sync.timer is deliberately NOT here. It ran `git pull --rebase --autostash` on the
# runtime tree every 30 minutes, which on a rendered tree leaves conflict markers, and in the whole
# history of this repo its commit half never fired once. Disabling it by hand was not enough while
# this loop re-enabled it on every install.
for t in model-router-refresh.timer hermes-update.timer; do systemctl --user enable --now "$t" 2>/dev/null || true; done
systemctl --user disable --now vault-sync.timer 2>/dev/null || true
MON="$HSRC/ops/conductor-monitor.sh"
crontab -l 2>/dev/null | grep -qF "$MON" || { (crontab -l 2>/dev/null; echo "*/5 * * * * $MON >> $HHOME/conductor-monitor.log 2>&1") | crontab - && ok "conductor-monitor cron added"; }
"$MON" --init >/dev/null 2>&1 || true

# ── 6. Telegram session enrollment (interactive) ─────────────────────────────
c "6/8 Telegram MTProto/userbot enrollment"
if [ "$SKIP_ENROLL" = 1 ] || [ -z "${S[TG_API_ID]}" ]; then warn "skipped (no TG_* creds or --skip-enroll)"
elif [ -t 0 ] && [ "$ASSUME_YES" = 0 ]; then
  ( cd "$HHOME/mtproto" && python3 -m venv venv >/dev/null 2>&1 && ./venv/bin/pip install -q telethon cryptography >/dev/null 2>&1 ) || true
  echo "  A Telegram login code will be sent to ${S[TG_PHONE]}. Follow the prompts."
  # The program must live in a FILE, not a heredoc: a heredoc IS stdin, so telethon's
  # input() for the login code hit EOF and enrollment could never succeed interactively.
  # Passing the phone explicitly also drops one prompt — only the code (and the 2FA
  # password, when the account has one) is asked for.
  cat > "$HHOME/mtproto/enroll.py" <<'PY'
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from cryptography.fernet import Fernet
client = TelegramClient(StringSession(), int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])
client.start(phone=os.environ.get("TG_PHONE") or None)
me = client.get_me(); print(f"signed in as {me.first_name} | @{me.username} | id {me.id}")
s = client.session.save(); client.disconnect()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "session.enc")
open(out, "wb").write(Fernet(os.environ["MTPROTO_SESSION_KEY"].encode()).encrypt(s.encode()))
os.chmod(out, 0o600); print("OK")
PY
  chmod 600 "$HHOME/mtproto/enroll.py"
  if ( cd "$HHOME/mtproto" && set -a && . creds.env && set +a && ./venv/bin/python ./enroll.py ); then
    ok "MTProto session enrolled (session.enc)"
  else warn "MTProto enrollment skipped/failed"; todo "Enroll MTProto later: ops/mtproto/README.md"; fi
else warn "non-interactive — cannot receive SMS code"; todo "Enroll MTProto+userbot sessions (interactive): ops/mtproto/README.md, ops/telegram-userbot/README.md"; fi

# ── 7. Claude Code side ──────────────────────────────────────────────────────
c "7/8 Claude Code side"
if [ "$SKIP_CLAUDE" = 1 ]; then warn "skipped (--skip-claude)"
else
  # settings + MCP already scaffolded by bootstrap; inject the tokens we have
  # Lock it BEFORE writing anything secret into it. bootstrap created ~/.mcp.json
  # with the default umask (0664 here), and this step seds a GitHub PAT and a
  # Postgres connection string into it — while the six files below get chmod 600
  # and this one never did. On this box /home/sergiy_prod happens to be 0750; on a
  # stock Debian/Ubuntu VPS, which is what this script targets, /home/<user> is
  # 0755 and every local account could read both.
  [ -e "$HOME/.mcp.json" ] && chmod 600 "$HOME/.mcp.json" 2>/dev/null || true
  [ -n "${S[GITHUB_PERSONAL_ACCESS_TOKEN]}" ] && sed -i "s|REPLACE_WITH_GH_PAT|${S[GITHUB_PERSONAL_ACCESS_TOKEN]}|" "$HOME/.mcp.json" 2>/dev/null || true
  [ -n "${S[POSTGRES_CONNECTION_STRING]}" ] && sed -i "s|REPLACE_WITH_PG_CONN_STRING|${S[POSTGRES_CONNECTION_STRING]}|" "$HOME/.mcp.json" 2>/dev/null || true
  command -v claude >/dev/null && ok "claude CLI present" || todo "Install Claude Code: sudo npm i -g @anthropic-ai/claude-code"
  command -v codebase-memory-mcp >/dev/null || todo "Install codebase-memory: curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config"
  [ -x "$CSRC/DEV/switch-profile.sh" ] && todo "Activate default system: $CSRC/DEV/switch-profile.sh dev  (then restart Claude Code)"
fi

# ── 8. verify + report ───────────────────────────────────────────────────────
c "8/8 Verify"
sleep 3
STATE="$(python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.hermes/gateway_state.json'))).get('platforms',{}).get('telegram',{}).get('state','?'))" 2>/dev/null || echo '?')"
if [ "$STATE" = connected ]; then ok "TELEGRAM CONNECTED — the bot is live. Send it a message."
else warn "telegram state: $STATE — check: systemctl --user status hermes-gateway ; ~/.hermes/logs/gateway.log"; fi
todo "hermes auth   (provider OAuth, if your LLM provider needs it)"
todo "Recreate Hermes cron jobs: cp $HSRC/cron/jobs.json.example ~/.hermes/cron/jobs.json (edit chat_id)"
printf '\n\033[1;35m════ REMAINING (%d) ════\033[0m\n' "${#TODO[@]}"; i=1; for t in "${TODO[@]}"; do printf '  %2d. %s\n' "$i" "$t"; i=$((i+1)); done
printf '\n\033[1;32m✔ Install complete.\033[0m  Bot bound to token …%s. Verify per REPRODUCE.md.\n' "${S[TELEGRAM_BOT_TOKEN]: -6}"
