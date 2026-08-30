---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/linkedin-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
coordinator_review:
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/linkedin-company/post.md`
**Total: 16/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5

- Source discipline correct. Line 16 cites `published-live-2026-08-28.md`, not a superseded `draft-v*`; the live URL is on line 17. Both `_run-brief.md` traps (publish-package has no body; drafts no longer match the live page) were respected.
- `linkedin-post-prompts.md` → `## linkedin-company` honoured on every countable item: 267 words inside 180–280 (verified by hand, self-report on line 20 is accurate), 1 emoji, 0 hashtags, third-person/"we" voice with no founder register, CTA to read the full article.
- Run-brief items that are usually missed were hit: `GLP-1` expanded at first use (line 27, `glucagon-like peptide-1 (GLP-1)`), `article_slug: glp-1-market` not the folder name, and the design tip does **not** repeat the twitter post's false "assets avoid photography" claim — line 48 names `cover-3.webp` as photographic and says why it is the wrong reference.
- **Self-check not reported (the shallow step).** `post-drafter` rule 6c requires a one-line self-check before the checker, and `_run-brief.md` §"You cannot call post-brand-checker" instructs the agent to run the 10-point checklist, Part 2 terminology guardrails and the ai-tells hard fails itself **and report the self-check**. Nothing in the artifact reports any of it. Pack-wide: `facebook-company` and `linkedin-nick` also ship without it, so this is a prompt/brief-level gap, not a one-off.
- **Step 4 (read 5+ past posts) unverifiable and not evidenced.** This is the one profile whose corpus path resolves (15 files in `brand-assets/past-posts/linkedin-company/`). Every one of those 15 uses at least one skim device (arrow lists, ✅/→ rows, one-line verdicts); this post uses none. Not proof it was skipped, but nothing in the output shows it was used.

### B. Factual accuracy — 4/5

- Every sourced claim traces to the live page: Reuters/August 2026 segmentation (post line 27 vs article line 69), IQVIA 2026–2030 on oral GLP-1 and combination therapies (line 27 vs article line 71), "Changes in delivery format, pricing, coverage and patient adoption may affect program volume and workflow design" (line 29, near-verbatim from article line 71), the capture spec and `less than 1 cm` repeatability (line 33 vs article lines 145–147), the five requirements (line 35 vs article lines 129–139).
- Claims discipline clean: repeatability is scoped ("for most evaluated measurements", "typical scan-to-scan differences of less than 1 cm"), no single universal accuracy number, no DEXA/scale-replacement claim, no eligibility decisioning, medical framing stated directly ("FitXpress is not a medical device", never "positioned as"). `audience.md` segment 1 "Don't" list respected, no bleed into UK pharmacy compliance. Correct product (`fitxpress`), no invented customers, no anti-positioning claim.
- **Line 29: "each format has its own cadence and duration" is not in the live article and is stated without a hedge.** Grep for `cadence` in `published-live-2026-08-28.md` returns nothing; the article's only use of "duration" is *program* duration (lines 46, 83), never per-format dosing cadence. It is a plausible real-world statement about oral vs injectable schedules, but the run brief says every claim must be traceable to the live text, and this is a treatment-schedule assertion in regulated-adjacent content.
- **Line 29: "one provider may end up running several at once across different delivery routes" is also not on the live page.** The article lists delivery models that exist in the market (lines 44, 91–97); it never says one provider runs several. Hedged with "may", lower risk than the cadence claim, but same traceability problem. Two untraceable claims in one paragraph is what keeps this off 5.
- Proof-points cap deliberately not applied: "30 to 45 seconds" is not literally in `proof-points.md` ("Under 45 seconds"), but it is the live article's own published wording and sits inside that bound. The cap targets invented product numbers; penalising the agent for quoting the published page would penalise correct behaviour. Same reading as the twitter report used for the $200B / 25M figures.
- Cross-reference on line 47 checked and correct: `facebook-company/post.md` lines 44–45 really is a landscape card with four delivery-route labels on the same `banner_2-2.webp`.

### C. Brand & tone — 2/3

- **Two em dashes in agent-authored lines: line 39 ("Explicit but soft — \"Read it here\"") and line 45 ("`banner_2-2.webp` — the five requirements...").** `terminology-guardrails.md` Part 1.7 is "Avoid, always. No exceptions, in any channel… a hard fail at every gate." Line 14 is excluded from the count: the em dashes there come from `post-drafter`'s own heading template. The twitter report in this same pack scored C 3/3 on a file-wide grep showing zero em dashes, so the standard being applied is file-wide, and applying it here costs a point. Same pattern in `facebook-company` line 43 and `linkedin-nick` line 51 — fix belongs in the prompt's design-tip template, not in this one file.
- **The published body itself is clean.** Grep over the file for leverage / utilize / harness / robust / seamless / comprehensive / delve / tapestry / realm / unlock / unleash / game-changing / cutting-edge / revolution / positioned as / objective / by hand / "let" / benefit-"so" / capability-"plus" / "the reader" / "this article": zero matches. No "not just X, it's Y", no triple parallelism, no hashtags, one emoji.
- Voice matches `about-me.md`: "Our view:" is a claim of ownership (licensed use of "our" under guardrail 2.2) and satisfies rule 6c's "take a position somewhere". Buyer framing ("enterprise health operators", "programs") over "you"-spam. Limits stated in the same breath as the capability, per the honest-about-limits fingerprint.
- Watch item, not scored: "Programs that settle that early… Programs that improvise per format…" is a binary parallel contrast sitting near corrective negation. It reads as consequence, not "X, not Y", so it passes.
- Social override: style comparison against 3+ past company posts run. All 15 predate the current house rules (hashtag blocks, emoji-heavy bullet stacks), so divergence from them is correct, not a lapse. Detector `detect-ai-tells.py` not run — this QC pass has no Bash.

### D. Format & structure — 3/3

- Frontmatter complete and correct: `product: fitxpress` present, `article_slug: glp-1-market` matches publish-package frontmatter and the live URL (this is the field the twitter/instagram drafts got wrong), plus useful extras (`handle`, `article_url`, `vertical`, `format`).
- Path correct: `workspace/social/articles/{slug-dir}/linkedin-company/post.md`. All four design-tip fields present. Word count in range and self-reported accurately.
- `manifest.json` follows the canonical schema: only its own `linkedin-company` entry touched, exactly one length field and the right unit for LinkedIn (`word_count_body: 267`), `profiles_skipped: []`, `ready_for_review: false`.
- Non-blocking deviations from the template: `Angle` (line 18) runs three sentences where the template asks for one, and `Live URL` / `Claims used` / `Length` are additions the template does not define. Additive audit trail, consistent across the pack, nothing mandatory missing, so no deduction.

### E. Output quality — 3/4

- **Skimmability is the weakest part.** The profile brief says "Use short paragraphs" and the shared LinkedIn rules say "Strong hook. Short paragraphs. Easy to skim." Paragraph 4 (line 31) is 4 sentences / 57 words and paragraph 5 (line 33) is 5 sentences / 71 words, both unbroken prose with no visual anchor. `about-me.md` sets 2–4-sentence paragraphs. Inside this same pack `linkedin-nick` runs 2-sentence paragraphs on denser material, so this is not a constraint of the topic.
- **~100 of 267 words are close paraphrase or near-verbatim of the source** (paragraph 2 compresses the article's market-structure section; line 29's second sentence is article line 71 almost word for word; line 33's middle sentences track article lines 145–147). The post is not a summary — "Our view: as the formats multiply, the capture method is the one variable that should stay fixed" is genuinely its own thesis — but the connective tissue is lifted, which is what makes it read compiled in places.
- **The FitXpress block is 71 words, 27% of the post, and is the longest paragraph**: capability spec, repeatability figure, then two sentences of boundary language. The brief says business value over product promotion and "never the centre of the post". The boundary sentences are required once the capability is stated; the spec list is what could be trimmed.
- **"GLP-1" appears exactly once, inside the IQVIA citation sentence.** The hook says "obesity-drug market" and the CTA line says nothing. For a GLP-1 hub post on the company page, the topic term is absent from both the pre-"see more" hook and the close.
- Credit: the angle is genuinely distinct from all five siblings drafted before it (market scale, individual check-in record, four delivery models, and the CEO procurement angle), and the design tip verifiably differentiates itself from `facebook-company` on the same asset (square vs landscape, treatment-format chips vs delivery-route labels) instead of duplicating it.
- Estimate: 5–10 minutes of Vadim's editing, all of it structural (break paragraphs 4–5, trim the spec sentence), none of it factual.

## Top 3 issues (приоритет для improver)

1. Line 29: "each format has its own cadence and duration" and "one provider may end up running several at once" are not on the live page. The first is unhedged and is a treatment-schedule claim in regulated-adjacent content. The run brief required every claim to be traceable to `published-live-2026-08-28.md`.
2. Lines 39 and 45: em dashes in the CTA note and the design tip, against `terminology-guardrails.md` Part 1.7 ("no exceptions, in any channel"). Pack-wide pattern — `post-drafter`'s design-tip template needs the ban stated for annotation lines, not just body copy.
3. The required self-check (rule 6c + `_run-brief.md`) is not reported anywhere in the artifact, and paragraphs 4–5 (57 and 71 words) miss the brief's explicit "short paragraphs, easy to skim" while all 15 past company posts use a skim device.

## Coordinator review

