---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/twitter-company/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement: ✅ agree — the 240-260 brief target (post is 271) and the §1.9 one-use cap on corrective negation are both real; it still ships since lint and post-brand-checker (the terminology gate) passed, but the notes are correct for improver.
  top_issue: A "what we are NOT" concept naturally pulls the drafter into a corrective-negation triplet and toward the linter's 280 ceiling — the fix is to cap negation to the single medical-device exception (paraphrase SOC 2/FDA as plain statements) and draft to the profile's tighter char target.
---

# QC Report — post-drafter — twitter-company — 2026-09-20

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
- `profile_brief.length` says "240-260 chars for single tweet". `lint.chars` is 271 —
  inside the global 1-280 budget the linter enforces, but 11 characters over the
  profile's own single-tweet target. This is a brief-level miss the linter cannot see
  (it only gates the wider platform ceiling), not a hard fail.
- Everything else in the brief is met: 100% FitXpress content, no hashtags, no emoji,
  "industry commentary tone" delivered through the procurement-question framing, and
  the CTA (`Full FAQ linked in bio.`) matches `cta: "Link in bio…"` exactly.
- Content type matches `content_types` ("Short POV on industry trend the article
  touches") rather than a flat stat pull — correct choice for this profile.

### C. Brand & tone — 2/3
- The post leans on corrective-negation structure three times in four sentences:
  "FitXpress is not a medical device." / "Not cleared by the Food and Drug
  Administration." / "SOC 2 in progress, not certified." `terminology-guardrails.md`
  §1.9 allows corrective negation **once**, for a single regulatory boundary statement
  — the medical-device sentence is the canon use of that exception. The SOC 2 line
  repeats the pattern with an un-sourced paraphrase ("SOC 2 in progress") instead of
  the compliance-canon phrase "working toward obtaining a SOC 2 Attestation Report,"
  which drops the one substantive detail (Attestation Report) that makes the status
  concrete rather than vague.
- `lint.warnings` flags `monotone rhythm: sentence-length variation 0.32 (want >0.35)`
  — three short, structurally identical declaratives back to back ("X. Not Y. Z, not
  W.") is the mechanical cause of that flag and reads as a listy AI cadence rather than
  a written voice, compounding the corrective-negation issue above.
- No banned words, no em dash, tone otherwise on-brief (punchy, data-first).

### E. Output quality — 3/4
- **Position:** "The harder question procurement actually asks: what are you NOT?"
  is a real editorial stance, not a recap of the FAQ — it reframes the source article's
  Quick-answers table as a claim about vendor-page honesty rather than restating the
  table. This clears the "does it judge, not just state" bar.
- The closing "We answered in writing." lands as a genuine kicker tied to the CTA,
  not a slogan tail.
- Held to 3/4 rather than 4/4 because of the monotone-triplet execution flagged under C
  and the char overage under A — a 5-10 minute trim (shorten the SOC 2 line, vary
  sentence length) would put this at 4/4 as-is.
- **Angle distinctness:** `sibling_angles` lists no other profile yet for this pack, so
  distinctness cannot be judged against siblings — flagging for whoever reviews the
  rest of the pack, not scoring it here.

## Top issue for `post-drafter`

When a profile brief states a tighter single-tweet character target than the linter's platform ceiling, draft to the brief's number, not the linter's; and cap corrective-negation ("X, not Y" / "not certified" / "not cleared") to the one regulatory-boundary exception even when the post's whole concept is "what we are NOT" — paraphrase the remaining negatives as plain statements instead of repeating the pattern.
