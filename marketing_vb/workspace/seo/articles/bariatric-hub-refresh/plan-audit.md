---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
plan: plan.md
role: checkpoint-1 reviewer package and planning rationale
audience: Vadim, external reviewer, seo-publisher
created: 2026-09-03
status: awaiting_vadim
---

# Bariatrics hub refresh — checkpoint-1 package and planning rationale

`plan.md` is what a writer needs. This file is why the plan is what it is. Nothing here is required
to write a section.

**Inputs, in order of authority.** The gap analysis
(`refresh-gap-analysis.md`) wins over the context pack
(`workspace/seo/_context-packs/2026-09-03-bariatric-hub-refresh.yaml`) on any conflict; the live
baseline (`published-live-2026-07-27.md`) is the text of record. Conflicts actually encountered are
in §B.

---

## §A. Checkpoint-1 summary for the external reviewer

| Field | Value |
|---|---|
| Page | `https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` — **refresh in place, slug unchanged** |
| Hub / cluster | Hub 6 — Bariatrics → Main hub. This page is the hub. |
| Action type | `Refresh / expand existing`. Phase 0 gate overridden by Vadim's direct request, 2026-09-03. Precedent: `glp-1-market` 2026-08-28, `online-pharmacy-bmi-verification` 2026-08-24. |
| Intent | Hub, BOFU-weighted |
| Priority | P0, September 2026 |
| Cannibalization guardrail | *"Keep bariatrics tied to obesity-care intake, pre-auth, pre-qualification, and patient progress. Do not duplicate GLP-1 or telehealth generic pages."* |
| Vertical boundary | Owns pre-qualification, pre-auth documentation, obesity-care intake, post-op progress, patient records. Does **not** own clinical care: no eligibility determination, diagnosis, procedure selection, clinical outcomes of surgery, clearance, or replacement of clinician review or protocol-defined reference methods. |
| Primary keyword | `bariatric pre-qualification` — **no measured US volume.** See §K. |
| Recommended H1 | *Bariatric Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams* |
| Structure | 12 sections, `content-strategy-guidelines.md` §12, scope note before Section 1 (sensitive vertical) |
| Target | 4,400 prose words (live: ~4,100). Range for a Type A use-case deep-dive is 3,500 to 4,200; the brief sets 4,000 to 4,500. |
| Open decision | **D-1**, the *"About bariatric surgery"* FAQ block. §D-1 below. This is the only item that blocks. |

**The three things a structural reviewer can most usefully overturn here, cheaply:**
1. The keyword decision in §K, which is a strategic call, not a mechanical one.
2. D-1, which changes the FAQ composition and about 180 words.
3. Whether Sections 3, 4 and 5 should be three "why now" sections or two. They are three because the
   documented-BMI-history argument (S5) is the sharpest new operational point on the page and it
   dies as a paragraph inside a GLP-1 section.

---

## §B. Where the inputs disagreed, and what won

| Conflict | Resolution |
|---|---|
| Pack `content_strategy.recommendation`: *"Expand with pre-auth, patient progress, GLP-1 bridge, and post-op tracking."* | **Not followed literally.** The July 27 live version already has H2s for all four. The row was seeded from the Backlink Analysis Report against the **June 5** version. Taking it literally re-does shipped work. The refresh case rests on staleness and two substantiation defects instead. Gap analysis §1 wins. |
| Pack `icp_context.pain_points` carries "Pre-operative dropout is high" with the 50-60% figure still visible | Pack's own `SUPERSEDED_BY_GAP_ANALYSIS` block forbids reuse. Restated as a range in S1. |
| Pack `external_citations.verified_current_keep` lists the JAMA Network Open 8.7% claim as on-page | Superseded by JAMA Surgery 13 May 2026. `CUT`. |
| Pack lists the KFF employer-coverage figure as "on live page; keep" | **Overruled on cannibalization grounds, not on accuracy grounds.** The figure is correct. Hub 3 (`glp-1-market`) owns GLP-1 market and coverage stats and already publishes that exact row in its market-indicator table. The pack's own sideways-link note says "link, but do not re-explain GLP-1 market growth stats." `CUT` and replaced with a link. Reversible if Vadim wants the coverage backdrop retained. |
| Pack `published_inventory.inventory_discrepancy` says `published-articles-inventory.md` is behind the live page | **Already fixed.** The inventory now carries row 11 with both dates and a note that it is a correction added 2026-09-03. No action. |
| Phase 0 step 1a says `already_live: true` → STOP | Overridden by Vadim's direct request. This is a refresh of a live page, which is the whole task. |

---

## §C. Deliberate omissions of our own material

| Item | Why it is not on this page |
|---|---|
| **FX-003, the ISO 8559-1:2017 benchmark (0.40 cm)** | Three reasons, and the first alone is enough. (1) The page needs the internal figures in two different sections (accuracy in S7, repeatability in S8), and the two-benchmarks rule means the ISO figure could not sit next to either. (2) It answers a question this page does not ask: session-to-session repeatability against a 3D-scanner-average reference is a technical-diligence figure, not a documentation-workflow one. (3) Adding it doubles the surface for the one failure `article_lint.py` treats as a hard fail. Recorded here so nobody reads its absence as an oversight. |
| **FX-004, `95%+ overall repeatability consistency`** | Internal only. The live framework article describing the same 2025 study gives no such percentage. The publishable repeatability claim is FX-002. |
| **FX-010, bariatric TAM $10-30M / SAM $2-8M** | Illustrative internal-deck sizing. Not a customer-facing statistic, and publishing our own market sizing on a buyer-facing hub reads as a pitch deck leaked into a blog. |
| **Per-measurement girth figures** (wrist 0.54 cm, waist 2.14 cm and similar) | Technical material. The live framework article publishes only "varying by body part" plus methodology under NDA. |
| **SOC 2** | Not certified yet (in progress per `compliance.md`). Absent entirely; not hedged, not mentioned. |
| **Pricing** | Never in a content-hub article. |

---

## §D. Deletions ledger

Every removal from the live page, with its reason. A reviewer should be able to check this list
against the live text without reading 4,100 words.

| # | What leaves the page | Reason |
|---|---|---|
| 1 | H1 *"Bariatric Pre-Qualification with Mobile 3D Body Scanning: Faster Pre-Auth"* | Leads with the technology. CLAUDE.md §3 moved positioning to outcomes, workflow and governance, and instructs SEO to write about the use case. Also buries progress tracking, which the content-plan title co-headlines. |
| 2 | Meta description opening with the product name | Same defect, one line down. |
| 3 | *"an estimated 33 million US adults meet eligibility criteria, yet fewer than 1% complete surgery in any given year"* and its citation | Citation mismatch. The cited paper is a qualitative attrition study, not an eligibility-prevalence source. No source on file supports a 33 million figure. Replaced by two ASMBS statements that carry their own numbers. |
| 4 | *"pre-operative dropout rates of up to 50-60% are reported across bariatric programs"* (used twice, in live H2 #2 and H2 #9) | Publishes the top of a wide, measurement-dependent range as if it were typical. Guardrails #1 and #4. Restated as the range with its methodology dependence, which is a better argument. |
| 5 | *"bariatric surgery use fell 8.7% between 2022 and 2023"* (JAMA Network Open via StatNews) | Superseded by JAMA Surgery, 13 May 2026. Also secondary trade press where a primary source now exists (terminology guardrails §1.3). |
| 6 | *"Payer review windows commonly run from a few weeks to several months"* | Now wrong for impacted payers on standard requests under CMS-0057-F. Not replaced with a new universal number. |
| 7 | KFF employer-coverage sentence (43% / 28%) | Cannibalization. Hub 3 owns it and already publishes it. Replaced with a link. |
| 8 | Six FAQ questions merged into others (see §F) | The live FAQ asks the same pre-auth question four ways. |
| 9 | *"About bariatric surgery"* FAQ block, six questions | **Blocked on D-1.** |
| 10 | H2 #9 title *"Why mobile body scanning beats manual measurement workflows"* | `beats` is hype-adjacent and the framing is technology-first. Converted to a comparison table with a workflow-fit framing. |
| 11 | H2 #4 title *"What FitXpress captures, and how"* as a standalone section | Merged into S7 with the patient-journey table. The live pair says the same thing at two altitudes. |
| 12 | Every em dash on the page | Hard fail at every gate, no exceptions. |
| 13 | Mid-body eBook promo block (*"The Digital Health Revolution"*) | Second CTA in the body, which the style guide forbids. **Open Item #10** — this one is a decision, not a done deal. |

### Claims considered and rejected before drafting

| Claim | Verdict |
|---|---|
| *"Semaglutide lost exclusivity in March 2026, prices to fall 30-50%"* | **Do not use.** The 2026 expiries are China, India, Canada, Brazil and 100+ other countries. **Not the US**, where protection runs into the early 2030s. This page's audience is US bariatric programs, so the claim would be materially misleading in frame. Admissible only as an explicitly ex-US note, and only if the hub deliberately broadens beyond the US. |
| *"Volume peaked at 230,207 in 2022 and dropped to 177,297 in 2024"* | **Do not publish.** Secondary trade-press report; the primary source returned HTTP 403 and is unverified. A third, unreconciled volume series on a page that already has two. |
| *"Surgery appears to be rebounding as GLP-1 patients turn to one-time procedures"* | **Needs a primary citation before use.** Currently only in ASMBS press-summary language, and directionally opposite to the live page's closing read. Open Item #7. |
| A named bariatric customer story | **None exists.** No bariatric case study in `case-studies/` or `proof-points.md`, unlike insurance, wellness and telehealth. Do not fabricate, imply or anonymize one. Open Item #4. |

---

## §E. Keep ledger — what survives, and why it is worth protecting

Gap analysis §8 item 9. These are the parts of the live page that already work, and a rewrite is the
most common way to lose them by accident.

| Kept | Where it lands |
|---|---|
| The four-stage pre-qualification workflow, stages 1 to 4 | S6, structure intact |
| The mechanism paragraph (*"the scan does not determine whether a patient is medically eligible… what the scan supplies is a structured, verifiable body-data signal the program uses to triage"*) | S6. The single most important sentence on the page. Do not soften, do not compress. |
| The patient-journey table (Inquiry → Long-term monitoring) | S7, unchanged in content |
| The scope note and italic disclaimer, **verbatim** | Front matter. Also the framing the five child articles reuse. |
| The compliance-posture paragraph | S10, expanded with FX-005 and FX-006 |
| The three properties that matter (timestamped structured outputs, remote capture, compliance posture) | S7 |
| The anti-manipulation paragraph, with its existing hedging | S9, with the guardrail-#5 limit stated in the same breath |
| Privacy and regulatory detail as **plain text, not a link** | S10. The live page does this correctly because the central FAQ is unpublished. |
| The operational-not-clinical framing throughout | Every section, and S9 states it as its own block |
| CDC 40.3% / 9.4% prevalence; CDC self-report 40% underestimate; ASMBS >270,000 in 2023; ACS Bulletin Funk and Kurian quotes; Johns Hopkins one-in-seven | S1, S4, S8 |

---

## §F. FAQ mapping, live 20 → planned 13

| Live question | Action |
|---|---|
| How can bariatric clinics pre-qualify patients remotely? | KEEP → Q2 |
| What is bariatric pre-qualification? | KEEP → Q1 |
| How can body measurements support bariatric surgery pre-authorization? | ABSORBED into Q3 |
| How can clinics reduce wasted bariatric consult slots? | KEEP → Q6 |
| How can mobile body scanning support bariatric intake workflows? | ABSORBED into Q2 |
| Can FitXpress help with bariatric pre-auth documentation? | ABSORBED into Q3 |
| Can FitXpress replace in-clinic measurements? | ABSORBED into Q13 |
| How does FitXpress support early bariatric patient screening? | ABSORBED into Q2 |
| How can patients track progress after bariatric surgery? | REWRITE → Q10, reframed from patient-facing to program workflow |
| Why is weight alone not enough for bariatric surgery progress tracking? | KEEP → Q8 |
| What body measurements matter after bariatric surgery? | REWRITE → Q7, as the progress-record question |
| Why is body composition tracking useful after bariatric surgery? | ABSORBED into Q8 |
| How can visual progress tracking support bariatric patients? | ABSORBED into S8 prose |
| How can bariatric programs monitor patients remotely after surgery? | KEEP → Q9 |
| What is bariatric surgery? | **D-1**, returns only under Branch B |
| What are the main types of bariatric surgery? | **D-1**, returns only under Branch B |
| What are common bariatric surgery requirements? | **D-1**. Under Branch A its documentation half is answered by Q3. |
| What are the benefits of bariatric surgery? | **CUT under both branches.** Clinical-outcome claim. |
| What are the side effects of bariatric surgery? | **CUT under both branches.** Clinical-outcome claim. |
| What are the pros and cons of weight loss surgery? | **CUT under both branches.** Clinical-outcome claim. |
| — | NEW: Q4 payer decision clock · Q5 documented BMI history · Q11 decisioning · Q12 who reviews · Q13 what it does not do |

Live 20 → planned 13 (Branch A) or 16 (Branch B). Guidelines §14 asks for FAQs that answer real
search and procurement questions, 2 to 5 sentences each; the live page's 20 include four ways of
asking the same pre-auth question.

---

## §D-1. The decision for Vadim

**The live page ends its FAQ with a block titled *"About bariatric surgery"*: what is bariatric
surgery · main types · common requirements · benefits · side effects · pros and cons.** It has to be
cut or kept, and it cannot be half-solved by the pipeline, because the trade-off is a strategy call
about what this vertical is for.

**What is actually true about it.** The six answers are clinical-care answers. The Bariatrics
boundary (guidelines §9) is pre-qualification, pre-auth documentation, obesity-care intake, post-op
progress and patient records. Two of the answers go further than "outside the boundary": the benefits
answer (*"associated with sustained weight loss and improvement in obesity-related conditions such
as type 2 diabetes, hypertension, and obstructive sleep apnea"*) and the side-effects answer are
clinical-outcome claims published by a body-data vendor with no clinical evidence base of its own.

**It is also the only part of the page with measured search demand, and the page's main GEO/AEO
surface.** `bariatric surgery requirements` is 1,100/mo at KD 54 with a traffic potential of 5,000.
`bariatric surgery` is 69,000/mo. Every buyer-side term on this page returns no data at all. The
block is also the part most likely to be lifted verbatim into an LLM answer, because it is the part
shaped like a definitional question.

### Cut it

- Clean boundary. The page owns documentation and intake, and says so consistently.
- No clinical-outcome claims from a body-data vendor, which is the actual claims exposure here, not
  a theoretical one.
- Removes the one place the page already drifts patient-facing, which is the drift Open Item #1
  warns about.
- **Cost:** loses the only real search volume in the vertical, and shrinks the page's most
  LLM-liftable surface. Any traffic the page currently gets probably comes from here.

### Keep it

- Keeps the volume and the GEO surface, on a page that otherwise has neither.
- Answers questions a real intake coordinator is asked daily, so it is not useless to the B2B reader
  either.
- **Cost:** the page owns clinical-care content and clinical-outcome claims it has no evidence base
  for, in a sensitive vertical, on a hub whose entire credibility argument is "we stay on the
  operational side of the line." Every child article inherits the precedent, and the next reviewer
  who reads the boundary against the FAQ finds the contradiction.

### Recommendation

**Cut the block as it stands, then re-add exactly three of its six questions in rewritten form.**
This is Branch B in `plan.md` §Section 11, and it is not a fudge: it separates the two things the
block is doing.

- **Returns**, rewritten: *what is bariatric surgery* (definitional, procedures named, no outcome
  claim), *what are the main types* (with the sleeve-gastrectomy share cited to the ASMBS Fact
  Sheet), *what are common program and payer requirements* (reframed as documentation and criteria
  set by the program and the payer). The third of these is a documentation question wearing a
  patient-facing title, and it is where the 1,100/mo actually lives.
- **Does not return, under either branch:** benefits, side effects, pros and cons. These are the
  clinical-outcome claims. If Vadim wants them anyway, they need sentence-by-sentence attribution to
  a named clinical body and an explicit "not medical advice" line, and even then guidelines §9 says
  this vertical does not own clinical care. That is a separate decision, not this one.

Cost of the recommendation: keeps roughly the definitional and requirements share of the block's
demand, drops the outcome-shaped share, and adds 180 words. Both branches are fully planned, so
either answer proceeds straight to `write` with no re-plan.

---

## §K. The keyword decision, and the cost of the alternatives

Ahrefs API v3, keywords-explorer, `country=us`, pulled 2026-09-03. Seven seeds. Files in
`workspace/seo/_keywords/`.

| Phrase | Volume | KD | TP | Note |
|---|---|---|---|---|
| `bariatric pre-qualification` | **no data** | — | — | The current H1's own term. No idea list returned either. |
| `bariatric patient progress` | **no data** | — | — | `bariatric patient` 500 / KD 39 / TP 10. Idea list is bariatric **equipment** (patient lift, bed, chair, transport). |
| `bariatric pre authorization` | **no data** | — | — | `pre authorization` alone 1,800 / KD 37, but its idea list is insurance and credit-card senses. |
| `bariatric intake` | **no data** | — | — | Entire idea list is post-op **nutrition** intake (protein, calorie, water). A different sense of the word. |
| `body composition after bariatric surgery` | **no data** | — | — | `after bariatric surgery` 450 / KD 16 (parent: long-term diet after gastric sleeve). `body composition` 32,000 / KD 32, owned by Hub 1 / Hub 3. |
| `obesity care` | **80** | 53 | 80 | Parent topic is **"obesity week"**, a conference. Thin and wrong-intent despite having a number. Half of the content plan's proposed title. |
| `bariatric surgery requirements` | **1,100** | 54 | 5,000 | Informational, **patient-facing**: insurer coverage, BMI thresholds. |
| `bariatric surgery` | **69,000** | 50 | — | Patient-facing head term. |

**`null` is not `0`.** Five seeds returned no measurement for the exact phrase. That is different
from a measured zero, and it is different again from `obesity care` at 80, which is measured, thin
and pointed at a conference.

### The mechanical rule, and why it is refused here

Phase 1 says: when `seed_has_data` is false, take a head term from the variants that does have
volume, make it primary, keep the original as the angle. That rule exists because of
`remote-body-measurement-online-fitness-coaching` (2026-08-25), which shipped on a zero-data primary
keyword and nobody noticed until afterwards.

Applied here, the rule produces `bariatric surgery requirements` or `bariatric surgery`. **Both are
patient-facing.** Adopting either as the primary keyword does not change the page's keyword; it
changes the page's **audience**, from a few hundred US bariatric programs to prospective patients.
That is a guidelines §9 boundary violation, it duplicates nothing we own and competes with
patient-education publishers at KD 50 to 54, and it is exactly the drift the live *"About bariatric
surgery"* FAQ block already represents.

### What is actually true about demand here

Buyer-side terms have no measured volume because the buying committee is small and does not search
in vendor language. A few hundred US bariatric programs, whose directors of operations and pre-auth
coordinators search for payer policy documents and CMS rules, not for "bariatric pre-qualification
software." No keyword tool measures the LLM-answer surface, which is where a procurement-shaped
question ("what body data do payers require in a bariatric pre-auth packet") actually gets asked in
2026.

**So the honest statement, and it belongs in front of Vadim now:** this page is a BOFU / GEO /
sales-enablement asset and a hub for five P1 children to link up to. It is not an organic-volume
play, and it should not be measured as one. If the success metric for this refresh is organic
sessions, the refresh is the wrong investment and Vadim should know that at checkpoint 1, not from
Search Console in six months.

### The three options, priced

| Option | What it costs |
|---|---|
| **Chosen: keep `bariatric pre-qualification` as primary, accept zero measured volume** | No organic-volume upside. The page is judged on GEO capture, sales use and hub structure. Keeps the boundary, the URL, the slug and the audience. |
| Swap to `bariatric surgery requirements` (1,100/mo) | Boundary violation, audience change, clinical-outcome claims re-enter, competes with patient-education publishers at KD 54, and every child article inherits a patient-facing hub. Rejected. |
| Split: keep this page B2B, create a separate patient-facing page for the 1,100/mo | Not this run's decision, and it needs its own strategy row. Worth Vadim's consideration as a **new** content-plan row, since the demand is real and currently unserved. **Not** a second bariatric hub. |

---

## §L. Coverage map, live 9 H2s → planned 12 sections

| Live section | Words (approx) | Fate |
|---|---|---|
| H1 + intro + disclaimer | 250 | REWRITE → Front matter. Disclaimer verbatim. |
| #1 Why bariatric programs need faster pre-qualification | 350 | REWRITE, merged → S1 |
| #2 The intake gap: when eligibility gets confirmed too late | 400 | REWRITE, merged → S1 |
| (eBook promo block) | — | Open Item #10 |
| #3 The GLP-1 shift: volume contracted, intake complexity rose | 600 | REWRITE → S4. Every number changes. |
| #4 What FitXpress captures, and how | 400 | REWRITE, merged → S7 |
| #5 Pre-qualification: structured body data before the consult | 700 | KEEP → S6 (Use Case Summary block moves to front matter) |
| #6 Pre-auth documentation: cleaner packets, fewer delays | 600 | SPLIT: the payer-clock argument is replaced by S3 (NEW); the packet list moves to S3; the documentation mechanics move to S9 |
| #7 Post-procedure: turning the baseline into longitudinal tracking | 300 | REWRITE and expand → S8, 400 words, promoted to a co-equal spine |
| #8 Where FitXpress fits in the bariatric patient journey | 200 | REWRITE, merged → S7. Table kept. |
| #9 Why mobile body scanning beats manual measurement workflows | 400 | REWRITE → S10 as a comparison table, retitled |
| #10 FAQ, 20 questions in 3 blocks | ~1,100 | REWRITE → S11, 13 questions in 3 blocks (16 in 4 under Branch B) |
| CTA + Related reading (2 links) | 100 | REWRITE → S12, 7 related links |
| — | — | NEW: S2 short answer · S3 CMS-0057-F · S5 documented BMI history |

**Net:** 3 sections merged away, 3 new sections added, 1 section split, 1 promoted, 7 FAQ questions
removed. Word count roughly flat at 4,400 against ~4,100. The nine changes the brief requires all
land: retitle (§D row 1, `plan.md` Recommended Title) · CMS-0057-F (S3) · GLP-1 rebuilt on 2026 data
(S4) · documented BMI history (S5) · both substantiation defects (S1, §D rows 3 and 4) · progress
tracking promoted (S8) · the FAQ block (D-1, both branches planned) · internal links in four
directions plus five down-link landing anchors (`plan.md` link table) · the keep ledger (§E).

---

## §M. Open items

**#1 — The primary keyword has no measured US demand, and neither does anything else on the buyer
side.** Full analysis in §K. The page is planned as a BOFU / GEO / sales-enablement hub, not an
organic-volume play. Adopting the reasoning means accepting that organic sessions are the wrong
success metric for this refresh. Arguing against it means changing the page's audience, which the
vertical boundary forbids. **Either way, Vadim has to see this now.** Same failure class as
`remote-body-measurement-online-fitness-coaching`, 2026-08-25.

**#2 — D-1, the *"About bariatric surgery"* FAQ block.** §D-1. The only item that blocks `write`;
both branches are planned so neither answer forces a re-plan.

**#3 — `audience.md` has no Bariatrics segment layer.** Its seven FitXpress health segments are
Telehealth/GLP-1, UK BMI Verification, Connected Fitness, Wellness Rewards, Insurance Underwriting,
BCRL/Oncology and Plastic Surgery. The buyer, pain and "what NOT to say" data used in this plan was
reconstructed from `icp-detail.md` §5 (a file that itself marks that section as *"not covered by the
new ICP doc, carried over from the previous version"*), plus `about-me.md` hard rules, plus the live
page's own scope note. **A canonical Bariatrics layer is missing** and this hub plus five P1 children
will keep reconstructing it. Not a gate on this refresh.

**#4 — No named bariatric customer story exists.** All evidence on this page is third-party citation
or an approved internal claim. Insurance, wellness and telehealth all have a case study; this hub
does not, and it reads thinner for it. Is there a bariatric pilot that can be referenced, even
anonymized (*"a US multi-site bariatric network"*)? If not, the plan stands as written.

**#5 — No FitXpress bariatric vertical page.** The down-link goes to `/for-bmi-verification/`, which
is a BMI-verification page of roughly 659 words with no FAQ and no cases, and is CLAUDE.md §16's
first rewrite candidate. CLAUDE.md §16 lists only BMI verification, telehealth and connected fitness
as existing verticals. An open item for `page-builder`, not a gate here. Note that a bariatric
vertical page would not clear G-I today: it needs two publishable cases from the vertical and there
are zero (see #4).

**#6 — The Data, Privacy, Security and Regulatory FAQ is still unpublished.** The only remaining P0
hub gap (draft at `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/`). S10's
compliance detail stays **plain text with no link**, which is what the live page already does
correctly. When it ships, S10 gets the trust link and this hub should be revisited.

**#7 — *"Surgery appears to be rebounding"* has no primary citation.** Currently only in ASMBS
press-summary language, and directionally opposite to the live page's closing read. Excluded. If a
primary source is found before `write`, it belongs in S4's closing paragraph and it changes the
section's conclusion.

**#8 — FX-005's characterized weight range tops out at 210 kg.** A severe-obesity intake population
includes patients above that, and this is the one vertical where the validation-population ceiling is
operationally relevant rather than a formality. S10 states it plainly, which is the honest move.
Worth confirming with product whether any newer characterization exists before `write`.

**#9 — Lint blind spot: the pack's `internal_link_targets` sits at the top level, not under
`content_strategy`.** `article_lint.py` gate 6 reads
`pack["content_strategy"]["internal_link_targets"]`, so the four-direction link check will silently
skip at the article stage and report nothing. The writer and editor must verify the four directions
against `plan.md`'s link table manually, or the pack shape gets normalised.

**#10 — The mid-body eBook promo block.** The live page carries a *"The Digital Health Revolution"*
eBook block with its own download CTA after live Section 2. `blog-style-guide.md` §5 allows one CTA
per article and forbids banner-style mid-body promos. Cut it, or keep it as a deliberate exception?
Default in the plan is to flag rather than delete.

**#11 — Inventory.** `published-articles-inventory.md` row 11 was corrected on 2026-09-03 and now
carries both dates. Closed, no action. Row 11 will need its `updated` date changed again when this
refresh republishes.

---

## §N. What the article deliberately does not cover

For the external reviewer: this list is as much of the plan as the outline is. A hub that covers
everything adjacent is how a vertical boundary dies.

**Outside the vertical boundary (guidelines §9):**
- Clinical outcomes of bariatric surgery: benefits, disease remission, side effects, complication
  rates, revisional surgery, mortality.
- Whether a given patient qualifies. No qualifying BMI stated as guidance, no payer threshold
  published, no procedure recommended or compared clinically.
- Procedure selection, surgical risk assessment, anesthesia risk, psychological readiness criteria.
- Post-operative clinical care: diet, vitamins, protein targets, exercise programming, hair loss,
  pregnancy. This is the patient-facing content that dominates the keyword idea lists, and it is the
  single easiest way for this page to drift.

**Owned by a neighbouring hub, linked instead:**
- GLP-1 market sizing, employer coverage economics, drug pricing, drug-class comparison → GLP-1
  Market hub.
- Remote-prescribing compliance and BMI-verification methodology → Online Pharmacy BMI Verification.
- General telehealth workflow, privacy and patient experience → AI in Telehealth hub.
- Body-composition method comparison, DXA and bioelectrical impedance analysis trade-offs, accuracy
  framing in depth → the accuracy framework and the DXA comparison article.
- Multi-site screening consistency as a general argument → Occupational Health hub.
- Anthropometric standardization for trials → Clinical Trials hub.

**Excluded on evidence grounds:** semaglutide ex-US exclusivity; the unverified 230,207 / 177,297
volume series; "surgery is rebounding"; any named customer story; SOC 2; the ISO 8559 benchmark;
per-measurement girth figures; our own market sizing; pricing.

**Excluded on claims grounds:** any statement that the scan determines eligibility, makes or
accelerates the payer's decision, diagnoses, replaces clinical evaluation, guarantees compliance or
an approval, or detects manipulation automatically.
