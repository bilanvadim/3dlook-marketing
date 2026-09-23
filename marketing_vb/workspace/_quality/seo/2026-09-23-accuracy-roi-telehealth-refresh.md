# QC Report — accuracy-drives-roi-digital-health (refresh in place)

**Slug:** accuracy-roi-telehealth-refresh
**Date:** 2026-09-23
**Context:** Refresh-in-place of a live article that dropped from the index 20.09; old version had compliance violations and unverifiable numbers (NHANES/PLOS/40%-no-scale/93%/20%/$5-6M), now removed. Byline Vadim Bilan retained by instruction. FAQ intentionally trimmed 4→3 by editor (duplicate questions merged).

## A. Adherence to plan and intent — 5/5

All 10 outline sections are present and each does what it promised; nothing extraneous was added.

- Section 3 ("Where the manual work comes from as a program grows") delivers exactly the promised breakdown: *"That check creates four kinds of manual work: Verification checks and exception review... Resubmissions... Follow-up measurement... Documentation after the fact."*
- Section 4 delivers the promised four-method comparison with operationally useful columns ("Typical failure mode", "What a reviewer can see afterwards", "Best fit in the program") rather than a generic feature table.
- Section 7 ("Where FitXpress fits, and where it does not") literally structures both halves of its own title — the "does not" half is substantive, not decorative: *"FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population."*
- Keyword "digital health ROI" is worked naturally into the title and into the Section 5 heading ("A digital health ROI model the program fills in" — a minor, sensible rewording of the outline's "A transparent ROI model the program fills in"; the "transparent" idea survives in-copy: *"3DLOOK does not supply outcome figures for this model, because the inputs differ by program."*).
- FAQ trim (4→3) was a pre-approved editorial decision per coordinator note, not a plan deviation — outline only specified an FAQ section, not a count.

No intent drift: the piece reads as an operations-framed MOFU explainer with an honest BOFU product section (7) and a standard next-steps CTA (10) — consistent with a "digital health roi" head-term target.

## B. Factual accuracy — 5/5 (per code verdict, not re-checked)

Lint PASS, detector 0.0/1000 with empty hard_fails, mechanical checklist 17/17. Writer-notes confirm the CDC *Preventing Chronic Disease* 2023 stat was independently opened via WebFetch, and the unverifiable NHANES/PLOS/40%-no-scale/93%/20%/$5-6M figures from the old live version were removed rather than carried forward. Approved-claims usage spot-checked while reading (FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-HIPAA, FXS-GDPR, FXS-IDS, FXS-RETENTION, FXS-SCOPE, FXS-MEDICAL) all match their approved wording closely, no "most accurate" leadership claim anywhere.

## C. Brand & tone — 3/3

No banned words found (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge — none present).

- Strong expert-voice reframe, not filler: *"Accuracy matters as far as it lets a reviewer accept a record without checking it again."*
- Honest, non-generic admission that a compiled template wouldn't volunteer: *"3DLOOK does not supply outcome figures for this model, because the inputs differ by program. The model shows what to measure."*
- Hedges are calibrated, not smothering — e.g. *"approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part"* — precise about uncertainty without hedge-stacking.

Minor stylistic tic (not enough to dock a point, but worth flagging for agent-improver): the internal-link sentences are formulaic and repeat near-verbatim five times — *"...is covered in the telehealth AI overview,"* *"...is described in the guide to remote BMI verification methods,"* *"...are covered in the GLP-1 market overview,"* *"The case for that link is made in the article on...,"* *"...describes the test conditions,"* *"...sets out the reference and conditions..."* — same "X is covered/described in Y" skeleton reused across ~2160 words reads as templated on close reading.

## D. Format & structure — 3/3 (per code verdict, not re-checked)

Mechanical checklist 17/17 ok; lint PASS at 2161/2150 words (essentially on target).

## E. Output quality / value — 4/4

Ready to ship as-is; has a genuinely differentiated angle a generic ROI-content template would not produce.

- The explicit ROI framework is a real operational model, not vendor filler: *"Monthly handling cost = P × (m + e × x) × c ÷ 60"* with a full variable table (P, m, e, x, c, d, a, s) telling the reader exactly what to measure and where each figure comes from.
- The disability-population caveat is a limitation disclosure a sales-first template would omit: *"This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path."*
- Precise, product-literate operational detail: *"For weight checks, the program compares BMI from the scan's weight estimate with BMI from self-reported weight. Both use the same supplied height. The program sets the threshold and reviews the exceptions."* — only someone who understands the actual product flow writes this.

## Total: 20/20 — Excellent

**Verdict: ship**

## for_agent_improver

1. **seo-writer/seo-editor:** the "X is covered in / described in / sets out" internal-link connective is reused near-verbatim 5-6 times in this piece. Vary the phrasing per link (or vary sentence position — lead vs. trail) so cross-links don't read as templated on a close pass.
2. **seo-planner/coordinator:** when an editor intentionally trims a planned sub-count (here FAQ 4→3), log that delta somewhere QC-visible (e.g. a one-line note in the package or checklist) — I only knew this wasn't a plan violation because the coordinator told me out of band in this prompt; without that note this would have looked like a dropped outline item.
3. **Worth reusing as a positive pattern:** the "3DLOOK does not supply outcome figures for this model... the model shows what to measure" framing (honest about what the vendor won't claim) is a strong template for other ROI/product-fit sections — flag it to seo-writer as a model example for future refresh jobs that need to sound expert rather than promotional.
