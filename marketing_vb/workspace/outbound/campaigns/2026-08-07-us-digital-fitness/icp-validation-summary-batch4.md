---
product: fitxpress
profile: nick
market: USA
campaign: 2026-08-07-us-digital-fitness
batch: 4
step: icp-validator
status: pending Vadim approval
created: 2026-08-10
---

# ICP Validation Summary — Batch 4 (US Digital Fitness, profile: nick)

## Total scored
**160 / 160** contacts from `people-raw-batch4.csv` classified and written to `people-validated-batch4.csv`.

- **PASS: 15** (P1: 5, P2: 7, P3: 3)
- **WEAK: 16**
- **FAIL: 129**

## FAIL breakdown by bucket (129 total)

| Bucket | Count | Notes |
|---|---|---|
| NOISE (pre-tagged `NOISE:` company rows) | 31 | Homonyms / unrelated employers / self-employed / VC-adjacent: iFit Golf, Echelon Health & Fitness (gym), Space Dynamics Laboratory, undefined, Reddit, Tzorin Cuisine, Tonal Music Inc, Tonal Salon, Tonal Domination Studio, Calibrate Estates/ADHD/Visuals/Network/Clinic/IV Hydration/Bodyworks (x2), A.D.A.S Calibrate, Adaptive ADAS Calibrate, Edge-Calibrate, General Mills, FOX Sports, Vivint, TA Associates, Retailsync, Self-employed (x2), Isle Madame iFit Centre (x2) |
| Non-target role at a target company | ~77 | Bulk of FAILs — HR/talent/payroll, finance/FP&A/accounting/revenue, IT infra/DevOps/security/business-systems, clinical/case-management/UM/compliance, account-management/client-success/sales/BD-territory, logistics/supply-chain/sourcing/procurement/ops, retail/showroom/store/regional managers, execution-level creative/video/broadcast production, hardware/mechanical engineering |
| Other (un-tagged homonym / mismatch / unverifiable) | ~21 | 'Owner'/'Entrepreneur' at Found with no company page (Monica routen, Deshana Ashford, Tracey Egloff); Echelon homonyms — architecture LLC, record labels, university student, generic no-page Directors/CEOs (Kyle Hehenberger, Maurice Hood, Monica Butler, Hilton Foote, Kenzie Flood, Echelon Pro, Darkin Sabestian, Ric Okoniewski, Lindsey Record); 'Future' homonyms (Future Research Inc; two Chinese-titled 总经理/Managing Director rows with no page); 'Train Well' physician-educator venture (not the Trainwell app); generic no-function iFIT/Personify Directors (G A, Melissa Huckins, Steven Ortner, Callista Smith); box-trucking owner mis-tagged to iFIT |
| Geo (non-US-HQ) | 0 | Not applicable — all 13 target companies are fixed/pre-verified US-HQ; the 5 Canada-based individuals were scored on role, not geo (per the company-HQ rule) |

## PASS + WEAK count per target company (31 total)

| Company | PASS | WEAK | Total |
|---|---|---|---|
| iFIT / NordicTrack / FreeMotion / ProForm | 6 | 2 | **8** |
| Calibrate | 1 | 2 | **3** |
| Echelon | 1 | 2 | **3** |
| MyFitnessPal | 2 | 1 | **3** |
| Personify Health | 0 | 2 | **2** |
| Tonal | 0 | 2 | **2** |
| Hydrow | 1 | 1 | **2** |
| Future | 0 | 2 | **2** |
| Found | 0 | 2 | **2** |
| Trainwell | 1 | 0 | **1** |
| Ladder | 1 | 0 | **1** |
| Shotsy | 0 | 0 | **0** |
| **Total** | **15** | **16** | **31** |

No Shotsy contacts appeared in this batch.

## message_angle distribution (across 31 PASS+WEAK)

| Angle | Count |
|---|---|
| member-engagement | 22 |
| weight-management | 5 |
| technical-integration | 3 |
| digital-transformation | 1 |

No clinical-operations / virtual-care / compliance / preventive-health angles were used. The weight-management angle was applied only at the GLP-1 programs (Calibrate, Found) per the explicit exception.

## 5 PASS examples

1. **Matt Spettel — Co-Founder & CEO, Trainwell — P1**, member-engagement. Founder/CEO economic buyer at a human-coach subscription where progress photos are core.
2. **Mandy Cooper — CEO, MyFitnessPal — P1**, member-engagement. Economic buyer at a nutrition/tracking app where verified body metrics are the natural next feature.
3. **Eric Watterson — Sr VP Marketing, iFIT — P1**, member-engagement. Senior marketing leader owning acquisition/retention/brand; primary champion for a retention/visible-progress feature.
4. **Stephanie Slade, PhD — VP Member Care, Calibrate — P2**, weight-management. Senior member-experience/retention owner at a GLP-1 program — direct fit for the fat-vs-lean-mass outcomes wedge.
5. **Josh Bovarnick — VP of Software Engineering, Echelon — P3**, technical-integration. Technical C-level exec sponsor/implementer, correctly routed to the API/SDK angle rather than auto-failed as "just an engineer."

## 5 FAIL examples

1. **Steve Teddy — VP, Client Management, Personify Health** — account/client-management (enterprise) territory, which the brief explicitly excludes for Personify Health.
2. **John Roberts Jr — Technical Director, Hydrow** — title matches the WEAK technical-lead pattern, but the bio is TV/broadcast production, unrelated to software/API integration (same false-positive pattern flagged in batch 3).
3. **Jeff Shapiro — Physician Health Educator, "Train Well"** — a physician-education venture (Yale/Stanford exercise-physiology speaker), not the Trainwell coaching app whose CEO (Matt Spettel) is the real target in this same batch.
4. **Maurice Hood — CEO, Echelon** — bio reveals an independent record label; a homonym, not Echelon Fitness (Echelon produced ~9 homonym rows this batch).
5. **Tracey Egloff — Owner, Found** — generic "Owner" title with no company LinkedIn page, inconsistent with Found's VC-backed structure; one of three likely Found homonyms not pre-tagged NOISE.

## Top concerns

1. **This batch is dominated by non-buyer functions at two big employers.** Personify Health (~50 rows) and iFIT (~35 rows) contributed the overwhelming majority of contacts, but almost all were HR, finance, clinical/case-management, claims, account-management, logistics, or IT — not the consumer-product/member-experience/engagement/digital buyer. Personify Health produced **0 PASS** in this batch. Future pulls for both should filter on titles containing Product / Growth / Engagement / Digital Experience / Retention, not a company-wide export.
2. **Homonym contamination is heavy and only partly pre-tagged.** Beyond the 31 pre-tagged NOISE rows, ~21 more are homonyms/mismatches that slipped through: "Echelon" (record labels, an architecture LLC, a university student, generic no-page CEO/Director rows), "Future" (Future Research Inc + two Chinese-titled rows), "Found"/"Train Well" small-business owners. The common signal is **a target-company name with NO `company_linkedin_url` plus a generic title (Owner/Director/CEO/Manager)** — recommend the normalization step auto-flag these for review before validation.
3. **Title-only matching keeps producing false positives.** "Technical Director" (Hydrow = broadcast), "VP of Instructional Design," and several "Director"/"Manager" strings look like buyer titles but resolve to production, content, ops, or retail once the bio is read. Bios were decisive; a title-only pass would have wrongly promoted several FAILs.
4. **Two duplicate people appear across rows.** Blake Watterson (COO, iFIT) appears twice (rows for `blake-watterson-a016aa167` and `blake-watterson-62937925b`) and Kristen Zedrick (Director of Implementation, Calibrate) appears twice — both scored consistently. De-dupe before import so the same person is not sequenced twice.
5. **Real economic buyers are thin but high-quality.** The 5 P1s are all genuine CEOs/founders or a senior marketing SVP at target apps (Trainwell, Hydrow, Ladder, MyFitnessPal, iFIT). iFIT is again the deepest well (8 PASS+WEAK), skewed toward content/brand/growth leaders rather than a named CPO/Head of Product — no clean product-owner title surfaced for iFIT in this batch.
6. **GLP-1 targets (Calibrate, Found) surfaced mostly clinical/ops staff.** The only senior member-experience owner was Calibrate's VP Member Care; Found produced only a Medical Director (WEAK, influencer) and two homonym owners. A named Head of Product / Growth pull for Calibrate and Found would strengthen the weight-management wedge.

## Recommendations

1. **Send order:** P1 (5) → P3 (3, exec sponsors) → P2 (7) → WEAK (16, lighter-touch / second wave).
2. **Approve for outreach:** the 15 PASS contacts — member-engagement (Trainwell, Hydrow, Ladder, MyFitnessPal, iFIT), weight-management (Calibrate), technical-integration (Echelon).
3. **Hold/deprioritize the 16 WEAK:** mostly manager-level engagement/community/partnership/experience roles, design/content leads, unverified generic "Future"/Personify titles, and clinical/technical influencers without budget.
4. **De-dupe before import:** collapse the duplicate Blake Watterson (iFIT COO) and Kristen Zedrick (Calibrate) rows.
5. **Vadim decision needed:** whether the ~21 un-tagged homonym/mismatch FAILs (especially the three "Found" owners and the generic no-page "Echelon"/"Future" rows) should be manually re-verified on LinkedIn before permanent exclusion.
6. **No Shotsy contacts** appeared — a dedicated Sales Navigator pull is needed if Shotsy is a priority target.
7. Proceed to Vadim's Telegram approval checkpoint before message-sequencer runs on the approved list.

## Vadim — please confirm
1. WEAK group (16 people): include in the campaign (lighter sequence) or exclude?
2. The ~21 un-tagged homonym/mismatch FAILs: re-verify manually, or drop and save closelyhq credits?
