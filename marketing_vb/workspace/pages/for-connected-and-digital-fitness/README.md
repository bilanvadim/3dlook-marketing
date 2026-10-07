---
product: fitxpress
type: handoff-readme
vertical: connected-and-digital-fitness
status: final (Vadim, 2026-10-07), passed to design; product checks P1-P3 open
date: 2026-10-07
---

# Handoff: FitXpress for connected and digital fitness

A rewrite in place of the live page `/fitxpress/for-connected-and-digital-fitness/`, built from Nika's
draft through the page-builder kit, with Asselya's register rules of 2026-10-02 applied.

## What is in the box

| File | What it is |
|---|---|
| `page-final-2026-10-07.html` | **Final (Vadim, 2026-10-07: "the latest and the most correct")**: Drive "fitxpress-connected-fitness-merged-2026-10-07.html", v3 merged with the team's fixes from "final (2)" and the fitness logos. The source of truth; the kit's structure benchmark |
| `page-final-2026-10-07.md` | Text transcript of the final, block by block, with the Yoast fields. If it differs from the HTML, the HTML wins |
| `page-v3-2026-10-06.md` | v3, superseded by the final, block by block, with Yoast fields and layout notes; built from Nika's 10-06 iteration under the kit's "Sell, not educate" rules |
| `page-v3-2026-10-06.html` | v3 prototype, superseded, rendered from the v3 copy on Nika's template (Satoshi, `DESIGN.md` tokens), schema included |
| `nika-final-2026-10-06.html` / `.md` | Nika's iteration (Drive, 10-06) and its text transcript |
| `review-2026-10-06-nika.md` | Review of Nika's iteration: what v3 kept, 24 fixes (Ukrainian) |
| `page.md` / `page.html` | v2 (2026-10-02), superseded |
| `review-2026-10-02-nika.md` | Review of Nika's draft: 23 fixes, what was kept, the 2-pager notes (Ukrainian) |
| `fact-sheet.md` | The source behind every figure and statement |
| `gate-reports.md` | G-I (standing FX waiver), G-A with the Search Console baseline, dropped slots |
| `open-items.md` | Product checks P1-P3 and four detector/canon spots M1-M4 in the final, then the older questions |
| `TODO.md` | Blockers, build steps, post-launch checks |
| `judge-round-N.json` | Blind-judge rounds |
| `log.md` | Run log |

## The page in one line

A commercial page for connected-fitness platforms and fitness and coaching apps: members see measured body
change at the first check-in, and the platform gets a body scan without hardware, priced from $1,000 a
month with no integration fee.

## The final

What changed against v3: a new H1 ("A mobile gym body scanner alternative for fitness apps"), value cards
for members before the problem, Zing Coach and verv logos, the safer capture wording (RTPV "gives pose and
framing guidance"; the record lists "Processing status and timestamps"), the platform linking scan IDs, an
encryption data line and the privacy contact, one line per price tier, a randomised comparison cohort with
an evaluate step, two new FAQ (results delivery with the API documentation link, scan frequency), the
comparison as cards on mobile. About 1,560 visible words, 6 FAQ, "you / your" 2.6 per 1,000. Not re-judged.
The rules it settled are in `kit-vertical-page.md`, "Fitness final".

## Blind judge

**v3 (2026-10-06, 100-point scale with the new Sales argument axis): 69 → 71 → 73 / 85. Gate not taken;
weakest axis = `place_and_technical`.** Round 1 had one hard fail ("validated capture"), fixed. What holds
it below 85: the G-T items only a WordPress build can measure, no fitness logo or figure (standing FX
waiver), and shared accuracy, data and pricing blocks. Details in `gate-reports.md`.

v2 (2026-10-02, old 105-point table): three rounds, three fresh judges: **71 → 73 → 76 / 85, no hard fails. Gate not taken; weakest axis =
`proof_of_belonging`.** What holds it below 85 is mostly outside the copy: no approved fitness case or
logo (standing FX waiver), the G-T items that only a WordPress build can measure (analytics, contrast,
768/1440), and the Kit's shared accuracy and data blocks, which judges count as boilerplate. Vadim decides
whether it ships at 76 (`gates-and-scorecard.md`: no silent publishing below 85).

## Placement

URL unchanged (`/fitxpress/for-connected-and-digital-fitness/`), canonical to self, parent `/fitxpress/`,
primary keyword `gym body scanner`. Hub article: `ai-in-fitness-industry`. The landing-map row is already
`live`, so no relink is needed.

## Not done here

The WordPress build, image production, Rich Results validation and the analytics check (G-T), and
anything about the 2-pager and the deck beyond the notes in the review.
