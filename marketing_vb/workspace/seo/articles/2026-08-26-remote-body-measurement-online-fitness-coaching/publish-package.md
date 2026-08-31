---
slug: remote-body-measurement-online-fitness-coaching
product: fitxpress
status: ready_for_review
created: 2026-08-31
revision: 1
checkpoint: "2 (re-run) - final text + meta, regenerated after external review round 1"
source_draft: draft-v3-revision1.md
review_source: review1-comments.md
supersedes: "publish-package-v1-20260826.md (written 2026-08-26 against draft-v2-final.md, structure now obsolete)"
---

# Publish Package: remote-body-measurement-online-fitness-coaching (revision 1)

> **This is a re-run of checkpoint 2.** The first package (2026-08-26) was built on `draft-v2-final.md`.
> An external editorial review (`review1-comments.md`, 8 priority items) then reordered the article,
> deleted the retention economics, added two new sections and rewrote several claim sentences, so the old
> meta description no longer describes the text it was written for. The old package is preserved verbatim
> at `publish-package-v1-20260826.md` and is superseded by this file.
>
> **Single source for the body: `draft-v3-revision1.md`.** `draft-v2-final.md` is history.
>
> **STOP after this file. Do not publish until Vadim approves the text and the meta together, and until
> the six decision items in section 4A are answered.**

---

## 1. Meta

**Recommended title (57 chars):**
Online Fitness Coaching Programs: Remote Body Measurement

**Recommended description (146 chars):**
Online fitness coaching programs can capture client body data from a guided phone scan. See how it fits check-ins and what a pilot should measure.

**Slug:** `remote-body-measurement-online-fitness-coaching` (unchanged, matches the draft frontmatter and the working folder)

**Category:** AI in Fitness (Hub 1, `ai-in-fitness-industry`), sub-category / tag: Digital Coaching.
Recommended URL, matching the pattern used by the adjacent articles in this hub:
`https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/`. Not confirmed against a
live CMS taxonomy list, so flag it if the hub uses a different taxonomy field.

**Why this description and not the 2026-08-26 one.** The old recommended description was
*"Coaches can't tape-measure remote clients. See how a guided smartphone scan gives online fitness
coaching programs structured progress data clients trust."* Two problems after revision 1: it put the head
term in the middle rather than the front, and "progress data clients trust" is an audience-reaction promise
of exactly the kind review item 4 stripped out of the body (all six retention and engagement sentences were
deleted). The old alternate variant 3 was worse, it named "visible retention gains" outright. The new
description leads with the head term at character 1, states the mechanism, points at the two blocks the
review added (check-in fit, pilot measurement), and promises no engagement or retention outcome.

**Head term vs H1.** The primary SEO head term is `online fitness coaching programs` (100/mo, US,
difficulty unmeasured, see 4B item 2). The H1 and the `content-plan.md` strategy row use the buyer-facing
phrasing *"Remote Body Measurement for Online Fitness Coaching Programs"*, which puts the head term in the
last four words. The recommended title reorders to front-load it; title tags do not have to match H1
verbatim. Variant 3 in section 5 keeps the exact H1 wording if Vadim prefers title/H1 consistency.

**Brand suffix:** not applied. `| 3DLOOK` is only allowed when the title is 49 chars or fewer without it;
the recommended title is 57.

---

## 2. AI-tells detector, actually run on the new draft

Run by me in this session, against `draft-v3-revision1.md`, not cited from the editor's changelog:

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/draft-v3-revision1.md \
    --channel article --summary
SEO / blog article · en · 3015 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

JSON form of the same run (same file, no `--summary`), the fields the checklist asks for verbatim:

```
"total_words": 3015
"ai_density_per_1000_words": 0.0
"density_budget": 6.0
"severity": "low"
"hard_fails": []
"house_rule_violations": []
"markers_by_category": {}
"top_offenders": []
"style_metrics": {"em_dashes": 0, "bold_count": 15, "title_case_headings": 0, "emoji_count": 0,
                  "bullet_lines": 16, "list_to_prose_ratio": 0.37, "wall_of_text": false,
                  "punch_triads": [], "punch_triad_count": 0,
                  "rhythm": {"sentences": 107, "mean_words": 20.9, "variation": 0.48, "monotone": false,
                             "uniform_paragraphs": false}}
```

Exit code 0 on both runs. No permission prompt, no workaround: the `settings.json` fix from 2026-08-26 is
holding, so this line is a measurement and not an estimate.

### Supplementary mechanical checks (my own greps on the body, lines 26 to end of `draft-v3-revision1.md`)

| Check | Result |
|---|---|
| Em dash / en dash | 0 |
| `±` character | 0 |
| `DEXA` | 0 (DXA throughout, expanded once) |
| `positioned as` (whole file, frontmatter included) | 0 |
| Banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/unleash/game-changing/revolutionary/cutting-edge/disrupt) | 0 |
| `the reader` / `the audience` / `the following sections` / `see below` / `below` | 0 |
| `this article` / `this guide` / `our content` | 0 |
| `by hand` | 0 |
| `objective` | 0 |
| `let` (as the banned verb) | 0 |
| `plus` as a connector | 0 |
| `so` (any occurrence at all, including the benefit shape) | 0 |
| `, not ` corrective negation | 0 |
| `rather than` | 0 |
| `we` / `our` / `us` / `you` / `your` | 0 |
| Presumed audience reaction phrases | 0 |
| FX-004 markers (`ISO 8559`, `0.40 cm`, `1,152`, `14 companies`, `multi-company`) | 0 |
| Named competitors (Prism, Bodygram, Size Stream, Mirrorsize, Styku, Naked Labs) | 0 |

The one residual `so` that the 2026-08-26 package flagged as a judgment call is gone: the string does not
occur in the body at all now.

### Two judgment calls surfaced rather than silently passed

1. **Intro paragraph 2 carries a three-clause sentence:** "Capture has to fit the check-in cadence a
   program already runs, the outputs have to land in the tool the coach works in daily, and the limits of
   the data have to be understood before a progress screen gets built on top of them." The detector
   reports `punch_triad_count: 0` because it only flags adjectival punch triads, by design. This is three
   substantive clauses of different length and content, not a `fast, reliable, scalable` rhythm, so I read
   it as inside the rule. Recorded because a human reviewer may still hear a triad.
2. **BIA and DXA appear first inside a heading** ("Comparison with scales, tape measurements, photos, BIA,
   and DXA") and are expanded in the first sentence underneath it. The reviewer's section title is kept
   verbatim per review item 2, and abbreviation rule M1 governs first use in running text. A mechanical M1
   check will see the heading first, which is why the editor flagged it and why it is repeated here.

### Privacy claims: independently re-verified by me against the live policy

The editor's privacy rewrite cites the FitXpress Privacy Policy "verified 2026-08-31". I fetched
`https://3dlook.ai/fitxpress-privacy-policy/` myself in this session rather than take that on trust:

| Article sentence | Live policy text | Verdict |
|---|---|---|
| "photos are either deleted immediately after processing or retained for up to 30 days, depending on the business client's configuration" | "Based on the requirements and instructions of our Business Client ... we permanently delete end-users' photos either: (i) immediately after the processing ... or (ii) in 30 days of the generation of the Deliverables." | supported |
| "Retained photos are automatically blurred." | "When temporary storage is selected, all retained photos are automatically blurred to ensure additional privacy protection." | supported |
| "Data is encrypted in transit and at rest" | "All the data (including Personal Data) is automatically encrypted both during transmission and at-rest ... Encryption is enforced by default; storage encryption is always on and cannot be disabled." | supported |
| "on Amazon Web Services (AWS) infrastructure" | Two separate statements: "The Service is hosted on a leading cloud infrastructure provider" (provider unnamed in that sentence) and a sub-processor table row "AWS, Amazon Web Services, Inc., Cloud data hosting, CDN, Object Storage, Instance hosting" | supported by composition of two statements, not by one sentence. Low risk, recorded for precision |
| `SSE-S3` | absent from the policy | confirms the editor's reason for dropping it from the body (decision item 4A.2) |
| "complies with the Health Insurance Portability and Accountability Act (HIPAA)" | HIPAA is **not mentioned anywhere in the public policy**; GDPR and CCPA are | rests on FX-007 (internal security commitment) alone, not on a public artifact. Not a new claim, but see 4B item 7 |

---

## 3. Checklists

### 3.1 SEO checklist (15 points)

1. ✅ **Primary keyword in H1, first paragraph, 1-2 H2.** `online fitness coaching programs` appears 4
   times: H1 (title case), intro paragraph 1 sentence 2 ("Remote body measurement is how online fitness
   coaching programs close that gap"), the H2 "The measurement problem in online fitness coaching
   programs", and FAQ question 1. One H2 carries it, which satisfies the 1-2 band without stuffing.
2. ✅ **Meta title 57 chars (limit 60), head term starts at character 1** (first half satisfied trivially).
3. ✅ **Meta description 146 chars** (band 140-160, task ceiling 155). Head term once, at character 1. Does
   not restate the title.
4. ✅ **All numbers trace to approved claims.** Extracted every numeral in the body: `80+`, `under 45
   seconds`, `96 to 97%`, `1.5 to 2.0 cm`, `less than 1 cm`, `approximately 3.5%`, `30 days`, `9+ years`,
   `150K+`, `30K+`, `430K+`. Mapped to FX-005, FX-001, FX-002, FX-003, FX-006, FX-007, FX-008. FX-004
   absent, so it is never combined with FX-001/FX-003. Remaining figures are neutral scenario references
   (two hundred clients, week one, week eight, six-week block, twelve-week challenge, half an inch, about a
   minute). The illustrative "1.4 cm" from the previous version is gone. Two claim **wordings** differ from
   `context-pack.md` and need sign-off, see 4A.2 and 4A.6, which is a record-keeping gap and not an
   unapproved number.
5. ✅ **No banned words.** Zero matches across the full CLAUDE.md section 6 list plus `utilize` (table in
   section 2).
6. ❌ **Word count outside the plan's target band.** Body is 2,584 prose words (my count; draft frontmatter
   says 2,582; 2,916 including table rows; 3,015 as the detector tokenizes). `plan.md` "Article meta"
   states "Estimated words: ~2,000 (range 1,900-2,300)", so plus-or-minus 10 percent of that target is
   1,800-2,200 and the article is 17 to 29 percent above it depending on which figure is read as the
   target. It **is** inside the `context-pack.md` band ("1,800-2,800 words typical for a P1 supporting
   article in this hub") and inside the revision round's own 2,300-2,600 target. Marked ❌ against the
   literal checklist rule rather than re-defining the target to make it pass, exactly as the 2026-08-26
   package did at 2,525 words. What changed since then: the reviewer deleted one section and **required two
   new ones** (the coaching-stage table, the pilot-metrics section), so the plan's estimate no longer
   describes the article anyone asked for. Recommendation: Vadim closes this by accepting the length, or
   asks for a trim, which would now mean cutting reviewer-mandated content.
7. ✅ **Intro hook inside the first 2 sentences.** Sentence 1: "A coach carrying two hundred remote clients
   cannot put a tape measure around anyone's waist, and the measurement still has to happen." Sentence 2
   names the mechanism and the head term.
8. ✅ **CTA placement and type match the intent.** MOFU evaluation link at the end of section 7 "Where
   FitXpress fits" ("Programs at the comparison stage can review how FitXpress supports remote progress
   tracking for coaching programs before scoping a build"), BOFU line in the conclusion ("Explore FitXpress
   for connected and digital fitness ... or book a demo"). `plan.md` specified "after H2.6"; the reviewer's
   reorder moved the FitXpress section from position 5 to 7, so the mid-article slot moved with it. Type is
   evaluation then direct demo, which matches MOFU/BOFU. Demo-only, no self-serve trial, as planned.
9. ✅ **No generic AI patterns.** Detector: 0 markers, 0 punch triads, 0 em dashes, 0 title-case headings,
   sentence-length variation 0.48 against a 0.35 monotone threshold, `uniform_paragraphs: false`. One
   judgment call recorded in section 2.
10. ✅ **Terminology guardrails** (`terminology-guardrails.md`). Every hard ban greps to 0, see the table in
    section 2: no em dash, no `objective`, no reader/audience/below references, no `this article`, no `by
    hand`, no `let`, no `plus` connector, no `so` connector (zero occurrences of the word), no `positioned
    as`, no presumed reactions, no behaviour attributed to concepts, no corrective negation, no corrective
    `rather than`. Links sit on descriptive anchors. `we/our/you` do not appear.
11. ✅ **Abbreviations (M1 plus the 2026-08-25 exception).** Expanded at first use in running text: BMR,
    BIA, DXA, API, SDK, HIPAA, GDPR, AWS, CTO, GLP-1. Left bare, correctly: BMI, CEO. `DEXA` zero. The
    heading-before-expansion nuance for BIA/DXA is recorded in section 2 rather than hidden.
12. ✅ **Medical framing stated directly.** "FitXpress is not a medical device" twice, in the scope note and
    in the boundary section, plus the intended-use sentence "It does not diagnose conditions, make clinical
    decisions, or determine treatment eligibility". Zero `positioned as`. This is where the article
    knowingly departs from review item 3, see decision item 4A.1.
13. ✅ **Links on meaningful anchors; third-party sources.** 5 links, all internal `3dlook.ai`, all on
    descriptive anchors ("AI in the fitness industry", "2-Photo vs Video vs Hardware body scanning",
    "FitXpress supports remote progress tracking for coaching programs", "mobile body scanning accuracy
    framework", "FitXpress for connected and digital fitness"). No bare URLs, no "click here". **Zero
    third-party sources**, so the guardrail on vendor-blog citations cannot be breached, and nothing
    neutral and high-quality is cited either. Flagged as 4B item 5, not silently absent, because
    `quality-controller` caps category B at 3 on this basis (CLAUDE.md, 2026-08-26).
14. ✅ **AI-tells detector genuinely run**, both forms, output pasted verbatim in section 2 with exit codes.
    No estimate anywhere in this package.
15. ✅ **Images / alt text suggestions** provided in section 6, including the two new sections. `visual-brief`
    still runs after approval per CLAUDE.md section 9, so these are directional, not a brief.

**Result: 14/15. One ❌: item 6, word count against the plan's estimate.** Below the 2-or-more ❌ STOP
threshold, and not in the positioning, compliance or cannibalization category. **No STOP.**

### 3.2 Content strategy checklist (9 points, `content-strategy-guidelines.md` section 16)

1. ✅ **Correct hub.** AI in Fitness (Hub 1, live hub `ai-in-fitness-industry`, published 2026-07-31),
   Digital coaching cluster, as recorded in `plan.md` and `content-pack`. The up-link points at that hub.
2. ✅ **action_type respected.** `create net-new` with `existing_urls: []`. Nothing was refreshed or
   sectioned into an existing page.
3. ✅ **No duplication of existing_urls; cannibalization guardrail held.** The row's guardrail is "Targets
   coaches/platform workflows, not generic fitness apps. Do not duplicate the hub's broad overview." The
   revision strengthened this: the standalone "Why this matters now" section and all fitness-industry and
   market-trend prose were deleted, and the hub link survives as a single clause. Every section now serves
   coach or platform workflow, onboarding, check-ins, reading the data, integration, pilot evaluation or
   limits. Head term (`online fitness coaching programs`) differs from the legacy page's intent.
   **Open, and it needs a decision, but it is not a breach by this article:** review item 1 identifies
   overlap with the older live page `ai-body-scanning-for-fitness` and asks for that page to be redirected
   or rescoped "separately". That is a content-ops task on the other URL, see decision item 4A.4.
4. ✅ **Vertical boundary held; scope note present.** Scope note is the third block under the H1. `GLP-1`
   occurs exactly once, inside the boundary section, expanded. No wellness-rewards language. No clinical,
   diagnostic, eligibility, underwriting or employment framing outside the boundary statement.
5. ✅ **Internal links in all 4 directions** (this closes the ❌ the 2026-08-26 package carried):
   up ×1 `content-hub/ai-in-fitness-industry/`, sideways ×1 `content-hub/body-scanning-technology-comparison/`
   (added per review item 6), trust ×1 `content-hub/mobile-body-scanning-accuracy/`, down ×2
   `fitxpress/for-connected-and-digital-fitness/` (mid-article evaluation plus conclusion CTA, plan-sanctioned,
   two different anchors). Verified by URL count: 1/1/1/2.
6. ✅ **FAQ section present and GEO/AEO-friendly.** 7 questions, answers measured at 2 to 3 sentences each,
   inside the 2-5 rule.
7. ✅ **"What FitXpress does not do" present; no banned positioning claims.** No "most accurate", no
   "guaranteed compliance", no FDA or medical-device claim, no "replaces DXA/BIA/a calibrated scale" (the
   reference-method boundary is conditional: "not equivalent to DXA, BIA, or a calibrated scale where a
   workflow or protocol requires those reference methods"), no named competitors. **Heading-level note:**
   the section is now an H3 inside section 10, because the reviewer's 12-part order has no standalone slot
   for it. Content and force unchanged. Anyone building FAQ or Article schema from the H2 list should know
   the boundary block sits one level down.
8. ✅ **No unsubstantiated medical / legal / underwriting / employment / clinical-trial claims.** Compliance
   is framed entirely on data-privacy grounds (HIPAA, GDPR, encryption, retention). Two compliance-claim
   **wordings** changed against `context-pack.md` and need product/security sign-off before publish, see
   4A.2 (FX-007) and 4A.6 (FX-006). Both are softenings or reviewer-mandated precision, not expansions of
   what is claimed, which is why this is a decision item and not a ❌.
9. ✅ **Owns one distinct search intent:** how a remote coaching program captures and compares client body
   data, and how to evaluate that as a build. Distinct from the hub's broad overview, from the accuracy
   framework, from the technology comparison, and from the GLP-1/telehealth cluster.

**Result: 9/9. No ❌. No STOP.**

### 3.3 STOP-rule arithmetic, stated explicitly

- SEO checklist: 1 ❌ (word count). Threshold is 2 or more per checklist. Not triggered.
- Strategy checklist: 0 ❌. Not triggered.
- Positioning / compliance / cannibalization auto-STOP: **not triggered.** The medical-device wording
  conflict (4A.1) is a conflict between governing documents, and the text as it stands complies with the
  newer canonical rule and passes the detector. The FX-006 and FX-007 wording changes (4A.2, 4A.6) narrow
  or sharpen approved claims, they do not assert anything new. The `ai-body-scanning-for-fitness` overlap
  (4A.4) is a task on a different URL.
- **Nothing returns to `seo-editor`.** What is blocking is Vadim's six decisions in 4A, not text quality.

---

## 4. Open items

### 4A. Decision needed from Vadim BEFORE publish

**1. Which document wins on medical-device framing.** *(positioning, and the only place this article
deliberately disobeys the reviewer)*

Carried verbatim from `changelog-revision1.md` and `log.md`:

> **NOT APPLIED — "Use the approved wording: 'FitXpress is not positioned as a medical device.'"** (review
> item 3, seventh bullet.) The article keeps the direct form: **"FitXpress is not a medical device."**
> Reason: "positioned as" is a hard ban for product, intended-use and regulatory statements in
> `brand-assets/content-strategy/terminology-guardrails.md` (Part 2 §2.10, and the Overrides table at the
> top of that file, ~line 32) ... its Overrides table records explicitly that it **supersedes**
> `brand-assets/style-guides/editorial-guardrails.md` #6, which is where the reviewer's wording comes from
> (that principle prescribed "not positioned as a medical device" from 2026-06-09 until the 2026-08-25
> amendment). `CLAUDE.md` §6 and §15 hard requirement #7 carry the same override, and the detector flags
> `not positioned as` as a hard fail. Applying the review line as written would fail the gate this article
> has to pass. **This is an unresolved conflict between two governing documents and one reviewer
> instruction. Listed as an open item for Vadim/Asselya to settle (which document wins).**

Publisher's note: I verified both sides. `positioned as` is 0 in the file, the direct form appears twice,
and the detector run in section 2 has `hard_fails: []`. If Vadim rules for the reviewer, the text change is
two words in two places, but it will fail `detect-ai-tells.py` and CLAUDE.md section 6 until the guardrail
file is changed first. **Decide the rule, then the text.**

**2. FX-007 wording: SSE-S3 out, automatic blurring in.** *(compliance claim record)*

Carried verbatim from `changelog-revision1.md`:

> 1. **FX-007, SSE-S3 downgraded to a plain encryption statement.** The body now says "encrypted in transit
>    and at rest on Amazon Web Services (AWS) infrastructure" and no longer names Amazon Simple Storage
>    Service or server-side encryption with Amazon S3 managed keys (SSE-S3). Reason: the public FitXpress
>    Privacy Policy (verified 2026-08-31) states encryption in transit and at rest, enforced by default, and
>    AWS hosting, but does not state SSE-S3; SSE-S3 is an internal security-commitment detail. FX-007's text
>    in `context-pack.md` still names SSE-S3, so this is a deliberate softening of an approved claim, not a
>    drafting slip.
> 2. **FX-007, blurring detail added.** "Retained photos are automatically blurred." is new to this article,
>    sourced from the privacy policy ("When temporary storage is selected, all retained photos are
>    automatically blurred") and consistent with `about-me.md` ("auto-blurred if retained").

Publisher's note: I re-fetched the live policy myself today and both halves check out (table in section 2).
Approving the text also means **updating the FX-007 record in `context-pack.md`**, which still reads "AWS S3
SSE-S3 encryption", and CLAUDE.md section 12, which still lists "AWS S3 SSE-S3 encryption for all data".
Otherwise the next article inherits the old wording and this one looks like the outlier. Also worth a
product/security glance: HIPAA is not mentioned anywhere in the public policy, so the article's HIPAA
sentence rests on FX-007 alone.

**3. Confirm the canonical BOFU URL.** *(path debt, blocks publish because it is linked twice)*

Carried verbatim from `plan.md` Open items #4 and `log.md`:

> **BOFU URL path debt.** `/fitxpress/for-connected-and-digital-fitness/` is flagged in CLAUDE.md §16 as
> using a non-existent path level with a breadcrumb pointing at a redirect. URL kept as written in
> content-plan.md. Confirm the canonical URL to link down to before publish.

Publisher's note: linked **twice** in this revision (mid-article evaluation line at the end of section 7,
and the conclusion CTA). If the canonical path is different, both occurrences change, and so does the
"down" leg of the 4-direction link check.

**4. The older `ai-body-scanning-for-fitness` page: redirect or rescope.** *(cannibalization, separate task)*

Carried verbatim from `review1-comments.md` item 1:

> There is also overlap with the older [AI-powered fitness tracking article](https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/). Consider redirecting or rescoping that older page separately.

and from `changelog-revision1.md`:

> **Out of scope — the older `ai-body-scanning-for-fitness` page.** Review item 1 suggests redirecting or
> rescoping it "separately". Nothing in this deliverable touches that page. Carried to open items.

Publisher's note: nothing in this package changes that page, and this article does not breach its own
cannibalization guardrail (checklist 3.2 item 3). The decision is still needed **around** publish, because
publishing puts a second live URL into the same hub against overlapping intent. Two clean options: 301 the
legacy page here, or rescope it and keep both. It is a separate task either way, not an edit to this text.

**5. Repeatability convention: `< 1 cm` or "less than 1 cm".** *(house convention vs reviewer's sentence)*

Carried verbatim from `changelog-revision1.md`:

> 3. **Repeatability is no longer written as `< 1 cm`.** `about-me.md` locks the convention "write
>    repeatability as `< 1 cm`"; the reviewer's mandated sentence spells it "less than 1 cm". The reviewer's
>    wording is used, matching the precedent set in `glp-1-market-hub/changelog-revision1.md` item 4. If the
>    locked convention is meant to win, the two sentences need reconciling at source, not per article.

Publisher's note: the shipped sentence is "For most evaluated measurements, repeated scans showed typical
scan-to-scan differences of less than 1 cm", once in the body and once in the FAQ. `< 1 cm` appears zero
times. Either answer is a two-string edit; the point is that `about-me.md` and the reviewer currently
disagree and the next article will hit this again.

**6. FX-006 wording: the `±` is gone, and the claim record still has it.** *(compliance claim record)*

From `review1-comments.md` item 3:

> Replace "average error margin of ±3.5%." The approved claim is approximately 3.5% average prediction error
> under evaluated conditions. The ± symbol implies a different statistical meaning.

Shipped sentence: "A predicted weight from Smart Scales, read from the images with approximately 3.5%
average prediction error under evaluated conditions." Zero `±` in the file. But `context-pack.md` FX-006
still reads "Weight estimation ±3.5% average error margin", and CLAUDE.md section 1 still reads "Weight
estimation ±3.5%". Lower stakes than 4A.2 because the reviewer asserted the corrected wording as the
approved one, so approval here is mostly **updating the claim record** so the next writer does not
reintroduce `±`.

### 4B. Informational, carried forward, not blocking

1. **Word count.** 2,584 prose words against `plan.md`'s ~2,000 (range 1,900-2,300). The single ❌ on the SEO
   checklist. Full reasoning in checklist item 6. Earlier framings, carried verbatim:
   > **Word count vs plan ceiling (editorial call, resolved toward quality).** ... Held here deliberately
   > rather than stripping must-cover content ... Publisher/Vadim can request a further trim to <=2,300 if
   > the plan ceiling is hard, but it would mean cutting must-cover depth.
   and from revision 1:
   > **Word count vs the plan's 2,300 soft ceiling** (edit #1): superseded by the review's own target shape.
2. **Head-term difficulty is still TBD.** Carried verbatim:
   > **Difficulty is TBD.** Ahrefs returned `null` (no measurement) for the head term's difficulty, and
   > `remote body measurement` has null volume. Not invented. If a difficulty read matters before writing, a
   > targeted re-pull can be requested.
   Declared here on purpose: an undeclared TBD dependency caps `quality-controller` category A (CLAUDE.md,
   2026-08-26).
3. **Thin demand, already decided at checkpoint 1.** Carried verbatim:
   > **Thin demand — confirm the head term and the go/no-go.** The exact topic phrase has no measured demand
   > (`seed_has_data: false`). The working head term `online fitness coaching programs` is **100/mo,
   > difficulty unmeasured**, and the whole cluster is low tens-to-hundreds. ... Approve as-is, or ask to
   > fold this angle into a higher-volume sibling / the hub instead.
   Repeated for visibility only. Volume 100/mo and CPC ~$6.00 are real Ahrefs figures.
4. **No named coaching customer exists.** Carried verbatim:
   > **Not attempted — a named coaching customer.** No fitness-coaching customer exists in
   > `proof-points.md` (Yazen and UK Meds are weight-loss/pharmacy and would breach the vertical boundary).
   > The article still runs on capability and segment framing with zero named customers.
5. **Zero third-party / external sources.** All 5 links are internal. Carried verbatim:
   > **Zero external sources** (publish-stage flag): unchanged. All five links are internal. The article's
   > factual load is product claims and one privacy policy, and no external authority was added in this
   > round; `quality-controller` will still cap category B on that basis.
6. **Central Privacy / Regulatory FAQ is still not live.** Carried verbatim:
   > **Central Privacy/Regulatory FAQ not live** (plan #5): still not live, but the privacy content is now
   > verified against the public privacy policy instead of standing on an internal note alone, so the
   > missing hub is no longer the only backing for the section.
7. **HIPAA has no public artifact.** New this round, from my own verification: the live FitXpress Privacy
   Policy names GDPR and CCPA and does not mention HIPAA. The article's HIPAA sentence therefore rests on
   FX-007 (internal security commitment) alone. Approved claim, so not a deviation, but worth knowing if a
   prospect follows the link.
8. **Boundary section is an H3, not an H2.** Carried verbatim:
   > **Applied differently — the boundary section's heading level.** Review item 2's 12-part order leaves no
   > slot for a standalone `What FitXpress does not do` H2 ... It is now an **H3 inside section 10** ...
   > Content and force unchanged.
   Matters at CMS time for any auto-generated table of contents or schema built from H2s.
9. **BIA and DXA are expanded under the heading, not in it.** Carried verbatim:
   > **Applied differently — BIA and DXA are expanded in the first sentence under the section heading, not
   > in the heading itself.** ... Flagged because a mechanical M1 check will see the heading first.

### 4C. Closed, recorded so nobody reopens them

- **Sideways internal link omitted** (plan #6, write #3, edit #4, publish 2026-08-26): **closed** by review
  item 6. `body-scanning-technology-comparison` is a technology comparison in the same product family, so
  the Fitness/GLP-1 boundary concern that drove the omission does not apply. All 4 link directions present.
- **`±3.5%` in the body:** closed, 0 occurrences.
- **`DEXA` spelling:** closed, 0 occurrences, DXA expanded once.
- **Six unsupported retention / CAC sentences:** closed, all deleted. Retention and engagement now appear
  only as something a pilot measures against a program's own baseline (3 places, all measurement framing).
- **Repetition of the five recurring claims:** closed. Verified by my own grep, one body instance plus one
  FAQ instance each: `80+` 1+1, `under 45 seconds` 1+1, `less than 1 cm` 1+1, privacy/`30 days` 1+1,
  who-decides 1+1. `1.5 to 2.0 cm` also 1+1. `96 to 97%` and `3.5%` body only.
- **Residual `so` connector** flagged in the 2026-08-26 package: closed, the word does not occur.
- **The old package's stale meta description:** closed, superseded by section 1 of this file.

---

## 5. Alt options

### Meta title variants

1. **Online Fitness Coaching Programs: Remote Body Measurement** (57 chars), **RECOMMENDED.** Head term at
   character 1, keeps the `remote body measurement` secondary phrase (difficulty 26) in the string, reads as
   the same topic as the H1.
2. **Online Fitness Coaching Programs: Body Measurement Workflow** (59 chars), head term still at
   character 1, and "Workflow" is the truer label for the revised article (workflow, coaching-stage table,
   pilot evaluation). Costs the `remote body measurement` phrase match.
3. **Remote Body Measurement for Online Fitness Coaching Programs** (60 chars), exact `content-plan.md`
   row and H1 wording. Use if title/H1 consistency should beat front-loading; head term lands at character
   29, still inside the first 60 but not front-loaded.

### Meta description variants

1. **Online fitness coaching programs can capture client body data from a guided phone scan. See how it
   fits check-ins and what a pilot should measure.** (146 chars), **RECOMMENDED.** Head term first,
   mechanism, then the two blocks the review added. No engagement or retention promise, no audience-reaction
   claim, does not restate the title.
2. **Online fitness coaching programs can standardize remote client measurement with a guided two-photo
   scan. See where it fits a check-in and where it stops.** (153 chars), same front-loading, adds the
   two-photo detail and carries the article's stated-limits posture into the SERP. Slightly long.
3. **Online fitness coaching programs need client records that compare across weeks. See how a guided
   two-photo scan fits check-ins, with its limits stated.** (151 chars), leads on comparability, which is
   the actual argument of section 2. Softest hook of the three.

Rejected on purpose: anything built on the old "clients trust", "visible progress" or "retention gains"
framing. Review item 4 deleted those claims from the body, so a meta tag promising them would be a claim the
article no longer makes.

---

## 6. Images / alt text suggestions

No visual brief exists yet. `visual-brief` runs after Vadim approves this package (CLAUDE.md section 9), so
these are directional. `DESIGN.md` tokens only: electric blue `#143DFF`, navy `#050F40`, Satoshi. No
clinical or lab imagery anywhere, this is the non-clinical Fitness vertical. No ranked or scored leaderboard
of methods, the comparison is by role.

1. **Hero / OG image.** Split composition: a smartphone in guided-capture pose (front and side silhouette
   outline with an on-screen framing guide) beside a two-model side-by-side progress comparison.
   **Alt:** "Smartphone capturing a guided body scan beside a side-by-side 3D progress comparison for an
   online fitness coaching program."
2. **Workflow visual, at "How it fits the coaching workflow".** Four numbered steps matching the list:
   baseline at onboarding, structured outputs generated, results in the coach's view, comparison at each
   check-in.
   **Alt:** "Four-step remote body measurement workflow: baseline capture at onboarding, structured outputs
   generated, results in the coach's view, and comparison at each check-in."
3. **NEW: coaching-stage decision table, at "How coaches can use the results".** Render the four-row table
   as a graphic, with the fourth column ("Limitation") given the same visual weight as the other three, not
   set as fine print. That column is the point of the section.
   **Alt:** "Table of four coaching stages with the data reviewed, the possible coach action, and the
   limitation at each stage: onboarding, recurring check-in, apparent plateau, and program completion."
4. **NEW: pilot-evaluation visual, at "How to evaluate a pilot".** The seven process measures in the
   article's order, with the first two (scan completion, retake rate) visually gated ahead of the rest and
   engagement or retention last. Do not draw an upward trend line or a percentage: the section's argument is
   that these are measured against the program's own baseline, not promised.
   **Alt:** "Seven pilot measures for a remote body measurement rollout, ordered from scan completion and
   retake rates through coach review time to engagement or retention measured against a baseline."
5. **Method comparison table (optional, good for social reuse).** Rendered version of the seven-row
   comparison, keeping consumer smart scale and professional BIA on separate rows and keeping the
   "Limitation to disclose" column visible.
   **Alt:** "Comparison of client self-report, home tape measurement, consumer smart scale, professional
   BIA, DXA, progress photos, and mobile body scan, showing what each provides and its limitation for a
   coaching program."

---

## 7. Article (CMS-ready)

Body of `draft-v3-revision1.md` with the YAML frontmatter removed and every internal
`<!-- claim: FX-00X -->` / `<!-- source: ... -->` annotation stripped. Headings, tables, emphasis and
markdown links are otherwise byte-identical to the approved draft (verified by diff). Two tables, seven FAQ
items, five internal links, zero em dashes.

# Remote Body Measurement for Online Fitness Coaching Programs

A coach carrying two hundred remote clients cannot put a tape measure around anyone's waist, and the measurement still has to happen. Remote body measurement is how online fitness coaching programs close that gap: a guided smartphone scan becomes the point where body data gets captured, in place of an in-person intake or check-in appointment.

The operational question is narrower than the technology question. Capture has to fit the check-in cadence a program already runs, the outputs have to land in the tool the coach works in daily, and the limits of the data have to be understood before a progress screen gets built on top of them. Wider background on how structured body data is used across fitness products sits in the [AI in the fitness industry](https://3dlook.ai/content-hub/ai-in-fitness-industry/) hub.

*Scope note: a fitness progress and intake layer for coaching programs, non-clinical. FitXpress is not a medical device and does not make clinical or eligibility decisions.*

## The measurement problem in online fitness coaching programs

Coaching delivered remotely runs on data the coach never collects in person. A client reads a weight off a home scale, takes a progress photo in whatever light the room offers, and sometimes wraps a tape measure around their own waist at a height no two weeks match. How each of those figures was produced goes unrecorded.

Comparison is where that becomes expensive. A coach adjusting a program at week eight needs to know what changed since week one, which requires both records to have been made the same way. Self-reported weight moves with hydration, food timing, and which scale was used. A tape held half an inch higher reads as a loss that never happened. Photos taken in a different room at a different hour are hard for either side to read as evidence of anything.

The missing piece is comparability: records captured the same way each time, at the points in a program where somebody makes a decision.

## What remote body measurement provides

Remote body measurement is the practice of capturing a client's body data from their own device, without an in-person appointment. In coaching that usually means a guided smartphone scan. The client takes two photos, front and side, and software returns a structured record in under 45 seconds.

Five kinds of output come back, and the differences between them matter once a coach starts reading them:

- Model-generated body measurements, 80+ of them, extracted from the 3D model the software builds from the two photos.
- Software-derived body-composition estimates, including body fat percentage, lean mass, and fat mass.
- Calculated outputs such as BMI and basal metabolic rate (BMR), computed from scan outputs together with entered profile values.
- A predicted weight from Smart Scales, read from the images with approximately 3.5% average prediction error under evaluated conditions.
- The 3D model itself, which is what makes a side-by-side visual comparison between two check-ins possible.

The line between a measured value and an estimate is worth holding onto. A waist circumference comes out of the model's geometry. Body fat percentage is derived by applying a formula to those figures, which means it carries the formula's assumptions along with the scan's. Composition estimates read best as a trend across several scans; a single reading deserves more caution. On a client-facing progress screen they also draw the most attention, which is an argument for showing circumference trends next to them.

## How it fits the coaching workflow

The workflow attaches to a cadence that exists: a baseline at the start, then follow-up scans at the check-in points already on the calendar.

1. **Baseline at onboarding.** The client completes the program's profile step, then follows an on-screen flow to take two photos, front and side. On-screen guidance corrects framing and pose during capture. Which profile fields that step requires varies by program, and weight is optional in supported workflows, since Smart Scales predicts a figure from the photos and the software flags a difference when a self-reported weight is also supplied. BMI is a calculated output that depends on height and weight both being available.
2. **Structured outputs generated.** Processing returns the measurements, the composition estimates, the calculated values, the predicted weight, and the 3D model as structured data.
3. **Results appear in the coach's view.** Outputs land in the coaching platform where clients are reviewed, which removes the parallel spreadsheet and the manual entry of tape figures.
4. **Comparison at each check-in.** A follow-up scan lines up against the baseline. The coach sees which measurements moved and by how much; the client sees the two 3D models side by side.

The cadence stays the program's own, whether that is monthly check-ins, six-week training blocks, or a scan at each end of a twelve-week challenge.

## How coaches can use the results

Structured data earns its place only if it changes something a coach does. Four stages cover most coaching programs, and each one supports a different action and stops at a different limit.

| Coaching stage | Data reviewed | Possible coach action | Limitation |
| :- | :- | :- | :- |
| Onboarding | Baseline measurements and 3D model | Establish the starting record | Does not prescribe a program |
| Recurring check-in | Measurement and composition trends | Review progress with other client data | Small changes require context |
| Apparent plateau | Weight and regional measurements | Investigate different progress signals | Cannot determine the cause |
| Program completion | Full longitudinal comparison | Summarize progress | Avoid causal conclusions |

The fourth column carries the weight. A scan can show that a waist circumference moved across six weeks by more than the scan-to-scan variation. It cannot say whether the training block, the diet change, or a sleep change produced that movement, and it cannot say what to do next. FitXpress supplies the structured record; the coach makes the call.

## Comparison with scales, tape measurements, photos, BIA, and DXA

Remote coaching programs draw on six other measurement methods, and two of those, professional bioelectrical impedance analysis (BIA) and dual-energy X-ray absorptiometry (DXA), require the client to be in a room with a device.

| Method | What it provides | Limitation to disclose | Where it fits a coaching program |
|--------|------------------|------------------------|----------------------------------|
| Client self-report | Weight and rough circumference figures | Varies by scale, timing, and technique; hard to compare across weeks | Low-stakes check-ins, budget programs |
| Tape measurement at home | Circumferences | Placement varies between sessions; difficult to reproduce | Motivated clients who measure carefully |
| Consumer smart scale | Weight, and an impedance-based body-composition estimate | Composition estimates depend on hydration, device model, and electrode placement | Daily weight trend at home |
| Professional BIA | Weight and segmental composition estimates from a calibrated device | Requires an in-person visit; results depend on the device and the preparation protocol | Periodic assessment where a studio or clinic is available |
| DXA | Reference-grade body composition and regional fat and lean distribution | Clinic-based and appointment-bound; access and cost depend on the provider; circumference measurements sit outside its output | Occasional reference reads for clients who need them |
| Progress photos | Visual change | Lighting, pose, and framing vary; not measurable | Motivation and qualitative review |
| Mobile body scan | Measurements, composition estimates, calculated values, a predicted weight, and a 3D model, comparable across scans | Depends on capture conditions; not a clinical reference method | Standardized intake and longitudinal progress across a remote roster |

A calibrated scale remains the right instrument for a precise weight. DXA is a reference method for body composition in clinical and research settings, and professional BIA sits between the two, quicker to run and sensitive to the client's hydration state on the day. None of the three runs remotely across a whole roster at every check-in, which is the practical constraint a coaching program works inside.

A mobile scan works alongside them. A client can weigh in daily on a connected scale, book a DXA read when a program genuinely calls for one, and scan monthly for the circumference and composition trend the coach reviews. Differences between scanning approaches themselves, including two-photo capture, video, and hardware booths, are set out in [2-Photo vs Video vs Hardware body scanning](https://3dlook.ai/content-hub/body-scanning-technology-comparison/).

## Where FitXpress fits

FitXpress is the body-data capture and scan-to-scan comparison layer inside a coaching product. A platform integrates it through an application programming interface (API) or a software development kit (SDK), which handles guided capture, processing, and the structured output.

3DLOOK provides the capture flow, the measurements, the composition estimates, the calculated values, the 3D model, and the comparison data across scans. The platform builds what the coach and the client actually see: program logic, check-in scheduling, messaging, and how results are presented. FitXpress returns structured data, and the platform team decides how that data is used.

Programs at the comparison stage can review how [FitXpress supports remote progress tracking for coaching programs](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) before scoping a build.

## Accuracy, repeatability, privacy, and implementation

### Accuracy and repeatability

The better question is narrower: accurate enough for which decision? A coach is not underwriting an insurance policy or planning a procedure. The decision in front of them is whether a client's waist is trending down across eight weeks and whether the program should change.

Internal validation against expert manual measurements showed approximately 96 to 97% accuracy, with typical absolute error of 1.5 to 2.0 cm. Those figures describe agreement with a manual reference under consistent capture conditions, which is why capture guidance matters more in production than any single headline figure.

For progress tracking, repeatability carries more weight than one-off accuracy. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. When scan-to-scan differences stay that small, a modest real change is more likely to be distinguishable from capture variation. What counts as accurate depends on the reference method, the capture protocol, the population measured, and the intended workflow, all four of which the [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out in full.

### Privacy and consent

Client body data needs a stated privacy posture before the first scan. FitXpress complies with the Health Insurance Portability and Accountability Act (HIPAA) and aligns with the principles of the General Data Protection Regulation (GDPR). Data is encrypted in transit and at rest on Amazon Web Services (AWS) infrastructure, and photos are either deleted immediately after processing or retained for up to 30 days, depending on the business client's configuration. Retained photos are automatically blurred. A coaching program still owns its own consent language and needs a retention rule it can state plainly to clients.

### Implementation

**Integration scope.** Scope the first build to one capture point and one comparison view. The platform team owns display, storage, and the client-facing progress screen; the integration returns the structured record.

**Capture protocol.** Production conditions are not lab conditions. Clients scan in odd lighting, in loose clothing, holding the phone at the wrong angle. Consistent on-screen guidance and retake prompts do more for real-world results than any single accuracy figure, which makes capture testing with real clients the first thing to schedule.

**Change thresholds.** Decide in advance what size of change the program treats as meaningful, and base that threshold on measured scan-to-scan variation. A movement smaller than the variation is best read as capture noise.

**Model maturity.** Behind the outputs are 9+ years of training data, including 150K+ photos, 30K+ 3D scans, and 430K+ measurements, which is the context a technical buyer usually asks for during diligence.

## How to evaluate a pilot

A pilot answers process questions before it answers commercial ones. Seven measures are worth instrumenting, and each one is a process measure the platform reads from its own data:

- Scan completion and retake rates.
- The share of clients with a usable baseline-to-follow-up comparison.
- Coach review time per client at a check-in.
- Scheduled check-in completion.
- Support requests generated by the scan step.
- Client use of the progress view.
- Engagement or retention measured against the program's own pre-pilot baseline.

The first two govern everything after them. A high retake rate is a finding about capture guidance, and it has to be fixed before the later measures can be read as anything. Review time is the measure most often skipped and the one an operations lead asks about first, since coach hours are what caps how many clients a program can serve well.

Engagement and retention belong at the end of that list on purpose. A pilot can test whether a progress view moves them against a baseline the program already has. Treating the movement as a given before the test defeats the point of running one.

## Best-fit coaching programs and limitations

Remote body measurement fits coaching businesses that deliver remotely and bill on a recurring basis, and its value grows with the size of the roster and the length of the client relationship.

- Online coaching programs running subscription memberships with regular check-ins.
- Digital coaching platforms serving many coaches at once, where measurement consistency has to hold across the whole base.
- Hybrid personal-training studios extending coaching between in-person sessions.
- Corporate fitness coaching delivered to distributed employees.

Evaluation usually sits with the founder or CEO, the chief product officer, or the head of growth or engagement, with a product manager or chief technology officer (CTO) handling integration. The question they bring is whether body-data personalization moves engagement and retention enough to justify the build, which a pilot measured against a baseline can answer.

It is not the right tool for every practice. A solo coach with a handful of local, in-person clients gains little from remote capture. A program with no recurring revenue has fewer check-ins to standardize and less to protect.

### What FitXpress does not do

FitXpress is not a medical device. It does not diagnose conditions, make clinical decisions, or determine treatment eligibility. It has no role in glucagon-like peptide-1 (GLP-1) eligibility, and who qualifies for a coaching program remains a matter for the coach and the program's own rules. Software-derived body-composition estimates are not equivalent to DXA, BIA, or a calibrated scale where a workflow or protocol requires those reference methods.

What FitXpress does is narrower. It captures structured body data remotely, standardizes how a coaching program measures clients, and supports comparison from one scan to the next.

## FAQs

**What is remote body measurement for online fitness coaching programs?**

It is capturing a client's body data from their own smartphone, without an in-person appointment. A guided two-photo scan returns measurements, body-composition estimates, calculated values such as BMI, a predicted weight, and a 3D model. Those outputs form a record a coach can compare from one check-in to the next.

**How do clients take the measurements?**

The client completes the program's profile step and follows an on-screen flow to take two photos, front and side, with guidance on framing and pose. Capture takes about a minute, and processing returns results in under 45 seconds.

**Can it replace a smart scale, BIA, or DXA?**

No. A connected scale gives a precise weight, and BIA and DXA are in-person methods for body composition, with DXA used as a reference method in clinical and research settings. A mobile scan complements all three by adding a comparable remote record across scans that none of them produces at roster scale.

**How accurate and repeatable is it?**

Accuracy depends on the decision, the reference method, the capture protocol, and the population measured. In internal validation against expert manual measurements, typical absolute error ran 1.5 to 2.0 cm. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, which is the property that matters most for comparing check-ins.

**What body data does it capture?**

From two photos, FitXpress generates 80+ body measurements along with software-derived body-composition estimates, including body fat percentage and lean and fat mass, and calculated outputs including BMI and BMR. A predicted weight and a 3D model come back with them.

**Is client body data private?**

FitXpress is HIPAA-compliant and GDPR-aligned. Data is encrypted in transit and at rest, and photos are either deleted immediately after processing or retained for up to 30 days, depending on how the business client configures it. A coaching program should still obtain explicit client consent and state its own retention rule.

**Does the coach or the tool decide anything?**

The coach decides. FitXpress provides structured body data and scan-to-scan comparison; it makes no recommendations and no program decisions. Standardized capture changes the quality of the input to the coach's judgment.

## Conclusion and next steps

Remote body measurement changes one operational thing for a coaching program. Inconsistent self-reports and progress photos become a structured record captured from the client's own phone, comparable from one check-in to the next, with the limits of that record written down where coaches can see them.

What a program builds on top of that record is a product decision, and the honest way to find out whether it lands is to instrument the pilot: completion and retake rates first, coach review time second, engagement measured against a baseline last. Explore [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) to review the workflow, or book a demo to walk through it with the 3DLOOK team against a specific program.
