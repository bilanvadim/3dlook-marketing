---
product: fitxpress
type: fact-sheet
vertical: insurance-underwriting
date: 2026-08-31
---

# Fact sheet — /for-insurance-underwriting/

Everything a reviewer cannot see from the copy: the source behind every figure and every name, and what
was measured versus what was specified but not yet built.

## Page identity

| | |
|---|---|
| Final URL | `https://3dlook.ai/for-insurance-underwriting/` |
| Canonical | Self |
| Parent | `https://3dlook.ai/` |
| Breadcrumb | Home → FitXpress for Insurance Underwriting (2 levels) |
| Indexable | Yes, specified. Not yet verifiable, the page is not built |
| Language | en-US |
| Word count, page copy | ~1,750 |
| `<h1>` count | 1 |

## Schema specified

`Service` with `audience` (`BusinessAudience` with `audienceType`) and `areaServed`, `FAQPage` covering
all 13 questions, `BreadcrumbList` with 2 levels. `WebPage`, `Organization` and `WebSite` come from the
Yoast site template. Full JSON-LD is written out in `README.md`, modelled on the graph already live on
`/structured-body-data-for-telehealth-digital-health-programs/`. **Not yet validated**, because the page
does not exist.

## Every number on the page, and where it comes from

| Figure | Where it appears | Source |
|---|---|---|
| 2 guided photos | Hero, quick-answer | `proof-points.md` → Speed |
| Under 45 seconds | Hero, quick-answer, comparison table | `proof-points.md` → Speed |
| 80+ body measurements | Hero, quick-answer | `proof-points.md` → Output coverage |
| BMI, BMR, body fat %, lean mass, fat mass | Quick-answer | `proof-points.md` → Output coverage; `tech-spec.md` |
| 96-97% accuracy against expert manual measurement | Accuracy table, FAQ | `proof-points.md` → Accuracy, 2025 Accuracy & Repeatability Study |
| Typical absolute error 1.5 to 2.0 cm | Accuracy table, FAQ | `proof-points.md` → Accuracy |
| Scan-to-scan repeatability `< 1 cm` | Accuracy table, comparison table, FAQ | `proof-points.md` → Repeatability, "variance across repeated scans < 1 cm". Written in the locked `< 1 cm` form from `about-me.md` |
| Weight estimation ±3.5% average error | Accuracy table | `proof-points.md` → Accuracy, FitXpress deck, real-world conditions |
| Ages 16 to 78, heights 150 to 205 cm, weights 38 to 210 kg, 48% male / 52% female, US and Europe | Accuracy conditions, FAQ | `proof-points.md` → Training data, "Demographic coverage". Labelled on the page as demographic coverage, which is what the source calls it. **Conflict flagged:** `about-me.md` states the internal validation population as 150 to 220 cm. The page uses the `proof-points.md` figure and the discrepancy is in `open-items.md` |
| Photos deleted immediately or within 30 days | Quick-answer, compliance, FAQ | `compliance.md`; `proof-points.md` → Compliance & security |
| TLS in transit, AWS S3 SSE-S3 at rest, always on | Compliance, FAQ | `compliance.md` |
| Automatic blur on stored photos, face obfuscation at capture | Compliance | `compliance.md`; `tech-spec.md` |
| No personal identifiers processed, images not shared with third parties, excluded from model training | Compliance, FAQ | `compliance.md` |
| $1,000 per month up to 500 scans; $1,500 up to 1,000 scans | Price signal | Live `/pricing/`, **re-verified 2026-08-31**: Starter $1,000 per month up to 500 scans, Pro $1,500 per month up to 1,000 scans, Personalized custom. Unchanged since the 2026-08-23 reading in `site-inventory.md`. **Conflict flagged:** the internal `pricing.md` volume table does not match the published tiers. `open-items.md` |
| One-month trial, 200 requests, full SDK access | Price signal, FAQ | `proof-points.md` → Pricing anchors; `faq.md` |
| Founded 2016 | Deployment block | `proof-points.md` → Funding & company milestones |
| 112,100 scans across 67 active customers in 2025 | Deployment block | `proof-points.md` → Aggregate. **Publication rights unconfirmed**, see `open-items.md` |
| A scan failing on pose is not billable | FAQ | `faq.md` → Pricing & Commercials |
| Integration measured in days | Integration, FAQ | `faq.md` → Integration |
| Customers who build their own camera flow see worse measurement quality | Integration | `tech-spec.md`, stated there as the single biggest factor in measurement accuracy |

## External sources cited on the page

| Claim | Attribution | Where it came from |
|---|---|---|
| Changes in build and weight were the top reason for variance in risk-class assessment; build and BMI misrepresentation is the second-largest driver of misclassification after smoking non-disclosure | Munich Re, 2025 accelerated underwriting analysis | Already published by 3DLOOK in `mobile-body-scanning-insurance-underwriting` (May 2026, Assel Sekerova). **Not re-verified against the Munich Re original during this build** |
| Self-reported survey data underestimated the prevalence of severe obesity by 40% | Centers for Disease Control and Prevention (CDC) researchers | Same published article. **Not re-verified against the CDC original** |
| Accelerated underwriting models must be fair, transparent, grounded in sound actuarial principles and monitored for unfair discrimination | National Association of Insurance Commissioners (NAIC) | Same published article. **Not re-verified against the NAIC original** |

## Customer names and quotes

**No customer name, logo, client metric or testimonial appears anywhere on the page.** Two deployments
are described without naming the customer: BMI verification inside a UK online-pharmacy order flow
(`case-studies/uk-meds.md`, Pattern B, server-side eligibility, metrics never shown to the end user) and
longitudinal body-composition tracking in weight-management programs (`case-studies/yazen.md`). No
per-customer scan volume is published. No Mobile Tailor customer ARR appears.

## Reserved and boundary wording

- "third-party" appears once, in the negative disclosure editorial guardrail #3 requires: peer review
  and third-party clinical certification are stated as absent. No positive independence claim is made
  anywhere on the page. "independent", "validated" and "clinically validated" do not appear as claims.
- Medical framing: "FitXpress is not a medical device", stated once, in the approved wording. The
  underwriting boundary is stated once more as "FitXpress supports underwriter review; it is not a
  standalone decisioning engine".
- No sentence asserts that a regulatory framework does not apply. HIPAA reach is written as depending on
  the carrier's lines and its handling of health information.
- Accuracy is scoped through "accurate enough for which decision?" with all four conditions named. No
  bare headline percentage: every figure carries its reference and "detailed methodology available under
  a non-disclosure agreement".

## Measured versus specified

| Item | State |
|---|---|
| Performance (page weight, Core Web Vitals) | **Not measured.** The page is not built |
| Viewports 375 / 768 / 1280 / 1440 | **Not checked.** No rendered page |
| Contrast results | **Not measured.** Tokens are taken from `DESIGN.md` (navy `#050F40` surfaces, `#143DFF` accent, `#B1BDFF` focus ring at 3px with 2px offset), which is specified to meet AA, and no contrast pair has been tested |
| Keyboard operation, FAQ accordion | **Not verified.** No rendered page |
| Analytics events (form view, first input, submit, demo-link click) | **Named, not verified.** Verification is a post-publish task |
| Schema validation | **Not run.** JSON-LD written, not yet parsed by a validator |
| Images and alt text | **No assets produced.** `assets/` is empty. Every visual marker has a brief and an alt-text string in `README.md` |
| Internal links | **Verified 2026-08-31.** All eight outbound internal links return HTTP 200: `/`, `/pricing/`, `/case-studies/`, `/for-bmi-verification/`, `/structured-body-data-for-telehealth-digital-health-programs/`, `/content-hub/mobile-body-scanning-insurance-underwriting/`, `/content-hub/mobile-body-scanning-accuracy/`, `/ebook-the-next-big-leap-in-health/` |
| AI-tell detector | **Run**, `--channel page`, verdict CLEAN, density 0.0 per 1,000 words against a budget of 6.0 |

## Design tokens

Every token comes from `DESIGN.md`: Satoshi throughout, `#143DFF` as a single accent, navy `#050F40`
with the radial glow on hero, proof and closing bands, the 4/5/15/20/30-40 px radius scale, the 8-step
spacing rhythm, container 1200px, focus ring `#B1BDFF`. Nothing improvised.
