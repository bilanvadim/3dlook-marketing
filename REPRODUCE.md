# Reproduce this bot on any VPS

Everything needed to stand up the **Ivan Djedaev** Telegram-bot AI agent
(Hermes orchestrator + Claude Code systems) on a fresh server. The repo tracks all
**code + config templates**; real secrets are never committed — you supply them once.

## One-command install (zip kit)

Build a self-contained zip and deploy it anywhere:

```
bash make-release.sh                      # → dist/ai-agent-bot-<sha>.zip  (no secrets inside)
```
On the fresh VPS:
```
unzip ai-agent-bot-*.zip && cd ai-agent-bot
cp secrets.env.example secrets.env && nano secrets.env    # bot token + TG API id/hash + keys
./install.sh                                               # installs everything, binds to your bot, starts it
```
`install.sh` does it all — prereqs, upstream hermes-agent, path rewrite for this
machine, writes+locks your secrets (auto-generates the Fernet/bridge keys),
scaffolds ops/skills/patches/units, enrols the Telegram session interactively,
starts the gateway, and verifies **telegram: connected**. Steps needing a human
(provider OAuth, the SMS login code when non-interactive) are prompted or printed
as a short TODO list. Fully non-interactive for an agent:
`./install.sh --secrets secrets.env --yes`.

> The mechanical-only subset (no secrets, no bind) is still available as
> `bash bootstrap-vps.sh` — it prints a TODO checklist instead of prompting.

## What the repo gives you (vs what you provide)

| Layer | In git (reproducible) | You provide (secrets / enrollment) |
|---|---|---|
| **Hermes** | ops (model-router, claude-switcher, patchers, vault-sync, hermes-update), systemd unit templates, SOUL.md, `*.example` for `.env`/`config.yaml`/`mem0.json`, skills | `~/.hermes/.env`, `config.yaml`, `mem0.json`, `auth.json` (`hermes auth`) |
| **Forward-picker** | `ops/mtproto/list_topics.py` + README (Fernet enrollment) | `mtproto/creds.env` + minted `session.enc` |
| **Userbot** | `ops/telegram-userbot/*.py` + README | `telegram-userbot/.env` + minted `session.session` |
| **Conductor bridge** | `ops/conductor-bridge/bridge.py` + unit template | `conductor-bridge/bridge.env` (only if you run an external job producer) |
| **Cron jobs** | `cron/jobs.json.example` | `~/.hermes/cron/jobs.json` (your scheduled prompts) |
| **Claude Code** | 5 systems (dev/seo/marketing/security/**test**) as marketplaces, switcher, hooks, permission baseline, `config/*.example` (MCP + settings) | GH PAT, Postgres conn, magic API key; codebase-memory binary; `hermes/claude` account auth |

## Order of operations
1. **Clone** the repo to `/srv/<user>/ai-agents-config` (paths in templates assume this; adjust `YOUR_USER`).
2. **Install upstream hermes-agent** into `~/.hermes/hermes-agent` — see [`hermes-agent/SETUP.md`](agents-ai/telegram-bot-agent/hermes-agent/SETUP.md) §2.
3. **`bash bootstrap-vps.sh`** — scaffolds config, copies ops+skills, applies patches, stages runtime helpers, installs unit/cron templates, scaffolds the Claude Code side.
4. **Work the printed TODO list** — fill `.env`/`config.yaml`, `hermes auth`, enroll MTProto + userbot sessions, enable systemd units + cron, run `claude-code-agent/DEV/switch-profile.sh dev-sm`, install the codebase-memory binary.
5. **Verify** per SETUP.md §verify: `gateway_state.json.platforms.telegram.state == "connected"`, DM the bot, `/tabs` works, model-router posts "🌅 Модель дня", a forward shows the topic-picker.

## Detailed guides
- Hermes side: [`agents-ai/telegram-bot-agent/hermes-agent/SETUP.md`](agents-ai/telegram-bot-agent/hermes-agent/SETUP.md) · [`CONFIG.md`](agents-ai/telegram-bot-agent/hermes-agent/CONFIG.md)
- Claude Code side: [`agents-ai/telegram-bot-agent/claude-code-agent/INSTALL.md`](agents-ai/telegram-bot-agent/claude-code-agent/INSTALL.md) · [`DEV/SYSTEMS.md`](agents-ai/telegram-bot-agent/claude-code-agent/DEV/SYSTEMS.md)
- Component enrollment: `ops/mtproto/README.md` · `ops/telegram-userbot/README.md` · `ops/conductor-bridge/README.md`

> **Security:** the repo `.gitignore` blocks `.env`, `config.yaml`, `auth.json`,
> `*.session`, `*.enc`, `creds.env`, `*.key`. Never commit real credentials — only
> `*.example` templates. `chmod 600` every real secret file on the box.

## Проверки, добавленные вместе с бесплатным стеком (31.07.2026)

```bash
# 1. Память жива: Qdrant поднят, ключ обязателен, коллекция на месте
systemctl --user is-active hermes-qdrant.service                      # active
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6343/collections   # 401 (без ключа)
KEY=$(grep '^QDRANT__SERVICE__API_KEY=' ~/.hermes/qdrant-server/qdrant.env | cut -d= -f2-)
curl -s -H "api-key: $KEY" http://127.0.0.1:6343/collections | head -c 200    # 200 + hermes_mem0

# 2. Выбор моделей на день (ничего не пишет)
python3 ~/.hermes/model-router/refresh.py --dry-run

# 3. Запасной кодинг-агент. ОБЯЗАТЕЛЬНО внутри git-репозитория —
#    вне проекта opencode run молча выходит с кодом 0
cd /srv/$USER/ai-agents-config && opencode run 'Reply with exactly: BACKUP-OK'

# 4. Вкладки и тяжёлый режим доехали до бота
python3 -c "import sys;sys.path.insert(0,'$HOME/.hermes/hermes-agent');\
from hermes_cli.commands import COMMAND_REGISTRY as R;n=[c.name for c in R];\
print('heavy/normal:', all(x in n for x in ('heavy','normal')))"
```

Если п.3 печатает пустоту — причина одна из трёх, все дают `exit 0` без вывода:
нет кредов провайдера в `~/.local/share/opencode/auth.json`, платная `small_model`
в `opencode.jsonc` (её 401 убивает стрим), запуск вне git-репозитория.
Подробности — `agents-ai/telegram-bot-agent/opencode-agent/README.md`.
