---
qc_date: 2026-09-03
agent: seo-writer + seo-editor + seo-publisher (one full run)
artifact: workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md
track: seo
artifact_type: seo-final
total_score: 19/20
status: good
scope: judgment only
coordinator_review: |
  agreement: agree
  top_issue: The medical-framing sentence ships in the form the run brief ordered ("FitXpress is not a medical device.") while CLAUDE.md, plan.md and the publisher checklist prescribe the restored "It is not positioned as a medical device." Third flip of one rule; needs one line from Vadim, and that line should retire the losing form from all four documents at once.
---

# QC Report — full SEO run — 2026-09-03

**Artifact:** `workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md`
**Total: 19/20** — good

**Scope of this report is judgment only.** Mechanics were gated by
`scripts/article_lint.py` (9 gates, VERDICT PASS, exit 0) and
`brand-assets/style-guides/scripts/detect-ai-tells.py` (CLEAN, 0 hard fails, 0 house-rule
violations, density 0.34/1000 against a budget of 6.0). Hard bans, prose word count, claim
traceability in both directions, banned claims, superseded figures, link canonicalisation,
keyword placement, M1 abbreviations and accuracy discipline are therefore taken as facts here
rather than re-judged. What follows is the part a script cannot decide: whether the argument
holds and whether each section earns its place.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## A. Adherence — 5/5

All 12 planned sections exist in the planned order, each holding its assigned goal and its
must-covers. The three boundaries the plan audit called hard are all held in the text, not just
in the frontmatter:

- **FX-001 is never turned into "digital beats a tape measure".** Section 7 states the reference
  in the same paragraph as the figure and then says outright that a superiority claim over a tape
  measure is out of reach because expert manual measurement is what the figure is measured
  against. FAQ Q1 repeats the same refusal in answer form. This is the single most likely
  overclaim in the topic and the article argues against its own commercial interest on it.
- **Repeatability, not one-time accuracy, is the differentiator.** FX-003 is quoted verbatim from
  `accuracy-formulations.md` section 1.2, carries its conditions (internal repeatability testing,
  real-world customer dataset, five repeated scans per participant), and the paragraph carrying
  it links to the accuracy framework rather than parking the link in a further-reading list.
- **FX-004 is absent.** No percentage of repeatability consistency appears anywhere. The linter
  confirms it as "approved but uncited".

Sources: three of the four external sources were opened directly during this run (the OSHA
Appendix C page, the NHANES anthropometry PDF, the EEOC guidance) and the passages used are
quoted from what was actually on the page. The NHANES protocol passage was written from the PDF
text as the plan required, not from a paraphrase. `bls.gov` returned HTTP 403, so the hires
figure is carried from `plan-audit.md`, which verified it the same day; this is disclosed in the
final frontmatter and in the publish package rather than passed off as a fresh fetch.

**Two declared departures from the plan's letter**, both recorded rather than silent:

1. Section 1's H2 was planned as "The intake step, not the examination, is where screening
   programs lose time". Shipped as "The intake step is where screening programs lose time".
   Reason: the planned form is corrective negation, which the terminology guardrails restrict to
   real product, clinical, legal or regulatory boundaries. A rhetorical "X, not Y" in a heading
   is not one of those.
2. Section 5's H2 was planned as "Manual and digital intake compared, dimension by dimension".
   Shipped as "Manual vs digital intake, compared dimension by dimension". Reason: the plan
   assigns the H2 occurrence of the primary keyword to Section 5, and the planned wording does
   not contain the exact string, so the keyword-placement gate would have failed on it.

## B. Factual accuracy — 5/5

Every product figure traces to an approved claim and sits on a line carrying its marker: under 45
seconds (FX-006), two photos (FX-007), 80+ body measurements (FX-008), the body-composition
outputs (FX-009), the compliance bundle (FX-014), repeatability (FX-003), accuracy with its
reference and population condition (FX-001). Both accuracy formulations are verbatim from the
canon, hyphen forms intact (`96-97%`, `1.5-2.0 cm`, `less than 1 cm`).

The ISO 8559 benchmark does not appear at all, so the two-benchmark rule cannot be broken. No
per-measurement figures. Methodology is offered as "available under a non-disclosure agreement"
rather than as a bare percentage. Body-composition outputs list only the subset that survived the
2026-09-02 wellness-copy decision; essential fat and beneficial fat are absent.

The four external facts are stated at the level the sources support: the JOLTS hires level and
rate with "little changed" preserved, the NHANES waist protocol as procedure rather than as
evidence about anyone's accuracy, the OSHA questionnaire's timing, confidentiality and routing
requirements, and the EEOC conditional-offer boundary. The OSHA paragraph explicitly says
FitXpress does not administer that questionnaire, which is the one inference a reader could
otherwise draw.

## C. Brand & tone — 3/3

The reframe move opens Section 7 in its canonical form ("which decision it has to be accurate
enough for"). Register stays buyer-framed rather than "you"-framed: no second person anywhere in
the body. The comparison is not a clean sweep, and it is not a token concession either. Manual
intake wins three of nine dimensions in the table (scope, access, setup cost) and the prose
reading names all three; Section 9 opens on the five conditions under which manual intake is
still the right choice, before the digital case is made.

Rhythm variation is 0.73 against a 0.35 floor, helped by the short verdict lines ("The rows split
cleanly.", "It never decides a candidate.", "In five situations."). Two corrective negations from
the draft were rewritten in the edit pass, and the one remaining negation cluster is the scope
note, where a single "does not" governs three verbs. That is the approved shape, and the hub has
the same construction.

## D. Format & structure — 3/3

Frontmatter complete on both `final.md` and `publish-package.md` (`slug`, `product`, `status`,
`word_count`, `author`, `hub`, `cluster`, `intent`, `action_type`, `primary_keyword`,
`claims_verified`, `claims_withheld`, `changes_summary`, `self_check`). Correct paths. Twelve H2s,
two tables, one CTA, FAQ in bold-question form.

**One structural imbalance worth naming.** Section 4 runs 351 prose words against a 260 target
(+35%) and Section 12 runs 33 against 60. Section 4 earns most of its overrun, since it carries
the article's central mechanism and both regulator citations, but it is now the longest section in
a piece whose core is meant to be Sections 5 and 9. If Vadim wants the balance corrected, the
cheapest cut is the NHANES protocol clause list, which could lose 30 words without losing the
point. The total is 2,745 against 2,500, which is +9.8% and inside both the publisher's +/-10%
band and the linter's +/-15% band.

## E. Output quality — 3/4

Not a 4, for one reason: it cannot ship as-is. Two decisions sit above the text.

1. The medical-framing sentence is in the form the run brief ordered, which contradicts the form
   `CLAUDE.md`, `plan.md` and the publisher checklist currently prescribe. The detector licenses
   both, so nothing is broken; it is a wording ruling only Vadim can make, and it has now flipped
   three times.
2. The sideways trust link is an unresolved placeholder, because the Privacy and Regulatory FAQ is
   still unpublished. Section 6 carries the anchor phrase and an HTML comment where the URL should
   be. Someone has to either ship the FAQ or drop the sentence at CMS entry.

Everything else reads as expert copy. The genuinely new contribution over the hub is the
decomposition of intake into four components with two marked as remote-capable, which is what lets
the comparison be honest and lets Section 9 recommend a hybrid without hedging. The OSHA
confidentiality-routing point is the strongest fresh fact in the piece and it belongs to no other
page in the cluster.

## Top 3 issues (priority for improver)

1. **`seo-editor.md` Pass 3 item 2 is stale and actively harmful.** It instructs the editor to add
   "The common mistake is..." and "What most teams miss is...". Both are hard fails in the
   detector's `presumed_reaction` category, added 2026-08-25. An editor following the prompt
   literally would introduce the failure the same prompt's Pass 3c then catches. Fix the prompt.
2. **The medical-framing rule lives in five places and has flipped three times.** This run had to
   choose between a run brief and three repo documents that disagreed. Whatever Vadim decides,
   the losing form should be deleted from the documents rather than left as a second opinion.
3. **`article_lint.py` gate 3b fires on any four-digit numeral in prose.** Years and regulation
   numbers (`2021`, `1910.134`) read as unsourced product figures and demand a claim marker. This
   run avoided the gate by keeping years and the CFR number out of the prose entirely, which is a
   real editorial constraint imposed by a false positive. Worth narrowing the `\d{4,}` branch, for
   instance by exempting a bare four-digit number in the 1900-2099 range and any token of the
   shape `\d+\.\d+` that follows a section sign or "CFR".
