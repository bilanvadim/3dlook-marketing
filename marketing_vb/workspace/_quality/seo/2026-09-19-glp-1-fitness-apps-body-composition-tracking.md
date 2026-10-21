# QC: 2026-09-19-glp-1-fitness-apps-body-composition-tracking (revision 3, Review 2 round)

Total: 16/20 (Good). Verdict: approve with minor fixes (ship with notes).

Reviewer: seo-qc (sonnet), input from `scripts/article_package.py qc-prompt`, 2026-10-21. The agent could
not overwrite the revision 2 report (Write-only, file existed); the coordinator saved its report here
verbatim in substance. The revision 2 report is in git (commit 93c4d79).

B and D are taken from the code verdicts (lint FAIL only on the accepted M1 gate for GLP-1 in the H1;
detector 0.0/1000; checklist 17/17; 1,820 words incl. concept lines). A, C and E are judgment.

| Category | Score | Max |
|---|---|---|
| A. Plan and intent | 4 | 5 |
| B. Facts (from code) | 5 | 5 |
| C. Voice, readability, argument | 2 | 3 |
| D. Format (from code) | 2 | 3 |
| E. Position and value | 3 | 4 |

## A. Plan and intent: 4/5
All seven outline sections are present and in order. Section 2 does not deliver its H2 promise "what a
scan cannot determine": those limits moved to Section 5.

## B. Facts: 5/5
Accepted from the code verdict.

## C. Voice, readability, argument: 2/3
The through-line holds: weight does not say what changed; label sources; do not assign a cause. The
middle reads as assembled from approved lines.

## D. Format: 2/3
Checklist 17/17. One point off for the lint FAIL on M1 (GLP-1 in the H1), the accepted known failure.

## E. Position and value: 3/4
The article has a position; about 10 minutes of edits. Detector 0.0/1000 (≤ 25% threshold met).

## Top findings
1. "The scan does not measure muscle" repeats four times before Section 5: the short answer, the scope
   note ("its lean mass estimate is not a measurement of muscle"), the end of Section 2, and the table
   cell ("lean mass is not muscle mass"); again in the FAQ and Section 5. The scope note carries three
   disclaimers in one paragraph. Keep one strong place plus the FAQ.
2. The bridge into the 34K point does not follow: "Before an app commits to periodic check-ins at that
   scale, it needs to know whether its own members come back for repeat scans." Another platform's
   scale says nothing about this app's members. Also the join "approximately 96-97%" straight into "not
   validated accuracy for lean mass". Add connective sentences around locked lines, do not touch them.
3. Section 2 is unfinished and the pilot is thin. The Neeland ranges ("40% to 60%" vs "approximately 15%
   or less") come without a conclusion for app design; add one sentence on what the spread means for
   the display. The pilot reduces to "sets in advance the repeat-completion level"; name 2-3 metrics
   with an example threshold form. Weak line: "An app that offers workouts can support one part of that
   guidance."

## What works
- "A weight chart alone leaves that training record disconnected from body-change data."
- The "second record made by a different method" idea for DXA/BIA.
- The "alternative path" block for members who cannot use standard capture.
- The disagreement paragraph: "weight falls and the waist measurement stays the same".

Minor: the "(Cover) - Concept" line sits inside Section 1; check it is stripped at publication.

## for_agent_improver
1. Editor: add connectives around verbatim claim lines. Merge "scan does not measure muscle" repeats
   into the scope note and FAQ.
2. Outliner/writer: place "what a scan cannot determine" in Section 2, as the plan promises, and draw a
   conclusion from the 40-60% vs 15% spread.
3. Writer: give the pilot 2-3 named metrics and an example threshold form instead of "set in advance".

## coordinator_review

```
agreement: ✅ agree (16/20 is fair; same score as revision 2, but the Review 2 asks are now in: concrete progress-view table with sources, disagreement paragraph, short answer at the top, reviewer's H1)
top_issue: Section 2 lost its "what a scan cannot determine" sentence when review-2-decisions §2 allowed cutting the repeat; finding 3a fixed in the editor's QC fix pass (one sentence drawing the conclusion from the Neeland spread). Declined: finding 1 (the short answer, scope note and table cell are reviewer-mandated or locked); finding 2 (the 34K bridge came from the revision 2 QC fix pass, and it states what the app must check about its own members); finding 3b (no approved numbers exist for pilot thresholds; inventing them breaks claims discipline); the "workouts" sentence stays.
```
