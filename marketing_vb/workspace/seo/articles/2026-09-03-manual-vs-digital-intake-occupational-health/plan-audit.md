---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
plan: plan.md
review_package: checkpoint-1-review-package.md
stage: plan
created: 2026-09-03
audience: seo-publisher, Vadim, external reviewer
---

# Plan audit — why the plan is what it is

Everything here explains a decision. Nothing here is needed to write a section. `plan.md` is the
writing document; this file is the record.

---

## 1. The keyword decision, and what each alternative would have cost

### The finding first

`seed_has_data: false`. Vadim's topic phrase and every fragment of it carry no measured demand.
`manual intake` on its own is volume **0**, which is a measured absence of demand, a different fact
from the `null` on the other fragments, which is an absence of measurement. Three seed pulls were
merged (topic seed, digital-intake space, occupational-health head space) for 2,366 Ahrefs units, so
the candidate spaces are all on the table and none of this is guesswork about coverage.

**The conclusion the plan states in one line: there is no measured, in-vertical, un-owned head term
available to this article.** Every candidate is owned by the live hub, reserved for a sibling row,
off-vertical, or unmeasured. The plan therefore treats the page as a GEO / answer-engine and
long-tail procurement-question play, and says so where a reader of checkpoint 1 will see it.

### Priced alternatives

| Option | Real metrics | What it would gain | What it would cost |
|---|---|---|---|
| `occupational health screening` | 250 / KD 6 | The only genuine in-vertical volume, and low difficulty | **Off limits.** It is the live hub's own `target_keyword`. Taking it puts a supporting article head-to-head with the P0 hub it is supposed to feed, which is precisely the failure the row's guardrail exists to prevent. |
| `occupational health` | 5,400 / KD 22 | The biggest head term in the space | Hub territory and far too broad. Ranking for it means writing a second general occupational-health overview, which guidelines §2 forbids outright when a hub exists. |
| `intake forms` | 700 / KD 4 | Highest volume of any adjacent measured term | Parent topic is `intake form`. The result set is form builders and practice-management software. Zero occupational-health relevance, wrong buyer, wrong page shape. Ranking would require abandoning the row's angle. |
| `digital patient intake forms` | 200 / KD 3 | Measured, very low difficulty, and genuinely about digital intake | It is **patient** intake at clinics and dental and primary-care practices. Wrong buyer (a patient, not a candidate or an employee), wrong compliance frame (no post-offer boundary, no employer in the picture). To rank we would write for the wrong reader, and the vertical boundary would blur. |
| `digital patient intake` | 150 / KD 4 | Same | Same relevance cost. |
| `patient intake forms` | 150 / KD 6 | Same | Same relevance cost. |
| `pre employment occupational health screening` | 100 / KD 1 | Measured, in-vertical, difficulty 1. On paper the best trade in the whole table. | Breaks two guardrails at once. `content-plan.md:211` gives pre-employment intake to the hub explicitly, and row 219 reserves "Pre-Employment Medical Screening Intake" as a P2 `section first` topic. Annexing it would strand a planned row and cannibalize a live page. |
| `occupational health pre employment screening` | 80 / KD 0 | Same | Same. |
| `occupational health screening services` | 100 / no KD data | In-vertical, commercial | Vendor-shopping intent, not comparison intent. Kept as a secondary weave in Section 10 where evaluation language belongs. |
| `occupational health employee screening tool` | 30 / no KD data | In-vertical, tool-evaluation intent, and not the hub's declared target | Thin at 30 a month, and it sits next to the hub's `occupational health screening software`. Kept as a secondary weave in Section 10, not as the target. |
| `digital occupational health intake` | no data | Names the category the page argues about | It is the hub's **secondary keyword #1**, and two of the hub's H2s carry the phrase verbatim ("How FitXpress supports digital occupational health intake", "What improves with digital occupational health intake?"). Making it the primary would be a self-inflicted cannibalization on the one page whose job is to avoid it. Used as prose in Sections 4 and 6, never as a heading target. |
| **`manual vs digital intake` (chosen)** | **no data / no data** | Names the page's distinct intent exactly. Zero overlap with the hub's target or its six secondaries. Zero overlap with sibling rows. Short enough to sit naturally in the H1, the first paragraph and one H2, which is what the keyword-placement gate checks. Carries the "vs" that answer engines match comparison queries on. | No measured classical-search upside. The entire return is answer-engine coverage, long-tail procurement questions, and cluster authority feeding the hub. |

### Why not the full topic phrase as the primary

`manual intake vs digital intake in occupational health screening` is nine words. `article_lint.py`
gate 7 requires the primary keyword as an **exact substring** in the H1, in the first paragraph, and
in at least one H2. A nine-word phrase forced into all three positions is keyword stuffing that a
reviewer would rightly cut, and the gate would then fail. The plan keeps the full phrase as the H1
scope clause and in the FAQ question phrasings, where it reads naturally, and uses the shortened form
as the gated primary.

### The precedent this is written against

2026-08-25, `remote-body-measurement-online-fitness-coaching` went to publish with a primary keyword
carrying zero measured data, and that only surfaced afterwards. The difference here is disclosure,
not luck: the finding is in `plan.md` above the keyword table, in the review package, and in the Open
items below.

---

## 2. Cannibalization working against the live hub

The hub was read in full at `workspace/seo/articles/2026-06-08-occupational-health-screening/v2-asselya/draft-final.md`,
not just summarised from the pack. Fourteen H2s, published 2026-07-10, updated 2026-07-17.

### The five questions, answered (guidelines §5)

1. **Does an existing article already answer this same question?** No. The hub answers "what is
   occupational health screening intake, and how does FitXpress support it". It never asks which
   intake method a program should choose, and it never sets out the conditions under which manual
   intake is the correct answer. That question is unanswered on the site.
2. **Does the title overlap with the hub?** No. The hub's H1 is "Standardizing Occupational Health
   Screening: Faster Intake, Better Documentation, Fewer Rescreens". Ours leads on the method
   comparison and does not contain the hub's target keyword as a phrase.
3. **Broad enough for a hub, or should it be a section?** It is a supporting article, and
   `content-plan.md:212` already classifies it that way. Guidelines §2 names this exact title as its
   own example of a legitimate supporting article. The comparison table and the decision framework
   together are too large for a hub section without unbalancing a hub that is already ~4,500 words.
4. **Does the recommendation say refresh, section first, or do not duplicate?** No. The row says
   "Net-new supporting", and the Hub-8 preamble at `content-plan.md:207` lifts the publish-the-hub-
   first block.
5. **What exact search intent should this page own?** "Should we move occupational health intake from
   paper and tape to a digital channel, how do the two actually differ, and which fits our program?"

### What stays the hub's, H2 by H2

| Hub H2 | Stays the hub's | How this article avoids it |
|---|---|---|
| The problem: screening still slowed by manual intake | Yes | Section 1 states the problem in two sentences and links up. It does not re-run the three-failure-mode analysis. |
| Why this matters now | Yes, including its **BLS 2024 SOII figure** (2.5 million nonfatal injuries, 2.3 per 100 FTE) | Section 3 uses a different BLS release, JOLTS July 2026, and a different driver (hiring volume, not injury volume). |
| What is occupational health screening intake? | **Yes, the category definition and its ACOEM citation** | Section 2 defines the two *methods*, not the category. ACOEM is not cited here at all. |
| How FitXpress supports digital occupational health intake | Yes | Section 6 is deliberately short and scoped to one intake component. |
| Standardizing pre-employment screening before the appointment | **Yes, including its fuller EEOC passage** | Section 9 uses EEOC for one sentence on the post-offer boundary. Row 219 also reserves pre-employment intake as a `section first` topic. |
| Reducing delays in return-to-work and fit-for-duty workflows | **Yes, and rows 213 and 214 reserve the rest** | Return-to-work appears nowhere as an argument. One clause in Section 10 and a link up. |
| Pre-employment vs return-to-work screening | Yes, including its four-row workflow table | Our Section 5 table compares **methods** across dimensions, not workflows against each other. Different axis, different table. |
| Better documentation across sites and vendors | **Yes, including its OSHA 29 CFR 1904 recordkeeping citation** | Section 4 and 5 use OSHA **1910.134 Appendix C** instead, which is a different standard about a different thing: how the questionnaire must be administered and routed. |
| What improves with digital occupational health intake? | Yes, its six-outcome list | Section 7 covers outcomes in three hedged clauses and spends its length on the evidence and its conditions, which the hub does not have. |
| Who uses FitXpress for occupational health screening? | **Yes, the four-buyer roster** | Section 10 names which buyer the switch pays back fastest for, then links up for the roster. It does not rebuild it. |
| More than body scanning: workflow rules, QA, reporting, scale | Yes | Not covered. |
| What FitXpress does and does not do | Shares the boundary, which every article in this vertical must state | Section 8 is shorter and pointed at the comparison. The boundary is a compliance requirement, so restating it is intentional and approved (see the clinical-trials article's `known_issues`: a repeated scope disclaimer that fits its section is not a defect). |
| How digital occupational health intake works with FitXpress | **Yes, the five-step sequence** | Not covered. Section 6 explicitly does not rebuild it. |
| Frequently asked questions | Yes, all seven | Checked question by question in §4 below. |

### The genuine open ground

**The hub never states an accuracy or a repeatability figure.** FX-001, FX-002 and FX-003 are unspent
across all fourteen H2s. That is the largest piece of unclaimed ground in the vertical, and it is
also the substantively right thing for a *comparison* article to own, because the manual-vs-digital
question is a question about measurement consistency. Section 7 takes it, with FX-003 as the primary
figure and FX-001 carrying its reference.

The second piece of open ground is the decomposition of intake into components (Section 4). The hub
treats intake as one thing. Splitting it into four parts and marking which two a remote channel can
carry is what makes an honest comparison possible at all, and it is the reason Section 9 can
recommend a hybrid without hedging.

### The correction this working produced

The most tempting framing for this article is "digital intake is more accurate than a tape measure".
It is not available to us. FX-001 is measured **against expert pattern-maker manual measurement as
the reference**, so expert manual measurement is the yardstick, not the competitor. The plan carries
this as a hard boundary on Sections 5, 7 and FAQ Q1. Without it, this article would have shipped an
overclaim that our own canonical accuracy language contradicts.

---

## 3. Why the 12-part structure was reordered

`content-strategy-guidelines.md` §12 puts the comparison table at position 8, after the
what-FitXpress-does-not-do section. The plan puts it at Section 5 and the decision framework at
Section 9.

Reasons:

1. The brief for this run states that for GEO/comparison intent the comparison table and the decision
   framework are the core of the article, not an optional block. A core block at position 8 of 12 is
   not the core.
2. The comparison is **method against method**. It does not depend on FitXpress having been
   introduced, and putting the product first would make the table read as a product-versus-tape
   table, which is the clean sweep guidelines §7 forbids.
3. `blog-style-guide.md` Article Type C, the comparison template, puts the comparison table at
   position 4 and "Where 3DLOOK Fits Best" at position 7. The plan follows Type C's ordering inside
   §12's inventory of sections.

Every §12 item is present. Items 9 (buyer/ICP fit) and 10 (implementation and evaluation) are merged
into Section 10, because for a 2,500-word supporting article under a hub that already carries the
buyer roster, two separate sections would each be too thin to earn its heading.

---

## 4. FAQ non-overlap check

The hub carries seven formal FAQ questions and five bolded inline mini-Q&As. All twelve were checked
against the six planned questions.

| Planned question | Closest hub question | Verdict |
|---|---|---|
| Is digital intake more accurate than manual tape measurement? | none | **Clear.** The hub never discusses accuracy or repeatability at all. |
| Which parts of intake cannot move to a digital channel? | "Can body measurement software replace an occupational health exam?" | **Clear.** The hub's answers one question (no, it cannot replace the exam). Ours enumerates which of the four intake components stay manual, which is a different answer. |
| What happens if a candidate cannot complete a remote scan? | none | **Clear.** Access and fallback appear nowhere in the hub. |
| Does a digital channel change the post-offer boundary? | "What data is usually collected during pre-employment screening?" | **Clear.** The hub's answer lists data types and mentions EEOC in passing. Ours answers whether the channel affects the boundary, which is the compliance-buyer question. |
| Can digital records be compared against earlier manual measurements? | inline "How can occupational health clinics standardize body measurements across sites?" | **Clear.** The hub's inline answers how to standardise going forward. Ours answers whether a mixed-method historical series is comparable, and says it is weaker. |
| What should a program measure to know whether it worked? | inline "What causes rescreens…?" and "How does digital intake improve throughput?" | **Adjacent, and worth a reviewer's eye.** The hub says what improves; ours says what to instrument. The distinction is real but it is the thinnest of the six. Flagged in Open items. |

---

## 5. Deletions ledger

Things considered for the plan and deliberately left out.

| Cut | Why |
|---|---|
| `FX-004`, "95%+ overall repeatability consistency" | Marked `publishable: false` in the pack. The live framework article describes the same 2025 study and gives no such percentage. It has no published home. FX-003 covers the same ground in approved words. |
| The ISO 8559 session-to-session figure | Not in the article at all. It uses a different reference from the internal figures, and combining them in a paragraph is a linter failure and a misrepresentation of both. Keeping it out entirely removes the chance of a writer reaching for it in the comparison section. |
| Per-measurement accuracy figures | Technical material, not a hub or a supporting comparison. "Varying by body part" plus methodology under NDA is the published level of detail. |
| Two of the fat-classification outputs listed in FX-009's pack text | Both were cut from wellness copy on 2026-09-02 and are flagged by the linter. `plan.md` quotes only the subset that remains publishable. |
| The hub's BLS 2024 injuries figure | Reusable, but re-citing the same statistic in a supporting article under the same hub is the "plagiarism costume party" guidelines §6 warns about. JOLTS July 2026 is a different release, a different driver, and on-angle for an intake-volume argument. |
| ACOEM fitness-for-duty guidance | The hub owns it, and it is a clinical-review citation. This page is about intake method selection. Linking up covers it. |
| OSHA 29 CFR 1904 recordkeeping | The hub owns it. 1910.134 Appendix C is the fresher and more on-angle OSHA source for a comparison about *how intake documents are administered*. |
| `/for-bmi-verification/` as a down-link | The hub already routes there, and putting a BMI-verification product page next to employment-screening copy invites the BMI-based-employment reading the vertical boundary forbids. Down-links go to the FX parent and the demo modal instead. |
| A pre-injury baseline argument | Belongs to rows 213 and 214. The hub already makes it. |
| The `1.0-1.5 cm` and `0.4-0.8 cm` ranges from `body-scanning-technology-comparison.md` | Category ranges from a different article, not our approved claims. That article also uses reserved words about evidence. Read it for shape, not for figures. |
| A comparison against any named vendor | `competitors.md` has no vendor in occupational-health intake, and named-competitor comparisons are banned regardless. |

---

## 6. Source quality notes (terminology guardrails Part 1, rule 3)

All four external sources are regulators or national statistics offices. No vendor blogs, no
adjacent-vendor content, no trade press.

| Source | Class | Verification status |
|---|---|---|
| Appendix C to § 1910.134, *OSHA Respirator Medical Evaluation Questionnaire (Mandatory)* — `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134AppC` | Regulator, primary text | **Fetched and verified 2026-09-03.** Confirmed on the page: the employer or supervisor "must not look at or review your answers"; the employer must inform the employee how to deliver the questionnaire to the reviewing health care professional; the employer "must allow you to answer this questionnaire during normal working hours, or at a time and place that is convenient to you"; and answers to Section 1 and to question 9 of Section 2 part A "do not require a medical examination". |
| BLS *Job Openings and Labor Turnover Summary*, July 2026 — `https://www.bls.gov/news.release/jolts.nr0.htm` | National statistics office | **Fetched and verified 2026-09-03.** Exact sentence: "The number and rate of hires were little changed at 5.1 million and 3.2 percent, respectively, over the month." |
| CDC / NCHS *NHANES Anthropometry Procedures Manual*, 2021 — `https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf` | National health statistics agency, protocol document | **URL confirmed live** (5.5 MB PDF). The specific passages were **not machine-readable at plan stage**, so `plan.md` instructs the writer to open the PDF and quote the protocol text directly. Do not write this passage from a paraphrase. If the 2021 manual turns out not to carry the needed protocol detail, the 2020 and 2013 manuals are at the same path pattern and are acceptable substitutes. |
| EEOC enforcement guidance on pre-employment disability-related questions and medical examinations — `https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical` | Regulator | Reused from the hub, which cites it with this URL. Correct authority for the one post-offer sentence in Section 9 and for FAQ Q4. |

---

## 7. Priority conflict, unresolved

`content-plan.md:212` marks this row **P0**. `published-articles-inventory.md:379` lists the same row
in its P1 gap table ("Manual Intake vs Digital Intake | #11 Occupational Health").

`plan.md` uses **P0**, because that is the priority the Orchestrator resolved Phase 0 against and
`content-plan.md` is the offline copy of the strategy spreadsheet, which is the priority system of
record. The plan does not attempt to reconcile the two documents. **This is Vadim's call**, and it
matters beyond this article: three other Hub-8 rows are queued behind it, and if the inventory's P1 is
the right figure then row 213 (Return-to-Work Screening Documentation, P0 in both documents) should
run first.

---

## 8. Open items for Vadim and for Asselya

Per editorial guardrail #11, these are surfaced rather than decided.

1. **The primary keyword has no measured volume, and no alternative does better.** `manual vs digital
   intake` is unmeasured; the only measured in-vertical term is the hub's own. Confirm that a
   GEO / answer-engine play with effectively zero classical-search upside is the intended trade for a
   P0 slot, or redirect the row. §1 above prices every alternative. **This is the first thing to look
   at on checkpoint 1.**
2. **P0 versus P1.** `content-plan.md` and `published-articles-inventory.md` disagree on this row's
   priority. §7. Whichever is right, one of the two documents needs an edit.
3. **The Privacy/Regulatory FAQ is still unpublished**, and it is one of two trust assets guidelines
   §11 permits this vertical to link sideways to. The plan carries it as a placeholder anchor in
   Section 6. The publisher either resolves the URL or drops the anchor. It has been the remaining P0
   gap for some time; a second article now depends on it.
4. **No sibling article exists to link sideways to.** Rows 213 through 220 are all unwritten, so this
   page's sideways links collapse onto the two permitted trust assets. That is compliant, and it is
   also thin. It resolves itself when row 213 ships.
5. **FAQ Q6 is the thinnest of the six** on hub non-overlap (§4). If a reviewer reads it as a
   restatement of the hub's throughput answer, cut it and run five questions. Five is inside the
   guidelines §14 range of four to eight.
6. **`audience.md` does not cover this vertical.** Its seven health-segment layers exclude
   occupational health, and `icp-detail.md` §6 is itself flagged as not covered by the newer ICP
   document. The plan uses the hub's `compliance_guardrails` and guidelines §9 instead, which are
   more specific and already approved for this vertical. This is a real gap in the audience document,
   not a gap in this plan, and it will recur on every Hub-8 article until someone writes the layer.
7. **The messaging line "speed clearance decisions"** sits in `messaging.md` for this segment and
   means shortening time-to-decision. The plan forbids it as a capability claim in Sections 6 and 7.
   Worth deciding whether the messaging line itself should be reworded at source, because it will keep
   turning up in briefs for this vertical.
8. **Two hub-owned claims are being knowingly restated** in Section 8: the does-and-does-not boundary
   and the compliance-framing sentence. This is intentional. Every article in a sensitive vertical
   states its own boundary, and the clinical-trials reference article records that a repeated scope
   disclaimer fitting its section is approved rather than a defect. Flagging it so it is not read as
   an oversight at checkpoint 2.
