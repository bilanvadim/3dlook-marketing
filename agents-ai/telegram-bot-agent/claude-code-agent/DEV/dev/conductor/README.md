# Hermes Orchestrator — Conductor

Автономный дирижёр над Claude Code. Берёт задачи из очереди, прогоняет их через Claude Agent SDK (тот же движок, что и Claude Code), держит безопасность и **durable resume** через circuit breaker, эскалирует человеку в Telegram только когда нужно. **Деньги/бюджет НЕ контролирует** — приоритет качество, единственная защита от runaway — детект зацикливания. Наследует весь marketplace (агенты, CLAUDE.md, settings.json, guard.py) через `settingSources: ['project']`.

Состояние — **SQLite/libSQL** (`@libsql/client`): по умолчанию локальный файл (ноль инфраструктуры), тем же кодом — сетевой libSQL-сервер или Turso Cloud по смене `DATABASE_URL`. Полное описание архитектуры и решений — в `ARCHITECTURE.md`.

## Как это соотносится с marketplace
- **hermes-marketplace** (слои A+B) = агенты + правила для Claude Code. «Оркестр и партитура».
- **hermes-conductor** (слой C, это репо) = сервис, который запускает Claude Code автономно. «Дирижёр».

Дирижёр живёт в `conductor/`, но `.claude/` от marketplace лежит в корне репозитория (на уровень выше). Поэтому **`work_dir` каждой job должен указывать на корень репо** (или на целевой проект, в котором есть свой `.claude/`).

## Быстрый старт
```bash
# 1. Конфиг (по умолчанию state = локальный файл file:./ho.db)
cp .env.example .env && $EDITOR .env

# 2. State — создать/обновить схему (идемпотентно)
npm install
sqlite3 ho.db < sql/schema.sql          # для file: ; conductor-run.sh делает это сам при старте
#   Turso/сетевой libSQL: turso db shell <db> < sql/schema.sql

# 3. Проверка ядра (безопасно, без API/сети)
npm test                                 # breaker + steploop + steprunner + store (libSQL smoke)

# 4. Запуск воркера
npm start
```
Поставить задачу: `insert into ho_jobs(kind,title,prompt,profile,work_dir) values(...)` (через `sqlite3 ho.db`, `turso db shell`, или n8n).

## Поток
1. Триггер (cron/webhook/ручной insert) кладёт job в `ho_jobs`.
2. Воркер атомарно забирает job (`store.claimJob` — write-транзакция SQLite; single-writer, гонок нет by construction).
3. `query()` запускает агентский цикл с наследованием `.claude/`; permissionMode по умолчанию `acceptEdits`.
4. На каждое событие SDK — сохраняем `session_id` на job (для resume), прогон через circuit breaker.
5. ASK-действие (merge / destructive SQL / db push / terraform) → пауза + Telegram (approve/deny/abort) → `waitEscalation` ждёт решения. `git push` НЕ гейтится — это штатный авто-поток.
6. Token/rate-лимит или падение → job `deferred`/recovered с `resume_session_id`; следующий claim продолжает сессию (durable resume).
7. Терминал: done / failed / paused / deferred / escalated / aborted → уведомление в Telegram.

## Circuit breaker (сердце; `src/core/breaker.ts`)
Контролирует ТОЛЬКО то, что агент не решит сам: **зацикливание** (`stuck` при 6 одинаковых ходах подряд — основной контроль) + щедрые backstop'ы (300 ходов, 4 ч wall-clock) + пауза по rate/token-лимиту (→ durable resume) + ask-gate. **Бюджета/денег нет** — сознательно. Покрыт юнит-тестами (`npm test`).

## Безопасность
- `permissionMode: acceptEdits` — пишет код сам, но опасные shell-команды остаются под нашим `guard.py` из marketplace и превращаются в эскалации. **Никогда `bypassPermissions`** в автономе.
- `DATABASE_URL`: для `file:` — просто путь к файлу (держи вне образа/репо); для Turso/libSQL — URL с authToken, только server-side, через `--env-file`.
- Полного аудита событий нет (осознанно): храним только статус job/run, `session_id` и последнюю ошибку.
- Для авто commit+push+deploy нужна git-аутентификация (deploy-токен/SSH-ключ) и подключённая Vercel Git-интеграция.

## Step mode (фаза 2) — пошаговое исполнение
Если у job есть строки в `ho_steps`, conductor идёт пошаговым путём:
`store.nextStep` (следующий шаг с выполненными `depends_on`) → `runStep` (executor → независимые гейты → `code-reviewer` 0-100 → `runtime-verifier` когда нужно → решение `decideStep`: done/retry/needs_review/blocked) → прогресс/эскалация. Контракт с менеджером Hermes — в **`INTEGRATION.md`**; surface для Hermes: вью `ho_project_status` (статус+%), таблицы `ho_steps`, `ho_questions` (async-интервью). Claim/next-step/recover/answer-логика — в `store.ts` (транзакции SQLite вместо PL/pgSQL-функций). Логика (`steploop.ts`/`steprunner.ts`) покрыта тестами; SDK-вызовы изолированы в `agent-runner.ts`.

## Файлы
```
INTEGRATION.md             контракт Hermes ↔ Fullstack agents (статус-машина, surfaces)
ARCHITECTURE.md            архитектура и решения
sql/schema.sql             полная схема (SQLite/libSQL): jobs/runs/escalations/steps/questions + вью
src/core/breaker.ts        circuit breaker (чистая логика, тестируемая)
src/core/steploop.ts       решение per-step цикла (progress-delta/plateau/needs_review) — тестируемое
src/core/steprunner.ts     оркестрация одного шага (executor→gates→review→runtime→retry) — тестируемая
src/core/agent-runner.ts   SDK-адаптер для шагов (integration seam)
src/core/store.ts          доступ к SQLite/libSQL (jobs/runs/steps/questions/status; claim/next-step в транзакциях)
src/core/conductor.ts      главный цикл: whole-job ИЛИ step-mode (если есть ho_steps) + durable resume
src/escalation/*           Telegram уведомления + приём решения человека
test/{breaker,steploop,steprunner,store}.test.ts  юнит-тесты + libSQL store smoke
Dockerfile, .env.example
```

## Статус (честно)
- **Durable resume реализован, но не обкатан на живом SDK.** `session_id` пишется на job сразу; пауза по token/rate-лимиту → `deferred` с backoff → следующий claim продолжает через `resume:`. Упавший процесс ловит `store.recoverStale()`. Сквозной автономный прогон против реального SDK ещё не гонялся.
- **Деньги не считаем** (осознанно) — ни ledger, ни бюджет.
- **Single-writer.** SQLite/libSQL — один писатель; для одного дирижёра достаточно. Флот параллельных воркеров = повод вернуть Postgres.
- Дашборды/observability — нет (осознанно). Приоритизация задач примитивная (priority + FIFO).
