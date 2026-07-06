# Fullstack agents Conductor

Автономный дирижёр над Claude Code. Берёт задачи из очереди, прогоняет их через Claude Agent SDK (тот же движок, что и Claude Code), держит безопасность и **durable resume** через circuit breaker, эскалирует человеку в Telegram только когда нужно. **Деньги/бюджет НЕ контролирует** — приоритет качество, единственная защита от runaway — детект зацикливания. Наследует весь marketplace (агенты, CLAUDE.md, settings.json, guard.py) через `settingSources: ['project']`.

Полное описание архитектуры и решений — в `ARCHITECTURE.md`.

## Как это соотносится с marketplace
- **hermes-marketplace** (слои A+B) = агенты + правила для Claude Code. «Оркестр и партитура».
- **hermes-conductor** (слой C, это репо) = сервис, который запускает Claude Code автономно. «Дирижёр».

Дирижёр живёт в `conductor/`, но `.claude/` от marketplace лежит в корне репозитория (на уровень выше). Поэтому **`work_dir` каждой job должен указывать на корень репо** (или на целевой проект, в котором есть свой `.claude/`). По умолчанию запускай контейнер с рабочей директорией = корень `ai-agents-config` (или монтируй туда целевой репозиторий): `docker run --env-file .env -v /path/to/repo:/work hermes-conductor`, и ставь `work_dir=/work` в job.

## Быстрый старт
```bash
# 1. State (plain Postgres — no Supabase)
psql "$DATABASE_URL" -f sql/schema.sql           # любой Postgres; миграция фазы 2: sql/002_steps_questions.sql

# 2. Конфиг
cp .env.example .env && $EDITOR .env

# 3. Проверка ядра (безопасно, без API/сети)
npm install
npm test                                         # 27 тестов: breaker + steploop + steprunner

# 4. Запуск воркера (локально)
npm start
# или в изоляции:
docker build -t hermes-conductor .
docker run --env-file .env -v /srv/your-repo:/work hermes-conductor
```
Поставить задачу: вызвать n8n webhook `POST /hermes-job` с телом `{kind,title,prompt,priority,max_turns,work_dir}` — или напрямую `insert into hc_jobs(...)`.

## Поток
1. n8n (cron/webhook) кладёт job в `hc_jobs`.
2. Воркер атомарно забирает job (`hc_claim_job`, FOR UPDATE SKIP LOCKED — несколько воркеров не столкнутся).
3. `query()` запускает агентский цикл с наследованием `.claude/`; permissionMode по умолчанию `acceptEdits`.
4. На каждое событие SDK — сохраняем `session_id` на job (для resume), прогон через circuit breaker.
5. ASK-действие (merge / destructive SQL / db push / terraform) → пауза + Telegram (approve/deny/abort) → `waitEscalation` ждёт решения. `git push` НЕ гейтится — это штатный авто-поток.
6. Token/rate-лимит или падение → job `deferred`/recovered с `resume_session_id`; следующий claim продолжает сессию (durable resume).
7. Терминал: done / failed / paused / deferred / escalated / aborted → уведомление в Telegram.

## Circuit breaker (сердце; `src/core/breaker.ts`)
Контролирует ТОЛЬКО то, что агент не решит сам: **зацикливание** (`stuck` при 6 одинаковых ходах подряд — основной контроль) + щедрые backstop'ы (300 ходов, 4 ч wall-clock) + пауза по rate/token-лимиту (→ durable resume) + ask-gate. **Бюджета/денег нет** — сознательно. Покрыт 9 юнит-тестами (`npm test`). Причина существования: SDK по умолчанию НЕ ограничивает ходы — без детекта зацикливания автономный агент может крутиться бесконечно.

## Безопасность
- `permissionMode: acceptEdits` — пишет код сам, но опасные shell-команды остаются под нашим `guard.py` из marketplace и превращаются в эскалации. **Никогда `bypassPermissions`** в автономе: он снимает guard у всех субагентов.
- `DATABASE_URL` (с паролем Postgres) — только server-side. Не паковать в образ, подавать через `--env-file`.
- Рабочий репозиторий монтируется в контейнер; хостовые секреты не пробрасываются.
- Полного аудита событий нет (убран осознанно): храним только статус job/run, `session_id` и последнюю ошибку.
- Для авто commit+push+deploy в контейнере нужна git-аутентификация (deploy-токен/SSH-ключ) и подключённая Vercel Git-интеграция.

## Step mode (фаза 2) — пошаговое исполнение
Если у job есть строки в `hc_steps` (план разложен на шаги), conductor идёт пошаговым путём:
`hc_next_step` (следующий шаг с выполненными `depends_on`) → `runStep` (executor → независимые гейты → `code-reviewer` 0-100 → `runtime-verifier` когда нужно → решение `decideStep`: done/retry/needs_review/blocked) → прогресс/эскалация. Контракт с менеджером Hermes — в **`INTEGRATION.md`**; surfaces для Hermes: вью `hc_project_status` (статус+%), таблицы `hc_steps`, `hc_questions` (async-интервью), функции `hc_next_step`/`hc_answer_question`. Логика (`steploop.ts`/`steprunner.ts`) покрыта тестами; SDK-вызовы изолированы в `agent-runner.ts` (integration seam, на живом SDK ещё не обкатан).

## Файлы
```
INTEGRATION.md             контракт Hermes Agent AI ↔ Fullstack agents (статус-машина, surfaces)
ARCHITECTURE.md            архитектура и решения
sql/schema.sql             полная схема (v2): jobs/runs/escalations/steps/questions + функции/вью
sql/002_steps_questions.sql миграция фазы 2 (для уже развёрнутого v1)
src/core/breaker.ts        circuit breaker (чистая логика, тестируемая)
src/core/steploop.ts       решение per-step цикла (progress-delta/plateau/needs_review) — тестируемое
src/core/steprunner.ts     оркестрация одного шага (executor→gates→review→runtime→retry) — тестируемая
src/core/agent-runner.ts   SDK-адаптер для шагов (integration seam)
src/core/store.ts          доступ к Postgres (jobs/runs/steps/questions/status)
src/core/conductor.ts      главный цикл: whole-job ИЛИ step-mode (если есть hc_steps) + durable resume
src/escalation/*           Telegram уведомления + приём решения человека
n8n/hermes-dispatcher.json webhook для задач + дневной cron для scout
test/{breaker,steploop,steprunner}.test.ts  27 юнит-тестов
Dockerfile, .env.example
```

## Статус (честно)
- **Durable resume реализован, но не обкатан на живом SDK.** `session_id` пишется на job сразу; пауза по token/rate-лимиту → `deferred` с backoff (часы ок) → следующий claim продолжает через `resume:`. Упавший процесс ловит `hc_recover_stale()`. Сквозной автономный прогон против реального SDK ещё не гонялся.
- **Деньги не считаем** (осознанно убрано) — ни ledger, ни бюджет, ни дневной пул.
- **Один SDK-coupling.** Маппинг сообщений SDK живёт в одном месте — `mapSdkMessage()` в conductor.ts. SDK быстро меняется (TS V2 в preview) — если форма сообщений уедет, правится только эта функция, остальное завязано на нашу нормализованную `Event`.
- Дашборды/observability — нет (осознанно). Приоритизация задач примитивная (priority + FIFO).
