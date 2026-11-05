---
product: fitxpress
type: vertical-page
vertical: clinical-trials
status: review
---

# Fact sheet for the blind judge: clinical trials landing, round 2 (draft of 2026-11-03)

What the judge cannot see from the copy. One draft: `nika-v3b-2026-11-03.html` (local HTML prototype).
Anything not verified is labelled unverified.

## Page and technical layer

- Canonical: `https://3dlook.ai/fitxpress/for-clinical-trials/` (self), the URL in the site's landing map.
  Parent `/fitxpress/` is not live yet, so the breadcrumb has two levels (Home → page).
- Schema: WebPage, Service (`audience` = BusinessAudience with audienceType; `areaServed` present), FAQPage
  (5 questions, matches the visible FAQ), BreadcrumbList (2 levels). FAQ questions are H3.
- Title 55 characters, description 144.
- Visible copy, hero to form, mocks and the mobile duplicate of the comparison table excluded: ~1,990 words.
- Viewports: not re-checked for this draft. The template is the one checked on 2026-10-28 at 1280×800 and
  375×812 (H1 and hero CTA in the first screen, no horizontal scroll). 768 and 1440 not checked. Contrast and
  performance not measured.
- Form: HubSpot embed at `#demo`, form id `f227f5ce-…` = the public /contact-us/ form. The site's shared
  FitXpress demo form is a different form (`11acb23a-…`, carries the hidden `fx_vertical` field). The author
  notes in the top HTML comment flag the swap. Analytics events: not verified firing.
- Author notes in a long HTML comment at the top ("CONFIRM BEFORE PUBLISHING" list). No `[PLACEHOLDER]` string.
- Links: hub article, accuracy article, trust FAQ, /technology/, /pricing/, privacy policy, contact page,
  legal@ and privacy@ mailto, primary sources under the problem cards. No links to sibling vertical pages.

## Sources behind every number and client name

| On the page | Source | Status |
|---|---|---|
| 100+ clients, since 2016 | `proof-points.md` | verified |
| Logos: Yazen, UK Meds, Healthyr | 3DLOOK clients, logos approved for site use | verified; none runs clinical trials. No clinical trial client exists |
| Caption "…since 2016, including digital health and weight management programs" | client list | true; the page kit's rule says the caption ends at "since 2016" when no client of the vertical is in the row |
| 2 photos; under 45 sec from photos to a structured record | `proof-points.md` / `tech-spec.md` ("under 45 seconds from the photos to structured results") | verified |
| 80+ body measurements | `proof-points.md` | verified |
| From $1,000 per month; no integration fee | live `/pricing/` and the coming pricing | verified. A redesigned /pricing/ (billing unit: API requests) goes live within days; the page names no unit |
| < 1 cm typical scan-to-scan difference for most evaluated body measurements | `proof-points.md` (internal, not peer-reviewed, methodology under NDA) | verified |
| 96-97% vs expert manual measurement, typical absolute error 1.5-2.0 cm | same | verified. House format (`accuracy-formulations.md`) is `96-97%` and `1.5-2.0 cm` with hyphens, not "96 to 97%" / "1.5 to 2.0 cm" as on the page |
| Validation population 16-78, 38-210 kg, 150-220 cm, US and Europe | `proof-points.md` (150-220 cm confirmed 2026-09-02; the older 150-205 cm is superseded) | verified |
| "Accuracy is not published by body shape or skin tone" | no product-info file | statement of absence; no breakdown by body shape or skin tone is published |
| Photos deleted after processing or kept up to 30 days, blurred, face obfuscation | `compliance.md` | verified |
| AWS US-West-2 / US-East-1; GDPR controller / processor sentence; DPA + SCCs + UK Addendum; SOC 2 "working toward"; documents under NDA (security overview, pen-test summary, diagrams, incident response) | `compliance.md` | verified, canonical wording |
| UK MDR / EU MDR assessment sentence; "not cleared, authorized or approved by the FDA"; "FitXpress is not a medical device" | `compliance.md` | verified, canonical |
| EMA: waist circumference as a secondary endpoint in weight-management trials | EMA guideline 2016, §4.2.1 | verified |
| Self-measured waist differs from a trained measurer by 1 to 6 cm on average, either direction | Ross et al. 2020 (IAS/ICCR); Contardo Ayala et al. 2014 (+5.98 cm, n = 622); Dekkers et al. 2008 (+1.1 cm, n = 1,298) | verified as a range across three studies; direction varies |
| "Remote check-ins already return body weight" | FDA DHT guidance, Dec 2023, §IV.D.2 (home weight for the same endpoint with verification and validation) | verified (paraphrase, not attributed on the page) |
| FDA DHT guidance (Dec 2023): fit-for-purpose, verification and validation, "whether or not the technology is a device" | FDA final guidance | verified ("regardless of whether the DHT meets the definition of a device") |
| All mock values (waist 112.4 → 108.1 cm, hip, body-fat estimate, −6.2 / −4.1 cm at week 12, participant and site numbers, dates, task list) | invented for illustration | labelled "Illustrative" on the page |

## Capability claims and their status

| Claim | Status |
|---|---|
| Web and mobile SDKs, including supported iOS and Android integrations | verified (`tech-spec.md` public wording) |
| White-label inside the platform's app; no separate app to install | verified for SDK embedding; the capture layer itself stays fixed |
| Real-Time Pose Validation guides pose and framing | verified |
| "Guided capture with pose and clothing checks" | verified at the level "the Clothing Detector identifies clothing conditions that may interfere with capture and can prompt corrective action" |
| Mock caption "Capture checks passed; added to the study record" | partly verified: pose and clothing flags are stored on the 3DLOOK side; product has not confirmed them as fields returned to the customer |
| Timestamp and scan identifier on every record | verified |
| "Scan records use randomly generated identifiers, which the study maps to its own participant numbers" | verified (`compliance.md`: random IDs, 3DLOOK cannot identify a person from stored data) |
| **"No personal identifiers are processed on the 3DLOOK side."** | **contradicts `compliance.md`**: photos and measurements may be personal data; "no personal identifiers" wording is retired (2026-09-18). Approved line: scan records use random IDs and 3DLOOK cannot identify a specific individual from the stored data |
| JSON via API, CSV export from the Admin Panel, 3D model export | verified; Admin Panel is an optional monitoring and export interface |
| No prebuilt EDC integration | consistent with product docs |
| BMI and BMR calculated; body composition estimates; lean mass includes organs, bone and water | verified |
| Results hidden from participants: decided by the study team / platform | verified as the platform's control, not a FitXpress feature |
