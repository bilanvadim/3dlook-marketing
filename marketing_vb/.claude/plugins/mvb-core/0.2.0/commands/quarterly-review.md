---
description: Запускает квартальный анализ соцсетей и формирует план на следующий квартал
---

Quarterly review для соцсетей.

## Шаги

1. Проверь, есть ли `workspace/social/analytics/Q{N}-raw/` с выгрузками от Вадима. Если нет — STOP, попроси.
2. Запусти `social-analytics` → дождись отчёта.
3. **Telegram-нотификация Вадиму** с TL;DR из отчёта. Жди апрува learnings.
4. После апрува — запусти `quarterly-strategist` с указанием на новый отчёт + previous strategies.
5. Telegram: «Q{N+1} план готов, на ревью».

## Что должен показать Вадиму бот

В обоих чекпоинтах (после analytics и после strategy) — кнопки Approve / Edit / Reject.
