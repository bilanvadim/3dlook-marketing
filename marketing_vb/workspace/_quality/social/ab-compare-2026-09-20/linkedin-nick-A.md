---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-nick/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-nick — 2026-09-20

**Total: 17/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Hook meets the personal-profile spec exactly: "The weakest part of post-op progress tracking is usually the baseline." — ~12 words, a concrete claim someone could disagree with, not a question or teaser.
- Location discipline holds. `lint.metrics.geo_mentions: 1` is the word "American" inside the organization's proper name ("The American Society for Metabolic and Bariatric Surgery") — a citation, not a targeting announcement. No "For US teams…", no line about who Nick talks to daily (the brief explicitly bans that sentence — "the perspective, never the claim").
- Teaches exactly one thing, stated as a first-person recommendation: "What I'd do: start the structured record at intake, then run the same guided capture after surgery." — not a listicle, not a walk through the article's structure.
- Closing question earns its place: "If your baseline starts at the consultation, how much of the pre-surgery change are you not measuring?" — needs the reader's own numbers, not a "Thoughts?" placeholder.
- FitXpress appears once, naturally, not centered: "FitXpress returns the same field structure at both points…"
- The one place this is executed superficially: personal rule 2 ("Vary the length — a four-word line next to a twenty-word one is rhythm; nine sentences of the same length is a machine") is not followed — see C below. Everything else in the profile brief and the five-personal-profile rules is met, so this is a 4, not a 5.

### C. Brand & tone — 2/3
- `lint.warnings`: `ai-tells:house_rule` — "monotone rhythm: sentence-length variation 0.27 (want >0.35)". Checked the actual sentence lengths: 12, 16, 18, 5, 16, 13, 10, 18, 17, 14, 17 words. Only one short outlier ("That window matters more now.", 5 words) breaks an otherwise tight 10–18-word band across eleven sentences — the machine-tell the personal-profile rule names directly ("nine sentences of the same length is a machine"). Low severity per the lint (`"severity": "low"`), but it is a real, named AI signature, not a restatement of a mechanical check the lint already scores elsewhere.
- No banned words, no em-dash, no clichés, no triple parallelism, no first/third-person mismatch — clean on every other C criterion.

### E. Output quality — 3/4
- **Position:** clearly present — "What I'd do: start the structured record at intake, then run the same guided capture after surgery." This is a stance a reader could push back on (e.g., "why not just start at intake for everyone regardless of GLP-1 use?"), not a recitation of the article's facts.
- **Angle distinctness:** the post's own angle line claims "Untaken lane for this pack (RPM / evidence-generation, not intake or pre-auth)" — plausible against the article, which devotes separate sections to pre-qualification/pre-auth documentation versus post-op progress tracking, and this post draws only from the latter. Caveat: this input did not include a `sibling_angles` list for the pack, so distinctness against the other eight profiles' actual drafts is asserted by the post's own metadata, not independently verified here.
- Held to 3, not 4, because the same monotone-rhythm tell that dings C means this is not fully "as-is": varying two or three sentence lengths is a two-minute fix, not a rewrite, but it is a fix.

## Top issue for `post-drafter`

When a post clears length and structure cleanly, check sentence-length variance before finishing — a run of 10–18-word sentences with only one outlier reads mechanical even at a good average, and the personal-profile brief already states the fix explicitly ("a four-word line next to a twenty-word one is rhythm").
