# Outbound Exclusion Registry

> **Один писатель: `scripts/outbound-registry.py`.** JSON в этой папке руками не правит ни
> человек, ни агент. Обновлено 2026-08-23.
>
> Что было не так до этого: всё описанное ниже было специфицировано и не реализовано. Ни один
> из восьми `mvb-outbound` агентов не ссылался на `exclusions/`; `company-researcher` и
> `campaign-analyzer` ссылались на `workspace/outbound/exclusions.md` — плоский файл, которого
> никогда не существовало, поэтому каждое чтение молча возвращало пусто, а каждая запись уходила
> в никуда. Десять кампаний прошли, и реестры по-прежнему показывали `excluded_people: 0`.
> Четыре промпта, правящие один и тот же JSON, — это и есть причина.
>
> ```bash
> python3 scripts/outbound-registry.py status                                   # где какая кампания
> python3 scripts/outbound-registry.py check    --profile P --input people.csv  # кого исключить
> python3 scripts/outbound-registry.py record   --campaign S [--profile P]      # после импорта
> python3 scripts/outbound-registry.py reply    --campaign S                    # после разбора ответов
> python3 scripts/outbound-registry.py backfill --dry-run                       # исторические кампании
> ```
>
> Все пишущие команды поддерживают `--dry-run`. Скрипт идемпотентен.

Система запоминает компании и людей по которым уже запускались рассылки с каждого из 5 профилей. Цель — **никогда не отправлять одному и тому же человеку дважды с одного профиля**, и не рассылать на одну компанию с нескольких профилей одновременно.

## Профили и рынки

Рынки взяты из `brand-assets/social-profiles-config.md`. Каждый профиль рассылает **только по своему гео**.

| profile | Owner | Рынок |
|---------|-------|-------|
| `katerina` | Katerina Galich (CEO) | UK |
| `nick` | Nick Omelchak (BD) | USA |
| `olena` | Olena Kudryavtseva (BD) | Europe / EU |
| `katya` | Katya Boychuk (BD) | Israel |
| `vadim` | Vadim Bilan (Marketing) | Australia |

## Структура

```
workspace/outbound/exclusions/
├── README.md                         (этот файл)
├── katerina-registry.json            профиль — Katerina (UK)
├── nick-registry.json                профиль — Nick (USA)
├── olena-registry.json               профиль — Olena (EU)
├── katya-registry.json               профиль — Katya (Israel)
├── vadim-registry.json               профиль — Vadim (Australia)
└── global-company-registry.json      cross-profile: какие компании покрыты каким профилем
```

## Формат registry (per-profile)

```json
{
  "profile": "vadim",
  "last_updated": "2026-04-30",
  "campaigns": [
    {
      "campaign_id": "2026-04-15-fx-insurance-uw",
      "product": "fitxpress",
      "date_started": "2026-04-15",
      "companies": ["prudential", "metlife", "guardian-life"],
      "people": [
        {
          "linkedin_url": "https://linkedin.com/in/sarah-jones-123",
          "name": "Sarah Jones",
          "company": "prudential",
          "title": "VP Underwriting",
          "status": "sent",
          "reply": "interested"
        }
      ]
    }
  ],
  "excluded_companies": ["prudential", "metlife", "guardian-life"],
  "excluded_people_urls": ["https://linkedin.com/in/sarah-jones-123"]
}
```

## Формат global-company-registry

```json
{
  "last_updated": "2026-04-30",
  "companies": {
    "prudential": {
      "covered_by_profile": "vadim",
      "campaign_id": "2026-04-15-fx-insurance-uw",
      "product": "fitxpress",
      "date": "2026-04-15",
      "status": "active"
    },
    "safariland": {
      "covered_by_profile": null,
      "status": "existing_customer_excluded"
    }
  }
}
```

## Как агенты используют

### hypothesis-generator
Перед генерацией гипотезы — прочитай global-company-registry. Не предлагай вертикали где все ключевые компании уже покрыты.

### company-researcher
После составления списка — проверь каждую компанию через global-company-registry:
- Если `status: active` и `covered_by_profile != текущий` → ИСКЛЮЧИТЬ (не рассылать с двух профилей)
- Если `status: existing_customer_excluded` → ИСКЛЮЧИТЬ (это наш клиент)
- Если не в registry → ОК

### icp-validator
Перед валидацией (Шаг 0):
```bash
python3 scripts/outbound-registry.py check --profile {profile} \
  --input .../people-raw.csv --output .../people-checked.csv
```
Строки с `exclusion_flag=EXCLUDE` получают `decision: FAIL` и `reason` из `exclusion_reason`.
**`linkedin_url` обязан быть в `people-validated.csv`** — раньше `icp-validator` его терял, из-за
чего проверка по людям на этом этапе была невозможна, а importer восстанавливал URL
сопоставлением по имени и компании.

### closelyhq-importer
После формирования CSV:
```bash
python3 scripts/outbound-registry.py record --campaign {slug} --profile {profile}
```
Скрипт сам добавляет компании в global-company-registry, людей в per-profile registry и
обновляет `last_updated`. Он читает `closelyhq-import*.csv` (файл, который реально уходит в
closely.io), дедуплицирует по канонизированному person-URL и отказывается записывать кампанию,
у которой в CSV нет ни одного URL.

### campaign-analyzer
После анализа:
```bash
python3 scripts/outbound-registry.py reply --campaign {slug} --profile {profile}
```
Переносит категорию из `responses-classified.csv` в поле `reply`. Без этого правило «через 6
месяцев компания освобождается, если `reply` = no_reply» неприменимо: освобождать нечего.

## Правила cross-profile

1. **Одна компания = один профиль.** Если Prudential уже получает от Vadim → Katerina не рассылает по Prudential.
2. **Исключение:** через 6 месяцев после последней рассылки (если reply = no_reply) компания «освобождается» и может быть покрыта другим профилем.
3. **Existing customers** (Safariland, Burlington, UK Meds, Yazen, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Healthyr) — всегда excluded из outbound. Обновляй этот список если появляются новые клиенты.

## Workflow для Вадима при запуске нового outbound

1. Orchestrator спрашивает: «С какого профиля рассылка?» (katerina / nick / olena / katya / vadim)
2. Context Pack Builder включает exclusions для этого профиля в context pack
3. Все агенты outbound трека используют exclusions
4. После формирования CSV — `closelyhq-importer` запускает `outbound-registry.py record`, и компании с людьми попадают в реестр
