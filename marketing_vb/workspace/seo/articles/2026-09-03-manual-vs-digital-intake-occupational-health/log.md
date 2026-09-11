# Run log — 2026-09-03-manual-vs-digital-intake-occupational-health

| When | Stage | What happened |
|---|---|---|
| 2026-09-03 | plan | `seo-planner` Phase 0-3. `plan.md` + `plan-audit.md` + `checkpoint-1-review-package.md`. Checkpoint 1 approved by Vadim: title, primary keyword, 12-section outline. `plan.md` carries `status: approved`. |
| 2026-09-03 | write | `draft.md`, 2,922 prose words, 12 H2s, 10 claim markers. Sources opened directly during the run: OSHA Appendix C (HTTP 200, confidentiality/timing/routing language quoted from the page), NHANES anthropometry PDF (5.5 MB, downloaded and converted, waist protocol read from Chapter 3 and the examiner/recorder role from section 1.5), EEOC guidance (HTTP 200, conditional-offer passage quoted). `bls.gov` returned HTTP 403, so the JOLTS hires figure is carried from `plan-audit.md`, which verified it the same day. |
| 2026-09-03 | lint (draft) | `article_lint.py`: 8 of 9 gates ok. FAIL on prose length only, 2,922 vs band 2,125-2,875. Detector CLEAN, density 0.64/1000. |
| 2026-09-03 | edit | `final.md`, 5 passes. 177 prose words cut (Section 4 -85, Section 9 -40, FAQ -30, Section 7 -19). Two corrective negations rewritten. Landed at 2,745, which is +9.8% on the 2,500 target and inside the publisher's +/-10% band. |
| 2026-09-03 | lint (final) | `article_lint.py` VERDICT PASS, exit 0, all 9 gates. Detector CLEAN, 0 hard fails, 0 house-rule violations, density 0.34/1000, rhythm variation 0.73. |
| 2026-09-03 | publish | `publish-package.md`. Meta title 57 chars, description 156 chars, 3 variants each. SEO checklist 14/15 with one item flagged for Vadim (medical-framing wording), strategy checklist 9/9. Alt-text suggestions for two illustrations. 5 open items. |
| 2026-09-03 | qc (judgment) | `workspace/_quality/seo/2026-09-03-seo-full-manual-vs-digital-intake-occupational-health.md`, 19/20, scope limited to judgment because both scripts had already gated the mechanics. |
| 2026-09-03 | STOP | Checkpoint 2. Waiting on Vadim: full text plus meta together, and the medical-framing ruling. |

## Deviations from the plan, both declared

1. Section 1 H2 shipped as "The intake step is where screening programs lose time" instead of the
   planned "The intake step, not the examination, is where screening programs lose time". The
   planned form is corrective negation in a heading, which the terminology guardrails restrict to
   real product, clinical, legal or regulatory boundaries.
2. Section 5 H2 shipped as "Manual vs digital intake, compared dimension by dimension" instead of
   "Manual and digital intake compared, dimension by dimension". The plan assigns the primary
   keyword's H2 occurrence to Section 5 and the planned wording does not contain the exact string,
   so the keyword-placement gate would have failed.

## Deviation from `plan.md` taken on the run brief's instruction — REVERTED 2026-09-03

The writer wrote the medical-device boundary directly, "FitXpress is not a medical device.", in the
Section 1 scope note, because item 7 of the run brief instructed that form, and it flagged the
conflict with `plan.md`, `CLAUDE.md` sections 6 and 15, the context pack and the `seo-publisher`
checklist, all of which prescribe the licensed "It is not positioned as a medical device." restored
2026-09-02 by Review 1 and Vadim's call.

**The brief was wrong and the flag was right.** Its stated reason, that the detector hard-fails on
the "positioned as" form, does not hold: `detect-ai-tells.py` carries the lookahead
`(?!a\s+medical\s+device\b)` specifically to license that sentence, and its remediation string
tells the author to write it verbatim. The scope note was restored to the licensed sentence in
`draft.md`, `final.md` and `publish-package.md` after the run; `article_lint.py` and
`detect-ai-tells.py` were re-run and both still pass. "Positioned as" appears nowhere else in the
article. The rule has now flipped three times across five files, which is carried to Vadim as open
item 1 - not as a blocker on this article, but as a question about where the rule should live.

## 2026-09-04 — Review 1 applied against the VERBATIM review (second pass)

**Two runs of the same request collided on these files.** Vadim's message went to the conductor
as `/new-article` (session `b2b6a3f2`, cwd `marketing_vb`, 09:08–09:47, non-interactive) and to an
interactive session (`eece794d`, 09:22 onward) at the same time. The conductor run had no Drive
access and no Bash: it reconstructed the review through WebFetch and could not execute
`article_lint.py` or `detect-ai-tells.py` (its own `final.md` frontmatter records both as "NOT
executed this session" — the known `settingSources:['project']` permissions gotcha). It wrote
`final.md` at 09:44 from `draft.md` rev 1 plus the interactive session's `plan.md` rev 2, then
exited. That file is kept as `final.md.conductor-0944-unverified` and is NOT the basis for
anything downstream: it is unlinted prose from the superseded draft.

The interactive session pulled the review verbatim from the source Google Doc
(`mcp__claude_ai_Google_Drive__read_file_content`). The reconstruction it replaced is at
`review-1.md.reconstructed-bak`. Four things the reconstruction missed, all now applied:
the whole "How the workflows differ" section and its table (reviewer graded *Workflow
differences: Partial* and supplied the table); the reviewer's own eight-row evaluation-metrics
table (rev 1 invented a five-row one whose header carried a hard-banned `you`); four more flagged
product statements in item 7 (six, not two); and the entire "What should be preserved" list,
whose item 6 protects the five implementation questions that rev 1 had cut to two.

**Open item for whoever publishes the Data, Privacy, Security & Regulatory FAQ.** The compliance
paragraph in the FitXpress section is stated inline at `compliance.md` precision because that
central FAQ is still unpublished (`content-plan.md:24`, last open P0 hub gap). Once it ships,
trim that paragraph to a link. The draft-only side-link placeholder that rev 1 carried has been
removed from the article entirely — review item 7 forbids a placeholder reaching the CMS version.

## 2026-09-04 — edit pass on `draft.md` rev 2 → `final.md` rev 3 (interactive session, Bash available)

Both gates were **executed**, not asserted. `article_lint.py` VERDICT PASS, exit 0, all 9 gates.
`detect-ai-tells.py` verdict CLEAN, `hard_fails: []`, `house_rule_violations: []`, exit 0, run on
channel `any` (nothing muted, the stricter setting). ai_density 0.42/1000 before and after,
rhythm_variation 0.65 → 0.66. Verdict blocks are pasted into `final.md` frontmatter under
`gate_article_lint` and `gate_detect_ai_tells`.

**The 09:44 `final.md` was overwritten**, as instructed. The unverified conductor output survives
only at `final.md.conductor-0944-unverified` and nothing was merged from it.

**Word band.** 2,200 → **2,199**, inside the reviewer's binding 1,900-2,200. The draft was at the
ceiling, so this pass ran as a zero-sum ledger: +23 words added (Section 4 table lead-in 11, the
cost side of the hybrid split in Section 6 +12), -24 cut (Section 1's closing "The intake around
the examination runs long" -7, Figure 1 callout -4, the duplicated "because the person is on site"
clause in the Section 4 reading paragraph -6, the universal EEOC framing -4, the Section 8 reframe
rewritten to the canonical "accurate enough for which decision?" -5, the duplicated
"across staff/sites" triple -2, EEOC short form in FAQ Q4 -3, Section 2 bullet 3 merged -1).

**Section 8 was checked before it was cut, per the run brief, and it was not cut.** Roughly 200 of
its 369 words are fixed approved text: FX-003 with its conditions sentence, FX-001 with its
reference in the same breath, the NDA-methodology line, the `compliance.md` precision sentence and
the boundary pair. Removing any of it would strip a figure of its conditions or its reference,
which is a worse outcome than 99 words over the per-section budget. Only editable prose changed
there ("capture" three times in three sentences, the impersonal "The role is", the duplicated
triple).

**Protected content verified programmatically, before and after.** Both reviewer-supplied tables
are byte-identical to `plan.md`: the five-row workflow table in Section 5 and the eight-row metrics
table in Section 7. The six reviewer-verbatim cells in the Section 4 comparison table and the
reviewer's verbatim reading paragraph after it are unchanged. All five implementation questions are
present. The scope note, the boundary pair and the evaluation-oriented CTA are untouched. Two
Section 4 cells that are **ours**, not the reviewer's, were fixed: "Integration dependency |
Depends on integration with the receiving system" was circular and now reads "Requires a receiving
system and a defined transfer path", and the data-entry cell lost the ninth "depends on".

**One sourcing gap closed.** The OSHA Appendix C passage asserted what a federal standard requires
and carried no link, while NHANES and EEOC both had one. It now sits on a meaningful anchor
(terminology guardrails Part 1 rule 2), at zero prose-word cost.

**Placeholders and side-links.** The only HTML comments in `final.md` are the seven claim markers,
which `v1/final.md` also carried and which the claim-traceability gate reads. No draft-only
placeholder, nothing pointing at the unpublished Data, Privacy, Security & Regulatory FAQ. The open
item above (trim the compliance paragraph to a link once that FAQ ships) still stands.

**Self-check (Pass 3c step 4)** is written out in the `self_check` field of `final.md`. The one
soft marker the detector still reports, `1x "serve as"`, is inside the protected scope note ("or
serve as a basis for hiring or employment decisions") and was left verbatim on purpose.

## 2026-09-04 — seo-publisher, rev-2 package against `final.md` rev 3

Both gates re-run independently in this session (not trusted from frontmatter): `article_lint.py`
VERDICT PASS, all 9 gates ok, prose 2,199 words; `detect-ai-tells.py` CLEAN, 0 hard fails, 0
house-rule violations, ai_density 0.42/1000. Both outputs match `final.md`'s recorded frontmatter
exactly.

**Cannibalization guardrail re-verified against the live hub**, fetched fresh today (not from
memory or from the rev-0 package's claim). Confirmed removed: the does/does-not table, the
buyer-profile roster, the standalone BLS why-now section, the five-step implementation walk, the
pre-employment-vs-return-to-work table. Confirmed owned by this article and absent from the hub:
the 14-row method-comparison table, the reviewer's workflow-differences table, the decision
framework, the reviewer's evaluation-metrics table, the accuracy/repeatability figures (hub's own
inventory records these as never spent there). One residual flagged, not certified clean: the
Section 1 opening scene still echoes the hub's opening paragraph, cut by roughly 80% and
repurposed toward appointment-slot economics rather than the hub's narrative. Recorded as open
item 1 for Vadim rather than smoothed over.

Meta title: "Manual vs Digital Intake in Occupational Health Screening" (57 chars). Meta
description: "Manual vs digital intake in occupational health screening, compared step by step:
workflow, cost, exceptions and the metrics to test before switching." (150 chars). SEO checklist
15/15. Content strategy checklist 9/9 (one item passed on a documented judgment call, not a bare
mechanical check — see the cannibalization section in `publish-package.md`).

`publish-package.md` rewritten wholesale as the rev-2 package (`revision: 2`,
`status: ready_for_review`), not amended from the rev-0 file. The rev-0 package's central claim
(cannibalization clean) is explicitly not carried forward without re-verification.

**STOP.** Checkpoint 2. Waiting on Vadim: full text plus meta together, and a call on the
Section 1 opening-scene echo (open item 1) if he wants it at zero rather than "substantially
resolved."

## 2026-09-07 — Review 2 pulled, applied through the pipeline, QC'd and remediated

**Source.** Google Doc tab "Review 2" (`t.9ltdnz6zu0ug`), pulled through the `oo` googledocs
connector with `include_tabs_content=true` — the claude.ai Drive MCP is gone since the account
change, `oo` is the route now. Verbatim into `review-2.md`; nothing reconstructed, unlike the
Review 1 first pass. Soft line breaks (`\x0b`) restored, or four of the five editorial refinements
would have collapsed into unreadable single lines.

**Base verified before anything was edited.** `final.md` rev 3 was normalised (links to anchor
text, emphasis stripped, claim markers dropped) and diffed against the doc's "Version 2" tab:
**identical, 85 of 85 content lines**. So the reviewer read exactly the shipped text and every
"current wording" quote in the review resolves to a unique string in the file. Worth keeping as a
step — it is cheap and it is the thing that makes `count == 1` replacements safe.

**A coordinator hand-pass was written and then reverted.** The first application of Review 2 was
done by hand in this session, gates passing, before Vadim said the pipeline must apply reviewer
rounds, not the coordinator. `final.md` and `publish-package.md` were restored from `v2/`, the
hand-pass was moved OUT of the article dir so it could not contaminate the agents' inputs, and the
run was handed to `seo-editor` -> `seo-publisher` -> `quality-controller`. Only the coordinator
artifacts survived from it: `review-2.md` and `review-2-decisions.md`. **`review-2-decisions.md`
§9 still carried the hand-pass's gate numbers for a while (2,173 words, 20 replacements) — a file
that was never shipped.** `seo-editor` flagged it rather than editing the coordinator's section,
which was the right call; §9 is now rewritten with the shipped numbers.

**Revisions.**

| Rev | By | What | Prose | Gates |
|---|---|---|---|---|
| 4 | `seo-editor` | Review 2 applied, 22 replacements, each asserting `count == 1` | 2,185 | PASS / CLEAN, exit 0 |
| 4 | `seo-publisher` | `publish-package.md` rev 3 | — | re-run, agreed |
| — | `quality-controller` | **17/20** (A4 B5 C2 D3 E3) | — | judgment scope only |
| 5 | `seo-editor` | QC remediation, four fixes | **2,160** | PASS / CLEAN, exit 0 |
| — | `seo-publisher` | `publish-package.md` rev 4 | — | re-run, agreed |

Both gates were executed at every stage and re-run independently by the coordinator between
stages. Three separate runs of each agree on the final numbers: `article_lint.py` PASS exit 0 all
9 gates, 2,160 prose words inside the reviewer's binding 1,900-2,200 band with 40 words of
headroom where rev 3 had one; `detect-ai-tells.py` CLEAN exit 0, `hard_fails: []`,
`house_rule_violations: []`, ai_density 0.86 against a budget of 8.0, rhythm variation 0.66.

**The one real defect this pass produced, and it was the coordinator's.** `review-2-decisions.md`
graded editorial refinement E5 as "Verbatim" and said "Q1 and Q5 survive". E5 actually says reduce
the five questions to "which components move, and **how measurement performance was evaluated**".
`seo-editor` applied the decisions row rather than the instruction, kept the old narrow Q5, and the
retained question then duplicated the E3 sentence beneath it — which was escalated to Vadim as an
unresolvable reviewer-vs-reviewer conflict. It was neither. `quality-controller` caught it
(finding A-1), rev 5 applies E5 in the reviewer's own words, the duplication is gone and the open
item is struck from the package.

**Standing lesson, for whoever writes the next `review-N-decisions.md`:** the editing agent reads
the decisions file, not the review. A row that summarises an instruction loosely *becomes* the
instruction. Grade rows against the reviewer's words, and where a row says "verbatim", quote the
words.

**Three sub-points of review item 6 were declined on source-of-truth grounds** and are open for
Vadim, not for the pipeline: R2-2 (remove "processes no personal identifiers" — it is the literal
text of approved claim FX-014 and the sentence carries that marker, so cutting it desyncs the
article from a claim it still cites; a cut has to reach `compliance.md`, `proof-points.md`,
`how-it-works.md` **and** the context-pack claim text, or the next pack regenerates the phrase),
R2-3 (GDPR controller/processor — in no brand-asset), R2-4 (retention of generated outputs — the
asset documents photo retention only, and the article inherits that silence). R2-1, the one
genuine reviewer-vs-reviewer overlap in Section 4, is also left in deliberately; `quality-
controller` independently agreed it should not be settled by the pipeline.

**STOP.** Checkpoint 2, again. Waiting on Vadim: the three privacy calls, R2-1, and whether he
wants a "Version 3" tab written back to the source Google Doc.

---

## 2026-09-11 — editorial final received, rules updated from it

Vadim shared the editor's final (Google Doc tab "Final version") and Assel's verdict on our
revision 5: «в той версии мне не нравилась длинна предложений, были повторения и читалось это всё
как явно AI». Revision 5 is the doc's "Version 3" tab (similarity 0.98); "Version 4" and
"Version 5" are her intermediate passes.

- **Saved:** `editorial-final-2026-09-11.md`, the text of record until the page is live (the URL
  returned 404 today), and `editorial-delta-2026-09-11.md`: what changed, how the Review 2 open
  items were settled, where the final departs from canon.
- **Measured** with the new gate: revision 5 averages 17.7 words per prose sentence, 14% over 25
  words, 6 over 35. The final: 14.7, 3.2%, 1. Prose words 2,160 → 1,877.
- `final.md` and `publish-package.md` stay at revision 5, as history. `social_pack.py source` now
  resolves to `editorial-final-2026-09-11.md`, and so does the switcher.
- **Rules:** `brand-assets/style-guides/editorial-rewrites.md`, `article_lint.py` gate
  `sentence length`, agents re-synced from DEV. Full entry: `docs/changelog.md`, 2026-09-11.
- **Open for Vadim:** the medical-device sentence; BAA, retention and personal-identifier wording;
  the disability limitation; primary keyword absent from the first paragraph.

## 2026-09-11 (later) — Vadim's decisions on the canon departures

- **Medical device:** "FitXpress is not a medical device." everywhere. The detector no longer
  licenses "It is not positioned as a medical device." The revision 5 files in this directory
  still carry the old sentence and stay as history.
- **`compliance.md` unchanged for now.** The final's privacy wording is not reused.
- **The disability limitation is approved:** `proof-points.md`, `accuracy-formulations.md` §5.
- **Gate 7 softened:** `editorial-final-2026-09-11.md` now passes it. Its only remaining lint
  failure is claim traceability, which is expected: an editor's file carries no claim markers.
