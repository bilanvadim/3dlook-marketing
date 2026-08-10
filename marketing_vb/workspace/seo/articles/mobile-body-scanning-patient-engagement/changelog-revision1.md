# Changelog — Revision 1 (Review 1 comments applied)

> Base: `draft-v4-publisher-final.md`. Output: `draft-v5-revision1.md`. Source of comments: `review1-comments.md` (Review 1 — Legal/Product/Editorial, Google Doc tab "Review 1"). Applied 2026-08-03.

## Highest-priority corrections

**1. Repeatability claim**
- Before: "Scan-to-scan repeatability of `< 1 cm` means a small real change registers as signal rather than measurement noise, so a two-week gain shows up instead of washing out."
- After: "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. Consistent capture conditions help programs compare results more reliably over time." (used verbatim, in the "Five ways it can support patient engagement" section). The two-week-detectability promise is removed, not softened — it does not appear anywhere in the revision.

**2. Privacy section**
- Before: "Photos are deleted immediately or within 30 days under the client's retention policy, photos are automatically blurred when stored, and no names or personal identifiers are processed."
- After: "Production photos are deleted after processing, while structured outputs may be retained according to the customer's configuration and agreement. Data is encrypted in transit with Transport Layer Security (TLS) and at rest. Standard hosting runs through Amazon Web Services (AWS) in the United States, with EU or UK hosting available on request. FitXpress supports Health Insurance Portability and Accountability Act (HIPAA)-compliant workflows, with a Business Associate Agreement (BAA) available where required, and General Data Protection Regulation (GDPR)-aligned data handling." (in "Where FitXpress fits, and where other methods remain necessary"). The FAQ "What data is captured?" answer was updated to match (no more "no names or personal identifiers processed" line).

**3. GLP-1 discontinuation statistic**
- Before: "A 2025 retrospective cohort study in *JAMA Network Open* reported that 64.8% of adults with overweight or obesity and without type 2 diabetes discontinued glucagon-like peptide-1 (GLP-1) receptor agonists within one year..." (in "Why this matters now").
- After: Removed entirely. No substitute statistic was added — this pass had no way to independently verify a new broader source (patient-engagement in virtual care / remote-monitoring adherence / patient-portal engagement), so the section proceeds on the remaining telehealth-adoption statistic (MEPS/*Healthcare*, EXT-TELEHEALTH) plus qualitative framing, per the reviewer's stated fallback ("if no strong broader source is available, the section can work without a second statistic"). Flagged in the publish package delivery notes for Vadim/Asselya to supply an approved substitute if one exists.

**4. Softened cause-and-effect claims**
- "Visible change sustains effort..." → "A body-composition record can help patients recognize that change and give them a reason to keep engaging." (Five ways, motivation bullet)
- "Recurrence scans create a rhythm..." → "Recurring scans can give programs a shared reference and create opportunities for more meaningful check-ins." (Five ways, goals bullet)
- "The engagement loop produces operational effects..." → "Running this loop consistently can support a few operational patterns." (How the scan-to-scan experience works)
- "...gives members a reason to stay and upgrade." → removed; retention language throughout now uses "can support," "may help," "does not guarantee" (e.g., "Visible progress can support repeat check-ins, which may help retention across a program cycle, though it does not guarantee the outcome.")

## Positioning issues

**5. "What FitXpress does NOT do" section**
- Before: standalone H2 section with 7 bullets (diagnose, treatment/eligibility/underwriting, replace clinicians, DEXA/BIA equivalence, guarantee outcomes, fraud detection, medical-device framing), repeated again in FAQ and the closing disclaimer.
- After: renamed and folded into "Where FitXpress fits, and where other methods remain necessary" (sentence case, no em dash — "and" used instead), trimmed to 4 boundaries: supports review rather than diagnosis; does not make clinical or eligibility decisions; does not replace required clinical assessments; does not guarantee engagement or health outcomes. Fraud-detection and underwriting bullets removed (out of scope for this article). Recapped once in FAQ 8, not repeated in the conclusion.

**6. Opening overstates self-report weakness**
- Before: "People misremember, round down, or estimate."
- After: "Self-reported weight and BMI offer a limited view of change. Readings may come from different scales, capture conditions vary, and a single number cannot show how measurements or body composition are changing." (used verbatim, opening section)

**7. "Clinical-facing documentation"**
- Before: "One capture produces both the patient-facing signal and the clinical-facing documentation."
- After: "One capture can support both a patient-facing progress experience and a structured record for care-team review." (used verbatim, "What mobile body scanning adds")

**8. Remote patient monitoring qualification**
- Before: "Remote patient monitoring depends on a reproducible body record for longitudinal check-ins between clinical assessment points..."
- After: "In remote monitoring and longitudinal care programs, recurring scans can provide an additional body-data record between formal assessment points, where consistency across captures matters more than any single reading." (used verbatim, "Applications beyond GLP-1")

## Structural improvements

**9. Section merge**
- Before: three separate H2 sections — "The engagement mechanics of structured body data," "The scan-to-scan engagement loop in practice," "What improves operationally."
- After: split differently per the reviewer's recommended 9-part outline — "Five ways it can support patient engagement" (mechanics, trimmed 6→5) and "How the scan-to-scan experience works" (loop + operational effects + honest limits, merged). Full mapping documented in `plan.md` under "Revision 1 structural update."

**10. Internal links**
- Before: mixed markdown links and a few plain mentions.
- After: all 7 required anchors are live hyperlinks: AI in telehealth (telehealth hub), visual progress tracking for GLP-1 adherence and retention (GLP-1 article — now appears ONLY in "Applications beyond GLP-1," not in the central argument), beyond BMI, mobile body scanning accuracy, FitXpress for telehealth and weight loss, two photos into structured body data, privacy and data-handling terms (`/legal/` — no dedicated privacy/security resource is published yet, so no new URL was invented, consistent with the original plan's note).

## Minor editorial problems

**11. "Section 4" / "Section 10" references**
- Before: "Section 4 covers why each of these matters for engagement" and "Section 10 covers frequency" / "Section 10 covers this in more detail."
- After: removed. "What mobile body scanning adds" now points to the next section by its actual title ("Five ways it can support patient engagement, covered next..."); the loop step and FAQ answer on scan frequency no longer cross-reference by number at all — each stands as a complete, self-contained answer.

**12. BMI over-expansion**
- Before: "Body Mass Index (BMI)" expanded at first use, then "Body Mass Index" spelled out again in the outputs list and again in the FAQ.
- After: expanded once ("Body Mass Index (BMI)" in the opening section); every later mention uses "BMI" only, including in the FAQ's "What data is captured?" answer.

**13. Capture time**
- Before: "in under 45 seconds" (appeared twice: body + FAQ).
- After: "in approximately 30 to 45 seconds" (both instances updated).

**14. "Composition change explains what the scale hides"**
- Before: that exact phrase, in the original "broader than GLP-1" section.
- After: "can provide context that weight alone does not show" (used in both "Five ways" and "Applications beyond GLP-1," consistent phrasing per the reviewer's suggested wording).

**15. "Clinical team" → "care team"**
- Before: "which lowers the load on the clinical team as volume grows" (original "What improves operationally" section).
- After: "care team" used throughout (the phrase now lives inside "How the scan-to-scan experience works": "...reducing the manual reconciliation of self-reported data as volume grows," with "care team" already the standard term used everywhere else in the article, including coaches/wellness professionals).

**16. Repeated medical-device disclaimer in the conclusion**
- Before: closing italic line — "FitXpress is a structured body-data capture layer that supports clinician review. It is not positioned as a medical device, and clinical decisions stay with the care team." (third repetition of the same disclaimer, after the scope note in section 2 and the boundaries list).
- After: removed from "Next steps." The disclaimer still appears once as the italic scope note ("What mobile body scanning adds") and once in the boundaries list ("Where FitXpress fits, and where other methods remain necessary") plus once in the FAQ ("Is this a medical device?") — not repeated a third time in the close.

**17. Sentence case for "does not"**
- Before: heading "What FitXpress does NOT do."
- After: no such heading remains — the renamed section title is "Where FitXpress fits, and where other methods remain necessary" (sentence case throughout, no all-caps "NOT").

## Terminology guardrails pass (per Review 1's note on "General Approach & Language Guardrails for Corporate Content")

Applied `brand-assets/content-strategy/terminology-guardrails.md` across the full revision during the editor/publisher pass:
- Zero em dashes in the article body (verified by grep; matches the v4 precedent of allowing em dashes only in internal publish-package/checklist prose, never in the published article text).
- Zero uses of "so" as a result/consequence connector in the article body (one instance — "...does not show, so a patient in a plateau may see..." — was caught during the pass and rewritten to "...does not show, allowing a patient in a plateau to see...").
- Zero uses of "we/our/you/your" in the article body (company referred to by name, "FitXpress," throughout).
- No "let," "by hand," or "plus" found.
- No "objective" used in relation to 3DLOOK's technology/outputs.
- Corrective negation ("X, not Y") is confined to the boundaries list, which the guardrail explicitly allows as an exception for necessary product/clinical/regulatory boundaries.

## Verification notes

- All fixes were cross-checked with `grep` against the final `draft-v5-revision1.md` for: em dashes, banned words, the removed GLP-1 statistic, "under 45 seconds," the old privacy phrasing, "Section 4"/"Section 10," "People misremember," "clinical-facing," and "clinical team." None remain in the article body.
- Word count of the revised article body: ~2,300 words (still within the plan's 2,200–3,000-word target band).
- `plan.md` updated with a "Revision 1 structural update" section mapping the old H2.1–H2.12 outline to the new 9-part structure; the original outline is left intact above it as historical rationale, per the task's instruction to keep plan and final in sync only where structure materially changed.
