---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
plan: plan.md
stage: plan
created: 2026-09-19
revised: 2026-10-20 (Review 1 re-plan appended at the end; earlier sections unchanged)
audience: seo-publisher, Vadim, external reviewer
---

# Plan audit: why the plan is what it is

This file explains decisions. Nothing in it is needed to write a section; `plan.md` is the
writing document. When the two files disagree about what to write, `plan.md` governs. This
file records the reasons.

---

## 1. The keyword decision, and what each alternative would have cost

### The finding

`seed_has_data: false`. Four Ahrefs pulls were run on 2026-09-19 (US, API v3):

| Pull | Result |
|---|---|
| Title seed "GLP-1 and fitness apps tracking body composition not just weight" | No data. The auto-picked idea seed `just weight` (150 / KD 0) is junk, and its 40 ideas are workout noise. `glp-1 and` is 30 / no KD. |
| `glp-1 body composition` | **No data** (Ahrefs has no figure, which is not 0). `glp-1 body` is 20 / no KD. Ideas drift to `body composition` (40,000 / KD 35 / TP 2,300, parent `what is body composition`) and scale and shopping terms. |
| `glp-1 muscle loss` | 600 / KD 45 / CPC 8 / **TP 100**, parent `glp1 muscle loss`, informational only. About 40 variants, mostly 30-250 / mo, most with no KD. |
| `glp-1 app` | 100 / no KD, informational plus commercial. Ideas are consumer tracker-app queries (300 / 200 / 150 ...), all with no KD, one branded. |

In the muscle-loss list, many rows are the same question spelled differently ("does glp-1 cause
muscle loss", "does glp 1 cause muscle loss", "do glp 1 cause muscle loss"). They must not be
summed as independent demand.

### Priced alternatives (full)

| Option | Ahrefs (US) | What it would gain | What it would cost |
|---|---|---|---|
| **`glp-1 muscle loss` (chosen)** | 600 / KD 45 / TP 100 | The only measured, on-topic term. No 3dlook.ai page targets it: the GLP-1 hub targets `GLP-1 market growth`, the listicle `remote body composition tools for GLP-1 clinics`, the coaching article `online fitness coaching programs`. It names the problem that both the app team and the GLP-1 program use. The site already has GLP-1 topical depth (hub, listicle, visual progress, BMI verification). | The SERP is consumer and clinical. Most searchers are patients. KD 45 on a health SERP with no clinical reviewer on the byline makes the top 10 unlikely. TP 100 caps the prize even at position 1. The keyword pulls the text toward clinical advice, so `plan.md` carries a "cannot claim" list. An H1 that puts muscle loss next to a vendor that *estimates* lean mass implies a muscle measurement; the scope note in Section 1 must correct it. |
| `glp 1 muscle loss` as the declared primary | 400 / KD 11 | The lowest difficulty in the cluster | The same query written without the hyphen. "GLP 1" in an H1 is the wrong spelling for a B2B page. It rides on the hyphenated H1 anyway. |
| `glp-1 muscle loss prevention` | 250 / KD 37 | Measured, with lower KD than the seed | Advice intent ("how do I prevent it"). This is the worst mismatch: the page would have to prescribe, which the vertical boundary forbids. |
| `glp-1 tracker app free` and cluster | 300; `glp 1 app` 200; `best app for glp 1 tracking` 150; `glp-1 app` 100; all KD no data | Matches "apps" in the row title | Consumer app-store intent: dose and injection logging, with a branded app in the ideas. The SERP wants a roundup that names consumer products. It overlaps the top-7 tools intent. Wrong reader entirely. |
| `body composition tracking` | **not pulled** | Names the method, B2B-neutral | Demand is unknown. The term is generic and sits next to row 167 ("Body Composition Tracking for GLP-1 Patients", P2) and row 126 (recomposition). |
| `body composition` | 40,000 / KD 35 / TP 2,300 | Large head term | Definition intent (`what is body composition` 9,000). That is `how-to-measure-body-composition` territory, and a second primer is what the guidelines forbid. |
| `body composition scan` | 3,100 / KD 35 | Commercial | Product-page territory, not a bridge article. |
| `body composition scale` | 4,400 / KD 20 | Measured | Owned by the live `body-composition-scale` page and row 123 (smart scale comparison). |
| `muscle loss` | 700 / KD 4 / TP 6,600, parent `muscle atrophy` | High traffic potential | Not GLP-1-specific. Background only. |
| Row title phrase | seed_has_data false | Exact intent | No measured demand. On 2026-08-25, `remote-body-measurement-online-fitness-coaching` shipped under an unmeasured primary, and that surfaced only after publication. |

### Why the mismatch is accepted

The page's realistic return is answer-engine coverage and the link path between Hub 1 and Hub 3,
not classical organic volume. Every option has thin or unmeasured demand. Among them,
`glp-1 muscle loss` is the only one that is measured, on-topic and owned by no other page. Its
answer is legitimate for any reader when every figure is sourced and lean mass is kept distinct
from muscle. The cost is a consumer-heavy SERP with low conversion value. That cost is stated at
checkpoint 1, not discovered later in Search Console.

If Vadim rejects a medical-sounding H1 on a vendor page, the fallback is the row title verbatim
with an unmeasured primary, and the price is zero measured demand (Open item 1).

---

## 2. Phase 0 and cannibalization

### Gate reading

- The row is `content-plan.md:122`. The action type reads `Create net-new` verbatim: family
  create-net-new, with no qualifier after `/`, `:` or `;` and no *if / only if / unless*. The gate
  is GO. The Notes column's "Net-new bridge or section in GLP-1 Market" is a recommendation note,
  not a conditional action value (see §4 and Open item 2).
- Priority is P1, pencilled for October 2026. `content-plan.md` was last synced 2026-09-17.
- Published inventory: `already_live: false` (line 475, open-P1 list only). The inventory and the
  plan agree.

### The five questions (guidelines §5)

1. **Does an existing article already answer this?** Partly. `glp-1-market` argues that scale
   weight is incomplete for *programs* and cites the same 2024 review. The coaching article covers
   coach workflow and a method table for general fitness. Neither addresses a fitness app serving
   members on GLP-1 treatment, or the split of responsibilities between the app and the
   prescribing program.
2. **Does the title overlap with a hub?** No. The Fitness hub H1 is "AI in Fitness: How Structured
   Body Data Powers ..." and the GLP-1 hub H1 is "GLP-1 Market Growth and the Need for Better
   Patient Progress Tracking". A title that collided with row 123 was rejected (§5).
3. **Is it broad enough for a hub, or should it be a section?** The *thesis* (scale weight is
   incomplete) is section-sized and already lives in `glp-1-market`. The app-side workflow, the
   role split and the decision framework add up to about 2,000 words of fitness-vertical content.
   Putting that into the GLP-1 market hub would break the row's own guardrail. The answer is a
   supporting page, narrowed (§4).
4. **Does the recommendation say refresh, section first or do not duplicate?** It says "net-new
   ... or section in GLP-1 Market", together with the do-not-duplicate list at
   `content-plan.md:157`. That list is applied in full.
5. **What exact search intent should this page own?** "Our fitness or coaching app has members
   taking GLP-1 medications. What should we record and show besides scale weight, what does
   research say about lean mass, and which questions belong to the prescribing program?"

### Adjacent rows and how the outline stays clear

| Row / page | Owns | How this page stays clear |
|---|---|---|
| 116 Fitness hub preamble | Broad fitness overview; the "What FitXpress does not do" list | Up-link only; Section 7 is a role split, not that list |
| 121 coaching article (live) | Coach workflow, method-by-method table, nine-row pilot list | Sideways link in Section 8; no method table; pilot measures limited to three sentences |
| 123 Smart Scale vs AI Body Scan (P2, Review/decide) | One shared comparison page, if demand supports it | One sentence on smart scales plus a link; title option with "What Fitness Apps Should Track" rejected |
| 125 "AI Fitness Progress Tracking: Why Weight Alone Is Not Enough" (P2) | Fitness "weight alone" thesis | The thesis is the premise (Sections 1-2), not the subject |
| 126 Body Recomposition Tracking (P2) | Recomposition and progress | No recomposition tutorial |
| 141 patient engagement (live, canonical engagement asset) | Engagement and visual progress | No engagement argument; the Visual Progress page is linked for it |
| 157 GLP-1 hub preamble, 161 GLP-1 hub (live) | Market, ecosystem, program-side tracking requirements | Up-link in Section 3; Section 5 is app-side only |
| 162 top-7 listicle (live) | Tool and vendor evaluation for GLP-1 clinics | No tools list; optional link in Section 9 |
| 166 "GLP-1 Progress Tracking: Why Weight Alone ..." (refresh of the Visual Progress page) | GLP-1 "weight alone" thesis | Same as row 125 |
| 167 "Body Composition Tracking for GLP-1 Patients: Metrics, Methods, Limits" (P2) | Methods education for GLP-1 patients | No methods tutorial; the H1 avoids that phrasing; see Open item 9 |
| 171 GLP-1 engagement (refresh/link) | Visual-progress engagement | Linked, not repeated |

### Actors

The ICP context asks the page to serve both actors. The primary reader is the fitness or
coaching app, because the row sits in Hub 1 and its guardrail keeps fitness strategy apart from
GLP-1 content. The GLP-1 program appears as the other party in Section 7 and as a routed reader
in Section 9. Tone is lighter on the fitness half and hedged on the GLP-1 half (audience.md
segments 3 and 1).

---

## 3. CTA reasoning

The fitness product page is the only CTA, for four reasons:

- The home hub is AI in Fitness, and the Hub 1 preamble names this URL as the BOFU destination.
- The page's one job is the fitness-app question.
- The row's guardrail keeps fitness strategy apart from GLP-1 content, and a telehealth close would
  tilt the page toward GLP-1 clinical workflow.
- GLP-1 programs already reach the telehealth page from the GLP-1 hub CTA and the listicle, while
  the fitness side has no GLP-1-aware route.

The CTA is evaluation-framed (MOFU, guidelines §15). A "book a demo" close would suit a BOFU page,
and this is not one.

The telehealth page is kept as one in-body link (Section 9) at its canonical URL. CLAUDE.md §16
also names that URL as the one vertical page built to the current standard. Verification on
2026-09-19 is in §7.

The weakness: the fitness page is old copy. Its H1 is "Elevate Your Fitness Platform with
AI-Powered Body Scanning", its H2s include "Seamless Integration" and "Leading-Edge Tech", it has
no GLP-1 mention, and it sits on the non-existent `/fitxpress/` path level (CLAUDE.md §16 debt).
A reader who clicks from a GLP-1 article lands on a generic page (Open item 3).

---

## 4. Standalone page or section in GLP-1 Market

The row's note allows either. The recommendation is **standalone, narrowed**.

**For a section:**

- The exact intent has no measured demand.
- The thesis already lives in the GLP-1 hub.
- Four P2 rows orbit "weight alone is not enough".

**For a standalone page:**

- The action type is `Create net-new` at P1, and the sheet already made that call.
- A fitness-app workflow inside the GLP-1 *market* hub would blur the vertical boundary, which is
  exactly what the row's guardrail forbids.
- `glp-1 muscle loss` is unowned on the site, and a hub section would not compete for it.
- Hub 1 and Hub 3 need a page that links them, and the role split has no home in either hub.

**Fallback, if Vadim or the reviewer judges the narrowed angle too thin:**

- About 250 words in `glp-1-market`, under its "Why Scale Weight Alone Provides an Incomplete
  Progress Record" H2, covering strength training, fitness apps and the joint advisory.
- A short paragraph in `ai-in-fitness-industry` linking to it.
- No new URL.

---

## 5. Structure, title and length decisions

- **12 sections.** Guidelines §12 and `about-me.md` set the 12-part order. `editorial-rewrites.md`
  §7 says a cluster article whose hub owns "What FitXpress does not do" has no such section, and
  the Fitness hub does own one. The resolution: Section 7 is a **role split**, a table of app,
  prescribing program, member and FitXpress, followed by two or three boundary sentences. It keeps
  the §12 slot, because GLP-1 is a sensitive vertical, without copying the hub's list. The
  reviewer may fold it into the scope note (Open item 8).
- **Format taken from the editorial final:**
  - bold-label scope note;
  - short-answer bullets;
  - bold-label workflow bullets;
  - one table of at most 11 rows (here 4);
  - three "fits when" H3s;
  - FAQ with three questions;
  - Next steps in two sentences;
  - cover plus two images.
- **FAQ.** "Does GLP-1 cause muscle loss?" (250 / mo) is left out of the FAQ because Section 3
  settles it (`editorial-rewrites.md` §2, where the EEOC question was cut for the same reason).
- **Length: 2,000.** The pack gave 1,800-2,400. The editorial final of a comparable cluster piece
  landed at 1,877 against a plan of 2,050 and lost nothing substantive.
- **Title.** "Beyond Scale Weight" replaces the row's "Not Just Weight". The row form is the
  corrective "X, not Y" shape (`terminology-guardrails.md` §1.8) and is close to the detector's
  banned "not just X" family. The pack judged the row form acceptable, so it stays as option 1.
  - Option 2 is rejected because it reuses row 123's subtitle.
  - Option 3 is rejected because it drops the reframe and edges toward row 167.
  - Option 4, the row title verbatim, fails gate 7 unless the primary keyword changes.
- **Headings.** They describe rather than assert, hedged where needed ("can fall short"). No
  content-plan labels appear in the H1, the H2s or anchors (`terminology-guardrails.md` §1.10).

---

## 6. Claims ledger

| Claim | Used? | Why |
|---|---|---|
| FX-001 accuracy (96-97%, 1.5-2.0 cm) | Section 6, §5 short form, own paragraph | Secondary to repeatability for trend views |
| FX-002 repeatability (< 1 cm) | Section 6, §5 short form, with framework link | The claim that carries the trend-view argument |
| FX-003 "95%+ repeatability consistency" | **Never** | Internal; no published home |
| FX-004 weight estimate ±3.5% | Not used | Not needed; weight feeds composition estimates, and a second estimate layer would complicate the lean-mass boundary |
| FX-005 composition outputs | Section 6 | The two fat sub-categories were retired in Review 1 item 13 (superseded gate) and are left out |
| FX-006 80+ measurements, two photos, under 45 s | Section 6 | Core |
| FX-007 Yazen 34,000 scans in 2025 | Section 6 | Use fields only. No GLP-1 attribution (not in the case file), no geography, no outcome. The "highest scan volume of any customer" superlative is dropped: it compares against undisclosed customers and reads as a sales line. **First public naming of Yazen in an article** (none of the published-live copies names it): Open item 11 |
| FX-008 HIPAA/GDPR | Optional, GDPR sentence only, Section 10 | Short note plus a trust-FAQ link, per the privacy rows' "link to central FAQ" |
| UK Meds | Not used | Wrong bridge (BMI verification) |
| Per-measurement figures, ISO 0.40 cm | Not used | Technical material; two-benchmark risk |
| Market sizing table | Not used | No matching vertical |
| "Lean mass preservation tracking" (use-case KPI line) | Not used as a capability | It implies clinical muscle monitoring that FitXpress does not do |
| Drug names, trial-by-trial figures (STEP 1, SURMOUNT-1 DXA substudies) | Not used | The Neeland range carries the evidence. Naming trials pulls the page into drug-specific clinical content |

---

## 7. Source verification log (2026-09-19)

WebFetch returns summaries written by a small model. **Only the Neeland abstract was obtained
verbatim.** Every other quote must be re-fetched and checked by the writer before it goes into
the text.

- **Neeland, Linge, Birkenfeld (2024), *Diabetes, Obesity and Metabolism* 26 Suppl 4:16-27, doi
  10.1111/dom.15728, PubMed 38937282.** Wiley returned 403 and PubMed showed a cookie wall. The
  abstract was obtained verbatim through the Europe PMC REST API. Usable sentences, verbatim:
  - "in some studies, reductions in lean mass range between 40% and 60% as a proportion of total
    weight lost, while other studies show lean mass reductions of approximately 15% or less of
    total weight lost."
  - "changes in lean mass may not always reflect changes in muscle mass as the former measure
    includes not only muscle but also organs, bone, fluids, and water in fat tissue."
  - "skeletal muscle changes with GLP-1RA treatments appear to be adaptive"

  The abstract's sentence on age, disease severity and candidate selection is clinical and was
  left out of the must-cover (§9).
- **Joint advisory, 30 May 2025.** Authors: the American College of Lifestyle Medicine, the
  American Society for Nutrition, the Obesity Medicine Association and The Obesity Society
  (Mozaffarian et al.). Published in *Obesity* (doi 10.1002/oby.24336, PubMed 40445127), *AJCN*,
  *Obesity Pillars* and *AJLM*. The Obesity Society page was fetched and gives "adequate protein
  intake and strength training to preserve lean mass"; that phrase came through the summarizer.
  PMC showed a reCAPTCHA. The writer confirms the wording in the journal text.
- **Conte, Hall, Klein, "Is Weight Loss-Induced Muscle Mass Loss Clinically Relevant?", *JAMA*
  2024;332(1):9-10, doi 10.1001/jama.2024.6586.** Existence and citation are confirmed. The content
  was confirmed **only through a TCTMD news report**, which quotes "the recent concern that marked
  weight loss induced by GLP-1-based anti-obesity medications can cause physical frailty or
  sarcopenia is not supported by data." This is unverified at the primary source, so it is
  optional in the plan (Open item 7).
- **KFF Health Tracking Poll, fielded 27 Oct to 2 Nov 2025.** Found through search: about one in
  eight adults (12%) currently taking a GLP-1 drug, to lose weight or to treat a chronic
  condition; 18% ever. The URL is in `plan.md` Section 4. The writer re-fetches it.
- **3dlook.ai pages:**
  - `/fitxpress/for-connected-and-digital-fitness/` is live, with old copy and no GLP-1 mention.
  - `/fitxpress/for-telehealth-and-weight-loss/` returned telehealth content, but the summarizer
    reported a different final URL. A redirect is likely (CLAUDE.md §16 says `/fitxpress/` 301s)
    and unconfirmed.
  - `/structured-body-data-for-telehealth-digital-health-programs/` is live, with H1 "Structured
    Body Data for Telehealth & Digital Health Programs" and no GLP-1 mention. It is the URL the
    live GLP-1 hub links.
- **Repo copies read in full:**
  - GLP-1 hub live text (`glp-1-market-hub/published-live-2026-08-28.md`);
  - coaching live text (`2026-08-26-.../published-live-2026-09-04.md`);
  - Fitness hub headings (`ai-in-fitness-hub/final.md`, `FINAL-PUBLISHED.md`).

---

## 8. Gate notes

- **`--plan`:**
  - frontmatter carries slug, primary_keyword, hub, intent, action_type and status (draft);
  - `target_words: 2000`, and the total row matches;
  - 12 headings in the `### Section N.` form;
  - no superseded terms in the plan (grep for DXA's retired spelling, the retired fat
    sub-categories, the retired height range, the retired composition-values wording, and em and
    en dashes found nothing).
- **Article stage, gate 7:** `glp-1 muscle loss` appears in the H1 and in the Section 3 H2.
- **Article stage, gate 9 (accuracy):** the accuracy-shaped regex matches a percentage within 40
  characters after `varian…`, `error`, `accur…`, `toleran…`. Section 3's "40% and 60%" must not
  follow "variation" or "variance" closely, or it will be read as an unapproved accuracy figure.
  `plan.md` warns the writer.
- **Article stage, link directions:** the pack's `down` list includes the fitness URL, so the
  gate passes even though the telehealth link uses a different URL than the pack.
- **M1:** see Open item 6.

---

## 9. Changes after the interrupted session

The first session wrote `plan.md` (40 KB) and stopped before this file existed. On resume, and
at the coordinator's request:

- Rationale, the full priced alternatives, CTA reasoning and title reasoning moved here. `plan.md`
  keeps the Checkpoint 1 block, the reviewer package and what the writer needs.
- **Two corrections to `plan.md`:**
  1. Section 3 no longer asks for the abstract's age, disease-severity and candidate-selection
     sentence. It is clinical treatment-selection content, and the must-cover was pulling a
     clinical point into a fitness page.
  2. Section 6 now names Yazen **only if Open item 11 clears it**. Otherwise the text reads "a
     weight-loss management platform". No published article names Yazen yet.
- Nothing else changed: keyword, title, CTA, the 12 sections, budgets and links are as first
  planned.

---

## 10. Open items for Vadim

1. **Primary keyword differs from the topic phrase** (`seed_has_data: false`). Confirm
   `glp-1 muscle loss` (600 / KD 45 / TP 100, consumer-leaning SERP). The fallback is the row
   title as H1 with an unmeasured primary; the price is zero measured demand. Either way, the
   organic ceiling is small (§1).
2. **Standalone page or section in GLP-1 Market.** The row allows either. The recommendation is
   standalone, narrowed to the app side and the role split. The fallback is about 250 words in
   `glp-1-market` plus a paragraph in the Fitness hub (§4). Please confirm.
3. **The CTA destination is a weak landing** for this article: old copy, no GLP-1 mention, and
   the `/fitxpress/` path debt. Not blocking. Worth a `/page` refresh later (§3).
4. **The telehealth URL in the pack** (`/fitxpress/for-telehealth-and-weight-loss/`) looks like a
   redirect. The plan uses `/structured-body-data-for-telehealth-digital-health-programs/`.
   Coordinator: confirm with `curl -sI`.
5. **Optional Ahrefs pulls before `write`** (about 1,000 units each): `body composition tracking`,
   `strength training on glp-1` or `glp-1 exercise`, and `glp-1 fitness app`. If a fitness-side
   term shows measured demand, it may fit better than muscle loss. The change would touch the H1
   and the Section 3 H2 only.
6. **The M1 gate reads the H1 as the first use of "GLP-1".** An H1 that opens with GLP-1 cannot
   carry the expansion before it, so gate 8 will fail on the H1 line whatever the writer does.
   The live GLP-1 hub and the listicle have the same H1 shape. This needs a call: a gate
   exemption for headings, or an accepted known failure.
7. **The JAMA Viewpoint** was verified only through a news report. It is included only if the
   writer confirms it on the JAMA page; otherwise it is cut.
8. **Section 7 structure.** A role split takes the "does not do" slot, because the Fitness hub
   already has that list. The reviewer may prefer to fold it into the scope note, per
   `editorial-rewrites.md` §7.
9. **Content-plan side effect.** Once this ships targeting `glp-1 muscle loss`, rows 125, 166 and
   167 should not target muscle loss. A note for the next `content-plan.md` sync.
10. **Live-page debt, not ours:** the live coaching article's privacy paragraph still says
    "maintains HIPAA compliance" and "adheres to GDPR principles". `compliance.md` has retired
    both since 2026-09-18. The writer is told not to model it.
11. **Yazen named publicly for the first time in an article.** The case file permits SEO use and
    the pack approves FX-007, but no live article names Yazen yet. Please confirm, or the text
    says "a weight-loss management platform".

---

## Review 1 re-plan (2026-10-20)

`plan.md` is now revision 2. Its frontmatter carries `revision: 2` and `review_round: "Review 1
(2026-10-20), structural"`. The 12-section plan it replaces is snapshotted in `v2/plan.md`, and
its text in `v2/final.md`.

Everything above this heading describes that 12-section plan and stays as history. Where it
disagrees with `plan.md` revision 2, `plan.md` governs.

- **Still in force:** §1 (keyword decision), §2 (Phase 0 and the adjacent rows), §3 (CTA
  reasoning) and §7 (source log).
- **Settled:** §4, by Vadim on 2026-09-19 (standalone).
- **Superseded:** §5's 12-section structure and §6's `FX-00N` claim ids. The pack of 2026-10-20
  uses `FXS-*` and `T-*`.

**Inputs, in authority order:**

1. `review-1-decisions.md`, which wins;
2. the context pack rebuilt on 2026-10-20;
3. `review-1.md` (the reviewer read `v1/final.md`, an older text);
4. `v2/plan.md` and `v2/final.md`.

The run is in no-checkpoint mode (Vadim, 2026-09-21). Every judgment call below was decided by the
canon and is recorded here for the publisher and for Vadim.

### R1. H1 candidates and the choice

The rule (decisions §1) has three parts:

- the H1 carries the exact string "GLP-1 muscle loss";
- it frames muscle loss as the question or concern the app team faces;
- it must not read as if the app or the scan identifies, tracks or measures muscle loss.

The second half stays "Tracking Body Change Beyond Scale Weight" or close to it.

| Candidate | Keyword position | Could it read as the app or scan measuring muscle loss? | Verdict |
|---|---|---|---|
| **GLP-1 Muscle Loss Concerns for Fitness Apps: Tracking Body Change Beyond Scale Weight** | words 1-3 | No. "Concerns" makes muscle loss the worry the app team handles; the second half names what the app tracks, which is body change | **Chosen** |
| When Members Ask About GLP-1 Muscle Loss: Tracking Body Change Beyond Scale Weight in Fitness Apps | words 5-7 | No | Rejected: 15 words, and the keyword runs past the first six words (Phase 2 rule) |
| GLP-1 Muscle Loss and Fitness Apps: Tracking Body Change Beyond Scale Weight | words 1-3 | Yes, mildly: its first half is the pairing the reviewer flagged in v1 | Rejected |

**Why the chosen H1.**

- Gate 7 passes, with the keyword at the very start.
- The framing answers the reviewer's concern directly. Members and coaches raise the concern, and
  the second half gives the app's response: tracking body change beyond scale weight.
- "for Fitness Apps" keeps the B2B reader in the title.
- "Questions" was weighed in place of "Concerns" and dropped. "Muscle loss questions for fitness
  apps" reads as questions the app should answer, and the article sends those to the clinician.
- It avoids the landing's primary keyword, "body scanning for fitness apps" (`landing-map.md`
  rule 3). The meta title and description follow the same rule (`plan.md`, Article meta).

The reviewer's verbatim H1 is not a candidate under gate 7. It stays a one-line swap for Vadim
(R7, item 1).

### R2. Decisions file mapped to the plan

| Decisions item | Disposition | Where in `plan.md` | Note |
|---|---|---|---|
| What does NOT change | kept | Frontmatter; Content Strategy Fit; Section 2 sources | Keyword, slug, author, hub, P1, one CTA, unnamed customer, three external sources, M1 accepted |
| §1 Headline | amended | Recommended Title; Section 2 H2; Section 6 Q1 | Keyword in the H1 and the Section 2 H2 only; FAQ 1 first, v2 wording |
| §2 Estimates | verbatim | Section 3 (T-ESTIMATES) | "Split" wording retired everywhere; the formula is not named |
| §3 Table | verbatim | Section 3 (T-TABLE); Image 1 | One or two lead-in sentences; no sentence after the table restates it |
| §4 Measurement vs composition | verbatim | Section 5, P3 (FXS-REPEAT, T-REPEAT-SCOPE, T-VALIDATION) | The §1.2 sentence replaces v2's; accuracy and NDA sentences kept; framework link once; no 0.40 cm |
| §5 34,000 scans | kept with conditions | Section 5, P5 (T-34K); Writing constraints R4 | Own paragraph, no link, never with the product link; open item |
| §6 Opening | accepted | Section 1 (opening, scope note) | Under the Section 1 H2. Short answer dropped; scale and circumference points moved into the opening and the table |
| §6 Section 1 | accepted; KFF amended | Section 1 | KFF in one sentence, scoped to US adults; market and retention links; no retention claims |
| §6 Section 2 | accepted; advisory amended | Section 2 | Neeland range; lean mass vs muscle; "appear to be adaptive"; advisory as broader management; T-MUSCLE-FUNCTION |
| §6 Section 3 | accepted | Section 3 | Table, Image 1, estimates, weight source |
| §6 Section 4 | accepted | Section 4 | T-BASELINE; cadence from v2 FAQ 2; thresholds with coaching link; FXS-POPULATION plus a manual or weight-only option |
| §6 Section 5 | accepted | Section 5 | Outputs, Body Progress, records and privacy, evidence, guardrail, 34,000 scans, pilot; one contextual product link in P1 |
| §6 FAQ | accepted | Section 6 | Two questions (R4, item 2) |
| §6 Next steps | kept | Section 7 | The v2 two sentences |
| §6 Condensed or removed | applied | R3 below | |
| §6 Length | applied | `target_words: 1600` | Inside 1,400-1,800 |
| G1 | accepted | Section 2 (T-MUSCLE-FUNCTION); "reference methods" banned in Writing constraints | DXA and BIA never presented as equivalent references |
| G2 | amended | Section 3 (T-WEIGHT-SOURCE) | Smart Scales and the scan's weight estimate stay out of the article |
| G3 | verbatim | Section 5, P2 (T-BODY-PROGRESS) | |
| G4 | amended | Section 5, P2 (T-PRIVACY-ROLES); Section 6 Q2 | FAQ link once mid-paragraph; Q2 wording per R4, item 3 |
| G5 | verbatim | Section 5, P2 (T-RECORDS-ACTORS); Writing constraints (actors) | No "organization(s)" for a known actor, article-wide |
| G6 | accepted | Illustrations | "Illustrative example" label on Image 1; no muscle imagery on any visual |
| H | open items | R7 | Incoming links, the reviewer's H1, customer permission |

### R3. What was cut, and where its job went

| v2 element | Fate | Where the job went |
|---|---|---|
| S1 opening and scope note | kept | Section 1. The scope note is verbatim. "Approximate picture of what changed and where" is retired because it implied the estimates show which tissue changed |
| S2 Short answer (4 bullets) | removed (decisions §6) | Scale point: opening. Circumference point: opening and table row 2. Training history: Section 1 body and table row 2. The "split" bullet is replaced by T-ESTIMATES in Section 3 |
| S3 research | condensed | Section 2. The reasons sentence (population, drug-specific, comorbidity) is dropped. The strength-training line is replaced by the amended advisory point. The `glp-1-market` link moves to Section 1 |
| S4 why relevant to apps | condensed | Section 1. KFF goes from three sentences to one. The "likely to count some of these adults" hedge is cut: it is the extrapolation the reviewer warned against. The visual-progress link stays |
| S5 app-side workflow | split | Baseline, check-ins and capture go to Section 4; the progress view goes to Section 3. "The workflow runs the same way whether or not the app knows…" is cut: FAQ 2 answers it, and decisions §6 keeps a FAQ only when the body does not |
| S6 Where FitXpress fits | rebuilt | Section 5. T-BODY-PROGRESS replaces "FitXpress compares two scans that the app selects". FXS-REPEAT replaces the v2 repeatability sentence. The reframe sentence is dropped; the Section 4 thresholds point carries why repeatability matters for trends |
| S7 roles table (4 rows) and dose sentence | removed (decisions §6) | Integration responsibilities go to Section 5, P2 (T-BODY-PROGRESS, T-RECORDS-ACTORS, T-PRIVACY-ROLES). The dose and decision-support sentence is cut: the scope note and table row 3 carry that boundary. editorial-rewrites §7 allows the scope note plus one boundary sentence in "Where FitXpress fits", here R2 |
| S8 "which fits when" (three H3s, smart-scale sentence) | removed (decisions §6) | One sentence and the coaching link in Section 5, P4. The consumer smart-scale sentence goes with the section |
| S9 "programs this workflow fits" | cut (decisions §6) | Second-record point: one optional sentence in Section 5, P4, placed after R2 so that DXA is expanded first (M1). Top-7 link: optional in Section 5, P1. Telehealth page link: cut (R4, item 12) |
| S10 implementation | split | Privacy goes to Section 5, P2. Thresholds and the alternative path go to Section 4. The pilot goes to Section 5, P6 |
| S11 FAQ (3 questions) | 2 kept | Q1 verbatim. "How often" goes to Section 4, Cadence. Q3 becomes Q2, with G4 wording |
| S12 Next steps | kept | Section 7, verbatim |
| Cover concept (stacked fat and lean bar per check-in) | replaced | It drew the "split" that decisions §2 retires. The new cover is in Illustrations |

### R4. Calls made by the canon (no checkpoint)

1. **Where the opening sits.** "No H2 of its own beyond the first section's" is read as: the
   opening sits under the Section 1 H2. That matches the house pattern in editorial-rewrites §7:
   no prose between the H1 and the first H2, and the cover goes under the first H2. Section 1's H2
   fits the opening scene.
2. **Two FAQ questions, not three.** editorial-rewrites §7 asks for three. Decisions §6 keeps a
   question only if the body does not answer it, and only two qualify. The body already answers
   every in-scope AEO prompt, so none adds a third question.
3. **FAQ 2 wording.** G4 says the answer "keeps 'purpose, notice' and replaces a bare 'consent'
   with 'lawful basis, notice, and consent where required'". Applied literally, "notice" would
   appear twice. The merge is "purpose, lawful basis, notice, and consent where required". It
   keeps every term G4 names, once each.
4. **Mixed accuracy forms in one paragraph.** `accuracy-formulations.md` §5 says not to mix §1 and
   §5 wording in one paragraph. Decisions §4 does three things:
   - it locks the §1.2 repeatability sentence;
   - it keeps the current §5 accuracy and NDA sentences ("current wording is canon");
   - it puts the scope and validation sentences in the same paragraph, with one framework link.

   Decisions wins. Every claim, figure and hedge is canon wording; only the register mixes.
5. **Down-link depth.** `landing-map.md` rule 1 wants the down link in the first 30% of the body.
   Decisions §6 places "one contextual product link … where the integration workflow is
   discussed", which is Section 5, at about 63-68% of the body. Decisions wins. A second
   contextual link higher up would break "one" (R7, item 4).
6. **Joint advisory link.** The pack note says "One link (PubMed record)". Two sources say
   obesity.org instead:
   - decisions, "What does NOT change": "the 2025 joint advisory on obesity.org";
   - Vadim's checkpoint 2 on 2026-09-19, which moved the link to obesity.org (recorded in
     `v2/final.md`).

   The plan uses obesity.org.
7. **FXS-POPULATION.** Decisions quote sentence 1 only and add one sentence on the app's
   alternatives.
   - Sentence 2 ("This matters when a disability affects the standard standing pose or capture
     sequence.") is allowed: optional, and verbatim if used.
   - Sentence 3 ("the program needs a documented alternative measurement path") is replaced by the
     app-specific alternatives sentence that decisions §6 asks for.
8. **Two links to the coaching article.** Decisions §6 asks for the thresholds point "with its link"
   (Section 4) and for "one sentence with a link" for the method comparison (Section 5). The two
   links have different anchors, sit about 300 words apart and serve different jobs. Both stay.
9. **"Let" in the reviewer's table.** Decisions §3 rules that no terminology fix is needed. The
   detector's `let` pattern only fires on "let you/them/teams/…", so "Let a member" passes. If the
   editor applies the guardrail's `let` to `allow` swap, that is the one kind of change §3
   permits. The plan says so.
10. **KFF hedge cut.** v2's "likely to count some of these adults among their members" inferred
    app membership from a general-population figure. The reviewer: "describes US adults
    generally, not fitness app members". With one sentence allowed, the hedge goes.
11. **The Section 3 H2 avoids "GLP-1-aware".** The decisions' working title says "GLP-1-aware
    fitness progress view". That can read as an app that records medication status, which
    conflicts with FAQ 2: tracking does not need it. The H2 is "What a fitness progress view can
    show for members on GLP-1 treatment".
12. **Telehealth page link cut.** v2 linked it in the removed "programs this workflow fits"
    section. Decisions keep "one CTA to the fitness product page" and do not list the telehealth
    link as surviving. GLP-1 programs reach their landing from the GLP-1 hub.
13. **Anchors to the fitness landing.**
    - The Section 5 contextual link uses the row's first anchor, "body scanning for fitness apps",
      in body copy only. That helps the landing hold its keyword, and rule 3 bars the anchor only
      from the title, H1 and meta title.
    - Next steps keeps v2's anchor, a light inflection of "body composition tracking for fitness
      apps".
14. **US spelling** in text that is not locked ("fulfill", "labeled"). The reviewer's table
    already uses US forms.
15. **Claim marker ids.** The pack moved from `FX-00N` to `FXS-*` and `T-*`, and gate 3 fails a
    marker that is not in `approved_claims`. External sources sit outside that list, so they keep
    v2's `claim: external, source: …` form.
16. **T-PRIVACY-ROLES runs 26 words.** editorial-rewrites §8 would split a reviewer sentence over
    25 words. Decisions say "do not paraphrase or improve", and decisions wins. One sentence over
    25 words is inside gate 10's 6% allowance.
17. **Length 1,600.** That is the middle of the 1,400-1,800 range. Section 5 gets the largest
    budget (430) because it carries 12 locked claims.
18. **No DXA or BIA in Section 2.** Their first use must be R2 in Section 5, which carries both
    expansions. An earlier mention would fail M1 or double-expand R2.

### R5. AEO

- The `aeo_signals` were pulled on 2026-10-20, with `no_prompt_covers_topic: false`. No tracked
  prompt asks about GLP-1 muscle loss directly. The mapping is in `plan.md`, "AI-assistant
  questions (AEO)".
- Prompt 565495617300 (28% visibility; our top-7 page cited 15 times): the must-cover names
  FitXpress (3DLOOK) in the Section 5 P1 answer paragraph.
- Prompt 565780364091 (1% visibility, the DXA alternatives question): not answered, because the
  method comparison is removed. The coaching link is the route. It is the one in-scope prompt the
  article leaves to another page.
- `open_recommendations`: none matches this topic. The open items are about bariatrics, YouTube,
  LinkedIn and PR, so no recommendation id applies.

### R6. Gate notes

- **The `--plan` lint was not run in this session.** The planner had no shell (Read, Write and
  Grep only). Manual check against `gate_plan` and `SUPERSEDED`:
  - frontmatter carries slug, primary_keyword, hub, intent, action_type and status (`draft`);
  - `target_words: 1600`, and the labelled total row matches;
  - there are seven `### Section N.` headings;
  - a grep for retired terms found one hit. The terms checked: DXA's retired spelling, the two
    retired fat sub-categories, the retired composition wording, the retired height range and the
    wellness-scoped weight phrase. The one hit is the AEO prompt row, which carries "DXA (also
    written DEXA)" on one line and is licensed by the DXA-on-the-same-line rule;
  - no em or en dashes.
  - The coordinator runs `python3 scripts/article_lint.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/plan.md --plan`
    before the write stage.
- **Article stage:**
  - Gate 7: the H1 and the Section 2 H2 carry `glp-1 muscle loss`.
  - M1: the known failure on the H1 is accepted.
  - Gate 9: the framework link is in Section 5, P3. There is no ISO benchmark. In Section 2, "40%
    to 60%" is kept away from "variation" and similar words.
  - Gate 3: the new id scheme, see R4, item 15.
  - Gate 6: the plan covers all four link directions in the pack's `internal_link_targets`.

### R7. Open items for Vadim (publish package and digest)

1. **The reviewer's verbatim H1.** "GLP-1 and Fitness Apps: Tracking Body Change Beyond Scale
   Weight" is a one-line swap if Vadim prefers it. The price: `glp-1 muscle loss` leaves the H1
   and gate 7 fails. The swap therefore also changes the primary keyword, and with it the Section 2
   H2, the meta title and the meta description. The chosen H1 meets the reviewer's concern and
   keeps the keyword.
2. **Customer permission for the 34,000-scan description.** The reviewer asks for explicit
   permission to describe the customer's use publicly. Vadim's decision of 2026-09-19 covers the
   anonymized mention ("a weight-loss management platform", never named). If he wants the
   customer's sign-off on the use description, the two sentences in Section 5, P5 cut cleanly; the
   paragraph stands alone.
3. **Incoming links (CMS work, after publication).** Add contextual links into this article from
   the AI in Fitness hub (`/content-hub/ai-in-fitness-industry/`) and the GLP-1 market article
   (`/content-hub/glp-1-market/`). This is work on two other live pages for Assel or the site
   editors. The pipeline does not do it.
4. **Down-link depth.** The one contextual link to the fitness landing sits in Section 5, at
   about 63-68% of the body, where decisions §6 places it. `landing-map.md` rule 1 asks for the
   first 30%. If Vadim wants both, a second contextual link in the Section 1 body is a one-line
   add.
5. **Carried over, no action.**
   - M1 on "GLP-1" in the H1 remains the accepted known failure (Vadim, 2026-09-19).
   - Of the earlier open items (§10), 1, 2, 6, 7 and 11 were closed on 2026-09-19.
   - `landing-map.md` now lists the fitness landing as live, which bears on §10 item 3. Whether
     its copy mentions GLP-1 was not re-checked in this re-plan.
