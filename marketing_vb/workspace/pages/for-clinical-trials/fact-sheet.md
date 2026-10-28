---
product: fitxpress
type: vertical-page
vertical: clinical-trials
status: review
---

# Fact sheet for the blind judge: clinical trials landing (three drafts, 2026-10-27)

What the judge cannot see from the copy. It covers three drafts of the same page: **A** =
`nika-v3-2026-10-27`, **B** = `nika-v2-2026-10-27`, **C** = `asselya-v4-2026-10-27`. Anything not
verified is labelled unverified. All three are local HTML prototypes on one template.

## Page and technical layer

- Canonical in all three: `https://3dlook.ai/fitxpress/for-clinical-trials/` (self). The site's landing map
  lists the same URL. Parent `/fitxpress/` is not live yet, so the breadcrumb has two levels (Home → page).
- Schema: WebPage, Service (`audience` = BusinessAudience; `areaServed` US, GB, EU in A and B), FAQPage
  (matches the visible FAQ: A 10, B 10, C 5 questions), BreadcrumbList (2 levels).
- Yoast title / description length: A 54 / 145, B 57 / 144, C 66 / 160.
- Visible copy, hero to form, mobile duplicate table cards excluded: A ~3,150 words, B ~2,910, C ~2,070.
- Viewports: B and C checked at 1280×800 (H1 and the hero "Book a demo" inside the first screen) and
  375×812 (no horizontal scroll, hero CTA in the first screen). A shares B's template, not measured.
  768 and 1440 not checked. Contrast and performance not measured. No sticky mobile CTA.
- Form: HubSpot embed at `#demo` in all three, form id `f227f5ce-…` = the public /contact-us/ form. The
  site's shared FitXpress demo form is a different form. Analytics events: not verified firing.
- One `[PLACEHOLDER]` HTML comment in all three (remaining client logos to come from design); A has a
  second one (hub article URL). A and B carry author notes in a long HTML comment at the top.

## Sources behind every number and client name

| On the page | In | Source | Status |
|---|---|---|---|
| 100+ clients, since 2016 | A B C | `proof-points.md` (the one public client count; founded 2016) | verified |
| Logos: Yazen, UK Meds, Healthyr | A B C | 3DLOOK clients; logos approved for site use | verified; none runs clinical trials. No clinical trial client exists |
| 2 photos; under 45 sec | A B C | `proof-points.md` / `tech-spec.md`: "under 45 seconds from the photos to structured results" | verified |
| 80+ body measurements | A B C | `proof-points.md` | verified |
| From $1,000 per month; Starter $1,000 / 500 scans; Pro $1,500 / 1,000 scans incl. 3D Body Progress and 3D Goal Visualization; Personalized: higher volumes, multilingual flow | A B | live `/pricing/` (checked 2026-10-28) | verified against today's page. The company is moving FitXpress billing from scans to API requests; the live page has not changed yet |
| "request-based pricing" (no figure) | C | internal pricing model | consistent with the coming pricing; the live `/pricing/` still says scans; C has no link to `/pricing/` |
| < 1 cm typical scan-to-scan difference for most evaluated body measurements | A B C | `proof-points.md` (internal study, not peer-reviewed, methodology under NDA) | verified |
| 96-97% vs expert manual measurement, typical absolute error 1.5-2.0 cm | A B C | same | verified. House format uses hyphens; C's FAQ and paragraph use en dashes |
| Validation population ages 16-78, 38-210 kg, 150-220 cm, US and Europe | A B | `proof-points.md` | verified (C omits the population) |
| Photos deleted after processing or kept up to 30 days, blurred, face obfuscation | A B | `compliance.md` (live trust FAQ) | verified |
| AWS US-West-2 / US-East-1; GDPR controller / processor; DPA + SCCs + UK Addendum; HIPAA BAA sentence; SOC 2 "working toward"; encryption; model training | A B C | `compliance.md`, canonical wording | verified |
| "An independent regulatory assessment concluded … UK MDR / EU MDR … current intended purpose"; "not cleared, authorized or approved by the FDA" | A B | `compliance.md` canonical | verified. C replaces it with "The current regulatory assessment applies to the product's assessed intended purpose" and has no "FitXpress is not a medical device" sentence |
| All mock values (waist 112.4 → 108.1 cm, hip 121.0 → 118.2 cm, body-fat estimate 41.3% → 39.8%, −6.2 / −4.1 cm at week 12, participant and site numbers, dates) | A B C | invented for illustration | labelled "Illustrative" on the page; not data |
| Third-party statistics (FDA draft guidance Jan 2025, JAMA 2016 attrition 30-45%, BELIEVE 92.8% / 71.8%, FDA DHT guidance Dec 2023, ICH E6(R3)) | A: FDA quote, 30-45%, DHT, ICH. B: BELIEVE, FDA "expensive", calibrated-scale endpoint, DHT. C: none | primary sources, checked 2026-10-28 (`sources-problem-block.md`) | **FDA "procedure is not standardized"** (A): verbatim, draft guidance Jan 2025 §III.B.3.b; FDA's wording is "not considered a surrogate for visceral fat content or metabolic abnormalities", and it gives two further reasons (non-visceral fat; lower accuracy at BMI > 35) that capture standardization does not address. **FDA "expensive… multiple blinded, central readers"; body composition in "a representative sample" "by DXA or a suitable alternative"** (B): correct, joined from two sections (pp. 3 and 12); the page's "subset" paraphrases "sample". **Primary endpoint "measured on a calibrated scale"** (B): endpoint correct ("mean percentage change from baseline body weight"); "calibrated scale" is not in the guidance. **30-45% attrition** (A): figure correct (Khera, JAMA 2016: 28 one-year trials of five older drugs, "30%-45% in all trials"); the paper does not link attrition to visits; recent trials differ (STEP 1: 94.3% completed). **BELIEVE 92.8% / 71.8%** (B): conference press figures, superseded by the peer-reviewed paper (Nature Medicine, March 2026: 92.3% vs 71.1% at week 48, DXA, phase 2); the page cites Medscape. **FDA DHT guidance, December 2023** (A, B): final guidance, correct; FDA's term is "fit-for-purpose"; "regardless of whether the DHT meets the definition of a device" confirmed. **ICH E6(R3)** (A): adopted January 2025, topics present (mostly "source records") |

## Capability claims and their status

| Claim | In | Status |
|---|---|---|
| Web and mobile SDKs; supported iOS and Android integrations | A B C | verified (`tech-spec.md` public wording) |
| "React Native kit" / "React Native" | A B C | **unverified**: `tech-spec.md` says do not write React Native (not confirmed by product) |
| "Native kits capture on the device and work offline" | A B | **unverified**: no source in the product docs; flagged as unconfirmed on an earlier page |
| Results through webhook events, polling fallback; "webhooks have no automatic retries or signature verification" | A B | **unverified**: no source in the product docs |
| iOS 15 or later; older Android models with lower frame rate; standing-only capture; wheelchair users and amputees not supported; two gender options; height difference above 2 cm affects results | A B | **unverified**: no source in `tech-spec.md`; earlier pages cut these for the same reason |
| Height, weight and gender are required inputs | A B | partly verified: height and gender required; weight optional for measurements |
| "Version requirements for the study period are agreed with 3DLOOK before the study starts" | B | **unverified** (the draft's own note asks product to confirm) |
| Real-Time Pose Validation guides pose and framing | A B C | verified (`tech-spec.md`) |
| Pose validation results and Clothing Detector flags "stored with each scan" and returned as record fields; scans arrive "complete or flagged"; "flagged scans go to a retake" | A B (C: "indicators available in its configuration") | partly verified: `compliance.md` lists pose-validation flags and clothing classification among stored technical data; product has not confirmed them as fields returned to the customer |
| "Each record shows … how they were captured" (capture source) | A B | **unverified** field |
| Scan records use random identifiers; 3DLOOK cannot identify an individual from stored records | A B | verified (`compliance.md`) |
| BMI and BMR are calculated metrics; body composition is an estimate | A B C | verified. BMI is calculated from the height and weight entered for the scan |
| Remote pre-check "surfaces BMI-based screening data before the first site visit" | A | BMI comes from entered height and weight, not from the photos |
| 3D Body Progress compares two scans (Pro) | A B C | verified as: Body Progress compares two scans the customer selects, by scan identifier; 3DLOOK does not link scans to people |
| FitXpress Admin Panel: central view and CSV export | A B | verified as an optional monitoring and export interface; it does not replace API / SDK integration |
| No prebuilt EDC integration | C | consistent with product docs (no EDC connector exists) |
| "Supports blinded study designs" | A B | not a product feature: describes results hidden from participants by the integrating platform |
| "Audit-ready records" supporting monitoring, QA and audit review; records "support" ICH E6(R3) documentation expectations | A | no audit-trail, 21 CFR Part 11 or GCP documentation exists for FitXpress |
| FitXpress is not a medical device | A B | verified, canonical sentence |
