# Outbound Exclusion Registry

Система запоминает компании и людей по которым уже запускались рассылки с каждого из 4 профилей. Цель — **никогда не отправлять одному и тому же человеку дважды с одного профиля**, и не рассылать на одну компанию с нескольких профилей одновременно.

## Структура

```
workspace/outbound/exclusions/
├── README.md                         (этот файл)
├── vadim-registry.json               профиль 1 — Vadim
├── katerina-registry.json            профиль 2 — Katerina
├── whitney-registry.json             профиль 3 — Whitney
├── profile4-registry.json            профиль 4 — [TBD]
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
Перед валидацией — прочитай per-profile registry. Каждого человека проверь по `excluded_people_urls`:
- Если URL в exclusions → автоматический FAIL с причиной «already contacted from {profile}»

### closelyhq-importer
После формирования CSV — обнови registry:
1. Добавь все новые компании в global-company-registry
2. Добавь всех людей в per-profile registry
3. Обнови `last_updated`

### campaign-analyzer
После анализа — обнови `reply` поле в per-profile registry для каждого контакта.

## Правила cross-profile

1. **Одна компания = один профиль.** Если Prudential уже получает от Vadim → Katerina не рассылает по Prudential.
2. **Исключение:** через 6 месяцев после последней рассылки (если reply = no_reply) компания «освобождается» и может быть покрыта другим профилем.
3. **Existing customers** (Safariland, Burlington, UK Meds, Yazen, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Healthyr) — всегда excluded из outbound. Обновляй этот список если появляются новые клиенты.

## Workflow для Вадима при запуске нового outbound

1. Orchestrator спрашивает: «С какого профиля рассылка?» (vadim / katerina / whitney / profile4)
2. Context Pack Builder включает exclusions для этого профиля в context pack
3. Все агенты outbound трека используют exclusions
4. После запуска кампании — closelyhq-importer автоматически обновляет registry
