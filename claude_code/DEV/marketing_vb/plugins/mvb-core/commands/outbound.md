---
description: Запускает новую outbound-кампанию или продолжает существующую с указанного шага
argument-hint: "[stage] [campaign-slug]"
---

Управляет outbound-флоу. Аргументы приходят целиком в `$ARGUMENTS`: **`$ARGUMENTS`**

## Разбор аргументов — читай это первым

`$ARGUMENTS` — строка вида `<stage> [campaign-slug]`. Разбирай её сам:

- **stage** — первое слово, и оно обязано быть одним из списка Stages ниже.
- **campaign-slug** — второе слово, если есть. Слаг всегда начинается с даты
  (`YYYY-MM-DD-...`), так что отличить его от stage невозможно спутать.
- Если первое слово не из списка Stages, а похоже на слаг — **СТОП**, спроси Вадима,
  какую стадию он имел в виду. Не угадывай.

**Почему разбор явный, а не позиционный.** Раньше stage и slug брались позиционными
подстановками (первый и второй аргумент). 2026-09-02 при программном вызове
`responses 2026-08-07-us-digital-fitness` первая подстановка получила слаг кампании, а
вторая не подставилась вовсе — команда запустила бы стадию с именем
`2026-08-07-us-digital-fitness`, которой не существует, потеряв при этом слаг.

Набранный вручную `/outbound responses <slug>` работает нормально, и остальные команды
репозитория (`post-one-profile`, `post-from-article`) на позиционных живут годами. Сдвиг
проявился именно на программном вызове. Разбор `$ARGUMENTS` целиком одинаково надёжен на
обоих путях, поэтому здесь он такой — но это НЕ повод править те команды, которые
работают.

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

1. Разобрать `$ARGUMENTS` в `stage` + `campaign-slug` по правилам выше.
2. Если `campaign-slug` не указан и `stage = hypothesis` — создать новую кампанию: slug = `{YYYY-MM-DD}-new`, попросить Вадима задать direction (или создать без направления).
3. Если `campaign-slug` указан — найти `workspace/outbound/campaigns/{campaign-slug}/`. Нет папки → СТОП, перечислить существующие.
4. Прогнать гейт этой стадии из таблицы ниже. Красный гейт = стадия не запускается.
5. Запустить субагент, соответствующий `stage`.
4. После завершения — Telegram-нотификация со статусом и предложением следующего шага.

## Механические гейты (код, не суждение агента)

Каждый гейт — exit code. Красный гейт означает «шаг не закончен», а не «предупреждение».

| Stage | Гейт перед выходом из шага |
|---|---|
| `hypothesis` | — (апрув Вадима) |
| `research` | `outbound-pipeline.py hypothesis-gate --campaign X --stamp` (в начале), затем `search-health.py`, `web-verify.py verify`, `outbound-pipeline.py validate-companies --campaign X --write-routed` |
| `extract` | `outbound-pipeline.py extract-people --campaign X --dry-run`, потом без `--dry-run` |
| `validate` | `outbound-registry.py check --profile P --input people-raw.csv` (шаг 0 icp-validator) |
| `messages` | — |
| `import` | `outbound-pipeline.py check-import --campaign X` |
| `responses` | `closely-pull.py pull --campaign X`, затем `outbound-pipeline.py check-responses --campaign X` |
| `analyze` | — (нужны `responses-classified.csv` + `metrics-final.json`) |

Скрипты лежат в `/home/vadim_prod/3dlook-marketing/marketing_vb/scripts/`, резолвят пути
от `__file__` и работают из любого cwd — вызывай абсолютным путём, без `cd &&`.

**`research` не запускать, если `search-health.py` вернул exit 1.** 2026-09-02 поиск
ослеп в 03:50 и оставался слепым до 05:08 (все апстрим-движки SearXNG в suspend по
rate-limit и CAPTCHA), и прогон догенерировал 26 непроверяемых компаний.

**Шаги 8-9 не запускались ни разу** — 6 из 11 кампаний ждали ручного экспорта
`responses-raw.csv` при 1276 отправленных сообщениях. С 2026-09-02 файл тянется кодом:
`scripts/closely-pull.py pull --campaign X` (приватный API их веб-приложения, путь B в
`workspace/outbound/CLOSELY-CONNECTIVITY.md`; нужны `CLOSELY_TOKEN` /
`CLOSELY_REFRESH_TOKEN` в `~/.hermes/.env`). Первый запуск на кампании — всегда
`probe`, потом `pull --max-conversations 5 --dry-run`, и только потом полный прогон.
Раз в неделю (пн 09:05 Киева) `outbound-pipeline.py remind --notify` присылает Вадиму
список блокеров.

**Если `people-validated.csv` без `first_name` / `linkedin_url`** — не переписывай его
руками: `outbound-pipeline.py fix-validated --campaign X` вернёт identity из
`people-raw.csv`. Именно эта потеря колонок положила `2026-07-16-au-telehealth` на 7 недель.

**`import` не отдавать Вадиму, если `check-import` вернул exit 1.**
`2026-07-16-au-telehealth` — 253 строки с пустыми `first_name` / `last_name` /
`linkedin_url`, семь недель в статусе «imported» с нулём отправленных.

## Чекпоинты Вадима (НЕ запускаешь автоматически)

- После `hypothesis` → Вадим читает гипотезу
- После `validate` → **критично, ждать апрува** (это первый чекпоинт менеджера)
- После `messages` → ждать апрува (просмотр сэмпла перед импортом)
- После `analyze` → **второй чекпоинт менеджера**, выводы для следующей кампании

## Если шаги не сделаны

Если запросили `validate`, а `people-raw.csv` нет → STOP и список пропущенных шагов.
