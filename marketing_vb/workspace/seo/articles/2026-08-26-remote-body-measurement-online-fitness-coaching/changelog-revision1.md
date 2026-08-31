# Changelog — Remote Body Measurement for Online Fitness Coaching Programs, Revision 1

**Base text:** `draft-v2-final.md` (status `edited`, 2026-08-26; frozen review copy `review1-version1.md`, identical body)
**Review input:** `review1-comments.md` (Review 1 tab, 8 numbered priority recommendations)
**Output:** `draft-v3-revision1.md` (status `revision1`, 2026-08-31)
**Editor:** seo-editor (revision round, not a fresh edit)

This is a revision on top of the reviewed text. Section order, section boundaries and a large share of
the phrasing changed. The approved claims used are unchanged in substance (FX-001, FX-002, FX-003,
FX-005, FX-006, FX-007, FX-008); FX-004 remains absent. Two claim *wordings* changed and need Vadim's
sign-off, both flagged under "Claim-wording changes for approval" below.

**Length:** 2,582 prose words (body from H1 to end, HTML claim-comments and table markup rows excluded);
2,839 body words including tables; detector counts 3,015 including headings and markup. Target band for
this round was 2,300-2,600. Previous version: 2,525 prose words.

**Detector, final run (run by me on this output, 2026-08-31):**

```
SEO / blog article · en · 3015 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

JSON form of the same run: `hard_fails: []`, `house_rule_violations: []`, `markers_by_category: {}`,
`em_dashes: 0`, `punch_triad_count: 0`, sentence-length variation `0.48` (monotone threshold is 0.35).

---

## Item-by-item

### 1. Sharpen the differentiation — applied

- **Deleted the standalone `## Why this matters now` H2 in full** (the online-coaching-as-standard-model
  framing, the rising-CAC argument, the retention-economics argument, the "clients arrive expecting
  personalization" paragraph). None of it was relocated. The retention economics went out with item 4,
  not into another section.
- **The up-link to the AI-in-fitness hub survives as a single clause** in the second intro paragraph:
  "Wider background on how structured body data is used across fitness products sits in the
  [AI in the fitness industry](https://3dlook.ai/content-hub/ai-in-fitness-industry/) hub." One anchor,
  descriptive, no market-trend prose attached to it.
- No general fitness-industry or market-trend discussion remains anywhere in the body. Every section now
  serves one of: coach and platform workflow, onboarding, recurring check-ins, how coaches read the data,
  integration, pilot evaluation, limitations.
- The reviewer's second note (overlap with the older `ai-body-scanning-for-fitness` page, "consider
  redirecting or rescoping that older page separately") is **out of scope for this deliverable** and is
  carried to open items for Vadim as a separate content-ops decision.

### 2. Improve the article order — applied, exactly the reviewer's sequence

| # | Reviewer's section | Where it is now |
|---|---|---|
| 1 | Introduction and scope | H1 + two intro paragraphs + italic scope note |
| 2 | The measurement problem in remote coaching | `## The measurement problem in online fitness coaching programs` |
| 3 | What remote body measurement provides | `## What remote body measurement provides` |
| 4 | How it fits the coaching workflow | `## How it fits the coaching workflow` |
| 5 | How coaches can use the results | `## How coaches can use the results` (new, item 5) |
| 6 | Comparison with scales, tape, photos, BIA, DXA | `## Comparison with scales, tape measurements, photos, BIA, and DXA` (rebuilt, item 6) |
| 7 | Where FitXpress fits | `## Where FitXpress fits` (moved from position 5 to 7) |
| 8 | Accuracy, repeatability, privacy, implementation | `## Accuracy, repeatability, privacy, and implementation` (three H3s) |
| 9 | How to evaluate a pilot | `## How to evaluate a pilot` (new, item 5) |
| 10 | Best-fit programs and limitations | `## Best-fit coaching programs and limitations` (+ H3 `What FitXpress does not do`) |
| 11 | FAQs | `## FAQs` (7 items) |
| 12 | Conclusion and CTA | `## Conclusion and next steps` |

Consequences of the move worth recording:

- The old `What improves operationally` H2 is gone as a section. Its defensible content was redistributed:
  intake consistency into section 4, coach-time economics into section 9 (as a pilot measure), and the
  premium-tier monetization line was **dropped entirely** (unsupported commercial framing, item 4).
- The old standalone `What FitXpress does not do` H2 is now an **H3 inside section 10**, because the
  reviewer's 12-part order has no twelfth slot for it and section 10 is explicitly the limitations
  section. The boundary language itself is unchanged in force and is stated in full. Flagged so the
  publisher's strategy checklist ("boundary section present") is not confused by the heading level.
- Section 1 is the intro block under the H1 (no H2 of its own), which is how the previous version and the
  house 12-part template already worked, so the body carries 11 H2s for reviewer sections 2-12.

### 3. Correct or qualify product statements — applied

- **Five output classes separated** into an explicit five-item list in section 3: model-generated body
  measurements (80+); software-derived body-composition estimates (body fat percentage, lean mass, fat
  mass); calculated outputs (BMI, BMR); a predicted weight from Smart Scales; the 3D model. Body
  composition is never called "body composition" flat again; it is "body-composition estimates" or
  "software-derived body-composition estimates" everywhere, including in the comparison table, in section
  10's boundary paragraph, and in the FAQ.
- **A follow-on paragraph states the measured-vs-derived distinction** in plain terms (a circumference
  comes from the model's geometry; body fat percentage comes from a formula applied to those figures and
  carries the formula's assumptions), with the practitioner note that composition reads best as a trend.
- **`±3.5%` is gone.** Replaced with the approved wording: "approximately 3.5% average prediction error
  under evaluated conditions" (FX-006). Zero `±` characters in the file.
- **The broad repeatability claim is gone.** "FitXpress scan-to-scan repeatability is typically < 1 cm"
  (four occurrences in the previous version) is replaced by the reviewer's exact sentence, used once in
  the body and once in the FAQ: "For most evaluated measurements, repeated scans showed typical
  scan-to-scan differences of less than 1 cm." (FX-003)
- **96-97% and 1.5-2.0 cm are attributed** as "Internal validation against expert manual measurements
  showed approximately 96 to 97% accuracy, with typical absolute error of 1.5 to 2.0 cm" (FX-001,
  FX-002), and in the FAQ as "In internal validation against expert manual measurements, typical absolute
  error ran 1.5 to 2.0 cm." The reserved words "independent", "third-party" and standalone "validated"
  are not used (editorial guardrail #3); "internal validation" is the sanctioned default framing.
- **Weight is no longer presented as a universally required input.** Section 4, step 1 now reads: "Which
  profile fields that step requires varies by program, and weight is optional in supported workflows,
  since Smart Scales predicts a figure from the photos and the software flags a difference when a
  self-reported weight is also supplied. BMI is a calculated output that depends on height and weight
  both being available." Verified against `tech-spec.md` (BMI calculated from height + weight; Smart
  Scales estimate + mismatch flag "when self-reported weight provided") and `how-it-works.md`. **Age is
  no longer listed as a required input at all** (the previous version's "height, current weight, age,
  gender" enumeration is gone), because the required field set varies by program.
- **DXA everywhere.** Expanded once at first use as "dual-energy X-ray absorptiometry (DXA)" in the first
  sentence of section 6; short form thereafter. `DEXA` appears zero times in the file. BIA expanded in the
  same sentence as "bioelectrical impedance analysis (BIA)".
- **Privacy wording aligned to the live policy** (verified 2026-08-31): "Data is encrypted in transit and
  at rest on Amazon Web Services (AWS) infrastructure, and photos are either deleted immediately after
  processing or retained for up to 30 days, depending on the business client's configuration. Retained
  photos are automatically blurred." The blurring sentence carries
  `<!-- source: FitXpress Privacy Policy, verified 2026-08-31 -->`. HIPAA-compliant / GDPR-aligned is
  retained as FX-007 (internal commitment) and is **not** attributed to the privacy policy. `SSE-S3` and
  `Amazon Simple Storage Service` no longer appear in the body.
- **Not applied:** the reviewer's requested sentence "FitXpress is not positioned as a medical device."
  See "Not applied" below.

### 4. Remove unsupported commercial claims — applied, all six deleted

| Flagged sentence | Status |
|---|---|
| "Progress a client cannot see is progress they stop paying for." | Deleted (was intro para 1) |
| "Retention is the number that decides whether an online coaching business survives its second year." | Deleted (was intro para 1) |
| "Acquiring a new client costs more every year." | Deleted with the whole `Why this matters now` section |
| "A subscriber who renews for a year is worth several who churn." | Deleted with the same section |
| "A client…has a concrete reason to renew." | Deleted (was `What improves operationally`) |
| "Visible progress supports retention." | Deleted (was the conclusion) |

Retention and engagement now appear only as something a platform can test against a baseline, in three
places, all framed as measurement:

1. Pilot metric 7: "Engagement or retention measured against the program's own pre-pilot baseline."
2. Section 9's closing paragraph: "A pilot can test whether a progress view moves them against a baseline
   the program already has. Treating the movement as a given before the test defeats the point of running
   one."
3. Section 10's buyer paragraph: "The question they bring is whether body-data personalization moves
   engagement and retention enough to justify the build, which a pilot measured against a baseline can
   answer." (A buyer's evaluation question, not an asserted effect.)

The conclusion no longer mentions retention at all.

### 5. Add more decision-making value — applied

- **Section 5 "How coaches can use the results"** carries the reviewer's 4-row table verbatim in
  structure and, with one exception, verbatim in content: columns *Coaching stage / Data reviewed /
  Possible coach action / Limitation*; rows *Onboarding / Recurring check-in / Apparent plateau / Program
  completion*. **One word changed:** row 3's "Weight plus regional measurements" is written as "Weight and
  regional measurements", because "plus" as a connector of outputs is a hard ban
  (`terminology-guardrails.md` §2.7). A short paragraph after the table points at the fourth column and
  closes with the single body-side statement of who decides ("FitXpress supplies the structured record;
  the coach makes the call").
- **Section 9 "How to evaluate a pilot"** carries all seven pilot metrics, in the reviewer's order,
  introduced as process measures the platform reads from its own data. Two paragraphs of judgment follow:
  completion and retake rates gate everything after them, coach review time is the measure operations
  leads ask about first, and engagement/retention sits last on purpose. No pilot metric is presented as an
  outcome FitXpress promises.

### 6. Refine the method-comparison table — applied, rebuilt

Old table: 5 rows (self-report, tape, connected scale, progress photos, mobile body scan), with
"Connected scale | Weight, sometimes an impedance estimate | One number; hides recomposition".

New table: 7 rows.

- **Consumer smart scale split from professional BIA.** Consumer scale now reads "Weight, and an
  impedance-based body-composition estimate", limitation "Composition estimates depend on hydration,
  device model, and electrode placement". Professional BIA is its own row ("Weight and segmental
  composition estimates from a calibrated device", limitation "Requires an in-person visit; results depend
  on the device and the preparation protocol").
- **The "one number" framing is gone** from the table and from the body. The old "a single-number scale"
  phrasing in the comparison prose and in FAQ 3 is also gone (grep: 0 occurrences of "one number").
- **DXA row added:** "Reference-grade body composition and regional fat and lean distribution",
  limitation "Clinic-based and appointment-bound; access and cost depend on the provider; circumference
  measurements sit outside its output".
- **Mobile scanning is presented as complementary, not as a replacement.** The prose after the table
  reads: "A mobile scan works alongside them. A client can weigh in daily on a connected scale, book a DXA
  read when a program genuinely calls for one, and scan monthly for the circumference and composition
  trend the coach reviews." FAQ 3 ("Can it replace a smart scale, BIA, or DXA?") answers "No" and
  describes complementarity.
- **DXA is not called the universal reference.** The previous version's "DEXA remains the clinical
  reference method for body composition" is now "DXA is a reference method for body composition in
  clinical and research settings", with circumferences explicitly outside its output.
- **Sideways link added:** "Differences between scanning approaches themselves, including two-photo
  capture, video, and hardware booths, are set out in [2-Photo vs Video vs Hardware body
  scanning](https://3dlook.ai/content-hub/body-scanning-technology-comparison/)." This closes the
  long-standing "sideways link omitted" open item (plan Open items #6, write-stage #3, edit-stage #4,
  publish-stage). The reviewer's instruction overrides the earlier editorial choice to omit it; the target
  is a technology-comparison page in the same product family, so there is no Fitness/GLP-1 boundary risk,
  which was the original reason for the omission.

### 7. Reduce repetition — applied, counts verified by grep on the output

| Point | Body | FAQ | Total |
|---|---|---|---|
| `80+` measurements | 1 (section 3, output list) | 1 (FAQ 5) | **2** |
| `under 45 seconds` | 1 (section 3) | 1 (FAQ 2) | **2** |
| repeatability sentence (`less than 1 cm`) | 1 (section 8) | 1 (FAQ 4) | **2** |
| privacy / photo deletion (`30 days`, `immediately after processing`) | 1 (section 8) | 1 (FAQ 6) | **2** |
| who decides | 1 (section 5, "the coach makes the call") | 1 (FAQ 7, "The coach decides.") | **2** |
| visible progress / retention as an effect | 0 | 0 | **0** (item 4) |

Also de-duplicated on the way: the `1.5 to 2.0 cm` figure (1 body + 1 FAQ), `HIPAA` / `GDPR` (expanded
once in section 8, short form once in FAQ 6), and the "production conditions are not lab conditions" line
(1). `FitXpress is not a medical device` appears twice on purpose (scope note + boundary section), which
`editorial-guardrails.md` M2 permits explicitly: the rule governs negation density inside a sentence, not
disclaimer frequency across sections.

### 8. Adjust the tone — applied, all five lines gone

| Flagged line | What replaced it |
|---|---|
| "easy to misrepresent, whether on purpose or not" | "How each of those figures was produced goes unrecorded." Self-report is described as varying by scale, timing and technique, with no imputed motive. |
| "an invisible result is a cancelled renewal" | Deleted with the retention framing (item 4). Nothing punchy substituted. |
| "The split is clean" | Deleted. The integration boundary is now stated plainly across two sentences ("3DLOOK provides… The platform builds…"). |
| "Small real changes survive measurement noise" | "When scan-to-scan differences stay that small, a modest real change is more likely to be distinguishable from capture variation." |
| "a coach can point to it and defend it" | Deleted. No replacement assertion. |

No new punchy assertions were introduced in their place. The strongest remaining lines are analytical
rather than promotional (the fourth-column paragraph in section 5, the review-time observation in section
9, the "not the right tool for every practice" paragraph in section 10).

---

## Claim-wording changes for approval (Vadim)

Both come from item 3 and both change how an approved claim is worded, so they need a yes before publish.

1. **FX-007, SSE-S3 downgraded to a plain encryption statement.** The body now says "encrypted in transit
   and at rest on Amazon Web Services (AWS) infrastructure" and no longer names Amazon Simple Storage
   Service or server-side encryption with Amazon S3 managed keys (SSE-S3). Reason: the public FitXpress
   Privacy Policy (verified 2026-08-31) states encryption in transit and at rest, enforced by default, and
   AWS hosting, but does not state SSE-S3; SSE-S3 is an internal security-commitment detail. FX-007's text
   in `context-pack.md` still names SSE-S3, so this is a deliberate softening of an approved claim, not a
   drafting slip.
2. **FX-007, blurring detail added.** "Retained photos are automatically blurred." is new to this article,
   sourced from the privacy policy ("When temporary storage is selected, all retained photos are
   automatically blurred") and consistent with `about-me.md` ("auto-blurred if retained"). Carries an
   inline `<!-- source: FitXpress Privacy Policy, verified 2026-08-31 -->` comment.

Also worth a glance, lower stakes:

3. **Repeatability is no longer written as `< 1 cm`.** `about-me.md` locks the convention "write
   repeatability as `< 1 cm`"; the reviewer's mandated sentence spells it "less than 1 cm". The reviewer's
   wording is used, matching the precedent set in `glp-1-market-hub/changelog-revision1.md` item 4. If the
   locked convention is meant to win, the two sentences need reconciling at source, not per article.

---

## Not applied / applied differently

1. **NOT APPLIED — "Use the approved wording: 'FitXpress is not positioned as a medical device.'"**
   (review item 3, seventh bullet.)
   The article keeps the direct form: **"FitXpress is not a medical device."**
   Reason: "positioned as" is a hard ban for product, intended-use and regulatory statements in
   `brand-assets/content-strategy/terminology-guardrails.md` (Part 2 §2.10, and the Overrides table at the
   top of that file, ~line 32). That file is the offline copy of Asselya's Doc *"General Approach &
   Language Guardrails for Corporate Content"*, doc modified **2026-08-13**, synced into the repo
   **2026-08-25**, and its Overrides table records explicitly that it **supersedes
   `brand-assets/style-guides/editorial-guardrails.md` #6**, which is where the reviewer's wording comes
   from (that principle prescribed "not positioned as a medical device" from 2026-06-09 until the
   2026-08-25 amendment). `CLAUDE.md` §6 and §15 hard requirement #7 carry the same override, and the
   detector flags `not positioned as` as a hard fail. Applying the review line as written would fail the
   gate this article has to pass.
   **This is an unresolved conflict between two governing documents and one reviewer instruction. Listed
   as an open item for Vadim/Asselya to settle (which document wins).** No silent bend either way: the
   guardrail was followed and the deviation from the review is recorded here.

2. **Applied differently — the boundary section's heading level.** Review item 2's 12-part order leaves no
   slot for a standalone `What FitXpress does not do` H2, and the positioning rules require the section to
   exist. It is now an **H3 inside section 10** ("Best-fit coaching programs and limitations"), which is
   the section the reviewer designated for limitations. Content and force unchanged.

3. **Applied differently — BIA and DXA are expanded in the first sentence under the section heading, not
   in the heading itself.** The reviewer's section title ("Comparison with scales, tape measurements,
   photos, BIA, and DXA") is kept verbatim, so the acronyms' first appearance in the file is a heading.
   Both are expanded in the sentence immediately following it. Guardrail M1 is about first use in the
   text; expanding inside a heading would read as boilerplate. Flagged because a mechanical M1 check will
   see the heading first.

4. **Out of scope — the older `ai-body-scanning-for-fitness` page.** Review item 1 suggests redirecting or
   rescoping it "separately". Nothing in this deliverable touches that page. Carried to open items.

5. **Not attempted — a named coaching customer.** No fitness-coaching customer exists in
   `proof-points.md` (Yazen and UK Meds are weight-loss/pharmacy and would breach the vertical boundary).
   The article still runs on capability and segment framing with zero named customers. Unchanged from the
   previous version, and still an open item.

---

## Guardrail and hard-rule verification (run on the output)

- **Claims:** only FX-001, FX-002, FX-003, FX-005, FX-006, FX-007, FX-008. **FX-004 absent** (grep for
  "ISO 8559", "0.40 cm", "1,152", "14 companies", "multi-company": zero hits), so it is never combined
  with FX-001/FX-003.
- **No number outside the approved set.** The previous version's illustrative "1.4 cm" example was
  rewritten to "moved… by more than the scan-to-scan variation" so no unapproved figure reads as a claim.
  Remaining numbers are approved claims or neutral scenario references (week one, week eight, six-week
  blocks, twelve-week challenge, two hundred clients, about a minute).
- **Named competitors:** none (Prism / Bodygram / Size Stream / Mirrorsize: zero hits).
- **Vertical boundary:** `GLP-1` appears exactly once, inside the boundary statement, expanded as
  "glucagon-like peptide-1 (GLP-1)". No wellness-rewards language anywhere.
- **Em dashes:** 0. **Banned words** (CLAUDE.md §6 list, plus `utilize`): 0. **`positioned as`:** 0 in the
  whole file, frontmatter included. **`by hand`:** 0. **`plus` as a connector:** 0. **`objective` about
  our own tech:** 0. **`so` as a result connector:** 0 (two were introduced during drafting and removed on
  the second pass). **`rather than`:** 0. **Presumed reader reactions:** 0. **Behaviour attributed to
  concepts/platforms:** 0 (the v1 anthropomorphism hard fail stays fixed; "the platform team decides how
  that data is used" keeps the actor human, and a "the number that decides" phrasing written during this
  round was removed).
- **Internal links, four directions, each anchor once:** up ×1 (AI in the fitness industry), sideways ×1
  (2-Photo vs Video vs Hardware body scanning), trust ×1 (mobile body scanning accuracy framework),
  down ×2 with two different descriptive anchors (mid-article MOFU evaluation after section 7, BOFU in the
  conclusion). Five links total, all internal.
- **Abbreviations expanded at first use:** BMR, BIA, DXA, API, SDK, HIPAA, GDPR, AWS, CTO, GLP-1. BMI and
  CEO left bare per the 2026-08-25 commonly-known exception.
- **Stacked negation (M2):** the boundary paragraph states the medical-device boundary directly, then the
  intended-use sentence, then the conditional reference-method sentence, one negation each, followed by a
  positive "What FitXpress does is narrower" paragraph.
- **FAQ:** 7 items retained, all 2-5 sentences, including "Can it replace a smart scale, BIA, or DXA?"
  (widened from the old smart-scale/DEXA pair) and "Does the coach or the tool decide anything?".
- **CTA by intent:** mid-article MOFU evaluation link, BOFU demo line in the conclusion. Author unchanged
  (Assel Sekerova). Scope note unchanged and still in position 1.
- **Pass 3c self-check** (the "what still reads like machine text?" step) is written into the draft's
  frontmatter `self_check` field, per the editor's own pass requirement. Five points, including the two
  slips the detector cannot match (a `so`-as-result connector and behaviour attributed to a number) that
  were fixed on the second pass, and the one weakness left standing (no named customer, no external
  source).
