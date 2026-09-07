---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
section: full
status: edited
title: "Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams"
meta_description: "See how obesity care teams can use remote body data for bariatric pre-qualification, intake, pre-auth preparation, and post-op progress tracking."
primary_keyword: bariatric pre-qualification
hub: Hub 6 - Bariatrics
cluster: Main hub
intent: Hub (BOFU-weighted)
action_type: refresh-expand-in-place
live_url: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
baseline: published-live-2026-07-27.md
faq_branch: B
author: Assel Sekerova
created: 2026-09-03
edited: 2026-09-07
editor: seo-editor
review_round: 1
review_source: review-1-decisions.md (wins over review-1.md)
word_count: 4413          # prose_words per article_lint.py, table cells included
word_count_ex_tables: 3988
editing_passes: 5
ai_density_before: 0.36
ai_density_after: 1.0
claims_verified: [FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009]
claims_used: [FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009]
changes_summary: |
  - Restructured 12 sections into 10 per decisions §C. Today's §1 market context compressed
    into two intro sentences, the four-stage workflow moved from position 6 to position 2, and
    the operational answer now arrives at 20% of the page instead of 45%.
  - B1: deleted the two CMS-0057-F inference sentences, placed the corrected timeframe
    statement verbatim (dates and numerals conformed to the page's style per the ruling), kept
    the ERISA and Medicare fee-for-service sentences, rewrote the FAQ timeframe answer with the
    QHP exclusion and the 14-day extension.
  - B2: payer acceptance distinction placed verbatim in §1 and carried into the workflow, the
    documentation section, the GLP-1 section, the FitXpress section, the comparison table and
    two FAQ answers. Comparison table row renamed to "Documentation generated" and a new
    "Payer acceptance" row added.
  - B3: three-row indicator table and the ASMBS-versus-claims reconciliation paragraph removed.
    One indicator survives, cited to the JAMA Surgery paper (doi) instead of the EurekAlert
    release. The Funk and Kurian quotes stay as the funnel-shape evidence.
  - B4: five "Text to place" blocks placed verbatim (product outputs, BMI cross-check, the
    3.5% qualification, Use Case Summary Outputs and Role rows, Stage 1, post-operative
    paragraph). Smart Scales named plural and marked beta at first mention.
  - B5: Business value row rewritten as what a pilot measures; five outcome phrases removed;
    the six pilot KPIs listed verbatim as a set. CDC self-report sentence untouched, its
    generalising inference removed.
  - B6: all seven guide promises removed plus §10's privacy-FAQ promise, with the preceding
    sentence answering the question instead (packet body-data contents in §3, record contents
    in §5, hybrid schedule folded into Stage 3).
  - B7: compliance bullet replaced verbatim, including the controller/processor formulation and
    the concrete photo-retention wording. Validation population and strength bullets untouched.
  - D1 introduction placed verbatim, with one added sentence so the primary keyword still lands
    in the first paragraph (lint gate 7). D2 Stage 2 rewritten around completeness, routing and
    retake fallback. D3 estimates-versus-methods boundary added post-op. D4 "weeks apart"
    removed. D5 line placed verbatim and the seven-row pilot table added. D6 FAQ cut. D7 three
    links removed. D8 meta description replaced in frontmatter.
  - Citation dedup: 7 distinct internal targets, 14 links. The accuracy framework is linked
    three times, once from each paragraph carrying a figure, which is the accuracy-discipline
    rule rather than a dedup miss.
  - Length: 4,712 -> 4,413 all-in (3,988 excluding table cells). Deletions took out roughly
    1,100 words; the mandated additions put back roughly 800. Not padded.
self_check: |
  - The ruling's own repetitions are the biggest remaining machine-tell, and they are not mine
    to fix: "predicted weight through Smart Scales (beta)" appears three times because the
    Outputs row, Stage 1 and the product paragraph are three separate verbatim blocks that all
    list outputs, and the DXA/BIA/calibrated-scale boundary appears three times because D3 and
    the "what FitXpress does not do" block both require it. I varied the third instance (FAQ)
    and left the two mandated ones alone.
  - Payer acceptance was starting to read as one sentence pasted five times. Kept the verbatim
    §1 wording and the identical table cells, then re-cut the other three so each states the
    boundary in its own shape.
  - Two paragraphs are heavier than the rest: §5's repeatability-plus-predicted-weight block
    and §6's accuracy block. Both are dense because the accuracy rule puts the figure, its
    condition and the framework link in one paragraph. Left dense on purpose.
  - The article is 4,413 words, not the "well below" the review expected. The deletions were
    made in full; the additions the same review mandates are what refilled it. Cutting further
    would have meant cutting mandated text or failing the length gate's 3,740 floor.
  - One gate does not pass. `article_lint.py` gate 5 fails on six instances of `predicted
    weight`, all six inside B4 "Text to place" blocks. Detail and remediation options in
    editor-report-review-1.md.
---

# Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams

Bariatric programs often collect or verify body measurements during the first consultation. When those inputs are missing, inconsistent or captured too late, pre-qualification and pre-authorization preparation can require additional follow-up. Structured remote intake can provide dated body measurements before the visit, establish a baseline for progress tracking and leave eligibility and treatment decisions with the care team. Bariatric pre-qualification runs on that record, and so does patient progress tracking after the procedure.

The demand side is not in dispute. The [most recent clinical-measurement cycle from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/nchs/products/databriefs/db508.htm), running from August 2021 to August 2023, shows 40.3% of US adults have obesity and 9.4% have severe obesity, at a BMI of 30 or higher and 40 or higher respectively, while the American Society for Metabolic and Bariatric Surgery (ASMBS) puts surgery's reach at [about 1% of those who meet eligibility requirements](https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf). <!-- ext-claim: CDC-DB508 --> <!-- ext-claim: ASMBS-FACTSHEET-2025 --> Inside that narrow funnel, pre-operative attrition varies with program design and with how it is counted: a [2026 narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/) reports dropout as high as 60%, one cohort in the same literature reports 22.25%, and programs with mandatory pre-operative pathways complete at roughly 36% to 76%. <!-- ext-claim: PMC12964095 --> That spread is a stronger case for a standardized intake record than any single figure inside it.

**Use Case Summary**

| Field | Detail |
| :-- | :-- |
| **Industry** | Bariatric surgery centers, hospital bariatric programs, multi-site surgical networks, metabolic and obesity clinics |
| **Problem** | Eligibility confirmed late, consult slots spent collecting measurements, pre-auth packets built from notes a payer reviewer cannot date |
| **Solution** | A guided two-photo remote scan completed before the consult, returning a structured body-data record to the program |
| **Outputs** | Predicted weight through Smart Scales (beta), BMI values for comparison, 80+ body measurements, body-composition estimates, capture timestamp and capture-quality outcomes |
| **Role** | Provides structured body-data inputs and discrepancy signals for program review; it does not determine eligibility or payer acceptance |
| **Business value** | What a pilot sets out to measure: intake completion, time from inquiry to a completed body-data record, pre-authorization rework, measurement-only appointments, follow-up completion |

The people who own that problem are bariatric program directors, directors of operations, pre-authorization coordinators and medical directors. What they answer for does not move on measurement accuracy alone. It moves on whether the right dated record exists before the review starts.

**Disclaimer.** *Mobile body scanning solutions described here do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions. They produce body measurement and composition data intended as supporting evidence within decisioning workflows operated by licensed bariatric programs and their compliance and payer counterparts.*

## 1. What structured remote body data contributes, and what it does not decide

**Short answer.** Bariatric pre-qualification is the intake step in which a program assesses whether an inquiry meets its own eligibility criteria and a payer's medical-necessity criteria, before a full clinical consult is scheduled. A bariatric patient progress record is the dated, comparable body-data series a program keeps from before the procedure through long-term follow-up. Structured remote body data supplies the measurement inputs for both. The eligibility determination and the pre-authorization decision are made elsewhere, by the licensed program and by the payer.

*Structured* carries an operational meaning here. The same guided capture sequence runs every time, the output is machine-readable, each capture carries a timestamp, and the records stay comparable across patients and across time points.

A structured scan record can give the program a dated and standardized body-data input before the consultation. Whether a payer accepts that record for a specific documentation requirement depends on the plan and should be confirmed during implementation.

At the top of the funnel, that input usually sits next to a self-reported number. CDC researchers reported in Preventing Chronic Disease that [self-reported BMI underestimated the prevalence of severe obesity by 40%](https://www.cdc.gov/pcd/issues/2023/23_0005.htm), at 5.3% on self-report against 8.8% after bias correction in 2020 data. <!-- ext-claim: CDC-PCD-2023 --> That is a population-level comparison between two ways of measuring prevalence, and it characterizes neither an individual patient nor an individual file. How much weight to give a self-reported figure at intake stays a program policy.

For obesity care teams the division of labour is the point: the measurement is standardized upstream, and the judgment stays downstream with the people licensed to make it. Bariatrics is one workflow among several that run on the same capture, and the [AI body data for health hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) maps the others.

## 2. Remote body measurement for bariatric patient intake: a four-stage pre-qualification workflow

The redesign is one move, and the rest of the workflow turns on it: body measurement goes from stage three, inside the consult, back to stage one, before it.

- **Stage 1. Remote capture at intake.** After the patient submits the intake questionnaire, the program sends a scan link. The patient completes the guided two-photo capture on their smartphone. FitXpress returns structured body data, including predicted weight through Smart Scales (beta), BMI, body measurements and body-composition estimates. Where self-reported weight is also collected, the program can compare the resulting BMI values and route material differences for human review.
- **Stage 2. Pre-consult review.** A coordinator confirms the record is complete and routes it for authorized clinical review against the program's intake criteria before a consult is scheduled. Pose validation runs during the capture and the clothing detector prompts the patient to adjust, which means an unusable capture surfaces in session. Where quality is still insufficient, the patient retakes the scan or is booked for in-clinic measurement. The [BMI verification capability](https://3dlook.ai/for-bmi-verification/) behind the capture is what that review reads.
- **Stage 3. Clinical consult.** The visit opens with the body data already in the patient's record, which moves the conversation to history, comorbidities, surgical risk and patient education. The same capture supports a hybrid schedule, where virtual check-ins alternate with in-person visits.
- **Stage 4. Documentation handoff.** The record that supported the pre-consult review is available to the pre-authorization coordinator from the start of the case. Whether that changes how long a packet takes to assemble is one of the things a pilot measures.

The scan does not determine whether a patient is medically eligible for surgery; the bariatric program makes that determination after evaluation. What the capture supplies is a structured, dated body-data input the program uses when it decides which consult slots to open and in what order. Each of the four stages names the person who reviews.

## 3. Bariatric pre-qualification and pre-authorization documentation

Stage 4 hands the record to a pre-authorization coordinator, and the clock it lands on belongs to the plan. For Medicare Advantage, Medicaid and Children's Health Insurance Program (CHIP) plans, the Centers for Medicare and Medicaid Services (CMS) now sets it.

Beginning 1 January 2026, [CMS-0057-F](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f) requires Medicare Advantage organizations and specified Medicaid and CHIP payers to issue standard non-drug prior-authorization decisions within 7 calendar days and expedited decisions within 72 hours, subject to applicable extension provisions. The rule did not change the decision timeframes for Qualified Health Plans on Federally Facilitated Exchanges. It also requires specific denial reasons and public reporting of aggregated prior-authorization metrics. <!-- ext-claim: CMS-0057-F -->

It does not cover every commercial plan governed by the Employee Retirement Income Security Act. Medicare fee-for-service does not use prior authorization for bariatric procedures at all. How much of a program's volume sits on this clock depends on its payer mix, and reading the rule against a specific plan contract is work for compliance counsel. <!-- ext-claim: CMS-0057-F -->

Window length changes what the documentation has to do. A long review window absorbs a request for more information, and 7 calendar days leaves little room for one.

The packet itself has not changed. A standard bariatric pre-authorization submission typically carries documented BMI history, confirmation of comorbidities, prior weight-loss attempts, participation in a supervised diet program where the plan requires it, psychological evaluation outcomes, and a body-measurement record. The body-data half of that packet is short: a dated BMI, the height and weight behind it, waist and hip circumference where the plan asks for them, and a record of when and how each was captured. What changed is how much of that has to be complete on the first pass.

None of this shortens the payer's own clock. A program controls one variable, whether its first submission is complete, and standardized capture is what makes that variable repeatable across coordinators. The mechanics of verifying a BMI figure remotely, including live capture and pose validation, are set out in the [compliance guide to online pharmacy BMI verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

What the file has to hold is steady. Who arrives at intake is not: many patients now reach the consult after a year on a glucagon-like peptide-1 (GLP-1) medication that did not take them to their goal.

## 4. The GLP-1 bridge: current BMI, historical BMI and documentation continuity

The shift is visible in claims. Metabolic bariatric surgery use fell 34.1% while GLP-1 receptor agonist use rose 140.4% between 2022 and 2024, measured inside one insured claims cohort of 11.7 million adults ([JAMA Surgery, 13 May 2026](https://doi.org/10.1001/jamasurg.2026.1343)). <!-- ext-claim: JAMA-SURG-2026 --> Coverage economics, prescribing growth and drug-class comparison sit on the [GLP-1 market hub](https://3dlook.ai/content-hub/glp-1-market/); what matters at an intake desk is who now walks up to it.

In the [American College of Surgeons Bulletin in April 2025](https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/), Luke Funk, a bariatric surgeon at the University of Wisconsin-Madison, described GLP-1 medications as "the initial gateway for a lot of patients" who later move toward surgery. Marina Kurian, clinical professor of surgery at NYU Langone Health, said in the same piece that "Most of my colleagues around the country are seeing an increase in new consults coming for surgery." <!-- ext-claim: ACS-BULLETIN-2025-04 --> A wider and more heterogeneous funnel is feeding surgical capacity that has not grown.

The sharpest operational change shows up in patient files. An [ASMBS release on 5 May 2026](https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/) reported a study by Chhabra and colleagues at NYU Grossman School of Medicine, presented at ASMBS 2026, drawing on Epic Cosmos electronic health records from 2019 to 2025. It compared 6,700 patients with prior GLP-1 use, 2,395 of them gastric bypass and 4,315 sleeve gastrectomy, against roughly 127,000 patients without prior GLP-1 use, followed for three years. Patients lost about 8% of total body weight on GLP-1 medications before surgery. Total loss reached more than 25% after gastric bypass and about 20% after sleeve gastrectomy. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA -->

For an intake coordinator the consequence lands on the file. A patient who has already lost about 8% of body weight on a GLP-1 may arrive at consult with a current BMI below a payer's threshold while their documented history still meets it. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA --> Eligibility then turns on dated BMI history, and one measurement taken in the room no longer carries the case by itself. What a payer's threshold is, and whether a given history meets it, stay questions for the program and the plan.

Bariatric surgery requirements, at this stage of the workflow, are documentation requirements: which measurements exist, when each was taken, and what sits behind each one. That is a records problem before it is a clinical one. A serial scan record carries its own date and its own capture conditions. A tape measurement typed into a free-text note carries neither, which leaves a reviewer with the note and nothing behind it. Whether a scan record then satisfies a given plan's documentation requirement is a separate question, and it is settled with the plan.

The pathway runs in both directions, since for some patients a medication becomes the bridge to surgery later on. An intake record that begins when a patient first enters obesity care is therefore more useful than one that begins at the surgical consult.

## 5. Patient progress tracking before and after surgery

The scan captured before surgery is the reference the follow-up scans are compared against. Because every capture runs the same guided sequence, a scan taken three months after the procedure is structurally comparable to the baseline instead of standing as a separate ad-hoc measurement.

For longitudinal use, repeatability is the property that carries the comparison. Accuracy describes how close one measurement sits to a reference; repeatability describes whether two scans of the same body produce numbers a program can compare. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-002 --> How that was measured, and why it answers a different question from accuracy, is set out in the [accuracy framework article](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). Predicted weight can add another consistent data point to remote follow-up, and it stays a software estimate: a calibrated scale remains the reading wherever the program's clinical protocol requires a directly measured weight.

Body composition after bariatric surgery moves on a different timeline from scale weight. The same weight can sit on top of different body-composition profiles, and that difference matters for patient counselling and for program-level outcome reporting. It matters to the multidisciplinary team around the patient too, in nutrition, behavioural health and surgical follow-up. Body-composition estimates complement weight and circumference trends where the program considers them appropriate. They are not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods.

The post-procedure window increasingly holds a pharmacotherapy component alongside surgical recovery. [Johns Hopkins researchers reporting on a JAMA Surgery analysis](https://publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs) found that roughly one in seven bariatric patients initiate GLP-1 therapy after surgery. <!-- ext-claim: JHU-2025-JAMA-SURG --> A baseline scan along with serial follow-up scans gives the program a body-data series that stays visible across the whole window, independent of medication adherence. Remote follow-up workflows are covered on the [AI in telehealth hub](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/).

A side-by-side comparison of the baseline capture and a recent scan is also a counselling artifact, often more useful than a single weight number on a chart, and it stays supporting evidence inside the program's monitoring workflow.

What belongs in a bariatric patient progress record is a short list: a dated BMI, waist and hip circumference, body-composition estimates, and a capture-quality outcome for each scan. Each entry carries its date and its capture conditions, and the cadence follows the program's monitoring protocol.

## 6. Where FitXpress fits: outputs, accuracy and limitations

FitXpress by 3DLOOK is a mobile body-scanning solution built around a guided two-photo flow, with no specialized hardware involved. The output can include a 3D model, 80+ body measurements, predicted weight through Smart Scales (beta), BMI, basal metabolic rate (BMR), body-fat percentage, lean mass and fat mass. Results come back in under 45 seconds from a guided two-photo capture completed on the patient's own smartphone. <!-- claim: FX-007 -->

Three properties matter for this use case. Outputs are structured and timestamped at capture, which allows a record to be placed in time and compared later. Capture happens remotely on the patient's own phone, which takes the appointment slot out of the measurement step. The third is the compliance posture, and its diligence questions belong with the pilot evaluation.

One measurement-accuracy figure applies here, and it comes from one specific comparison. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. <!-- claim: FX-001 --> The useful diligence question is accurate enough for which decision: against which reference method, under which capture protocol, for which population, and at what tolerance the workflow can absorb. Consult-slot triage and a payer packet do not set the same tolerance. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) states the conditions that make any such figure meaningful.

FitXpress can support an additional BMI cross-check through Smart Scales. Where the program also collects a self-reported weight, the capture compares it against the estimate and flags a mismatch. BMI from the patient's self-reported height and weight can then be read against BMI from the same height and the predicted weight. A material difference between the two values becomes a review signal rather than an automated eligibility conclusion.

Predicted weight stays a software estimate. Against scale weight it carries a ±3.5% average error margin under real-world conditions, an average across the evaluated captures rather than a bound on any single reading. A calibrated scale remains the reading wherever a clinical protocol or a payer requires a directly measured weight. <!-- claim: FX-008 --> Scale weight is the reference for that figure; expert manual measurement is the reference for the accuracy figures, and the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out why two figures taken against two references never collapse into one.

| Pathway stage | What the capture contributes |
| :-- | :-- |
| Inquiry | Early body data captured outside the clinic |
| Pre-consult | Supports pre-qualification review and consult-slot triage |
| Pre-authorization | Provides structured, timestamped documentation inputs |
| Procedure preparation | Establishes a baseline body-data record |
| Post-surgery follow-up | Tracks body measurement and composition change over time |
| Long-term monitoring | Supports remote progress review without a clinic visit |

The same data structure can be generated at multiple pathway stages alongside measurements required by the program or payer. The technology behind the capture is described on the [3DLOOK technology page](https://3dlook.ai/technology/).

**What FitXpress does not do in a bariatric program.** It does not determine medical or surgical eligibility. It does not diagnose. It does not replace clinical evaluation. It does not make the pre-authorization decision. It does not guarantee compliance or an approval. It does not make a record acceptable to a payer; that acceptance sits with the plan. It is not equivalent to DXA, bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods. It is not positioned as a medical device.

## 7. Manual measurement versus guided capture

Manual measurement and guided capture sit under different constraints. The comparison that matters runs workflow area by workflow area.

| Workflow area | Manual measurement at the consult | Guided scan-based capture |
| :-- | :-- | :-- |
| Appointment slot | Required; the measurement and the slot are one event | Not required; capture runs before, during or after a clinical event |
| Cross-operator comparability | Varies with operator, tool, technique and participant preparation | Same capture and processing sequence each time, comparable across patients and time points |
| Documentation generated | A note stating a measurement was taken | A record carrying a capture timestamp and capture-quality outcomes |
| Reuse across pre-qualification, pre-auth and post-op | Each stage collects its own measurement | The same data structure generated at several stages |
| What it depends on | Trained staff, protocol adherence, in-person attendance | Patient smartphone access, capture instructions, retake logic, deployment thresholds |
| Payer acceptance | Follows the plan's own documentation requirements and is confirmed during implementation | Follows the plan's own documentation requirements and is confirmed during implementation |

At the consult, manual measurement stays where the protocol requires it, and where a clinician needs a hand on the anatomical landmark. Neither method replaces the other, and a program running both decides which one a given step calls for.

The fit is clearest at bariatric surgery centers, hospital programs, multi-site surgical networks and metabolic and obesity clinics. Directors of operations, medical directors, vice presidents of patient access and chief operating officers own the measures at stake: consult-to-procedure conversion, late-stage disqualifications and cancellations, pre-authorization cycle time, and staff time per packet. At a multi-site network, cross-site consistency is the whole argument.

## 8. What to confirm in a bariatric pilot

None of this is a settled outcome for any particular program. A pilot is where the claims get tested against one program's patients and one program's payer mix, and it has to keep two things apart: what the capture produces, and what the program's review does with it.

In the pre-authorization packet the first of those is narrow and concrete. The file gains a structured body-data record: a capture timestamp, the capture-quality outcomes recorded in session, and the measurement set in machine-readable form, consistent across patients because the sequence does not vary between them. Serial captures on one timeline, a baseline at intake, a second before submission, a third before the procedure, produce comparable records instead of three measurements taken three different ways. Audit-readiness is the program's own determination, and a human reviewer still reads every record.

The anti-manipulation controls support that posture without completing it. Capture runs live in session instead of accepting a camera-roll upload, pose validation runs in real time, and clothing detection is built in. Those controls reduce the risk of a manipulated capture. They leave in place the need for capture instructions, retake logic and deployment-specific thresholds. They are fraud-prevention support inside a human review process.

The measures worth instrumenting before a pilot starts are intake completion, retake rate, time from inquiry to completed body-data record, pre-auth rework, measurement-only appointments, and follow-up completion. Each is a hypothesis on the way in and a number on the way out.

Alongside the numbers sit seven things a program confirms for itself.

| What to confirm | The question the pilot answers |
| :-- | :-- |
| Capture completion | What share of invited patients finish a usable capture without staff help |
| Quality failures and retakes | How often a capture is rejected, and how many retakes clear it |
| Workflow integration | Where the record lands in the intake system or the electronic health record, and who moves it there |
| Role-based review | Which role reads the record, against which criteria, and what happens to a flagged mismatch |
| Population fit | How the program's own patients sit against the validation scope |
| Payer acceptance | Which plans in the payer mix accept the record for which documentation requirement |
| Data governance | Retention, access control, Business Associate Agreement scope, and where photos and outputs sit |

Three vendor-side questions belong in the same diligence.

- **Compliance posture.** FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts and supports Business Associate Agreement execution. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR). Data is encrypted at rest in Amazon Web Services S3 with server-side encryption always on, and in transit over Transport Layer Security. Photos are permanently removed immediately after processing, or within 30 days, depending on the client's configured policy, and are automatically blurred when stored. FitXpress does not receive names, contact details, or other direct identifiers that connect the scan with a specific individual. Body data and session-linked outputs can still qualify as personal data, which is the program's own assessment to make. <!-- claim: FX-009 -->
- **Validation population.** The internal validation population included participants aged 16 to 78, heights of 150 to 220 cm, weights of 38 to 210 kg, and participants from the US and Europe. Performance outside this scope has not been characterized. <!-- claim: FX-005 --> A severe-obesity intake population includes patients above that weight range, worth checking early in evaluation.
- **Validation strength.** 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study. <!-- claim: FX-006 -->

Those three are the floor to confirm with any vendor handling patient body data before a pilot begins.

## 9. Frequently asked questions

### Pre-qualification and pre-authorization documentation

**What is bariatric pre-qualification?**
Bariatric pre-qualification is the intake step in which a program checks an inquiry against its own eligibility criteria and a payer's medical-necessity criteria before a full clinical consult is scheduled. Eligibility determination stays with the licensed program.

**How can bariatric programs pre-qualify patients remotely?**
The program sends a body-scan link at intake and the patient completes the guided capture on their own smartphone. BMI, body measurements and body-composition estimates reach the program before the consult, where clinical evaluation still happens.

**What body-data documentation do payers commonly require in a bariatric pre-authorization packet?**
A standard packet typically carries documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation where the plan requires it, psychological evaluation outcomes and a body-measurement record. A capture timestamp dates the measurement record; whether a given plan accepts that record for a specific requirement is confirmed with the plan.

**How long do payers have to decide a bariatric prior authorization?**
Under CMS-0057-F, since 1 January 2026, Medicare Advantage organizations and specified Medicaid and CHIP payers decide standard non-drug requests within 7 calendar days and expedited requests within 72 hours. <!-- ext-claim: CMS-0057-F --> Some requests qualify for an extension of up to 14 additional calendar days under program-specific conditions. The rule did not change the decision timeframes for Qualified Health Plans on Federally Facilitated Exchanges, it does not reach every commercial plan under the Employee Retirement Income Security Act, and Medicare fee-for-service uses no prior authorization for bariatric procedures.

**What are common program and payer requirements?**
Each program and plan sets its own list, and the common items are documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation and psychological evaluation outcomes. At intake the question is documentary: what exists, dated when, and what record sits behind it.

**Why does documented BMI history matter more when a patient has been on a GLP-1?**
Patients in one 2026 study lost about 8% of total body weight on GLP-1 medications before surgery. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA --> A patient who arrives that much lighter may show a current BMI below a payer's threshold while their documented history still meets it. That reading belongs to the program and the payer.

### Patient progress tracking

**What body data belongs in a bariatric patient progress record?**
A dated BMI, waist and hip circumference, body-composition estimates, and a capture-quality outcome for each scan. The set and the cadence follow the program's monitoring protocol.

### Scope and governance

**Is scan data used to make eligibility or pre-authorization decisions?**
No. The scan produces body measurement and composition data used as supporting evidence inside workflows the licensed program and its payer counterparts operate. Eligibility and pre-authorization decisions are made by people, against those parties' criteria. Whether a payer accepts a scan record for a given documentation requirement is decided by the plan.

**What does FitXpress not do in a bariatric program, and can it replace in-clinic measurement?**
It does not determine medical or surgical eligibility, diagnose, or make the pre-authorization decision, and it does not guarantee compliance or an approval. Where a protocol or a regulatory standard calls for DXA, bioelectrical impedance analysis or a calibrated scale, those remain the methods of record. In-clinic measurement stays where the protocol asks for it.

## 10. Next steps and related reading

See how FitXpress can support pre-qualification, pre-authorization documentation and post-procedure progress tracking inside a bariatric program. A useful first step is mapping one payer's packet requirements against what the file already holds on the day of the consult. [Request a FitXpress demo](https://3dlook.ai/for-bmi-verification/) or contact sales@3dlook.ai.

Related reading:

- [AI body data across health programs](https://3dlook.ai/content-hub/ai-body-data-health-hub/)
- [GLP-1 market growth and patient progress tracking](https://3dlook.ai/content-hub/glp-1-market/)
- [AI in telehealth: workflows, privacy and remote body data](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [Online pharmacy BMI verification compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)
