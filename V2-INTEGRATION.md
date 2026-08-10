# Интеграция ветки `v2` в `main` — 2026-08-10

`v2` — orphan-ветка (общих коммитов с `main` нет), в которой лежит кит Сергея:
его система + копия marketing_vb, разложенные под `agents-ai/telegram-bot-agent/`
и под его пути (`/srv/sergiy_prod/…`, профили `dev-sm`/`seo-sm`/…).

Сюда перенесено то, чего в `main` **не было**, с адаптацией под уже работающую
установку. Раскладка `main` (`hermes_agent/`, `claude_code/`) не менялась —
профили, юниты и дирижёр продолжают жить по прежним путям.

## Что приехало

**Телеграм-бот (главное).** `hermes_agent/ops/claude-switcher/` — нижняя панель
из двух ролей, у каждой свои вложенные кнопки:

```
🧑‍💼 Менеджер (Hermes)          → 👥 Совет моделей · 1️⃣ Одна модель · 🎓 Learn · 🗺 Journey
⚙️ Исполнитель (Claude, OpenCode) → 🛠 Dev · 🔍 SEO · 📣 Marketing · 🛡 Security
```

Плюс вкладки-топики (`/tabs`, `/cwd`, `/name`), режим прямого чата с Claude Code
(`/claude`), заём сильной модели дня на одну задачу (`/heavy`, `/normal`) и
форвард-пикер «в какую вкладку положить пересланное сообщение».

**Остальное:** `ops/vision-switch/` (модель-«глаза» как заём на ход),
`ops/agent-hooks/` (4 хука-барьера), `ops/conductor-bridge/`, `ops/hermes-update.py`,
`ops/task-scope.py`, `ops/searxng/`, `ops/telegram-userbot/`, `ops/mtproto/`,
`ops/bench/`, `ops/scripts/`; model-router v2 (`refresh.py` 85 → 767 строк,
`router_lib.py` 130 → 446, `free_providers.py`); документация
`SETUP.md` / `CONFIG.md` / `MODEL-ROUTER.md` / `SOUL.md` и шаблоны
`config.yaml.example`, `.env.example`, `mem0.json.example`, `qdrant.env.example`;
скиллы `claude-code-hermes`, `telegram-userbot-vps`, `vps-maintenance` и
расширенный `vps-orchestration` (373 → 552 строки).

`claude_code/DEV`: профиль `sandbox_sm`, `conductor/RUNBOOK.md`, `.mcp.json` для
hermes-core, три новых SEO-писателя в `mvb-seo`, `settings.json.example`.
`switch-profile.sh` научился `runFrom` → пишет `~/.claude/.active-profile-cwd`,
откуда свитчер берёт рабочую папку вкладки; `marketing_vb` и `marketing_vb_sm`
теперь объявляют `runFrom: ../../marketing_vb`.

## Что НЕ взято из v2 — и почему

| Файл | Причина |
|---|---|
| `ops/vault-sync.sh` | в v2 путь захардкожен (`/srv/sergiy_prod/…`); версия в `main` портируемая — она лучше |
| `ops/conductor-run.sh` | то же: в v2 пути под его раскладку. Взят только смысл; `CONDUCTOR_WORKERS=3` **не** добавлен — здешний дирижёр этой переменной не знает (нужен апгрейд его исходников) |
| Переименование профилей `dev-sm`/`seo-sm`/… | сломало бы юнит дирижёра, который стартует из `full_stack_sm/conductor` |
| `install.sh` / `bootstrap-vps.sh` из v2 | ставят второе дерево в `/srv/vadim_prod/ai-agents-config` и переписывают systemd-юниты на него. Здесь система живёт в репозитории — установщик не запускался |
| Исходники дирижёра из v2 | в `main` свои правки (лестница бэкоффа, hash-signature, approve=continue). Слияние движка — отдельная задача |
| `ho:*`-ветка свитчера | в шлюзе уже есть свой релей `ho:*` на вебхук дирижёра (`:3001`); две ветки перехватывали бы одни и те же нажатия |

## Адаптации, без которых бы не заработало

1. **Версия upstream.** Кит v2 писан под hermes-agent ~0.19, здесь стоит
   **0.16.0**. Разошлись: адаптер Telegram (`plugins/platforms/telegram/adapter.py`
   → `gateway/platforms/telegram.py`), `_prepare_profile_scoped_inbound_message_text`
   → `_prepare_inbound_message_text` (без `session_key`), `_adapter_for_source`
   → словарь `runner.adapters`. В `claude_switcher.py` добавлен слой
   совместимости (`_adapter_for`, `_prepare_inbound`), который **предпочитает
   новое имя** — файл переживёт апгрейд до 0.19 без правок. Установщик патча
   держит по два якоря на каждый шов и пропускает косметические, которых в 0.16 нет.

2. **Имена профилей.** Свитчер слал в дирижёра `dev-sm`/`seo-sm`/…, а
   `ho_jobs.profile` имеет `check (profile in ('dev','seo','marketing','security',
   'marketing_vb','marketing_vb_sm'))` — база отвергла бы такую вставку, и кнопки
   «Исполнителя» падали бы с ошибкой SQL. Перемаплено на имена манифестов
   `claude_code/DEV/profiles/<name>.json`.

3. **`HO_DB`.** По умолчанию свитчер пишет в `~/.hermes/ho.db`, которого здесь нет:
   дирижёр стартует с `DATABASE_URL=file:./ho.db` из своей `WorkingDirectory`.
   Указан явно на `claude_code/DEV/full_stack_sm/conductor/ho.db` — иначе задачи
   уходили бы в пустую базу, которую никто не читает.

## Как переустановить после `hermes update`

Апгрейд upstream затирает vendored-код. Патч идемпотентен:

```bash
python3 ~/3dlook-marketing/hermes_agent/ops/claude-switcher/apply-claude-switcher-patch.py
systemctl --user restart hermes-gateway
```

Код возврата `2` = якорь уехал, свитчер **не** установлен. Бэкапы файлов до патча:
`~/.hermes/backups/switcher-20260810/`. Окружение —
`~/.config/systemd/user/hermes-gateway.service.d/10-claude-switcher.conf`.

## Порты

Новых не заводилось: Qdrant остался на `6333/6334` (его слушает
`hermes-qdrant.service`, и `mem0.json` указывает туда же), вебхук дирижёра — `3001`.
SearXNG приехал файлами, но не поднимался — при запуске ему нужен свободный порт.
