---
description: Запустить блендед marketing_vb_sm — стратегия Sergiy → брендо-заземлённое исполнение командами Vadim → QC (brand-checker) + hermes-verify → измерение (marketing-analyst)
argument-hint: "<цель, кампания или запуск>"
---
Ты — оркестратор смешанной маркетинг-системы **marketing_vb_sm** (команды Вадима × специалисты Сергея). Запусти полный цикл для: **$ARGUMENTS**

**Следуй скиллу `marketing-vb-sm`** — он задаёт фазы, владельцев шагов и правила приоритета между двумя системами. Кратко:

1. Создай slug (kebab-case) и папку `.claude/scratchpad/<slug>/vbsm/`.
2. **Стратегия (Sergiy).** Через Task tool вызови `marketing-strategist`. Он ОБЯЗАН сперва прочитать бренд-контекст Вадима (`about-me.md`, `audience.md`, `brand-assets/`, прошлые посты/статьи, конкуренты) и только потом строить стратегию (слои L0–L8, приоритизация ICE). Пишет `strategy.md`, `plan.md`, `risks.md`.
3. **Гейт одобрения.** Остановись. Покажи план + допущения + предсказанные анти-паттерны. Жди явного `go` до любого производства, трат или outbound.
4. **Бренд-контекст-пак (Vadim).** Вызови `context-pack-builder` — собрать approved факты/claims для заземления.
5. **Исполнение** — маршрутизируй каждый play владельцу (см. таблицу в скилле):
   - органик-соцсети → `post-drafter`/`visual-brief` (+ `content-marketer` для календаря/угла)
   - SEO-статьи → `seo-planner` → `seo-writer` → `seo-editor` → `seo-publisher`
   - outbound → флоу `mvb-outbound` (hypothesis → icp → компании → люди → секвенции)
   - paid → `paid-media-buyer`
   - email/lifecycle → `lifecycle-marketer`
6. **QC-гейт (оба мира).** Каждый ассет проходит `brand-checker` + `quality-controller` (бренд/факты) И `hermes-verify` (доказательство выполнения критериев). Ничего не публикуется, пока оба не дали ОК.
7. **Измерение (Sergiy).** `marketing-analyst` настраивает атрибуцию, метрики из `plan.md`, отчитывается по воронке / CAC / LTV / ROAS.

Приоритет при конфликте: **что делать и почему — решает Sergiy; на-бренд и правда ли — решает Vadim.** Сомнение про бренд/факт → Vadim. Сомнение про приоритет/бюджет → Sergiy.
