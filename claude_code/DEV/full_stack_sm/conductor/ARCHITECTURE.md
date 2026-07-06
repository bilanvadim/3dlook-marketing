# Fullstack agents Conductor — автономный дирижёр над Claude Code

Слой C. Сервис, который запускает Claude-Code-стек (marketplace из слоёв A+B) **без человека за рулём**: берёт задачу, прогоняет через Agent SDK, держит безопасность и **durable resume**, эскалирует человеку только когда нужно. Бюджет/деньги НЕ контролирует (осознанно).

## Что это и чем НЕ является
- **Является:** долгоживущий TypeScript-сервис вокруг `@anthropic-ai/claude-agent-sdk`, который программно запускает тот же агентский цикл, что и Claude Code, наследуя наш `.claude/` конфиг через `settingSources: ['project']`.
- **НЕ является:** заменой агентов из marketplace. Дирижёр их не дублирует — он их *исполняет*. Оркестрация внутри прогона по-прежнему делается product-architect + scratchpad-протоколом.

## Главный принцип: дирижёр — это про ОСТАНОВКУ и ВОЗОБНОВЛЕНИЕ, не про запуск
Факт из доков (проверено 15.06.2026): Agent SDK по умолчанию `max_turns: unlimited`, нет retry, нет durable execution, нет observability. Всё это — наша ответственность. Поэтому ядро дирижёра — **circuit breaker (детект зацикливания)** + **durable resume по `session_id`**, а не «умный запускатель». Деньги сознательно не контролируем — приоритет качество.

## Архитектура (5 слоёв)

```
┌─ TRIGGER ────────────────────────────────────────────────┐
│ n8n: cron (scout daily) | webhook (новая задача) | вручную│
└───────────────┬───────────────────────────────────────────┘
                │ enqueue job
┌─ STATE (Postgres) ─────────────────────────────────────────┐
│ jobs (resume_session_id) · runs (session_id) · escalations │
└───────────────┬───────────────────────────────────────────┘
                │ poll next queued job
┌─ CONDUCTOR CORE (этот сервис, TS) ─────────────────────────┐
│ 0. recoverStale(): упавшие run'ы → deferred с session_id  │
│ 1. claim job (atomic, FOR UPDATE SKIP LOCKED)              │
│ 2. есть resume_session_id? → продолжаем сессию            │
│ 3. query() c options: settingSources:['project'],         │
│    permissionMode, resume:<session_id> если есть          │
│ 4. stream события → сохраняем session_id на job           │
│ ┌─ CIRCUIT BREAKER (на каждое событие) ─────────────────┐ │
│ │ stuck-detection (основное) · turn/wallclock backstop ·│ │
│ │ RateLimitEvent → pause+resume · ASK-gate              │ │
│ └───────────────────────────────────────────────────────┘ │
│ 5. terminal: done | failed | paused | escalated | aborted │
└───────────────┬───────────────────────────────────────────┘
                │ on escalation / done
┌─ ESCALATION ───────────────────────────────────────────────┐
│ Telegram-бот: пауза + контекст + кнопки approve/deny/abort │
│ человек отвечает → resume(sessionId) или abort             │
└────────────────────────────────────────────────────────────┘
```

## Поток одного прогона (happy path)
1. n8n кладёт job в Postgres (`status=queued`, тип, промпт, `max_turns`/`max_wall_secs` опц.).
2. Воркер сначала `recoverStale()` (переочередь упавших с их `session_id`), затем забирает job атомарно.
3. Если у job есть `resume_session_id` — продолжаем ту же сессию; иначе старт с нуля.
4. `query()` с `settingSources:['project']` (наследует marketplace), `permissionMode`, `resume:<session_id>` если есть, системным промптом = роль Fullstack agents из CLAUDE.md.
5. На каждое сообщение из стрима: сохраняем `session_id` на job (для resume), прогоняем через circuit breaker.
6. Token/rate-лимит → job `deferred` с backoff (часы ок), сессия сохранена → позже продолжится. Завершение → результат, `resume_session_id` очищается.

## Permission-режимы (главный рычаг автономности)
- `default` — спрашивает на каждое нестандартное действие. Для дирижёра бесполезно (некому отвечать в реалтайме) → превращается в эскалации.
- `acceptEdits` — авто-принимает правки файлов, но НЕ shell-команды из ask/deny. **Рекомендуемый дефолт** для автономных прогонов: код пишет сам, опасное эскалирует.
- `bypassPermissions` — НЕ использовать в автономе. Факт из доков: родитель в bypass раздаёт full autonomous access всем субагентам. Это снимает наш guard.py.
Наш `.claude/settings.json` + `guard.py` остаются активны при `acceptEdits` — ask/deny-правила превращаются в точки эскалации, а не в немой автозапуск.

## Circuit breaker — условия (бюджета НЕТ; деньги не контролируем)
| Триггер | Дефолт | Действие |
|---|---|---|
| **Stuck** (нет прогресса: те же файлы/tool-calls подряд) — основной контроль | 6 повторов | эскалация (зациклился) |
| Ходы (turns) — runaway backstop | 300 | эскалация |
| Wall-clock — runaway backstop | 4 ч | стоп, job=failed(timeout) |
| RateLimit/token-лимит = rejected | — | **пауза + backoff → durable resume**, job=deferred |
| RateLimit = allowed_warning | — | продолжить, снизить параллелизм |
| Запрос ASK-действия (merge / destructive SQL / db push / terraform) | — | пауза, эскалация человеку. `git push` НЕ гейтится |
| Падение процесса посреди прогона | `HC_STALE_RUN_SECS` | `hc_recover_stale()` → deferred с `session_id` → resume |

## State-модель (Postgres, см. sql/schema.sql) — минимальная, ради resume
- `jobs` — очередь задач (queued/claimed/running/paused/done/failed/deferred/escalated/aborted) + `resume_session_id` + `attempts`.
- `runs` — попытки исполнения job; ключевое поле — `session_id` (для durable resume) + `stop_reason` + `error`.
- `escalations` — открытые вопросы к человеку + их разрешения.
- `hc_claim_job()` — атомарный захват; `hc_recover_stale()` — переочередь упавших с их session_id.
- Нет `run_events` и `budget_ledger` — полный аудит и подсчёт денег осознанно убраны.

## Почему так (ключевые решения)
1. **TS, не Python** — стек Sergiy (Next.js/TS), и SDK на TS bundle'ит native Claude Code binary (один npm install).
2. **Postgres как state** — уже его паттерн из OrchestrAgent; FOR UPDATE SKIP LOCKED даёт безопасную многопоточную очередь без отдельного брокера.
3. **n8n только как trigger** — не как место бизнес-логики. Логика и лимиты — в коде (тестируемо), n8n дёргает и доставляет уведомления.
4. **Эскалация через Telegram** — у Sergiy уже есть бот; человек остаётся в петле на дорогих/опасных решениях, но не на рутине.
5. **Docker-изоляция executor** — его паттерн; дирижёр и Claude Code крутятся в контейнере с смонтированным рабочим репозиторием и без доступа к хостовым секретам.

## Статус и что НЕ покрывает (честно)
- **Durable resume реализован** (pause-on-limit + `hc_recover_stale` + `resume:`), но сквозной прогон против живого SDK ещё не обкатан.
- **Деньги/бюджет/стоимость — убраны полностью** (осознанно, по требованию: приоритет качество).
- **Авто `/clear` каждые N запросов в интерактиве — невозможно хуком** (хук не запускает слэш-команды); сделан счётчик-напоминание, реальная экономия — встроенная авто-компакция + scratchpad. В дирижёре каждый job — свежая сессия.
- Мульти-тенантность и RBAC; observability/дашборды — нет (осознанно).
- Приоритизация задач примитивная (FIFO + priority).
