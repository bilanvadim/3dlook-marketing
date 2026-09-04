---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
review: 1
decided: 2026-09-04
revised: 2026-09-04 (second pass, against the VERBATIM review — the first pass ran against a lossy reconstruction)
decided_by: coordinator (orchestrator)
purpose: >
  How each Review 1 item is applied, and how it was checked against brand-assets / content-plan.
  seo-planner / seo-writer / seo-editor / seo-publisher MUST read this alongside review-1.md.
  Where this file and review-1.md disagree, THIS FILE WINS.
---

# Review 1 — application decisions

## 0. What changed on the second pass (read this first)

The first decisions pass was written against a WebFetch reconstruction of the review, because
that session had no Drive access. The verbatim text is now in `review-1.md`. Two gaps mattered:

1. **"What should be preserved" was missing entirely.** It is now recovered — eight named
   elements, listed in §F below. They are protected from the duplication cuts in item 1.
2. **Item 7 listed 2 flagged statements; the real item flags 6**, plus two extra instructions
   (no draft-only placeholder in the CMS version; stop listing the full body-composition
   inventory). See §B.

Also newly in hand and NOT in the reconstruction: the reviewer's own compliance-with-brief
table (which grades **Evaluation criteria** and **Workflow differences** as *Partial* — that is
what drives the two new tables), and the verbatim contents of both proposed tables in the
recommended structure. **Use the reviewer's own table rows as written; do not re-invent them.**

Both open items carried to Vadim in the first pass (D1 fidelity, D2 the missing section) are
resolved. Nothing is blocking.

## A. Cross-check against content-plan.md and content-strategy-guidelines.md

`brand-assets/content-strategy/content-plan.md`, Hub 8 (Occupational Health), row "Comparison —
Manual Intake vs Digital Intake in Occupational Health Screening": hub is live (published
2026-07-10), row confirms this article's action type is correctly "Net-new supporting," and
states the guardrail directly: *"Throughput, missing data, rescreens, multi-site consistency.
No medical/clearance claims."* The Main hub row states it *"Owns pre-employment/pre-placement/
return-to-work intake, fit-for-duty documentation support, rescreens, multi-site, workforce
screening vendors, workers'-comp."*

`content-strategy-guidelines.md` §5 (Prevent cannibalization) is explicit: *"If an existing
page already owns the main topic, the new article must have a narrower angle"* and *"Do not
copy the existing article's structure and rewrite it with slightly different wording."* This is
existing, standing policy — not a new rule the reviewer is inventing.

**Verdict: Review item 1 (excessive duplication with the hub) is correct and is an enforcement
of a rule we already have.** The buyer-profile section, the full does/does-not-do table, and
the workflow explanation belong to the hub by that guardrail. Executed as stated.

Note the reviewer's brief table also grades "Avoid medical or clearance claims" as *Mostly
compliant* with the comment that the article **spends too much space** on clearance, OSHA and
EEOC for a comparison page. That is a trim instruction, not a compliance failure. The
boundaries stay; the airtime shrinks.

## B. Item 7 — the six flagged product/privacy statements, checked one by one

Five of the six are standing approved compliance language, not fabrications and not
placeholders. The sixth is a genuine over-reach and gets cut.

| Flagged statement | Source in brand-assets | Decision |
|---|---|---|
| "Processes no personal identifiers." | `product-info/compliance.md:23`, `proof-points.md:137`, `how-it-works.md:56` | Grounded. Keep, in `compliance.md` wording. |
| "Deletes photos immediately or within 30 days according to client policy." | `how-it-works.md:54`, `CLAUDE.md` §12 | Grounded. Keep, with the client-policy conditionality stated, not implied. |
| "Outputs are time-stamped at the moment of capture." | `product-info/use-cases/fx-occupational-health.md:10`, `faq.md:90` | Grounded as a product fact. **But** review item 5 separately forbids the inference that time-stamping *by itself* makes records comparable. Keep the fact, drop the inference. |
| "Maintains HIPAA safeguards." | `compliance.md:9`, `faq.md:27-28` | Grounded. Keep. |
| "Follows GDPR principles." | `compliance.md:10`, `proof-points.md:132`, `how-it-works.md:57` | Grounded. Keep — and keep the exact hedge "follows GDPR principles," never "GDPR compliant." |
| "The document reaches the reviewer without passing through the employer." | **none** | **Not grounded.** This is our own inference from OSHA Appendix C, not a product property and not what the standard says. **Cut.** It also falls under review item 6 (the OSHA passage narrows to one regulated example). |

**So the fix is precision, not evidence-hunting** — with one real deletion. Two further
instructions inside item 7, both executed:

- **"A draft-only placeholder should not remain in the CMS version."** `final.md:135` currently
  carries `<!-- SIDE-LINK PLACEHOLDER ... -->` pointing at the unpublished Data, Privacy,
  Security & Regulatory FAQ. `content-plan.md:24` confirms that page is still the last open P0
  hub gap (drafts under `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/`,
  nothing live). **Decision: drop the placeholder sentence entirely and keep the compliance
  paragraph short and precise.** Add a line to `log.md` so whoever ships the central FAQ knows
  to come back and trim this paragraph to a link.
- **"Consider whether listing basal metabolic rate and every body-composition output adds
  value."** It does not, in a comparison page. **Decision: cut the inventory** (`final.md:111`,
  "80+ body measurements along with BMI, basal metabolic rate, body fat percentage, lean mass
  and fat mass") down to the outputs the intake workflow actually consumes. Bonus: removing
  "basal metabolic rate" removes the abbreviation-expansion problem noted at `final.md:43`.

## C. Items applied as stated, no conflict found

- **Item 2 (intake definition split)** — applied. The reviewer's three-phase model
  (pre-appointment intake / on-site screening / decision) matches the hub's own boundary
  language better than the current flat four-part list. Adopt the reviewer's framing that the
  real comparison is *on-site manual intake vs structured pre-appointment intake inside a
  hybrid workflow*. No brand-assets conflict.
- **Item 3 (FitXpress vs digital-intake scope line)** — applied, using the reviewer's own
  sentence, placed early. Factually correct (FitXpress does not administer questionnaires) and
  matches `product-info/overview.md`'s "workflow layer, not the whole system" framing.
- **Item 4 (comparison table)** — applied. All six replacement rows are hedged, accurate
  versions of claims already in scope; none introduces a number needing `proof-points.md`
  sourcing. Also add the five missing dimensions the reviewer names: ongoing labor, exception
  handling, integration dependency, fallback availability, data-entry correction rates.
- **Item 5 (unsupported claims)** — applied. All seven. Every requested fix is "cite it,"
  "hedge it," or "cut it," which is `editorial-guardrails.md` principle #1 (substantiation)
  applied to sentences the writer should have caught. Use the reviewer's own replacement
  paragraph for the throughput claim.
- **Item 6 (sourcing)** — applied. BLS paragraph **removed** (no occupational-health-specific
  substitute is available; do not go hunting for one to keep the paragraph alive). NHANES stays
  with the reviewer's neutral conclusion replacing the staffing claim. OSHA narrows to one
  regulated example. EEOC labelled US-specific and cut to a short note.

## D. Structure and budget

The reviewer's 9-section structure is adopted as given, including both new tables **verbatim
from `review-1.md`** — the side-by-side workflow table (fixes "Workflow differences: Partial")
and the evaluation-metrics table (fixes "Evaluation criteria: Partial", and promotes the metrics
out of the FAQ where they were an afterthought).

Target: **1,900–2,200 words**, down from 2,745. FAQs go from 6 to the reviewer's 4.

## E. Process

Items 1 and 2 change the section list and the word budget, which is a `plan.md`-level change,
not a `final.md` patch — per `.claude/commands/new-article.md`, structural review feedback is
applied to the plan, not painted onto finished prose. `seo-planner` revises `plan.md` first,
then `seo-writer` → `seo-editor` → `seo-publisher` run in the normal chain. No checkpoint-1
re-approval; revision cycles flow straight through to checkpoint 2.

`v1/` already holds the snapshot of the reviewed state (draft, final, plan, publish-package).

## F. Protected — do NOT cut these while executing item 1

The reviewer names eight elements to preserve. The duplication trims in item 1 must not take
them out:

1. The central manual-versus-digital comparison concept.
2. The recognition that manual intake still fits certain programs.
3. The hybrid conclusion.
4. The focus on appointment time, multi-site standardization and pre-visit availability.
5. The distinction between accuracy and repeatability.
6. The five implementation questions.
7. The explicit boundary around examinations and employment decisions.
8. The restrained, evaluation-oriented CTA.

The reviewer's closing instruction governs the whole rewrite: the article's centre of gravity
moves away from explaining the occupational-health use case (the hub owns that) and toward
helping a buyer **compare methods, identify tradeoffs and define a measurable pilot**.
