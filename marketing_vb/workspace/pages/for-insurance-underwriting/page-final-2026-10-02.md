---
product: fitxpress
type: use-case-page
vertical: insurance-underwriting
status: final (passed to design 2026-10-02)
url: /fitxpress/for-insurance-underwriting/
canonical: self
language: en
replaces: page-v2-short.md (2026-09-30)
built_from: page-v2-short.md, edited by Asselya (deduplication and language-guardrails pass, 21 edits) and approved by Vadim
source: Drive "page-v2-short (3).html" (uploaded by Vadim 2026-10-02 16:40), saved here as page-final-2026-10-02.html
edits: comments-asselya-2026-10-02.md · what changed beyond her list: review-2026-10-02-final-vs-v2.md
date: 2026-10-02
---

<!-- Transcript of the final HTML, the copy the designer builds from. It is the shape and register
     benchmark for every FitXpress use-case landing (kit-vertical-page.md, "Length and order").
     If the HTML and this file ever differ, the HTML wins. -->

## Yoast

| Field | Value | Length |
|---|---|---|
| SEO title | `Accelerated Underwriting: Build & BMI Evidence \| FitXpress` | 58 / 60 |
| Meta description | `Add remote build and BMI evidence to life insurance accelerated underwriting: two guided photos, predicted weight and a disclosure flag in under 45 seconds.` | 155 / 155 |
| Focus keyphrase | `accelerated underwriting` | |
| Breadcrumb | Home → FitXpress → FitXpress for Insurance Underwriting | |

---

<!-- 1 · HERO -->
**Eyebrow:** FitXpress for life insurance underwriting

# Second-source build and BMI evidence for accelerated underwriting

Check disclosed build inside the application, without adding an appointment. Two guided smartphone
photos return predicted weight, scan-derived BMI and a discrepancy flag against your threshold to your
underwriters in under 45 seconds.

**Primary:** [Book a demo](#demo) · **Secondary:** [Review the case-file output →](#record)

**Under the button:** A walkthrough on a phone, with a sample underwriting record.

**[HERO] mock, case record:** Scan complete · 14:32 UTC · Supplied height 178 cm · Disclosed weight
84.0 kg · Predicted weight (Smart Scales) 89.6 kg · Disclosed BMI / scan-derived BMI 26.5 / 28.3 · Gap vs
your 5% threshold +6.7% · Disclosure flag: Route to review · chips: Pose passed, Framing passed, 2 photos.
Caption: *Illustrative example. Threshold and routing are set by the carrier.*

**Proof strip:**

| 2 photos | Under 45 sec | Your threshold | No integration fee |
|---|---|---|---|
| front and side, on the applicant's own phone | from the photos to structured results | you decide which gap goes to review | plans from $1,000 a month |

---

<!-- 2 · PROBLEM -->
## Why does accelerated underwriting need a second source of build evidence?

The evidence gap becomes material when build affects risk classification but the application relies on
self-reported height and weight.

| 59% | #1 | 9 vs 27 |
|---|---|---|
| of individual life applications qualify for an accelerated path. [Gen Re, 2025 Next Gen Underwriting Survey](https://www.genre.com/content/dam/generalreinsuranceprogram/documents/surveylhilnextgen25-en.pdf) | Build and BMI is the leading misclassification reason in accelerated underwriting monitoring studies, ahead of tobacco. [Munich Re, misclassification analysis](https://www.munichre.com/us-life/en/insights/future-of-risk/misclassification-driving-mortality-slippage-in-auw.html) | average days to decision, accelerated vs traditional underwriting. [LIMRA, automated and accelerated underwriting study](https://www.limra.com/en/newsroom/industry-trends/2020/life-insurers-look-to-make-the-underwriting-process-easier-for-customers/) |

The speed is worth keeping. The remaining gap is independent build evidence.

Underwriting stages, fraud-prevention support and compliance, in depth:
[AI in insurance underwriting →](/content-hub/mobile-body-scanning-insurance-underwriting/)

---

<!-- 3 · HOW IT WORKS -->
## A two-photo check inside your application

FitXpress is embedded in the carrier's e-application through a web or mobile software development kit
(SDK). Results can return to the existing review workflow.

1. **The applicant discloses and scans.** Height, weight, age and gender come through your existing
   fields. Two guided photos follow, with live pose and framing guidance. Clothing-related information
   can be surfaced for review.
2. **FitXpress compares.** Smart Scales predicts weight from the scan. Disclosed and scan-derived BMI use
   the same supplied height. The carrier-defined threshold determines whether the response includes a
   disclosure flag.
3. **The carrier's rules determine case routing.** Cases below the carrier-defined threshold can remain
   on the accelerated path under the carrier's rules. Flagged cases go to the existing review queue.

**Recommended setup:** the applicant sees "Scan submitted", and the results go only to your systems.

The same weight check in other regulated flows: [remote BMI verification →](/for-bmi-verification/)

---

<!-- 4 · RECORD · id="record" -->
## The underwriting case-file output

FitXpress returns one timestamped, machine-readable record per applicant through its application
programming interface (API). The record can be delivered to the carrier's underwriting workbench,
case-management system or policy administration system.

| Field | Returned output |
|---|---|
| Predicted weight (Smart Scales) | A software estimate for comparison with the disclosed weight, with approximately 3.5% mean absolute error under evaluated conditions. Not a scale reading |
| BMI comparison | Disclosed BMI next to scan-derived BMI, both from the same supplied height |
| Disclosure flag | Raised when the gap crosses the threshold you set |
| Build measurements | The circumferences your guideline references. 80+ body measurements, body composition estimates and a 3D model are available when enabled for the deployment |
| Quality and status | Pose and framing validation results, applicable capture-failure reasons, clothing-related information surfaced for review, and a timestamp |

[Get a sample payload](#demo)

---

<!-- 5 · COMPARE -->
## FitXpress compared with self-report and a paramedical examination

| Dimension | FitXpress | Self-reported build | Paramedical exam |
|---|---|---|---|
| Where it happens | Remote, inside your application | Application form | Scheduled visit |
| Time to evidence | Under 45 seconds from the photos | Immediate | Days to weeks |
| Disclosure check | Disclosed vs predicted weight, gap quantified | None | Measured on site |
| Record | Timestamped structured record | A self-declared field | Examiner report |
| Best for | Standard-risk cases on the accelerated path | Low face amounts where build isn't material | Complex and high face amount cases |

A paramedical examination remains part of cases for which the carrier's guidelines require one.
FitXpress adds structured build evidence to cases that remain on the accelerated path.

---

<!-- 6 · PROOF + TRUST -->
## How accurate is FitXpress, and how is underwriting data handled?

| 96-97% | < 1 cm | 3.5% |
|---|---|---|
| accuracy against expert manual measurement, typical absolute error 1.5-2.0 cm | typical scan-to-scan difference for most measurements | mean absolute error of Smart Scales predicted weight under evaluated conditions |

These figures come from internal validation. Peer review and third-party clinical certification are not
part of that record, and the full methodology is available under a non-disclosure agreement (NDA).
[Body scanning accuracy: an enterprise framework →](/content-hub/mobile-body-scanning-accuracy/)

- **Photos.** Deleted immediately after processing or retained for up to 30 days under a
  customer-specific policy. Retained photos are blurred, and face obfuscation is applied during capture.
- **Scan records.** Scan records use anonymized, randomly generated identifiers.
- **HIPAA and GDPR.** FitXpress can support HIPAA-governed deployments under an executed Business
  Associate Agreement (BAA). In most enterprise deployments, the customer acts as the data controller and
  3DLOOK acts as the data processor under GDPR.
- **Model training.** 3DLOOK does not use production customer data to train its models without your
  explicit, documented authorization.
- **Decisions.** FitXpress is not a medical device. It adds evidence to the file, and eligibility, risk
  class and pricing stay with your underwriters.

See the [Data, Privacy, Security & Regulatory FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/)
for storage, retention, System and Organization Controls 2 (SOC 2), and U.S. Food and Drug
Administration (FDA) information.

---

<!-- 7 · PILOT + PRICE -->
## Evaluate FitXpress before using its outputs in underwriting decisions

FitXpress uses production infrastructure already deployed in remote BMI-verification and
weight-management workflows. The underwriting configuration applies the same capture, processing and
integration infrastructure to disclosure comparison, internal-only output and case-file integration.

**Pricing.** Plans start at $1,000 a month for up to 500 scans, with no integration fee.
[See pricing →](/pricing/)

1. **Walkthrough.** The applicant flow on a phone, a sample payload and your integration pattern.
2. **Shadow evaluation.** A defined cohort scans while outputs stay out of underwriting decisions.
3. **Evidence comparison.** Scan results against independently collected build evidence, on success
   criteria agreed before the evaluation begins.

The evaluation should quantify: completion and retake rates · agreement with your reference evidence ·
how many cases each candidate threshold would flag · the effect on review volume.

[Book a demo](#demo)

---

<!-- 8 · FAQ · FAQPage schema, answers byte-identical in JSON-LD -->
## Questions underwriting teams ask

### Does FitXpress replace the paramedical exam?
No. It adds build evidence to cases your guidelines already send down the accelerated path. Where a
guideline calls for an exam, lab work or an attending physician statement, those stay in place.

### How does remote height and weight verification work for life insurance?
Height comes from the application. Smart Scales predicts weight from two guided photos, and both BMIs are
calculated from the same supplied height. Your threshold checks the gap between disclosed and predicted
weight.

### What happens when a scan fails?
Real-Time Pose Validation pauses capture until pose and framing requirements are met. Clothing-related
information may be surfaced for review; it does not trigger a retake. FitXpress returns applicable
capture-failure reasons with the record.

### Does FitXpress support HIPAA-governed deployments?
Yes. 3DLOOK can act as a business associate under an executed BAA for qualifying enterprise deployments.
The full answer is in the
[Data, Privacy, Security & Regulatory FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

---

<!-- 9 · FORM · id="demo" · shared HubSpot form FX | LP | Demo, GTM fx_vertical = insurance -->
## Review the applicant flow and case-file output

We walk the applicant flow on a phone, show a sample underwriting record, and scope a shadow evaluation
against your current build evidence.

Not ready for a call? [Start with the underwriting analysis](/content-hub/mobile-body-scanning-insurance-underwriting/).

**Form:** shared `FX | LP | Demo`. The prototype mock shows Work email, Company, Job title and the
optional "Expected monthly scan volume"; the live page embeds the shared HubSpot form.

**Footer:** FitXpress for insurance underwriting · Procurement and security documentation:
[legal@3dlook.me](mailto:legal@3dlook.me)
