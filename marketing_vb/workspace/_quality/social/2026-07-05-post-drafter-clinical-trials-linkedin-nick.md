---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-nick/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-nick/post.md`
**Total: 18/20** — ⭐ Excellent

## Special focus: unsourced-claim check (per sibling failure precedent)

`linkedin-katerina` v1 for this same article failed QC (10/20) for asserting a specific, dated, unsourced regulatory claim ("MHRA became a full ICH member in 2022," a UK ICH E6(R3) fold-in date) that existed nowhere in the source article or `product-info/`. This draft was checked line-by-line against that exact failure mode:

- **Line 18 (opener):** "Every clinical trial buyer conversation I have with US sponsors and CROs eventually lands on... the measurement-only visit." This is a personal-voice anecdote about Nick's own conversations, not an external factual claim — no institution, date, or market statistic is asserted. The `manifest.json` note explicitly frames this as intentional: "Framed as a recurring observation from Nick's own buyer conversations, not a market-size or regulatory-status claim." Consistent with the accepted personal-opinion framing used in the `linkedin-katya` draft that scored 18/20 on this same check.
- **Line 20:** "monitoring window that can stretch past twelve months" and the coordinator-variability sentence trace directly to `publish-package.md` v3 lines 430 ("Documentation conventions can drift over a twelve-month study" / "A trained coordinator at one site may measure waist circumference slightly differently from a trained coordinator at another site") and line 439 ("study window can run twelve months or longer"). No number, date, or institution beyond the article.
- **Line 22:** "The FDA's guidance on digital health technologies for remote data acquisition already gives sponsors a framework to work inside of." Matches the article's own citation (line 505, `FDA DHT guidance... final, December 2023`) — but critically, the post does **not** repeat the FDA guidance's date or make any regulatory-status assertion beyond what the article already states. This is the exact category of claim that sank `linkedin-katerina` v1 (a dated regulatory fact), and here it is deliberately left unspecific/hedged.
- **Line 24:** "Not a DEXA replacement, not an endpoint-validation tool" — a direct, correctly-scoped restatement of the article's own compliance guardrails (`no_dexa_alternative`, `no_endpoint_validation_claim`, Section 11 of `publish-package.md`), not an invented positioning claim.
- **No named CROs or sponsors** (e.g., IQVIA, Parexel, PPD) are used, despite being listed as target examples in `fx-clinical-trials.md` — the `manifest.json` note explains this was a deliberate choice "to avoid implying a customer relationship that isn't sourced." No client names, no case studies, no market-size figures ($10-40M TAM from `fx-clinical-trials.md` is correctly omitted rather than casually dropped into BD copy).
- **Conclusion: the sibling failure mode does not recur here.** Every checkable claim traces to the source article or is explicitly framed as personal opinion/observation, consistent with the corrected pattern established in `linkedin-katerina` v2 and `linkedin-katya`.

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
No issues. `CLAUDE.md` tone/no-go rules applied. Profile block (`linkedin-nick`, `social-profiles-config.md` lines 168-192) correctly read and honored: `product_bias: 100% fitxpress`, tone ("BD practitioner... First person"), length 800-1400 chars, soft CTA pattern ("Happy to share more" + article in comments — line 26 matches verbatim). `avoid` list respected: no European regulatory context, no fashion/apparel content, no generic promo copy. `brand-assets/past-posts/linkedin-nick/` is empty — correctly handled per the prompt's edge case ("if empty, continue without them, do not STOP") and documented in `manifest.json` rather than silently skipped. Article (`publish-package.md` v3) read for claims and Section 4 OG image brief. Minor observation (not a deduction): `linkedin-nick`'s listed `icp_focus` (telehealth, GLP-1 platforms, online pharmacies, insurance) does not explicitly name "clinical trials/CROs," but CROs/pharma sponsors are a documented FitXpress ICP segment in `CLAUDE.md` §4 and `fx-clinical-trials.md`, and the profile's `content_types` ("US market angle on the article," "relevant pain point for US buyers") is broad enough to cover it — a reasonable adaptation, not a scope violation.

### B. Factual accuracy — 5/5
No issues. All claims trace to `publish-package.md` v3 (see special-focus section above for line-level mapping). No invented numbers (no percentages or figures used at all — no exposure under the proof-points hard rule since no number appears in the post), no invented case studies or client names, no dated regulatory claim added beyond the article's own citation. No compliance-guardrail violation: correctly disclaims DEXA-replacement and endpoint-validation, matching Section 11 of the publish package.

### C. Brand & tone — 2/3
- Line 24: *"Not a DEXA replacement, not an endpoint-validation tool — a standardized way to capture the measurement step across sites, staff, and timepoints..."* Two parallel negations followed by an em-dash introducing the "what it actually is" clause is structurally close to the banned AI-signature family in `CLAUDE.md` §6 ("em-dash in rhetorical constructions," of which "X — it's not just Y" is only the given example, not the only instance). It stops short of the literal "not just X, it's Y" template, but the shape (negate, negate, em-dash, define) is the same rhetorical tic.
- The other em-dash in the post (line 20: "measurement — BMI, waist and hip circumference, body composition —") is a lower-risk parenthetical list-separator, not a rhetorical contrast — noted but not scored.
- No banned words from `messaging.md` found (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). "Across sites, staff, and timepoints" (line 24) is a triple, but it is lifted near-verbatim from the article's own phrasing (`publish-package.md` line 496: "inconsistent across sites, staff, and timepoints"), not an invented adjective triad — not counted as the banned "fast, reliable, scalable" pattern.
- Style-consistency check against `past-posts/linkedin-nick/` (per rubric's Social-post override) could not be performed — the folder is empty. No penalty applied; documented as N/A.

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path. Template fully followed (Angle / Goal / body / CTA / Design tip with all 4 required fields). Body copy measures 1,320 characters — within the profile's 800-1400 char range. Design tip accurately quotes the Section 4 OG image brief (multi-site dot-map motif, guided two-photo capture icon, timestamp/structured-record icon, dark teal-blue palette) and correctly identifies the article's actual comparison table ("Scan-based capture vs manual anthropometric measurement") as the infographic source.

### E. Output quality — 3/4
- Opening line is a specific, credible hook ("the same unglamorous line item: the measurement-only visit") that lands before LinkedIn's "see more" cutoff and sets up a distinct angle (operational layer beneath the FDA framework) rather than restating the article's regulatory framing wholesale.
- Line 24's disclaimer-then-pitch construction ("Not a DEXA replacement, not an endpoint-validation tool — a standardized way to...") reads slightly more like a compliance checklist than natural BD voice — functionally correct and necessary (it satisfies the article's own scope guardrails) but a touch stiff for a first-person LinkedIn post.
- Net: publish-ready with a light polish pass (soften the line-24 construction per the C-category note) rather than a substantive rewrite.

## Top 3 issues (приоритет для improver)

1. Line 24: negation-negation-em-dash construction ("Not a DEXA replacement, not an endpoint-validation tool — a standardized way to...") is a mild AI-signature pattern — rework as two sentences or drop the em-dash to avoid the "negate, negate, define" tic.
2. Minor: the disclaimer-then-pitch sequence in line 24 is functionally correct (required by the article's compliance guardrails) but reads slightly stiffer than the rest of the post's BD voice — a candidate for a more conversational rephrase in a future iteration.
3. Process note (not a defect): `past-posts/linkedin-nick/` remains empty, so the Social-post rubric's style-consistency-vs-history check cannot be applied to this or future `linkedin-nick` drafts. Flag to Vadim to seed 5-10 reference posts for this profile.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
