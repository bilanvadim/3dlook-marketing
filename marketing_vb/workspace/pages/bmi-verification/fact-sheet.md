---
product: fitxpress
type: feature-page
vertical: bmi-verification
status: review
draft: asselya-v3-2026-10-22
---

# Fact sheet: BMI verification page, Asselya's mockup v3 (2026-10-22)

What the judge cannot see from the copy. Page text: `asselya-v3-2026-10-22.txt`.

## Placement

- Page type: FitXpress **feature page** (one feature, several verticals), not a single-vertical use-case
  page. No Kit exists for feature pages; it is judged against the vertical Kit, adapted (the "proof of
  belonging" axis reads as proof for the feature's buyers: online pharmacies, telehealth, insurers,
  wellness programmes).
- URL: rebuilt in place at `/for-bmi-verification/` (live today, ~990 words, title "FitXpress for Weight &
  BMI verification"). It moves to `/fitxpress/bmi-verification/` with a 301 when `/fitxpress/` ships
  (`/fitxpress/` currently 301s to the homepage). Canonical: not set in the mockup (mockup carries
  `noindex,nofollow`).
- Primary keyword (landing map): "BMI verification"; secondaries "remote BMI verification", "weight and
  BMI verification".
- Sibling pages: the insurance landing `/for-insurance-underwriting/` (live, sells "build and BMI
  evidence" to carriers); the article "Online pharmacy BMI verification: a 2026 compliance guide".

## Technical (mockup state)

- Schema: none in the mockup. The live page ships only WebPage + BreadcrumbList.
- Performance, contrast, 375/768/1280/1440 viewports: not measured in this review.
- Analytics events: not verified (mockup form does not submit). The production page will embed the
  shared HubSpot form `FX | LP | Demo` at `#demo`.
- Yoast title 60 characters, description 154 characters (mockup `<title>` and meta).

## Sources behind every figure on the page

| Figure on the page | Source | Status |
|---|---|---|
| "Results within 45 seconds" | `proof-points.md`: "Under 45 seconds", one public definition "under 45 seconds from the photos to structured results" | traced; wording differs from the canonical form |
| Two guided photos (front + side) | `tech-spec.md` | traced |
| Example: 78.0 kg reported, 84.0 kg predicted, 173 cm, BMI 26.1 / 28.1, +7.7%, 5% threshold; "within" example 80.0 kg, +2.6% | invented illustrative values, labelled "Illustrative data · not a patient record"; arithmetic checked and correct in metric and imperial | illustrative, not a claim |
| BMI = kg ÷ m² | standard formula | fine |
| Weight-estimate accuracy | `proof-points.md` has an approved page wording: "approximately 3.5% mean absolute error under evaluated conditions" | **not on the page**; the page gives no accuracy figure for predicted weight |
| Third-party statistics | none on the page | — |
| Prices | none on the page. Live `/pricing/` (2026-11-05): FitXpress Starter $1,000/month with 500 API requests, Pro $1,500/month with 1,000 | no price signal |

## Clients and logos

- Logo row: Burlington Medical, Verv, MagicFit, Healthyr, Coredirection, under the heading "Selected
  companies using FitXpress". Client logos may be used on the website (Vadim, 2026-10-21).
- **Burlington Medical is a Mobile Tailor customer** (custom-fit radiation aprons), not a FitXpress one.
- The FitXpress client that actually runs BMI verification, UK Meds (online pharmacy), and the weight-loss
  client Yazen are not in the row. No client is named in the copy (allowed: logos only, no case studies).

## Product claims and their status

- Live in-session capture, no camera-roll upload: supported by the published online-pharmacy BMI
  article ("access to the device's camera roll is disabled").
- RTPV "checks positioning before capture can continue" / "requires alignment checks": product has
  confirmed only "gives pose and framing guidance during capture"; the stronger "pauses capture" level is
  an open item with product.
- Clothing Detector "does not automatically request a clothing change or rescan": unconfirmed; the
  approved public wording says it "can prompt corrective action". Open item with product.
- "Prompted-action liveness — Coming soon": not in `tech-spec.md`; no confirmed release.
- Smart Scales: in beta internally; public pages say "Smart Scales" without a beta label (Vadim,
  2026-10-21). Height is an input, not measured by FitXpress (correct).
- "FitXpress is not a medical device": correct fixed language.
- HIPAA/GDPR: page says responsibilities "depend on the parties' roles"; approved lines exist (BAA
  available for qualifying enterprise deployments; customer = controller, 3DLOOK = processor in most
  deployments; photos deleted after processing or within 30 days; encryption in transit and at rest).

## Length

- About 1,300-1,400 words of visible body copy (nav, mock UI and form excluded); 7 FAQ answers.
- Direct address: ~22 "you / your" per 1,000 words (budget 12.5).
