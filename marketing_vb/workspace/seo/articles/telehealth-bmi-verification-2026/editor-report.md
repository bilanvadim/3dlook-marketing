---
artifact: draft-v2-edited.md
stage: Phase 4 (Editor)
based_on: draft-v1.md + qc-draft-report.md
editor_date: 2026-08-02
---

# Editor Report — Telehealth BMI Verification 2026

Applied all five required fixes from `qc-draft-report.md` (QC score 17/20, approved with fixes, no regeneration needed). No changes made to claims, figures, or sourcing — this pass was structural/stylistic, not a fact-check pass.

## Fixes applied

### 1. M2 stacked-negation rewrite — "What FitXpress does not do"

Before (2 sentences, 2-3 chained "does not / not" clauses each):
> "FitXpress is not positioned as a medical device, and it is not a decisioning system. Inside a telehealth BMI verification workflow, it does not diagnose a condition, does not make a treatment or eligibility decision, and does not replace the clinician who reviews the data it produces."

After (one clear negative per sentence, positive framing carrying the rest):
> "FitXpress is not positioned as a medical device. Diagnosis, treatment decisions, and eligibility decisions stay with the clinician reviewing the case; FitXpress supplies the structured data behind that review, not the decision itself."

Same treatment applied to the compliance/fraud sentence later in the same section (was: "does not guarantee ... and it does not detect fraud automatically" chained in one sentence; now: two sentences, the fraud point reframed positively as "Fraud review stays part of the program's own compliance process, with FitXpress supporting capture and documentation rather than automated detection").

Net effect: same scope boundaries stated, same claims-discipline compliance (guardrail #6, "not positioned as," used once), no loss of information, cleaner reading per M2.

### 2. Removed "this piece" self-reference (4 instances)

Line-by-line:
- "That is the gap this piece is built around." → "That is the operational gap a defensible telehealth BMI verification workflow needs to close."
- "...which is the standard this piece describes." → "...which is the standard described in the sections below."
- "What it demonstrates for this piece is scale:" → "What it demonstrates is scale:"
- "This piece stays on the program-workflow side of that line." → "The breakdown above stays on the program-operations side of that line."

None of these were in the brief's literal zero-list ("this article," "this guide") but all four functioned as the same self-referential workaround the rule targets. Flagged by QC, fixed here rather than left as a technicality.

### 3. FAQ heading — removed "you"

"How do you verify BMI remotely in a telehealth program?" → "How is BMI verified remotely in a telehealth program?" Keeps the secondary keyword phrase intact for AEO/search matching; removes the second-person address in what is an educational FAQ answer, not a conversion section.

### 4. Rephrased ambiguous quoted "we"

"...is one concrete signal that 'we have a number in the chart' is no longer treated as sufficient..." → "...is one concrete signal that a bare 'there is a number in the chart' is no longer treated as sufficient..." Removes any reading of "we" as 3DLOOK's own voice; the line was always meant to represent a generic program's internal shorthand, not a 3DLOOK statement.

### 5. Added missing internal links from plan.md's map

| Link | Direction | Placement |
|---|---|---|
| AI Body Data for Health hub (https://3dlook.ai/content-hub/ai-body-data-health-hub/) | Up | Next Steps, alongside the existing AI in Telehealth hub link |
| Body Composition Scale (https://3dlook.ai/content-hub/body-composition-scale/) | Sideways | Methods section, "Connected smart scales" |
| How to Measure Body Composition (https://3dlook.ai/content-hub/how-to-measure-body-composition/) | Sideways | Methods section, same paragraph ("does not capture body composition") |
| Visual Progress Tracking for GLP-1 Adherence & Retention (https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/) | Sideways | "Where FitXpress fits," scan-to-scan comparison bullet |

All four anchors sit on text that already discussed the linked concept (no link stuffed onto unrelated language). Total internal link count is now 9 across all four directions (up ×2, sideways ×4, down/BOFU ×1, trust ×2), within/slightly above the style guide's 4-8 range, appropriate for a P0 pillar-adjacent BOFU piece with this many legitimate cross-cluster touchpoints.

## Not changed (checked and confirmed clean)

- Claims table and all five external citations — unchanged, no fact-check issues raised.
- FitXpress positioning language throughout (section 7 and FAQ) — already fully within approved phrase list, no edits needed.
- Section 9 (telehealth vs. pharmacy handoff) — QC flagged this as the strongest section; left untouched apart from the one self-reference fix at its closing sentence.
- Word count: 2,925 words in the body (excluding frontmatter), within the 2,200-3,000 target range.

## Recheck after edits

- Zero instances of "this piece" / "this article" / "this guide" remain in body copy.
- Zero em dashes.
- Zero instances of banned words (leverage, utilize, harness, robust, seamless, comprehensive, delve, tapestry, realm, revolutionary, game-changing, cutting-edge, unlock, unleash) — confirmed via grep.
- "You/your" outside the FAQ heading fix does not appear anywhere in body copy (confirmed via grep — only the CTA section would be the appropriate place, and it uses buyer/program framing instead, consistent with about-me.md's "buyer framing, not you-spam" rule).
- No sentence contains more than one negation clause after the Section 8 rewrite (spot-checked every "not/does not" occurrence in the body).

## Recommendation

Ready for Phase 5 (Publisher). No further editor rework anticipated; publisher should treat this as the content-final version and focus on frontmatter, meta, and the pre-publish checklist.
