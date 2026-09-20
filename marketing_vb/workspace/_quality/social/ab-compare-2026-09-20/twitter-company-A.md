---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/twitter-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — twitter-company — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 4 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Content type: brief lists "One striking stat or claim from the article" and "Short POV on industry trend" as separate options; the post fuses both in one tweet (`Bariatric surgery use fell 34.1% as GLP-1 use rose 140.4%…` → `Which number counts, from when, and how was it captured?`) without needing the thread fallback, which fits "Punchy, data-first. One sharp insight… не переказ."
- Length: lint reports 258 chars, inside the brief's tighter 240-260 target, not just under the platform's 280 cap.
- CTA: "Full breakdown of the intake workflow, link in reply." matches the brief's `cta: "Link in bio / article link у відповіді до треду"` mechanism exactly.
- Avoid list respected: no bullet lists, no emoji, no long paragraph, no generic corporate speak (lint: hashtags 0, emoji 0).

### B. Factual accuracy — 4/5 (lint clean; one judged formulation slip)
- The 34.1% / 140.4% / 2022-2024 / JAMA Surgery figures match the article verbatim (`metabolic bariatric surgery use fell 34.1% while … GLP-1 receptor agonist use rose 140.4% (JAMA Surgery, May 13, 2026)`, `Between 2022 and 2024`) — no drift, no subject swap.
- Judged catch lint can't see: the article hedges this claim as a possibility for an individual — "*A patient may therefore arrive* at bariatric intake with a current BMI below an earlier documented value" — while the post states it as a flat, generic plural fact: "Patients arrive at intake with a current BMI below their earlier documented value." This isn't a number-drift or a wrong-subject swap (so not ≤3), but it does convert a hedged, individual "may" into an unqualified claim about "patients" in general, in an article whose register is otherwise carefully hedged throughout (compliance-heavy, "may or may not matter", "typically", etc.). Minor formulation overreach, matches rubric level 4 ("минорная ошибка в позиционировании или формулировке"), not a hallucinated fact.

### C. Brand & tone — 3/3
- No banned-words-checklist hits (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge), no em dash, no "not just X, it's Y" construction.
- Voice is punchy and data-first as specified — leads with the number, closes with a blunt rhetorical question and a one-line verdict, no throat-clearing.

### E. Output quality — 3/4
- **Position:** "That's the documentation problem." names the framing directly — the post doesn't just recite the JAMA stat, it converts it into a specific operational claim ("Which number counts, from when, and how was it captured?"), which lines up with CLAUDE.md §3's mandate to sell workflow/governance rather than a raw stat. This is a real judgment, not a compiled recap.
- **Angle distinctness:** not assessable — this input has no `sibling_angles` field (this run is an A/B comparison of a single profile/slug, not a fan-out pack), so there's nothing to compare the angle against.
- Held to 3 rather than 4 because the hedge-drop noted under B (turning "a patient may arrive" into "Patients arrive") slightly overstates the claim's certainty for a text otherwise ready to publish as-is; a 5-10 min tightening pass ("Some patients arrive…" or keeping "may") would close the gap.

## Top issue for `post-drafter`

When compressing a hedged claim into tweet length, keep the source's modal verb (e.g. "may arrive") instead of flattening it into a generic plural assertion ("Patients arrive…") — the numbers were preserved correctly here, but the certainty was not.
