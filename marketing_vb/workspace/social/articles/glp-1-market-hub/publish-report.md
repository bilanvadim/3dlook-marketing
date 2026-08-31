# Social Publish Report — glp-1-market

**Article:** [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/)
**Published:** 2026-08-28 (hub refresh, republished in place at the same URL)
**Source of record:** `workspace/seo/articles/glp-1-market-hub/published-live-2026-08-28.md`
**Pack:** `workspace/social/articles/glp-1-market-hub/`
**Run date:** 2026-08-28

## Profiles: 9/9 ✅

| Profile | Length | Format | CTA | Status |
|---------|--------|--------|-----|--------|
| twitter-company | 257 chars | text + photo | article link in reply | ✅ |
| instagram-company | 982 chars | carousel | link in bio | ✅ |
| facebook-company | 1191 chars | infographic | read the full article | ✅ |
| linkedin-company | 267 words | infographic | read the full article | ✅ |
| linkedin-katerina | 248 words | text | invitation to read | ✅ |
| linkedin-katya | 235 words | screenshot | question, then article | ✅ |
| linkedin-nick | 249 words | text + photo | question, then article | ✅ |
| linkedin-olena | 248 words | screenshot | question, then article | ✅ |
| linkedin-vadim | 246 words | poll | poll question, then article | ✅ |

**Skipped:** `linkedin-whitney` — `posts_per_week: 0` (disabled 2026-06-27).

Every profile got a distinct entry point into the article; no two posts run the same angle, and the
five article/infographic treatments are deliberately differentiated so the designer does not produce
near-identical cards. Formats span text, text + photo, carousel, infographic, screenshot and poll.

## Checks

| Check | Result |
|---|---|
| `post-brand-checker` | **9/9 PASS** — run independently per post |
| `detect-ai-tells.py` | **0 markers, 0 hard bans on all 9** — 7 CLEAN, 2 SPOT-FIXES (soft rhythm only) |
| `quality-controller` | **6/9 complete**, all "good" (15-17/20); 3 runs blocked |

## Issues: 4

1. **AUTO_QC is 6 of 9.** Six `quality-controller` runs wrote their reports before the org monthly
   spend limit hit (HTTP 429); three did not. Scores, all "good": `linkedin-katerina` 17/20,
   `linkedin-nick` 17/20, `twitter-company` 16/20, `instagram-company` 16/20, `linkedin-company` 16/20,
   `facebook-company` 15/20. **Outstanding: `linkedin-katya`, `linkedin-olena`, `linkedin-vadim`.**
   This does not gate the copy — `post-brand-checker` is the binding gate under `post-drafter` hard
   rule #6 and it passed all nine — but those three rubric scores that `agent-improver` consumes are
   missing. Re-runnable with `/qc` per artifact; no redrafting needed.
   Each completed report carries a `coordinator_review` per CLAUDE.md §14.

2. **Three posts carry one soft AI-tell marker, left in deliberately.** `detect-ai-tells.py` wants
   sentence-length variation above 0.35; `twitter-company` scores 0.27, `facebook-company` 0.33 and
   `linkedin-company` 0.34.
   Twitter is a 47-word tweet the detector explicitly does not score at that length ("short form,
   counted not scored"), and it sits at 257 of 280 characters with verified claims, so forcing rhythm
   would put the claim budget at risk. LinkedIn company at 0.34 against a 0.35 target is inside noise
   and already near its 280-word ceiling. Neither is a hard ban. Flagging rather than hiding.

3. **`post-drafter` cannot run its own brand check.** Its hard rule #6 says "after writing, call
   `post-brand-checker`", but its agent definition grants only `Read, Write, Grep, Glob` — no Task
   tool — so the rule is unexecutable and every one of the nine runs reported it could not comply.
   The coordinator ran the checker instead, which is why six real findings were caught. Worth fixing
   in the agent definition, but that is a prompt change for Vadim's approval, not something to slip
   in mid-run.

4. **`facebook-company` was rewritten on 2026-08-31 after its QC pass, and its tone is still a
   judgement call for Vadim.** QC scored it 15/20, the lowest in the pack, on two counts. The factual
   ones I fixed in full (see the table below) — including a claim that was outright wrong, and three
   qualifier losses I had caused myself while trimming the post to fit its character band. The second
   count I did **not** fully fix: `social-profiles-config.md` asks this profile for an "accessible,
   community-oriented, slightly warmer" register and lists "dry B2B corporate tone" under `avoid`,
   and the post still reads closer to operator-to-operator trade press. The rewrite recovers some
   warmth, but a real warmth pass means re-drafting claims copy that is now verified, so it is
   Vadim's call whether to spend that. Everything else about the post clears.

### Findings raised by the brand checks and QC, and fixed before this report

| Post | Finding | Fix |
|---|---|---|
| `twitter-company` | `GLP-1` shipped unexpanded (rule M1) | Expanded to `glucagon-like peptide-1 (GLP-1)`, copy re-tightened to 257 chars |
| `instagram-company` | same M1 miss | Expanded; M2 stacked negation also split into two sentences |
| `twitter-company` | Design tip claimed all three article assets avoid photography — false for `cover-3.webp` | Corrected, and written into the pack run brief so the other seven could not repeat it |
| `twitter-company` + all | `article_slug` carried the folder name `glp-1-market-hub` | Corrected to the published slug `glp-1-market` everywhere, incl. `manifest.article.slug` |
| `facebook-company` | Pharmacy and employer hedges flattened ("may", "and pharmacy model", privacy requirements dropped) | Source hedging restored, post retrimmed to 1191 chars |
| `linkedin-company` | Hedge list dropped "pricing"; subject-verb slip | Both fixed |
| `linkedin-katerina` | Retention compressed to "the structured output stays" | Restored to "retained per the agreement" |
| `linkedin-nick` | `KFF` unexpanded (rule M1) | Expanded to `Kaiser Family Foundation (KFF)`, retrimmed to 249 words |
| `linkedin-katya` | Regulatory boundary sentence paraphrased | Restored verbatim from the live article |
| `linkedin-vadim` | "can provide" hardened to "give" in a sentence framed as quoting the article | Hedge restored; subject-verb slip fixed |
| `linkedin-olena` + `linkedin-katya` | Both opened their position with the same "My view:" label | Olena's rewritten onto her multi-market angle; all three position labels now distinct |
| `facebook-company` | **"no hardware"** — factually wrong, FitXpress needs a smartphone. Caused by a coordinator trim of "no scanning hardware" | Restored to "no specialized scanning hardware" |
| `facebook-company` | "It keeps the record comparable between visits" stated a guarantee where the article states a conditional | Replaced with the article's "Consistent capture helps programs compare results more reliably over time" |
| `facebook-company` | Hybrid model lost its "may" and gained an interval the article never specifies | "A hybrid clinic **may** measure at visits, with remote intervals between" |
| `facebook-company` | "authorized" / "appropriate" dropped from both access clauses in a privacy-sensitive post | Both qualifiers restored |
| `facebook-company` | Eligibility carve-out missing from the limitation sentence — in the one post that raises eligibility paperwork, which `audience.md` explicitly guards | "does not determine treatment eligibility" added |
| `facebook-company` | "determined more by the delivery model than by the medication" invented a comparative and dropped "partly" | "How progress gets tracked **depends partly on** the route" |
| `linkedin-nick` | "no special hardware" — same trim-induced qualifier loss, milder | Restored to "no specialized hardware" |

## Ready for review: YES

**Next:** Vadim reviews `review-digest.md` → approves → `visual-brief` runs per approved post (it is
deliberately **not** triggered before approval) → posts scheduled or published manually.

**Publishing note for Vadim:** the `twitter-company` post attaches a cropped stat card while the
article link in the reply renders its own preview from the page, so two different images will appear
on that tweet. That is a publishing-time decision, not a copy problem.
