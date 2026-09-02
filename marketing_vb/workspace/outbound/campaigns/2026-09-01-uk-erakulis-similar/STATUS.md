# STATUS — 2026-09-01-uk-erakulis-similar

**Блокер: Вадим выбирает гипотезу. Пока не выбрана — шаг 3 (Sales Navigator) не запускать.**

Обновлено 2026-09-02, по разбору лога Telegram за это утро.

---

## Что случилось

В 03:23 в Telegram прилетело «Повторити спробу і додати епки з фізичними вправами, фітнес
епки та нутрішн епки». Прогон расширил список, но `hypothesis.md` остался прежним —
«Private GLP-1 / weight-loss telehealth, England-HQ, cash-pay». Дальше два независимых
отказа наложились друг на друга:

1. **Поиск ослеп в 03:50 и оставался слепым до 05:08.** SearXNG отдавал по 10 результатов
   до `03:50:06`, а с `03:50:10` — ноль на все 19 запросов, включая контрольный
   `weather London`, который агент попробовал сам. Причина (найдена 2026-09-02 в
   `unresponsive_engines`): все апстрим-движки ушли в suspend — `brave: too many requests`,
   `duckduckgo: CAPTCHA`, `google cse: too many requests`, `startpage: CAPTCHA`. SearXNG в
   таком состоянии отвечает `200 OK` с пустым списком, поэтому отказ выглядел как «в
   подсегменте ничего нет».
2. **`web_extract` недоступен в принципе** — SearXNG search-only, платный extract-бэкенд не
   настроен. Проверить ни один сайт было нечем.

Итог: 26 компаний, у всех `verification=unverified-desk`, 10 из них `Exclude`, 8 US-HQ,
1 Sweden, 1 Scotland. Список, собранный по памяти модели, в формате исследования.

## Что сделано 2026-09-02

- `companies.csv`, `companies.md` и их верификация убраны в `_quarantine-2026-09-02/`.
  Не удалены — это запись о том, что было заявлено. Из-за этого трекер честно показывает
  кампанию на стадии `1 · hypothesis`, а не на «2 · companies».
- Оба списка прогнаны через новый `scripts/web-verify.py` (живой HTTP, браузерный UA,
  cookie-jar — вендорский ключ не нужен):

| Список | Строк | `verified-live` | `blocked` | `dead` | без сайта |
|---|---|---|---|---|---|
| `_quarantine-2026-09-02/companies-verified.csv` (расширенный) | 26 | 19 | 5 | 1 | 1 |
| `companies-glp1-telehealth-verified.csv` (по гипотезе) | 30 | 28 | 2 | 0 | 0 |

  `blocked` — сайт не открывается с этого VPS ни curl, ни живым headless Chrome (IP
  датацентра). Ретраить браузером бессмысленно, нужен человек или residential proxy:
  расширенный список — Cambridge Weight Plan, Lifesum, The Protein Works, Noom UK,
  Anytime Fitness UK; GLP-1 список — Voy, Pharmacy2U.
  `dead` в расширенном — Care/of: `takecareof.com` не резолвится (проверено и браузером,
  домен мёртв), а в CSV он стоял как живая компания со статусом `Exclude`.

## Решение, которое нужно от Вадима

**Вариант A — остаться на утверждённой гипотезе (быстрый).**
`companies-glp1-telehealth-verified.csv`: 30 компаний, 28 проверены живыми, гео совпадает
с профилем `katerina` (UK). `hypothesis.md` править не нужно. Дальше — шаг 3.

**Вариант B — расширить на fitness / nutrition апки (как просили в 03:23).**
Тогда сначала переписывается `hypothesis.md`: sub-segment, use case, buyer persona и
anti-cases сейчас все описывают GLP-1 телехелс и отправят `icp-validator` не туда. После
переапрува гипотезы список собирается заново — расширенный из карантина взять нельзя, он
собран во время слепого поиска. И 10 не-UK строк в нём принадлежат другим профилям:
Lose It! / MyFitnessPal / Noom → `nick`, Lifesum → `olena`; им нужны свои кампании.

**Отдельно:** Bupa Global и Aetna UK из карантинного списка — реальный ICP по сегменту
health plans, но это другой buyer и другое сообщение (underwriting / wellness
verification). Своя гипотеза, не эта.

## Перед шагом 3 — обязательное

```bash
python3 scripts/search-health.py          # exit 1 = поиск слепой, ничего не запускать
python3 scripts/web-verify.py verify --campaign 2026-09-01-uk-erakulis-similar \
        --in <выбранный список>.csv
```
