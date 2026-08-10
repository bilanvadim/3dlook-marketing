---
product: fitxpress
profile: nick
market: USA
campaign: 2026-08-07-us-digital-fitness
step: icp-validation (batch2)
validated: 2026-08-10
total_scored: 161
---

# ICP Validation Summary — US Digital Fitness Campaign, Batch 2

**Input:** `people-raw-batch2.csv` (161 contacts, Sales Navigator export normalized by `people-extractor`)
**Output:** `people-validated-batch2.csv` (161 rows, all scored — row-for-row match confirmed against input `person_id` order; row count verified with `wc -l` at 162 including header)
**Method:** manual LLM classification against `hypothesis.md` buyer personas + `icp-detail.md` §8 (Connected & Digital Fitness) and the IT/Technical Roles secondary-buyer policy, one contact at a time, per the scope/classification rules in the task brief.

## Headline numbers

| Verdict | Count | % of 161 |
|---|---|---|
| PASS | 40 | 24.8% |
| WEAK | 29 | 18.0% |
| FAIL | 92 | 57.1% |

PASS by priority: **P1 = 17**, **P2 = 17**, **P3 = 6**.

## FAIL breakdown (92 total)

| Bucket | Count |
|---|---|
| Noise/off-target entity (pre-tagged `NOISE:` rows — VC/PE funds, homonyms, unrelated employers, self-employed) | 21 |
| Sales / business development / "Strategic Development" corp-dev / enterprise sales territory / sales enablement | 14 |
| Operations, manufacturing, supply chain, logistics, workforce management, internal automation, procurement, implementation PM | 13 |
| Enterprise clinical operations / population health / customer analytics & reporting / medical economics / claims ops (B2B, not consumer product) | 5 |
| Account management / client success / customer success / "Customer Happiness" | 5 |
| IT infrastructure / DevOps / Cloud engineering / QA / general IT / ITIL problem management | 5 |
| Other / unclear function (Chief of Staff, generic "Manager" with no detail, self-employed consultant, unclear business unit, enterprise transformation, video contractor) | 6 |
| Finance / Accounting / Payroll | 4 |
| Legal | 4 |
| Content operations / Corporate Communications / PMO / Post-production / Content Integration (non-engagement content ops) | 4 |
| HR / People | 4 |
| Likely homonym or mismatched company record, not pre-tagged (Found ×2, Echelon ×1) | 3 |
| Hardware / firmware IC engineering (not relevant to software/API integration) | 2 |
| Self-employed / local franchise dealer under a target brand name ("Pro Form/Proform Fitness") | 2 |

## PASS + WEAK by target company

| Company | PASS | WEAK | PASS+WEAK |
|---|---|---|---|
| Personify Health | 8 | 12 | 20 |
| iFIT (incl. NordicTrack/FreeMotion/PROFORM) | 6 | 5 | 11 |
| MyFitnessPal | 4 | 5 | 9 |
| Tonal | 6 | 2 | 8 |
| Hydrow | 4 | 3 | 7 |
| Echelon | 3 | 0 | 3 |
| Calibrate | 2 | 1 | 3 |
| Future | 2 | 1 | 3 |
| Ladder | 2 | 0 | 2 |
| Fitbod | 1 | 0 | 1 |
| Found | 1 | 0 | 1 |
| Trainwell | 1 | 0 | 1 |
| Shotsy | 0 | 0 | 0 |

**Gap flag:** Shotsy has zero contacts in this raw batch (sourcing gap, not a rejection). Found, Ladder, Fitbod, and Trainwell are thin (1-2 each) — the same three companies (Found, Ladder, Trainwell/Fitbod-adjacent) flagged thin in the batch1 summary, so this is now a two-batch pattern worth a dedicated sourcing pass.

## Message angle distribution (PASS + WEAK, 69 contacts)

| Angle | Count | % of 69 |
|---|---|---|
| member-engagement | 39 | 56.5% |
| technical-integration | 19 | 27.5% |
| digital-transformation | 6 | 8.7% |
| weight-management | 5 | 7.2% |

`digital-transformation` was used only for Personify Health enterprise-product-team contacts, per the campaign's angle-scoping rule (it is explicitly scoped to "enterprise-product teams at Personify Health" and not used for any other company).

## 5 PASS examples

1. **Michelle Gattuso** — VP of Product Management, iFIT. P1, `member-engagement`. Exact CPO/Head of Product match ("hardware and software innovation") at a top connected-fitness target.
2. **Federico Locatelli** — Senior Director, User Engagement & Retention, iFIT. P1, `member-engagement`. Title is a verbatim function match to the primary VP Engagement/Retention persona.
3. **Kartik Khanna** — VP, AI & Platform, iFIT. P1, `technical-integration`. Owns the ML/AI build-vs-buy decision most directly relevant to a computer-vision body-scan feature — directly answers the "we could build this" objection in the hypothesis.
4. **Sam Margo** — VP, Strategy, BizOps & Growth, Found (foundhealth). P1, `weight-management`. Head of Growth persona at a GLP-1 weight-loss platform.
5. **Pete McCabe** — CEO, Personify Health. P1, `digital-transformation`. Founder/CEO persona at the campaign's largest enterprise target.

## 5 FAIL examples

1. **Jenna Lafayette** — Regional Vice President, Healthcare, Personify Health. Enterprise sales territory role, explicitly excluded by the Personify Health buyer note ("NOT enterprise sales territories").
2. **Ron Vormittag** — Owner, `NOISE: Calibrate Them LLC`. Pre-tagged noise, homonym of Calibrate the GLP-1 platform.
3. **neisha wallace** — "Owner, found" at company_name `Found` with no company LinkedIn URL; her bio explicitly describes an unrelated art & print studio ("vintage scarves and prints"), not Found Health.
4. **Andy Stevens** — EVP, Chief People Officer, iFIT. HR executive, excluded by scope rules.
5. **Daniel Ackerman** — VP, Legal, Personify Health. Legal function, not a product or engagement buyer.

## Top concerns

1. **Personify Health is again the single largest source block (53 of 161 raw contacts, ~33%) but converts at a low rate against the narrow buyer note.** Only 20 of 53 (37.7%) landed PASS+WEAK; the rest are enterprise sales/account-management/HR/finance/legal/ops roles the hypothesis explicitly excludes ("buyer = consumer-product/member-experience/engagement/digital team, NOT enterprise sales territories"). Recommend a tighter Sales Navigator title filter for any repeat pull on this employer (Product / Engagement / Growth / Engineering / Marketing keywords).
2. **"VP, Strategic Development" is a recurring, ambiguous Personify Health title** (Diane Schechner, Jaci Haack, Micah DeHenau, Brian Baker — 4 separate contacts, all FAIL). It reads as corporate/business development, not the consumer-product/member-experience/digital function the buyer note requires. Worth a quick sanity-check with Vadim in case this is actually a product-adjacent strategy team he wants reconsidered.
3. **Three likely homonym mismatches were not caught by the pre-tagging step**: two "Found" contacts (tom lynch, neisha wallace — sparse profiles, no company LinkedIn URL, one bio explicitly describing an unrelated art & print studio) and one "Echelon" contact (Brad Herr, whose bio names "ECHELON Resource Consultants, LLC" rather than Echelon Fit). Generic single-word company names are prone to this; worth flagging to whoever runs Sales Navigator normalization for a stricter company-LinkedIn-URL requirement.
4. **Two contacts carry company_name "iFIT" but read as local retail-dealer owners**, not corporate employees (Austin Treloar: "Owner at Pro Form Fitness"; Mark Hanson: "owner/Trainer at Proform Fitness"). Flagged FAIL for this campaign's ICP (not a corporate product/engagement decision-maker), though worth a manual LinkedIn spot-check in case either is actually iFIT corporate staff whose bio is just outdated.
5. **Company coverage is uneven and Shotsy has zero contacts in this batch** (sourcing gap, not a rejection); Found, Ladder, Fitbod, and Trainwell are also thin (1-2 PASS+WEAK each) — mirroring the same gap batch1 flagged for Trainwell/Found/Ladder. If the campaign wants balanced coverage across all 13 target companies, a follow-up sourcing pass targeting Shotsy plus these four is worth prioritizing before Wave 2 goes out.

## Recommendations

1. **Sequence sends by priority, not by company.** Start with the 17 P1 contacts, then P2 (17), then P3 (6), spreading across companies rather than exhausting one employer (e.g., Personify Health, iFIT) first.
2. **Hold the 29 WEAK contacts for a second wave.** Roughly 2/3 of this batch's WEAKs are Directors of Engineering / Software Engineers / Solution Architects picked up via the IT-role `technical-integration` exception policy — useful champions, but lower-intent than the P1/P2 product and growth cohort. The rest are member-services/support-adjacent roles at Personify Health with genuine title ambiguity.
3. **Drop the 3 suspected homonym rows** (tom lynch, neisha wallace, Brad Herr) from any import — do not send to them.
4. **Combine with batch1 before sending, and dedupe by `person_id` and by `person_linkedin_url`.** Both batches validated the same 13 target companies independently; check for overlapping contacts (e.g., duplicate Sales Navigator pulls on Personify Health or iFIT) before building a combined send list.
5. **Consider a targeted follow-up Sales Navigator pull** for Shotsy (zero contacts across both batches so far), Found, Ladder, Fitbod, and Trainwell to round out company coverage before declaring this ICP net "done" for the campaign.
6. **Proceed to Vadim's Telegram approval checkpoint** with this validated batch2 list; flag the Personify Health sourcing-precision concern, the "VP Strategic Development" title ambiguity, and the 3 homonym drops explicitly in that approval message.
