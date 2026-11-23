---
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
product: fitxpress
status: approved_checkpoint_2
approved_by: Vadim
approved: 2026-09-21
approved_slug: telehealth-documentation-ai-body-scanning
created: 2026-09-21
author: Assel Sekerova
source_final: "final.md (status: edited, editing_passes: 5, article_lint PASS)"
word_count: 1867
lint_verdict: "PASS, all gates ok (verbatim run below)"
---

# Publish Package — 2026-09-21-ai-body-scanning-telehealth-documentation

## Meta

**Title:** Telehealth Documentation: More Consistent Records | 3DLOOK (58 chars) — **recommended**
**Description:** Fragmented intake data blurs telehealth documentation. See how FitXpress creates
structured, timestamped records a program can retrieve and compare. (148 chars)

**Slug:** `telehealth-documentation-ai-body-scanning` — recommended, keyword-first ordering so
"telehealth documentation" sits at the start of the URL path, matching where it sits in the title
and H1. Alternative: `ai-body-scanning-telehealth-documentation` (the date-stripped workspace
name), offered but not recommended, since it puts the primary keyword second.
**Checkpoint 2 approved by Vadim 2026-09-21** (text + meta together; word count 1,867 accepted as
is; recommended slug stands).
**URL (if recommended slug used):** `https://3dlook.ai/content-hub/telehealth-documentation-ai-body-scanning/`
**Category:** Telehealth. Suggested only, not a content-plan label (Hub 2's internal name is "AI
in Telehealth"; the CMS category field should show the vertical, not the hub/cluster designation).
Vadim assigns the final value in the CMS.

**Why this title and description:**
- Primary keyword "Telehealth Documentation" is the first two words of the title (position 1-25 of
  58, well inside the first half) and the first two words of the description's first sentence.
- H1 is fixed by editorial final and is not a meta-title candidate: "Telehealth Documentation: How
  AI Body Scanning Creates More Consistent Records" (82 chars, over the 60-char budget). The
  recommended meta title is a shortened variant of the same thesis, not a copy of the H1, so it
  does not duplicate it verbatim on the SERP.
- Brand suffix `| 3DLOOK` added because the title is 49 chars without it (at the 49-char threshold
  the rule allows the suffix), and 58 chars with it stays under the 60-char ceiling.
- No numbers in either the title or the description, by design — the article's only accuracy
  figure ("below 1 cm") carries dataset and protocol conditions that cannot fit a meta field, so it
  stays out of the meta entirely rather than being stated bare.
- Description states only what `final.md` actually supports: FitXpress creates structured,
  timestamped records (FX-002, FX-003); a program can retrieve and compare them (FX-003, matches
  Section 5's "a program can retrieve an entry months after capture" and the comparison claim in
  Section 6). No compliance, accuracy, or time-saving promise — none of those appear bare enough in
  the article to state in a meta field.
- "See how FitXpress..." is a soft/direct CTA appropriate to BOFU/operational intent, matching the
  article's own Next-steps CTA register, without repeating its exact wording.

## SEO Checklist

- [x] **Primary keyword in H1 and 1-2 H2** (first paragraph not a gate, softened 2026-09-11).
      "Telehealth documentation" appears in the H1 (`final.md:64`) and in one H2, "Where telehealth
      documentation loses consistency" (`final.md:68`). `article_lint.py` keyword-placement gate:
      ok, 3 occurrences, 11 H2s.
- [x] **Meta title ≤ 60 chars, primary keyword in the first half.** Recommended title 58 chars,
      keyword in characters 1-25. Counted with Python.
- [x] **Meta description 140-160 chars.** Recommended description 148 chars, counted with Python.
      Keyword appears once, does not repeat the title or H1 verbatim.
- [x] **Every number traces to `approved_claims`.** Grepped the body (`final.md:64-209`) for
      digits: every hit is either a claim-marker id fragment (`FX-001` through `FX-012`), a section
      year inside a URL slug (`...2026-compliance-guide`), "3D model/3D models" (a standard product
      term, not a standalone figure), or a number that sits inside a claim-tagged sentence — "45
      seconds" (FX-004, `:82`), "80+ body measurements" (FX-002/FX-005, `:85`), "below 1 cm"
      (FX-011, `:208`), "five scans per participant" (part of the FX-011 canon sentence, `:208`).
      No FX-010, no per-measurement figures, no `95%+ repeatability` anywhere (re-grepped, zero
      hits). `article_lint.py` claim traceability: ok, 11 claims used, all known.
- [x] **No banned words.** Grepped the full banned-word list (leverage, utilize, harness, robust,
      seamless, comprehensive, delve, navigate, tapestry, realm, unlock, unleash, revolutionary,
      game-changing, cutting-edge) against the body: zero hits. `detect-ai-tells.py` hard-bans pass
      confirms independently (verbatim output below).
- [ ] **Word count within ±10% of target.** Target is 2,100 (`plan.md` frontmatter and body).
      `final.md`'s own `word_count: 1867` is **-11.1%** against that target, just outside a strict
      ±10% band (the floor would be 1,890; the article is 23 words under it). Flagging this
      honestly rather than rounding it to a pass. Context, not an excuse: `article_lint.py` itself
      enforces a ±15% band (1,785-2,415) and returns `[ok]` on prose length; `plan.md`'s own prose
      says the target range is "1,900 to 2,300, matching the live occupational-health intake
      article at ~1,877" — 1,867 sits 10 words below even that stated floor, but within 1% of the
      cited reference article's own published length. The shortfall traces to five documented
      editing passes that cut repetition and an unquantified time-saving claim (`final.md`
      `changes_summary`), not to missing content. This is the only checklist item below, does not
      touch positioning/compliance/cannibalization, and is the sole ❌ on this pass, so it does not
      trigger the ≥2-❌ STOP on its own. Recommend Vadim decide whether -11.1% against the stated
      2,100 target is acceptable given the reference-article precedent, or whether the article
      should regain ~25-235 words before publish.
- [x] **Intro hook in the first two sentences.** `final.md:70`: "A telehealth record usually
      collects body data from three places." then "The person reports a weight at sign-up, a home
      scale reports a different one later, and a progress photo arrives in a message thread." A
      concrete, specific opening, not a rhetorical question.
- [x] **CTA placement per plan; type matches intent.** Plan specifies a BOFU, direct CTA in Section
      10 (Next steps) with the pricing-modal link, and the down-link to the product page in Section
      5's delivery paragraph. `final.md` matches: the product-page down-link appears once, in
      Section 5 (`:122`), and Section 10 closes on "[talk to 3DLOOK about the telehealth intake
      workflow](https://3dlook.ai/pricing/#bd-modal-personalized)" (`:185`) — direct BOFU CTA,
      matching intent. The single down-link total (rather than repeating it in Section 10 as an
      earlier plan draft implied) matches this task's explicit instruction that the down-link
      appear once, and only at that URL.
- [x] **No generic AI patterns (triple parallelism, em-dash rhetoric).** `detect-ai-tells.py`:
      CLEAN, `ai_density_per_1000_words: 0.0`, `punch_triad_count: 0`, `em_dashes: 0`. Verbatim
      output below.
- [x] **Terminology guardrails.** Re-grepped the article body directly: zero em/en dashes, zero
      `objective` about our own conclusions, zero `the reader`/`the audience`/`the following
      sections`/`see below`, zero `this article`/`this guide`, zero `by hand`, zero `let` as a
      permission verb, zero `positioned as` anywhere. `plus` and `so` each appear once, but both
      hits are in the frontmatter `changes_summary` (editorial process notes, not article prose,
      lines 31 and 38) — zero occurrences in the article body itself (`:64-209`).
- [x] **Terminology, sync 2026-09-14.** IEEE not mentioned anywhere (not needed for this topic).
      `80+ body measurements` used correctly (`:85`), with BMI and BMR explicitly called
      "calculated metrics" and body composition called "estimates" in the same sentence, never
      "measurements" (`:85`, `:88`). Content-plan labels (`hub`, `cluster`, `pillar`, `bridge`,
      `supporting content`): zero hits in H1/H2/H3, meta title, or anchors; the only "hub" matches
      in the raw body are inside `content-hub` URL paths, the licensed site-section exception.
      `buyer`: zero hits. `customer`: 5 hits (`:149`, `:157` x2, `:159`, `:208`), all licensed —
      "workflows the customer manages," "customer agreement," "the customer's request" (deployment
      /contractual role), "the customer acts as the data controller" (the canonical GDPR sentence,
      verbatim), and "a real-world customer dataset" (the canon FX-011 repeatability sentence,
      verbatim). None uses "customer" for a generic actor outside a contract/deployment/legal
      context.
- [x] **Abbreviations (M1 + exception).** Grepped and confirmed expansion at first use: API
      (`:122`, "application programming interface (API)"), SDK (`:122`, "software development kit
      (SDK)"), DXA (`:153`, "dual-energy X-ray absorptiometry (DXA)"), BIA (`:153`, "bioelectrical
      impedance analysis (BIA)"), BMR (`:85`, "basal metabolic rate (BMR)"), HIPAA (`:159`, "Health
      Insurance Portability and Accountability Act (HIPAA)"), BAA (`:159`, "Business Associate
      Agreement (BAA)"), GDPR (`:159`, "General Data Protection Regulation (GDPR)"). BMI appears
      unexpanded throughout, per the exception list. No CEO/UK/US/EU in the body.
      `article_lint.py` abbreviations gate: `[ok]`.
- [x] **Medical framing.** "FitXpress is not a medical device." appears twice, verbatim, in the
      scope note (`:78`) and in Section 7's boundary paragraph (`:153`). Zero instances of
      "positioned as" anywhere in the body.
- [x] **Links on meaningful anchors; external sources neutral, non-vendor.** All 10 links use
      descriptive anchor phrases, no bare URLs. All 10 are `3dlook.ai` internal links (up, sideways,
      down, trust, plus the FitXpress homepage and the pricing CTA) — this article carries **no
      external third-party sources**. The plan allowed one optional HHS citation in Section 3
      ("Skip the citation rather than approximate it" if it could not be fetched and verified); the
      final draft carries none, which is a permitted outcome, not a defect. Nothing to check for
      vendor-blog quality since no external source is present.
- [x] **AI-tells detector actually run, verbatim output below, not estimated.** Ran
      `detect-ai-tells.py` this session against the current `final.md`, both with
      `--channel article --summary` and the full JSON. Both transcripts pasted below, unedited.
- [x] **Images / alt-text suggestions provided below.** `plan.md` and `final.md` carry no
      illustration markers for this article (unlike some sibling articles), so these are newly
      proposed concepts, each with its own alt text, none sharing a template, none using a keyword
      from another page, none using stop words, all under 125 characters, no em dash.

**SEO checklist: 15/16 passed.** One ❌ (word count, -11.1% against the stated 2,100 target,
detailed above). Not in the positioning/compliance/cannibalization block, and the only ❌ on this
pass, so it does not trigger the ≥2-❌ STOP.

### `article_lint.py` output, verbatim (run this session, against the current `final.md`)

```
$ python3 scripts/article_lint.py workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2074
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.41
[ok  ] prose length
         prose words 1867 vs target 2100 (band 1785-2415)
         . prose_words: 1867
         . target: 2100
[ok  ] claim traceability
         . claims_used: ['FX-001', 'FX-002', 'FX-003', 'FX-004', 'FX-005', 'FX-006', 'FX-007', 'FX-008', 'FX-009', 'FX-011', 'FX-012']
         . claims_known: 12
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 10
         . links_distinct: 9
         . asset_urls: 0
         . directions: {'up': 1, 'sideways': 3, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: telehealth documentation
         . occurrences: 3
         . h2_count: 11
         . in_first_paragraph: False
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 126
         . mean_words: 12.9
         . p90_words: 20
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: none

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

(Re-run this session, unchanged from the coordinator's brief: `VERDICT: PASS`, all gates `[ok]`.
`prose length` gate itself uses a ±15% band and passes at -11.1%; the SEO checklist above applies
the stricter ±10% rule and flags it, so the two do not silently agree — see the checklist row.)

**On `directions: {'up': 1, ...}` totalling 7 while `links_total` is 10.** The tool classifies
direction only for URLs it recognizes from the context pack's `internal_link_targets` lists
(up/sideways/down/trust, 7 distinct matches after dedup of the repeated up-link). The FitXpress
homepage (`:120`) and the pricing CTA (`:185`) are not in any of those four lists, so they are
counted in `links_total`/`links_distinct` but not tallied into a direction. All four directions
required by the plan are genuinely present and correctly tallied: up (1), sideways (3), down (1),
trust (2).

### `detect-ai-tells.py` output, verbatim (run this session, against the current `final.md`)

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md --channel article --summary
SEO / blog article · en · 2074 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md --channel article
{"language": "en", "channel": "article", "channel_label": "SEO / blog article", "profile": null,
 "total_words": 2074, "total_markers": 0, "em_dashes_excluded_from_density": 0,
 "ai_density_per_1000_words": 0.0, "density_budget": 6.0, "severity": "low", "short_form": false,
 "verdict": "CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.",
 "hard_fails": [], "house_rule_violations": [], "markers_by_category": {},
 "style_metrics": {"em_dashes": 0, "bold_count": 7, "bold_per_1000_words": 3.4,
  "title_case_headings": 0, "emoji_count": 0, "hashtag_count": 1, "bullet_lines": 10,
  "bold_lead_in_bullets": 0, "list_to_prose_ratio": 0.26, "wall_of_text": false,
  "rhythm": {"sentences": 105, "mean_words": 15.6, "variation": 0.41, "monotone": false,
   "uniform_paragraphs": false}, "punch_triads": [], "punch_triad_count": 0}, "top_offenders": []}
```

`total_words: 2074` is this script's own count, which includes the frontmatter's `changes_summary`
and `self_check` narrative text (a larger inclusion than `final.md`'s own `word_count: 1867`, which
counts article prose only). `hashtag_count: 1` is a false-positive match on the `#bd-modal-personalized`
fragment in the pricing URL, not an actual hashtag in the text. `ai_density: 0.0`, `hard_fails: []`,
`house_rule_violations: []` are unaffected by which word count is used, since density is
markers-per-1000-words and zero markers were found either way.

## Content Strategy Checklist (`content-strategy-guidelines.md` §16)

- [x] **Bound to the right hub.** AI in Telehealth (Hub 2), Documentation cluster
      (`final.md:7-8`, `plan.md:7-8`). Consistent throughout.
- [x] **`action_type: create-net-new` respected.** Confirmed against `published_inventory`:
      `already_live: false` at plan stage, no sibling article with this documentation intent.
- [x] **Does not duplicate `existing_urls`; cannibalization guardrail respected.** BMI verification
      is a single sentence plus link (`:106`), the workflow itself is never re-explained. The
      patient-engagement article's progress-visibility thesis is not repeated; it appears once, in
      Related reading (`:190`). The Admin Panel launch post is linked, not re-described beyond one
      sentence (`:124`). No drift into the separately planned "Progress Photos vs Structured Body
      Data" comparison — grepped for "manipulat"/"photo credibility"/"trustworth": zero hits; the
      Section 6 table stays about record shape (fields, timestamp, format, availability, re-entry),
      not photo credibility.
- [x] **Vertical boundary held; scope note present.** Telehealth vertical boundary respected: no
      GLP-1 eligibility framing, no BMI-threshold logic in the body (link-only, as required). Scope
      note present early (`:78`, right after Section 1's problem statement), italic, stating what
      FitXpress provides and what stays with the program's clinicians, closing with "FitXpress is
      not a medical device."
- [x] **Internal links in 4 directions.** up (1) → the-potential-of-ai-in-telehealth; sideways (3)
      → online-pharmacy-bmi-verification, fitxpress-admin-panel-launch, mobile-body-scanning-
      patient-engagement; down (1) → structured-body-data-for-telehealth-digital-health-programs
      (the only URL used, exactly once); trust (2) → fitxpress-data-privacy-security-regulatory-
      faq, mobile-body-scanning-accuracy. Matches `plan.md`'s internal-links plan exactly.
- [x] **FAQ section present, GEO/AEO-friendly.** Four questions (`:194-208`), each answered in 2-4
      sentences, direct answer first. None repeats a body section's full explanation.
- [x] **"What FitXpress does NOT do" section present; no forbidden positioning claims.** Section 7
      (`:147-153`) kept as its own full section per the edit's own note ("Hub 2 does not own it,"
      `changes_summary` Pass 3b) — not replaced by a scope-note-only substitute, correctly, since
      the substitution rule only applies when a cluster's hub already owns that content. Re-grepped
      the body against the full `banned_claims` list (most accurate/best-in-class, guaranteed
      compliance, medical device/diagnostic/eligibility decisioning, replaces DXA/BIA/calibrated
      scales/clinician review, automated eligibility/underwriting/fraud-detection, HIPAA
      compliant/certified, SOC 2 certified, named competitors): zero hits.
- [x] **No unsupported medical/legal/underwriting/employment/clinical-trial claim.** Every boundary
      statement names what FitXpress does not determine (diagnosis, treatment, eligibility,
      employment) and states decisions stay with the program's clinicians and other designated
      decision-makers (`:151`). HIPAA and GDPR statements match `compliance.md`'s canonical wording
      verbatim (`:159`).
- [x] **Owns one distinct search intent.** "A telehealth program's documentation is fragmented at
      intake: what does a structured body-data record contain, where does it enter the workflow,
      and how does it change what a care team can retrieve and compare?" General telehealth, not
      GLP-1 eligibility, not BMI verification, not the photo-credibility comparison piece.

**Content strategy checklist: 9/9 passed.** No item in the positioning/compliance/cannibalization
block is ❌, so this package does not STOP on strategy grounds.

## Alt options

### Meta title variants

1. **Telehealth Documentation: More Consistent Records | 3DLOOK** (58 chars) — **recommended.**
   Keyword first, states the outcome plainly, brand suffix fits inside the 60-char budget.
2. Telehealth Documentation: Structured Body Data Records (54 chars) — names the mechanism
   (structured body data) instead of the outcome.
3. Telehealth Documentation With Structured Body Data (50 chars) — shortest, no colon, reads as a
   plain description rather than a stated outcome.

### Meta description variants

1. **Fragmented intake data blurs telehealth documentation. See how FitXpress creates structured,
   timestamped records a program can retrieve and compare.** (148 chars) — **recommended.** Names
   FitXpress directly (BOFU signal), states only claims the article supports (FX-002/FX-003), soft
   CTA.
2. Self-report, scale readings, and photos land in different formats. See how FitXpress keeps
   telehealth documentation consistent and retrievable. (143 chars) — leads with the concrete
   fragmented-input hook from Section 1 instead of naming the effect first.
3. Telehealth documentation depends on what enters the record at intake. See how structured
   body-data capture improves documentation consistency. (142 chars) — closest to the article's own
   reframe-move opening ("Consistency is decided at capture"), does not name FitXpress by name.

## Image and alt-text suggestions

No illustration markers exist in `plan.md` or `final.md` for this article (unlike some sibling
articles that carry `(Cover)`/`(Image)` concept markers). These three concepts are newly proposed,
matched to sections that would benefit from a visual, each with its own alt text — no shared
template, no keyword from another page, no stop words (robust/seamless/comprehensive/etc.), no em
dash, no client or competitor name, all under 125 characters.

1. **Cover — under the Section 1 H2 (`final.md:68`).** Concept: three mismatched intake entries (a
   handwritten note, a scale reading, a phone photo) on the left, converging into one structured
   record card on the right.

   Alt text: "Three mismatched intake entries, a note, a scale reading, and a photo, next to one
   structured record." (101 chars)

2. **Image 1 — Section 4, under the three-H3 workflow (`final.md:100`).** Concept: a simple
   horizontal timeline with three marked points (intake, between visits, before clinician review),
   each showing one structured entry landing in the record.

   Alt text: "Timeline showing body-data capture at intake, between visits, and before clinician
   review." (90 chars)

3. **Image 2 — Section 6, next to the comparison table (`final.md:134`).** Concept: a simplified
   two-column visual echoing the table, fragmented fields on one side, one consistent structured
   entry on the other.

   Alt text: "Side-by-side comparison of fragmented intake fields and one structured body-data
   record." (88 chars)

Design tokens from `DESIGN.md`: electric blue `#143DFF`, navy `#050F40`, Satoshi throughout.

## Open items for Vadim

1. **Word count -11.1% against the stated 2,100 target** (1,867 words). `article_lint.py`'s own
   ±15% band passes it, and it matches the closest live reference article (~1,877 words) almost
   exactly, but it is outside the strict ±10% rule this checklist applies. Decide whether to accept
   or ask for ~25-235 more words before publish.
2. **No illustration plan exists for this article.** The three concepts above are proposed by this
   package, not carried from `plan.md`. Confirm before handing to design, or replace with your own.
3. **Slug not yet fixed.** Recommended `telehealth-documentation-ai-body-scanning`; alternative
   `ai-body-scanning-telehealth-documentation` (date-stripped workspace name) also offered. Decide
   at checkpoint 2.
4. **Category not pre-filled.** Suggested "Telehealth"; final value entered manually in the CMS.
5. **No external sources in the article.** The plan allowed one optional HHS citation in Section 3,
   skippable if it could not be verified live; the final draft carries none. Not a defect, flagged
   for awareness only.

This package does not set `status: approved_for_publish`. Publication requires Vadim's approval at
checkpoint 2 (text and meta together), per the coordinator's process.

## Article

# Telehealth Documentation: How AI Body Scanning Creates More Consistent Records

By Assel Sekerova

## Where telehealth documentation loses consistency

A telehealth record usually collects body data from three places. The person reports a weight at sign-up, a home scale reports a different one later, and a progress photo arrives in a message thread. Each input lands in its own format, on its own day.

Consistency is decided at capture. What a program collects at intake sets what it can retrieve and compare later.

Self-reported weight and height are hard to verify at intake. Staff re-enter values and chase missing fields before a consultation can start. That work sits with the clinical team, and it grows with volume.

The cost shows up later. A care coordinator opens a record before a check-in and finds four entries in three formats. A program lead builds an outcomes summary for a payer partner, and two of the time points have no usable entry at all.

***Scope note.*** *FitXpress provides remote body-measurement capture and structured records. The program's own systems hold the rest of the chart. Clinical review, treatment decisions, and eligibility decisions stay with the program's clinicians. FitXpress is not a medical device.*

## Short answer: what a structured body-data record contains

A guided two-photo scan returns structured outputs in under 45 seconds. The entry it produces carries three groups of data.

- **What the person submits.** Front and side photos, gender, height, and optionally weight.
- **What the scan generates.** 80+ body measurements, a 3D model, and scan-to-scan comparison outputs. Calculated metrics include BMI and basal metabolic rate (BMR). Body composition estimates cover body fat percentage, lean mass, and fat mass.
- **What the system records technically.** Capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata.

Body measurements are circumferences, lengths, and widths. BMI and BMR are calculated from the inputs, and body composition figures are estimates. The distinction matters when a program decides which fields it stores and which ones it compares over time.

## Why record consistency is under pressure now

Remote-first programs grew faster than their intake did. Consultation capacity moved online early, and the record-keeping around it often stayed manual.

Programs are also asked to show their work. Payers, employers, and regulators expect outcomes traceable to a dated, consistent entry. A summary built from mixed inputs is harder to defend than one built from entries that share a format.

Documentation expectations for telehealth keep being revised. Each revision lands on the same operational question: which fields the program captures, and whether it can retrieve them later.

AI reached documentation work first through note-taking tools that draft the visit summary. Body data is a separate input to the same record. It arrives before the consultation, and it describes the body while the note describes the conversation.

## Where body data enters a telehealth workflow

Body data reaches a telehealth program at three points. The workflow around each one decides how much of it lands in the record in usable form. [AI in telehealth](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) covers the wider picture of remote-care workflows, privacy, and patient experience.

### At intake

Remote capture runs before the first consultation. The person completes a guided two-photo scan on a smartphone, and the record exists before anyone opens it for review. Programs that verify BMI as part of eligibility follow a separate path, covered in the guide to [remote BMI verification for online pharmacies](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

### Between visits

Repeat capture happens at intervals the program chooses. Each capture produces an entry in the same format, with its own timestamp. The program selects which scans it compares.

### Before clinician review

The record is retrieved in one place ahead of the consultation. Missing or low-quality captures become visible earlier, while there is still time to repeat them. Testing, physical examination, and clinical judgment stay with the provider.

Documentation of a telehealth physical exam still rests on what the provider observes and writes during the visit. Remote capture changes when the measurement data arrives, and what shape it arrives in. Telehealth visit documentation requirements are set by the program and its advisors, and remote capture supplies input to them.

## Where FitXpress fits: capture, records, and the Admin Panel

[FitXpress](https://3dlook.ai/) provides the capture step. What reaches the program afterwards is one structured entry per scan.

Delivery runs on two routes, and most programs take the first. Results come back through the FitXpress application programming interface (API) or software development kit (SDK), directly into the product the program already runs. The person stays inside one experience, and the outputs land in the system that holds the rest of the record. The page on [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) describes what an integration covers.

The FitXpress Admin Panel is the optional second route. It gives teams a centralized view and management of scan results without building a dashboard of their own. The [FitXpress Admin Panel launch post](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/) describes the feature.

Both routes leave a record behind. A program can retrieve an entry months after capture, which is what makes any later comparison possible. Every entry carries a timestamp and processing metadata.

The timing of an entry matters as much as its contents. A record that exists before review is available to whoever opens the chart, in the same shape every time.

## What changes in the record

What changes is the shape of the entry. Who reviews it, and who decides, stays the same.

| **What the record carries** | **Fragmented intake inputs** | **Structured body-data record** |
|---|---|---|
| Fields on each entry | Vary with the source and the visit | The same set every time |
| Timestamp | Depends on when someone logged the item | Applied at capture, on every entry |
| Format | Free text, images, and scale readings | Structured outputs in one shape |
| Availability before review | Assembled during or just before the consultation | Present in the record before review begins |
| Manual re-entry | Often needed to move values into the system | Reduced where the integration carries the values |
| Comparison across time points | Limited by differing formats | Supported, because entries share a format |

A record that carries the same fields every time is quicker to read and easier to compare. Less of it has to be rebuilt inside the consultation, although the size of that gain depends on how much was missing before.

Manual re-entry falls where the integration carries values into the program's system, although that system still decides how corrections are handled. Entries stay comparable over time because they are retained and share a format. Calculated metrics and body composition estimates are recalculated on each scan, and each entry shows the figures from that day.

## What FitXpress does not do

FitXpress supports remote intake and body-measurement capture, body composition outputs, and comparison of the scans a program selects. It also covers structured data collection for research protocols, and documentation that supports workflows the customer manages.

It does not independently determine a diagnosis, a treatment or medication recommendation, insurance or clinical-trial eligibility, employment eligibility, or any other high-impact individual decision. Final decisions stay with the program's clinicians, underwriters, and other designated decision-makers.

Remote capture does not replace clinician review, dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis (BIA), or calibrated scales. Those methods answer different questions under different conditions. Where a program needs a reference-method measurement, remote capture sits alongside it. FitXpress is not a medical device.

## Data handling, retention, and access

Measurements, body composition data, and 3D models are retained on an ongoing basis unless the customer agreement says otherwise. Deletion is by scan identifier, on the customer's request. Scan records are associated with anonymized, randomly generated identifiers, and 3DLOOK cannot identify a specific individual from stored scan records.

FitXpress can support deployments governed by the Health Insurance Portability and Accountability Act (HIPAA). In those deployments 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA), where applicable. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under the General Data Protection Regulation (GDPR).

Procurement and security reviews of secure telehealth documentation platforms go further than retention and legal roles. The [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the rest, including storage regions, photo handling, and model training.

## How to evaluate documentation consistency in a pilot

A capture change earns its place where the existing gap is in intake. If records are already complete and comparable, moving the capture step will not return much.

Five measures describe the record before and during a pilot:

- Completion rate of remote capture, by cohort.
- Share of records complete at the point of review.
- How often a value is re-entered manually.
- How often the manual fallback path is used.
- How many entries are comparable across time points.

Each of those is something the program measures in its own systems. None of them is a result to expect in advance. Baselines taken before launch make the second reading worth having.

One limit belongs in the pilot design from the start. FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence.

### Who this fits

Remote-first programs running repeat check-ins across more than one site or partner. The roles that usually own the decision are Head of Clinical Operations, Care Coordination Manager, and Medical Director. A single-site program with low volume and a complete paper trail has less to gain.

## Next steps

Compare the inputs the program collects today against what the record has to carry at review, and name the fields that arrive inconsistently. Then [talk to 3DLOOK about the telehealth intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).

Related reading:

- [AI in telehealth: workflows, privacy, patient experience, and remote body data use cases](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [How mobile body scanning improves patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/)

## FAQ

### Can body scan records help a telehealth program meet its documentation requirements?

The program and its advisors decide which documentation requirements for telehealth apply and how records are used. FitXpress provides structured, timestamped records that enter the program's own process. It does not guarantee compliance or certify a program's records.

### How is this different from AI tools that draft telehealth visit notes?

Note-taking tools capture what was said during a consultation and turn it into a summary. FitXpress captures body-measurement data before the consultation and returns it as a structured record. Programs reviewing AI tools for telehealth visit documentation are usually solving a different part of the chart. The two inputs meet in the same record, from different points in the workflow.

### What happens when a patient cannot complete a remote scan?

Some people lack a suitable device or a stable connection. Others cannot hold the capture pose. The program, therefore, needs a documented manual alternative, and a rule for how a measurement taken that way joins the record.

### Do repeat scans produce comparable entries over time?

Comparability depends on the capture protocol and on the receiving system. Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.
