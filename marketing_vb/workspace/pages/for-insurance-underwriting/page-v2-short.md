---
product: fitxpress
type: use-case-page
vertical: insurance-underwriting
status: draft-v2-short (Vadim's decisions of 2026-09-30 applied)
url: /fitxpress/for-insurance-underwriting/
canonical: self
language: en
replaces: page.md (2026-08-31, ~2,700 words, 13 H2, 13 FAQ)
built_from: Nika's draft (Drive, 2026-09-30), Asselya's draft (fitxpress-insurance-underwriting.hr-d114.chatgpt.site), page.md v1
keywords: workspace/research/seo-fitxpress-2026-09/2026-09-29-landing-keywords.md §5
facts: brand-assets/product-info/compliance.md, proof-points.md, accuracy-formulations.md, live /pricing/ (2026-09-30)
review: review-2026-09-30-nika-asselya.md
date: 2026-09-30
---

<!-- Short commercial version. Target: ~1,000 words of visible copy, 8 H2.
     Anything that needs more than a paragraph of explanation lives in an article, and the page
     gives it one line and a link. Builder notes stay in the review file, never here. -->

## Yoast

| Field | Value | Length |
|---|---|---|
| SEO title | `Accelerated Underwriting: Build & BMI Evidence \| FitXpress` | 58 / 60 |
| Meta description | `Add remote build and BMI evidence to life insurance accelerated underwriting: two guided photos, predicted weight and a disclosure flag in under 45 seconds.` | 155 / 155 |
| Focus keyphrase | `accelerated underwriting` | |
| Breadcrumb | Home → FitXpress → FitXpress for Insurance Underwriting | |

---

<!-- 1 · HERO -->
**Eyebrow:** FitXpress for insurance underwriting

# Remote build and BMI evidence for accelerated underwriting

Accelerated underwriting took the paramedical exam out of most life applications, and the build field
now rests on what the applicant types. FitXpress adds a second source inside your e-application. Two
guided smartphone photos, and in under 45 seconds your underwriters get predicted weight, scan-derived
BMI and a flag when the disclosed weight falls outside your threshold.

**Primary:** [Book a demo](#demo) · **Secondary:** [See what lands in the case file](#record)

**Under the button:** A walkthrough on a phone, with a sample underwriting record.

**Proof strip:**

| 2 photos | Under 45 sec | Your threshold | No integration fee |
|---|---|---|---|
| front and side, on the applicant's own phone | from the photos to structured results | you decide which gap goes to review | plans from $1,000 a month |

---

<!-- 2 · PROBLEM -->
## Accelerated underwriting got faster. Build evidence got weaker.

The accelerated path removed the one step where someone measured the applicant. The build field kept
its weight in the risk class.

| 59% | #1 | 9 vs 27 days |
|---|---|---|
| of individual life applications qualify for an accelerated path (Gen Re, 2025 Next-Gen Underwriting Survey) | Build and BMI is the leading misclassification reason in accelerated underwriting monitoring studies, ahead of tobacco (Munich Re) | average time to decision, accelerated vs traditional underwriting (LIMRA) |

The speed is worth keeping. The build field is where it leaks.

→ Underwriting stages, fraud-prevention support and compliance, in depth:
[AI in insurance underwriting](/content-hub/mobile-body-scanning-insurance-underwriting/)

---

<!-- 3 · HOW IT WORKS -->
## How it works: a two-photo check inside your application

No new app for the applicant and no new queue for your team. FitXpress runs inside your e-application
through a web or mobile SDK.

1. **The applicant discloses and scans.** Height, weight, age and gender come through your existing
   fields. Two guided photos follow, with live pose, framing and clothing checks.
2. **FitXpress compares.** Smart Scales predicts weight from the scan. Disclosed and scan-derived BMI use
   the same supplied height. A gap above your threshold comes back flagged.
3. **Your rules route the case.** Clean cases stay on the accelerated path. Flagged cases go to the review
   queue you already run.

**Recommended setup:** the applicant sees "Scan submitted", and the results go only to your systems.

→ The same weight check in other regulated flows: [remote BMI verification](/for-bmi-verification/)

---

<!-- 4 · RECORD · id="record" -->
## What lands in the case file

One timestamped, machine-readable record per applicant. It returns over the API to your underwriting
workbench, case-management system or policy administration system.

| Field | What your underwriter gets |
|---|---|
| Predicted weight (Smart Scales) | A software estimate for comparison with the disclosed weight, ±3.5% average error. Not a scale reading |
| BMI comparison | Disclosed BMI next to scan-derived BMI, both from the same supplied height |
| Disclosure flag | Raised when the gap crosses the threshold you set |
| Build measurements | The circumferences your guideline references. 80+ body measurements, body composition estimates and a 3D model are available if you need them |
| Quality and status | Pose, framing and clothing results, the reason for any failed capture, and a timestamp |

[Get a sample payload →](#demo)

---

<!-- 5 · COMPARE -->
## FitXpress vs self-report vs the paramedical exam

| | FitXpress | Self-reported build | Paramedical exam |
|---|---|---|---|
| Where it happens | Remote, inside your application | Application form | Scheduled visit |
| Time to evidence | Under 45 seconds from the photos | Immediate | Days to weeks |
| Disclosure check | Disclosed vs predicted weight, gap quantified | None | Measured on site |
| Record | Timestamped structured record | A self-declared field | Examiner report |
| Best for | Standard-risk cases on the accelerated path | Low face amounts where build isn't material | Complex and high face amount cases |

Keep the paramedical exam where your guideline calls for one. FitXpress covers the build field on the
cases your guidelines already route away from it.

---

<!-- 6 · PROOF + TRUST -->
## Accuracy and data handling on one screen

| 96-97% | < 1 cm | ±3.5% |
|---|---|---|
| accuracy against expert manual measurement, typical absolute error 1.5-2.0 cm | typical scan-to-scan difference for most measurements | average error of Smart Scales predicted weight |

These figures come from internal validation. Peer review and third-party clinical certification are not
part of that record, and the full methodology is available under NDA.
→ [Body scanning accuracy: an enterprise framework](/content-hub/mobile-body-scanning-accuracy/)

- **Photos** are deleted after processing, or within 30 days under your policy. Retained photos are
  blurred, and faces are obfuscated at capture.
- **Scan records** are tied to anonymized, randomly generated IDs.
- **HIPAA and GDPR.** FitXpress can support HIPAA-governed deployments under an executed BAA. In most
  enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor
  under GDPR.
- **Model training.** 3DLOOK does not use production customer data to train its models without your
  explicit, documented authorization.
- **Decisions.** FitXpress is not a medical device. It adds evidence to the file, and eligibility, risk
  class and pricing stay with your underwriters.

→ Storage, retention, SOC 2 and FDA:
[Data, Privacy, Security & Regulatory FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/)

---

<!-- 7 · PILOT + PRICE -->
## Prove it before it touches a live decision

FitXpress already runs BMI verification inside a UK online-pharmacy order flow. There, eligibility is
checked server-side and customers never see their metrics. Your underwriting pilot runs on the same
production infrastructure that serves 3DLOOK's 100+ clients.

1. **Walkthrough.** The applicant flow on a phone, a sample payload and your integration pattern.
2. **Shadow evaluation.** A defined cohort scans while outputs stay out of underwriting decisions.
3. **Evidence comparison.** Scan results against independently collected build evidence, on success
   criteria agreed before day one.

You finish with numbers: completion and retake rates, agreement with your reference evidence, how many
cases each candidate threshold would flag, and the effect on review volume.

**Pricing.** Plans start at $1,000 a month for up to 500 scans, with no integration fee.
[See pricing](/pricing/)

[Book a demo](#demo)

---

<!-- 8 · FAQ · FAQPage schema, answers byte-identical in JSON-LD -->
## Questions underwriting teams ask

### What is accelerated underwriting?
Accelerated underwriting allows a life insurer to issue a policy without a paramedical exam or lab work
for applicants who qualify. Third-party data and the application answers take the place of fluids and an
exam. It is faster, but height and weight usually rest on self-report.

### Does FitXpress replace the paramedical exam?
No. It adds build evidence to cases your guidelines already send down the accelerated path. Where a
guideline calls for an exam, lab work or an attending physician statement, those stay in place.

### How does remote height and weight verification work for life insurance?
Height comes from the application. Smart Scales predicts weight from two guided photos, and both BMIs are
calculated from the same supplied height. Your threshold checks the gap between disclosed and predicted
weight.

### Can results stay internal to the carrier?
Yes, and we recommend it. The applicant sees that the photos were submitted, and the measurements go only
to your systems.

### What happens when a scan fails?
Live pose and framing feedback catches most problems before submission. The clothing detector asks for a
retake when clothing affects quality, and the reason for any failed capture comes back with the record.

### Does FitXpress support HIPAA-governed deployments?
Yes. 3DLOOK can act as a business associate under an executed BAA for qualifying enterprise deployments.
The full answer is in the
[Data, Privacy, Security & Regulatory FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

---

<!-- 9 · FORM · id="demo" · shared HubSpot form FX | LP | Demo, GTM fx_vertical = insurance -->
## See what a scan adds to your case file

We walk the applicant flow on a phone, show a sample underwriting record, and scope a shadow evaluation
against your current build evidence.

**Form:** shared `FX | LP | Demo`, including the optional "Expected monthly scan volume" field added
2026-09-30. No page-specific fields.

Not ready for a call? [Start with the underwriting analysis](/content-hub/mobile-body-scanning-insurance-underwriting/).

---

<!-- 10 · KEEP READING -->
## Keep reading

- [AI in insurance underwriting: mobile 3D body scanning for remote evidence collection](/content-hub/mobile-body-scanning-insurance-underwriting/)
- [Wellness rewards verification for employers and insurers](/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/)

**Up:** [FitXpress](/fitxpress/) · **Feature:** [Weight and BMI verification](/for-bmi-verification/) ·
**Conversion:** [Pricing](/pricing/)
