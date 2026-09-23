---
qc_date: 2026-09-23
agent: post-drafter
artifact: workspace/social/articles/2026-09-03-manual-vs-digital-intake-occupational-health/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Same underlying claim as linkedin-company's angle, just reframed first-person — not a blocking issue for this pack, but worth watching if it recurs across packs.
---

# QC Report — post-drafter — linkedin-katerina — 2026-09-23

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Rule 3 (no location announced): the post never mentions the UK, and the brief explicitly says "most posts should carry no UK mention at all" — correct choice, not an omission.
- Rule 5 (opening claim, closing question tied to reader's own data): opens with "Enterprise health buyers have stopped asking me one question about measurement" (claim, not a question) and closes with "If you ran your intake data across every site tomorrow, would the numbers agree?" — exactly the required shape.
- Word/sentence mechanics inside brief band (149 words, avg 9.3 words/sentence, longest 17) confirmed by lint; no independent issue found.
- "It is not a medical device, and the clinical call stays with the clinician" tracks the article's scope note ("FitXpress is not a medical device"; "clearance, eligibility, and fitness-for-duty determinations remain with the responsible professionals") without overreach — checked against `published-live-2026-09-21.md`.

### C. Brand & tone — 2/3
- `lint.warnings` flags `ai-tells:house_rule`: "uniform paragraph length: every block the same size." Confirmed reading the post — nine of ten blocks are one or two short declarative sentences with almost identical rhythm ("They used to ask how accurate a body scan is. One number." / "That is a different bar. That shifts the question from precision to governance."). This is a real, machine-catchable-only-partially AI signature: no single sentence is wrong, but the sameness of block size across the whole post reads as generated rather than written. Counts as the one minor lapse the rubric allows before dropping to 2.
- No banned words, no em-dash, no "not just X, it's Y" — otherwise clean.

### E. Output quality — 3/4
- **Position:** the post does take a stand, not just recite facts. "That shifts the question from precision to governance" and "FitXpress is one way to reach that consistency" are judgments about what matters, not neutral description — this clears the E≤2 bar for constating-only posts.
- **Angle distinctness:** the core insight — "the real question is consistency across sites, not a single accuracy number" — is the same idea `linkedin-company`'s sibling angle states almost verbatim ("Measurement consistency across sites, not a single accuracy number, is the real enterprise problem"). The vehicle differs (Katerina frames it as a first-person shift in what buyers ask her; company states it as a third-person business claim), and personal-profile framing is legitimate, but the underlying argument for these two profiles in the same pack is the same claim restated rather than two distinct cuts on the article. Capped at 3/4 for this reason, not for craft — the writing itself is ready to publish as-is.

## Top issue for `post-drafter`

Vary block size across the post (mix one-line beats with a genuine two-to-three-sentence paragraph) — the uniform-paragraph AI-tell the lint house rule caught here is a pattern worth checking for on every personal-profile post, since the 100-170 word ceiling makes short, same-size blocks the path of least resistance.
