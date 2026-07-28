# Revision 2 Changelog — telehealth-hub-refresh (draft-v4-publisher-final.md → draft-v5-revision2.md)

Applied all 10 Revision 2 editorial comments on top of the approved `draft-v4-publisher-final.md`. One note per comment below, plus fact-verification notes and one terminology fix found in the process.

## 1. Replaced outdated product-page references
Both instances of "FitXpress for telehealth and weight loss" (Related resources bullet + closing CTA) replaced. Link text now "Telehealth & Digital Health" / "FitXpress for Telehealth & Digital Health" per the comment's suggested wording.

**URL verification:** the old URL (`https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/`) still resolves live and currently redirects in intent (the comment states so); the canonical current page was located via the live sitemap (`page-sitemap.xml`, last modified 2026-07-24): `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/` (H1: "Structured Body Data for Telehealth & Digital Health Programs"). Fetched and confirmed it independently states: structured results via API, two-photo capture, 80+ ISO-compatible measurements, under-45-second processing, FitXpress Admin Panel, and "Photos are processed to generate results and deleted after processing by default." Used this URL for both replaced links.

## 2. Replaced the model-bias paragraph
Old paragraph (conflating model bias with capture conditions) replaced verbatim with the reviewer's 3-point framework in "How to evaluate an AI tool for telehealth": population performance/bias → capture quality → implementation readiness. Rendered as a short numbered list under "Three operational realities sit underneath these questions."

## 3. Clarified measured / predicted / calculated outputs
Body §5 opening and FAQ "What body data does FitXpress capture?" both rewritten to the reviewer's exact framing: two photos + onboarding inputs (gender, height) → 80+ measurements + predicted/calculated outputs (predicted weight, BMI calculated from predicted weight and supplied height, BMR, estimated body-fat percentage, lean mass, fat mass).

**"Essential and beneficial fat" — resolved, not just flagged.** Fetched the live Telehealth & Digital Health page directly: it lists BMI, BMR, body fat %, lean mass, and fat mass only. Essential fat and beneficial fat are confirmed absent from the current public product page, so both were removed from the article (body + FAQ) per the comment's instruction ("remove unless Product confirms"). `proof-points.md` still lists essential/beneficial fat under "Product spec" — flagging this discrepancy between the internal proof-points doc and the live page as an open item for Vadim/Product (see Open Items below), but the article now matches what's publicly published.

## 4. Refined the self-report comparison (3 instances)
- §2 closing: "It replaces loosely captured self-report…" → "It supplements manually entered body data with a more standardized capture record for provider review."
- "The remote body-data gap" opening: "Self-report widens the gap. It is inconsistent, hard to verify…" → "Self-reported measurements can vary with the patient's equipment, technique, recall, and reporting format, making longitudinal comparison more difficult."
- FAQ "How is this different from self-reported weight and BMI?": same softened phrasing reused (one-number/one-phrasing consistency rule) in place of "Self-reported data is inconsistent and hard to verify across a population."

## 5. Yazen figure retained without naming the company
Body (§5): "Yazen, a weight-loss management program," → "one weight-loss management program using the capture layer across its member base." Figure (about 34,000 scans in 2025) and "internal figures" framing kept.
FAQ "What kinds of telehealth programs use mobile body scanning?": Yazen sentence removed entirely, per the comment's "remove from the FAQ at minimum." Question now answered with the three program-type categories only. `claims_used` unaffected (FX-010 still traces to the one remaining body mention).

## 6. Added vendor links; revised two outcome-flavored sentences
- AliveCor/KardiaMobile → linked to `https://alivecor.com/products` (verified live, describes the KardiaMobile line).
- Ada Health → linked to `https://www.ada.com` (verified live; no more specific standalone symptom-assessment URL found, so used the primary domain).
- Augmedix → linked to `https://www.augmedix.com/product-overview` (verified live, describes the ambient documentation product tiers).
- "The software surfaces patterns; the provider interprets them." → "Depending on the product and configuration, accompanying software may analyze the recording and surface findings for provider review." (generalized per the comment's fallback option, since a single applicable AliveCor analysis-feature URL wasn't clearly separable from the product-line page).
- "which shortens the clinician's setup time" → "which can give the clinician a structured symptom history to review before or during the consultation."

## 7. Simplified the encryption sentence
Body Privacy section: "Data is encrypted in transit with Transport Layer Security (TLS) and at rest in Amazon Simple Storage Service (S3) with server-side encryption (SSE-S3), which stays always on." → "Data is encrypted in transit and at rest." This exactly matches the wording independently verified live on the current Telehealth & Digital Health page ("Encryption in transit & at rest"). The FAQ HIPAA answer already used this simplified form in v4 — now consistent everywhere. TLS/S3/SSE-S3 acronyms no longer appear in the article (removed, not just unexpanded).

## 8. Changed the HIPAA FAQ question
"Is FitXpress HIPAA compliant?" → "Can FitXpress support a HIPAA-compliant telehealth implementation?" Answer replaced with the reviewer's exact text, dropping the retention/identifier restatement from this answer (already covered in the Privacy section — also serves comment 9's de-duplication goal).

## 9. Reduced repeated boundary/non-diagnostic language
Kept in full: (1) opening scope note, (2) "FitXpress capabilities and boundaries" 4-part section, (3) closing disclaimer.
Trimmed elsewhere:
- §5 workflow paragraph: cut "…the result is documented consistently, and the record supports the next follow-up. Provider review and documentation are the human steps. The layer supports them and does not decide, triage, or flag anything on its own." → paragraph now ends after "A provider reviews the data, and the results can then be documented according to the program's workflow." (exact phrasing the comment suggested; also resolves comment 10's "documented consistently" item for this location).
- Privacy section closing: cut the restated "FitXpress is not positioned as a medical device, and its compliance posture rests on data-privacy frameworks" clause; kept only the legal-center pointer sentence.
- FAQ Q2 (mobile-scanning fit): cut the trailing "The scan supports the workflow rather than replacing any human step in it." restatement.
- Left Q3 (replace DEXA) and Q6 (make clinical decisions) fully intact — the boundary statement IS the substance of those two questions, not a repeated aside.

## 10. Small editorial corrections
- "The sharper question" → "The more useful question," using the reviewer's full replacement sentence.
- "A patient in one session might use a bathroom scale, a cloth tape measure, and a guess" → "A patient may use a bathroom scale, take measurements with a cloth tape, or provide an estimate."
- "Comparability is the whole point" → "For longitudinal programs, comparability is essential."
- "A remote scan removes a common source of friction" → "A remote scan can reduce the need for a separate in-person measurement appointment in workflows where remote capture is appropriate."
- "the result is documented consistently" — resolved as part of comment 9's paragraph cut above (no separate "consistent format" phrase needed since the trailing clause was removed).
- **Acronym consistency:** found one additional instance beyond the ones named in the comment — FAQ Q3 re-spelled "dual-energy X-ray absorptiometry (DEXA) scan" after DEXA was already expanded in body §5. Trimmed to "DEXA scan." Checked all other acronyms (BMI, BMR, API, HIPAA, GDPR, BAA) end to end in reading order — each now expands once at first use only, acronym-only thereafter.

## Additional fix found during revision (not one of the 10, but directly relevant)
`brand-assets/content-strategy/terminology-guardrails.md` (flagged as missing/unlocatable in the Phase 2 report on v3/v4) was located this pass. Its rule "❌ Reader / audience / … — To apply: NEVER" flags the §1 sentence "The audience for that question is practical: care teams, clinical operations leads, chief medical officers, and heads of member engagement at remote-first health organizations." Reformulated to "That question matters most to care teams, clinical operations leads, chief medical officers, and heads of member engagement at remote-first health organizations" — removes "audience," keeps the ICP framing. This resolves the non-blocking open item carried in `phase3-publisher-report.md` §6 item 1.

## Open items for Vadim / Asselya (flag, don't decide — guardrail #11)
1. **`proof-points.md` vs. live product page mismatch on body-composition outputs.** `proof-points.md` lists "essential fat, beneficial fat" under Product spec; the live Telehealth & Digital Health page does not. The article now follows the live page (comment 3's instruction). Recommend Product/Vadim reconcile `proof-points.md` so future articles don't reintroduce the discrepancy.
2. **Ada Health link is the homepage, not a symptom-assessment-specific page.** No live, more specific official URL was found during verification. Acceptable as "official product documentation" per the comment's intent, but flagging in case Vadim has a preferred deep link.
3. **Carried forward, still open:** the "FitXpress Admin Panel" product-feature mention (§5 body + FAQ Q2) — same status as flagged in `phase2-editor-report.md` / `phase3-publisher-report.md`; unchanged this pass since Revision 2 didn't address it. Confirm acceptable, or ask for it to be softened to "a vendor console."
4. **Carried forward, still open:** audience-segment filtering (telehealth vs. GLP-1 boundary in `audience.md`) — unchanged this pass, no new information.

## Claims / positioning audit
- `claims_used` unchanged: FX-003, FX-005, FX-006, FX-007, FX-010, FX-012, FX-013, FX-014, FX-015, FX-016 — all still traced, all still byte-identical wherever repeated (verified: "under 45 seconds," "more than 80 body measurements," the exact repeatability sentence, "about 34,000 scans in 2025").
- No new banned words / AI-signatures introduced (no em-dash, no "not just X it's Y," no triple parallelism, none of the banned vocabulary list) — spot-checked across every edited sentence.
- Positioning intact throughout: FitXpress does not diagnose / does not autonomously triage or determine eligibility / does not replace protocol-required methods / does not make the workflow compliant on its own.
