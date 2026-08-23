---
description: Запускает page-builder — производственную линию страниц сайта 3dlook.ai. Гейты G-I / G-A / G-T + слепой судья 85/100.
argument-hint: "[vertical or URL] [stage (gate/build/judge/handoff/full)]"
---

Запусти скил `page-builder` (`.claude/skills/page-builder/SKILL.md`) для страницы сайта.

Это **не** статья. Блог, хабы, comparison и buyer guides идут через `/new-article` (mvb-seo) —
скил сам отправит туда, если запрос на самом деле про статью.

## Stages

| Stage | What happens |
|-------|--------------|
| `gate` | Phase 0–2: интейк, роутинг в Kit, гейты G-I (стоит ли страница существовать) и G-A (архитектура, URL, каннибализация). Останавливается на чекпоинте Вадима |
| `build` | Phase 3: структура по слотам Kit → копирайт → пасс гардрейлов и гуманизации → AI-visibility → UI/UX по DESIGN.md → конверсия → техслой |
| `judge` | Phase 4–5: гейт G-T + слепой судья в свежем сабагенте, порог 85/100, до 3 раундов |
| `handoff` | Phase 6: пакет для того, кто публикует в WordPress — README, TODO, fact-sheet, Yoast и schema инструкции |
| `full` | От текущего состояния до ближайшего чекпоинта |

## Checkpoints

1. **После `gate`** — Вадим одобряет размещение, URL и угол. Родитель FitXpress-вертикалей — главная
   страница, URL вида `/for-{vertical}/`; у Mobile Tailor родитель свой, `/mobile-tailor/`. Уровня
   `/fitxpress/` не существует — он 301-ит на главную.
2. **После `judge`** — Вадим одобряет финальную страницу, мету и итоговый счёт вместе. Публикация
   ниже 85 без явного флага запрещена.

## Артефакты

`workspace/pages/{slug}/` — `page.md`, `fact-sheet.md`, `gate-reports.md`, `judge-round-N.json`,
`README.md`, `TODO.md`, `open-items.md`, `log.md`, `assets/`. Frontmatter обязателен:
`product`, `type`, `vertical`, `status`.

## Что нужно до старта

- Use-case файл `brand-assets/product-info/use-cases/{fx|mt}-{vertical}.md` — без него G-I не проходит
- Кейсы этой вертикали в `brand-assets/product-info/case-studies/` — минимум 2, иначе страницы нет
  (см. таблицу покрытия в `references/page-types.md`: сегодня порог проходят только вертикали
  Mobile Tailor)
- Все числа — только из `proof-points.md`. Нет числа — идёт в open items, а не на страницу
