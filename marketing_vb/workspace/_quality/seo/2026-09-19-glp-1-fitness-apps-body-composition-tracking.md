# QC: 2026-09-19-glp-1-fitness-apps-body-composition-tracking (revision 2)

Total: 16/20 (Good). Verdict: ship with notes.

B and D are taken from the code verdicts (lint FAIL only on the accepted M1 gate for GLP-1 in the H1 and on word count 1749 against a target of 1600 when concept notes are included; detector 0.0/1000; checklist 17/17). A, C and E are my judgment.

| Category | Score | Max |
|---|---|---|
| A. Plan and intent | 4 | 5 |
| B. Facts (from code) | 5 | 5 |
| C. Voice, readability, argument | 2 | 3 |
| D. Format (from code) | 2 | 3 |
| E. Position and value | 3 | 4 |

## A. Plan and intent: 4/5
All seven outline sections are present and in order. The MOFU intent holds: the CTA is an evaluation link, not a demo button. The vertical boundary holds, with no dosing, no drug names and no muscle assessment.
- Section 2 does what it promised. "A body scan cannot settle what this research leaves open about muscle" closes the evidence section on the limit.
- Section 4's five parts (baseline, cadence, capture conditions, review of differences, alternative path) match the plan's "comparable check-ins" promise.
- Section 5 carries more than its title says. "Where FitXpress fits, and what to test in a pilot" holds the product description, the privacy roles, the repeatability and accuracy figures, the DXA guardrail and the 34K case. The "what to test in a pilot" part is a single closing paragraph. The plan's second half is underweight.

## C. Voice, readability, argument: 2/3
Sections 1 to 4 have a clear through-line: the scale number is ambiguous, the evidence is unsettled, so the app labels its data, and check-ins are made comparable. That reads like someone who knows the problem.
- Strong: "The number shows how much weight changed. It does not show whether fat mass, lean mass, or fluid made up the change." This opens plainly and sets up the whole argument.
- Strong: "Scans spaced closer than the change they are meant to show add records without adding information." This is the voice of someone who has thought about cadence.
- Weak: Section 5 reads as assembled. Roughly nine paragraphs run one after another, each a separate locked claim: delivery, T-BODY-PROGRESS, records and privacy, repeatability, accuracy, scope, DXA, 34K. The thread between them is thin. The 34K paragraph is stated and dropped, with no link to the pilot that follows. The editor's self-check already admits this.
- Minor: the Section 1 "Scope note" and the two pointer sentences at the end of the section slow the opening before the argument starts.
- Hedges are present but not smothering. The KFF sentence ("a figure for adults generally, not fitness app members") is an honest limit.

## E. Position and value: 3/4
The page takes a position a template would not: a scan estimate is a labeled model output, not a verdict on fat or muscle, and the app should say so in the UI.
- The three-column table ("What it should avoid concluding") turns a disclaimer into a design rule. A generic page would only list benefits.
- "Where the prescribing provider already records body composition with DXA or BIA, the app's scans form a second record made by a different method. Each record is best read against its own earlier values." This is a practical insight about two records that do not reconcile.
- "Repeat completion matters most, because every comparison depends on members scanning again at the planned interval." A real pilot priority.
- Gap: the pilot paragraph stays abstract. It names no thresholds, no sample, no duration and no decision rule. "Measures the app already records... can be compared with their pre-launch levels" could be written about any feature. The title promises "what to test", and this part is the one a product person would want.

## For agent-improver
for_agent_improver:
1. Editor, locked-copy sections: when a section is more than half locked sentences (here Section 5), write one bridging sentence per join that states why the next claim follows from the previous one, not just a topic repeat. Add a closing sentence that ties the 34K case to what the pilot tests.
2. Writer or planner: give "what to test in a pilot" its own concrete content in the outline (for example, the check-in interval chosen against observed scan-to-scan variation, the repeat-scan completion target, the decision rule for continuing). The outline slot was too generic, so the section came out generic.
3. Editor: the Section 1 scope note and the two pointer sentences delay the argument. Where the hub owns the boundary, keep the scope note to one sentence and move the pointers to Next steps or the relevant later section.

## coordinator_review

```
agreement: ✅ agree (16/20 is fair: sections 1-4 carry the app-team thread; Section 5 is the weakest because ~270 of its words are locked copy the Review 1 decisions required verbatim)
top_issue: Section 5 joins and a thin pilot slot — fixed in the editor's round-3 fix pass (bridge sentence after the 34,000-scan paragraph, two-sentence pilot decision rule, no new numbers); finding 3 (trim the scope note) declined because review-1-decisions.md §6 keeps the scope note verbatim
```

Note for agent-improver: two of the three QC findings trace back to the coordinator's decisions file, not to the writer or editor. Locking many sentences into one section (decisions §4, §5, G3-G5 all landed in Section 5) makes it read as assembled; a decisions file should spread locked copy across sections or leave the editor room for one bridge per join. Also, the decisions file said the reviewer's table needed no fix while row 2 opened with the hard-banned "Let"; the planner caught it.
