---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/instagram-company/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — instagram-company — 2026-09-20

**Total: 17/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 3 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 3/5
- Fits: content type "Human outcome from the article" (patient taking the two guided photos at home), product bias 100% FitXpress, length 833 chars inside the 600-1000 budget, zero hashtags, CTA "Link in bio for the whole workflow." matches the brief's suggested `«Link in bio»` almost verbatim, hook is a single clean sentence that fits before Instagram's "more" cut.
- Miss: the brief's `avoid` field says explicitly "Занадто технічні деталі, API-talk, pricing, jargon." Paragraph 4 — "A single record may hold a capture timestamp, selected body measurements, two BMI values for comparison, and any quality flags." — is a near-verbatim lift of the article's field-by-field record description (`workspace/seo/articles/bariatric-hub-refresh/published-live-2026-09-20.md` line 60: "A single record may contain a capture timestamp, selected body measurements, two BMI values for comparison, and any quality flags."). It reads as a database schema, not "visual storytelling... less corporate, more brand," and is the opposite of what this profile's brief asks the drafter to strip out.
- Related: FitXpress is named exactly once, inside the disclaimer sentence ("FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility."). The product is never introduced by name in the human-angle part of the caption, so the only brand mention on the account's own feed is a legal-register sentence — a byproduct of importing the article's compliance line wholesale instead of adapting it to the caption's voice.

### C. Brand & tone — 3/3
- No banned-word-list hits (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) and no em dash, consistent with `lint.hard_fails: []`.
- No slogan-style close, no first-person leakage in a channel that should stay third-person/company voice; "Link in bio for the whole workflow. 💙" stays soft and on-brief for the CTA.
- The compliance sentence flagged under A is a register mismatch with the brief, not a banned-word or AI-tell violation, so it is scored there rather than here.

### E. Output quality — 3/4
- **Position:** "By the time the consultation starts, the numbers are already in the record. The appointment can be about medical history, comorbidities, surgical risk and patient education. The measuring already happened." paired with "A single record... What it never holds is a decision." This is an actual stance — the software's job stops at capture, the clinician's job starts at judgment — argued twice (once as workflow, once as record contents) rather than a bare feature list.
- **Angle distinctness:** `sibling_angles` was not included in this task's input (the shared preamble names `profile_brief`, `lint`, `post_body`, `post_meta`, `article_path` but the per-profile section below the divider has no sibling-angles block), so overlap with other profiles in this pack cannot be judged from what was supplied.
- Execution: the record-enumeration-plus-disclaimer paragraph (see A) is what keeps this from as-is-ready — it needs a short pass to translate into the account's human register before publishing, which is why this lands at 3 rather than 4.

## Top issue for `post-drafter`

When a claim requires the article's compliance/output-list language, paraphrase it into the profile's register instead of quoting the source sentence near-verbatim — on `instagram-company` this collided directly with the brief's own "avoid jargon/technical detail" instruction.
