---
description: Запускает новую outbound-кампанию или продолжает существующую с указанного шага
argument-hint: "[stage] [campaign-slug]"
model: sonnet
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

## Сначала — где кампания стоит

```bash
python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/outbound_pack.py next --campaign <slug>
python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/outbound_pack.py next --find "лена еракуліс"
```

Одна команда вместо десятка `ls` и `cat`: стадия, что блокирует, сколько людей на каждом
шаге, не уехал ли скоуп гипотезы, и точные следующие команды. `--find` понимает, как Вадим
называет кампанию: «Лена» это профиль `olena`, «еракуліс» это `erakulis` в слаге.
`STATUS.md` кампании читай только если `next` не ответил на вопрос.

## Stages — кто что делает

Ты координатор: ставишь стадию, гонишь скрипты, запускаешь агента там, где нужно
суждение. Текстов не пишешь и людей не оцениваешь.

| Stage | Скрипты ДО агента | Агент | Скрипты ПОСЛЕ |
|---|---|---|---|
| `hypothesis` | — | `hypothesis-generator` (opus) | — |
| `research` | `hypothesis-gate --stamp`, `search-health.py` | `company-researcher` | `web-verify.py`, `validate-companies`, затем люди: `outbound_pack.py sales-nav-query` (Sales Navigator) **или** `apollo-pull.py search` → `enrich` (Apollo) |
| `extract` | `extract-people --dry-run`, прочитай unmatched, потом без `--dry-run` | **нет** | — |
| `validate` | `outbound-registry.py check`, `outbound_pack.py compact`, `outbound_pack.py card --for validate` | `icp-validator` | (агент сам: `apply-decisions`, `skipped`) |
| расширение списка | — | **нет** | `outbound_pack.py promote --names "…"` |
| `messages` | `outbound_pack.py card --for messages`, `outbound_pack.py profiles` | `message-sequencer`, **по одному на пачку, параллельно** | `outbound_pack.py check-messages` по всей кампании |
| `import` | — | **нет** | `outbound_pack.py build-import`, `outbound-registry.py record` |
| `responses` | `closely-pull.py pull` (если файл старше 24 ч), `check-responses` | `response-classifier` | `check-classified` |
| `analyze` | — | `campaign-analyzer` (opus) | — |

`extract` и `import` — это код. Агентов `people-extractor` и `closelyhq-importer` запускай
только разбираться, почему команда упала.

### Шаг 3: откуда люди — Sales Navigator или Apollo

Оба источника пишут в `sales-nav-raw/`, и `extract-people` читает их вместе. Можно один,
можно оба: человек, который есть в обоих, остаётся строкой Sales Navigator (в ней Bio и
Skills), дубль по LinkedIn URL отбрасывается.

- **Sales Navigator** (как раньше): `outbound_pack.py sales-nav-query`, Вадим выгружает CSV
  в `sales-nav-raw/`. Список, который Вадим принёс сам, — всегда этот путь.
- **Apollo** (с 2026-10-01, использование для LinkedIn-аутрича согласовано Вадимом с Apollo):

  ```bash
  python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/apollo-pull.py search --campaign <slug>
  python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/apollo-pull.py enrich --campaign <slug> --max-credits N
  ```

  `search` бесплатный: ищет по домену каждой компании из шортлиста и по блоку ```titles
  гипотезы, пишет `apollo-candidates.csv` и печатает, сколько кредитов уйдёт (1 на
  человека). `enrich` тратит кредиты, не выходит за `--max-credits` и пишет
  `sales-nav-raw/apollo-<дата>.csv` в колонках Sales Navigator. Журнал — `apollo-log.md`.
  Если кредитов больше 100 — назови Вадиму число до `enrich`. `--all-functions` снимает
  фильтр по должностям (как выгрузка по компании) — только по просьбе Вадима: выгрузка по
  компании стоила двух кампаний (см. hypothesis-generator).

**Ловушка Apollo:** фильтр по домену ловит и бывших сотрудников. Скрипт отсекает их дважды
(по названию текущей компании до обогащения и по домену после), отсеянные — в
`apollo-log.md`. Ключ — `APOLLO_API_KEY` в `~/.hermes/.env`, scoped (поиск + bulk_match),
не master.

### Авто-QC — opus `quality-controller`, после трёх стадий

Решение Вадима 2026-09-28: для outbound QC остаётся на opus. После `hypothesis`,
`validate` и `messages`, **до** пинга Вадиму:

```bash
python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/outbound_pack.py qc-prompt \
    --campaign <slug> --stage hypothesis|validate|messages
```

Команда печатает промпт для `quality-controller`: что оценивать и что агенту было дано
(карточка и compact-список, а не гипотеза и сырой экспорт). Передай его дословно. Для
`messages` — один QC на кампанию, после `check-messages` по всем пачкам.

После QC допиши в отчёт `coordinator_review` (`agreement` + `top_issue`, CLAUDE.md §14), а
в пинг Вадиму — одну строку: `QC: 17/20 ✅ good. Top: …`. **QC ниже 12 → дальше не идёшь**,
Вадиму уходит red flag с предложением перегенерировать.

### `messages`: пачки

`outbound_pack.py profiles` сам делит список на пачки (большая группа — своя пачка,
мелкие вместе, до 35 человек) и печатает план. На каждую пачку — один
`message-sequencer` в фоне, все одним сообщением. Промпт агенту — четыре строки:

```
Step 5 (messages). Campaign: {slug}. Batch: {batch}.
Read workspace/outbound/campaigns/{slug}/card-messages.md and
workspace/outbound/campaigns/{slug}/messages/_profiles-{batch}.md. Nothing else.
Write messages/_batch-{batch}.md, run split-messages until exit 0, then stop.
```

Правила кампании в промпт не переписывай: они в карточке, дословно из гипотезы. Когда
все пачки вернулись, сам прогони `check-messages` по всей кампании и верь ему, а не
отчётам агентов: 2026-09-28 пачка Welltech отчиталась о 34 людях из 35.

### Расширение списка после чекпоинта

Вадим называет людей или пулы → `promote`, без агента. Если расширение меняет персону
или кеп, сначала допиши датированный блок `Vadim's decisions YYYY-MM-DD` в
`hypothesis.md` (и `cap_per_group` во frontmatter), потом `hypothesis-gate --stamp`,
потом `promote`. Прошлую версию списка `promote` сохраняет сам.

## Одна стадия — одна сессия

Состояние между стадиями лежит на диске: `STATUS.md`, файлы кампании и вывод `next`.
Контекст сессии его не несёт и не должен.

- **Headless** (`mvb-run.py outbound`): одна job — одна стадия, до чекпоинта Вадима.
- **Интерактивно**: после чекпоинта предложи Вадиму `/clear` и продолжай с
  `outbound_pack.py next`.

Замер 2026-09-28: координатор одной длинной сессии на самой большой модели — 18M токенов
и 57% счёта за кампанию. Он 105 раз перечитал контекст с медианой 171K, потому что в нём
лежали все предыдущие стадии.

## Что не тащить в контекст

- Скрипты `outbound_pack.py` печатают до ~2 КБ и пишут полный отчёт в файл. Читай
  файл, только если строки в выводе не хватило.
- Не `cat` и не `Read` целиком: `hypothesis.md`, `people-*.csv`, сырой экспорт,
  `messages/*.md`. Нужна цифра → её считает скрипт.
- Отчёт агента — это его слова. Проверяемое проверяй командой.

## Алгоритм

1. Разобрать `$ARGUMENTS` в `stage` + `campaign-slug` по правилам выше.
1a. `outbound_pack.py next --campaign <slug>`: стадия и блокеры. Запрошенная стадия не
   та, что следующая по `next` → скажи об этом Вадиму до запуска.
2. Если `campaign-slug` не указан и `stage = hypothesis` — создать новую кампанию: slug = `{YYYY-MM-DD}-new`, попросить Вадима задать direction (или создать без направления).
3. Если `campaign-slug` указан — найти `workspace/outbound/campaigns/{campaign-slug}/`. Нет папки → СТОП, перечислить существующие.
4. Прогнать гейт этой стадии из таблицы ниже. Красный гейт = стадия не запускается.
5. Прогнать скрипты стадии и запустить агента, если он в таблице Stages есть.
4. После завершения — Telegram-нотификация со статусом и предложением следующего шага.

## Механические гейты (код, не суждение агента)

Каждый гейт — exit code. Красный гейт означает «шаг не закончен», а не «предупреждение».

| Stage | Гейт перед выходом из шага |
|---|---|
| `hypothesis` | — (апрув Вадима) |
| `research` | `outbound-pipeline.py hypothesis-gate --campaign X --stamp` (в начале), затем `search-health.py`, `web-verify.py verify`, `outbound-pipeline.py validate-companies --campaign X --write-routed` |
| `extract` | `outbound-pipeline.py extract-people --campaign X --dry-run`, потом без `--dry-run` |
| `validate` | `outbound-registry.py check` до агента; `outbound_pack.py apply-decisions` после (каждому человеку ровно одно решение) |
| `messages` | `outbound_pack.py check-messages --campaign X` (полнота, лимиты, подпись, запреты, детектор, повторы) |
| `import` | `outbound_pack.py build-import --campaign X` (внутри: `check-messages`, `check-import` по каждому файлу, `cap_per_group`) |
| `responses` | `closely-pull.py pull --campaign X` (**пропусти, если `responses-raw.csv` моложе 24 ч**: его тянет ночной cron, а каждый pull выбивает Вадима из app.closelyhq.com), затем `outbound-pipeline.py check-responses --campaign X` |
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

**С 2026-09-21 шаг 8 идёт сам, без Вадима.** `scripts/outbound-responses-daily.py night`
(та же cron-строка 23:30 UTC, сразу после `closely-pull.py pull-all`) коммитит и пушит
файлы ответов и ставит `/outbound responses <slug>` на каждую кампанию с
неклассифицированными ответами. `morning` (06:00 UTC) коммитит результат, если
`check-classified` зелёный, и присылает Вадиму в Telegram отчёт: новые ответы по кампаниям
и аккаунтам, с категорией классификатора. Если ты запущен так, делай только шаг
`responses`: классифицируй весь `responses-raw.csv`, после записи прогони
`check-classified`. **Не коммить и не пуш сам** — это делает скрипт, и только после гейта.

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
