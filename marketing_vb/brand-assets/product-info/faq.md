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

**Q: Where is data stored?**
A: AWS S3, encrypted at rest with mandatory SSE-S3 (always on). TLS in transit.

**Q: How long do you keep photos?**
A: Either deleted immediately after processing, or within 30 days — your choice. When stored, photos are auto-blurred.

**Q: Are you HIPAA compliant?**
A: Yes, FitXpress is HIPAA-compliant. We follow GDPR principles for EU. We sign BAAs.

**Q: Do you train on our customers' photos?**
A: No. Photos sent through your tenant are deleted per retention policy and not used to train the model.

**Q: Are you a medical device?**
A: No — we don't provide medical advice, diagnosis, or treatment recommendations. Medical device certifications don't apply.

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
A: Yes — 1 month, 200 free requests, full SDK access.

**Q: Pricing tiers?**
A: For FitXpress: $1,000/mo for 500 requests up to $10,000/mo for 20,000 requests, scaling per-request rate from $2 to $0.50. Custom above 20K.

**Q: Mobile Tailor pricing?**
A: Custom enterprise contracts. Pricing reflects ARR ranges $50K-$300K depending on volume and use case complexity.

**Q: Do you charge for failed scans?**
A: Failed-due-to-pose scans are not billable. Successful scans are billed, regardless of whether end user weight matches Smart Scales output.

## Competitive

**Q: How do you compare to Prism Labs?**
A: They're focused on clinical body composition, especially for GLP-1 / population health. We have broader workflow integration depth, two-product portfolio (FX + MT), and stronger compliance posture for regulated workflows.

**Q: How do you compare to Bodygram?**
A: Bodygram is well-priced for SMB trainers / dieticians. We're enterprise-grade — HIPAA, audit logs, white-label depth, fraud detection (Smart Scales mismatch). Different fit.

**Q: What if Apple / Google launches body measurement primitives?**
A: We don't lead with "best model" — we lead with workflow integration, audit logs, longitudinal tracking, and compliance. Apple/Google won't ship those workflows. They might commoditize one input, but they won't replace the trusted layer above it.

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
