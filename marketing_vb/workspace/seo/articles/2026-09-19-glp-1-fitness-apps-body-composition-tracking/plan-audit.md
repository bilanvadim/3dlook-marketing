---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
plan: plan.md
stage: plan
created: 2026-09-19
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
