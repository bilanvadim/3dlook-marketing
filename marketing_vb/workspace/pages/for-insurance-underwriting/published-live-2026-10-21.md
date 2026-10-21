---
slug: for-insurance-underwriting
title: "Second-source build and BMI evidence for accelerated underwriting"
status: published
published_url: https://3dlook.ai/for-insurance-underwriting/
article_published_time: 
article_modified_time: 
captured_from_live: 2026-10-21
capture_method: "scripts/capture-live.py — curl of the live page, body converted to markdown; images, eBook CTA and author bio dropped"
source_of_truth: live page
---

# Second-source build and BMI evidence for accelerated underwriting

Check disclosed build inside the application, without adding an appointment. Two guided smartphone photos return predicted weight, scan-derived BMI and a discrepancy flag against your threshold to your underwriters in under 45 seconds. [Book a demo](#form)

- 2 smartphone photos
- No integration fee plans from $1,000 a month
- 45sec from scan to results

Trusted by healthcare, digital health & remote-care teams

The Problem

## Why does accelerated underwriting need a second source of build evidence?

The evidence gap becomes material when build affects risk classification but the application relies on self-reported height and weight.

- 59% of applications qualify for accelerated underwriting. [Gen Re, Next Gen Underwriting Survey](https://www.genre.com/content/dam/generalreinsuranceprogram/documents/surveylhilnextgen25-en.pdf)
- #1 build and BMI are the top misclassification reason. [Munich Re,
misclassification analysis](https://www.munichre.com/us-life/en/insights/future-of-risk/misclassification-driving-mortality-slippage-in-auw.html)
- 9vs27 days in automated programs vs. traditional underwriting. [Gen Re, Next Gen Underwriting Survey](https://www.limra.com/en/newsroom/industry-trends/2020/life-insurers-look-to-make-the-underwriting-process-easier-for-customers/)

The speed is worth keeping. The remaining gap is independent build evidence.

Underwriting stages, fraud-prevention support and compliance, in depth:
[AI in insurance underwriting →](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/)

How It Works

## A two-photo check inside your application

FitXpress is embedded in the carrier’s e-application through a web or mobile software development kit (SDK). Results can return to the existing review workflow.

1

The applicant
discloses and scans

Height, weight, age and gender come through your existing fields. Two guided photos follow, with live pose and framing guidance. Clothing-related information can be surfaced for review.

2

FitXpress compares

Smart Scales predicts weight from the scan. Disclosed and scan-derived BMI use the same supplied height. The carrier-defined threshold determines whether the response includes a disclosure flag.

3

The carrier’s rules determine case routing

Cases below the carrier-defined threshold can remain on the accelerated path under the carrier’s rules. Flagged cases go to the existing review queue.

**Recommended setup:** the applicant sees "Scan submitted", and the results go only to your systems.

The same weight check in other regulated flows: [remote BMI verification →](https://3dlook.ai/for-bmi-verification/)

The Underwriting Record

## The underwriting case-file output

FitXpress returns one timestamped, machine-readable record per applicant through its application programming interface (API). The record can be delivered to the carrier’s underwriting workbench, case-management system or policy administration system.

### Accurate 3D body models

Body composition estimates and a 3D model are available when enabled for the deployment.

80+

### Comprehensive Measurements

Access over 80 precise body measurements (circumference and linear).

August, 9th

Disclosed

- Height: 5 ft 5 in
- BMI: 24
More VS

August, 9th

Predicted

- Height: 5 ft 5 in
- BMI: 21
More

### BMI comparison

Disclosed BMI next to scan-derived BMI, both from the same supplied height.

### Quality and status

Pose and framing validation results, applicable capture-failure reasons, clothing-related information surfaced for review, and a timestamp.

### Predicted weight (Smart Scales)

Software-estimated weight for comparison, with ~3.5% mean absolute error under evaluated conditions. Not a scale reading.

### Disclosure flag

Raised when the gap crosses the threshold you set. Disclosed 120 lb Predicted 124 lb +3.3% [Get a sample payload](#form)

Comparison

## FitXpress compared with self-report and a paramedical examination

|  | FitXpress | Self-reported build | Paramedical exam |
|---|---|---|---|
| Where it happens | Remote, inside your application | Application form | Scheduled visit |
| Time to evidence | Under 45 seconds from the photos | Immediate | Days to weeks |
| Disclosure check | Disclosed vs predicted weight, gap quantified | None | Measured on site |
| Record | Timestamped structured record | A self-declared field | Examiner report |
| Best for | Standard-risk cases on the accelerated path | Low face amounts where build isn’t material | Complex and high face amount cases |

A paramedical examination remains part of cases for which the carrier’s guidelines require one. FitXpress adds structured build evidence to cases that remain on the accelerated path.

Proof and Data Handling

## How accurate is FitXpress, and how is underwriting data handled?

Scan records use anonymized, random identifiers to keep scan data separate from direct identification.

- 96-97% measurement accuracy
Typical absolute error: 1.5—2.0 cm 3DLOOK does not use production customer data to train its models.
- < 1cm typical scan-to-scan
difference FitXpress is not a medical device and
does not make underwriting decisions.
- 3.5% Smart Scales predicted
weight mean absolute error

These figures come from internal validation. Peer review and third-party clinical certification are not part of that record, and the full methodology is available under a non-disclosure agreement (NDA). [Body scanning accuracy: an enterprise framework →](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)

### Photos

Deleted after processing or retained for up to 30 days, with retained photos blurred and faces obfuscated during capture.

### Scan records

Scan records use anonymized randomly generated identifiers to keep scan data separate from direct identification.

### Privacy

FitXpress supports HIPAA-governed deployments under a BAA, while under GDPR, customers are typically controllers and 3DLOOK is the processor.

### Training

3DLOOK does not use production customer data to train its models.
Any training use requires explicit, documented authorization.

### Decisions

FitXpress is not a medical device and does not make underwriting decisions. Eligibility, risk class, and pricing remain with your underwriters.

See the [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)

It covers storage, retention, SOC 2, and FDA information.

Pilot

## Evaluate FitXpress before using its outputs in underwriting decisions

FitXpress uses production infrastructure already deployed in remote BMI-verification and weight-management workflows. The underwriting configuration applies the same capture, processing and integration infrastructure to disclosure comparison, internal-only output and case-file integration.

Plans start at $1000 a month for 500 API requests, with no integration fee. [See pricing →](https://3dlook.ai/pricing/)

1. 1

### Walkthrough

The applicant flow on a phone, a sample payload and your integration pattern.
2. 2

### Shadow evaluation

A defined cohort scans while outputs stay out of underwriting decisions.
3. 3

### Evidence comparison

Scan results against independently collected build evidence, on success criteria agreed before the evaluation begins.

### The evaluation should quantify:

- Completion and retake rates
- Agreement with your reference evidence
- How many cases each candidate threshold would flag
- The effect on review volume
[Book a Demo](#form)

##  Frequently asked questions  Questions underwriting teams ask

### Does FitXpress replace the paramedical exam?

No. It adds build evidence to cases your guidelines already send down the accelerated path. Where a guideline calls for an exam, lab work or an attending physician statement, those stay in place.

### How does remote height and weight verification work for life insurance?

Height comes from the application. Smart Scales predicts weight from two guided photos, and both BMIs are calculated from the same supplied height. Your threshold checks the gap between disclosed and predicted weight.

### What happens when a scan fails?

Real-Time Pose Validation pauses capture until pose and framing requirements are met. Clothing-related information may be surfaced for review; it does not trigger a retake. FitXpress returns applicable capture-failure reasons with the record.

### Does FitXpress support HIPAA-governed deployments?

Yes. 3DLOOK can act as a business associate under an executed BAA for qualifying enterprise deployments. The full answer is in the Data, Privacy, Security & Regulatory FAQ.

Last updated: October 2026
