---
qc_date: 2026-11-06
agent: post-drafter
artifact: workspace/social/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/twitter-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Rewrite fixed the no-position problem (15→18/20); the remaining overlap with instagram-company's sentence shape is a pack-level dedup note, not worth a third rewrite round.
---

# QC Report — post-drafter — twitter-company — 2026-11-06

**Total: 18/20** — excellent (re-check, borderline with good — see E notes)

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Content type matches the brief's "Short POV on industry trend" bucket, CTA matches "link in reply," 0 hashtags, 265/280 chars is inside the hard budget.
- Brief tone is explicitly "Punchy, **data-first**." The post carries no number at all, not even the article's own stat — it stays qualitative ("fat mass, lean mass, or fluid"). That's a defensible choice for a POV tweet, but it leaves "data-first" half-unaddressed, and spelling out "glucagon-like peptide-1 (GLP-1)" burns ~25 of the 265 characters on an expansion the target audience (industry commentary readers who already know the term) doesn't need — works against "punchy." Soft length target was 240-260; actual is 265, inside the hard wall but past the aim.

### C. Brand & tone — 3/3
- No banned words, no em dash, no triple parallelism, no AI-tell constructions. Clean.

### E. Output quality — 3/4
- **Position:** present, and this is the actual fix from the 15/20 version. The post now runs assumption → correction: *"A dropping number on glucagon-like peptide-1 (GLP-1) looks like a win."* sets up a presumed success, then *"The scale can't tell whether fat mass, lean mass, or fluid made up the change."* undercuts it, then *"Put measurements, composition estimates and training history on one timeline"* tells the reader what to do instead. That is a stance (don't trust the falling number at face value), not a recap of the article's premise. It clears the bar the previous version failed.
- Where it falls short of a 4: the corrective sentence is close to verbatim restatement of `post_meta`'s **Claims used** line rather than an industry-commentary framing with teeth (e.g., naming who gets this wrong, or why it matters commercially) — it reads as "here is the fact" dressed with a setup sentence, not as an opinion a person would defend. And the opening clause ("A dropping number on glucagon-like peptide-1 (GLP-1)") is a slightly awkward construction that a 5-minute pass would tighten before posting (e.g., "A falling number during a GLP-1 program looks like a win").
- **Angle distinctness:** directionally distinct from `facebook-company` (which ends on a question, broader-audience framing) and from the LinkedIn personal angles (which go to buyer-trust/market framing). It overlaps more than it should with `instagram-company`'s core sentence: this post's *"Put measurements, composition estimates and training history on one timeline"* is structurally the same list-of-three-on-one-timeline construction as Instagram's *"weight, waist, body composition and strength training on one timeline, each labeled by source."* Different platform, same sentence shape and same payload — acceptable since both draw from the same article fact, but worth flagging since twitter-company's job is specifically "the sharpest single-tweet hook," and a hook that's one clause away from the Instagram caption is not maximally distinct.

## Top issue for `post-drafter`

When the fix for "no position" is a setup-then-correction structure, make sure the correction sentence is rewritten in the profile's own words rather than lifted close to verbatim from `post_meta`'s Claims used line — restating a claim precisely is not the same as taking a position on it.
