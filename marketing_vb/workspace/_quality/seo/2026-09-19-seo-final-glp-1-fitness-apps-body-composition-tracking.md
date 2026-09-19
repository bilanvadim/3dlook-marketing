---
qc_date: 2026-09-19
agent: seo-editor (final.md) + seo-publisher (publish-package.md)
artifact: workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md (+ publish-package.md)
track: seo
artifact_type: seo-final
total_score: 14/20
status: marginal
scope: judgment only, checkpoint 2
coordinator_review: |
  agreement: ⚠️ disagree on one fix (I agree with the score and with #1 and #2). Folding S9 into S7 removes a section from the 12-part outline Vadim approved at checkpoint 1. I am trimming S9 and taking out the paraphrase of the coaching article, but S9 stays.
  top_issue: The publisher treated the plan's "cannot claim" list as rules for the body text and never checked the meta against it, so an unattributed clinical claim reached the search snippet.
---

# QC Report — seo-editor + seo-publisher — 2026-09-19

**Artifact:** `workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md` and `publish-package.md`
**Total: 14/20** — marginal. The article body on its own would score about 16. The blocking defect is in the package meta.

**What this report covers.** The mechanical checks are taken as passed: every `article_lint.py` gate passes except M1 on the H1, which Vadim accepted at checkpoint 1, and the detector returns CLEAN 0.0. This report covers only judgment. I could not re-fetch the external sources, because this session has no WebFetch. Source fidelity was checked against the verbatim log in plan-audit §7 and the editor's verification notes.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- **The body follows the plan closely.**
  - All 12 sections are present, in the planned order.
  - Only the planned claims are used: FX-001, FX-002, FX-005, FX-006 and FX-007.
  - All 9 internal links are in place.
  - The JAMA Viewpoint was cut, which the plan allowed.
  - Yazen does not appear in the copy.
  - The H1 is unchanged: `final.md:36` matches `plan.md:175`.
  - M1 is recorded as the accepted failure.
- **The editor's `self_check` does not match the text.**
  - It says the clinical boundary "now appears once each in the scope note, the Section 5 route bullet and the Section 7 compliance line" (:30). It also appears at :56, :143-144, :164 and :174.
  - It calls the pointer-sentence shape "Fixed" (:29). Thirteen pointer sentences remain, including a standalone one-sentence paragraph at :66.
- **The publisher's checklist contradicts the text in three places.**
  - package:128 says "`buyer`/`customer`: neither word appears". `final.md:104` has "real-world customer dataset". That wording is the canon §5 sentence, so it is acceptable, but the check was not actually run.
  - package:303-305 says :158 "uses the live trust-FAQ's own HIPAA and GDPR sentences". The paragraph uses neither sentence. It points to the FAQ, which is the right move.
  - package:68 announces "Three external figures" and then lists four.
- **The meta was not checked against the plan's claim limits.** The publisher did not apply plan.md's "What the article cannot claim about muscle loss" to the meta (see B). Under `seo-publisher.md:69`, a positioning failure means STOP. The package shipped as 9/9 instead.
- **Yazen appears in both files, read literally.** package:344-345 has "No Yazen in any alt text…" and `final.md:27` has "No Yazen, no UK Meds". Neither is copy, but Vadim's constraint names the package.
- **The JAMA decision is not recorded.** Plan Open item 7 was dropped without a line saying whether verification was attempted.

### B. Factual accuracy — 4/5
- **Numbers.** Every figure traces to FX-001, FX-002, FX-005, FX-006, FX-007 or one of the three marked external claims. The accuracy short forms are verbatim from §5, with "Internal" restored. There are no drug names, doses or trial names.
- **Sourcing.** There are 3 external sources, all neutral:
  - PubMed 38937282, linked twice (:60, :170);
  - PubMed 40445127 (:64);
  - KFF (:70).

  obesity.org appears only in a comment; package Open item 2 covers the mismatch with the link target. There are no vendor blogs.
- **Fidelity to Neeland et al.**
  - The range keeps "some" and both ends (:60).
  - The point that lean mass is not muscle carries the full list: organs, bone, fluids and water in fat tissue (:62).
  - "appear to be adaptive" is quoted and attributed.
  - One sentence is not in the plan-audit §7 verbatim log: "The authors list population, drug-specific, and comorbidity effects among the possible reasons." (:60). The editor says it was checked against the abstract, and it is hedged. I could not re-fetch it. Low risk.
- **Lean mass versus muscle in the body.** The distinction holds everywhere. FitXpress is never said to measure or monitor muscle (:48, :98, :170).
- **The meta description breaks the claim rules.** Recommended description (package:21-22): "Scale weight can hide GLP-1 muscle loss. See what fitness apps can track instead, body composition estimates and circumferences…".
  - It asserts muscle loss in our own voice, without attribution.
  - It presents composition estimates as what reveals muscle loss.
  - The body spends four sentences separating lean mass from muscle. The search snippet undoes that, with no scope note beside it.
  - Variant 3 goes further: "A falling scale number hides GLP-1 muscle loss."
- **The body implies a capability the plan forbids.** Two sentences read together:
  - :64 "Strength training is the part of that priority a fitness app already delivers."
  - :74 "Circumferences and composition estimates, shown next to training history, can make that contribution easier to see."

  Together they say the app delivers the lean-mass-preservation priority and the composition view shows whether it worked. That is the "lean mass preservation tracking" capability that plan.md:160 forbids, reached by implication. No approved evidence supports it either: FX-002 covers body measurements, not composition estimates.
- **Professional BIA is called a "reference method"** at :100 and :142. The live coaching page uses "reference method" only for DXA and describes BIA as periodic assessment with standardized equipment. That wording is loose for a body-composition audience.

### C. Brand & tone — 2/3
- **The judgment lines are clean.**
  - No we, our or you.
  - No corrective "X, not Y" or "rather than" in the body. The scope note's "is not a measurement of muscle" is the one licensed product boundary.
  - "FitXpress is not a medical device." is verbatim (:48, :121).
  - HIPAA and GDPR are named only as topics of the FAQ, with no status claim (:158). That matches compliance.md §9: link, don't restate.
  - "customer" appears only inside the canon repeatability sentence (:104).
  - No content-plan labels appear in the copy.
- **The boundary refrain is too heavy for audience.md segment 3**, which asks for a lighter, less clinical tone. It is the repetition pattern Assel sent revision 5 back for.
  - "Clinical questions stay with the clinician" appears in 8 places: :48, :56, :84, :116 with :121, :143-144, :164 and :174.
  - The "medication, doses, side effects" triad appears 3 times (:48, :84, :116).
  - "FitXpress is not a medical device." appears twice.
  - "Does not measure muscle" appears 3 times (:48, :98, :170).
- **The meta description reintroduces the corrective frame.** "track instead" is the shape the H1 was reworded to avoid with "Beyond Scale Weight". The appositive "instead, body composition estimates and circumferences, and where FitXpress fits" also does not parse.

### D. Format & structure — 2/3
- **What is complete.**
  - `final.md` frontmatter has product, status, claims, `changes_summary` and `self_check`.
  - The package has the meta, both checklists, verbatim lint and detector output, alt text, open items and clean article copy.
  - The meta title is 56 characters and the description 154.
- **Word counts disagree.** `final.md` carries a non-publishable Open items block after the article body (:184-191). That block is why lint reports 2223 prose words. The three files now give three counts: `final.md` `word_count` 2031, the package 2164, lint 2223.
- **The Category value would put internal labels on the site.** package:26 reads "Content Hub — AI in Fitness (Hub 1), GLP-1 bridge into GLP-1 Market (Hub 3)". It carries content-plan labels and an em dash. Pasted into the CMS as written, both become visible. It is flagged as inferred (Open item 6) but still offered as the value.

### E. Output quality — 3/4
**The page's intent is distinct at its core.** Three things appear on no sibling page:
- the role split in S7;
- the question of whether the app needs to know about medication (:90, FAQ 3);
- the fitness-app reading of the lean-mass evidence in S3.

The strongest line on the page is at :74: "For members treated for weight management, a falling scale weight is the expected direction. A progress view built on the scale then says little about what the training program adds." There is no overlap with top-7, since the page lists no tools, and none with visual-progress, which is only linked for engagement.

**Where the page repeats its siblings:**
- **S5 repeats glp-1-market's "What Scalable GLP-1 Progress Tracking Requires".**
  - :80 "It uses the same guided capture as every later scan." The hub has: "The initial record should use the same defined capture process that will be applied during later check-ins."
  - :82 paraphrases the hub's "Repeatable remote capture" item.
  - Only the route bullet and :90 are specific to GLP-1.
- **S9 repeats coaching's "Best-fit" section.**
  - :154 "Fit is lower for apps without a check-in cadence or a training program, and for apps with no defined use for composition data." Coaching has: "Operational benefit may be limited when measurement is infrequent, … or longitudinal body data has no defined use."
  - Its first two bullets restate the scope note.
- **S10 partly repeats coaching's implementation section.**
  - "Change thresholds" (:160) paraphrases coaching's "Change thresholds" line.
  - "An alternative path" mirrors coaching's "Accessibility and alternatives".
  - The consent paragraph, about two separate organizations, earns its place.

**Section verdicts:**
- **S1:** keep.
- **S2:** keep for answer engines. Bullets 1 and 5 restate S1 and the scope note.
- **S3:** keep. It carries the page's evidence.
- **S4:** keep. It carries the page's argument. Drop the capability clause at :74.
- **S5:** trim to the GLP-1-specific parts.
- **S6:** keep.
- **S7:** keep the table. The closing paragraph repeats the scope note.
- **S8:** keep. The third and fourth "Body composition estimates fit when" bullets restate S5 (:82, :83).
- **S9: cut.** Move its two links for GLP-1 programs into S7.
- **S10:** keep the consent paragraph and the pilot. Compress the thresholds and alternative path.
- **FAQ 1:** the scope note and :98 already settle it. Keep it for the search results on the keyword, but shorten it.
- **FAQ 2:** says nothing beyond "depends".
- **FAQ 3:** strong.

**Lines that still read as machine-made:**
- :46 "For an app team, the choice turns on two questions: …". This is the reference article's formula, used where no choice has been set up.
- :104, :106 and :108 are three paragraphs in a row that close on "[page] describes / sets out / describes …". The article has 13 such pointer sentences. The reference final has 3 in 1,877 words.
- :88 "Two parts of this workflow are hard to repair later: the baseline and the capture conditions." This is the "position" the editor added. It is a colon aphorism (editorial-rewrites §1 and §4). Its support overstates: "A baseline skipped at onboarding cannot be taken afterwards". A later baseline can be taken; it simply starts later. The real expert point is missing: members often join the app mid-treatment, so the app's baseline is rarely the start of GLP-1 weight loss.
- :125 "Each method answers a different question, and one program can use more than one."
- The page has 12 H2s, a list-to-prose ratio of 0.93 and 25 bold labels. It is the §7 comparison template filled in section by section. The reference final landed at 9 H2s.

## Top 3 issues (priority for improver)

1. **The meta description states GLP-1 muscle loss in our voice and implies apps can track it.** Quote (package:21-22 and variants 2-3): "Scale weight can hide GLP-1 muscle loss. See what fitness apps can track instead…"
   - **Fix (seo-publisher):** rewrite all three variants.
     - Present muscle loss as the topic the research examines.
     - Present composition estimates and circumferences as recorded alongside scale weight.
     - Drop "instead".
     - Imply nowhere that an app or FitXpress detects muscle loss.
   - Then re-run the content-strategy checklist; this should have been a STOP. **Blocks checkpoint 2.**
2. **S3 and S4 imply lean-mass-preservation tracking.** Quotes: :64 "Strength training is the part of that priority a fitness app already delivers." and :74 "…can make that contribution easier to see."
   - **Fix (seo-editor):** end S3 by placing strength training within the app's own programs, without "delivers".
   - In S4, state what the view displays, not that it shows the training's contribution.
   - The approved compliance.md §3 point can carry the method: composition values are estimates derived from the measurements plus height and optional weight.
   - Fix in the same round as #1.
3. **Repetition and overlap with sibling pages.** The boundary appears in 8 places, 13 paragraphs close on a pointer, and S9 and S10 paraphrase the coaching page. Quote: :154 "Fit is lower for apps without a check-in cadence…"
   - **Fix (seo-editor):**
     - Fold S9 into S7.
     - Reduce S10's thresholds and alternative path to one sentence each, with the coaching link.
     - Keep the clinical boundary in the scope note, the S5 route bullet and the S7 table with its sentence on doses and symptom tracking. Drop the last sentence of :174 and the "clinical questions routed out of the app" pilot measure (:164).
     - Keep one of the two sentences saying FitXpress does not measure muscle (:98 or the first sentence of FAQ 1).
     - Cut pointer closers where the paragraph above already carries the link, for example :106.
   - Not blocking.

Minor, not blocking:
- Replace "Yazen" in package:344 and `final.md:27` with "no customer name".
- Do not enter the Category string (package:26) as written.
- Fix the three package checklist claims listed in A.
- Record the JAMA decision.
- :88 overstates the baseline point.
- BIA is called a "reference method" (:100, :142).

## Coordinator review

(filled in by Claude in chat after the automatic QC run)
