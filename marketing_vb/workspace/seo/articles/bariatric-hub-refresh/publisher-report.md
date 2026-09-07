---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
artifact: publisher report (Review-1 rebuild)
role: seo-publisher
input: draft-v3-editor.md, review-1-decisions.md, review-1.md, editor-report-review-1.md, plan.md
prior_package: publish-package.md as it stood after the first pass (2026-09-03, from draft-v2-editor.md; snapshotted at v1/publish-package.md)
output: publish-package.md (rewritten in place)
created: 2026-09-07
revised: 2026-09-07
status: ready_for_review
stage: publish only — nothing sent to the CMS
qc_fix_pass: "2026-09-07 — corrects §3 item 4 (two deviations to three, G2) and open item 9 (G3 ruling); gate and detector numbers re-run against draft-v3-editor.md after the coordinator applied G1"
---

# Publisher report — Bariatric hub refresh, Review 1 rebuild

This is the **second** publisher report for this article. The first (`v1/publisher-report.md`)
documented the live-page-to-`draft-v2-editor.md` delta and is left untouched. This report documents
what changed in `publish-package.md` between that first pass and this rebuild, why, and what is
still open. It does not re-derive the live-vs-draft delta table — that ground did not move under
Review 1, and `v1/publisher-report.md` §2 is still the record of it.

**This is a fix pass on this same report**, applied 2026-09-07 after `quality-controller` scored the
package 17/20. Two things needed correcting: §3 item 4 understated the count of disclosed heading
deviations (two, not three — the coordinator's ruling **G2** is the third), and open item 9 was still
open when the coordinator had already ruled it (**G3**, allowed). Gate and detector figures in §1 are
also re-run, because the coordinator applied **G1** to `draft-v3-editor.md` between this report's
first version and this fix pass, which changed the word count and marker counts slightly.

---

## 1. Gate verification, re-run this session

**Without the context pack** (base mechanics):

```
$ python3 scripts/article_lint.py workspace/seo/articles/bariatric-hub-refresh/draft-v3-editor.md

[ok  ] hard bans (detect-ai-tells)          ai_density: 0.81, verdict: CLEAN, rhythm_variation: 0.57
[ok  ] prose length                          prose words 4387 vs target 4400 (band 3740-5060)
[ok  ] claim traceability                    claims_used: FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links                        links_total: 14, links_distinct: 7
[ok  ] keyword placement                     keyword: bariatric pre-qualification, occurrences: 6, h2_count: 10
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline                   accuracy_figures_present: True, links_to_framework: True

VERDICT: PASS
```

**Fix-pass rerun, this session, against `draft-v3-editor.md` as it now stands after the coordinator
applied G1.** Prose words 4,387 (was 4,413 in the report's first version) and AI density 0.81 (was
1.0) — both drops trace to G1 removing the duplicated ±3.5% passage from §5; `claims_used` is
unchanged (7 distinct ids, same as before) because the gate reports distinct ids, not occurrence
counts, so it never surfaced the duplicate `FX-008` marker in the first place (`publish-package.md`
§3a and §3h).

**With the context pack** (adds the link-direction breakdown):

```
$ python3 scripts/article_lint.py workspace/seo/articles/bariatric-hub-refresh/draft-v3-editor.md \
    --pack workspace/seo/_context-packs/2026-09-03-bariatric-hub-refresh.yaml --report

[ok  ] internal links   links_total: 14, links_distinct: 7, asset_urls: 0
                         directions: {'up': 1, 'sideways': 3, 'down': 1, 'trust': 1}
[ok  ] all other gates as above

approved but uncited: FX-003, FX-004, FX-010
VERDICT: PASS
```

**9 of 9 gates, both runs.** The `superseded figures` gate is the one that mattered here: it failed
on six `predicted weight` hits on the editor's first pass through this ruling, against a
`SUPERSEDED` row inherited from the wellness hub's Review 1. Per this task's own framing, that is
resolved and not re-litigated in this report: Vadim scoped the row to wellness copy on 2026-09-07,
the gate now passes cleanly, and `plan.md` writer note 6 ("No `predicted weight`") is overridden for
this page by decision B4.

**AI-tells detector, run directly, this session:**

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/bariatric-hub-refresh/draft-v3-editor.md --channel article --summary

SEO / blog article · en · 4953 words
AI density: 0.81/1000 (budget 6.0) -> low
VERDICT: CLEAN
TOP SOFT MARKERS:
  2x 'facilitated' (L135)
  2x 'rather than' (L183)
```

Fix-pass rerun. The word count (4,953, was 4,983) and AI density (0.81, was 1.0) are both lower than
the report's first version because G1 removed the duplicated ±3.5% passage and its `rather than`
clause from §5, not because the detector or the file's other content changed. `draft-v3-editor.md`'s
own frontmatter still says `ai_density_after: 1.0`, which is now stale against the body (the editor's
frontmatter was not re-run after the coordinator's direct edit); this session's number is the one
verified against the file on disk. The two `rather than` hits left are both in §6, the B4
product/accuracy-boundary sentences the decisions file explicitly forbids rewriting; the two
`facilitated` hits sit inside the proper noun *Federally Facilitated Exchange*.

**Additional independent checks, run directly against the file:**

```
$ grep -cP '[\x{2013}\x{2014}]' draft-v3-editor.md        -> 0   (zero em or en dashes)
$ grep -in "dexa" draft-v3-editor.md                       -> no match (DXA used throughout, never DEXA)
$ grep -c 'DOWN-LINK' draft-v3-editor.md                    -> 0   (all seven markers removed by the editor)
$ grep -o '<!-- ext-claim: [A-Za-z0-9_.-]*' ... | sort | uniq -c   -> 9 distinct ids, 13 markers
$ grep -o '<!-- claim: [A-Za-z0-9_.-]*' ... | sort | uniq -c       -> 7 distinct ids, 7 markers (was 8;
                                                                       G1 dropped the duplicate FX-008)
$ grep -n "positioned as" draft-v3-editor.md                -> 1 hit, the licensed medical-device sentence
$ grep -in "occupational-health\|insurance-underwriting\|wellness-rewards" draft-v3-editor.md  -> no match
```

---

## 2. What changed in `publish-package.md` between the two passes

This is the delta in the **package**, not in the article body (`editor-report-review-1.md` already
carries the full body-level B/C/D delta table against `draft-v2-editor.md`; this section does not
repeat it).

| Package section | First pass (from `draft-v2-editor.md`) | This rebuild (from `draft-v3-editor.md`) |
|---|---|---|
| §1 meta description | Led with the 7-day payer clock, 154 chars | Leads with four workflow nouns (pre-qualification, intake, pre-auth preparation, post-op tracking), 145 chars, D8 verbatim |
| §1 "Why this direction" | Argued the payer clock was "the single most important factual change on the page" | Rewritten: explains why that framing is now obsolete (B1 narrowed the clock claim itself) and why the reviewer's replacement is more durable |
| §1 meta title | 54 chars, keyword-first | **Unchanged** — D8 rules on the description only |
| §2 SEO checklist | 10 grouped items reported against a 15-item literal list, with a note about the mismatch | Re-derived, 15 items reported as 15, same mismatch-with-template note carried forward rather than re-litigated |
| §2 content-strategy checklist | 9/9, internal links `{up:1, sideways:6, down:1, trust:1}` | 9/9, internal links `{up:1, sideways:3, down:1, trust:1}` — the drop is D7, recorded explicitly so it is not read as regression |
| §3a marker table | 16 `ext-claim` / 10 distinct ids, 8 `claim:FX` (after two prior miscounts on the same draft) | 13 `ext-claim` / 9 distinct ids, 7 `claim:FX` / 7 distinct ids (post-G1 count; see §2a below) — recomputed fresh against the current file, not carried forward |
| §3b DOWN-LINK table | 7 rows mapping anchor sentences to 7 planned P1/P2 child articles | Empty — B6 removed all 7 anchors plus an 8th (privacy FAQ). Replaced with an explanation of what that means for future children (E2) rather than a stale table |
| §3c privacy FAQ note | Described the "not yet published" sentence in the live compliance bullet | Updated: that sentence is gone (B6), but the underlying "never link it" rule is unchanged |
| §3g (new) | Did not exist | New section recording that D7 removed two links the context pack marked "Already present — keep," so a CMS operator does not treat their absence as a defect |
| §3h-3j (new, this fix pass) | Did not exist | New sections recording G1 (resolved), G2 (disclosed) and G3 (allowed) — see §2a below |
| §4 image suggestions | Anchored to old section numbers (workflow at §6, comparison table at §7 or §10) | Anchored to new section numbers (workflow at §2, comparison/pilot tables at §7/§8) |
| §5 internal links table | 18 instances / 10 distinct targets / 6 sideways links | 14 instances / 7 distinct targets / 3 sideways links, rebuilt from a fresh grep against `draft-v3-editor.md`, not adjusted from the old table |
| §6 CMS-ready body | `draft-v2-editor.md` body, comments stripped | `draft-v3-editor.md` body, comments stripped — post-G1 as of this fix pass, so a different text from both the first-pass body and this table's own original entry |
| faq_branch (frontmatter) | `B (16 questions)` | `B, 9 questions` |
| Approval framing | Standard STOP block | Same STOP block plus an explicit note that any informal approval given before Review 1 does not carry forward, since the content changed substantively under B1-B7 |

### 2a. What this fix pass changed, on top of the table above

The table above documents the draft-v2-to-v3 rebuild and was accurate when first written. Two things
moved under it afterward, both from `review-1-decisions.md` §G (the coordinator's rulings on QC's
17/20 report), and this subsection records the delta rather than silently editing the table's history:

- **G1 edited `draft-v3-editor.md` itself** (the coordinator's direct edit, 2026-09-07), removing the
  duplicated ±3.5% passage from §5. That changed the file the table's right-hand column describes:
  prose words 4,413 to 4,387, the `claim:FX` count 8 to 7 (one `FX-008` marker instead of two), the
  total comment-marker count 21 to 20, and the body's `rather than` count 3 to 2. §1 above is the
  fresh rerun; `publish-package.md` §3a and §3h carry the full recount.
- **Three self-verification errors in the pre-fix `publish-package.md`** are corrected in this same
  fix pass: an external-citation breakdown that listed ASMBS ×3 against a real count of ×2, a meta
  rationale that rested on a false claim about where the product name first appears in the body
  (corrected to point at §2 Stage 1), and a marker-count reconciliation that did not add up to its own
  stated total. None of these three touched the shipped article body; all three were in the package's
  own explanatory prose.

---

## 3. Conflicts found, and how each resolved

The task asked specifically what conflicts turned up between the decisions file and what is actually
in the draft. Four came up during this rebuild; none blocked the package. **Item 4 is corrected in
this fix pass** (three deviations, not two — QC's own finding at 17/20; see below).

1. **The decisions file corrects its own arithmetic mid-paragraph (D6).** Its opening sentence says
   "Sixteen questions go to nine," then a parenthetical admits "the ruling first said eight," then
   states "the explicit remove-list below names seven of the sixteen, which leaves nine. The list
   governs." This is not a conflict between the decisions file and the draft — the draft (9 FAQ
   questions, verified directly: 9 bolded question lines across 3 H3 blocks) matches the list, not
   the stray "eight." It is a conflict the decisions file resolved against itself, and the editor
   followed the resolution correctly. Recording it here because a careless read of just the opening
   sentence would flag a mismatch that is not real.

2. **`predicted weight` — resolved before this session, not re-opened here.** The `SUPERSEDED` lint
   row that blocked the editor's first pass was scoped by Vadim to wellness copy on 2026-09-07, per
   this task's explicit instruction not to re-litigate it. Recorded as a conflict that existed and
   is now closed, not as an open item.

3. **D7 overrides a live `plan.md` / context-pack instruction, not just a stale draft.** `plan.md`
   lines 764-765 mark the insurance-underwriting and wellness-rewards links "Already present, keep"
   and mark the occupational-health link a "GAP" the plan wanted filled. D7 removes all three anyway.
   This is not an error in either file — `review-1-decisions.md` D7 states outright that it
   "knowingly drops two live internal links... record it... so nobody restores it." But it means
   `plan.md`'s own internal-links table is now stale on this specific point, and nothing in this
   pipeline updates `plan.md` automatically when a later review overrides it. Flagged in
   `publish-package.md` §3g so the override is visible at CMS-entry time, not just in this report.

4. **Three mechanical/wording deviations from the reviewer's literal text — corrected count, this
   fix pass.** This report's first version said "two," re-verifying only the §3 heading; QC's 17/20
   review found a third, undisclosed until the coordinator's ruling **G2**. All three:
   - §3 H2 — Title Case to sentence case, because `detect-ai-tells.py` bans Title-Case H2s (a
     house-rule lint failure).
   - §3 H2 — "bariatric" added, because lint gate 7 requires the exact primary keyword in at least
     one H2. The reviewer's proposed §3 wording omits it.
   - §6 H2 — "repeatability" dropped from the reviewer's proposed wording ("outputs, accuracy,
     repeatability and limitations" to "outputs, accuracy and limitations"). Undisclosed by the
     editor and not caught by this report's first version; **ruled correct and disclosed by G2**,
     2026-09-07 — the repeatability figure lives in §5, not §6, so the shipped heading matches what
     the section actually delivers.

   The first two are formatting/mechanical conformances the decisions file's own house style
   principle (B1b) anticipates ("style, not content"). The third is a small content-shaped change
   (a heading promising less than the reviewer's literal wording) that needed a ruling rather than a
   style-exception, and now has one. Confirmed by reading all three headings directly against
   `review-1.md`'s and `review-1-decisions.md` §C's proposed wording.

No conflict found rose to the level of contradicting a **ruling** (as opposed to a stale downstream
artifact, an internal arithmetic slip, or an undisclosed-but-now-ruled deviation). Nothing here
changed what shipped in `publish-package.md` §6 beyond G1 (§2a above) — the three heading deviations
are explanatory notes about existing text, not new corrections to the body.

---

## 4. Open items carried forward to Vadim (not blockers)

Re-derived against the current state, not copied from the first report. Items resolved by Review 1
are marked closed rather than dropped silently, so the history is visible.

1. **`external_claims:` schema gap — still open.** The context pack has no equivalent of
   `approved_claims:` for third-party statistics; the `ext-claim` comments remain scaffolding.
   Recommendation unchanged: add an `external_claims:` block to the schema.
2. **`sales@3dlook.ai` vs `@3dlook.me` — still open.** §10's CTA still uses the live page's existing
   address. Not touched by Review 1, not resolved by this rebuild.
3. **No named bariatric customer story — still open.** Every operational claim still rests on a
   third-party citation or a disclosed internal limit. Not fixable at the publisher stage.
4. **Zero measured US search volume for the primary keyword — still open, unchanged fact.** The page
   remains a BOFU/GEO/sales-enablement play by design, not an organic-volume play.
5. **The mid-body eBook promo block is still not restored — still open, untouched by Review 1.**
6. ~~**Byline spelling.**~~ **Closed 2026-09-03**, before Review 1. `Assel Sekerova` throughout.
7. ~~**CDC *Preventing Chronic Disease* wording.**~~ **Closed by Review 1's B5 carve-out.** The
   reviewer explicitly confirmed the sentence is correct as written and ordered it left untouched;
   what changed is only the inference drawn from it in the next sentence, which is gone.
8. **New: curated internal links now 7 distinct, against `plan.md`'s 8-11 target — not a defect.**
   D7 removed three links deliberately; the plan's numeric target predates that ruling. All four
   link directions are still covered. Surfaced here so Vadim sees the count moved, not just that the
   checklist still passes.
9. **"Consult-to-procedure conversion" survives once, in §7's buyer-fit paragraph, as a metric
   directors are accountable for. Ruled allowed, 2026-09-07 (G3) — corrected from "open" to
   "decided."** B5 removed the claim that the *product* raises this metric (the Use Case Summary
   Business-value row); naming it as something a director's role owns is a different, narrower
   statement, and the coordinator's ruling confirms that is the distinction B5 draws. Kept as
   written. Still listed here, per G3's own instruction, so the next reviewer sees a decision rather
   than a leftover — see `publish-package.md` §3j for the full ruling.
10. **New: D7's occupational-health removal reverses a `plan.md` "GAP" instruction, not just a
    "keep."** See conflict #3 above. `plan.md` itself is not corrected by this rebuild — that would
    be an edit to a synced planning artifact, which is out of scope for a `publish`-stage pass — but
    the override is recorded in `publish-package.md` §3g so it does not get silently re-applied.
11. **Any P1 child article that ships later (pre-authorization documentation guide, patient progress
    record guide, hybrid care guide) will need to find its own anchor point.** B6 removed the
    sentences that used to reserve one. Not a defect in this rebuild; a note for whoever writes that
    next article.
12. ~~**The ±3.5% passage shipped twice, in §5 and §6, with the package silent about it.**~~
    **Closed 2026-09-07, ruling G1.** QC's top issue at 17/20: the editor's own report flagged this
    for a coordinator ruling and it reached neither the pre-fix `publish-package.md` nor this report's
    §4. The coordinator applied G1 directly to `draft-v3-editor.md`; the figure now ships once, in
    §6. Full record in `publish-package.md` §3h.
13. ~~**§6's heading drops "repeatability" from the reviewer's proposed wording, undisclosed.**~~
    **Closed 2026-09-07, ruling G2.** Kept as shipped; disclosed and approved rather than reverted.
    Full record in `publish-package.md` §3i and §3 item 4 above (now three deviations, not two).

None of these thirteen items is a ❌ on either checklist in `publish-package.md` §2. Items 12 and 13
are closed, kept here (struck through) rather than dropped silently, matching how item 6 and item 7
are handled above. The rest are open items for Vadim's visibility, not gates.

---

## 5. Status

`status: ready_for_review`. Per `project_mvb_publish_package_status.md`, the `approved_for_publish`
gate has never been reachable mechanically in this pipeline; the actual gate is Vadim's approval of
the text and meta together. **Any approval given informally on the first package does not carry
forward** — the body changed substantively under decisions B1 through B7, C and D, so this is a
fresh checkpoint, not a resumption of the prior one. This fix pass changes the body once more (G1,
§2a and §3h above) and corrects the package's own prose (the three self-verification slips QC's
17/20 report located at pkg :231, :120 and :342 of the pre-fix package) but does not reopen anything
B1-B7, C or D settled. Next step is Vadim's review of `publish-package.md` (text + meta), after which
he or a CMS operator publishes manually, re-dating `datePublished` per §0.2 of that file.
