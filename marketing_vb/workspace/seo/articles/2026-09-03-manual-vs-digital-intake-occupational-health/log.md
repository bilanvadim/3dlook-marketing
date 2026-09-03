# Run log — 2026-09-03-manual-vs-digital-intake-occupational-health

| When | Stage | What happened |
|---|---|---|
| 2026-09-03 | plan | `seo-planner` Phase 0-3. `plan.md` + `plan-audit.md` + `checkpoint-1-review-package.md`. Checkpoint 1 approved by Vadim: title, primary keyword, 12-section outline. `plan.md` carries `status: approved`. |
| 2026-09-03 | write | `draft.md`, 2,922 prose words, 12 H2s, 10 claim markers. Sources opened directly during the run: OSHA Appendix C (HTTP 200, confidentiality/timing/routing language quoted from the page), NHANES anthropometry PDF (5.5 MB, downloaded and converted, waist protocol read from Chapter 3 and the examiner/recorder role from section 1.5), EEOC guidance (HTTP 200, conditional-offer passage quoted). `bls.gov` returned HTTP 403, so the JOLTS hires figure is carried from `plan-audit.md`, which verified it the same day. |
| 2026-09-03 | lint (draft) | `article_lint.py`: 8 of 9 gates ok. FAIL on prose length only, 2,922 vs band 2,125-2,875. Detector CLEAN, density 0.64/1000. |
| 2026-09-03 | edit | `final.md`, 5 passes. 177 prose words cut (Section 4 -85, Section 9 -40, FAQ -30, Section 7 -19). Two corrective negations rewritten. Landed at 2,745, which is +9.8% on the 2,500 target and inside the publisher's +/-10% band. |
| 2026-09-03 | lint (final) | `article_lint.py` VERDICT PASS, exit 0, all 9 gates. Detector CLEAN, 0 hard fails, 0 house-rule violations, density 0.34/1000, rhythm variation 0.73. |
| 2026-09-03 | publish | `publish-package.md`. Meta title 57 chars, description 156 chars, 3 variants each. SEO checklist 14/15 with one item flagged for Vadim (medical-framing wording), strategy checklist 9/9. Alt-text suggestions for two illustrations. 5 open items. |
| 2026-09-03 | qc (judgment) | `workspace/_quality/seo/2026-09-03-seo-full-manual-vs-digital-intake-occupational-health.md`, 19/20, scope limited to judgment because both scripts had already gated the mechanics. |
| 2026-09-03 | STOP | Checkpoint 2. Waiting on Vadim: full text plus meta together, and the medical-framing ruling. |

## Deviations from the plan, both declared

1. Section 1 H2 shipped as "The intake step is where screening programs lose time" instead of the
   planned "The intake step, not the examination, is where screening programs lose time". The
   planned form is corrective negation in a heading, which the terminology guardrails restrict to
   real product, clinical, legal or regulatory boundaries.
2. Section 5 H2 shipped as "Manual vs digital intake, compared dimension by dimension" instead of
   "Manual and digital intake compared, dimension by dimension". The plan assigns the primary
   keyword's H2 occurrence to Section 5 and the planned wording does not contain the exact string,
   so the keyword-placement gate would have failed.

## Deviation from `plan.md` taken on the run brief's instruction — REVERTED 2026-09-03

The writer wrote the medical-device boundary directly, "FitXpress is not a medical device.", in the
Section 1 scope note, because item 7 of the run brief instructed that form, and it flagged the
conflict with `plan.md`, `CLAUDE.md` sections 6 and 15, the context pack and the `seo-publisher`
checklist, all of which prescribe the licensed "It is not positioned as a medical device." restored
2026-09-02 by Review 1 and Vadim's call.

**The brief was wrong and the flag was right.** Its stated reason, that the detector hard-fails on
the "positioned as" form, does not hold: `detect-ai-tells.py` carries the lookahead
`(?!a\s+medical\s+device\b)` specifically to license that sentence, and its remediation string
tells the author to write it verbatim. The scope note was restored to the licensed sentence in
`draft.md`, `final.md` and `publish-package.md` after the run; `article_lint.py` and
`detect-ai-tells.py` were re-run and both still pass. "Positioned as" appears nowhere else in the
article. The rule has now flipped three times across five files, which is carried to Vadim as open
item 1 - not as a blocker on this article, but as a question about where the rule should live.
