---
description: Запускает новую outbound-кампанию или продолжает существующую с указанного шага
argument-hint: "[stage] [campaign-slug]"
---

Управляет outbound-флоу для кампании `$2` (или новой, если не указано).

## Stages

- `hypothesis` — запустить hypothesis-generator
- `research` — запустить company-researcher (требует approved hypothesis)
- `extract` — запустить people-extractor (требует sales-nav-raw/ загружен Вадимом)
- `validate` — запустить icp-validator (требует extract done)
- `messages` — запустить message-sequencer (требует approved validation)
- `import` — запустить closelyhq-importer (требует approved messages)
- `responses` — запустить response-classifier (требует responses-raw.csv загружен)
- `analyze` — запустить campaign-analyzer (после кампании, требует metrics-final)

## Алгоритм

1. Если `$2` (campaign-slug) не указан и `$1 = hypothesis` — создать новую кампанию: slug = `{YYYY-MM-DD}-new`, попросить Вадима задать direction (или создать без направления).
2. Если `$2` указан — найти `workspace/outbound/campaigns/{$2}/`.
3. Запустить субагент соответствующий `$1`.
4. После завершения — Telegram-нотификация со статусом и предложением следующего шага.

## Чекпоинты Вадима (НЕ запускаешь автоматически)

- После `hypothesis` → Вадим читает гипотезу
- После `validate` → **критично, ждать апрува** (это первый чекпоинт менеджера)
- После `messages` → ждать апрува (просмотр сэмпла перед импортом)
- После `analyze` → **второй чекпоинт менеджера**, выводы для следующей кампании

## Если шаги не сделаны

Если запросили `validate`, а `people-raw.csv` нет → STOP и список пропущенных шагов.
