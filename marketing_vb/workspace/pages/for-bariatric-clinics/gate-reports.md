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
