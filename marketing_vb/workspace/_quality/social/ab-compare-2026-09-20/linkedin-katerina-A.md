---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-katerina — 2026-09-20

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
- **No location announced.** `geo_mentions: 0` in lint, and the post never invokes the UK
  lens at all, matching the personal-profile rule "most posts should carry no UK mention"
  and the ban on a geo opener. Correctly treats the market as who she's writing for, not
  something to say.
- **Hook matches the earn-the-read spec exactly.** "A body measurement is only as good as
  its source." — 10 words, a concrete, disagreeable claim, not a question or teaser, per
  rule 5 of the personal-profile section.
- **Closes on the right device.** "Worth asking your own team: when they open a patient
  record today, what share of the values carry a source and a date?" — a question that
  needs the reader's own numbers, not "thoughts?" filler. This correctly follows the
  2026-09-04 personal-profile closing rule (question) rather than the older per-profile
  instruction to "end by inviting readers to explore the article" — the newer rule wins by
  its own stated precedence, and the post gets that precedence right.
- **Founder register, one first-person instance, no sales pitch, FitXpress not forced in.**
  "The shift I'm watching is quiet but real" is the only first-person line — matches "speak
  from experience without pretending to have experiences the article does not support,"
  and the post never names the product, consistent with "mentioned only where it fits
  naturally."
- **One thing taught, not a listicle.** The single teachable unit — attach source + timestamp
  to every value, route what's above threshold — is stated once and not diluted into three
  takeaways.

### C. Brand & tone — 2/3
- **One corrective-negation construction, the shape CLAUDE.md §6 hard-bans.** "That is not
  a story about patients being dishonest. It is a story about numbers with no provenance."
  Splitting it across two sentences avoids the `post-lint.py` regex for "It's not just X,
  it's Y" and for comma-spliced "X, not Y," but the rhetorical shape is identical: lead with
  the negation, then supply the correction. `terminology-guardrails.md` §1.8 asks for the
  opposite order — state the recommended reading first, put the limitation in its own
  sentence — and reserves the negate-then-correct order for a one-time regulatory/legal/
  clinical boundary statement (e.g. "FitXpress is not a medical device"), which this isn't.
  Nothing else in the post trips a banned word, an em dash, or a triple-adjective
  parallelism — this is the one lapse, which is why the category lands at 2 rather than 3.

### E. Output quality — 3/4
- **Position:** the post argues that a body-data value without a recorded source and date is
  no longer good enough for enterprise buyers — "A body measurement is only as good as its
  source" plus "Buyers no longer ask only for a measurement. They ask where it came from,
  when it was captured, and how a discrepancy gets reviewed" is a claim someone could
  contest (e.g., "the number itself still matters more than its metadata"), and the closing
  question ("what share of the values carry a source and a date?") is written to make the
  reader's own team look under-prepared by that standard. This is a real judgment, not a
  recap of the CDC stat.
- **Angle distinctness:** per the post's own `Angle` note, the pack already has GLP-1,
  human-moment, bottleneck and CMS-deadline angles taken; "provenance of the number, not the
  number itself" is a distinct register (CEO market-observation) from all four and doesn't
  restate any of them in different words.
- **Why not 4:** the negation-then-correction sentence flagged under C is the one line an
  editor would rewrite before this goes out (e.g., "This isn't about patients being
  dishonest — it's about numbers with no provenance" reordered to state the provenance point
  first), which is a 5-minute fix, not a re-draft. That keeps this at "minimal edits" rather
  than "ready as-is."

## Top issue for `post-drafter`

Watch for negation-then-correction sentence pairs ("That is not X. It is Y.") — they carry
the same rhetorical DNA as the banned "it's not just X, it's Y" even when split across two
sentences to dodge the lint regex; state the correct reading first and put the limitation in
its own sentence instead.
