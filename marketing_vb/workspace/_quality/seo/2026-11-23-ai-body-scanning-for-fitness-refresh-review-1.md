---
qc_date: 2026-11-23
agent: seo-editor (Review 1 round; final.md)
artifact: workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md
slug: ai-body-scanning-for-fitness
product: fitxpress
track: seo
artifact_type: seo-final
stage: review round 1 (Asselya Sekerova), edit round on v1/final.md
total_score: 18/20
status: excellent
verdict: ship after fixes 1 and 4 (editor-side, inside A2/B1 text); fixes 2 and 3 need a coordinator override of section E
coordinator_review: pending
---

# QC Report: ai-body-scanning-for-fitness, Review 1 round, 2026-11-23

**Artifact:** `workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md`
**Total: 18/20, excellent.** All seven decisions (A1, A2, A3, B1, B2, B3, D3) are applied as written, and section E is untouched. The round added repetition in S3 and S6, and fixes 1-4 below remove it. Line numbers refer to final.md.

Inputs read: qc-prompt-review1.md (rubric, lint facts, claims pack, article), review-1.md, review-1-decisions.md, v1/final.md, blog-style-guide.md §5, editorial-rewrites.md §1-6, publish-package.md, meta.md, landing snapshot `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md`.

## Scores

| # | Category | Score | Max | Source |
|---|----------|-------|-----|--------|
| A | Adherence (decisions, then plan) | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | code verdict (lint PASS, detector 0.0/1000, checklist 19/19), accepted |
| C | Brand, tone, argument | 2 | 3 | judged |
| D | Format and structure | 3 | 3 | code verdict, accepted |
| E | Output quality, position | 3 | 4 | judged |
| | **Total** | **18** | **20** | |

Hard-rule check: 3 external sources (Adjust, JMIR, ACSM via Newswise), so the B ≤ 3 cap does not apply. plan.md has no TBD, so the A ≤ 2 cap does not apply. No client or competitor names, no "most accurate" lead, and `product: fitxpress` is present.

## What was wrong (specific)

### A. Adherence: 5/5
Decision by decision, v1 compared with the current text:
- **A1:** done. Line 83 matches v1 line 73. The CTA at lines 85 and 87 matches the decision character for character and links to the landing, not `#form`, at 15.7% of the body. Package Open item 4 notes the button rendering. This fits the new §5 rule: one early CTA and one closing CTA, with the line 153 link as a contextual internal link.
- **A2:** done.
  - The H2 at line 129 is verbatim.
  - The section is about 213-220 words, against a target of 180-220.
  - The opening has 2 sentences and keeps FIT-CAPTURE and FIT-SDK. The pitch and outputs sentences are removed, along with FXS-SPEED and FXS-OUTPUTS.
  - BIA is spelled out on first use.
  - There are 3 lists of 3 bullets each, and the own-brand bullet is dropped.
  - "The options can work together." and the trend-line sentence are kept. The comparison link is in one sentence.
  - The section ends on the map anchor "mobile alternative to a gym body scanner".
  - The landing H1 wording is not used in any heading.
  - The text says "is an alternative" where the decision says "is the alternative". That fits the decision-7 hedge and is not a defect.
- **A3:** done. The example is verbatim and sits between "Scheduled check-ins." and "Coach review." (line 97).
- **B1:** done.
  - The H2 is kept.
  - The Adjust qualifiers (global, 2022 data, all app users) are folded into one sentence.
  - The Kidman scope is kept, with "None of these sources tested body scans." covering the "not body-scanning interventions" half.
  - The ACSM part is 2 sentences.
  - The hub link and the weight-loss link are each in one sentence.
  - The question at line 117 is verbatim and comes after the statistics.
  - S8 states the hypothesis in different words.
  - The section is 225 words against "about 200", which Open item 10 discloses.
- **B2:** done. Line 78 is verbatim, including the claim comment.
- **B3:** done.
  - "The primary outcome is …" (line 168).
  - The secondary metrics are verbatim and in the decision's order.
  - The friction reason is given in the article's own words.
  - The landing FAQ line is not copied.
  - The rest of S8 is unchanged.
- **D3:** done. The description is verbatim in final.md, meta.md and the package (146 chars).
- **Section E:** unchanged. The intro, scope note, S2 bullets 2-4 and closing paragraph, S3 (apart from line 97), S5, S7, S8 paragraphs 3-4, all three FAQs and Next steps match v1 word for word.
- The editor made two extra cuts in S6 ("A club can keep its device…" and "are not measured and"). Both are justified by the length target, and the first one also removes a landing echo.

### B. Factual accuracy: 5/5
- Code verdict, accepted. The B2 timing line uses the canon wording. C1 is answered in Open item 1.
- Sourcing: JMIR is peer-reviewed. ACSM via Newswise is described as "does not report usage". Adjust is a vendor blog and is disclosed in Open item 6; the link returns 429 to the bot and needs a check by eye.

### C. Brand, tone, argument: 2/3
Clean on hard bans (detector 0.0, no em dash, mean sentence length 13.4). The round introduced 2 minor lapses:
1. **Verbatim 7-word repeat in S6.** Line 131 has "It fits members who **train at home or between club visits**." Line 149 has "Members **train at home or between club visits**." The two are 18 lines apart. The self_check says "A2 requires both". A2 requires the idea in both places, but it is not marked VERBATIM for either one, so the identical string is avoidable.
2. **The S4 lead-in at line 117:** "The question an app team can test is narrower: Does showing …"
   - The capital "D" is correct: AP and Chicago both capitalize a complete direct question after a colon. It is not an error.
   - The weakness is the frame. "The question … is: …?" is the pattern that editorial-rewrites.md §4 cuts ("The useful question about any measurement method is: …?"), and §1 says a colon does not turn two ideas into one sentence.
   - "an app team" is the only time that actor appears. Everywhere else the article says "product team" (lines 70, 91, 95, 101, 103).

Accepted residuals, all VERBATIM or frozen, so not scored against the editor:
- "takes … takes" in line 78 (B2).
- "guided" ×3 in lines 76-85 (S2, B2, A1).
- "for fitness apps" ×3 in lines 83-87 (E and A1).
- The A1 CTA's three-item list.
- "a guided scan on the member's own phone" in both line 68 and line 131. A2 prescribed the line 131 wording, and v1 already had it.

### D. Format and structure: 3/3
- Code verdict, accepted. The frontmatter changes_summary records every decision. self_check names the residuals honestly.

### E. Output quality, position: 3/4
- **What the round added works.** The CTA gives a MOFU reader a path to the landing at 16%. S6 now helps a team choose a workflow and no longer pitches the product, so the distance from the landing H1 and comparison table is clear. S4 ends on a question that S8 turns into a test design with primary and secondary metrics, which is the article's own position.
- **S3 now makes the coach point 3 times in a row.**
  - Line 97, the A3 example: "If a coach reviews the program, the two scan records provide additional context for **the next training block**."
  - Line 99, the next paragraph: "**Before planning the next training block**, the coach can check the change between two of the member's scans."
  - Both restate landing step 3: "the coach reviews the same record before setting the next program block". The v1 QC pass removed exactly this echo, and the round brought it back through the example.
- **"Who decides what is shown" is said twice.**
  - Line 97: "The app determines which results to show and how to use them."
  - Line 103: "The product team also decides what members and coaches see."
  - Line 95 also says "The product team chooses which two scans to compare". The example's "The app" goes against the article's convention that "the product team" makes the decisions.
- **"The options can work together." (line 153) still works after the cut.** The bullet directly above, "Members train at home or between club visits.", tells the reader how the options combine: hardware at visits, phone scans between them. The trend-line sentence assumes the methods are used together. Bringing back the cut sentence would also bring back the landing's comparison close ("An in-gym scanner still suits members who visit the club; FitXpress covers the check-ins between visits."). That is why fix 1 changes the opening sentence and leaves the bullet alone.
- **Landing echoes in the new text.** A spot-check against the 11-19 snapshot found no 7-word verbatim overlap. Echoes in meaning only:
  - (a) Line 133 (hardware sentence) matches the landing FAQ "What is a body scan at the gym?" (camera booth, bioelectrical impedance platform, "Each repeat needs a club visit."). A2 prescribed this content, so it is accepted.
  - (b) Line 97 sentences 2-3 match the landing's "Display waist measurements … alongside entered weight" and step 3. The example is VERBATIM, so it is accepted. Fix 2 removes the third restatement.
  - (c) Line 168's metrics match the landing list "Scan completion and retake rates … Free-to-premium conversion". The list is VERBATIM, and the landing FAQ line is not copied.
- Why 3 and not 4: the S3 cluster in lines 97-103 reads as the same point made three times, right after the round's only concrete example. That takes about 5 minutes to fix, but 2 of the edits touch frozen text.

## Top 3 issues (priority for the fix pass)

1. S6 has a verbatim duplicate between the answer and the bullet (lines 131 and 149). The editor can fix this inside the A2 text.
2. S3 repeats the coach point across the A3 example and Coach review (lines 97 and 99), and the repeat is also a landing echo. This needs a coordinator override of section E.
3. S3 says "who decides what is shown" twice (lines 97 and 103). This needs a coordinator override of section E; it matches package Open item 9.

## Fixes (exact text)

1. **Line 131 (A2 text, editor).**
   - Current: "It fits members who train at home or between club visits."
   - Replace with: "It fits members who train away from the club, at home or between visits."
   - The bullet on line 149 stays as it is, because it is the line that makes "The options can work together." work.
2. **Line 99 (frozen by E, coordinator override).**
   - Current: "**Coach review.** Before planning the next training block, the coach can check the change between two of the member's scans."
   - Replace with: "**Coach review.** The coach can check the change between two of the member's scans."
   - The A3 example stays verbatim.
3. **Line 103 (frozen by E, coordinator override; same as package Open item 9).**
   - Current: "In every placement, the onboarding, consent, and results screens follow the app's design. The product team also decides what members and coaches see. The photo-capture step is the one fixed part: …"
   - Replace with: "In every placement, the onboarding, consent, and results screens follow the app's design. The photo-capture step is the one fixed part: …"
   - FIT-WHITELABEL stays on the paragraph.
   - Optional, VERBATIM so the coordinator decides: in line 97, change "The app determines" to "The product team determines" to restore the actor convention.
4. **Line 117 (B1 text, editor).**
   - Current: "The question an app team can test is narrower: Does showing structured body progress increase the likelihood that a member returns for another check-in?"
   - Replace with: "A product team can test a narrower question. Does showing structured body progress increase the likelihood that a member returns for another check-in?"
   - The question stays verbatim. Rerun the lint and detector after the change, because it creates a standalone question sentence.
5. **Optional, low priority. Line 153 (A2 text, editor; the anchor stays).**
   - Current: "Integration options and plans are on the FitXpress [mobile alternative to a gym body scanner](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) page."
   - Replace with: "Integration details and plans are on the FitXpress page for a [mobile alternative to a gym body scanner](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)."
   - This removes the noun stack "the FitXpress [anchor] page" and avoids reusing the CTA's "integration options".

## for_agent_improver

- **seo-editor:** a decision that gives the same content for two places, without marking it VERBATIM, does not require the same words. Before writing "A2 requires both" in self_check, run the editor's own 7-word overlap check inside the changed section, not only against the landing.
- **Coordinator (review-decisions template):** when a VERBATIM insertion sits next to a section frozen under E, the template should pre-authorize the minimal edit to the adjacent frozen sentence that the insertion duplicates. Otherwise every round ends with an override like fixes 2 and 3.

## Coordinator review

```
agreement: ✅ agree
top_issue: the round's verbatim example (A3) re-created the S3 coach/next-block repeat the v1 QC had removed; fixed by overriding section E for two S3 sentences (fixes 2-3), the example itself kept verbatim.
```
