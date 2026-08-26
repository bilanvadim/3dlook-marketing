---
description: Запускает SEO workflow через orchestrator. 4 агента, 2 чекпоинта.
argument-hint: "[topic or slug] [stage (plan/write/edit/publish/full)]"
---

Запроси orchestrator для SEO workflow.

## Stages

| Stage | Agent | What happens |
|-------|-------|--------------|
| `plan` | seo-planner | Keywords → title → outline (всё в одном шаге) |
| `write` | seo-writer | Пишет все секции по approved плану |
| `edit` | seo-editor | 4 прохода: dedup citations, structure, expert voice, polish |
| `publish` | seo-publisher | Meta title + description + checklist + final package |
| `full` | all | От текущего состояния до БЛИЖАЙШЕГО НЕПРОЙДЕННОГО чекпоинта |

## Checkpoints

1. **После `plan`** — Вадим одобряет title + outline
2. **После `publish`** — Вадим одобряет финальный текст + meta вместе

Чекпоинтов ровно два, и **между `write`, `edit` и `publish` их нет**. Если
чекпоинт 1 закрыт (в промпте есть «АПРУВ ЕСТЬ» или `plan.md` несёт
`status: approved`), то `full` идёт `write → edit → publish` одним прогоном и
останавливается только на чекпоинте 2. Закончив `write`, сразу начинай `edit`;
закончив `edit` — сразу `publish`. Не трактуй отдельную стадию как повод
завершить работу: на 2026-08-25 прогон остановился после `edit` с выводом
«edit is a standalone stage, it does not chain into publish», и статью пришлось
доводить двумя лишними job'ами.

Именованная стадия (`/new-article "<тема>" edit`) — наоборот, означает «ровно
одна эта стадия»: её и выполняй, дальше не иди.
