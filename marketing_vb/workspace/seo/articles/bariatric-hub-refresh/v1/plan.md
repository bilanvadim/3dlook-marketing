---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
product: fitxpress
primary_keyword: bariatric pre-qualification
primary_use_case: brand-assets/product-info/use-cases/fx-bariatric-pre-auth.md
hub: "Hub 6 — Bariatrics"
cluster: Main hub
intent: Hub (BOFU-weighted)
action_type: refresh-expand-in-place
priority: P0
target_words: 4400
target_month: September 2026
live_url: https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/
baseline_file: published-live-2026-07-27.md
baseline_words: ~4100
author: Assel Sekerova
audit: plan-audit.md
status: approved
approved: 2026-09-03
checkpoint_1: closed
faq_branch: B
created: 2026-09-03
---

# SEO Plan — Bariatrics hub, refresh in place

> **CHECKPOINT 1 CLOSED — Vadim approved 2026-09-03. АПРУВ ЕСТЬ.**
> Proceed `write` → `edit` → `publish` in one pass, stopping only at checkpoint 2.
>
> **D-1 answered: Branch B — KEEP.** Vadim approved without naming a branch, which was taken as
> approval of the recommendation in `plan-audit.md` §D-1. Write the fourth FAQ block,
> *"Bariatric surgery basics"*, as **three** questions only: what is bariatric surgery · what are
> the main types (sleeve-gastrectomy share cited to the ASMBS Fact Sheet) · what are common program
> and payer requirements (framed as a documentation question, not an eligibility answer).
> **Benefits, side effects and pros-and-cons do not return.** They are clinical-outcome claims from
> a body-data vendor and the Bariatrics vertical does not own them.
> Budget offset, as planned: FAQ 520 → 700; Sections 1, 4 and 6 each drop 60 words. Total 4,400.
>
> **Title: the recommended H1**, with the `2026` signal. Slug unchanged.

**Republish at the existing URL. The slug does not change.** No net-new page, no second bariatric hub.
Everything below is a diff against `published-live-2026-07-27.md` (~4,100 words, 9 H2s, 20 FAQ questions).

The reasoning behind every choice here lives in `plan-audit.md` (coverage map, deletions ledger,
open items, the checkpoint-1 decision question). This file is what a writer needs to write.

---

## Content Strategy Fit (Phase 0)

- **Hub / cluster:** Hub 6 — Bariatrics → Main hub. This page *is* the hub.
- **Action type:** `Refresh / expand existing`. The Phase 0 gate normally stops here and returns a
  recommendation. **Gate overridden:** Vadim asked for the rewrite directly on 2026-09-03, which is
  the real gate. Same precedent as `glp-1-market` (2026-08-28) and
  `online-pharmacy-bmi-verification` (2026-08-24), both refresh/expand rows that shipped and were
  republished in place.
- **Why the refresh is justified, and it is not the row's reason.** The content-plan row asks to
  "expand with pre-auth, patient progress, GLP-1 bridge, and post-op tracking." The July 27 version
  already has H2s for all four. The row was seeded against the **June 5** version. The real case is
  that the page is factually stale: its GLP-1 section stops at 2023 data, its pre-auth section
  predates CMS-0057-F, and two substantiation defects are live.
- **Existing pages:**
  - `bariatric-pre-qualification-mobile-3d-body-scanning` — **this page**, the refresh target.
  - Five net-new P1 children (pre-auth documentation · GLP-1 bridge · post-op progress · patient
    records · hybrid care) are unpublished. The refresh must leave a **landing section each** so
    they can be linked down from when they ship. Anchors named per section below.
- **Cannibalization guardrail** (verbatim from `content-plan.md`): *"Keep bariatrics tied to
  obesity-care intake, pre-auth, pre-qualification, and patient progress. Do not duplicate GLP-1 or
  telehealth generic pages."*
  How it is honoured: GLP-1 market growth, employer coverage economics and drug-class comparison are
  **linked, not re-explained** (Hub 3 owns them). The KFF employer-coverage figure is removed from
  this page for exactly that reason. Telehealth workflow and remote-prescribing compliance are
  linked to the Telehealth hub and to Online Pharmacy BMI Verification. Body-composition methodology
  is linked to the accuracy framework.
- **Vertical boundary** (guidelines §9): Bariatrics **owns** bariatric pre-qualification, pre-auth
  documentation, obesity-care intake, post-op progress, and patient records. It does **not** own
  clinical care. No eligibility determination, no diagnosis, no procedure selection, no clinical
  outcomes of surgery (benefits, disease remission, side effects, complication rates), no clearance,
  no replacement of clinician review or of protocol-defined reference methods.
- **Sensitive vertical:** yes. Scope note plus italic disclaimer early, before Section 1.
- **Internal links planned:** up → Main Health Hub · side → GLP-1 Market, AI in Telehealth, Online
  Pharmacy BMI Verification, Occupational Health, Insurance Underwriting, Wellness Rewards · down →
  `/for-bmi-verification/` and the five P1 landing anchors · trust → accuracy framework in the same
  paragraph as every accuracy figure; Privacy/Regulatory FAQ as **plain text, never a link** (still
  unpublished). Full table at the end of this file.

---

## Keyword Analysis (Phase 1)

Ahrefs API v3, keywords-explorer, `country=us`, pulled 2026-09-03. Files in
`workspace/seo/_keywords/`. Figures below are as returned. **`null` is written "no data" and is not
the same thing as zero** — it means Ahrefs has no measurement for the exact phrase.

### This cluster is a deliberate zero-volume choice. Read Open Item #1 before approving.

**5 of 7 seeds returned no figure at all, and every phrase in the content plan's target title has
zero measured US demand.** The only real volume in the vertical is patient-facing. That is not a
reason to change the page's audience, and the cost of the alternative is set out in
`plan-audit.md` §K. It **is** a reason Vadim has to see this at checkpoint 1 rather than in Search
Console in six months, which is what happened with `remote-body-measurement-online-fitness-coaching`
on 2026-08-25.

### Primary cluster

- **Primary keyword:** `bariatric pre-qualification`
- **Monthly volume:** no data (Ahrefs returned no figure for the exact phrase, and no idea list)
- **Difficulty:** no data
- **Seed had data:** **false.** The topic as framed has no measured demand. The normal Phase 1 move
  is to swap in a head term from the idea lists that *does* have volume. **That move is refused
  here, deliberately**, because every term with volume in this vertical is patient-facing
  (`bariatric surgery requirements` 1,100/mo, `bariatric surgery` 69,000/mo) and adopting one as
  primary would change the page's audience, not its keyword. See `plan-audit.md` §K.
- **What this page is instead:** a BOFU / GEO / sales-enablement hub. Its measurable jobs are LLM
  answer capture on procurement-shaped questions, sales-conversation support, and being the hub the
  five P1 children link up to. Not organic volume.
- **Why the phrase stays anyway:** it is the term the URL, the slug and the existing H1 already own,
  the URL is not changing, and it is the concept the vertical boundary is drawn around.

### Secondary clusters

| Cluster | Keywords | Volume / KD | Intent | Where it is woven |
|---|---|---|---|---|
| Pre-auth documentation | `bariatric pre authorization`, `bariatric surgery pre authorization`, `prior authorization documentation` | no data (bariatric-specific); `pre authorization` 1,800 / KD 37 | Commercial / informational | S3, S9, FAQ Q3-Q4 |
| Patient progress record | `bariatric patient progress`, `bariatric patient progress record` | no data; `bariatric patient` 500 / KD 39 (TP 10) | Commercial | S8, FAQ Q7-Q10 |
| Obesity care operations | `obesity care`, `obesity care teams`, `metabolic clinic intake` | `obesity care` 80 / KD 53 (TP 80) | Informational | H1 subtitle, S2, S10 |
| Requirements documentation | `bariatric surgery requirements` used **only** in the documentation sense (what a program and payer require in the file) | 1,100 / KD 54 (TP 5,000) | Informational, patient-facing | FAQ Q3 only. **Boundary:** the answer describes what documentation programs and payers require. It does not tell a reader whether they personally qualify. |
| Post-op body composition | `body composition after bariatric surgery` | no data; `after bariatric surgery` 450 / KD 16; `body composition` 32,000 / KD 32 | Informational | S8. **Do not chase `body composition` (32,000/mo)** — Hub 1 / Hub 3 own it. |
| Remote intake | `remote bariatric intake`, `bariatric intake workflow` | `bariatric intake` no data | Commercial | S6. **Do not mine the `bariatric intake` idea list** — it is entirely post-op nutrition intake (protein, calories, water), a different sense of the word. |

**Do-not-touch idea lists:** `bariatric patient progress` (dominated by bariatric *equipment* queries
— patient lift, bed, chair, transport), `bariatric intake` (post-op nutrition), `body composition
after bariatric surgery` (patient-facing post-op lifestyle: diet, hair loss, pregnancy, exercise).

---

## Recommended Title

**H1:** **Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams**

Primary keyword in the first three words. Both spines co-headlined. The technology is absent from
the title, which is the point: CLAUDE.md §3 moved positioning to outcomes, workflow and governance,
and instructs SEO to write about the use case. The `2026` signal matches the sibling
`online-pharmacy-bmi-verification-a-2026-compliance-guide` and earns the refresh in the SERP snippet
and in LLM answers, at the cost of one annual title edit. It is cheap here because **the slug does
not change** and the year never enters the URL.

**Meta description (to be finalised by `seo-publisher`, direction only):** lead with the two
workflows and the payer clock, not with FitXpress. The live description leads with the product name.

### Other options

1. **Bariatric Pre-Qualification and Patient Progress Tracking: Body Data for Obesity Care Teams**
   — the content plan's target title, verbatim. Correct framing, co-headlines progress tracking,
   names the audience. Not chosen because "Body Data for Obesity Care Teams" carries no recency
   signal on a page whose entire refresh case is that the 2026 facts changed, and `obesity care`
   resolves to a conference (parent topic "obesity week"). **Use this if Vadim wants the plan's copy
   unchanged.**
2. **Bariatric Pre-Qualification, Pre-Auth Documentation, and Patient Progress Tracking: Body Data
   Across the Obesity Care Pathway** — most complete coverage of what the hub actually owns, and it
   names all three child-article clusters. Not chosen: 17 words, three colonless clauses before the
   colon, and it truncates in the SERP well before "Progress Tracking".
3. **Bariatric Pre-Qualification and Patient Progress Tracking: Documenting BMI History on a 7-Day
   Pre-Auth Clock** — the sharpest and most differentiated framing, built on the two strongest new
   arguments. Not chosen for the hub: the subtitle is entirely pre-auth, which under-serves the
   progress-tracking spine a hub has to hold. **Reserve it as the H1 for the P1 child "Bariatric
   Pre-Authorization Documentation."**
4. **Body Data for Bariatric Programs: Pre-Qualification, Pre-Auth Documentation, and Patient
   Progress Tracking** — leads with the deliverable rather than the workflow. Not chosen: pushes
   `bariatric pre-qualification` out of the first six words, and "Body Data" as an opener reads like
   a category page.

**Not an option:** anything leading with mobile 3D body scanning. That is the live H1's defect.

---

## Article Outline

Structure follows `content-strategy-guidelines.md` §12 (12 parts) and `about-me.md`'s standard
article structure. Bariatrics is a listed sensitive vertical, so the scope note and the italic
disclaimer land **before Section 1**, not in a footer.

### How to read `refresh_action`

| Value | Means |
|---|---|
| `KEEP` | The argument, structure and claims carry over. **Not the prose.** The live text is full of em dashes and of constructions the current terminology guardrails ban, so every kept sentence is still re-passed. Nothing on this page is safe to paste. |
| `REWRITE` | The section survives but its spine changes. The live counterpart is named. |
| `NEW` | No counterpart on the live page. |
| `CUT` | Removed. Full ledger in `plan-audit.md` §D. |

### Front matter — H1, Use Case Summary, opening, scope note

- **Goal:** State the buyer problem in the first sentence, name the two co-equal spines, and put the
  boundary on the page before any argument runs.
- **Word count target:** 300
- **refresh_action:** `REWRITE` — maps to live H1, live subtitle, live intro paragraphs 1-2 and the
  live `**Disclaimer.**` block.
- **Must-cover:**
  1. New H1 (above). New meta description that does not open with the product name.
  2. **Use Case Summary block**, the FX pattern (Industry / Problem / Solution / Outputs / Role /
     Business value), as a clean Markdown table. The live page has this content in Section 5 as a
     bullet list; promote it to the top, which is where the corpus puts it.
     `Role` reads: *supporting evidence for program and payer review, not eligibility or
     pre-authorization decisioning.*
  3. Opening two paragraphs: the structural mismatch between intake demand and surgical capacity,
     and the fact that patients now arrive with a longer treatment history than the intake stack was
     built for. Reframe move: not "how accurate is a remote scan" but "which record does a program
     need in the file, dated when, for whom to review."
  4. One orientation paragraph naming the audience: bariatric program directors, directors of
     operations, pre-authorization coordinators, medical directors at metabolic and obesity clinics.
  5. **Disclaimer, verbatim from the live page.** It is approved, em-dash-free, and "this article"
     is licensed inside a scope note (terminology guardrails §2.5). Reuse this exact framing in the
     five child articles:
     *"Mobile body scanning solutions described in this article do not determine medical eligibility
     for bariatric surgery, provide diagnoses, replace clinical evaluations, or make
     pre-authorization decisions. They produce body measurement and composition data intended as
     supporting evidence within decisioning workflows operated by licensed bariatric programs and
     their compliance and payer counterparts."*
- **Keywords to weave:** `bariatric pre-qualification`, `patient progress tracking`, `obesity care`
- **Approved claims:** none yet. No figure in the front matter.
- **Boundary:** the disclaimer is the boundary. Do not soften it and do not move it below the fold.

### Section 1 — The bariatric intake gap: eligibility confirmed late, documentation assembled after the consult

- **Goal:** Establish that the bottleneck is upstream, in verification and documentation, and fix
  both live substantiation defects while doing it.
- **Word count target:** 420
- **refresh_action:** `REWRITE` — merges live H2 #1 ("Why bariatric programs need faster
  pre-qualification") and live H2 #2 ("The intake gap: when eligibility gets confirmed too late").
  Two sections became one because the live pair repeats its own premise.
- **Must-cover:**
  1. `KEEP` CDC prevalence: 40.3% of US adults have obesity and 9.4% have severe obesity (BMI ≥30
     and ≥40), August 2021 to August 2023 cycle. **Do not mix the 9.4% crude figure with the 9.7%
     age-adjusted trend figure from the same brief.** Still the most recent
     clinical-measurement cycle as of 2026-09-03.
  2. **Substantiation fix 1 of 2 — the eligibility gap.** `CUT` the live sentence "an estimated 33
     million US adults meet eligibility criteria, yet fewer than 1% complete surgery in any given
     year" and `CUT` its citation, which points at a qualitative attrition paper that is not an
     eligibility-prevalence source. Replace with two ASMBS statements that carry their own numbers:
     "about 1% of those who meet eligibility requirements" (2025 Fact Sheet) and **90-95% of
     patients with severe obesity received no treatment during the study period** (ASMBS, 5 May
     2026). Do not reconstruct a "33 million" figure from CDC prevalence; no source on file
     supports it.
  3. `KEEP` the self-report data-quality point: CDC researchers reported in *Preventing Chronic
     Disease* that self-reported BMI underestimated the prevalence of severe obesity by 40% (5.3%
     self-report against 8.8% after bias correction, 2020 data). Re-verify the exact wording at
     fact-check.
  4. **Substantiation fix 2 of 2 — attrition.** `CUT` "pre-operative dropout rates of up to 50-60%
     are reported across bariatric programs", which publishes the top of a range as if it were
     typical. Restate as the range **with its methodology dependence**: a 2026 narrative review
     reports figures as high as 60%, one cohort reports 22.25%, Canadian programs with mandatory
     pre-operative pathways complete at roughly 36% to 76%, US programs at roughly 39% to 70%, and
     one single-centre series reported 8.9% before the pandemic. The variability is the argument:
     attrition depends on program design and on how attrition is measured, which is a stronger case
     for standardised intake data than a single scary number. Guardrails #1 and #4.
  5. Close on the operational consequence: consult slots, OR days and pre-authorization coordinators
     are finite, so when intake demand rises against unchanged surgical capacity the bottleneck moves
     upstream into verification and documentation.
- **Keywords to weave:** `bariatric pre-qualification`, `obesity care`, `bariatric intake workflow`
- **Sources:** `https://www.cdc.gov/nchs/products/databriefs/db508.htm` ·
  `https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf` ·
  `https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/` ·
  `https://www.cdc.gov/pcd/issues/2023/23_0005.htm` ·
  `https://pmc.ncbi.nlm.nih.gov/articles/PMC12964095/`
- **Approved claims:** none. No FitXpress figure in this section.
- **Boundary:** prevalence and attrition are context, not a clinical argument. Do not imply that a
  scan reduces attrition; the claim is that in-person verification steps are funnel-loss points.

### Section 2 — Short answer: what structured body data contributes, and what still decides

- **Goal:** GEO/AEO answer block. Define bariatric pre-qualification and a patient progress record
  in two paragraphs an LLM can lift, and put the "who decides" boundary in the same breath.
- **Word count target:** 180
- **refresh_action:** `NEW` — the live page has no short-answer block. The pattern comes from the
  refreshed `glp-1-market` hub, which opens with a bolded **Short answer.** followed by an italic
  scope note.
- **Must-cover:**
  1. **Short answer.** in bold, 3 to 4 sentences: bariatric pre-qualification is the intake step in
     which a program assesses whether an inquiry meets its eligibility criteria and payer
     medical-necessity criteria before a full clinical consult is scheduled. A patient progress
     record is the dated, comparable body-data series a program keeps from before the procedure
     through long-term follow-up. Structured remote body data supplies the measurement inputs for
     both. The eligibility determination and the pre-authorization decision are made elsewhere.
  2. One sentence naming what "structured" means here operationally: same guided capture sequence
     each time, machine-readable output, capture timestamp, comparable across patients and across
     time.
  3. **Link up to the hub** on the anchor phrase, first curated internal link on the page.
- **Keywords to weave:** `bariatric pre-qualification`, `bariatric patient progress record`,
  `obesity care teams`
- **Internal link:** up → `https://3dlook.ai/content-hub/ai-body-data-health-hub/`
- **Approved claims:** none.
- **Boundary:** the definition must not read as eligibility guidance. It defines the program's step,
  not the patient's chances.

### Section 3 — Why now (1): prior authorization runs on a 7-calendar-day clock

- **Goal:** Replace the live page's "weeks to several months" with the current rule, and invert the
  argument from "cleaner packets, fewer delays" to "first-pass completeness is the whole game."
- **Word count target:** 420
- **refresh_action:** `NEW` argument, replacing the payer-timeline paragraph inside live H2 #6
  ("Pre-auth documentation: cleaner packets, fewer delays"). This is the single most important
  factual change on the page.
- **Must-cover:**
  1. CMS Interoperability and Prior Authorization Final Rule **CMS-0057-F**, operational since
     **1 January 2026**. Impacted payers must decide prior authorizations within **72 hours
     (expedited)** and **7 calendar days (standard)**, must give **specific reasons for each
     non-drug denial** regardless of submission channel, and must **publicly report
     prior-authorization metrics annually**, with initial reporting due **31 March 2026**.
  2. **Scope, stated explicitly and in the same section, not in a footnote.** The rule reaches
     Medicare Advantage, Medicaid, CHIP and Qualified Health Plans on the Federally Facilitated
     Exchange. It does **not** cover all commercial ERISA plans. Medicare fee-for-service does not
     use prior authorization for bariatric procedures at all. A program's payer mix therefore
     determines how much of its volume sits on this clock.
  3. `CUT` the live sentence "Payer review windows commonly run from a few weeks to several months."
     For impacted payers on standard requests it is now wrong. Do not replace it with a new
     universal number; the honest statement is that the window depends on the payer, the plan type
     and whether the request is expedited.
  4. The inversion, which is the section's spine: on a 7-day clock there is no room for a leisurely
     request-for-more-information cycle. A missing timestamped BMI record stops being a delay and
     becomes a denial with a published reason. Published denial reasons also mean the pattern of a
     program's incomplete submissions becomes legible over time.
  5. What a standard bariatric pre-authorization packet typically contains: documented BMI history,
     comorbidity confirmation, prior weight-loss attempts, supervised diet program participation
     where required, psychological evaluation outcomes, and a body-measurement record. `KEEP` this
     list from live H2 #6.
  6. **Down-link landing anchor** for the P1 child *"Bariatric Pre-Authorization Documentation: What
     Body Data Payers May Need"*. Leave one sentence whose anchor phrase that child can take over.
- **Keywords to weave:** `bariatric pre authorization`, `prior authorization documentation`,
  `pre-auth cycle time`
- **Sources:** `https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f`
- **Approved claims:** none. FitXpress does not appear in this section; it is a regulatory
  "why now."
- **Boundary:** describe the rule, never interpret it as legal advice, and never imply that
  structured body data guarantees an approval or shortens the payer's own clock. The claim is about
  first-pass submission completeness, which the program controls.
- **Internal link:** sideways → `https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/`
  on the BMI-verification-methodology anchor, so this section does not re-explain verification
  mechanics that page already owns.

### Section 4 — Why now (2): GLP-1 reshaped the funnel, not just the volume

- **Goal:** Rebuild the stalest section on 2026 data, and keep three irreconcilable volume series
  from contaminating each other.
- **Word count target:** 460
- **refresh_action:** `REWRITE` — live H2 #3 ("The GLP-1 shift: volume contracted, intake complexity
  rose"). The argument survives; every number in it changes.
- **Must-cover:**
  1. **A market-indicator table**, reusing the pattern from the refreshed `glp-1-market` hub:
     columns `Indicator | Figure, with the citation on the anchor | What it indicates`. That pattern
     exists precisely to stop incompatible figures from being read as one series. Rows:

     | Indicator | Figure | What it indicates |
     |---|---|---|
     | US procedure volume, 2023 | more than 270,000 procedures, down about 3.5% from the prior year — ASMBS 2025 Fact Sheet, a national estimate built from BOLD, ACS/MBSAQIP, National Inpatient Sample data and outpatient estimations; **the series ends at 2023** | The national volume anchor. |
     | Utilization change, 2022 to 2024 | metabolic bariatric surgery utilization down **34.1%**, GLP-1 receptor agonist use up **140.4%** over the same period — JAMA Surgery, 13 May 2026, **a claims cohort** | A utilization rate inside one insured cohort. Absolute counts in the same cohort move about −7.3%. Not a national count. |
     | Cohort procedure counts | 40,265 (2022), 42,615 (2023), 37,339 (2024), **33,429 (2025)** — same claims cohort | The decline continued into 2025 within that cohort. The live page stopped at 2023. |
     | Untreated share | **90-95%** of patients with severe obesity received no treatment during the study period — ASMBS, 5 May 2026 | The distance between eligibility and any treatment at all. |

  2. **A note directly under the table**, not buried: the two series use different populations and
     methods and are not comparable. ASMBS states that its own estimates use broader patient
     populations and additional datasets than the study. **Hard rule for the writer: the ASMBS
     national estimate and the JAMA Surgery cohort never appear in the same sentence, and every
     cohort figure carries its cohort scope.**
  3. `CUT` the live "bariatric surgery use fell 8.7% between 2022 and 2023" and its StatNews
     citation. It is the smaller, older cut of the same story, and it is secondary trade press where
     a primary source now exists.
  4. `KEEP` the intake-complexity evidence from the American College of Surgeons Bulletin, April
     2025: GLP-1 medications as "the initial gateway for a lot of patients" who later move toward
     surgery (Funk), and "Most of my colleagues around the country are seeing an increase in new
     consults coming for surgery" (Kurian).
  5. `KEEP` the net argument, now better supported: a wider and more heterogeneous intake funnel
     feeding unchanged surgical capacity makes structured pre-qualification more valuable, not less.
  6. `CUT` the KFF employer-coverage sentence (43% of firms with 5,000 or more workers in 2025, up
     from 28%). Hub 3 owns GLP-1 market and coverage stats and already carries that row. Replace
     with one sentence and a **sideways link** to the GLP-1 Market hub. This is the cannibalization
     guardrail being enforced, not a gap.
  7. **Down-link landing anchor** for the P1 child *"GLP-1 Before Bariatric Surgery: Why Body
     Composition and Progress Matter"*.
- **Keywords to weave:** `GLP-1 before bariatric surgery`, `bariatric surgery volume`,
  `obesity care`
- **Sources:** ASMBS 5 May 2026 release
  `https://asmbs.org/news_releases/as-glp-1-use-skyrockets-and-bariatric-surgery-slows-most-obesity-goes-untreated/` ·
  ASMBS 2025 Fact Sheet `https://asmbs.org/wp-content/uploads/2025/06/MBSFactSheet2025.pdf` ·
  ACS Bulletin April 2025 `https://www.facs.org/for-medical-professionals/news-publications/news-and-articles/bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/` ·
  JAMA Surgery 13 May 2026 (Calzaretta et al., Analysis Group) — **cite the journal or the ASMBS
  release, not the aggregator.** `https://www.eurekalert.org/news-releases/1127781` is the fallback
  locator only; terminology guardrails §1.3 prefers the primary.
- **Internal link:** sideways → `https://3dlook.ai/content-hub/glp-1-market/`
- **Approved claims:** none.
- **Boundary:** do not adjudicate whether medication or surgery is the better treatment. Do not use
  "surgery appears to be rebounding" (no primary citation yet — Open Item #7). Do not use the
  semaglutide exclusivity story: the 2026 expiries are ex-US and this page's audience is US
  programs.

### Section 5 — Why now (3): current BMI and qualifying BMI history have come apart

- **Goal:** The sharpest new operational point on the page, and the one that lands entirely on
  documentation rather than on a clinical claim. Give it its own section, not a paragraph.
- **Word count target:** 350
- **refresh_action:** `NEW` — nothing on the live page makes this argument.
- **Must-cover:**
  1. The finding, with its scope: ASMBS, 5 May 2026, Chhabra et al., NYU Grossman School of
     Medicine, presented at ASMBS 2026. Epic Cosmos electronic health records, 2019 to 2025,
     **6,700 patients with prior GLP-1 use** (2,395 gastric bypass, 4,315 sleeve gastrectomy)
     against roughly **127,000 without**, followed three years. Patients lost about **8% of total
     body weight on GLP-1s before surgery**; total loss reached more than **25% after gastric
     bypass** and about **20% after sleeve gastrectomy**.
  2. The operational consequence, which is the section: a patient who has already lost about 8% of
     body weight on a GLP-1 may arrive at consult with a **current** BMI below a payer's threshold
     while their **documented history** still qualifies. Eligibility therefore increasingly turns on
     dated, verifiable BMI history rather than on one measurement taken at the consult.
  3. Why that is a records problem before it is a clinical one: a timestamped serial-scan record
     carries its own date and capture conditions. A tape measurement recorded in a free-text note
     does not, and a reviewer at the payer cannot verify when or how it was taken. Tie back to the
     7-day clock in Section 3: a history that has to be reconstructed after a
     request-for-information does not fit inside seven calendar days.
  4. One sentence on the reverse direction, since the same pathway runs both ways: medications may
     also serve as a bridge to later surgery, which is why an intake record that starts before the
     medication is more useful than one that starts at the surgical consult.
  5. **Down-link landing anchor** shared with Section 4's GLP-1 bridge child, and with the P1 child
     *"What Body Data Should Be in a Bariatric Patient Progress Record?"*
- **Keywords to weave:** `documented BMI history`, `bariatric surgery requirements` (documentation
  sense only), `GLP-1 before bariatric surgery`
- **Sources:** `https://asmbs.org/news_releases/new-study-finds-metabolic-and-bariatric-surgery-after-glp-1-treatment-significantly-boosts-weight-loss/`
- **Approved claims:** none in this section. The argument is about records, and pulling an accuracy
  figure in here would invite the reading that the scan settles eligibility.
- **Boundary:** **hard.** Do not state or imply what BMI qualifies a patient, what a payer threshold
  is, or that a documented history secures an approval. The claim is that the program's file needs
  dated measurements, and that the program and payer decide what the file means. Do not present the
  8% figure as a treatment outcome recommendation.

### Section 6 — The pre-qualification workflow: moving the measurement step to intake

- **Goal:** The concrete four-stage workflow. This is what already works on the live page and it is
  what a buyer screenshots.
- **Word count target:** 420
- **refresh_action:** `KEEP` — live H2 #5 ("Pre-qualification: structured body data before the
  consult"), stages 1 to 4 intact. Light `REWRITE` only: the Use Case Summary bullet list moves to
  the front matter, the em dashes go, and Stage 2 and Stage 4 pick up the Section 3 clock and the
  Section 5 history argument.
- **Must-cover:**
  1. The frame: the redesign moves the body-measurement step from stage three back to stage one.
  2. **Stage 1 — remote scan at intake.** After the baseline questionnaire, the program sends a scan
     link and the patient completes the guided two-photo capture on their own smartphone, typically
     the same day. The program receives a structured record.
  3. **Stage 2 — pre-consult review.** A coordinator or clinical reviewer checks the output against
     the program's eligibility thresholds and any program-specific intake criteria before scheduling
     the consult. Patients who clearly meet criteria move into a clinical-evaluation consult; others
     are routed into medical-management or referral pathways without occupying a surgical consult
     slot. **Down-link** to `/for-bmi-verification/` on the verification-capability anchor.
  4. **Stage 3 — clinical consult.** The visit opens with the body data already in the record, so the
     conversation starts at history, comorbidities, surgical risk and patient education instead of
     at measurement.
  5. **Stage 4 — documentation handoff.** The same record that supported the triage decision is
     available to the pre-authorization coordinator from the start of the case. Connect explicitly to
     Section 3: on a 7-day standard clock, "available from the start" is the difference between a
     first-pass submission and a resubmission.
  6. `KEEP` the mechanism paragraph, which is the section's most important sentence and must not be
     softened: the scan does not determine whether a patient is medically eligible. What it supplies
     is a structured, verifiable body-data signal the program uses to triage which consult slots are
     opened, in what order, and with what supporting record already attached.
  7. **Down-link landing anchors** for the P1 children *"Remote Body Measurement for Bariatric
     Patient Intake"* and *"Hybrid Bariatric Care: Virtual Check-Ins With Standardized Body Data"* —
     one sentence in Stage 1 and one in Stage 2 respectively.
- **Keywords to weave:** `bariatric pre-qualification`, `bariatric intake workflow`,
  `remote bariatric intake`, `consult-to-procedure conversion`
- **Internal link:** down → `https://3dlook.ai/for-bmi-verification/`
- **Approved claims:** FX-007 may be referenced in a clause if the front matter has not already
  carried it. Prefer to keep the numbers in Section 7.
- **Boundary:** triage is not decisioning. Every stage description names the human who reviews.

### Section 7 — Where FitXpress fits across the bariatric pathway

- **Goal:** Product mechanics and pathway coverage in one place, so the workflow sections stay about
  the workflow. This is the only section that carries an accuracy figure.
- **Word count target:** 280
- **refresh_action:** `REWRITE` — merges live H2 #4 ("What FitXpress captures, and how") and live H2
  #8 ("Where FitXpress fits in the bariatric patient journey"). The two say the same thing at
  different altitudes.
- **Must-cover:**
  1. FX-007, verbatim in substance: two photos, guided capture, results in under 45 seconds, 80+
     body measurements along with BMI, BMR, body-fat percentage, and lean and fat mass. No
     specialized hardware.
  2. `KEEP` the three properties that matter for this use case, unchanged in substance:
     timestamped structured outputs; remote capture, which removes the appointment slot as the
     verification gate; and the compliance posture, which is expanded in Section 10.
  3. **One accuracy paragraph, and the accuracy-framework link must sit inside it**, not in a
     footer. Use FX-001 verbatim: *"Internal validation across multiple real-world scan events with
     five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's
     measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error
     of 1.5-2.0 cm per measurement, varying by body part."* Then the condition, in the same
     paragraph: accurate enough for which decision, against which reference, under which protocol,
     for which population. **Do not put the ISO 8559 benchmark on this page at all** (see
     `plan-audit.md` §C).
  4. `KEEP` the **patient-journey table** from live H2 #8, as a clean Markdown table:
     Inquiry / Pre-consult / Pre-auth / Procedure preparation / Post-surgery follow-up / Long-term
     monitoring, each with the capture's role. Add nothing to it; it already works.
  5. `KEEP` the closing point: one capture asset, applied repeatedly across the pathway, in place of
     fragmented manual measurements that today live in separate parts of the program's workflow.
- **Keywords to weave:** `mobile body scanning`, `structured body data`, `bariatric patient journey`
- **Internal links:** trust → `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`
  **in the accuracy paragraph itself** · `https://3dlook.ai/technology/` (already live, keep)
- **Approved claims:** FX-007, FX-001.
- **Boundary:** the accuracy figure exists to be conditioned, not to impress. No figure without its
  reference method, population and workflow. Reserved words are off-limits about our own evidence:
  no `independent`, `third-party`, `validated`, `clinically validated`, `peer-reviewed`.

### Section 8 — Patient progress tracking after the procedure

- **Goal:** Promote progress tracking from a subordinate section to a co-equal spine, as the H1 now
  promises. This section has to earn the second half of the title.
- **Word count target:** 400
- **refresh_action:** `REWRITE` and expand — live H2 #7 ("Post-procedure: turning the baseline into
  longitudinal tracking"), which is currently the seventh of nine sections and about 300 words.
- **Must-cover:**
  1. The baseline logic: the scan captured before surgery is the reference the follow-up scans are
     compared against, and the capture sequence is the same each time, so a scan taken three months
     after the procedure is structurally comparable to the baseline instead of being a separate
     ad-hoc measurement.
  2. **Repeatability is the property that matters for longitudinal use, not accuracy**, and this is
     the section where that distinction is made. FX-002 verbatim: *"For most evaluated measurements,
     repeated scans showed typical scan-to-scan differences of less than 1 cm."* Link the accuracy
     framework **in this paragraph too**, on the repeatability-versus-accuracy anchor. FX-008 in the
     same area, correctly scoped: weight estimation carries a ±3.5% average error margin and is a
     software output, not a scale. **Do not put the ISO figure in this paragraph or anywhere else on
     the page.**
  3. `KEEP` the composition argument: the same weight can sit on top of different body-composition
     profiles, and the difference matters for patient counselling, program-level outcome reporting
     and the multidisciplinary team (nutrition, behavioural health, surgical follow-up).
  4. `KEEP` the adjunct-medication point: roughly one in seven bariatric patients initiate GLP-1
     therapy after surgery (Johns Hopkins reporting on a JAMA Surgery analysis), so the
     post-procedure window increasingly includes a pharmacotherapy component alongside surgical
     recovery. A baseline scan plus serial follow-up scans give the program a body-data series that
     is visible across the full window and does not depend on medication adherence to be recorded.
  5. `KEEP` the counselling artifact: a side-by-side comparison between the baseline capture and a
     recent scan is a tangible artifact for patient counselling, often more useful than a single
     weight number. Absorbs the live FAQ question on visual progress tracking.
  6. **NEW, and this is the promotion:** what belongs in a bariatric patient progress record and at
     what cadence. Name the components (dated BMI, waist and hip circumference, body-composition
     estimates, the capture-quality outcomes from the guided flow) and state plainly that the
     cadence is set by the program's monitoring protocol. This is the **down-link landing anchor**
     for the two P1 children *"Tracking Body Changes After Bariatric Surgery Beyond Weight Loss"*
     and *"What Body Data Should Be in a Bariatric Patient Progress Record?"*
- **Keywords to weave:** `bariatric patient progress`, `patient progress tracking`,
  `body composition after bariatric surgery`, `bariatric patient progress record`
- **Sources:** `https://publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs`
- **Internal links:** trust → `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` ·
  sideways → `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/` on the
  remote-follow-up anchor
- **Approved claims:** FX-002, FX-008.
- **Boundary:** **hard.** Post-operative progress tracking is supporting evidence inside the
  program's monitoring workflow. It is never medical advice, never a clinical decisioning output,
  and never a nutritional or recovery recommendation. Do not drift into post-op diet, vitamins,
  protein targets or exercise: that is the patient-facing content the keyword idea lists are full of
  and it is outside the vertical boundary. Do not claim the scan detects a complication or a
  plateau.

### Section 9 — What improves operationally, and what FitXpress does not do

- **Goal:** §12 items 6 and 7 in one place, capability and limit in the same breath, which is the
  house voice.
- **Word count target:** 250
- **refresh_action:** `REWRITE` — takes the documentation-mechanics half of live H2 #6 and the
  audit-posture bullets of live H2 #9, and adds an explicit boundary block the live page only has as
  a top disclaimer.
- **Must-cover:**
  1. What changes in the pre-authorization packet: a structured body-data file with a capture
     timestamp, the capture-quality outcomes from the guided flow, and the measurement set in a
     machine-readable format, consistent across patients because the capture sequence is the same
     each time. Serial captures on the same timeline (baseline at intake, a second before
     submission, a third before the procedure) produce comparable records.
  2. `KEEP` the anti-manipulation paragraph, hedged as it already is: live in-session capture rather
     than a camera-roll upload, real-time pose validation, built-in clothing detection. State the
     limit in the same breath per guardrail #5: these controls reduce risk, they do not remove the
     need for capture instructions, retake logic or deployment-specific thresholds. **Never**
     "fraud detection"; "fraud-prevention support" only.
  3. **What FitXpress does not do**, as its own short bolded list, drawn from the disclaimer and
     stated once each without stacking negations (guardrail M2): it does not determine medical or
     surgical eligibility, does not diagnose, does not replace clinical evaluation, does not make
     the pre-authorization decision, does not guarantee compliance or an approval, and is not
     equivalent to DXA, bioelectrical impedance analysis or a calibrated scale where the workflow,
     protocol or regulatory standard requires those methods. Include the licensed sentence: *"It is
     not positioned as a medical device."*
  4. **Down-link landing anchor** for the P1 children *"Bariatric Pre-Authorization Documentation"*
     and *"What Body Data Should Be in a Bariatric Patient Progress Record?"*, and for the P2 lead
     magnet *"Bariatric Documentation Checklist"*.
- **Keywords to weave:** `bariatric pre authorization`, `audit-ready records`,
  `pre-auth documentation`
- **Approved claims:** none new. Reference FX-009's posture only by pointer; the detail is Section 10.
- **Boundary:** this section *is* the boundary. "Positioned as" is banned everywhere except the
  medical-device sentence. Do not write that a framework "does not apply."

### Section 10 — Comparison, buyer fit, and what to confirm before a pilot

- **Goal:** §12 items 8, 9 and 10 compressed into one closing operational section: the decision
  framework, who this fits, and the diligence list.
- **Word count target:** 300
- **refresh_action:** `REWRITE` — live H2 #9 ("Why mobile body scanning beats manual measurement
  workflows"). The four bullets survive as arguments; the framing does not. `beats` is hype and the
  title is technology-first. Convert the prose list into a comparison table, which is what the
  argument structurally is.
- **Must-cover:**
  1. **Comparison table**, `Workflow area | Manual measurement at the consult | Guided scan-based
     capture`, modelled on the clinical-trials article's table. Rows: appointment slot required ·
     cross-clinic and cross-operator comparability · what a payer reviewer can verify · reuse across
     pre-qualification, pre-auth and post-op · what it depends on. Compare by role, never a clean
     sweep. Manual measurement at the consult stays where the program's protocol requires it.
  2. **Buyer fit**, short: bariatric surgery centers, hospital programs, multi-site surgical
     networks, metabolic and obesity clinics. Buyer roles: director of operations, medical director,
     VP patient access, COO at multi-site networks. Name the KPIs they actually own:
     consult-to-procedure conversion, late-stage disqualifications and cancellations, pre-auth cycle
     time, staff time per pre-auth packet. Multi-site networks are the case where cross-site
     consistency is the whole point; **sideways link** to the Occupational Health hub, which owns
     the multi-site-consistency argument in its own vertical.
  3. **Evaluation considerations, and this is where the honest limits go.**
     - FX-009's compliance posture: HIPAA-maintained for US healthcare contexts, BAA-ready,
       GDPR-aligned, AWS S3 SSE-S3 encryption at rest, TLS in transit, no personal identifiers
       processed, photos deleted immediately after processing or within a configurable retention
       window. **Do not claim SOC 2 certification.** Keep the privacy and regulatory detail as
       **plain text with no link** — the central Data, Privacy, Security and Regulatory FAQ is still
       unpublished, and the live page already handles this correctly.
     - FX-005, and it matters more here than in any other vertical: the internal validation
       population included participants aged 16 to 78, heights of 150 to 220 cm, weights of 38 to
       210 kg, and participants from the US and Europe. Performance outside this scope has not been
       characterized. A severe-obesity intake population includes patients above that weight range,
       and a program evaluating this should know that before a pilot rather than after.
     - FX-006: 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through
       a third-party clinical study.
     - One sentence that these are the floor to confirm with any vendor handling patient body data,
       before a pilot begins.
- **Keywords to weave:** `manual measurements vs body scanning`, `bariatric clinics`,
  `obesity care teams`
- **Internal link:** sideways → `https://3dlook.ai/content-hub/occupational-health-screening-software/`
- **Approved claims:** FX-009, FX-005, FX-006.
- **Boundary:** no competitor is named, ever, in any form. No pricing. No "most accurate." The
  comparison answers which method fits which workflow.

### Section 11 — FAQ

- **Goal:** GEO/AEO capture on procurement-shaped questions. Answers 2 to 5 sentences, direct, each
  one liftable on its own.
- **Word count target:** 520 under Branch A (13 questions, about 40 words each). **Branch B adds
  about 180 words** and three questions — see the decision below.
- **refresh_action:** `REWRITE` — the live FAQ has **20** questions across three blocks with heavy
  internal overlap. Six live questions are absorbed into others, six are `CUT` pending the decision
  below, and five are `NEW`. Per-question mapping in `plan-audit.md` §F.
- **Branch A — the 13 questions to write** (the recommended core, unaffected by the decision):

  *Pre-qualification and pre-authorization documentation*
  1. What is bariatric pre-qualification? — `KEEP`
  2. How can bariatric programs pre-qualify patients remotely? — `KEEP`, absorbing the live
     "mobile body scanning support bariatric intake workflows" and "early bariatric patient
     screening" questions
  3. What body-data documentation do payers commonly require in a bariatric pre-authorization
     packet? — `REWRITE`, absorbing two live pre-auth questions. **This is the one place
     `bariatric surgery requirements` (1,100/mo) is answered, and it is answered as a documentation
     question.** It describes what programs and payers require in the file. It does not tell a
     reader whether they qualify.
  4. How long do payers have to decide a bariatric prior authorization? — `NEW`. CMS-0057-F, 72
     hours expedited and 7 calendar days standard, **with the scope limitation in the answer
     itself.**
  5. Why does documented BMI history matter more when a patient has been on a GLP-1? — `NEW`
  6. How can programs reduce wasted bariatric consult slots? — `KEEP`

  *Patient progress tracking*
  7. What body data belongs in a bariatric patient progress record? — `REWRITE` of the live
     "what body measurements matter after bariatric surgery"
  8. Why is weight alone not enough for bariatric progress tracking? — `KEEP`, absorbing the live
     body-composition question
  9. How can bariatric programs monitor patients remotely after surgery? — `KEEP`
  10. How is a follow-up scan compared with the baseline? — `REWRITE` of the live patient-facing
      "how can patients track progress after bariatric surgery", reframed to the program's workflow

  *Scope and governance* (all `NEW`; guidelines §14 names these as required FAQ types)
  11. Is scan data used to make eligibility or pre-authorization decisions?
  12. Who reviews the scan data?
  13. What does FitXpress not do in a bariatric program, and can it replace in-clinic measurement? —
      absorbs the live "Can FitXpress replace in-clinic measurements?"

- **The decision that changes this section:** the live *"About bariatric surgery"* block (what is
  bariatric surgery · main types · common requirements · benefits · side effects · pros and cons)
  answers clinical-care questions and sits outside the vertical boundary. **Full trade-off and
  recommendation: `plan-audit.md` §D-1.** Both branches are planned so Vadim's answer does not force
  a re-plan:
  - **Branch A (cut):** write the 13 questions above. Total stays 4,400.
  - **Branch B (keep):** add a fourth block, *"Bariatric surgery basics"*, of **three** questions
    rewritten to carry no clinical-outcome claim: what is bariatric surgery; what are the main types
    (with the sleeve-gastrectomy share cited to the ASMBS Fact Sheet); what are common program and
    payer requirements. **The benefits, side-effects and pros-and-cons answers do not return under
    either branch** — they are clinical-outcome claims from a body-data vendor and the vertical does
    not own them. Budget offset: FAQ 520 → 700, and Sections 1, 4 and 6 each drop 60 words. Total
    stays 4,400.
- **Keywords to weave:** every secondary cluster gets one FAQ question. `bariatric surgery
  requirements` appears in Q3 only under Branch A.
- **Approved claims:** none new. Any figure repeated in an answer must be byte-identical to the
  body (guardrail #2).
- **Boundary:** no answer states a qualifying BMI, recommends a procedure, or describes a clinical
  outcome of surgery.

### Section 12 — Next steps and related reading

- **Goal:** BOFU CTA, and rebuild the four link directions that the live page half-does.
- **Word count target:** 100
- **refresh_action:** `REWRITE` — live CTA block and live "Related reading", which is two links and
  stale.
- **Must-cover:**
  1. **BOFU CTA, direct** (§15, and this is a hub with BOFU weight, not a TOFU explainer): see how
     FitXpress can support pre-qualification, pre-auth documentation and post-procedure progress
     tracking in a bariatric program. Request a demo or contact sales. One CTA only.
     Target: `https://3dlook.ai/for-bmi-verification/`. **Demo only, never a self-serve trial** —
     compliance-buyer audience.
  2. **Related reading, rebuilt.** Add the four missing siblings, keep the two that are there:
     Main Health Hub (up) · GLP-1 Market · AI in Telehealth · Online Pharmacy BMI Verification ·
     Occupational Health · Insurance Underwriting (keep) · Wellness Rewards Verification (keep).
     **Do not link the Wellness Platforms hub** — its draft has no `FINAL-PUBLISHED.md` and it is
     not live.
  3. **Decide the eBook promo block** currently sitting mid-article after live Section 2
     (*"The Digital Health Revolution"*). It is a second CTA in the body, which the style guide
     forbids. Open Item #10.
- **Approved claims:** none.
- **Boundary:** no pricing signal in a content-hub article.

---

## Article meta

| Section | Target words | refresh_action |
|---|---|---|
| Front matter (H1, Use Case Summary, opening, disclaimer) | 300 | REWRITE |
| 1. The bariatric intake gap | 420 | REWRITE (live #1 + #2) |
| 2. Short answer | 180 | NEW |
| 3. Why now (1): the 7-day prior-authorization clock | 420 | NEW |
| 4. Why now (2): GLP-1 reshaped the funnel | 460 | REWRITE (live #3) |
| 5. Why now (3): current BMI and qualifying history | 350 | NEW |
| 6. The pre-qualification workflow | 420 | KEEP (live #5) |
| 7. Where FitXpress fits across the pathway | 280 | REWRITE (live #4 + #8) |
| 8. Patient progress tracking after the procedure | 400 | REWRITE + expand (live #7) |
| 9. What improves, and what FitXpress does not do | 250 | REWRITE (live #6 + #9) |
| 10. Comparison, buyer fit, and pilot diligence | 300 | REWRITE (live #9) |
| 11. FAQ | 520 | REWRITE (20 questions → 13) |
| 12. Next steps and related reading | 100 | REWRITE |
| | | |
| | **Total** | **4400** |

- **Estimated read time:** about 20 minutes
- **Baseline:** ~4,100 words, 9 H2s, 20 FAQ questions → 12 sections, 13 FAQ questions. Net word count
  is roughly flat; the composition changes substantially.
- **Branch B variant:** FAQ 520 → 700, Sections 1, 4 and 6 each −60. Total unchanged at 4,400.
- **CTA placement:** one, in Section 12. No mid-body second CTA (Open Item #10 covers the live eBook
  block).
- **H2 count:** 12. Style guide range for a use-case deep-dive is 11 to 15.
- **Article type:** Type A, use-case deep-dive, per `blog-style-guide.md` §9.

### Internal links, four directions

| Direction | Target | Where | Status on live page |
|---|---|---|---|
| up | `https://3dlook.ai/content-hub/ai-body-data-health-hub/` | S2 | **GAP.** Appears only in the auto-generated carousel, which is not a deliberate link. |
| sideways | `https://3dlook.ai/content-hub/glp-1-market/` | S4 | **Missing.** Link, do not re-explain its stats. |
| sideways | `https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` | S3 | **Missing.** Link for BMI-verification methodology. |
| sideways | `https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/` | S8 | **Missing.** |
| sideways | `https://3dlook.ai/content-hub/occupational-health-screening-software/` | S10 | **GAP.** Went live before the July 27 refresh and was still omitted. |
| sideways | Insurance Underwriting · Wellness Rewards Verification | S12 | Already present, keep. |
| down | `https://3dlook.ai/for-bmi-verification/` | S6, S12 | Already the demo CTA, keep. |
| down | five P1 landing anchors (pre-auth documentation S3/S9 · GLP-1 bridge S4/S5 · post-op progress S8 · patient records S5/S8/S9 · hybrid care S6) | as marked | **New structure.** Leave the anchor phrases; the links go in when each child ships. |
| trust | `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` | **inside the accuracy paragraph in S7 and the repeatability paragraph in S8** | **GAP.** The live page never links it despite discussing structured and timestamped measurement data. |
| trust | Data, Privacy, Security and Regulatory FAQ | S10 | **Plain text, never a link.** Still unpublished. The live page already does this correctly. |
| product | `https://3dlook.ai/technology/` | S7 | Already present, keep. |

Target 8 to 11 curated internal links in the body, descriptive anchors only.

---

## Writer notes that are cheaper to read here than to fix later

1. **Nothing on the live page is safe to paste.** The live text uses em dashes throughout, and em
   dashes are a hard fail at every gate with no exceptions. `KEEP` means the argument survives, not
   the sentence. The one exception is the disclaimer block, which is already clean.
2. **Accuracy formulations are copied verbatim from
   `brand-assets/product-info/accuracy-formulations.md`, never reassembled from
   `proof-points.md`.** Format is `96-97%` and `1.5-2.0 cm` with hyphens, and repeatability is
   written `< 1 cm`. `95%+ overall repeatability consistency` is internal and does not publish.
3. **The ISO 8559 benchmark (0.40 cm) is not used anywhere on this page.** Two benchmarks in one
   paragraph is a lint failure, the page needs the internal figures in two different sections, and
   the ISO figure adds nothing to a bariatric documentation argument. This is a deliberate omission,
   recorded in `plan-audit.md` §C.
4. **DXA, not DEXA.** `DEXA` is only legitimate where it is the search term, written
   `DXA (also written DEXA)`. Expand `DXA` as dual-energy X-ray absorptiometry at first use, and
   `BIA` as bioelectrical impedance analysis, and `GLP-1` as glucagon-like peptide-1, and `HIPAA`,
   `GDPR`, `API`, `SDK`, `BMR`. **Do not expand BMI, US, EU, UK, CEO, AI.**
5. **Height is 150 to 220 cm.** The 150-205 figure is superseded and the lint fails it.
6. **Body composition estimates**, never "body composition values". No `predicted weight`.
7. Banned as connectors and constructions: `plus`, `so` introducing a benefit, `let`, `by hand`,
   `this article` outside the scope note, `objective` about our own output, `positioned as` outside
   the medical-device sentence, presumed audience reaction, behaviour attributed to concepts,
   corrective `X, not Y` outside a real boundary, corrective `rather than`.
8. **No named bariatric customer story exists.** Every piece of evidence on this page is a
   third-party citation or an approved internal claim. Do not invent, imply or anonymize a customer.
9. **Guardrail #2, and this page is unusually exposed to it.** Four volume figures, four percentage
   changes and two study cohorts are in play. Every number must be byte-identical in the body, the
   table and the FAQ, and every cohort figure must carry its cohort scope every single time.
10. `slug` in any downstream artifact is `bariatric-pre-qualification-mobile-3d-body-scanning`, the
    published slug. `bariatric-hub-refresh` is the workspace directory name and has bitten this
    pipeline before.
