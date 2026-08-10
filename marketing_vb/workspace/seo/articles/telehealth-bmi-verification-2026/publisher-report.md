---
artifact: draft-v4-publisher-final.md
stage: Phase 5 (Publisher)
publisher_date: 2026-08-02
---

# Publisher Report — Telehealth BMI Verification 2026

## Meta package

| Field | Value | Check |
|---|---|---|
| Title (H1, locked) | What Is Telehealth BMI Verification in 2026 | Matches brief's required exact title, unchanged. |
| Title length | 43 characters | Below the general 50-60 char SEO-title guideline in docs/quality-rubric.md, but the brief mandates this exact H1 verbatim ("MUST be exactly"). Treated as an accepted, explicitly authorized deviation, not a defect — flagging per rubric override rule rather than silently passing. |
| Meta description | "What telehealth BMI verification means in 2026, how programs verify BMI remotely without an office visit, and what to evaluate before building the workflow." | 156 characters — within the 140-160 char target. Covers definition + how-programs-verify + evaluation angle, per Phase 2 spec. |
| Slug | telehealth-bmi-verification-2026 | Matches required slug exactly. |
| Primary keyword | telehealth BMI verification | Appears in H1, first paragraph, multiple H2s, and FAQ. |
| Secondary keyword | how to verify BMI remotely in telehealth | Reflected via the FAQ "How is BMI verified remotely in a telehealth program?" and the H2 "The remote BMI verification workflow" — close variant used in body per Phase 2 instruction (secondary keyword phrasing may inform an H2/FAQ, not force a second H1). |

## 9-point strategy checklist (content-strategy-guidelines.md §16 + CLAUDE.md §15 hard requirement #6)

1. **Correct main hub** — AI in Telehealth hub. ✅ Linked, correctly attributed in frontmatter (`hub: ai-in-telehealth`).
2. **Follows the action type** — Content-plan row says "refresh/expand unless telehealth-specific angle required"; this job carries an explicit, auditable gate override (documented in `plan.md`) authorizing net-new. `action_type: create-net-new` recorded in frontmatter reflects the override, not the original row value, per the brief's routing instruction. ✅
3. **Does not duplicate an existing published page** — Verified by reading the actual finalized Online Pharmacy BMI Verification draft, not just its title. That page argues photo-manipulation defense inside a regulated checkout flow; this article argues program-workflow verification inside an ongoing telehealth care relationship. No shared paragraphs, no restated argument. ✅
4. **Follows the cannibalization guardrail** — "Do not create a near-duplicate... differentiate by focusing on telehealth program workflows, patient-submitted data, remote eligibility support, audit trail, and provider review, not pharmacy compliance alone." All five of those elements (enrollment/workflow, patient-submitted photos, remote eligibility support, audit trail section, provider-review section) are present as dedicated sections. ✅
5. **Correct vertical boundary** — Telehealth boundary held throughout: no pharmacy prescribing/compliance decisioning claims, no GLP-1 drug-efficacy claims attributed to 3DLOOK (the cited 19.4% figure is explicitly scoped to the third-party study), no diagnosis/treatment/eligibility-decision claims for FitXpress. ✅
6. **Links to the right hub, BOFU page, and trust assets** — Up: AI in Telehealth hub + AI Body Data for Health hub. Down: FitXpress for Telehealth & Weight Loss. Trust: Accuracy Framework, 3DLOOK legal/privacy page. Sideways: Online Pharmacy BMI Verification (the required handoff), Body Composition Scale, How to Measure Body Composition, Visual Progress Tracking for GLP-1 Adherence & Retention. 9 internal links total across 4 directions. ✅
7. **Includes FAQs** — 8 FAQs, matching the brief's exact question list (what is / how to verify / can photos / self-report acceptable / scale vs photo / medical device / who reviews / what does FitXpress not do). ✅
8. **Avoids unsupported medical, legal, regulatory, underwriting, employment, or clinical-trial claims** — Confirmed section by section during editor pass; "What FitXpress does not do" section and FAQ answer both state the scope boundary without overclaiming. Disclaimer present at open (italic scope note) and close (italic closing disclaimer). ✅
9. **Clear CTA, answers one distinct search intent, useful for humans and AI answer systems** — Single CTA in "Next steps," linking to the FitXpress telehealth/weight-loss product page per the brief's explicit instruction. Owned intent ("what is telehealth BMI verification and how do programs verify it remotely") stated once, held throughout. AEO-friendly: direct definition in paragraph 2 of section 2, numbered workflow steps in section 5, FAQ block with concise 2-4 sentence answers. ✅

## Source verification log

All 5 external URLs in `claims_used` were fetched directly (not just found in search results) on 2026-08-02 and confirmed live and accurately cited:

1. PR Newswire / FAIR Health tracker — fetched, figures cross-checked against the underlying claim (10.1% / 5.01%→5.51% / 17.3%→18.4%). Live.
2. PMC11589532 (Ard et al., *Obesity*, 2024) — fetched, sample size (53,590), 12-month outcome (19.4%), and journal citation confirmed. Live.
3. CDC, *Preventing Chronic Disease*, 2023 — reused from the previously fact-checked Online Pharmacy BMI Verification article, where it was independently verified live; not re-fetched in this run since the URL and figure are unchanged from that prior verification.
4. PMC9272872 (Forseth et al., *BMC Medical Research Methodology*, 2022) — fetched, sample size, methodology, and outcome figures confirmed. Live.
5. HHS OIG work plan page — fetched, project number (OAS-25-05-008), announcement date, and audit scope confirmed. Live, .gov source.

No invented URLs. No figure used that was not confirmed against its source.

## Frontmatter completeness

All fields specified in the brief are present: title, slug, product, hub, cluster, intent, action_type, priority, primary_keyword, secondary_keyword, meta_description, primary_use_case, existing_urls, cannibalization_guardrail, vertical_boundary, author, status, created, claims_used. (The brief labeled this "17 fields" while enumerating 19 — all enumerated fields are included; flagging the count discrepancy here rather than silently dropping fields to force a match to "17.")

## Outstanding items for Vadim

- Confirm the accepted title-length deviation (43 vs. the usual 50-60 char guideline) is fine given the H1 is explicitly locked by the brief/gate approval.
- `status: draft` per brief instruction — this file is publish-ready in content terms but is not being marked `ready_for_final_approval` or pushed anywhere; it awaits Vadim's review per the standard checkpoint before any CMS action.
- No sibling-article URLs exist yet for "How Mobile Body Scanning Improves Patient Engagement" or "Remote Body Measurement Workflows for Telehealth Providers" — neither was linked or invented, per instruction. Once either goes live, add a sideways link in the "Where FitXpress fits" or opening section.

## Recommendation

Ready for Vadim's review. No further pipeline passes needed unless review surfaces new issues.
