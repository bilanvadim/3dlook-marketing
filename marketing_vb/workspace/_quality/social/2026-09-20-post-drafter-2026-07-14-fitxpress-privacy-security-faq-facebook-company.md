---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/facebook-company/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree — decision-boundary angle is distinct and the medical-device / non-determination lines carry the source qualifiers intact.
  top_issue: none
---

# QC Report — post-drafter — facebook-company — 2026-09-20

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
- Content type matches the brief's "industry question that sparks discussion" exactly: opens on "who is actually making the call about your care?" and closes on "where do you think that line should sit?" — both are hooks a broad, non-B2B audience can answer without domain knowledge.
- Tone lands on "accessible… slightly warmer" as specified: plain-language framing ("We just published a plain-language answer"), no API/pricing detail, no jargon beyond the necessary product nouns (measurements, body composition, 3D model), which are spec facts a reader needs to follow the argument, not technical/API mechanics the brief tells the writer to avoid.
- CTA is "Read the full FAQ below" against the brief's "«Read the full article» з посиланням" — functionally the same instruction (link to the source), close enough not to be a deviation.
- Checked against the source article (`published-live-2026-09-18.md`): "under 45 seconds" (line 46), "does not independently determine a diagnosis, treatment… or other high-impact individual decision" (line 210), and "clinicians, underwriters, or other designated decision-makers" (line 220) all carry their source qualifiers intact — no dropped quantifier, no case swap.

### C. Brand & tone — 3/3
- No banned words, no em-dash, no triple parallelism, no clichéd AI-tell openers.
- "It is not a medical device" uses the approved direct phrasing (CLAUDE.md §6, decision 2026-09-11), not the banned "positioned as" construction, and matches the source's UK/EU MDR conclusion (line 39) without overclaiming into a certification statement.
- "We think that is the right line to draw" is first-person-plural opinion voice on a Facebook company page — appropriate register for this profile (brief calls for warmth), not the third-person enterprise voice reserved for `linkedin-company`.

### E. Output quality — 4/4
- **Position:** "We think that is the right line to draw. Software can gather clean, consistent information. Judgement about a person's health or eligibility belongs to a trained human who can be accountable for it." This is a stated normative claim about where authority should sit, not a recitation of what the FAQ says — the post argues a case rather than summarizing one.
- **Angle distinctness:** the pack's other angles are procurement honesty (twitter), the photo's journey (instagram), market-process/security review (linkedin-company), governance-as-differentiator (linkedin-katerina), data location (linkedin-katya), GDPR controller/processor (linkedin-olena), and data-lifecycle/retention (linkedin-vadim). None of them argues where decision authority should sit; this post's "software gathers, people decide" framing is a genuinely separate cut of the same source article, not a restatement of any sibling angle.

## Top issue for `post-drafter`

None.
