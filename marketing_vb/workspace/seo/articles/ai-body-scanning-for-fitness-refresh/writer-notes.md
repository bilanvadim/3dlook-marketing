---
slug: ai-body-scanning-for-fitness
workspace: ai-body-scanning-for-fitness-refresh
product: fitxpress
stage: seo-writer
draft: draft-v1-writer.md
date: 2026-11-18
---

# Writer notes: draft-v1-writer.md

## Lint

`python3 scripts/article_lint.py workspace/seo/articles/ai-body-scanning-for-fitness-refresh/draft-v1-writer.md`

- Run 1: FAIL on one gate. The detector flagged `anthropomorphism x1` ("platform wants", S6 bullet). Rewritten as "The scan should appear under the platform's own brand."
- Run 2 and the run after the frontmatter update: **VERDICT: PASS**, all ten gates.
- Prose words 1,954 against a target of 1,950 (band 1,657-2,242).
- Sentences: 133, mean 12.8 words, p90 20, none over 25 words.
- Detector: CLEAN, density 0.0, no soft hits, no house-rule violations.
- Links: 13 total, 9 distinct. Up 1, sideways 5, down 1 (three text CTAs and `#form`), trust 2.
- Claim markers: 33 markers across 21 IDs. Approved but not cited: FXS-GDPR, FXS-HIPAA, and FXS-RETENTION. The plan keeps retention, hosting, and regulatory detail out (FAQ 3 links the trust FAQ).

## CTA placement (share of prose words before the link)

| CTA | Anchor | Position |
|---|---|---|
| 1 | body scanning for fitness apps | 15.1% (S2, after the bullets) |
| 2 | mobile alternative to a gym body scanner | 59.2% (S6 answer paragraph) |
| 3 | body composition tracking for fitness apps | end (S10) |
| Demo | book a demo → `/fitxpress/for-connected-and-digital-fitness/#form` | end (S10) |

The plan estimated CTA 2 at about 53%. It lands at 59% because S3-S5 came out close to budget and S6 slightly under. It is still mid-article.

## Open items for the editor and the publish package

1. **Byline.** The frontmatter author is Assel Sekerova, and the live byline is Dana Vioreanu (2024). This is her call. Flag it in the package.
2. **"3D model" as a per-scan output (S2 bullet 2, S5 paragraph 1).** The plan asks for it. The trace is FXS-LIFECYCLE ("a 3D model" under generated data) and the pack's `company_oneliner`. The FIT-PLAN note says the live /pricing/ page lists no 3D model on Starter. The 3D *features* (3D Body Progress tracking, 3D Goal Visualization) are tied to the Pro plan in S3. The editor should confirm the plain "a 3D model" can stay, or whether it needs a plan qualifier.
3. **ACSM link.** The link goes to ACSM's own release on Newswise (2026-10-20), the source the coordinator verified. I re-read it on 2026-11-18. It confirms:
   - Wearables are No. 1 (the 10th time).
   - Mobile exercise apps rose from No. 4 to No. 2.
   - Data-driven training technology held at No. 8.
   - More than 1,400 fitness professionals took part. They rated "how widely they observed" trends.
   - The release says the ranking "does not establish that a particular product or program is effective."

   `acsm.org/2027-fitness-trends/` returns 403 from the VPS. The publisher can swap to it if it resolves. The text uses ordinals ("ranked first", "from fourth to second", "stayed at eighth") in place of "No. 1". That reads more cleanly and keeps the sentence splitter from cutting at "No.". The text says nothing about body scanning in connection with ACSM.
4. **S7 bullet label changed.** The plan had "A record the platform owns". The draft says "A record inside the platform". Data ownership is a contract and legal-role question (see the FXS-GDPR controller and processor sentence), and the bullet should not imply terms.
5. **S3 lead does not name the four placements.** S2's "Where it sits" bullet already lists them. `editorial-rewrites.md` §2 says to list a set once. The lead is now: "A product team chooses among four placements, and each one changes what the scan is for."
6. **FAQ 1 heading expands DXA.** The heading is the first DXA mention, so gate 8 needs the expansion there. The heading runs 17 words. "DXA (also written DEXA)" sits in the anchor to `ai-body-scanners-vs-dexa-scans/`. The answer opens with the §2.1 sentence verbatim (FIT-EVIDENCE-LIMIT note).
7. **S8 overlap with the landing.** The "comparison cohort" paragraph sits close to the landing's pilot step 2 (random assignment where practical). It is kept to the decision angle and is shorter than the landing. The hypothesis example is framed as "A hypothesis might read: …" so it cannot be read as a result.
8. **FAQ set.** The FAQ uses the plan's three questions only. "What does FitXpress not do?" and the decisioning question are answered in the body: the S2 bullet "What it does not do" and the S5 boundary paragraph ("FitXpress is not a medical device."). The plan says no FAQ answer repeats a body section.
9. **Judgment lines for the editor to check:**
   - "The step matters most in online coaching" (S3). This is the writer's comparative and has no source.
   - "the main alternative to a hardware 3D body scanner is a guided scan inside that app" (S6). This is the AEO answer phrasing.
   - "A lean mass estimate does not measure muscle directly" (S5). This is plan wording and terminology §2.13. There is no separate claim ID; it sits on the FXS-MEDICAL / FXS-SCOPE line.
10. **Repetition hints from gate 10 (not gated):**
    - "a fitness app" x4
    - "the first check-in" x3
    - "the app needs" x3
    - "does not measure" x3
    - "body composition estimates" x3

    These are topic phrases and were left in. The "progress tracking and" and "a cohort test" refrains from run 1 were cut.
11. **"customer"** appears only inside the verbatim §5 repeatability sentence ("real-world customer dataset"). The word is not used as an audience label anywhere.
12. **Headings** are taken from the plan, in sentence case, with no content-plan labels. S3, S6, and S7 are question-shaped H2s by plan decision (AEO prompts 565780358696 and 565540613659), although `blog-style-guide.md` prefers declarative headings.

## Deviations from the plan, by section

| Section | Plan words | Draft words (lint) | Note |
|---|---|---|---|
| 1 Opening (with H1 and cover concept) | 110 | ~150 incl. H1 and concept line | Prose itself is about 98 words |
| 2 Short answer | 160 | 169 | `ai body scan fitness app` used once, in the lead-in |
| 3 Member journey | 260 | 248 | Lead changed (item 5) |
| 4 Retention | 240 | 253 | FIT-ACSM used with its note; the limit reads "None of these sources tested body scans." |
| 5 Outputs and boundary | 250 | 268 | §5 short forms verbatim, with the framework link in both figure paragraphs |
| 6 Alternative to hardware | 320 | 279 | Three H3s; the limit for progress photos is its own bullet |
| 7 What to look for | 190 | 187 | Label changed (item 4) |
| 8 Cohort test | 210 | 179 | |
| 9 FAQ | 170 | 185 | |
| 10 Next steps | 40 | 38 | Two sentences; the second starts with "Then" |

## Inputs and rules applied

- The draft follows `plan.md` (approved). Per the writer prompt, `plan-audit.md` was not read. The coordinator's notes on its open items 1-2 were applied: all FIT-* IDs resolve in `approved_claims`, and FIT-ACSM is used with its note.
- I read `refresh-gap-analysis.md` and `published-live-2026-11-18.md`. None of the live sentences, numbers (>10% market growth, 28%, 53%, 71%, Stanford 2021, PMC6238835), competitor names, MRI or exercise-form claims, or homepage links were carried over.
- There are no client names, no competitor or device-maker names, no prices, no plan request counts, no pilot length, and no retake figures.
- There is no `essential fat`, `beneficial fat`, or `body composition values`. "Body composition estimates" is used throughout. BMI and BMR are called calculated metrics. "BMI comes from height and weight and does not measure body fat." fixes the live-page defect.
- Abbreviations are expanded at first use: SDK, API, BMR, BIA, DXA, and ACSM. The GLP-1 abbreviation is not used; the GLP-1 article is linked as "muscle loss questions in fitness apps". "Real-Time Pose Validation" is written in full.
- "Published: June 12, 2024" is kept as `published: 2024-06-12` in the frontmatter only. The publisher sets "Updated".
- Visuals: `(Cover) - Concept` under the H1 and `(Image 1) - Concept` after the S3 placements, as in the plan's visuals table.
