---
qc_date: 2026-09-23
agent: post-drafter
artifact: workspace/social/articles/2026-09-03-manual-vs-digital-intake-occupational-health/twitter-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: The tweet compresses the article's trade-off instead of sharpening it into a punchier stance; accurate but leans compressed-paraphrase over "industry commentary."
---

# QC Report — post-drafter — twitter-company — 2026-09-23

**Total: 18/20** — excellent

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
- Content type matches brief exactly: "One striking stat or claim from the article" — the 45-second scan claim is the payload, and the CTA (`Link in bio`) matches the single-tweet CTA spec (`Link in bio / article link у відповіді до треду`).
- No bullets, no emoji, single paragraph — respects `avoid: "Long paragraphs, bullet lists, emoji flood, generic corporate speak"`.
- Length is 238 chars against `lint.metrics.budget` [1, 280] (pass), but the profile brief's own target is narrower: `"240-260 chars for single tweet"`. The post lands 2 chars short of that band. Trivial on its own, but it is the kind of drift that compounds if the drafter treats the lint ceiling as the target instead of the brief's tighter range.
- Tone requirement is "Punchy, data-first... Industry commentary tone" — the post is data-first but reads closer to a compressed process description than commentary; see E below for the same observation from the output-quality angle.

### C. Brand & tone — 3/3
- No banned words, no em dash, no triple-adjective parallelism, no corporate-speak filler. Clean against CLAUDE.md §6 and the rubric's banned-words checklist.
- One phrasing note, not a tone violation: "forms, tape measuring and record entry" mixes noun forms (a plain noun, a gerund, another noun) instead of a clean parallel list ("forms, measurements and record entry"). Doesn't trip any hard-ban pattern, but it reads as slightly assembled rather than written — flagged under E for polish, not scored down here.

### E. Output quality — 3/4
- **Position:** the post carries one imperative clause that functions as a recommendation, not pure description — `"Move the eligible steps ahead of the visit and a two-photo scan captures measurements in under 45 seconds."` The "move X and Y" construction is an implicit endorsement of moving steps earlier, echoing the article's central argument (§"Where manual intake can slow occupational health screening"). It is a real position, but a thin one: it never states what is gained (fewer transcription errors, appointment time freed up) or names a cost of the status quo beyond "competes for the same slot." Compare to the article's own framing, which explicitly names the trade-off ("incomplete forms, unusable measurements, and manual record entry compete with testing and examination for the same appointment time") — the tweet compresses this correctly but doesn't sharpen it into a stronger claim the way "punchy... industry commentary tone" implies.
- **Angle distinctness:** matches `sibling_angles` row for `twitter-company` ("the appointment-time squeeze... moving eligible steps earlier is the trade") and is genuinely distinct from the other eight — closest neighbor is `facebook-company`'s decision-framework angle, but that post is explicitly balanced/discussion-oriented while this one stays declarative and narrower (time-slot competition only, no manual-fits-when / digital-fits-when framing). No overlap risk.
- The "tape measuring" noun-form mismatch (see C) is the one polish issue keeping this from a 4 — ready to post, but a careful editor would tighten that clause in under a minute.

## Top issue for `post-drafter`

When the content type is "one striking stat or claim" for `twitter-company`, push past restating the article's mechanism toward a sharper one-line judgment (what the appointment-time squeeze actually costs, or why it matters now) — the current post is accurate and clean but reads as a compressed paraphrase rather than commentary with a stance.
