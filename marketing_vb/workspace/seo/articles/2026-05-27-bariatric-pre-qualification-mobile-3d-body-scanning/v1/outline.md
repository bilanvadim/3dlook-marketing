---
phase: 2_outline
article: 2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning
date: 2026-05-27
status: awaiting_approval_before_phase_3
based_on: workspace/seo/articles/2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning/v1/fact-check-report.md
---

# Outline — Bariatric Pre-Qualification Article (v1)

10 H2 structure (condensed from original 16-H2 brief). Target length 2,500–3,000 words. Type A — FX use-case deep-dive. Author: Assel Sekerova.

---

## Header block

- **H1:** Bariatric Pre-Qualification with Mobile 3D Body Scanning: Faster Intake, Cleaner Pre-Auth Documentation
- **Byline:** By **Assel Sekerova**, Marketing Lead at 3DLOOK.
- **Disclaimer block** (early, before H2.1) — bariatric-specific phrasing:
  > "Mobile body scanning solutions described in this article do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions. They produce body measurement and composition data intended as supporting evidence within decisioning workflows operated by licensed bariatric programs and their compliance and payer counterparts."
- **Intro:** Two short paragraphs setting up the operational pain: bariatric programs face rising upstream intake demand, slower documentation cycles, and a verification stack still built around in-clinic measurement. The article covers the gap and how a remote scan-derived body-data layer slots into pre-consult and pre-auth workflows. No stat in the intro — stats live inside H2.1.

---

## H2.1 — Why bariatric programs need faster pre-qualification

**1-line summary:** Frame the operational backdrop — high obesity prevalence, large eligible pool, low completion rate — and why intake is the bottleneck.

**Stats mapped:**
- **FACT 5** — CDC NHANES Aug 2021–Aug 2023: 40.3% adult obesity, 9.4% severe obesity. → `cdc.gov/nchs/products/databriefs/db508.htm`
- **FACT 4** — 33M+ US adults eligible for bariatric surgery; <1% complete annually. → `pmc.ncbi.nlm.nih.gov/articles/PMC10136401/`
- **FACT 1** — ASMBS 2023: 270,089 procedures, sleeve gastrectomy 58%. → `asmbs.org/resources/estimate-of-bariatric-surgery-numbers/`

**Closes with:** transition to the intake gap.

---

## H2.2 — The intake gap: when eligibility gets confirmed too late

**1-line summary:** Define the operational pain — wasted consult slots, manual measurement at the appointment, pre-auth documentation that starts after the consult, patient momentum lost during waiting.

**Stats mapped:**
- **FACT 4** — Pre-op attrition 50–60% in bariatric programs (Surgical Endoscopy 2023 review). → `pmc.ncbi.nlm.nih.gov/articles/PMC10136401/`

**Stylistic note:** No further new sources here; the section is operational-narrative and runs on the attrition figure plus a short list of what manual intake actually looks like today (measurement-only consult slots, paper or scratchpad measurement entry, BMI computed at the visit rather than before it).

---

## H2.3 — The GLP-1 shift: volume contracted, intake complexity rose

**1-line summary:** Honest framing — bariatric procedure volume declined in 2023, but new-consult volume is rising as GLP-1 functions as a gateway. That makes faster, structured pre-qualification more valuable, not less. (Per Vadim's H2.3 approval, this is the corrected framing — `brief_corrections` flag carried to frontmatter.)

**Anchor paragraph (Vadim-approved phrasing):**
> "GLP-1 medications have not replaced bariatric surgery — they have changed who arrives at the consult and when. Procedure volume contracted in 2023, while bariatric program leaders report rising new-consult volume from patients who started on a GLP-1 and escalated. For programs, this means more upstream intake to triage with the same surgical capacity downstream — making faster, structured pre-qualification more valuable, not less."

**Stats mapped:**
- **FACT 2** — JAMA Network Open / Tsai et al.: 8.7% YoY decline 2022→2023 in 17M privately insured. → `statnews.com/2024/10/25/bariatric-surgery-falls-as-glp-1-demand-rises-wegovy-zepbound/`
- **FACT 8** — ACS Bulletin April 2025: Dr. Funk "initial gateway", Dr. Kurian "increase in new consults". → `facs.org/.../bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/`
- **FACT 6** — KFF 2025: 43% of firms 5,000+ workers cover GLP-1 for weight loss, up from 28% prior year. → `kff.org/health-costs/2025-employer-health-benefits-survey/`
- **FACT 3** — JAMA Surgery Aug 2025 / Johns Hopkins: 14% (one in seven) of bariatric patients initiate GLP-1 post-surgery (n=112,858). → `publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs`

**Closes with:** transition to "so what does the program need to capture differently."

---

## H2.4 — What FitXpress captures, and how

**1-line summary:** Brief product explanation — two-photo guided scan, ~45 seconds, BMI + 80+ measurements + body composition estimates, time-stamped + structured + HIPAA-maintained.

**Stats mapped:**
- **FACT 10** — 3DLOOK internal product facts; no external citation.
- Internal link: `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/` ("weight-loss and telehealth")
- Internal link: `https://3dlook.ai/technology/` ("3DLOOK technology page" — for the data-architecture side)

**Stylistic note:** This is the shortest H2 — a positioning paragraph plus 4–5 bullets. Keeps the article from drifting into product-deep-dive territory; the use cases come next.

---

## H2.5 — Pre-qualification: structured body data before the consult ⭐ USE CASE #1

**1-line summary:** Main use-case section #1 — workflow walkthrough of remote scan → structured data delivered to clinic → team reviews before consult → consult focuses on clinical evaluation rather than measurement collection.

**Stats mapped:**
- **FACT 7** — CDC PCD: self-reported BMI underestimated severe obesity by 40% (5.3% vs 8.8%). → `cdc.gov/pcd/issues/2023/23_0005.htm` — used to argue why a remote scan-derived BMI baseline beats a self-reported number before the consult.

**Use Case Summary block placement** (right after the opening paragraph of H2.5, before the workflow walkthrough):
```
### Use Case Summary: Bariatric Pre-Qualification
- **Industry:** Bariatric clinics, surgical weight-loss programs
- **Problem:** Eligibility confirmed too late in intake; consult slots spent on measurement collection rather than clinical evaluation
- **Solution:** FitXpress remote two-photo scan delivers structured body data before the appointment
- **Outputs:** BMI, 80+ body measurements, body composition estimates, time-stamped audit trail
- **Role:** Pre-consult intake step — supporting evidence for clinical review, not clinical decisioning
- **Business value:** Higher consult-to-procedure conversion; reduced measurement-only visits; earlier documentation start
```

**Internal link:** `https://3dlook.ai/for-bmi-verification/` — pointed to from "BMI verification capabilities" anchor.

**Section length:** Longest H2 in the article (~400–450 words). Workflow walkthrough is the substance here.

---

## H2.6 — Pre-auth documentation: cleaner packets, fewer delays ⭐ USE CASE #2

**1-line summary:** Main use-case section #2 — what pre-auth packets typically require, why manual measurements struggle (inconsistent, untimestamped, hard to audit), how time-stamped structured FitXpress data slots into the packet, and the anti-fraud angle (clothing detection, weight cross-check) that supports payer trust.

**Stats mapped:**
- **FACT 9** — Pre-auth windows (qualitative, soft phrasing approved by Vadim — "from a few weeks to several months"). No numeric anchor. No external link.
- Reference to FitXpress's existing BMI verification capabilities: `https://3dlook.ai/for-bmi-verification/`

**Stylistic note:** Workflow language, not feature language. Audit trail framing throughout. Brings in HIPAA-maintained / BAA / encrypted in transit and at rest / role-based access controls as a single compliance paragraph at the end. No HHS breach stat (per fact-check decision — drops a stat from the v3 BMI article that would crowd this section).

**Section length:** Second-longest (~350–400 words).

---

## H2.7 — Post-procedure: turning the baseline into longitudinal tracking

**1-line summary:** Secondary use case — first scan = baseline, subsequent scans = body composition and measurement trends, visual progress tracking for patient engagement. Connects the SEO secondary keywords for "body composition tracking after bariatric surgery" and "bariatric patient monitoring software" naturally without keyword-stuffing.

**Stats mapped:**
- **FACT 3** (light touch) — JAMA Surgery / Johns Hopkins one-in-seven post-surgery GLP-1 finding referenced here to note that longitudinal body-composition tracking matters even more when patients are on adjunct GLP-1 therapy after surgery. → `publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs`

**Stylistic note:** Hedged — "supports tracking", "may indicate", "supports patient engagement". Not "guarantees improved outcomes." Avoids the multivitamin / nutrition supplement intent (per brief — one passing mention of nutrition as part of multidisciplinary care, no more).

**Section length:** Medium (~250 words).

---

## H2.8 — Where FitXpress fits in the bariatric patient journey

**1-line summary:** AEO-friendly journey table — each row a stage, each value is FitXpress role at that stage. Reinforces the "single asset, multiple workflows" thesis.

**Stats mapped:** None — this is a positioning table.

**Table (per brief):**

| Stage | FitXpress role |
|-------|----------------|
| Inquiry | Remote scan captures early body data |
| Pre-consult | Supports pre-qualification review |
| Pre-auth | Provides structured, time-stamped documentation inputs |
| Procedure preparation | Establishes baseline |
| Post-surgery follow-up | Tracks body measurement and composition changes |
| Long-term monitoring | Supports remote progress review |

**Section length:** Short (~150 words — one intro paragraph plus the table).

---

## H2.9 — Why mobile body scanning beats manual measurement workflows

**1-line summary:** Differentiation section. No hardware required. No measurement-only visits. Scalable across high-volume intake. Structured data supports intake, documentation, AND tracking from a single capture — single asset, multiple workflows.

**Stats mapped:** None new. Light callback to **FACT 4** attrition framing (50–60% pre-op dropout → friction reduction matters).

**Stylistic note:** Avoid effusive comparison language ("revolutionary", "transformative" — all banned). Concrete operational contrasts: "in-clinic measurement requires an appointment slot; remote scan does not", "manual tape measurements vary by operator; structured scan outputs are machine-readable and repeatable", "measurement and follow-up are separate captures today; they can be the same workflow."

**Section length:** Medium (~250 words).

---

## H2.10 — FAQ

**1-line summary:** SEO informational-intent block. 9 Q&A pairs — 6 broad-keyword (educational), 3 product-specific. Each answer 2–3 sentences max, no full-section depth.

**Q1.** What is bariatric surgery? *(SEO: "what is bariatric surgery", 12k volume)*
**Q2.** What are common bariatric surgery requirements? *(SEO: "bariatric surgery requirements")*
**Q3.** What are the main types of bariatric surgery? *(SEO: "types of bariatric surgery", 2.6k volume)*
**Q4.** What are the benefits of bariatric surgery? *(SEO: "bariatric surgery benefits", 600 volume)*
**Q5.** What are the side effects of bariatric surgery? *(SEO: "side effects of bariatric surgery", 350 volume)*
**Q6.** What are the pros and cons of weight loss surgery? *(SEO: "pros and cons of weight loss surgery", 350 volume)*
**Q7.** How can bariatric clinics pre-qualify patients remotely? *(product-specific)*
**Q8.** Can FitXpress replace in-clinic measurements? *(product-specific — answer: NO, supporting evidence not replacement)*
**Q9.** How does FitXpress support bariatric pre-auth documentation? *(product-specific)*

**Stylistic note:** Hedged answers. No diagnosis claims. No "guarantees" or "ensures". For Q4–Q6 (educational broad-keyword Qs) — answers stay informational and brief; we are not writing a patient-education page. Each is 2 sentences, factual, no FitXpress mention. Q1–Q3, Q7–Q9 — short factual answers, with Q7–Q9 referencing FitXpress functions.

**Section length:** ~350–400 words across 9 pairs.

---

## CTA block (after FAQ, separate from FAQ)

```
### See FitXpress inside a bariatric intake

See how FitXpress can support pre-qualification, pre-auth documentation, and post-procedure tracking in your bariatric program. [Request a FitXpress demo](https://3dlook.ai/for-bmi-verification/) or contact sales@3dlook.ai.
```

**Audience-CTA discipline:** Compliance-buyer (bariatric program directors, pre-auth coordinators) → demo only, never self-serve trial. Confirmed per style guide section 5.

---

## Related reading block (after CTA)

```
### Related reading

- [AI in Insurance Underwriting: Mobile 3D Body Scanning for Remote Evidence Collection](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/)
- [Wellness Rewards Verification for Employers & Insurers Using AI 3D Body Scanning](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/)
- (Future link, after publish) Online Pharmacy BMI Verification: A 2026 Compliance Guide — to be added once published.
```

---

## Internal-link inventory (target ≥4)

1. `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/` — in H2.4
2. `https://3dlook.ai/technology/` — in H2.4 or H2.6 (architecture context)
3. `https://3dlook.ai/for-bmi-verification/` — in H2.5 and H2.6 (BMI verification capabilities) and CTA
4. `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/` — in Related reading
5. `https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` — in Related reading

**Count: 5 internal links** (meets ≥4 minimum, matches "newer FX article 3–5" range from style guide).

---

## External citation inventory (8 verified sources)

1. ASMBS (procedure volume) — H2.1
2. PMC10136401 (attrition, 33M eligible) — H2.1, H2.2 callback
3. CDC NCHS DB508 (obesity prevalence) — H2.1
4. STAT / JAMA Network Open (Tsai 8.7%) — H2.3
5. ACS Bulletin (Funk + Kurian quotes) — H2.3
6. KFF 2025 EHBS (43% / 28%) — H2.3
7. JAMA Surgery / Johns Hopkins (14% post-surgery GLP-1) — H2.3, H2.7
8. CDC PCD (40% self-report underestimate) — H2.5

---

## Frontmatter (planned for v1/draft-final.md)

```yaml
---
track: seo
product: fitxpress
article_type: use_case_deep_dive
target_keyword: bariatric pre-qualification
secondary_keywords:
  - bariatric surgery requirements
  - bariatric pre-auth documentation
  - bariatric surgery pre-authorization
  - remote bariatric patient intake
  - AI body measurements for bariatric clinics
  - bariatric patient monitoring software
  - body composition tracking after bariatric surgery
  - mobile 3D body scanning
seo_anchor_keyword: bariatric surgery
audience: bariatric clinic administrators, program directors, pre-auth coordinators, telehealth weight-loss platform leads
author: Assel Sekerova
status: in_progress
created: 2026-05-27
version: v1
brief_source: SEO research doc (Vadim, 2026-05-26)
structure_decision: condensed_10_H2 (replaced original 16-H2 brief)
fact_check: workspace/seo/articles/2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning/v1/fact-check-report.md
brief_corrections:
  - "Original brief claimed GLP-1 era expanded bariatric pipeline. Fact-check (ASMBS 2023 estimate, JAMA Network Open / Tsai et al.) showed procedure volume contracted -3.5% YoY in 2023. Article corrected to: volume contracted, intake complexity rose."
---
```

---

## Length plan

| Section | Target words |
|---------|--------------|
| Disclaimer + Intro | 180 |
| H2.1 | 280 |
| H2.2 | 280 |
| H2.3 | 380 |
| H2.4 | 220 |
| H2.5 (use case #1) | 430 |
| H2.6 (use case #2) | 380 |
| H2.7 | 240 |
| H2.8 | 160 |
| H2.9 | 250 |
| H2.10 (FAQ) | 380 |
| CTA + Related reading | 130 |
| **Total** | **~3,310** |

**Note:** Target is 2,500–3,000 (per brief). Currently planning 3,310, which is over the upper bound. I'll trim during drafting — likely shave 100–150 words from H2.5 + H2.6 (the two use-case sections) and 50–80 from FAQ where 2-sentence answers can be 1 sentence. Final target: **2,800–2,950 words**.

---

## Ready for Phase 3

Awaiting Vadim's approval on:
1. The 10-H2 sequence and 1-line summaries
2. Stat-to-section mapping
3. Use Case Summary block phrasing for H2.5
4. Journey table contents in H2.8
5. FAQ Q-list (9 pairs — 6 broad keyword + 3 product-specific)
6. CTA wording + Related reading list
7. Frontmatter shape including `brief_corrections` field
8. Length plan (acknowledging current 3,310 → trim to 2,800–2,950 during draft)

Once approved, I move to Phase 3 — full draft in `workspace/seo/articles/2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning/v1/draft-final.md`.
