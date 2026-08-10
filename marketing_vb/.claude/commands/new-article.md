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
| `full` | all | От текущего состояния до первого чекпоинта |

## Checkpoints

1. **После `plan`** — Вадим одобряет title + outline
2. **После `publish`** — Вадим одобряет финальный текст + meta вместе
