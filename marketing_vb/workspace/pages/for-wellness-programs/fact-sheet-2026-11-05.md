---
product: fitxpress
type: vertical-page
vertical: wellness-programs
status: review
---

# Fact sheet for the blind judge: wellness programs landing, round 2 (draft of 2026-11-03)

What the judge cannot see from the copy. One draft: `nika-v4-2026-11-03.html` (local HTML prototype).
Anything not verified is labelled unverified.

## Page and technical layer

- Canonical: `https://3dlook.ai/fitxpress/for-wellness-programs/` (self), the URL in the site's landing map.
  Parent `/fitxpress/` is not live yet, so the breadcrumb has two levels (Home → page).
- Schema: WebPage, Service (`audience` = BusinessAudience with audienceType; `areaServed` present), FAQPage
  (5 questions, matches the visible FAQ), BreadcrumbList (2 levels). FAQ questions are H3.
- Title 58 characters, description 150.
- Visible copy, hero to form, hero mock excluded: ~1,520 words.
- Viewports: not re-checked for this draft. The template is the one checked on 2026-10-28 at 1280×800 and
  375×812. 768 and 1440 not checked. Contrast and performance not measured.
- Form: HubSpot embed at `#demo`, form id `f227f5ce-…` = the public /contact-us/ form. The site's shared
  FitXpress demo form is a different form (`11acb23a-…`, carries the hidden `fx_vertical` field). The author
  notes in the top HTML comment flag the swap. Analytics events: not verified firing.
- Author notes in an HTML comment at the top ("CONFIRM BEFORE PUBLISHING" list). No `[PLACEHOLDER]` string.
- Links: wellness rewards article, accuracy article, trust FAQ, /pricing/, privacy policy, contact page,
  KFF and Gallup sources under the problem cards. No link to the wellness hub article or to sibling vertical
  pages. No logo row.

## Sources behind every number and client name

| On the page | Source | Status |
|---|---|---|
| 100+ clients, since 2016 | `proof-points.md` | verified. No client in employee wellness exists |
| 2 photos; under 45 sec from the photos to structured results | `proof-points.md` / `tech-spec.md` | verified, canonical wording |
| 80+ body measurements | `proof-points.md` | verified |
| Starter from $1,000 / up to 500 requests; Pro from $1,500 / up to 1,000 requests; Enterprise custom; no integration fee; "a request is the billing unit" | internal pricing model | verified against the coming pricing. Live `/pricing/` still says "scans" on 2026-11-05; the redesigned /pricing/ with requests goes live within days, and this page is planned to publish with it |
| 96-97% vs expert manual measurement, typical absolute error 1.5-2.0 cm; < 1 cm typical scan-to-scan difference for most evaluated measurements | `proof-points.md` (internal, not peer-reviewed, methodology under NDA) | verified, house format |
| Validation population 16-78, 38-210 kg, 150-220 cm, US and Europe | `proof-points.md` | verified |
| "Half of large employers with a screening program offer no remote way to complete it" | KFF Employer Health Benefits Survey 2025: 50% of large firms with screening allow remote completion | verified (inverse of the 50%) |
| 62% of US firms with 200+ workers and a screening program use incentives or penalties to get employees to complete it | KFF EHBS 2025, section 12 | verified; this is for completion, not results (14% reward results) |
| 78% of US employees with remote-capable jobs work hybrid (52%) or fully remote (26%) | Gallup Hybrid Work indicator, May 2026 | verified; remote-capable employees only. The card captions carry no year |
| Biometric screening = in-person check by a medical professional: BMI, blood pressure, cholesterol, glucose | KFF definition | verified |
| Photos deleted after processing or kept up to 30 days, blurred, face obfuscation | `compliance.md` | verified |
| GDPR controller / processor sentence | `compliance.md` | verified, canonical |
| HIPAA: "3DLOOK can execute a BAA" / "can act as a business associate under an executed BAA" | `compliance.md` ("can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA") | verified in substance |
| "Encryption and access controls support deployment review" | `compliance.md` (TLS in transit, SSE-S3 at rest; RBAC, tenant isolation) | verified but generic; hosting (AWS US) and the privacy contact are not on the page |
| No compliance claim under HIPAA, ADA, GINA or EEOC rules | EEOC 30% incentive limit vacated from 2019, no replacement rule | correct boundary |
| "FitXpress is not a medical device" | `compliance.md` | verified, canonical |
| All mock values (waist 35.8 in, hip 40.2 in, BMI 26.1, body fat 29.4%, scan ID, date) | invented for illustration | labelled "Illustrative" on the page |

## Capability claims and their status

| Claim | Status |
|---|---|
| API and SDKs for wellness platforms | verified |
| Visual and voice prompts during capture | verified (`tech-spec.md`: voice prompts for a person scanning alone) |
| **Camera-only capture; gallery upload not supported** | **unverified**: not in `tech-spec.md`; the author notes ask product to confirm |
| **"Participants who cannot use the current standing capture flow need an alternative"** | **unverified**: standing-only capture is not in `tech-spec.md` |
| Real-Time Pose Validation guides pose and framing; Clothing Detector "identifies clothing conditions that may interfere with capture and can prompt corrective action" | verified, approved wording |
| "Quality checks" in the mock | partly verified: checks run during capture; product has not confirmed check results as returned fields |
| BMI calculated from entered height and weight; body composition estimates | verified |
| "Weight-source verification is available through Smart Scales" | partly verified: Smart Scales returns a weight estimate and a mismatch flag when self-reported weight is provided |
| Integration can use scan identifiers without sending names or contact details | verified (random IDs) |
| Program links scans to the participant; 3DLOOK does not | verified |
| Reward thresholds above scan-to-scan variation (< 1 cm) | consistent with the repeatability figure; a design recommendation, not a product feature |
