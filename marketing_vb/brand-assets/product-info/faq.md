# FAQ & Objection Handling (3DLOOK)

> Used by `message-sequencer` (when buyer raises objection in reply) and `response-classifier` (to draft responses).

## General

**Q: How accurate is your scanning?**
A: Internal validation against expert pattern-maker manual measurements shows approximately 96-97% accuracy across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. Detailed methodology, including sample size and measurement-level results, is available under NDA. (Per-measurement figures are in `proof-points.md` and are internal: the live framework article publishes none. Full published wording: `brand-assets/product-info/accuracy-formulations.md`)

**Q: How does it compare to InBody / DXA / scales?**
A: We're a different category. InBody and DXA (also written DEXA, which is how buyers usually search for it) are clinical-grade hardware (slow, expensive, in-clinic). Scales tell you weight only. We give 80+ measurements + body composition from any smartphone, in any location, in 45 seconds — at scale.

**Q: What happens if photo lighting is bad?**
A: Our model is minimally affected by lighting. Real-time pose validation guides the user. AI clothing detector flags issues. We've tested across hundreds of real-world environments.

**Q: Does it work with all body types?**
A: Yes — training data spans ages 16-78, weight 38-210 kg, height 150-220 cm, 48% male / 52% female. We continuously improve for unique body proportions.

## Privacy & Security

> Answers follow the live [Data, Privacy, Security & Regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) (2026-09-18). More answers: `compliance.md` §10.

**Q: Where is data stored?**
A: On AWS, primarily US-West-2 and partially US-East-1. Data in Amazon S3 is encrypted with SSE-S3 (S3-managed keys), on by default; TLS in transit.

**Q: How long do you keep photos?**
A: Deleted immediately after processing, or within 30 days under your policy. Retained photos are automatically blurred, and faces are obfuscated at capture. Measurements and 3D models are kept on an ongoing basis unless the agreement says otherwise.

**Q: Are you HIPAA compliant?**
A: HIPAA is a framework, not a certification. FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA. Under GDPR, in most enterprise deployments the customer is the data controller and 3DLOOK the data processor.

**Q: Are you SOC 2 certified?**
A: Not yet. 3DLOOK is working toward a SOC 2 Attestation Report and has completed an initial readiness assessment; security documentation is available under NDA.

**Q: Do you train on our customers' photos?**
A: No. 3DLOOK does not use production customer data to train its models.

**Q: Are you a medical device?**
A: An independent regulatory assessment concluded FitXpress does not meet the definition of a medical device under the UK MDR or EU MDR. It is not cleared, authorized or approved by the FDA, and 3DLOOK makes no representation on whether clearance is needed for a specific use case.

**Q: Can we use this for clinical decisions?**
A: We provide an information layer (body data). Your clinical workflows / providers make decisions. We're not a substitute for clinical assessment.

## Integration

**Q: How long does integration take?**
A: SDK integration is days, not months. API can be days. We provide React, iOS, and Android SDKs plus REST API.

**Q: Do we need special hardware?**
A: No — any smartphone camera. No additional hardware.

**Q: Can we white-label?**
A: Yes — onboarding, consent flow, progress UI, output UI are fully yours. The only protected layer is the photo capture step (pose/tilt validation in our SDK), which we lock to protect accuracy.

**Q: What if we want to not show body data to end users?**
A: Supported. Pattern B integration: scan happens, results consumed server-side only, end user sees "submitted" message. We have customers running this exact pattern (e.g., online pharmacy BMI verification).

**Q: Do you have an API rate limit?**
A: Yes, configurable per tier. We can also burst higher with notice.

## Pricing & Commercials

**Q: Is there a free trial?**
A: There is no self-serve trial. After a demo call, your team gets hands-on access to a demo page to run scans and review the outputs. Once the contract is signed, the first month is free for integration and testing. Billing then follows your plan.
*Path confirmed by Vadim 2026-10-14. Sales keeps the length and scan counts flexible per deal, so public copy names no figures (internal ones: `pricing.md`). Never call it a "free trial" in outbound.*

**Q: Pricing tiers?**
A: For FitXpress: $1,000/mo for 500 requests up to $10,000/mo for 20,000 requests, scaling per-request rate from $2 to $0.50. Custom above 20K.

**Q: Mobile Tailor pricing?**
A: Custom enterprise contracts. Pricing reflects ARR ranges $50K-$300K depending on volume and use case complexity.

**Q: Do you charge for failed scans?**
A: Failed-due-to-pose scans are not billable. Successful scans are billed, regardless of whether end user weight matches Smart Scales output.
*Sales answer only, not for website pages (Vadim 2026-09-30).*

## Competitive

*Competitor facts below were last verified 2026-10-15; full profiles in `competitors.md`. Never name competitors in cold outbound or articles.*

**Q: How do you compare to Prism Labs?**
A: Prism focuses on clinical body composition (GLP-1 programs, insurers, providers) and uses a 360° video scan. FitXpress works from two photos with Real-Time Pose Validation, flags self-reported weight mismatches for verification workflows (Smart Scales, beta), and sits next to Mobile Tailor for apparel and uniforms.
*(Internal: Prism claims SOC 2 Type II and we have no SOC 2 report yet, so don't claim a stronger compliance posture; answer security questions with `compliance.md` wording. Don't argue accuracy; use `accuracy-formulations.md`.)*

**Q: How do you compare to Size Stream?**
A: Size Stream combines a consumer app, booth scanners and, since July 2026, a health business unit. FitXpress is built to embed in the customer's own app through a white-label API and SDK, with verification features for regulated onboarding.
*(Internal: Size Stream announced SOC 2 Type 2 in March 2026; same caveat as Prism.)*

**Q: How do you compare to Fit:match?**
A: Fit:match is a multi-vertical platform whose 2026 focus is youth sports, with an iOS-only app. FitXpress runs on iOS and Android, embeds white-label, and adds verification features for health workflows.

**Q: How do you compare to Bodygram?**
A: Bodygram is well-priced for SMB trainers / dieticians. We're enterprise-grade — BAA-backed HIPAA support, audit logs, white-label depth, weight-mismatch detection (Smart Scales, beta). Different fit.

**Q: What if Apple / Google launches body measurement primitives?**
A: We don't lead with "best model" — we lead with workflow integration, audit logs, scan-to-scan comparison, and compliance. Apple/Google won't ship those workflows. They might commoditize one input, but they won't replace the trusted layer above it.

## Reliability & Operations

**Q: What's your SLA?**
A: Standard enterprise SLA — 99.5% uptime, support response within business hours. Custom SLAs available.

**Q: What if your model drifts?**
A: We have drift monitoring on the model and per-tenant performance dashboards. Customers see their accuracy trending over time.

**Q: Can we audit the model output?**
A: Yes — every scan returns a validation message bundle. For audit-heavy use cases (insurance, clinical trials), we provide structured, time-stamped audit logs.

## How agents should use FAQ

- `message-sequencer` reads the relevant FAQ before drafting step 2 / 3 of an outbound sequence — pre-empts objections
- `response-classifier` uses FAQ to pattern-match incoming questions → draft answer
- `seo-section-writer` can use FAQ as raw material for FAQ sections in articles (rephrased, never copy-pasted)
