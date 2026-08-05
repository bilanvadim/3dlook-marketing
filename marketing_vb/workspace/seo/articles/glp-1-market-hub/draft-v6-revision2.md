---
slug: glp-1-market
product: fitxpress
title: GLP-1 Market Growth and the Need for Better Patient Progress Tracking
primary_keyword: GLP-1 market growth
secondary_keyword: GLP-1 patient progress tracking
meta_description: "GLP-1 market growth is outpacing how programs track patient progress. Why scale weight alone falls short, and what better tracking looks like."
primary_use_case: FitXpress for Telehealth & Weight Loss
hub: glp-1-market
cluster: main-hub
intent: hub
action_type: refresh-expand-existing
priority: P0
existing_urls: https://3dlook.ai/content-hub/glp-1-market/
cannibalization_guardrail: "Avoid duplicating GLP-1 Market, Visual Progress Tracking, Beyond BMI, and Online Pharmacy BMI Verification. Make each page own a distinct intent."
vertical_boundary: "Owns GLP-1 market growth, program models (telehealth, in-person/hybrid clinic, pharmacy-led, employer/wellness), the progress-tracking gap as an industry-level problem, and the operator/clinic-workflow view. Does not own diagnosis, treatment/eligibility/underwriting decisions, replacement of clinicians or DXA/BIA/calibrated scales, guaranteed weight-loss/adherence/compliance outcomes, automatic fraud detection, medical-device framing, or GLP-1 drug clinical-efficacy claims."
author: Assel Sekerova
status: draft
created: 2026-08-01
revised: 2026-08-05
revision_note: "Review 2 applied per review2-comments.md (18 priority + structural refinements)."
claims_used: [FX-001, FX-003, FX-004, FX-005, FX-006, FX-007, FX-009, FX-010, FX-012]
---

# GLP-1 Market Growth and the Need for Better Patient Progress Tracking

## GLP-1 Growth Is Changing How Weight-Management Programs Operate

Few categories in healthcare have scaled as fast as glucagon-like peptide-1 (GLP-1) medications for weight management. What started inside diabetes care has widened into a broad weight-management market with its own operators, delivery models, and economics.

That growth pulled in far more than drug manufacturers. Telehealth clinics, in-person and hybrid weight-loss clinics, pharmacy-led programs, and employer and wellness platforms have all built GLP-1 offerings around the medications. Each runs a longitudinal program: a patient starts treatment, then checks in over weeks and months while their body changes.

As patient volumes climb, the operational focus extends beyond onboarding to supporting patients through months of treatment. Documenting and reviewing progress across months of treatment, at the volumes GLP-1 programs now handle, is where the infrastructure gets tested. This hub covers the market side of that story: how fast GLP-1 programs are growing, what is driving that growth, how the delivery models built around GLP-1 differ, and what the resulting infrastructure challenge means for progress tracking.

**Short answer.** GLP-1 market growth is expanding from diabetes treatment into dedicated weight management, pulling in more delivery models and more patients per program. That growth is creating an infrastructure challenge: programs need a repeatable way to document patient progress beyond scale weight, at a volume that makes manual methods increasingly difficult to scale.

*Scope note. This is a market and workflow resource, not medical or clinical advice. Nothing here describes eligibility, diagnosis, dosing, or treatment. Those determinations belong to clinicians and to each program's own protocols.*

Several adjacent topics have their own pages, and the links below point to them rather than repeating them. For the evidence connecting visible progress to member engagement and retention, see [Visual Progress Tracking for GLP-1](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/). For why body mass index (BMI) is only a partial signal, see [Beyond BMI](https://3dlook.ai/content-hub/beyond-bmi-business/). For the regulated online-pharmacy compliance workflow, see [Online Pharmacy BMI Verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) and the [GLP-1 Compliance Challenge](https://3dlook.ai/content-hub/glp-1-compliance-challenge/).

## GLP-1 Market Size and Growth Trajectory

The headline figures are large and rising. J.P. Morgan Research projects the global market for GLP-1 and related incretin therapies to reach roughly **$200 billion by 2030**, framing obesity treatment as one of the fastest-growing areas in pharmaceuticals ([J.P. Morgan Research](https://www.jpmorgan.com/insights/global-research/current-events/obesity-drugs)). The trajectory is driven mainly by patient volume rather than price, as more people start and stay on treatment.

Patient counts show the same climb. The same analysis estimates that GLP-1 use in the United States rose from about 6 million people in 2024 to roughly 10 million in 2025, and projects 25 to 30 million Americans on these medications by 2030.

The runway extends further still. Only about 7% of people with diabetes and roughly 2% of people with obesity who may be eligible for treatment were using GLP-1 medications globally, which leaves substantial headroom as the use case widens from diabetes management into dedicated weight management.

Employer participation shows the same widening, and it comes with cost pressure attached. The Kaiser Family Foundation (KFF) 2025 Employer Health Benefits Survey found that **43% of firms with 5,000 or more workers covered GLP-1 agonists when used primarily for weight loss in 2025, up from 28% the year before**. Among those large employers, **59% reported higher-than-expected utilization** of the benefit, and **66% said GLP-1 coverage had a significant effect on their prescription-drug spending** ([KFF](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/)). Coverage is expanding and, at the same time, running ahead of what employers budgeted for.

## What Is Driving Market Expansion

Several forces are compounding at once, and together they explain why GLP-1 has moved from a diabetes drug class to a mainstream weight-management category with its own delivery infrastructure.

**The use case is expanding beyond diabetes.** GLP-1 medications were developed for diabetes management, and weight management is now the faster-growing indication. That shift changes who the patient population is and how long a typical program runs.

**Employers and payers are participating at greater scale.** The move from 28% to 43% coverage among large employers in a single year signals that weight-loss coverage is becoming more common among very large employers.

**Virtual and hybrid care models are absorbing much of the new volume.** Telehealth and hybrid programs let a patient start and continue GLP-1 treatment without visiting a clinic for every check-in, one of the delivery shifts behind the market's rapid growth.

**Utilization is exceeding what payers expected.** KFF's finding that 59% of large employers saw higher-than-expected utilization suggests demand is outpacing the assumptions programs and payers built their coverage models around.

**Cost and coverage pressure is following demand.** With 66% of large employers reporting a significant effect on drug spending, this cost pressure may increase demand for clearer program-level outcome reporting.

**The commercial relationship is shifting from medication access to ongoing program support.** Early GLP-1 programs largely competed on getting patients access to a prescription. As coverage becomes more common, competition moves toward what happens after the prescription: how well a program supports a patient through months of treatment.

**Program infrastructure matters more as patient volumes increase.** A program managing dozens of patients can absorb manual, inconsistent documentation. A program managing thousands cannot: the tools built for a smaller, access-focused market do not scale cleanly to the volume and duration GLP-1 programs now operate at. That gap is the subject of the next two sections.

## How the GLP-1 Care Ecosystem Is Evolving

GLP-1 care now runs through several distinct delivery models, and each shapes how a program can realistically track patient progress.

**Telehealth programs** onboard patients entirely online. A patient never visits a clinic in person, so intake and every check-in depend on data the patient can produce remotely, without a clinician present to take a measurement.

**In-person and hybrid clinics** combine scheduled office visits with remote stretches between them. The gap a program has to fill is that interval between appointments, where a clinic still wants a consistent record without asking a patient to come in.

**Pharmacy-led programs**, common in regulated markets, may combine intake and eligibility-related documentation with recurring remote reviews over the course of treatment. The regulated BMI-verification workflow that governs the point of prescription is covered separately in the [Online Pharmacy BMI Verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) guide.

**Employer and wellness programs** attach GLP-1 support to a benefits or wellness platform, often across a distributed workforce. These programs need standardized check-ins that produce comparable records across many participants, since the employer or plan is typically the party asking for reporting.

Across all four models, the shared requirement is the same: a way to capture body data consistently, whether or not a clinician is in the room, and whether a patient is onboarding for the first time or checking in for the tenth time.

## The Infrastructure Challenge Created by Market Growth

Most GLP-1 programs today track progress with a thin set of signals: scale weight, patient self-report, and an occasional, manually captured progress photo. That combination was inherited from the pre-medication weight-loss world, and the growth described above is exposing its limits.

The first limitation is consistency. Self-reported measurements are easy to misstate. Differences in lighting, pose, distance, and camera angle can make successive photos harder to compare consistently.

The second limitation is what this does to clinical review. A care team opening a patient record and finding a single weight value and a free-text note has little structured information that can be compared consistently across check-ins. At the caseload sizes described above, thin and inconsistent inputs slow review down rather than speeding it up.

The third limitation is what it does to program economics and engagement. As payers and employers cover the weight-loss indication at greater scale and see costs run ahead of expectations, that cost pressure may increase demand for programs that can document outcomes rather than rely on self-reported figures. Limited progress visibility can also make it harder for programs to maintain member engagement between check-ins; the detailed evidence behind that link lives on the [Visual Progress Tracking for GLP-1](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/) page.

Structured, repeatable body measurement addresses these three limitations directly, and the next two sections cover what that looks like and what it requires.

## Why Scale Weight Alone Provides an Incomplete Progress Record

Scale weight and BMI are partial signals. Both compress a complex physical change into one number, and neither separates whether a change in weight came from fat, lean mass, or fluid. For a GLP-1 program, that gap matters because preserving lean mass during rapid weight loss is a recognized clinical concern documented in the endocrinology literature ([Neeland et al., *Diabetes, Obesity and Metabolism*, 2024](https://dom-pubs.onlinelibrary.wiley.com/doi/10.1111/dom.15728)), and a scale cannot show whether it is happening.

Body composition is a richer longitudinal signal than weight alone. Fat percentage, lean mass, and fat mass, tracked over successive check-ins, describe the shape of a change rather than only its size. Longitudinal body-composition estimates can provide additional context that scale weight alone does not capture.

The fuller critique of BMI as a metric, including where it still has operational uses, lives on the [Beyond BMI](https://3dlook.ai/content-hub/beyond-bmi-business/) page.

## What Better GLP-1 Progress Tracking Looks Like

Across delivery models, better progress tracking for a GLP-1 program tends to share five properties.

**Consistent baseline.** Every patient starts from a measurement captured the same way, so later check-ins have something reliable to compare against.

**Repeatable remote capture.** The check-in method needs to work whether or not a clinician is present, and it needs to produce comparable results each time a patient uses it, rather than a fresh set of assumptions with every visit.

**Longitudinal comparison.** Comparing one check-in to the next only works if the measurement noise between them is small enough that a real change is not lost inside it.

**Body-composition estimates.** As covered above, a program that can look past scale weight toward composition has a more complete view of what is changing in a patient's body during treatment.

**Clinician-accessible records.** Structured, consistent data is faster for a clinician or care coordinator to scan across a caseload than a free-text note and a lone weight value, which matters as caseloads grow.

How these properties come together in practice depends on where a program sits in the ecosystem described above, but the pattern holds wherever volumes are high: when every patient is captured through the same guided process, review is faster, longitudinal comparison is more meaningful, and the program has a stronger basis for the outcome reporting that cost-conscious employers and payers may increasingly ask for, a dynamic covered in more detail on the [GLP-1 Compliance Challenge](https://3dlook.ai/content-hub/glp-1-compliance-challenge/) page.

Several vendors and internal tools address parts of this list. FitXpress is one structured body-data capture layer built around these five requirements; the next section covers specifically where it fits and where its role stops.

## Where FitXpress Fits

FitXpress is a structured body-data capture layer that programs can build into a GLP-1 workflow at intake and at every check-in, giving clinical and program teams more consistent longitudinal records to work from instead of self-report.

A guided scan uses two photos, front and side, and returns results in under 45 seconds, producing 80+ body measurements without specialized hardware. FitXpress provides BMI-related and calculated outputs, including BMI and basal metabolic rate (BMR), alongside software-derived body-composition estimates such as body fat percentage, lean mass, and fat mass. In testing with participants wearing tight-fitting clothing, predicted weight showed a mean absolute error of approximately 3.5%, offered as context rather than a replacement for a calibrated scale.

The core of the fit for a GLP-1 program is longitudinal comparison: for most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, letting a program compare changes using a consistent capture method rather than differently posed photos or self-reported numbers. Measurement-level accuracy against expert manual measurement is detailed on the [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) page.

FitXpress is delivered as a white-label application programming interface (API) and software development kit (SDK), so a program can build the guided scan into its own patient experience. Photos are deleted after processing in production workflows, while structured outputs are retained according to the applicable deployment and agreement. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR; under an executed Business Associate Agreement, 3DLOOK can also act as a business associate for HIPAA-regulated deployments. Full detail is on the [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) page.

UK Meds uses FitXpress for BMI verification in an online-pharmacy context, covered on the [Online Pharmacy BMI Verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) page. For how two photos become structured body data, see [How 3DLOOK Turns Two Photos Into Structured Body Data](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/). This hub sits under the [AI Body Data for Health hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/).

## Role and Limitations of Mobile Body Scanning

FitXpress supports capture, comparison, and documentation within a program's existing workflow: it standardizes how a body measurement is taken and makes successive check-ins comparable. Diagnosis, prescribing, and eligibility decisions stay with clinicians and the program's own protocols. Where a workflow or regulatory standard calls for dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis (BIA), or a calibrated scale, FitXpress is designed to complement those methods rather than substitute for them, and its outputs are meant to be read in the context of the program's own protocol and clinical judgment.

## Frequently Asked Questions

**How big is the GLP-1 market?**
J.P. Morgan Research projects the global market for GLP-1 and related incretin therapies to reach roughly $200 billion by 2030. Estimates vary by firm and by how each defines the category, and the trajectory is driven mainly by patient volume rather than price. The runway is large: only a small share of the eligible diabetes and obesity populations currently use these medications.

**What is driving GLP-1 market growth?**
Growth comes from several forces compounding together: the use case expanding from diabetes into dedicated weight management, wider employer and payer coverage of the weight-loss indication, and utilization running ahead of what payers initially expected. KFF found that 43% of firms with 5,000 or more employees covered GLP-1s for weight loss in 2025, up from 28% in 2024, with 59% of those employers reporting higher-than-expected utilization and 66% reporting a significant effect on drug spending.

**Why do GLP-1 programs need progress tracking?**
As coverage and patient volumes grow, cost pressure on payers and employers may increase demand for programs that document outcomes rather than rely on self-reported figures alone. Scale weight is a thin signal on its own, and manual, inconsistent inputs are harder for care teams to review at scale. Structured, repeatable body data, including longitudinal body-composition estimates, gives programs a clearer, more comparable record of what is changing over the course of treatment.

**What should GLP-1 programs track beyond scale weight?**
Body composition, meaning fat percentage, lean mass, and fat mass tracked over successive check-ins, gives a program a view of the shape of a change rather than only its size. Programs also benefit from a consistent capture method at intake and at every check-in, so results are comparable over time rather than dependent on who captured them or how.

### Next Steps

See how FitXpress supports GLP-1 programs with structured progress tracking: explore [FitXpress for telehealth and weight loss](https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/).

*For data, privacy, and regulatory details, see the [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) and 3DLOOK's [legal information](https://3dlook.ai/legal/).*
