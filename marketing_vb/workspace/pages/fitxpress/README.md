---
product: fitxpress
type: handoff-readme
vertical: all
status: draft-for-judge
date: 2026-09-27
---

# Handoff: FitXpress product page (/fitxpress/)

The new FitXpress product parent on 3dlook.ai (WordPress + Yoast), per Vadim's 2026-09-27 hierarchy
decision: `/fitxpress/` is the FitXpress parent, verticals live at `/fitxpress/for-{vertical}/`, the
homepage becomes the general 3DLOOK products page. Nothing in this pipeline publishes; the developer
builds from this folder.

**State:** gate not taken after 3 rounds (74/85); see Read first. G-T not passed (the page is not built). No
placeholders left in the copy.

## Read first

1. **Gate not taken: 74/85 after 3 blind-judge rounds (70, 68, 74), weakest axis = Proof of belonging.**
   Post-round-3 fixes are applied but unscored.
2. **The proof lever is a cleared anonymised FitXpress deployment figure** (`open-items.md` A18). No
   `proof-points.md` row can go on the page today without identifying a logo'd client. This is the
   decision that moves the score most.
3. **Design/technical and Place-in-site axes can only be scored after the page is built.** The planned
   build is in `fact-sheet.md`; nothing is measured yet.

## What is in the box

| File | What it is |
|---|---|
| `page.md` | Page copy in order, visual markers inline |
| `fact-sheet.md` | Source file and line for every figure and client name; what was not measured. For the judge |
| `gate-reports.md` | Kit substitution and slot map, G-I (n/a), G-A with GSC baseline and cannibalisation split, G-T state, detector runs, humanisation log |
| `open-items.md` | 21 decisions to confirm and 10 canon contradictions found |
| `TODO.md` | Blockers first |
| `wordpress-notes.md` | Yoast fields, full JSON-LD, FAQ markup, components, alt text, analytics events |
| `log.md` | Run log |
| `assets/` | Not created: no images were produced |

## Kit substitution (stated, per the skill)

There is no product-page Kit. The page was built from `references/kit-vertical-page.md` and adapted:
vertical context (slot 4), vertical cases (10) and quote (11) were dropped; H1, hero proof, pains,
workflow and FAQ were adapted to a cross-vertical parent; the outputs table, the industries grid (the
parent's in-body link down to all eight verticals) and a separate pricing section were invented. Full
slot map in `gate-reports.md`.

## Page structure

1. Breadcrumbs: Home → FitXpress
2. Hero: H1 "FitXpress AI body scanner: body measurements your health program can act on", spec row, Book a demo, logo strip (UK Meds, Yazen, Healthyr)
3. Why programs stop trusting self-reported body data
4. What FitXpress returns from one scan (outputs table, §2.13 categories)
5. How a scan works (6 steps; RTPV, Clothing Detector, timing canon)
6. Where FitXpress is used (8 industry cards linking down)
7. How FitXpress fits into your product (API, web and mobile SDKs, two patterns, optional Admin Panel, access after demo/NDA, docs link)
7a. What you get back and where it goes (payload in words, Admin Panel export, destinations per program)
8. Accurate enough for which decision? (four conditions, repeatability, 96-97% / 1.5-2.0 cm scoped, population scope, disability limitation, DXA/BIA boundary)
9. Data privacy, security and regulatory status (verbatim `compliance.md` table, "FitXpress is not a medical device.", link to trust FAQ)
10. What FitXpress costs (Starter, link to `/pricing/`)
11. FAQ, 12 questions (FAQPage)
12. Closing: Book a demo + one soft alternative (accuracy framework)

~1,800 words of prose (~2,600 including tables and cards). Detector: CLEAN. Sentence mean 11.3 words.

## What was skipped, in writing

- No case studies or quotes (clients refused; logos only).
- No anonymised customer figure (none that would not identify a client; `open-items.md` A4).
- No trial mention, anywhere.
- No IEEE or award strip: the approved IEEE sentences are about retail and add nothing to a health
  product page.
- No comparison block (FitXpress vs in-clinic vs consumer apps): the telehealth page owns it; repeating it
  here would duplicate a child page.
- No HTML prototype, no images, no performance, contrast or viewport measurements.
- Internal link status codes not re-checked.

## Tokens used (`DESIGN.md`)

Satoshi only; navy `#050F40` with radial glow for hero and closing band; `#143DFF` as single accent;
white CTA with dark text on navy; 20px card radius, 15px chips, 4-5px buttons; focus ring `#B1BDFF`
3px / 2px offset; spacing from the 8-step scale; container 1200px. Nothing improvised. Details in
`wordpress-notes.md` §4.
