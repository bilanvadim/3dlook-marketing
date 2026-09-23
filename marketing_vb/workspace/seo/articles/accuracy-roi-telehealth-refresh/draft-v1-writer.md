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
stage: draft-v1
section: full
word_count: 2135
claims_used: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-SCOPE, FXS-MEDICAL, FXS-HIPAA, FXS-GDPR, FXS-RETENTION, FXS-IDS]
external_sources: [CDC-PCD-2023]
---

# Accuracy and Digital Health ROI: Scaling Patient Monitoring Without More Manual Work

By Vadim Bilan

## Where manual work grows as a telehealth program scales

(Cover) - Concept: a program dashboard view. One column of self-reported entries with gaps and flags, one column of timestamped structured records. No numbers on the image.

A telehealth or glucagon-like peptide-1 (GLP-1) weight-management program doubles its enrollment. Every self-reported height and weight that needs checking, chasing, or re-entering becomes staff time.

The return from better body data rarely comes from a more accurate number alone. It comes from fewer manual touches per patient, at a data quality the program's review workflow accepts.

That makes telehealth patient monitoring an operations question. It sits with operations and program leaders at telehealth, digital-health, and GLP-1 or weight-management providers. The wider picture of [remote body data in telehealth workflows](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) is covered in the telehealth AI overview.

**Scope note.** The workflows and the cost model described here are operational. FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility. <!-- claim: FXS-SCOPE --> Eligibility and dosing decisions stay with the program's clinicians. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

## Short answer: self-reported or verified body data

- **Self-reported or verified: which gives better data?** Verified capture gives the program a record it did not have to take on trust. A connected scale, video-observed measurement, and a guided mobile scan are all verified capture. Self-report is the fastest to collect and needs the most checking downstream. "Better" here means better documented and less manual.
- **Where the cost sits.** Most of it sits in staff minutes per verification, in exceptions and resubmissions, and in patients who stop at the verification step.
- **How to model the return.** Measure those three cost streams before and during a pilot, using the program's own figures.
- **What stays the same.** Clinicians still review the record and make every clinical decision.

## Where the manual work comes from as a program grows

Self-reported height and weight carry a known bias at population level. Centers for Disease Control and Prevention (CDC) researchers reported in [*Preventing Chronic Disease*](https://www.cdc.gov/pcd/issues/2023/23_0005.htm) that self-reported BMI underestimated the prevalence of severe obesity by 40%. The comparison was against bias-corrected estimates: 5.3% versus 8.8% in 2020 data. <!-- ext-claim: CDC-PCD-2023 --> The finding describes a population and does not measure the gap in any single submission. It is one reason programs check self-reported against measured weight at some point.

That check creates four kinds of manual work:

- **Verification checks and exception review.** Staff compare submitted values with a second source and review the cases that do not match.
- **Resubmissions.** A blurred photo, a missing weight, or an incomplete form sends the patient back for another attempt.
- **Follow-up measurement.** Video calls or clinic visits for repeat measurements need a staff slot for each patient.
- **Documentation after the fact.** Staff assemble the record of what was checked and when, often from several systems.

Each of these grows with enrollment. Unless the capture step changes, staff time grows roughly in step with patient volume. In remote patient monitoring, the same work repeats at every check-in.

Onboarding adds a separate cost. Every extra step before a first consult is a point where a started signup can stop. The acquisition spend on that signup is then lost.

## Self-reported vs verified body data: how four capture methods compare

Programs usually combine methods. The practical question is which one fits enrollment, routine monitoring, and exception review. The verification workflow itself is described in the [guide to remote BMI verification methods](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

| **Question** | **Self-report** | **Connected scale** | **Video-observed measurement** | **Guided mobile scan** |
|---|---|---|---|---|
| What the program receives | Height and weight typed into a form | Device-recorded weight; some models estimate body composition, often with bioelectrical impedance analysis (BIA); height is usually a separate input | A measurement a staff member watched the patient take | A weight estimate from two guided live photos and supplied height, BMI calculated from the two, body measurements, and body-composition estimates |
| Where the manual work sits | Downstream, in checking, chasing, and exception review | Device logistics and a separate height entry | Scheduling and running each session | At capture, where the guided flow handles retakes |
| Staff time per capture | None at capture; review comes later | None at capture | A live session per patient | None at capture |
| Typical failure mode | Rounded, outdated, or mistyped values | No device at home, or readings that do not sync | No-shows and rescheduling | Poor lighting, loose clothing, or a wrong pose triggers a retake |
| What a reviewer can see afterwards | The typed values | A device-recorded weight with its timestamp | The staff member's note of the observation | A timestamped scan record with capture-quality flags and structured outputs |
| Best fit in the program | Sign-up and administrative fields | Routine weight check-ins | Cases where a protocol requires staff to observe | Enrollment, milestones, and progress records at volume |

Self-report moves the work downstream to review. Video observation moves it into scheduled staff time. A connected scale and a guided scan move it to the capture step, where software carries most of it. A hybrid of two or three methods is common. Scale-based and photo-based body-composition outputs are both estimates.

## A digital health ROI model the program fills in

3DLOOK does not supply outcome figures for this model, because the inputs differ by program. The model shows what to measure.

| **Variable** | **What to measure** | **Where the figure comes from** |
|---|---|---|
| `P` | Patients or submissions per month that need a body-data step | Enrollment and check-in logs |
| `m` | Staff minutes per manual verification or measurement: checking, chasing, a video session, record entry | A timed sample of real verifications |
| `e` | Share of submissions that need a second touch | Exception and resubmission logs |
| `x` | Staff minutes per exception | A timed sample of exception cases |
| `c` | Loaded staff cost per hour | Finance or HR |
| `d` | Share of started signups lost at the verification step | Funnel analytics at that step |
| `a` | Acquisition cost per started signup | Growth or marketing reporting |
| `s` | Cost per scan or per verification under the program's contract | The vendor quote |

(Image 1) - Concept: three cost streams (staff handling time, exceptions and resubmissions, onboarding drop-off) flow into one "cost per patient onboarded" box, split into "before pilot" and "during pilot". Shows the logic, no figures.

The arithmetic has two lines:

- Monthly handling cost = `P × (m + e × x) × c ÷ 60`
- Monthly drop-off cost = `P × d × a`

Run both lines twice. The first run covers a baseline period on the current workflow. The second covers the pilot period with the new capture step and adds `P × s` as its cost. The difference between the two totals is the return.

Reliable inputs come from records. Time a sample of verifications to set `m` and `x`. Count resubmissions in the logs to set `e`. Measure `d` at the same funnel step in both periods. The same structure works for any health ROI or digital care ROI case that depends on body data.

Some programs expect visual progress to affect retention. They can add retention as a fourth stream and measure it the same way, before and during the pilot. The case for that link is made in the article on [patient engagement with mobile body scanning](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/).

## GLP-1 clinic operations: progress tracking between visits

GLP-1 clinics need progress data between visits, and in-person appointments do not grow with enrollment. The market and its [progress-tracking requirements for GLP-1 programs](https://3dlook.ai/content-hub/glp-1-market/) are covered in the GLP-1 market overview.

A common operational pattern has three steps:

- **Baseline at enrollment.** The patient completes a guided scan when the program starts.
- **At-home scans.** Further scans follow at intervals the clinic's protocol sets.
- **Review at the visit.** A clinician reviews the comparison between scans the clinic selects.

(Image 2) - Concept: a between-visit timeline for a GLP-1 program. Baseline scan at enrollment, at-home scans at program-set intervals, a clinician visit reviewing the comparison.

For GLP-1 progress tracking, repeatability matters more than accuracy. The comparison depends on how consistent repeated scans are. Repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FXS-REPEAT --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.

Each scan can also return body-composition estimates alongside the weight estimate. <!-- claim: FXS-OUTPUTS --> The clinician reads them as estimates within the wider record.

## Where FitXpress fits, and where it does not

FitXpress guides a patient through two photos, front and side, and returns structured outputs in under 45 seconds. <!-- claim: FXS-SPEED --> The outputs include 80+ body measurements, along with BMI and basal metabolic rate (BMR) as calculated metrics and body-composition estimates. <!-- claim: FXS-OUTPUTS --> Programs receive the results through an application programming interface (API) and software development kit (SDK) inside their own product. The FitXpress Admin Panel is an optional interface for monitoring and export, for teams that do not build their own dashboard. <!-- claim: FXS-DELIVERY -->

Guided capture includes real-time pose validation and clothing detection. When a capture is unusable, the guided flow requests a retake. These controls reduce resubmissions; they do not guarantee data quality.

For weight checks, the program compares BMI from the scan's weight estimate with BMI from self-reported weight. Both use the same supplied height. The program sets the threshold and reviews the exceptions.

A separate validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. <!-- claim: FXS-ACCURACY --> What counts as adequate performance depends on how the measurements will be used. The [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the reference and conditions behind each figure.

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path. <!-- claim: FXS-POPULATION -->

FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility. <!-- claim: FXS-SCOPE --> Where a protocol requires dual-energy X-ray absorptiometry (DXA), BIA, or a calibrated scale, that method stays in place. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

The [FitXpress data, privacy, and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) covers the Health Insurance Portability and Accountability Act (HIPAA), the General Data Protection Regulation (GDPR), and data retention. FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. <!-- claim: FXS-HIPAA --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. <!-- claim: FXS-GDPR --> Photos are deleted immediately after processing, or within 30 days under the customer's policy. Measurements, body composition data, and 3D models are retained unless the customer agreement says otherwise, with deletion by scan identifier. <!-- claim: FXS-RETENTION -->

## When standardizing capture pays back, and how to test it

### Self-report with spot checks fits when

- Monthly volume is low enough for staff to review every exception.
- Body data is administrative and feeds no review threshold.
- No program threshold depends on the submitted height or weight.

### Scheduled observation fits when

- The program has few patients and staff time for live sessions.
- A protocol requires staff to observe the measurement directly.
- Patients already attend visits where measurement can take place.

### Guided remote capture fits when

- Enrollment is growing faster than the review team.
- Body data feeds a review threshold or a progress record.
- Staff time per patient is the main constraint on growth.

A pilot tests the model with real figures. Measure the ROI model inputs on the current workflow first. Then run the new capture step with a defined cohort for the same length of time. Compare handling time, exceptions, and drop-off at the same funnel step.

## FAQ

### Does verified body data replace clinician review or a calibrated scale?

No. A guided scan supports clinician review with a structured, timestamped record. DXA, BIA, or a calibrated scale stays in place wherever the program's protocol requires it.

### Is scan data used to decide eligibility or medication dosing?

No. FitXpress supplies body data for clinician review. <!-- claim: FXS-SCOPE --> Treatment eligibility and medication dosing are decided by the program's clinicians.

### Can a program use self-reported and scan-based data together?

Yes. A common pattern collects self-reported data at sign-up and adds a guided scan at enrollment and milestones. Self-report then covers administrative fields, and the scan supports review thresholds and progress comparisons.

### What happens to the photos and the scan results?

Photos are deleted after processing or within 30 days, depending on the customer's policy. Scan results are retained, linked to randomly generated IDs, and deleted by scan identifier on request. <!-- claim: FXS-RETENTION --> <!-- claim: FXS-IDS --> The [privacy and security FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the detailed questions.

## Next steps

Run the ROI model on the current workflow, using timed samples and logged exceptions. Then [talk to 3DLOOK about the program's body-data workflow](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/#bd-modal).
