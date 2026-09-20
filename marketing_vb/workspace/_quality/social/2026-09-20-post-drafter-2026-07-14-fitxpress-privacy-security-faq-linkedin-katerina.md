---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: The quoted "Not X, but Y" pivot echoes the banned corrective-negation family the lint can't catch in quoted form; worth a post-drafter prompt note, but not a rewrite round here — 18/20, lint PASS, brand 15/15.
---

# QC Report — post-drafter — linkedin-katerina — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Hits every structural requirement of the personal-profile rules (2026-09-04): hook is a claim not a question ("Accuracy is no longer what separates one body-scanning vendor from another."), no geo announced in the first sentence, one thing taught (accuracy-to-governance shift), closes on a real question requiring the reader's own experience rather than "Thoughts?". UK lens is delivered through the concrete detail (UK MDR) rather than a location statement, which is the correct pattern for this profile.
- One brief item only partially met: "short sentences, nothing longer than 30 words... most under 15." The sentence "One line I keep coming back to: an independent regulatory assessment concluded it does not meet the definition of a medical device under the UK Medical Devices Regulations." runs 28 words — inside the hard 30-word ceiling but well outside the target the brief actually states for most sentences (lint flags this itself as a warning: "longest sentence 28 words (brief wants most under 15)"). Everything else in the post is short; this is the one line that would need a split for full compliance.

### C. Brand & tone — 2/3
- "Not 'how accurate are you,' but 'what have you decided you are not, and who made that call?'" is a corrective-negation contrast built as the pivot of the whole post. It is not the exact banned string ("it's not just X, it's Y"), but it is the same rhetorical family CLAUDE.md §6 names as an AI signature, and it is the one construction the mechanical detector (ai-density 0.0) is not built to catch in this quoted form. Everything else is clean: no banned words, no em dash, no triple parallelism, no slogan close, first person used correctly for a founder's own observation.
- The actual regulatory boundary statement — "FitXpress is not a medical device." — is done right: direct, no "positioned as," matches the compliance canon in CLAUDE.md §12 and the live FAQ's Quick-answers row verbatim in substance.

### E. Output quality — 4/4
- **Position:** "It means stating your limits in writing, before a deal, with the qualifications attached." and "Boundaries like that used to surface in a sales call. Buyers now expect to read them in public." — this is a judgment about where the market is moving, not a restatement of the FAQ. The post argues that disclosure of limits, not accuracy, is becoming the differentiator, and treats the UK MDR line as evidence for that claim rather than as the point itself.
- **Angle distinctness:** Adjacent to `twitter-company` ("the honesty is the move, not a compliance badge") in that both use the same medical-device disclosure as proof, but the framing differs in scope: `twitter-company` justifies why 3DLOOK published the FAQ; this post treats the FAQ as one data point inside a broader CEO-level market thesis (accuracy commoditizing, buyer questions changing) and closes by asking the reader to test that thesis against their own vendor evaluations. Distinct enough to stand, but the shared anchor (the same disclosure line as the proof point) is worth flagging if a future pack reuses it a third time.

## Top issue for `post-drafter`

The "Not X, but Y" quoted-question construction used as the post's turn is the same family as the banned "it's not just X, it's Y" AI signature and the lint detector cannot see it in this quoted form — when a post's hook depends on reframing one question as another, write it as two separate direct sentences instead of a corrective-negation pair.
