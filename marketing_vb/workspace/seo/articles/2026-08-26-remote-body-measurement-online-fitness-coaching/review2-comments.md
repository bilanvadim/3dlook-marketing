---
artifact: review2-comments
slug: remote-body-measurement-online-fitness-coaching
source_doc: https://docs.google.com/document/d/18OTBvrxBuDgvU7MLBVL7Yd5Odh6v7RHgA3rqqhzwYpE/edit?tab=t.drn1yvk966qf
source_tab: "Review 2"
reviewed_version: review2-version2.md (== draft-v3-revision1.md, the Version 2 tab)
synced: 2026-08-31
status: verbatim copy of the reviewer's text, no edits
vadim_ruling: "всі формулювання тут точні і бери як головний істочнік" (2026-08-31) — this document
  outranks the internal guardrail files on WORDING for this article, including the medical-device
  phrasing that revision 1 declined. See item 1.
---

# Review 2 — verbatim

The updated version is substantially stronger and now fulfills the brief much better. I would rate it around 8.5/10. It needs one more focused revision before publication, mainly for factual precision, repetition, and corporate-language compliance.

| Area | Status |
| :- | :- |
| Remote coaching focus | Fixed |
| Differentiation from the fitness hub | Fixed |
| Structure and workflow logic | Fixed |
| Measurements versus estimates | Mostly fixed |
| Unsupported retention claims | Fixed |
| Coaching-decision table | Fixed |
| Pilot-evaluation value | Fixed |
| Method comparison | Improved, with corrections needed |
| Privacy/legal wording | Partially fixed |
| Medical-device wording | Still incorrect |
| Length and repetition | Still needs work |

## Required corrections

1. **Use the approved medical-device wording.**
   The front matter says the content agent deliberately rejected the reviewer's wording because of its internal terminology guardrail. That is unacceptable because the corporate instruction takes precedence.
   Use:
   FitXpress is not positioned as a medical device.
   Apply this in the scope note and limitations section.

2. **Remove the GLP-1 reference.**
   "It has no role in glucagon-like peptide-1 eligibility" introduces an unrelated healthcare keyword and conflicts with the cannibalization guardrail separating fitness from GLP-1 content. The general diagnosis, treatment, and eligibility boundary is sufficient.

3. **Correct the Smart Scales workflow description.**
   The article says "the software flags a difference" when self-reported weight is supplied. This is too definite. The platform can compare self-reported and predicted weight and configure discrepancy logic, but an automatic flag is not universal across every fitness implementation.

4. **Do not imply that model-generated measurements are direct measurements.**
   The output classification is much better, but "the line between a measured value and an estimate" may still suggest that waist circumference is directly measured. Keep the distinction as:
   - model-generated body measurements;
   - software-derived body-composition estimates;
   - calculated metrics;
   - predicted weight.

5. **Define Smart Scales as software.**
   "Read from the images" is imprecise. Clarify that Smart Scales is a software-based predicted-weight output, not a physical scale.

6. **Correct the scale comparison.**
   "A connected scale gives a precise weight" is too broad. Consumer connected scales vary in quality and calibration. Refer to a direct weight reading, or reserve "precise" for a calibrated scale.

7. **Correct the remote-method statement.**
   "None of the three runs remotely across a whole roster" is inaccurate because scales can be used remotely at home. DXA and professional BIA require facility access; home scales do not.

8. **Avoid treating sub-variance changes as confirmed noise.**
   "A movement smaller than the variation is best read as capture noise" is too categorical. It means the difference cannot be confidently distinguished from expected scan-to-scan variation. It is not proof that no physical change occurred.

9. **Add the micro-change limitation.**
   The article should state that mobile scanning is intended for longitudinal trends rather than very small short-term changes.

10. **Fix the legal-basis language.**
    "A coaching program still owns its own consent language" is vague, while the FAQ says programs should always obtain explicit consent. Consent is one possible legal basis, not universally the only one.
    Use the approved role statement:
    In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR.
    Then explain that the customer must establish an appropriate legal basis, provide the required notice, and obtain consent where required or relied upon.

## Content and style refinements

11. Replace "a coach carrying two hundred remote clients" with more natural language such as managing a large remote roster. The number 200 also feels invented.
12. "In place of an in-person intake or check-in appointment" overstates the role. The scan can replace the measurement component, not necessarily the entire appointment.
13. "Self-reported weight moves with hydration" is technically awkward. Body weight or the scale reading varies; the self-reported value simply records it.
14. "A tape held half an inch higher reads as a loss that never happened" is too absolute. It can produce an apparent difference caused by placement rather than body change.
15. "Which removes the parallel spreadsheet" should become a potential operational benefit. It depends on how the platform implements and stores the results.
16. "The fourth column carries the weight" feels editorial and slightly artificial. Remove it and lead directly with the interpretation limitation.
17. "A scan can show that a waist circumference moved" should say it records a measurement difference. Confirming physical change requires reviewing the size of the difference and capture conditions.
18. Change "progress photos…not measurable" to "not inherently standardized or quantitative."
19. "Coach hours are what caps how many clients a program can serve well" is another universal claim. Present review time as a potential capacity constraint.
20. Remove "less to protect" from the best-fit section. It is vague and unnecessarily commercial.

## Evidence and sourcing

The absence of a named coaching customer is acceptable; do not invent one. However, the method-comparison section would benefit from two external sources:

- Support the hydration sensitivity of BIA with relevant [published research](https://pubmed.ncbi.nlm.nih.gov/32182203/).
- Support the need for standardized DXA protocols and acknowledge DXA variability with this [methodology review](https://pubmed.ncbi.nlm.nih.gov/25029265/).

This would strengthen the article without turning it into a research-heavy piece.

## Length and repetition

The body contains approximately 2,980 words, while the front matter says 2,582 and the detector reports 3,015. Recalculate these values after the final revision.

The article can be reduced by approximately 10–15% by consolidating:

- outputs listed in three places;
- accuracy and repeatability repeated in the FAQ;
- privacy repeated in the main section and FAQ;
- "the coach decides" repeated across several sections;
- engagement and retention repeated in the pilot, best-fit, and conclusion sections.

Also remove the internal revision_note, self_check, detector commentary, and discussion of reviewer conflicts before publishing. These are production notes, not article metadata.

After these corrections, the article should be ready for a final proofreading pass.
