---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
coordinator_review: |
  agreement: ✅ agree
  top_issue: None. Highest-scoring post in the pack alongside nick; the retention wording was tightened pre-QC.
  notes: |
    No action needed. The one claims item, retention compressed to "the structured output stays",
    was already restored to "retained per the agreement" before QC ran.
    The UK lens held: buyer-behaviour observation only, no MHRA/CQC/NHS fact invented, and the
    controller/processor split keeps the article's "in most enterprise deployments" hedge.
    Agreed on design-tip verbosity, pack-wide.
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/linkedin-katerina/post.md`
**Total: 17/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Missing self-check report.** `_run-brief.md` §"You cannot call `post-brand-checker`" (lines 62-67) instructs: "Run the 10-point checklist, the Part 2 terminology guardrails and the ai-tells hard fails yourself, and **report your self-check**." The artifact has no self-check block. It is the compensating control for the un-runnable `post-brand-checker` on regulated-health copy, and it silently disappeared. Systemic, not personal: `linkedin-company/post.md` and `facebook-company/post.md` omit it too, and `post-drafter.md` §"File structure" (lines 105-138) defines no slot for it — the template and the run-brief contradict each other.
- **Past posts: no evidence the step ran.** Run-brief line 77 says read the 9 posts at `past-posts/linkedin-personal/katerina-galich/` and "do not silently continue without them." Nothing in the artifact records that read. The resulting voice does land near her corpus (the verdict-line cadence of "Finding them at amendment stage is expensive." matches "It's a board-level responsibility." from `2026-02-06-data-trust-board-level-responsibility.md`), so this reads as undocumented rather than skipped.
- Everything else from the brief is visibly done: `glucagon-like peptide-1 (GLP-1)` expanded at first use (line 26, rule M1 — the trap that caught the Twitter and Instagram posts), `article_slug: glp-1-market` not the folder name, `cover-3.webp` correctly described as a photograph (the exact error QC flagged in the Twitter design tip), angle checked against all four siblings, manifest carries `word_count_body` only.

### B. Factual accuracy — 4/5
- **GDPR hedge intact — confirmed.** Line 36: "In most enterprise deployments the customer is the controller and 3DLOOK is the processor" against the live article line 151: "In most enterprise deployments, the customer acts as the controller, and 3DLOOK acts as the processor under the General Data Protection Regulation (GDPR)." Hedge preserved verbatim in substance; dropping the regulation name is correct for this profile (brief line 98 bans EU-specific regulatory framing) and does not misattribute anything, since UK GDPR uses the same two roles.
- **No invented UK regulatory fact — confirmed.** No MHRA, CQC or NHS position anywhere; line 20 of the artifact documents that decision explicitly. The article names no UK instrument, and the post claims none.
- **Line 34 compresses a three-part determinant into two.** "with access and reporting rights set by structure and contract" — the article (line 97) says these "depend on the program structure, contractual roles, **and applicable privacy requirements**." Dropping the privacy leg makes a governance sentence read as purely contractual. In this material that is the wrong thing to shorten.
- **Line 30: "In the UK, I see the shift in the order of the questions."** A personal market observation the article does not support. `post-drafter.md` hard rule #1 names "personal experience the article doesn't support" explicitly, and `linkedin-post-prompts.md` line 86 repeats it. Precedent exists in her own corpus (`2026-03-27`: "I've had the same conversation with multiple online pharmacy teams across the UK"), so this is a sign-off question for Katerina, not a fabrication.
- Zero numbers in the post, so no `proof-points.md` exposure. Photo-deletion/retention (line 36) and the not-a-medical-device framing (line 38, in the post-2026-08-25 direct form) both trace cleanly to article lines 149 and 155.

### C. Brand & tone — 3/3
- Zero banned words. Zero hashtags. One emoji (👇, line 40) against the 1-2 ceiling. No negative parallelism, no punch triads, no `positioned as`, no presumed-reaction opener, no reserved words.
- **No em dash in the post body** (verified by grep). Three em dashes exist in the artifact, all in the Design tip metadata (lines 49, 50, 51) — and line 51's "no visual needed — native platform format" is copied verbatim from `post-drafter.md` line 99, which prescribes that exact string. Not scored against the writer; it belongs to the template. Improver item.
- Takes a position (line 36: "My position is simple: a vendor should be able to state its role in writing before a pilot starts"), which clears ai-tells category 21. Paragraph lengths vary 18/33/50/22/30/50/23 words — no monotone block pattern.
- Segment boundary held: touches employer-supported programs and UK buyers without bleeding into online-pharmacy BMI compliance (`audience.md` segment 1 "Don't").

### D. Format & structure — 3/3
- Frontmatter complete, `product: fitxpress` present, `article_slug: glp-1-market` correct, path correct, all four Design tip fields present, manifest entry appended without touching other rows and `ready_for_review` left `false`.
- **Word count is reported three different ways.** The artifact says 248 (line 21), `manifest.json` says 245, an independent count of the body gives ~246. All three sit inside 180-250, so nothing is breached, but the pack has no pinned convention for whether the emoji and the bare URL count. Worth fixing before a post lands at 251.

### E. Output quality — 3/4
- Angle is genuinely new against all four siblings (Twitter = market scale, Instagram = the individual check-in record, Facebook = the four delivery models, LinkedIn company = market-structure shift). Governance-as-procurement-question is the one entry point none of them took.
- **Line 36 is the paragraph a reviewer will touch.** Three vendor facts stacked in one place (controller/processor, photo deletion, retention) makes a founder post start reading like a data-processing addendum. Katerina's brief (line 98) puts "product features" on the avoid list; this is compliance detail rather than features, so it is defensible, but it is the least founder-sounding passage in the post.
- The "I see the shift" line needs Katerina's own confirmation before publishing. That is a 5-minute check, not a rewrite.
- At ~246 words against a 250 ceiling there is no headroom: any addition during review forces a cut elsewhere.

## Top 3 issues (priority for improver)

1. The run-brief demands a written self-check as the substitute for the un-runnable `post-brand-checker`, and `post-drafter.md`'s file template has no field for it — so the whole pack shipped without one. Add the slot to the template or drop the requirement; do not leave it stated in one file and impossible in the other.
2. `post-drafter.md` line 99 prescribes an em-dash string ("no visual needed — native platform format") that `terminology-guardrails.md` bans without exception. The spec is teaching the violation.
3. Line 34 drops "applicable privacy requirements" from the article's list of what determines access and reporting rights. Compression is the failure mode to watch in governance sentences.
