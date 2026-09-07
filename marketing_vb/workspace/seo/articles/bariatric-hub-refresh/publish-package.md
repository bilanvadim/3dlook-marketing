---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
status: ready_for_review
created: 2026-09-03
revised: 2026-09-07
publish_type: refresh-republish-in-place
live_url: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
source_draft: draft-v3-editor.md
lint_verdict: "PASS, 9/9 gates (2026-09-07 fix-pass rerun of scripts/article_lint.py against draft-v3-editor.md as it stands after G1, with and without the context pack — see publisher-report.md §1)"
qc_fix_pass: "2026-09-07 — corrects three self-verification slips QC found at 17/20 (external-citation breakdown, meta-name-timing premise, marker-line recount) and re-syncs §6 to G1 (review-1-decisions.md §G); G1/G2/G3 recorded in §3h-3j"
review_applied: "review-1.md (verbatim extract of the Google Doc tab \"Review 1\") + review-1-decisions.md (the decisions file wins wherever the two differ)"
datePublished_action: "RE-DATE to the republish date — Vadim's call, 2026-09-03. Review 1 does not touch this."
datePublished_original: 2026-06-05
dateModified_set_to: publish date
author_byline: "Assel Sekerova"
vadim_decisions: "byline Assel · re-date the post · slug unchanged (2026-09-03, untouched by Review 1) · predicted-weight SUPERSEDED lint row scoped to wellness copy only, so it no longer fires on this page (2026-09-07)"
faq_branch: "B, 9 questions (down from 16 pre-Review-1; Review 1 D6)"
---

# Publish Package — Bariatric hub refresh (Review 1 rebuild)

`bariatric-hub-refresh` is the workspace directory name only. **Every downstream reference — CMS
slug, canonical URL, this file's own frontmatter — uses the published slug**
`bariatric-pre-qualification-mobile-3d-body-scanning`. This has bitten the pipeline before
(`plan.md` writer note #10).

This is the **second** publish package for this article. The first (superseded, snapshotted at
`v1/publish-package.md`) was built from `draft-v2-editor.md` on 2026-09-03 and went to an external
reviewer. This version is built from `draft-v3-editor.md`, which carries every ruling in
`review-1-decisions.md` applied by `seo-editor`. Nothing here has gone to the CMS; this rebuild is
the `publish` stage only.

**This is a fix pass on this same package**, applied 2026-09-07 after `quality-controller` scored it
17/20. Three lines in the package's own prose were wrong — an external-citation breakdown (§2), a
premise about where the product name enters the body (§1), and a marker-arithmetic recount (§3a) —
and are corrected below, each re-derived directly from the file rather than adjusted to fit. §6 is
re-extracted from `draft-v3-editor.md` as it now stands after the coordinator applied **G1**
(`review-1-decisions.md` §G) between the first version of this package and this one: the ±3.5%
weight-estimate passage no longer ships twice. §3h-3j record G1, G2 and G3 as resolved or open items,
the same discipline §3g already applies to decision D7.

---

## 0. Read this before touching the CMS — this is a republish IN PLACE

*Carried forward verbatim from the first package. Review 1 did not touch any of this; it is
reproduced here rather than referenced so this file stays self-contained.*

This is not a new article. It replaces the body of a live page at the **same URL** and the **same
slug**. Four things to get right at CMS entry. Items 2 and 3 are **Vadim's decisions of
2026-09-03**, already settled; items 1 and 4 are hazards that have cost this pipeline before:

1. **The slug does not change, even though it now mismatches the H1.** Live slug:
   `bariatric-pre-qualification-mobile-3d-body-scanning`. New H1 does not say "mobile 3D body
   scanning" (that framing was deliberately dropped, see §5 below). **Do not "fix" the slug to
   match the new H1.** The slug carries the page's publish history and backlinks. Changing it
   would require a 301 and lose both for no benefit.
2. **`datePublished` is RE-DATED to the republish date. Vadim's call, 2026-09-03.**
   This reverses the recommendation that stood earlier in this file's history, so the reasoning is
   worth recording. Re-dating buys a visible freshness signal on a page whose entire refresh case is
   that the 2026 facts moved, and it matches what the two sibling republishes did this year:
   `glp-1-market` (2026-08-28) and `online-pharmacy-bmi-verification` (2026-08-24) were both
   re-dated by the CMS. The cost is that the page's **June 5, 2026 origin date disappears from the
   live site**, exactly as it did for those two.
   **Where the original date survives:** `brand-assets/content-strategy/published-articles-inventory.md`
   (row 11 and the Hub #9 entry) records `datePublished` 2026-06-05T13:44:40+00:00 and the
   2026-07-27 expansion, and `published-live-2026-07-27.md` in this workspace is the captured
   pre-refresh text. Those two are now the only record of this article's true age. Set
   `dateModified` to the republish date as well.

3. **Byline: `Assel Sekerova`. Vadim's call, 2026-09-03.** Resolved, use it as-is. For the record
   of why it needed a decision: the live site alternates between two spellings of the same author.
   `Assel Sekerova` appears on this page's June and July versions and on the Online Pharmacy BMI
   Verification rewrite; `Asselya Sekerova` appears on GLP-1 Market and the "Top 7" listicle. Every
   draft in this workspace already says `Assel`, so nothing in the body changes. This decision
   settles the byline for this page only. The site-wide inconsistency is still open and still
   tracked in `published-articles-inventory.md`.

4. **Nothing in this body is safe to hand-edit at CMS-entry time.** Every sentence went through the
   terminology-guardrails pass; a well-meant copy edit at paste time (adding a clarifying em dash,
   softening the medical-device sentence, adding "leverage") re-introduces exactly what the editing
   passes removed. If something needs to change, change it in the workspace and re-lint, not in the
   CMS editor.

---

## 1. Meta

**Recommended title** (54 chars, **unchanged by Review 1** — D8 rules on the description only):
`Bariatric Pre-Qualification & Progress Tracking (2026)`

**Recommended description** (145 chars, **new — Review 1 decision D8, verbatim**):
`See how obesity care teams can use remote body data for bariatric pre-qualification, intake, pre-auth preparation, and post-op progress tracking.`

**Slug:** `bariatric-pre-qualification-mobile-3d-body-scanning` — **unchanged, see §0.1.**

**Category:** Use Cases (matches the live page's existing taxonomy — this is a republish, not a
re-categorization; not touched by Review 1)

**Tags:** Use Cases, Health, Technology (live page's current tags; carry forward as-is)

### Why this direction, and what changed from the first package

**The title is untouched.** `review-1-decisions.md` D8 says so directly: *"The recommended meta
title is untouched by this review."* It stays the compressed H1 (*"Bariatric Pre-Qualification and
Patient Progress Tracking..."*, 104 chars, over budget), keyword-first, with the `2026` recency
signal the slug itself never carries.

**The description rationale from the first package is obsolete and is replaced here, not left
standing, per the task brief.** The superseded rationale led with the 7-day payer clock as *"the
single most important factual change on the page."* Review 1's B1 ruling narrowed that same claim:
the clock excludes Qualified Health Plans on the Federally Facilitated Exchanges, applies only to
Medicare Advantage, Medicaid and Children's Health Insurance Program (CHIP) payers, and the two
inference sentences that gave it its edge in the meta description's register ("a missing timestamped
BMI record...becomes a denial that now carries a published reason") were deleted outright as
unsupported (B1a). The clock is still true and still stated correctly in §3 of the body, but a
snippet that has to stand alone without a paragraph's worth of qualification around it is the wrong
place for a claim that now needs three sentences of scope just to be accurate.

The reviewer's replacement drops the fact-claim hook entirely and leads with what the page's own
new ten-section spine actually delivers: four workflow touchpoints — pre-qualification, intake,
pre-auth preparation, post-op progress tracking — that map directly onto §1/§2 (pre-qualification
and the four-stage intake workflow), §3 (pre-authorization documentation) and §5 (patient progress
tracking). That is a more durable hook than a regulatory deadline that can itself be re-scoped by a
future rule change, and it still carries the primary keyword `bariatric pre-qualification` exactly
once, inside the first half of the string. FitXpress is still not named in either the title or the
description, consistent with `about-me.md`'s CTA-by-funnel-stage logic for a Hub page. **Corrected
premise (this fix pass).** The earlier version of this section rested that conclusion on a claim that
the product name "enters the body from §6 onward"; QC caught this as false. Checked directly against
`draft-v3-editor.md`: FitXpress is named exactly once before §6, as the actor in Stage 1 of the
four-stage workflow (§2, "FitXpress returns structured body data"), and then not again until §6
("Where FitXpress fits"), the section built to explain what it is, what it outputs and what it does
not do. The recommendation survives on the corrected premise: a title or description that leads with
the product name would front-load detail the body itself only front-loads once, in passing, well
before the section that actually carries it.

**One mechanical note.** `draft-v3-editor.md`'s own frontmatter `meta_description` field (line 8)
already carries the D8 text verbatim — the editor placed it directly, and this package is the record
of why it fits the budget and what it replaced, not a re-derivation.

### Alt options

**Meta title variants** (unchanged set from the first package; D8 does not touch the title)

| # | Variant | Chars | Note |
|---|---|---|---|
| 1 | **Bariatric Pre-Qualification & Progress Tracking (2026)** | 54 | **Recommended.** Keyword-first, keeps the year signal, keeps both spines. |
| 2 | Bariatric Pre-Qualification: Patient Progress Tracking | 54 | The content-plan's original target title, compressed, with "Patient" restored. No year signal. Use if Vadim prefers the plan's literal copy over the year signal. |
| 3 | Bariatric Pre-Qualification and Progress Tracking, 2026 | 55 | Same content as the recommendation, "and" instead of "&" and a comma instead of parentheses, for house style if ampersands are disfavored in titles (not currently specified anywhere in CLAUDE.md). |

**Meta description variants**

| # | Variant | Chars | Note |
|---|---|---|---|
| 1 | **See how obesity care teams can use remote body data for bariatric pre-qualification, intake, pre-auth preparation, and post-op progress tracking.** | 145 | **Recommended — this is D8's verbatim text and the one to ship.** Do not paraphrase it; the decisions file's own instruction is that verbatim rows are literal copy, not description of copy. |
| 2 | Obesity care teams can use remote body data for bariatric pre-qualification, patient intake, pre-authorization preparation, and post-op progress tracking. | 154 | A closer paraphrase kept for record only, not for shipping without a fresh review decision. Same four workflow nouns, fully spelled abbreviations. |
| 3 | Remote body data supports bariatric pre-qualification, patient intake, pre-authorization preparation, and post-op progress tracking for obesity care teams. | 155 | Same note as #2 — reference only. |

Both #2 and #3 exist so a character-budget adjustment has somewhere to go if the CMS field turns out
to truncate below 145; as written, #1 fits every band this pipeline checks (140-160 general, ≤155
task-brief cap) and is the one Review 1 actually authorized.

---

## 2. Final checklist

Re-derived against `draft-v3-editor.md`, not copied from the superseded package. Section numbers
below are the H2 numbers as they appear in the current draft (1 through 10; front matter is
unnumbered, matching the reviewer's own section 1).

### SEO / mechanical checklist

- [x] **Primary keyword in H1, first paragraph, 1-2 H2.** `article_lint.py`: 6 occurrences. In the
      H1 ("Bariatric Pre-Qualification and Patient Progress Tracking..."), in the first paragraph
      ("Bariatric pre-qualification runs on that record, and so does patient progress tracking..."),
      and in H2 §3's own title ("Bariatric pre-qualification and pre-authorization documentation").
      This H2 is sentence case, not the reviewer's Title Case, and its wording adds "bariatric" that
      the reviewer's proposed title omitted — both are mechanical conformances the editor made to
      clear lint gates 1 and 7 without touching content (`editor-report-review-1.md`, section map
      notes 1-2).
- [x] **Meta title ≤ 60 chars, primary keyword in first half.** 54 chars, keyword at position 1.
      Unchanged by Review 1.
- [x] **Meta description 140-160 chars.** 145 chars, D8 verbatim.
- [x] **All numbers from approved_claims (none invented).** `article_lint.py` claim traceability: ok.
      `claims_used`: FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009 — all seven present in
      `approved_claims`. The `superseded figures` gate, which failed on six `predicted weight` hits
      on the first pass through a rule inherited from the wellness hub, now passes: Vadim scoped
      that `SUPERSEDED` row to wellness copy only on 2026-09-07 (per this task's own instruction,
      not re-litigated here). Third-party figures (CMS-0057-F, the JAMA Surgery claims-cohort
      indicator, the Chhabra GLP-1 study, CDC prevalence and self-report figures, the ASMBS reach
      figure, the ACS Bulletin quotes, the JHU post-op figure) each carry an `ext-claim` marker
      resolving to a cited source; §3a below lists all nine ids.
- [x] **No banned words.** Detector CLEAN, this session's run (below). Zero em/en dashes
      (`grep -cP '[\x{2013}\x{2014}]'` returns 0). `objective`, `by hand`, `let`, `this article`,
      `this guide`, `we`/`our`, `you`/`your` — zero hits in the body, checked directly. `positioned
      as` appears exactly once, in the licensed medical-device sentence (§6: *"It is not positioned
      as a medical device."*). `plus` and `so` do not appear as connectors anywhere in the body (the
      one `so` in the body, "and so does patient progress tracking after the procedure," is the
      idiomatic "also," not a result/benefit connector, and it is D1's own added sentence. `rather
      than` appears twice in the body (§6 x2), both inside the product/accuracy-boundary exception
      `terminology-guardrails.md` Part 1 grants, and both are B4 "Text to place" blocks the editor was
      instructed not to rewrite. A third instance used to sit in §5; G1 removed it along with the
      duplicated ±3.5% passage it belonged to (§3h below).
- [x] **Word count within ±10% of target.** Target 4,400 (`plan.md` line 12). Prose words (linter's
      count, table cells included) 4,387 = -0.3%. Excluding table cells, 3,962 = -9.95%, inside band
      by a narrow margin. Both figures are inside the linter's accepted band (3,740-5,060), which is
      wider than a literal ±10%. Recomputed this pass against `draft-v3-editor.md` as it stands after
      the coordinator applied **G1** (§3h below): removing the duplicated ±3.5% passage from §5
      dropped both counts by 26 words each from this package's pre-fix figures (4,413 / 3,988). Note:
      the decisions file (F6) expected the count to land "well below" 4,712 after the B1/B3/B5/B6
      deletions; it landed almost exactly on target instead, because the same review mandates roughly
      800 words of new text (B2's distinction, five B4 blocks, the D5 pilot table, the B5 KPI list,
      the B7 bullet, the D1 intro) against roughly 1,100 words removed. Not padding, flagged by the
      editor, and not a defect.
- [x] **Intro hook in the first two sentences.** The Review-1 intro (D1, verbatim): *"Bariatric
      programs often collect or verify body measurements during the first consultation. When those
      inputs are missing, inconsistent or captured too late, pre-qualification and pre-authorization
      preparation can require additional follow-up."* This replaces the prior package's reframe-move
      hook ("Most diligence on remote body data starts at accuracy...") by direct instruction from
      the reviewer; it states the operational gap rather than reframing a diligence question, and
      that trade was ruled on, not left to this pass to second-guess.
- [x] **CTA placement per plan; type matches intent.** One CTA, in §10 ("Next steps and related
      reading"): direct demo request to `/for-bmi-verification/` plus a sales email, no self-serve
      trial signal. Matches `plan.md` line 751 ("one, in Section 12 [now §10]. No mid-body second
      CTA") and the BOFU-weighted hub intent. No second CTA anywhere in the body.
- [x] **No generic AI patterns.** Zero em/en dashes (verified directly). No triple parallelism found
      on read-through (the comma-separated lists that do appear, industry types and documentation
      items, are literal enumerations, not rhetorical adjective stacks). Rhythm variation 0.57 per
      the detector (fresh run this fix pass, below).
- [x] **Terminology guardrails.** Checked directly against the body (front-matter `changes_summary`
      and `self_check` prose excluded, since those are pipeline scaffolding, not shipped copy): zero
      em dashes; `objective` not used about our own conclusions; `the reader`/`the audience`/`the
      following sections`/`see below` not used (the few plain-English uses of the word "below," as
      in "a current BMI below a payer's threshold," are comparative, not self-referential); `this
      article`/`this guide`/`our content` not used; `by hand` not used; `let` not used; `plus`/`so`
      not used as connectors; `positioned as` used exactly once, in the licensed sentence;
      presumed-reaction phrasing not found; no behavior attributed to a concept rather than a person
      or the program. Corrective negation ("X, not Y") does not appear in the body. Corrective
      "rather than" appears twice, both inside the licensed product/regulatory-boundary exception in
      §6 (B4's BMI-mismatch and weight-estimate sentences, which the decisions file explicitly
      instructs the editor not to rewrite). A third instance, in §5, was removed under G1 along with
      the duplicated ±3.5% passage it belonged to.
- [x] **Abbreviations (M1 + exception).** `article_lint.py` abbreviations gate: ok. CDC, ASMBS, CHIP,
      CMS(-0057-F), GLP-1, DXA, BIA (bioelectrical impedance analysis), HIPAA, GDPR, BAA, TLS, BMR,
      ERISA all expanded at first use. **DXA, not DEXA** (`grep -in "dexa"` returns no match).
      BMI, US, EU stay bare per the 2026-08-25 override.
- [x] **Medical framing.** *"It is not positioned as a medical device."* present verbatim in §6, and
      it is the only "positioned as" instance in the body (checked by grep against the whole file).
- [x] **Links on semantic anchors; third-party sources are neutral quality sites, not vendor blogs.**
      14 internal-link instances across 7 distinct 3dlook.ai targets, plus 9 external citation links
      (CDC x2, ASMBS x2, CMS, PMC, ACS Bulletin, JAMA Surgery doi, Johns Hopkins) — every one on a
      meaning-carrying anchor phrase, no bare URLs. No vendor blog cited anywhere. Full table in §5.
- [x] **AI-tells detector actually run** (not estimated). Command and full output below, this
      session:

  ```
  $ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
      workspace/seo/articles/bariatric-hub-refresh/draft-v3-editor.md --channel article --summary

  SEO / blog article · en · 4953 words
  AI density: 0.81/1000 (budget 6.0) -> low
  VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

  TOP SOFT MARKERS:
    2x 'facilitated' (L135)
    2x 'rather than' (L183)
  ```

  Both soft markers are accounted for above: the two `rather than` instances are the licensed B4
  boundary sentences in §6, and the two `facilitated` hits are inside the proper noun *Federally
  Facilitated Exchange*, not editable text. This is a fresh run against `draft-v3-editor.md` on disk
  this fix-pass session, after the coordinator applied **G1** (§3h below). The lower count against the
  pre-fix run (4,983 words, 1.0/1000, three `rather than` hits) reflects the duplicated ±3.5% passage
  and its `rather than` clause coming out of §5, not a change in the detector: the numbers agree with
  the editor's own pre-fix figure of 1.0/1000 for the same reason they agree with each other, because
  it is the same script against the same input each time, not because one run stood in for another.
- [x] **Images / alt text suggestions.** No images exist in this text-only draft. See §4 below for
      suggested placements and alt text, updated for the new section order (workflow now at §2,
      comparison table now at §7, the new pilot-evaluation table at §8).

**15 of 15 mechanical items pass. No blockers in this checklist.** (Counting each bullet above as one
item; the general publisher checklist template in this role's instructions references a round "10,"
which the previous package also found did not match its own literal item count — reporting the real
total here rather than forcing a mismatch.)

### Content strategy checklist (`content-strategy-guidelines.md` §16)

- [x] **Article tied to the correct hub.** Hub 6 — Bariatrics → Main hub, per frontmatter. Untouched
      by Review 1.
- [x] **`action_type` respected.** `refresh-expand-in-place`, per frontmatter. The Phase 0 override
      for this refresh row was Vadim's direct request on 2026-09-03; Review 1 is an `edit` round on
      top of that same refresh, not a new action-type decision (`review-1-decisions.md` frontmatter:
      *"this is an edit round, not a re-plan"*).
- [x] **Does not duplicate `existing_urls`; cannibalization guardrail honored.** B3 replaced the
      three-row market-indicator table with one indicator, cited to the JAMA Surgery paper directly,
      and links the GLP-1 market hub for the wider economics picture instead of re-explaining it —
      exactly what `content-plan.md` row 67's cannibalization guardrail asks for (*"Do not duplicate
      GLP-1 or telehealth generic pages"*, quoted in B3). The 2023 ASMBS national estimate and its
      procedure-type split are gone entirely, including from the FAQ.
- [x] **Vertical boundary respected; sensitive-vertical scope note present.** The italic disclaimer
      sits before §1, verbatim, unchanged by this review. The "Bariatric surgery basics" FAQ H3 is
      gone entirely (D6) — its remaining two clinical-adjacent questions are removed along with it,
      so no patient-facing clinical-outcome content exists anywhere on the page.
- [x] **Internal links in 4 directions.** `article_lint.py` with the context pack: `{up: 1, sideways:
      3, down: 1, trust: 1}`, 14 links across 7 distinct targets. Down from 6 sideways / 10 distinct
      in the pre-Review-1 draft — D7 removed three sideways links deliberately (occupational health,
      insurance underwriting, wellness rewards). All four directions still covered; see §5 and the
      D7 note below for what was removed and why it should not be restored.
- [x] **FAQ section present, GEO/AEO-friendly, 2-5 sentences per answer.** 9 questions across 3 H3
      blocks (down from 16 across 4 blocks). Checked directly: every remaining answer runs 2-3
      sentences, inside the 2-5 sentence guideline.
- [x] **"What FitXpress does NOT do" section present; no forbidden positioning claims.** §6 carries
      eight unstacked negation statements (one more than the pre-Review-1 draft — B2 added "It does
      not make a record acceptable to a payer; that acceptance sits with the plan"), closing on the
      licensed medical-device sentence. No diagnosis, eligibility, treatment, underwriting, hiring or
      clearance claim anywhere. No automated fraud-detection claim (only "fraud-prevention support
      inside a human review process," §8).
- [x] **No unsubstantiated medical / legal / underwriting / employment / clinical-trial claims.** The
      CMS-0057-F description now states its own scope limit in the same paragraph as the timeframe
      (B1b), rather than carrying the rule's full-list scope into the timeframe claim — the specific
      defect A1 found and B1 corrected. The compliance-posture bullet (FX-009) is the B7-ruled text,
      sourced to `compliance.md`, not a new claim manufactured for this article. Reading the rule
      against a specific plan contract is still stated as work for compliance counsel (§3, kept per
      B1c). **Routing note, not a fail:** any compliance-adjacent claim belongs on a legal/product/
      security review pass before publish; FX-009 is pre-approved corpus language, so this is a
      confirmation step.
- [x] **Article owns one distinct search intent.** BOFU/GEO/sales-enablement hub intent, unchanged
      by Review 1 and distinct from the GLP-1 Market and Telehealth hubs (reinforced, not weakened,
      by D7's link-focus tightening). **Not a failure, but worth repeating:** the primary keyword
      still has zero measured US search volume (carried from the pre-Review-1 package's open item);
      this review did not change that fact and did not need to.

**9 of 9 content-strategy items pass. No ❌ in the positioning / compliance / cannibalization block.
No STOP condition is triggered.**

---

## 3. Publish-time technical notes

### 3a. Recomputed marker counts — do not carry the old numbers forward

The old package's own §3a records two prior miscounts on `draft-v2-editor.md` (23 total, then
corrected to 31 on 16/8/7). This fix pass corrects a third: the pre-fix version of *this* package (the
one `quality-controller` scored 17/20) stated "21 comment markers across 18 comment lines (two lines
carry two markers each)," and that description did not reconcile with its own total (18 lines with two
doubled lines is 20, not 21) — the QC finding this section now corrects. Recomputed fresh this session
with `grep` against the current `draft-v3-editor.md`, not carried from any prior count or from
`editor-report-review-1.md`'s prose description.

**`ext-claim` comments: 13 occurrences across 9 distinct ids.** Unchanged by G1 — the duplication
`review-1-decisions.md` §G1 fixed was an internal `claim:` marker (`FX-008`), not an external citation.

| id | Occurrences | What it backs |
|---|---|---|
| `CMS-0057-F` | 3 | The prior-authorization timeframe statement and scope limit (§3), and the FAQ timeframe answer (§9) |
| `ASMBS-2026-05-05-CHHABRA` | 3 | The GLP-1-before-surgery weight-loss study (6,700 vs ~127,000 patients, the ~8% figure), in §4 and again in the FAQ |
| `CDC-DB508` | 1 | 40.3% / 9.4% obesity prevalence |
| `ASMBS-FACTSHEET-2025` | 1 | "About 1% of those who meet eligibility requirements" |
| `PMC12964095` | 1 | The 2026 narrative review on pre-operative attrition |
| `CDC-PCD-2023` | 1 | Self-reported BMI underestimate, 40% |
| `JAMA-SURG-2026` | 1 | The one surviving B3 indicator: 34.1% / 140.4% shift, 11.7 million adults, cited to the JAMA Surgery doi directly (the EurekAlert link from the pre-Review-1 draft is gone) |
| `ACS-BULLETIN-2025-04` | 1 | Funk and Kurian quotes on GLP-1 as an intake gateway |
| `JHU-2025-JAMA-SURG` | 1 | The one-in-seven post-op GLP-1 initiation figure |

**`<!-- claim: FX-xxx -->` comments: 7 occurrences across 7 distinct ids** (FX-001, FX-002, FX-005,
FX-006, FX-007, FX-008, FX-009 — one marker each). Down from 8 occurrences over the same 7 ids in the
pre-fix package: **G1** moved the ±3.5% passage that used to ship in both §5 and §6 down to a single
instance in §6 only, and its `FX-008` marker moved with it. `draft-v3-editor.md` now carries `FX-008`
once, not twice. Matches `article_lint.py`'s reported `claims_used` list (the gate reports distinct
ids, not occurrence counts, so it would not itself have caught the prior double marker).

**Total: 20 comment markers across 18 comment lines.** One line carries three markers, the CDC/ASMBS/
PMC sentence in §1's second paragraph (`CDC-DB508`, `ASMBS-FACTSHEET-2025` and `PMC12964095` all on
one line). Every other comment line carries exactly one marker; none carries two. This is a real change
from the pre-fix package, not a restatement of it: the line that used to carry two markers (`FX-002`
and `FX-008` together, in §5) now carries only `FX-002`, because `FX-008` moved to §6 under G1. **Zero
`DOWN-LINK LANDING` markers remain** — see §3b.

**Also strip the frontmatter block itself** (everything above the `---` that opens the H1). §6
below is the H1 onward only, with all 20 comment markers removed, verified by `grep -c '<!--'`
returning 0 against it.

### 3b. `DOWN-LINK LANDING` markers — none remain, and none should be re-added at this stage

The pre-Review-1 draft carried seven `DOWN-LINK LANDING` comments, each reserving an anchor phrase
for a future child article, plus an eighth informal promise (the "not yet published" privacy FAQ
sentence in §10 of that draft). **Decision B6 removed all eight**, on the reviewer's finding that
these are visible reader-facing promises, not invisible scaffolding, and that the hub already
contains the material those promised guides would have covered. Where a promise was deleted, the
sentence before it now answers the question directly instead of trailing off to a guide that does
not exist (`editor-report-review-1.md`'s B6 row lists exactly which sentence now closes each spot).

**Recomputed against `draft-v3-editor.md`: zero `DOWN-LINK LANDING` markers remain.** The prior
package's §3b table (mapping seven anchor sentences to seven planned P1/P2 child articles) has
nothing left to rebuild against, because B6 deleted the anchor sentences along with the promises.
Reproducing that table here as "rebuilt" would misstate the draft.

**What this means going forward, for whoever edits this hub next:**

- Open item **E2** in `review-1-decisions.md` records that the reviewer ruled content-plan rows 68
  (Pre-qualification refresh) and 69 (Remote intake) need no separate pages — the hub now owns both
  intents in full. That closes the need for most of the P2-level anchor reservations that existed
  in the prior draft.
- The three surviving P1 targets from the original plan (a bariatric pre-authorization documentation
  guide, a bariatric patient progress record guide, a hybrid bariatric care guide) are not
  contradicted by this ruling — E2 is about rows 68/69 specifically — but the draft no longer
  reserves a sentence for any of them. If one of those three ships later, whoever writes it will need
  to find its own anchor point in the current §3/§5/§6 prose; there is no pre-marked slot waiting for
  it anymore.
- Do not add a new `DOWN-LINK LANDING` comment or a "covered in a separate guide" sentence back into
  the body to compensate. That is exactly the pattern B6 removed, and re-adding it would reopen the
  defect the reviewer flagged (a reader-facing promise with nothing behind it).

### 3c. Compliance-posture bullet stays plain text, no link to the privacy FAQ

§8's "Compliance posture" bullet (the B7 text, verbatim) describes HIPAA, Business Associate
Agreement readiness, GDPR roles, encryption and photo retention as prose with **no link**. This is
unchanged in substance from the pre-Review-1 draft: the central Data, Privacy, Security and
Regulatory FAQ is still not live, and `plan.md`'s own internal-links table already specified this
direction as "plain text, never a link." What changed under B6 is only that the prose sentence
promising a future FAQ ("A dedicated FitXpress privacy and regulatory FAQ, not yet published, holds
the fuller detail") is gone — the same defect class as the seven guide promises, removed the same
way. **Do not add a link to that FAQ at CMS-entry time even if a draft URL exists somewhere.** When
that FAQ publishes, this bullet is the one to revisit first.

### 3d. Open item for the schema, not for this page

Unchanged from the pre-Review-1 package. The context pack has no `external_claims:` block
equivalent to `approved_claims:`, which is why the `ext-claim` comments exist as an ad hoc
workaround rather than resolving through the linter directly. **Recommendation, not a blocker for
this article:** add an `external_claims:` block to the context-pack schema and teach
`context-pack-builder` to emit it.

### 3e. FX-003, FX-004 and FX-010 are correctly absent

`article_lint.py`'s own report still lists them: `approved but uncited: FX-003, FX-004, FX-010`.
Confirming here so a reviewer scanning the pack against the body does not read their absence as an
omission — unchanged from the pre-Review-1 package, and explicitly endorsed by `review-1-decisions.md`
section F, item 4 (*"Do not add an accuracy or repeatability figure that is not already on the
page"*): FX-003 (ISO 8559, 0.40 cm) and FX-004 (95%+ repeatability, non-publishable) stay out for
the two-benchmark and non-publishability reasons already on file; FX-010 (bariatric TAM/SAM) stays
out as internal deck sizing.

### 3f. Inventory is already correct

Unchanged. `brand-assets/content-strategy/published-articles-inventory.md`, row 11 and the Hub #9
narrative block, already carry the corrected record (both `2026-06-05` and `2026-07-27` dates, the
"in flight" flag). No action needed on the inventory file itself beyond the natural update to the
real CMS-publish date once this article actually republishes.

### 3g. Three internal links were removed deliberately — do not restore them as a "missing link"

This is the item the task brief specifically asks to be recorded so a CMS operator does not "fix" it
back in. **Decision D7 removed three sideways links; two of the three were live on the page in the
pre-Review-1 draft and are marked "Already present — keep" in `plan.md`'s own internal-links table
(lines 764-765).**

| Removed link | Was it live before this review round? | Source of the "keep" note the reviewer overrides |
|---|---|---|
| `occupational-health-screening-software` | **No.** `plan.md` line 764 marks it a **GAP** — it went live on the site *before* the July 27 refresh but was omitted from that refresh, and the pre-Review-1 draft added it back in as a planned fix. | The plan wanted it added; D7 says do not. |
| `mobile-body-scanning-insurance-underwriting` | **Yes.** `plan.md` line 765: "Already present, keep." | The plan's own instruction, now overridden. |
| `wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning` | **Yes.** Same line, same instruction, now overridden. | Same. |

The reviewer's stated reason (`review-1.md` line 159): these three "weaken bariatric topical focus,"
and `content-strategy-guidelines.md` §11 names this exact anti-pattern. `review-1-decisions.md` D7
records the same override directly: *"This decision knowingly drops two live internal links in
exchange for topical focus on a hub... record it in the package as a deliberate removal so nobody
restores it at CMS entry as a 'missing link.'"* Consider this that record. **Whoever enters this
page in the CMS should not treat the absence of these three links as an oversight**, and should not
re-add the occupational-health link either, even though the underlying `plan.md` context-pack row
still describes it as a gap — that row is now overridden by this decision for this page.

### 3h. G1 (resolved) — the ±3.5% passage no longer ships twice

This was QC's top issue at 17/20. B4 supplied both a "wherever the figure lands" block and a separate
post-operative block, and the editor placed both, leaving roughly 55 words of the same content in §5
and §6. Neither the pre-fix version of this file nor `publisher-report.md` §4 said so, which was QC's
second, process-level finding: an editor-flagged item that reached neither checkpoint artifact.

**Resolved by the coordinator, 2026-09-07, applying `review-1-decisions.md` §G1.** The figure stays in
**§6** ("Where FitXpress fits"), next to the two-references explanation and the `FX-008` marker. §5 was
rewritten to keep the use and the boundary without repeating the number:

> Predicted weight can add another consistent data point to remote follow-up, and it stays a software
> estimate: a calibrated scale remains the reading wherever the program's clinical protocol requires a
> directly measured weight.

`article_lint.py` re-run against the result: **PASS**, all 9 gates, accuracy-discipline gate included
(§5 still links the accuracy framework for the repeatability figure it does carry, so removing the
duplicated weight-estimate sentence did not touch that gate). Downstream effects, all recomputed this
pass rather than estimated: prose word count fell by 26 words (4,413 to 4,387, table cells included;
3,988 to 3,962 excluding them, §2 above); the `claim: FX-008` marker count fell from two to one and the
total comment-marker count from 21 to 20 (§3a above); the body's `rather than` count fell from three to
two (§2 above); the AI-tells detector's word count and density both dropped slightly on rerun (§2
above). §6 below is re-extracted from this corrected draft.

### 3i. G2 (disclosed, approved) — §6's heading drops "repeatability," and the count of mechanical deviations is three, not two

`review-1-decisions.md` §C's mapping names the section *"Where FitXpress fits: outputs, accuracy,
repeatability and limitations."* The shipped H2 is `## 6. Where FitXpress fits: outputs, accuracy and
limitations` — "repeatability" dropped. **Ruled correct and kept, 2026-09-07 (§G2).** The repeatability
figure lives in §5 now, where longitudinal comparison is the argument; a §6 heading promising
repeatability would promise something the section no longer delivers.

What was wrong was not the heading, it was that nobody disclosed the change. `editor-report-review-1.md`
states "Two deviations from the reviewer's literal wording," and the pre-fix `publisher-report.md` §3
item 4 re-verified only those two: §3's own H2, Title Case changed to sentence case, and "bariatric"
added to satisfy the primary-keyword-in-an-H2 lint gate. **The real count is three:**

1. §3 H2 — Title Case to sentence case (house-rule lint requirement, `detect-ai-tells.py` bans
   Title-Case H2s).
2. §3 H2 — "bariatric" added (lint gate 7, primary keyword required in at least one H2).
3. §6 H2 — "repeatability" dropped (this item; ruled by G2; previously undisclosed anywhere in the
   pipeline's checkpoint artifacts).

`publisher-report.md` §3 is corrected in this same fix pass to state three deviations, not two.

### 3j. G3 (allowed) — "consult-to-procedure conversion" survives once, recorded as a decision, not a leftover

§7's buyer-fit paragraph names the measures the buyer-side roles are accountable for: *"consult-to-
procedure conversion, late-stage disqualifications and cancellations, pre-authorization cycle time, and
staff time per packet."* B5 turned outcome claims into hypotheses and KPIs elsewhere on the page (the
Use Case Summary's Business-value row no longer claims the product moves this metric); this instance
names a measure a director's role already owns and does not assert that the product moves it, which is
the distinction B5 draws between a claim about the product and a fact about who is accountable for what.

**Ruled allowed, 2026-09-07 (§G3).** Kept as written. Carried into the open items list below so the
next reviewer sees a decision, not a leftover — before this ruling, the flag reached only
`editor-report-review-1.md` and the pre-fix `publisher-report.md` §4 item 9, and neither of those is
the file Vadim reads at this checkpoint.

---

## 4. Image / alt-text suggestions

No images exist in the current draft; this is a text-only markdown deliverable. Suggested minimum
for a content-hub article of this length and BOFU weight, updated for the new section order:

| Placement | Suggested content | Suggested alt text |
|---|---|---|
| Hero / OG image | A calm, editorial image evoking a clinical intake or documentation setting (not a stock "doctor with tablet" cliché); should not depict a specific patient or imply a clinical claim | "Bariatric program staff reviewing patient intake documentation" |
| Inline, near §2 (four-stage workflow) | A simple 4-stage flow graphic mirroring Stage 1-4 (remote capture at intake, pre-consult review, clinical consult, documentation handoff) | "Four-stage bariatric pre-qualification workflow, from remote capture to documentation handoff" |
| Inline, near §7 (manual vs. guided capture table) or §8 (pilot-evaluation table) | The existing comparison table or the new pilot-evaluation table rendered as a lightweight visual, if the CMS template supports table-to-graphic conversion; otherwise the markdown table renders fine as-is | Not needed if left as a rendered table |

None of these are gating. The mandated tables (Use Case Summary, pathway table, comparison table,
pilot-evaluation table) already carry the page's structural information in text form, so a missing
hero image is a polish item, not a publish blocker.

---

## 5. Internal links, four directions (rebuilt against `draft-v3-editor.md`, verified against `article_lint.py`)

| Direction | Target | Section(s) | Anchor |
|---|---|---|---|
| up | `https://3dlook.ai/content-hub/ai-body-data-health-hub/` | §1, §10 | "AI body data for health hub" / "AI body data across health programs" |
| sideways | `https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` | §3, §10 | "compliance guide to online pharmacy BMI verification" / "Online pharmacy BMI verification compliance guide" |
| sideways | `https://3dlook.ai/content-hub/glp-1-market/` | §4, §10 | "GLP-1 market hub" / "GLP-1 market growth and patient progress tracking" |
| sideways | `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/` | §5, §10 | "AI in telehealth hub" / "AI in telehealth: workflows, privacy and remote body data" |
| down | `https://3dlook.ai/for-bmi-verification/` | §2, §10 | "BMI verification capability" / "Request a FitXpress demo" |
| trust | `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` | §5, §6 (×2) | "accuracy framework article" / "mobile body scanning accuracy framework" / "accuracy framework" — present in every paragraph carrying an accuracy or repeatability figure, per the accuracy-discipline rule |
| (uncategorized by the direction gate) | `https://3dlook.ai/technology/` | §6 | "3DLOOK technology page" |

**14 total link instances across these 7 distinct targets.** `article_lint.py` with the context pack
reports `{up: 1, sideways: 3, down: 1, trust: 1}` — matches exactly. Down from 18 instances / 10
distinct targets / `{up: 1, sideways: 6, down: 1, trust: 1}` in the pre-Review-1 draft; the drop is
D7 removing three sideways links (occupational health, insurance underwriting, wellness rewards —
§3g above has the deliberate-removal record) and one duplicate EurekAlert citation swapped for the
JAMA Surgery doi (an external, not internal, link). All four directions are still covered, so the
guideline's four-direction requirement still passes even though the total curated-link count (7) now
sits below `plan.md`'s 8-11 target — that target predates D7 and is not a checklist gate.

The **Data, Privacy, Security and Regulatory FAQ** direction (trust) stays plain text, no link, per
§3c above — unchanged from the pre-Review-1 draft and from the live page.

---

### About the body in §6

`§6` below carries `draft-v3-editor.md`'s body — H1 onward, frontmatter excluded, as the file stands
after the coordinator applied **G1** — with **every** HTML comment removed and no prose rewritten.
Re-extracted this fix pass (the pre-fix version of this package still carried the duplicated ±3.5%
passage that G1 removed; §3h has the full record). Verified with `perl -pe 's/\s*<!--.*?-->//g'`
against the H1-to-end range and cross-checked with `grep -c '<!--'` returning 0 on the result, and
with a line-by-line diff against the source showing no change outside the comment text itself (no
stray double spaces where a comment used to sit).

**Verification for whoever pastes into the CMS.** Against **everything after the `§6` heading**,
plain-text search for each of these three and expect no hits: the HTML comment opener `<!--`,
`ext-claim`, and `DOWN-LINK`. (There is no `claim:` marker to search for separately since it never
appears outside an HTML comment.) All three were confirmed clean at the time of writing, this fix
pass, against the re-extracted body. Scope the search to below the `§6` heading, since §3a and §3b
above name these strings on purpose and will match themselves.

`word_count` (prose, per `article_lint.py`, table cells included): **4,387**, against 4,712 in the
pre-Review-1 draft and 4,413 in the pre-fix version of this package (§3h: G1 removed a 26-word
duplicated passage). The frontmatter `meta_description` in `draft-v3-editor.md` already matches
§1's recommended description verbatim — no override needed there, unlike the pre-Review-1 package
where the working draft's meta fields were stale against the recommendation. The frontmatter `title`
field is the full H1 (104 chars), not the meta title tag; use §1's 54-char recommendation for the
`<title>` tag.

---

## 6. Article (CMS-ready body)

---

# Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams

Bariatric programs often collect or verify body measurements during the first consultation. When those inputs are missing, inconsistent or captured too late, pre-qualification and pre-authorization preparation can require additional follow-up. Structured remote intake can provide dated body measurements before the visit, establish a baseline for progress tracking and leave eligibility and treatment decisions with the care team. Bariatric pre-qualification runs on that record, and so does patient progress tracking after the procedure.

The demand side is not in dispute. The [most recent clinical-measurement cycle from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/nchs/products/databriefs/db508.htm), running from August 2021 to August 2023, shows 40.3% of US adults have obesity and 9.4% have severe obesity, at a BMI of 30 or higher and 40 or higher respectively, while the American Society for Metabolic and Bariatric Surgery (ASMBS) puts surgery's reach at [about 1% of those who meet eligibility requirements](https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf). Inside that narrow funnel, pre-operative attrition varies with program design and with how it is counted: a [2026 narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/) reports dropout as high as 60%, one cohort in the same literature reports 22.25%, and programs with mandatory pre-operative pathways complete at roughly 36% to 76%. That spread is a stronger case for a standardized intake record than any single figure inside it.

**Use Case Summary**

| Field | Detail |
| :-- | :-- |
| **Industry** | Bariatric surgery centers, hospital bariatric programs, multi-site surgical networks, metabolic and obesity clinics |
| **Problem** | Eligibility confirmed late, consult slots spent collecting measurements, pre-auth packets built from notes a payer reviewer cannot date |
| **Solution** | A guided two-photo remote scan completed before the consult, returning a structured body-data record to the program |
| **Outputs** | Predicted weight through Smart Scales (beta), BMI values for comparison, 80+ body measurements, body-composition estimates, capture timestamp and capture-quality outcomes |
| **Role** | Provides structured body-data inputs and discrepancy signals for program review; it does not determine eligibility or payer acceptance |
| **Business value** | What a pilot sets out to measure: intake completion, time from inquiry to a completed body-data record, pre-authorization rework, measurement-only appointments, follow-up completion |

The people who own that problem are bariatric program directors, directors of operations, pre-authorization coordinators and medical directors. What they answer for does not move on measurement accuracy alone. It moves on whether the right dated record exists before the review starts.

**Disclaimer.** *Mobile body scanning solutions described here do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions. They produce body measurement and composition data intended as supporting evidence within decisioning workflows operated by licensed bariatric programs and their compliance and payer counterparts.*

## 1. What structured remote body data contributes, and what it does not decide

**Short answer.** Bariatric pre-qualification is the intake step in which a program assesses whether an inquiry meets its own eligibility criteria and a payer's medical-necessity criteria, before a full clinical consult is scheduled. A bariatric patient progress record is the dated, comparable body-data series a program keeps from before the procedure through long-term follow-up. Structured remote body data supplies the measurement inputs for both. The eligibility determination and the pre-authorization decision are made elsewhere, by the licensed program and by the payer.

*Structured* carries an operational meaning here. The same guided capture sequence runs every time, the output is machine-readable, each capture carries a timestamp, and the records stay comparable across patients and across time points.

A structured scan record can give the program a dated and standardized body-data input before the consultation. Whether a payer accepts that record for a specific documentation requirement depends on the plan and should be confirmed during implementation.

At the top of the funnel, that input usually sits next to a self-reported number. CDC researchers reported in Preventing Chronic Disease that [self-reported BMI underestimated the prevalence of severe obesity by 40%](https://www.cdc.gov/pcd/issues/2023/23_0005.htm), at 5.3% on self-report against 8.8% after bias correction in 2020 data. That is a population-level comparison between two ways of measuring prevalence, and it characterizes neither an individual patient nor an individual file. How much weight to give a self-reported figure at intake stays a program policy.

For obesity care teams the division of labour is the point: the measurement is standardized upstream, and the judgment stays downstream with the people licensed to make it. Bariatrics is one workflow among several that run on the same capture, and the [AI body data for health hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) maps the others.

## 2. Remote body measurement for bariatric patient intake: a four-stage pre-qualification workflow

The redesign is one move, and the rest of the workflow turns on it: body measurement goes from stage three, inside the consult, back to stage one, before it.

- **Stage 1. Remote capture at intake.** After the patient submits the intake questionnaire, the program sends a scan link. The patient completes the guided two-photo capture on their smartphone. FitXpress returns structured body data, including predicted weight through Smart Scales (beta), BMI, body measurements and body-composition estimates. Where self-reported weight is also collected, the program can compare the resulting BMI values and route material differences for human review.
- **Stage 2. Pre-consult review.** A coordinator confirms the record is complete and routes it for authorized clinical review against the program's intake criteria before a consult is scheduled. Pose validation runs during the capture and the clothing detector prompts the patient to adjust, which means an unusable capture surfaces in session. Where quality is still insufficient, the patient retakes the scan or is booked for in-clinic measurement. The [BMI verification capability](https://3dlook.ai/for-bmi-verification/) behind the capture is what that review reads.
- **Stage 3. Clinical consult.** The visit opens with the body data already in the patient's record, which moves the conversation to history, comorbidities, surgical risk and patient education. The same capture supports a hybrid schedule, where virtual check-ins alternate with in-person visits.
- **Stage 4. Documentation handoff.** The record that supported the pre-consult review is available to the pre-authorization coordinator from the start of the case. Whether that changes how long a packet takes to assemble is one of the things a pilot measures.

The scan does not determine whether a patient is medically eligible for surgery; the bariatric program makes that determination after evaluation. What the capture supplies is a structured, dated body-data input the program uses when it decides which consult slots to open and in what order. Each of the four stages names the person who reviews.

## 3. Bariatric pre-qualification and pre-authorization documentation

Stage 4 hands the record to a pre-authorization coordinator, and the clock it lands on belongs to the plan. For Medicare Advantage, Medicaid and Children's Health Insurance Program (CHIP) plans, the Centers for Medicare and Medicaid Services (CMS) now sets it.

Beginning 1 January 2026, [CMS-0057-F](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f) requires Medicare Advantage organizations and specified Medicaid and CHIP payers to issue standard non-drug prior-authorization decisions within 7 calendar days and expedited decisions within 72 hours, subject to applicable extension provisions. The rule did not change the decision timeframes for Qualified Health Plans on Federally Facilitated Exchanges. It also requires specific denial reasons and public reporting of aggregated prior-authorization metrics.

It does not cover every commercial plan governed by the Employee Retirement Income Security Act. Medicare fee-for-service does not use prior authorization for bariatric procedures at all. How much of a program's volume sits on this clock depends on its payer mix, and reading the rule against a specific plan contract is work for compliance counsel.

Window length changes what the documentation has to do. A long review window absorbs a request for more information, and 7 calendar days leaves little room for one.

The packet itself has not changed. A standard bariatric pre-authorization submission typically carries documented BMI history, confirmation of comorbidities, prior weight-loss attempts, participation in a supervised diet program where the plan requires it, psychological evaluation outcomes, and a body-measurement record. The body-data half of that packet is short: a dated BMI, the height and weight behind it, waist and hip circumference where the plan asks for them, and a record of when and how each was captured. What changed is how much of that has to be complete on the first pass.

None of this shortens the payer's own clock. A program controls one variable, whether its first submission is complete, and standardized capture is what makes that variable repeatable across coordinators. The mechanics of verifying a BMI figure remotely, including live capture and pose validation, are set out in the [compliance guide to online pharmacy BMI verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

What the file has to hold is steady. Who arrives at intake is not: many patients now reach the consult after a year on a glucagon-like peptide-1 (GLP-1) medication that did not take them to their goal.

## 4. The GLP-1 bridge: current BMI, historical BMI and documentation continuity

The shift is visible in claims. Metabolic bariatric surgery use fell 34.1% while GLP-1 receptor agonist use rose 140.4% between 2022 and 2024, measured inside one insured claims cohort of 11.7 million adults ([JAMA Surgery, 13 May 2026](https://doi.org/10.1001/jamasurg.2026.1343)). Coverage economics, prescribing growth and drug-class comparison sit on the [GLP-1 market hub](https://3dlook.ai/content-hub/glp-1-market/); what matters at an intake desk is who now walks up to it.

In the [American College of Surgeons Bulletin in April 2025](https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/), Luke Funk, a bariatric surgeon at the University of Wisconsin-Madison, described GLP-1 medications as "the initial gateway for a lot of patients" who later move toward surgery. Marina Kurian, clinical professor of surgery at NYU Langone Health, said in the same piece that "Most of my colleagues around the country are seeing an increase in new consults coming for surgery." A wider and more heterogeneous funnel is feeding surgical capacity that has not grown.

The sharpest operational change shows up in patient files. An [ASMBS release on 5 May 2026](https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/) reported a study by Chhabra and colleagues at NYU Grossman School of Medicine, presented at ASMBS 2026, drawing on Epic Cosmos electronic health records from 2019 to 2025. It compared 6,700 patients with prior GLP-1 use, 2,395 of them gastric bypass and 4,315 sleeve gastrectomy, against roughly 127,000 patients without prior GLP-1 use, followed for three years. Patients lost about 8% of total body weight on GLP-1 medications before surgery. Total loss reached more than 25% after gastric bypass and about 20% after sleeve gastrectomy.

For an intake coordinator the consequence lands on the file. A patient who has already lost about 8% of body weight on a GLP-1 may arrive at consult with a current BMI below a payer's threshold while their documented history still meets it. Eligibility then turns on dated BMI history, and one measurement taken in the room no longer carries the case by itself. What a payer's threshold is, and whether a given history meets it, stay questions for the program and the plan.

Bariatric surgery requirements, at this stage of the workflow, are documentation requirements: which measurements exist, when each was taken, and what sits behind each one. That is a records problem before it is a clinical one. A serial scan record carries its own date and its own capture conditions. A tape measurement typed into a free-text note carries neither, which leaves a reviewer with the note and nothing behind it. Whether a scan record then satisfies a given plan's documentation requirement is a separate question, and it is settled with the plan.

The pathway runs in both directions, since for some patients a medication becomes the bridge to surgery later on. An intake record that begins when a patient first enters obesity care is therefore more useful than one that begins at the surgical consult.

## 5. Patient progress tracking before and after surgery

The scan captured before surgery is the reference the follow-up scans are compared against. Because every capture runs the same guided sequence, a scan taken three months after the procedure is structurally comparable to the baseline instead of standing as a separate ad-hoc measurement.

For longitudinal use, repeatability is the property that carries the comparison. Accuracy describes how close one measurement sits to a reference; repeatability describes whether two scans of the same body produce numbers a program can compare. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. How that was measured, and why it answers a different question from accuracy, is set out in the [accuracy framework article](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). Predicted weight can add another consistent data point to remote follow-up, and it stays a software estimate: a calibrated scale remains the reading wherever the program's clinical protocol requires a directly measured weight.

Body composition after bariatric surgery moves on a different timeline from scale weight. The same weight can sit on top of different body-composition profiles, and that difference matters for patient counselling and for program-level outcome reporting. It matters to the multidisciplinary team around the patient too, in nutrition, behavioural health and surgical follow-up. Body-composition estimates complement weight and circumference trends where the program considers them appropriate. They are not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods.

The post-procedure window increasingly holds a pharmacotherapy component alongside surgical recovery. [Johns Hopkins researchers reporting on a JAMA Surgery analysis](https://publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs) found that roughly one in seven bariatric patients initiate GLP-1 therapy after surgery. A baseline scan along with serial follow-up scans gives the program a body-data series that stays visible across the whole window, independent of medication adherence. Remote follow-up workflows are covered on the [AI in telehealth hub](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/).

A side-by-side comparison of the baseline capture and a recent scan is also a counselling artifact, often more useful than a single weight number on a chart, and it stays supporting evidence inside the program's monitoring workflow.

What belongs in a bariatric patient progress record is a short list: a dated BMI, waist and hip circumference, body-composition estimates, and a capture-quality outcome for each scan. Each entry carries its date and its capture conditions, and the cadence follows the program's monitoring protocol.

## 6. Where FitXpress fits: outputs, accuracy and limitations

FitXpress by 3DLOOK is a mobile body-scanning solution built around a guided two-photo flow, with no specialized hardware involved. The output can include a 3D model, 80+ body measurements, predicted weight through Smart Scales (beta), BMI, basal metabolic rate (BMR), body-fat percentage, lean mass and fat mass. Results come back in under 45 seconds from a guided two-photo capture completed on the patient's own smartphone.

Three properties matter for this use case. Outputs are structured and timestamped at capture, which allows a record to be placed in time and compared later. Capture happens remotely on the patient's own phone, which takes the appointment slot out of the measurement step. The third is the compliance posture, and its diligence questions belong with the pilot evaluation.

One measurement-accuracy figure applies here, and it comes from one specific comparison. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. The useful diligence question is accurate enough for which decision: against which reference method, under which capture protocol, for which population, and at what tolerance the workflow can absorb. Consult-slot triage and a payer packet do not set the same tolerance. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) states the conditions that make any such figure meaningful.

FitXpress can support an additional BMI cross-check through Smart Scales. Where the program also collects a self-reported weight, the capture compares it against the estimate and flags a mismatch. BMI from the patient's self-reported height and weight can then be read against BMI from the same height and the predicted weight. A material difference between the two values becomes a review signal rather than an automated eligibility conclusion.

Predicted weight stays a software estimate. Against scale weight it carries a ±3.5% average error margin under real-world conditions, an average across the evaluated captures rather than a bound on any single reading. A calibrated scale remains the reading wherever a clinical protocol or a payer requires a directly measured weight. Scale weight is the reference for that figure; expert manual measurement is the reference for the accuracy figures, and the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out why two figures taken against two references never collapse into one.

| Pathway stage | What the capture contributes |
| :-- | :-- |
| Inquiry | Early body data captured outside the clinic |
| Pre-consult | Supports pre-qualification review and consult-slot triage |
| Pre-authorization | Provides structured, timestamped documentation inputs |
| Procedure preparation | Establishes a baseline body-data record |
| Post-surgery follow-up | Tracks body measurement and composition change over time |
| Long-term monitoring | Supports remote progress review without a clinic visit |

The same data structure can be generated at multiple pathway stages alongside measurements required by the program or payer. The technology behind the capture is described on the [3DLOOK technology page](https://3dlook.ai/technology/).

**What FitXpress does not do in a bariatric program.** It does not determine medical or surgical eligibility. It does not diagnose. It does not replace clinical evaluation. It does not make the pre-authorization decision. It does not guarantee compliance or an approval. It does not make a record acceptable to a payer; that acceptance sits with the plan. It is not equivalent to DXA, bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods. It is not positioned as a medical device.

## 7. Manual measurement versus guided capture

Manual measurement and guided capture sit under different constraints. The comparison that matters runs workflow area by workflow area.

| Workflow area | Manual measurement at the consult | Guided scan-based capture |
| :-- | :-- | :-- |
| Appointment slot | Required; the measurement and the slot are one event | Not required; capture runs before, during or after a clinical event |
| Cross-operator comparability | Varies with operator, tool, technique and participant preparation | Same capture and processing sequence each time, comparable across patients and time points |
| Documentation generated | A note stating a measurement was taken | A record carrying a capture timestamp and capture-quality outcomes |
| Reuse across pre-qualification, pre-auth and post-op | Each stage collects its own measurement | The same data structure generated at several stages |
| What it depends on | Trained staff, protocol adherence, in-person attendance | Patient smartphone access, capture instructions, retake logic, deployment thresholds |
| Payer acceptance | Follows the plan's own documentation requirements and is confirmed during implementation | Follows the plan's own documentation requirements and is confirmed during implementation |

At the consult, manual measurement stays where the protocol requires it, and where a clinician needs a hand on the anatomical landmark. Neither method replaces the other, and a program running both decides which one a given step calls for.

The fit is clearest at bariatric surgery centers, hospital programs, multi-site surgical networks and metabolic and obesity clinics. Directors of operations, medical directors, vice presidents of patient access and chief operating officers own the measures at stake: consult-to-procedure conversion, late-stage disqualifications and cancellations, pre-authorization cycle time, and staff time per packet. At a multi-site network, cross-site consistency is the whole argument.

## 8. What to confirm in a bariatric pilot

None of this is a settled outcome for any particular program. A pilot is where the claims get tested against one program's patients and one program's payer mix, and it has to keep two things apart: what the capture produces, and what the program's review does with it.

In the pre-authorization packet the first of those is narrow and concrete. The file gains a structured body-data record: a capture timestamp, the capture-quality outcomes recorded in session, and the measurement set in machine-readable form, consistent across patients because the sequence does not vary between them. Serial captures on one timeline, a baseline at intake, a second before submission, a third before the procedure, produce comparable records instead of three measurements taken three different ways. Audit-readiness is the program's own determination, and a human reviewer still reads every record.

The anti-manipulation controls support that posture without completing it. Capture runs live in session instead of accepting a camera-roll upload, pose validation runs in real time, and clothing detection is built in. Those controls reduce the risk of a manipulated capture. They leave in place the need for capture instructions, retake logic and deployment-specific thresholds. They are fraud-prevention support inside a human review process.

The measures worth instrumenting before a pilot starts are intake completion, retake rate, time from inquiry to completed body-data record, pre-auth rework, measurement-only appointments, and follow-up completion. Each is a hypothesis on the way in and a number on the way out.

Alongside the numbers sit seven things a program confirms for itself.

| What to confirm | The question the pilot answers |
| :-- | :-- |
| Capture completion | What share of invited patients finish a usable capture without staff help |
| Quality failures and retakes | How often a capture is rejected, and how many retakes clear it |
| Workflow integration | Where the record lands in the intake system or the electronic health record, and who moves it there |
| Role-based review | Which role reads the record, against which criteria, and what happens to a flagged mismatch |
| Population fit | How the program's own patients sit against the validation scope |
| Payer acceptance | Which plans in the payer mix accept the record for which documentation requirement |
| Data governance | Retention, access control, Business Associate Agreement scope, and where photos and outputs sit |

Three vendor-side questions belong in the same diligence.

- **Compliance posture.** FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts and supports Business Associate Agreement execution. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR). Data is encrypted at rest in Amazon Web Services S3 with server-side encryption always on, and in transit over Transport Layer Security. Photos are permanently removed immediately after processing, or within 30 days, depending on the client's configured policy, and are automatically blurred when stored. FitXpress does not receive names, contact details, or other direct identifiers that connect the scan with a specific individual. Body data and session-linked outputs can still qualify as personal data, which is the program's own assessment to make.
- **Validation population.** The internal validation population included participants aged 16 to 78, heights of 150 to 220 cm, weights of 38 to 210 kg, and participants from the US and Europe. Performance outside this scope has not been characterized. A severe-obesity intake population includes patients above that weight range, worth checking early in evaluation.
- **Validation strength.** 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study.

Those three are the floor to confirm with any vendor handling patient body data before a pilot begins.

## 9. Frequently asked questions

### Pre-qualification and pre-authorization documentation

**What is bariatric pre-qualification?**
Bariatric pre-qualification is the intake step in which a program checks an inquiry against its own eligibility criteria and a payer's medical-necessity criteria before a full clinical consult is scheduled. Eligibility determination stays with the licensed program.

**How can bariatric programs pre-qualify patients remotely?**
The program sends a body-scan link at intake and the patient completes the guided capture on their own smartphone. BMI, body measurements and body-composition estimates reach the program before the consult, where clinical evaluation still happens.

**What body-data documentation do payers commonly require in a bariatric pre-authorization packet?**
A standard packet typically carries documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation where the plan requires it, psychological evaluation outcomes and a body-measurement record. A capture timestamp dates the measurement record; whether a given plan accepts that record for a specific requirement is confirmed with the plan.

**How long do payers have to decide a bariatric prior authorization?**
Under CMS-0057-F, since 1 January 2026, Medicare Advantage organizations and specified Medicaid and CHIP payers decide standard non-drug requests within 7 calendar days and expedited requests within 72 hours. Some requests qualify for an extension of up to 14 additional calendar days under program-specific conditions. The rule did not change the decision timeframes for Qualified Health Plans on Federally Facilitated Exchanges, it does not reach every commercial plan under the Employee Retirement Income Security Act, and Medicare fee-for-service uses no prior authorization for bariatric procedures.

**What are common program and payer requirements?**
Each program and plan sets its own list, and the common items are documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation and psychological evaluation outcomes. At intake the question is documentary: what exists, dated when, and what record sits behind it.

**Why does documented BMI history matter more when a patient has been on a GLP-1?**
Patients in one 2026 study lost about 8% of total body weight on GLP-1 medications before surgery. A patient who arrives that much lighter may show a current BMI below a payer's threshold while their documented history still meets it. That reading belongs to the program and the payer.

### Patient progress tracking

**What body data belongs in a bariatric patient progress record?**
A dated BMI, waist and hip circumference, body-composition estimates, and a capture-quality outcome for each scan. The set and the cadence follow the program's monitoring protocol.

### Scope and governance

**Is scan data used to make eligibility or pre-authorization decisions?**
No. The scan produces body measurement and composition data used as supporting evidence inside workflows the licensed program and its payer counterparts operate. Eligibility and pre-authorization decisions are made by people, against those parties' criteria. Whether a payer accepts a scan record for a given documentation requirement is decided by the plan.

**What does FitXpress not do in a bariatric program, and can it replace in-clinic measurement?**
It does not determine medical or surgical eligibility, diagnose, or make the pre-authorization decision, and it does not guarantee compliance or an approval. Where a protocol or a regulatory standard calls for DXA, bioelectrical impedance analysis or a calibrated scale, those remain the methods of record. In-clinic measurement stays where the protocol asks for it.

## 10. Next steps and related reading

See how FitXpress can support pre-qualification, pre-authorization documentation and post-procedure progress tracking inside a bariatric program. A useful first step is mapping one payer's packet requirements against what the file already holds on the day of the consult. [Request a FitXpress demo](https://3dlook.ai/for-bmi-verification/) or contact sales@3dlook.ai.

Related reading:

- [AI body data across health programs](https://3dlook.ai/content-hub/ai-body-data-health-hub/)
- [GLP-1 market growth and patient progress tracking](https://3dlook.ai/content-hub/glp-1-market/)
- [AI in telehealth: workflows, privacy and remote body data](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [Online pharmacy BMI verification compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)

---

## STOP — awaiting Vadim's approval

`status: ready_for_review`, not `approved_for_publish`. Per repo history
(`project_mvb_publish_package_status.md`), that gate could never pass mechanically; Vadim's ask for
this refresh plus his approval of the digest (text and meta together) is the actual publish gate.
This package does not invent an approval state, and no one should treat `ready_for_review` as
sufficient to paste into the CMS. Once Vadim approves the text and meta together, he or the CMS
operator publishes manually, preserving the re-date decision per §0.2 above.

This is a **Review-1 rebuild**. Vadim's approval on the first package (if any was given informally
before the review came back) does not carry forward — this text changed substantively under B1
through B7, C and D. What needs approval now is `draft-v3-editor.md`'s content plus this package's
meta recommendation, together, as a fresh checkpoint.
