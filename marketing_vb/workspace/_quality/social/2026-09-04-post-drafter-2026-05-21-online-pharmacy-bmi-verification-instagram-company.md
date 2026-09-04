---
qc_date: 2026-09-04
agent: post-drafter
artifact: workspace/social/articles/2026-05-21-online-pharmacy-bmi-verification/instagram-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
lint: pass
coordinator_review: |
  agreement: ✅ agree — article scopes the claim to UK pharmacies only (UK teams, GPhC, "a leading UK online pharmacy"); post generalized to "online pharmacies" globally.
  top_issue: Fixed post-QC — "online pharmacies" changed to "UK online pharmacies" in the drafter's one-line correction pass; re-lint PASS, no other changes.
---

# QC Report — post-drafter — instagram-company — 2026-09-04

**Total: 16/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 3 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Hook, length (982 chars, within 600-1000), CTA ("Link in bio"), and design-tip alignment all match the `instagram-company` brief precisely. The human-anecdote angle ("Our CEO asked ChatGPT to make her look 27 kg heavier") is exactly the content type the brief asks for ("Human outcome from the article", "Less corporate, more brand").
- One step past the brief's "avoid: занадто технічні деталі... jargon": the paragraph "online pharmacies are moving BMI verification into live, in-session capture. Photos taken inside the flow, camera roll disabled, with pose and liveness checks" shifts from the personal narrative into a workflow/feature list. Not jargon-heavy, but it's the least "visual storytelling" sentence in the post and reads more like the LinkedIn angle than an Instagram caption.

### B. Factual accuracy — 3/5
- Lint passed with no hard fails; the specific claims checked against the article (27 kg, ChatGPT widened the body/kept the face, Gemini altered the face/produced a more plausible body, "did not test whether those images would pass a pharmacy's clinical review", camera roll disabled, live in-session capture, pose/liveness checks, "under 45 seconds") all match the source verbatim or in close paraphrase — this is genuinely clean transcription.
- One scope quantifier is lost, the kind lint cannot catch: "This is why **online pharmacies** are moving BMI verification into live, in-session capture" generalizes a claim the article scopes to **UK** pharmacies specifically. The article opens with "In conversations with **UK** online pharmacy teams..." and the regulatory driver it cites (GPhC) is a UK-only regulator; the one concrete customer proof point is "a leading **UK** online pharmacy runs it as the BMI verification step in its checkout today." Nothing in the article supports "online pharmacies" as an unqualified, global industry movement. This is the same failure pattern as dropping "firms with 5,000+ workers" down to "employers" — the number/fact is real, its boundary is not carried over.

### C. Brand & tone — 3/3
- No em dash, no banned words (leverage/utilize/harness/seamless/etc.), no hashtags, no emoji (matches lint: 0/0). No "not just X, it's Y" or triple-parallel constructions. "The fix is quieter than it sounds" is a stylistic flourish but not on the banned list and doesn't read as AI-signature filler — it's followed by a concrete claim, not a vague tail.
- "Our CEO" / "our" is a legitimate ownership claim (referring to 3DLOOK's own CEO), consistent with CLAUDE.md's judgment rule on we/our.

## E. Output quality — 3/4
- **Position:** the post takes a real stance, not just a recap. "She never tested whether those images would clear a pharmacy's clinical review. She didn't need to. The point landed anyway: when weight-loss eligibility rests on a self-reported number and a photo pulled from the camera roll, that evidence says little about when, how, or by whom the image was made." — this is a judgment about what the experiment proves, not a restatement of it. The closing line, "The fix is quieter than it sounds: capture the evidence live, where it can be audited end to end," is also a stated position (the solution is procedural, not dramatic), not a slogan.
- **Angle distinctness:** clearly distinct from `linkedin-katya`'s procurement-question/buying-behaviour angle — this post is a visual, human-story angle built around the CEO's experiment, with no overlap in framing or evidence used.
- Held to 3/4 rather than 4/4 because the unqualified "online pharmacies are moving..." line (see B) needs a light edit — either scope it to UK or soften it to match what the article actually supports — before this is publish-ready as-is.

## Top issue for `post-drafter`

When a post generalizes a source claim into a shorter industry-level statement, it must carry over the article's scope qualifiers (geography, regulator, "one customer" vs. "the industry"), not just its numbers — this pack lost "UK" the same way other packs have lost numeric thresholds.
