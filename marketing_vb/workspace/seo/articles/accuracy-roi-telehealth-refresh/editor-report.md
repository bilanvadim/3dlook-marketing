---
slug: accuracy-drives-roi-digital-health
workspace: accuracy-roi-telehealth-refresh
stage: final
input: draft-v1-writer.md
output: final.md
editor: seo-editor
date: 2026-09-23
---

# Editor report, final

## Gates

- `article_lint.py final.md --pack …/accuracy-roi-telehealth-refresh.yaml`: **PASS**, all 10 gates `ok`. The second run passed. The first failed on a single detector hit, `claims_discipline` "Diagnosis", in my own rewording of S7, which is now fixed.
- Detector (`--channel article`): **CLEAN**, AI density 0.0/1000. Density was already 0.0 before editing.
- Prose words: **2,161** against a target of 2,150 (band 1,827-2,472). The writer's draft had 2,135.
- Sentence length: mean 11.9 words, none over 25 or 35 words. Near-duplicate pairs: none. Repeated phrases: none.

## Lint findings from the draft

| Finding | Resolution |
|---|---|
| L43~L138 (1.00) | S7 now reads "Inside the program, the scan record is one input to clinician review. Clinical decisions, including treatment eligibility, remain with the care team." The scope note keeps the canonical intended-use sentence. |
| L140~L180 (0.75) | FAQ 4 no longer repeats the 30-day figure (plan S9: "prefer none"). It says photos and results follow different rules and adds FXS-IDS, which the body does not state. |
| L147~L159 (0.62) | S8 bullets are rewritten. The self-report list had said "no threshold depends on it" twice. The third guided-capture bullet now names an observable symptom: patients stop at verification while they wait for a call or visit. |
| L138~L168 (0.53) | The two FAQ questions that S7 and the scope note already answer are merged into one, "Is scan data used to decide eligibility or medication dosing?". This keeps the decisioning FAQ required by §14. The FAQ now has 3 questions instead of 4. The editorial-rewrites §2 rule to drop FAQ questions that a section already answers outranks the plan's count. |
| "a guided scan" x4 | Now 0. The replacements are "guided mobile capture" (S4), "the first scan" (S6) and "a scan" (FAQ). The FAQ that used it was merged away. |
| "the current workflow" x3 | Now 1, in the S8 pilot. S5 says "the existing process". Next steps reworded. |

## Writer-flagged items

- **(a) The reframe.** "Rarely comes from X alone. It comes from Y" read as corrective contrast. It now reads: "Most of the return from better body data comes from fewer manual touches per patient, at a data quality the program's review workflow accepts. Accuracy matters as far as it lets a reviewer accept a record without checking it again." This keeps "accuracy" in the argument without the negation.
- **(b) Accuracy short form.** Accepted. The S7 accuracy paragraph and the S6 repeatability sentence match `accuracy-formulations.md` §5 verbatim, and §5 is approved on a par with §1. The two sections are not mixed within any paragraph. The framework link sits in the same paragraph in both S6 and S7. There is no ISO figure on the page.
- **(c) Photo deletion.** Kept in S7 as written: "immediately after processing, or within 30 days under the customer's policy", sourced from compliance.md. FAQ 4 summarizes it without the figure.
- **(d) Yazen.** Left cut.

## Baseline defects (pack `refresh.defects_to_remove`)

A grep of the final body finds none of the following: compliant, medical-grade, "Dose medications", altered photos or fraud, eliminates, "80+ body metrics", objective, "Regulatory bodies", robust, Disruption, Moreover, "rather than", em or en dashes, "in-house R&D", "weeks, not months", "1,000 to 100,000", "automatic photo deletion", 16h/1.25h/93%, 20%, "$5-6 million", "ten minutes". The only em dashes in the file are in the frontmatter `hub` strings copied from the plan. HIPAA and GDPR use FXS-HIPAA and FXS-GDPR verbatim, with a link to the trust FAQ.

## ROI section check

The ROI section contains no outcome number supplied by 3DLOOK. It uses named variables only (`P m e x c d a s`). The one vendor-side input, `s`, comes from the program's own quote. The section says outright that 3DLOOK supplies no outcome figures. I also removed the keyword-filler sentence ("any health ROI or digital care ROI case") and put a caveat in its place: one-time integration and training costs sit outside the two lines, and they belong in the pilot column when a payback period is needed.

## Figures in the body

- CDC: 40%, 5.3% vs 8.8%, 2020 data. The *Preventing Chronic Disease* 2023 inline link is unchanged.
- 45 seconds (FXS-SPEED), 80+ body measurements (FXS-OUTPUTS), 96-97% and 1.5-2.0 cm (FXS-ACCURACY §5), below 1 cm (FXS-REPEAT §5), 30 days (compliance.md).

Nothing else.

## Other edits

- The opening H2 almost duplicated the S3 H2. It is now "Patient volume and the staff time behind body data".
- The intro's triple "checking, chasing, or re-entering" is now "a second check or a re-entry".
- The audience sentence is merged into the previous one: "an operations question for program leaders at …".
- S3's population caveat is now a positive statement: "the gap in a single submission can be larger or smaller".

## For the publisher and digest

- The byline stays Vadim Bilan, per the pack's `live_byline`. Flag this in the digest.
- The slug is unchanged: `accuracy-drives-roi-digital-health`.
- `BAA` is not expanded, because it sits inside the verbatim FXS-HIPAA sentence. The M1 gate passes. If the web editor wants it expanded, write "business associate agreement (BAA)" and leave the rest of the sentence unchanged.
- The FAQ count changed from 4 to 3 (see above). The FAQ schema should use 3 entries.
