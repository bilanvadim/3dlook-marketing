---
slug: accuracy-drives-roi-digital-health
workspace: accuracy-roi-telehealth-refresh
product: fitxpress
primary_keyword: digital health roi
primary_use_case: brand-assets/product-info/use-cases/fx-telehealth-weight-loss.md
hub: "Hub 2 — AI in Telehealth"
cluster: Scale
secondary_hub: "Hub 3 — GLP-1 Market & Progress Tracking (cluster: Clinic operations, section only)"
intent: BOFU
action_type: refresh-expand-in-place
priority: P2
target_words: 2150
live_url: https://3dlook.ai/content-hub/accuracy-drives-roi-digital-health/
baseline_file: published-live-2026-09-23.md
baseline_words: ~1280
author: Vadim Bilan
audit: plan-audit.md
status: approved
approved_by: auto-pipeline (no-checkpoint mode, 2026-09-21)
created: 2026-09-23
---

# SEO Plan — Accuracy Drives ROI in Digital Health, refresh in place

**Republish at the existing URL. The slug does not change.** No net-new page.
Everything below is a rewrite against `published-live-2026-09-23.md` (~1,280 words, 5 H2s, no FAQ).
Google dropped the page from the index on 2026-09-20 ("Crawled – currently not indexed", a quality
judgement). The refresh has to fix quality, not only add words.

Reasoning, rejected alternatives and open items live in `plan-audit.md`. This file is what the
writer needs.

---

## Content Strategy Fit (Phase 0)

- **Hub / cluster:** Hub 2 — AI in Telehealth → Scale (primary). Hub 3 — GLP-1 Market & Progress
  Tracking → Clinic operations, delivered as **one section** of this page, not a standalone article.
- **Action type (verbatim from the sheet):** row 1 `Refresh / expand existing` (P2, Executive/BOFU,
  "Expand accuracy-drives-roi-digital-health (or a linked BOFU article)"); row 2 `Create if validated`
  (P2, BOFU, "Section in accuracy-drives-roi-digital-health, or standalone if targeting clinic
  operators"). Both are non-create families and the gate would normally STOP.
  **Gate overridden: Vadim gave an explicit «го» on 2026-09-23** after reading the diagnosis in
  Telegram. Precedent: `bariatric-hub-refresh` (09-03), `glp-1-market` (08-28),
  `online-pharmacy-bmi-verification` (08-24), each a refresh/expand row republished in place.
  `already_live: true` is expected: this URL is the refresh target.
- **Existing pages and how they are used:**
  - this page: refresh target.
  - `the-potential-of-ai-in-telehealth`: link up; do not re-survey telehealth AI.
  - `online-pharmacy-bmi-verification-a-2026-compliance-guide`: link sideways for the verification
    workflow; our comparison table must agree with its "Remote verification methods".
  - `mobile-body-scanning-patient-engagement`: link sideways for retention only.
  - `glp-1-market`: link up from the GLP-1 section; no market figures here.
  - `mobile-body-scanning-accuracy`, `fitxpress-data-privacy-security-regulatory-faq`: trust anchors.
  - `structured-body-data-for-telehealth-digital-health-programs`: link down, the CTA target.
  - `telehealth-documentation-ai-body-scanning`: **not live.** Documentation may be named as one
    source of manual work, in one sentence, with no link.
- **Cannibalization guardrail, and how it is honoured:** this page owns one intent: *how much manual
  work body-data verification and monitoring create as a program grows, and how to model the return
  of standardizing the capture step.* It does not explain how to verify BMI (BMI guide), does not
  survey AI in telehealth (hub), does not argue engagement (engagement article), does not size the
  GLP-1 market (glp-1-market), does not explain accuracy methodology (framework).
- **Vertical boundary:** Telehealth owns remote-care workflows, documentation, privacy, remote
  monitoring. GLP-1 owns progress tracking and clinic workflows. **Not allowed anywhere on the
  page:** eligibility decisions, dosing, diagnosis, treatment recommendations, fraud detection,
  replacement of clinician review, DXA (dual-energy X-ray absorptiometry), BIA or a calibrated
  scale, guaranteed compliance, and any 3DLOOK-supplied ROI or outcome figure.
- **Sensitive verticals:** telehealth and GLP-1 both apply. Scope note before Section 2.
- **Internal links planned:** up → `the-potential-of-ai-in-telehealth`, `glp-1-market` · side →
  `online-pharmacy-bmi-verification-a-2026-compliance-guide`, `mobile-body-scanning-patient-engagement`
  · down → `structured-body-data-for-telehealth-digital-health-programs` · trust →
  `mobile-body-scanning-accuracy`, `fitxpress-data-privacy-security-regulatory-faq`.

---

## Keyword Analysis (Phase 1)

Ahrefs API v3, `country=us`, pulled 2026-09-23 (files in `workspace/seo/_keywords/2026-09-23-accuracy-roi-telehealth-refresh*.yaml`).
`null` is written "no data" and is not zero.

**Honest line: this is a thin-demand page.** The primary term measures 40/month. The strongest real
signal is Search Console, not Ahrefs: the question-shaped "self-reported vs verified" family, which
Ahrefs has no data for, sits at positions 4-9. The page's job is GEO answer capture on that
question, BOFU sales support, and closing the internal-link gap to the telehealth hub. Not volume.

### Primary cluster

- **Primary keyword:** `digital health roi`
- **Monthly volume:** 40 · **Difficulty:** 0 · CPC: no data
- **Search Console:** 115 impressions, average position 18.0 (Jan-Sep 2026)
- **Seed had data:** true. The term stays because the URL and title already rank for it and it names
  the page's promise. Do not over-index on it: use it in the H1 area, the short answer and one H2
  area, no more.

### Secondary clusters

| Cluster | Keywords | Intent | Volume / KD | Where woven |
|---|---|---|---|---|
| Self-reported vs verified (GEO) | `self-reported vs verified data accuracy`, `which platforms provide better data accuracy, self-reported or verified`, `self-reported vs measured weight` | Informational, question-shaped | Ahrefs: no data (all variants). Search Console: 93 impr. pos 4.1 · 13 impr. pos 6.7 · 10 impr. pos 8.6 | Section 2 (first bullet answers it directly), Section 4 H2 and table |
| Telehealth patient monitoring | `telehealth patient monitoring`, `patient monitoring` | Informational / commercial | 100 / KD 26 · 800 / KD 33 | H1, Sections 1, 3 |
| Remote patient monitoring | `remote patient monitoring`, `benefits of remote patient monitoring` | Informational + commercial | 6,800 / KD 51 · 200 / KD 37 | Sections 3 and 6, once each. **Do not chase:** the SERP is RPM software and reimbursement, which this page does not own |
| Health / care ROI | `health roi`, `digital care roi` | Informational | 70 / KD 1 · Ahrefs no data (SC: 20 impr., pos 24.1) | Section 5 |
| GLP-1 clinic operations | `glp-1 progress tracking`, `glp-1 clinic workflow` | Commercial | not pulled for this run | Section 6 only |

---

## Recommended Title

**H1:** **Accuracy and ROI in Digital Health: Scaling Patient Monitoring Without More Manual Work**

Keeps "Accuracy" and "ROI" (the words the URL has ranked for) in the first five words and puts the
content-plan row's working title after the colon. 14 words, 86 characters: fine for an H1, too long
for a SERP title.

**SEO title (for `seo-publisher`):** `Accuracy and ROI in Digital Health: Self-Reported vs Verified Data`
(66 characters). It carries the position 4-9 question into the snippet.

**Meta description (direction only):** lead with the manual work that grows with patient volume and
the reader-filled ROI model. Do not open with FitXpress.

### Other options

1. **Accuracy Drives ROI in Digital Health** (live H1, unchanged): no signal of what changed, and the
   verb is the claim the page can no longer make with numbers.
2. **Digital Health ROI: Self-Reported vs Verified Body Data at Scale**: strongest keyword fit, but
   drops "Accuracy" from the front and reads as a comparison-only page. Used as the SEO title instead.
3. **How Telehealth Programs Scale Patient Monitoring Without More Manual Work**: the content-plan
   title verbatim. Loses both ranked words.
4. **Accuracy and ROI in Digital Health: A Workflow Comparison**: the editorial-rewrites §7 pattern.
   Not chosen because the page's core asset is the ROI model, not the comparison.

---

## Article Outline

Structure: the 12-part standard compressed into 10 sections, using the comparison/workflow format of
`editorial-rewrites.md` §7 where it fits (bold scope note, short answer bullets, one comparison
table, a decision framework with three H3s, FAQ, two-sentence next steps). The hub pages own "What
FitXpress does not do" as a full section; here the boundary sits in the scope note and in Section 7.

**Nothing on the live page is safe to paste.** It has 20 em dashes, Title Case headings and five
compliance defects. Where a section says "carry over", the argument survives, not the sentence.

### Visuals

| Name | Placement | Concept |
|---|---|---|
| Cover | Top, under the H1 area | A program dashboard view: one column of self-reported entries with gaps and flags, one column of timestamped structured records. No numbers on the image. |
| Image 1 | Section 5, after the model table | The three cost streams (staff handling time, exceptions and resubmissions, onboarding drop-off) flowing into one "cost per patient onboarded" box, with a "before pilot / during pilot" split. Shows the logic, not figures. |
| Image 2 | Section 6 | A between-visit timeline for a GLP-1 program: baseline scan at enrollment, at-home scans at program-set intervals, clinician visit reviewing the comparison. |

### Section 1. Opening: the manual work that grows with patient volume

- **Goal:** state the operational problem in the first two sentences and put the boundary on the
  page before any argument.
- **Word budget:** 180
- **refresh_action:** REWRITE (live intro paragraphs 1-2 and "The Hidden Costs of Inaccuracy" opening)
- **Must-cover:**
  1. The scene in two sentences: a telehealth or GLP-1 program doubles enrollment; every self-reported
     height and weight that needs checking, chasing or re-entering becomes staff time.
  2. The reframe as a plain statement: the return does not come from a more accurate number in
     isolation. It comes from fewer manual touches per patient at a data quality the program's
     review workflow accepts. (Do not quote "Accurate enough for which decision?"; this is not an
     accuracy piece.)
  3. Name the audience by actor: operations and program leaders at telehealth, digital-health and
     GLP-1/weight-management providers.
  4. Link up to the telehealth hub on an anchor about remote body data in telehealth workflows.
  5. **`**Scope note.**`** as a bold-label paragraph, 4-5 short sentences: the page describes
     operational workflows and a cost model; FitXpress does not diagnose conditions, make clinical
     decisions, or determine treatment eligibility; dosing and eligibility stay with the program's
     clinicians; FitXpress is not a medical device. "This article" is allowed only inside this note.
- **Keywords:** `telehealth patient monitoring`, `digital health roi`
- **Internal link:** up → https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/
- **Approved claims:** FXS-MEDICAL, FXS-SCOPE (condensed)
- **Boundary:** no "precision medicine" opening, no "eligibility without ambiguity" line (both live
  defects in spirit: they promise decisioning).

### Section 2. Short answer

- **Goal:** a GEO/AEO block an LLM can lift. The first bullet answers the position 4.1 query.
- **Word budget:** 150
- **refresh_action:** NEW
- **Must-cover:** 4 bullets, each a bold label and one or two sentences.
  1. **Self-reported or verified: which gives better data?** Verified capture (a connected scale,
     video-observed measurement or a guided mobile scan) gives the program a record it did not have to
     take on trust. Self-report is fastest to collect and needs the most checking downstream.
  2. **Where the cost sits:** in staff minutes per verification, exceptions and resubmissions, and
     patients who drop off at the verification step.
  3. **How to model the return:** measure those three streams before and during a pilot, with the
     program's own figures.
  4. **What does not change:** clinicians still review and decide.
- **Keywords:** `self-reported vs verified data accuracy`, `digital health roi`
- **Approved claims:** none
- **Boundary:** "better" means better documented and less manual, never "clinically correct".

### Section 3. Where the manual work comes from as a program grows

- **Goal:** break the cost into named components, with one population-level source on self-report.
- **Word budget:** 250
- **refresh_action:** REWRITE (live "The Hidden Costs of Inaccuracy in Digital Health")
- **Must-cover:**
  1. One evidence paragraph on self-report limits. **Preferred source:** CDC researchers in
     *Preventing Chronic Disease*: self-reported BMI underestimated severe obesity prevalence by 40%
     against bias-corrected estimates (5.3% vs 8.8%, 2020 data). This is the figure the BMI guide
     already carries, so the two pages agree. State that it is population-level and does not
     measure error in any single submission. **Writer: verify with WebSearch against the primary
     source, else cut.**
  2. The four sources of manual work, as bold-label bullets: verification checks and exception
     review; resubmissions when a photo, weight or form is unusable; manual measurement scheduling
     for follow-up (video calls, clinic visits); documentation assembled after the fact (one
     sentence only, no link: a separate article will own documentation consistency).
  3. The scaling point: each of these grows with enrollment, so staff time grows roughly in step
     with patient volume unless the capture step changes. Phrase as reasoning, no figure.
  4. Onboarding drop-off: every extra step before a first consult is a point where a started signup
     can stop. Acquisition spend on that signup is lost. No percentage.
- **Keywords:** `telehealth patient monitoring`, `remote patient monitoring` (once), `self-reported vs measured weight`
- **Sources:** https://www.cdc.gov/pcd/issues/2023/23_0005.htm
- **Unsupported numbers from the live page (each: writer: verify with WebSearch against the primary source, else cut):**
  - NHANES self-report bias "height +~1 cm, weight -0.75 kg, BMI -0.6" (live link PMC2784464).
    Default: **cut**, the CDC figure above carries the point. Keep only if the primary paper states
    exactly these values for the population named.
  - PLOS "10-20% misclassification rates for treatment eligibility" (live link
    journals.plos.org/plosone/…0231229). Default: **cut** unless the paper says treatment
    eligibility in those words.
  - "approximately 40% of adults lack access to scales at home" (no source). Default: **cut**.
  - "Regulatory bodies now demand [...] documented verification": **cut** (unsourced, and the live
    sentence uses a banned word about our output). Replace with nothing, or with one specific cited
    requirement if the writer finds one; do not generalise.
- **Approved claims:** none
- **Boundary:** no "patients manipulate photos to meet thresholds" framing. No regulatory claim
  without a named rule.

### Section 4. Self-reported vs verified body data: how four capture methods compare

- **Goal:** the table behind the position 4-9 queries. It compares where the manual work sits, not
  which method "wins".
- **Word budget:** 280 (lead-in, table cells, reading)
- **refresh_action:** NEW
- **Must-cover:**
  1. Two-sentence lead-in: programs usually combine methods; the question is which one fits each
     stage (enrollment, routine monitoring, exception review). Link the BMI guide on an anchor about
     remote BMI verification methods, and say the verification workflow itself is described there.
  2. **One table**, bold header row, methods as columns: Self-report · Connected scale ·
     Video-observed measurement · Guided mobile scan. Rows (6, max 8):
     - What the program receives
     - Where the manual work sits
     - Staff time per capture (words, not minutes: "none at capture", "a live session per patient")
     - Typical failure mode
     - What a reviewer can see afterwards
     - Best fit in the program
  3. **Consistency rules with the BMI guide** (do not contradict it): connected scale = device-recorded
     weight, may estimate body composition depending on the model (many use BIA, bioelectrical
     impedance analysis), height usually a separate input, no body measurements. Video-observed =
     staff observe the measurement directly, needs staff time per session. Guided scan = two guided
     live photos plus supplied height produce a weight estimate, BMI calculated from supplied height
     and the estimated weight, body measurements and body-composition estimates. Both scale and
     photo-based composition outputs are estimates.
  4. Three-sentence reading after the table: self-report moves the work downstream to review;
     video moves it to scheduled staff time; scale and guided scan move it to the capture step, where
     it scales with software instead of staff. A hybrid is common.
- **Keywords:** `self-reported vs verified data accuracy`, `self-reported vs measured weight`
- **Internal link:** side → https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/
- **Approved claims:** none in the table. No accuracy figure in this section.
- **Boundary:** no row on "fraud prevention". The guided-scan failure mode is stated honestly
  (poor lighting, loose clothing, wrong pose trigger a retake; outputs are estimates). No named
  competitors, no pricing.

### Section 5. A transparent ROI model the program fills in

- **Goal:** replace every live ROI figure with a model built from the program's own numbers. This
  section is why an operations lead bookmarks the page.
- **Word budget:** 350
- **refresh_action:** REWRITE (live "Data Accuracy That Pays Off" and the retention arithmetic in
  "From Trust to Retention")
- **Must-cover:**
  1. One sentence: 3DLOOK does not supply outcome figures here, because the inputs differ by program;
     the model shows what to measure.
  2. **A variables table**, `Variable | What to measure | Where the figure comes from`:
     - `P` patients or submissions per month that need a body-data step
     - `m` staff minutes per manual verification or measurement (checking, chasing, a video session,
       record entry)
     - `e` share of submissions needing a second touch (exception or resubmission)
     - `x` staff minutes per exception
     - `c` loaded staff cost per hour
     - `d` share of started signups lost at the verification step
     - `a` acquisition cost per started signup
     - `s` cost per scan or per verification under the program's contract (from the vendor quote;
       **no price on the page**)
  3. The arithmetic in plain words (a formula line is fine):
     monthly handling cost = `P × (m + e × x) × c ÷ 60`; monthly drop-off cost = `P × d × a`.
     Run it twice: a baseline period on the current workflow, then the pilot period with the new
     capture step, adding `P × s`. The return is the difference.
  4. How to get honest inputs: time a sample of verifications instead of estimating; count
     resubmissions from logs; measure `d` at the same funnel step in both periods.
  5. Retention as an optional fourth stream, in one or two sentences: programs that expect
     visual progress to affect retention can add it, measured the same way. Link the engagement
     article for that argument; no retention figure here.
  6. `(Image 1) - Concept` after the table.
- **Keywords:** `digital health roi`, `health roi`, `digital care roi`
- **Internal link:** side → https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/
- **Unsupported numbers from the live page, all CUT by default (writer: verify with WebSearch
  against the primary source, else cut; the live page cites only "internal reviews from telehealth
  providers", so expect to cut):**
  - "up to ten minutes per patient"
  - "16 hours of verification work and 1.25 hours, a 93% reduction" (100 patients/day)
  - "lift consultation capacity by up to 20% without adding staff"
  - "80% to 90% monthly retention … 10 months instead of 5 … roughly $5-6 million" (10,000-patient
    clinic at $100/month). Hypothetical arithmetic presented as an outcome; cut in full.
- **Approved claims:** FXS-SPEED only, and only if the section needs the capture time as context
  ("under 45 seconds", no other timing variant).
- **Boundary:** no worked example with invented figures, no customer figure attached to the model,
  no pricing. Do not name UK Meds or Yazen in this section.

### Section 6. GLP-1 clinic operations: progress tracking between visits

- **Goal:** answer the second content-plan row in one short operational section: how a GLP-1 clinic
  keeps progress data coming in as patient numbers grow, without adding in-person visits.
- **Word budget:** 200
- **refresh_action:** NEW
- **Must-cover:**
  1. One sentence of context and a link up to `glp-1-market` for the market and progress-tracking
     requirements. **No market size, prescription growth or coverage figure.**
  2. The operational pattern: baseline capture at enrollment, at-home captures at intervals the
     clinic's protocol sets, clinician review of the comparison at the scheduled visit. The clinic
     compares scans it selects (never "FitXpress tracks each patient").
  3. Why repeatability matters more than accuracy for this use. FXS-REPEAT in the
     `accuracy-formulations.md` §5 short form: "Repeatability testing used a real-world customer
     dataset with five scans per participant. For most of the evaluated measurements, typical
     scan-to-scan differences remained below 1 cm." Link the accuracy framework
     (https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) **in this paragraph**.
  4. Body-composition estimates alongside weight, stated as estimates.
  5. `(Image 2) - Concept`.
- **Keywords:** `glp-1 progress tracking`, `remote patient monitoring` (only if not used in S3)
- **Internal links:** up → https://3dlook.ai/content-hub/glp-1-market/ · trust →
  https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/
- **Approved claims:** FXS-REPEAT, FXS-OUTPUTS (composition half)
- **Boundary:** hard. No dosing, no titration, no "muscle preservation" claim, no plateau detection,
  no statement about what the clinician should decide. The accuracy figure stays in Section 7,
  never in this section.

### Section 7. Where FitXpress fits, and where it does not

- **Goal:** product mechanics and limits in one place, replacing the live "Deploying FitXpress" list
  and every defect in it.
- **Word budget:** 280
- **refresh_action:** REWRITE (live "Deploying FitXpress Without Operational Disruption",
  "Personalization Built on Reality", "Proven Use Cases")
- **Must-cover:**
  1. What it provides, three short sentences: two guided photos, structured outputs in under 45
     seconds (FXS-SPEED); 80+ body measurements, along with BMI and BMR as calculated metrics and
     body-composition estimates (FXS-OUTPUTS, correct terminology); delivered through API and SDK
     into the program's own product, with the Admin Panel as an optional interface for monitoring
     and export for teams that do not build a dashboard (FXS-DELIVERY, this order).
  2. Capture controls, as canon describes them: guided capture with real-time pose validation and
     clothing detection, which request a retake when the capture is unusable. They reduce
     resubmissions; they do not guarantee data quality.
  3. Weight comparison, stated as the BMI guide states it: the program compares BMI from the scan's
     weight estimate with BMI from self-reported weight using the same supplied height, against a
     threshold the program sets. Review of exceptions stays with the program.
  4. **Accuracy paragraph, on its own:** the `accuracy-formulations.md` §5 short form ("A separate
     validation compared FitXpress measurements with expert pattern-maker tape measurements. Across
     the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical
     absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under
     a non-disclosure agreement."), followed by "What counts as adequate performance depends on how
     the measurements will be used." Link the framework
     (https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) **in this paragraph**. No ISO
     figure anywhere on the page.
  5. Population limit, FXS-POPULATION, all three sentences.
  6. Boundary in two sentences: FitXpress does not diagnose conditions, make clinical decisions, or
     determine treatment eligibility, and it does not replace DXA, BIA or a calibrated scale where a
     protocol requires them. FitXpress is not a medical device.
  7. **Privacy paragraph, four sentences:** FXS-HIPAA verbatim; FXS-GDPR verbatim; photos deleted
     immediately after processing or within 30 days under the customer's policy, while measurements,
     body-composition estimates and 3D models are retained unless the agreement says otherwise, with
     deletion by scan identifier (FXS-RETENTION); link the trust FAQ for the rest.
  8. Optional, one sentence: guided capture already runs at volume in weight-loss programs, for
     example Yazen with 34,000 scans in 2025 (FX-YAZEN). Not attached to any ROI claim.
- **Keywords:** `telehealth patient monitoring`
- **Internal links:** trust → https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ · trust →
  https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- **Approved claims:** FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY (short form), FXS-POPULATION,
  FXS-SCOPE, FXS-MEDICAL, FXS-HIPAA, FXS-GDPR, FXS-RETENTION, FX-YAZEN (optional)
- **Boundary:** every live defect dies here. See the defect checklist below.

### Section 8. When standardizing capture pays back, and how to test it

- **Goal:** decision framework plus a three-sentence pilot, per `editorial-rewrites.md` §7.
- **Word budget:** 180
- **refresh_action:** NEW
- **Must-cover:**
  1. Three H3s, 3-4 bullets each, every bullet a complete sentence of about ten words:
     - **Self-report with spot checks fits when**: low volume, body data is administrative, no
       threshold depends on it.
     - **Scheduled observation fits when**: few patients, a protocol requires staff to observe the
       measurement, visits happen anyway.
     - **Guided remote capture fits when**: volume is growing, body data feeds a review threshold or a
       progress record, and staff time per patient is the constraint.
  2. Pilot in three sentences: measure the Section 5 inputs on the current workflow first; run the
     new capture step on a defined cohort for the same period; compare handling time, exceptions and
     drop-off at the same funnel step.
- **Keywords:** `digital health roi`
- **Approved claims:** none
- **Boundary:** no metrics table, no diligence-question list (the BMI guide owns the vendor
  checklist).

### Section 9. FAQ

- **Goal:** GEO/AEO answers, 2-4 sentences each, no question that a body section already answers.
- **Word budget:** 230
- **refresh_action:** NEW (the live page has no FAQ)
- **Questions (4):**
  1. Does verified body data replace clinician review or a calibrated scale? No; it supports review;
     DXA, BIA or a scale stay where the protocol requires them.
  2. Is scan data used to decide eligibility or medication dosing? No; FitXpress does not diagnose
     conditions, make clinical decisions, or determine treatment eligibility; the program's
     clinicians decide.
  3. Can a program use self-reported and scan-based data together? Yes, for example self-report at
     sign-up and a guided scan at enrollment and milestones.
  4. What happens to the photos and the scan results? One-sentence summary of FXS-RETENTION and
     FXS-IDS, then link the trust FAQ. Do not restate its answers beyond that.
- **Keywords:** one secondary term per answer where natural
- **Internal link:** trust → https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
- **Approved claims:** FXS-RETENTION, FXS-IDS, FXS-SCOPE
- **Boundary:** any figure repeated here must be byte-identical to the body. Prefer none.

### Section 10. Next steps

- **Goal:** BOFU CTA, direct, one only.
- **Word budget:** 40
- **refresh_action:** REWRITE (live "The Path Forward" and CTA)
- **Must-cover:** two sentences. First: run the Section 5 model on the current workflow. Second
  starts with "Then" and carries the CTA: talk to 3DLOOK about the program's workflow, linking
  https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ (demo modal as on
  the live page). Drop the live "Further reading" block unless the publisher confirms each link is
  live and relevant; never add a second CTA in the body.
- **Approved claims:** none
- **Boundary:** no "eliminate guesswork", no "proven path", no "measurably improved outcomes".

---

## Live defects: writer checklist (every row must be gone from the draft)

| Live text | Replace with |
|---|---|
| "HIPAA- and GDPR-compliant" | FXS-HIPAA + FXS-GDPR verbatim, link trust FAQ (S7) |
| "automatic photo deletion after model generation" | photos deleted immediately or within 30 days per customer policy; outputs retained (FXS-RETENTION) |
| "medical-grade measurements" / "medical-grade precision" | §5 accuracy short form + "FitXpress is not a medical device." |
| "Dose medications accurately." | removed; intended-use sentence (S1 scope note, S7, FAQ 2) |
| "prevents altered photos, ensuring trustworthy data" / "Fraud prevention" label | pose validation and clothing detection request retakes; no fraud framing |
| "eliminates weight discrepancies" | program compares scan-based and self-reported BMI against its own threshold |
| "over 80 precise body metrics, including … BMI, fat percentage, lean mass" | "80+ body measurements", BMI/BMR calculated metrics, composition estimates |
| "Regulatory bodies now demand [...] documented verification" | cut |
| the live accuracy sentence in "Deploying FitXpress" | §5 short form in S7, framework link in the paragraph |
| em dashes (20), Title Case H2/H3 (12), the four banned words and connectors the gap analysis lists | editor pass; sentence-case headings |
| "Scaling from 1,000 to 100,000 patients requires no new infrastructure" | cut (unsourced) |
| "deployment in weeks, not months" | cut (unsourced timing) |
| "the benefits of in-house R&D, without the cost, delay, or compliance overhead" | cut |
| "Track progress with medical-grade precision" / "measured fat loss and muscle preservation" | cut; S6 repeatability framing |

---

## Article meta

| Section | Words | refresh_action |
|---|---|---|
| 1. Opening + scope note | 180 | REWRITE |
| 2. Short answer | 150 | NEW |
| 3. Where the manual work comes from | 250 | REWRITE |
| 4. Self-reported vs verified: four methods | 280 | NEW |
| 5. ROI model | 350 | REWRITE |
| 6. GLP-1 clinic operations | 200 | NEW |
| 7. Where FitXpress fits, and where it does not | 280 | REWRITE |
| 8. When it pays back, and how to test it | 180 | NEW |
| 9. FAQ (4) | 230 | NEW |
| 10. Next steps | 40 | REWRITE |
| **Total** | **2140** | |

- **Target:** 2,150 prose words (frontmatter `target_words`). Baseline ~1,280. The ~870-word
  increase is the three new assets (comparison table + reading, ROI model, GLP-1 section) and the FAQ;
  the cut unsupported numbers and repeated use-case list free about 350 words of the baseline.
  Comparable editorial finals in this format land near 1,900; this page carries one extra asset
  (the model), hence slightly above.
- **Read time:** about 9 minutes.
- **CTA placement:** once, Section 10.
- **H2 count:** 10.
- **Byline:** Vadim Bilan (kept; flag in the digest).
- **Sentence length:** mean ≤ 16 words (article_lint gate 10). Reference shape:
  `brand-assets/past-articles/blog/manual-vs-digital-intake-occupational-health-screening.md`.

### Internal links, four directions

| Direction | Target | Where |
|---|---|---|
| up | https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/ | S1 |
| up | https://3dlook.ai/content-hub/glp-1-market/ | S6 |
| side | https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/ | S4 |
| side | https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/ | S5 |
| side | telehealth-documentation-ai-body-scanning | **no link**, not live; one-sentence mention in S3 |
| down | https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/ | S10 (and optionally S7) |
| trust | https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ | S6 repeatability paragraph, S7 accuracy paragraph |
| trust | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | S7 privacy paragraph, FAQ 4 |

Descriptive anchors only. 7-8 curated links in the body.

### Writer notes

1. Accuracy and repeatability sentences are copied from `accuracy-formulations.md` §5, never rebuilt
   from numbers, and each carries the framework link
   (https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) in its own paragraph. Accuracy
   lives in S7, repeatability in S6. No ISO 8559 figure on the page. No internal
   repeatability-consistency percentage.
2. The only FitXpress timing figure is "under 45 seconds". No "40 seconds", no "under a minute".
3. Expand DXA, BIA, API, SDK, BMR, GLP-1 (glucagon-like peptide-1), HIPAA, GDPR at first use. Do not
   expand BMI, US, UK, EU, AI.
4. Reserved words are off-limits about our own evidence (see the hard-bans card). The banned word
   for "unbiased" data is off-limits about our output.
5. No figure enters the page unless it is in the pack's approved claims or verified by WebSearch
   against a primary source in this run, with the URL recorded in the draft's source notes.
6. `slug` in every downstream artifact is `accuracy-drives-roi-digital-health`, not the workspace
   name.
