---
description: Запускает agent-improver — анализирует QC отчёты и coordinator notes за период, формирует proposals на улучшение промптов агентов. Не применяет автоматически — нужен апрув Вадима.
argument-hint: "[period_days=30] [target_agent (optional)]"
---

Запусти `agent-improver`.

## Параметры

- `$1` — period_days (default 30)
- `$2` — target_agent (optional, e.g., `message-sequencer`). Если не указан — анализирует всех.

## Что произойдёт

1. agent-improver соберёт все QC отчёты + coordinator notes за период
2. Найдёт паттерны (recurring issues) у каждого агента
3. Для агентов с avg < 16 ИЛИ recurring issues 3+ создаст proposal:
   - Stats (avg score, trend)
   - Recurring issues (с примерами)
   - Root cause hypothesis
   - Конкретный diff для промпта
   - Validation plan
4. Создаст summary digest всей системы
5. Уведомит Вадима через notify

## Apply workflow

После генерации proposals:
1. Вадим открывает `workspace/_quality/improvements/{date}-{agent}-proposal.md`
2. Читает diff и rationale
3. Если согласен — применяет diff вручную (или через `git apply`)
4. Меняет `status: pending_approval` → `status: applied` в frontmatter
5. Наблюдает 5 следующих артефактов от агента — Category-X должна вырасти

## Recommendation

Запускать раз в 2 недели или после каждых 20 артефактов прошедших QC. Чаще — недостаточно данных. Реже — паттерны накапливаются и сложнее разделять effects.
