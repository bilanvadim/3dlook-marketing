---
product: fitxpress
type: feature-page
vertical: bmi-verification
status: review
draft: asselya-v7-2026-11-12
---

# Fact sheet: BMI verification page, Asselya's mockup v7 (2026-11-12)

What the judge cannot see from the copy. Page text: `asselya-v7-2026-11-12.txt`; HTML (links, logos):
`asselya-v7-2026-11-12.html`.

## Role of the page (Vadim, 2026-11-09)

- FitXpress **feature page**: it explains how BMI verification works, routes visitors to the use-case
  landings that sell, and holds keywords. It is not a selling landing: pilot and pricing belong to the
  use-case landings; one pricing line and a demo form are enough here.
- URL: rebuilt in place at `/for-bmi-verification/`. Moves to `/fitxpress/bmi-verification/` with a 301 when
  `/fitxpress/` ships (`/fitxpress/` currently 301s to the homepage).
- Keywords it holds (GSC 16 months): "fitxpress" (brand; since 2026-08 Google shows only this page for it,
  90-day position 6.1), "bmi verification" (90-day position 6.4), "what is bmi verification" (position ~1-8),
  "fit xpress" / "3dlook fitxpress". Ahrefs adds "telehealth bmi verification methods" (20/month US) and,
  in the UK, "voy bmi verification call" (online clinics verify BMI over a video call). FitXpress must be in
  the title and H1 while `/fitxpress/` does not exist.

## Links on the page (checked 2026-11-16)

| Card / place | Target | HTTP |
|---|---|---|
| Online pharmacies | `/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` (article; a UK pharmacy landing is planned, not built) | 200 |
| Digital health programs | `/structured-body-data-for-telehealth-digital-health-programs/` | 200 |
| Life insurance underwriting | `/for-insurance-underwriting/` (live landing) | 200 |
| Employer and insurer wellness | `/content-hub/ai-body-data-wellness-platforms/` (hub article) | 200 |
| Bariatric programs | `/fitxpress/for-bariatric-programs/` | **404** (landing not published; an article `/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` exists and ranks #1 for "mobile body scanning software remote bmi verification") |
| Weight accuracy | `/content-hub/mobile-body-scanning-accuracy/` | 200 |
| Progress tracking FAQ | `/fitxpress/for-connected-and-digital-fitness/` (live fitness landing) | 200 |
| Privacy | trust FAQ `/content-hub/fitxpress-data-privacy-security-regulatory-faq/`, privacy@3dlook.me | 200 |
| Pricing | `/pricing/` | 200 |
| GLP-1 landing `/fitxpress/for-glp-1-programs/` | not linked | 404 (not published) |
| CDC study | `cdc.gov/pcd/issues/2023/23_0005.htm` | same source the published bariatric article cites |

## Technical (mockup state)

- Schema: none in the mockup. The live page ships WebPage + BreadcrumbList only; plan for production is
  Service + FAQPage + BreadcrumbList.
- Yoast title 60 characters; meta description 160 characters (Google truncates at ~155).
- Mockup carries `noindex,nofollow` (mockup only). Production form: shared HubSpot `FX | LP | Demo` at `#demo`.
- Performance, contrast, viewports: not measured.

## Sources behind every figure on the page

| Figure on the page | Source | Status |
|---|---|---|
| "Under 45 sec" / "Under 45 seconds from the photos to structured results" | `proof-points.md` canonical public wording | traced, canonical |
| "approximately 3.5% mean absolute error under evaluated conditions" | `proof-points.md`, approved page wording since 2026-10-02 | traced, canonical |
| 5.3% vs 8.8% severe obesity, 2020 US survey data | CDC, *Preventing Chronic Disease* 2023 | traced |
| Example 78.0 / 84.0 kg, 173 cm, BMI 26.1 / 28.1, +7.7%, 5% threshold | illustrative, labelled "Illustrative data · not a patient record"; arithmetic correct (checked on v3, same values) | illustrative |
| "100+ clients have used 3DLOOK body scanning since 2016" | `proof-points.md`; "100+ clients" is the only public client count | traced |

## Clients and logos

- Logo row (no heading): UK Meds, Yazen, Knosis Health, Warrior Consultants, BeMap, Healthyr, Burlington
  Medical; caption "100+ clients have used 3DLOOK body scanning since 2016, including online pharmacies."
- The live FitXpress use-case landings (insurance, fitness) carry one shared strip by Vadim's rule
  (2026-11-06, "the same strip on every use case"): BeMap, Burlington Medical, Erakulis, Healthyr, Knosis,
  UK Meds, Warrior Consultants, Yazen. Client logos may be used on the website (Vadim, 2026-10-21).
- Burlington Medical is a Mobile Tailor customer (radiation aprons). UK Meds is the FitXpress client that
  runs BMI verification (online pharmacy); Yazen is a weight-loss FitXpress client. Erakulis is in the
  shared strip but not in this row.

## Product claims and their status (`roadmap.md`, `tech-spec.md`, 2026-11-11)

- Live in-session capture, no camera-roll upload: confirmed (published pharmacy article).
- RTPV: live; approved wording "gives pose and framing guidance during capture".
- Clothing Detector: API release planned Q4 2026, not confirmed; until then only the safer wording
  "identifies clothing conditions that may interfere with capture", no claim about prompting a rescan.
- Prompted-action liveness ("anti-fraud live human validation", iOS/Android SDK): ready for release; Vadim
  2026-11-11: it will be live before this page ships. Rule: keep "Coming soon" until product confirms the
  release; at publication, if released, describe it as available.
- Smart Scales: public pages say "Smart Scales" without a beta label (Vadim, 2026-10-21). Height is an
  input; FitXpress does not measure it.
- Data lines (photos deleted after processing or within 30 days; blurred; face obfuscation; anonymized,
  randomly generated IDs; GDPR controller/processor sentence; encryption in transit and at rest; no training
  on production data without documented authorization): all match `compliance.md` / the live trust FAQ.
  HIPAA/BAA line ("can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an
  executed BAA") exists in canon; not used on this page.
- "FitXpress is not a medical device": fixed language, correct.
- Abbreviations: house rule expands GLP-1, SDK, API at first use; BMI, US, UK are not expanded.

## Length and register

- ~1,400 words incl. mock UI; 5 FAQ answers.
- Detector `--channel page`: no hard bans; AI density 0.7/1,000; direct address 19.5 per 1,000 (budget 12.5);
  soft marker "serve as" ×1.
