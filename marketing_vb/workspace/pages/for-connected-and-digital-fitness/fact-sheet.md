---
product: fitxpress
type: fact-sheet
vertical: connected-and-digital-fitness
date: 2026-10-02
---

# Fact sheet: /fitxpress/for-connected-and-digital-fitness/

Everything a reviewer cannot see from the copy: the source behind every figure and every name, and what
was measured versus what was specified but not yet built.

## Page identity

| | |
|---|---|
| Final URL | `https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/` (live today; this is a rewrite in place, the URL does not change) |
| Canonical | Self |
| Parent | `https://3dlook.ai/fitxpress/` (ships with the use-case release; today it 301s to `/`) |
| Breadcrumb | Home → FitXpress → FitXpress for Connected and Digital Fitness (3 levels) |
| Indexable | Yes. The live URL is indexed today |
| Language | en |
| Visible copy | ~1,320 words (H1 to form, tables and FAQ included, builder notes excluded) |
| `<h1>` count | 1 |
| FAQ | 4 questions (gym body scan, SDKs for remote users, scan frequency, Apple Health / Health Connect) |
| Primary action | "Book a demo" → `#demo`, the shared HubSpot form `FX \| LP \| Demo` |
| "you / your" density | 0 per 1,000 words in the copy |

## Schema specified

`Service` with `audience` (`BusinessAudience`, `audienceType` "Connected fitness platforms, digital
fitness and coaching apps") and `areaServed` (US, GB, CA, DE, AE, AU and the Nordic countries, from the
ICP), `FAQPage` covering all 4 questions with answers byte-identical to the visible text,
`BreadcrumbList` with 3 levels. `WebPage`, `Organization` and `WebSite` come from the Yoast template.
Written into the HTML prototype (`page.html`); parses and matches the visible FAQ. **Not yet validated in
Google's Rich Results Test**, because the page is not published.

## Performance, accessibility, analytics

Measured on the HTML prototype (`page.html`, 2026-10-02, Playwright): at 375 px `scrollWidth` = 375, no
horizontal overflow; at 1280×800 the H1, the hero paragraph and the primary button sit inside the first
viewport (button bottom at 774 px). Tokens come from `DESIGN.md` through the approved insurance template:
Satoshi, `#143DFF` as the single accent, navy `#050F40` hero. JSON-LD parses as one `@graph` (WebPage,
Service, FAQPage, BreadcrumbList), and the four FAQ answers are byte-identical to the visible text. No em
or en dashes in the file. Not measured: 768 and 1440 px, contrast ratios, keyboard operation and page
weight; these are checked on the WordPress build (G-T). Analytics events
(`generate_lead` with `form_name = fx_lp_demo` and `fx_vertical`, `demo_click`, `meeting_booked`) come from
the shared form and GTM and have not been verified on this page.

## Every number on the page, and where it comes from

| Figure | Where it appears | Source |
|---|---|---|
| 2 photos, front and side | Hero, strip | `proof-points.md` → Speed |
| Under 45 seconds from the photos to structured results | Hero, strip | `proof-points.md` → Speed (the one public definition, 2026-09-23) |
| 80+ body measurements | Hero, record table, comparison table | `proof-points.md` → Output coverage |
| BMI, BMR, body-fat percentage, lean mass, fat mass | Record table | `proof-points.md` → Output coverage; live `/pricing/` |
| 24% of health and fitness app users active on day 1, 7% on day 30 (global, 2022 data) | Problem | Adjust, *Mobile app retention benchmarks for 2023*. **Verified on the primary page 2026-10-02** (read through a reader proxy after direct requests returned HTTP 429): "…health & fitness at 24%" (Day 1, 2022) and "Fintech and lifestyle apps led in 2022, with Day 30 retention rates of 9%, followed by health & fitness and social apps, both with a rate of 7%." Global figures |
| A median of 70% of users stopped within 100 days; lack of personalization among the reasons | Problem | Kidman PG, Curtis RG, Watson A, Maher CA. *When and Why Adults Abandon Lifestyle Behavior and Mental Health Mobile Apps: Scoping Review.* J Med Internet Res 2024;26:e56897. Abstract: "a median of 70% of users discontinued use within the first 100 days". Full text lists "Lack of personalization" under "Content and features". Verified via Europe PMC on 2026-10-02 |
| `< 1 cm` typical scan-to-scan difference for most measurements | Accuracy | `accuracy-formulations.md` §1.2 |
| 96-97% accuracy against expert manual measurement, typical absolute error 1.5-2.0 cm | Accuracy | `accuracy-formulations.md` §1.1 |
| Validation population: ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg; "performance outside this scope has not been characterized" | Accuracy | `accuracy-formulations.md` §1.4 |
| The accuracy figures describe body measurements; body composition values are estimates derived from them with height and weight | Accuracy | `compliance.md` §3 ("body composition values are estimates derived from them plus height and optional weight"); terminology guardrails §2.13 |
| Photos deleted immediately after processing or retained for up to 30 days | Data handling | `compliance.md` §3; wording as on the final insurance page (2026-10-02) |
| $1,000 a month up to 500 scans; Pro $1,500 a month up to 1,000 scans, with 3D body progress tracking and 3D Goal Visualization | Strip, record table, pilot | Live `/pricing/`, read 2026-10-02 |
| No integration fee | Strip, pilot | `pricing.md` (Vadim, 2026-09-30) |
| Hero mock: 82.4 / 82.1 kg, 27.1% / 25.3%, 60.1 / 61.3 kg, 92.0 / 88.6 cm | Hero visual | **Illustrative, not a claim.** Captioned "Illustrative example" on the page, the same pattern as the case-record mock on the final insurance page. The numbers are internally consistent (fat mass + lean mass = weight) |
| Day-30 and day-90 retention, repeat scan rate | Pilot | Metric names the evaluation should measure, not results |

## Statements that are not numbers, and their sources

| Statement | Source |
|---|---|
| Web and mobile SDKs, including supported iOS and Android integrations | `tech-spec.md`, public SDK wording (Vadim, 2026-09-23) |
| Real-Time Pose Validation pauses capture until pose and framing requirements are met; clothing-related information can be surfaced for review | Final insurance page (2026-10-02); `tech-spec.md` note of the same date |
| Voice guidance during capture | The live fitness page ("Guided voice prompts lead users step-by-step") |
| The consent screen belongs to the platform, in its own wording | `tech-spec.md` → What's customizable: "Consent / instructions: your wording, your flow" |
| The member sees a comparison of the scans the platform selects | `compliance.md` §4: Body Progress compares two scans chosen by the customer; 3DLOOK does not track individuals |
| The platform designs onboarding, consent and results screens; the photo-capture layer, where pose validation runs, stays fixed to protect measurement quality | `tech-spec.md` → What's customizable / What's NOT customizable ("by design, it protects measurement accuracy") |
| Scan at onboarding and at fixed check-ins; the same conditions each time: form-fitting clothing, the same place, the phone on a stable surface | `tech-spec.md` → Recommended capture environment; repeatability depends on consistent capture (`accuracy-formulations.md` §1.2 context) |
| Sync to Apple Health or Health Connect is built by the platform | FitXpress delivers through the API and SDKs only (`tech-spec.md`); Google retired the Google Fit APIs in favour of Health Connect, hence the name |
| 3DLOOK shows the member flow, a sample payload and the integration pattern (pilot walkthrough) | Same pilot pattern as the final insurance page (2026-10-02) |
| Scan records use anonymized, randomly generated identifiers | `compliance.md` §4 |
| GDPR role sentence | `compliance.md` §2, verbatim |
| No training on production customer data without explicit, documented authorization | `compliance.md` §1 |
| FitXpress is not a medical device | `compliance.md` §1, short form |
| Production infrastructure already deployed in remote weight-management and BMI-verification workflows | Final insurance page (2026-10-02); `proof-points.md` → Customer outcomes, FitXpress (weight-loss management and BMI verification customers, not named) |
| App Store privacy details and Google Play Data safety form cover health and fitness data and photos | Apple App Store privacy details (data types "Health", "Fitness", "Photos or Videos") and Google Play Data safety (data types "Health and fitness", "Photos and videos"); platform documentation, not a 3DLOOK claim |

## External sources cited on the page

- Adjust, mobile app retention benchmarks for 2023: https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/
- Kidman et al., JMIR 2024: https://www.jmir.org/2024/1/e56897

## Client names on the page

None.
