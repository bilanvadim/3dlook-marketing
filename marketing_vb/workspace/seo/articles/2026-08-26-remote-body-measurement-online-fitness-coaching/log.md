# Log — remote-body-measurement-online-fitness-coaching

## 2026-08-26 — Write stage completed (seo-writer)

- **Artifact:** `draft-v1.md` (full article, 12-section outline per plan.md, H2.1–H2.12 + short intro + scope note).
- **Word count:** ~2,680 (approximate).
- **Author byline:** Assel Sekerova (default).
- **Claims used:** FX-001, FX-002, FX-003, FX-005, FX-006, FX-007, FX-008. FX-004 (ISO 8559-1:2017 benchmark) deliberately NOT used — plan did not call for it and it must never be combined with FX-001/003 (different reference method).
- **Internal links placed:**
  - up → AI in Fitness hub (`/content-hub/ai-in-fitness-industry/`) in H2.3.
  - trust → accuracy framework (`/content-hub/mobile-body-scanning-accuracy/`) in H2.2 and H2.10.
  - down → BOFU product page (`/fitxpress/for-connected-and-digital-fitness/`) as soft MOFU evaluation link after H2.6 and as direct BOFU CTA in the conclusion.
  - sideways → **omitted** (see open items #3 below).
- **Self-check (grep):** no em dash, no banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/etc.), no "positioned as", no "by hand", no "objective" about our tech, no named competitors, no banned claims. The only matches for diagnose/eligibility/underwriting terms are inside the boundary section (H2.7), the scope note, and the reframe contrast in H2.2 — all correct usages, no asserted claims.

### Deviations / open items flagged for review

1. **Word count vs plan estimate (deviation).** plan.md article-meta estimates ~2,000 (range 1,900–2,300) and asks for the shorter end, but the sum of the per-section word-count targets in the outline is ~2,970 (mins) to ~4,130 (maxes). The two figures are arithmetically incompatible. I prioritized the per-section must-cover depth and wrote toward the lower end of each section, landing ~2,680. This is above the stated ~2,300 ceiling but below the section-target sum, and still within the corpus norm (blog-style-guide §2 floor is 2,000). Editor/Vadim to confirm whether to trim toward 2,300 (would require dropping must-cover content) or accept ~2,680.
2. **Difficulty is TBD** for the head term (Ahrefs returned null) — carried from plan Open items #2, unchanged at write stage.
3. **Sideways internal link omitted.** Per plan Open items #6 and the vertical-boundary guardrail, the only live sideways candidate is the GLP-1 tools list (different vertical). I did not link it to avoid blurring the Fitness/GLP-1 boundary. Article ships with up/down/trust links only. Confirm whether to hold a slot for the planned "Smart Scale vs AI Body Scan" / "GLP-1 and Fitness Apps" siblings once written.
4. **No named fitness-coaching customer** exists in proof-points (plan Open items #3). Draft uses capability + segment framing with no named customer, as planned.
5. **BOFU URL path debt** (plan Open items #4): `/fitxpress/for-connected-and-digital-fitness/` is flagged in CLAUDE.md §16 as using a non-existent path level with a redirect breadcrumb. URL kept as written in content-plan.md/plan.md; confirm canonical URL before publish.
6. **Central Privacy/Regulatory FAQ not live** (plan Open items #5): privacy handled as a short practical note (H2.5, H2.10, FAQ #6); no dead link inserted.

### Next step
Draft ready for `seo-editor` (Pass 3b strategy compliance, Pass 3c detector, Pass 4 terminology-guardrails full pass).

## 2026-08-26 — Edit stage completed (seo-editor)

- **Artifact:** `draft-v2-final.md` (edited, status: edited). Feeds directly to publish (no checkpoint between edit and publish).
- **Body word count:** ~2,525 prose words (2,599 from H1 to end minus 72 claim-comment tokens; frontmatter `word_count: 2525`). Down from v1's ~2,640 prose.
- **detect-ai-tells.py (channel article), actual final output:**
  `SEO / blog article · en · 2646 words / AI density: 0.0/1000 (budget 6.0) -> low / VERDICT: CLEAN`
  (baseline on draft-v1 was `1.08/1000`, VERDICT `HARD FAILS (1)` — anthropomorphism "platform decides").

### Pass-by-pass

- **Pass 1 — citation dedup.** The accuracy-framework trust link (`/content-hub/mobile-body-scanning-accuracy/`) was linked twice in v1 (H2.2 and H2.10). Kept one anchor in H2.2; H2.10 now says "as the accuracy framework sets out" without re-linking (also avoids the positional "linked above"). BOFU down-link kept in two spots (H2.6 soft MOFU eval + conclusion BOFU demo) — plan-sanctioned CTA placement, not a dup. Verified link inventory: up ×1, trust ×1, down ×2.
- **Pass 2 — structure & flow.** Intro already lands the pain in two sentences; wove the primary keyword into the second intro sentence and into the H2.1 heading so it appears in H1 + first paragraph + one H2 + body (4 occurrences total). No Furthermore/Moreover/Additionally transitions. Conclusion is actionable (next step + two CTAs).
- **Pass 3 — expert voice.** Fixed the anthropomorphism hard fail ("the platform decides" -> "the platform team decides how to use it"). Converted H2.6 from a bold-headed checklist to prose so it no longer clones H2.10's checklist (two identical lists back-to-back was the main "template" tell). Removed ungrammatical keyword-stuffed phrases ("client retention online coaching", "visible progress coaching", "body composition tracking for coaching") and rewrote naturally. Kept/sharpened the stated positions (the "accurate enough for which decision?" reframe; the "not the right tool for every practice" call).
- **Pass 3b — strategy compliance.** No banned positioning claim; boundary section H2.7 present and direct. Vertical boundary held (GLP-1 appears only inside the boundary statement; no wellness-rewards bleed). Narrow coaching-workflow angle held (no hub-overview duplication). Internal links up/down/trust present; sideways deliberately omitted (plan Open item #6, avoids Fitness/GLP-1 boundary blur). FAQ (7 items) intact; CTA-by-intent (MOFU eval + BOFU demo) intact.
- **Pass 3c — detector + self-check.** Ran the detector twice mid-edit (caught a fresh anthropomorphism "body data feels current" introduced by a trim, rewrote it), final run CLEAN 0.0/1000. Self-check written into the artifact `self_check` field.
- **Pass 4 — terminology & polish.** Expanded BMR, CTO, HIPAA, GDPR, and SSE-S3 at first use (matching the house convention in `online-pharmacy-bmi-verification.md`); BMI kept bare per the 2026-08-25 override. Removed two "so"-as-result connectors in H2.6. Removed corrective negations: the "with real clients, not staff" line (-> "under real conditions"), the "is noise, not progress" line (-> positive "only a larger move should read as progress"), the "repeatability, not one-off variation" line (-> "base thresholds on measurement repeatability"), and the FX-006 "software estimate, not a reading from a physical scale" clause (-> "a software output read from the images"). Split the one stacked negation in H2.7 (GLP-1 + qualification) into a positive frame for the qualification half. Removed em dashes from the frontmatter notes as well (body had none).

### Verification (all pass)
- No claim outside the approved list: only FX-001, FX-002, FX-003, FX-005, FX-006, FX-007, FX-008 used.
- **FX-004 absent** (grep for ISO 8559 / 0.40 cm / multi-company / 14 companies / 1,152 all negative) — not combined with FX-001/003.
- **Repeatability written as "< 1 cm"** in all 4 occurrences.
- **No named competitors** (Prism / Bodygram / Size Stream all absent).
- **Vertical boundary held** — no GLP-1-clinical or wellness-rewards claims outside the boundary statement.
- **"FitXpress is not a medical device"** stated directly (scope note + H2.7), never "positioned as".
- Internal links correct per context-pack: up (`/content-hub/ai-in-fitness-industry/`), trust (`/content-hub/mobile-body-scanning-accuracy/`), down (`/fitxpress/for-connected-and-digital-fitness/` ×2).
- Zero em dashes; zero banned words; no "positioned as" / "by hand" / "plus"-stacking / "objective"-about-our-tech / "so"-as-result-connector in the body.

### Open items carried to publish
1. **Word count vs plan ceiling (editorial call, resolved toward quality).** Final body ~2,525 prose words. This sits inside the context-pack's stated "1,800-2,800 typical for a P1 supporting article in this hub" band, and modestly above the plan's soft 2,300 ceiling. Trimmed ~115 prose words from v1 (duplicated retention/recomposition + a redundant privacy line) without cutting any FAQ item, the boundary section, or any approved claim. Held here deliberately rather than stripping must-cover content, per the writer's flagged plan/section arithmetic conflict (open item #1 above). Publisher/Vadim can request a further trim to <=2,300 if the plan ceiling is hard, but it would mean cutting must-cover depth.
2. **BOFU URL path debt** (plan Open item #4): `/fitxpress/for-connected-and-digital-fitness/` flagged in CLAUDE.md §16 as a non-existent path level with a redirect breadcrumb. URL kept as written in content-plan.md; **confirm the canonical down-link URL before publish.**
3. **Central Privacy/Regulatory FAQ not live** (plan Open item #5): privacy kept as a short practical note (H2.5 + H2.10 + FAQ), no dead link inserted.
4. **Sideways internal link still omitted** (plan Open item #6): ships with up/down/trust only; hold a slot for the planned "Smart Scale vs AI Body Scan" / "GLP-1 and Fitness Apps" siblings once written.
5. **Head-term difficulty still TBD** (plan Open item #2): Ahrefs returned null; unchanged at edit stage.

### Next step
`draft-v2-final.md` ready for `seo-publisher` (meta generation + final checklist, incl. its own detector re-run and the BOFU-URL confirmation).

## 2026-08-26 — Publish stage completed (seo-publisher)

- **Artifact:** `publish-package.md` — meta title/description (3 variants each), full 15-point SEO checklist,
  9-point strategy checklist, all open items carried forward explicitly, alt-image suggestions, full CMS-ready
  article body.
- **detect-ai-tells.py re-run by me, not cited from the editor.** Ran
  `python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/draft-v2-final.md --channel article --summary`
  directly via Bash (no permission issue — the `settings.json` fix from earlier on 2026-08-26 held).
  Result: `2646 words · AI density 0.0/1000 (budget 6.0) -> low · VERDICT: CLEAN`. Also ran the non-summary
  JSON form: `hard_fails: [], house_rule_violations: [], em_dashes: 0, punch_triad_count: 0`. This confirms
  the editor's Pass 3c number rather than assuming it carries over.
- **Recommended meta title (57 chars):** "Online Fitness Coaching Programs: Remote Body Measurement" —
  front-loads the actual SEO head term (100/mo, US); 2 alt variants provided, including the exact
  content-plan.md/H1 phrasing as an option if title/H1 consistency is preferred over front-loading.
- **Recommended meta description (154 chars):** "Coaches can't tape-measure remote clients. See how a
  guided smartphone scan gives online fitness coaching programs structured progress data clients trust."
  2 alt variants provided.
- **SEO checklist: 14/15 pass.** One flagged deviation: word count (2,525 prose words vs plan's stated
  ~2,000/1,900-2,300 estimate) — already an editorial call documented by writer and editor, not newly
  discovered, carried forward explicitly rather than silently accepted.
- **Strategy checklist: 8/9 pass.** One flagged deviation: sideways internal link omitted (deliberate,
  to avoid a Fitness/GLP-1 vertical-boundary blur — the only live sideways candidate is off-vertical and
  the two planned siblings are not yet written).
- **No STOP triggered.** Two single-item deviations across two separate checklists, both below the ≥2-❌
  threshold per checklist, neither in the positioning/compliance/cannibalization auto-stop category.
- **Zero third-party/external sources confirmed** — all 4 links are internal `3dlook.ai` URLs (up, trust,
  down ×2). Flagged explicitly per the 2026-08-26 CLAUDE.md finding that this caps quality-controller's
  category B score, so it reads as a declared fact rather than an oversight if `quality-controller` runs
  on this package next.
- **All open items from the write/edit stages carried forward verbatim** into publish-package.md §4: word
  count vs ceiling, BOFU URL path debt (`/fitxpress/for-connected-and-digital-fitness/`, CLAUDE.md §16),
  sideways link omission, central Privacy/Regulatory FAQ not live, head-term difficulty TBD, thin-demand
  checkpoint-1 decision, zero external sources. The TBD dependency is declared in the package itself, per
  the 2026-08-26 CLAUDE.md note that an undeclared TBD caps quality-controller's category A score.
- **Minor judgment-call note, not a fail:** one residual "so" in the Implementation section (capture-
  protocol bullet) reads as an imperative recommendation following a claim, not the detector's narrowly-
  scoped benefit shape. Flagged for editorial awareness in publish-package.md §2, not treated as a hard
  fail since the mechanical detector correctly did not flag it.

### Status
Article is now at **checkpoint 2** — text + meta together, awaiting Vadim's approval in Telegram. No
further pipeline action until that approval; publishing to the CMS is manual (Vadim or via API), per
CLAUDE.md §10.

## 2026-08-31 — Revision 1 (seo-editor)

External editorial review arrived on the published-ready text (`review1-comments.md`, 8 numbered priority
recommendations, verbatim from the Review 1 tab). This was a revision round on `draft-v2-final.md`, run on
the pattern set by `workspace/seo/articles/glp-1-market-hub/` (review1-comments → draft-v5-revision1 →
changelog-revision1).

- **Artifacts written:** `draft-v3-revision1.md` (status `revision1`, date 2026-08-31,
  `review_source: review1-comments.md`, inline `<!-- claim: FX-00X -->` markers kept on every claim
  sentence) and `changelog-revision1.md` (item-by-item 1-8, plus "not applied / applied differently" and a
  claim-wording block for approval). `publish-package.md`, `draft-v1.md`, `draft-v2-final.md` and the
  `review1-*.md` files were not touched; the publisher runs after this.
- **Word count:** 2,582 prose words (H1 to end, HTML comments and table markup rows excluded), 2,839
  including tables, 3,015 as the detector counts. Previous version: 2,525 prose. Round target was
  2,300-2,600, so the long-running "word count vs plan's 2,300 ceiling" open item is now closed by the
  review itself: the review cut one section and added two blocks, and the reviewer set the shape.
- **detect-ai-tells.py (channel article), run by me on this output:**
  `SEO / blog article · en · 3015 words / AI density: 0.0/1000 (budget 6.0) -> low / VERDICT: CLEAN`
  JSON form: `hard_fails: []`, `house_rule_violations: []`, `markers_by_category: {}`, `em_dashes: 0`,
  `punch_triad_count: 0`, sentence-length variation 0.48 (monotone threshold 0.35). CLEAN on the first
  run; two soft slips found by my own second pass (a `so`-as-result connector introduced while drafting,
  and a "the number that decides" anthropomorphism the detector does not match) were fixed and the
  detector re-run.

### What each review item changed

1. **Differentiation.** `## Why this matters now` deleted outright, with the retention-economics and
   CAC framing removed rather than relocated. The AI-in-fitness hub up-link survives as one clause in the
   intro. No fitness-industry or market-trend prose left in the body.
2. **Order.** Rebuilt to the reviewer's 12-part sequence exactly, including moving `Where FitXpress fits`
   from position 5 to 7. `What improves operationally` disappeared as a section (content redistributed or
   dropped); `What FitXpress does not do` became an H3 inside section 10, the limitations section.
3. **Claim precision.** Five output classes separated; `±3.5%` replaced with "approximately 3.5% average
   prediction error under evaluated conditions"; the broad repeatability line replaced with the reviewer's
   exact sentence; 96-97% and 1.5-2.0 cm attributed to internal validation against expert manual
   measurements; weight no longer a universally required input and age dropped from the input list; DXA
   everywhere with one expansion, zero `DEXA`; privacy wording aligned to the live policy.
4. **Unsupported commercial claims.** All six flagged sentences deleted. Retention and engagement now
   appear only as things a pilot measures against a baseline (three places, all measurement framing).
5. **Decision value.** New section 5 with the reviewer's 4-row coaching-stage table, and new section 9
   with the seven pilot metrics as process measures.
6. **Method comparison.** Table rebuilt 5 rows to 7: consumer smart scale split from professional BIA, DXA
   row added, "one number" framing gone, complementary framing in the prose and in the FAQ.
7. **Repetition.** 80+, under 45 seconds, the repeatability sentence, privacy/deletion and who-decides now
   sit at exactly one body instance plus one FAQ instance each (grep counts in the changelog).
8. **Tone.** All five flagged lines removed or rewritten, with no new punchy assertions substituted.

### Open items for Vadim (this round)

1. **Which document wins on medical framing.** The review asks for "FitXpress is not positioned as a
   medical device." `brand-assets/content-strategy/terminology-guardrails.md` (Asselya's Doc, modified
   2026-08-13, synced 2026-08-25) bans "positioned as" for product/intended-use/regulatory statements in
   Part 2 §2.10 and records in its Overrides table that it **supersedes** `editorial-guardrails.md` #6,
   which is where the reviewer's wording came from. The detector treats `not positioned as` as a hard
   fail. The article therefore keeps **"FitXpress is not a medical device."** Vadim/Asselya to settle the
   conflict at source so the next reviewer and the next agent read the same rule.
2. **FX-007 wording, two changes needing approval.** (a) SSE-S3 and Amazon Simple Storage Service removed
   from the body in favour of "encrypted in transit and at rest on Amazon Web Services (AWS)
   infrastructure", because the public privacy policy (verified 2026-08-31) does not state SSE-S3;
   `context-pack.md` FX-007 still names it. (b) "Retained photos are automatically blurred." added, from
   the policy, carrying an inline source comment.
3. **Repeatability convention.** `about-me.md` locks repeatability as `< 1 cm`; the reviewer's mandated
   sentence spells it "less than 1 cm", which is what shipped (same call as the GLP-1 hub revision). If
   the locked convention is to win, reconcile the two documents rather than per article.
4. **The older `ai-body-scanning-for-fitness` page.** Review item 1 suggests redirecting or rescoping it.
   Out of scope here; needs a separate content-ops decision.
5. **Still no named coaching customer** (carried from plan Open items #3). Capability and segment framing
   only, no invented outcome.
6. **BOFU URL path debt still open** (carried): `/fitxpress/for-connected-and-digital-fitness/` is flagged
   in CLAUDE.md §16 as using a path level that does not exist. Linked twice in this revision as written in
   `content-plan.md`. Confirm the canonical URL before publish.
7. **Head-term difficulty still TBD** (carried from plan Open items #2): Ahrefs returned null.

### Closed by this round

- **Sideways internal link omitted** (plan #6, write #3, edit #4, publish): closed. Review item 6 requires
  the `body-scanning-technology-comparison` link, and the target is a technology comparison in the same
  product family, so the Fitness/GLP-1 boundary concern that drove the omission does not apply.
- **Central Privacy/Regulatory FAQ not live** (plan #5): still not live, but the privacy content is now
  verified against the public privacy policy instead of standing on an internal note alone, so the missing
  hub is no longer the only backing for the section.
- **Word count vs the plan's 2,300 soft ceiling** (edit #1): superseded by the review's own target shape.
- **Zero external sources** (publish-stage flag): unchanged. All five links are internal. The article's
  factual load is product claims and one privacy policy, and no external authority was added in this
  round; `quality-controller` will still cap category B on that basis.

### Next step

`draft-v3-revision1.md` goes to `seo-publisher` for meta regeneration against the new structure (the
recommended meta description in `publish-package.md` still describes the old text) and the final
checklist, including its own detector re-run and the BOFU-URL confirmation.

## 2026-08-31 — Publish stage re-run (seo-publisher)

Second pass at checkpoint 2, run against `draft-v3-revision1.md` after the external review round. The
2026-08-26 package was built on `draft-v2-final.md`, whose structure no longer exists, and its recommended
meta description leaned on the tape-measure hook plus "progress data clients trust", which is the kind of
audience-reaction promise review item 4 removed from the body.

- **Files written:** `publish-package.md` (rewritten from `draft-v3-revision1.md`) and
  `publish-package-v1-20260826.md` (plain `cp` of the old package before the rewrite, md5-verified
  identical, not edited). `draft-v3-revision1.md`, `changelog-revision1.md`, `review1-comments.md`,
  `review1-version1.md`, `draft-v1.md` and `draft-v2-final.md` were not touched.
- **detect-ai-tells.py, run by me on the new draft** (both forms, exit 0 both times, no permission prompt):
  `SEO / blog article · en · 3015 words / AI density: 0.0/1000 (budget 6.0) -> low /
  VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.`
  JSON: `ai_density_per_1000_words: 0.0`, `severity: "low"`, `hard_fails: []`,
  `house_rule_violations: []`, `markers_by_category: {}`, `top_offenders: []`, `em_dashes: 0`,
  `punch_triad_count: 0`, rhythm variation 0.48 (monotone threshold 0.35). The editor's number is
  confirmed by measurement, not carried over.
- **Recommended meta title (57 chars):** "Online Fitness Coaching Programs: Remote Body Measurement".
  Head term at character 1. No brand suffix (only allowed at 49 chars or fewer without it).
- **Recommended meta description (146 chars):** "Online fitness coaching programs can capture client body
  data from a guided phone scan. See how it fits check-ins and what a pilot should measure." Head term
  front-loaded, points at the two blocks the review added (check-in fit, pilot measurement), and promises
  no engagement or retention outcome. Both alternates avoid the deleted retention framing as well.
- **SEO checklist: 14/15.** One ❌: word count. 2,584 prose words (2,916 with tables, 3,015 as the detector
  tokenizes) against `plan.md`'s "~2,000 (range 1,900-2,300)". Inside the context-pack's 1,800-2,800 band
  and inside the revision round's own 2,300-2,600 target, outside plus-or-minus 10 percent of the recorded
  plan target. Marked ❌ against the literal rule rather than re-defining the target, same call the
  2026-08-26 package made at 2,525 words; what changed is that the reviewer deleted one section and
  required two new ones, so the plan estimate no longer describes the commissioned article.
- **Strategy checklist: 9/9.** The 2026-08-26 ❌ (sideways internal link missing) is closed by review item 6:
  `body-scanning-technology-comparison` is now linked, so all four directions are present (up ×1,
  sideways ×1, trust ×1, down ×2, verified by URL count).
- **No STOP.** One ❌ in one checklist, below the 2-or-more threshold, and not in the positioning,
  compliance or cannibalization category. Nothing goes back to `seo-editor`; what blocks publish is six
  decisions for Vadim, not text quality.
- **Verified mechanically, not assumed:** heading order matches the reviewer's 12-part sequence exactly
  (intro + scope, measurement problem, what it provides, workflow, how coaches use results, comparison,
  where FitXpress fits, accuracy/repeatability/privacy/implementation with three H3s, pilot, best-fit and
  limitations with the boundary H3, FAQs, conclusion); each of the five deduplicated claims is 1 body + 1
  FAQ (`80+`, `under 45 seconds`, `less than 1 cm`, privacy/`30 days`, who-decides; `1.5 to 2.0 cm` also
  1+1); zero `DEXA`, zero `±`, zero em dashes, zero `positioned as`, zero `so` (any occurrence), zero
  banned words, zero `we/our/you`, FX-004 absent, no named competitors; primary keyword in H1, intro
  paragraph 1 and one H2; 7 FAQ answers at 2-3 sentences each.
- **Privacy claims independently re-verified.** I fetched `https://3dlook.ai/fitxpress-privacy-policy/`
  myself rather than trusting the editor's "verified 2026-08-31" note. Deletion/30-day retention, automatic
  blurring of retained photos, and encryption in transit and at rest are all supported verbatim. `SSE-S3`
  is absent from the policy, which confirms why it was dropped. "on AWS infrastructure" is supported by
  composing two policy statements (hosting on "a leading cloud infrastructure provider" plus the AWS
  sub-processor row), not by one sentence. **New finding: HIPAA is not mentioned anywhere in the public
  policy** (GDPR and CCPA are), so the article's HIPAA sentence rests on FX-007 alone.
- **Six decision items for Vadim before publish** (package section 4A, all carried verbatim from their
  sources): (1) which document wins on medical-device framing, review's "not positioned as" vs the
  `terminology-guardrails.md` ban that the article follows; (2) FX-007 wording, SSE-S3 out and automatic
  blurring in, approving means updating `context-pack.md` FX-007 and CLAUDE.md section 12; (3) confirm the
  canonical BOFU URL `/fitxpress/for-connected-and-digital-fitness/`, linked twice; (4) redirect or rescope
  the older `ai-body-scanning-for-fitness` page, a separate content-ops task on that URL; (5) repeatability
  convention `< 1 cm` (`about-me.md`) vs the reviewer's "less than 1 cm" that shipped; (6) FX-006 wording,
  the `±` is gone from the article and still in the claim record.
- **Nine informational items carried forward** (package section 4B), including word count, difficulty TBD,
  thin demand (100/mo), no named coaching customer, zero third-party sources (caps `quality-controller`
  category B), the privacy FAQ hub still not live, the boundary section now sitting at H3, and the
  BIA/DXA-expanded-under-the-heading nuance. Seven items recorded as closed (package section 4C) so they do
  not get reopened.
- **Two judgment calls surfaced rather than buried:** a three-clause sentence in intro paragraph 2 that the
  detector correctly does not treat as a punch triad, and the fact that BIA and DXA first appear inside the
  reviewer's verbatim heading.
- **CMS-ready body** is in package section 7: frontmatter removed, all `<!-- claim: -->` and
  `<!-- source: -->` annotations stripped, everything else byte-identical to the approved draft (verified
  by diff against a mechanically stripped copy).

### Status

Back at **checkpoint 2**, awaiting Vadim's approval of text plus meta together, and answers to the six
decision items. No pipeline action until then. Publishing to the CMS stays manual (CLAUDE.md section 10).
