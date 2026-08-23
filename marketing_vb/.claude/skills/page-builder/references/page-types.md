# Page type registry — 3DLOOK

Which page types this site needs, what each one is for, and whether a Kit exists.
`Kit ✓` = a full Kit ships with this skill. `gap` = no Kit yet; build from the nearest Kit and say so
in the handover. `routed away` = a different pipeline owns it.

## Bottom of funnel — pages that close

| Type | Job | Kit |
|---|---|---|
| **Use-case / vertical page** | One product retold in one vertical's language, regulators and KPIs | `kit-vertical-page.md` ✓ |
| **Campaign landing** | One campaign, one offer, one action, no nav, no sibling block | `kit-vertical-page.md` ✓ (stripped) |
| **Product page** | The parent for a product line: FitXpress uses the homepage, Mobile Tailor has `/mobile-tailor/` | gap — nearest: vertical Kit. Homepage *positioning* is out of scope |
| **Case study page** | One customer, one number, one narrative | gap — no such page exists on the site yet |
| **Pricing** | Tiers, what moves the number, what the trial includes | gap — a page already exists, rewrite only |
| **Technology** | How the capture, model and API work, cross-product | gap — nearest: vertical Kit |

## Middle of funnel — pages that qualify

| Type | Job | Kit |
|---|---|---|
| **Gated asset landing** | Ebook, buyer checklist, evaluation guide behind a form | `kit-vertical-page.md` ✓ (stripped, one action) |
| **Comparison / alternatives** | 3DLOOK against a named approach a buyer already knows | routed away → `/new-article` |
| **Buyer checklist** | Vertical evaluation checklist | routed away → treat as a gated asset, per the content strategy |

## Top of funnel

| Type | Job | Kit |
|---|---|---|
| **Hub article** | The authority page a vertical's cluster hangs off | routed away → `/new-article` (mvb-seo) |
| **Supporting article, guide, definition, listicle** | One narrower buyer question | routed away → `/new-article` |
| **Webinar / event page** | An event with a registration action | gap |

## Company and legal

`about-us`, `careers`, `partners`, `contact-us`, policies. Out of scope for this skill unless the ask
is explicitly a rewrite; legal pages are never written here.

---

## How to decide whether a page gets built at all

Ask in order. A "no" ends it for now.

1. **Does a use-case file exist** in `brand-assets/product-info/use-cases/` for this vertical? No file
   → write the use-case first, or stop.
2. **Are there 2+ publishable case studies from this vertical** in `product-info/case-studies/`? No
   → G-I fails, the vertical gets a section on the product page and its hub article carries it.
3. **Is there demand?** A row in `content-plan.md`, Search Console volume on vertical-named queries,
   or ≥15% of outbound pipeline from `workspace/outbound/campaigns/`.
4. **Is there something to say that no existing page or article already says?** Check both inventories.
5. **Does it have a parent and a URL?** FitXpress verticals hang off the homepage at
   `/for-{vertical}/`; Mobile Tailor verticals sit under `/mobile-tailor/`. See `site-inventory.md`.

Volume without these produces a site of pages that rank for nothing and answer no one.

## Vertical coverage as of 2026-08-23

| Vertical | Use-case file | Cases available | Live page |
|---|---|---|---|
| FX — telehealth / weight loss | `fx-telehealth-weight-loss.md` | Yazen (34K scans) | `/structured-body-data-for-telehealth-digital-health-programs/` |
| FX — online pharmacy / BMI | `fx-online-pharmacy-bmi.md` | UK Meds (7.5K scans) | `/for-bmi-verification/` |
| FX — digital fitness | `fx-digital-fitness.md` | — | `/fitxpress/for-connected-and-digital-fitness/` |
| FX — insurance underwriting | `fx-insurance-underwriting.md` | — | none |
| FX — wellness rewards | `fx-wellness-rewards.md` | — | none |
| FX — bariatric pre-auth | `fx-bariatric-pre-auth.md` | — | none |
| FX — occupational health | `fx-occupational-health.md` | — | none (hub article live) |
| FX — clinical trials | `fx-clinical-trials.md` | — | none (hub article live) |
| FX — plastic surgery, BCRL | **missing** | — | none |
| MT — made to measure | `mt-made-to-measure.md` | Generation Tux, Jim's Formal Wear | `/mobile-tailor/for-made-to-measure/` |
| MT — on-demand manufacturing | `mt-on-demand-manufacturing.md` | — | `/mobile-tailor/for-on-demand-manufacturing/` |
| MT — uniform fitting | `mt-uniform-fitting.md` | Safariland, Burlington Medical | `/mobile-tailor/for-uniforms/` |
| MT — wrist measurement | `mt-wrist-measurement.md` | — | none |

Read this table as the G-I pre-check. On today's evidence **MT uniforms** (Safariland + Burlington
Medical) clears the "2+ cases from this vertical" bar outright, and **MT made-to-measure** clears it
if formal-wear rental counts as the same vertical as made-to-measure — that is Vadim's call, not an
assumption to make while drafting. Every other vertical needs a second case, an approved customer
reference, or a G-I waiver recorded with Vadim's decision and its reason.
