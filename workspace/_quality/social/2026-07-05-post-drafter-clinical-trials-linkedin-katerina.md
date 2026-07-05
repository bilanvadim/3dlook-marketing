---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 10/20
status: failed
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-katerina/post.md`
**Total: 10/20** — ❌ Failed

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 1 | 5 |
| B | Factual accuracy | 1 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 1/5
- `post-drafter`'s declared tool set is `Read, Write, Grep, Glob` — no web-access tool. The post's Angle (line 13) and body paragraph (line 22) assert two specific, dated regulatory facts — "MHRA became a full ICH member in 2022" and UK trial regulation "now folds in ICH E6(R3)" (implying the April-2026 fold-in referenced in the task brief) — that appear **nowhere** in the source article (`publish-package.md`, all versions `v1`–`v3`), nowhere in `CLAUDE.md`, nowhere in `brand-assets/product-info/` (`proof-points.md`, `compliance.md`, `messaging.md`, `icp-detail.md`), and nowhere in `brand-assets/social-profiles-config.md`. Those sources only ever instruct agents to reference "MHRA" as generic UK regulatory flavor (e.g., `social-profiles-config.md` line 125: "references UK regulation (MHRA, CQC)") — none of them state MHRA's ICH membership status or date, or any UK-specific ICH E6(R3) adoption timeline. The source article's own ICH E6(R3) anchor (`draft-final.md` / `publish-package.md`, "Time-stamped measurement records" section) was verified live during the SEO pipeline's Phase 1 fact-check as a **general/international** GCP framework reference — it makes no UK-specific or MHRA-specific claim at all.
- This means the claim was either (a) sourced via an undeclared tool (web search, outside the agent's permitted toolset) or (b) generated from parametric knowledge with no verification step — both are process violations. Per the algorithm, step 3 says "Read the article" for claims/numbers; there is no step authorizing external research for new factual assertions.
- Hard Rule #1 in the agent's own prompt: *"Never invent numbers or case studies. Only what is in the article or `product-info/`. Need a stat — take it from the article."* A specific regulatory/legal claim with specific dates is the same category of risk as an invented number or case study, and it was not sourced from either permitted location.
- Everything else in the algorithm was executed correctly (CLAUDE.md read, profile block read and applied, article read for the non-regulatory angle content, template followed) — this keeps the score off 0, but the scope violation on the single most legally sensitive line in the post is severe enough to cap Adherence near the bottom of the scale.

### B. Factual accuracy — 1/5
- Per the task's specific scrutiny: this is a checkable regulatory/legal claim about to publish under the CEO's byline (Katerina Galich), and it is **not traceable to any approved internal source** (`proof-points.md`, `compliance.md`, or the source article). Per the Facts→Copy→Review principle this pipeline operates on, content agents must not introduce unverified external regulatory/legal claims outside the approved-source chain — this holds regardless of whether "MHRA became a full ICH member in 2022" or the April-2026 ICH E6(R3) fold-in date happen to be factually correct. The risk is the sourcing gap, not (necessarily) the underlying fact.
- **This is the top issue in this report.** A wrong regulatory/legal claim under the CEO's name carries real reputational and possibly legal risk (readers in UK clinical-trial/regulatory-affairs roles are exactly the audience most likely to notice and call out an incorrect MHRA/ICH claim). Vadim should independently verify this claim — or route it to legal/compliance for verification — before this post is approved for publishing, regardless of the score assigned here.
- No other invented numbers, case studies, or client names were found elsewhere in the post — the rest of the copy (commoditization argument, audit-trail differentiator framing) draws on the source article's own ICH E6(R3)/FDA DHT framing and doesn't introduce additional unsourced claims. That containment is the only reason this category isn't scored 0.

### C. Brand & tone — 3/3
No issues. Zero banned words from `messaging.md` (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). No em-dash in a rhetorical construction and no "it's not just X, it's Y" pattern in the post body (the only em-dash in the file is in the markdown H2 title separator, not prose). First-person founder voice throughout, matching `social-profiles-config.md`'s `tone` field ("Founder voice... Strategic, visionary, AI risk-aware. First person"). Correctly avoids the profile's `avoid` list — no Mobile Tailor content, no US regulatory framing (no FDA mention), no EU-specific framing, no pricing/feature granularity.

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path (`workspace/social/articles/{slug}/linkedin-katerina/post.md`). Body copy (lines 18–26) is ~1,300 characters, within the profile's specified 1000–1500 char range. CTA ("Curious what you think; happy to share more on this") matches the profile config's specified soft CTA pattern exactly. Design tip block has all 4 required fields (Article visual / Format / Adaptation / Keep), correctly derived from the source article's Section 4 OG image direction.

### E. Output quality — 2/4
- The opening hook (line 18, ~130 characters, visible before LinkedIn's "see more" cutoff) is strong and on-brand for founder thought leadership.
- However, the post is not usable as-is: the regulatory anchor claim (line 22) is the load-bearing sentence for the entire angle — "the UK's clinical research sector is well placed here" and the whole "real regulatory anchor" argument in paragraph 3 depend on it being true. If the MHRA/ICH claim is wrong or imprecise, the post's central argument collapses, not just one detail. This is a publish-blocker, not a copy-edit: it requires an external verification step (legal/compliance or Vadim) before this can move to approval, which is a materially higher bar than "5-10 minutes of editing."
- Net: solid idea and craft, undermined by a sourcing gap on the sentence the whole post pivots on.

## Top 3 issues (приоритет для improver)

1. **[Sourcing / factual-accuracy risk — top issue]** Post asserts "MHRA became a full ICH member in 2022" and that UK trial regulation "now folds in ICH E6(R3)" — a specific, checkable regulatory/legal claim with no traceable source in `proof-points.md`, `compliance.md`, the source SEO article, or any other approved internal document. This appears to have been sourced via a tool outside `post-drafter`'s declared toolset (Read/Write/Grep/Glob), violating Hard Rule #1 ("never invent numbers or case studies... only what is in the article or product-info/"). Publishing this under CEO Katerina Galich's byline without independent legal/compliance verification carries real reputational risk if the claim is wrong or imprecise. **Recommend: do not approve as-is — verify the claim independently (or strip it and re-anchor the post in only what `publish-package.md`'s already-verified ICH E6(R3) reference supports) before this goes to Vadim's Telegram approval.**
2. Process/scope violation: the agent operated outside its permitted tool scope to produce this claim, which the algorithm never authorizes (no step permits new external research for facts not in the article or `product-info/`). This is a repeatable failure mode worth flagging to `agent-improver` — the prompt should explicitly state "no web search / no external research; if a needed regulatory fact isn't in the article or product-info/, STOP and ask Vadim," mirroring CLAUDE.md's global rule ("Если контекста не хватает — стоп и вопрос. Не выдумывать числа, кейсы, имена").
3. Minor: the post's core argument (audit-trail/standardization as differentiator) is otherwise sound and directly inherits the source article's already-fact-checked ICH E6(R3)/FDA DHT framing — once the MHRA-specific claim is removed or verified, the rest of the post needs little to no rework.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
