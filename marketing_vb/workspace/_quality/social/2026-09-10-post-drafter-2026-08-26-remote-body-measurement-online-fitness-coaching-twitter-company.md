---
qc_date: 2026-09-10
agent: post-drafter
artifact: workspace/social/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/twitter-company/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree — 20/20 is fair; the reframe (flat number vs. capture noise) is a real position and repeatability figure is used correctly and separately from the accuracy benchmark.
  top_issue: none | the monotone-rhythm lint warning is cosmetic at 254 chars, not worth a rewrite round.
---

# QC Report — post-drafter — twitter-company — 2026-09-10

**Total: 20/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Content type matches brief exactly: "One striking stat or claim from the article" — the post is built entirely around the scan-to-scan <1 cm figure, no recap of the article's structure.
- Length: 254 chars, inside the profile's stated 240-260 char band and the lint's 1-280 budget.
- Tone matches "punchy, data-first... industry commentary tone" — three short beats (question, stat, verdict), no bullet list, no paragraph over two sentences, per `avoid: "Long paragraphs, bullet lists..."`.
- CTA matches brief exactly: "Link in bio / article link у відповіді до треду" → post ships with "Soft. Article link in the reply to the tweet."

### C. Brand & tone — 3/3
- No banned words (leverage/utilize/harness/etc.), no em dash, no corrective negation, no hollow tail ("...underscoring our commitment" pattern absent).
- Closer "The coach still makes the call." is a plain declarative, not a slogan — reads as an editorial verdict, not marketing copy.
- One thing worth flagging for the record, not a deduction: lint reports `warning only: monotone rhythm sentence-length variation 0.31 (want >0.35)`. Sentence lengths are actually 8/5/10/10/6 words — the two middle sentences land at the same length, which is what the metric is catching. At this length (5 sentences, 38 words) this reads as a natural constraint of the format rather than a tonal lapse, and it is a warning, not a hard fail.

### E. Output quality — 4/4
- **Position:** "The coach still makes the call." — this is the post's actual claim, not a restatement of the stat above it. It pushes back on the implicit assumption a coach might make (no movement = no progress) and asserts that a sub-1cm delta is not itself a verdict; the scan is evidence, not the decision. That is a judgment, not a constatation.
- **Angle distinctness:** `sibling_angles` is empty for this pack ("none yet"), so there is nothing to differentiate against yet. The angle itself ("is this plateau real, or capture noise") is narrow and specific enough — tied to one row of the article's coaching-stage table — that it is unlikely to collide with a broader company-wide stat pull if one appears later.

## Fact-check against article

Checked `workspace/seo/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/published-live-2026-09-04.md` because the tweet reframes source language rather than quoting it.

- "typically show scan-to-scan differences under 1 cm" ⟷ article line 127/211: "repeated scans showed typical scan-to-scan differences of less than 1 cm." Quantifier preserved (not overstated to "all measurements").
- "a difference may fall within expected variation" ⟷ article line 129: "Very small short-term differences may fall within expected variability." Hedge preserved, not dropped.
- "The coach still makes the call" ⟷ article line 85 / 217: "the coach remains responsible for interpretation and program decisions." Correctly attributed to the coach, not to FitXpress or the scan.
- "capture noise" (post) vs. article's "capture conditions" / "measurement variation" (lines 81, 129) — a paraphrase, not a quoted term, and it does not introduce a number or claim absent from the source. Flagging only so `agent-improver` knows this was checked and passed, not overlooked.

## Top issue for `post-drafter`

none.
