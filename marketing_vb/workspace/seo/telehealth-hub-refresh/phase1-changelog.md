# Phase 1 Changelog — telehealth-hub-refresh (draft-v1 → draft-v2-revised)

Editor: applied all 15 revision-letter comments to `conductor-draft-v1.md`, output `draft-v2-revised.md`. One-line note per comment below.

1. **Strategy language out of body copy.** Deleted "What This Hub Covers (and Who It's For)", "This hub maps four pillars…", "Each section below routes to…", "Explore the Telehealth Cluster", "This hub anchors a set of supporting articles…". Opening now reads as plain reader-facing prose; audience is named in one natural sentence with no page-architecture meta-commentary.

2. **Weak opening statistics removed.** Cut the 97% adoption (TechReport), $79.93B→$290.90B (Market Research Future), 75%/80% (MedTech Intelligence), and 11%/76% physical-exam-vs-history stats entirely. Replaced with the operational argument from comment #6 rather than substitute statistics.

3. **Internal-link narration removed.** Kept the accuracy-framework, two-photos, online-pharmacy, product-page, and legal-center links but stripped "the right next reads", "routes to a deeper cluster article", "Related clusters sit alongside…", and the "central FAQ will replace that interim link" note. Links now read as plain editorial recommendations (accuracy-framework anchor uses the exact suggested phrasing).

4. **"AI in telehealth body data" phrase eliminated.** The verbatim phrase appears nowhere in the body. Rotated natural variants instead: "AI in telehealth", "structured body data in remote care", "AI-supported body-data capture", "mobile body scanning for telehealth", "remote body data". Frontmatter `primary_keyword` changed to "AI in telehealth".

5. **Restructured to the 11-section reader-journey order.** Sections now: (1) What is AI in telehealth? (2) Where AI fits in remote-care workflows (3) Common AI-supported use cases (4) The remote body-data gap (5) How mobile body scanning fits into telehealth (6) Patient-experience considerations (7) Privacy, security, and data governance (8) FitXpress capabilities and boundaries (9) How to evaluate an AI tool for telehealth [new, built from boundary/guardrails material as an evaluative checklist] (10) FAQ (11) Related resources. Old "Why AI Matters Now", "Challenges and Guardrails", "Future Outlook", "Next Steps" content was mapped into the new order or retired.

6. **Opening rebuilt around the supplied text.** Used the two supplied paragraphs as the base of §1; removed the em dash from the first sentence (split into two sentences). Preserved "Higher remote volume raises the cost of inconsistent intake" in §2, adapted to stand without the deleted surrounding statistics.

7. **Use-case section fixed.** Workflow-stage categories are now the main content (remote monitoring, virtual triage/assistants, AI-assisted diagnostics, personalized care insights, behavioral support, documentation automation). Kept 3 named, clearly-telehealth examples described cautiously: AliveCor/KardiaMobile (RPM), Ada Health (triage), Augmedix (documentation). Dropped Viz.ai/Aidoc (imaging category described generically and flagged as closer to in-clinic radiology), Merative (care-insights category described generically), Woebot (behavioral category described generically, availability/positioning uncertain), and Resmed.

8. **Repeatability wording corrected.** Replaced the `< 1 cm` framing with the exact sentence: "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm." Deleted "a small real change is less likely to disappear into measurement noise" and "small real changes stay legible" with no equivalent substitute; routed the fuller treatment to the accuracy framework. Same exact sentence reused in FAQ (byte-identical).

9. **Product-workflow wording de-automated.** Replaced "drops a clean, comparable set of metrics into the patient profile" / "delivers structured measurements into the patient record" with: "FitXpress processes the scan and returns structured outputs. Depending on the implementation, results can be delivered through the API to the customer's existing interface or accessed through the FitXpress Admin Panel." Kept "under 45 seconds" (matches FX-005). NOTE: did not use "30-45 seconds" anywhere — that figure is not confirmed in proof-points.md; flagging per instruction.

10. **Patient-experience section broadened.** Removed the "visible progress → repeat check-ins → adherence/retention" causal chain; replaced with the supplied "Progress views can give patients and care teams another way to discuss change…" sentence. Added hedged coverage of: two-photo capture explained to patients + informed consent; comfort with image capture and privacy; pose/clothing/lighting instructions; accessibility/device/space limits; retakes and failed captures; an alternative path for patients who cannot/will not scan; outputs are estimates; and who can access outputs (provider vs patient vs platform admin).

11. **Yazen / UK Meds reconciled.** UK Meds removed entirely from the hub (no mention anywhere). Yazen kept but framed explicitly as an internal/company figure ("According to the company's internal figures… about 34,000 scans in 2025"), not externally audited, with no public case-study link claimed. Weight-management framed as one use case among longitudinal-monitoring and member-engagement uses, not the dominant framing.

12. **Privacy corrections applied.** (a) Photo deletion replaced with "deleted after processing by default… alternative retention arrangement is defined contractually…"; auto-blur removed. (b) Identifiers replaced with "3DLOOK does not require names or direct personal identifiers… Customers control how session identifiers are associated…". (c) HIPAA replaced with "supports HIPAA-compliant implementations, including a BAA on request, and GDPR-aligned workflows" (HIPAA/GDPR/BAA expanded at first use per M1). (d) "central FAQ will replace that interim link" note removed; legal center linked plainly. TLS + AWS S3 SSE-S3 (FX-014) kept.

13. **Telehealth boundary narrowed.** Removed GLP-1 program specifics, BMI-verification detail, eligibility, underwriting, hiring, fitness-for-duty, fraud review, and payer/employer reporting. Retained only: one one-line sideways link to the online-pharmacy BMI guide (in Related resources) and the telehealth product page + accuracy/legal trust links; GLP-1 links omitted entirely (comment #14 supersedes the optional GLP-1 mention for the resources section). "What FitXpress Does NOT Do" narrowed to exactly the four telehealth boundaries (no diagnose/treat; no autonomous triage/eligibility; no replacing protocol-required methods; does not make the workflow compliant on its own).

14. **Cluster-navigation transformed into "Related resources."** No unpublished articles listed as if live. Only live links, grouped exactly as specified: Understand the technology (two-photos), Evaluate evidence (accuracy framework), Explore a specific workflow (online-pharmacy BMI, one line), Assess product fit (product page), Review policies (legal center). GLP-1 hub, GLP-1 compliance, visual-progress GLP-1, accuracy-drives-ROI, and Admin Panel launch not mentioned.

15. **FAQ made consistent with corrected body.** Q5 uses corrected §12 HIPAA/retention/identifier language (BAA on request; deleted-after-processing-by-default; no auto-blur; program owns compliance). Q8 uses the exact §8 repeatability sentence once, then links the accuracy framework — no universal minimum-detectable-change claim. Q2 uses corrected §9 API/Admin-Panel delivery language, no automatic-entry-into-record wording. Q7 hedges Yazen as an internal figure. Weight-loss kept to a single question among several telehealth use cases.

## Global-requirements audit
- Positioning: "supports clinician review" / "structured-data-capture and remote-intake layer" / "helps standardize" used throughout; no diagnose/eligibility/replace-DEXA/guarantee-compliance claims.
- Banned words/constructions: no em-dash rhetorical constructions, no "not just X, it's Y", no hype-triple parallelisms, none of the banned vocabulary list, no "Furthermore/Moreover/Additionally" openers.
- M1: BMI, BMR, DEXA, HIPAA, GDPR, BAA, API, TLS, S3, SSE-S3, RPM, ECG expanded at first use. (GLP-1 intentionally not used, per boundary narrowing.)
- M2: boundaries stated once, positively where possible; medical framing is "not positioned as a medical device."
- One-number consistency: "under 45 seconds", "more than 80 body measurements", the exact `< 1 cm` repeatability sentence, and the Yazen "about 34,000 scans in 2025" internal figure are identical in body and FAQ.
- No new numbers/sources/client names introduced beyond the approved_claims table. `claims_used` updated to drop FX-009 (UK Meds removed).
- Author: Assel Sekerova (frontmatter). Body length ~3,050 words (within the 2,800–3,300 target).

## Open items for Asselya / Vadim
- FX-004 (weight ±3.5%) not used; not required by any section after the revision. No action needed unless a weight-estimation callout is wanted.
- "30-45 seconds" phrasing from an unknown source was NOT used; only the proof-points-backed "under 45 seconds" appears (see comment #9).
- SOC 2 and FDA status remain unasserted per context-pack flags.
