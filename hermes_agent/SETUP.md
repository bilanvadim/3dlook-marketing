# Hermes Agent — полная установка с нуля на VPS

Это пошаговый гайд для воспроизведения конфигурации Hermes Agent AI на новом VPS.
Любой AI-агент (Claude Code, Gemini, opencode) может следовать этому гайду,
чтобы поднять идентичную конфигурацию. Все секреты — плейсхолдеры; подставь свои.

> **Что получится:** Telegram-бот Hermes, который:
> - отвечает в Telegram как оркестратор-менеджер (делегирует код в Claude Code);
> - каждое утро в 07:00 шлёт «🌅 Модель дня» с выбором рабочей Go-модели по формуле;
> - автоматически переключается на free-fallback при лимите Go;
> - ведёт Obsidian-вики (AI Second Brain) и синхронит его в git;
> - (опционально) управляет автономным конду́ктором для A→Z проектов.

---

## 0. Prerequisites

```bash
# OS: Ubuntu/Debian Linux, user с sudo
# Пакеты:
sudo apt update && sudo apt install -y \
  git python3 python3-venv python3-pip sqlite3 curl jq \
  nodejs npm chromium-browser   # chromium для browser-тулов Hermes

# systemd user session (linger — чтобы сервисы жили без SSH-сессии):
sudo loginctl enable-linger $USER
export XDG_RUNTIME_DIR=/run/user/$(id -u)   # добавить в ~/.bash_profile
echo 'export XDG_RUNTIME_DIR=/run/user/$(id -u)' >> ~/.bash_profile
```

## 1. Клонировать репозиторий

```bash
sudo mkdir -p /srv/$USER
sudo chown $USER:$USER /srv/$USER
cd /srv/$USER
git clone https://github.com/@GH_OWNER@/ai-agents-config.git
cd ai-agents-config
```

## 2. Установить Hermes Agent (upstream)

Hermes Agent — это Python-приложение от NousResearch. Установка через их setup-скрипт:

```bash
# Официальный установщик клонирует в ~/.hermes/hermes-agent и создаёт venv
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/setup-hermes.sh | bash
# ИЛИ вручную:
git clone https://github.com/NousResearch/hermes-agent.git ~/.hermes/hermes-agent
cd ~/.hermes/hermes-agent
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Проверка:
```bash
~/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main --version
# или: hermes --version  (если venv в PATH)
```

## 3. Конфиг ~/.hermes/config.yaml

Это главный конфиг Hermes. Полный reference: [`CONFIG.md`](./CONFIG.md).
Минимально-необходимая конфигурация для нашего setup:

```yaml
model:
  default: deepseek-v4-pro          # будет перезаписано model-router каждое утро
  provider: opencode-go             # провайдер Go (subscription, сильные модели)
  max_tokens: 16384
terminal:
  backend: local
  cwd: /srv/vadim_prod             # рабочая директория для Telegram-сессий
  timeout: 180
tool_loop_guardrails:
  warnings_enabled: true
  hard_stop_enabled: false
compression:
  enabled: true
  threshold: 0.5
  target_ratio: 0.2
  protect_last_n: 20
  protect_first_n: 3
prompt_caching:
  cache_ttl: 5m
memory:
  memory_enabled: true
  user_profile_enabled: true
  provider: mem0
  memory_char_limit: 2200
  user_char_limit: 1375
  nudge_interval: 10
  flush_min_turns: 6
session_reset:
  mode: both
  idle_minutes: 1440                # 24ч — авто-ресет простаивающей сессии
  at_hour: 4                        # + ресет в 4:00
group_sessions_per_user: true
streaming:
  enabled: false
agent:
  max_turns: 60
  verbose: false
  reasoning_effort: medium
platform_toolsets:
  cli:
  - hermes-cli
  telegram:
  - hermes-telegram
stt:
  enabled: true
  local:
    model: base
code_execution:
  timeout: 300
  max_tool_calls: 50
delegation:
  max_iterations: 50
approvals:
  mode: "off"                       # без промптов Always/Session (макс. автономия);
                                    # кавычки обязательны (bare off = YAML false)
  destructive_slash_confirm: false
display:
  compact: false
  tool_progress: all
  streaming: true
  skin: default
# fallback будет перезаписан model-router:
fallback_providers:
  - provider: opencode-zen
    model: deepseek-v4-flash-free
```

> **Важно:** `model.default` и `fallback_providers` перезаписываются автоматически
> скриптом `model-router/refresh.py` каждое утро (раздел 6). Не правь их руками —
> правь `model-strength.json` (раздел 7).

### Mem0 OSS + Gemini (без Ollama)

Скопируйте `hermes_agent/mem0.json.example` в `~/.hermes/mem0.json` и задайте
Gemini API key в `~/.hermes/.env`:

```bash
cp hermes_agent/mem0.json.example ~/.hermes/mem0.json
chmod 600 ~/.hermes/mem0.json ~/.hermes/.env
```

В `.env` используется `OPENAI_API_KEY`, потому что Mem0 обращается к Gemini
через официальный OpenAI-compatible endpoint. Сам векторный индекс Qdrant
хранится локально в `~/.hermes/mem0_qdrant`; Ollama не требуется.

## 4. Секреты ~/.hermes/.env

Готовый шаблон — [`.env.example`](./.env.example) в этом каталоге репо
(`cp hermes_agent/.env.example ~/.hermes/.env` и заполнить значения) — либо
собрать вручную тем же heredoc-ом:

```bash
cat > ~/.hermes/.env << 'EOF'
# === Провайдеры LLM ===
OPENCODE_GO_API_KEY=sk-YOUR_OPencode_GO_KEY
OPENCODE_ZEN_API_KEY=sk-YOUR_OPencode_ZEN_KEY
# (GO и ZEN могут быть одним ключом, если провайдер один)

# === Telegram ===
TELEGRAM_BOT_TOKEN=1234567890:ABC-DEF_your_bot_token_from_BotFather
TELEGRAM_ALLOWED_USERS=YOUR_TELEGRAM_USER_ID

# === AI Second Brain (Obsidian wiki) ===
WIKI_PATH=/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain
OBSIDIAN_VAULT_PATH=/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain

# === Browser (опционально) ===
AGENT_BROWSER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# === Gemini failover (опционально, для vps-orchestration skill) ===
GEMINI_API_KEY=your_gemini_api_key
EOF
chmod 600 ~/.hermes/.env
```

### Как получить значения:
| Переменная | Где взять |
|---|---|
| `OPENCODE_GO_API_KEY` / `OPENCODE_ZEN_API_KEY` | [opencode.ai](https://opencode.ai) → dashboard → API keys |
| `TELEGRAM_BOT_TOKEN` | Telegram → [@BotFather](https://t.me/BotFather) → `/newbot` |
| `TELEGRAM_ALLOWED_USERS` | Telegram → [@userinfobot](https://t.me/userinfobot) → свой numeric ID |
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) |

## 5. Persona (SOUL.md)

`~/.hermes/SOUL.md` определяет личность бота (системный промпт, ВСЕГДА в контексте).
Загружается заново на каждое сообщение — рестарт не нужен. Канонич. персона — в репо
[`SOUL.md`](./SOUL.md); просто скопируй в рантайм:

```bash
cp hermes_agent/SOUL.md ~/.hermes/SOUL.md
```

⚠️ **Не оставляй дефолтную персону NousResearch** («…writing and editing code…
executing actions via your tools») — она толкает Hermes КОДИТЬ САМ и перебивает
policy-скилл `vps-orchestration` (который грузится лишь по релевантности). Правило
«ты менеджер, не кодер; весь тех-труд — в Claude Code» должно жить в SOUL.md, т.к.
персона всегда в контексте, а скилл — нет. `hermes setup`/переустановка могут
сбросить SOUL.md на дефолт — после апдейта проверяй `head ~/.hermes/SOUL.md`.

## 6. Model Router — «Модель дня» (ежедневный выбор в 07:00)

Это ядро утреннего сообщения. Скрипт `refresh.py` каждый день:
1. Опрашивает `/models` API Go и Zen провайдеров (0 LLM-запросов, только listing).
2. Оценивает каждую Go-модель по формуле: `score = strength − cost_weight×output_cost + ctx_bonus×(context≥1M)`.
3. Выбирает лучшую Go-модель (primary) и лучшую бесплатную (fallback).
4. Пишет обе в `config.yaml` (`model.default` + `fallback_providers`).
5. Перезапускает gateway (подхватывает новую модель).
6. Делает 1 health-probe запрос к Go (проверка alive/limited).
7. Шлёт Telegram-сообщение «🌅 Модель дня».

### Установка:

```bash
# Скопировать из репо в рантайм:
mkdir -p ~/.hermes/model-router/cache
cp /srv/$USER/ai-agents-config/hermes_agent/ops/model-router/refresh.py      ~/.hermes/model-router/
cp /srv/$USER/ai-agents-config/hermes_agent/ops/model-router/router_lib.py   ~/.hermes/model-router/
cp /srv/$USER/ai-agents-config/hermes_agent/ops/model-router/model-strength.json ~/.hermes/model-router/
```

### systemd timer (запуск в 07:00 каждый день):

```bash
# Юниты уже в репо: hermes_agent/ops/systemd/model-router-refresh.{service,timer}
cp /srv/$USER/ai-agents-config/hermes_agent/ops/systemd/model-router-refresh.service ~/.config/systemd/user/
cp /srv/$USER/ai-agents-config/hermes_agent/ops/systemd/model-router-refresh.timer   ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now model-router-refresh.timer
```

### Ручной запуск (проверка):

```bash
python3 ~/.hermes/model-router/refresh.py
# должен: выбрать модель, перезаписать config.yaml, перезапустить gateway,
#         отправить Telegram-сообщение «🌅 Модель дня ...»
```

### Формула и веса (`model-strength.json`):

```json
{
  "cost_weight": 3.0,       // штраф за дорогой output (за 1M токенов)
  "ctx_bonus": 4.0,         // бонус за context ≥ 1M
  "ctx_big": 1000000,       // порог контекста для бонуса
  "default_strength": 60,   // для неизвестных моделей
  "strength": {
    "glm-5.2": 92, "deepseek-v4-pro": 90, "kimi-k2.7-code": 88, ...
  }
}
```

Полная документация логики: [`MODEL-ROUTER.md`](./MODEL-ROUTER.md).

## 7. systemd — Gateway (Telegram-бот 24/7)

Gateway — это процесс Hermes, который держит long-polling к Telegram API
и обрабатывает входящие сообщения.

```bash
# Юнит уже в репо (ops/systemd/hermes-gateway.service) — скопировать в user-systemd:
cp /srv/$USER/ai-agents-config/hermes_agent/ops/systemd/hermes-gateway.service ~/.config/systemd/user/

systemctl --user daemon-reload
systemctl --user enable --now hermes-gateway.service

# Проверка:
systemctl --user status hermes-gateway.service
# должно быть: active (running), telegram: connected
```

⚠️ Если после старта в логах (`~/.hermes/logs/gateway.log`) видно
`Failed to process config.yaml — falling back to .env / gateway.json values` —
значит `config.yaml` не парсится (битый YAML). Проверить:
`python3 -c "import yaml; yaml.safe_load(open('~/.hermes/config.yaml'))"`
— укажет строку ошибки. Частая причина — дубликат/осиротевший блок
`fallback_providers:` (см. §6, баг был в старой версии `router_lib.py`,
исправлено — см. ниже).

## 8. Cron — conductor-monitor (каждые 5 минут)

`conductor-monitor.sh` читает SQLite-состояние конду́ктора (`ho_*` таблицы)
и пушит в Telegram новые вопросы/эскалации/завершённые джобы. Dedup через state-файл.

```bash
# Установить crontab:
crontab -l 2>/dev/null | { cat; echo "# Hermes conductor monitor — push escalations to Telegram"; echo "*/5 * * * * /srv/$USER/ai-agents-config/hermes_agent/ops/conductor-monitor.sh >> ~/.hermes/conductor-monitor.log 2>&1"; } | crontab -

# Инициализация (отметить текущее состояние как уже-виденное — без спама):
/srv/$USER/ai-agents-config/hermes_agent/ops/conductor-monitor.sh --init
```

## 9. Vault Sync — авто-коммит AI Second Brain (каждые 30 мин)

```bash
# Скопировать vault-sync.sh в рантайм:
cp /srv/$USER/ai-agents-config/hermes_agent/ops/vault-sync.sh ~/.hermes/vault-sync.sh
chmod +x ~/.hermes/vault-sync.sh

# systemd timer:
cp /srv/$USER/ai-agents-config/hermes_agent/ops/systemd/vault-sync.service ~/.config/systemd/user/
cp /srv/$USER/ai-agents-config/hermes_agent/ops/systemd/vault-sync.timer   ~/.config/systemd/user/
# ⚠️ Поправить WIKI_PATH в vault-sync.service если путь другой:
# sed -i "s|/srv/vadim_prod|/srv/$USER|" ~/.config/systemd/user/vault-sync.service
# ⚠️ Поправить REPO в vault-sync.sh:
# sed -i "s|/srv/vadim_prod|/srv/$USER|" ~/.hermes/vault-sync.sh
systemctl --user daemon-reload
systemctl --user enable --now vault-sync.timer
```

## 10. Установить скилл vps-orchestration

Это операционная политика Hermes — как маршрутизировать задачи, когда
делегировать в Claude Code, как фейловерить на Gemini, как управлять
конду́ктором. Без него Hermes — просто чат-бот; с ним — оркестратор.

```bash
mkdir -p ~/.hermes/skills/autonomous-ai-agents
cp -r /srv/$USER/ai-agents-config/hermes_agent/skills/vps-orchestration \
      ~/.hermes/skills/autonomous-ai-agents/
# Перезапустить gateway, чтобы скилл подхватился:
systemctl --user restart hermes-gateway.service
```

## 11. (Опционально) Claude Code — profiles и conductor

Полный setup включает Claude Code с 4 системами (dev/seo/marketing/security)
и автономный конду́ктор. Это отдельный слой — см. корневой [`README.md`](../README.md)
раздел «Get started». Для базового Telegram-бота Hermes это не обязательно.

## 12. Auto-update Hermes (каждое утро 06:00 UTC)

Каждое утро автоматически подтягивает свежий upstream (`hermes update -y --backup`
= git pull + reinstall), перезапускает gateway и пишет в Telegram, если версия сменилась.
Ставится через systemd --user timer (тот же паттерн, что model-router).

```bash
# Скрипт + юниты из репо в рантайм:
cp hermes_agent/ops/hermes-update.py              ~/.hermes/hermes-update.py
cp hermes_agent/ops/systemd/hermes-update.service ~/.config/systemd/user/
cp hermes_agent/ops/systemd/hermes-update.timer   ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now hermes-update.timer
# Проверка / ручной прогон:
systemctl --user list-timers hermes-update.timer
python3 ~/.hermes/hermes-update.py          # разово (перезапустит gateway)
```

- Использует `router_lib.telegram()` + `restart_gateway()` (из `~/.hermes/model-router/`).
- **После апдейта восстанавливает канонический `SOUL.md` из репо** — `hermes update` умеет
  сбрасывать персону на дефолт NousResearch (→ Hermes начинает кодить сам); скрипт возвращает
  оркестраторскую персону, чтобы утром бот не «поглупел».
- **После апдейта пере-применяет file-tool guard** (`ops/apply-file-tool-guard.py`) — патч
  `tools/file_tools.py`, блокирующий запись кода проектов через file-инструмент Hermes
  (см. §5.1). `hermes update` перетирает vendored-код, поэтому guard ставится заново; если
  upstream сменил анкер функции — алерт в Telegram (барьер временно снят). Первичная установка:
  `python3 hermes_agent/ops/apply-file-tool-guard.py`.
- Уведомляет **только** при реальной смене версии или при сбое (без ежедневного шума).
- `--backup` даёт откат (`updates.backup_keep=5`); `-y` — авто-yes для миграции конфига/stash.
- Время: `OnCalendar=*-*-* 06:00:00` (сервер = UTC; за час до model-router 07:00).
  Поменять — правь `OnCalendar` в `hermes-update.timer` + `daemon-reload`.
- Лог: `~/.hermes/logs/hermes-update.log`.

---

## Проверка — чеклист после установки

```bash
# 1. Gateway запущен и Telegram подключён:
systemctl --user status hermes-gateway.service
cat ~/.hermes/gateway_state.json | jq .platforms.telegram.state
# → "connected"

# 2. Напиши боту в Telegram: "привет" — должен ответить как Hermes.

# 3. Модель дня (ручной запуск):
python3 ~/.hermes/model-router/refresh.py
# → Telegram-сообщение «🌅 Модель дня DD.MM Day ...»

# 4. Config перезаписан:
grep "default:" ~/.hermes/config.yaml    # → выбранная Go-модель
grep "model:" ~/.hermes/config.yaml      # → выбранная free-fallback

# 5. pick.json создан:
cat ~/.hermes/model-router/pick.json | jq .
# → {go, free, go_score, go_runners, free_available}

# 6. Timers активны:
systemctl --user list-timers --all | grep -E "model-router|vault"

# 7. Cron на месте:
crontab -l | grep conductor-monitor

# 8. Скилл загружен:
ls ~/.hermes/skills/autonomous-ai-agents/vps-orchestration/SKILL.md
```

## Каталог файлов рантайма (~/.hermes/)

| Путь | Что | Источник в репо |
|---|---|---|
| `config.yaml` | главный конфиг Hermes | `hermes_agent/CONFIG.md` (reference) |
| `.env` | секреты (API keys, tokens) | раздел 4 этого гайда |
| `SOUL.md` | персона бота | раздел 5 |
| `hermes-agent/` | upstream код Hermes (git clone) | шаг 2 |
| `model-router/refresh.py` | ежедневный выбор модели | `hermes_agent/ops/model-router/refresh.py` |
| `model-router/router_lib.py` | общие хелперы (API, Telegram, config edit) | `hermes_agent/ops/model-router/router_lib.py` |
| `model-router/model-strength.json` | веса формулы + сила моделей | `hermes_agent/ops/model-router/model-strength.json` |
| `model-router/pick.json` | результат последнего выбора (генерируется) | — |
| `model-router/cache/modelsdev.json` | кэш каталога models.dev (генерируется) | — |
| `vault-sync.sh` | авто-коммит вики | `hermes_agent/ops/vault-sync.sh` |
| `skills/autonomous-ai-agents/vps-orchestration/` | операционная политика | `hermes_agent/skills/vps-orchestration/` |
| `gateway_state.json` | состояние gateway (генерируется) | — |
| `conductor-monitor.log` | лог monitor-скрипта (cron) | — |
| `.conductor-monitor-state` | dedup-файл monitor-скрипта | — |
| `ho.db` | SQLite конду́ктора (опционально) | `claude_code/DEV/full_stack_sm/conductor/sql/schema.sql` |
| `state.db` | SQLite сессий Hermes (генерируется) | — |

## Обновление

```bash
# Обновить репозиторий:
cd /srv/$USER/ai-agents-config && git pull

# Синхронизировать ops-скрипты в рантайм:
cp hermes_agent/ops/model-router/refresh.py      ~/.hermes/model-router/
cp hermes_agent/ops/model-router/router_lib.py   ~/.hermes/model-router/
cp hermes_agent/ops/model-router/model-strength.json ~/.hermes/model-router/
cp hermes_agent/ops/vault-sync.sh                 ~/.hermes/vault-sync.sh
cp hermes_agent/ops/hermes-update.py              ~/.hermes/hermes-update.py
cp -r hermes_agent/skills/vps-orchestration       ~/.hermes/skills/autonomous-ai-agents/

# Обновить Hermes Agent (upstream):
cd ~/.hermes/hermes-agent && git pull && source venv/bin/activate && pip install -e .

# Перезапустить сервисы:
systemctl --user restart hermes-gateway.service
systemctl --user daemon-reload
```
