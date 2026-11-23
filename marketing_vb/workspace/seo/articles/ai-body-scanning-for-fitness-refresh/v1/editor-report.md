---
slug: ai-body-scanning-for-fitness
workspace: ai-body-scanning-for-fitness-refresh
product: fitxpress
stage: seo-editor
input: draft-v1-writer.md
output: final.md
date: 2026-11-18
verdict: PASS (article_lint, 10/10 gates)
---

# Editor report: ai-body-scanning-for-fitness (refresh in place)

## Gates on final.md

`python3 scripts/article_lint.py workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md`, **VERDICT: PASS**, all ten gates.

| Measure | Writer draft | Final |
|---|---|---|
| Prose words (target 1,950, band 1,657-2,242) | 1,954 | 2,068 |
| Sentences / mean words / p90 | 133 / 12.8 / 20 | 139 / 13.1 / 20 |
| Over 25 / over 35 words | 0 / 0 | 0 / 0 |
| Detector (`--channel article`) | CLEAN, 0.0 | CLEAN, 0.0, no soft markers |
| Rhythm variation | 0.42 | 0.46 |
| Links: up / side / down / trust | 1 / 5 / 1 / 2 | 1 / 5 / 1 / 2 |
| Landing CTAs (share of prose before the link) | 15% / 59% / end | 15.4% / 60.0% / end, demo `#form` |
| Claim IDs cited | 21 | 20 (FXS-LIFECYCLE dropped with the 3D model line) |

The draft also passed every gate. The editing work was judgment: fixing the 3D-model claim, hedging unsupported lines, removing repeats, and breaking up the template structure.

## QC fix pass (2026-11-18, QC 17/20)

The QC report is `workspace/_quality/seo/2026-11-18-ai-body-scanning-for-fitness-refresh.md`. The coordinator asked for items 1-5.

1. **S7 evidence bullet, claims ambiguity.** It now reads: "FitXpress publishes its figures for body measurements: accuracy against expert pattern-maker tape measurements, and scan-to-scan repeatability. Its composition estimates are derived from those measurements." FIT-OUTPUTS-NOTE is added to the markers.
2. **S7 answer.** It now reads: "FitXpress by 3DLOOK captures two smartphone photos inside the app through the FitXpress SDK. The API then delivers 80+ body measurements and body composition estimates to the app." There is no superiority claim.
3. **S6 opening.** The answer now covers any studio: the scan runs in the studio's app or on its website, per the FIT-SDK web SDK. It states what the scan returns and drops the "hardware-free … no extra hardware" repeat. The H3 is now "A phone scan fits when".
4. **Landing echoes.** Claim IDs are unchanged.
   - The coach review no longer says "the same record"; the coach checks the change between two of the member's scans.
   - The S6 bullet now reads "reviews scan results remotely".
   - The S3 white-label close and the S7 SDK / recommended-setup sentences are reworded.
   - S8 now argues why the comparison group and a pre-set threshold matter (season, campaign, another release). It no longer restates the landing's pilot steps.
   - The onboarding-completion point is kept once (the S3 trade-off) and cut from S8.
   - A 7-word n-gram check against `published-live-2026-11-13.md` now finds only canonical claim text: capture conditions, Pro plan feature names, output names, the NDA line, and FIT-OUTPUTS-NOTE.
5. **Premium tier.** A hedged outcome line is added: "A cohort test can also show whether those views change how many members upgrade."

Also fixed: the S3 actor is now consistently "the product team" (QC C, actor drift).

QC items not addressed in this pass (outside the 1-5 brief), now open items:
- The ACSM paragraph's last two sentences state a difference without a product-team consequence.
- The publish-package meta description differs from `meta_description` in final.md.
- The package CTA positions and word count are stale. Use 15.4% / 60.0% / end and 2,068 words.
- The hub's "seven in ten users… stop using a fitness app" framing differs from this page's Kidman wording.

## Fix pass after the package STOP (2026-11-18)

`article_package.py assemble` stopped on `boundary_section` and `scope_note_early`. Changes:

- Added a bold-label scope note after the intro, before the short answer. It sits at body line 12, inside the check's 40-line window, in the editorial-rewrites §7 shape. The text, verbatim: "**Scope note.** The scope is body scanning in fitness and coaching apps: member check-ins, progress views, and coach review. FitXpress is not a medical device. Interpretation of results and training decisions stay with the app and its coaches. The scan does not diagnose or assess health risk."
- Removed the S2 bullet "What it does not do" (S2 now has four bullets) and the S5 boundary paragraph. The boundary is now stated once, in the scope note, and "FitXpress is not a medical device." appears once.
- The scope note avoids "this article": the detector fails it everywhere, scope notes included.
- Gates after the fix: lint PASS (10 of 10), 1,992 prose words, mean 13.1, 0 sentences over 25, detector CLEAN at 0.0.
- I did not run `article_package.py` or any link check against 3dlook.ai. The package's 40-line scope-note test was reproduced locally on final.md and returns True.
- Plan deviation: the plan said "no scope note; the medical-device line once in Section 5". The coordinator's fix overrides that.

## Coordinator decisions applied

1. **3D model.** The plain "a 3D model" is gone from the S2 output bullet and from the S5 output paragraph. The base output list is now 80+ body measurements, body composition estimates, and BMI/BMR as calculated metrics. 3D appears only as "3D Body Progress tracking and 3D Goal Visualization are features of the FitXpress Pro plan" (S3, FIT-PLAN). The Image 1 concept marks the 3D progress view as a Pro plan feature, and the cover concept now says "flat body silhouettes".
2. **ACSM.** The Newswise link and the professional-survey framing stay. The ranking "reflects how widely more than 1,400 fitness professionals observe each trend, and it does not report usage."
3. **"A record inside the platform."** Kept.
4. **S3 opening.** Kept.
5. **FAQ 1 heading.** The 17-word heading is now "Is a phone body scan the same as a DXA scan?" (10 words). DXA is expanded at its first body use, in the S7 bullet "Evidence with its reference": "…such as expert tape measurement or dual-energy X-ray absorptiometry (DXA)…". Gate 8 passes.
6. **S8.** The four bold-label paragraphs are now three short prose paragraphs (about 120 words), focused on the decisions. They no longer mirror the landing's step layout. One change of substance: the test now fixes **one baseline placement**. In the draft, "test one placement, onboarding or the first check-in" sat next to a hypothesis that needed scans at both points.
7. **Judgment lines.**
   - "matters most in online coaching" is now a description: the coach may never meet the member, and the record gives the coach a view of body change.
   - "the main alternative" is now "a hardware-free alternative". It carries no ranking or market-share claim.
   - The lean mass line is now a limit of the estimates: "Lean mass is one of those estimates, and it is not a direct measure of muscle." It moved into the evidence-limits paragraph.

The three landing CTAs, the absence of competitor and client names, the verbatim §5 accuracy wording with the framework link in the same paragraph, "FitXpress is not a medical device." stated directly, and the Assel Sekerova byline (still an open item) are all unchanged.

## What else changed (by pass)

- **Pass 1, citations.** Adjust, JMIR, and ACSM/Newswise each appear once. The accuracy framework is linked twice on purpose, once from each figure paragraph (repeatability, accuracy). accuracy-formulations §3.2 asks for this, and so does your "link in the same paragraph" rule. This is the one exception to dedup.
- **Pass 2, flow.** The S4 H2 is now hedged: "How visible progress may affect fitness app retention". Its earlier wording stated a finding, while the section's own limit is that no source tested body scans (editorial-rewrites §4). The S8 lead repeated the intro's cohort-test sentence and was cut. The link sentences no longer all read "X covers Y".
- **Pass 3, voice.**
  - Added one expert trade-off in S3: a baseline at onboarding vs at the first check-in.
  - Added two stated positions: separate trend lines per method (S6), and fallback-path results reported separately (S8).
  - The tape-measure claim is hedged ("usually need a second person").
  - The boundary paragraph uses positive scoping: "Interpreting a change for the member stays with the app and its coaches."
- **Pass 3c.** Pass 1 introduced "The platform decides", an anthropomorphism hard fail. It now reads "The product team decides". The self-check is in the final.md frontmatter.
- **Pass 3d, repetition.**
  - The capture-conditions list now appears once (S3), and S8 refers to it.
  - Reduced: "inside the app" x3, "come back" x2, "calculated … calculated", "onboarding, onboarding", and "a fitness app" from 4 to 3.
  - Gate hints still printed: "the first check-in" x3 and "body composition estimates" x3. Both are topic phrases and stay.
- **Pass 4.**
  - M1: the FAQ 3 anchor "…FAQ" is now "FitXpress data, privacy, and security answers", removing the bare abbreviation.
  - Banned words: none.
  - M2: there is one negation per sentence.
  - Numbers: all traced to `approved_claims`.
  - Primary keyword: in the H1 and the S2 H2.

## Guardrails audit

| Rule | Result |
|---|---|
| #1 substantiation | pass: unsourced comparatives hedged or removed |
| #2 one number everywhere | pass |
| #3 reserved words | pass: only in the §1.9 disclaimer |
| #4 bare percentages | pass |
| #5 caveats | pass: Adjust read as app users, Kidman as a median, ACSM as a survey, "None of these sources tested body scans." |
| #6 medical framing | pass: "FitXpress is not a medical device." |
| #7 conditional equivalence | pass: FAQ 1, the guardrail sentence verbatim |
| #8 diligence register | pass |
| #9 reframe | pass: as a statement (intro, S5) |
| #10 structure | pass |
| #11 flag, don't decide | see the open items below |
| M1 abbreviations | pass: SDK, API, BMR, ACSM, BIA, and DXA expanded; BMI and iOS bare; "IDs" kept bare inside the verbatim compliance sentence |
| M2 stacked negation | pass |
| M3 terminology pass | pass, with one judgment flag (item 2 below) |

## Open items for the publish package

These are defects or decisions I found but did not resolve, plus deliberate deviations someone has to sign off.

1. **Byline.** The frontmatter names Assel Sekerova; the live byline is Dana Vioreanu (2024). This is her call.
2. **Adjust source is on a vendor's blog** (`adjust.com/blog/…`). Terminology §1.3 says to avoid vendor blogs. Adjust is a mobile-measurement company, not a competitor, and this is its own benchmark data. FIT-ADJUST is approved in the pack and the landing uses the same source, so it stays. Asselya should confirm, or replace it with a neutral source carrying the same figures.
3. **ACSM link** goes to ACSM's release on Newswise. If `https://www.acsm.org/2027-fitness-trends/` resolves at publish (it returns 403 from the VPS), the publisher may swap to it. The text does not change.
4. **Two links to the accuracy framework** in consecutive S5 paragraphs. This is deliberate (see Pass 1). If Asselya prefers one, drop the link from the accuracy paragraph, as her 2026-09-11 final did.
5. **DXA is first expanded in S7**, as an example reference method ("expert tape measurement or dual-energy X-ray absorptiometry (DXA)"), so that FAQ 1 can carry a short heading. Asselya should confirm the example reads right. The next sentence makes clear that FitXpress's figures are tied to tape measurement.
6. **S8 is in prose, without bold labels**, at about 130 words against the plan's 210. The total length (2,068) stays inside the band.
7. **Pilot design differs from the landing.** The article recommends fixing one baseline placement per test. The landing's pilot step 2 has one cohort scan "at onboarding and the first check-in". The two are compatible (the landing's version is the onboarding-baseline case) but can read as different advice. Align the wording if Asselya sees a conflict.
8. **The S4 H2 differs from the plan**: "How visible progress may affect fitness app retention". This does not affect the meta title or description.
9. **Re-check at publish:** `/fitxpress/for-connected-and-digital-fitness/` returns 200 and the `#form` anchor exists (verified 2026-11-18).
10. **Post-publish internal links** (refresh-gap-analysis §6, not the editor's job):
    - Add a down-link from the hub `ai-in-fitness-industry`.
    - Add a link from `glp-1-muscle-loss-fitness-apps`.
    - Update the old-title anchor on `remote-body-measurement-online-fitness-coaching` to the new H1.

## Inputs

I read `draft-v1-writer.md`, `writer-notes.md`, `plan.md`, `refresh-gap-analysis.md`, the context pack, the live landing snapshot (`workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-13.md`, for the overlap check), and the canon files: terminology-guardrails (full pass), hard-bans-card, editorial-guardrails, editorial-rewrites, accuracy-formulations, compliance, ai-tells-sweep, landing-map, content-strategy-guidelines §8/9/11/14/15, about-me, and the relevant parts of blog-style-guide. I did not read `plan-audit.md`: the seo-editor prompt routes it to the publisher and to people, not to the editor.
