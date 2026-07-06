---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-katya/post.md`
**Total: 18/20** — ⭐ Excellent

## Special focus: unsourced-claim check (per sibling failure precedent)

The `linkedin-katerina` draft for this same article failed QC v1 (10/20) for asserting an unsourced, dated regulatory claim ("MHRA became a full ICH member in 2022") that existed nowhere in the source article or `product-info/`. This draft was checked line-by-line against that specific failure mode:

- **Every measurement/trial claim traces to `publish-package.md` v3:** "twelve-month study" (line 430: *"Documentation conventions can drift over a twelve-month study"*; line 439: *"study window can run twelve months or longer"*), site-to-site coordinator variability (line 430), BMI/waist/hip/body-composition at baseline/follow-up/monitoring window (line 418, 428), hybrid/decentralized remote check-ins raising pressure on measurement (line 439/474), guided two-photo structured/time-stamped capture usable at site or remotely (lines 454-456), and "not replacing the reference methods" (paraphrases lines 424/458/519 — the article's own scope-note language, and correctly avoids naming DEXA at all, consistent with the article's `no_dexa_alternative` guardrail).
- **The Israel-ecosystem claim is correctly hedged and unsourced-safe.** The Angle field explicitly frames it as "no specific market claim, just Katya's opinion," and the body honors that: "I think this is the kind of infrastructure problem Israel's health-tech scene is well suited to take seriously" — no named companies, no market-size figures, no regulatory specifics, no dates. This is exactly the correction pattern that got `linkedin-katerina` v2 to 19/20, applied proactively here rather than after a failure. `manifest.json`'s note for this draft confirms the reasoning explicitly and confirms no WebSearch/WebFetch was used.
- **No invented clients or case studies** — no client names appear anywhere in the post (unlike `linkedin-company`/`facebook-company` drafts for other articles which cite named customers).
- **Conclusion: the specific failure mode flagged for the sibling draft does not recur here.** This is the strongest part of the artifact.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
No issues. `CLAUDE.md` tone/no-go rules applied. Profile block (`linkedin-katya`, `social-profiles-config.md`) correctly read and honored: `product_bias: 100% fitxpress`, length range 800-1400 chars, `avoid` list respected (no EU regulatory specifics, no US payer-system context, no apparel/fashion topics). `brand-assets/past-posts/linkedin-katya/` is empty — the prompt's edge case ("if empty, continue without them, do not STOP") was correctly handled and documented in `manifest.json` rather than silently skipped. Article (`publish-package.md` v3) read for claims and for the Section 4 OG image brief, which the design tip quotes accurately (multi-site dot-map motif, guided two-photo capture icon, timestamp/structured-record icon, teal-blue palette). Manifest updated correctly with the new draft entry.

### B. Factual accuracy — 5/5
No issues. All claims trace to `publish-package.md` v3 (see special-focus section above for line-level mapping). No invented numbers, no invented case studies or client names, no proof-points.md figures misquoted (none were needed or used). No compliance-guardrail violation: the post avoids DEXA comparison entirely, makes no GCP-compliance, eligibility-determination, or efficacy claim, and correctly frames FitXpress's role as narrow ("standardizing capture around the protocol, not replacing the reference methods it already defines").

### C. Brand & tone — 2/3
- Line 22 (post body): *"...well suited to take seriously — the ecosystem here is built for operational rigor, not just for a good demo."* This combines an em-dash with a "not just X" fragment immediately after it — structurally close to the banned AI-signature pattern in `CLAUDE.md` §6 ("em-dash in rhetorical constructions like «X — this is not just Y»"). It stops short of the full "it's not just X, it's Y" template, but it is the one place in the prose where both flagged signatures (em-dash + "not just") co-occur, and it lands on the post's central opinion sentence.
- No banned words from `messaging.md` found (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge).
- Two other em-dashes in the file (line 13, the `Angle` metadata field, and line 28, the CTA field: "Article in comments — curious what others here think.") are lower-risk — the CTA one is a simple list-style separator, not a rhetorical contrast, and the Angle field is internal metadata, not published copy — so they are noted but not scored.
- Style-consistency check against `past-posts/linkedin-katya/` (per rubric's Social-post override) could not be performed — the folder is empty. No penalty applied; documented as N/A rather than skipped.

### D. Format & structure — 3/3
Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path (`workspace/social/articles/{slug}/linkedin-katya/post.md`). Template fully followed (Angle / Goal / body / CTA / Design tip with all 4 required fields). Body copy measures 1,395 characters — within the profile's 800-1400 char range (98% of the ceiling, but compliant).

### E. Output quality — 3/4
- Opening line is a genuine hook ("everyone wants the flashy AI layer, and almost no one wants the unglamorous operational problem underneath it") and lands before LinkedIn's "see more" cutoff.
- The closing sentence — "standardizing capture around the protocol, not replacing the reference methods it already defines" — has an ambiguous pronoun ("it" refers back to "the protocol," two clauses earlier), which reads slightly awkwardly on a first pass. A minor copy-edit, not a factual problem.
- Minor cross-profile note (does not affect this artifact's score per the "score only this artifact" rule, mentioned for awareness): this post's opener ("I keep having a version of...") and `linkedin-katerina`'s opener ("I keep coming back to the same pattern...") use near-identical framing devices for two posts published from the same article on the same day — worth a glance before both go out together.
- Net: publish-ready with a 5-minute polish pass (soften the line-22 em-dash construction, clarify the "it" pronoun) rather than a substantive rewrite.

## Top 3 issues (приоритет для improver)

1. Line 22: em-dash + "not just" construction on the post's central opinion sentence — soften to avoid the AI-signature pattern (e.g., split into two sentences, or drop "not just for a good demo").
2. Minor: ambiguous "it" pronoun in the closing FitXpress sentence ("the reference methods it already defines") — clarify what "it" refers to.
3. Process note (not a defect): `past-posts/linkedin-katya/` remains empty, so the Social-post rubric's style-consistency-vs-history check cannot be applied to any future `linkedin-katya` draft either. Flag to Vadim to seed 5-10 reference posts for this profile.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
