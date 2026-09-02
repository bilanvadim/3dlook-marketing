---
product: fitxpress
type: use-case-page
vertical: insurance-underwriting
status: draft-awaiting-vadim
url: /for-insurance-underwriting/
parent: /
canonical: self
language: en
kit: references/kit-vertical-page.md
gi_status: waived-pending-vadim (zero insurance case studies)
date: 2026-08-31
---

<!-- Page copy. Slot order follows references/kit-vertical-page.md. Visual markers in square
     brackets have an entry in README.md. Builder annotations live in gate-reports.md, never here. -->

<!-- slot 1 -->
**Breadcrumbs**

`Home` → `FitXpress for Insurance Underwriting`

---

<!-- slot 2-3 · [HERO] -->
**Eyebrow:** FitXpress for insurance underwriting

# Remote build and BMI evidence for accelerated life insurance underwriting

**Sub-headline:**
A guided smartphone scan captures structured build and BMI data inside your application flow and
returns a timestamped record that supports underwriter review on the accelerated path.

**Spec row (oversized numerals):**

| 2 | under 45 sec | 80+ |
|---|---|---|
| guided photos, front and side | from capture to structured results | body measurements returned per scan |

**Primary action:** Book a demo
**Inline secondary:** See how the scan fits the workflow (anchor to the journey block)

**Trust line:** Built for life and group carriers, reinsurers and digital distribution partners running
accelerated underwriting programs.

---

<!-- slot 5 · [CONTEXT] -->
## The evidence gap accelerated underwriting created

Accelerated underwriting took the paramedical exam out of a large share of applications. It did not take
away the need for reliable build data.

Munich Re's 2025 accelerated underwriting analysis reports that changes in build and weight were the top
reason for variance in risk-class assessment, with build and BMI misrepresentation the second-largest
driver of misclassification after smoking non-disclosure. Researchers at the Centers for Disease Control
and Prevention (CDC) found that self-reported survey data underestimated the prevalence of severe obesity
by 40%. The build field is at once the most consequential body signal in the file and the one most exposed
to inconsistent reporting.

Each of the usual ways to close that gap costs something.

**Four cards:**

| Method | What it gives | What it costs |
|---|---|---|
| Self-reported height and weight | Collected at application in seconds | Unverified, weak for risk classification and weak as documentation |
| Paramedical exam | Established, examiner-verified | Scheduling, travel and examiner availability across a distributed applicant population |
| Attending physician statement (APS) | Physician-verified detail | Frequently weeks of wait, often arriving after the underwriter has opened the review |
| Consumer body-scan app | Convenient capture | No governance controls, no retention policy the carrier can set, no integration boundary |

**Verdict line:** Each one either slows the path the program was built to accelerate, or leaves the build
field unverified.

---

<!-- slot 6 · [CONTEXT] -->
## What an underwriting team receives

| | |
|---|---|
| **Input** | Two guided photos, front and side, alongside the disclosed height, weight, age and gender your intake already collects |
| **Output** | 80+ body measurements, BMI, body composition including body fat percentage, lean mass, fat mass and basal metabolic rate (BMR), a 3D body model, and a comparison signal between disclosed and captured values |
| **Speed** | Structured results in under 45 seconds, with no manual review step |
| **Record** | Timestamped and machine-readable, filed per case |
| **Deployment** | Application programming interface (API) and software development kit (SDK), white-label, photos deleted after processing or within 30 days per the policy you set |

**Boundary.** FitXpress is not a medical device. It supplies structured body data as supporting evidence,
and risk classification, pricing and the final decision stay inside your underwriting guidelines.

---

<!-- slot 7 · [WORKFLOW] -->
## Where underwriting changes the workflow

Most of the capture flow is identical in every vertical. Three things run differently here.

**1. Disclosure comparison is its own step.** The applicant discloses height and weight at intake. After
capture, disclosed values and measured values are compared, and a material gap is returned as a flag on
the case.

**2. A flagged scan goes to an underwriter.** Mismatches and quality failures route into the review queue
the carrier already operates, with the reason attached, instead of landing in a generic support ticket.

**3. The record is filed, and often never displayed.** Many regulated deployments run the internal-only
pattern: the applicant sees confirmation that the photos were submitted, and the body data goes to the
underwriting platform and the case file without being shown back.

That third one is a recommendation, and 3DLOOK will argue for it. Showing an applicant their body
composition partway through a life application starts a conversation the underwriting file has no use
for, and it turns an evidence step into a health product. Keep the outputs on the underwriting side.

Re-checks at policy update follow the same capture protocol, which keeps build data consistent across
events instead of comparing one method against another.

---

<!-- slot 9 · [ACCURACY] -->
## Accuracy, scoped to the decision it supports

The diligence question worth asking is: accurate enough for which decision? Four conditions decide the
answer, and a figure quoted without them means very little.

1. **Reference method.** Internal validation compares scan output against expert manual measurement. Read
   against a clinical reference method, the figures would be different.
2. **Measurement protocol.** Guided capture through the SDK, with real-time pose and framing validation.
   Quality falls away when capture is unguided or clothing is oversized, which is why the capture layer is
   the one surface that is never white-labelled.
3. **Population covered.** The model's demographic coverage spans ages 16 to 78, heights 150 to 220 cm
   and weights 38 to 210 kg, across the US and Europe, at a 48% male and 52% female distribution. A body
   outside that range is outside what the figures describe.
4. **Intended workflow.** Supporting evidence inside underwriter review.

| Measure | Figure | Against what |
|---|---|---|
| Accuracy against expert manual measurement | 96-97% | Internal validation, typical absolute error 1.5 to 2.0 cm |
| Scan-to-scan repeatability | `< 1 cm` | Same internal validation, back-to-back capture |
| Weight estimation | ±3.5% average error | Real-world conditions. A software estimate, and not a scale reading |

Detailed methodology is available under a non-disclosure agreement (NDA). These figures come from internal
validation. Peer review and third-party clinical certification are not part of that record, which is worth
saying before a diligence reviewer asks.

For a carrier that refreshes build data at policy update, repeatability carries more weight than a single
accuracy number. The change between two scans has to be real movement instead of measurement noise.

---

<!-- slot 8 · [COMPLIANCE] -->
## Compliance and data governance

For a carrier this section decides the deal well before the demo does.

**Data handling.** Photos are encrypted in transit with Transport Layer Security (TLS) and at rest in
Amazon S3 with server-side encryption using S3-managed keys (SSE-S3), which cannot be switched off. Photos
are deleted immediately after processing, or within 30 days, depending on the policy you set. Stored
photos are automatically blurred, and face obfuscation is applied at capture.

**What never enters the pipeline.** No names and no personal identifiers pass through the scan. Images are
excluded from model training and are not shared with third parties.

**Health-data frameworks.** FitXpress maintains Health Insurance Portability and Accountability Act
(HIPAA) compliance and follows General Data Protection Regulation (GDPR) principles for European
processing. Whether HIPAA obligations reach a given carrier depends on the lines it writes and how it
handles health information; 3DLOOK signs a Business Associate Agreement (BAA) where the customer is a
covered entity. Confirm the position for your own entity with privacy counsel.

**How the data may be classified.** Depending on jurisdiction, processing purpose and how the flow is
designed, photos and body-derived outputs may be treated as personal data, and in some jurisdictions as
health data or as biometric data. Consent language, data minimisation and retention design stay a carrier decision, and
3DLOOK supplies the processing and security documentation that review needs.

**What the controls do not cover.** Encryption, deletion and access controls reduce exposure. They do not
remove the need for capture instructions, retake logic, deployment-specific thresholds, or the consent
wording an applicant actually reads.

**Governance posture.** The National Association of Insurance Commissioners (NAIC) expects accelerated
underwriting models to be fair, transparent, grounded in sound actuarial principles and monitored for
unfair discrimination. FitXpress supports underwriter review; it is not a standalone decisioning engine.

Logging covers scan status, timestamps, quality flags and failure reasons per case. Applicants exercise
privacy rights through privacy@3dlook.me.

---

<!-- slot 12 · [INTEGRATION] -->
## Integration and the boundary you control

Guided capture runs inside your application flow through the Web SDK. Your backend orchestrates the API
call and receives a structured payload. Where the results appear, and whether the applicant ever sees
them, is your design decision.

**3DLOOK provides**

- Guided capture with real-time pose, framing and clothing validation
- Photo processing and body modelling
- The structured results payload, including measurements, BMI and the disclosure comparison signal
- Integration documentation and implementation support

**You build**

- The application journey and the intake fields feeding the scan
- Consent language and privacy messaging
- Where evidence lands in the case-management system or the policy administration system (PAS)
- Underwriting rules, escalation paths and case routing

The capture layer is the one surface that stays standardized. Pose and tilt validation live there, and
they are the single largest factor in measurement quality, which is why customers who build their own
camera flow see measurably worse results.

**Formats and support.** Structured payload over the API, native iOS and Android camera SDKs, a React SDK
for web, 3D model export, and bulk export from the Admin Panel for audit and cohort review. Integration is
measured in days.

**Admin Panel (optional).** Every scan under your API key in one filterable table, with status, quality
flags and failure reasons, sortable and exportable, fully anonymized. It complements the integration and
does not replace it.

---

<!-- slot 7b · [WORKFLOW] -->
## Where the scan sits in the underwriting journey

| Stage | When the scan runs | What reaches the underwriter |
|---|---|---|
| Pre-screening | At intake, alongside disclosed height and weight | Structured build data before full review opens |
| Evidence collection | As a digital step inside the application flow | A case file that is not waiting on scheduling |
| Applicant verification | After processing, disclosed against captured | Flagged mismatches, with the gap quantified |
| Underwriter review | Alongside the rest of the case evidence | Measurements in place of a subjective build description |
| Program insight | Post-decision, across the book | Patterns in evidence quality and triage effectiveness |

Carriers keep full control of decisioning at every stage. The scan changes what is in the file, and it does
not change who decides.

---

<!-- slot 10 · [CASE CARD] -->
## Where FitXpress runs today

In life underwriting FitXpress is at pilot stage. The closest production deployments sit in adjacent
regulated remote workflows: BMI verification inside an online-pharmacy order flow in the UK, where
eligibility is checked server-side and body metrics are never displayed to the customer, and longitudinal
body-composition tracking inside weight-management programs.

3DLOOK has been building body-measurement models since 2016 and processed 112,100 scans across 67 active
customers in 2025.

---

<!-- slot 9b · [ACCURACY] -->
## Compare by role

| | Self-reported build | Paramedical exam | FitXpress |
|---|---|---|---|
| Where it happens | The application form | A scheduled visit | Remote, inside your flow |
| Time to evidence | Immediate | Days to weeks | Under 45 seconds after capture |
| Consistency | Varies with the applicant | Varies with the examiner | Guided capture, `< 1 cm` scan-to-scan |
| Quality controls | None | Examiner judgment | Live capture, pose validation, clothing detection |
| Record left behind | A self-declared field | A report into the file | A timestamped structured record |
| Best fit | Low face amounts where build is not material | Complex and high face amount cases needing a full medical workup | Standard-risk cases already on the accelerated path |

A paramedical exam is the right instrument where the underwriting guideline calls for one. The scan covers
the build field on cases that guidelines have already routed away from a full workup.

---

<!-- slot 14 -->
## What it costs

FitXpress starts at $1,000 per month for up to 500 scans, with a Pro tier at $1,500 for up to 1,000 scans
and custom pricing above that. A one-month trial includes 200 requests and full SDK access, which is
usually enough to run an internal evaluation against a sample of decided cases. Full tiers are on the
[pricing page](/pricing/).

---

<!-- slot 13 · FAQPage schema -->
## Questions underwriting teams ask

### Can FitXpress replace medical underwriting?
No. It supports evidence collection and review. Required exams, lab work and underwriter judgment stay in
place, and the decision stays with the carrier's guidelines.

### Is this an automated underwriting or fraud detection engine?
No. FitXpress returns structured body data and a comparison signal between disclosed and captured values.
Routing, risk classification and any determination about misrepresentation stay with the carrier's rules
and its reviewers.

### How does the disclosed-versus-captured comparison work?
Disclosed height and weight enter through your intake fields. After the scan, captured measurements and
the estimated weight are compared against those values, and a material gap is returned as a flag on the
case for underwriter attention.

### Does HIPAA apply to a life carrier using this?
Whether the rule reaches a given carrier depends on the lines it writes and how it handles health
information. FitXpress maintains HIPAA compliance and signs a Business Associate Agreement where the
customer is a covered entity. Confirm the position for your entity with privacy counsel.

### Is body data biometric data?
Depending on jurisdiction, processing purpose and implementation design, photos and body-derived outputs
may be treated as personal data, and in some jurisdictions as health data or as biometric data. Consent,
minimisation and retention design belong with the carrier, and 3DLOOK supplies the processing and
security documentation for that review.

### How are photos handled, and how long are they kept?
Photos flow through your backend to the API and are deleted immediately after processing, or within 30
days, depending on the policy you choose. Stored photos are automatically blurred. Encryption is TLS in
transit and SSE-S3 at rest. Images are excluded from model training and are not shared with third parties.

### Can outputs stay internal to the underwriting team?
Yes. In the internal-only pattern the applicant sees confirmation that photos were submitted, and
measurements are consumed by your systems without being displayed back.

### What happens when a scan fails?
Real-time pose and framing feedback catches most problems before submission, and the clothing detector
prompts a retake where what the applicant is wearing would affect quality. A scan that fails on pose is
not billable, and the failure reason is returned with the record.

### What is behind the accuracy figures?
Internal validation against expert manual measurement, with demographic coverage spanning ages 16 to 78,
heights 150 to 220 cm and weights 38 to 210 kg across the US and Europe. Typical absolute error is 1.5 to
2.0 cm, and scan-to-scan repeatability is under 1 cm. Detailed methodology is available under a non-disclosure
agreement. Peer review and clinical certification are not part of that record.

### How does it compare with a clinical body-composition assessment?
Dual-energy X-ray absorptiometry (DEXA) and bioelectrical impedance analysis (BIA) measure against
different references under clinic conditions. FitXpress captures external body measurements remotely and
repeatably. Where a guideline or protocol calls for a clinical reference method, that method is the one to
use.

### Which systems does it plug into?
The scan sits inside your e-application or applicant portal, and results return over the API into the
underwriting workbench, the case-management system or the PAS. Bulk export from the Admin Panel covers
audit and cohort review.

### How long does integration take?
Integration is measured in days. The recommended pattern relays photos through your backend, which keeps
credentials, orchestration and data control inside your environment.

### What does a pilot look like?
Most teams start with the demo link, review sample outputs against a set of already-decided cases, then
scope the integration. The trial covers 200 requests over one month with full SDK access, which is enough
to test evidence quality on a real applicant sample before contracting.

---

<!-- slot 15 · [HERO] navy band -->
## See the evidence a scan puts in the case file

Book a demo to walk the capture flow, review a sample evidence payload, and map the integration
against your accelerated underwriting program.

**Primary action:** Book a demo

**Form fields:** work email, company, role, market, one free-text line. Visible consent checkbox,
confirmation state on submit.

---

<!-- slot 16 -->
## Keep reading

- [AI in insurance underwriting: mobile 3D body scanning for remote evidence collection](/content-hub/mobile-body-scanning-insurance-underwriting/)
- [Body scanning accuracy: a framework for enterprise decisions](/content-hub/mobile-body-scanning-accuracy/)
- [The next big leap in health](/ebook-the-next-big-leap-in-health/)

**Sibling verticals**

- [Weight and BMI verification](/for-bmi-verification/)
- [Telehealth and digital health programs](/structured-body-data-for-telehealth-digital-health-programs/)

**Up:** [FitXpress](/) · **Conversion:** [Pricing](/pricing/) · [Case studies](/case-studies/)
