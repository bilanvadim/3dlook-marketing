# Brand Assets — 3DLOOK

Эта папка — единственный источник правды по бренду и продукту для всех агентов.

## Структура (текущая)

```
brand-assets/
├── README.md                       (этот файл)
├── brand-guidelines/               # Официальный гайдбук [НУЖНО ЗАЛИТЬ]
├── logos/                          # Логотипы [НУЖНО ЗАЛИТЬ]
├── color-palette/
│   └── colors.md                   # ✓ Готов (Vadim confirm точных HEX)
├── fonts/
│   └── fonts.md                    # ✓ Готов (Inter, Vadim confirm)
├── past-posts/                     # [НУЖНО ЗАЛИТЬ Vadim]
│   ├── README.md                   # ✓ Гайд что класть
│   └── _figma-exports/             # Banners + website pages (НУЖНО)
├── product-info/                   # ✓ ПОЛНОСТЬЮ ЗАПОЛНЕНО ПОД 3DLOOK
│   ├── INDEX.md
│   ├── overview.md
│   ├── how-it-works.md
│   ├── proof-points.md             ← все цифры со ссылками
│   ├── icp-detail.md               ← ICP по обоим продуктам
│   ├── pricing.md
│   ├── competitors.md              ← Prism Labs, Bodygram, Size Stream
│   ├── compliance.md               ← HIPAA, GDPR, encryption
│   ├── tech-spec.md
│   ├── faq.md                      ← Objection handling
│   ├── messaging.md                ← Hero messages + banned words
│   ├── use-cases/  (12 файлов)
│   │   ├── fx-telehealth-weight-loss.md
│   │   ├── fx-online-pharmacy-bmi.md
│   │   ├── fx-insurance-underwriting.md
│   │   ├── fx-wellness-rewards.md
│   │   ├── fx-bariatric-pre-auth.md
│   │   ├── fx-occupational-health.md
│   │   ├── fx-clinical-trials.md
│   │   ├── fx-digital-fitness.md
│   │   ├── mt-made-to-measure.md
│   │   ├── mt-on-demand-manufacturing.md
│   │   ├── mt-uniform-fitting.md
│   │   └── mt-wrist-measurement.md
│   └── case-studies/  (6 файлов)
│       ├── safariland.md
│       ├── burlington-medical.md
│       ├── uk-meds.md
│       ├── yazen.md
│       ├── jims-formal-wear.md
│       └── generation-tux.md
└── competitors/
    └── list.md                     # ✓ Готов (нужны screenshots)
```

## Что Вадиму осталось залить

### Критично (без этого визуальные агенты не работают):
1. **`logos/`** — `logo-primary.svg`, `logo-white.svg`, `logo-mono.svg`, `logo-favicon.png`
2. **`brand-guidelines/`** — официальный бренд-бук PDF (если есть)
3. **`past-posts/{profile}/`** — минимум 10 постов на каждый активный профиль с метриками
4. **`past-posts/_figma-exports/`** — топ-10 banner'ов из Blog banners Figma + ключевые страницы 3DLOOK website Figma

### Желательно:
5. **`color-palette/colors.md`** — confirm точных HEX из Figma
6. **`fonts/fonts.md`** — confirm font family из brand book
7. **`competitors/screenshots/`** — скриншоты Prism Labs / Bodygram / Size Stream

## Как агенты пользуются

| Агент | Что читает | Когда |
|-------|------------|-------|
| post-drafter | overview + proof-points + messaging + 1-2 use-cases + 10 past-posts | Перед каждым постом |
| visual-brief | colors + fonts + past-posts/visuals + figma-exports | Перед каждым брифом |
| hypothesis-generator | use-cases (по продукту) + icp-detail + competitors | Перед каждой гипотезой |
| icp-validator | icp-detail (правильный продукт) | Перед валидацией |
| message-sequencer | proof-points + case-study + faq + compliance | Перед каждой цепочкой |
| seo-section-writer | how-it-works + proof-points + use-case | Перед каждой секцией |
| brand-checker | messaging + past-posts + CLAUDE.md tone | После любого текста |

## Чек-лист готовности

- [x] CLAUDE.md заполнен под 3DLOOK
- [x] product-info/ — полная база знаний
- [x] color-palette + fonts (предварительно)
- [x] competitors/list.md
- [ ] logos/ — Vadim
- [ ] brand-guidelines/ — Vadim
- [ ] past-posts/{profile}/ — Vadim
- [ ] past-posts/_figma-exports/ — Vadim
