---
product: fitxpress
type: vertical-page
vertical: wellness-programs
status: review
---

# Fact sheet for the blind judge: wellness landing (three drafts, 2026-10-27)

What the judge cannot see from the copy. Three drafts for the same landing slot: **A** = `nika-v1-2026-10-27`
(wellness apps, member progress), **B** = `nika-v2-2026-10-27` (wellness rewards verification for employers
and insurers), **C** = `asselya-v3-2026-10-27` (remote biometric screening for employee wellness programs).
Anything not verified is labelled unverified. All three are local HTML prototypes.

## Page and technical layer

- Site landing map for this slot: URL `/fitxpress/for-wellness-programs/`, angle "remote biometric screening",
  primary keyword `at home biometric screening` (US 80), secondaries: biometric screening companies, onsite
  biometric screening, company biometric screening, wellness rewards program, corporate wellness platform,
  employee wellness app. The informational query "biometric screening" (8,600) belongs to a planned article.
  Boundary rule for this slot: FitXpress covers the body-measurement part of a screening only; blood pressure
  and blood tests are out of scope and the page says so; no ADA, GINA, EEOC or HIPAA wellness-program
  compliance claims; no result interpretation.
- Canonicals: A `/fitxpress/for-wellness-platforms/`, B `/fitxpress/for-health-plans-and-employer-wellness/`,
  C `/fitxpress/for-wellness-programs/`. Parent `/fitxpress/` is not live; breadcrumb has two levels in all.
- Schema: A and B: WebPage, Service (`audience` BusinessAudience, `areaServed` set), FAQPage (9 questions, matches
  the visible FAQ), BreadcrumbList. C: WebPage, Service (no `audience`, no `areaServed`), FAQPage (6), BreadcrumbList.
- Yoast title / description: A 57 / 142, B 51 / 150, C 59 / **161**. C's title ends "| 3DLOOK", not FitXpress.
- Visible copy, hero to form, mobile table cards excluded: A ~2,610 words, B ~2,770, C ~1,470.
- you/your per 1,000 words: A 14.2, B 8.3, C 6.1.
- Viewports: B and C checked at 1280×800 (H1 and hero "Book a demo" in the first screen) and 375×812 (no
  horizontal scroll). A shares B's template, not measured. 768 / 1440, contrast and performance not measured.
- Form: HubSpot embed at `#demo` in all three, form id `f227f5ce-…` = the public /contact-us/ form, not the
  site's shared FitXpress demo form. Analytics events not verified.
- `[PLACEHOLDER]` HTML comments: A 2, B 2, C 0. A and B carry long author notes in an HTML comment.
- Links: B links `/fitxpress/for-connected-fitness/` and `/fitxpress/for-telehealth-and-weight-loss/`; neither URL
  exists (the fitness page is `/fitxpress/for-connected-and-digital-fitness/`). A and B link the hub articles as
  placeholders. C links the rewards article, the trust FAQ and `/pricing/`.
- Logos: none in any draft. A and B show "100+ clients … since 2016, across digital health, weight management and
  apparel"; C has no client count.

## Sources behind every number and client name

| On the page | In | Source | Status |
|---|---|---|---|
| 100+ clients, since 2016 | A B | `proof-points.md` | verified |
| 2 photos; under 45 seconds | A B C | `proof-points.md` / `tech-spec.md`: "under 45 seconds from the photos to structured results" | verified |
| 80+ body measurements | A B C | `proof-points.md` | verified |
| < 1 cm typical scan-to-scan difference for most evaluated measurements | A B C | `proof-points.md` (internal study, not peer-reviewed, methodology under NDA) | verified |
| 96-97% vs expert manual measurement; 1.5-2.0 cm typical absolute error | A B C | same | verified. House format uses hyphens; C uses an en dash ("96–97%") in one place and "96 to 97%" in another |
| Waist repeatability 0.89 cm; waist mean absolute error 2.14 cm | A B | `proof-points.md` (same study) | figures verified. `accuracy-formulations.md` rule 6: per-measurement figures belong in technical material, not on general pages; they were cut from the wellness hub for that reason |
| Validation population 16-78 years, 38-210 kg, 150-220 cm, US and Europe | A B | `proof-points.md` | verified (C omits it and the NDA line) |
| Plans: Starter $1,000 / 500, Pro $1,500 / 1,000 incl. 3D Body Progress and 3D Goal Visualization; Personalized | A B ("scans") C ("requests") | live `/pricing/` (checked 2026-10-28: "scans") | A and B match today's page. C's "requests" matches the coming billing change, not today's page |
| Photos deleted immediately after processing or retained up to 30 days, blurred, face obfuscation | A B | `compliance.md` | verified |
| "For the FitXpress health workflow, input photos are not stored after processing" | C | `compliance.md` says deleted immediately or kept up to 30 days under the customer's policy | **contradicts** the approved wording |
| HIPAA BAA sentence; GDPR processor / DPA / SCC / UK Addendum; AWS US-West-2 / US-East-1; RBAC and least privilege; SOC 2 "working toward"; model training | A B (C partly) | `compliance.md` | verified. The canonical GDPR sentence is "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR"; none of the drafts uses it verbatim |
| UK MDR / EU MDR assessment; not FDA cleared | B | `compliance.md` canonical | verified |
| All mock values (waist, hip, body-fat, BMI 26.1, weights, participant IDs, dates, "waist reduction of 3 cm" rule) | A B C | invented for illustration | labelled illustrative |
| Third-party statistics in B: CDC 40% (self-report vs severe obesity), KFF 43% and 62% (biometric screening, incentives), Gallup 78% (hybrid / remote) | B | primary sources, checked 2026-10-28 (`sources-problem-block.md`) | **CDC 40%**: correct as quoted (Zhao et al., Preventing Chronic Disease 2023, BRFSS 2020): a population gap in severe-obesity prevalence (5.3% self-reported vs 8.8% corrected), not an individual error; it also concerns self-entered height and weight, which FitXpress uses for BMI. **KFF 43%**: correct, EHBS 2025, firms with 200+ workers offering health benefits that offer workers the opportunity to complete a biometric screening; "recurring verification workload for HR" is not in the source. **KFF 62%**: correct number, EHBS 2025, incentives or penalties for *completing* the screening; only 14% of large firms tie rewards to biometric *results*, so "when money depends on the result" misstates it. **Gallup 78%**: correct (May 2026: 52% hybrid, 26% fully remote; base = remote-capable employees, about half the US workforce). "Onsite screening days miss many of them": partly supported only; KFF 2025: 50% of large firms with screening already allow remote completion. KFF defines biometric screening as an in-person exam by a medical professional (BMI, blood pressure, cholesterol, glucose). A workplace study (Dekkers 2008, 1,298 employees) found self-reported BMI and waist close to measured on average |

## Capability claims and their status

| Claim | In | Status |
|---|---|---|
| Web and mobile SDKs, API | A B C | verified |
| Real-Time Pose Validation guides pose and framing | A B C | verified |
| Clothing Detector "checks clothing before the scan is accepted"; pose / clothing flags "stored with each scan" and returned as fields; "Pose check passed / Clothing check passed" in mocks | A B (C: "clothing checks help identify issues") | partly verified: approved public wording is "identifies clothing conditions that may interfere with capture and can prompt corrective action"; flags as returned fields not confirmed by product |
| "Voice and visual prompts / guidance" | B C | **unverified**: not in `tech-spec.md`; a published fitness article mentions it, the capture-quality FAQ deliberately left it out pending product confirmation |
| "No upload from the phone's gallery" / "camera-only capture" | B C | **unverified** in product docs; stated in the live wellness-rewards article; author's note asks product to confirm |
| "FitXpress does not receive names or contact details" / "integration can use scan identifiers without sending names" | B C | consistent with `compliance.md` (random scan IDs; 3DLOOK cannot identify an individual) |
| Smart Scales "in beta" | C | product docs list Smart Scales; public wording since 2026-10-21 is "Smart Scales" without a beta label |
| BMI calculated from entered height and weight, not from photos; body composition = estimates | A B C | verified |
| iOS 15 or later; older Android with lower frame rate; standing only; wheelchair users / amputees not supported; two gender options; "height, weight and gender are required inputs"; "entered height within 2 cm" | A B (C: "standing capture flow" only) | **unverified**: not in `tech-spec.md`; cut from earlier pages for that reason. Weight is optional for measurements |
| Webhook delivery, polling fallback, "no automatic retries or signature verification" | B | **unverified** |
| FitXpress Admin Panel CSV export | A B | verified as an optional monitoring and export interface |
| 3D Body Progress compares two scans (Pro) | A B C | verified as: compares two scans the customer selects, by scan ID; 3DLOOK does not link scans to people |
| "Reviewers compare each scan with earlier ones for the same participant" | B | the program links scans to participants; 3DLOOK does not |
| FitXpress is not a medical device | A B C | verified, canonical sentence |
