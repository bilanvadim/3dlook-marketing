---
product: fitxpress
type: vertical-page
vertical: bariatric
status: review
---

# Fact sheet for the blind judge: bariatric landing (prototype, 2026-10-16)

What the judge cannot see from the copy. Anything not verified is labelled unverified.

## Page and technical layer

- Final URL: not decided. The draft's canonical is `https://3dlook.ai/fitxpress/for-bariatric-programs/`
  (self-canonical). The site's landing map lists `/fitxpress/for-bariatric-clinics/`.
- Parent `/fitxpress/` is not live yet (it redirects), so the breadcrumb has two levels.
- Schema in the prototype: WebPage, Service (`audience` = BusinessAudience, **no `areaServed`**),
  FAQPage (7 questions, matches the visible FAQ), BreadcrumbList (2 levels). Organization comes from the
  site template.
- Yoast title 53 characters, meta description 144 (version B: 55 / 146).
- Performance: not measured (local prototype). Viewports checked: 1280×800 (H1, lede and "Book a demo"
  fit the first screen), 375×812 (no horizontal scroll, the comparison table becomes cards, hero CTA in
  the first screen). 768 and 1440 not checked. Contrast: not measured. No sticky mobile CTA.
- Form: HubSpot embed at `#demo`, currently the public contact-page form id; the shared FitXpress demo
  form id is to be swapped in. Analytics events in the prototype: `demo_click`,
  `fitxpress_demo_form_submitted`; not verified firing.
- One `[PLACEHOLDER]` HTML comment: remaining client logos to come from design.

## Sources behind every number and client name

| On the page | Source | Status |
|---|---|---|
| 100+ clients, since 2016 | `proof-points.md` (the one public client count) | verified |
| Logos: Yazen, UK Meds, Healthyr | 3DLOOK clients; the same logos are on the live `/pricing/` page | verified; none of them is a bariatric program |
| 2 photos; under 45 sec | `proof-points.md`, canonical wording "under 45 seconds from the photos to structured results" | verified (the page words it "processing from photos to a structured record") |
| 80+ body measurements | `proof-points.md` | verified |
| From $1,000 per month; Starter $1,000 / 500; Pro $1,500 / 1,000 incl. 3D Body Progress and 3D Goal Visualization; Personalized: higher volumes, multilingual guided capture | live `/pricing/` (2026-10-16) | verified. The live page counts "scans"; the company is moving billing to API requests (decided 2026-10-16), so "API requests" (version B) matches the coming pricing and "scans" (version A) matches today's page |
| < 1 cm typical scan-to-scan difference for most evaluated body measurements | `proof-points.md` / `accuracy-formulations.md` (internal validation, not peer-reviewed, methodology under NDA) | verified |
| 96-97% vs expert manual measurement, typical absolute error 1.5-2.0 cm | same | verified |
| Validation population 38-210 kg, 150-220 cm, ages 16-78, US and Europe | `proof-points.md` | verified. Unresolved conflict: the public API documentation accepts entered weight 40-200 kg and height 145-220 cm |
| Photos deleted after processing or kept up to 30 days, blurred, face obfuscation | `compliance.md` (from the live trust FAQ) | verified |
| HIPAA / BAA sentence; GDPR controller / processor sentence | `compliance.md`, canonical wording | verified |
| 44.6% (five-year follow-up) | third-party: Krietenstein et al., Nutrients 2024 (PMC11357598), linked on the page | number verified: follow-up rate at year 5, prospective single-centre study, Würzburg, Germany, 573 patients. Reasons: "long distance" named by 29.7% of 219 interviewed lost patients; the abstract calls travel issues "the main reason", the conclusion says "Though not frequently mentioned, travel issues were the most common reasons" |
| 40% (self-reported BMI and severe obesity) | third-party: Zhao et al., Preventing Chronic Disease 2023, linked on the page | number verified: "Self-reported BRFSS data underestimated the overall prevalence of severe obesity by 40% (5.3% vs 8.8%)", 2020 US survey data, a relative difference in population prevalence of BMI ≥40, not an individual error |
| All values in the three mocks (119.0 kg, 131.5 cm, 46.8%, BMI 44.6 / 44.9 etc., dates in Oct 2026 / Jan 2027, patient numbers) | invented for illustration | labelled "Illustrative" on the page; not data |

## Capability claims and their status

| Claim | Status |
|---|---|
| Real-Time Pose Validation guides pose and framing | verified (`tech-spec.md`) |
| Smart Scales weight estimate and the BMI comparison | the feature exists; `tech-spec.md` still labels Smart Scales "beta"; the live `/pricing/` lists "Predicted weight" without a beta label. Beta status unconfirmed |
| Weight-estimate accuracy | `proof-points.md` has "approximately 3.5% mean absolute error under evaluated conditions"; the page does not use it |
| "Pose validation results and clothing flags are stored with each scan"; "capture checks passed" in the mock | partly verified: `compliance.md` lists pose-validation flags and clothing classification among stored technical data; product has not confirmed these as fields returned to the customer |
| "Timestamp and capture source" in each record | timestamp verified; "capture source" field unverified |
| Body Progress compares a follow-up scan with the baseline | verified as: Body Progress compares two scans chosen by the customer, by scan identifier; 3DLOOK does not link scans to people |
| FitXpress Admin Panel: central view and CSV export | verified as an optional monitoring and export interface; it does not replace API / SDK integration |
| FitXpress is not a medical device | verified, canonical sentence |
