# ⚡ ДЛЯ AI-АГЕНТА: как с этим работать (читай первым)

> Ты получил доступ к репозиторию `ai-agents-config`. Это система Fullstack agents — команда из 10 специализированных Claude Code субагентов под управлением оркестратора + автономный дирижёр. Этот раздел — операционная инструкция: что делать, в каком порядке, какими командами. Концепцию и обоснования см. ниже (разделы 0–7).

> **Две сущности — не путай:**
> - **Fullstack agents** — ЭТА система (внутри Claude Code): 10 агентов + команды `/sm-*` + скиллы. Исполнительный слой («рабочие»).
> - **Hermes Agent AI** — ВНЕШНИЙ оркестратор/менеджер (продукт NoSearch на VPS). Управляющий слой: маршрутизирует задачи между проектами/каналами (Claude Code-код, Claude Code-SEO, Canva-дизайн…), независимо проверяет результат Claude Code и держит связь с человеком. `conductor/` — первый кусок интеграции Hermes именно с каналом Claude Code (очередь/resume/эскалации), а не сам Hermes.

## Кто ты в этой системе?
Определи свою роль — от неё зависит всё:

- **Если ты — главная сессия Claude Code** (человек открыл проект с подключённым этим marketplace): ты **оркестратор Fullstack agents**. Твоя работа — планировать и делегировать субагентам, НЕ писать код самому. Твоя конституция — файл `CLAUDE.md` в корне. Следуй ей.
- **Если ты — субагент** (тебя вызвали через Task tool): ты исполнитель одного слоя. Твои инструкции — в твоём `.md` файле (`plugins/hermes-*/agents/*.md`). Делай свою задачу, пиши отчёт в scratchpad, не лезь в чужие слои.
- **Если ты — внешний агент, которому поручили развернуть/поддерживать систему**: следуй разделу «Развёртывание» ниже. Не запускай ничего деструктивного без подтверждения человека.

## Карта: что где лежит
```
ai-agents-config/
├── FULLSTACK-AGENTS.md              ← ты здесь. Единый бриф.
├── CLAUDE.md              ← конституция оркестратора (правила делегирования, тиринг моделей)
├── README.md             ← краткий обзор
├── .claude/
│   ├── settings.json      ← permissions: что разрешено / спросить / запретить
│   └── hooks/guard.py     ← хук безопасности: блокирует опасные команды
├── .claude-plugin/marketplace.json  ← манифест 9 плагинов
├── plugins/              ← сами агенты (по плагину на слой)
│   ├── hermes-core/      → product-architect (Opus) + project-planning (интервью→детальный план) + scratchpad-протокол + session-handoff (через /clear/сжатие) + команды
│   ├── hermes-design/    → design-director
│   ├── hermes-frontend/  → frontend-engineer
│   ├── hermes-backend/   → backend-engineer
│   ├── hermes-data/      → database-engineer
│   ├── hermes-platform/  → platform-engineer (хостинг+облако+CI/CD)
│   ├── hermes-quality/   → qa-engineer + security-auditor (Opus)
│   ├── hermes-sre/       → sre-engineer (ошибки+кэш+rate limit+доступность)
│   ├── hermes-scout/     → trend-scout (ежедневный скан) + solution-evaluator (/sm-evaluate конкретного решения)
│   └── hermes-verify/    → code-reviewer (0-100+evidence) + runtime-verifier (e2e front+back+db) + verification-protocol + ultracite-lint + policy-packs
└── conductor/            ← автономный дирижёр (TS-сервис, запускает всё это без человека)
```

## Сценарий A — построить фичу (ты = оркестратор)
1. Запусти `/sm-feature "<описание фичи>"`. Сначала — **адаптивное интервью** (скилл `project-planning`, слои L0–L11) + предсказание анти-паттернов.
2. product-architect (Opus) пишет в `.claude/scratchpad/<slug>/`: `spec.md`, `architecture.md`, `nfr.md`, `risks.md` и **детальный `plan.md`** (шаги с acceptance/tags/quality_bar/depends_on — это контракт для верификации).
3. Прочитай `plan.md`. Покажи человеку сводку. **Жёсткий гейт: остановись, дождись явного `go`** перед написанием кода.
4. Делегируй задачи из `plan.md` субагентам через Task tool. В каждый промпт включи: путь к scratchpad, номер задачи, требование записать отчёт в `handoff/NN-<role>.md`. (Детали — скилл `scratchpad-protocol`.)
5. После возврата субагента читай его **handoff-файл**, не только summary. Обновляй статусы в `plan.md`.
6. После каждой задачи — **верификация** (скилл `verification-protocol`, команда `/sm-verify`): независимый перезапуск гейтов (`ultracite lint`→typecheck→test→build) → `code-reviewer` (0-100 + acceptance с доказательством) → при approve `runtime-verifier` (поднять db+back+front, e2e). Ретраи по progress-delta + накопленным критикам; needs-review/block → эскалация. Перед релизом — `security-auditor` (BLOCK останавливает).
7. Заверши командой `/sm-docs`.

## Сценарий B — кого вызывать под задачу (таблица делегирования)
| Триггер в задаче | Субагент | Модель |
|---|---|---|
| архитектура, спека, выбор стека | product-architect | Opus |
| UI, дизайн, анимация, лендинг | design-director | Sonnet |
| компонент, страница, React/Next | frontend-engineer | Sonnet |
| API, эндпоинт, бизнес-логика, очередь | backend-engineer | Sonnet |
| схема, миграция, SQL, RLS, индекс | database-engineer | Sonnet |
| деплой, CI, облако, хостинг, релиз | platform-engineer | Sonnet |
| тест, QA, E2E, регрессия | qa-engineer | Opus |
| ревью/приёмка кода (0-100, acceptance с доказательством) | code-reviewer | Opus |
| «реально ли работает» — поднять стек, e2e front+back+db | runtime-verifier | Opus |
| аудит безопасности перед продом | security-auditor | Opus |
| ошибка, инцидент, медленно, кэш, алерт | sre-engineer | Sonnet |
| «что нового в экосистеме», тренды | trend-scout | Opus |
| оцени конкретное решение (repo/plugin/skill/MCP/ссылку) + интеграция | solution-evaluator (`/sm-evaluate`) | Opus |

## Сценарий C — ежедневный скан экосистемы (ты = trend-scout или дирижёр)
1. Вызови субагента `trend-scout` (или дирижёр ставит scout-job по cron).
2. Он следует скиллу `trend-scan`: collect.py (GitHub) → WebFetch источников → score.py (скоринг) → security-гейт → дайджест.
3. Результат — дайджест в `.claude/scratchpad/scout/`. **Scout НИЧЕГО НЕ УСТАНАВЛИВАЕТ** — только рекомендует. Решение за человеком.

## Сценарий D — автономный запуск (ты = дирижёр / разворачиваешь его)
1. `cd conductor && cp .env.example .env` — DATABASE_URL по умолчанию `file:./ho.db` (+ опц. TELEGRAM_*).
2. `npm install && npm test` — 168 тестов (breaker/steploop/steprunner/store/backoff/signature/askgate/callback/heartbeat/profiles), SQLite через better-sqlite3, без сети.
3. Создать схему: `sqlite3 ho.db < conductor/sql/schema.sql` (для file:; или `turso db shell` для Turso).
4. Запуск: `docker build -t hermes-conductor conductor/ && docker run --env-file conductor/.env -v $(pwd):/work hermes-conductor`. Ставь `work_dir=/work` в job (там лежит `.claude/`).
5. Поставить задачу: `insert into ho_jobs(kind,title,prompt,...)` или через n8n webhook.

## 🔒 Незыблемые правила (нарушение = поломка системы)
1. **commit + push — автоматически, merge — НИКОГДА сам.** После каждого хода `Stop`-хук коммитит и пушит ветку (push триггерит Vercel-деплой через Git-интеграцию). Запрещены и требуют человека только: `gh pr merge`, destructive SQL (DROP/TRUNCATE), `supabase db push`, terraform apply/destroy. Enforced в `guard.py` и в ask-gate дирижёра. **На ветках `main`/`master` авто-push отключён.**
2. **Контекст между агентами — только через файлы** scratchpad, не через summary.
3. **trend-scout НИКОГДА не устанавливает** найденное. Только дайджест.
4. **Никогда `bypassPermissions`** в автономном режиме — это снимает guard у всех субагентов.
5. **Секреты — никогда** в код / логи / коммиты / Docker-образ. Только имена переменных.
6. **Падающий тест — это находка, а не препятствие.** Не ослабляй и не удаляй тесты ради зелёной сборки.
7. **Тиринг моделей:** Opus последняя (`claude-opus-4-8`) — на ВСЁ (все 10 агентов); Sonnet — только рутина, которая мало что значит (explore/grep/форматирование). Затраты не оптимизируем.
8. **Перед установкой стороннего скилла/MCP — прочитай его исходник.** 13.4% публичных скиллов имели критические уязвимости.

---

# Fullstack agents — полная вертикаль автономной full-stack разработки на Claude Code

> Этот документ — единый бриф всей системы. Он написан так, чтобы его мог прочитать и человек, и AI-агент, которому передаётся управление. Если ты — AI-агент, читающий это: ниже описана система, частью которой ты являешься или которой управляешь. Сначала прочитай весь этот файл, затем углубляйся в указанные подпапки по мере необходимости.

---

## 0. Что это и зачем

Fullstack agents — это система, которая позволяет вести **настоящую production full-stack разработку** силами AI-агентов под управлением оркестратора, с человеком в петле только на дорогих и опасных решениях.

Отправная идея: «vibe-кодеры думают, что full-stack = фронт + бэк», тогда как production-реальность — это ~14 слоёв (фронтенд, API, БД, auth, хостинг, облако, CI/CD, безопасность, rate limiting, кэш/CDN, балансировка/масштабирование, трекинг ошибок, доступность/восстановление) плюс дизайн. Fullstack agents раскладывает все эти слои на специализированных агентов и оркестрирует их.

Система живёт в **одном репозитории** `ai-agents-config` из **двух зон** (двух слоёв), которые работают вместе:

```
┌──────────────────────────────────────────────────────────────┐
│  conductor/  (слой C)  —  «ДИРИЖЁР»                            │
│  Автономный TS-сервис. Запускает Claude Code без человека,     │
│  держит безопасность + durable resume, эскалирует в Telegram.  │
│                          │ запускает через Agent SDK           │
│                          │ settingSources:['project']          │
│                          ▼                                     │
│  корень репо  (слои A+B)  —  «ОРКЕСТР + ПАРТИТУРА»            │
│  Claude Code plugin marketplace: 9 агентов + trend-scout,      │
│  правила оркестрации (CLAUDE.md), протокол передачи контекста, │
│  enforcement безопасности (settings.json + guard.py).          │
└──────────────────────────────────────────────────────────────┘
```

**Аналогия:** marketplace — это оркестр (музыканты) и партитура (правила). Conductor — дирижёр, который запускает оркестр автономно. Fullstack agents как «роль оркестратора» живёт внутри marketplace (главная сессия Claude Code, ведомая CLAUDE.md); Fullstack agents как «автономный сервис» — это conductor.

---

## 1. Карта репозиториев

### A+B — `<repo root>/`  (конфиг ДЛЯ Claude Code)
Это нативный Claude Code plugin marketplace. Подключается командой `/plugin marketplace add <repo>`.

```
<repo root>/
├── CLAUDE.md                        ← КОНСТИТУЦИЯ ОРКЕСТРАТОРА. Главный файл.
│                                      Рабочий цикл, таблица "триггер→агент",
│                                      тиринг моделей, правила параллелизма и прод-операций.
├── .claude/
│   ├── settings.json                ← permissions allow/ask/deny
│   └── hooks/guard.py               ← PreToolUse-хук: блок destructive-команд,
│                                      ask-гейт на прод-действия (протестирован)
├── .claude-plugin/marketplace.json  ← манифест маркетплейса (9 плагинов)
└── plugins/
    ├── hermes-core/                 ← product-architect (Opus) + scratchpad-протокол +
    │                                  команды /sm-feature, /sm-handoff-status, /sm-docs
    ├── hermes-design/               ← design-director (UI/UX, дизайн-токены, motion)
    ├── hermes-frontend/             ← frontend-engineer (TS/React/Next, визуальная самопроверка)
    ├── hermes-backend/              ← backend-engineer (API, бизнес-логика, контракты)
    ├── hermes-data/                 ← database-engineer (PostgreSQL, миграции, RLS)
    ├── hermes-platform/             ← platform-engineer (хостинг, облако, IaC, CI/CD через gh CLI)
    ├── hermes-quality/              ← qa-engineer (TDD, Playwright) + security-auditor (Opus, ToB-метод)
    ├── hermes-sre/                  ← sre-engineer (Sentry, observability, кэш, rate limit, availability)
    └── hermes-scout/                ← trend-scout (ежедневный скан экосистемы; report-only)
```

### C — `conductor/`  (автономный сервис НАД Claude Code)
TypeScript-сервис вокруг `@anthropic-ai/claude-agent-sdk`. НЕ Claude Code plugin — это процесс, который Claude Code запускает.

```
conductor/
├── ARCHITECTURE.md                  ← 5-слойная схема и обоснования
├── sql/schema.sql                   ← очередь задач, прогоны (session_id для resume), эскалации
│                                      + ho_claim_job() (атомарный захват) + ho_recover_stale() (resume упавших)
├── src/core/
│   ├── breaker.ts                   ← CIRCUIT BREAKER. Сердце. Логика остановки. 11 тестов.
│   ├── store.ts                     ← доступ к Postgres
│   └── conductor.ts                 ← главный цикл: SDK ↔ breaker ↔ store ↔ escalation
├── src/escalation/
│   ├── telegram.ts                  ← уведомление человеку (кнопки approve/deny/abort)
│   └── bot-callback.ts              ← приём решения человека → в ho_escalations
├── n8n/hermes-dispatcher.json       ← webhook для постановки задач + дневной cron для scout
├── test/breaker.test.ts             ← 11 юнит-тестов ядра
├── Dockerfile, .env.example
```

---

## 2. Как это работает — полный поток одной задачи

```
[человек или cron]
   │  ставит задачу
   ▼
n8n  ──POST /hermes-job──►  SQLite: insert into ho_jobs (status=queued)
   ▼
conductor/ (воркер)
   │ 1. store.claimJob() — атомарно берёт задачу (write-транзакция SQLite, single-writer)
   │ 2. preflight: есть resume_session_id? (упавший/приостановленный прогон — продолжаем)
   │ 3. query() из Agent SDK с settingSources:['project'] (+ resume:<session_id> если есть)
   │      └─► наследует ВСЁ из marketplace (корень репо):
   │          • системная роль = Fullstack agents из CLAUDE.md
   │          • доступны 9 агентов как субагенты
   │          • активны settings.json + guard.py
   │          • permissionMode: acceptEdits (код сам, опасное — гейт)
   │ 4. на каждое событие SDK:
   │      • сохраняем session_id на job (для durable resume)
   │      • прогон через CIRCUIT BREAKER (без бюджета):
   │          stuck(зацикливание) | turn/wall backstop | rate-limit→пауза+resume | ask-gate
   │ 5. ВНУТРИ прогона главная сессия (Fullstack agents) сама:
   │      • зовёт product-architect → spec/architecture/plan/risks в scratchpad
   │      • делегирует задачи агентам по plan.md через Task tool
   │      • агенты пишут отчёты в .claude/scratchpad/<feature>/handoff/
   │      • гейт качества: qa-engineer → security-auditor
   ▼
если агент хочет гейтнутое действие (merge / destructive SQL / db push / terraform):
   │ breaker/guard → ПАУЗА → эскалация
   ▼
Telegram: "🟡 approve / deny / abort"  ──►  человек жмёт кнопку
   │                                          ▼
   │                              bot-callback пишет решение в ho_escalations
   ▼                                          │
conductor.waitEscalation() ◄─────────────────┘  (resume или abort)
   ▼
терминал: done | failed | deferred | escalated | aborted
   ▼
Telegram: "✅/❌ job <status> + summary"
```

---

## 3. Ключевые принципы (не нарушать)

1. **Контекст между агентами — через файлы**, не через summary. Субагенты изолированы и не общаются; всё идёт через `.claude/scratchpad/<feature>/` (см. скилл `scratchpad-protocol`). Это же делает безопасным `/clear` для экономии токенов — состояние поднимается с диска.
2. **Тиринг моделей.** Opus последняя (`claude-opus-4-8`) — на ВСЁ (архитектура, код, дизайн, БД, тесты, безопасность, SRE, scout). Sonnet — только рутина, которая мало что значит. Затраты сознательно НЕ оптимизируем — приоритет качество.
3. **commit/push авто, merge — человек.** После каждого хода `Stop`-хук коммитит+пушит ветку → Vercel деплоит сам (Git-интеграция). Гейтятся только: `gh pr merge`, destructive SQL, `supabase db push`, terraform. Два уровня: `guard.py` (внутри Claude Code) и ask-gate (в дирижёре). На `main`/`master` авто-push выключен.
4. **Дирижёр — это про остановку и про возобновление, не про бюджет.** Agent SDK по умолчанию НЕ лимитирует ходы. Бюджет/деньги НЕ контролируем. Единственный runaway-контроль — детект зацикливания (`stuck`) + щедрые backstop'ы по ходам/времени. При исчерпании токенов/лимита — пауза и **durable resume** по `session_id` (хоть через 5–25 часов). Всё в `breaker.ts` + `conductor.ts`.
5. **Никогда `bypassPermissions` в автономе.** Он раздаёт full-access всем субагентам и снимает guard. Только `acceptEdits`.
6. **scout ничего не устанавливает.** Только дайджест; решение об установке — за человеком (после статистики: 13.4% публичных скиллов имели критические уязвимости).
7. **Падающий тест — это находка, а не препятствие.** Не ослаблять и не удалять тесты ради зелёной сборки.
8. **Секреты — никогда в код/логи/коммиты/образ.** пароль Postgres (DATABASE_URL) — только server-side, через `--env-file`.

---

## 4. Стек по умолчанию
TypeScript strict / Next.js (App Router, Route Handlers) или FastAPI (Python) / **plain PostgreSQL** (RLS; расширения `pg_cron`/`pgvector`/`pgmq`/`pg_net`) / Drizzle ORM или SQLAlchemy+Alembic / **Better Auth** (MIT, self-host) / **PGMQ** очереди / Valkey кэш / gh CLI. По требованию: SeaweedFS (файлы) · Centrifugo (realtime) · PgBouncer · Keycloak. Gateway — Traefik. **Supabase НЕ используем** (исключение — way2buy; Studio на `supabase.smiro.dev`). **Полная карта замены Supabase→OSS — в `STACK.md`.** Состояние дирижёра — локальный SQLite через better-sqlite3, НЕ Postgres и НЕ libSQL/Turso (@libsql/client снят: его локальный драйвер отдавал соединение каждой transaction() и не закрывал — 33 021 осиротевшее соединение и 5.4 ГБ RSS на опросе ПУСТОЙ очереди; dbPath() теперь отвергает удалённые схемы). DATABASE_URL обязан быть абсолютным. Триггеры — n8n. Эскалации — Telegram.

---

## 5. Развёртывание (порядок)

1. **Marketplace.** Залить `<repo root>/` в git. В рабочем проекте: `/plugin marketplace add <repo>`, поставить `hermes-core` + нужные слои. Внешние компаньоны: `frontend-design@claude-plugins-official`, `superpowers@claude-plugins-official`, `trailofbits/skills`.
2. **State.** Создать схему: `sqlite3 ho.db < conductor/sql/schema.sql` (file:; или Turso `turso db shell`).
3. **Проверка ядра.** В `conductor/`: `npm install && npm test` (breaker/steploop/steprunner/store/profiles/askgate — 168 тестов, без сети/API).
4. **Conductor.** Заполнить `.env` (см. `.env.example`; DATABASE_URL по умолчанию `file:./ho.db`). `npm start` (или `docker build`/`docker run --env-file .env -v <repo>:/work`). Рабочий репозиторий должен содержать `.claude/` от marketplace.
5. **Triggers.** Импортировать `n8n/hermes-dispatcher.json`, подключить путь к локальной `ho.db` (абсолютный) и Telegram-бота.
6. **Первый прогон.** Поставить тестовую задачу (`insert into ho_jobs` или webhook) с небольшим `max_turns` и смотреть статусы в `ho_jobs` / `ho_runs`. Проверить, что `resume_session_id` проставляется, и что пауза по лимиту переводит job в `deferred`, а не в `failed`.

---

## 6. Что проверено, а что — нет (честно)

**Проверено в этой сборке:**
- `breaker.ts` — 9 юнит-тестов зелёные (stuck/turns/timeout/rate-limit→pause/ask-gate/completion/error).
- Весь `src/` дирижёра проходит strict TypeScript (`tsc --noEmit`).
- `guard.py` marketplace — протестирован на матрице block/ask/allow.
- Все JSON-манифесты валидны, у 10 агентов корректный frontmatter (все Opus), Python-хуки парсятся.

**Реализовано в этой итерации (но НЕ обкатано на живом автономном прогоне):**
- **Durable resume.** `session_id` пишется на job сразу; пауза по token/rate-лимиту → `deferred` с backoff (хоть часы) → следующий claim продолжает сессию через `resume:`. Упавший процесс ловит `ho_recover_stale()` и переочередает с resume. Логика есть, сквозной прогон против живого SDK ещё не гонялся.
- **Авто commit+push+deploy** через `Stop`-хук (push → Vercel Git-деплой). Логика есть; нужна git-аутентификация на VPS/в контейнере.

**НЕ реализовано / осознанно убрано:**
- **Контроль денег убран полностью.** Бюджет/ledger/дневной пул не считаем — приоритет качество, защита только от зацикливания.
- **Авто-`/clear` каждые N запросов в интерактиве — невозможно хуком** (хук не умеет запускать слэш-команды). Сделан только счётчик-напоминание (`clear-counter.py`); реальная экономия — встроенная авто-компакция Claude Code и изоляция контекста по scratchpad. В дирижёре каждый job — это и так свежая сессия.
- **Единая точка связи с SDK** — `mapSdkMessage()` в `conductor.ts`. SDK быстро меняется (TS V2 в preview); если форма сообщений уедет, правится только эта функция.
- Observability/дашборды — нет (осознанно). Приоритизация задач — примитивная (priority + FIFO).
- Эвалы для агентов/скиллов — отложены; полагаемся на ручную проверку на реальной фиче.

---

## 7. Глоссарий (чтобы AI-агент не путал сущности Claude Code)
- **Plugin** — контейнер-дистрибутив. Содержит агентов, скиллы, команды, hooks, MCP-конфиги. (Агент НЕ состоит из плагинов — наоборот.)
- **Subagent** — markdown-файл: system prompt + список tools + модель + опц. память. Изолированный контекст. Не общается с другими субагентами. Не может спавнить субагентов.
- **Skill** — знание («как делать»). Progressive disclosure: ~100 токенов описания на старте, тело — по триггеру. Дёшево.
- **MCP server** — доступ к внешним системам («руки»). Самый дорогой по токенам. У Fullstack agents подключается per-project, не глобально.
- **Orchestrator (Fullstack agents-роль)** — главная сессия Claude Code, ведомая CLAUDE.md, делегирует субагентам через Task tool.
- **Conductor (Fullstack agents-сервис)** — внешний автономный процесс, запускающий оркестратор без человека.
- **scratchpad** — `.claude/scratchpad/<feature>/` — файловый канал передачи контекста между агентами.
- **circuit breaker** — модуль остановки/паузы автономного прогона: детект зацикливания, backstop по ходам/времени, пауза по rate-лимиту (→ durable resume), ask-gate. Бюджет НЕ контролирует.
- **durable resume** — продолжение прогона по сохранённому `session_id` после паузы по лимиту или падения процесса (через минуты или часы).
- **escalation** — пауза прогона с передачей решения человеку (Telegram).
