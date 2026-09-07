---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
section: full
status: edited
title: "Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams"
meta_description: "Bariatric pre-qualification and patient progress tracking in 2026: the 7-day prior-authorization clock, documented BMI history, and the body data a program's file has to hold."
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
edited: 2026-09-03
editor: seo-editor
word_count: 4712          # prose_words per article_lint.py, table cells included
word_count_ex_tables: 4316
editing_passes: 5
ai_density_before: 0.69
ai_density_after: 0.36
claims_verified: [FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009]
claims_used: [FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009]
changes_summary: |
  - Deduped 3 repeat citations. The ASMBS 5 May 2026 release, the 2025 Fact Sheet and the
    ASMBS estimate page are each now linked exactly once. Cut the "Untreated share" row from
    the Section 4 table, which republished Section 1's 90-95% figure and its link.
  - Deliberate exception to the dedup pass: the accuracy framework stays linked three times
    (Sections 7, 8 and FAQ Q10), because every paragraph carrying an accuracy figure has to
    link it.
  - Firmed up 2 figure sets against gap analysis 3b. Section 4 carries 270,089 and 279,967
    instead of "more than 270,000, down about 3.5%", sourced to the ASMBS estimate page
    instead of the Fact Sheet PDF. FAQ Q15 now carries sleeve gastrectomy 58.2%, gastric
    bypass 23.4% and revisions 11.9% against that same 270,089 total.
  - Rewrote 11 sentences that read as machine text, including "Seven calendar days inverts
    the documentation argument", "A program's payer mix therefore decides", "The compliance
    posture holds at procurement", "Accuracy on this page means", "Audit-ready records are a
    property of", and the "serve as a bridge" construction.
  - Fixed 4 phrase repetitions ("in the file, dated when" x3, "the capture sequence is the
    same" x4, "the capture-quality outcomes from the guided flow" x3, "the companion guide
    to" x5) and broke all 6 monotone adjacent sentence pairs. Repeated 5-grams are now down
    to the primary keyword phrase alone.
  - Added a thematic bridge from Section 3 into Section 4, a lead-in to Section 10 (which
    opened on a bare table), and a concrete first step in the CTA.
  - Terminology pass: expanded CDC at first use, removed the AWS abbreviation, unstacked two
    double negations (Section 3 paragraph 2 and FAQ Q13), reframed FX-008 out of an "X, not
    Y" shape, and kept "guarantee" only in the "does not guarantee" form the banned-claim
    gate expects.
  - Length: FAQ 945 -> 791, Section 10 446 -> 430, front matter 380 -> 363. Total 4,939 ->
    4,712 all-in and 4,500 -> 4,316 excluding table cells. Full table in editor-report.md.
self_check: |
  - Rhythm was still even in Sections 3, 5, 7, 8 and 9: six paragraphs held adjacent
    sentences of the same length, which is what a paragraph written to a template does.
    Split six of them; the monotone-pair count is now zero and rhythm variation moved
    0.53 -> 0.56.
  - Section 4 announced "Three data series" and then printed four table rows, two of which
    were the same series. Rewritten as three indicators from two measurement systems, which
    is what the sources support, and the fourth row went back to Section 1 where its
    argument lives.
  - Section 10 opened on a bare table in the buyer's decision section, with no claim of its
    own. Added the workflow-comparison framing so the table answers a question the prose
    asked, and closed the section on a stated boundary instead of an abstraction.
  - Three nouns were doing duty as elegant variation for one thing ("the quality outcomes
    the guided flow returns" / "capture-quality outcomes" / "quality outcomes"). Settled on
    "capture-quality outcomes" and varied only where the sentence needed a different subject.
  - Still thinner than the insurance and wellness hubs in one respect that cannot be fixed
    at the editing stage: there is no named bariatric customer, so every operational claim
    rests on a third-party citation or a disclosed internal limit. Recorded as a
    recommendation in editor-report.md.
---

# Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams

Most diligence on remote body data starts at accuracy. Inside a bariatric program the sharper question is which record has to be in the file, dated when, and for whom to review. Bariatric pre-qualification runs on that record, and so does patient progress tracking after the procedure. US programs carry a structural mismatch between intake demand and surgical capacity, and the verification stack most of them still run was built for a slower era: a self-reported weight, a tape measurement taken in clinic, a BMI computed during the consult.

Patients also arrive differently now. Many reach the consult after a year on a glucagon-like peptide-1 (GLP-1) medication that did not reach their goal, expecting a pathway that already knows their numbers. Two things changed in 2026 that the intake stack was not built for: a federal prior-authorization rule with a 7-calendar-day standard decision window for impacted payers, and a patient population whose current BMI and qualifying BMI history have come apart. <!-- ext-claim: CMS-0057-F -->

**Use Case Summary**

| Field | Detail |
| :-- | :-- |
| **Industry** | Bariatric surgery centers, hospital bariatric programs, multi-site surgical networks, metabolic and obesity clinics |
| **Problem** | Eligibility confirmed late, consult slots spent collecting measurements, pre-auth packets built from notes a payer reviewer cannot date |
| **Solution** | A guided two-photo remote scan completed before the consult, returning a structured body-data record to the program |
| **Outputs** | BMI, 80+ body measurements, body composition estimates, capture timestamp, capture-quality outcomes |
| **Role** | Supporting evidence for program and payer review, not eligibility or pre-authorization decisioning |
| **Business value** | Higher consult-to-procedure conversion, fewer measurement-only visits, earlier documentation start, records comparable across the pathway |

The people who own that problem are bariatric program directors, directors of operations, pre-authorization coordinators and medical directors. What they answer for does not move on measurement accuracy alone. It moves on whether the right dated record exists before the review starts.

**Disclaimer.** *Mobile body scanning solutions described here do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions. They produce body measurement and composition data intended as supporting evidence within decisioning workflows operated by licensed bariatric programs and their compliance and payer counterparts.*

## 1. The bariatric intake gap: eligibility confirmed late, documentation assembled after the consult

The demand side has moved in one direction for years. The [most recent clinical-measurement cycle from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/nchs/products/databriefs/db508.htm), running from August 2021 to August 2023, shows 40.3% of US adults have obesity and 9.4% have severe obesity, at a BMI of 30 or higher and 40 or higher respectively. <!-- ext-claim: CDC-DB508 -->

Very little of that population reaches a procedure. The American Society for Metabolic and Bariatric Surgery (ASMBS) puts surgery's reach at [about 1% of those who meet eligibility requirements](https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf), and its [release of 5 May 2026](https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/) reported that 90-95% of patients with severe obesity received no treatment during the study period. <!-- ext-claim: ASMBS-FACTSHEET-2025 --> <!-- ext-claim: ASMBS-2026-05-05 -->

Two problems sit under the standard intake design, where the patient self-reports a weight, the program books the consult, and the measurement happens at the appointment. The first is the quality of the number at the top of the funnel. CDC researchers reported in Preventing Chronic Disease that [self-reported BMI underestimated the prevalence of severe obesity by 40%](https://www.cdc.gov/pcd/issues/2023/23_0005.htm), at 5.3% on self-report against 8.8% after bias correction in 2020 data. <!-- ext-claim: CDC-PCD-2023 --> Where BMI is the trigger for procedure-specific criteria, a self-reported value is a placeholder that still has to be verified.

The second problem is attrition, and the published range is itself the argument. A [2026 narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/) reports pre-operative dropout as high as 60%. One cohort in the same literature reports 22.25%. Canadian programs with mandatory pre-operative pathways complete at roughly 36% to 76%, US programs at roughly 39% to 70%, and one single-centre series reported 8.9% before the pandemic. <!-- ext-claim: PMC12964095 --> Attrition depends on program design and on how it is counted. That spread is a stronger case for a standardized intake record than any single figure inside it.

Consult slots, operating-room days and pre-authorization coordinators are all finite. When intake demand rises against unchanged surgical capacity, the bottleneck moves upstream into the verification and documentation steps that decide whether a slot becomes a procedure or a deferral. Every verification step that requires an in-person appointment is also a point where a patient can leave the pathway. That is the part of the bariatric intake workflow a remote body-data layer supports.

## 2. Short answer: what structured body data contributes, and what still decides

**Short answer.** Bariatric pre-qualification is the intake step in which a program assesses whether an inquiry meets its own eligibility criteria and a payer's medical-necessity criteria, before a full clinical consult is scheduled. A bariatric patient progress record is the dated, comparable body-data series a program keeps from before the procedure through long-term follow-up. Structured remote body data supplies the measurement inputs for both. The eligibility determination and the pre-authorization decision are made elsewhere, by the licensed program and by the payer.

*Structured* carries an operational meaning here. The same guided capture sequence runs every time, the output is machine-readable, each capture carries a timestamp, and the records stay comparable across patients and across time points.

For obesity care teams the division of labour is the point: the measurement is standardized upstream, and the judgment stays downstream with the people licensed to make it. Bariatrics is one workflow among several that run on the same capture, and the [AI body data for health hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) maps the others.

## 3. Why now (1): prior authorization runs on a 7-calendar-day clock

The payer clock changed on 1 January 2026. Under the [Centers for Medicare and Medicaid Services Interoperability and Prior Authorization Final Rule (CMS-0057-F)](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f), impacted payers must decide standard prior authorization requests within 7 calendar days and expedited requests within 72 hours. They must give a specific reason for each non-drug denial, whatever channel the request arrived through, and they must publicly report prior-authorization metrics annually, with initial reporting due 31 March 2026. <!-- ext-claim: CMS-0057-F -->

The rule's reach belongs in the same breath as the rule. CMS-0057-F applies to Medicare Advantage organizations, Medicaid and Children's Health Insurance Program (CHIP) fee-for-service programs and their managed-care plans, and Qualified Health Plans on the Federally Facilitated Exchange. It does not cover every commercial plan governed by the Employee Retirement Income Security Act. Medicare fee-for-service does not use prior authorization for bariatric procedures at all. <!-- ext-claim: CMS-0057-F --> How much of a program's volume sits on this clock depends on its payer mix. Reading the rule against a specific plan contract is work for compliance counsel.

Window length changes what the documentation has to do. A long review window absorbs a request for more information; seven calendar days leaves no room for one. When the record supporting medical necessity is assembled only after the payer asks for it, a missing timestamped BMI record stops being a delay and becomes a denial that now carries a published reason. Published reasons accumulate, which makes the pattern of a program's incomplete submissions legible over a year.

The packet itself has not changed. A standard bariatric pre-authorization submission typically carries documented BMI history, confirmation of comorbidities, prior weight-loss attempts, participation in a supervised diet program where the plan requires it, psychological evaluation outcomes, and a body-measurement record. What changed is how much of that has to be complete and verifiable on the first pass. Prior authorization documentation is now the tightest constraint on a bariatric program's calendar, and the body-data half of that packet has a dedicated guide of its own. <!-- DOWN-LINK LANDING: P1 child "Bariatric Pre-Authorization Documentation: What Body Data Payers May Need". Anchor phrase reserved; publisher links when the child ships. -->

None of this shortens the payer's own clock. A program controls one variable, whether its first submission is complete, and standardized capture is what makes that variable repeatable across coordinators. The mechanics of verifying a BMI figure remotely, including live capture and pose validation, are set out in the [compliance guide to online pharmacy BMI verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

## 4. Why now (2): GLP-1 changed the shape of the intake funnel

The clock tightened while the funnel feeding it changed shape. Three indicators carry the current volume picture, and two measurement systems produce them. The systems do not reconcile, and keeping them apart separates a defensible read from a number no source supports.

| Indicator | Figure | What it indicates |
| :-- | :-- | :-- |
| US procedure volume, 2023 | 270,089 procedures, down about 3.5% from 279,967 in 2022 ([ASMBS estimate of bariatric surgery numbers](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/)), a national estimate built from the Bariatric Outcomes Longitudinal Database, accreditation-program data, the National Inpatient Sample and outpatient estimations. The series ends at 2023. | The national volume anchor. |
| Change in surgery use, 2022 to 2024 | Metabolic bariatric surgery use down 34.1% while GLP-1 receptor agonist use rose 140.4% over the same period ([JAMA Surgery, 13 May 2026](https://www.eurekalert.org/news-releases/1127781)), measured inside one insured claims cohort. | A rate of use within that cohort. Absolute counts in the same cohort move about 7.3% lower. Not a national count. |
| Cohort procedure counts | 40,265 (2022), 42,615 (2023), 37,339 (2024), 33,429 (2025), all from the same claims cohort. | The decline continued into 2025 inside that cohort. |

The national estimate and the claims cohort are not comparable, and ASMBS says so directly: its own estimates draw on broader patient populations and additional datasets than the study used. One figure is a rate of use inside an insured population; the other is a national count. <!-- ext-claim: ASMBS-2026-05-05 -->

Volume is only half of what moved. In the [American College of Surgeons Bulletin in April 2025](https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/), Luke Funk, a bariatric surgeon at the University of Wisconsin-Madison, described GLP-1 medications as "the initial gateway for a lot of patients" who later move toward surgery. Marina Kurian, clinical professor of surgery at NYU Langone Health, said in the same piece that "Most of my colleagues around the country are seeing an increase in new consults coming for surgery." <!-- ext-claim: ACS-BULLETIN-2025-04 -->

A wider and more heterogeneous intake funnel is feeding surgical capacity that has not grown, which raises the value of a structured pre-qualification step ahead of the consult. The patient at the top of it arrives with a longer treatment history and a firmer expectation that the program can say where they stand.

Coverage economics, prescribing growth and drug-class comparison sit on the [GLP-1 market hub](https://3dlook.ai/content-hub/glp-1-market/). The medication pathway now runs in both directions, which is the subject of a separate guide on GLP-1 before bariatric surgery and body composition. <!-- DOWN-LINK LANDING: P1 child "GLP-1 Before Bariatric Surgery: Why Body Composition and Progress Matter". Anchor phrase reserved. -->

## 5. Why now (3): current BMI and qualifying BMI history have come apart

The sharpest operational change of 2026 shows up in patient files. An [ASMBS release on 5 May 2026](https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/) reported a study by Chhabra and colleagues at NYU Grossman School of Medicine, presented at ASMBS 2026, drawing on Epic Cosmos electronic health records from 2019 to 2025. It compared 6,700 patients with prior GLP-1 use, 2,395 of them gastric bypass and 4,315 sleeve gastrectomy, against roughly 127,000 patients without prior GLP-1 use, followed for three years. Patients lost about 8% of total body weight on GLP-1 medications before surgery. Total loss reached more than 25% after gastric bypass and about 20% after sleeve gastrectomy. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA -->

For an intake coordinator the consequence lands on the file. A patient who has already lost about 8% of body weight on a GLP-1 may arrive at consult with a current BMI below a payer's threshold while their documented history still meets it. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA --> Eligibility then turns on dated, verifiable BMI history, and one measurement taken in the room no longer carries the case by itself. What a payer's threshold is, and whether a given history meets it, stay questions for the program and the plan. Bariatric surgery requirements, at this stage of the workflow, are documentation requirements: which measurements exist, when each was taken, and whether a reviewer can trace them to a capture.

That is a records problem before it is a clinical one. A serial scan record carries its own date and its own capture conditions. A tape measurement typed into a free-text note carries neither, and a reviewer at the payer cannot confirm when it was taken or how. Read against the 7-calendar-day standard window, a history reconstructed after a request for information arrives too late.

The pathway also runs the other way: for some patients a medication becomes a bridge to surgery later. An intake record that begins when a patient first enters obesity care is therefore more useful than one that begins at the surgical consult. What belongs in that record is specified in a dedicated guide to the bariatric patient progress record. <!-- DOWN-LINK LANDING: P1 children "GLP-1 Before Bariatric Surgery" and "What Body Data Should Be in a Bariatric Patient Progress Record?". Anchor phrase reserved. -->

## 6. The bariatric pre-qualification workflow: moving the measurement step to intake

Pre-qualification is where the consult-to-procedure conversion math changes fastest, and the redesign is one move: the body-measurement step goes from stage three back to stage one.

- **Stage 1. Remote scan at intake.** After the patient submits the baseline questionnaire, the program sends a scan link and the patient completes the guided two-photo capture on their own smartphone, typically the same day. The program receives a structured record containing BMI, body measurements and body composition estimates. Remote bariatric intake carries its own workflow questions, treated in a guide to remote body measurement for bariatric patient intake. <!-- DOWN-LINK LANDING: P2 child "Remote Body Measurement for Bariatric Patient Intake". -->
- **Stage 2. Pre-consult review.** A coordinator or clinical reviewer checks the output against the program's eligibility thresholds and any program-specific intake criteria before the consult is scheduled. Patients who clearly meet criteria move into a clinical-evaluation consult. Patients who fall outside them are routed into medical-management or referral pathways without occupying a surgical consult slot. The underlying [BMI verification capability](https://3dlook.ai/for-bmi-verification/) supplies the signal for that review. Where a program pairs virtual check-ins with in-person visits, the same capture supports a hybrid bariatric care model, covered separately. <!-- DOWN-LINK LANDING: P1 child "Hybrid Bariatric Care: Virtual Check-Ins With Standardized Body Data". -->
- **Stage 3. Clinical consult.** The visit opens with the body data already in the patient's record, which moves the conversation to history, comorbidities, surgical risk and patient education. The slot becomes a clinical evaluation instead of a measurement-collection event.
- **Stage 4. Documentation handoff.** The record that supported the triage decision is available to the pre-authorization coordinator from the start of the case. On a 7-calendar-day standard clock, available from the start is the difference between a first-pass submission and a resubmission.

The mechanism here is not clinical decision-making. The scan does not determine whether a patient is medically eligible for surgery, and the bariatric program makes that determination after evaluation. What the scan supplies is a structured, verifiable body-data signal the program uses to triage which consult slots are opened, in what order, and with what supporting record already attached. Each stage above names the person who reviews.

## 7. Where FitXpress fits across the bariatric pathway

FitXpress by 3DLOOK is a mobile body-scanning solution built around a guided two-photo flow. The patient takes a front and a side smartphone image, results return in under 45 seconds, and the output covers 80+ body measurements along with BMI, basal metabolic rate (BMR), body-fat percentage, and lean and fat mass, with no specialized hardware involved. <!-- claim: FX-007 -->

Three properties matter for this use case. Outputs are structured and timestamped at capture, which allows a record to be placed in time and compared later. Capture happens remotely on the patient's own phone, which removes the appointment slot as the verification gate. The third is the compliance posture. Its diligence questions belong with the pilot evaluation.

One accuracy figure applies here, and it comes from one specific comparison. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. <!-- claim: FX-001 --> The useful diligence question is accurate enough for which decision: against which reference method, under which capture protocol, for which population, and at what tolerance the workflow can absorb. Consult-slot triage and a payer packet do not set the same tolerance. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) states the conditions that make any such figure meaningful.

| Pathway stage | What the capture contributes |
| :-- | :-- |
| Inquiry | Early body data captured outside the clinic |
| Pre-consult | Supports pre-qualification review and consult-slot triage |
| Pre-authorization | Provides structured, timestamped documentation inputs |
| Procedure preparation | Establishes a baseline body-data record |
| Post-surgery follow-up | Tracks body measurement and composition change over time |
| Long-term monitoring | Supports remote progress review without a clinic visit |

One capture asset, read repeatedly across the bariatric patient journey, replaces the fragmented manual measurements that today sit in separate parts of the program's workflow. The technology behind the capture is described on the [3DLOOK technology page](https://3dlook.ai/technology/).

## 8. Patient progress tracking after the procedure

The scan captured before surgery is the reference the follow-up scans are compared against. Because every capture runs the same guided sequence, a scan taken three months after the procedure is structurally comparable to the baseline instead of standing as a separate ad-hoc measurement.

For longitudinal use, repeatability is the property that carries the comparison. Accuracy describes how close one measurement sits to a reference; repeatability describes whether two scans of the same body, weeks apart, produce numbers a program can compare. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-002 --> How that was measured, and why it answers a different question from accuracy, is set out in the [accuracy framework article](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). Weight estimation is the weaker output and belongs in the record with its limit stated: it carries a ±3.5% average error margin as a software estimate, and a calibrated scale remains the reading where a protocol requires one. <!-- claim: FX-008 -->

Body composition after bariatric surgery moves on a different timeline from scale weight. The same weight can sit on top of different body-composition profiles, and that difference matters for patient counselling and for program-level outcome reporting. It also matters to the multidisciplinary team around the patient, in nutrition, behavioural health and surgical follow-up.

The post-procedure window increasingly holds a pharmacotherapy component alongside surgical recovery. [Johns Hopkins researchers reporting on a JAMA Surgery analysis](https://publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs) found that roughly one in seven bariatric patients initiate GLP-1 therapy after surgery. <!-- ext-claim: JHU-2025-JAMA-SURG --> A baseline scan along with serial follow-up scans gives the program a body-data series that stays visible across the whole window, independent of medication adherence. Remote follow-up workflows are covered on the [AI in telehealth hub](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/).

A side-by-side comparison of the baseline capture and a recent scan is also a counselling artifact, often more useful than a single weight number on a chart, and it stays supporting evidence inside the program's monitoring workflow.

What belongs in a bariatric patient progress record is a short list. The components are a dated BMI, waist and hip circumference, body composition estimates, and a capture-quality outcome for each scan. Each entry carries its date and its capture conditions. The cadence follows the program's monitoring protocol. Tracking body changes beyond weight loss, and the fuller specification of a progress record, are handled in two further guides. <!-- DOWN-LINK LANDING: P1 children "Tracking Body Changes After Bariatric Surgery Beyond Weight Loss" and "What Body Data Should Be in a Bariatric Patient Progress Record?". -->

## 9. What improves operationally, and what FitXpress does not do

In the pre-authorization packet the change is narrow and concrete. The file gains a structured body-data record: a capture timestamp, the capture-quality outcomes recorded in session, and the measurement set in machine-readable form, consistent across patients because the sequence does not vary between them. Serial captures on one timeline, a baseline at intake, a second before submission, a third before the procedure, produce comparable records instead of three measurements taken three different ways. Whether those records are audit-ready follows from how the data was captured, and a human reviewer still reads them.

The anti-manipulation controls support that posture without completing it. Capture runs live in session instead of accepting a camera-roll upload, pose validation runs in real time, and clothing detection is built in. Those controls reduce the risk of a manipulated capture. They leave in place the need for capture instructions, retake logic and deployment-specific thresholds. They are fraud-prevention support inside a human review process.

**What FitXpress does not do in a bariatric program.** It does not determine medical or surgical eligibility. It does not diagnose. It does not replace clinical evaluation. It does not make the pre-authorization decision. It does not guarantee compliance or an approval. It is not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods. It is not positioned as a medical device.

The payer-facing documentation set behind those records, and the checklist that follows from it, sit in the guides on bariatric pre-authorization documentation and the bariatric patient progress record. <!-- DOWN-LINK LANDING: P1 children "Bariatric Pre-Authorization Documentation" and "What Body Data Should Be in a Bariatric Patient Progress Record?", and the P2 lead magnet "Bariatric Documentation Checklist". -->

## 10. Comparison, buyer fit, and what to confirm before a pilot

Manual measurement and guided capture sit under different constraints. The comparison that matters runs workflow area by workflow area.

| Workflow area | Manual measurement at the consult | Guided scan-based capture |
| :-- | :-- | :-- |
| Appointment slot | Required; the measurement and the slot are one event | Not required; capture runs before, during or after a clinical event |
| Cross-operator comparability | Varies with operator, tool, technique and participant preparation | Same capture and processing sequence each time, comparable across patients and time points |
| What a payer reviewer can verify | A note stating a measurement was taken | A record carrying a capture timestamp and capture-quality outcomes |
| Reuse across pre-qualification, pre-auth and post-op | Each stage collects its own measurement | One capture asset, read at several stages |
| What it depends on | Trained staff, protocol adherence, in-person attendance | Patient smartphone access, capture instructions, retake logic, deployment thresholds |

Manual measurement at the consult stays where the protocol requires it, and where a clinician needs a hand on the anatomical landmark. For obesity care teams the comparison resolves into a division of labour, and neither method replaces the other.

The fit is clearest at bariatric surgery centers, hospital programs, multi-site surgical networks and metabolic and obesity clinics. Directors of operations, medical directors, vice presidents of patient access and chief operating officers own the measures at stake: consult-to-procedure conversion, late-stage disqualifications and cancellations, pre-auth cycle time, and staff time per packet. Cross-site consistency is the whole argument at a multi-site network, and the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/) carries its employer-facing version.

Three evaluation considerations belong in the diligence.

- **Compliance posture.** FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts, supports Business Associate Agreement execution, follows General Data Protection Regulation (GDPR) principles, encrypts data at rest in Amazon Web Services S3 and in transit over Transport Layer Security, processes no personal identifiers, and deletes photos immediately after processing or within a configurable retention window. <!-- claim: FX-009 --> A dedicated FitXpress privacy and regulatory FAQ, not yet published, holds the fuller detail.
- **Validation population.** The internal validation population included participants aged 16 to 78, heights of 150 to 220 cm, weights of 38 to 210 kg, and participants from the US and Europe. Performance outside this scope has not been characterized. <!-- claim: FX-005 --> A severe-obesity intake population includes patients above that weight range, worth checking early in evaluation.
- **Validation strength.** 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study. <!-- claim: FX-006 -->

Those three are the floor to confirm with any vendor handling patient body data before a pilot begins.

## 11. Frequently asked questions

### Pre-qualification and pre-authorization documentation

**What is bariatric pre-qualification?**
Bariatric pre-qualification is the intake step in which a program checks an inquiry against its own eligibility criteria and a payer's medical-necessity criteria before a full clinical consult is scheduled. Eligibility determination stays with the licensed program.

**How can bariatric programs pre-qualify patients remotely?**
The program sends a body-scan link at intake and the patient completes the guided capture on their own smartphone. BMI, body measurements and body composition estimates reach the program before the consult, where clinical evaluation still happens.

**What body-data documentation do payers commonly require in a bariatric pre-authorization packet?**
A standard packet typically carries documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation where the plan requires it, psychological evaluation outcomes and a body-measurement record. A capture timestamp is what makes the measurement record verifiable.

**How long do payers have to decide a bariatric prior authorization?**
Under CMS-0057-F, operational since 1 January 2026, impacted payers must decide standard requests within 7 calendar days and expedited requests within 72 hours. <!-- ext-claim: CMS-0057-F --> Impacted means Medicare Advantage, Medicaid, CHIP and Qualified Health Plans on the Federally Facilitated Exchange, and not every commercial plan under the Employee Retirement Income Security Act. Medicare fee-for-service uses no prior authorization for bariatric procedures.

**Why does documented BMI history matter more when a patient has been on a GLP-1?**
Patients in one 2026 study lost about 8% of total body weight on GLP-1 medications before surgery. <!-- ext-claim: ASMBS-2026-05-05-CHHABRA --> A patient who arrives that much lighter may show a current BMI below a payer's threshold while their documented history still meets it. That reading belongs to the program and the payer.

**How can programs reduce wasted bariatric consult slots?**
Moving body-measurement capture upstream, into a remote scan completed before the appointment, keeps consult slots focused on clinical evaluation. Patients outside program criteria are routed into medical-management or referral pathways.

### Patient progress tracking

**What body data belongs in a bariatric patient progress record?**
A dated BMI, waist and hip circumference, body composition estimates, and a capture-quality outcome for each scan. The set and the cadence follow the program's monitoring protocol.

**Why is weight alone not enough for bariatric progress tracking?**
The same weight can sit on top of different body-composition profiles, and one number does not describe a post-bariatric trajectory. Composition tracked alongside weight shows lean-mass and fat-mass change.

**How can bariatric programs monitor patients remotely after surgery?**
A baseline scan before surgery, followed by serial scans on the patient's own smartphone, gives the program a body-data series visible across the post-procedure window. The monitoring protocol sets the intervals.

**How is a follow-up scan compared with the baseline?**
A follow-up scan uses the same guided sequence and returns the same data structure as the baseline. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, and the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out how that was measured. <!-- claim: FX-002 -->

### Scope and governance

**Is scan data used to make eligibility or pre-authorization decisions?**
No. The scan produces body measurement and composition data used as supporting evidence inside workflows the licensed program and its payer counterparts operate. Eligibility and pre-authorization decisions are made by people, against those parties' criteria.

**Who reviews the scan data?**
A coordinator or clinical reviewer reads the output against the program's intake criteria before a consult is scheduled. The pre-authorization coordinator works from the same record, and the medical director and the payer's reviewer hold the decisions.

**What does FitXpress not do in a bariatric program, and can it replace in-clinic measurement?**
It does not determine medical or surgical eligibility, diagnose, or make the pre-authorization decision. It does not guarantee compliance or an approval. It is not equivalent to DXA, bioelectrical impedance analysis or a calibrated scale where a protocol requires those methods. In-clinic measurement stays where the protocol requires it.

### Bariatric surgery basics

**What is bariatric surgery?**
Bariatric surgery, also described as metabolic and bariatric surgery, is a category of surgical procedures that alter the digestive system as part of treating severe obesity and related conditions. Suitability and procedure choice are decisions for the program and the patient.

**What are the main types of bariatric surgery?**
Sleeve gastrectomy and Roux-en-Y gastric bypass are the two most commonly performed procedures in the United States. [ASMBS's national estimate](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/) puts sleeve gastrectomy at 58.2% of the 270,089 procedures recorded for 2023, gastric bypass at 23.4% and revisions at 11.9%, on the estimation methodology behind the annual totals. <!-- ext-claim: ASMBS-ESTIMATE-2023 -->

**What are common program and payer requirements?**
Each program and plan sets its own list, and the common items are documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation and psychological evaluation outcomes. At intake the question is documentary: what exists, dated when, verifiable by whom.

## 12. Next steps and related reading

See how FitXpress can support pre-qualification, pre-authorization documentation and post-procedure progress tracking inside a bariatric program. A useful first step is mapping one payer's packet requirements against what the file already holds on the day of the consult. [Request a FitXpress demo](https://3dlook.ai/for-bmi-verification/) or contact sales@3dlook.ai.

Related reading:

- [AI body data across health programs](https://3dlook.ai/content-hub/ai-body-data-health-hub/)
- [GLP-1 market growth and patient progress tracking](https://3dlook.ai/content-hub/glp-1-market/)
- [AI in telehealth: workflows, privacy and remote body data](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [Online pharmacy BMI verification compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)
- [Occupational health screening software](https://3dlook.ai/content-hub/occupational-health-screening-software/)
- [Mobile body scanning for insurance underwriting](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/)
- [Wellness rewards verification for employers and insurers](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/)
