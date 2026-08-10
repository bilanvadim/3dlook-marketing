---
product: fitxpress
profile: nick
market: USA
campaign: 2026-08-07-us-digital-fitness
step: icp-validation (batch1)
validated: 2026-08-10
total_scored: 161
---

# ICP Validation Summary — US Digital Fitness Campaign, Batch 1

**Input:** `people-raw-batch1.csv` (161 contacts, Sales Navigator export normalized by `people-extractor`)
**Output:** `people-validated-batch1.csv` (161 rows, all scored — row-for-row match confirmed against input `person_id` order)
**Method:** manual LLM classification against `hypothesis.md` buyer personas + `icp-detail.md` §8 (Connected & Digital Fitness), one contact at a time, per the scope/classification rules in the task brief.

## Headline numbers

| Verdict | Count | % of 161 |
|---|---|---|
| PASS | 62 | 38.5% |
| WEAK | 32 | 19.9% |
| FAIL | 67 | 41.6% |

PASS by priority: **P1 = 15**, **P2 = 16**, **P3 = 31**.

## FAIL breakdown (67 total)

| Bucket | Count |
|---|---|
| noise/off-target entity (pre-tagged `NOISE:` rows — VC funds, homonyms, unrelated employers, self-employed) | 12 |
| Sales / BD / enterprise account territory (regional, key-account, dealer, national-accounts, strategic-sales titles) | 11 |
| Enterprise account management / client success / customer success | 7 |
| Operations, manufacturing, supply chain, logistics, QA, or enterprise health-plan/benefits administration | 11 |
| HR / Talent Acquisition | 6 |
| Finance / Accounting staff (non-CFO, incl. Chief Accounting Officer, SVP Finance, Treasury) | 4 |
| Hardware / mechanical / electrical engineering (not relevant to software/API integration) | 3 |
| Internal IT / ERP (SAP CoE) / helpdesk-support | 2 |
| Likely homonym or duplicate/mismatched company record | 2 |
| Generic title, no function detail (insufficient evidence) | 2 |
| Board member / advisor (non-exec) or Executive Business Partner (EA-type) | 2 |
| Legal (Chief Legal Officer) | 1 |
| Security / Compliance (CISO/Chief Compliance & Privacy Officer) | 1 |
| Clinical / Medical (Chief Medical Officer) | 1 |
| Internal leadership development / coaching (HR-adjacent) | 1 |

## PASS + WEAK by target company

| Company | PASS | WEAK | PASS+WEAK |
|---|---|---|---|
| Personify Health | 15 | 15 | 30 |
| iFIT (incl. NordicTrack/FreeMotion/PROFORM) | 15 | 5 | 20 |
| Tonal | 6 | 4 | 10 |
| MyFitnessPal | 8 | 1 | 9 |
| Hydrow | 4 | 3 | 7 |
| Calibrate | 5 | 1 | 6 |
| Future | 3 | 1 | 4 |
| Fitbod | 1 | 1 | 2 |
| Shotsy | 1 | 1 | 2 |
| Echelon | 2 | 0 | 2 |
| Found | 1 | 0 | 1 |
| Ladder | 1 | 0 | 1 |
| Trainwell | 0 | 0 | 0 |

**Gap flag:** no Trainwell contacts at all appeared in this raw batch (sourcing gap, not a rejection). Found and Ladder are thin (1 contact each).

## Message angle distribution (PASS + WEAK, 94 contacts)

| Angle | Count | % of 94 |
|---|---|---|
| member-engagement | 42 | 44.7% |
| technical-integration | 26 | 27.7% |
| digital-transformation | 13 | 13.8% |
| weight-management | 13 | 13.8% |

digital-transformation was used only for Personify Health enterprise-product-team contacts, per the campaign's angle scoping rule.

## 5 PASS examples

1. **Kevin Duffy** — CEO, iFIT. P1, `member-engagement`. Primary Founder/CEO persona at a top connected-fitness target.
2. **Vidya Rao** — Director of Member Engagement, Tonal. P2, `member-engagement`. Exact title/function match: owns lifecycle messaging and churn for Tonal's 175K+ member community.
3. **Matt Holford** — VP of Engineering, MyFitnessPal. P3, `technical-integration`. VP Engineering persona, technical-integration entry point.
4. **Rob Rebak** — CEO, Calibrate. P1, `weight-management`. Founder/CEO at a GLP-1 weight-management target company.
5. **Heather Fitzpatrick** — VP, Member Engagement, Personify Health. P1, `member-engagement`. Title is a verbatim match to the primary "VP Engagement" persona.

## 5 FAIL examples

1. **Leana Balasco** — VP Commercial Operations, `NOISE: Virta Health`. Pre-tagged noise/off-target entity.
2. **Hannah Jurich** — Director, Enterprise Sales, Personify Health. Sales role, not a product owner; explicitly excluded by the Personify Health buyer note ("NOT enterprise sales territories").
3. **Jennifer Clark** — VP of Human Resources, iFIT. HR function, excluded by scope rules.
4. **Amy FosterDavis** — "Owner," Echelon (company_linkedin_url blank; profile summary says "Interior Designer"). Likely homonym mismatch, not the target connected-fitness Echelon.
5. **Jeff Jacques, MD** — Chief Medical Officer, Personify Health. Clinical/population-health function, not a product or growth buyer for this consumer, non-clinical use case.

## Top concerns

1. **Personify Health sourcing is noisy relative to the buyer note.** Personify Health contributed the largest single block of contacts (roughly half of the 161), but a large share are enterprise sales/account/HR/finance/ops roles that the hypothesis explicitly scopes out ("buyer = consumer-product/member-experience/engagement/digital team, NOT enterprise sales territories"). Of Personify Health's contacts, only 30 landed PASS+WEAK against a much larger FAIL pool. Recommend a tighter Sales Navigator title filter for any follow-up pull on this company (Product / Engagement / Growth / Engineering / Design keywords).
2. **"Member Services" is a recurring ambiguous title at Personify Health** (Geza Csank, Jesse Duprey, Cheryl Waller — all WEAK). It reads as service/support operations rather than digital member-experience, but the title overlaps enough with the "member experience" P2 function that a hard FAIL felt too aggressive. Recommend Vadim spot-check 1-2 of these on LinkedIn before deciding whether to include them in the live send.
3. **Two likely data-quality mismatches** (Amy FosterDavis at "Echelon" — profile says Interior Designer, blank company LinkedIn URL; carol Morgan at "Future Corp" — blank company LinkedIn URL, conflicts with the already-confirmed CEO Ali Jafari at the real target Future). Both are common/generic company names prone to homonym collisions during company matching. Recommend flagging this pattern to whoever runs the Sales Navigator normalization step.
4. **Company coverage is uneven.** iFIT and Personify Health dominate the qualified pool (20 and 30 respectively); Found, Ladder, Fitbod, and Shotsy are thin (1-2 each); Trainwell has zero. If the campaign wants balanced coverage across all 13 target companies (per hypothesis's three flavors — connected fitness, GLP-1 companion apps, nutrition/wellness), a second sourcing pass targeting the thin/missing companies is worth considering before Wave 1 goes out.
5. **CTO/VP Engineering coverage is strong** (13 of 26 technical-integration contacts are P3 PASS), which is good news for the CTO/eng persona explicitly called out in the hypothesis — but sequencing should not let this technical bench crowd out the higher-intent P1/P2 product and growth contacts when message-sequencer builds send order.

## Recommendations

1. **Sequence sends by priority, not by company.** Start with the 15 P1 contacts, then P2 (16), then P3 (31), spreading across companies rather than exhausting one employer (e.g., Personify Health) first.
2. **Hold the 32 WEAK contacts for a second wave** pending Vadim's decision on the "Member Services" ambiguity and the generally lower-confidence Manager/Director-adjacent roles — don't mix them into Wave 1 with the 62 PASS contacts.
3. **Drop the 2 suspected homonym/mismatch rows** (Amy FosterDavis, carol Morgan) from any import — do not send to them.
4. **Consider a targeted follow-up pull** for Found, Ladder, Fitbod, Shotsy, and Trainwell to round out company coverage before declaring this ICP net "done" for the campaign.
5. **Proceed to Vadim's Telegram approval checkpoint** with this validated list; flag the Personify Health sourcing-precision concern and the two homonym drops explicitly in that approval message.
