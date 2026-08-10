---
track: seo
product: fitxpress
article_type: use_case_vertical
vertical: occupational_health
target_keyword: occupational health screening software
secondary_keywords:
  - digital occupational health intake
  - pre-employment screening software
  - return-to-work clearance software
  - remote occupational health screening
  - fit-for-duty assessment software
  - workforce screening software
audience: occupational health providers, workforce screening vendors, workers comp administrators, multi-site employers
author: Assel Sekerova
status: ready_for_vadim_full_read
created: 2026-06-08
version: v1
brief_source: Google Doc occupational health (Vadim, 2026-06-08)
compliance_sensitive: true
compliance_guardrails: [no_clearance_decisions, EEOC_pre_post_offer, no_BMI_based_employment, intake_not_clearance_language, no_medical_device_claims]
customer_reference_status: none_yet_research_mode
asselya_review_required: true
external_citations:
  - EEOC enforcement guidance on preemployment disability-related questions and medical examinations under the ADA
  - BLS Survey of Occupational Injuries and Illnesses 2024 (2.5M private-industry cases)
  - ACOEM fitness-for-duty guidance for occupational medicine physicians
  - OSHA 29 CFR Part 1904 recordkeeping
parent_phases: [phase-1-fact-check.md, phase-2-outline.md]
---

# Standardizing Occupational Health Screening: Faster Intake, Better Documentation, Fewer Rescreens

By **Assel Sekerova**, Marketing Lead at 3DLOOK.

> **Industry** — Occupational health providers, workforce screening vendors, workers' compensation administrators, multi-site employers
> **Problem** — Manual intake and inconsistent body measurements slow occupational health screening throughput and cause rescreens, rework, and delayed candidate clearance
> **Solution** — Guided mobile body scan from two smartphone photos completed remotely before the appointment
> **Outputs** — Structured, time-stamped body measurements and BMI/body composition estimates as intake documentation
> **Role** — Intake and documentation layer that supports clinician review — not a fitness-for-duty assessment, clearance decision tool, or basis for hiring decisions
> **Business value** — Faster pre-appointment intake, fewer rescreens, more consistent multi-site documentation, audit-ready records

High-volume occupational health screening still runs on manual intake. Candidates and employees fill out paper questionnaires in the waiting room, medical assistants record body measurements by tape at the appointment, and the same data flows into the clearance workflow through fragmented documentation. The bottleneck is no longer the medical examination — it is the unstructured intake step that happens around it.

The operational consequence is visible at scale. Occupational health providers face capacity-constrained appointment slots; multi-site employer programs face documentation inconsistency across locations; workers' compensation and absence management programs face delayed return-to-work timelines when intake records are incomplete. None of those problems is solved by adding more clinic capacity.

This guide is for occupational health providers, workforce screening vendors, workers' compensation administrators, and multi-site employers evaluating how digital intake supports pre-employment screening, return-to-work clearance, and fit-for-duty workflows. It walks through where FitXpress fits, the two primary use cases, the documentation and compliance posture, and the operational outcomes a digital intake layer can deliver.

> **Disclaimer.** FitXpress and the mobile body scanning workflow described in this article support intake and documentation steps in occupational health screening programs. They do not perform medical examinations, make fitness-for-duty or clearance determinations, replace clinician review or employer policies, or function as a medical device under any regulatory framework. Body measurement and composition outputs are intake data points within the documentation workflow; they are not designed for, and should not be used as, the basis of hiring or employment decisions.

## The problem: occupational health screening still slowed by manual intake

Most occupational health screening programs still depend on intake steps performed by hand at the appointment. The applicant or returning employee arrives at the clinic, completes a written health questionnaire, has body measurements taken by a medical assistant with a tape, and waits while paper records get transferred into the screening file. The medical examination itself happens after that intake work is complete, not before.

That sequencing produces three predictable failure modes. Measurements vary by site, staff member, vendor, or process — tape measurements taken at clinic A are not directly comparable to measurements taken by a different medical assistant at clinic B, and neither is comparable to self-reported numbers from an online employer intake form. Missing or inconsistent information triggers rescreens — when the screening file lands on the reviewer's desk with a missing field or a measurement that does not match other inputs, the candidate or employee is asked back for a second appointment. High-volume employee screening makes small intake inefficiencies expensive — multi-site employer programs that screen thousands of candidates per quarter feel every minute of manual intake added to each appointment.

For programs running across distributed locations and multiple vendors, the cumulative cost is operational rather than clinical. The clearance workflow itself is not broken — the intake feeding it is.

**What causes rescreens in occupational health screening?**
Rescreens often happen when required intake data is missing, body measurements are inconsistent across sites or staff, candidate records do not match provider documentation requirements, or measurement data cannot be verified against other inputs in the file.

## Why this matters now: employers need faster screening without adding clinic capacity

Several pressures are pushing the operational gap wider. Employer hiring volume in workforce-intensive sectors continues to draw on a fixed supply of occupational health appointment slots, and clinic capacity has not expanded proportionately. Workforce screening vendors absorbing multi-employer contracts need repeatable workflows that hold across locations. Workers' compensation and absence administrators face documentation expectations that have moved upstream — review teams now expect structured data, not paper notes.

The volume of return-to-work cases gives the problem its scale. According to the U.S. Bureau of Labor Statistics' Survey of Occupational Injuries and Illnesses for 2024, private industry employers reported 2.5 million nonfatal workplace injuries and illnesses, with an incidence rate of 2.3 cases per 100 full-time-equivalent workers. Each recordable case represents a potential return-to-work clearance pathway later in the workflow. When the intake step for each of those clearances depends on a separate clinic visit, the bottleneck compounds.

The point is not to replace occupational health providers. It is to remove repetitive intake steps before the appointment, so clinical and administrative teams can focus on review, clearance workflows, and exception handling rather than measurement collection.

## What is occupational health screening intake?

Occupational health screening intake is the process of collecting candidate or employee information before a pre-employment, pre-placement, return-to-work, or fit-for-duty assessment. It typically includes identity and role information, health questionnaires, body-related measurements (including BMI inputs), program-specific documentation requirements, and other structured inputs that feed the clearance review.

The boundary between intake and clearance matters. Intake is data collection — gathering the information clinicians and program reviewers need before they make a determination. Clearance is the determination itself, made by a licensed occupational health provider against employer policies, role-specific requirements, and applicable regulatory frameworks. ACOEM guidance for occupational medicine physicians describes fitness-for-duty evaluation as a process of medical review, examination, and documentation conducted within the physician's professional judgment — clarifying that the evaluation itself is clinician-led, with intake data feeding the review rather than substituting for it.

**What is occupational health screening intake?**
Occupational health screening intake is the process of collecting candidate or employee information before a pre-employment, pre-placement, return-to-work, or fit-for-duty assessment. It may include identity details, job-role information, health questionnaires, body measurements, BMI-related data, and the documentation needed to support screening workflows.

## How FitXpress supports digital occupational health intake

[FitXpress by 3DLOOK](https://3dlook.ai/fitxpress/) is a mobile body scanning solution built around a guided two-photo flow. A candidate or returning employee completes a front and side smartphone capture in roughly 45 seconds, without specialized hardware, and FitXpress returns structured body data — 80+ body measurements, BMI inputs, and body composition estimates — to the program before the appointment.

Three properties matter for the occupational health use case:

- **Remote, pre-appointment capture.** The scan happens outside the clinic, on the candidate's or employee's own smartphone, before the visit. The intake data arrives ahead of the appointment slot.
- **Structured, time-stamped outputs.** Each scan generates a record with capture timestamp, validation outcomes from the guided capture, and the underlying measurement set in a machine-readable format — the building block of an audit-ready intake trail.
- **Compliance posture.** FitXpress maintains HIPAA compliance and adheres to GDPR principles, supports Business Associate Agreement (BAA) execution, and runs on encrypted-in-transit, encrypted-at-rest storage with role-based access controls. Personal identifiers are not processed, and captured images are deleted immediately after processing or within a configurable retention window, depending on program policy.

The body-related verification capabilities are the same ones used in [BMI/build verification](https://3dlook.ai/for-bmi-verification/) deployments outside the occupational health context.

BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow. They are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions. Clinical review, fitness-for-duty determination, and employer clearance policies remain with the licensed occupational health provider and the employer's compliance framework.

## Standardizing pre-employment screening before the appointment

Pre-employment screening is where high-volume employer programs feel intake-step inefficiency first. A candidate who has accepted a conditional offer waits to start a job until the screening clears; an occupational health clinic running pre-employment evaluations as part of a workforce screening contract carries a queue of candidates whose start dates are tied to clinic throughput.

In U.S. employment contexts, pre-employment medical examinations apply only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC enforcement guidance under the Americans with Disabilities Act (ADA). FitXpress intake operates inside that framework — it does not enable a pre-offer medical examination and should not be deployed in a way that would.

Inside the post-offer framework, the intake step that precedes the examination is the part that benefits from a digital workflow. The candidate completes a remote two-photo scan on their own smartphone before the appointment, the program receives structured body measurements and BMI inputs ahead of the clinic visit, and the clinic team opens the appointment with the intake record already attached to the case rather than starting the visit by collecting that data manually.

The cumulative effect is operational. Standardized pre-employment screening intake reduces the variability that produces rescreens. Body measurements captured through the same guided flow each time are comparable across candidates, across clinics, and across timepoints — which is what high-volume employer programs and multi-site workforce screening vendors need to make case review repeatable.

FitXpress supports the intake step that feeds the post-offer medical examination. It does not perform the examination, make clearance determinations, or replace clinician review.

**How can employers speed up pre-employment medical clearance?**
Employers and occupational health providers can speed up pre-employment medical clearance by collecting required intake data before the appointment, standardizing candidate body-measurement records, reducing missing information, and giving clinic teams structured records to review during the visit rather than collecting them at it.

## Reducing delays in return-to-work and fit-for-duty workflows

Return-to-work and fit-for-duty workflows share the same operational shape as pre-employment screening but carry more documentation weight. Workers' compensation administrators, absence management programs, and employer health teams need consistent intake records to support clinician review of an employee's readiness to resume duties after injury, illness, or absence.

Delays happen when intake documentation is incomplete or when the program has to schedule a separate measurement visit to fill a gap in the file. A baseline body measurement captured before injury or at first absence does not exist in most program workflows. When a return-to-work review is requested, the clinician is comparing current observation against either self-reported recall or a measurement taken at the same visit. Neither is auditable.

FitXpress can support remote intake before the return-to-work review. The employee completes the same guided two-photo scan on their own smartphone, and the program receives the structured body measurement record ahead of the appointment or asynchronous review. For multi-site employer programs, the data is captured through the same workflow each time, producing comparable records across locations and across pathway stages. The pattern mirrors the [bariatric pre-qualification workflow](https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/), where a baseline scan before a clinical decision and serial scans after it produce structured longitudinal data for program review.

FitXpress supports the intake step that feeds the return-to-work and fit-for-duty workflow. The clearance determination — whether the employee can resume specific job duties — remains with the licensed clinician and the employer's clearance policy.

**What is return-to-work clearance?**
Return-to-work clearance is the process of determining whether an employee can resume specific job duties after injury, illness, absence, or work restriction. It may involve occupational health review, employer policies, role-specific requirements, documentation, and medical or functional assessment, depending on the case.

## Pre-employment screening vs return-to-work screening

The two workflows share intake mechanics but differ in goal, documentation expectations, and clearance criteria.

| Workflow | Typical goal | Common intake need | FitXpress role |
|----------|---------------|---------------------|------------------|
| Pre-employment screening | Support candidate clearance for entry into a job category | Candidate data, body measurements, BMI inputs, program documentation | Remote intake before the post-offer appointment |
| Pre-placement health assessment | Assess readiness for a specific role or placement | Role-specific intake inputs and standardized records | Structured body measurement capture before placement review |
| Return-to-work screening | Support clearance after injury, illness, or absence | Updated body data, documentation, review inputs | Time-stamped intake data before the return-to-work review |
| Fit-for-duty assessment | Assess ability to perform required job duties | Consistent intake and supporting documentation | Standardized measurement data feeding clinical review |

The common thread is that FitXpress sits before the clinical review in each case, never inside it. The clearance and fitness-for-duty determinations belong to the licensed clinician operating against employer policies and applicable regulatory frameworks.

**What is the difference between pre-employment screening and return-to-work screening?**
Pre-employment screening supports candidate clearance before entry into a job category, typically after a conditional offer of employment. Return-to-work screening supports clearance for an existing employee to resume duties after injury, illness, absence, or restriction. Both rely on consistent intake documentation, but the clearance criteria, employer policies, and review pathways are different.

## Better occupational health documentation across sites and vendors

Documentation is where the operational value of structured intake compounds. Under OSHA's 29 CFR Part 1904 recordkeeping standards, employers with 10 or more employees in covered industries are required to maintain records of work-related injuries and illnesses on OSHA Forms 300, 300A, and 301, with annual electronic submission required from establishments meeting size and industry criteria. The recordkeeping framework presumes that the underlying data is consistent across reporting periods and across sites. Free-text notes captured by hand at the appointment do not meet that bar; structured, time-stamped records do.

For occupational health programs, the documentation gains from digital intake are concrete:

- **Standardized body-measurement records** captured through the same workflow each time, comparable across candidates, sites, and program stages.
- **Time-stamped screening documentation** showing when each measurement was captured, under what validation conditions, and against which intake form version.
- **Structured data for review, QA, reporting, and audit defense** — a machine-readable file that can be queried, compared, and validated rather than transcribed.
- **Multi-site consistency** for employer programs running screening across multiple clinics, vendors, or geographies.
- **Easier longitudinal comparison** because intake records produced through the same guided flow at different times sit in the same structural format.

The compliance posture matters at procurement. FitXpress is HIPAA-maintained, BAA-ready, and runs on encrypted-in-transit, encrypted-at-rest storage with role-based access controls — the floor an occupational health program or workforce screening vendor should expect from any partner handling employee body data.

**How can occupational health clinics standardize body measurements across sites?**
Clinics can standardize body measurements by using a consistent digital intake workflow that captures measurements through the same guided flow at every site, stores structured and time-stamped records, and applies the same documentation rules across locations, clinicians, and vendor partners.

## What improves with digital occupational health intake?

Digital intake delivers operational outcomes the buyer can quantify. The relevant metrics are throughput, rework, time to data availability, and documentation quality.

- **Reduced pre-appointment intake delays.** Body measurement capture moves out of the appointment slot. The clinical visit opens with intake data already attached.
- **Higher clinic throughput.** With manual measurement collection removed from the appointment, the same clinic team can process more candidates or employees per day without adding capacity.
- **Fewer rescreens and rework.** Structured intake reduces missing or inconsistent body measurement data — the most common cause of repeat appointments.
- **Faster pre-appointment data turnaround.** Better intake data, available earlier, reduces back-and-forth between intake teams, clinicians, and reviewers. The clearance decision itself remains with the clinician, but the path to the decision shortens.
- **Better documentation quality.** Time-stamped, standardized records support audit-friendly workflows and easier reporting across programs.
- **Lower screening cost per candidate.** More efficient intake reduces repetitive manual work, and the cost saving compounds at multi-site or high-volume scale.

The outcome a buyer should evaluate is not the clearance decision itself — that remains a clinician determination. The right question is whether the workflow leading to clearance has fewer manual steps and produces more consistent records.

## Who uses FitXpress for occupational health screening?

Four buyer profiles deploy FitXpress in occupational health contexts, each with a distinct operational priority.

**Occupational health providers.** Clinics and clinic networks use FitXpress to standardize intake before pre-employment, pre-placement, and return-to-work appointments. The operational gain is throughput per appointment slot and reduced rescreen volume.

**Workforce screening vendors.** Vendors operating multi-employer screening contracts use FitXpress to deliver a repeatable candidate intake workflow across employer programs and across clinic partners. Standardization is the buyer's primary requirement.

**Workers' compensation administrators and absence management providers.** Programs supporting workers' comp claims and absence cases use FitXpress to capture structured body measurement intake for return-to-work documentation. The operational gain is documentation completeness and reduced delay between absence and clearance review.

**Large multi-site employers.** Employer health services, especially across distributed workforces, use FitXpress to drive consistency across locations, screening vendors, and employee populations. The buyer profile here parallels the [employer-side underwriting use case](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/), where the value is structured remote evidence collection at scale.

In each case, FitXpress operates as an intake and documentation layer. The clinical decisioning remains with the licensed provider and the employer's clearance framework.

## More than body scanning: workflow rules, QA, reporting, and scale

FitXpress operates as a digital intake and documentation layer for high-volume occupational health screening workflows. Beyond the raw body measurement capability, it standardizes intake, supports QA, generates structured reporting, and deploys across multi-site programs without on-site hardware. The operational layer is what makes the difference at enterprise scale, where reliable measurement on its own does not solve the screening throughput problem.

Generic body scanning tools may capture measurements. Occupational health programs need more than that — consistent intake workflows, multi-site standardization, audit-ready documentation, role-based access controls, integration paths for downstream review systems, and a compliance posture that holds at procurement. Those are the table stakes for enterprise deployment.

## What FitXpress does and does not do

Compliance and scope are non-negotiable in employment-decision contexts. The table below makes the boundary explicit.

| FitXpress helps with | FitXpress does not do |
|------------------------|--------------------------|
| Remote body measurement intake | Diagnose medical conditions |
| Structured, time-stamped body data | Replace occupational health examinations |
| BMI and body composition estimates as intake inputs | Make fitness-for-duty or clearance decisions |
| Multi-site documentation consistency | Replace clinician judgment or employer policies |
| Workflow standardization across vendors | Override employer clearance frameworks |
| Reporting, QA, and audit-trail support | Act as a standalone medical authority |
| Pre-appointment data turnaround | Inform hiring or employment decisions based on body measurements or BMI |

Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply. The compliance evaluation for an occupational health deployment of FitXpress runs on data privacy and recordkeeping frameworks (HIPAA, GDPR, OSHA recordkeeping, employer-specific data handling) — not on medical device frameworks.

**Can body measurement software replace an occupational health exam?**
No. Body measurement software can support occupational health intake and documentation, but it does not replace occupational health examinations, clinician review, employer-specific clearance policies, or legally required medical decision-making processes.

## How digital occupational health intake works with FitXpress

The implementation pattern is the same across pre-employment, return-to-work, and fit-for-duty workflows. Five steps connect the scan link to the program's existing screening process.

- **Step 1 — The candidate or employee receives a scan link.** The link is sent before the appointment or review, on whatever channel the program already uses for intake communication.
- **Step 2 — The user completes a two-photo scan.** Front and side images, captured on a standard smartphone, with no app installation required. The guided capture runs in roughly 45 seconds.
- **Step 3 — FitXpress captures structured body data.** 80+ body measurements, BMI inputs, and body composition estimates are computed from the two photos. The record is time-stamped and validated through the guided capture sequence.
- **Step 4 — The data becomes part of the intake workflow.** Structured, time-stamped, and ready for clinician review or program-level QA before the appointment.
- **Step 5 — Providers or program teams use the data.** Intake records feed clearance review, documentation, QA, multi-site reporting, and audit-trail workflows. The clinical and clearance decisioning steps continue to run on the program's existing rules.

The integration shape is light. FitXpress sits before the appointment in the program's existing intake channel, and the structured output flows into the existing screening record. No clinic-facing hardware is required.

## Frequently asked questions

**What is occupational health screening intake?**
Occupational health screening intake is the process of collecting candidate or employee information before a screening, physical exam, return-to-work review, or fit-for-duty assessment. It typically includes identity and role information, health questionnaires, body-related measurements, BMI inputs, and program documentation requirements.

**How does digital intake improve occupational health screening throughput?**
Digital intake collects required data before the appointment, reducing manual steps, missing information, and repetitive documentation work during the visit. Clinical visits open with intake data already attached, so the appointment slot can be spent on examination and review rather than data collection.

**How can occupational health providers reduce pre-employment screening bottlenecks?**
Providers can reduce bottlenecks by collecting intake data remotely, standardizing body measurement capture across sites and staff, and giving clinic teams structured records before the appointment. The clearance decision itself remains with the clinician, but the path to it shortens.

**What data is usually collected during pre-employment screening?**
Depending on the employer, role, and provider workflow, pre-employment screening may collect candidate information, job-related requirements, health questionnaires, body measurements, BMI-related data, and the documentation needed for post-offer review. In U.S. contexts, the medical examination component applies only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC guidance under the ADA.

**What is return-to-work clearance?**
Return-to-work clearance is the process of determining whether an employee can resume specific job duties after injury, illness, absence, or work restriction. It may involve occupational health review, employer policies, role-specific requirements, documentation, and medical or functional assessment.

**Can body measurement software replace an occupational health exam?**
No. Body measurement software can support intake and documentation, but it does not replace occupational health examinations, clinician review, or employer-specific clearance policies. FitXpress provides intake data; the clearance determination remains with the licensed provider.

**How does FitXpress support occupational health documentation?**
FitXpress captures structured, standardized, time-stamped body measurement data and BMI inputs that can support consistent intake documentation, QA, multi-site reporting, and audit-trail workflows. The data is machine-readable and produced through the same guided capture each time, making it directly comparable across candidates, sites, and program stages.

### Next steps

See how **FitXpress** can support pre-employment screening, return-to-work clearance documentation, and fit-for-duty intake workflows in your occupational health program. Get in touch with 3DLOOK or [book a FitXpress demo](https://3dlook.ai/pricing/#bd-modal-personalized) to explore the technology in practice with our team.
