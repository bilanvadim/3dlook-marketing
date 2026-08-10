---
product: fitxpress
profile: nick
market: USA
campaign: 2026-08-07-us-digital-fitness
batch: 3
step: icp-validator
status: pending Vadim approval
created: 2026-08-10
---

# ICP Validation Summary — Batch 3 (US Digital Fitness, profile: nick)

## Total scored
**161 / 161** contacts from `people-raw-batch3.csv` classified and written to `people-validated-batch3.csv`.

- **PASS: 35** (P1: 7, P2: 20, P3: 8)
- **WEAK: 19**
- **FAIL: 107**

## FAIL breakdown by bucket (107 total)

| Bucket | Count | Notes |
|---|---|---|
| NOISE (pre-tagged `NOISE:` company rows) | 13 | Homonyms/unrelated employers/self-employed/VC-adjacent/board seats at unrelated entities: The Belasco Theatre, Chamber, Lionsgate, Centerville Grace Church, Bruker, Handmade Motion LLC, New York Life Insurance, Self-employed, Northern California Employee Benefit Council, CleanBoss Inc, CommonSpirit Health, Wondr Health, Encore Strategies LLC |
| Non-target role at a target company (off-scope function: finance/accounting non-CFO, HR/Talent, IT infra/DevOps/Security, clinical/care-management, sales/account-management/client-success, legal, ops/logistics/supply chain/procurement, QA, execution-level creative/production, retail/field ops, compliance/safety) | 92 | Bulk of FAILs — mostly Personify Health (account management, clinical, claims, finance, data/BI, comms), iFIT (finance, IT/legal, logistics/ops/warehouse, execution-level creative), MyFitnessPal (finance, HR, QA, ad sales, IT infra), Tonal (finance, IT, embedded firmware, retail GM), Hydrow/Future (ops/exec support), Trainwell (recruiting) |
| Other (likely homonym/mismatch not pre-tagged NOISE) | 2 | `angela marie` "Co Owner at found" (no company LinkedIn page, generic small-business title inconsistent with Found's VC-backed structure) and `Andrey Patenko` "Owner at Proform Fitness LLC" (reads as an independent small-business/franchise owner, not the ProForm brand division of iFIT/Icon Health & Fitness corporate) |
| Geo (non-US-HQ) | 0 | Not applicable — all 13 target companies are fixed/pre-verified US-HQ; 2 individuals based in Canada (Tonal, MyFitnessPal-adjacent) were kept per the geo-discipline rule (company HQ, not residence) |

## PASS + WEAK count per target company (54 total)

| Company | PASS | WEAK | Total |
|---|---|---|---|
| iFIT / NordicTrack / FreeMotion / ProForm | 13 | 2 | **15** |
| Personify Health | 7 | 4 | **11** |
| MyFitnessPal | 2 | 5 | **7** |
| Ladder | 4 | 1 | **5** |
| Future | 0 | 4 | **4** |
| Fitbod | 1 | 2 | **3** |
| Echelon | 2 | 0 | **2** |
| Found | 1 | 1 | **2** |
| Calibrate | 2 | 0 | **2** |
| Hydrow | 1 | 0 | **1** |
| Trainwell | 1 | 0 | **1** |
| Tonal | 1 | 0 | **1** |
| Shotsy | 0 | 0 | **0** |
| **Total** | **35** | **19** | **54** |

No Shotsy contacts appeared in this batch at all.

## message_angle distribution (across 54 PASS+WEAK)

| Angle | Count |
|---|---|
| member-engagement | 27 |
| technical-integration | 12 |
| digital-transformation | 8 |
| weight-management | 7 |

No clinical-operations / virtual-care / compliance / preventive-health angles were used, per campaign scope (the one exception — Calibrate's Associate CMO — was scored under weight-management per the explicit Calibrate/Found exception, not a clinical angle).

## 5 PASS examples

1. **Tom Digan** — Co-Founder & President, Ladder — **P1**, member-engagement. Founder-level economic buyer at a strength-training subscription app.
2. **Rachelle L. Roy** — VP Digital Experience, Personify Health — **P1**, digital-transformation. Direct digital-product ownership matching the "enterprise-product team" buyer, not enterprise sales territory.
3. **Alice Sykes** — Senior Director of Product, Growth, Found — **P1**, weight-management. Owns Growth Product at a GLP-1 coaching platform — sharpest fit for the body-composition-outcomes wedge.
4. **Joshua Gnanayutham** — VP of Product (Head of Product), Fitbod — **P1**, member-engagement. Direct product economic buyer; company bio confirms ARR/growth ownership.
5. **Andrew Hulsizer** — VP Engineering, Ladder — **P3**, technical-integration. Technical C-level exec sponsor, correctly routed to the API/SDK angle instead of auto-failed as "just an engineer."

## 5 FAIL examples

1. **Sankaran Thirugnanasambandam** — Director, Data & Analytics, Personify Health — data infrastructure/BI function; not the consumer-product/member-experience/engagement/digital buyer this campaign targets (data & BI roles were consistently FAILed across Personify Health, iFIT, Tonal — see non-target-role bucket).
2. **Joseph Cappellano** — VP, Strategic Solutions - Ecosystem, Personify Health — reads as enterprise partnerships/B2B territory, which the campaign brief explicitly excludes for Personify Health ("NOT enterprise sales territories").
3. **Justin Gonzalez** — Technical Director, Echelon — title literally matches the WEAK technical-lead pattern, but the bio is live-stream broadcast production (OBS/vMix/PTZ cameras), unrelated to software/API integration — flagged as a false-positive title match and FAILed rather than mechanically WEAK'd.
4. **angela marie** — "Co Owner at found" — likely homonym: missing company LinkedIn page link (unlike the two verified Found/foundhealth contacts in this batch) and a generic small-business title inconsistent with Found's VC-backed startup structure.
5. **Katrina Z.** — Director of Nursing, Calibrate — clinical operations staff; even though Calibrate is one of the two companies where the weight-management angle is permitted for clinical-program contacts, a floor-level clinical operations role is not a plausible product/purchasing decision maker.

## Top concerns

1. **Personify Health is noisy and needs a scoped list, not a company-wide pull.** 11 of its ~50 contacts in this batch passed/weakened; the rest span claims, care management, HR, legal, finance, and account management — divisions unrelated to the consumer member-app buyer this campaign wants. A future pull should target titles containing "Product," "Digital Experience," "Engagement," or "Transformation" specifically rather than a full company export.
2. **Title-only keyword matching produces false positives.** Two cases (`Technical Director` at Echelon = broadcast production; `Member Services` at Hydrow = technical support) show that title strings can superficially match a buyer persona while the actual function is unrelated. Bios were essential to override these.
3. **Two likely un-tagged homonyms slipped past NOISE pre-tagging** (`Found` "Co Owner", `iFIT` "Owner at Proform Fitness LLC") — both read as small, unrelated businesses. Recommend tightening the NOISE pre-tagging heuristic to flag "Owner"/"Co Owner" titles with missing `company_linkedin_url` for manual review before this stage.
4. **MyFitnessPal skews WEAK (5) over PASS (2).** Most of its senior product/growth people are more monetization/ads-engineering-adjacent than core consumer-engagement owners; the two clean PASSes (Director of Product Management, CFO) are the priority sends.
5. **Future and Fitbod have thin PASS coverage** (Future: 0 PASS / 4 WEAK; Fitbod: 1 PASS / 2 WEAK) — the raw pull for these two companies leaned heavily into generalist/technical titles rather than named Product/Growth/Engagement leaders. A follow-up Sales Navigator pull targeting Fitbod's and Future's named CPO/Head of Growth (if not already the ones captured) would strengthen this segment.
6. **iFIT is the deepest well** (15 PASS+WEAK) reflecting its large corporate footprint (iFIT/NordicTrack/FreeMotion/ProForm/Icon Health & Fitness) — sequencing should likely prioritize the 13 PASS contacts there first given volume, spread across Subscription/Product/Creative/Growth functions.

## Recommendations

1. **Send order:** P1 (7) → P3 (8, exec sponsors) → P2 (20) → WEAK (19, lower priority / smaller sequences or hold for a second wave).
2. **Approve for outreach:** all 35 PASS contacts across member-engagement (iFIT, Ladder, Echelon, Found, Personify Health, Hydrow, Trainwell), digital-transformation (Personify Health only), weight-management (Found, Calibrate, MyFitnessPal), technical-integration (Ladder, Tonal, iFIT).
3. **Hold/deprioritize:** the 19 WEAK contacts — mostly manager-level product roles, UX/design leads, and technical leads without direct budget authority. Consider a lighter-touch or delayed sequence for these rather than the full campaign cadence.
4. **Vadim decision needed:** confirm whether the 2 likely-homonym FAILs (`angela marie` / Found, `Andrey Patenko` / iFIT-ProForm) should be manually re-verified via LinkedIn before being permanently excluded, since they were not pre-tagged NOISE by the normalization step.
5. **No Shotsy contacts** appeared in this batch — if Shotsy is a priority target, a separate Sales Navigator pull is needed.
6. Proceed to Vadim's Telegram approval checkpoint per the outbound workflow before message-sequencer runs on the approved list.
