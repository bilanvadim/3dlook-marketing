---
product: fitxpress
type: product-page
vertical: all
status: draft-for-judge
url: /fitxpress/
parent: /
canonical: self
language: en
kit: references/kit-vertical-page.md (adapted; no product-page Kit exists)
date: 2026-09-27
---

<!-- Page copy. Visual markers in square brackets are listed in README.md. Builder notes live in
     gate-reports.md, never here. -->

<!-- slot 1 · breadcrumbs -->
**Breadcrumbs:** `Home` → `FitXpress`

---

<!-- slot 2-3 · [HERO] -->
<!-- builder: eyebrow --> FitXpress by 3DLOOK

# FitXpress AI body scanner: body measurements your health program can act on

FitXpress is body scanning software for digital health, insurance, wellness and fitness programs. A person takes two guided photos with a smartphone. From those photos, the AI body scanner builds a 3D model and returns 80+ body measurements with body composition estimates, through an application programming interface (API) and software development kits (SDKs). The whole process takes under 45 seconds from the photos to structured results.

<!-- builder: spec row, oversized numerals -->

| 2 | 80+ |
|---|---|
| guided photos, front and side | body measurements per scan |

<!-- builder: primary button --> **Book a demo**
<!-- builder: text link to #outputs --> [See what a scan returns](#outputs)

<!-- builder: [LOGO STRIP], grayscale logos, alt text in wordpress-notes §5 -->
Used by health programs including UK Meds, Yazen and Healthyr.

---

<!-- slot 5 · the problem this product removes -->
## Why programs stop trusting self-reported body data

Remote programs collect weight and BMI through forms. Self-reported numbers are often out of date, and some are misreported on purpose. In-clinic measurement is more reliable, but a program that checks in every few weeks cannot send people to a clinic each time.

The fix is a standardized capture step inside the program's own app. Every scan produces the same structured record, with a timestamp and a random scan ID. Clinicians, underwriters and coaches then work from one record format, whatever phone the person used.

---

<!-- slot 6 · [OUTPUTS] what the product returns -->
<a id="outputs"></a>
## What FitXpress returns from one scan

Each successful scan returns one structured payload. The categories matter, because they carry different levels of certainty.

| Output | What it is | Typical use |
|---|---|---|
| 80+ body measurements | Circumferences, lengths and widths, such as waist, hip, chest and inseam | Intake records, measurement trends, sizing |
| Calculated metrics | BMI and basal metabolic rate (BMR), calculated from the scan and the height entered | Eligibility documentation, program intake |
| Body composition estimates | Body fat %, lean mass and fat mass | Progress review between clinical assessments |
| 3D model | A 3D body model generated from the two photos | Visual progress, member engagement |
| Predicted weight | A weight estimate from the scan (Smart Scales, in beta) | Can flag a mismatch with the weight a person reports |
| Scan-to-scan comparison | A side-by-side comparison of two scans the program selects | Progress review, check-ins |
| Capture-quality flags | Pose and clothing signals from the capture step | Retake prompts, review queues |

Body composition values are estimates. They come from the measurements, the height entered and an optional weight. 3DLOOK does not track individuals or decide whether two scans belong to the same person. The program chooses which scans to compare.

---

<!-- slot 7 · [WORKFLOW] how it works -->
## How a scan works

1. **The person enters basic details.** Gender and height are required. Weight is optional and is used for body composition outputs.
2. **The phone guides the capture.** Real-Time Pose Validation (RTPV) checks position and framing before each photo. A separate check guides the phone angle.
3. **Clothing is checked.** The Clothing Detector identifies clothing conditions that may interfere with capture and can prompt corrective action.
4. **Two photos are taken.** One from the front, one from the side, on a standard smartphone camera. No scanner or wearable is needed.
5. **Faces are obfuscated at capture.** This applies whatever photo retention policy the program chooses.
6. **Results go to the program's backend** as one structured payload.

Guided capture helps reduce retakes and inconsistent inputs. Programs still need clear capture instructions in their own onboarding.

---

<!-- slot 16 (moved up) · [INDUSTRIES] link down to every vertical -->
## Where FitXpress is used

Eight sectors run the same scan. What differs is the problem they start from, and what happens to the record afterwards.

**[Telehealth and glucagon-like peptide-1 (GLP-1) weight-loss programs](/structured-body-data-for-telehealth-digital-health-programs/)**
Programs rely on self-reported weight and inconsistent check-ins, and members drop off when progress is not visible. Scans add body composition and 3D comparison between clinical visits.

**[Online pharmacies and BMI verification](/for-bmi-verification/)**
Patients misreport BMI to qualify, and manual photo review is inconsistent. A scan inside the order flow documents BMI before a prescriber reviews the request.

**[Connected and digital fitness](/fitxpress/for-connected-and-digital-fitness/)**
Engagement plateaus when progress means only weight and workout count. Scans add visible progress and body data for personalized plans.

**[Life insurance underwriting](/content-hub/mobile-body-scanning-insurance-underwriting/)**
Underwriting still depends on self-reported body metrics and manual verification, driving delays and weak documentation. Timestamped build and BMI records support underwriter review.

**[Employer wellness and health plans](/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/)**
Self-reported progress leads to low trust and disputes over incentives. Remote check-ins give HR and benefits teams one consistent record, without a clinic visit.

**[Occupational health screening](/content-hub/occupational-health-screening-software/)**
High-volume screening runs into clinic bottlenecks, rescreens and uneven documentation across sites. A scan before the appointment standardizes intake.

**[Clinical trials](/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/)**
Manual measurements vary by site and staff, and measurement-only visits add dropout risk. Scans keep anthropometric capture consistent across sites and remote visits.

**[Bariatric and metabolic clinics](/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/)**
Eligibility is confirmed too late, and consult slots are wasted. Clinics can see structured BMI and body composition data before the first consult.

Apparel and uniform teams use [Mobile Tailor](/mobile-tailor/), the 3DLOOK product for fit and sizing.

---

<!-- slot 12 · [INTEGRATION] -->
## How FitXpress fits into your product

Delivery is a body scanning API with web and mobile SDKs, including supported iOS and Android integrations. The SDK runs the guided capture inside your app or website. Your backend sends the photos to the API and receives structured results.

Two integration patterns cover most deployments:

- **Results in your interface.** Your app shows the 3D model, measurements or progress view in your own design.
- **Results server-side only.** The person sees a confirmation screen. The body data goes straight to your review or eligibility workflow.

Onboarding, consent wording, loading screens, error messages and the results view are yours to design. The photo capture layer stays fixed, because pose and tilt checks run there.

We recommend the SDK for capture even when results never reach the end user. In our experience, capture quality is the largest single factor in measurement quality that a program controls.

Teams that want a view without building one can use the FitXpress Admin Panel, an optional, complementary interface for monitoring and exporting results. It does not replace API or SDK integration.

API and SDK access is set up after a demo call or under a non-disclosure agreement. Engineering teams can review the [FitXpress API documentation](https://docs.fitxpress.3dlook.me) before the call.

---

<!-- invented slot · [PAYLOAD] results and destinations -->
## What you get back and where it goes

One structured payload per successful scan reaches your backend. It groups the body measurements, calculated metrics and body composition estimates, with a link to the 3D model and the capture-quality flags. Each scan record carries a random scan ID, and processing logs carry timestamps. The 3D model is delivered in a standard 3D file format. Exact field names are in the [API documentation](https://docs.fitxpress.3dlook.me).

Where the results go next depends on the program. These are destinations programs choose, in their own systems:

| Program | Where results typically go |
|---|---|
| Telehealth and GLP-1 programs | The patient app and the care team's patient assessment dashboard |
| Online pharmacies | The prescriber review step, with the record kept in the compliance audit trail |
| Life insurers | The underwriting file, as a time-stamped record and structured export |
| Employer wellness and health plans | The check-in record and the audit trail for HR and benefits teams |
| Occupational health providers | The screening record, in the same format across sites |
| Clinical trial sponsors | Study documentation and site monitoring records |
| Bariatric clinics | The pre-auth packet and the patient's intake documentation |
| Fitness platforms | The member's progress view inside the app |

---

<!-- slot 9 · [ACCURACY] scoped -->
## Accurate enough for which decision?

A single accuracy percentage tells a procurement team very little. What counts as adequate performance depends on how the measurements will be used. Four conditions give a figure meaning: the reference method, the measurement protocol, the population tested and the intended workflow.

The model behind FitXpress was trained on 9+ years of data: 150,000+ photographs, 30,000+ 3D scans and 430,000+ individual measurements. Training data describes what the model has seen. Performance is a separate question, and two internal studies answer it.

Repeatability testing used a real-world customer dataset with repeated scans of each participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. Repeatability is especially important for programs that compare scans over time.

A separate internal study compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. The full framework is in [Body Scanning Accuracy: A Framework for Enterprise Decisions](/content-hub/mobile-body-scanning-accuracy/).

These findings establish performance relative to the selected reference. The study dataset covers ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, and participants across the US and Europe. Performance outside this scope has not been characterized.

FitXpress was not specifically trained on data representing people with physical disabilities. Its measurement performance has not been established for this population.

FitXpress is not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis (BIA) or a calibrated scale when the workflow, protocol or regulatory standard requires those methods.

---

<!-- slot 8 · [COMPLIANCE] trust -->
## Data privacy, security and regulatory status

Security and legal reviews usually start with hosting, photo retention and contract roles. Encryption, output retention, System and Organization Controls 2 (SOC 2) status, model training and U.S. Food and Drug Administration (FDA) questions are answered in the [FitXpress data privacy, security and regulatory FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

| Topic | Status |
|---|---|
| Health Insurance Portability and Accountability Act (HIPAA) | FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed business associate agreement (BAA), where applicable. |
| General Data Protection Regulation (GDPR) | In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. |
| Hosting | Amazon Web Services (AWS), primarily in the US-West-2 region and partially in US-East-1. |
| Photos | Deleted immediately after processing, or within 30 days under the customer's policy. Retained photos are automatically blurred. |
| Identifiers | Scan records carry anonymized, randomly generated IDs. 3DLOOK cannot identify a specific individual from stored scan records. |

FitXpress is not a medical device. The regulatory detail behind that statement is in the [trust FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

The scan provides structured body data. Clinical, underwriting and eligibility decisions stay with the program's clinicians, underwriters or other designated decision-makers.

Controls like these reduce risk without shifting duties. The deploying organization still provides privacy notices, obtains consent where needed and sets its own retention policy.

---

<!-- slot 14 · price signal -->
## What FitXpress costs

Plans start with Starter at $1,000 per month for up to 500 scans. Higher tiers add 3D body progress tracking and goal visualization, and custom plans cover larger scan volumes. Plans and features are on the [pricing page](/pricing/).

---

<!-- slot 13 · [FAQ] -->
## Frequently asked questions about FitXpress

### What is FitXpress?
FitXpress is 3DLOOK's AI body scanner for health, wellness, insurance and fitness programs. It turns two guided smartphone photos into 80+ body measurements, calculated metrics such as BMI, body composition estimates and a 3D model. Results are delivered through an API and SDKs.

### What does each scan return?
Each scan returns 80+ body measurements, BMI and BMR, body composition estimates (body fat %, lean mass, fat mass), a 3D model and a predicted weight. Capture-quality flags come with the results. Programs can also compare two scans they select.

### How long does a scan take?
The time is under 45 seconds from the photos to structured results. The person takes two photos, one from the front and one from the side.

### Does FitXpress need special hardware?
No. FitXpress works with a standard smartphone camera and needs no additional hardware.

### How accurate is the FitXpress body scanner?
3DLOOK's published figures use expert tape measurements as the reference. Reported accuracy is approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. The relevant question is whether the reported error and repeatability are suitable for the intended workflow. Detailed methodology is available under a non-disclosure agreement.

### Is there a body measurement API and SDK?
Yes. FitXpress is delivered through an API and web and mobile SDKs, including supported iOS and Android integrations. Access is set up after a demo call or under a non-disclosure agreement.

### Can we use our own branding and keep results server-side?
Yes. Onboarding, consent wording and the results view are yours to design. Results can also stay server-side, with the person seeing only a confirmation screen. The photo capture layer stays fixed to protect measurement quality.

### Where is data stored, and how long are photos kept?
Data is hosted on AWS, primarily in US-West-2 and partially in US-East-1. Photos are deleted immediately after processing, or within 30 days under the customer's policy. Retained photos are automatically blurred, and faces are obfuscated at capture.

### Is FitXpress HIPAA compliant?
HIPAA is a regulatory framework, not a certification. FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA. The BAA is available for qualifying enterprise deployments.

### Is FitXpress a medical device, and what about the FDA?
FitXpress is not a medical device. It is not cleared, authorized or approved by the FDA, and 3DLOOK makes no representation as to whether FDA clearance, authorization or approval is required for a particular use case. The UK and EU position is in the [trust FAQ](/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

### Does 3DLOOK train its models on our data?
No. 3DLOOK does not use production customer data to train its models unless the customer gives explicit, documented authorization.

### How much does FitXpress cost?
The entry plan, Starter, is $1,000 per month for up to 500 scans. Custom plans cover larger volumes. Current plans are on the [pricing page](/pricing/).

---

<!-- slot 15-16 · closing CTA + soft alternative -->
## See FitXpress in your workflow

A demo walks through your capture flow and the outputs your program needs. It also settles which integration pattern fits your stack. API and SDK access follows the call.

<!-- builder: primary button --> **Book a demo**

Not ready for a call? Read the [accuracy framework](/content-hub/mobile-body-scanning-accuracy/) first. It sets out the questions to ask any body scanning vendor, 3DLOOK included.
