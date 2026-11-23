---
qc_date: 2026-11-23
agent: seo-editor (Review 1 round; final.md)
artifact: workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
product: fitxpress
track: seo
artifact_type: seo-final
stage: review round 1 (Asselya Sekerova), edit round on v1/final.md
total_score: 16/20
status: good
verdict: ship after editor-side fixes 1-4; fixes 5-7 need coordinator rulings (actor conflict in the decisions, one scan-ID sentence, external source / B cap); fixes 8-9 optional
coordinator_review: done 2026-11-23 (see section at the end)
---

# QC Report: telehealth documentation, Review 1 round, 2026-11-23

**Artifact:** `workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md`
**Total: 16/20, good.** All decisions from A to M are applied, and the deviations are authorized or documented. The article still argues its thesis ("Consistency is decided at capture.", line 93). The round added a dense layer of responsibility statements. Each one is prescribed and accurate, but together they make the S4-to-FAQ half read closer to a scope document than v1 did. B is capped at 3 by the no-external-source hard rule. Without the cap the total would be 18. Line numbers refer to final.md.

Inputs read: qc-prompt-telehealth-r1.md (rubric, lint facts, claims pack, article), review-1.md, review-1-decisions.md, editor-report.md (with coordinator addendum), v1/final.md, plan.md, the rebuilt publish-package.md, the v1 QC report, compliance.md §3-4.

## Scores

| # | Category | Score | Max | Source |
|---|----------|-------|-----|--------|
| A | Adherence (decisions, then plan) | 5 | 5 | judged |
| B | Factual accuracy | 3 | 5 | code verdict accepted (lint PASS, detector 0.0/1000, checklist 19/19); capped at 3 by the hard rule |
| C | Brand, tone, argument | 2 | 3 | judged |
| D | Format and structure | 3 | 3 | code verdict, accepted |
| E | Output quality, position | 3 | 4 | judged |
| | **Total** | **16** | **20** | |

Hard-rule check:
- **External sources: zero.** All 11 links go to 3dlook.ai (8 distinct). The B ≤ 3 cap applies.
- plan.md has volume 40 and KD 10, with no TBD, so the A ≤ 2 cap does not apply.
- No client or competitor names, no "most accurate" lead, and `product: fitxpress` is present.

## What was wrong (specific)

### A. Adherence: 5/5
- **A:** done. The H1 at line 85 is verbatim and the frontmatter `title:` matches it. The byline (line 87) and the slug are unchanged.
- **B:** done, with the authorized fallback. Line 101 is its own paragraph, directly after the scope note, and the anchor and URL are verbatim.
  - The M1 expansion is recorded in three places: editor-report deviation 1, package change log 3, and the reviewer notice.
  - The link sits at 9.4% of the body.
- **C:** done.
  - Line 108 lists the five items in the decision's order.
  - Line 109 adds the "not every technical field" sentence and makes no claim about which field appears where.
  - Line 111 keeps the measurement / calculated / estimate distinction.
  - Line 105 still says "in under 45 seconds".
- **D:** done. The S4 lead (line 125) names the five things the program controls. "Between visits" (line 133) has three sentences with one negation each.
- **E:** done.
  - The lead (line 143) has two sentences and states the record point once.
  - E1 (line 147) covers capture in the app, outputs via the API/SDK, mapping, and EHR work, and carries the map anchor.
  - E2 (lines 151-161) has the canon line plus EHR, 7 bullets, no tab names, no Clothes Detector, FX-014 and the launch-post link.
  - The H3 "for scan management" deviation is documented (Title Case gate).
  - One small drift: E1 says EHR work is "on the customer's side", where the decision text says "the program's integration work" (fix 4).
- **F:** done.
  - The H2 at line 163 and the cells in lines 169-174 are verbatim.
  - "quicker to read" is gone.
  - The hedge and the recalculation sentence are kept (line 176).
- **G:** done. Line 182 adds the diagnostic-tool sentence and line 186 adds the compliance paragraph. The other boundaries are at lines 99, 182 and 184.
- **H:** done.
  - The photo sentence comes first, with "within 30 days" (line 190).
  - The GDPR sentence at line 192 is verbatim.
  - The FAQ link is at line 194.
  - The section is 155 words against 145 in v1.
- **I:** done. The measures (lines 202-206) are in v1 order, the steps (lines 210-214) are in the verbatim order, and FX-012 is at line 216.
- **J:** done. Line 246 links the landing with a demo anchor. There is no other promotional text.
- **K:** done.
  - The FAQ 1-4 questions are unchanged.
  - FAQ 4 (line 238) is updated, and its dataset, below-1-cm and framework-link sentences are untouched.
  - FAQ 5 (line 242) is verbatim.
- **L:** done. No new "AI", no "objective", no client count, no roadmap feature.
- **M:** done. All seven URLs are present, every anchor is distinct, and the pharmacy guide appears only in "At intake".
- **Order:** the coordinator moved the FAQ above Next steps (addendum). The reviewer's J ("final demo CTA after the pilot discussion") still holds.

### B. Factual accuracy: 3/5
- **Claims and figures:** the code verdict is accepted.
  - All 15 claim IDs trace.
  - "below 1 cm" is used only in FAQ 4, with its dataset condition and the framework link.
  - Spot-check: no overstatement found in the new text. The table cells are hedged, and "months after capture" (line 143) rests on FX-003.
- **Sourcing: zero links to third-party sources.**
  - The plan (plan.md line 118) allowed one optional HHS citation in S3. The v1 package flagged its absence as open item 5.
  - The rebuilt package drops that item. It marks `anchors_sources` ok with "trust sources are our own privacy FAQ and accuracy framework" (package line 50). This is the failure the hard rule was written for.
  - The unsourced claims a Head of Clinical Ops would want backed are in S3:
    - line 117, "Payers, employers, and regulators expect outcomes traceable to a dated, consistent entry."
    - line 119, "Documentation expectations for telehealth keep being revised."
  - Fix 7.

### C. Brand, tone, argument: 2/3
The text is clean on hard bans: detector 0.0, no em dash, no "you/we/buyer/organization", mean sentence length 12.8. The round introduced several sentence-level lapses:
1. **"stay(s) with" refrain, 5 times.** Lines 99, 137, 176, 182 and 186. The two at lines 176 and 186 are new.
2. **Line 176 has an orphan sentence and a double hedge.**
   - "Correction handling stays with the program's record system." is what is left of v1's re-entry sentence after the editor cut it. It no longer has an antecedent, so the reader is not told what gets corrected.
   - The sentence before it stacks two hedges: "may need rebuilding … although any gain depends …".
3. **The line 182 sentence reads like a checklist item.** "FitXpress is not a clinical diagnostic tool." sits between a sentence that already rules out diagnosis and "Final decisions stay with …".
4. **Line 147, "The FitXpress page on its [body scanning API …]":** the possessive is clumsy.
5. **Actor naming in S5.**
   - The integration owner is "the program" at line 125 but "the customer" twice at line 147.
   - The same party is "the customer's API keys" at line 153 and "selected FitXpress clients … client credentials" at line 161.
   - The decisions cause part of this: D says "the program controls … the integration", while the actors preamble assigns integration to "customer". In telehealth, the platform company and the clinical program can be different entities, so the reviewer's vague-actor concern is real here.

Accepted residuals (prescribed or authorized, not scored against the editor):
- **The early-link sentence (line 101) reads acceptably.**
  - It is 33 words long. The expansion makes the middle list item 10 words long, but the three-item list still parses.
  - It uses the reviewer's words plus the decision's own fallback.
  - If she objects, an M1 waiver for "API/SDK" at this position is the only way to get her 26-word original back.
- The G sentence is 29 words long.
- "API/SDK integration" appears 3 times, and "the program's own" 4 times.
- Line 109 names "the Admin Panel" before S5 introduces it (decision C).

Why 2 and not 1: none of these lapses touches a hard ban or breaks the voice. Everything except the actor ruling is a 10-minute editor fix.

### D. Format and structure: 3/3
- The code verdict is accepted.
- The frontmatter `changes_summary` records each decision, and `self_check` names the residuals.
- The package is rebuilt: 5-question JSON-LD, link map, change log, open questions.

### E. Output quality, position: 3/4
- **The argument holds.**
  - S1 ends on the thesis (line 93).
  - The S6 lead (line 165) says what changes and what does not.
  - The pilot section opens with a condition (line 198: "A capture change earns its place where the existing gap is in intake.").
  - "Who this fits" (line 220) names who gains less.
- **Additions that read as part of the article:**
  - The S4 lead chains "the workflow … decides" into "The program controls that workflow" (line 125).
  - E1 states the EHR boundary as a division of work, not as a disclaimer (line 147).
  - The G paragraph closes S7 and hands over to S8 (line 186).
  - The table cells (lines 169-174) are qualified without losing the contrast.
- **Additions that read bolted on:**
  - Line 182 (C3).
  - The orphan sentence at line 176 (C2).
  - The two developer-facing E2 bullets (line 154 API-key environments, line 159 API key / allowance / subscription). These are the least relevant items for a Head of Clinical Ops. The reviewer listed them, so they stay.
- **Repetition introduced by the round.** All of it is prescribed and accepted:
  - "the program selects / picks" the scans: 5 times (line 108 C, line 133 D, line 174 F verbatim, line 180 v1/G KEEP, line 238 K). v1 had it twice.
  - Body Progress: 3 times (lines 108, 133, 238).
  - Patient association belongs to the program: 3 times (lines 125, 147, 242).
  - The Admin Panel is not an EHR: line 151 (E2) and line 242 (FAQ 5 verbatim). The FAQ answer has to stand alone for FAQPage, so this pair is fine.
  - Net effect: about 15 responsibility sentences between S4 and FAQ 5. None of them is wrong, but the density is the cost of four decisions each requiring the same boundary.
- **Thin points for a telehealth Head of Clinical Ops:**
  - **How a scan reaches the right chart is never stated.** The article says the program owns patient association (lines 125, 242), that Body Progress picks scans by ID (lines 133, 238), and that 3DLOOK stores only random IDs (line 190). It never joins these three facts: the program keeps the link between a scan ID and its own patient record (fix 6).
  - **No outside source** behind the S3 regulatory-change claim (fix 7).
  - **The pilot steps (lines 210-214) are generic.** The order is VERBATIM, so this is accepted. But cutting v1's "Baselines taken before launch make the second reading worth having." removed the only stated reason for step 1. "The pilot itself" (line 208) is filler (fix 8).
  - **"The record is retrieved in one place" (line 137)** is passive. The reader is not told who retrieves the record or who repeats a failed capture (fix 9).
- **Overstated:** nothing found.
- Why 3 and not 4: fixes 1-4 take about 10 minutes, but fixes 5-7 need coordinator rulings before the text is final.

## Top 3 issues (priority for the fix pass)

1. **Zero external sources.** The rebuilt package dropped v1's open item and marked `anchors_sources` ok. This caps B at 3 and needs a coordinator decision (fix 7).
2. **The S6 reading paragraph (line 176)** has an orphaned correction sentence and a double hedge. It is the round's most machine-like spot (fix 1, editor).
3. **The integration and patient-association owner is named two ways.** It is "the program" at line 125 and "the customer" at line 147, because decision D and the actors preamble disagree (fix 4 editor, fix 5 coordinator).

## Fixes (exact text)

1. **Line 176 (F text, editor).**
   - Current: "Less of the record may need rebuilding inside the consultation, although any gain depends on how much was missing before. Correction handling stays with the program's record system."
   - Replace the first sentence with: "How much less of the record needs rebuilding inside the consultation depends on how much was missing before."
   - This keeps decision F's hedge once and adds no efficiency claim.
   - Move the correction point to the end of the paragraph, after the FX-005 sentence, as: "Corrections to an entry are made in the program's record system." Alternatively, cut it; lines 125 and 147 already place the record system with the program.
2. **Line 182 (G text, editor).**
   - Move "FitXpress is not a clinical diagnostic tool." to the start of the paragraph: "FitXpress is not a clinical diagnostic tool. It does not independently determine a diagnosis, … decision. <!-- claim: FX-006 --> Final decisions stay with …".
   - It then works as the topic sentence, with the next sentence as its specification.
3. **Line 186 (G text, editor).**
   - Current: "Compliance stays with the program and its legal advisors."
   - Replace with: "The program and its legal advisors remain responsible for compliance."
   - This leaves "stay(s) with" 3 times, all of them v1 text.
4. **Line 147 (E1 text, editor).**
   - (a) Current: "The FitXpress page on its [body scanning API for telehealth platforms](…) describes what an integration covers." Replace with: "The page on the FitXpress [body scanning API for telehealth platforms](…) describes what an integration covers." The anchor stays the same.
   - (b) Current: "… is integration work on the customer's side." Replace with: "… is the program's integration work." This uses decision E1's own words and matches line 125.
5. **Line 147 (coordinator ruling: decision D and the actors preamble conflict).**
   - Current: "The customer decides how those results map into its own record systems."
   - Replace with: "The program decides how those results map into its own record systems."
   - FAQ 5 (line 242) stays VERBATIM with "customer".
   - Optional in the same ruling: line 161 "selected FitXpress clients … client credentials" against line 153 "the customer's API keys".
6. **Line 133 (D text; coordinator check, because this is a new process statement).**
   - Current: "FitXpress does not keep a patient timeline; that history sits in the program's records."
   - Replace with: "FitXpress does not keep a patient timeline; the program links each scan ID to its own patient record." Marker: FX-016.
   - Support:
     - FX-016: the customer chooses scans by ID.
     - FX-009: random IDs, and 3DLOOK cannot identify a person.
     - compliance.md §3: "Customer provides the relevant scan identifiers".
     - FAQ 5: "associated with patients".
7. **Sourcing (coordinator; S3 is frozen by the decisions).** Choose one:
   - (A) Override the S3 freeze and add one verified neutral source behind line 119. Per plan.md line 118, use telehealth.hhs.gov, fetched live and described as the page states.
   - (B) Accept the cap. The publisher then restores "No external sources in the article" to Open items and corrects the `anchors_sources` line (package line 50).
   - B stays at 3 under (B).
8. **Line 208 (I text, editor, optional).**
   - Current: "None of them is a result to expect in advance. The pilot itself follows this order:"
   - Replace with: "None of them is a result to expect in advance, which is why the baseline comes first. The pilot follows this order:"
9. **Line 137 (actor preamble, editor, optional; v1 text the decisions do not freeze).**
   - Current: "The record is retrieved in one place ahead of the consultation."
   - Replace with: "The clinical team retrieves the record in one place ahead of the consultation."

After the fixes, rerun `article_lint.py` and the detector: fixes 1, 2 and 6 move claim markers or sentence boundaries.

## for_agent_improver

- **seo-editor:**
  - When you keep a clause from a sentence you cut, check that it still has an antecedent (line 176).
  - Do not add a modal ("may") on top of a hedge the decision requires.
  - Check verb-phrase refrains such as "stay(s) with" across sections. The lint's `repeated_phrases` did not catch this one.
- **seo-publisher:** the rebuild must carry v1 open items forward unless a decision closes them. `anchors_sources` should state the external-source count as a number. "No vendor blogs" is not the same as "no external sources".
- **Coordinator (review-decisions template):**
  - When three or more decisions require the same boundary (here C, D, F and K for "the program selects the scans"), name one home section. The other sections then refer to it briefly.
  - Make the actors preamble agree with the decision text: D gives the integration to "the program", the preamble gives it to "customer".

## Coordinator review

(filled in by the coordinator)

## coordinator_review

agreement: ✅ agree (16/20; the B cap is real and was a known v1 open item)
top_issue: zero external sources; HHS (the one source plan.md allows in S3) returns 403 to curl, WebFetch and a Playwright browser on 2026-11-23, so it cannot be verified and is not added (plan.md S3: "Skip the citation rather than approximate it").

Rulings:
1. ACCEPT (editor).
2. ACCEPT (editor).
3. ACCEPT (editor).
4. ACCEPT (editor), (a) and (b).
5. ACCEPT: E1 "The customer decides how those results map…" → "The program decides…". FAQ 5 stays verbatim (reviewer's text). Keep "customer's API keys" (account/contract) and "selected FitXpress clients" (wording of the launch post and of the reviewer).
6. ACCEPT: "…; the program links each scan ID to its own patient record." Support: FX-016 (patient association is the customer's), FX-009. Keep the FX-016 marker.
7. Option B: accept the cap. Coordinator restores the open item "No external sources" in meta.md and corrects the anchors_sources line, then re-assembles the package.
8. ACCEPT (editor).
9. ACCEPT (editor): names the actor, which review §3 asks for.
