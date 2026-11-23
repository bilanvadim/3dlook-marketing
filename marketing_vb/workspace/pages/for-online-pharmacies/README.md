---
product: fitxpress
type: handoff-readme
vertical: online-pharmacies
status: gate-not-taken-75
date: 2026-11-23
---

# FitXpress for online pharmacies: handoff

> **Gate not taken: 75/85 after 3 blind rounds (73, 71, 75), weakest axis Sales argument. Publishing requires Vadim's
> explicit decision.** Fixes made after round 3 (claims accuracy, schema, length) were not re-scored.
> After round 3, at Vadim's request (2026-11-23), the scan-record block was moved before How it works (value before
> mechanics; this matches round 1's one_fix), and the scan was added as an option during or straight after an online
> consultation. Neither change was re-scored.

A UK-led use-case landing for online pharmacies and digital prescribers that supply weight-loss medication. Angle
(approved by Vadim 2026-11-09): a weight estimate from photos taken live in the order flow, checked by the prescriber
before supplying, with a dated record the pharmacy keeps. Built on the live fitness landing's template, with one
departure Vadim asked for on 2026-11-23 (the scan record before How it works), and kept clear of the BMI verification feature page, the compliance guide and the GLP-1 landing
(non-competition matrix in `gate-reports.md`).

## What is in the box

| File | What it is |
|---|---|
| `page.md` | The copy, block by block, with Yoast fields, visual markers and the JSON-LD. Source of truth for the copy |
| `page.html` | Self-contained prototype of the same copy in the fitness template (CSS from `page-final-2026-10-07.html`, classes namespaced `.fx-op-*`). Open with a double click |
| `wordpress-notes.md` | Yoast fields, schema block, FAQ markup, form embed and anchors, breadcrumb, 301 plan, analytics |
| `TODO.md` | Everything unfinished, blockers first |
| `open-items.md` | Every bent guardrail and every claim waiting for Vadim, product, Whitney, Asel or Katerina |
| `fact-sheet.md` | The source behind every number and named fact, and what was measured versus not |
| `gate-reports.md` | Intake, G-I, G-A, the Phase 3 build record, the non-competition matrix, every judge round and the fixes after it |
| `judge-round-1.json` … `judge-round-3.json` | The three blind-judge rounds, verbatim |
| `screenshot-1280.png`, `screenshot-375.png` | Full-page renders of the final prototype |
| `log.md` | What was done, when and why |

No `assets/` folder: the page uses no new images. Client logos load from the live theme folder
(`/wp-content/themes/3dlook/assets/img/bmi-evidence/trusted/`), and the hero mock is HTML, captioned "Illustrative
example".

## Page structure (value first: the scan record before How it works, Vadim 2026-11-23)

1. Hero: H1, lede, "Book a demo", "See what the prescriber receives →", four-fact strip, order-timeline mock; logo
   row with UK Meds first
2. For patients: four cards, link to the BMI feature page, button "See the patient flow in the demo"
3. The problem: GPhC guidance (quoted), two GPhC review figures, scope sentence, link to the compliance guide
4. The scan record (`#record`): five tiles, boundary sentence, button "See a sample record in the demo"
5. How it works: three steps (checkout, re-order or an online consultation · RTPV capture · PMR / prescriber
   dashboard / order management), recommended setup, "Book a demo"
6. Comparison: FitXpress in the order flow compared with manually reviewed evidence (cards under 960 px), button "See
   the order flow in the demo"
7. Accuracy and data handling: 3.5% weight-estimate figure (open item), method and population limitation, five data
   lines, trust-FAQ link
8. Pilot and pricing: Starter and Pro from the live `/pricing/`, three steps, tracking list, "Book a demo"
9. FAQ: four questions (FAQPage schema), related-pages line
10. Form (`#demo`, alias `#form`): shared HubSpot form `FX | LP | Demo`

Visible copy: 1,596 words. Detector (`detect-ai-tells.py --channel page`): CLEAN.

## Yoast

| Field | Value |
|---|---|
| SEO title | `Order-Flow Weight Checks for Online Pharmacies \| FitXpress` (58) |
| Meta description | `Weight checks for online pharmacies: FitXpress adds a weight estimate from photos taken live at checkout, for the prescriber to review before supplying.` (152) |
| Focus keyphrase | `weight checks for online pharmacies` (title and meta; not in the lede, open item 16d) |
| Canonical | `https://3dlook.ai/for-online-pharmacies/` (self) |
| Breadcrumb | Home → FitXpress for Online Pharmacies |

Both differ from the BMI feature page's and the compliance guide's title and description.

## Tokens

All from `DESIGN.md` through the approved fitness prototype: Satoshi, `#143DFF` single accent, navy `#050F40` bands
with the radial glow, radius 5 / 15 / 20 / 40 px, spacing from the scale, focus ring `#B1BDFF`. Page-specific
additions: a smaller hero H1 size (the H1 is longer than the fitness one), the order-timeline mock, a 3 + 2 tile grid,
and 12 px captions raised from `#808080` to `#666` for contrast (5.74:1).

## Blind judge: three rounds, gate not taken

| Axis | Weight | Round 1 | Round 2 | Round 3 |
|---|---|---|---|---|
| Proof of belonging to the vertical | 15 | 11 | 11 | 12 |
| Claims discipline | 15 | 12 | 12 | 12 |
| Sales argument | 15 | 9 | 11 | 11 |
| Uniqueness against the parent | 10 | 8 | 7 | 7 |
| Conversion | 10 | 8 | 6 | 8 |
| Copy in the buyer's language | 10 | 8 | 7 | 8 |
| Human copy | 10 | 7 | 7 | 7 |
| Search and AI visibility | 10 | 7 | 7 | 7 |
| Place in the site and technical layer | 5 | 3 | 3 | 3 |
| **Total** | **100** | **73** | **71** | **75** |

Where round 3 lost points, in short: the H1 states the product, not the paid-for outcome; the problem block opened
with regulation (fixed after round 3, unscored); the GPhC paraphrase had dropped "independently" (fixed after round 3,
unscored); overlap risk with the BMI feature page and the compliance guide (inherent to the vertical); about 2,500 px
without a button across the accuracy block; US spelling and USD prices on a UK page; brand-phrased FAQ headings;
siblings as a text line; performance, analytics and a keyboard tab-through not verified. Full text in
`judge-round-3.json`.

## What was skipped, in writing

- **Cases and a customer quote** (Kit slots 10 and 11): standing FX waiver, logos only; UK Meds is not named in the
  copy.
- **Sibling-vertical cards** (slot 16): the fitness template has none; two sibling links sit in the body and a
  related-pages line.
- **Block order:** the live fitness order (How it works before the record) was kept through the three judge rounds as
  Vadim's template requirement; after round 3 Vadim asked for the record first (value before mechanics). The live
  fitness page still has the opposite order; the same change could be proposed there.
- **Not measured:** performance, 1440 px, a full keyboard tab-through, validator.schema.org, analytics firing.
- **Not on the page by decision:** liveness (coming soon outside the BMI page), Clothing Detector (Q4), MHRA and CQC
  (not in canon sources), GBP prices (none published), body measurements and composition (GLP-1 and fitness
  territory).
