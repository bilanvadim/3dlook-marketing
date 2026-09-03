---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
hub: "Bariatrics (Hub 6)"
cluster: Main hub
intent: Hub
action_type: refresh-expand-hub
priority: P0
target_month: September 2026
live_url: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
live_published: 2026-06-05
live_modified: 2026-07-27
baseline_file: published-live-2026-07-27.md
baseline_words: ~4100
prepared: 2026-09-03
status: input-to-plan
---

# Refresh gap analysis — Bariatrics hub

Prepared before Phase 0 so the plan argues from the live page, not from the content-plan row alone.
The row was seeded from the Backlink Analysis Report against the **June 5** version; the page was
expanded again on **July 27**, outside the pipeline. Both facts matter.

---

## 1. The content-plan row is partly already satisfied

Row instruction: *"This is already the hub. Expand with pre-auth, patient progress, GLP-1 bridge, and
post-op tracking."*

| Row asks for | Live page as of 2026-07-27 | Verdict |
|---|---|---|
| Pre-auth | H2 #6 "Pre-auth documentation: cleaner packets, fewer delays" (~600 w) | **Done** |
| Patient progress | H2 #7 "Post-procedure: turning the baseline into longitudinal tracking" + 6 FAQ | **Done, but subordinate** |
| GLP-1 bridge | H2 #3 "The GLP-1 shift: volume contracted, intake complexity rose" | **Done, now factually stale** |
| Post-op tracking | folded into H2 #7 | **Done** |

Taking the row literally would re-do work already shipped. The real refresh case rests on items 2–6
below, not on the row's expansion list.

`published-articles-inventory.md` still records this article as "Jun 5, 2026 — Hub" with no note of
the July 27 update. **Inventory correction needed regardless of what happens to the article.**

---

## 2. The GLP-1 section is out of date — this is the strongest reason to refresh

The live section describes a **2023 snapshot** and the 2024-era "will GLP-1 replace surgery?" debate.
The 2026 picture is materially different, and none of it could have been on the page in July.

**New, verified since the live version:**

- **[JAMA Surgery, 13 May 2026](https://www.eurekalert.org/news-releases/1127781)** (Calzaretta et al.,
  Analysis Group): metabolic bariatric surgery utilization **−34.1% from 2022 to 2024**, GLP-1 receptor
  agonist use **+140.4%** over the same period. The live page's "fell 8.7% between 2022 and 2023" is
  now the smaller, older cut of the same story.
- **[ASMBS, 5 May 2026](https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/)**:
  **90–95% of patients with severe obesity received no treatment** during the study period. Stronger
  and better-sourced than the live page's "fewer than 1% complete surgery."
- **The decline continued into 2025.** Study-cohort volumes: 2022: 40,265 · 2023: 42,615 · 2024: 37,339
  · **2025: 33,429**. The live page stops at 2023.
- **The "bridge" pathway is now documented from both directions.** The study author's framing — patients
  who benefit most from surgery *may forgo it* for GLP-1s, while medications may serve as *"a bridge to
  future surgery"* — plus the existing Johns Hopkins one-in-seven post-op initiation finding, gives the
  hub a real GLP-1-bridge spine instead of a single "shift" section. This is also the seed for the P1
  net-new child *"GLP-1 Before Bariatric Surgery."*
- **ASMBS reports surgery "appears to be rebounding"** as GLP-1 patients turn to one-time procedures.
  Directionally opposite to the live page's closing read. Needs a primary citation before use.

---

## 2b. Two 2026 developments that change the argument, not just the numbers

These are the strongest additions available, and neither exists anywhere on the live page. Each also
sharpens the product case rather than merely updating a statistic.

### a) The pre-auth clock got short — CMS-0057-F

[CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F)](https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f).
Operational since **1 January 2026**, impacted payers must decide prior authorizations within **72 hours
(expedited)** and **7 calendar days (standard)**, must give **specific reasons for each non-drug denial**
regardless of submission channel, and must **publicly report prior-authorization metrics annually**, with
initial reporting due **31 March 2026**.

**Scope, and it must be stated:** the rule reaches Medicare Advantage, Medicaid, CHIP and Qualified Health
Plans on the Federally Facilitated Exchange. It does **not** cover all commercial ERISA plans, and Medicare
fee-for-service does not use prior authorization for bariatric procedures at all.

The live page currently says *"Payer review windows commonly run from a few weeks to several months."* For
impacted payers on standard requests that is now wrong. More importantly it inverts the argument: on a
7-day clock, **first-pass submission completeness is the whole game** — there is no longer room for a
leisurely request-for-more-information cycle, and a missing timestamped BMI record is no longer a delay,
it is a denial with a published reason. That is a materially stronger case for structured body data than
"cleaner packets, fewer delays," and it is the section's new spine.

### b) Patients now arrive already lighter — the GLP-1 bridge, quantified

[ASMBS, 5 May 2026](https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/)
— Chhabra et al., NYU Grossman School of Medicine, presented at ASMBS 2026. Epic Cosmos electronic health
records, 2019–2025: **6,700 patients with prior GLP-1 use** (2,395 gastric bypass, 4,315 sleeve gastrectomy)
against roughly **127,000 without**, followed three years. Patients lost about **8% of total body weight on
GLP-1s before surgery**; total loss reached **more than 25% after gastric bypass** and **about 20% after
sleeve gastrectomy**.

The operational consequence is the insight this hub has been missing. A patient who has already lost ~8% of
body weight on a GLP-1 may present at consult with a **current** BMI below the payer's threshold while their
**documented history** still qualifies. Eligibility therefore increasingly turns on dated, verifiable BMI
history rather than on a single measurement taken at the consult — precisely what a timestamped serial-scan
record provides and what a tape measurement in a free-text note does not. This is the bridge argument the
content-plan row asks for, and it lands on documentation rather than on clinical claims.

---

## 3. Three incompatible volume series — a guardrail #2 blocker

Editorial guardrail #2 is "one number, everywhere the same." There are currently three series in play
and they do not reconcile:

| Series | Figures | Scope / methodology | Use? |
|---|---|---|---|
| **A — ASMBS national estimate** | >270,000 in 2023, −3.5% YoY | [2025 Fact Sheet](https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf): "best estimation from available data (BOLD, ACS/MBSAQIP, National Inpatient Sample Data and outpatient estimations)". **Series ends at 2023.** | **Yes** — volume anchor, already published, authoritative |
| **B — JAMA Surgery 2026 cohort** | 40,265 (2022) → 33,429 (2025); −34.1% utilization 2022–24 | Claims cohort. ASMBS states its own "estimates are based on broader patient populations and additional datasets than used in this particular study." −34.1% is a **utilization rate**, not a count change (counts move −7.3% over the same span). | **Yes, but** only for direction and the substitution effect, explicitly scoped as a cohort |
| **C — "peaked at 230,207 in 2022, 177,297 in 2024"** | — | Secondary trade-press report; primary source returned HTTP 403, **unverified** | **No** — do not publish |

**Rule for the writer:** A and B never share a sentence. Every B figure carries its cohort scope.
C stays out until someone reads the primary source.

---

## 3b. Series A, fully sourced — added 2026-09-03 after the plan was approved

The 2025 Fact Sheet PDF carries its year-by-year numbers and its procedure-type split **as a
graphic**, so they do not extract and cannot be quoted from it. The extractable source is ASMBS's
own [Estimate of Bariatric Surgery Numbers](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/)
page. Cite that URL, not the PDF, for anything in this block.

| Year | ASMBS national estimate |
|---|---|
| 2019 | 256,000 |
| 2020 | 198,651 |
| 2021 | 262,893 |
| 2022 | 279,967 |
| **2023** | **270,089** |

Series A ends at 2023. The live page's `270,089` and its `-3.5%` both check out: 270,089 / 279,967
= −3.5%. Same methodology footnote as the Fact Sheet: *"based on the best estimation from available
data (BOLD, ACS/MBSAQIP, National Inpatient Sample Data and outpatient estimations)."*

**2023 procedure-type split** (of 270,089): sleeve gastrectomy **58.2%** (157,254) · Roux-en-Y
gastric bypass 23.4% (63,132) · revision 11.9% (32,267) · BPD-DS 1.4% (3,775) · SADI 0.9% (2,387)
· band 0.3% (773). This is the citation for **Branch B's FAQ question on the main procedure types**,
and it confirms the live page's "more than half" sleeve framing.

**This also kills Series C for good.** The ASMBS national series puts 2022 at 279,967, so the
"peaked at 230,207 in 2022, 177,297 in 2024" report is not this series under any reading. Stays out.

---

## 4. Two substantiation defects already live

- **"Pre-operative dropout rates of up to 50–60% are reported across bariatric programs"** (H2 #2, reused
  in H2 #9). The published range is far wider and measurement-dependent: a
  [2026 narrative review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/) says "as high as 60%," one
  cohort reports **22.25%**, Canadian programs with mandatory pre-op pathways complete at ~36–76%, US
  programs at ~39–70%, and one single-centre series reports 8.9% pre-pandemic. The live page presents the
  top of the range as typical. That is guardrail #4 (no bare percentage without methodology) and #1
  (substantiation). **Fix:** state the range and that it varies by program design and by how attrition is
  measured — which is a stronger argument for standardised intake data anyway.
- **Citation mismatch.** The "33 million US adults meet eligibility criteria, yet fewer than 1% complete
  surgery" claim points at [PMC10136401](https://pmc.ncbi.nlm.nih.gov/articles/PMC10136401/), which is a
  *qualitative attrition* paper, not an eligibility-prevalence source. The ASMBS fact sheet carries the
  "about 1% of those who meet eligibility requirements" line directly. **Re-cite or drop.**

**Verified as still current, keep unchanged:** CDC NHANES **40.3%** adult obesity / **9.4%** severe
obesity, [Data Brief 508](https://www.cdc.gov/nchs/products/databriefs/db508.htm), August 2021–August
2023 cycle. No newer clinical-measurement cycle exists. Do not mix the 9.4% crude figure with the 9.7%
age-adjusted trend figure from the same brief.

---

## 5. Rejected angle — generic semaglutide

An early read suggested "semaglutide lost exclusivity in March 2026, prices to fall 30–50%" as a driver.
**Do not use it on this page.** The 2026 expiries are **China (20 March), India (March), Canada
(January), Brazil (March)** and 100+ other countries — **not the US**, where protection runs into the
early 2030s. This page's stated audience is "bariatric programs in the United States." The claim would
be materially misleading in that frame. Admissible only as an explicitly ex-US note, and only if the hub
deliberately broadens beyond the US.

---

## 6. Positioning and boundary problems on the live page

**a) The title leads with the technology.** Live H1: *"Bariatric Pre-Qualification with Mobile 3D Body
Scanning: Faster Pre-Auth."* CLAUDE.md §3 sets the positioning shift away from "best model" toward
outcomes and workflow, and instructs SEO to write "про use case, не про technology." The content-plan
target title — *"…Patient Progress Tracking: Body Data for Obesity Care Teams"* — is the use-case/audience
framing, and it co-headlines progress tracking instead of burying it at section 7.

**b) The "About bariatric surgery" FAQ block crosses the vertical boundary.** Six questions — what is
bariatric surgery · main types · common requirements · benefits · side effects · pros and cons — answer
*clinical care* questions. The Bariatrics boundary (guidelines §9) is: *owns pre-qualification, pre-auth
documentation, obesity-care intake, post-op progress, patient records.* The benefits answer ("associated
with sustained weight loss and improvement in obesity-related conditions such as type 2 diabetes,
hypertension, and obstructive sleep apnea") and the side-effects answer are clinical-outcome claims from
a body-data vendor. This block is chasing patient-facing volume (see §7) at the cost of the boundary.
**This is a decision for Vadim, not for the pipeline** — see the checkpoint question.

**c) Related reading is two links and stale.** Live: insurance underwriting + wellness rewards only.
Missing siblings that went live or were republished after this page: occupational health hub, the
refreshed `glp-1-market`, the rewritten `online-pharmacy-bmi-verification`. The Data/Privacy/Security
FAQ remains an unpublished P0 gap — plain text, never a link.

**d) No link-down structure.** Hub 6 has **five net-new P1 children** in the plan (pre-auth
documentation · GLP-1 bridge · post-op progress · patient records · hybrid care). The hub should be
shaped so each has a landing section to be linked down from when it ships.

---

## 7. The keyword problem — Open Item #1 for checkpoint 1

Ahrefs, country `us`, pulled 2026-09-03. Files in `workspace/seo/_keywords/`.

| Phrase | Volume | KD | Note |
|---|---|---|---|
| `bariatric pre-qualification` | **no data** | — | the current H1's own term |
| `bariatric patient progress` | **no data** | — | the target title's other half |
| `bariatric pre authorization` | **no data** | — | `pre authorization` alone is 1800/mo but generic |
| `bariatric intake` | **no data** | — | variants are all nutrition intake (calories, protein) |
| `body composition after bariatric surgery` | **no data** | — | `body composition` alone 32000/mo, wrong intent |
| `obesity care` | 80 | 53 | parent topic is **"obesity week"** — conference intent |
| `bariatric surgery requirements` | **1100** | 54 | TP 5000, informational, **patient-facing** |
| `bariatric surgery` | 69000 | 50 | patient-facing head term |
| `bariatric patient` | 500 | 39 | TP 10 |

**Every phrase in the content plan's target title has zero measured US demand.** The only real volume in
this vertical is patient-facing — surgery requirements, diet, vitamins, before-and-after. This is the
same failure the Ahrefs producer was built to catch after the 2026-08-25
`remote-body-measurement-online-fitness-coaching` article shipped on a zero-data primary keyword.

Read honestly, that is not an argument for changing the page's audience. Buyer-side terms
(pre-qualification, pre-auth documentation, intake workflow) have no search volume because this is a
small B2B buying committee — a few hundred US bariatric programs, with directors of operations and
pre-auth coordinators who do not search in vendor language. The page's job is BOFU/GEO capture and sales
enablement, not organic volume. **What must not happen is the page quietly drifting into patient-facing
content to chase the 1100/mo — which is exactly what the "About bariatric surgery" FAQ block already
does.** Vadim should see that trade-off stated, at checkpoint 1, rather than discover it in GSC.

---

## 7b. What `article_lint.py` says about the live text

Run 2026-09-03 against `published-live-2026-07-27.md` with this refresh's pack. Three gates fail on
text that is **currently published**, which settles the "patch or rewrite" question: this is a
line-level rewrite, not a patch.

| Gate | Result | What it means |
|---|---|---|
| hard bans | **FAIL — 43** | `em_dash` **× 39** and `terminology_guardrails` × 4 (`This guide`). Em dash is a hard ban and the live copy is built on it. `This guide is for bariatric clinic administrators…` in the intro breaks the Part-2 ban on `this article/guide`. |
| abbreviations (M1) | **FAIL — 4** | `GLP-1` (line 15), `HIPAA` (line 82), `DXA` and `BIA` (line 266) all used before first expansion. The M1 override covers BMI/CEO/UK/US/EU only, not these. |
| claim traceability | **FAIL — 31** | `claims_used: []` against `claims_known: 10`. Expected for scraped copy rather than a pipeline draft, but it does mean **no figure on the live page is tied to an approved claim id** — every one has to be re-traced on the rewrite. |
| internal links | **FAIL — trust** | 18 links, 15 distinct, `directions: {up: 1, sideways: 5, down: 1, trust: 0}` — see the note below on why this reading took two attempts. |
| accuracy discipline | ok, but | `accuracy_figures_present: False`, `links_to_framework: False`. The page discusses structured measurement data and never states a scoped accuracy figure or links the framework article. |

**The link gate was passing vacuously, and the pack was the reason.** The first run reported
`[ok] internal links` with every direction at `0`. That was not a result — `article_lint.py` gate 6
reads `internal_link_targets` from **inside** `content_strategy`, while this pack had emitted it at
top level, so the gate found no targets and passed on an empty set. Every other parseable pack in
`workspace/seo/_context-packs/` nests it, so the pack was the deviation, not the script. Nesting it
then surfaced a second shape mismatch: the gate expects each direction to be a string or a list of
`"URL  # notes"` strings, and this pack held a list of `{target, status}` maps, which crashed
`gate_links` on `w.split("#")`. Both fixed in the pack. The reading above is from the repaired run.

Two consequences worth carrying forward. **(a)** The corrected numbers partly soften §6c: the
up-link and down-link do resolve, and 5 of 6 sideways targets are present — the genuine misses are
the **occupational health hub** sideways and the **accuracy framework** trust link, which is the one
hard FAIL. The up-link resolves only through the auto-generated "You may also like" carousel, which
the linter cannot distinguish from a deliberate body link, so §6c's point stands editorially even
though the gate is now satisfied. **(b)** A gate that passes on an empty target set is
indistinguishable from a gate that passes on a correct page. Worth a `--report` check on any pack
before trusting a green link gate.

**Also found, pre-existing and out of scope here:** `2026-08-01-glp-1-market-hub-refresh.yaml` and
`2026-08-02-top-7-remote-body-composition-tools-glp-1-clinics.yaml` are **unparseable YAML** —
`banned_words` list items contain unquoted `: `, so the parser reads a mapping inside a sequence.
`article_lint.py` does not degrade gracefully on this: it raises an uncaught `ParserError` and dies,
so neither of those two articles can currently be linted against its own pack at all. Two things to
decide separately from this refresh: quote those list items, and give the pack loader a try/except.

**Section word counts — the "progress tracking is buried" claim, quantified:**

| Live H2 | Words |
|---|---|
| FAQ (three sub-blocks) | **1,319** |
| Pre-qualification | 400 |
| Pre-auth documentation | 380 |
| GLP-1 shift | 355 |
| The intake gap | 286 |
| Why scanning beats manual | 277 |
| **Post-procedure / longitudinal tracking** | **224** |
| Why programs need faster pre-qualification | 207 |
| What FitXpress captures | 202 |
| Where FitXpress fits (journey table) | 114 |

Total prose 4,068 words. **The FAQ is 32% of the article**, and patient progress tracking — the half
of the content plan's target title that is supposed to be co-headlined — gets 224 words, less than
either pre-qualification or pre-auth, and less than the GLP-1 section it depends on. The journey
table section, at 114 words, is the thinnest thing on the page.

---

## 8. What the refresh should therefore do

1. **Retitle** to the plan's use-case framing; co-headline progress tracking; drop the technology-first H1.
2. **Rewrite the pre-auth section around the CMS-0057-F clock** (§2b-a) — the 7-day standard decision
   window, published denial reasons, and first-pass completeness. Scope the rule's reach explicitly.
   This replaces "payer review windows run weeks to months," which is now wrong for impacted payers.
3. **Rebuild the GLP-1 section on 2026 data** — JAMA Surgery May 2026, ASMBS May 2026, the decline through
   2025, and the quantified bridge (§2b-b). Series A and B kept apart.
4. **Add the documented-BMI-history argument** (§2b-b) — the ~8% pre-surgical loss means current BMI and
   qualifying BMI history have come apart. This is the hub's sharpest new operational point.
5. **Fix the two substantiation defects** — the 50–60% attrition figure and the mis-cited eligibility claim.
6. **Promote patient progress tracking** from section 7 to a co-equal spine, per the plan's title.
7. **Resolve the "About bariatric surgery" block** — Vadim's call (see checkpoint question).
8. **Rebuild internal links** in all four directions; add link-down landing sections for the five P1 children.
9. **Keep** what already works: the four-stage pre-qualification workflow, the pathway table, the scope
   note and disclaimer, the compliance-posture paragraph, the operational-not-clinical framing throughout.

Republish in place at the same URL, as with `glp-1-market` (2026-08-28) and
`online-pharmacy-bmi-verification` (2026-08-24).
