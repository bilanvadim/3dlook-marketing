---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
status: fixture
fixture: frozen known-good article for scripts/test-pipeline-changes.sh
fixture_source: the editor's final of the occupational-health intake article, 2026-09-11, plus claim markers
---

# Manual vs Digital Intake in Occupational Health Screening: A Workflow Comparison

## Where manual intake can slow occupational health screening

(Cover) - Concept

Where a screening process requires both a health questionnaire and body measurements, those tasks often take place during the appointment. The candidate or employee completes the form, the clinic staff takes measurements with a tape measure, and the information is entered into the record before clinical review begins.

Moving eligible steps online changes when the record becomes available and how much work remains inside the appointment.

When intake takes place during the visit, incomplete forms, unusable measurements, and manual record entry compete with testing and examination for the same appointment time. Adding more slots may increase capacity, but it leaves that work unchanged inside each visit.

The choice turns on two questions: which steps can be completed remotely, and whether moving them addresses a documented operational problem. The [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/) covers the broader category, common use cases, and end-to-end workflow.

**Scope note.** Digital intake refers to the overall pre-appointment process. FitXpress provides remote body-measurement capture. The program’s intake system handles questionnaire collection; testing, examination, and clinical review take place within the wider screening process. FitXpress does not perform medical examinations, make fitness-for-duty or clearance determinations, or serve as a basis for hiring or employment decisions. FitXpress is not a medical device.

## Short answer: what each intake method covers
- **Manual intake** combines a paper or staff-administered health questionnaire, tape measurement, and record entry at or around the appointment.
- **Digital intake** collects questionnaire content through the program’s structured pre-appointment system. FitXpress adds remote body-measurement capture through a guided two-photo smartphone scan completed in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 -->
- **What was moved before the visit?** Questionnaires and eligible body measurements can be completed remotely. Equipment-based testing and physical examination continue on-site.
- **Effect on appointment time.** Moving eligible steps before the visit can reduce in-appointment collection and transcription, although the result varies with completion rates, fallback volume, integration quality, and the causes of existing rescreens.
- **How the methods differ.** Manual intake provides immediate in-person support, while digital intake makes eligible information available before the appointment.

## The three phases of the occupational health screening workflow

Occupational health screening consists of three phases. Pre-appointment intake is the first step, followed by on-site screening and clinical review. Remote intake applies to the first phase; testing, examination, and clinical review fall under the broader screening process.
- **Pre-appointment intake.** The health-history questionnaire, required documents, and eligible body measurements can be collected before the visit.
- **On-site screening.** Drug screening, vision and hearing checks, functional assessment, and physical examination may require equipment or in-person evaluation.
- **Clinical review.** The reviewing provider assesses the record and makes any determination required by the program.

(*Image 1*) - Concept

The measurement step is particularly sensitive to differences in technique. The [National Health and Nutrition Examination Survey (NHANES) anthropometry procedures manual](https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf) specifies the waist-measurement procedure in detail: the examiner palpates the uppermost lateral border of the right ilium, marks it at the midaxillary line, asks a recorder to check that the tape is level, and takes the reading at normal expiration. The protocol outlines the training, landmarking, and quality-control requirements for producing standardized manual measurements.

The [Occupational Safety and Health Administration (OSHA) respiratory protection standard](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134AppC) illustrates how confidentiality requirements can shape the intake route. Appendix C requires employees to be able to complete the questionnaire privately and prevents employers and supervisors from reviewing their answers. The rule applies specifically to respirator medical evaluations, and the form must be submitted to the reviewing health care professional through an appropriate channel.

The program’s intake system administers the questionnaire; the reviewing health care professional conducts the medical evaluation and makes any clearance determination.

## Manual vs digital intake, compared dimension by dimension

The capture method is one part of the comparison. Set-up, ongoing staff work, access, integration, and exception handling also affect the choice.

| **Dimension** | **Manual intake** | **Digital intake** |
|---|---|---|
| Where intake happens | Usually at or around the clinic appointment | Remotely before the appointment |
| Capture and measurement | Clinic staff take measurements with a tape measure | The individual captures guided photos; [FitXpress](https://3dlook.ai/) generates the measurements |
| Procedure consistency | Varies with technique, landmarking, and local training | Uses a standardized guided procedure, subject to capture-quality and validation requirements |
| Record format and transfer | May require manual entry or document scanning; structure depends on the receiving system | Can provide structured data when the integration supports it |
| Questionnaire confidentiality | Depends on paper handling, access controls, and local routing | Depends on permissions, configuration, and the program’s data-handling design |
| Appointment-time work | Can include questionnaire completion, measurement, and transcription | Can focus on testing, examination, and intake exceptions that require staff support |
| Access and support | Provides immediate in-person support but requires attendance | Requires a compatible device and network access, with support for incomplete or failed capture |
| Set up an ongoing effort | Lower initial technology requirements; recurring staff time for collection, measurement, and record entry | Integration, configuration, and staff training before launch; ongoing monitoring and exception support |
| Exceptions and fallback | Usually handled in person during or after the visit; available as the in-person pathway | Requires a defined manual alternative for people unable to complete the remote intake |
| Integration dependency | Can operate without systems integration, but may require manual entry into the receiving system | Automated transfer requires a receiving system and integration path; a portal can provide a separate review route when automated transfer is unavailable |
| Corrections | May require re-entry or record amendment | Integration can reduce manual re-entry; the receiving system determines how corrections are handled |

Manual intake is easier to introduce and gives staff an immediate way to help. Digital intake requires more setup, but it can make records available earlier and reduce transcription where systems are connected. Volume, access, exception rates, and existing technology determine which trade-offs matter most.

## How the workflows differ

The steps are similar; their timing and location change.

| **Manual or on-site intake** | **Structured pre-appointment intake** |
|---|---|
| Forms are completed at or around the appointment | Forms are completed through the program’s intake system |
| Staff perform required measurements | The individual captures the required inputs remotely; measurements are generated for the record |
| Information is entered or transcribed | Structured data can be validated and transferred according to the integration design |
| Missing items are handled during or after the visit | Exceptions can be identified before the visit |
| Tests and examinations follow | Tests and examinations remain on site |

Completing intake early gives the program time to identify missing information before the person arrives, provided the process includes the necessary validation rules. Testing and examination continue on site.

## A decision framework: which intake method fits which program

### Manual intake fits when
- Appointment capacity is sufficient for the current volume.
- Reliable smartphone or network access is limited.
- Body measurement represents a small part of the intake workflow.
- Measurement is intentionally completed during the examination.
- The downstream system cannot receive structured records.

### Digital intake fits when
- High volume places pressure on fixed appointment capacity.
- Multiple sites or vendor partners require a standardized process.
- Rescreens are linked to missing or inconsistent intake data.
- Records need to be available before the appointment.
- The receiving system can accept structured information.

### A hybrid model fits when
- Eligible questionnaires and measurements can be completed before the visit.
- Equipment-based testing and examination remain on-site.
- A manual fallback and transfer path is defined for each remote step.

In US pre-employment processes, [EEOC guidance](https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical) explains that disability-related questions and medical examinations may be introduced only after a conditional job offer. The same inquiry or examination must apply to all entering employees in the job category, and medical information must remain confidential. When technology is part of the process, the organization must consider potential disadvantages for people with disabilities and provide reasonable accommodations where required. These obligations apply regardless of the capture method. Requirements in other jurisdictions vary.

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path.

Programs can test the operational effect by comparing appointment-time intake, missing records, corrections, and rescreens before and during the pilot. They should also track pre-appointment completion, manual fallback, and records transferred without re-entry. Changes in throughput or rescreens are meaningful when the existing causes are connected to intake.

## Where FitXpress fits

(Image 2) - Concept

[FitXpress](https://3dlook.ai/) provides remote body measurement within pre-appointment intake. The individual completes a guided two-photo smartphone scan in under 45 seconds. The resulting record includes 80+ body measurements, BMI, and a session timestamp. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 --> <!-- claim: FX-009 -->

What counts as adequate performance depends on how the measurements will be used. For intake documentation, two questions matter: how closely results match the selected reference and how consistently repeated scans perform across sites and time points.

Repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and distinguishes repeatability from accuracy, robustness, output fit, and validation strength. <!-- claim: FX-003 -->

A separate validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. These findings establish performance relative to the selected reference; they do not demonstrate superiority over expert tape measurement. <!-- claim: FX-001 -->

Operational value also comes from when and how results enter the process. A timestamped record can support comparison and reduce re-entry, though comparability still depends on the measurement protocol and receiving system.

FitXpress encrypts data in transit and at rest, deletes photos after processing, and retains generated outputs in accordance with the deployment terms. In most enterprise deployments, the customer acts as the controller, and 3DLOOK acts as the processor under the General Data Protection Regulation (GDPR). A Business Associate Agreement under the Health Insurance Portability and Accountability Act (HIPAA) is available on request. FitXpress supplies body-measurement data for clinician review; clearance, eligibility, and fitness-for-duty determinations remain with the responsible professionals.

## Frequently asked questions

### Is digital intake more accurate than manual tape measurement in occupational health screening?
3DLOOK’s published figures compare FitXpress with expert tape measurements, which serve as the reference. The relevant question is whether the reported error and repeatability are suitable for the intended workflow. For most evaluated measurements, typical differences between repeated scans were below 1 cm; the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the evaluation conditions. <!-- claim: FX-003 -->

### Which parts of occupational health screening remain on-site?
Initial history and symptom collection can occur remotely, while clinical follow-up remains with the reviewing provider. Equipment-based testing, functional assessment, and physical examination continue on-site when they require equipment or in-person evaluation.

### What happens if a person cannot complete a remote scan?
Some people may lack the required device or connection; others may be unable to complete the capture protocol. The program, therefore, needs a documented manual alternative.

## Next steps

Compare the two intake models against the program’s throughput, rescreen causes, and documentation requirements to determine which steps belong before the appointment. Then [talk to 3DLOOK about the intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).
