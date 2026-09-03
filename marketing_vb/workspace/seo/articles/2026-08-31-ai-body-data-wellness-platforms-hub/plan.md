---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
proposed_url_slug: ai-body-data-wellness-platforms
product: fitxpress
primary_keyword: wellness platform
primary_use_case: brand-assets/product-info/use-cases/fx-digital-fitness.md (+ fx-wellness-rewards.md for the employer/insurer subsection)
hub: Wellness Platforms (Hub #8)
cluster: Main hub
intent: Hub
action_type: create-net-new
priority: P0
status: approved
revision: 2
revision_reason: Review 1 (2026-09-02)
checkpoint_1_approved: 2026-08-31 (title/hub), keyword re-decided 2026-09-02
target_words: 1750  # lowered from the outline's 2,650 by Vadim, 2026-09-03. See "Revision 6".
revision_6: final-google-doc.md  # the shipping text; final.md is revision 3 and is superseded
created: 2026-08-31
context_pack: workspace/seo/_context-packs/2026-08-31-ai-body-data-wellness-platforms-hub.yaml
keywords_file: workspace/seo/_keywords/2026-08-31-ai-body-data-wellness-platforms-hub.yaml
backlink_report: workspace/research/backlinks/  (Ahrefs export, snapshot 2026-08-31)
review: workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/review-1.md
review_decisions: workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/review-1-decisions.md
v1_snapshot: workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub/v1/
---

## Revision 6: Vadim's calls on the Google Doc final (2026-09-03)

The article kept moving in the Google Doc after this repo stopped at revision 3. The shipping
text is `final-google-doc.md`; `final.md` is revision 3 and is superseded. Three calls, all
Vadim's, all recorded here so the gates and the next writer agree with what shipped.

**1. Length: the delivered text stands, the target moves to meet it.** The final runs 1,737
prose words against the outline's 2,650, which failed the length gate by 23% of the floor.
Vadim's call is to keep the text as written rather than pad it back to the outline, so
`target_words` is now 1,750 in the frontmatter. The per-section budget table further down is
left untouched on purpose: it records what was planned, not what shipped. The gate reads the
frontmatter first, so it now measures the article against the decision instead of against a
plan the article deliberately left behind.

**2. `corporate wellness platform` is abandoned, not restored.** This overrides
`review-1-decisions.md` §A1 ("keeps a real home so the 500/mo term is not abandoned") and
Review 2 item 13, which had narrowed that home to one place, the corporate subsection. The
final version carries zero instances and Vadim's call is to leave it that way. Cost, stated
plainly so nobody rediscovers it later: the page trades 500/mo at KD 11 for `wellness platform`
at 150/mo and KD 36. The 500/mo term now has no page on the site. If it is ever wanted back, it
belongs in a separate employer-facing page, not retrofitted into this hub.

**3. The closing CTA comes back.** Revision 3's `Where to go next` was dropped somewhere in
versions 4-6, leaving a P0 hub with no route out. It is restored after the FAQ with the three
routes rewritten to match the final version's register, and it does not repeat the links already
carried by `Related wellness and body-data resources`.

Still open after this pass, and not Vadim's to close alone: the inbound-link pass has no owner,
the three illustrations are planned but not produced, and the GDPR controller/processor sentence
in `Privacy and data handling` has no source line in `brand-assets/` (see below).

---

## Revision 2: Review 1 (2026-09-02)

Sources for this revision: `review-1.md` (stakeholder review, 20 items plus a recommended
12-section structure) and `review-1-decisions.md` (Vadim's calls and conflict resolutions).
**Where the two disagree or can be read two ways, the decisions file wins.**

What changed against v1:

1. **Primary keyword broadens.** `corporate wellness platform` (500/mo, KD 11) is demoted to
   secondary. Primary is now `wellness platform` (150/mo, KD 36), with `wellness app` (1000/mo,
   KD 1) and `corporate wellness` (1000/mo, KD 3) as support terms. Decisions §A1.
2. **Corporate wellness stops being the frame.** It becomes one application in one three-point
   subsection inside section 10. Consumer wellness apps, lifestyle-change platforms, nutrition and
   habit-coaching products, digital wellbeing ecosystems, and coaching get equal or greater weight.
   Review item 2.
3. **New 12-section structure, applied verbatim** from the review, replacing v1's 12 H2s. Three v1
   sections are cut outright, two are merged into one, one new section is added, one is kept.
4. **Word count target drops from 3,200 to 2,650 (±150).** This is the main structural deduction.
5. **The strongest section is protected.** Progress visibility is marked `keep` per review item 7,
   with one mandatory sentence-level change and the over-detailed figures cut.
6. **Engagement language is capped** at the reviewer's four supportive formulations. No causal
   retention claim anywhere. Review item 9.
7. **New wellness user-experience material** (optional, goal-led, non-judgemental, member-controlled
   indicators) is the clearest differentiator from the fitness hub. Review item 10.
8. **Wording corrections applied throughout:** DXA not DEXA, "body composition estimates" not
   "values", "API, web SDK, and mobile SDKs", capture-quality and verification signals instead of
   "does not detect fraud", "It is not positioned as a medical device." (licensed exception, see
   `terminology-guardrails.md` §2.10 re-reversal note of 2026-09-02), and the approved
   controller/processor GDPR sentence.
9. **Two factual corrections that run against the review or against v1.** `predicted weight` is
   **not** added to the output list, because no approved claim supports it (decisions §B3). And the
   **height range is 150 to 220 cm**, resolved by Vadim on 2026-09-02: v1's figure of 150 to 205 cm
   was simply wrong, one figure now covers both the training-data coverage and the internal
   validation population, the figure is propagated across the repo including claim FX-011, and the
   live accuracy article already published 150 to 220 cm, so no CMS work is needed and no public
   divergence exists. Closed, with no follow-ons. Decisions §B2.
10. **The training-data paragraph is still cut**, on the review's own "not essential to this hub"
    ground plus the word-count target. FX-010 goes uncited; FX-011 survives as one clause in
    section 8.
11. **The checkpoint-1 H1/meta split is void.** v1 argued the H1 deliberately omits the head term
    while the meta title carries it. With `wellness platform` as primary, both carry it.
    Decisions §A1.
12. **H1, hub placement, action type, priority, internal-link directions, backlink strategy, the
    re-parenting decision and the publish-step tasks are unchanged** and are transferred below.
    Decisions §E.

---

## Checkpoint 1 record (2026-08-31, amended 2026-09-02)

Approved at checkpoint 1 and still standing: the title, Hub #8 placement, `create-net-new` action
type, P0 priority, and the architecture re-parenting decision. **Amended by Review 1:** the primary
keyword decision (item 2 of the original three) was reversed on 2026-09-02, see decisions §A1.

Still open and deliberately not blocking the rewrite: no wellness proof points exist (argue from
mechanism, never re-label Yazen or UK Meds as wellness), and the Data, Privacy, Security &
Regulatory FAQ is still unpublished, so section 8 and FAQ Q5 carry short inline answers with
`<!-- TODO(publish) -->` markers.

---

# SEO Plan (revision 2), AI Body Data for Wellness Platforms (Hub #8)

## Content Strategy Fit (Phase 0), transferred unchanged

Phase 0 is not re-litigated in this revision. Transferred from `v1/plan.md` with em dashes replaced
by commas or colons (the dash ban is absolute), substance untouched.

- **Hub / cluster:** Wellness Platforms (Hub #8), Main hub
- **Action type:** `create-net-new`, **gate passes.** The content-plan row exists verbatim ("AI Body
  Data for Wellness Platforms: Progress Tracking, Personalization, and Engagement", Main hub, Hub,
  Create net-new, P0). No broad Wellness Platforms page exists in
  `published-articles-inventory.md`, so this is not a duplicate or a disguised refresh.
- **Priority:** P0. One of the last two open P0 items in the whole health plan (the other is the
  Data, Privacy, Security & Regulatory FAQ).

### Existing pages and how each is used

| URL | Role here | What we must NOT do |
|---|---|---|
| `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` (Mar 30, 2026) | Employer/insurer **sub-hub**. Linked sideways and down from section 10. Owns rewards verification, disputes, participation, audit trail. | Do not replace it. Do not re-explain rewards verification at depth. Three points, then link. |
| `/content-hub/beyond-bmi-business/` (Jul 2025) | Broad **educational bridge**. Linked from section 2. | Do not restate Beyond BMI's argument in full. Two or three sentences, then link. |

### Cannibalization guardrail

Verbatim from the plan row:

> "Keep wellness softer: engagement, personalization, rewards, and progress visibility.
> Avoid clinical or clearance-decision framing."

**How this outline complies (the 5 questions, §5 guidelines):**

1. *Does an existing article already answer this?* Partly. Wellness Rewards answers the
   employer/insurer verification question. Beyond BMI answers why BMI alone is thin. Neither answers
   how a wellness platform uses body data as a product input for progress visibility,
   personalization, engagement, and coaching. That is the gap this page owns.
2. *Does the title overlap with an existing hub?* No page carries "Wellness Platforms." The overlap
   risk is with **Hub #4 (AI in Fitness)**, which owns fitness-app product strategy, progress
   visibility, and retention. Boundary drawn below. Review 1 raised the same overlap as its second
   structural objection, which is why section 1 now carries an explicit scope note and section 10
   carries the routing.
3. *Broad enough for a hub, or should it be a section?* Broad enough: 12 planned cluster rows sit
   beneath it (2 × P0, 6 × P1, 5 × P2).
4. *Does the recommendation say refresh / section-first / do-not-duplicate?* It says **create
   net-new**, with an explicit do-not-replace instruction on Wellness Rewards. Honored, and
   tightened further by review item 3.
5. *Exact search intent this page owns:* "What should a wellness platform do with body data, and
   what does adding it change?" Commercial-informational, pre-vendor-shortlist.

**Boundary vs Hub #4 (AI in Fitness):** Fitness owns training and coaching outcomes, meaning
workouts, recomposition, trainer workflows, and fitness-app features. Wellness owns program
participation and wellbeing, meaning check-ins, incentives, personalization of non-training
programs, and employee wellness. Where they meet (progress visibility), this hub states the wellness
case once and links sideways to `ai-in-fitness-industry` instead of re-arguing it. Review item 1
makes this a linked redirect in section 1, not just an internal discipline.

**Boundary vs the P1 "Top Employee Rewards Platforms" listicle:** that row owns vendor-landscape and
named-brand queries (`wellhub corporate wellness platform`, `best corporate wellness platform for
enterprises`, and the 8 vendor-brand terms parked in the keywords file). This hub does not target
them and includes no vendor comparison table.

### Vertical boundary (§9 guidelines, applies to every section)

Wellness **owns**: engagement, personalization, progress visibility, rewards, wellness apps,
employee wellness, coaching.

Wellness **must not**: use medical, diagnostic, clearance, or clinical decisioning language.
Concretely, the following are banned across this article: no "screening", no "health risk
assessment" as something FitXpress performs, no "cleared to participate", no "identifies members at
risk", no implication that a scan decides a reward, an eligibility, or a program tier. Softer verbs
only: *supports, makes visible, standardizes, documents, informs, personalizes*.

### Internal links planned (4 directions, §11), transferred unchanged

All four directions must survive the word-count cut (decisions §E).

- **Up** → `/content-hub/ai-body-data-health-hub/` (Main Health Hub), sections 10 and 12
- **Sideways** → Wellness Rewards Verification (sub-hub, sections 10 and 12) ·
  Beyond BMI (bridge, section 2) · `ai-in-fitness-industry` (Hub #4, sections 1 and 10) ·
  `how-to-measure-body-composition` (section 10)
- **Down** → `https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/` (sections 9 and 12)
- **Trust** → `/content-hub/mobile-body-scanning-accuracy/` (Trust Asset #1, sections 4, 8 and 9,
  linked once) · Data, Privacy, Security & Regulatory FAQ **(planned, not yet published,
  `<!-- TODO(publish) -->` marker in sections 8 and 11)**

Outbound links are only half the job. See the link-equity section below for the **inbound** links
this hub needs in order to rank at all.

### Link equity: this hub inherits nothing, so internal links have to carry it

Transferred unchanged. Source: `workspace/research/backlinks/` (Ahrefs export, snapshot 2026-08-31),
figures read from `links-by-segments.csv` and cross-checked against `all-links.csv`.

**The two pages this hub is meant to sit above have essentially no external authority:**

| Page | Backlinks |
|---|---|
| `/content-hub/beyond-bmi-business/` | **1** |
| `/content-hub/wellness-rewards-verification-…/` | **0**, the URL does not appear anywhere in the 14,680-row `all-links.csv` |

So the standard hub assumption, that we sit on top of established pages and absorb their equity,
does not hold. Re-parenting Wellness Rewards under this hub is an information-architecture gain, not
an authority gain. **This page starts from zero external links.**

**Where the Health segment's authority actually sits** (Health = 1,005 backlinks total, against
Apparel 2,398 and General 9,999; four URLs hold roughly 92% of it):

| Donor page | Backlinks | Relationship to this hub |
|---|---|---|
| `/content-hub/ai-in-fitness-industry/` | 326 | Hub #4, closest adjacent vertical, strongest donor |
| `/content-hub/the-potential-of-ai-in-telehealth/` | 263 | Hub #5, shares the remote-capture argument |
| `/content-hub/glp-1-market/` | 183 | Hub #6, shares progress-tracking-beyond-weight |
| `/mobile-tailor/` | 153 | Apparel product page, no credible wellness link, excluded |
| `/content-hub/top-fitness-industry-trends/` | 36 | TOFU fitness, plausible contextual link |
| `/content-hub/weight-loss-industry-overview/` | 33 | TOFU weight-loss, plausible contextual link |

**Consequence: inbound links matter more than outbound ones.** Revision 2 raises the stakes here,
because the new primary keyword carries KD 36 against v1's KD 11 (see the keyword section). A page
with zero external links does not reach a KD 36 term on content quality alone.

**Required inbound-link pass, a publish-step deliverable, not a writing task:**

| From (donor) | Link into | Natural anchor context |
|---|---|---|
| `/content-hub/ai-in-fitness-industry/` (326) | this hub | Where the fitness hub distinguishes training outcomes from wellbeing programs and corporate wellness. It already draws that line, so the link is contextual |
| `/content-hub/the-potential-of-ai-in-telehealth/` (263) | this hub | Where it covers remote capture outside clinical care |
| `/content-hub/glp-1-market/` (183) | this hub | Where it discusses progress tracking beyond weight for non-clinical programs |
| `/content-hub/top-fitness-industry-trends/` (36) | this hub | Corporate and employee wellness trend mentions |
| `/content-hub/weight-loss-industry-overview/` (33) | this hub | Employer and insurer wellness program mentions |

Three of those five (fitness, telehealth, GLP-1) were refreshed in the last five weeks, so their
internal-link sections are current and cheap to amend.

**Two link-hygiene notes from the same export:**
- The BOFU page this hub routes down to, `/fitxpress/for-connected-and-digital-fitness/`, has
  **1 backlink**. It cannot pull the hub up; traffic has to flow the other way.
- The export shows duplicate and parameterised variants in the wild (`/content-hub/ai-in-fitness/`,
  `/content-hub/ai-fitness-app/`, `the-potential-of-ai-in-telehealth` without a trailing slash, and
  several `?ref=` forms). Every internal link from this article must use the canonical
  trailing-slash URL.

**Strategic backing from the same report.** The Pivot tab is hand-written content strategy from the
report's author, not a pivot table. Its Priority 1 line for AI in fitness reads, verbatim, "Build a
full Health cluster around it," and its recommended effort split allocates **40% to Health cluster
expansion** ("Health has fewer pages but strong performance. Biggest growth opportunity"). A net-new
P0 hub hanging off the strongest Health page is that instruction executed.

### Architecture re-parenting decision, APPROVED 2026-08-31, unchanged

`published-articles-inventory.md` currently records `wellness-rewards-verification…` as **the hub**
for Wellness (Hub #8) and draws it as the hub node in the internal-linking map. The content plan
demotes it to sub-hub. Publishing this page therefore **re-parents the wellness cluster**: Wellness
Rewards stops being the hub and starts being a child. That is an information-architecture change on
a live page (its internal links and possibly its intro need a pass), not just a new URL. Approved by
Vadim on 2026-08-31 and reconfirmed in decisions §E. Review item 3 reinforces it: the review points
readers to the Wellness Rewards hub for incentive verification, which only reads correctly once the
parent/child relationship is right in the inventory and in the live linking.

Related: the plan row's own condition, "create a separate Wellness Platforms hub only if wellness
apps become a priority ICP", reads as satisfied. `icp-detail.md` carries wellness apps inside the
Digital Fitness segment and carries employer wellness as its own segment #4.

---

## Keyword Analysis (revised 2026-09-02)

This is the only part of Phase 1 that changes. The Ahrefs pull is not redone: all figures below come
verbatim from `workspace/seo/_keywords/2026-08-31-ai-body-data-wellness-platforms-hub.yaml`
(5 real pulls, 3,408 units, 2026-08-31). `null` means Ahrefs has **no measurement**, not zero.

### Seed check, unchanged

`seed_has_data: false`. The exact phrase "ai body data for wellness platforms" returns no Ahrefs data
at all, and neither does any near-slice of it (`ai body data for`, `data for wellness platforms`,
`for wellness platforms`, `wellness app engagement`). `ai body data` itself is 10/mo with `null`
difficulty. The hub name is an internal architecture label, not a search phrase. It stays as the H1;
the head term comes from elsewhere.

### The re-decision (decisions §A1)

| Role | Keyword | Volume / KD | Where it lives |
|---|---|---|---|
| **Primary** | `wellness platform` | 150 / KD 36 | Section 1 first paragraph, meta title, **section 2** (the designated primary-carrying H2) |
| Support | `wellness app` | 1000 / KD 1 | Body prose in sections 4, 5, 6 and the FAQ, 2-3 times total |
| Support | `corporate wellness` | 1000 / KD 3 | The employer/insurer subsection in section 10 only |
| **Secondary (demoted)** | `corporate wellness platform` | 500 / KD 11 | Meta description plus the employer/insurer subsection in section 10 only |

**Which H2 carries the primary: section 2, "What AI body data means for wellness platforms."** It is
the definitional short-answer block, it sits high on the page, it is the section answer engines
extract, and its heading carries the term verbatim in the plural. Its **opening sentence must use
the singular exact match** `wellness platform`. That sentence is the designated primary placement.
Section 7 ("Practical wellness-platform workflow") carries the second placement in its heading in
hyphenated form. Total exact-match uses across the article: 4 to 6, capped. Do not force more.

**Honest read of the trade, for the record.** The re-decision moves the primary from 500/mo at KD 11
to 150/mo at KD 36. That is one third of the measured volume at roughly three times the difficulty,
on a page with **zero external backlinks**. It is the right call on strategy (review item 2 is
correct that a hub tilted at employers cannot be the wellness hub, and the demoted term keeps a real
home), but nobody should read it as a traffic upgrade. Two consequences follow:

- The realistic traffic in this cluster now sits with the two support terms, `wellness app` (1000,
  KD 1) and `corporate wellness` (1000, KD 3), and with the plural `wellness platforms` (150, KD 2),
  which Ahrefs measures separately from the singular and rates far easier.
- The inbound-link pass from the five donor pages moves from "important" to **load-bearing**. KD 36
  is the hardest number in this plan.

**Demand honesty line (required).** Outside `wellness app` (1000) and `corporate wellness` (1000),
this entire cluster sits at 10 to 500/mo, and most of the long tail is 10 to 40/mo with `null`
difficulty (Ahrefs has no measurement, *not* zero). This is a thin-demand hub. Legitimate for a P0
architecture page whose job is to hold a cluster together and to be citable by answer engines. Not a
traffic play, and it should not be sold internally as one.

### Secondary clusters

| Cluster | Keywords | Intent | Volume / KD | Sections |
|---|---|---|---|---|
| Wellness platform (head) | `wellness platform` · `wellness platforms` | informational / commercial | 150/KD36 · 150/KD2 | 1, 2, 3, 7 |
| Wellness apps & engagement | `wellness app` · `app engagement` · `wellness tracker app` · `wellness coach app` | informational / commercial | 1000/KD1 · 400/KD7 · 150/KD5 · 200/KD0 | 4, 5, 6, 11 |
| Corporate & employer programs | `corporate wellness` · `corporate wellness platform` · `workplace wellness app` · `employee wellness app` · `wellness program software` · `employee wellness program` | commercial | 1000/KD3 · 500/KD11 · 150/KD1 · 100/KD6 · 100/KD1 · 700/KD47 | 7, 10 |
| Body data & progress tracking | `ai body` · `ai body data` · `body composition tracking` · `body composition tracking app` | informational | 400/KD8 · 10/KDnull · 50/KDnull · 10/KDnull | 2, 4, 11 |
| Product integration | `3d body scanning app` · `body scanning app` | commercial / transactional | 100/KDnull · 60/KD26 | 9 |
| Buyer requirements | `corporate wellness platform requirements` · `corporate wellness platform integrations` · `benefits of corporate wellness platform` | commercial | 10/KDnull · 30/KDnull · 20/KDnull | 8 |

**`employee wellness` (2000 / KD 78)** stays out of scope: real volume, unwinnable difficulty for a
page with no external links.

**`body composition` (32000 / KD 32)** stays out of scope: owned by `how-to-measure-body-composition`
and the GLP-1 cluster. Targeting it here would be textbook cannibalization.

**Dropped from v1's weave list:** `wellness app development` (600 / KD 0) and `corporate wellness
app development` (80 / KD null). Both are development-agency intent, not our buyer, and the section
that carried them (v1 H2.10) is merged and cut to 250 words.

**Not targeted (reserved):** all 8 named-vendor terms (`wellhub…`, `virgin pulse…`, `wellable…`,
`gympass…`, `personify health…`, `corehealth…`, `vantage fit…`, `yumuuv…`, 10 to 30/mo each) belong
to the P1 "Top Employee Rewards Platforms" listicle and are parked in the keywords file. Naming
competitors also violates `about-me.md`.

---

## Title and meta

**H1 (unchanged, verbatim from the content-plan strategy row):**

> AI Body Data for Wellness Platforms: Progress Tracking, Personalization, and Engagement

Not revisited in this revision. Decisions §E.

**Meta title (changed):** target `AI Body Data for Wellness Platforms | 3DLOOK`. It now carries the
primary keyword, because the v1 split (H1 omits the head term, meta title carries it) is void under
decisions §A1. 44 characters as written; decisions §A1 records 48. Either count sits inside the
usable range.

**Meta description (constraint, not final copy):** must contain `corporate wellness platform`
verbatim, exactly once. That plus the section 10 subsection are the only two homes the demoted
500/mo term gets. 150 to 160 characters, no em dash. Final copy is `seo-meta-generator`'s job.

---

## Article Outline (revision 2), 12 sections

Structure is the review's "Recommended structure", applied verbatim (decisions §D, final row).
Sections are numbered 1 to 12 to match the review's list so feedback maps cleanly.

**Global rules for the rewrite:**

- Target **2,650 words ±150**, down from v1. Per-section targets below sum to 2,650 exactly.
- `v1_disposition` tells the writer whether to carry v1 text across or start from scratch. `keep`
  means the v1 prose is the base and only the listed edits apply.
- Every figure comes from an `FX-*` claim listed on the section. No section may cite a claim not
  listed on it, and no section may stretch a claim past what its text actually says.
- Number formats are fixed: `96-97%`, `1.5-2.0 cm`, repeatability as the approved sentence, height
  range as `150 to 220 cm`. Hyphens, never en or em dashes, anywhere in the article.

**No-repeat rule (review structure note: "repeated limitations across the body, FAQ, and FitXpress
section").** Each of these is stated exactly once:

| Statement | Its one home | Where it may be referenced without restating |
|---|---|---|
| Full product boundary, including the medical-device sentence | Section 9 | Section 10, one sentence on program decisions |
| Accuracy figures (FX-001, FX-002) | Section 8 | Section 4 links to the accuracy framework, no numbers |
| Approved repeatability sentence (FX-003) | Section 4 | Section 8 names repeatability as a separate property, no restatement of the figure |
| Population coverage clause (FX-011) | Section 8, one clause | Nowhere else. Section 9 carries no training-data or demographic figure at all |
| Output list (BMI, BMR, body fat percentage, lean mass, fat mass, 80+ body measurements, 3D model) | Section 2 | Section 9 and FAQ Q1/Q2 refer to it without re-listing |
| HIPAA | Section 8, one mention, as something to ask about | Nowhere else, including the FAQ |
| Wellness Rewards handoff | Section 10 | Section 12 routing link |

---

### Section 1. Introduction and scope

- **Goal:** open on the limited visibility a wellness platform has into physical progress between
  check-ins, then fix the hub's scope so the reader knows in 30 seconds what this hub covers and
  where the adjacent topics live.
- **Target word count:** 210
- **Must-cover:**
  - The new frame (review item 4): between check-ins, a platform sees self-reported entries and
    scale weight, and neither is comparable to itself months later. Visibility is the problem,
    engagement is an outcome, retention is not promised.
  - One sentence naming the plural audience: consumer wellness apps, lifestyle-change platforms,
    nutrition and habit-coaching products, digital wellbeing ecosystems, human-led and automated
    coaching. Corporate wellness appears as one application, never as the frame.
  - Scope note (review item 1): this hub covers non-clinical wellness platforms, lifestyle and
    nutrition coaching, habit-building and progress-tracking apps, and member and employee wellness
    experiences.
  - The three redirects, as anchor links, inside the scope note: workout programming and performance
    belong to the AI in Fitness hub; patient monitoring belongs to healthcare and telehealth
    content; incentive verification belongs to the Wellness Rewards hub.
- **Keywords to weave:** `wellness platform` (150 / KD 36, primary, in the first paragraph) ·
  `wellness platforms` (150 / KD 2) · `wellness app` (1000 / KD 1)
- **Sources:** `audience.md` layers 3 and 4 · `use-cases/fx-digital-fitness.md` · the three redirect
  URLs (fitness hub, telehealth hub, Wellness Rewards hub)
- **Approved claims:** none. This is the buyer's situation, not our proof.
- **Boundary:** describe program visibility, never health risk. No "members at risk". "This hub" is
  the one permitted self-reference (terminology guardrails Part 2 allows it in a scope note only).
- **v1_disposition:** `rewrite` (merge-from: v1 intro paragraph + v1 H2.1 "Wellness platforms lose
  members before the program works"). The retention frame is replaced, not trimmed, and all five
  flagged phrases are gone. The scope note is new material.
- **Review items closed:** 1, 2, 4

### Section 2. What AI body data means for wellness platforms

- **Goal:** the definitional short-answer block, extractable by answer engines. **This is the
  designated primary-keyword-carrying section**, and its opening sentence must contain the singular
  exact match `wellness platform`.
- **Target word count:** 250
- **Must-cover:**
  - Definition: structured body measurements and body composition **estimates**, captured remotely,
    repeatably, and timestamped so two check-ins are comparable. Never "values" (review item 13).
  - The output list, exactly and only this (decisions §B3, corrected 2026-09-02): BMI, BMR, body fat
    percentage, lean mass, fat mass, 80+ body measurements, and a 3D model.
    **Essential fat and beneficial fat do not appear. `predicted weight` does not appear either**,
    it is in the reviewer's list but in none of ours, and no approved claim supports it.
  - Capture in one sentence: two photos, front and side, results in under 45 seconds.
  - The one clause rescued from the deleted "Why this matters now" (review item 5, decisions §D row
    5): smartphone capture makes structured body data available without dedicated scanning hardware.
    A clause, not a paragraph, and no claim about budgets or expectations.
  - One sentence flagging that comparability depends on repeatability, with the treatment left to
    sections 4 and 8.
  - Two or three sentences on why weight and BMI alone under-describe change, then the Beyond BMI
    link. Do not restate Beyond BMI's argument.
  - The framing boundary in one sentence: this is a data input to a program, not an assessment of a
    person.
- **Keywords to weave:** `wellness platform` (150 / KD 36, heading and opening sentence) ·
  `wellness platforms` (150 / KD 2) · `ai body data` (10 / KD null) · `ai body` (400 / KD 8) ·
  `body composition tracking` (50 / KD null)
- **Sources:** `proof-points.md` · `how-it-works.md` · `use-cases/fx-digital-fitness.md` ·
  `/content-hub/beyond-bmi-business/`
- **Approved claims:** FX-006, FX-007, FX-008. **FX-009 supports only BMI, BMR, body fat percentage,
  lean mass and fat mass here**: its "essential fat, beneficial fat" wording is cut per decisions
  §B3, and it contains no weight output, so it may not be cited for one. **No weight figure and no
  "predicted weight" output in this article.** FX-005 (weight estimation, ±3.5%) is a separate
  proof-point belonging to Smart Scales mismatch flagging, not to the composition output list, and
  it is not cited anywhere in this article. See open item 3.
- **Boundary:** body composition estimates are outputs, never a health verdict. No risk-marker
  language.
- **v1_disposition:** `rewrite` (merge-from: v1 H2.2 "What body data means for a wellness platform"
  + one clause from the deleted v1 H2.3). The definition and the Beyond BMI paragraph survive in
  substance; the output list and the "values to estimates" change are mandatory.
- **Review items closed:** 2, 5 (the surviving clause), 13

### Section 3. Where body data creates value: summary table

> The review's heading uses an em dash. Rendered here with a colon; the dash ban is absolute.

- **Goal:** give the hub a scannable value map immediately after the definition so the page functions
  as a hub instead of a long linear argument (review item 6).
- **Target word count:** 80 (a two-sentence lead-in plus the table; cells are not prose)
- **Must-cover:**
  - The reviewer's five rows verbatim, three columns (Wellness objective · Body-data contribution ·
    Platform application): Progress visibility / Repeatable baseline and later records /
    Baseline-to-current comparison · Personalization / Starting measurements and change trends /
    Goal-relevant content or coaching · Engagement / Meaningful recurring feedback / Progress views
    and milestone check-ins · Coaching / Structured longitudinal context / Better-informed coaching
    conversations · Program insights / Consistent timestamped records / Adoption and progress
    reporting.
  - No extra rows. No numbers in the table. No product name in the table.
- **Keywords to weave:** `wellness platforms` (150 / KD 2) in the lead-in
- **Sources:** review item 6 (the table is supplied) · `use-cases/fx-digital-fitness.md` for the
  lead-in framing
- **Approved claims:** none. Nothing in this table is a measured claim.
- **v1_disposition:** `new`
- **Review items closed:** 6

### Section 4. Progress visibility beyond scale weight

- **Goal:** the article's most differentiated theme, protected. What repeatable body data shows that
  scale weight may not, and why comparability is the property that makes it work.
- **Target word count:** 330 (the largest section, down from roughly 430 in v1)
- **Must-cover (all four retained per review item 7):**
  - the explanation of changes that scale weight may not show;
  - baseline-to-current 3D comparison;
  - the distinction between accuracy and repeatability, stated as two properties evaluated
    separately;
  - the recommendation to show only goal-relevant metrics and hold the rest server-side, with body
    fat percentage handled as a trend line and not a headline number.
- **Mandatory edits to the kept v1 text (this is the whole edit list, nothing else changes):**
  1. **"The story the product tells is now accurate, and accurate is more motivating than
     optimistic"** becomes language around providing **"a more complete view of progress"**. This is
     the one sentence-level change review item 7 asks for, and it is not optional.
  2. Replace v1's internal-validation prose with the approved formulation, verbatim: *"For most
     evaluated measurements, repeated scans showed typical scan-to-scan differences of less than
     1 cm."*
  3. Cut the measurement-level girth figures (chest 0.60 cm, waist 0.89 cm), the ">95 percent
     repeatability consistency" phrasing, and "detailed methodology available under a
     non-disclosure agreement" (review item 16, decisions §B4). FX-016 is not cited anywhere in
     revision 2.
  4. Soften "Repeatability is the property that determines whether this works at all" to
     repeatability being **especially important for longitudinal tracking** (review item 16).
  5. Move the engagement half of v1's closing paragraph to section 6, so the two sections do not both
     argue engagement. What stays here is the measurement point.
  6. Trim to 330 words.
- **Keywords to weave:** `wellness app` (1000 / KD 1) · `body composition tracking` (50 / KD null) ·
  `body composition tracking app` (10 / KD null)
- **Sources:** `proof-points.md` (repeatability) · `/content-hub/mobile-body-scanning-accuracy/`
  (link once, do not restate)
- **Approved claims:** FX-003, expressed **only** through the approved repeatability sentence.
  FX-004 is not cited here. FX-001 and FX-002 belong to section 8. FX-016 is cut.
- **Boundary:** no retention or engagement uplift number. None exists for a wellness deployment
  (context pack `claim_gaps`). Write the mechanism.
- **v1_disposition:** `keep` (v1 H2.6 "Progress visibility: what changes when members can see
  change") with the six edits above. This is the only `keep` in the article.
- **Review items closed:** 7, 16 (the repeatability half)

### Section 5. Personalization using goals, starting points, and trends

- **Goal:** state what body data adds to personalization and, in the same breath, what it cannot do
  alone.
- **Target word count:** 240
- **Must-cover:**
  - Body data is one input among several. Name the six the review asks for (item 8): the user's
    stated goals, preferences, activity and habit information, schedule and available resources,
    relevant limitations, and previous progress.
  - What a measured baseline plus a trend adds that an onboarding survey cannot: a starting point
    that updates as the person changes.
  - Grouping members by measured starting point is **retained**, with aggregated reporting, purpose
    limitation, and appropriate privacy controls named in the same paragraph (review item 8,
    decisions §D row 8).
  - One or two sentences routing nutrition and lifestyle coaching to the planned P1 cluster row,
    without promising a link to a page that does not exist yet.
- **Keywords to weave:** `wellness app` (1000 / KD 1) · `wellness tracker app` (150 / KD 5)
- **Sources:** `use-cases/fx-digital-fitness.md` · `messaging.md` · `audience.md` layer 3
- **Approved claims:** none required. Do not re-cite FX-008 or FX-009 here; the output list is stated
  once, in section 2.
- **Boundary:** never suggest that measured body data alone defines appropriate targets or nutrition
  intake (review item 8). No calorie, macro, or training recommendation attributed to a scan. v1's
  "Targets become specific to the member instead of generic to the cohort" does not survive.
- **v1_disposition:** `rewrite` (merge-from: v1 H2.5 "Personalization: from stated goals to measured
  starting points"). The re-personalization idea and the honest-limit paragraph survive in
  substance; the targets claim and the cohort paragraph are rewritten.
- **Review items closed:** 2, 8

### Section 6. Engagement and coaching

- **Goal:** make the engagement case in supportive language, then add the wellness-specific
  user-experience considerations. This section is the clearest separation between this hub and both
  the fitness hub and weight-management content.
- **Target word count:** 270
- **Must-cover:**
  - The reviewer's four formulations, used as the ceiling on engagement language (review item 9):
    "supports more meaningful feedback", "can make progress easier to understand", "creates an
    additional check-in opportunity", "can contribute to continued engagement".
  - Coaching: a repeatable record gives a human coach a starting point and a change record to work
    from. In automated programs it feeds content selection and progress display, and judgement about
    a member stays with a person.
  - The five wellness user-experience points, new material (review item 10): body-data features
    should be optional and goal-led; not every wellness journey requires body measurement; visual
    comparisons should use neutral, non-judgemental language; progress should not be reduced to
    appearance or weight loss; users should be able to control which indicators they see.
- **Keywords to weave:** `app engagement` (400 / KD 7) · `wellness coach app` (200 / KD 0) ·
  `wellness app` (1000 / KD 1)
- **Sources:** `about-me.md` (claims discipline) · `audience.md` layer 3 ·
  `use-cases/fx-digital-fitness.md`
- **Approved claims:** none. No engagement or retention figure exists for any FitXpress wellness
  deployment, and any "improves retention by X%" claim would be fabricated (context pack
  `claim_gaps`).
- **Boundary:** no causal claim, in any direction, between body scanning and retention. Review
  item 9 asked for a neutral third-party source on self-monitoring and feedback; none is approved,
  so this section argues from mechanism only. **Do not invent a citation.** See open item 1.
- **v1_disposition:** `new` for the five user-experience points, plus
  `merge-from: v1 H2.4` (the coach-and-administrator-in-the-loop paragraph) and
  `merge-from: v1 H2.6` (the closing engagement-limit paragraph, moved here from section 4).
- **Review items closed:** 2, 9, 10

### Section 7. Practical wellness-platform workflow

- **Goal:** one short workflow that replaces both of v1's process sections, plus the shortened pilot
  metric list. Carries the second placement of the primary keyword.
- **Target word count:** 250 (down from roughly 740 across the two v1 sections)
- **Must-cover:**
  - The reviewer's five steps, in order (review item 11): 1) consent and baseline capture;
    2) selection of goal-relevant outputs; 3) result presentation; 4) recurring capture under
    consistent conditions; 5) comparison and connection to the platform's next step.
  - Cadence in one sentence: an interval matched to the pace at which change is measurable, with four
    to twelve weeks as a practical range.
  - Division of labour in one or two sentences: the platform owns program logic and the member
    relationship, the body-data layer owns capture, measurement output, and the comparable record.
  - The five pilot measures (review item 12): scan completion rate, retake rate, second-scan rate,
    engagement with the progress view, and user understanding of the displayed results. Continued
    participation may be compared, with no implication that scanning is the cause of higher
    retention.
- **Keywords to weave:** `wellness platform` (150 / KD 36, second placement, hyphenated in the
  heading) · `wellness program software` (100 / KD 1)
- **Sources:** `how-it-works.md` · `tech-spec.md` · `use-cases/fx-digital-fitness.md`
- **Approved claims:** FX-006, FX-007, on the capture step only, one mention.
- **Boundary:** cut both anxiety phrasings (review item 11): nothing suggesting that integrations
  commonly fail, and nothing about capture quality being "won or lost in the first ten seconds". No
  implementation timelines, no effort estimates in days, no pricing.
- **v1_disposition:** `merge-from: v1 H2.4 "Where body data fits in a wellness program workflow" +
  v1 H2.10 "Adding body scanning to a wellness product"`. Both v1 sections cease to exist as
  sections; their usable content is compressed into the five steps and the five metrics.
- **Review items closed:** 11, 12

### Section 8. What to evaluate in a body-data provider

- **Goal:** the evaluation framework. This is the MOFU value of the hub and the anchor for both trust
  assets.
- **Target word count:** 260
- **Must-cover:**
  - Accuracy asked properly: accurate enough for which decision, against which reference method,
    under which capture protocol, for which population, at what tolerance. Link to the accuracy
    framework as the canonical source. If a figure appears at all, it is `96-97%` and `1.5-2.0 cm`,
    formatted exactly (decisions §B4).
  - Accuracy and repeatability **evaluated separately**, with repeatability especially important for
    longitudinal tracking and the acceptable error depending on the expected magnitude of change and
    on the workflow (review item 16).
  - **Population coverage, one clause** (decisions §B2): ask a provider what population its model was
    validated on, and state ours once as ages 16 to 78, heights **150 to 220 cm**, weights 38 to
    210 kg, collected across the US and Europe. One clause, not a paragraph. There is no
    training-data enumeration anywhere in revision 2. The figure matches the live accuracy article
    this section links to, so the two pages agree in public.
  - Capture reliability across a distributed population: phones, lighting, clothing, pose validation,
    retake handling, and whether guided capture is supplied or has to be built.
  - Privacy and data handling as a procurement gate, using the approved wordings from decisions §C
    and nothing else: the GDPR role sentence ("In most enterprise deployments, the customer acts as
    controller and 3DLOOK acts as processor under GDPR."); photos permanently removed immediately
    after processing or within 30 days depending on the client's configured policy; photos
    automatically blurred when stored; Amazon S3 in the client's region with server-side encryption
    (SSE-S3) always on; no personal identifiers processed; photos not used to train the model.
  - Integration effort: how long until a member can complete a check-in inside the existing product
    and see a comparison.
  - First use of dual-energy X-ray absorptiometry (DXA) if a reference method is named here, DXA
    thereafter (review item 14).
- **Keywords to weave:** `corporate wellness platform requirements` (10 / KD null) ·
  `corporate wellness platform integrations` (30 / KD null) ·
  `benefits of corporate wellness platform` (20 / KD null)
- **Sources:** `/content-hub/mobile-body-scanning-accuracy/` · `compliance.md` · `about-me.md` ·
  `proof-points.md` (height row, updated 2026-09-02)
- **Approved claims:** FX-001 and FX-002 (only if a figure is used, formatted per decisions §B4),
  FX-003 (named as a separate property, the sentence itself lives in section 4), **FX-011 (the
  population-coverage clause, 150 to 220 cm as updated in the context pack on 2026-09-02)**, FX-014
  as a single procurement line. FX-015 may be cited **only** as a separate benchmark with its own
  reference stated, never combined with FX-001, FX-002 or FX-003. FX-010 is not cited here or
  anywhere.
- **Boundary:** never reduce accuracy to one universal number. **HIPAA appears exactly once in the
  whole article, here, as something to ask about** (review item 20, decisions §C). **SOC 2 is never
  mentioned**, it is not certified. Cut all three absolute statements from v1: the 2-centimetre
  tolerance line, "repeatability outranks accuracy", and "treat a provider who conflates the two as
  having answered neither". The privacy FAQ link stays a `<!-- TODO(publish) -->` marker until the
  trust asset ships.
- **v1_disposition:** `rewrite` (merge-from: v1 H2.9 "What a corporate wellness platform should
  evaluate in a body-data provider"). The filter structure survives; the three absolute statements,
  the vague "follows GDPR principles" line, and the free-standing HIPAA mentions are replaced. The
  population-coverage clause moves here from v1 H2.8, with the corrected figure.
- **Review items closed:** 14, 15, 16, 20

### Section 9. Where FitXpress fits

- **Goal:** place the product, then state the boundary once, compressed. This is the article's only
  full statement of the boundary.
- **Target word count:** 210 (down from roughly 420 in v1)
- **Must-cover:**
  - What FitXpress is here: the capture and structured-data layer inside the platform's own product.
    Two photos in, 80+ measurements and body composition estimates out, in under 45 seconds.
  - Integration, corrected (review item 17): **API, web SDK, and mobile SDKs.** "API or camera SDK"
    does not survive.
  - The provide-and-build boundary: the platform keeps onboarding, consent wording, the scan entry
    point, result display, and which metrics appear at all.
  - The boundary, compressed into one or two paragraphs instead of a five-item list (review item 19):
    **"It is not positioned as a medical device."** verbatim (licensed exception, decisions §A2 and
    `terminology-guardrails.md` §2.10 re-reversal of 2026-09-02); no diagnosis and no screening;
    decisions about program access stay with the program; reference methods including dual-energy
    X-ray absorptiometry (DXA) and bioelectrical impedance analysis (BIA) answer different questions
    and are not replaced; adding capture does not make a program compliant.
  - Fraud, corrected (review item 18): FitXpress can provide capture-quality and verification
    signals, and it does not make final fraud determinations. "It does not detect fraud" does not
    survive.
  - The evaluation CTA sits at the end of this section, where credibility peaks: one link down to
    `/fitxpress/for-connected-and-digital-fitness/`.
- **Keywords to weave:** `3d body scanning app` (100 / KD null) · `body scanning app` (60 / KD 26)
- **Sources:** `about-me.md` · `proof-points.md` · `tech-spec.md` ·
  `/fitxpress/for-connected-and-digital-fitness/` (which supports the broader integration wording) ·
  `terminology-guardrails.md` §2.10
- **Approved claims:** FX-006, FX-007, FX-008. If the output set is named again here (preferably it
  is not, see the no-repeat rule), it is the section 2 list and nothing more. **FX-010 is not cited
  in revision 2** and the training-data enumeration is deleted, replaced by a link to the accuracy
  framework (decisions §B2). **FX-011 lives in section 8, not here.** FX-005 is not cited either.
- **Boundary:** this section is the boundary. Write it in the same breath as the capability, not as a
  disclaimer footer, and do not restate it in section 10 or in the FAQ beyond what the no-repeat rule
  allows.
- **v1_disposition:** `rewrite` (merge-from: v1 H2.8 "Where FitXpress fits, and what it does not
  do"). Same job, half the words, with five mandatory wording corrections, the training-data
  enumeration deleted, and the population clause moved to section 8.
- **Review items closed:** 13, 14, 15, 17, 18, 19

### Section 10. Boundaries and related hubs

- **Goal:** hold the cannibalization line inside the text: name what this hub does not cover, route
  each adjacent topic to its owner, and give employer and insurer wellness its one short subsection.
- **Target word count:** 160
- **Must-cover:**
  - The employer and insurer subsection, exactly three points (review item 3, decisions §D row 3):
    standardized capture can support distributed wellness programs; reward-linked applications
    require additional governance and review; the Wellness Rewards hub covers verification in depth
    (link). Nothing else. No verification workflow, no fairness, dispute, audit-trail, eligibility
    or payment treatment.
  - Corporate wellness named explicitly as one application of the hub's subject, not its frame.
  - Related-hub routing, one line each: workout programming and performance to AI in Fitness;
    patient monitoring to healthcare and telehealth; measurement-method comparison to how to measure
    body composition; the broader map up to the Main Health hub.
  - One sentence, not a repeat of section 9: decisions about members and program access stay with
    the program, and a person stays responsible for them.
- **Keywords to weave:** `corporate wellness` (1000 / KD 3) · `corporate wellness platform`
  (500 / KD 11, secondary, this subsection and the meta description are its only two homes) ·
  `workplace wellness app` (150 / KD 1) · `employee wellness app` (100 / KD 6) ·
  `employee wellness program` (700 / KD 47, mentioned in passing, not targeted)
- **Sources:** `use-cases/fx-wellness-rewards.md` · the Wellness Rewards sub-hub URL ·
  `ai-in-fitness-industry` · `how-to-measure-body-composition` · `ai-body-data-health-hub`
- **Approved claims:** none. **Never publish the internal wellness-rewards TAM/SAM figures** from
  the use-case file (context pack `claim_gaps`).
- **Boundary:** the highest-drift section in the article. Never imply that a scan decides a reward,
  an incentive tier, program access, or eligibility. Keep claims soft.
- **v1_disposition:** `merge-from: v1 H2.7 "Employer and insurer wellness programs: participation,
  rewards, and reporting"`, reduced from roughly 430 words to a three-point subsection inside a
  160-word section. The standalone section is cut, see the deletions ledger.
- **Review items closed:** 1, 2, 3

### Section 11. Focused FAQ

- **Goal:** the GEO and AEO extraction surface. Six questions, 2 to 4 sentences each (§14
  guidelines).
- **Target word count:** 300
- **Questions (6, down from 7 in v1):**
  1. What is AI body data, and what does a wellness platform get from it?
  2. How does a remote body scan work for a wellness check-in?
  3. Can a body scan replace a DXA scan, a BIA device, or a calibrated scale? *(No. Different
     reference methods answer different questions. Its value in a wellness program is frequency and
     consistency. Reference the accuracy framework without a second link.)*
  4. Is body data used to make decisions about members or their access to a program? *(No. The scan
     produces a record; program decisions are made by the program under its own rules and a person
     stays responsible.* **Rewards are named in neither the question nor the answer**, see the
     deletions ledger.*)*
  5. What data is captured and stored, and what happens to the photos? *(Approved decisions §C
     wordings only: retention, automatic blur when stored, regional storage, no personal
     identifiers, photos not used to train the model. HIPAA does not appear, its single mention is
     spent in section 8.)*
  6. How often should a wellness program run check-in scans?
- **Keywords to weave:** `wellness app` (1000 / KD 1) · `body composition tracking` (50 / KD null) ·
  `ai body data` (10 / KD null)
- **Sources:** `compliance.md` · `proof-points.md` · `how-it-works.md` ·
  `/content-hub/mobile-body-scanning-accuracy/`
- **Approved claims:** FX-006, FX-007, FX-008 (Q2); FX-009 in Q1 **only** for BMI, BMR, body fat
  percentage, lean mass and fat mass. No weight output and no "predicted weight" in any answer. No
  demographic or height figure in the FAQ; FX-011 is spent in section 8.
- **Boundary:** Q3 and Q4 are the guardrail questions. Answer both plainly and in the negative. Every
  instance of DEXA becomes DXA (review item 14). `<!-- TODO(publish) -->` marker on Q5's privacy
  link.
- **v1_disposition:** `rewrite` (merge-from: v1 FAQ). Seven questions become six: v1's "What does
  FitXpress not do?" is cut under the no-repeat rule, v1's Q4 loses its rewards framing, Q3 is
  respelled to DXA, and Q5 is rewritten to the approved wordings.
- **Review items closed:** 3, 14, 20

### Section 12. Conclusion and CTA

- **Goal:** route by readiness, three routes, one short block. Intent is Hub, so the CTA is layered
  rather than a single hard ask (§15 guidelines).
- **Target word count:** 90
- **Must-cover:**
  - Soft route, still learning: Main Health hub, with Beyond BMI as the educational bridge.
  - Evaluation route: FitXpress for connected and digital fitness, for integration options and the
    shape of the returned data.
  - Employer or insurer route: the Wellness Rewards Verification sub-hub.
  - One closing sentence restating the hub's own claim in supportive language: repeatable body data
    can give a wellness platform a more complete view of progress between check-ins.
- **Keywords to weave:** none forced. Do not open this block with `corporate wellness platform` the
  way v1 did; that framed the whole conclusion around employers.
- **Sources:** the four internal-link targets
- **Approved claims:** none.
- **Boundary:** one primary CTA plus two secondary routes. No repeated demo banner between sections.
- **v1_disposition:** `rewrite` (merge-from: v1 "Where to go next"), compressed from roughly 150
  words to 90.
- **Review items closed:** 2

---

## Article meta

| Section | Title | Words | v1_disposition |
|---|---|---|---|
| 1 | Introduction and scope | 210 | rewrite (v1 intro + v1 H2.1) |
| 2 | What AI body data means for wellness platforms | 250 | rewrite (v1 H2.2 + clause from v1 H2.3) |
| 3 | Where body data creates value: summary table | 80 | new |
| 4 | Progress visibility beyond scale weight | 330 | **keep** (v1 H2.6, 6 edits) |
| 5 | Personalization using goals, starting points, and trends | 240 | rewrite (v1 H2.5) |
| 6 | Engagement and coaching | 270 | new + merge-from v1 H2.4, v1 H2.6 |
| 7 | Practical wellness-platform workflow | 250 | merge-from v1 H2.4 + v1 H2.10 |
| 8 | What to evaluate in a body-data provider | 260 | rewrite (v1 H2.9 + population clause from v1 H2.8) |
| 9 | Where FitXpress fits | 210 | rewrite (v1 H2.8) |
| 10 | Boundaries and related hubs | 160 | merge-from v1 H2.7 (reduced to a subsection) |
| 11 | Focused FAQ | 300 | rewrite (v1 FAQ, 7 questions to 6) |
| 12 | Conclusion and CTA | 90 | rewrite (v1 "Where to go next") |
| | **Total** | **2,650** | |

- **Target:** 2,650 words, tolerance ±150 (2,500 to 2,800, which is the review's own range).
  Decisions §D records v1 at 4,035 words; `v1/final.md` frontmatter records 3,428, counted
  differently. The cut is the same instruction either way, and 2,650 is the number to write to.
- **Estimated read time:** 10 to 11 minutes
- **Sections:** 12 (10 content, FAQ, CTA)
- **CTA placement:** evaluation CTA at the end of section 9, layered CTA block in section 12.
  Nowhere else.
- **Proposed URL slug:** `ai-body-data-wellness-platforms` (unchanged)
- **Author:** Assel Sekerova (unchanged)
- **Internal links (final list, unchanged from v1):**
  - up: `/content-hub/ai-body-data-health-hub/`
  - side: `/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` ·
    `/content-hub/beyond-bmi-business/` · `/content-hub/ai-in-fitness-industry/` ·
    `/content-hub/how-to-measure-body-composition/` · telehealth content (review item 1 redirect)
  - down: `/fitxpress/for-connected-and-digital-fitness/`
  - trust: `/content-hub/mobile-body-scanning-accuracy/` · Data, Privacy, Security & Regulatory FAQ
    (pending, TODO marker)
  - **inbound (publish step, not writing):** links INTO this hub from `ai-in-fitness-industry` (326
    backlinks) · `the-potential-of-ai-in-telehealth` (263) · `glp-1-market` (183) ·
    `top-fitness-industry-trends` (36) · `weight-loss-industry-overview` (33). This hub inherits no
    external authority from Beyond BMI (1 backlink) or Wellness Rewards (0), so the inbound pass is
    what makes it rankable, and the move to a KD 36 primary makes it more important, not less. All
    links use canonical trailing-slash URLs.

---

## Deletions ledger

What is cut, where it lived in v1, and on what basis. Nothing in this table may reappear in
revision 2.

| # | Cut | Where it was in v1 | Basis |
|---|---|---|---|
| 1 | **"Why this matters now for wellness platforms", the whole section**, including all four arguments ("Workforces distributed", "Budgets came under review", "Capture stopped requiring hardware", "Members expect more") and both dismissive budget claims (wellness spend that "once passed on goodwill", self-report not surviving finance scrutiny) | v1 H2.3, ~190 words | Review item 5, decisions §D row 5. No third-party evidence exists for the four claims. One clause survives in section 2: smartphone capture makes structured body data available without dedicated hardware |
| 2 | **The standalone employer and insurer section**, with its verification, fairness, incentive, review, eligibility, payment-decision and audit-trail coverage | v1 H2.7, ~430 words | Review item 3. It duplicates the Wellness Rewards page. Reduced to a three-point subsection in section 10, then a link out |
| 3 | **The standalone implementation section** "Adding body scanning to a wellness product" | v1 H2.10, ~310 words | Review item 11. Merged into section 7 as the five-step workflow plus the five pilot metrics |
| 4 | **The detailed training-data paragraph**, meaning the enumeration: 9+ years of data, 150,000+ photographs, 30,000+ 3D scans, 430,000+ individual measurements, and the gender split | v1 H2.8 | Review item 15 on its own ground, "the detailed training-data paragraph is not essential to this hub", plus the 2,650-word target. **This is a hub-appropriateness and length cut, not a figure dispute:** the height figure is settled (see row 9). **FX-010 goes uncited.** **FX-011 remains citable** and the population-coverage point survives as one clause in section 8: ages 16 to 78, heights 150 to 220 cm, weights 38 to 210 kg, US and Europe. What is cut is the enumeration and the paragraph shape, not the population fact |
| 5 | **Measurement-level repeatability figures** (chest 0.60 cm, waist 0.89 cm), the ">95 percent repeatability consistency" phrasing, and the "detailed methodology available under a non-disclosure agreement" remark | v1 H2.6 | Review item 16, decisions §B4. Too detailed for this hub; they stay in technical validation materials. **FX-016 is not cited in revision 2** |
| 6 | **The rewards FAQ question**, in its v1 form "Is body data used to make decisions about members, rewards, or eligibility?" | v1 FAQ Q4 | Review item 3, decisions §D row 3. The decisioning boundary survives as FAQ Q4 with rewards removed from both the question and the answer. Reward decisioning is covered in section 10 in three points and owned by the Wellness Rewards hub |
| 7 | **"essential fat" and "beneficial fat"** from the output list | v1 H2.2 and v1 FAQ Q2 | Review item 13, decisions §B3. The list becomes BMI, BMR, body fat percentage, lean mass, fat mass, 80+ body measurements, 3D model. FX-009 may be cited only for the five composition terms it shares with that list. Divergence flagged: `proof-points.md`, `how-it-works.md` and FX-009 itself still list both cut terms, see open item 3 |
| 8 | **`predicted weight`, not added** (corrected 2026-09-02) | Never in v1; the reviewer's documented output set proposes it | Decisions §B3. It appears nowhere in `brand-assets/product-info/` and FX-009 does not contain it. The only weight figure we hold is a separate proof-point (weight estimation, ±3.5%, `proof-points.md` line 21) that belongs to Smart Scales mismatch flagging, not to the composition output list. Publishing it as a composition output would be an unsupported claim, and the hub does not need it. **`seo-writer` must not add it** |
| 9 | **The old height figure, 150 to 205 cm** | v1 H2.8 | Decisions §B2, resolved 2026-09-02. Wherever a height appears in this article it is **150 to 220 cm**, one figure covering both training-data coverage and the internal validation population. v1's number was wrong, not disputed, and the live accuracy article already publishes the correct one, so nothing needs a CMS edit |

**Also cut by the same items, recorded so the writer does not reintroduce them:**

| # | Cut phrasing | Basis |
|---|---|---|
| 10 | The five flagged opening claims: "By roughly the ninety-day mark", "retention pays for itself every month", "The problem is rarely that nothing changed", "The scale reports failure", and the implied causal link between visible body change and retention | Review item 4 |
| 11 | The three absolute accuracy statements: "A 2-centimetre waist tolerance is irrelevant for a wellness progress chart", "repeatability outranks accuracy", "treat a provider who conflates the two as having answered neither" | Review item 16 |
| 12 | Two implementation-anxiety phrasings: the "getting it wrong is how these integrations become expensive" / "most common way to end up with disappointing measurements" pair, and "Capture quality is won or lost in the first ten seconds" | Review item 11 |
| 13 | "It does not detect fraud" (replaced by capture-quality and verification signals with no final fraud determinations) and "FitXpress is not a medical device" (replaced by "It is not positioned as a medical device.") | Review items 18 and 19, decisions §A2 |
| 14 | "API or camera SDK" (replaced by API, web SDK, and mobile SDKs) | Review item 17 |
| 15 | "follows GDPR principles" (replaced by the controller and processor role sentence) | Review item 20, decisions §C |
| 16 | Every instance of DEXA, including "dual-energy X-ray absorptiometry (DEXA)" (replaced by DXA) | Review item 14, decisions §B1. Divergence flagged: DEXA is still the house spelling in `terminology-guardrails.md` §1, `editorial-guardrails.md` #7, the Part 3 grep row, and ten-plus published articles, so the next article regenerates DEXA until Vadim takes that call. See open item 2 |
| 17 | "body composition values" (replaced by "body composition estimates" throughout) | Review item 13, decisions §B3 |
| 18 | v1's five-item bulleted limitations list as a list | Review item 19: compressed into one or two paragraphs in section 9 |

---

## Review item coverage map

Every one of the 20 items lands in at least one section or in the deletions ledger.

| Item | Subject | Where it lands |
|---|---|---|
| 1 | Scope note immediately after the intro | Section 1 (scope note plus three linked redirects), Section 10 (routing) |
| 2 | Broaden beyond corporate wellness | Sections 1, 2, 5, 6, 10, 12 plus the keyword re-decision |
| 3 | Cut the employer and insurer section | Section 10 (three points, link out), Section 11 (rewards FAQ removed), Deletions 2 and 6 |
| 4 | Rework the opening | Section 1, Deletions 10 |
| 5 | Remove "Why this matters now" | Deletions 1, with one clause in Section 2 |
| 6 | Value-map table | Section 3 |
| 7 | Keep progress visibility strongest | Section 4 (`keep`, with the "more complete view of progress" edit as mandatory) |
| 8 | Balance personalization | Section 5 |
| 9 | Engagement supportive, not causal | Section 6, plus open item 1 for the missing third-party source |
| 10 | Wellness user-experience consideration | Section 6 (new material) |
| 11 | Merge workflow and implementation | Section 7, Deletions 3 and 12 |
| 12 | Shorten pilot metrics | Section 7 (the five measures) |
| 13 | Output list | Section 2 (list and "estimates"), Section 9, Section 11 Q1, Deletions 7, 8 and 17 |
| 14 | DEXA to DXA | Sections 8, 9, 11, Deletions 16 |
| 15 | Training-data paragraph | Section 8 (one-clause population coverage at 150 to 220 cm), Section 9 (enumeration removed), Deletions 4 and 9 |
| 16 | Accuracy discussion | Section 4 (repeatability formulation), Section 8 (the framework), Deletions 5 and 11 |
| 17 | Integration wording | Section 9, Deletions 14 |
| 18 | "It does not detect fraud" | Section 9, Deletions 13 |
| 19 | Medical-device wording plus compressed limitations | Section 9, Deletions 13 and 18 |
| 20 | Privacy and compliance language | Section 8 (approved wordings, single HIPAA mention), Section 11 Q5, Deletions 15 |
| structure | 12-section outline | Applied verbatim as Sections 1 to 12 |
| length | 2,500 to 2,800 words | 2,650 exactly across the section table |

**Unclosed items: none.**

---

## Publish-step and CMS tasks (transferred unchanged, all still owed)

These are not writing tasks. They are the reason the page can rank at all.

1. **Inbound-link pass** on five live donor pages (`ai-in-fitness-industry`,
   `the-potential-of-ai-in-telehealth`, `glp-1-market`, `top-fitness-industry-trends`,
   `weight-loss-industry-overview`), contextual anchors as tabled above. Needs an owner and a slot.
2. **`published-articles-inventory.md` update:** `wellness-rewards-verification…` moves from hub to
   sub-hub, and the internal-linking map is redrawn with this page as the Hub #8 node.
3. **Internal-link pass on the sub-hub page itself**, which currently links as a hub and may need an
   intro adjustment.
4. **Canonical trailing-slash URLs** on every internal link, given the duplicate and parameterised
   variants in the backlink export.
5. **`<!-- TODO(publish) -->` markers** in sections 8 and 11 resolve to the Data, Privacy, Security &
   Regulatory FAQ once it publishes. Until then, short inline answers stand.

No CMS work is needed on the accuracy article: it already publishes 150 to 220 cm (decisions §B2).

---

## Open items

Five of the six items in decisions §F are still open and listed below. The sixth, the height range,
is **closed** with no follow-ons (see Revision 2 note 9) and is therefore not listed here.

1. **No third-party source on self-monitoring and feedback.** Review item 9 asks for a neutral
   third-party source on self-monitoring, goal setting, and feedback in digital lifestyle programs.
   None is approved. Section 6 argues from mechanism only, and inventing a citation is worse than
   omitting one. If Vadim clears a source, section 6 gets materially stronger.
2. **DEXA and DXA divergence in brand-assets.** DXA is applied in this article. `DEXA` is still the
   house spelling in `terminology-guardrails.md` §1, `editorial-guardrails.md` #7, the Part 3 grep
   row, and ten-plus published articles. Until Vadim takes that call, the next article regenerates
   DEXA. Recommendation from decisions §B1: change the abbreviation lists to DXA, leave published
   articles alone. Owner: Vadim.
3. **essential and beneficial fat vs `predicted weight`.** Two separate divergences between the
   review and `proof-points.md` / FX-009, both owner Vadim (decisions §B3):
   (a) `proof-points.md` line 48, `how-it-works.md` line 25 and **FX-009 itself** still list
   essential and beneficial fat, which the reviewer wants gone. Either the sources are stale or the
   reviewer is wrong about the product.
   (b) The reviewer's documented output set includes `predicted weight`, which **no approved claim
   supports**. This article omits it. If weight estimation really is a composition output, FX-009 and
   `proof-points.md` need the row added first.
4. **"Positioned as" is now in its third state** (#6 2026-06-09, superseded 2026-08-13, partially
   restored 2026-09-02). Review 1 and terminology guardrail §2.10 come from the same authority and
   pointed opposite ways. Three files were changed on 2026-09-02 so this article can pass its own
   lint gate, and the licence covers exactly one sentence. Worth settling in the Doc. Owner:
   editorial owner plus Vadim.
5. **Images still not produced.** Unchanged from v1. Needs design.

### Resolutions applied where the review could be read two ways

Not new open items. Recorded so nobody re-opens them mid-write. In each case the decisions file wins,
per its own header.

- **The recommended structure drops the employer and insurer section entirely, while review item 3
  keeps "one short subsection".** Decisions §D row 3 places that subsection inside section 10. That
  is what this plan does.
- **Review item 5 offers two options** ("add credible third-party evidence *or* shorten"). Decisions
  §D row 5 chooses full removal with one clause folded into section 2, because no evidence exists
  for the four claims. Removal it is.
- **Review item 15 offers two options** ("remove and link *or* update every figure"). Decisions §B2
  takes a hybrid: the enumeration is removed and linked, and the one fact worth keeping (population
  coverage) is kept as a clause with the corrected figure. That is the review's own "not essential to
  this hub" reasoning applied per sentence instead of per paragraph.
- **Review item 15 was also right about which number to doubt.** Our figure of 150 to 205 cm was
  wrong, not merely disputed, and 150 to 220 cm now covers both the training-data and
  validation-population labelling. Fixed at source rather than hedged in the article, and the live
  accuracy article was already correct, so the repo was the side that had drifted.
- **Review item 13 lists `predicted weight` as a documented output.** Decisions §B3 overrides the
  reviewer on a point of fact: no approved claim carries it. Omitted, and logged as open item 3b.
  This is the one place where the review is treated as wrong rather than authoritative, and it is
  the decisions file that says so.
- **Review item 3 removes the rewards FAQ question, while the vertical boundary and §14 both require
  a decisioning question.** Resolution: the rewards framing is removed from the FAQ, and the
  decisioning question stays as FAQ Q4 in a rewards-free form. Reward decisioning is owned by the
  Wellness Rewards hub.
- **§14 guidelines recommend a "What does FitXpress NOT do?" FAQ, while the review's structure note
  bans repeated limitations across the body, the FAQ, and the product section.** The review wins for
  this article. The boundary is stated once in section 9 and reaches the FAQ only through Q3
  (replacement) and Q4 (decisioning), which covers the same two search questions §14 cares about.
- **v1's checkpoint-1 note argued the H1 deliberately omits the head term while the meta title
  carries it.** Decisions §A1 voids that split. Both now carry `wellness platform`.
- **Word count of v1:** decisions §D says 4,035, `v1/final.md` frontmatter says 3,428. Decisions is
  the figure of record; the target of 2,650 is unaffected.
