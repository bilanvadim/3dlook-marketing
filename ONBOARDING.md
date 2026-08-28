# Онбординг-промпт для Claude Code (Вадим)

> Скопируй весь блок ниже (между линиями) и вставь в Claude Code, запущенный в
> корне свежесклонированного репозитория `3dlook-marketing`. Агент сам смёржит
> `sergiy_config → main`, настроит обе системы (Claude Code + Hermes), привяжет
> дирижёра к твоему Telegram-боту, активирует профиль `marketing_vb_sm` и
> проверит всё end-to-end.
>
> Секреты (Telegram chat id и т.п.) агент будет спрашивать у тебя, не угадывать.

---

Ты — Claude Code, работаешь в репозитории `https://github.com/bilanvadim/3dlook-marketing.git` (это репозиторий Вадима, у тебя полные права владельца через `gh`). Твоя задача — привести репозиторий в рабочее состояние: смёржить подготовленную ветку, настроить обе системы и запустить автономного дирижёра, привязанного к Telegram. Работай по шагам, **после каждого шага проверяй результат**, а секреты (токены, chat id) спрашивай у Вадима — не выдумывай.

## Контекст (что уже сделано за тебя)
- Ветка `sergiy_config` (PR #1 → `main`) содержит двухслойную систему поверх оригинала Вадима:
  - **Claude Code** — 6 переключаемых профилей (`dev`, `seo`, `marketing`, `security`, `marketing_vb`, `marketing_vb_sm`), см. `claude_code/DEV/SYSTEMS.md`.
  - **Hermes** — автономный оркестратор: дирижёр-воркер (Claude Agent SDK) тянет задания из очереди SQLite (`ho_*`, better-sqlite3) и эскалирует в Telegram.
- **Оригинальная система Вадима не тронута** — она целиком лежит в папке `marketing_vb/` (агенты, команды, `brand-assets/`, `workspace/`, `about-me.md`, `audience.md`, `DESIGN.md`, `CLAUDE.md`, `telegram-bot/`). Ничего в ней не меняй.
- PR #1 проверен: `main` после мёржа станет байт-в-байт равен `sergiy_config` (fast-forward), контент Вадима только добавляется.

## Шаг 0 — Сориентируйся
Прочитай в таком порядке: `README.md`, `INSTALL.md`, `claude_code/DEV/SYSTEMS.md`, `claude_code/DEV/marketing_vb/README.md`. Убедись, что `gh auth status` показывает аккаунт с правом записи в `bilanvadim/3dlook-marketing`.

## Шаг 1 — Смёржить PR #1 (`sergiy_config → main`)
```bash
gh pr view 1 --repo bilanvadim/3dlook-marketing --json mergeable,mergeStateStatus
# должно быть MERGEABLE / CLEAN; затем:
gh pr merge 1 --repo bilanvadim/3dlook-marketing --merge
```
Если предпочитаешь UI — нажми **Merge pull request** на странице PR #1. После мёржа переключись на `main` и подтяни:
```bash
git checkout main && git pull origin main
```
Проверка: в корне появились `claude_code/`, `hermes_agent/`, `marketing_vb/`, `install.sh`, `INSTALL.md`; папка `marketing_vb/brand-assets/` на месте.

## Шаг 2 — Проверь пререквизиты
`claude` CLI (залогинен в подписку **или** `ANTHROPIC_API_KEY`), `node` 20+, `npm`, `python3`, `sqlite3`. Чего нет — сообщи Вадиму, как поставить.

## Шаг 3 — Запусти установщик
```bash
bootstrap/install.sh --user vadim_prod --home /home/vadim_prod
```
`bootstrap/install.sh` **никогда не запускает sudo** — он готовит файлы (создаёт `conductor/.env` из примера, применяет SQLite-схему в `ho.db` (better-sqlite3; libSQL снят), рендерит systemd-юниты в `hermes_agent/ops/systemd/generated/`) и **печатает** привилегированные команды. Запиши, что он напечатал, — понадобится на шаге 6.

## Шаг 4 — Настрой `conductor/.env` (привязка к Telegram)
Файл: `claude_code/DEV/full_stack_sm/conductor/.env`. Выстави:
- `DATABASE_URL=file:./ho.db` — локальный файл, ноль инфраструктуры (оставь как есть; для сетевой БД — `libsql://…`/Turso).
- `ANTHROPIC_API_KEY=` — **оставь пустым**, чтобы использовать залогиненную подписку Claude (или впиши ключ, если биллинг по API).
- `TELEGRAM_BOT_TOKEN=` — **тот же токен, что у существующего бота Вадима** (`marketing_vb/telegram-bot/` использует `TELEGRAM_BOT_TOKEN`). Спроси у Вадима значение или возьми из его текущего окружения бота.
- `TELEGRAM_CHAT_ID=` — chat id Вадима, куда слать эскалации (спроси у Вадима; это его `CHAT_ID` из бота).

Никогда не коммить `.env` и `node_modules` (они в `.gitignore`).

## Шаг 5 — Прогони тесты дирижёра
```bash
cd claude_code/DEV/full_stack_sm/conductor
npm ci && npm test          # 168 тестов: breaker/store/profiles/askgate, без сети/API
cd -
```

## Шаг 6 — Установи и запусти сервис дирижёра
Выполни те `sudo`-команды, что напечатал `install.sh` (примерно):
```bash
sudo cp hermes_agent/ops/systemd/generated/hermes-conductor.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now hermes-conductor
systemctl status hermes-conductor --no-pager
```
Проверка: статус `active (running)`, в `journalctl -u hermes-conductor -n 30` виден воркер `ho-<pid>`, поллит очередь, ошибок нет, `DATABASE_URL → file:/home/vadim/.hermes/ho.db`.

## Шаг 7 — Push-нотификатор в Telegram (cron)
```bash
( crontab -l 2>/dev/null; \
  echo "*/5 * * * * $PWD/hermes_agent/ops/conductor-monitor.sh >> \$HOME/.hermes/conductor-monitor.log 2>&1" ) | crontab -
hermes_agent/ops/conductor-monitor.sh --init   # пометить текущее состояние как «просмотрено», без спама
```
Монитор читает `$HOME/.hermes/.env` (`TELEGRAM_BOT_TOKEN` / `TELEGRAM_ALLOWED_USERS`) — положи туда те же значения, что в `conductor/.env`.

## Шаг 8 — Активируй профиль `marketing_vb_sm`
```bash
claude_code/DEV/switch-profile.sh marketing_vb_sm
claude_code/DEV/switch-profile.sh --current      # подтверждение
```
**Перезапусти Claude Code** — плагины грузятся при старте сессии. После рестарта будет доступна команда `/vbsm-campaign` и скилл `marketing-vb-sm`.

## Шаг 9 — ⚠️ Правило рабочей директории (критично)
Для **маркетинговой** работы (`marketing_vb` / `marketing_vb_sm`) запускай Claude Code **из папки `marketing_vb/`**:
```bash
cd marketing_vb && claude
```
Агенты читают бренд-контекст относительными путями (`about-me.md`, `audience.md`, `DESIGN.md`, `brand-assets/`, `workspace/`) — они лежат в `marketing_vb/`. Запуск из корня репозитория → агенты не найдут эти файлы. Профиль (плагины) грузится глобально, но контент виден только из правильной папки.

## Шаг 10 — Проверка end-to-end
Поставь смоук-задачу в очередь и проследи `queued → running → done`:
```bash
DB=claude_code/DEV/full_stack_sm/conductor/ho.db
sqlite3 "$DB" "insert into ho_jobs(kind,title,prompt,profile,work_dir) \
  values('feature','smoke','напиши hello в файл hi.txt','marketing_vb_sm','$PWD/marketing_vb');"
sleep 20
sqlite3 "$DB" "select id,status,profile,result_summary from ho_jobs order by created_at desc limit 3;"
```
Убедись, что задача прошла и (если эскалировала) в Telegram пришло уведомление с кнопками Approve/Deny/Abort.

## Шаг 11 — Отчёт Вадиму
Кратко доложи: что смёржено, статус сервиса дирижёра, привязка к Telegram работает, активный профиль `marketing_vb_sm`. Затем объясни, как начать реальную работу:
- **Интерактивно (руки):** `cd marketing_vb && claude`, профиль `marketing_vb_sm`, команда `/vbsm-campaign` — стратегия Sergiy → брендо-заземлённое исполнение командами Vadim → двойной QC → измерение. Оригинальные команды Вадима (`/new-article`, `/weekly-posts`, `/outbound`, `/qc`, `/quarterly-review`) — тоже работают.
- **Автономно (оркестратор):** ставь задания в `ho_jobs` (поле `profile` выбирает систему) — дирижёр гоняет их сам и пишет в Telegram, когда нужно твоё решение.

## Ограничения
- Не модифицируй ничего в `marketing_vb/` (оригинал Вадима — источник правды).
- Секреты спрашивай у Вадима, не подставляй заглушки.
- Не коммить `.env`, `node_modules`, содержимое `hermes_agent/ops/systemd/generated/`.
- Проверяй каждый шаг фактами (статус сервиса, вывод SQL, наличие команды), а не «на словах».

---

**После настройки** самый частый вход в работу: `cd marketing_vb && claude` → профиль `marketing_vb_sm` → `/vbsm-campaign`.
