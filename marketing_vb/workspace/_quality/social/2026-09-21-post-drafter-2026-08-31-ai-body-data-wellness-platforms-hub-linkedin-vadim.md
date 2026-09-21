---
qc_date: 2026-09-21
agent: post-drafter
artifact: workspace/social/articles/2026-08-31-ai-body-data-wellness-platforms-hub/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: three stacked "X, not Y" corrective-negation constructions in one short post — terminology-guardrails.md bans the pattern outright outside a narrow boundary exception; worth a prompt tweak so post-drafter self-checks for repeats of its own opening rhetorical device.
---

# QC Report — post-drafter — linkedin-vadim — 2026-09-21

**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Hook is a claim, not a question: "Most bad progress data comes from the capture step, not the algorithm." Matches the brief's "hook is a claim not a question."
- No location announced anywhere, no "who I speak with daily" line — brief's two hard prohibitions for personal profiles both cleanly avoided.
- Closes on a question requiring the reader's own number, exactly as specified: "If you've deployed at-home scanning, what's your retake rate looking like?"
- Teaches one concrete, product-shaped thing — treat guided capture (pose check, fast retake) as a feature, not an afterthought — and stays on that single point instead of drifting into a second idea.
- 159 words per lint (166 per `post_meta`, discrepancy immaterial — both inside 100-170), avg 9.9 words/sentence, longest 22 — well inside "short sentences, none over 30."

### C. Brand & tone — 2/3
- The post stacks three "X, not Y" corrective-negation constructions in 159 words: "not the algorithm" (line 1), "measuring the room, not the body" (paragraph 3), and "a feature, not an afterthought" (paragraph 5). `terminology-guardrails.md` Part 1 bans this pattern outright except for a single narrow product/regulatory-boundary exception, which none of these three uses are. Lint's `ai_density_per_1000_words: 11.56` (severity: medium) is consistent with this — it's a repeated rhetorical tic lint doesn't gate as a hard fail because it isn't a fixed banned phrase, but three instances in one short post is a real, judged lapse, not a one-off.
- "So I'd treat capture guidance as a feature, not an afterthought" also uses "So" to introduce a conclusion/recommendation, which the guardrails prefer rephrased ("which can reduce…", "allowing…") — a second, smaller instance of the same family of issue in the same sentence as the third corrective negation.
- Everything else is clean: no banned words (leverage/utilize/harness/etc.), no em dash, no hashtags, no emoji-flood, voice reads as a practitioner's own observation ("Here's the failure mode I'd watch for") rather than marketing copy.

### E. Output quality — 4/4
- **Position:** clearly present, twice. "The fix isn't a better model. It's a guided capture flow... Boring, operational, and it's what makes a two-scan comparison mean anything" — a specific, arguable claim about where the fix belongs. And "So I'd treat capture guidance as a feature, not an afterthought" — a first-person recommendation, not a neutral recap of the article. This post does not read as compiled; it judges.
- **Angle distinctness:** the core teaching — capture inconsistency, not the model, breaks a two-scan comparison, and the fix is a guided capture flow — is distinct from all eight sibling angles. Closest neighbor is `linkedin-nick` ("the metric that predicts a program is working is the second-scan rate, not accuracy"), and this post's closing question ("what's your retake rate looking like?") brushes the same retake/second-scan territory Nick's angle owns. But the body of the post never makes retake-rate-as-leading-indicator its point the way Nick's does — it stays on capture conditions and the guided-flow fix throughout, with the retake mention arriving only in the CTA. Distinct enough; worth a light watch if this pack runs again with a different closing question for Vadim.

## Top issue for `post-drafter`

When a post opens with one "X, not Y" hook, check the rest of the draft for repeats of the same construction before finalizing — this one used it three times, and `terminology-guardrails.md` bans the pattern outright except for a single narrow product-boundary case.
