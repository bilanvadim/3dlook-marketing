# Hermes Agent — конфигурация (reference)

Полный разбор `~/.hermes/config.yaml` и `~/.hermes/.env` — все секции, ключи,
значения по умолчанию и что за что отвечает. Без секретов — только структура.

> Установленный конфиг живёт в `~/.hermes/config.yaml`. Редактируется вручную
> или через `hermes setup` (визард). `model.default` и `fallback_providers`
> перезаписываются автоматически model-router (см. [`MODEL-ROUTER.md`](./MODEL-ROUTER.md)).

---

## config.yaml

### `model:` — модель и провайдер

```yaml
model:
  default: deepseek-v4-pro    # ПЕРЕЗАПИСЫВАЕТСЯ model-router каждое утро
  provider: opencode-go       # провайдер: opencode-go (subscription) | opencode-zen (free) | openrouter | ...
  max_tokens: 16384           # лимит output-токенов на ответ
```

- `provider: opencode-go` — Go-подписка (сильные модели: deepseek-v4-pro, glm-5.2,
  kimi-k2.7-code и др.). Лимит сбрасывается каждые несколько часов.
- `provider: opencode-zen` — Zen (free модели). Без лимитов, но слабее.
- `OPENCODE_GO_API_KEY` / `OPENCODE_ZEN_API_KEY` — в `.env`.

### `fallback_providers:` — автоматический fallback

```yaml
fallback_providers:
  - provider: opencode-zen
    model: deepseek-v4-flash-free    # ПЕРЕЗАПИСЫВАЕТСЯ model-router
```

Hermes автоматически переключается на fallback, если primary-провайдер
возвращает 429/limit. Возвращается на primary при следующем запросе.

### `terminal:` — терминал-тул (выполнение команд)

```yaml
terminal:
  backend: local              # local | docker | ssh | modal | daytona
  cwd: /srv/vadim_prod       # рабочая директория для Telegram-сессий
  timeout: 180                # таймаут команды (сек)
  docker_mount_cwd_to_workspace: false
  lifetime_seconds: 300       # lifetime контейнера (docker backend)
  container_cpu: 1
  container_memory: 5120      # MB
  container_disk: 51200       # MB
  container_persistent: true
```

### `tool_loop_guardrails:` — защита от зацикливания

```yaml
tool_loop_guardrails:
  warnings_enabled: true
  hard_stop_enabled: false
  warn_after:
    exact_failure: 2          # N одинаковых ошибок → warning
    same_tool_failure: 3
    idempotent_no_progress: 2
  hard_stop_after:
    exact_failure: 5          # N → hard stop (если enabled)
    same_tool_failure: 8
    idempotent_no_progress: 5
```

### `compression:` — сжатие контекста

```yaml
compression:
  enabled: true
  threshold: 0.5              # начать сжатие при 50% контекстного окна
  target_ratio: 0.2           | сжать до 20%
  protect_last_n: 20          # не трогать последние 20 сообщений
  protect_first_n: 3          # не трогать первые 3 (system prompt)
```

### `prompt_caching:`

```yaml
prompt_caching:
  cache_ttl: 5m               # TTL кэша промпта (анти-cost)
```

### `memory:` — долгосрочная память

```yaml
memory:
  memory_enabled: true        # агент ведёт память диалога
  user_profile_enabled: true  # профиль пользователя
  provider: mem0              # Mem0 OSS + Gemini + локальный Qdrant
  memory_char_limit: 2200     # лимит памяти (символы)
  user_char_limit: 1375
  nudge_interval: 10          # каждые 10 ходов — nudge обновить память
  flush_min_turns: 6          # минимум 6 ходов перед flush
```

Для конфигурации Mem0 OSS скопируйте [`mem0.json.example`](./mem0.json.example)
в `~/.hermes/mem0.json`. Секрет Gemini хранится только в `~/.hermes/.env` как
`OPENAI_API_KEY` — это имя переменной, которое использует OpenAI-адаптер Mem0;
запросы направляются на Gemini endpoint, а не в OpenAI.

### `session_reset:` — авто-ресет сессии

```yaml
session_reset:
  mode: both                  # both | idle | scheduled
  idle_minutes: 1440          # 24ч простоя → reset
  at_hour: 4                  # + ежедневный reset в 4:00
```

### `agent:` — параметры агента

```yaml
agent:
  max_turns: 60               # max итераций tool-calling на один ответ
  verbose: false
  reasoning_effort: medium    # low | medium | high (для моделей с reasoning)
```

### `platform_toolsets:` — какие тулсеты на какой платформе

```yaml
platform_toolsets:
  cli: [hermes-cli]
  telegram: [hermes-telegram]
  discord: [hermes-discord]
  # ... slack, signal, whatsapp, homeassistant, qqbot, yuanbao, teams, google_chat
```

### `stt:` / `tts:` — голос

```yaml
stt:
  enabled: true
  local:
    model: base               # whisper local
  openai:
    model: whisper-1          # whisper API (если OPENAI_API_KEY)
tts:
  provider: edge              # edge (free) | openai | ...
```

### `display:` — отображение

```yaml
display:
  compact: false
  busy_input_mode: queue      # interrupt | queue | steer  (см. ниже)
  tool_progress: all          # all | new | off | verbose
  streaming: true
  skin: default               # default | ares | mono | slate | custom
  long_running_notifications: true
  busy_ack_detail: true
  show_reasoning: false
  bell_on_complete: false
```

**`busy_input_mode`** — что делать с сообщением, присланным пока агент ещё занят
предыдущим (единственный источник истины; env-override `HERMES_GATEWAY_BUSY_INPUT_MODE`):

| Режим | Поведение |
|---|---|
| `interrupt` (upstream-дефолт) | новое сообщение **прерывает** текущий прогон и запускает себя |
| **`queue`** (наш выбор) | каждое сообщение встаёт в **FIFO-очередь** отдельным turn'ом, авто-переход к следующему по завершении — **как input-queue в Claude Code / Cursor**. Cap 32 в очереди. |
| `steer` | новое сообщение вклинивается в текущий прогон между вызовами инструментов |

При `queue`: бот отвечает «Queued for the next turn. (N queued)»; глубину видно в `/status`;
`/queue <task>` кладёт явно (работает в любом режиме), `/steer <prompt>` — вклинить в текущий,
`/stop` — прервать, `/new`/`/reset` — очистить очередь. Требуется рестарт gateway после смены
(режим читается при старте). Живой config.yaml gitignored — правь и его, и этот пример.

### `auxiliary:` — вспомогательные модели (зрение, судья одобрений)

```yaml
auxiliary:
  free_only: true               # фолбэк на OpenRouter — только :free SKU
  vision:
    provider: opencode-go
    model: qwen3.7-plus         # ← ДОЛЖНА уметь картинки
  approval:
    provider: opencode-go
    model: deepseek-v4-flash-free   # быстрая, НЕ reasoning
```

- **`free_only`** — ⚠️ по умолчанию `false`. Цепочка авто-фолбэка вспомогательных задач
  вторым шагом идёт в **OpenRouter**, а ключ у нас есть — то есть при сбое основного
  провайдера side-задача молча уходила бы на **платную** модель. `true` ограничивает
  этот фолбэк `:free`-SKU. Для сознательно бесплатного стека — обязательно.
- **`approval`** — судья smart-одобрений (см. `approvals.mode`). Вызывается **инлайн**
  перед каждой флагнутой командой, поэтому латентность видна напрямую → быстрая
  НЕ-reasoning модель. У вызова `max_tokens=16`: reasoning-модель потратит их на
  размышление, вернёт пустоту, и всё выродится в ESCALATE.
  Бенч 2026-08-05 (12 команд, настоящий `_smart_approve`, настоящая политика):
  `deepseek-v4-flash-free` 12/12 при 3.5 с/вызов ← выбран; `mimo-v2.5-free` 12/12, но
  8.5 с/вызов (наша основная — слишком медленная для инлайна); `qwen3.6-plus-free`
  8/12 при 0.2 с — вырожденная, escalate на всё. Опасных APPROVE не было ни у одной.
- **`vision`** — модель для анализа изображений (скриншоты в Telegram, `vision_analyze`).
  С 08.08.2026 у неё **вторая, более важная роль**: это ещё и модель, на которую
  Hermes переключается целиком на тот ход, где пришла картинка, — см.
  `ops/vision-switch/`. Рабочая модель с тех пор выбирается по силе и вполне
  может быть text-only.
- ⚠️ **Только vision-capable модель.** `deepseek-v4-*` — текстовые: при отправке картинки
  провайдер отбивает `400 Upstream request failed`, и Hermes «видит» пустоту (симптом:
  «сейчас посмотрю на скриншот» → ничего). Проверено на `opencode-go` (эмпирически, отправкой
  реального изображения): **работают** `qwen3.7-plus` (лучший — точный ответ), `minimax-m3`
  (многословный), `glm-5.1`/`glm-5.2` (принимают, но часто пустой ответ); **НЕ работают**
  `deepseek-v4-pro/flash`, `qwen3.7-max`, `mimo-v2-omni`, `hy3-preview`.
- ⚠️ **model-router ТЕПЕРЬ перезаписывает** `auxiliary.vision` каждое утро (было:
  «задаётся статически»). Туда идёт сильнейшая бесплатная модель, доказавшая
  зрение red-square-пробой. Правки руками переживут ровно до 07:00 — если нужна
  своя модель насовсем, менять надо выбор в `refresh.py`, а не эту строку.
  Соседний `approval:` роутер не трогает.

### `delegation:` — субагенты

```yaml
delegation:
  max_iterations: 50
  # max_concurrent_children: 3   # параллельных субагентов
  # max_spawn_depth: 2           # глубина вложенности
```

### `code_execution:`

```yaml
code_execution:
  timeout: 300                # сек
  max_tool_calls: 50
```

### `approvals:` — одобрение действий агента

```yaml
approvals:
  mode: "smart"               # manual (деф.) | smart | off
  destructive_slash_confirm: false
  smart_policy: |             # правила оператора в системный промпт судьи
    ...
  # cron_mode: deny           # deny (деф.) | approve — политика для cron-действий
```

- **`mode`** — как одобряются действия (терминал, запись файлов, computer-use и т.п.):
  - `manual` (по умолчанию) — спрашивает **Always / Session / Once** на каждое действие;
  - **`smart`** (у нас с 2026-08-05) — флагнутую команду сначала оценивает
    вспомогательная модель: **APPROVE / DENY / ESCALATE**, и только ESCALATE доходит до
    тебя. В Telegram это **инлайн-кнопки** (`✅ Allow Once | ✅ Session | ✅ Always | ❌ Deny`),
    так что headless-gateway всё-таки умеет спросить — это и снимает старое возражение
    против `manual`. Проверено живьём: `rm -rf ~/hermes-approval-test` → APPROVE молча,
    `systemctl --user restart hermes-*` → кнопки в чате → Deny → команда не выполнена.
  - **`off`** — байпас всех промптов, максимальная автономия. Стояло у нас до 2026-08-05.
  - ⚠️ **Кавычки обязательны** (`mode: "off"`): без кавычек YAML парсит `off` как boolean `false`.
  - ⚠️ Режим читается через **mtime-кэш** → правка применяется **без рестарта gateway**
    (проверено: живой процесс подхватил `smart` и новый `auxiliary.approval` на лету).
    Обратная сторона той же медали: правка `config.yaml` = мгновенная смена политики,
    поэтому запись в него закрыта и `approvals.deny`, и shell-хуком.
- **`smart_policy`** — текст правил оператора, который дописывается в **системный**
  промпт судьи (доверенный канал; сама команда идёт в user-сообщении внутри
  `<command>`-делимитеров как недоверенный ввод, и судья предупреждён игнорировать
  инструкции внутри неё). Токены тратятся только на флагнутых командах, не каждый ход.
  Писать про **серую зону**: жёсткие случаи уже держат `deny`-глобы и shell-хуки.
- ⚠️ **`command_allowlist` держать пустым.** Записи там — не команды, а целые
  КАТЕГОРИИ опасных паттернов, разрешённые навсегда; пишет их кнопка **«Always»**.
  2026-08-05 в живом конфиге нашлись три: `script execution via heredoc`,
  `in-place edit of Hermes config/env`, `script execution via -e/-c flag` — ровно те
  три вектора, которыми агент однажды дописал себе исключение в SOUL.md. Вычищено;
  утренний `hermes-update.py` теперь алертит в Telegram, если там что-то появилось,
  и если `mode` перестал быть `smart`. В чате жать **Once/Session**, не «Always».
- **Защитный floor работает при ЛЮБОМ mode** (даже `off`): Hardline-блоклист
  (`rm -rf /`, перезапись блок-устройств, `shutdown`/`reboot`, DoS) и sensitive-write
  таргеты (`~/.hermes/config.yaml`, `~/.hermes/.env`, `~/.ssh`, shell-rc, `.netrc`/`.pgpass`,
  `/etc`) **никогда** не выполняются автоматически. Плюс пользовательский `approvals.deny`.
- **`cron_mode`** — отдельная поверхность для cron-триггеров: `deny` (по умолчанию —
  авто-отказ) или `approve`. Интерактив (Telegram) им НЕ управляется — только `mode`.
- **`deny`** — **МЕХАНИКА барьера «Hermes = менеджер, не кодер».** Список fnmatch-глобов
  (матч по всей строке команды, регистронезависимо, по деобфусцированным вариантам),
  которые блокируют команду **раньше** любого bypass — т.е. **даже под `mode: "off"`/yolo**
  (как code-shipped hardline, но пользовательский). У нас забиты глобы, запрещающие
  Hermes **искать/править код в зоне проектов `/srv/vadim_prod/*`** его собственным
  терминалом (`grep`/`rg`/`find`/`awk`/`sed`/редакторы/`> файл`), чтобы он делегировал в
  Claude Code / OpenCode, а не делал сам. **НЕ блокируются** (проверено): dispatch
  `claude`/`opencode` (даже если в промпте есть слово grep/sed), `git`, запись handoff,
  одиночный `cat`, и всё в `~/.hermes` (/home). ⚠️ Матч по команде — это сильный
  детеррент, но не песочница: (1) прямой tool записи файлов Hermes (`file`/write) НЕ
  проходит через approvals.deny — от правки кода этим путём защищает только персона;
  (2) хитрые переформулировки теоретически обходимы. Полный список — в `config.yaml.example`.

### `skills:`

```yaml
skills:
  creation_nudge_interval: 15 # каждые 15 ходов — nudge создать скилл
```

---

### `curator:` — гигиена библиотеки скиллов
Куратор архивирует скиллы, которыми не пользуются: `stale` после 30 дней, архив после 90.
Идёт сам раз в неделю. `consolidate: false` — на free-стеке оставлять выключенным:
тогда прогон чисто детерминированный и не тратит вспомогательную модель.
Статус: `hermes curator status`. Скиллы без provenance-маркера куратору не видны —
передать вручную: `hermes curator adopt <name>`.

### `security.website_blocklist:` — блок-лист веба
Проверка идёт ДО инструмента, покрывает `web_search`, `web_extract`, `browser_navigate`.
Смысл — закрыть metadata-эндпоинт облака и внутренние хосты.
⚠️ **Не добавлять `127.0.0.1` и `*.local`**: на localhost живут SearXNG (:8888) и
Qdrant (:6343), а правила работают по хостам — порт не вычтешь, и блок по localhost
убьёт агенту веб-поиск.

### `checkpoints:` — снапшоты перед деструктивными операциями
Барьер (`approvals.deny` + `pre_tool_call` хук) держит запись в `/srv`, но у него
известные дыры — относительные redirect'ы после `cd`. Чекпоинт снимается до операции,
откат — `/rollback`.

### `agent.verify_on_stop:` — судья кодинга
`"auto"` = включён на CLI/TUI, **выключен на мессенджерах**: в Telegram нарратив
верификации читается как шум. То есть для бота это no-op by design, работает при
ручных прогонах `hermes`. Настоящая верификация нашего контура живёт не здесь, а в
Claude Code (`hermes-verify` + `verification-protocol` + `runtime-verifier`).

### `moa:` — Mixture of Agents
Несколько моделей-советников + модель-агрегатор, которая отвечает.
**Объявление пресета не включает MoA**: он активируется только явным переключением
модели (`/model moa:council`); `hermes moa list` должен показывать
`Active in config: (off)`. На free-стеке это способ усилить маленькую основную модель,
не переходя на платные.
⚠️ Каталог free-моделей врёт — числятся закончившиеся промо. Перед правкой пресета
пинговать кандидатов: `router_lib.free_ok(key, model)` (ключ **первым** аргументом).
`reference_max_tokens: 600` режет болтливость советников: ход ждёт самого медленного,
а агрегатору нужна только суть.

## .env — секреты (API keys, tokens)

Файл `~/.hermes/.env`, права `600`. НЕ коммитится (в `.gitignore`).

### Обязательно для нашего setup:

| Переменная | Назначение | Где взять |
|---|---|---|
| `OPENCODE_GO_API_KEY` | Go-провайдер (primary, сильные модели) | opencode.ai → dashboard |
| `OPENCODE_ZEN_API_KEY` | Zen-провайдер (free fallback) | opencode.ai → dashboard |
| `TELEGRAM_BOT_TOKEN` | Telegram-бот | @BotFather → `/newbot` |
| `TELEGRAM_ALLOWED_USERS` | ID разрешённых пользователей (через запятую) | @userinfobot |
| `WIKI_PATH` | Путь к Obsidian-вики (AI Second Brain) | путь в репо |
| `OBSIDIAN_VAULT_PATH` | То же (alias) | путь в репо |

### Опционально:

| Переменная | Назначение |
|---|---|
| `GEMINI_API_KEY` | Gemini CLI failover (когда Claude в лимите) |
| `AGENT_BROWSER_EXECUTABLE_PATH` | Путь к Chrome/Chromium для browser-тулов |
| `BROWSERBASE_API_KEY` | Browserbase (облачный браузер) |
| `BROWSERBASE_PROXIES` | `true` — прокси для анти-детекта |
| `OPENROUTER_API_KEY` | OpenRouter (доступ к 100+ моделям) |
| `GITHUB_TOKEN` | `gh` CLI (коммиты, PR, релизы) |
| `VERCEL_TOKEN` | Vercel CLI (деплой) |
| `OPENAI_API_KEY` | OpenAI (whisper, GPT, если нужно) |
| `GOOGLE_API_KEY` | Google AI Studio (= GEMINI_API_KEY alias) |
| `EXA_API_KEY` | Exa search |
| `FIRECRAWL_API_KEY` | Firecrawl (web scraping) |

### Структура .env (пример без секретов):

```bash
# === LLM providers ===
OPENCODE_GO_API_KEY=sk-REPLACE_WITH_YOUR_KEY
OPENCODE_ZEN_API_KEY=sk-REPLACE_WITH_YOUR_KEY

# === Telegram ===
TELEGRAM_BOT_TOKEN=1234567890:REPLACE_WITH_BOTFATHER_TOKEN
TELEGRAM_ALLOWED_USERS=REPLACE_WITH_YOUR_NUMERIC_ID

# === AI Second Brain ===
WIKI_PATH=/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain
OBSIDIAN_VAULT_PATH=/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain

# === Browser ===
AGENT_BROWSER_EXECUTABLE_PATH=/usr/bin/chromium-browser
BROWSERBASE_PROXIES=true
BROWSERBASE_ADVANCED_STEALTH=false

# === Failover ===
GEMINI_API_KEY=REPLACE_WITH_GEMINI_KEY

# === CI/CD ===
GITHUB_TOKEN=ghp_REPLACE_WITH_GITHUB_TOKEN
VERCEL_TOKEN=REPLACE_WITH_VERCEL_TOKEN
```

> Полный список всех поддерживаемых переменных — в upstream `.env.example`:
> `~/.hermes/hermes-agent/.env.example` (300+ переменных, все закомментированы).

---

## SOUL.md — персона

`~/.hermes/SOUL.md` — текст, который добавляется в system prompt КАЖДОГО
сообщения. Загружается заново на каждый ход (без рестарта). Определяет
тон, личность, базовые правила.

Если файл пуст или отсутствует — используется `DEFAULT_AGENT_IDENTITY`
(встроенная персона Hermes из `agent/system_prompt.py`).

Пример для нашего setup:
```markdown
# Hermes Agent Persona

Ты — Hermes, личный AI-оркестратор Сергея на VPS.
Ты МЕНЕДЖЕР, не кодер: любой технический труд ты делегируешь в Claude Code.
Отвечаешь кратко, по-русски, конкретно.
Перед делегированием технической задачи — прочитай скилл `vps-orchestration`.
```

---

## channel_directory.json — реестр каналов

`~/.hermes/channel_directory.json` — авто-генерируется gateway. Хранит
подключённые чаты по платформам. Для Telegram — DM с пользователем:

```json
{
  "updated_at": "2026-07-09T13:01:38",
  "platforms": {
    "telegram": [
      {"id": "YOUR_TELEGRAM_USER_ID", "name": "Sergiy", "type": "dm", "thread_id": null}
    ]
  }
}
```

При первом сообщении боту — пользователь автоматически добавляется сюда.

---

## personalities (встроенные)

`config.yaml` → `agent.personalities` — предустановленные персоны (переключаются
через `/personality <name>` в Telegram). 12 штук: helpful, concise, technical,
creative, teacher, kawaii, catgirl, pirate, shakespeare, surfer, noir, uwu,
philosopher, hype. НЕТ функции «само-представления» — персона определяет ТОЛЬКО
тон ответов. Self-intro — это просто первый ответ бота на сообщение пользователя,
сформированный персоой + SOUL.md + загруженными скиллами.
