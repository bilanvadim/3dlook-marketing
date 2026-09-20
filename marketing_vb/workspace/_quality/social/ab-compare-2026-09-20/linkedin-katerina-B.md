---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-katerina — 2026-09-20

**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 4 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Hook is a claim, ~10 words, disagreeable-enough: "A single BMI reading is becoming weaker evidence every year." Meets the personal-profile rule 5 exactly (claim, not a question, not a teaser).
- Teaches one concrete thing per rule 4: "a body-data field that cannot say when it was captured and by what method is not documentation yet" is a usable rule of thumb, not a listicle or a walk through the article's structure.
- Close is a question that needs the reader's own record, not filler: "How many of the body-data fields in your intake record carry both a capture date and a source today?" — satisfies the "not 'thoughts?'" bar in rule 5.
- No location announced anywhere (rule 3) and no UK mention at all, which the brief explicitly allows ("most posts should carry no UK mention at all"). The one geo-shaped term the lint counted (`geo_mentions: 1`) is "American Society for Metabolic and Bariatric Surgery" — a source citation, not the author naming her market, so it does not trip the actual intent of rule 3.
- Correctly avoids the profile's "Avoid" list even though the source article is built entirely on US material (CMS-0057-F, CDC, an insured-claims JAMA Surgery cohort): the post pulls only the GLP-1/weight-loss clinical finding and leaves out FDA, CMS timelines and the US payer system. That is a real editorial choice, not an accident of length.
- CTA matches the meta field exactly: "**CTA:** Soft, full article in the comments." → post ends "The full piece on bariatric intake and progress records is in the comments."
- FitXpress is not named; the brief only requires it be natural if present ("Mention 3DLOOK only naturally"), so its absence is not a defect here.

### B. Factual accuracy — 4/5 (lint clean, one judged deduction)
- `lint.hard_fails` and `lint.warnings` are both empty; the ASMBS figure itself is reproduced correctly against the article ("more than 6,700 patients," "approximately 8% of total body weight," GLP-1 before bariatric surgery) — no number_drift.
- What lint cannot see: "A patient can therefore arrive at intake with a current BMI below a value documented **months earlier**." The article's parallel sentence says only "an earlier documented value" — it never quantifies the gap as months. This isn't a subject-swap or a proof-points number, so it doesn't rise to a hard fail, but it is an added specific the article doesn't support, the same class of quiet embellishment the lint is structurally blind to. Plausible, but invented.

### C. Brand & tone — 3/3
- No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) anywhere in the body.
- No em dash, no "not just X, it's Y," no triple parallelism, no "Furthermore/Moreover" openers.
- Register is calm and executive throughout ("That is the shift I keep watching," "My own rule of thumb") — no sales language, no slogan close, first person used exactly where the personal-profile rules call for it and nowhere else.

### E. Output quality — 4/4
- **Position:** stated twice, unambiguously. "Both numbers are real. Only one of them carries a date and a recorded source." is a judgment about what counts as evidence, not a fact recitation. "a body-data field that cannot say when it was captured and by what method is not documentation yet" goes further — it's a definitional claim a reader could push back on, which is exactly the bar rule 5 sets.
- **Angle distinctness:** `sibling_angles` were not part of this input (this run compares a single post's two drafts, not a pack), so cross-profile distinctness cannot be judged from what's here. Within the post itself, the angle ("provenance over precision" as the thing enterprise buyers are starting to ask for) is specific to the GLP-1-attrition mechanic in the article, not a generic restatement of the article's headline claim.
- Reads as edited, not compiled: short/long sentence rhythm (avg 12.6 words, longest 23) does real work here rather than just clearing the lint gate.

## Top issue for `post-drafter`

When paraphrasing a claim like "arrived at intake with an earlier documented BMI," don't add an unstated time qualifier ("months earlier") that the article never gives — state the comparison the way the source states it, or leave the gap unquantified.
