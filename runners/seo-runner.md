---
name: seo-runner
description: Координатор SEO-пайплайна. 4 агента, 2 чекпоинта. Вызывается orchestrator-ом.
---

## Пайплайн

```
seo-planner → [QC + VADIM checkpoint] → seo-writer → seo-editor → seo-publisher → [QC + VADIM checkpoint]
```

## Стадии

| Stage | Agent | Input | Output |
|-------|-------|-------|--------|
| `plan` | seo-planner | context pack + raw keywords | `plan.md` (keywords + title + outline) |
| `write` | seo-writer | approved plan.md | `draft.md` |
| `edit` | seo-editor | draft.md | `final.md` |
| `publish` | seo-publisher | final.md | `publish-package.md` (meta + checklist + article) |

## Autodetect state

| File exists | State |
|-------------|-------|
| Nothing | Start from `plan` |
| `plan.md` (not approved) | Waiting for checkpoint 1 |
| `plan.md` (approved) | Ready for `write` |
| `draft.md` | Ready for `edit` |
| `final.md` | Ready for `publish` |
| `publish-package.md` (not approved) | Waiting for checkpoint 2 |
| `publish-package.md` (approved) | Done — Вадим публикует |

## Auto-QC points

If `AUTO_QC_ENABLED=true`:
- After `plan` → QC on plan.md
- After `write` → QC on draft.md
- After `publish` → QC on publish-package.md

If QC < 12 → STOP, recommend regeneration.

## Checkpoints

**Checkpoint 1 (after plan):** Вадиму — title + outline summary. Approve → write. Edit → replan.

**Checkpoint 2 (after publish):** Вадиму — final text + meta title + meta description + checklist. Approve all → publish. Edit → back to editor or meta.
