---
qc_date: 2026-09-21
agent: post-drafter
artifact: workspace/social/articles/2026-08-31-ai-body-data-wellness-platforms-hub/instagram-company/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: closing line is a generalized maxim ("progress you can see tends to be progress people stick with") standing in for a specific claim — same angle-overlap issue as twitter-company, compounded by a templated repeated sentence shape.
---

# QC Report — post-drafter — instagram-company — 2026-09-21

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
- Hook works exactly as briefed: "The scale said nothing changed. Your body said otherwise." is two short sentences, visible before "see more", human and not corporate.
- Content type matches "Key stat turned into visual story" and pairs with the Design tip's two-3D-models image; CTA is exactly the brief's approved pair ("Save this post" / "Link in bio").
- Minor: the brief says avoid "занадто технічні деталі" — "two smartphone photos, one front and one side, in under 45 seconds. No gym, no special hardware, no clinic visit" is capture-mechanics detail rather than pure outcome framing. It stays accessible (no API-talk, no jargon), so this is a soft miss, not a violation.
- Checked against the source article (`published-live-2026-09-21.md`, lines 23 and 39): the eight-week / waist / chest-and-shoulders framing and the "in under 45 seconds" figure (line 110) are both quoted correctly with the subject intact — no quantifier drift.

### C. Brand & tone — 2/3
- Repeated construction "It just doesn't show up on a scale" / "It just can't tell you where the change happened" — the same sentence shape used twice in a 148-word post reads as templated rather than written, the kind of rhythm `lint`'s `ai-tells:house_rule` warning ("uniform paragraph length: every block the same size") is picking up on mechanically. It's a real style issue even though it isn't a hard fail.
- "Progress you can see tends to be progress people stick with" is a closing maxim/aphorism — the pattern `editorial-rewrites.md` flags as an editor cut, not a banned word but a recognizable AI-tell shape (generalized truism standing in for a specific claim).
- No banned words, no em dash, no clickbait — otherwise clean.

### E. Output quality — 3/4
- **Position:** the post does take a stance, not just report a fact. "This is where a body scan earns its place." and "Weight is still a useful trend. It just can't tell you where the change happened." both judge which metric matters and why, rather than only describing what the product does.
- **Angle distinctness:** weak versus `twitter-company`, whose sibling angle is "scale weight can stay flat while the waist moves, and a second scan turns a baseline into a comparison you can act on" — nearly the same mechanism and the same "scale is flat, scan finds it" spine as this post. The instagram post differentiates mainly through the visual specificity ("two 3D models side by side") and second-person coaching voice, which is enough to justify the format but not enough to call the underlying claim distinct — this is the same core idea as twitter and (to a lesser extent) facebook, restated for a visual caption rather than a genuinely different angle on the article.

## Top issue for `post-drafter`

When the pack's angle map gives several profiles the same "scale is flat, scan shows the real change" mechanism, push the visual profile (instagram) to lead with something the mechanism alone doesn't carry — e.g. the felt experience of checking in, not a restatement of the baseline/follow-up logic already assigned to twitter — and drop the closing maxim in favor of a specific, non-generalized last line.
