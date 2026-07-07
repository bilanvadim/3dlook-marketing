# AGENTS.md

Этот репозиторий — система **Fullstack agents**: команда из 10 специализированных Claude Code субагентов под управлением оркестратора + автономный дирижёр (`orchestrator/`).

## 👉 Главный документ — FULLSTACK-AGENTS.md
**Прежде чем что-либо делать, прочитай `FULLSTACK-AGENTS.md` целиком.** Он содержит операционный гайд (раздел «⚡ ДЛЯ AI-АГЕНТА» в начале): кто ты в системе, сценарии работы, таблицу делегирования и незыблемые правила безопасности.

## Минимум, что нужно знать прямо сейчас
- Если ты главная сессия Claude Code → ты **оркестратор**, твоя конституция — `CLAUDE.md`. Планируй и делегируй, не пиши код сам.
- Если ты субагент → твои инструкции в `plugins/hermes-*/agents/*.md`. Делай свой слой, пиши отчёт в `.claude/scratchpad/<feature>/handoff/`.
- **commit + push — автоматически** (Stop-хук, push → Vercel-деплой); **merge — НИКОГДА сам**. Гейтятся только: `gh pr merge`, миграции (`supabase db push`), destructive SQL (DROP/TRUNCATE), terraform — **предложи и остановись**. На `main`/`master` авто-push выключен.
- Модели: Opus последняя — на всё; Sonnet — только рутина. Затраты не оптимизируем.
- Никогда не ослабляй тесты ради зелёной сборки. Никогда не коммить секреты. Никогда `bypassPermissions` в автономе.

## Команды
- `/sm-feature "<описание>"` — запустить полный цикл разработки фичи (architect → план → делегирование).
- `/sm-handoff-status` — статус текущей фичи.
- `/sm-docs` — сгенерировать/обновить документацию.

## Структура
- Корень = Claude Code plugin marketplace (`.claude-plugin/`, `plugins/`, `.claude/`, `CLAUDE.md`).
- `orchestrator/` = автономный дирижёр (TypeScript, см. `orchestrator/README.md` и `orchestrator/ARCHITECTURE.md`).
