---
product: fitxpress
type: fact-sheet
vertical: all
date: 2026-09-27
---

# Fact sheet: /fitxpress/

What a reviewer cannot see from the copy: the source behind every figure and every client name, and
what was measured versus only specified. Line numbers refer to the files as of 2026-09-27.

## Page identity

| | |
|---|---|
| Final URL | `https://3dlook.ai/fitxpress/` |
| Canonical | Self (`https://3dlook.ai/fitxpress/`) |
| Parent | `https://3dlook.ai/` (Home) |
| Breadcrumb | Home → FitXpress (2 levels) |
| Page type | Product page (FitXpress product parent) |
| Indexable | Specified yes. Not verifiable: the URL currently 301s to `/` (checked by curl 2026-09-27) |
| Language | en-US |
| Word count | ~1,800 words of prose; ~2,600 including tables, card text and labels |
| `<h1>` count | 1 |
| Primary action | "Book a demo" (hero and closing section; same action twice) |
| Yoast title | `FitXpress: AI body scanner and body measurement API | 3DLOOK` (60 characters) |
| Yoast description | 146 characters (text in `wordpress-notes.md`) |

## Schema specified

`SoftwareApplication` (with `audience` as `BusinessAudience` + `audienceType`, `areaServed`, `offers`
for the Starter tier), `Organization`, `BreadcrumbList` (2 levels), `FAQPage` with all 12 visible
questions, `WebPage`. JSON-LD is in `wordpress-notes.md`. It parses as valid JSON (checked with
`python3 json.load`) and its FAQ answers were generated from the page text, so they match the visible
copy. **Not validated in Google's Rich Results Test or the Schema.org validator**, because the page is
not published.

## Every number on the page, and where it comes from

| Figure on the page | Where it appears | Source |
|---|---|---|
| 2 / two (guided photos, front and side) | Hero, spec row, workflow step 4, FAQ | `proof-points.md` L51 |
| Under 45 seconds from the photos to structured results | Hero sentence and one FAQ answer only | `proof-points.md` L50 (one public definition, Vadim 2026-09-23) |
| 80+ body measurements | Hero, spec row, outputs table, FAQ ×2 | `proof-points.md` L57 |
| BMI, BMR, body fat %, lean mass, fat mass | Outputs table, FAQ | `proof-points.md` L58; `tech-spec.md` Body composition outputs |
| Typical scan-to-scan differences below 1 cm | Accuracy section | `proof-points.md` L38 ("< 1 cm", publishable repeatability figure). Sentence wording: `accuracy-formulations.md` §5. The "five scans per participant" detail was removed in round 3 because it is not in `proof-points.md` |
| 9+ years of training data; 150,000+ photographs; 30,000+ 3D scans; 430,000+ individual measurements | Accuracy section | `proof-points.md` L65, L66, L67, L68 |
| Approximately 96-97% | Accuracy section, FAQ | `proof-points.md` L19 |
| 1.5-2.0 cm typical absolute error | Accuracy section, FAQ | `proof-points.md` L20 |
| Ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, US and Europe | Accuracy section | `proof-points.md` L69, L71, L70, L73 |
| 30 days (photo retention) | Trust table, FAQ | `proof-points.md` L141 |
| US-West-2, US-East-1 (AWS region names) | Trust table, FAQ | `proof-points.md` L140 |
| SOC 2 (standard name, not a figure) | Trust intro sentence (row cut after round 3) | `proof-points.md` L135 |
| $1,000 per month, up to 500 scans (Starter) | Pricing section, FAQ | Live `https://3dlook.ai/pricing/`, FitXpress tab, fetched 2026-09-27: "Starter $1 000 / month, Up to 500 scans per month". Not from `pricing.md` |
| "Higher tiers add 3D body progress tracking and goal visualization" | Pricing section | Live `/pricing/`, Pro tier feature list, 2026-09-27 |

**Round-3 digit sweep:** every digit on the page was grepped. Remaining numbers: 2, 80+, under 45 seconds, below 1 cm, 96-97%, 1.5-2.0 cm, 16 to 78, 150 to 220 cm, 38 to 210 kg, 9+, 150,000+, 30,000+, 430,000+, 30 days, $1,000, 500, plus names containing digits (SOC 2, US-West-2, US-East-1, 3D, GLP-1, list numbering). All trace to `proof-points.md` or live `/pricing/`. The fitness card's "first 90 days" (use-case file only) and "five scans per participant" were removed.

No anonymised customer figure appears on the page. Aggregate scan volumes exist in `proof-points.md`
but are either company-wide (including Mobile Tailor) or tied to a single FitXpress client, so they
were left off (see `open-items.md`).

## Every client name on the page

| Name | Where | Source and rights |
|---|---|---|
| UK Meds | Logo strip only | `proof-points.md` L87; `case-studies/uk-meds.md`. Logo use approved by Vadim 2026-09-27 (logos only, no metrics, no case card) |
| Yazen | Logo strip only | `proof-points.md` L85; `case-studies/yazen.md`. Same approval |
| Healthyr | Logo strip only | `proof-points.md` L89. **No case-study file exists.** Logo use rests on Vadim's 2026-09-27 instruction; see `open-items.md` |

No client name appears in body copy, FAQ or schema.

## Verbatim canon used (not numbers)

| Statement | Source |
|---|---|
| HIPAA sentence, "where applicable" | `compliance.md` L12 |
| GDPR controller / processor sentence | `compliance.md` L23 |
| SOC 2 status sentence | `compliance.md` L15 |
| "FitXpress is not a medical device." (short form only; the assessment sentence is not on the page, the trust FAQ carries it) | `compliance.md` L16; `editorial-guardrails.md` #6 |
| FDA sentence (full canon wording, FAQ answer only; not in the body) | `compliance.md` L17 |
| Model training sentence, with the qualifier "unless the customer gives explicit, documented authorization" (FAQ; trust-table row cut after round 3) | `compliance.md` L18; `proof-points.md` L145 |
| Random IDs sentence | `compliance.md` L53 |
| Decisions stay with clinicians / underwriters | `compliance.md` L80 (paraphrased, same scope) |
| Industries grid pains | Verbatim or near-verbatim from each `use-cases/fx-*.md` "The pain we remove" (insurance L4, pharmacy L4, telehealth L4, wellness L4, occ health L4, trials L4, bariatric L4, fitness L4) and `audience.md` segment "Core pain" (telehealth, pharmacy) |
| Results block: random scan ID, timestamps in processing logs | `compliance.md` L53, L35 (technical data) |
| Results block: link to the 3D model | `tech-spec.md` L122 ("returns JSON with measurements + 3D model URL") |
| Results block: "standard 3D file format" | `tech-spec.md` L116 ("3D model in standard format"); no format name exists in canon, none is given |
| Results block: destinations per program | `tech-spec.md` Pattern A/B (patient assessment dashboard, checkout verification); `case-studies/uk-meds.md` L23 (audit trail); use-cases: insurance L43 (time-stamped records, structured exports), wellness L45 (audit trail for HR / benefits team), occ health L27, trials L38, bariatric L37 (exports, audit-ready records), fitness L7. Stated as where programs send results, not as integrations 3DLOOK built |
| Real-Time Pose Validation (RTPV) description | `tech-spec.md` L49 |
| Clothing Detector sentence | `tech-spec.md` L58 (verbatim) |
| "web and mobile SDKs, including supported iOS and Android integrations" | `tech-spec.md` L22 (verbatim) |
| Admin Panel "optional, complementary interface for monitoring and exporting results" | `tech-spec.md` L26 |
| Population limitation (disabilities) | `accuracy-formulations.md` L292-294 (§5, first two sentences) |
| "FitXpress is not equivalent to DXA, BIA or a calibrated scale when…" | `editorial-guardrails.md` #7 L47 |
| "Performance outside this scope has not been characterized." | `accuracy-formulations.md` L72 |

## Links on the page

| Direction | Target |
|---|---|
| Up | Breadcrumb to `/` |
| Down (8 verticals) | 3 live vertical pages: `/structured-body-data-for-telehealth-digital-health-programs/`, `/for-bmi-verification/`, `/fitxpress/for-connected-and-digital-fitness/`. 5 live content-hub articles standing in for vertical pages that do not exist yet: insurance, employer wellness, occupational health, clinical trials, bariatric |
| Trust and accuracy | `/content-hub/fitxpress-data-privacy-security-regulatory-faq/` (trust intro, medical-device paragraph, FAQ), `/content-hub/mobile-body-scanning-accuracy/` |
| Conversion | `/pricing/`, "Book a demo" |
| Soft alternative | `/content-hub/mobile-body-scanning-accuracy/` (one link in the closing section) |
| External | `https://docs.fitxpress.3dlook.me` as the API documentation (integration and results sections), dofollow |
| Sibling product parent | `/mobile-tailor/`, one in-body line at the end of the industries section (added after round 3) |

All internal targets were taken from `content-plan.md` "Published assets" and `site-inventory.md`.
**HTTP status of each link was not re-checked** on 2026-09-27 (the site returns 503 on bursts; only
`/`, `/pricing/`, the telehealth page and `/fitxpress/` were fetched).

## What was NOT measured

The page does not exist yet, so none of the following could be verified. Each is unverified, not passed.

- **Performance** (Core Web Vitals, page weight): not measured.
- **Viewports** 375 / 768 / 1280 / 1440: not checked. No prototype was built.
- **Colour contrast**: not measured. The design notes specify `DESIGN.md` tokens (white CTA on navy,
  `#143DFF` accent on white); contrast of the built page is unverified.
- **Keyboard operation** and FAQ accordion behaviour: not verified.
- **Analytics events**: specified in `wordpress-notes.md`, not verified firing.
- **Indexation and sitemap inclusion**: not verifiable until the 301 comes off.
- **Rich-result eligibility** of the JSON-LD: not tested.
- **Logo image assets and alt text rendering**: no assets produced.

## Unresolved placeholders on the page

None. The documentation link points directly at `https://docs.fitxpress.3dlook.me`. A future `/developers/`
page is a TODO item, not a page marker.

## Conversion set-up (specified, not verified)

- One primary action: "Book a demo" (hero, closing band). One soft alternative: the accuracy framework
  article. Price signal: Starter tier with a link to `/pricing/`.
- Demo form: first name, last name, work email, company, consent checkbox, one optional text field.
- Events: `demo_click`, `generate_lead` (`form_name` = `fitxpress_demo`), `docs_click`, `pricing_click`,
  `soft_alt_click`, `vertical_card_click`, `faq_open`.
- **Not verified pre-publish.** No event has been seen firing; the form does not exist yet.

## Planned build (PLANNED, not measured)

Everything in this section is a specification for the developer. None of it has been built, rendered or
measured.

| Area | Plan | Source |
|---|---|---|
| Type | Satoshi only (400/500/600/700), headings sentence case | `DESIGN.md` §3 |
| Colour | `#143DFF` as the single accent (CTAs, links, key numerals), never a large fill; hover `#0F2ECD` | `DESIGN.md` §2 |
| Surfaces | Navy `#050F40` with radial glow and grain for hero and closing band; white content zones | `DESIGN.md` §2 |
| Buttons | Primary on navy: white button, dark text, 4-5px radius; focus ring `#B1BDFF` 3px, 2px offset | `DESIGN.md` §6 |
| Radius | 4-5px buttons and inputs, 15px chips, 20px cards (industries grid), 30-40px large bands | `DESIGN.md` §5 |
| Spacing | Only 2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 60 · 80 · 96 · 120; container 1200px; padding `clamp(24px, 5vw, 80px)` | `DESIGN.md` §4 |
| Mobile | Industries grid: 2 columns desktop, 1 column under 768px, whole card tappable, 44×44px minimum targets. Outputs, results-destination and trust tables scroll horizontally inside their own container; no page-level horizontal scroll at 320px. Body text ≥ 16px | `ux-pass.md` §2, §4 |
| Images | WebP with `srcset`, lazy-loaded below the hero, under 200KB each; hero image preloaded; Satoshi preloaded | `ux-pass.md` §3 |
| Performance target | LCP < 2.5 s on mobile, CLS < 0.1 (targets, not measurements) | Core Web Vitals thresholds |
| Accessibility | Contrast ≥ 4.5:1 body, 3:1 large text; keyboard-operable FAQ accordion with `aria-expanded`; alt text per `wordpress-notes.md` §5 | `ux-pass.md` §1 |
| Viewports to check | 320 / 375 / 768 / 1280 / 1440 | `ux-pass.md` |

### Place in the site (planned)

| Item | Plan |
|---|---|
| Breadcrumb | Home → FitXpress (BreadcrumbList, 2 levels) |
| Canonical | Self: `https://3dlook.ai/fitxpress/` |
| Sitemap | Add to `page-sitemap.xml` once the 301 to `/` is removed |
| Up-link | Homepage FitXpress block → `/fitxpress/`; nav and footer "FitXpress" items → `/fitxpress/` (not yet in place) |
| Down-links | In-body industries grid: 3 vertical pages live today, 5 hub articles standing in until `/fitxpress/for-{vertical}/` pages ship |
| Sibling | `/mobile-tailor/`, the other product parent; one in-body link (industries section) plus nav and homepage |
| Across | Trust FAQ, accuracy framework, `/pricing/`, API documentation |

**Measured so far:** only HTTP status of `/`, `/pricing/`, the telehealth page, `/fitxpress/` (301) and
`/fitxpress` (301) by curl on 2026-09-27. Nothing about the built page is measured.
