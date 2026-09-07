---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
artifact: publisher report (checkpoint 2 package + delta table)
role: seo-publisher
input: draft-v2-editor.md, plan.md, plan-audit.md, editor-report.md, refresh-gap-analysis.md
output: publish-package.md
created: 2026-09-03
status: ready_for_review
---

# Publisher report — Bariatrics hub refresh

This file carries the rationale, verification detail, and the draft-vs-live delta table behind
`publish-package.md`. It mirrors the `plan.md` / `plan-audit.md` split: the package is what a CMS
operator needs to publish; this report is why the package looks the way it does, for Vadim and any
later reviewer.

---

## 1. Final gate verification, re-run this session

```
$ python3 scripts/article_lint.py workspace/seo/articles/bariatric-hub-refresh/draft-v2-editor.md \
    --pack workspace/seo/_context-packs/2026-09-03-bariatric-hub-refresh.yaml --report

[ok  ] hard bans (detect-ai-tells)
         ai_density: 0.36, verdict: CLEAN, rhythm_variation: 0.57
[ok  ] prose length
         prose words 4712 vs target 4400 (band 3740-5060)
[ok  ] claim traceability
         claims_used: ['FX-001', 'FX-002', 'FX-005', 'FX-006', 'FX-007', 'FX-008', 'FX-009']
         claims_known: 10
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         links_total: 18, links_distinct: 10, directions: {'up': 1, 'sideways': 6, 'down': 1, 'trust': 1}
[ok  ] keyword placement
         keyword: bariatric pre-qualification, occurrences: 6, h2_count: 12
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         accuracy_figures_present: True, links_to_framework: True

approved but uncited: FX-003, FX-004, FX-010

VERDICT: PASS
```

**9 of 9, unchanged from the editor's report.** This is a fresh run against the current file and
pack on disk, not a re-statement of the editor's number. The report's final line ("Mechanics are
clean. Judgment is still open: run quality-controller on whether the argument holds and whether each
section earns its place.") is a standing reminder from the script, not a fail; the judgment call is
this publisher pass plus Vadim's read, not a further mechanical gate.

**AI-tells detector, also re-run this session, not estimated:**

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/bariatric-hub-refresh/draft-v2-editor.md --channel article --summary

SEO / blog article - en - 5545 words
AI density: 0.36/1000 (budget 6.0) -> low
VERDICT: CLEAN
TOP SOFT MARKERS:
  2x 'facilitated' (L121)
```

This matches `draft-v2-editor.md`'s own frontmatter (`ai_density_after: 0.36`) and the editor
report's Pass 3c figure exactly, because it is the same script against the same file. Recording the
actual command and output here (and in `publish-package.md`) per the 2026-08-25 correction to this
skill's instructions: an estimate, however close, is not the same as a run, and the difference has
mattered before on this exact pipeline.

**Additional independent checks run directly against the file, not through the linter:**

```
$ grep -cP '[\x{2013}\x{2014}]' draft-v2-editor.md   -> 0   (zero em or en dashes)
$ grep -in "dexa" draft-v2-editor.md                  -> no match (DXA used throughout, never DEXA)
$ grep -o '<!-- ext-claim: [A-Za-z0-9_.-]*' ... | sort | uniq -c   -> 10 distinct ids, 16 markers
$ grep -c 'DOWN-LINK LANDING' draft-v2-editor.md      -> 7
```

---

## 2. What changed between the live page and this draft

### 2a. Structure: 9 H2s (live) to 12 sections (new), FAQ 20 questions to 16

| Live section (published-live-2026-07-27.md) | Words | Fate in the new draft |
|---|---|---|
| H1 + intro + disclaimer | ~250 | REWRITE into Front matter. Disclaimer kept verbatim; H1 and meta description rewritten (§2c). |
| 1. Why bariatric programs need faster pre-qualification | ~207 | Merged with #2 into new **Section 1**, "The bariatric intake gap." |
| 2. The intake gap: when eligibility gets confirmed too late | ~286 | Merged into new **Section 1**. |
| (mid-body eBook promo block, "The Digital Health Revolution") | — | **Dropped.** Second CTA in the body, which the style guide forbids. Not carried forward; flagged as Open Item #10 in `plan-audit.md`, decision default is to omit rather than restore silently. |
| 3. The GLP-1 shift: volume contracted, intake complexity rose | ~355 | REWRITE into new **Section 4**, "GLP-1 changed the shape of the intake funnel." Every number in it changes (§2b). |
| 4. What FitXpress captures, and how | ~202 | Merged into new **Section 7**. |
| 5. Pre-qualification: structured body data before the consult | ~400 | KEPT (structure and mechanism paragraph intact) as new **Section 6**. Use Case Summary bullet list promoted to front matter. |
| 6. Pre-auth documentation: cleaner packets, fewer delays | ~380 | SPLIT. The payer-timeline paragraph is replaced entirely by new **Section 3** (CMS-0057-F). The packet-contents list moves to Section 3. The documentation-mechanics paragraph moves to new **Section 9**. |
| 7. Post-procedure: turning the baseline into longitudinal tracking | ~224 | REWRITE and expand into new **Section 8**, nearly doubled, promoted from the thinnest major section to a co-equal spine with pre-qualification. |
| 8. Where FitXpress fits in the bariatric patient journey | ~114 | Merged into new **Section 7**; the patient-journey table carries over unchanged. |
| 9. Why mobile body scanning beats manual measurement workflows | ~277 | REWRITE into new **Section 10**, retitled away from "beats" (hype-adjacent), converted from a bullet list into a comparison table. |
| 10. FAQ, 20 questions in 3 blocks | ~1,319 | REWRITE into new **Section 11**, 16 questions in 4 blocks (§2d). |
| CTA + Related reading (2 links) | ~100 | REWRITE into new **Section 12**, 7 related-reading links (up from 2). |
| — (no live counterpart) | — | **NEW: Section 2** ("Short answer" GEO/AEO block), **Section 3** (CMS-0057-F clock), **Section 5** (documented BMI history vs. current BMI). |

Net: 3 live sections merged away, 3 sections newly added, 1 section split across three new
locations, 1 section promoted, 1 mid-body promo dropped. Total prose is roughly flat (live ~4,100,
new 4,712 all-in / 4,316 excluding table cells), but the internal composition shifted substantially:
the FAQ shrank from 32% of the article to 16.8%, and patient progress tracking grew from the
thinnest major section (224 words) to a full co-equal section (390 words) plus its own share of
Section 5's new argument.

### 2b. FAQ: 20 questions to 16, not 13 — Branch B

The plan priced two branches for the live FAQ's "About bariatric surgery" block (`plan-audit.md`
§D-1): Branch A cuts it entirely (13 questions total), Branch B keeps three of its six questions in
rewritten, non-clinical-outcome form (16 questions total). **The shipped draft is Branch B**
(`draft-v2-editor.md` frontmatter: `faq_branch: B`), per `plan.md`'s header note that Vadim's
2026-09-03 approval, given without naming a branch, was taken as approval of the audit's own
recommendation to keep Branch B.

| Live FAQ block | Live count | New block | New count | What happened |
|---|---|---|---|---|
| Pre-qualification and pre-authorization | 8 questions | Pre-qualification and pre-authorization documentation | 6 questions | 2 absorbed into others, 1 new (payer-decision-clock), 1 new (documented BMI history) |
| Post-procedure progress tracking | 6 questions | Patient progress tracking | 4 questions | 2 absorbed into others |
| About bariatric surgery | 6 questions | Bariatric surgery basics | 3 questions | 3 clinical-outcome questions (benefits, side effects, pros/cons) cut under **both** branches; 3 remaining rewritten to carry no clinical-outcome claim (D-1 ruling) |
| — | — | Scope and governance (new block) | 3 questions | Guidelines §14 requires this block type; none existed on the live page |

Live 20 to new 16. Every new answer runs 2 to 4 sentences (guidelines §14 range), against a live FAQ
that asked the same pre-auth question four different ways.

### 2c. The four substantive argument changes named in the task brief

1. **CMS-0057-F, the 7-day prior-authorization clock (new Section 3).** The live page's payer-timeline
   sentence, *"Payer review windows commonly run from a few weeks to several months,"* is gone. It is
   now wrong for impacted payers on standard requests, and it is not replaced with a new universal
   number, because the honest statement is that the window depends on payer, plan type and whether
   the request is expedited. The new section states the rule (72 hours expedited / 7 calendar days
   standard, effective 1 January 2026), the scope limitation in the same breath (Medicare Advantage,
   Medicaid, CHIP, Federally Facilitated Exchange Qualified Health Plans; not all commercial ERISA
   plans; no prior authorization at all for Medicare fee-for-service), and inverts the live page's
   argument from "cleaner packets, fewer delays" to "first-pass completeness is the whole game."
2. **GLP-1 rebuilt on 2026 data (new Section 4).** The live section's numbers stopped at a 2023
   snapshot (*"bariatric surgery use fell 8.7% between 2022 and 2023,"* JAMA Network Open via
   StatNews). The new section replaces it with a three-row market-indicator table built from two
   measurement systems that are explicitly kept apart: the ASMBS national estimate (270,089 in 2023,
   down 3.5% from 279,967 in 2022, series ends 2023) and the JAMA Surgery 13 May 2026 claims cohort
   (utilization down 34.1% from 2022 to 2024, cohort counts through 33,429 in 2025). The two never
   share a sentence, per the two-series guardrail the gap analysis flagged as a blocker (§3).
3. **The documented-BMI-history section (new Section 5, no live counterpart at all).** Built on an
   ASMBS release (5 May 2026, Chhabra et al., NYU Grossman) showing patients lose roughly 8% of body
   weight on a GLP-1 before surgery. The operational point, entirely absent from the live page: a
   patient's **current** BMI can sit below a payer's threshold while their **documented history**
   still qualifies, which shifts eligibility toward dated, verifiable history rather than a single
   consult measurement. This is flagged in the plan and the audit as the single sharpest new
   operational argument on the page.
4. **Two substantiation fixes, both inside the new Section 1.**
   - The live page's *"an estimated 33 million US adults meet eligibility criteria, yet fewer than 1%
     complete surgery in any given year"* is gone. Its citation (PMC10136401) is a qualitative
     attrition paper, not an eligibility-prevalence source, and no source on file supports a "33
     million" figure. Replaced with two ASMBS statements that carry their own numbers: "about 1% of
     those who meet eligibility requirements" (2025 Fact Sheet) and "90-95% of patients with severe
     obesity received no treatment during the study period" (ASMBS, 5 May 2026).
   - The live page's *"pre-operative dropout rates of up to 50-60% are reported across bariatric
     programs"* (used twice on the live page) published the top of a wide, methodology-dependent range
     as if it were typical. Replaced with the full range and its dependency: a 2026 narrative review's
     "as high as 60%," one cohort at 22.25%, Canadian mandatory-pathway programs at roughly 36-76%, US
     programs at roughly 39-70%, and one single-centre series at 8.9% pre-pandemic, with the explicit
     statement that attrition depends on program design and how it is measured.

### 2d. Title, meta description and positioning

Live H1: *"Bariatric Pre-Qualification with Mobile 3D Body Scanning: Faster Pre-Auth."* Leads with
the technology, per CLAUDE.md §3's shift away from "best model" positioning, and subordinates
progress tracking entirely (224 words, buried at section 7 of 9). New H1: *"Bariatric
Pre-Qualification and Patient Progress Tracking: A 2026 Body-Data Guide for Obesity Care Teams,"*
co-headlining both spines and naming the audience instead of the technology. Live meta description
opened with "How bariatric programs can use FitXpress..."; the recommended replacement (§1 of
`publish-package.md`) leads with the payer clock and the two workflows instead, with FitXpress named
nowhere in either the title or the description.

---

## 3. Verified against the audit ledgers, nothing reintroduced

Grepped directly against `draft-v2-editor.md`, confirming `editor-report.md` §12's own claim: no
`ISO 8559` / `0.40 cm`, no `95%+`, no per-measurement girth figure (wrist 0.54 cm etc.), no `SOC 2`,
no pricing, no market sizing (`FX-010`), no `DEXA`, no `230,207` / `177,297` volume series, no
semaglutide ex-US-exclusivity angle, no KFF employer-coverage figure, no `33 million`, no `50-60%`
presented as typical, no "surgery is rebounding," no competitor name, no clinical outcome of
bariatric surgery (benefits, remission, side effects, complication rates). All of `plan-audit.md` §C
(deliberate omissions), §D (deletions ledger) and §N (what the article does not cover) hold in the
final draft.

**Keep ledger verified** (`plan-audit.md` §E): the four-stage workflow, the mechanism paragraph
("the scan does not determine whether a patient is medically eligible... what the scan supplies is a
structured, verifiable body-data signal the program uses to triage"), the patient-journey table, the
scope note and disclaimer verbatim, the compliance-posture paragraph (now expanded with FX-005 and
FX-006), the anti-manipulation paragraph with its hedging intact, and the operational-not-clinical
framing throughout. All present and unweakened in the final draft.

---

## 4. Open items carried forward to Vadim (not blockers, but not silent)

1. **Byline spelling.** `Assel Sekerova` throughout this workspace; the live site alternates between
   that spelling and `Asselya Sekerova` across other hub republishes (`published-articles-inventory.md`
   rows 8-10). Needs Vadim's call before this goes live; not resolved by this package on purpose (see
   `publish-package.md` §0.3).
2. **`external_claims:` schema gap.** The pack has no equivalent of `approved_claims:` for
   third-party statistics, which is why the 16 `ext-claim` HTML comments exist as scaffolding rather
   than resolving through the linter directly. Recommendation: add an `external_claims:` block to the
   context-pack schema and teach `context-pack-builder` to emit it. Every stats-heavy article hits
   this same gap (editor-report.md §11 item 1; carried here since it recurred on this article too).
3. **`sales@3dlook.ai` vs `@3dlook.me`.** The CTA in Section 12 uses the live page's existing address
   (`sales@3dlook.ai`), left unresolved by the editor pending someone with authority over the
   published contact address. Not changed in this package.
4. **CDC *Preventing Chronic Disease* wording** ("underestimated the prevalence of severe obesity by
   40%") is carried over from the live page's phrasing and was flagged by the plan for
   re-verification at fact-check; still open per the editor's report.
5. **No named bariatric customer story exists** anywhere in `case-studies/` or `proof-points.md`,
   unlike insurance, wellness and telehealth. Every operational claim on this page rests on a
   third-party citation or a disclosed internal limit. Not fixable at the publisher stage; flagged
   for whoever owns case-study sourcing.
6. **The primary keyword `bariatric pre-qualification` has zero measured US search volume**
   (`plan-audit.md` §K, Open Item #1). The page is planned and built as a BOFU/GEO/sales-enablement
   hub, not an organic-volume play. This is a strategic fact, not a defect in this package; Vadim
   should see it now rather than in Search Console in six months, per the same failure class as
   `remote-body-measurement-online-fitness-coaching` (2026-08-25).
7. **The mid-body eBook promo block is not restored.** Default per the plan was to flag rather than
   silently delete; restoring it (if Vadim wants it) is a one-paste addition and is not part of this
   package.
8. **Six of seven `DOWN-LINK LANDING` anchors have no live child to link to yet.** They are recorded
   as a table in `publish-package.md` §3b for whoever edits this hub next, once each P1/P2 child
   article ships.

None of these eight items is a ❌ on either checklist in `publish-package.md` §2. They are open
items for Vadim's visibility, not gates.

---

## 5. Status

`status: ready_for_review`. Per `project_mvb_publish_package_status.md`, the `approved_for_publish`
gate has never been reachable mechanically in this pipeline; the actual gate is Vadim's direct ask
for this refresh (already given, 2026-09-03) plus his approval of the text and meta together at this
checkpoint. This report and `publish-package.md` do not assert that approval has happened. Next step
is Vadim's review of `publish-package.md` (text + meta), after which he or a CMS operator publishes
manually, preserving `datePublished` at 2026-06-05 per the warning in that file's §0.2.
