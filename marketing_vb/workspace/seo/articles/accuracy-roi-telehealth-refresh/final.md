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
stage: final
section: full
word_count: 2340
claims_used: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-SCOPE, FXS-MEDICAL, FXS-HIPAA, FXS-GDPR, FXS-RETENTION]
external_sources: [CDC-PCD-2023]
edited_by: seo-editor
edited: 2026-11-02
review_round: 1
review_decisions: review-1-decisions.md
base_text: v1/final.md
editing_passes: 5
ai_density_before: 0.0
ai_density_after: 0.0
claims_verified: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-SCOPE, FXS-MEDICAL, FXS-HIPAA, FXS-GDPR, FXS-RETENTION, CDC-PCD-2023]
changes_summary: |
  - Review round 1 (Asselya Sekerova), applied per review-1-decisions.md. Base: v1/final.md (live since 2026-10-30).
  - P1 / A1: ROI section rebuilt. Variable table is now P, m_before, m_after, c, s, F, I; e, x, d and a are gone. Four formulas verbatim. L7a dropped; L7b directly after the operating-savings formula. Units stated once (net savings per month, payback in months, ROI as a ratio for a period). One sentence on logging exception rate and minutes per exception. Onboarding completion reported separately on a started-onboarding denominator; retention kept as an optional metric with its own denominator and the engagement link. No worked numbers.
  - P1 / A2: comparison H2 verbatim; "verified capture" and the "take on trust" line removed; scan cell verbatim; weight check rewritten as a discrepancy check; Short answer H2 renamed so "verified" names an option only in bullet 1; video column renamed "Staff-observed measurement (video)".
  - P1 / A3: v1 guided-capture paragraph deleted; RTPV sentence verbatim, capture-quality FAQ link, one pilot sentence. Clothing Detector not mentioned. Three scan cells verbatim. Timing phrase verbatim, then the journey note.
  - P1 / A4: repeatability sentence replaced verbatim; body-measurement scope sentence added verbatim after the accuracy short form; no weight-estimation figure.
  - P1 / A5: three text CTAs with different anchors. Early (landing, no modal, 18 words, at 10% of prose), mid after B1 (#bd-modal), final as the last sentence (#bd-modal).
  - P2 / B1: chain paragraph opens with L2, carries L3, ends on the company setting thresholds and no guarantee.
  - P2 / B3: "What stays the same" bullet removed; "or direct observation" added; eligibility FAQ cut to two sentences.
  - P2 / B4: retention sentences removed from the product section; photos FAQ rewritten in compliance.md order; FXS-IDS sentence and claim removed.
  - P2 / B5: CDC paragraph now says it is not an individual error rate; the listed generalizations made conditional; hybrid sentence dropped.
  - P2 / C: company / program / customer split applied; single-use acronyms written out (BMR, API, SDK, DXA); CDC now used twice.
  - D: L2-L10 applied verbatim where marked; L1 not added; L9 H2 verbatim.
  - P3 / E1, E3, E5, E6, E7: three short-answer bullets; FAQ gains the pilot-ROI question (4 questions); Image 1 replaced, Image 2 marked Illustrative; final section rebuilt with L10, pilot design moved from the cost-effective section, final CTA; intro is E7.
  - Length: 2,161 to 2,337 prose words; about 220 words trimmed from image lines, table read-out, ROI notes and the final section to fit the 1,950-2,350 band.
  - No sentence split from reviewer text was needed: no VERBATIM sentence was reworded. The two sentences over 25 words are both VERBATIM (ROI formula line, last intro sentence).
  - QC fix pass 2026-11-02 (seo-qc 18/20, ship with notes), four fixes only:
    - B1: L2 first and L3 verbatim, then two sentences. The first names measurement quality, repeatability, capture usability, and the company's thresholds and exception rules as deciding how many cases reach manual review. The second puts the no-guarantee point before the costs point and ends on "counts only after the new step's costs", leading into the mid CTA.
    - L7b kept verbatim; the next sentence names the excluded costs: the running costs `F` and the one-time costs `I`.
    - "Seen this way..." rewritten: the cost falls on program leaders at those providers, as reviewer time per submission. Keyword "telehealth patient monitoring" and the telehealth AI overview link kept.
    - Hedge stacking: "When fewer cases need review, staff time may fall" removed with the B1 rewrite. No other conditional sentence in the ROI section or the short answer stacked a hedge on its main verb; VERBATIM and mandated "can come from" wording left as is.
    - Prose words 2,337 to 2,340.
self_check: |
  - First pass: the B1 paragraph stacked four "can" hedges in a row. Superseded by the QC fix pass: L2 and L3 verbatim, then two direct sentences.
  - The final section was five imperatives in a row; one sentence now describes the cohorts instead.
  - The pilot-ROI FAQ answer repeated short-answer bullet 3 (lint pair L66~L190, 0.50); rephrased, pair cleared.
  - The FitXpress section opened on a five-sentence spec inventory; split into timing and outputs/delivery.
  - Still formula-heavy in the ROI section, by design (A1). Gate numbers after the QC fix pass: mean_words 13.1, p90 21, over_25 2 (1.5%), over_35 0, near_duplicate_pairs none; repeated_phrases are the precise terms C requires (scan-estimated weight, body-composition estimates, net monthly savings). Detector CLEAN, 0 markers.
---

# Accuracy and Digital Health ROI: Reducing Manual Patient Monitoring

By Vadim Bilan

## Patient volume and the staff time behind body data

(Cover) - Concept: a program dashboard view. One column of self-reported entries with gaps and flags, one column of timestamped structured records. No numbers on the image.

As telehealth and glucagon-like peptide-1 (GLP-1) weight-management programs grow, collecting and checking patient body measurements can demand more staff time. Self-reported information may require follow-up calls, additional checks, or resubmissions.

Mobile body scanning offers another approach. It can standardize how measurements are collected remotely and help companies identify cases that need additional review. Whether this lowers costs depends on the program's accuracy requirements, the frequency of exceptions, and the cost of implementing the workflow.

Comparing the main collection methods and the staff time behind each one gives a digital health company a way to evaluate its operational costs and potential return on investment.

In telehealth patient monitoring, that cost falls on program leaders at telehealth, digital-health, and GLP-1 or weight-management providers, as reviewer time per submission. The wider picture of [remote body data in telehealth workflows](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) is covered in the telehealth AI overview.

**Scope note.** The workflows and the cost model described here are operational. FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility. <!-- claim: FXS-SCOPE --> Eligibility and dosing decisions stay with the program's clinicians. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

For a company weighing these costs, FitXpress provides [remote body measurement for telehealth](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) through two guided smartphone photos. <!-- claim: FXS-SPEED -->

## Short answer: self-reported data and the cost of checking it

- **Self-reported or verified body data: which is more reliable?** Self-reported data is quick to collect but may require additional verification. Verification compares a submitted value with a second source: a device-recorded weight, a staff-observed measurement, or a scan-estimated weight. A scan-estimated weight that differs from the self-reported value flags a discrepancy for review; it does not prove the actual weight.
- **Where the costs come from.** Costs can come from staff minutes per submission, exceptions and resubmissions, and patients who stop at the verification step.
- **How to estimate savings.** Compare timed staff minutes per submission in comparable baseline and pilot cohorts, using the company's own figures.

## Where the manual work comes from as a program grows

Centers for Disease Control and Prevention (CDC) researchers reported in [*Preventing Chronic Disease*](https://www.cdc.gov/pcd/issues/2023/23_0005.htm) that self-reported BMI underestimated the prevalence of severe obesity by 40%. The comparison was against bias-corrected estimates: 5.3% versus 8.8% in 2020 data. <!-- ext-claim: CDC-PCD-2023 --> The CDC finding describes a population. It is not an error rate for an individual submission, where the gap can be larger or smaller. This bias is one reason programs check self-reported weight against another source.

That check creates four kinds of manual work:

- **Verification checks and exception review.** Staff compare submitted values with a second source and review mismatches.
- **Resubmissions.** A blurred photo, a missing weight, or an incomplete form sends the patient back.
- **Follow-up measurement.** Repeat measurements by video call or clinic visit need a staff slot per patient.
- **Documentation after the fact.** Staff assemble a record of what was checked and when, often from several systems.

If the capture and review steps stay the same, staff time tends to grow with patient volume. In remote patient monitoring, the same work can repeat at every check-in.

Onboarding adds a separate cost. Each extra step before a first consult is a point where a patient can stop. When a patient abandons enrollment, the company may not recover its acquisition costs.

## Self-reported vs device-recorded, observed, and scan-estimated body data

A program can combine methods. The [guide to remote BMI verification methods](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) describes the verification workflow itself.

| **Question** | **Self-report** | **Connected scale** | **Staff-observed measurement (video)** | **Guided mobile scan** |
|---|---|---|---|---|
| What the program receives | Height and weight typed into a form | Device-recorded weight; some models estimate body composition, often with bioelectrical impedance analysis (BIA); height is usually a separate input | A measurement a staff member watched the patient take | Scan-estimated weight from two guided live photos and the supplied height, BMI calculated from them, body measurements, and body-composition estimates |
| Where the manual work sits | Downstream, in checking, chasing, and exception review | Device logistics and a separate height entry | Scheduling and running each session | At capture, where pose and framing guidance runs; manual review remains for cases outside the company's rules |
| Staff time per capture | None; review comes later | None | A live session per patient | None |
| Common failure points | Rounded, outdated, or mistyped values | No device at home, or readings that do not sync | No-shows and rescheduling | Pose or framing that does not meet the capture requirements; guidance during capture asks for a correction |
| What a reviewer can see afterwards | The typed values | A device-recorded weight with its timestamp | The staff member's note of the observation | A scan record with processing status, timestamps, and structured outputs |
| Best fit in the program | Sign-up and administrative fields | Routine weight check-ins | Cases where a protocol requires staff to observe | Enrollment, milestones, and progress records at volume |

A connected scale and guided mobile capture move part of the manual work to the capture step. Cases outside the company's rules still go to manual review.

## A digital health ROI model the program fills in

3DLOOK does not supply outcome figures for this model, because the inputs differ by program.

| **Variable** | **What to measure** | **Where the figure comes from** |
|---|---|---|
| `P` | Body-data submissions per month: enrollment captures and repeat check-ins together | Enrollment and check-in logs |
| `m_before` | Average staff minutes per submission on the current process: checking, follow-up, video sessions, record entry, exceptions, and resubmissions | Timed real submissions in the baseline cohort, and exception logs |
| `m_after` | The same measure in the pilot cohort | Timed real submissions in the pilot cohort, and exception logs |
| `c` | Loaded staff cost per hour | Finance or HR |
| `s` | Cost per scan under the company's contract | The vendor quote |
| `F` | Other monthly running costs of the new step, where they apply, such as software and support | The vendor quote and internal estimates |
| `I` | One-time costs, such as integration and staff training | Internal estimates |

The exception rate and the minutes per exception are worth logging, because they explain a change between `m_before` and `m_after`.

(Image 1) - Concept, labeled "Illustrative": baseline and pilot cohorts in three panels (staff minutes per submission, exceptions per submission, onboarding completion on its own started-onboarding denominator). No figures or savings; any text says "three sources of cost".

Monthly operating savings come first:

- Monthly operating savings = `P × (m_before − m_after) × c ÷ 60 − P × s`

The difference shows estimated savings, before accounting for any excluded costs. Those are the running costs `F` and the one-time costs `I`. Three results add them in: net savings is money per month, payback is months, and ROI is a ratio for a stated period.

- Net monthly savings = monthly operating savings − `F`
- Payback period in months = `I ÷ net monthly savings`
- ROI for a chosen period = net savings for the period, minus `I`, divided by the total cost of the new step for that period (scan fees, running costs and `I`)

Onboarding completion is reported separately, outside the savings formula. Verification-step completion is the number of patients who complete the verification step, divided by the number who started onboarding in the same period. Retries and abandonment use the same denominator.

Some programs expect visual progress to affect retention. They can track it as an optional metric on its own denominator, apart from the savings calculation. The article on [patient engagement with mobile body scanning](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/) makes the case for that link.

Better body data can reduce staff verification time when the measurements meet the program's quality requirements. Reliable measurements can reduce the need for repeated checks. Measurement quality, repeatability, and capture usability, along with the company's thresholds and exception rules, decide how many cases reach manual review. The technology alone does not guarantee a lower review workload, and saved staff time counts only after the new step's costs.

The scan fee `s`, running costs `F`, and the integration scope behind `I` come from [a conversation with 3DLOOK about scan volume and integration](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/#bd-modal).

## GLP-1 clinic operations: progress tracking between visits

GLP-1 clinics need progress data between visits, and in-person appointment capacity does not automatically grow with enrollment. The GLP-1 market overview covers [progress-tracking requirements for GLP-1 programs](https://3dlook.ai/content-hub/glp-1-market/).

One possible pattern has three steps:

- **Baseline at enrollment.** The first scan sets the reference point.
- **At-home scans.** Further scans follow at intervals the clinic's protocol sets.
- **Review at the visit.** A clinician reviews the comparison between scans the clinic selects.

(Image 2) - Concept, labeled "Illustrative": a GLP-1 between-visit timeline, from the baseline scan through at-home scans to the clinician visit.

Repeatability is particularly important for longitudinal progress tracking, alongside accuracy. Repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FXS-REPEAT --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.

Each scan can also return body-composition estimates and a scan-estimated weight. <!-- claim: FXS-OUTPUTS --> Clinicians can review these estimates alongside other patient information.

## Where FitXpress fits, and where it does not

FitXpress guides a patient through two photos, front and side, and the scan takes under 45 seconds from the photos to structured results. <!-- claim: FXS-SPEED --> The full enrollment step, including the program's own onboarding inputs, can take longer.

The outputs include 80+ body measurements, along with BMI and basal metabolic rate as calculated metrics and body-composition estimates. <!-- claim: FXS-OUTPUTS --> FitXpress delivers the results into the company's own product through an application programming interface and a software development kit. The FitXpress Admin Panel is an optional interface for monitoring and export, for teams that do not build their own dashboard. <!-- claim: FXS-DELIVERY -->

Real-Time Pose Validation (RTPV) gives pose and framing guidance during capture. The [FitXpress capture-quality FAQ](https://3dlook.ai/content-hub/fitxpress-capture-quality-user-experience-faq/) explains what happens when a capture does not meet the requirements. Whether guided capture changes resubmissions in a given program is something a pilot measures.

For weight checks, the program can compare BMI calculated from the scan-estimated weight with BMI from self-reported weight. Both use the same supplied height. A large difference is a discrepancy to review and does not establish the actual weight. The company sets the threshold and the review rule.

A separate validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. <!-- claim: FXS-ACCURACY --> These figures describe body measurements, not weight, BMI, or body-composition estimates. The [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the reference and conditions behind each figure.

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path. <!-- claim: FXS-POPULATION -->

Inside the program, the scan record is one input to clinician review. Clinical decisions, including treatment eligibility, remain with the care team. <!-- claim: FXS-SCOPE --> Where a protocol requires dual-energy X-ray absorptiometry, BIA, a calibrated scale, or direct observation, that method stays in place. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

The [FitXpress data, privacy, and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) covers the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR). FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. <!-- claim: FXS-HIPAA --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. <!-- claim: FXS-GDPR -->

## When standardized measurement becomes cost-effective

### Self-report with spot checks fits when

- Monthly volume is low enough for staff to review every exception.
- The submitted values fill administrative fields only.
- No review threshold or progress comparison uses them.

### Scheduled observation fits when

- The program has few patients and staff time for live sessions.
- A protocol requires staff to observe the measurement directly.
- Patients already attend visits where measurement can take place.

### Guided remote capture fits when

- Enrollment is growing faster than the review team.
- Clinicians compare scans over time, or a review threshold uses the result.
- Patients stop at the verification step while waiting for a call or visit.

## FAQ

### How can a digital health company measure the ROI of a body-data pilot?

A pilot times staff minutes per submission in two comparable groups: one on the current process, one on the new step. Net monthly savings is the value of the time saved, minus scan fees and running costs. Payback is the one-time costs divided by net monthly savings. Onboarding completion is reported separately, on a started-onboarding denominator.

### Is scan data used to decide eligibility or medication dosing?

No. Prescribing clinicians decide eligibility and dosing, and the scan adds a structured, timestamped record to their review. <!-- claim: FXS-SCOPE -->

### Can a program use self-reported and scan-based data together?

Yes. One approach collects self-reported data at sign-up and adds a scan at enrollment and at program milestones. Self-report then covers administrative fields, and the scan supports review thresholds and progress comparisons.

### What happens to the photos and the scan results?

3DLOOK deletes photos immediately after processing, or within 30 days, per the customer's instructions. Measurements, body-composition estimates, and 3D models are retained unless the customer agreement says otherwise. Deletion is by scan identifier, on request. <!-- claim: FXS-RETENTION --> Copies the company keeps in its own systems follow its own policies. The [privacy and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) covers the details.

## How to evaluate the ROI of remote body measurement

Use actual staff time and verification records to estimate potential savings. Start with the ROI model's inputs on the current workflow, and time both the baseline and the pilot cohort. The two groups should be comparable, pass through consistent stages, and cover periods that match in conditions as well as length. Compare minutes per submission, exceptions, and onboarding completion on the started-onboarding denominator. Then [talk to 3DLOOK about the program's body-data workflow](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/#bd-modal).
