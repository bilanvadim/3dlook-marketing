---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/facebook-company/post.md
track: social
artifact_type: post
total_score: 15/20
status: good
coordinator_review:
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/facebook-company/post.md`
**Total: 15/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Correct source: line 16 cites `published-live-2026-08-28.md`, line 17 the live URL. No `draft-v*` anywhere. `article_slug: glp-1-market` (line 5) is correct — the error the twitter pass caught did not repeat.
- Profile config honoured on the mechanical fields: 1191 chars inside the 800-1200 band, no hashtags, no emoji, CTA is literally the config's `«Read the full article» з посиланням`, first paragraph carries full meaning per the Facebook platform rule.
- **The one step done superficially is the profile's `tone` / `avoid` block.** `social-profiles-config.md` lines 74-82 specify "Accessible and community-oriented. Broader audience than LinkedIn — explain without jargon. Slightly warmer" and `avoid: "Dry B2B corporate tone"`. Line 27 delivers "Pharmacy-led programs may keep eligibility paperwork separate from progress tracking" and "Employer-supported programs add a data-access question that depends on the contract" — that is operator-to-operator trade register, the LinkedIn lane. One sentence in the whole post ("Capture has to work in a kitchen") does what the config asks for. The config's most explicit instruction is the one dimension not applied.
- Design tip: the prompt asks for "3 lines"; `Adaptation` (line 45) is ~50 words and `Keep` (line 46) ~45. Same container problem the twitter pass flagged.
- `brand-assets/past-posts/facebook-company/` does not exist (whole folder absent). Prompt step 4 explicitly permits continuing, so not a violation, but the artifact does not flag the missing corpus.
- Not scored: the design tip does not state that `publish-package.md` §4 shipped no OG direction. The coordinator already ruled this a coordinator instruction, not an agent miss.

### B. Factual accuracy — 3/5
- **The hedges the coordinator restored did survive — two of four.** Line 27 keeps pharmacy "**may** keep eligibility paperwork separate ... with rules that **vary by** jurisdiction and pharmacy model" (article line 95) and employer "**depends on** the contract and the privacy rules that apply" (article line 97, compressed from "program structure, contractual roles, and applicable privacy requirements" — two of three retained, the licensed `depends on` verb intact). Both correct.
- **The hybrid model lost its hedge.** Line 27: "A hybrid clinic measures at each visit." Article line 93: "These programs **may** use professional measurements during clinic visits." The `may` is gone and the claim is now flat. "with weeks in between to cover" also fixes an interval the article never specifies for hybrid workflows.
- **Line 31 "no hardware" is wrong as written.** Article line 145: "without **specialized scanning** hardware". The post's own `Claims used` line 19 says "no specialized hardware" — so the frontmatter holds the qualifier and the body, which is the part that publishes, dropped it. FitXpress needs a smartphone.
- **Line 25 invents a comparison the article does not make:** "Progress tracking is determined more by the delivery model than by the medication." Article line 89 says the methods "depend **partly** on" whether care is remote, in person or hybrid, and never weighs delivery model against medication. `is determined by` is the guardrail-preferred verb (terminology-guardrails rule 4), but the comparative and the loss of "partly" are the post's own.
- **Line 31 "It keeps the record comparable between visits"** turns a conditional into a guarantee. Article line 147: "Consistent capture conditions **help programs compare** results more reliably over time."
- **"authorized" dropped twice in a privacy-sensitive post.** Line 27 "records the care team can open" vs article line 91 "records that **authorized** care teams can access"; line 29 "access for review teams" vs article line 99 "**appropriate** access for the teams responsible for patient or program review". The access-control qualifier is the point of both source sentences.
- **Eligibility carve-out omitted from the limitation sentence, in the one post that raises eligibility.** Line 31 says FitXpress "is not a medical device and makes no clinical decisions". Article line 155 also says "prescribe treatment, or **determine treatment eligibility**". Line 27 is what introduced eligibility paperwork into the post. `audience.md` lists "implying eligibility decisioning" under Don't for segment 1 and "imply automated eligibility" for segment 2.
- Clean on the hard checks: no invented customer, no invented capability, correct `product: fitxpress`, no anti-positioning claim, no accuracy or repeatability number at all (so `about-me.md`'s one-universal-number and `< 1 cm` rules are not engaged), no pricing, no competitor named. "two photos" and "30 to 45 seconds" are article-sourced (article line 145), permitted by post-drafter hard rule #1 — same reading applied in the twitter pass.

### C. Brand & tone — 2/3
- Zero banned words across the file (leverage / utilize / harness / robust / seamless / comprehensive / delve / tapestry / realm / unlock / unleash / game-changing / cutting-edge). No `positioned as`, no `objective` about our output, no "not just X, it's Y", no presumed-reaction opener. Medical framing is the post-2026-08-25 direct form: "It is not a medical device" (line 31), not "is not positioned as".
- **Two em dashes in the file body outside the template.** Line 37 `**CTA:** Explicit but soft — "Read the full article"` and line 43 `` `banner_2-2.webp` — the five requirements ``. (Line 14 is the template's own heading format and does not count.) Neither is in the published copy, but `terminology-guardrails.md` bans the character "всегда, без исключений" with no channel carve-out, and the sibling twitter artifact scored a clean grep on this same check.
- Register drift from the profile's `avoid: "Dry B2B corporate tone"` — see A. This is the Facebook page, not the company LinkedIn page, and the post does not read differently from one.
- Line 25 "Glucagon-like peptide-1 (GLP-1)" is **correct**, not a lapse — terminology-guardrails line 47 names GLP-1 explicitly as an expand-at-first-use acronym. The cost lands in E, not here.
- Watch items, not scored: line 29 "consistent capture, comparable records, access for review teams" is a three-item list, but it is the article's own three requirements (line 99), not an adjectival punch triad, so it is outside the banned pattern. Line 25's "more by X than by Y" sits near the corrective-contrast rule (rule 9) without being dismissive.
- Two checks could not be run: the rubric's social override (compare against 3+ posts in `past-posts/facebook-company/`) — folder does not exist; and `detect-ai-tells.py` — this QC pass has no Bash. Both are recurring infrastructure gaps, neither is post-drafter's fault.

### D. Format & structure — 3/3
- All 6 required frontmatter fields present including `product: fitxpress`, plus useful extras (`handle`, `article_url`, `vertical`, `format`). `article_slug: glp-1-market` matches publish-package and live frontmatter.
- Path correct: `workspace/social/articles/glp-1-market-hub/facebook-company/post.md`.
- **Char count verified independently at 1191**, self-report on line 20 is exact, inside the 800-1200 band.
- `manifest.json` correct: own `facebook-company` entry only, canonical schema (`profile_id` / `platform` / `handle` / `post_file` / `status` / `format`), exactly one length field and the right unit for the platform (`character_count_body: 1191`), `profiles_skipped: []`, `ready_for_review: false`, `article.slug: glp-1-market`.
- All 4 design-tip fields present. Minor, not scored: `Angle` (line 18) is a three-clause run-on where the template asks for one sentence.

### E. Output quality — 3/4
- **Copy and visual disagree on a number.** Line 29 promises "three shared needs"; the design tip (lines 43, 46) builds the card on the article's **five** requirement blocks. Both counts are real in the article (three at line 99, five at line 129), but pairing them puts a five-block graphic under copy that says three. This only becomes visible at publish.
- **Weak hook for this platform.** The first 18 words are a spelled-out drug-class name plus a four-item list of delivery models. The expansion is required, so the fix is reordering, not a rule conflict — but on a page whose brief is "broader audience, slightly warmer", the opener reads like a trade brief and nothing pulls a non-specialist past line one.
- **Design tip is a brief, not a tip, and it drifts from the source asset.** `Adaptation` asks to re-lay five blocks horizontally *and* add a new top row of four route labels with connectors — that is a new composition, against the prompt's "Do not suggest something entirely different". `Keep` (line 46) asserts navy `#050F40` ground, `#143DFF` as single accent and Satoshi for `banner_2-2.webp` — the tokens are the correct `DESIGN.md` ones (not `#2962FF`, not Inter), but they are stated as facts about an asset the drafter cannot see.
- Recurrence carried from the twitter pass, unflagged here too: format is `infographic` (an uploaded image) while line 35 puts the article URL in the body, and the article's `og:image` is `cover-3.webp`. Two different images are in play. The coordinator already routed this to Vadim as a publishing-time decision.
- Credit: the post takes a position (line 25) rather than only stating, satisfying rule 6c; FitXpress is scoped honestly to "the remote piece" instead of the whole workflow; the closing question is genuinely answerable by the audience.
- The angle does not use `audience.md` segment 1's hook (visible progress → repeat check-ins → adherence → retention), so the post ends on a taxonomy question with no stake for the reader. Legitimate given the assigned angle, noted for the pack.
- Editing estimate: 10-15 minutes — fix "no hardware", restore the hybrid `may`, resolve three-vs-five, trim the design tip.

## Top 3 issues (приоритет для improver)

1. Line 31 "no hardware" contradicts the post's own `Claims used` line 19 ("no specialized hardware") and the article's "without specialized scanning hardware". The body dropped a qualifier the metadata kept — the wrong direction for the field that publishes.
2. Hedge loss survived in three places the brand-check pass did not cover: hybrid clinics lost `may` (line 27), "keeps the record comparable" lost "consistent capture conditions help" (line 31), and "authorized / appropriate" was dropped from both access statements (lines 27, 29). The delivery-model paragraph was restored; the FitXpress paragraph was not re-checked to the same standard.
3. Copy says "three shared needs", design tip specifies a five-block card. Pick one before the visual is made; the mismatch is invisible in the file and obvious in the feed.

## Coordinator review

