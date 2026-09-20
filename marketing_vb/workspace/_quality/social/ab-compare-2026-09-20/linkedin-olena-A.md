---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-olena/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-olena — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 3 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Geo discipline is clean: `geo_mentions: 0`, no UK reference, no US-specific regulatory content pulled in even though the article spends a full section on CMS-0057-F (a US payer rule) — the post correctly leaves that out and pulls only the EU-relevant fact (GDPR controller/processor split) from the article's "Privacy and security" section instead.
- Structure matches the personal-profile rules exactly: hook is a ten-word, arguable claim ("Governance stalls remote-scan pilots in obesity care more often than accuracy does."), teaches one concrete thing ("My rule of thumb: write the data-governance answer into the pilot plan before the first scan."), and closes on a question that needs the reader's own program details ("Where does your program draw the line between what a scan captures and what it stores?") rather than a filler "Thoughts?".
- FitXpress is mentioned once, in service of the deletion-policy point ("With FitXpress, photos are deleted immediately after processing…"), not as the center of the post — matches the brief's "enabling technology" instruction.
- 161/170 words, longest sentence 21 words, avg 12.4 — comfortably inside both the house-rule band and the sentence-length rule.

### C. Brand & tone — 3/3
- No inflated-significance filler ("a new era of", "plays a crucial role"), no commitment-tail sentences, no sloganeering close — the last line is a real question, not a wrap-up statement.
- First person is used exactly where the brief wants it ("My rule of thumb…") and nowhere else; the rest stays in a neutral, teaching register appropriate to a BD-Europe voice.
- No banned words, no em dash, no corrective "X, not Y" construction, no triple parallelism.

### E. Output quality — 4/4
- **Position:** "Governance stalls remote-scan pilots in obesity care more often than accuracy does." is a real, arguable claim, not a neutral observation, and the post backs it with a prescriptive stance ("My rule of thumb: write the data-governance answer into the pilot plan before the first scan") rather than just restating article facts.
- **Angle distinctness:** the post's own angle line claims distinctness from GLP-1 / human moment / bottleneck / CMS deadline / provenance / post-op baseline / completion, and the body delivers on that — none of the other listed angles touch GDPR controller/processor roles or photo-deletion timing, so this reads as a genuinely separate cut of the article rather than a restated angle.

## Note on B (not a hard fail, but worth flagging for the next drafter pass)

`lint.hard_fails` and `lint.warnings` are both empty, so B defaults to 5 — except the post drops a quantifier the article states precisely. The post says: "The technology returns a body-data record in seconds." The article's own line, in the "Where FitXpress fits" section, is: "Results typically return in under 45 seconds." Lint has nothing to flag here because no wrong number appears — the specific figure was replaced with a vague "in seconds" rather than misstated, which is exactly the failure mode a number-comparison regex cannot see. It doesn't contradict the source, but it is a precision loss on a claim the article gives a hard number for. B = 3/5 on that basis (judged override, not a lint hard fail).

## Top issue for `post-drafter`

When restating a source claim that carries a specific number (e.g. "under 45 seconds"), keep the number or its stated bound instead of collapsing it into a vague qualitative phrase like "in seconds" — the article gives a precise figure for exactly this claim.
