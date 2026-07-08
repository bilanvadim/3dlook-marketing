---
description: Запустить полный цикл разработки фичи через команду агентов Fullstack agents (architect → план → делегирование)
argument-hint: "<описание фичи>"
---
Ты — оркестратор Fullstack agents. Запусти полный цикл для фичи/проекта: **$ARGUMENTS**

Следуй скиллу `project-planning`.
1. Создай slug (kebab-case) и папку `.claude/scratchpad/<slug>/`.
2. **Интервью.** Проведи адаптивное многослойное интервью (слои L0–L11 из скилла), задавая мне уточняющие вопросы небольшими порциями там, где есть риск/неоднозначность. Явно проговаривай допущения и предсказывай анти-паттерны. Глубина — по масштабу.
3. **Синтез.** Вызови `product-architect` через Task tool (описание + ответы интервью + путь к scratchpad). Он пишет `spec.md`, `architecture.md`, `nfr.md`, `risks.md` и **детальный `plan.md` по схеме project-planning** (каждый шаг: phase/agent/tags/description/acceptance/quality_bar/depends_on/risk/files).
4. Прочитай `plan.md`. Покажи мне сводку: фича, ключевые решения, первые 3–5 шагов с агентами, топ-риски.
5. **ЖЁСТКИЙ гейт одобрения.** ОСТАНОВИСЬ. Не пиши код, пока я явно не одобрю (`go`). Я могу уточнять: «edit step N: …» / «show step N».

После одобрения — делегируй шаги по `scratchpad-protocol`, соблюдая `depends_on` и лимиты параллелизма из CLAUDE.md. После КАЖДОГО шага — `verification-protocol` (его `acceptance`+`tags`+`quality_bar` ведут ревью и runtime-гейт). Перед релизом — `security-auditor`.
