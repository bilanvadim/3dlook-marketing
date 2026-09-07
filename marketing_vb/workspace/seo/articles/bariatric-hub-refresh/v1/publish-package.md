---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
status: ready_for_review
created: 2026-09-03
publish_type: refresh-republish-in-place
live_url: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
source_draft: draft-v2-editor.md
lint_verdict: "PASS, 9/9 (2026-09-03 rerun, see publisher-report.md §1)"
datePublished_action: "RE-DATE to the republish date — Vadim's call, 2026-09-03"
datePublished_original: 2026-06-05
dateModified_set_to: publish date
author_byline: "Assel Sekerova"
vadim_decisions: "byline Assel · re-date the post · slug unchanged (2026-09-03)"
faq_branch: B (16 questions)
---

# Publish Package — Bariatric hub refresh

`bariatric-hub-refresh` is the workspace directory name only. **Every downstream reference — CMS
slug, canonical URL, this file's own frontmatter — uses the published slug**
`bariatric-pre-qualification-mobile-3d-body-scanning`. This has bitten the pipeline before
(`plan.md` writer note #10).

---

## 0. Read this before touching the CMS — this is a republish IN PLACE

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
   softening the medical-device sentence, adding "leverage") re-introduces exactly what four editing
   passes removed. If something needs to change, change it in the workspace and re-lint, not in the
   CMS editor.

---

## 1. Meta

**Recommended title** (54 chars):
`Bariatric Pre-Qualification & Progress Tracking (2026)`

**Recommended description** (154 chars):
`The 7-day payer clock and documented BMI history are reshaping bariatric pre-qualification and progress tracking. See what a program's file needs to hold.`

**Slug:** `bariatric-pre-qualification-mobile-3d-body-scanning` — **unchanged, see §0.1.**

**Category:** Use Cases (matches the live page's existing taxonomy — this is a republish, not a
re-categorization)

**Tags:** Use Cases, Health, Technology (live page's current tags; carry forward as-is)

### Why this direction, and what it deliberately does not do

Per `plan.md`'s "Recommended Title" section, the meta description leads with the two workflows
(pre-qualification, progress tracking) and the new payer-clock fact, **not** with the product name.
The live meta description opens with "How bariatric programs can use FitXpress..." — that is the
defect this refresh corrects (`plan-audit.md` §D, deletion #2). Neither variant below names
FitXpress; the product appears in the body from Section 7 onward, which is where `about-me.md`'s
CTA-by-funnel-stage logic puts it for a Hub, BOFU-weighted page.

The recommended **meta title** is a compressed version of the new H1 (*"Bariatric Pre-Qualification
and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams"*, 104 chars — far over
any title-tag budget). It keeps the primary keyword `bariatric pre-qualification` at the very start
(well inside the first half of a 54-char string), keeps the co-headlined "Progress Tracking" spine
the plan insists on, and keeps the `2026` recency signal the plan argues is cheap here specifically
because the slug never carries the year (`plan.md` Recommended Title, paragraph 2).

### Alt options

**Meta title variants**

| # | Variant | Chars | Note |
|---|---|---|---|
| 1 | **Bariatric Pre-Qualification & Progress Tracking (2026)** | 54 | **Recommended.** Keyword-first, keeps the year signal, keeps both spines. |
| 2 | Bariatric Pre-Qualification: Patient Progress Tracking | 54 | The content-plan's original target title, compressed, with "Patient" restored. No year signal — same trade-off `plan.md` names for Option 1 under "Other options" (no recency cue on a page whose whole refresh case is that 2026 facts changed). Use if Vadim prefers the plan's literal copy over the year signal. |
| 3 | Bariatric Pre-Qualification and Progress Tracking, 2026 | 55 | Same content as the recommendation, "and" instead of "&" and a comma instead of parentheses, for house style if ampersands are disfavored in titles (not currently specified anywhere in CLAUDE.md). |

**Meta description variants**

| # | Variant | Chars | Note |
|---|---|---|---|
| 1 | **The 7-day payer clock and documented BMI history are reshaping bariatric pre-qualification and progress tracking. See what a program's file needs to hold.** | 154 | **Recommended.** Leads with the payer clock (the single most important factual change on the page, per `plan-audit.md` §A) and the documented-BMI-history argument (the sharpest new operational point, §A item 3), both ahead of the keyword phrase itself. |
| 2 | Bariatric pre-qualification and progress tracking run on a 7-day payer clock now. See what documented BMI history a program's file needs to hold, and when. | 155 | Leads with the exact-match primary keyword phrase instead of the payer-clock hook. Use if exact-match-first is preferred for this SERP snippet over the sharper hook. |

Both descriptions carry `bariatric pre-qualification` (or its near-exact phrase) exactly once, do
not repeat the recommended title, and end on an implicit promise rather than a hard sell, consistent
with a Hub page's soft-CTA register (`about-me.md` CTA-by-funnel-stage; the one direct CTA on the
page is inside the body, Section 12, not in the description).

---

## 2. Final checklist

### SEO / mechanical checklist

- [x] **Primary keyword in H1, first paragraph, 1-2 H2.** `article_lint.py` confirms 6 occurrences,
      H1, first paragraph ("Bariatric pre-qualification runs on that record..."), and H2 #6 title
      itself ("The bariatric pre-qualification workflow..."). Also opens Section 2's prose
      immediately after its own H2.
- [x] **Meta title ≤ 60 chars, primary keyword in first half.** Recommended: 54 chars, keyword at
      position 1.
- [x] **Meta description 140-160 chars.** Recommended: 154 chars (task brief's ≤155 cap and the
      general 140-160 band both satisfied).
- [x] **All numbers from approved_claims (none invented).** FX-001, FX-002, FX-005, FX-006, FX-007,
      FX-008, FX-009 all trace to `approved_claims` in the pack (`article_lint.py` claim-traceability
      gate: ok). The five ASMBS-estimate figures added after Checkpoint 1 (`270,089`, `279,967`,
      `58.2%`, `23.4%`, `11.9%`) are now in the pack's `external_citations.verified_current_keep`
      under `ext_claim_id: ASMBS-ESTIMATE-2023`, sourced to
      `https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/` rather than the Fact
      Sheet PDF (which carries them only as an unquotable graphic, per gap analysis §3b). **FX-003
      (ISO 8559, 0.40 cm), FX-004 (95%+ repeatability, non-publishable) and FX-010 (market sizing)
      are correctly absent** — `article_lint.py`'s own report lists them under "approved but
      uncited," confirming the omission was deliberate (`plan-audit.md` §C), not a miss.
- [x] **No banned words.** Detector CLEAN (see the AI-tells run below); editor Pass 4 hand-check
      clean on `plus`/`so`-as-connector/`let`/`by hand`/`this article`/`objective`/`positioned as`
      outside the licensed sentence.
- [x] **Word count within ±10% of target.** Target 4,400. Prose words (linter's count, includes
      table cells) 4,712 = +7.1%. Excluding table cells, 4,316 = -1.9%. Both inside the linter's
      accepted band (3,740-5,060).
- [x] **Intro hook in the first two sentences.** *"Most diligence on remote body data starts at
      accuracy. Inside a bariatric program the sharper question is which record has to be in the
      file, dated when, and for whom to review."* — the reframe move `about-me.md` specifies.
- [x] **CTA placement per plan; type matches intent.** One CTA, Section 12, direct demo request to
      `/for-bmi-verification/` plus a sales email, no self-serve trial signal — correct for a
      BOFU-weighted, compliance-buyer hub. No second, mid-body CTA (the live page's eBook promo
      block is not carried forward — Open Item, see publisher-report.md).
- [x] **No generic AI patterns.** Zero em/en dashes verified directly (`grep -cP
      '[\x{2013}\x{2014}]'` returns 0). No triple parallelism found on read-through. Rhythm
      variation 0.57 per the detector (0.53 before editing).
- [x] **Terminology guardrails.** Zero em dashes; `objective` not used about our own conclusions;
      `reader`/`audience`/`the following sections`/`below` not used; `this article`/`this guide` not
      used outside the licensed scope note; `by hand` not used; `let` not used; `plus`/`so` not used
      as connectors; `positioned as` used exactly once, in the licensed medical-device sentence;
      presumed-reaction phrasing removed (the "audit-ready records" sentence was rewritten out of a
      concept-has-behavior shape — editor-report.md §7).
- [x] **Abbreviations (M1 + exception).** CDC, GLP-1, CHIP, CMS-0057-F, DXA, BIA, HIPAA, GDPR, BMR,
      TLS, ERISA and Federally Facilitated Exchange all expanded at first use. BMI, US, EU stay bare
      per the 2026-08-25 override. `article_lint.py` abbreviations gate: ok.
- [x] **Medical framing.** *"It is not positioned as a medical device."* — present verbatim in
      Section 9, the licensed 2026-09-02 formulation. No other "positioned as" use anywhere in the
      body (checked by grep against the pattern).
- [x] **Links on semantic anchors; third-party sources are neutral quality sites, not vendor blogs.**
      18 links, 10 distinct targets, every one on a meaning-carrying anchor phrase (no bare URLs).
      External sources: CDC (2 documents), ASMBS (4 documents/pages), CMS, PubMed Central, Johns
      Hopkins, American College of Surgeons, EurekAlert (the AAAS press wire, used as the pack's own
      locator for the JAMA Surgery figures). No vendor blog cited anywhere.
- [x] **AI-tells detector actually run** (not estimated). Command and full output below, this run,
      this session:

  ```
  $ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
      workspace/seo/articles/bariatric-hub-refresh/draft-v2-editor.md --channel article --summary

  SEO / blog article - en - 5545 words
  AI density: 0.36/1000 (budget 6.0) -> low
  VERDICT: CLEAN - check the positive side (voice, varied rhythm, a stated boundary) and ship.

  TOP SOFT MARKERS:
    2x 'facilitated' (L121)
  ```

  The two `facilitated` hits are both inside the proper noun *Federally Facilitated Exchange* and
  are not editable text. This figure (0.36/1000, CLEAN) matches the editor-report.md figure exactly
  because it is the same script run against the same file, not a re-estimate.
- [x] **Images / alt text suggestions.** No images exist in this text-only draft. See §4 below for
      suggested placements and alt text, since a content-hub article of this length normally carries
      at least one hero/OG image and one supporting visual.

**10 of 10 mechanical items pass. No blockers in this checklist.**

Note: the general publisher checklist runs to 15 line items when every guardrail sub-bullet is
counted separately; grouped as the task specifies (mechanical/keyword items, claims, banned words,
length, hook, CTA, AI patterns, terminology, abbreviations, medical framing, links, detector run,
images) that is 13 groups, all passing. Reporting round numbers only where the group is atomic.

### Content strategy checklist (`content-strategy-guidelines.md` §16)

- [x] **Article tied to the correct hub.** Hub 6 — Bariatrics → Main hub. This page is the hub
      itself, per `plan.md`.
- [x] **`action_type` respected.** `refresh-expand-in-place`, not a net-new page. The Phase 0 gate
      that would normally stop a refresh/expand row was overridden by Vadim's direct request on
      2026-09-03 (same precedent as `glp-1-market` 2026-08-28 and `online-pharmacy-bmi-verification`
      2026-08-24), and the override is recorded in the plan, not silently taken.
- [x] **Does not duplicate `existing_urls`; cannibalization guardrail honored.** The KFF
      employer-coverage figure was cut and replaced with a link to the GLP-1 Market hub, which
      already publishes that row (`plan-audit.md` §D, deletion #7). GLP-1 market economics,
      telehealth workflow, BMI-verification mechanics, body-composition methodology and multi-site
      screening consistency are each linked to their owning hub, not re-explained.
- [x] **Vertical boundary respected; sensitive-vertical scope note present.** The italic disclaimer
      sits before Section 1, verbatim from the live page. No clinical outcome of bariatric surgery
      appears anywhere, including in the Branch B "Bariatric surgery basics" FAQ block (benefits,
      side effects and pros/cons did **not** return, per the D-1 ruling in `plan-audit.md`).
- [x] **Internal links in 4 directions.** `article_lint.py`: `{up: 1, sideways: 6, down: 1, trust:
      1}`, 18 links across 10 distinct targets. Full table in §5 below.
- [x] **FAQ section present, GEO/AEO-friendly, 2-5 sentences per answer.** 16 questions across 4
      blocks (Branch B). Editor report confirms every answer is 2-4 sentences.
- [x] **"What FitXpress does NOT do" section present; no forbidden positioning claims.** Section 9
      carries seven unstacked negation statements, closing on the licensed medical-device sentence.
      No diagnosis, eligibility, treatment, underwriting, hiring or clearance claim anywhere; no
      automated fraud-detection claim (only "fraud-prevention support inside a human review
      process").
- [x] **No unsubstantiated medical / legal / underwriting / employment / clinical-trial claims.**
      The CMS-0057-F description is a regulatory-fact citation, not legal advice, and says so
      directly ("Reading the rule against a specific plan contract is work for compliance counsel").
      The compliance-posture paragraph (FX-009: HIPAA, GDPR, BAA-ready) draws on already-approved
      claim language from `proof-points.md` / `compliance.md`, not a new claim manufactured for this
      article. **Routing note, not a fail:** per this checklist item's own instruction, any
      compliance-adjacent claim belongs on a legal/product/security review pass before publish; FX-009
      is pre-approved corpus language, so this is a confirmation step, not new-claim review.
- [x] **Article owns one distinct search intent.** BOFU/GEO/sales-enablement hub intent, distinct
      from the patient-facing bariatric-surgery intent (which the "About bariatric surgery" FAQ
      block would have chased at the cost of the vertical boundary — see the D-1 decision) and
      distinct from the GLP-1 Market and Telehealth hubs' intents (cannibalization guardrail). **Not
      a failure, but worth carrying forward:** the primary keyword itself has zero measured US
      search volume (Open Item #1, `plan-audit.md` §K, §M) — the page's intent is genuine and
      distinct, it is simply not an organic-volume intent. That is a strategic fact for Vadim to
      hold, not a checklist defect.

**9 of 9 content-strategy items pass. No ❌ in the positioning / compliance / cannibalization block.
No STOP condition is triggered.**

---

## 3. Publish-time technical notes

### 3a. Sixteen `ext-claim` HTML comments must be stripped before the body reaches the CMS

These sixteen comments across ten source ids exist purely to satisfy `article_lint.py` gate 3(b),
which requires a claim marker on every prose line carrying a figure or a 4-digit year. They carry no
reader-facing content and are invisible in a rendered page, but they are literal text in the markdown
source and must not survive a raw paste into a CMS field that does not strip HTML comments on save.
**The exact ids, so the paste can be checked with a plain-text search for `ext-claim`:**

| id | Occurrences | What it backs |
|---|---|---|
| `CMS-0057-F` | 4 | The 7-day/72-hour prior-authorization rule and its scope |
| `ASMBS-2026-05-05` | 2 | The 90-95% untreated-patients figure and the "estimates draw on broader populations" note |
| `ASMBS-2026-05-05-CHHABRA` | 3 | The GLP-1-before-surgery weight-loss study (6,700 vs ~127,000 patients, the ~8% figure) |
| `CDC-DB508` | 1 | 40.3% / 9.4% obesity prevalence |
| `ASMBS-FACTSHEET-2025` | 1 | "About 1% of those who meet eligibility requirements" |
| `CDC-PCD-2023` | 1 | Self-reported BMI underestimate, 40% |
| `PMC12964095` | 1 | The 2026 narrative review on pre-operative attrition |
| `ACS-BULLETIN-2025-04` | 1 | Funk and Kurian quotes on GLP-1 as an intake gateway |
| `ASMBS-ESTIMATE-2023` | 1 | The 270,089 / 279,967 procedure-volume series and the 58.2%/23.4%/11.9% sleeve/bypass/revision split |
| `JHU-2025-JAMA-SURG` | 1 | The one-in-seven post-op GLP-1 initiation figure |

**Also strip the seven `<!-- claim: FX-xxx -->` comments** (FX-001, FX-002 x2, FX-005, FX-006,
FX-007, FX-008, FX-009). The task brief names only the `ext-claim` markers explicitly, but these are
the same category of pipeline scaffolding for the same reason (claim-traceability gate 3a) and
should not survive into the CMS either. **The CMS-ready body in §6 below has all 23 comments (16
`ext-claim` + 7 `claim:FX`) already stripped**, verified by `grep -c '<!--'` returning 0 against it.
If the CMS import instead pulls directly from `draft-v2-editor.md` on disk, re-run that grep against
whatever actually gets pasted before publishing.

### 3b. The seven `DOWN-LINK LANDING` anchors are HTML comments, not live subheadings — strip them too, but keep this table

All seven are inline markdown comments (`<!-- DOWN-LINK LANDING: ... -->`) appended to the sentence
that reserves the anchor phrase for a future link. They render as nothing today and were never
intended as visible subheadings. They should be stripped from the CMS body for the same reason as
the `ext-claim` markers (invisible pipeline scaffolding, risk of surviving as literal text in a
non-comment-aware field). **What must not be lost is the mapping**, since these mark exactly where a
future writer inserts a live link when each P1/P2 child ships:

| Section | Anchor sentence (last clause before the comment) | Target child, when it ships |
|---|---|---|
| S3 | "...the body-data half of that packet has a dedicated guide of its own." | P1: *Bariatric Pre-Authorization Documentation: What Body Data Payers May Need* |
| S4 | "...a separate guide on GLP-1 before bariatric surgery and body composition." | P1: *GLP-1 Before Bariatric Surgery: Why Body Composition and Progress Matter* |
| S5 | "...specified in a dedicated guide to the bariatric patient progress record." | P1: *GLP-1 Before Bariatric Surgery* and P1: *What Body Data Should Be in a Bariatric Patient Progress Record?* |
| S6 Stage 1 | "...treated in a guide to remote body measurement for bariatric patient intake." | P2: *Remote Body Measurement for Bariatric Patient Intake* |
| S6 Stage 2 | "...supports a hybrid bariatric care model, covered separately." | P1: *Hybrid Bariatric Care: Virtual Check-Ins With Standardized Body Data* |
| S8 | "...are handled in two further guides." | P1: *Tracking Body Changes After Bariatric Surgery Beyond Weight Loss* and P1: *What Body Data Should Be in a Bariatric Patient Progress Record?* |
| S9 | "...sit in the guides on bariatric pre-authorization documentation and the bariatric patient progress record." | P1: *Bariatric Pre-Authorization Documentation*, P1: *Patient Progress Record*, and the P2 lead magnet *Bariatric Documentation Checklist* |

This table, not the comments, is the thing to carry forward. When each child article ships, whoever
edits this hub next should search for the matching sentence above and turn its anchor phrase into a
real link, the same way the plan's own internal-link table was built.

### 3c. Data, Privacy, Security & Regulatory FAQ stays plain text

Section 10's "Compliance posture" bullet describes HIPAA, BAA-readiness, GDPR, encryption and photo
retention as prose with **no link**. This is deliberate and correct: the central Data, Privacy,
Security and Regulatory FAQ (draft at
`workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/`) is still the one remaining P0
hub gap and is not live. Do not add a link to it at CMS-entry time even if a draft URL exists
somewhere. When that FAQ publishes, this section is the one to revisit first.

### 3d. Open item for the schema, not for this page

The context pack has no `external_claims:` block equivalent to `approved_claims:`, which is why the
16 `ext-claim` comments exist as an ad hoc workaround: gate 3(b) demands a marker on every line with
a figure, gate 3(a) only resolves ids inside `approved_claims` (FitXpress-only claims), and there is
nowhere for a third-party statistic's id to formally resolve. **Recommendation, not a blocker for
this article:** add an `external_claims:` block to the context-pack schema, shaped like
`approved_claims:` (id, text, source, checked date), and teach `context-pack-builder` to emit it.
Every stats-heavy article hits this same gap; it happened to surface here because this refresh added
five ASMBS-estimate figures mid-cycle.

### 3e. FX-003, FX-004 and FX-010 are correctly absent

`article_lint.py`'s own report lists them explicitly: `approved but uncited: FX-003, FX-004,
FX-010`. Confirming here so a reviewer scanning the pack against the body does not read their
absence as an omission:

- **FX-003** (ISO 8559-1:2017, 0.40 cm session-to-session repeatability) — omitted because the page
  already carries the internal accuracy figure (S7) and the internal repeatability figure (S8) in
  two different sections, and the two-benchmark rule means the ISO figure could not sit beside
  either without failing the linter's accuracy-discipline gate. `plan-audit.md` §C.
- **FX-004** (`95%+ overall repeatability consistency`) — internal-only; not publishable under any
  condition. The publishable repeatability claim is FX-002 (`less than 1 cm`), which is the one
  used.
- **FX-010** (bariatric TAM $10-30M / SAM $2-8M) — internal deck sizing, not a customer-facing
  statistic; publishing it on a buyer-facing hub would read as a leaked pitch-deck number.

### 3f. Inventory is already correct

`brand-assets/content-strategy/published-articles-inventory.md`, row 11 and the Hub #9 narrative
block, already carry the corrected record: both `2026-06-05` (published) and `2026-07-27` (expanded
in place) dates, a note that the July expansion did **not** re-date the post, and a flag that this
refresh is "in flight." **No action needed on the inventory file itself** beyond what will naturally
follow once this article actually republishes: row 11's `updated` date needs to move to the real
CMS-publish date at that time, which is a follow-up task, not part of this package.

---

## 4. Image / alt-text suggestions

No images exist in the current draft; this is a text-only markdown deliverable. Suggested minimum
for a content-hub article of this length and BOFU weight, matching the visual load on comparable
sibling hubs (`glp-1-market`, `online-pharmacy-bmi-verification`):

| Placement | Suggested content | Suggested alt text |
|---|---|---|
| Hero / OG image | A calm, editorial image evoking a clinical intake or documentation setting (not a stock "doctor with tablet" cliché); should not depict a specific patient or imply a clinical claim | "Bariatric program staff reviewing patient intake documentation" |
| Inline, near Section 6 (workflow) | A simple 4-stage flow graphic mirroring the Stage 1-4 list (intake scan, pre-consult review, clinical consult, documentation handoff) | "Four-stage bariatric pre-qualification workflow, from remote scan to documentation handoff" |
| Inline, near Section 7 or 10 (comparison / pathway table) | The existing pathway-stage table or comparison table rendered as a lightweight visual, if the CMS template supports table-to-graphic conversion; otherwise the markdown table renders fine as-is | Not needed if left as a rendered table |

None of these are gating. The mandated tables (Use Case Summary, market-indicator table, pathway
table, comparison table) already carry the page's structural information in text form, so a missing
hero image is a polish item, not a publish blocker.

---

## 5. Internal links, four directions (verified against `article_lint.py`)

| Direction | Target | Section | Anchor |
|---|---|---|---|
| up | `https://3dlook.ai/content-hub/ai-body-data-health-hub/` | S2 | "AI body data for health hub" |
| sideways | `https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` | S3 | "compliance guide to online pharmacy BMI verification" |
| sideways | `https://3dlook.ai/content-hub/glp-1-market/` | S4 | "GLP-1 market hub" |
| sideways | `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/` | S8 | "AI in telehealth hub" |
| sideways | `https://3dlook.ai/content-hub/occupational-health-screening-software/` | S10 | "occupational health screening software hub" |
| sideways | `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/` | S12 | "Mobile body scanning for insurance underwriting" |
| sideways | `https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` | S12 | "Wellness rewards verification for employers and insurers" |
| down | `https://3dlook.ai/for-bmi-verification/` | S6, S12 | "BMI verification capability" / "Request a FitXpress demo" |
| trust | `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` | S7, S8, FAQ Q10 | "mobile body scanning accuracy framework" (present in every paragraph carrying an accuracy or repeatability figure, per the accuracy-discipline rule) |
| product | `https://3dlook.ai/technology/` | S7 | "3DLOOK technology page" |

18 total link instances across these 10 distinct targets. `{up: 1, sideways: 6, down: 1, trust: 1}`
— matches `article_lint.py`'s reported directions exactly. The **Data, Privacy, Security and
Regulatory FAQ** direction (trust) stays plain text, no link, per §3c above — the live page already
does this correctly and this refresh preserves it.

---

### About the body in §6

`§6` below carries `draft-v2-editor.md`'s body with **every** HTML comment removed and no prose
rewritten. Recomputed 2026-09-03 against the draft: **31 markers on 29 comment lines**, two lines
carrying two markers each. That is **16** `ext-claim`, **8** `claim:FX` and **7**
`DOWN-LINK LANDING`. An earlier version of this package said "23 total" and "7 `claim:FX`"; both
were wrong, and the second disagreed with the lint report, which counts 8 (`FX-001`×1,
`FX-002`×2, `FX-005`, `FX-006`, `FX-007`, `FX-008`, `FX-009`).

**Verification for whoever pastes into the CMS.** Against **everything after the `§6` heading**,
plain-text search for each of these four and expect no hits: the HTML comment opener, `ext-claim`,
`claim:` and `DOWN-LINK`. All four were confirmed clean at the time of writing. Two notes on
method: scope the search to below the `§6` heading, because this paragraph names the strings and
will match itself; and search for the strings rather than comparing marker counts, since two lines
held two markers each.

`word_count` (prose, per `article_lint.py`, table cells included): **4,712**. The frontmatter
`title` and `meta_description` in `draft-v2-editor.md` are **superseded by §1 above**. Use the
recommended meta values at CMS entry, not the working title in the draft.

---

## 6. Article (CMS-ready body)

---

# Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams

Most diligence on remote body data starts at accuracy. Inside a bariatric program the sharper question is which record has to be in the file, dated when, and for whom to review. Bariatric pre-qualification runs on that record, and so does patient progress tracking after the procedure. US programs carry a structural mismatch between intake demand and surgical capacity, and the verification stack most of them still run was built for a slower era: a self-reported weight, a tape measurement taken in clinic, a BMI computed during the consult.

Patients also arrive differently now. Many reach the consult after a year on a glucagon-like peptide-1 (GLP-1) medication that did not reach their goal, expecting a pathway that already knows their numbers. Two things changed in 2026 that the intake stack was not built for: a federal prior-authorization rule with a 7-calendar-day standard decision window for impacted payers, and a patient population whose current BMI and qualifying BMI history have come apart.

**Use Case Summary**

| Field | Detail |
| :-- | :-- |
| **Industry** | Bariatric surgery centers, hospital bariatric programs, multi-site surgical networks, metabolic and obesity clinics |
| **Problem** | Eligibility confirmed late, consult slots spent collecting measurements, pre-auth packets built from notes a payer reviewer cannot date |
| **Solution** | A guided two-photo remote scan completed before the consult, returning a structured body-data record to the program |
| **Outputs** | BMI, 80+ body measurements, body composition estimates, capture timestamp, capture-quality outcomes |
| **Role** | Supporting evidence for program and payer review, not eligibility or pre-authorization decisioning |
| **Business value** | Higher consult-to-procedure conversion, fewer measurement-only visits, earlier documentation start, records comparable across the pathway |

The people who own that problem are bariatric program directors, directors of operations, pre-authorization coordinators and medical directors. What they answer for does not move on measurement accuracy alone. It moves on whether the right dated record exists before the review starts.

**Disclaimer.** *Mobile body scanning solutions described here do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions. They produce body measurement and composition data intended as supporting evidence within decisioning workflows operated by licensed bariatric programs and their compliance and payer counterparts.*

## 1. The bariatric intake gap: eligibility confirmed late, documentation assembled after the consult

The demand side has moved in one direction for years. The [most recent clinical-measurement cycle from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/nchs/products/databriefs/db508.htm), running from August 2021 to August 2023, shows 40.3% of US adults have obesity and 9.4% have severe obesity, at a BMI of 30 or higher and 40 or higher respectively.

Very little of that population reaches a procedure. The American Society for Metabolic and Bariatric Surgery (ASMBS) puts surgery's reach at [about 1% of those who meet eligibility requirements](https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf), and its [release of 5 May 2026](https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/) reported that 90-95% of patients with severe obesity received no treatment during the study period.

Two problems sit under the standard intake design, where the patient self-reports a weight, the program books the consult, and the measurement happens at the appointment. The first is the quality of the number at the top of the funnel. CDC researchers reported in Preventing Chronic Disease that [self-reported BMI underestimated the prevalence of severe obesity by 40%](https://www.cdc.gov/pcd/issues/2023/23_0005.htm), at 5.3% on self-report against 8.8% after bias correction in 2020 data. Where BMI is the trigger for procedure-specific criteria, a self-reported value is a placeholder that still has to be verified.

The second problem is attrition, and the published range is itself the argument. A [2026 narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/) reports pre-operative dropout as high as 60%. One cohort in the same literature reports 22.25%. Canadian programs with mandatory pre-operative pathways complete at roughly 36% to 76%, US programs at roughly 39% to 70%, and one single-centre series reported 8.9% before the pandemic. Attrition depends on program design and on how it is counted. That spread is a stronger case for a standardized intake record than any single figure inside it.

Consult slots, operating-room days and pre-authorization coordinators are all finite. When intake demand rises against unchanged surgical capacity, the bottleneck moves upstream into the verification and documentation steps that decide whether a slot becomes a procedure or a deferral. Every verification step that requires an in-person appointment is also a point where a patient can leave the pathway. That is the part of the bariatric intake workflow a remote body-data layer supports.

## 2. Short answer: what structured body data contributes, and what still decides

**Short answer.** Bariatric pre-qualification is the intake step in which a program assesses whether an inquiry meets its own eligibility criteria and a payer's medical-necessity criteria, before a full clinical consult is scheduled. A bariatric patient progress record is the dated, comparable body-data series a program keeps from before the procedure through long-term follow-up. Structured remote body data supplies the measurement inputs for both. The eligibility determination and the pre-authorization decision are made elsewhere, by the licensed program and by the payer.

*Structured* carries an operational meaning here. The same guided capture sequence runs every time, the output is machine-readable, each capture carries a timestamp, and the records stay comparable across patients and across time points.

For obesity care teams the division of labour is the point: the measurement is standardized upstream, and the judgment stays downstream with the people licensed to make it. Bariatrics is one workflow among several that run on the same capture, and the [AI body data for health hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) maps the others.

## 3. Why now (1): prior authorization runs on a 7-calendar-day clock

The payer clock changed on 1 January 2026. Under the [Centers for Medicare and Medicaid Services Interoperability and Prior Authorization Final Rule (CMS-0057-F)](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f), impacted payers must decide standard prior authorization requests within 7 calendar days and expedited requests within 72 hours. They must give a specific reason for each non-drug denial, whatever channel the request arrived through, and they must publicly report prior-authorization metrics annually, with initial reporting due 31 March 2026.

The rule's reach belongs in the same breath as the rule. CMS-0057-F applies to Medicare Advantage organizations, Medicaid and Children's Health Insurance Program (CHIP) fee-for-service programs and their managed-care plans, and Qualified Health Plans on the Federally Facilitated Exchange. It does not cover every commercial plan governed by the Employee Retirement Income Security Act. Medicare fee-for-service does not use prior authorization for bariatric procedures at all. How much of a program's volume sits on this clock depends on its payer mix. Reading the rule against a specific plan contract is work for compliance counsel.

Window length changes what the documentation has to do. A long review window absorbs a request for more information; seven calendar days leaves no room for one. When the record supporting medical necessity is assembled only after the payer asks for it, a missing timestamped BMI record stops being a delay and becomes a denial that now carries a published reason. Published reasons accumulate, which makes the pattern of a program's incomplete submissions legible over a year.

The packet itself has not changed. A standard bariatric pre-authorization submission typically carries documented BMI history, confirmation of comorbidities, prior weight-loss attempts, participation in a supervised diet program where the plan requires it, psychological evaluation outcomes, and a body-measurement record. What changed is how much of that has to be complete and verifiable on the first pass. Prior authorization documentation is now the tightest constraint on a bariatric program's calendar, and the body-data half of that packet has a dedicated guide of its own.

None of this shortens the payer's own clock. A program controls one variable, whether its first submission is complete, and standardized capture is what makes that variable repeatable across coordinators. The mechanics of verifying a BMI figure remotely, including live capture and pose validation, are set out in the [compliance guide to online pharmacy BMI verification](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

## 4. Why now (2): GLP-1 changed the shape of the intake funnel

The clock tightened while the funnel feeding it changed shape. Three indicators carry the current volume picture, and two measurement systems produce them. The systems do not reconcile, and keeping them apart separates a defensible read from a number no source supports.

| Indicator | Figure | What it indicates |
| :-- | :-- | :-- |
| US procedure volume, 2023 | 270,089 procedures, down about 3.5% from 279,967 in 2022 ([ASMBS estimate of bariatric surgery numbers](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/)), a national estimate built from the Bariatric Outcomes Longitudinal Database, accreditation-program data, the National Inpatient Sample and outpatient estimations. The series ends at 2023. | The national volume anchor. |
| Change in surgery use, 2022 to 2024 | Metabolic bariatric surgery use down 34.1% while GLP-1 receptor agonist use rose 140.4% over the same period ([JAMA Surgery, 13 May 2026](https://www.eurekalert.org/news-releases/1127781)), measured inside one insured claims cohort. | A rate of use within that cohort. Absolute counts in the same cohort move about 7.3% lower. Not a national count. |
| Cohort procedure counts | 40,265 (2022), 42,615 (2023), 37,339 (2024), 33,429 (2025), all from the same claims cohort. | The decline continued into 2025 inside that cohort. |

The national estimate and the claims cohort are not comparable, and ASMBS says so directly: its own estimates draw on broader patient populations and additional datasets than the study used. One figure is a rate of use inside an insured population; the other is a national count.

Volume is only half of what moved. In the [American College of Surgeons Bulletin in April 2025](https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/), Luke Funk, a bariatric surgeon at the University of Wisconsin-Madison, described GLP-1 medications as "the initial gateway for a lot of patients" who later move toward surgery. Marina Kurian, clinical professor of surgery at NYU Langone Health, said in the same piece that "Most of my colleagues around the country are seeing an increase in new consults coming for surgery."

A wider and more heterogeneous intake funnel is feeding surgical capacity that has not grown, which raises the value of a structured pre-qualification step ahead of the consult. The patient at the top of it arrives with a longer treatment history and a firmer expectation that the program can say where they stand.

Coverage economics, prescribing growth and drug-class comparison sit on the [GLP-1 market hub](https://3dlook.ai/content-hub/glp-1-market/). The medication pathway now runs in both directions, which is the subject of a separate guide on GLP-1 before bariatric surgery and body composition.

## 5. Why now (3): current BMI and qualifying BMI history have come apart

The sharpest operational change of 2026 shows up in patient files. An [ASMBS release on 5 May 2026](https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/) reported a study by Chhabra and colleagues at NYU Grossman School of Medicine, presented at ASMBS 2026, drawing on Epic Cosmos electronic health records from 2019 to 2025. It compared 6,700 patients with prior GLP-1 use, 2,395 of them gastric bypass and 4,315 sleeve gastrectomy, against roughly 127,000 patients without prior GLP-1 use, followed for three years. Patients lost about 8% of total body weight on GLP-1 medications before surgery. Total loss reached more than 25% after gastric bypass and about 20% after sleeve gastrectomy.

For an intake coordinator the consequence lands on the file. A patient who has already lost about 8% of body weight on a GLP-1 may arrive at consult with a current BMI below a payer's threshold while their documented history still meets it. Eligibility then turns on dated, verifiable BMI history, and one measurement taken in the room no longer carries the case by itself. What a payer's threshold is, and whether a given history meets it, stay questions for the program and the plan. Bariatric surgery requirements, at this stage of the workflow, are documentation requirements: which measurements exist, when each was taken, and whether a reviewer can trace them to a capture.

That is a records problem before it is a clinical one. A serial scan record carries its own date and its own capture conditions. A tape measurement typed into a free-text note carries neither, and a reviewer at the payer cannot confirm when it was taken or how. Read against the 7-calendar-day standard window, a history reconstructed after a request for information arrives too late.

The pathway also runs the other way: for some patients a medication becomes a bridge to surgery later. An intake record that begins when a patient first enters obesity care is therefore more useful than one that begins at the surgical consult. What belongs in that record is specified in a dedicated guide to the bariatric patient progress record.

## 6. The bariatric pre-qualification workflow: moving the measurement step to intake

Pre-qualification is where the consult-to-procedure conversion math changes fastest, and the redesign is one move: the body-measurement step goes from stage three back to stage one.

- **Stage 1. Remote scan at intake.** After the patient submits the baseline questionnaire, the program sends a scan link and the patient completes the guided two-photo capture on their own smartphone, typically the same day. The program receives a structured record containing BMI, body measurements and body composition estimates. Remote bariatric intake carries its own workflow questions, treated in a guide to remote body measurement for bariatric patient intake.
- **Stage 2. Pre-consult review.** A coordinator or clinical reviewer checks the output against the program's eligibility thresholds and any program-specific intake criteria before the consult is scheduled. Patients who clearly meet criteria move into a clinical-evaluation consult. Patients who fall outside them are routed into medical-management or referral pathways without occupying a surgical consult slot. The underlying [BMI verification capability](https://3dlook.ai/for-bmi-verification/) supplies the signal for that review. Where a program pairs virtual check-ins with in-person visits, the same capture supports a hybrid bariatric care model, covered separately.
- **Stage 3. Clinical consult.** The visit opens with the body data already in the patient's record, which moves the conversation to history, comorbidities, surgical risk and patient education. The slot becomes a clinical evaluation instead of a measurement-collection event.
- **Stage 4. Documentation handoff.** The record that supported the triage decision is available to the pre-authorization coordinator from the start of the case. On a 7-calendar-day standard clock, available from the start is the difference between a first-pass submission and a resubmission.

The mechanism here is not clinical decision-making. The scan does not determine whether a patient is medically eligible for surgery, and the bariatric program makes that determination after evaluation. What the scan supplies is a structured, verifiable body-data signal the program uses to triage which consult slots are opened, in what order, and with what supporting record already attached. Each stage above names the person who reviews.

## 7. Where FitXpress fits across the bariatric pathway

FitXpress by 3DLOOK is a mobile body-scanning solution built around a guided two-photo flow. The patient takes a front and a side smartphone image, results return in under 45 seconds, and the output covers 80+ body measurements along with BMI, basal metabolic rate (BMR), body-fat percentage, and lean and fat mass, with no specialized hardware involved.

Three properties matter for this use case. Outputs are structured and timestamped at capture, which allows a record to be placed in time and compared later. Capture happens remotely on the patient's own phone, which removes the appointment slot as the verification gate. The third is the compliance posture. Its diligence questions belong with the pilot evaluation.

One accuracy figure applies here, and it comes from one specific comparison. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. The useful diligence question is accurate enough for which decision: against which reference method, under which capture protocol, for which population, and at what tolerance the workflow can absorb. Consult-slot triage and a payer packet do not set the same tolerance. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) states the conditions that make any such figure meaningful.

| Pathway stage | What the capture contributes |
| :-- | :-- |
| Inquiry | Early body data captured outside the clinic |
| Pre-consult | Supports pre-qualification review and consult-slot triage |
| Pre-authorization | Provides structured, timestamped documentation inputs |
| Procedure preparation | Establishes a baseline body-data record |
| Post-surgery follow-up | Tracks body measurement and composition change over time |
| Long-term monitoring | Supports remote progress review without a clinic visit |

One capture asset, read repeatedly across the bariatric patient journey, replaces the fragmented manual measurements that today sit in separate parts of the program's workflow. The technology behind the capture is described on the [3DLOOK technology page](https://3dlook.ai/technology/).

## 8. Patient progress tracking after the procedure

The scan captured before surgery is the reference the follow-up scans are compared against. Because every capture runs the same guided sequence, a scan taken three months after the procedure is structurally comparable to the baseline instead of standing as a separate ad-hoc measurement.

For longitudinal use, repeatability is the property that carries the comparison. Accuracy describes how close one measurement sits to a reference; repeatability describes whether two scans of the same body, weeks apart, produce numbers a program can compare. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. How that was measured, and why it answers a different question from accuracy, is set out in the [accuracy framework article](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). Weight estimation is the weaker output and belongs in the record with its limit stated: it carries a ±3.5% average error margin as a software estimate, and a calibrated scale remains the reading where a protocol requires one.

Body composition after bariatric surgery moves on a different timeline from scale weight. The same weight can sit on top of different body-composition profiles, and that difference matters for patient counselling and for program-level outcome reporting. It also matters to the multidisciplinary team around the patient, in nutrition, behavioural health and surgical follow-up.

The post-procedure window increasingly holds a pharmacotherapy component alongside surgical recovery. [Johns Hopkins researchers reporting on a JAMA Surgery analysis](https://publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs) found that roughly one in seven bariatric patients initiate GLP-1 therapy after surgery. A baseline scan along with serial follow-up scans gives the program a body-data series that stays visible across the whole window, independent of medication adherence. Remote follow-up workflows are covered on the [AI in telehealth hub](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/).

A side-by-side comparison of the baseline capture and a recent scan is also a counselling artifact, often more useful than a single weight number on a chart, and it stays supporting evidence inside the program's monitoring workflow.

What belongs in a bariatric patient progress record is a short list. The components are a dated BMI, waist and hip circumference, body composition estimates, and a capture-quality outcome for each scan. Each entry carries its date and its capture conditions. The cadence follows the program's monitoring protocol. Tracking body changes beyond weight loss, and the fuller specification of a progress record, are handled in two further guides.

## 9. What improves operationally, and what FitXpress does not do

In the pre-authorization packet the change is narrow and concrete. The file gains a structured body-data record: a capture timestamp, the capture-quality outcomes recorded in session, and the measurement set in machine-readable form, consistent across patients because the sequence does not vary between them. Serial captures on one timeline, a baseline at intake, a second before submission, a third before the procedure, produce comparable records instead of three measurements taken three different ways. Whether those records are audit-ready follows from how the data was captured, and a human reviewer still reads them.

The anti-manipulation controls support that posture without completing it. Capture runs live in session instead of accepting a camera-roll upload, pose validation runs in real time, and clothing detection is built in. Those controls reduce the risk of a manipulated capture. They leave in place the need for capture instructions, retake logic and deployment-specific thresholds. They are fraud-prevention support inside a human review process.

**What FitXpress does not do in a bariatric program.** It does not determine medical or surgical eligibility. It does not diagnose. It does not replace clinical evaluation. It does not make the pre-authorization decision. It does not guarantee compliance or an approval. It is not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods. It is not positioned as a medical device.

The payer-facing documentation set behind those records, and the checklist that follows from it, sit in the guides on bariatric pre-authorization documentation and the bariatric patient progress record.

## 10. Comparison, buyer fit, and what to confirm before a pilot

Manual measurement and guided capture sit under different constraints. The comparison that matters runs workflow area by workflow area.

| Workflow area | Manual measurement at the consult | Guided scan-based capture |
| :-- | :-- | :-- |
| Appointment slot | Required; the measurement and the slot are one event | Not required; capture runs before, during or after a clinical event |
| Cross-operator comparability | Varies with operator, tool, technique and participant preparation | Same capture and processing sequence each time, comparable across patients and time points |
| What a payer reviewer can verify | A note stating a measurement was taken | A record carrying a capture timestamp and capture-quality outcomes |
| Reuse across pre-qualification, pre-auth and post-op | Each stage collects its own measurement | One capture asset, read at several stages |
| What it depends on | Trained staff, protocol adherence, in-person attendance | Patient smartphone access, capture instructions, retake logic, deployment thresholds |

Manual measurement at the consult stays where the protocol requires it, and where a clinician needs a hand on the anatomical landmark. For obesity care teams the comparison resolves into a division of labour, and neither method replaces the other.

The fit is clearest at bariatric surgery centers, hospital programs, multi-site surgical networks and metabolic and obesity clinics. Directors of operations, medical directors, vice presidents of patient access and chief operating officers own the measures at stake: consult-to-procedure conversion, late-stage disqualifications and cancellations, pre-auth cycle time, and staff time per packet. Cross-site consistency is the whole argument at a multi-site network, and the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/) carries its employer-facing version.

Three evaluation considerations belong in the diligence.

- **Compliance posture.** FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts, supports Business Associate Agreement execution, follows General Data Protection Regulation (GDPR) principles, encrypts data at rest in Amazon Web Services S3 and in transit over Transport Layer Security, processes no personal identifiers, and deletes photos immediately after processing or within a configurable retention window. A dedicated FitXpress privacy and regulatory FAQ, not yet published, holds the fuller detail.
- **Validation population.** The internal validation population included participants aged 16 to 78, heights of 150 to 220 cm, weights of 38 to 210 kg, and participants from the US and Europe. Performance outside this scope has not been characterized. A severe-obesity intake population includes patients above that weight range, worth checking early in evaluation.
- **Validation strength.** 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study.

Those three are the floor to confirm with any vendor handling patient body data before a pilot begins.

## 11. Frequently asked questions

### Pre-qualification and pre-authorization documentation

**What is bariatric pre-qualification?**
Bariatric pre-qualification is the intake step in which a program checks an inquiry against its own eligibility criteria and a payer's medical-necessity criteria before a full clinical consult is scheduled. Eligibility determination stays with the licensed program.

**How can bariatric programs pre-qualify patients remotely?**
The program sends a body-scan link at intake and the patient completes the guided capture on their own smartphone. BMI, body measurements and body composition estimates reach the program before the consult, where clinical evaluation still happens.

**What body-data documentation do payers commonly require in a bariatric pre-authorization packet?**
A standard packet typically carries documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation where the plan requires it, psychological evaluation outcomes and a body-measurement record. A capture timestamp is what makes the measurement record verifiable.

**How long do payers have to decide a bariatric prior authorization?**
Under CMS-0057-F, operational since 1 January 2026, impacted payers must decide standard requests within 7 calendar days and expedited requests within 72 hours. Impacted means Medicare Advantage, Medicaid, CHIP and Qualified Health Plans on the Federally Facilitated Exchange, and not every commercial plan under the Employee Retirement Income Security Act. Medicare fee-for-service uses no prior authorization for bariatric procedures.

**Why does documented BMI history matter more when a patient has been on a GLP-1?**
Patients in one 2026 study lost about 8% of total body weight on GLP-1 medications before surgery. A patient who arrives that much lighter may show a current BMI below a payer's threshold while their documented history still meets it. That reading belongs to the program and the payer.

**How can programs reduce wasted bariatric consult slots?**
Moving body-measurement capture upstream, into a remote scan completed before the appointment, keeps consult slots focused on clinical evaluation. Patients outside program criteria are routed into medical-management or referral pathways.

### Patient progress tracking

**What body data belongs in a bariatric patient progress record?**
A dated BMI, waist and hip circumference, body composition estimates, and a capture-quality outcome for each scan. The set and the cadence follow the program's monitoring protocol.

**Why is weight alone not enough for bariatric progress tracking?**
The same weight can sit on top of different body-composition profiles, and one number does not describe a post-bariatric trajectory. Composition tracked alongside weight shows lean-mass and fat-mass change.

**How can bariatric programs monitor patients remotely after surgery?**
A baseline scan before surgery, followed by serial scans on the patient's own smartphone, gives the program a body-data series visible across the post-procedure window. The monitoring protocol sets the intervals.

**How is a follow-up scan compared with the baseline?**
A follow-up scan uses the same guided sequence and returns the same data structure as the baseline. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, and the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out how that was measured.

### Scope and governance

**Is scan data used to make eligibility or pre-authorization decisions?**
No. The scan produces body measurement and composition data used as supporting evidence inside workflows the licensed program and its payer counterparts operate. Eligibility and pre-authorization decisions are made by people, against those parties' criteria.

**Who reviews the scan data?**
A coordinator or clinical reviewer reads the output against the program's intake criteria before a consult is scheduled. The pre-authorization coordinator works from the same record, and the medical director and the payer's reviewer hold the decisions.

**What does FitXpress not do in a bariatric program, and can it replace in-clinic measurement?**
It does not determine medical or surgical eligibility, diagnose, or make the pre-authorization decision. It does not guarantee compliance or an approval. It is not equivalent to DXA, bioelectrical impedance analysis or a calibrated scale where a protocol requires those methods. In-clinic measurement stays where the protocol requires it.

### Bariatric surgery basics

**What is bariatric surgery?**
Bariatric surgery, also described as metabolic and bariatric surgery, is a category of surgical procedures that alter the digestive system as part of treating severe obesity and related conditions. Suitability and procedure choice are decisions for the program and the patient.

**What are the main types of bariatric surgery?**
Sleeve gastrectomy and Roux-en-Y gastric bypass are the two most commonly performed procedures in the United States. [ASMBS's national estimate](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/) puts sleeve gastrectomy at 58.2% of the 270,089 procedures recorded for 2023, gastric bypass at 23.4% and revisions at 11.9%, on the estimation methodology behind the annual totals.

**What are common program and payer requirements?**
Each program and plan sets its own list, and the common items are documented BMI history, comorbidity confirmation, prior weight-loss attempts, supervised diet participation and psychological evaluation outcomes. At intake the question is documentary: what exists, dated when, verifiable by whom.

## 12. Next steps and related reading

See how FitXpress can support pre-qualification, pre-authorization documentation and post-procedure progress tracking inside a bariatric program. A useful first step is mapping one payer's packet requirements against what the file already holds on the day of the consult. [Request a FitXpress demo](https://3dlook.ai/for-bmi-verification/) or contact sales@3dlook.ai.

Related reading:

- [AI body data across health programs](https://3dlook.ai/content-hub/ai-body-data-health-hub/)
- [GLP-1 market growth and patient progress tracking](https://3dlook.ai/content-hub/glp-1-market/)
- [AI in telehealth: workflows, privacy and remote body data](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [Online pharmacy BMI verification compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)
- [Occupational health screening software](https://3dlook.ai/content-hub/occupational-health-screening-software/)
- [Mobile body scanning for insurance underwriting](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/)
- [Wellness rewards verification for employers and insurers](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/)

---

## STOP — awaiting Vadim's approval

`status: ready_for_review`, not `approved_for_publish`. Per repo history
(`project_mvb_publish_package_status.md`), that gate could never pass mechanically; Vadim's ask for
this refresh plus his approval of the digest (text and meta together) is the actual publish gate.
This package does not invent an approval state, and no one should treat `ready_for_review` as
sufficient to paste into the CMS. Once Vadim approves the text and meta together, he or the CMS
operator publishes manually, preserving `datePublished` per §0.2 above.
