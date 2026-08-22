---
qc_date: 2026-08-21
agent: post-drafter
artifact: workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/linkedin-katerina/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
coordinator_review: "agreement: ✅ agree | top_issue: none — unsourced MHRA claim caught by QC and removed by coordinator before proceeding"
revision: recheck (supersedes 14/20 initial QC)
---

# QC Report — post-drafter — 2026-08-21 (REVISION RECHECK)

**Artifact:** `workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/linkedin-katerina/post.md`
**Total: 20/20** — excellent

> **This is a revision recheck.** Initial QC scored 14/20 (marginal) on a single substantiation violation: an unsourced "As the MHRA tightens scrutiny of remote GLP-1 prescribing" claim on line 24. The coordinator removed that claim and reworded the UK paragraph. This recheck re-runs the full rubric on the corrected artifact.

## Fix verification

- **MHRA / named-regulator claim: gone.** Line 24 now reads "For UK operators this matters more than most. The buyers I speak with are changing what they expect from a measurement layer. They want data repeatable enough to show real change over time and defensible enough to hold up in an audit, positioned as support for clinician review rather than a decision made by software." No named regulator, no "tightens scrutiny" event, no unsourced regulatory assertion.
- **No other unsourced facts introduced.** Full sweep against `publish-package.md`: seven categories and names (connected scales, professional BIA, DXA, mobile body scanning, manual measurement, photos, wearables) match §6 FAQ exactly; "no single best tool" matches the article's central finding; FitXpress "support layer for clinician review, not a substitute" matches §6 positioning; "repeatable enough to show real change over time" maps to the article's <1 cm repeatability / longitudinal-comparison framing; "defensible enough to hold up in an audit" / "a regulator can trust" are generic buyer-expectation framings consistent with the FAQ's regulatory-status language, not new fact claims. Product correctly tagged `fitxpress`. No numbers cited, so no proof-points exposure.

## Scores

| # | Category | Score | Max | Δ from initial |
|---|----------|-------|-----|-----|
| A | Adherence | 5 | 5 | +2 |
| B | Factual accuracy | 5 | 5 | +3 |
| C | Brand & tone | 3 | 3 | 0 |
| D | Format & structure | 3 | 3 | 0 |
| E | Output quality | 4 | 4 | +1 |

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. The MHRA removal cleared the only prior adherence gap (the "where the article supports it" conditional on the UK lens, `linkedin-post-prompts.md` line 98, and the never-invent rule, line 37). Everything else in the katerina brief executes: broader industry shift (line 18), one strategic observation (line 22 "no single best tool" reframe), why the market is changing (line 24), what enterprise buyers expect (line 24), natural single FitXpress mention (line 26), UK lens applied as soft geo framing without an unsupported regulatory event, founder register (calm/executive), ends inviting to the article (line 28), no MT/US/EU framing, no product features/pricing, word count ~238 within 180–250.

### B. Factual accuracy — 5/5
- All facts trace to the source article. No fabrication, no unverified numbers (none cited), correct product, no anti-positioning lead ("most accurate" appears only as the framed *wrong* question, line 22). The prior substantiation violation is resolved.

### C. Brand & tone — 3/3
- No banned words. No em-dash rhetoric (post uses commas). No "not just X, it's Y". No triple parallelisms (only doublets: "repeatable enough ... defensible enough"; "worth attending and ... worth trusting"). Zero emoji (within 1–2 ceiling), no hashtags. Founder voice on-brief.

### D. Format & structure — 3/3
- Frontmatter complete with `product: fitxpress`, `status`, `profile`, `article_slug`, `created`. Correct path per CLAUDE.md §9. Full template (Angle / Goal / body / CTA / Design tip with all four fields).

### E. Output quality — 4/4
- Publishable as-is. Strong skimmable hook on line 18 (visible before "see more"), unique founder market-maturity angle rather than a summary, natural product mention, soft CTA.
- Minor non-blocking polish nit (not a deduction): the clinician-review framing echoes across two consecutive sentences — line 24 "positioned as support for clinician review rather than a decision made by software" then line 26 "a support layer for clinician review, not a substitute for it." A one-line founder tightening would remove the repetition; does not prevent as-is use.

## Top 3 issues (priority for improver)

1. None blocking. Prior top issue (unsourced MHRA claim) resolved.
2. Optional polish: de-duplicate the back-to-back "clinician review" framing (lines 24 and 26).
3. n/a

## Coordinator review

agreement: ✅ agree
top_issue: none remaining — the unsourced MHRA "tightens scrutiny" claim QC flagged (14/20) was a real substantiation violation; fixed by removing the named-regulator claim and rewording to a generic buyer-expectation framing. Good catch by QC, worth noting for agent-improver that post-drafter should default to generic/soft regulatory framing on personal-voice profiles unless the source article explicitly names the regulator.
