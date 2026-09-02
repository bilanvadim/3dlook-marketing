---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
product: fitxpress
status: ready_for_review
revision: 3
created: 2026-09-02
checkpoint: 2 (final text + meta), awaiting Vadim
---

# Publish Package: AI Body Data for Wellness Platforms (Hub #8) — Revision 3

This is the checkpoint-2 package for revision 3, produced after Review 2 (13 numbered items +
6 softenings, `review-2.md`) and `review-2-decisions.md` (decisions file wins on conflict, per
its own frontmatter). It supersedes `v2/publish-package.md`. Review 2 is sentence-level: no
section moved, no heading changed, no keyword re-decided, `plan.md` revision 2 stands untouched.
The one substantive change at the publisher layer is the meta description (Review 2 item 12).
Everything below was checked directly against `final.md` revision 3, not asserted from the plan
or carried forward from v2 without re-verification.

## Meta

**Title (unchanged):** AI Body Data for Wellness Platforms | 3DLOOK — **44 characters by direct
count.** `review-1-decisions.md` §A1 recorded 48 for this same string; that was a counting error,
caught and corrected by the revision-2 publisher, and reconfirmed here by an independent count.
Primary keyword `Wellness Platforms` starts at character 18 of 44 (index 17, 0-based), inside the
first half.

**Description (recommended, NEW per Review 2 item 12):** Measured body data gives a wellness
platform a repeatable progress signal the scale misses, supporting personalization and
engagement. See what to evaluate. — **156 characters** (counted, not estimated). Contains
`wellness platform` verbatim exactly once, singular. Contains **zero** instances of `corporate` or
`corporate wellness platform`. No em dash. Does not repeat the title. Hook (a progress signal the
scale misses) + value (personalization and engagement) + soft CTA (see what to evaluate), matching
this hub's Hub-level intent (no hard demo ask).

This narrows what `review-1-decisions.md` §A1 recorded: the meta description was the phrase's
second and last home. Review 2 item 12 is right that metadata frames the whole hub, and the
strategy deliberately broadened past corporate wellness, so the phrase now has **exactly one**
home — the "Corporate wellness" subsection in the body (`final.md` line 127, confirmed by direct
grep: 1 occurrence of the exact string `corporate wellness platform` in the entire article). This
follows the direction Vadim chose at §A1 rather than reversing it, per decisions §D item 12, so it
is applied without escalating.

**URL slug:** `ai-body-data-wellness-platforms` (unchanged)
**Category:** Content Hub, Health / Wellness (Hub #8 main hub)
**Word count:** **2,790 words** — this is the prose count from `final.md`'s own frontmatter
(`word_count: 2790`), independently confirmed by `scripts/article_lint.py`'s `prose_words: 2790`.
Target is 2,650 ±150, i.e. 2,500–2,800: 2,790 sits inside that band, 40 words below the top edge.
**Do not confuse this with the ai-tells detector's own `detector_words: 3,119`** below — the
detector counts markup (table cells, claim-marker HTML comments, TODO comments) as words, so its
total is not a length-gate number.

## Gate: `scripts/article_lint.py`, verbatim

Actually run, this session, against `final.md` revision 3:

```
$ python3 scripts/article_lint.py workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/final.md --report

workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 3119
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.53
[ok  ] prose length
         prose words 2790 vs target 2650 (band 2252-3047)
         . prose_words: 2790
         . target: 2650
[ok  ] claim traceability
         . claims_used: ['FX-001', 'FX-002', 'FX-003', 'FX-006', 'FX-007', 'FX-008', 'FX-009', 'FX-011', 'FX-014']
         . claims_known: 16
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 14
         . links_distinct: 8
         . directions: {'up': 1, 'sideways': 4, 'down': 1, 'trust': 1}
[ok  ] keyword placement
         . keyword: wellness platform
         . occurrences: 11
         . h2_count: 11
[ok  ] abbreviations (M1)

--- shape (descriptive, not gated) ---
prose words 2790 across 11 H2 sections
      232  What AI body data means for wellness platforms
       93  Where body data creates value: summary table
      313  Progress visibility beyond scale weight
      255  Personalization using goals, starting points, and tr
      277  Engagement and coaching
      271  Practical wellness-platform workflow
      344  What to evaluate in a body-data provider
      209  Where FitXpress fits
      114  Boundaries and related hubs
      364  Frequently asked questions
       97  Where to go next
  links 14 total, 8 distinct, by direction: {'up': 1, 'sideways': 4, 'down': 1, 'trust': 1}
  primary keyword 'wellness platform': 11 occurrences
  claim markers 17: {'FX-001': 1, 'FX-002': 1, 'FX-003': 2, 'FX-006': 3, 'FX-007': 4, 'FX-008': 3, 'FX-009': 1, 'FX-011': 1, 'FX-014': 1}
  approved but uncited: FX-004, FX-005, FX-010, FX-012, FX-013, FX-015, FX-016
  term group corporate: total 15  (employer 2, insurer 2, reward 6, corporate wellness 4, incentive 1, plan-year 0)
  term group broad: total 62  (consumer wellness 1, lifestyle 3, nutrition 4, habit 4, digital wellbeing 1, coaching 11, wellness app 5, member 33)

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

`term group corporate: corporate wellness 4` counts the substring `corporate wellness` (the
header, the topic sentence, and the subsection body), not the exact phrase `corporate wellness
platform` — a direct grep for that exact three-word phrase returns exactly 1 hit (line 127), which
is the number this package tracks per Review 2 item 12. `term group broad: total 62` against
`corporate: total 15` (ratio ~4:1) is consistent with v2 and confirms the audience-broadening
strategy from Review 1 was not undone by Review 2's sentence-level edits.

## SEO checklist (14/15 — images planned but not produced, same shape as v2)

- [x] **Primary keyword placement.** `wellness platform` opens paragraph 1 of the intro ("A
  wellness platform has limited visibility...", line 23) and opens section 1's first sentence
  ("For a wellness platform, AI body data means...", line 31). H1 (line 21) carries the plural
  form ("...for Wellness Platforms"). Two H2s carry the term: section "What AI body data means for
  wellness platforms" (line 29, plural) and "Practical wellness-platform workflow" (line 87,
  hyphenated). Verified counts: 6 singular exact-match instances, 5 plural instances, 11 total —
  unchanged from v2, since Review 2's edits were length-neutral wording changes, not keyword
  changes (decisions §E).
- [x] **Meta title** 44 chars (corrected from the 48 wrongly recorded at §A1), primary keyword
  starts at char 18 of 44, inside the first half. Unchanged this revision.
- [x] **Meta description** 156 chars, inside the 150-160 window. **Changed this revision** per
  Review 2 item 12: `corporate wellness platform` removed, `wellness platform` used instead. See
  Meta section above for the full rationale and two alternates below.
- [x] **Numbers traceable to approved claims.** Citations present: FX-001 (×1), FX-002 (×1),
  FX-003 (×2), FX-006 (×3), FX-007 (×4), FX-008 (×3), FX-009 (×1), FX-011 (×1), FX-014 (×1) —
  matches `final.md` frontmatter `claims_verified` exactly, unchanged from v2. **FX-010 and
  FX-016 are absent by design**, not an oversight: FX-010 was cut per Review 1 item 15 (the
  training-data enumeration, "not essential to this hub"), FX-016 per Review 1 item 16 (the
  2-centimetre tolerance / repeatability-outranks-accuracy framing, replaced with the
  five-condition accuracy question). FX-004, FX-005, FX-012, FX-013, FX-015 also absent, none
  required.
- [x] **No banned words.** Detector `hard_fails: []`. Manual grep for leverage/utilize/harness/
  robust/seamless/comprehensive/delve/navigate/tapestry/realm/game-changer/revolutionize/
  cutting-edge/disrupt/"unlock the power"/"struggling with"/"it's no secret": 0 hits.
- [x] **Word count** 2,790 prose words against target 2,650 ±150 (2,500-2,800). Inside the band,
  40 words below the top edge. `article_lint.py`'s own (wider, ±15%) band also passes:
  2,252-3,047.
- [x] **Intro hook**, first two sentences (line 23): "A wellness platform has limited visibility
  into physical progress between check-ins. What it usually holds is a self-reported entry and a
  scale reading." This is the reframed opening from Review 2 item 1 — the intro now states three
  distinct limitations (self-reported entries, scale weight, repeatable body data) instead of
  treating the first two as sharing one limitation, which was the factual error the reviewer
  flagged as most important.
- [x] **CTA placement and type.** Evaluation CTA at the end of "Where FitXpress fits" (line 123:
  "Teams that want to see the capture flow... can start with FitXpress for connected and digital
  fitness"), immediately after the boundary paragraph, matching the plan. Layered CTA in "Where to
  go next" (lines 151-159), 3 routes: soft (AI body data hub + Beyond BMI), evaluation (FitXpress
  product page), employer/insurer (Wellness Rewards Verification). Intent is Hub, so no single
  hard demo ask — unchanged from v2, Review 2 did not touch CTA placement.
- [x] **No generic AI patterns.** Detector: `hard_fails: []`, `rhythm_variation: 0.53` (want
  > 0.35, improved from v2's 0.51). Manual read found no negative-parallelism, no triple-adjective
  parallelism, no "not just X, it's Y" shapes. 0 em dash anywhere in the body (`grep` confirmed).
- [x] **Terminology guardrails.** 0 em dash. `objective` appears twice (lines 43, 45), both inside
  the summary-table header/cell "wellness objectives" — a business-goal noun, not a claim about
  our output, same reading as v2. 0 reader/audience/following-sections/see-below. 0 "this
  article"/"this guide" ("this hub" appears once in the scope note, the one permitted
  self-reference). 0 "by hand". 0 "let". 0 "plus" as a benefit-connector. 0 "we"/"our"/"you"/
  "your". 0 corrective negation ("X, not Y"). 0 corrective "rather than". One "so" (line 31,
  "timestamped so two check-ins can be compared") is a mechanical purpose clause, not a
  benefit-connector; detector's `house_rule_violations: []` treats it as a pass. **`positioned
  as` appears exactly once** ("It is not positioned as a medical device," line 121) — the
  licensed medical-device exception, confirmed the only instance in the article.
- [x] **Abbreviations.** DXA (not DEXA) — 2 instances (lines 121, 139), expanded at first use in
  section "Where FitXpress fits" ("Dual-energy X-ray absorptiometry (DXA)"), bare in FAQ Q3. BMR,
  GDPR, API, SDK, BIA, HIPAA each expanded once at first use, bare thereafter. BMI, US left bare
  per the commonly-known exception. 0 instances of "DEXA" anywhere in the article.
- [x] **Medical framing.** "It is not positioned as a medical device." (line 121) — the reviewer
  lists this among what is now working well (final bullet list, review-2.md). Stated directly and
  unchanged from v2.
- [x] **Links on meaningful anchors.** 14 links, 8 distinct targets, 0 bare URLs, all canonical
  trailing-slash `3dlook.ai` URLs. Direct count against `final.md`: `wellness-rewards-verification…`
  ×3, `fitxpress/for-connected-and-digital-fitness` ×2, `beyond-bmi-business` ×2,
  `ai-in-fitness-industry` ×2, `ai-body-data-health-hub` ×2, `the-potential-of-ai-in-telehealth`
  ×1, `mobile-body-scanning-accuracy` ×1, `how-to-measure-body-composition` ×1 = 14 total, 8
  distinct. No third-party citations (open item, see below), so no vendor-blog risk.
- [x] **Detector actually run**, by this agent, directly, via `scripts/article_lint.py --report`
  (wraps `detect-ai-tells.py`; full verbatim output above): `detector_words: 3119` ·
  `ai_density: 0.0` · `verdict: CLEAN` · `rhythm_variation: 0.53`. This is a real execution in this
  session, not a reasoned estimate — the failure mode flagged in this agent's own brief (2026-08-25
  incident, both seo-editor and seo-publisher skipped the run and guessed 0.6/1000) does not apply
  here.
- [ ] **Images / alt text: planned, not produced.** Changed from v2: the plan now exists (three banners, placements, alt text, constraints and rejected candidates, see the Illustration plan section and `illustrations.md`), and the alt text is written. What is missing is the assets. **Two dependencies, in order:** the Figma blog-banner exports must land in `brand-assets/past-posts/_figma-exports/blog-banners/` (Vadim), then design produces three `.webp` files. The checklist item stays open until the files exist and are referenced in `final.md`.

## Content strategy checklist (9/9, one item fulfilled via a documented, plan-approved deviation)

- [x] Correct hub: Wellness Platforms (Hub #8), main hub row from `content-plan.md`. Unchanged.
- [x] Action type honored: `create-net-new`, gate passed at Phase 0. Unchanged; Review 2 made no
  structural change.
- [x] Does not duplicate `existing_urls`; cannibalization guardrail held. Wellness Rewards keeps
  the verification workflow (3-point subsection then link); Beyond BMI keeps the BMI argument
  (summarized then linked). No vendor comparison table, 0 named vendors.
- [x] Vertical boundary held, and **tightened this revision** (Review 2 item 4): grouping members
  by measured starting point is no longer actively recommended. Section "Personalization" (line
  73) now reads "the same records aggregate into body-data trends for reporting: participation and
  change across appropriately defined cohorts... Segmentation is a separate question, and measured
  body characteristics are a weak default basis for it, particularly where the population is a
  workforce." This matters specifically because the hub includes employee wellness applications,
  which is the reviewer's stated reason.
- [x] Internal links in all four directions: **up** `ai-body-data-health-hub` (×2, line 155 and
  159 area) · **side** `wellness-rewards-verification…` (×3), `beyond-bmi-business` (×2),
  `ai-in-fitness-industry` (×2), `how-to-measure-body-composition` (×1),
  `the-potential-of-ai-in-telehealth` (×1) · **down**
  `fitxpress/for-connected-and-digital-fitness` (×2) · **trust**
  `mobile-body-scanning-accuracy` (×1). 14 links total, 8 distinct targets, all canonical
  trailing-slash form. All four directions and the full count are on the "must NOT change" list
  in decisions §E, verified directly against `final.md` rather than assumed.
- [x] FAQ section present: 6 questions, answers 2-3 sentences each, GEO/AEO-shaped. Two answers
  changed in wording this revision (Q5 privacy language per item 11; Q6 cadence softened per item
  8, "feeling progress" assertion dropped), question count and structure unchanged.
- [x] **"What FitXpress does NOT do" — deliberate, plan-approved deviation, not a checklist
  failure, unchanged from v2.** It exists as no standalone FAQ question or footer block.
  Content-strategy §8/§14 wants it; the no-repeat structure rule from Review 1 item 5 (echoed by
  Review 2 item 5, which removed a third repetition of the program-access boundary from
  "Boundaries and related hubs") treats a separate section as unwanted repetition. The boundary is
  stated in full in "Where FitXpress fits" (line 121: "It is not positioned as a medical device.
  FitXpress does not diagnose conditions or screen for them...") and reached from the FAQ through
  Q3 (replacement: DXA/BIA/scale) and Q4 (decisioning: program access). `plan.md` records this
  explicitly: "The review wins for this article." No positioning claims banned by §8 found
  anywhere in the text.
- [x] No unsupported medical, legal, underwriting, employment or clinical-trial claims. HIPAA
  appears exactly once (line 113), as something to ask about, not a certification claim. GDPR
  stated as the approved controller/processor sentence, verbatim. SOC 2 not mentioned. **Privacy
  wording tightened this revision** (Review 2 item 11 / decisions §C2): "FitXpress does not
  receive names, contact details, or other direct identifiers that connect the scan with a
  specific individual" replaces the looser "No personal identifiers are processed," in both
  section "What to evaluate in a body-data provider" (line 113) and FAQ Q5 (line 146) — this is a
  precision gain against the same approved source (`compliance.md`), not a new claim, and it
  correctly acknowledges that body photos and derived measurements can be personal data even
  without a direct identifier attached.
- [x] Owns one distinct search intent: "what should a wellness platform do with body data, and
  what changes if it does" (commercial-informational, pre-vendor-shortlist), unchanged from the
  Phase 0 gate.

## Review 2 closure table

The reviewer's own framing: "substantially stronger and close to publishable," ready for
"final proofreading and illustration planning" once these corrections land. This is the direct
answer to that review, item by item, sourced from `review-2-decisions.md` §D (decisions file
wins on any wording difference from `review-2.md`).

| # | Item (short) | Disposition | New wording in `final.md` |
|---|---|---|---|
| 1 | Opening logic: scale weight IS comparable over time | **Applied — the most important factual correction.** Self-reported entries, scale weight and repeatable body data now carry three distinct limitations instead of two sharing one | Line 23: "Self-reported entries get estimated or rounded... A scale reading compares cleanly against last month's. Its limitation is a different one: one number compresses every kind of body change into a single direction of travel. Repeatable body data adds a third record..." |
| 2 | Engagement outcome claim | **Applied — sentence removed, mechanism only.** This closes open item 1 (no third-party source needed, because the claim that needed one is gone) | Line 79: "creates an additional structured check-in... The record it leaves is also what coaching and content selection can draw on." No outcome/retention claim remains |
| 3 | Unsupported comparative in personalization | **Applied verbatim to the reviewer's wording.** Ranking claim removed, limitation kept | Line 69: "A scan carries no information about motivation, food environment, or the time a member can commit, and each of those also influences outcomes." |
| 4 | Grouping members by measured starting point | **Applied, and taken further than v2.** Turned into aggregated reporting plus an explicit segmentation caveat, because the hub covers employee wellness | Line 73: "...body-data trends for reporting: participation and change across appropriately defined cohorts... measured body characteristics are a weak default basis for it, particularly where the population is a workforce." |
| 5 | Repeated program-access boundary (3 places) | **Applied.** Deleted from "Boundaries and related hubs"; a boundary sentence remains in "Where FitXpress fits" and the fuller explanation remains in FAQ Q4 | Line 121 (short form) and line 143 (FAQ Q4, fuller form); confirmed absent from lines 125-129 |
| 6 | Compliance formulation | **Applied verbatim.** "Leaves compliance where it was" (too broad) replaced with continuing responsibility | Line 121: "The platform remains responsible for its program rules and applicable compliance requirements." |
| 7 | Automated-program contradiction | **Applied.** Removed the self-contradiction of "judgement stays with a person" inside a fully automated program | Line 83: "In automated programs the same record can support content selection and the progress display, while the platform stays responsible for the rules and recommendations it applies. Human review can be specified for reward, access, or other consequential decisions." |
| 8 | Cadence guidance | **Applied and softened,** in both the body and the FAQ; the FAQ's "feeling progress" assertion dropped | Line 97: "A four-to-twelve-week interval can be a practical starting point, depending on the program goal, the expected magnitude of change, and capture conditions." Line 148-149 (FAQ Q6) no longer asserts an emotional outcome |
| 9 | "similar time of day" | **Applied — removed everywhere, verified absent from every approved source.** `time of day` returns 0 hits in `final.md`, `product-info/`, `about-me.md`, and the context pack | Lines 63 and 94: "the same guided pose and similar capture conditions" |
| 10 | Server-side retention | **Applied.** Retention made conditional, matching data minimisation | Line 92: "which outputs are retained or made available to authorized program teams." |
| 11 | Privacy wording | **Applied, reviewer's precise version, in both places, split to avoid a stacked negation** | Line 113 and line 146: "FitXpress does not receive names, contact details, or other direct identifiers that connect the scan with a specific individual. Photos are not used to train the model." (two sentences, one boundary each — the editor's own fix caught the stacked-negation shape M2 exists to catch) |
| 12 | Meta description | **Applied — publisher-layer change, this package.** `corporate wellness platform` removed from metadata; `wellness platform` used. Narrows `review-1-decisions.md` §A1 without reversing Vadim's direction there | See Meta section above |
| 13 | Keyword stacking in the corporate subsection | **Applied.** `corporate wellness platform` kept once; the stacked "employee wellness app" / "employee wellness program" repetition removed | Line 127: "A corporate wellness platform working on that specific problem will find verification covered in depth in [wellness rewards verification...]" |
| — | 6 smaller softenings | **Applied, all six, verbatim in intent** | "may show apparent change" (line 59) · "a chart with reduced comparability" (line 63) · "a headline accuracy figure is incomplete on its own" (line 105) · "without requiring [members] to attend an onsite assessment" (line 127) · "additional context alongside the member's own account" (line 83) · "can be more useful as a trend than as an isolated headline number" (line 61) |

**What this closes that Review 1 left open:** open item 1 (no approved third-party source for
self-monitoring/engagement) is closed — not by finding a source, but by removing the one sentence
(item 2 above) that needed one. Nothing is left on Vadim for that item.

## What the reviewer confirmed is working (carried forward verbatim from `review-2.md`)

The reviewer's own closing list of what the article does successfully, unchanged by this
revision's edits:

1. Establishes a clear wellness scope
2. Broadens the audience beyond employers and insurers
3. Reduces rewards-verification cannibalization
4. Removes the weak "Why now" section
5. Introduces a useful summary table
6. Keeps progress visibility as the strongest part
7. Treats body data as one personalization input
8. Adds appropriate optionality and non-judgmental UX guidance
9. Separates accuracy from repeatability
10. Uses the correct 96-97% and 1.5-2.0 cm formatting
11. Uses DXA consistently
12. Shortens implementation guidance
13. Replaces the fraud-detection statement appropriately
14. Uses the approved medical-device wording
15. Creates clear routing to the fitness, health, and rewards hubs

## CMS tasks that ship with this article

Carried forward from v2, none changed in kind by Review 2's sentence-level edits, plus one new
task from item 11's fallback condition.

### 1. Inbound internal-link pass (required, load-bearing, unchanged from v2)

This hub inherits no external authority: Beyond BMI has 1 backlink, Wellness Rewards has 0. With
the keyword `wellness platform` (150/mo, KD 36) replacing `corporate wellness platform` (500/mo,
KD 11) at the Review-1 keyword re-decision, a page with zero external links reaching a KD 36 term
needs this pass to happen, not merely to help.

| Donor page | Backlinks | Anchor context to add |
|---|---|---|
| `/content-hub/ai-in-fitness-industry/` | 326 | Where it separates training outcomes from wellbeing and corporate wellness programs |
| `/content-hub/the-potential-of-ai-in-telehealth/` | 263 | Where it covers remote capture outside clinical care |
| `/content-hub/glp-1-market/` | 183 | Where it discusses progress tracking beyond weight for non-clinical programs |
| `/content-hub/top-fitness-industry-trends/` | 36 | Corporate and employee wellness trend mentions |
| `/content-hub/weight-loss-industry-overview/` | 33 | Employer and insurer wellness program mentions |

### 2. Architecture re-parenting (approved at checkpoint 1, unchanged)

`wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` stops being the
Wellness hub and becomes the employer/insurer sub-hub under this page. Required: update
`brand-assets/content-strategy/published-articles-inventory.md` (Hub #8 row, Wellness section,
Internal Linking Map) and run an internal-link pass on the Wellness Rewards page itself so it
points up to this hub.

### 3. Privacy FAQ dependency (2 placeholders in the text, unchanged in kind)

The Data, Privacy, Security & Regulatory FAQ is still an unpublished P0. Two
`<!-- TODO(publish) -->` markers sit in the source: section "What to evaluate in a body-data
provider" (line 113) and FAQ Q5 (line 146). Nothing is broken if the article ships as is; when the
FAQ publishes, both markers become links and the inline answers can shorten.

### 4. NEW — Privacy FAQ must explain direct identifiers vs. personal data (Review 2 item 11 fallback)

Review 2 item 11's fallback condition: "ensure the privacy FAQ explains the distinction between
direct identifiers and personal data." This revision applied the reviewer's precise wording
instead of relying on the fallback, but the fallback still binds the FAQ itself once it ships —
whoever writes the Data, Privacy, Security & Regulatory FAQ needs to state that distinction
explicitly (body photos and derived measurements can be personal data even with no direct
identifier attached), not just repeat the short "no personal identifiers" forms that
`compliance.md` carries for outbound and social. Owner: whoever drafts that FAQ; flag for
`page-builder` or the next SEO writer who touches it.

## Open items for Vadim

Five items. One closes this revision, one gains a note; three survive unchanged from v2.

1. ~~No third-party source on self-monitoring and feedback~~ **CLOSED by Review 2 item 2.** The
   outcome claim that needed a source ("that can contribute to continued engagement") is removed;
   the section argues from mechanism only. No source required, nothing left on Vadim for this.
2. **DEXA/DXA divergence in brand-assets.** Still open. `DEXA` remains the house spelling in
   `terminology-guardrails.md` §1, `editorial-guardrails.md` #7, and the Part 3 grep row.
   `article_lint.py` now catches it in any article that regenerates it, but the source documents
   are unchanged. Owner: Vadim.
3. **essential/beneficial fat vs `predicted weight` in `proof-points.md` / `how-it-works.md` /
   FX-009.** Still open. Review 2 sharpened this: the reviewer now explicitly defers to the
   approved repository ("The approved repository should take precedence over my earlier
   recommendation"), which means the repository has to be correct about the product. Owner:
   Vadim.
4. **"positioned as" is in its third policy state.** Still worth settling permanently in the
   source Doc rather than re-litigating per article. Owner: editorial owner + Vadim.
5. **Images: planned 2026-09-02, not produced.** The reviewer named illustration planning as the
   next step and that half is now done: three banners with placements, alt text, six
   article-specific constraints and a documented list of what was rejected and why, in
   `illustrations.md` and summarised above. **The blocker is upstream of design.** The Figma
   file cannot be read from here (authentication), `brand-assets/past-posts/_figma-exports/`
   does not exist, and `brand-assets/` holds zero image files. `visual-brief` already reads that
   directory and is instructed to STOP without it, so this gap is wired into the pipeline and
   has simply never been filled. **Owner: Vadim for the export, then design for the assets.**
   Two smaller open questions inside the plan: the 1200 px body width is inferred from the site
   container rather than confirmed, and the featured / OG image slot convention cannot be read
   from the corpus.
6. **NEW, small: `compliance.md` has no article-grade privacy line.** The short forms ("process
   zero personal identifiers" / "no personal identifiers stored") are correctly labelled for
   outbound and social, but there is no page/article-grade version on file, so the next writer who
   needs this wording has to reach for the reviewer's phrasing again from scratch rather than a
   documented source line. Worth adding the long form to `compliance.md` as the article/page
   variant. Owner: Vadim. Not done in this revision (out of scope for a wording pass).

## Alt options

### Meta title variants (unchanged this revision)

1. AI Body Data for Wellness Platforms | 3DLOOK (44 chars). **Recommended.** Carries the primary
   keyword verbatim in the plural, matches the H1, keyword in the first half.
2. Wellness Platform Body Data and Engagement | 3DLOOK (51 chars). Singular exact match at
   position 1, strongest keyword signal, reads less like the H1.
3. Body Data for Wellness Platforms | 3DLOOK (41 chars). Shortest, drops the "AI" framing.

### Meta description variants (NEW this revision, per Review 2 item 12)

1. Measured body data gives a wellness platform a repeatable progress signal the scale misses,
   supporting personalization and engagement. See what to evaluate. (**156 chars**).
   **Recommended.** Echoes the article's own reframed opening (Review 2 item 1), zero
   "corporate," soft CTA, no title repeat.
2. Repeatable body data helps a wellness platform show real progress between check-ins that a
   scale alone cannot capture. See what to evaluate in a provider. (**154 chars**). Leads with
   "repeatable," closer to the article's closing sentence; avoids the recommended option's
   "repeatable... progress" near-echo two words apart.
3. For a wellness platform, measured body data turns a flat scale reading into a comparable
   progress record between check-ins. See what to evaluate in a provider. (**159 chars**). Opens
   with the keyword phrase itself rather than the product, most literal restatement of what the
   article argues.

All three: counted (not estimated) at the stated lengths, exactly one instance of `wellness
platform`, zero instances of `corporate`, zero em dashes, no title repeat.

## Illustration plan (revision 3, planned 2026-09-02)

Full designer brief: **`illustrations.md`** in this directory. What follows is what needs
approving at checkpoint 2. **This replaces the four v1 suggestions**, which proposed a hero
image and an evaluation-checklist card; both are wrong against the published corpus and are
explained under "rejected" below.

### What the corpus does, measured

Of the nine articles in `brand-assets/past-articles/blog/`, **exactly one carries images**:
`online-pharmacy-bmi-verification`, 2,638 words, **2 images**, **no hero**, both in-body,
`.webp` at `/wp-content/uploads/YYYY/MM/banner_N.webp`. Alt text describes the frame first and
ties to the keyword last. So the house norm is two in-body banners. This article is 2,790 words
and hub-shaped, so three is defensible, with banner 3 the one to drop if capacity is short.

### The three banners

| # | Placement | What it shows | Why an image rather than prose |
|---|---|---|---|
| 1 | `final.md` line 53, **Progress visibility beyond scale weight** | Member-facing progress view comparing two check-ins: bodyweight unchanged, a body measurement moved, baseline and current 3D model alongside | The only one on the list showing something prose physically cannot. Both reviewers named this the article's strongest section |
| 2 | line 87, **Practical wellness-platform workflow** | The five steps as a horizontal flow, with the platform / body-data ownership split marked | A sequence is what a diagram reliably beats prose at. Already a house component pattern (DESIGN.md §11) |
| 3 | line 23, **the opening comparison** | Three columns: self-reported entry, scale reading, repeatable body data, each with its own distinct limitation | Review 2 item 1 rebuilt this paragraph so the three records no longer share a limitation. That correction is the article's frame |

**Alt text, as it will ship:**

1. "Wellness app progress view comparing two member check-ins, where bodyweight is unchanged and
   the waist measurement has moved, shown beside a baseline and current 3D body model."
2. "Five-step wellness platform workflow from consent and baseline capture through recurring
   check-ins to comparison, with platform responsibilities separated from the body-data layer."
3. "Three ways a wellness platform can record physical progress, comparing a self-reported
   entry, a scale reading, and repeatable body data."

### Rejected, with the reason

| Candidate | Why not |
|---|---|
| Hero banner (was v1 suggestion 1) | The corpus does not use one; the H1 leads. A hero here would be a new site convention, not this article's call |
| Evaluation checklist card (was v1 suggestion 4) | Re-renders prose as graphics and adds nothing, and a "checklist" graphic invites being read as a spec or certification, the exact reading the accuracy section works to prevent |
| The value-map table | Already a table. The article carries seven; a graphic version duplicates it and reads worse on mobile |
| A product shot in "Where FitXpress fits" | Tips a hub page toward a product page. That is the failure the cannibalization guardrail exists to prevent |

### Six constraints that come from this article's own claims

Brand tokens are in `illustrations.md` §7. These are the ones where breaking the rule makes the
image contradict the text:

1. **Nothing depicting a decision, score, diagnosis, eligibility or reward outcome.** A
   wellness-score dial, traffic light, or approved/declined badge would contradict the boundary
   section visually. Most likely way to get this wrong.
2. **A number inside an image must come from an approved claim or read as illustrative.**
   Do not invent a change figure such as "waist −3.2 cm over 8 weeks". **Verified 2026-09-02:
   `article_lint.py` fails an invented figure in alt text, and is blind to one rendered inside
   the image.** This one cannot be automated; it stays with the designer and with review.
3. **A stored photo is shown blurred; a live capture view is not a stored photo.** Blur is
   automatic *when photos are stored*, per `compliance.md` and per the article. The 3D model is
   a mesh and carries no face.
4. **No named vendors, no customer logos.** Zero wellness proof points exist. Yazen and UK Meds
   are GLP-1 and pharmacy and must not be re-labelled as wellness in an image any more than in
   prose.
5. **Not corporate-coded.** No office desks, lanyards, HR dashboards or benefits-portal styling.
   The article's broad:corporate term balance is 4.3 to 1 and the artwork should not invert what
   Review 1 item 2 removed from the text.
6. **Body representation.** A range of body types, no before/after weight-loss trope, no arrows
   implying a body should move one way. The article's own UX paragraph asks for neutral,
   non-judgemental comparison.

### Blocked, and this is the one thing needed from Vadim

The Figma file (`Blog-banners`, node `2088-4`) **cannot be read from here**: Figma requires
authentication and a fetch returns nothing but the word "Figma".

- `brand-assets/past-posts/_figma-exports/` **does not exist**
- `brand-assets/` contains **zero** image files
- `visual-brief` step 3 already reads `_figma-exports/blog-banners/` and is instructed to STOP
  when it is missing, so the gap is known and wired in, just never filled

**Export the banner frames as PNG into `brand-assets/past-posts/_figma-exports/blog-banners/`.**
That is the path the pipeline already expects, so filling it fixes this for every future
article. Until then the brief is derived from `DESIGN.md` tokens, which keeps a designer
on-brand but will not match the established banner composition.

### Production spec

`.webp`, named `banner_1..3.webp`, at `/wp-content/uploads/2026/09/`. Body width **1200 px at
2x** is *inferred* from the site container in DESIGN.md §4, not confirmed: exact export sizes
are not in the design export. **Open question:** the featured / OG image is a separate slot from
in-body banners and is what appears in a social share; the corpus markdown does not show it, so
the convention cannot be read from the repo. Recommend banner 1 doubles as featured, to be
confirmed with whoever owns WordPress.

### Nothing goes into `final.md` yet

The article carries no image markup and should not until the assets exist, because a broken
reference is worse than no image. When the files are produced: insert the three `![alt](url)` at
the named lines, re-run `article_lint.py` (must stay PASS), regenerate this package so its
embedded copy matches.

## Article

# AI Body Data for Wellness Platforms: Progress Tracking, Personalization, and Engagement

A wellness platform has limited visibility into physical progress between check-ins. What it usually holds is a self-reported entry and a scale reading. Self-reported entries get estimated or rounded, and they are not always collected the same way twice. A scale reading compares cleanly against last month's. Its limitation is a different one: one number compresses every kind of body change into a single direction of travel. Repeatable body data adds a third record, measurements and visual context captured under the same protocol each time and timestamped, which is what allows two check-ins months apart to be compared. Better visibility can support engagement, though it does not guarantee retention.

The same gap shows up across wellness platforms of very different shapes: consumer wellness apps, lifestyle-change platforms, nutrition and habit-coaching products, digital wellbeing ecosystems, and coaching that is human-led, automated, or a mix of both. Corporate wellness is one application of the same capture layer.

**Scope.** This hub covers non-clinical wellness platforms, lifestyle and nutrition coaching, habit-building and progress-tracking apps, and member and employee wellness experiences. Three adjacent topics have their own homes: workout programming and performance belong to the [AI in fitness hub](https://3dlook.ai/content-hub/ai-in-fitness-industry/), patient monitoring belongs to [healthcare and telehealth content](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/), and incentive verification belongs to the [wellness rewards hub](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/).

## What AI body data means for wellness platforms

For a wellness platform, AI body data means structured body measurements and body composition estimates, captured remotely, produced under the same protocol each time, and timestamped so two check-ins can be compared.

A capture uses two smartphone photographs, front and side, and returns results in under 45 seconds. <!-- claim: FX-007 --> <!-- claim: FX-006 --> The output covers more than 80 body measurements <!-- claim: FX-008 --> along with body composition estimates: BMI, basal metabolic rate (BMR), body fat percentage, lean mass, and fat mass. <!-- claim: FX-009 --> A 3D body model is generated alongside the numbers, which supports a side-by-side visual comparison at a later check-in. Because capture runs on a phone the member already owns, structured body data becomes available to a program without dedicated scanning hardware.

Comparability depends on repeatability. The same body, measured again under the same protocol, has to return close to the same number.

Weight and BMI are coarse instruments for this job. They compress a body into one or two numbers and discard the distribution, and BMI can sit flat through a period of genuine change while individual measurements move. The longer argument for looking past that single number is set out in [Beyond BMI](https://3dlook.ai/content-hub/beyond-bmi-business/).

One boundary sits at the front: body data of this kind is an input to a wellness program, and the outputs describe measurements. Interpreting what those measurements mean for a person's health stays outside the product.

## Where body data creates value: summary table

Body data contributes to five wellness objectives, and each one draws on a different property of the record: a comparable baseline, a change trend, or a consistent timestamped history. The mapping holds across most wellness platforms.

| Wellness objective | Body-data contribution | Platform application |
| :- | :- | :- |
| Progress visibility | Repeatable baseline and later records | Baseline-to-current comparison |
| Personalization | Starting measurements and change trends | Goal-relevant content or coaching |
| Engagement | Meaningful recurring feedback | Progress views and milestone check-ins |
| Coaching | Structured longitudinal context | Better-informed coaching conversations |
| Program insights | Consistent timestamped records | Adoption and progress reporting |

## Progress visibility beyond scale weight

Progress visibility is the mechanism that makes body data worth integrating into a wellness app, and it is simpler than it sounds.

A member who has been consistent for eight weeks opens the app. Instead of a weight number that has barely moved, they see their current 3D model beside the one from their baseline, with the measurements that changed listed next to it. Waist measurement down. Chest and shoulders holding. The product now shows a more complete view of progress than the scale reading on its own.

Repeatability is especially important for longitudinal tracking, because the comparison runs between a member and their own earlier scan. If scan-to-scan noise is larger than the change a member produced in eight weeks, the comparison may show apparent change that did not happen, or miss change that did. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-003 --> Accuracy is a separate property, measured against a reference method and evaluated with its own evidence.

Which numbers to show a member is a product decision with real consequences. Showing everything produces a dashboard that reads as clinical and invites interpretation the program cannot support. A defensible default is to surface the small number of measurements tied to the member's own goal, keep the visual comparison prominent, and limit the wider measurement set to authorized program teams with a reporting need for it. Body fat percentage deserves particular care in a wellness setting: it can be more useful as a trend than as an isolated headline number.

Underneath the product decisions sits a narrower measurement point. The comparison holds only when both sides of it were captured the same way: the same guided pose and similar capture conditions. A body composition tracking app that allows those conditions to drift between check-ins produces a chart with reduced comparability.

## Personalization using goals, starting points, and trends

A wellness app that knows a member's stated goal knows their intention. A measured baseline adds where that member is starting from physically, and a repeat capture adds which direction things moved.

Body data is one input among several, and it works when combined with the others: the member's stated goals, their preferences, activity and habit information, their schedule and available resources, any relevant limitations, and their previous progress. A scan carries no information about motivation, food environment, or the time a member can commit, and each of those also influences outcomes. Appropriate targets and nutrition intake are set by the program and the people running it.

What a measured record adds that an onboarding survey cannot is a starting point that updates. A survey personalizes a wellness tracker app once, at sign-up; a repeated body record allows the program to adjust as the member changes.

At the program level, the same records aggregate into body-data trends for reporting: participation and change across appropriately defined cohorts. That use stays within the purpose members were told about at consent and behind the same privacy controls as the record itself. Segmentation is a separate question, and measured body characteristics are a weak default basis for it, particularly where the population is a workforce.

Nutrition and lifestyle coaching platforms use the same input on longer horizons, where body composition adds context to intake planning that a coach or dietitian sets. That case shares the capture layer and deserves its own treatment.

## Engagement and coaching

A recurring capture gives a program something specific to report back at a check-in, which supports more meaningful feedback than a weight entry on its own. It can make progress easier to understand, and that matters most when weight has been flat for a month. It creates an additional structured check-in in a product that otherwise waits for the member to open the app. The record it leaves is also what coaching and content selection can draw on.

The limit sits right beside it. A progress view can support app engagement, and what a member gets out of the program still comes down to content quality, coaching, and program design.

Coaching is where a repeatable record earns most. In a wellness coach app with human coaches, a scan gives the coach a starting point and a change record to work from, additional context alongside the member's own account of how it is going. In automated programs the same record can support content selection and the progress display, while the platform stays responsible for the rules and recommendations it applies. Human review can be specified for reward, access, or other consequential decisions.

One user-experience consideration is specific to wellness. Body measurement is appropriate only when physical change is part of the member's chosen goal, which makes body-data features work best when they are optional and goal-led. Not every wellness journey needs a body measurement at all: a sleep, stress, or habit-formation goal can be complete without one. Visual comparisons should use neutral, non-judgemental language. Progress should not be reduced to appearance or weight loss, and members should be able to control which indicators they see.

## Practical wellness-platform workflow

Five steps cover the workflow, and the order matters.

1. Consent and baseline capture. The member agrees to what is captured and stored, then completes a first scan from two photographs. <!-- claim: FX-007 -->
2. Selection of goal-relevant outputs. The program decides which measurements and estimates the member sees, and which outputs are retained or made available to authorized program teams.
3. Result presentation. The first result sets a member's understanding of the whole feature, which is why plain labels and a one-line explanation of each number earn their space.
4. Recurring capture. The same guided pose and similar capture conditions each time, which is what keeps it comparable with the baseline.
5. Comparison and connection to the platform's next step. The new capture is compared against the baseline and the previous scan, and the program ties that comparison to the next action it wants.

Cadence is worth setting deliberately. A four-to-twelve-week interval can be a practical starting point, depending on the program goal, the expected magnitude of change, and capture conditions.

Division of labour is the other decision. The platform owns program logic and the member relationship, from onboarding through to result display. The body-data layer owns capture, measurement output, and the comparable record.

Instrument five measures from the first pilot: scan completion rate, retake rate, second-scan rate, engagement with the progress view, and whether members can explain what their progress view is telling them. Wellness program software teams can also compare continued participation between members who scan and members who do not. A gap there is a signal to investigate, and on its own it establishes nothing about cause.

## What to evaluate in a body-data provider

Accuracy is the question every evaluation opens with, and a headline accuracy figure is incomplete on its own. The answerable version carries five conditions: accurate enough for which decision, against which reference method, under which capture protocol, for which population, at what tolerance. Acceptable error depends on the expected magnitude of change and on the workflow. Internal validation against expert manual measurement puts overall accuracy at 96-97%, with typical absolute error of 1.5-2.0 cm, and the [body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out how those figures were produced and how to ask about the two properties separately. <!-- claim: FX-001 --> <!-- claim: FX-002 -->

Ask about repeatability separately. It carries particular weight for longitudinal tracking against a member's own earlier record. <!-- claim: FX-003 -->

Population takes one question: what population was the model validated on? For FitXpress it covers ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, collected across the US and Europe. <!-- claim: FX-011 --> Wellness populations often sit near the edges of a validation range, and edge behaviour is where a model is least tested.

Phones, lighting, and clothing all vary across a distributed population, which makes capture reliability the next filter. Ask what pose validation runs at capture, how retakes are handled, and whether guided capture is supplied or built.

Data handling is a procurement gate. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR). Photos are permanently removed immediately after processing, or within 30 days, depending on the client's configured policy, and are automatically blurred when stored. Storage is Amazon S3 in the client's region, with server-side encryption (SSE-S3) always on. FitXpress does not receive names, contact details, or other direct identifiers that connect the scan with a specific individual. Photos are not used to train the model. <!-- source: compliance.md, approved wordings per review-1-decisions §C --> The Health Insurance Portability and Accountability Act (HIPAA) is worth asking about where a program touches US healthcare. <!-- claim: FX-014 --> <!-- TODO(publish): swap this block for a link to the Data, Privacy, Security & Regulatory FAQ once it publishes; the inline answers above stand until then -->

The last question is integration effort: how long until a member can complete a check-in inside the existing product and see a comparison.

## Where FitXpress fits

FitXpress is the capture and structured-data layer inside a wellness platform's own product. Two photographs in, more than 80 measurements and body composition estimates out, in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 --> Integration runs through an application programming interface (API), a web software development kit (SDK), and mobile SDKs, with the guided-capture layer supplied. The platform keeps the rest: onboarding, consent wording, the scan entry point, result display, and which metrics appear at all. For a team adding a 3D body scanning app flow to an existing product, that division is what sets the scope of the build.

The boundary belongs in the same breath. It is not positioned as a medical device. FitXpress does not diagnose conditions or screen for them. Decisions about program access stay with the program. Dual-energy X-ray absorptiometry (DXA) and bioelectrical impedance analysis (BIA) measure composition against their own references, and a mobile scan is no substitute for either. On fraud, FitXpress can provide capture-quality and verification signals, while final determinations are reached by a person. The platform remains responsible for its program rules and applicable compliance requirements.

Teams that want to see the capture flow and the returned data inside a live member-facing product can start with [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## Boundaries and related hubs

**Corporate wellness.** Corporate wellness is one application of everything above. Standardized remote capture can support a distributed wellness program, where a workplace wellness app reaches members without requiring them to attend an onsite assessment. Reward-linked applications carry additional governance and review requirements. A corporate wellness platform working on that specific problem will find verification covered in depth in [wellness rewards verification for employers and insurers](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/).

Workout programming and performance sit with [AI in fitness](https://3dlook.ai/content-hub/ai-in-fitness-industry/). Patient monitoring sits with healthcare and telehealth content. Comparing measurement methods against each other starts with [how to measure body composition](https://3dlook.ai/content-hub/how-to-measure-body-composition/). The wider map of body data across health programs is the [AI body data hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/).

## Frequently asked questions

**What is AI body data, and what does a wellness platform get from it?**
AI body data is a set of body measurements and body composition estimates derived from smartphone photographs. The platform gets a measured baseline at onboarding and a comparable record at every check-in, which supports progress display, personalization, and body composition tracking without a clinic visit.

**How does a remote body scan work for a wellness check-in?**
A member takes two photographs, front and side, fully clothed, with their own phone. <!-- claim: FX-007 --> Guided capture validates the pose before submission. Results return in under 45 seconds, including more than 80 measurements, body composition estimates, and a 3D model. <!-- claim: FX-006 --> <!-- claim: FX-008 -->

**Can a body scan replace a DXA scan, a BIA device, or a calibrated scale?**
No. Those methods use different references and answer different questions, and a mobile scan is no substitute. Its value in a wellness program is frequency and consistency, repeated remotely as often as the program needs. Choosing between methods is covered in the accuracy framework.

**Is body data used to make decisions about members or their access to a program?**
No. The scan produces a measurement record. Decisions about members and their access to a program are taken by the program under its own rules, and a person stays responsible for them.

**What data is captured and stored, and what happens to the photos?**
Two photographs are processed into measurements, body composition estimates, and a 3D model. Photos are permanently removed immediately after processing, or within 30 days, depending on the client's configured policy, and are automatically blurred when stored. Storage sits in the client's own region. FitXpress does not receive names, contact details, or other direct identifiers that connect a scan with a specific individual. Photos are not used to train the model. <!-- TODO(publish): link to the Data, Privacy, Security & Regulatory FAQ here once it publishes; the answer above stands until then -->

**How often should a wellness program run check-in scans?**
Four to twelve weeks is a practical starting point for most wellness apps, and the right interval depends on the program goal, the expected magnitude of change, and how consistently members capture. Weekly captures sit close to normal daily variation in the body. Intervals longer than a quarter leave a sparse record to compare against.

## Where to go next

Three routes from here, depending on where a program is.

For teams still mapping the territory, the [AI body data hub](https://3dlook.ai/content-hub/ai-body-data-health-hub/) covers how body data is applied across health programs, and [Beyond BMI](https://3dlook.ai/content-hub/beyond-bmi-business/) is the shorter educational bridge.

For teams weighing integration options and the shape of the returned data, [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) is the closer fit.

For employers and insurers whose immediate question is rewards verification, [wellness rewards verification](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/) covers it in depth.

Repeatable body data can give a wellness platform a more complete view of progress between check-ins.
