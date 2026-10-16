---
product: fitxpress
type: vertical-page
vertical: bariatric
status: review
source: Nika's draft (Slack #marketing, 2026-10-15) + Asselya's chat-edited version (same thread)
---

# Gate reports: bariatric landing, review of Nika's draft (2026-10-16)

Inputs: `nika-draft-2026-10-15.html` (Nika, thread 1792072808.121969 in #marketing, "how accurately do I
hit the clinics' pain?") and `asselya-updated-2026-10-15.html` (Asselya's ChatGPT pass, 17 edits, same
thread). Text extracts: the `.txt` files beside them.

## Decisions by Vadim (2026-10-16)

1. **Post-op follow-up is the primary pain, pre-qualification is secondary.** «пост оп можливо сильніша
   біль для клінік ніж прекваліфікацію тому акцент на ній». This confirms Nika's angle and overrides the
   keyword map's primary (`bariatric pre-authorization documentation`, landing-keywords §7, built on a
   HubSpot AEO recommendation). The keyword-map row and `fx-bariatric-pre-auth.md` need a follow-up
   section; until then the landing's primary keyword is an open item.
2. **Pricing is moving to requests instead of scans.** «прайсінг наразі міняємо на реквести замість
   сканів». Asselya's edit 15 ("500 / 1,000 API requests") stands. The live `/pricing/` still says
   "Up to 500 scans per month" on 2026-10-16, so the page ships together with the pricing update, or the
   tier lines are re-read on the day it ships.

## G-I · should the page exist: PASS with the standing FX waiver

- Use-case file: `brand-assets/product-info/use-cases/fx-bariatric-pre-auth.md`. It covers
  pre-qualification and pre-auth only; post-op follow-up (now the primary job) is not in it. Add it.
- Cases: `G-I: standing FX waiver 2026-09-27` (no bariatric client; logos only).
- Demand: content-plan Hub 6; keyword map §7 says all Google demand is patient-side (YMYL), clinic-side
  demand exists only as GEO / AI-assistant prompts (AEO visibility 0%, 6%, 62%).
- Facts not on the parent: prior authorization, the surgeon consultation slot, the pre-surgery baseline,
  BIA / DXA as protocol methods, lean mass after surgery, follow-up schedule and coordinators. No named
  standard or body (ASMBS, MBSAQIP, NICE, CMS), so proof of belonging stays thin.
- BD owner: not asked. The UK bariatric campaign (2026-09-27, Katerina) got the objection "It's an app to
  calculate BMI from a photo?" from a bariatric surgeon, which the page should answer.

## G-A · architecture: OPEN (two decisions for Vadim)

- **URL.** The draft's canonical is `/fitxpress/for-bariatric-programs/`; `landing-map.md` and the
  keyword map say `/fitxpress/for-bariatric-clinics/`. The GLP-1 precedent (2026-10-07) kept the
  landing-map slug. "Programs" covers hospital programs and clinics alike, so either works; pick one and
  update `landing-map.md`.
- **Cannibalisation with the hub.** Draft title "Bariatric Follow-Up and Pre-Qualification | FitXpress"
  vs hub title "Bariatric Pre-Qualification and Patient Progress Tracking: …". The keyword map gives
  "bariatric pre-qualification" to the hub. With the post-op decision the landing title should lead with
  follow-up and drop "Pre-Qualification" from the title.
- Inbound links: the hub links to `/for-bmi-verification/` today (landing-map "Link now"); relink when
  this page is live. GSC baseline: new URL, none.

## Mechanical checks

| Check | Nika | Asselya | Rule |
|---|---|---|---|
| Visible words (kit count: no mocks, no form, comparison once) | 2,135 | 2,134 | 1,100-1,600; >1,700 = article's job |
| Visible words incl. mocks | 2,552 | 2,550 | |
| you/your per 1,000 | 11.7 | 10.8 | ≤ 12.5 |
| FAQ | 7 | 7 | 4-6 |
| Detector `--channel page` AI density | 0.0 | 0.36 | budget 6.0 |
| Detector hard fails | 7 en dashes in ranges | 8 | ranges with hyphens (`accuracy-formulations.md`: "96-97%", "1.5-2.0 cm") |
| "ID" unexpanded | no | "scan IDs" x3 | "identifiers" (register) |
| H1 count | 1 | 1 | 1 |
| Yoast title / description | 53 / 144 | 55 / 146 | ≤ 60 / ≤ 155 |
| Schema | WebPage, Service, FAQPage (7), BreadcrumbList (2 levels) | same | Service lacks `areaServed` |
| Form | contact-page form id, comment says swap to shared `FX \| LP \| Demo` | same | shared form at `#demo` |
| Hero at 1280×800 | fits (CTA bottom 703 px) | not rendered | |
| 375 px | no horizontal scroll, comparison → cards, CTA in first screen | not rendered | |

## Kit order vs the fitness final (structure benchmark)

Nika: hero → logos → **problem → value cards** → follow-up block (mock) → pre-qualification block
(mock) → outputs (6 cards) → how it works → comparison → accuracy + data → pilot + price → FAQ (7) →
form. Kit: value cards before the problem; one "What you get" table with a "what it changes" column; a
question H2 on accuracy with the answer first. The two job blocks with mocks are extra to the kit and
carry most of the length.

## G-J · blind judge, round 1 (2026-10-16): gate not taken

| Version | Total | Lowest | Hard fails |
|---|---|---|---|
| Nika (`judge-round-1-nika.json`) | 54 / 100 | sales_argument 5/15 | "validated" in an FAQ H3 (guardrail #3); boundary twice + chained negation (M2); logo `[PLACEHOLDER]` comment |
| Asselya (`judge-round-1-asselya.json`) | 53 / 100 | sales_argument 5/15 | boundary twice + chained negation; logo placeholder (the judge missed the same "validated" H3) |

No further rounds: this is a review of the team's draft, not a build. The fixes go to Nika
(`review-2026-10-16-nika-ru.md`); a rebuild by the pipeline only on Vadim's request.

## G-A closed (2026-10-16, Vadim: «головний ключ подивись в ахревс… на основі фінальний н1 і урл… щоб з хабом хоть пересікалось»)

- **Focus keyphrase `bariatric patient tracking`** (Ahrefs US 10/month, CPC $0.60). Every `bariatric
  follow up` variant is 0; pre-auth phrases have no row at all. The phrase overlaps the hub title
  "…Patient Progress Tracking" without taking its head term. Table and reasoning:
  `keywords-ahrefs-2026-10-16.md`.
- **URL `/fitxpress/for-bariatric-programs/`.** No keyword favours "clinics"; "programs" is the actor the
  page writes about and matches `/fitxpress/for-glp-1-programs/`. Nothing linked to the old planned URL.
  The folder was renamed to match; `landing-map.md`, the keyword map §7 and the tracking spec row
  (`fx_vertical = bariatric`) were updated.
- **H1:** "FitXpress for bariatric patient tracking: body data at every follow-up between clinic visits".
  **Title:** "Bariatric Patient Tracking Between Visits | FitXpress" (53). Compliance note: "patient
  tracking" names the program's use; the copy says the program links scan identifiers to patients.

## v2 build (2026-10-16, Vadim: «давай зберемо штмл сторінку з врахуванням всіх коментарів»)

`page-v2-2026-10-16.html` (built by script on Nika's fx-bar template: her CSS, logos, two mocks and the
form/tracking script reused), `page-v2-2026-10-16.md` (visible copy), `fact-sheet-v2.md`.

- Order per the fitness final: hero → logos → value cards for patients → problem (question H2, MBSAQIP +
  NICE, 3 sourced numbers) → record table (5 rows, output | what it changes) + chart mock → pre-qualification
  block + queue mock → how it works → comparison → accuracy + data → pilot + price → FAQ (4) → form.
- 1,621 visible words (kit count, screen-reader caption excluded); Vadim 2026-10-16: «1900 теж норм».
- Detector: density 0.44/1000, no hard fails; you/your 0 in copy (2 in the form text); no en or em dashes.
- All of Asselya's edits except the H1; all review items (sections 3 and 6 of the review) applied.
- Not used: the Smart Scales weight-error figure (Nika's note: contested internally) → open item.
- Placeholders: remaining client logos; API entered-weight limit (40-200 kg vs validation 38-210 kg).

## G-J · v2 blind judges: gate not taken, 71 / 85 after three rounds

| Round | Total | Lowest | Hard fails | Fixed after the round |
|---|---|---|---|---|
| 1 (`judge-round-1-v2.json`) | 71 | sales_argument 9/15 | logo and API-limit placeholders | H1 with a hedged outcome, Smart Scales "(beta)", FAQ as H3, problem close states the cost, comparison conclusion, figurative phrasing, `fx_vertical = bariatric` |
| 2 (`judge-round-2-v2.json`) | 71 | sales_argument 9/15 | logo placeholder; API-request units vs live `/pricing/`; API weight limit sourced outside `proof-points.md` | 4-row comparison with the distance conclusion, shorter problem block, EHR named, FAQ without body repeats, API limit moved to TODO, internal head comment removed |
| 3 (`judge-round-3-v2.json`) | 71 | conversion 6/10 | logo placeholder (design handoff) | without rescoring: fat/lean wording, CTA after the comparison, "patient app or portal", FAQ openings |

Nika's original scored 54. What still holds v2 below 85 is outside the copy: no bariatric client or case
(proof of belonging), the hub article sharing the topic family (uniqueness), the contact-page form and
unverified events (conversion), the parent `/fitxpress/` not being live (place). Final: 1,715 visible
words (Vadim 2026-10-16: up to 1,900 is fine), detector 0.0/1000, 4 FAQ, schema WebPage + Service with
`areaServed` + FAQPage + BreadcrumbList. HTML rebuilt by `build-v2.py` from the source HTML.
