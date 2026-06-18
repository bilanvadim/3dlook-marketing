# Product Info — Index (3DLOOK)

Карта продуктовых документов. Источник правды для агентов в outbound, SEO, social.

## Файлы

| Файл | Содержимое | Используется в |
|------|------------|----------------|
| `overview.md` | 1-pager 3DLOOK + два продукта | post-drafter, hypothesis-generator, seo-section-writer |
| `how-it-works.md` | Техническое описание стека | seo-section-writer (technical articles) |
| `proof-points.md` | Все цифры со ссылками на источник | message-sequencer, post-drafter, all SEO |
| `icp-detail.md` | Развёрнутый ICP по обоим продуктам | hypothesis-generator, icp-validator |
| `pricing.md` | FitXpress tiers, free trial | message-sequencer, faq |
| `competitors.md` | Prism Labs / Bodygram / Size Stream / Apple risk | hypothesis-generator, seo-outline-builder |
| `compliance.md` | HIPAA, GDPR, encryption, photo retention | message-sequencer (insurance/healthcare) |
| `tech-spec.md` | API, SDK, white-label | tech-focused content |
| `case-studies/` | Реальные клиенты с метриками | message-sequencer, post-drafter |
| `use-cases/` | Use case + ICP + KPI + market sizing | hypothesis-generator |
| `faq.md` | Возражения / ответы | message-sequencer |
| `messaging.md` | Hero messages, anti-positioning | post-drafter, message-sequencer |

## Use cases

### FitXpress
- `use-cases/fx-telehealth-weight-loss.md`
- `use-cases/fx-online-pharmacy-bmi.md`
- `use-cases/fx-insurance-underwriting.md`
- `use-cases/fx-wellness-rewards.md`
- `use-cases/fx-bariatric-pre-auth.md`
- `use-cases/fx-occupational-health.md`
- `use-cases/fx-clinical-trials.md`
- `use-cases/fx-digital-fitness.md`

### Mobile Tailor
- `use-cases/mt-made-to-measure.md`
- `use-cases/mt-on-demand-manufacturing.md`
- `use-cases/mt-uniform-fitting.md`
- `use-cases/mt-wrist-measurement.md`

## Case studies

| Файл | Клиент | Продукт | Метрика |
|------|--------|---------|---------|
| `case-studies/safariland.md` | Safariland | MT | 15.5K сканов/год, 5+ лет retention |
| `case-studies/burlington-medical.md` | Burlington Medical | MT | 11.5K сканов |
| `case-studies/uk-meds.md` | UK Meds | FX | BMI verification, 7.5K сканов |
| `case-studies/yazen.md` | Yazen | FX | Weight loss, 34K сканов |
| `case-studies/jims-formal-wear.md` | Jim's Formal Wear | MT | 3.2K сканов |
| `case-studies/generation-tux.md` | Generation Tux | MT | DTC formal wear rental |

## Когда что читать

- **post-drafter** → `overview.md` + `proof-points.md` + 1-2 case studies
- **hypothesis-generator** → `use-cases/` (по продукту) + `icp-detail.md` + `competitors.md`
- **message-sequencer** → `proof-points.md` + case-study + `faq.md` + `compliance.md`
- **seo-section-writer** → `how-it-works.md` + `proof-points.md` + use-case
- **seo-outline-builder** → `competitors.md` + use-case
