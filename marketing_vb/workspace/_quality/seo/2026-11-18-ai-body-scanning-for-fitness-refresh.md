---
qc_date: 2026-11-18
agent: seo-editor (final.md; writer seo-writer, plan seo-planner)
artifact: workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md
slug: ai-body-scanning-for-fitness
product: fitxpress
track: seo
artifact_type: seo-final
stage: final (refresh in place)
total_score: 17/20
status: good
verdict: ship after three sentence-level fixes (no regeneration)
coordinator_review: pending
---

# QC Report: ai-body-scanning-for-fitness (refresh in place, FitXpress), 2026-11-18

**Artifact:** `workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md`
**Total: 17/20, good.** Approve after minor edits. All three fixes below are single sentences in S6 and S7.

## Scores

| # | Category | Score | Max | Source |
|---|----------|-------|-----|--------|
| A | Adherence (plan and intent) | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | code verdict (lint PASS 10/10, detector 0.0/1000, checklist 18/18), accepted as given |
| C | Brand, tone, argument | 2 | 3 | judged |
| D | Format and structure | 3 | 3 | code verdict, accepted as given |
| E | Output quality, position | 3 | 4 | judged |
| | **Total** | **17** | **20** | |

Hard-rule check:
- External sources: 3 (Adjust, JMIR, ACSM via Newswise), so the "no external links, B ≤ 3" cap does not apply.
- Plan volume/KD: "no data (null, not zero)", which is a measured result rather than TBD, so the A ≤ 2 cap does not apply.
- No client or competitor names. No "most accurate" lead. Frontmatter has `product: fitxpress`.

Not scored as deviations, per the coordinator: the bold `**Scope note.**` (line 54), the hedged S4 H2, the three landing CTAs (16.0% / 60.8% / end), the S8 cut to prose (decision 6), and the removal of the 3D model (decision 1).

## What was wrong (specific)

### A. Adherence: 4/5
- All 10 plan parts are present in order. The H2s match the plan, apart from the sanctioned S4 hedge. The primary keyword is in the H1 and the S2 H2. `ai body scan fitness app` appears once, naturally (line 58: "An AI body scan in a fitness app…"). Every planned link is placed: up ×1, side ×5, trust ×2, landing ×3 plus `#form`. FAQ, scope note and next steps are present. Length is 1,992 against a target of 1,950.
- **Plan boundary breached (S3).** The plan says "Do not restate the landing's onboarding-completion answer." The article restates its substance twice:
  - Line 71: "Taken at onboarding, it records the starting point but adds a step for a new member. Taken at the first check-in, it leaves onboarding unchanged"
  - Line 147: "onboarding completion stays a guardrail measure, because the scan adds a step for a new member"
  - The landing's FAQ 1 already says: "It can. The product team chooses where the scan sits, at onboarding or at the first check-in. The pilot compares onboarding completion with the usual flow."
  - The editor added this as an "expert trade-off" in Pass 3, which conflicts with the plan's boundary.
- Minor: the S7 "Evidence with its reference" bullet does not point back to S5, although the plan asked for it ("point back to Section 5"). This is where the claims ambiguity in fix #1 comes from.
- Package-level drift. It is not in final.md, but the coordinator has to resolve it before Yoast:
  - The publish-package description, "AI body scanning for fitness apps: where a scan sits…", differs from `meta_description` in final.md and from the plan. It contains the landing's primary keyword string `body scanning for fitness apps`. Rule 3 allows that in a description, but the plan deliberately avoided it ("does not contain the landing's primary keyword").
  - meta.md's judgment line `cta_type` puts the CTAs "in the intro" and "in S5" at "about 10%". The actual positions are S2 at 16.0% and S6 at 60.8%.
  - Open item 6 says 1,997 words; the real count is 1,992.
  - Plan D3's accepted risk ("may lose what remains" of the consumer `ai body scanner` traffic) is not among the package's Open items.

### B. Factual accuracy: 5/5
- Taken from the code verdict. No independent re-check of figures.
- Sourcing:
  - JMIR (Kidman 2024, peer-reviewed).
  - ACSM 2027 trends via the Newswise release, framed as a survey of professionals ("it does not report usage").
  - Adjust benchmarks on a vendor blog. Flagged honestly in Open item 2; the link returns 429 to the bot, so it needs a manual check.
  - All three are traced to FIT-* IDs in the pack's approved_claims, not to proof-points.md. That is correct for third-party figures.
- Judgment observation, not deducted here (it is moved to E and fix #1). Line 140, "FitXpress ties its figures to expert pattern-maker tape measurements and a repeat-scan protocol.", sits under an H2 about **body composition** tracking, directly after a sentence naming DXA as a reference method. "its figures" can be read, and lifted by an assistant, as covering composition estimates. FIT-OUTPUTS-NOTE limits the figures to body measurements, and S5 line 103 says so, but S7 is the block the AEO answer is built from.

### C. Brand, tone, argument: 2/3
Clean on hard rules: no banned words, no em dash, no "plus"/"let"/"objective", detector 0.0, mean sentence length 13.1. The medical-device line appears once, stated directly. Light lapses in voice, readability and argument:
1. **Unanchored "the same record"**, which is also near-verbatim landing copy:
   - Line 75: "The coach reviews the same record before setting the next training block." The landing's step 3 reads "the coach reviews the same record before setting the next program block".
   - Line 130: "A coach reviews the same record remotely."
   - In both places the article never says which record is "the same".
2. **An argument that does not land (S4, line 89).** The ACSM paragraph is the longest in the retention section. It ends on "Wearables and apps record activity. A record of body change between check-ins is a different kind of data." This contrast pair states a difference without saying why a product team should care. The fresh example is decoration, not evidence.
3. **Filler and redundancy at the two AEO answers:**
   - Line 136: "FitXpress by 3DLOOK is one option built for this."
   - Line 107: "a hardware-free alternative to a 3D body scanner… with no extra hardware".
   - Line 145 has a spec-sheet run: "one hypothesis… One testable example… one measure", followed by "one spot" on line 147.
- Actor drift: "platform", "app" and "product team" swap roles within S3 (lines 73, 77, 79). Readable, but the subject keeps changing.

### D. Format and structure: 3/3
- Taken from the code verdict.

### E. Output quality, position: 3/4
**Commercial bridge for product and growth people: works.**
- It opens on a product scene (line 48: "The weight chart has barely moved… Nothing in the app shows it.") and turns it into a product decision (line 52).
- CTA 1 arrives at 16% after a liftable short-answer block. Every H2 is a decision a product team owns: placement, outputs and limits, hardware vs photos vs in-app, selection criteria, the test.
- It takes real positions:
  - "Each method should keep its own trend line, because numbers from different methods are not interchangeable" (line 132)
  - "They count all app users, and paying members may behave differently" (line 85)
  - "their results are reported separately" (S8)
  - the baseline-placement trade-off (line 71)
- What is missing for a growth reader: an outcome hypothesis for the premium tier. Line 77 only says the team "decides which features sit in the paid tier", and the audience.md hook for this segment is "premium-tier monetization".

**Distinct from the hub `ai-in-fitness-industry`: mostly.**
- No capability survey, no bias section, and one up link.
- S4 re-argues the hub's own "Why AI in fitness matters now" case (low day-30 retention, then visible progress as a reason to return) with different sources.
- Cross-page note, hub side: the hub cites a different "seven in ten users… stop using a fitness app" (mhealth.jmir 2026). A reader moving hub → article meets two different 70% framings, and the hub's wording is the one the pack forbids for this page ("Not 'fitness apps lose 70%'").

**Distinct from the landing: partly.** The framing differs, since the article argues and the landing sells. But four passages are near-verbatim landing copy:
- Line 79 (FIT-WHITELABEL) matches the landing's FAQ "What body scanning SDKs work…".
- Line 138, "The recommended setup pairs the SDK with the API, because pose and framing validation runs in the SDK's capture layer", matches the landing's "Recommended setup" line.
- Line 75 matches the landing's step 3.
- Line 149, "members assigned at random where practical… written down before launch", restates the landing's pilot steps 2-3.

Some of this is claim text the plan required, but the volume makes the page read as the landing's prose twin in S3, S7 and S8.

**AEO quotability: S6 is close; S7 is not yet quotable.**
- **565780358696** (hardware alternative for studios, line 107):
  - The answer-first shape is right and names FitXpress.
  - It only covers studios "that run a member app", although FIT-SDK includes a **web** SDK.
  - The paragraph never says what the scan returns. An assistant quoting it gets "a guided scan inside that app" and nothing measurable.
- **565540613659** (body composition tracking software, line 136):
  - The criteria sentence is good.
  - The FitXpress sentence ("one option built for this") gives an assistant nothing to quote: no outputs, no "body composition", no delivery route.
  - The evidence bullet (line 140) risks a misquote about composition validation (see B).

Why 3, not 4: the article is about 10-20 minutes of edits from shipping (fixes 1-3), and the landing duplication in S3, S7 and S8 is the remaining distinctness debt.

## Top 3 issues (priority for the fix pass and the improver)

1. **Claims ambiguity in the AEO block (S7, line 140).** Change: "FitXpress ties its figures to expert pattern-maker tape measurements and a repeat-scan protocol." It must say these are **body measurement** figures and that composition estimates are derived (FIT-OUTPUTS-NOTE). Otherwise, next to the DXA example, an assistant can quote it as composition validation.
2. **The S7 answer cannot be quoted (line 136).** Change: "FitXpress by 3DLOOK is one option built for this." It must state what FitXpress returns and how, within FXS-SPEED / FXS-OUTPUTS / FXS-DELIVERY: two smartphone photos, 80+ body measurements and body composition estimates, through an SDK and API inside the app.
3. **The S6 answer is too narrow and not self-contained (line 107).** Change: "For a studio or gym that runs a member app, a hardware-free alternative to a 3D body scanner is a guided scan inside that app."
   - It should not exclude studios without their own app. FIT-SDK names a web SDK.
   - It should drop the "hardware-free… no extra hardware" redundancy with the next sentence.
   - The paragraph should say what the scan returns (FXS-OUTPUTS), so the quoted answer carries a measurable output.

Next in line, not blocking:
- 4: de-duplicate the landing echoes (lines 75, 79, 138, 149) and the onboarding-completion restatement (lines 71/147).
- 5: give the ACSM paragraph (line 89) a product-team consequence, or cut its last two sentences.
- 6: reconcile the publish-package meta description with final.md.

## for_agent_improver

- **seo-editor:** before adding an "expert trade-off" or "position" in Pass 3, diff it against the live landing snapshot the editor already reads, and against the plan's per-section `Boundary`. The onboarding trade-off reintroduced the one landing answer the plan barred. Add a step that lists every sentence sharing 8 or more consecutive words with the landing, and justify each one as mandated claim text or rewrite it.
- **seo-editor / seo-planner (AEO sections):**
  - An answer-first paragraph that names the product must contain at least one concrete output and the delivery route. "X is one option built for this" fails.
  - Check that the answer's scope is no narrower than the AEO prompt: "studios" ≠ "studios that run a member app".
- **seo-planner:** when a criteria bullet sits under a body-composition heading and cites FXS-ACCURACY, the outline must say "body measurement figures" explicitly (FIT-OUTPUTS-NOTE), not "point back to Section 5".
- **seo-planner:** S8 asked for "random assignment where practical; success criteria written before launch". That is the landing's pilot steps 2-3 in other words, which contradicts the plan's own line "the landing owns the pilot steps". Cross-check must-cover items against the cannibalization table before handing off.
- **seo-publisher:** compute the CTA positions in meta.md's judgment checklist from the lint output (`landing CTAs at x% / y% / end`), not from the plan. Take the word count in Open items from the final lint run. Make the Yoast description equal final.md's `meta_description`, or state why it differs.

## Coordinator review

coordinator_review: (to be filled in by the coordinator)

```
agreement: ✅ agree
top_issue: S7 answer and evidence lines gave an assistant nothing quotable and let "its figures" read as composition validation; fixed in the editor's QC pass (2,068 words, lint PASS), along with the S6 answer scope and the landing echoes.
```
