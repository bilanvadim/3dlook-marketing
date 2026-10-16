---
product: fitxpress
type: vertical-page
vertical: bariatric
status: draft-v2
---

# Fact sheet for the blind judge: bariatric landing v2 (prototype, 2026-10-16)

What the judge cannot see from the copy. Anything not verified is labelled unverified.

## Page and technical layer

- URL and canonical: `https://3dlook.ai/fitxpress/for-bariatric-programs/` (self-canonical, decided).
- Focus keyphrase `bariatric patient tracking` (Ahrefs US 10/month, CPC $0.60; the only follow-up-side
  phrase with measured demand). Secondary: `bariatric tracking software` (10), `bariatric software` (30),
  `muscle loss after bariatric surgery` (10). Clinic-side demand is near zero for every phrasing.
- The vertical's hub article is "Bariatric Pre-Qualification and Patient Progress Tracking: Body Data for
  Obesity Care Teams" (content hub), linked twice from the page.
- Parent `/fitxpress/` is not live yet (redirects), so the breadcrumb has two levels and the page cannot
  link up to it. Sibling links go to the live telehealth page and the live BMI verification page; the
  GLP-1 landing is still planned and is not linked.
- Schema: WebPage, Service (`audience` BusinessAudience, `areaServed` US + UK), FAQPage (4 questions,
  matching the visible FAQ; each question is an H3 inside its accordion summary), BreadcrumbList (2 levels).
- Yoast title 53 characters, meta description 144.
- Viewports checked: 1280×800 (H1, lede and "Book a demo" fit the first screen; CTA bottom at 721 px), 375×812 (no horizontal
  scroll, three problem cards stack, record table fits without scrolling, comparison becomes cards, hero
  CTA at 613 px). 768 and 1440 not checked. Performance and contrast not measured (local prototype). No
  sticky mobile CTA in the prototype (WordPress template).
- Form at `#demo`: HubSpot embed, currently the public contact-page form id; the shared FitXpress demo
  form id is swapped in at integration. Events in the prototype: `demo_click`,
  `fitxpress_demo_form_submitted`; not verified firing.
- One `[PLACEHOLDER]` HTML comment is a handoff item: the remaining client logos come from design (the
  logo row must carry all clients' logos).

## Sources behind every number and client name

| On the page | Source | Status |
|---|---|---|
| 100+ clients, since 2016 | `proof-points.md` (the one public client count) | verified |
| Logos: Yazen, UK Meds, Healthyr | 3DLOOK clients; same logos on the live `/pricing/` page | verified; none is a bariatric program, and the caption does not say they are |
| 2 photos; under 45 sec from the photos to structured results | `proof-points.md`, canonical timing wording | verified |
| No integration fee; plans from $1,000 a month | `pricing.md` (public since 2026-09-30); live `/pricing/` | verified |
| Starter $1,000 / 500 API requests; Pro $1,500 / 1,000 API requests with 3D Body Progress tracking and 3D Goal Visualization | live `/pricing/` tiers; billing unit moves from scans to API requests (company decision 2026-10-16; the live page still says scans and is being updated) | verified, ships with the pricing update |
| 80+ body measurements | `proof-points.md` | verified |
| 30 days, 6 months and 1 year (US accredited programs) | American College of Surgeons, MBSAQIP Standards 2026, Standard 6.2: "It is mandatory that all patients be followed through the 30-day, 6-month, and 1-year follow-up time frames." | verified at the primary source |
| Two years (UK) | NICE guideline NG246 (2025, replaced CG189), 1.18.17: "a follow-up care package for a minimum of 2 years within the bariatric service" | verified at the primary source |
| 44.6% at five years; long distance most cited | Krietenstein et al., Nutrients 2024 (PMC11357598), prospective single-centre study, Würzburg, Germany, 573 patients; follow-up rate 44.6% at year 5; "long distance" named by 29.7% of 219 interviewed lost patients, the most frequent reason | verified at the primary source |
| 2 attempts per missed time frame, documented in the registry | MBSAQIP Standards 2026, Standard 6.2: "a minimum of two attempts to contact the patient for each follow-up time frame", documented in the MBSAQIP Registry | verified at the primary source |
| 8.1 kg lean body mass at 12 months; about 55% within 3 months | Nuijten et al., Obesity Reviews 2022 (PMC9285034), meta-analysis of 59 studies: "pooled LBM loss was -8.13 kg"; "About 55% of 12-month LBM loss occurred within 3-month postsurgery" (DXA / BIA studies) | verified at the primary source |
| 3, 6 and 12 months in How it works | example schedule ("such as"), set by the program | not a claim |
| < 1 cm; 96-97%, 1.5-2.0 cm | `proof-points.md` / `accuracy-formulations.md` (internal validation, not peer-reviewed, methodology under NDA) | verified |
| 38-210 kg ("up to 210 kg" in the FAQ), 150-220 cm, ages 16-78, US and Europe | `proof-points.md` | verified |
| Photo retention, identifiers, HIPAA/BAA, GDPR roles, encryption, model training | `compliance.md` (from the live trust FAQ), canonical wording | verified |
| All values in the two mocks (weights, waist, body-fat, BMI pairs, dates, patient numbers) | invented for illustration | labelled "Illustrative" on the page |

## Capability claims and their status

| Claim | Status |
|---|---|
| Real-Time Pose Validation gives pose and framing guidance, with voice prompts | verified (`tech-spec.md`, fitness final wording) |
| Record lists "Processing status and timestamps" | the confirmed level for public pages (pose / clothing fields not listed until product confirms) |
| BMI from entered weight vs BMI from the Smart Scales weight estimate, both from entered height | feature verified (`tech-spec.md`); Smart Scales is still labelled beta in `tech-spec.md`, while live `/pricing/` lists "Predicted weight" without a beta label; the weight-error figure is not used on the page (contested internally) |
| Body Progress compares two scans the program selects; the program links scan identifiers to patients | verified (`compliance.md`: 3DLOOK does not track individuals) |
| FitXpress Admin Panel: optional monitoring and CSV export | verified canonical wording; it does not replace API / SDK integration |
| The program designs consent and results screens; the capture layer stays fixed | verified (`tech-spec.md`, "What's NOT customizable") |
| Production infrastructure already deployed in remote BMI-verification and weight-management workflows | approved pilot-proof sentence (insurance final, 2026-10-02) |
| FitXpress is not a medical device | verified, canonical sentence |
