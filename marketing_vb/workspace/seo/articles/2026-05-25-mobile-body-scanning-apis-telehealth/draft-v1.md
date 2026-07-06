---
track: seo
product: fitxpress
article_type: comparison_buyers_guide
target_keyword: mobile body scanning solution
secondary_keywords:
  - telehealth body scanning
  - body scanning APIs for health apps
  - BMI verification
  - GLP-1 patient tracking
  - patient engagement metrics
  - longitudinal body data
author: Assel Sekerova
status: ready_for_qc
positioning: telehealth_verification_focused
created: 2026-05-25
---

# Best Body Scanning APIs for Telehealth, Verification & GLP-1 Programs in 2026: A Buyer's Guide

Body scanning has shifted from a fit-tech category to a verification category. Teams building telehealth weight-loss flows, online pharmacy BMI checks, insurance underwriting screens, and employer wellness programs are now evaluating mobile body scanning APIs as compliance and program infrastructure, not as a consumer engagement feature. This guide compares the leading vendors against the criteria that matter for those use cases — and shows where each one is the right fit.

**Disclaimer.** Mobile body scanning APIs can support telehealth, verification, and wellness workflows, but they do not provide diagnoses, replace required medical evaluations, or make clinical judgments. This guide compares vendor capabilities, not clinical performance. Decisions about prescribing, underwriting, or reward distribution remain with the operator and the relevant clinical or compliance reviewer.

**Author disclosure.** This guide is written by Assel Sekerova, Marketing Lead at 3DLOOK. 3DLOOK builds FitXpress, one of the products covered. Competitor information is drawn from publicly available vendor pages and third-party reporting; nothing in the competitor sections is invented. Where a vendor does not publicly document a capability, the entry reads "not publicly documented" rather than an assumed value.

## Why body scanning is becoming critical for telehealth and verification programs

Four shifts are pushing body scanning out of "nice to have" and into procurement decks.

GLP-1 prescribing has moved BMI verification from clinical hygiene into a regulatory front. According to KFF's 2025 Employer Health Benefits Survey, 43% of firms with 5,000 or more workers covered GLP-1 agonists for weight-loss purposes in 2025, and 34% of those firms now require enrollees to meet with a dietitian, case manager, or therapist, or to participate in a lifestyle program. The eligibility gate that triggers all of that is BMI. When BMI comes from a self-reported number plus a camera-roll photo, the gate is no longer defensible.

Self-reported body data is structurally unreliable. CDC researchers found that self-reported data underestimated the overall prevalence of severe obesity by 40%. Munich Re reported in 2025 that BMI misrepresentation is the second-largest driver of misclassification in accelerated underwriting programs, after smoking non-disclosure. These are not edge-case concerns.

Photo uploads have lost their evidentiary weight. Free generative AI tools can produce a convincing inflated "before" body image in seconds. A passive file upload has no capture time, no liveness, and no proof the photo belongs to the patient submitting it.

Compliance posture has become a procurement gate. HHS reported that in 2023 alone, more than 167 million individuals were affected by large health data breaches, and the number of breaches rose 102% from 2018 to 2023. For any vendor serving US healthcare or EU operations, documented HIPAA, BAA, and GDPR alignment is now table stakes.

Those four shifts shape the evaluation rubric in the next section.

## The evaluation checklist: 10 criteria that matter for healthcare use cases

These criteria are weighted toward telehealth, verification, GLP-1, and wellness rewards buyers specifically. Apparel-only or consumer-fitness buyers may rank some lower.

**1. Capture method.** Live SDK capture in-session, or camera-roll upload? Only in-session capture closes the AI-photo-manipulation gap that now affects every weight-loss eligibility flow.

**2. Repeatability for longitudinal programs.** Variance between back-to-back scans of the same subject. GLP-1 progress, wellness rewards, and insurance review all compare scans across weeks or months. High variance destroys the longitudinal trend signal.

**3. Accuracy and measurement coverage.** Number of measurements returned, benchmark methodology, ISO conformance. A vendor citing "highly accurate" with no published methodology is unverifiable.

**4. HIPAA / BAA / GDPR posture.** Documented compliance positioning, BAA willingness, encryption controls, retention policy. This is now a procurement gate for US healthcare and EU operations.

**5. Anti-manipulation defenses.** Liveness checks, pose validation, clothing detection, weight-disclosure cross-check. GLP-1 eligibility flows are now being gamed; vendors that built capture for fitness engagement five years ago may not have these layers.

**6. Deployment patterns.** Client-side, server-side, or hybrid. Compliance buyers often need body metrics never exposed back to the patient — a "Pattern B" server-side flow.

**7. Audit and exportable evidence.** Timestamped logs, exportable records, regulator-review readiness. When an audit comes, "we looked at the photo" is not a defense.

**8. Integration boundaries.** A clear "we provide / you build" scope and an SDK plus API model. A vendor that blurs scope creates integration risk and ownership ambiguity for the buyer.

**9. Patient experience.** Time to result, friction, device requirements. Completion rate determines program ROI, especially for GLP-1 retention where every additional step lowers compliance.

**10. Pricing transparency and program ROI tracking.** Published pricing tiers, visibility into measurable program outcomes. Budget approval and program ROI tracking both depend on it.

## 3DLOOK FitXpress — built for telehealth verification and GLP-1 programs

```
Industry      — Telehealth, online pharmacy, employer wellness, insurance underwriting
Problem       — Self-reported BMI is unreliable; photo uploads have no provenance;
                longitudinal programs need repeatable scans
Solution      — Two-photo guided capture via SDK, with server-side processing options
Outputs       — 80+ body measurements, BMI/BMR/body fat %/lean and fat mass, Smart Scales,
                Future Body, audit-ready records
Role          — Verification and longitudinal-tracking support layer — not clinical decisioning
Business value — Anti-manipulation defense layer, ISO 8559-1:2017-compatible accuracy,
                HIPAA + BAA + GDPR posture, clear "we provide / you build" boundary
```

FitXpress by 3DLOOK turns two smartphone photos into 80+ body measurements, body composition outputs (BMI, BMR, body fat %, lean and fat mass), and a 3D body model in under 45 seconds. The capture happens through an SDK with real-time pose validation, not from the camera roll. Clothing detection flags oversized or baggy attire used to inflate visual BMI. Smart Scales cross-checks the patient's self-reported weight against the AI-derived estimate and flags a mismatch when the gap is meaningful.

On accuracy and repeatability, 3DLOOK has published a multi-vendor benchmark covering 14 companies, 8 countries, 27 subjects, and 1,152 data points across a BMI range of 19–41 and an age range of 18–55. The benchmark reports a 0.40 cm average measurement difference between back-to-back scans, against 0.57 cm for 3D hardware scanners and 0.94 cm for expert manual measurement in the same setup. The platform is ISO 8559-1:2017 compatible on 11 measurements, with documented 96–97% accuracy against manual reference and 95%+ repeatability across repeated scans. For BMI specifically, the BMI verification page documents 89% accuracy with 76% of users seeing less than 5% deviation.

On compliance posture, FitXpress is HIPAA-compliant with BAA support and follows GDPR principles. Photos move over TLS and sit on AWS S3 with SSE-S3 server-side encryption at rest. Photos are deleted immediately after processing or per the operator's configurable retention policy. No personal identifiers are processed. Role-based access controls govern internal data access.

Deployment is structured as a clear "we provide / you build" boundary, with both client-side and server-side options. Pattern B — server-side verification where body metrics are never exposed back to the patient — is the common deployment for online pharmacy and employer wellness use cases. A leading UK online pharmacy runs FitXpress as the BMI verification step inside its order flow; named customers across telehealth, fitness, and clinical wellness include Burlington Medical, Verv, Healthyr, and Zing Coach.

**Best fit:** Telehealth platforms running GLP-1 or weight-loss programs that need longitudinal body data and HIPAA-aligned audit records; online pharmacies running BMI verification with anti-manipulation requirements; insurance underwriting and employer wellness programs needing repeatable remote scans across distributed populations.

**Tradeoffs.** FitXpress is not optimized as a consumer fitness engagement layer; vendors with heavier 3D-visualization investment may produce a more polished avatar for B2C apps. It is also not a hardware option — for sub-centimeter geometric fidelity in a controlled environment, hardware vendors remain valid.

## Prism Labs — broad clinically-positioned platform with academic publications

Prism Labs (`prismlabs.tech`) positions itself as a mobile body data platform, with a tagline of "a revolution in personal health" and the promise of tracking "fat loss, muscle gain and body shape with clinically validated precision from a mobile phone camera." Their public target markets span Weight Loss and GLP-1 programs, Insurance and Population Health, Chronic Disease Management, Healthcare Providers, Pharma and Clinical Trials, Fitness and Wellness, Research, and Corporate Wellness.

**Strengths (publicly available).** Prism Labs publishes a body-composition output set that includes lean and fat mass, basal metabolic rate, body roundness index, metabolic age, visceral fat tracking, segmental composition, and a body-shape visualization called "Future Me." They publicly cite "7 publications in peer-reviewed journals" as the basis for their precision claims, and reference "DEXA precision using a mobile device." Their named reference customer list includes Welldoc, Noom, Weight Watchers, Tempo, FitnessAI, Glucare, and Siphox.

**Best fit.** Teams building broad clinically-positioned body composition workflows where peer-reviewed academic backing is the primary trust signal, and where the buyer has the in-house capacity to do their own compliance and integration verification.

**Tradeoffs (based on publicly available information).** Prism Labs' homepage does not document HIPAA, BAA, GDPR, or general security posture. It does not surface anti-manipulation features (liveness, clothing detection, weight cross-check), audit-trail design, or specific deployment patterns like server-side verification with no patient-facing metric exposure. The specific accuracy methodology behind "DEXA precision" is referenced but not documented inline on the homepage. None of this means those capabilities are absent — it means a buyer evaluating for telehealth verification or compliance use cases will need to drive that conversation in evaluation.

## Size Stream — best for clinical research and hybrid hardware deployments

Size Stream (`sizestream.com`) describes itself as delivering "AI-driven mobile body scanning" that produces accurate body data for businesses, with on-premise and at-home scanning options. The company runs three product lines — MeThreeSixty, Formcut, and Mobile Fit — and serves apparel brands, retailers, researchers, and health and wellness customers.

**Strengths (publicly available).** Size Stream publicly cites over 240 body measurements per scan, 290,000+ data points per avatar, and over 2,000,000 successful 3D body scans across its installed base. They explicitly support hybrid deployment, with hardware-based on-premise capture alongside iOS and Android mobile capture. Their volume metric and three-product structure suggest a mature, multi-channel platform.

**Best fit.** Clinical research programs and anthropometric studies that require calibrated geometric capture; hybrid in-clinic and at-home deployment programs where a single hardware step is acceptable; apparel and made-to-measure workflows needing dense measurement output.

**Tradeoffs (based on publicly available information).** Size Stream's homepage does not document HIPAA, BAA, or GDPR posture, nor anti-manipulation features. Hardware deployment, where applicable, does not scale across distributed telehealth populations the way smartphone-only capture does, and adds per-scan cost. The three-product structure means a buyer should confirm which product line maps to their specific workflow — health and wellness, made-to-measure apparel, or hybrid retail capture.

## Bodygram — best for fitness coaching and dietician workflows

Bodygram (`bodygram.com`) positions itself as "the most complete AI model for body insights," with capture happening from "a selfie." The publicly stated target customers are fitness trainers and gyms, health professionals, dieticians and nutritionists, with secondary mentions of retail, uniform manufacturers, and insurance.

**Strengths (publicly available).** Bodygram cites 35 body measurements, body composition (body fat, muscle mass), posture analysis, and personalized health insights with body-goal tracking. They publicly report comparative results of "1.35x increase in conversions" and "6x decrease in returns" in their case studies. Their named customer list (Unicharm, Tential, Bonmax, Adastria, Meiji Yasuda, Airweave) is concentrated in the Japanese fitness and apparel market.

**Best fit.** Fitness coaching, dietician, and personal-trainer workflows where the body scan supports a one-to-one coaching or sales conversation rather than a compliance verification step; B2C wellness apps with a coaching layer.

**Tradeoffs (based on publicly available information).** Bodygram's homepage does not document HIPAA, BAA, GDPR, or anti-manipulation features at the depth telehealth verification or insurance buyers require. The 35-measurement output is sufficient for fitness and apparel context but smaller than the 80+ count typical for full-coverage workflows. Buyers in regulated healthcare segments will need to drive deeper diligence outside the public site.

## Fit:match — apparel-focused, not designed for healthcare workflows

Fit:match (`fitmatch.com`) is included in this guide because it surfaces frequently in body-scanning category searches. Based on publicly available information, the product is oriented to apparel sizing recommendations and e-commerce fit personalization, not to clinical or compliance workflows. Detailed evaluation against the 10-criterion rubric in Section 2 was not possible from publicly accessible materials at the time of writing.

**Best fit (based on category positioning).** E-commerce apparel sizing and fit-personalization use cases where the buyer needs a size recommendation rather than verified body metrics.

**Not fit for.** Telehealth weight-loss programs, online pharmacy BMI verification, insurance underwriting, or wellness rewards verification. Buyers in those categories should evaluate vendors with documented healthcare compliance and anti-manipulation capabilities.

## Comparison at a glance

Cell values use the vendor's own public documentation. "Not publicly documented" means the criterion was not surfaced on the vendor's primary marketing pages at the time of writing; it is a statement about public visibility, not about the underlying capability.

| Criterion | 3DLOOK (FitXpress) | Prism Labs | Size Stream | Bodygram | Fit:match |
|-----------|-------------------|------------|-------------|----------|-----------|
| Capture method | 2 photos, live SDK capture | Mobile phone camera (method detail not specified on home page) | Smartphone (iOS/Android) + on-premise hardware option | Selfie / mobile | Not publicly accessible to this guide |
| Repeatability | 0.40 cm avg back-to-back variance; published multi-vendor benchmark (14 companies, 8 countries, 27 subjects, 1,152 data points) | Not publicly documented as a single repeatability metric | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |
| Measurement count | 80+ measurements | Body composition output set; total count not publicly stated | 240+ measurements, 290,000+ data points per avatar | 35 measurements | Not publicly accessible to this guide |
| HIPAA / BAA / GDPR | HIPAA-compliant, BAA support, GDPR-aligned (publicly stated) | Not publicly documented | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |
| Anti-manipulation defenses | Live SDK capture, real-time pose validation, clothing detection, Smart Scales mismatch flag | Not publicly documented | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |
| Deployment patterns | Client-side or server-side; "Pattern B" server-side option for compliance use cases | Not publicly documented | On-premise + at-home; three product lines | Not publicly documented | Not publicly accessible to this guide |
| Audit / exportable evidence | Audit-ready records; timestamped capture and processing logs | Not publicly documented | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |
| Integration model | SDK + API; explicit "we provide / you build" boundary | API and contact-driven (boundary detail not on home page) | Three products with separate landing pages | Contact-form integration entry point | Not publicly accessible to this guide |
| Time to result | Under 45 seconds | Not publicly documented | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |
| Pricing visibility | Public tiered pricing (Starter through Enterprise) | Pricing page exists; tiers not stated on home page | Not publicly documented | Not publicly documented | Not publicly accessible to this guide |

## How to choose: matchmaking guide

The right vendor is the one whose documented strengths match the actual buying context. Seven common patterns:

**If you run a telehealth platform with GLP-1 prescribing flows that need longitudinal body data and HIPAA-aligned audit records** — evaluate 3DLOOK (FitXpress). The combination of repeatability benchmark, BAA support, and Pattern B server-side deployment maps directly to this use case.

**If you run BMI verification for online pharmacies and need anti-manipulation defenses with exportable audit evidence** — evaluate 3DLOOK (FitXpress). Live SDK capture, clothing detection, and Smart Scales cross-check are the layers that address the photo-manipulation problem in this flow.

**If you run employer wellness rewards or insurance verification programs needing repeatable remote scans across distributed populations** — evaluate 3DLOOK (FitXpress). Back-to-back repeatability and audit posture matter most where rewards or risk classifications depend on documented body data.

**If you are building a broad clinical body-composition platform and peer-reviewed academic backing is the primary trust signal you need to satisfy stakeholders** — shortlist Prism Labs alongside 3DLOOK. The seven peer-reviewed publications they cite are a real differentiator for stakeholders who weight academic precedent heavily. Expect to drive a separate conversation on compliance documentation.

**If you run clinical research with hybrid hardware deployments and require hardware-grade geometric fidelity** — evaluate Size Stream. The on-premise plus mobile option fits this profile better than smartphone-only vendors.

**If you build fitness coaching or dietician workflows where the body scan supports a one-to-one coaching relationship** — evaluate Bodygram. The product positioning and customer mix point to that use case.

**If you primarily need apparel sizing recommendations, not health data** — Fit:match and similar apparel-focused vendors are the right category; the vendors above are over-spec for that workflow.

## Closing thoughts and next steps

There is no single best body scanning API. The right vendor depends on which use case is on the procurement document.

For healthcare workflows — telehealth verification, GLP-1 progress tracking, BMI verification, insurance underwriting, employer wellness rewards — three capabilities are non-negotiable. The vendor must publicly document HIPAA, BAA, and GDPR posture; repeatability must be tight enough to support longitudinal review; and there must be an anti-manipulation defense layer that does not depend on the patient choosing not to alter a camera-roll photo. Not every vendor in this guide documents all three.

See how **FitXpress** can support remote BMI verification, GLP-1 progress tracking, and audit-ready evidence collection inside your program. Get in touch with 3DLOOK at https://3dlook.ai/contact-us/ to walk through how the technology applies to your specific workflow.

## FAQ

**Is mobile body scanning HIPAA compliant?**

Compliance depends on the vendor, not on the capture method. A mobile body scanning API is HIPAA-aligned only if the vendor publicly documents HIPAA posture, will sign a Business Associate Agreement (BAA), and applies the required administrative, physical, and technical safeguards to electronic protected health information. Buyers should request the vendor's HIPAA documentation and confirm BAA willingness before any pilot. Of the vendors in this guide, 3DLOOK publicly documents HIPAA compliance with BAA support; the others did not surface comparable documentation on their public marketing pages at the time of writing.

**Can patients fake BMI photos to qualify for GLP-1 medication?**

With a free generative AI tool, a passive photo upload can be altered in seconds. That is why anti-manipulation defenses — live SDK capture instead of camera-roll upload, real-time pose validation, clothing detection, and AI-derived weight cross-check against the self-reported value — now matter as much as the underlying measurement accuracy.

**How is mobile body scanning different from a DEXA scan?**

DEXA is a hardware-based clinical method for body composition analysis, used inside clinics and labs. Mobile body scanning is a remote, AI-driven method that uses smartphone images. Some mobile vendors claim "DEXA precision" for body composition outputs; those claims should be evaluated against the vendor's published methodology, sample size, and population coverage rather than the marketing line alone. Mobile body scanning outputs are best positioned as supportive body data, not as a substitute for clinical assessment.

**What is the difference between in-session capture and camera-roll upload?**

In-session capture happens inside the verification flow, through the vendor's SDK, with real-time validation of pose and image quality. The patient cannot pre-select a photo from their device. Camera-roll upload pulls an image the patient already has — meaning the photo could be old, of someone else, of a screen showing another photo, or altered with a generative AI tool. For any verification use case tied to a regulated medication, eligibility decision, or audited reward program, only in-session capture is defensible.

**Can a mobile body scanning vendor sign a Business Associate Agreement?**

Some can, some cannot. BAA willingness should be confirmed at the evaluation stage, not at contracting. 3DLOOK publicly documents BAA support. Vendors that do not publicly state BAA readiness may still be able to provide one, but buyers should treat absence of that language on a public page as a signal to ask the question early.
