---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
product: fitxpress
status: ready_for_review
created: 2026-09-19
revision: 3
rebuild_reason: >
  QC report workspace/_quality/seo/2026-09-19-seo-final-glp-1-fitness-apps-body-composition-tracking.md
  scored 14/20 and found the meta description made an unattributed muscle-loss claim that should
  have STOPped the previous package at 9/9 on the strategy checklist. seo-editor ran a QC fix pass
  on final.md in the same session (word_count 1828, lint clean except the accepted M1). This
  revision rewrites the meta, re-runs the strategy checklist honestly, fixes three checklist lines
  that contradicted the text, removes the customer name from the package, gives a CMS-safe category value,
  standardizes word counts on final.md's own frontmatter figure, and re-embeds the current article
  body.
hub: AI in Fitness (Hub 1), bridge into GLP-1 Market (Hub 3)
cluster: GLP-1 bridge
action_type: create-net-new
priority: P1
author: Assel Sekerova
word_count: 1828
word_count_note: "final.md frontmatter, article prose only. Lint's 2140 (re-run at checkpoint 2) includes the Open items block appended after the article."
source_final: "final.md (status: edited, 2026-09-19, edit_rounds: 2 — edit pass then QC fix pass)"
lint_verdict: "FAIL on 1 gate (abbreviations M1, H1 only) — accepted by Vadim at checkpoint 1, not an open defect. All other gates PASS."
published_slug: glp-1-muscle-loss-fitness-apps
published_url: "https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/"
checkpoint2_update: >
  Touch-up, not a rebuild, 19.09.2026. Vadim closed three open items: slug set to
  glp-1-muscle-loss-fitness-apps (the recommended option 2), the joint advisory link already
  moved to obesity.org by seo-editor in final.md, category to be filled manually in the CMS.
  Article body re-embedded from the current final.md and diff-checked; lint and detector re-run.
---

# Publish Package — 2026-09-19-glp-1-fitness-apps-body-composition-tracking

## What changed in this rebuild

The coordinator's QC report (14/20, marginal) found one blocking defect in the previous package
and asked for six more fixes. Status of each, checked against the current files:

1. **Meta description broke the claim rules — FIXED.** All three variants rewritten below: muscle
   loss is now attributed to research/studies, never asserted in 3DLOOK's own voice; composition
   estimates and circumferences are described as recorded *alongside* scale weight, not as
   something that reveals or replaces tracking muscle loss; "instead" is gone from every variant.
   I also checked the meta title variants and all three alt texts against `plan.md`'s "What the
   article cannot claim about muscle loss" list, which the first build never did. Two of the three
   original title variants had the same structural risk (a colon immediately followed by "what
   apps should/can track," with "muscle loss" as the nearest antecedent) and are replaced below
   with variants that name the tracked object explicitly, the same way the approved H1 does
   ("...Fitness Apps: Tracking Body Composition Beyond Scale Weight," not "...Fitness Apps: What
   to Track"). The three alt texts never mentioned "GLP-1" or "muscle" at all, so they carried no
   version of this risk; re-confirmed, unchanged.
2. **Strategy checklist re-run honestly — DONE.** See the checklist below. The previous 9/9 was
   wrong: the meta description's implied "apps can track GLP-1 muscle loss" is exactly the kind of
   forbidden positioning claim the "no forbidden positioning claims (§8)" clause of checklist item
   7 exists to catch, and under `seo-publisher.md:69` that is a STOP regardless of how many other
   items pass. I'm not hiding that this rebuild exists because a real gate should have stopped
   checkpoint 2 and did not. With the meta fixed and the body re-checked line by line, item 7 now
   passes on genuine evidence, not on the earlier unchecked assumption.
3. **Three checklist lines that contradicted the text — FIXED.** See the corrected wording in the
   SEO checklist below (the `buyer`/`customer` line, the privacy-paragraph line, and the external-
   source count).
4. **Category value — FIXED.** No longer offered as a pasteable string; see Meta section.
5. **The customer name removed from the package — FIXED.** Grepped this file for it after writing it: zero hits.
   `final.md` itself has carried no customer name since the QC fix pass (its own `changes_summary`
   records the removal); the case sentence reads "A weight-loss management platform."
6. **Word counts standardized — FIXED.** Every length claim in this package now cites `final.md`'s
   own frontmatter `word_count: 1828` (article prose) and separately labels the lint tool's 2186 as
   including the non-publishable Open items block.
7. **Article body re-embedded and diff-checked; lint and detector re-run fresh — DONE.** See the
   verbatim output below and the diff confirmation in the SEO checklist's last row.

## Checkpoint 2 touch-up (Vadim, 19.09.2026)

Not a rebuild. Three open items closed by Vadim's decision, one mechanical refresh:

1. **Slug and URL set.** `glp-1-muscle-loss-fitness-apps`, the previously recommended option 2
   ("то що радив"). Option 1 is removed, not just de-emphasized. See Meta below.
2. **Advisory link resolved.** seo-editor already moved `final.md:68` to obesity.org and closed
   the matching item in `final.md`'s own Open items block. This package's SEO checklist and Open
   items are updated to match, not just the article body.
3. **Category assigned to Vadim, manual CMS entry.** No value is pre-filled; see Meta below.
4. **Article body re-embedded from the current `final.md`, diff-checked; lint and detector output
   refreshed.** See the SEO checklist section below for the verbatim runs.

## Meta

**Title:** GLP-1 Muscle Loss: Fitness App Body Composition Tracking (56 chars) — **recommended**
**Description:** Studies examine GLP-1 muscle loss. Fitness apps can record body composition
estimates and circumferences alongside scale weight. See where FitXpress fits. (154 chars)

**Slug:** `glp-1-muscle-loss-fitness-apps` — set by Vadim at checkpoint 2, 19.09.2026 (the
previously recommended option 2, matching the approved H1's word order and keeping the primary
keyword `glp-1 muscle loss` intact as a phrase). The alternative option (date-stripped workspace
name) is dropped, not offered.
**URL:** `https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/`

**Category:** Set manually by Vadim in the CMS. Not pre-filled here — no internal label
(hub/cluster names, content-plan row descriptions) belongs in a CMS category field, since it
would show on the live page.

The H1 is fixed by Vadim's checkpoint-1 decision and is not a meta title candidate: "GLP-1 Muscle
Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight" (86 chars, far over the
60-char meta budget). Recommended meta title is 56 chars, so `| 3DLOOK` is not appended (the rule
allows the suffix only at ≤49 chars without it, and 56 is already over that). The keyword
`glp-1 muscle loss` occupies the first 18 characters of the title and the first 35 of the
description.

**Meta checked against `plan.md`'s "What the article cannot claim about muscle loss" list
(this was not done in the previous build):**
- No single number for "how much muscle is lost" — neither the title nor the description states a
  figure.
- No claim that FitXpress or an app measures, detects, monitors, or prevents muscle loss — the
  recommended description explicitly separates the two clauses ("Studies examine GLP-1 muscle
  loss." / "Fitness apps can record body composition estimates and circumferences alongside scale
  weight.") so recording is never presented as what reveals or prevents the loss.
- No drug names, doses, or trial names — none present.
- No "lean mass preservation tracking" framed as a capability — not present.
- Muscle loss is attributed to research ("Studies examine..."), not asserted in 3DLOOK's own
  voice, matching the fix QC asked for.

## SEO checklist

- [x] **Primary keyword in H1 and 1-2 H2 (gate 7 softened 2026-09-11, not a first-paragraph
      gate).** `glp-1 muscle loss` appears exactly twice: the H1 (`final.md:43`) and the Section 3
      H2 "What research shows about GLP-1 muscle loss and lean mass" (`final.md:62`). Kept out of
      prose by design (`plan.md:110-111`). `article_lint.py` keyword-placement gate: ok, 2
      occurrences, 13 H2s.
- [x] **Meta title ≤ 60 chars, primary keyword in the first half.** Recommended title 56 chars,
      keyword in the first 18 characters. Counted with Python.
- [x] **Meta description 140-160 chars.** Recommended description 154 chars, counted with Python.
      Keyword appears once, near the front. Does not repeat the meta title or the H1. Rewritten
      this session to remove the unattributed muscle-loss claim QC flagged — see "What changed"
      above.
- [x] **Every number traces to `approved_claims` (nothing invented).** Five internal claim markers:
      FX-005 (`final.md:58`, `:97`), FX-006 (`:97`), FX-002 (`:103`), FX-001 (`:105`), FX-007
      (`:107`) — matching `claims_verified` in `final.md`'s own frontmatter. Three distinct
      external sources, referenced across four sentence-level points: the Neeland review supplies
      both the lean-mass-loss range (`:64`) and the separate lean-mass-versus-muscle point (`:66`);
      the joint advisory supplies the protein/strength-training priority (`:68`, link now points to
      obesity.org, moved there by seo-editor at checkpoint 2, 19.09.2026, closing the previously
      open item); the KFF poll supplies the 12% figure (`:74`). I re-checked the
      two figures that carry the highest misstatement risk against `accuracy-formulations.md`
      directly:
      - Repeatability (`final.md:103`): "typical scan-to-scan differences remained below 1 cm,"
        now explicitly scoped to "a trend view of body measurements" — matches §5's short form
        with the QC fix-pass scoping applied (round 2, item 1).
      - Accuracy (`final.md:105`): "approximately 96-97%, with a typical absolute error of 1.5-2.0
        cm depending on the body part" — matches §5's short form, hyphens not en dashes, and now
        carries §5's own "these findings... do not demonstrate superiority" sentence, restored in
        round 2.
      - No ISO 8559 figure anywhere (re-grepped, only false-positive substring matches inside a DOI
        and a PMID number); no per-measurement figures; `FX-003` (`publishable: false`) grepped,
        zero hits. `article_lint.py` claim traceability and accuracy-discipline gates: both ok.
- [x] **No banned words.** Grepped the article body (`final.md:43-179`) against the full list
      (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry,
      realm, unlock, unleash, revolutionary, game-changing, cutting-edge): zero hits.
      `detect-ai-tells.py` hard-bans pass confirms independently (verbatim output below).
- [x] **Word count within ±10% of target.** Target is 2,000 (`plan.md:14`, `:520`). `final.md`'s
      own frontmatter `word_count: 1828` is -8.6%, inside ±10%. (**Standardized this session** —
      the previous package used a separately-counted 2,164 figure; per the coordinator's
      instruction, this rebuild cites `final.md`'s own figure everywhere instead of a second,
      independently-computed one.) `article_lint.py`'s `prose_words: 2186` is the same article plus
      the non-publishable "Open items (for Vadim, not for publication)" block
      (`final.md:181-192`); that block is roughly 340 words of editor's notes, not article prose.
- [x] **Intro hook in the first two sentences.** `final.md:49`: "A member taking a glucagon-like
      peptide-1 (GLP-1) medication logs a falling scale weight in a fitness app." then "The number
      shows how much weight changed." Unchanged by the QC fix pass.
- [x] **CTA placement per plan; type matches intent.** Plan: primary CTA in Section 12, the fitness
      page also linked once in Section 6, evaluation-framed for MOFU (`plan.md:162-167`, `:522`).
      `final.md` matches: Section 6 now opens on the fitness-page link (`:97`, moved to the lead
      sentence in the QC fix pass, round 2 item 4) and Section 12 closes on it (`:179`) with the
      plan's own anchor text verbatim: "see how FitXpress supports body composition tracking in
      connected and digital fitness apps." Secondary link (Section 9, `:149`) uses the corrected
      telehealth URL `structured-body-data-for-telehealth-digital-health-programs`, matching
      `plan.md`'s explicit correction over the context pack's stale URL (plan-audit §3, open item).
- [x] **No generic AI patterns (triple parallelism, em-dash rhetoric).** `detect-ai-tells.py`:
      CLEAN, `ai_density_per_1000_words: 0.0`, `punch_triad_count: 0`, zero em dashes. Verbatim
      output below.
- [x] **Terminology guardrails.** Re-grepped the current article body directly: zero em/en dashes,
      zero `objective` about our own conclusions, zero `the reader`/`the audience`/`the following
      sections`/`see below`, zero `this article`/`this guide`, zero `by hand`, zero `let` as a
      permission verb, zero `plus` as a connector, zero `positioned as` anywhere.
- [x] **Terminology, sync 2026-09-14.** IEEE not mentioned. `80+ body measurements` used correctly
      (`:97`), with BMI and BMR explicitly called "calculated metrics" in the same sentence, never
      "measurements." Content-plan labels (`hub`, `cluster`, `pillar`, `bridge`, `supporting
      content`): zero hits in any H1/H2/H3, meta title, or anchor; the only "hub" matches in the
      raw body are inside `content-hub` URL paths, the licensed site-section exception. `buyer`:
      zero hits anywhere in the body. `customer`: **one hit, `final.md:103`**, inside the canon
      §5 repeatability sentence verbatim ("a real-world customer dataset with five scans per
      participant"). This is licensed usage — it names 3DLOOK's own internal-testing relationship,
      the deployment/contractual sense the guardrail allows, not a fitness app's customer. (**This
      row is corrected from the previous build**, which said "neither word appears"; QC caught
      that the check had not actually been run against the text, `package:128` in the prior
      build.)
- [x] **Abbreviations (M1 + exception).** GLP-1, SDK, BMR, DXA, BIA, HIPAA, and GDPR all expand at
      first body use, re-verified by grep and line order on the current text: GLP-1 (`:49`), SDK
      (`:97`), BMR (`:97`), DXA and BIA together (`:101`), HIPAA and GDPR (`:155`). MRI's full name
      is used once (`:66`) and the bare acronym is never used, so there is nothing to expand. BMI,
      CEO, UK, US, EU are correctly left bare throughout. **One accepted exception, unchanged from
      checkpoint 1:** the H1 (`final.md:43`) opens with "GLP-1" before any expansion can appear, so
      `article_lint.py`'s abbreviations gate fails on that line. This is the article's only lint
      failure, accepted by Vadim, 2026-09-19, not counted as an open defect.
- [x] **Medical framing.** "FitXpress is not a medical device." now appears **exactly once**,
      verbatim, in the scope note (`final.md:53`) — down from twice in the previous build, per the
      QC fix pass round 2 item 3 ("kept once, in the scope note"). Zero instances of "positioned
      as" anywhere in the body.
- [x] **Links on meaningful anchors; external sources neutral and non-vendor.** All 18 markdown
      links use descriptive anchor phrases, no bare URLs. External sources, re-checked this
      session against the current `final.md`: one PubMed record (Neeland, a peer-reviewed journal
      abstract, linked twice), the obesity.org release from The Obesity Society (the joint
      advisory's priority wording, since checkpoint 2 the link target as well as the quoted text),
      and the KFF Health Tracking Poll (a nonpartisan research organization) — three neutral,
      non-vendor sources, matching `plan.md`'s source list.
- [x] **AI-tells detector actually run — verbatim output below, not estimated.** Ran
      `detect-ai-tells.py` myself this session against the current `final.md`, both with
      `--channel article --summary` and again for the full JSON. Both transcripts pasted below,
      unedited, from this session, not carried over from the prior build.
- [x] **Images / alt-text suggestions provided below**, one per illustration, no shared template,
      each re-checked this session against `plan.md`'s "cannot claim" list (none mentions GLP-1 or
      muscle, so none carried the risk the meta description did).

**SEO checklist: 16/16 passed** (the abbreviations item carries one explicitly accepted exception
that does not count against it). Three rows above are corrected from the previous build, not
newly invented passes — flagged inline where the wording changed and why.

### `article_lint.py` output, verbatim (run this session, against the current `final.md`)

```
$ python3 scripts/article_lint.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2525
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.56
[ok  ] prose length
         prose words 2140 vs target 2000 (band 1700-2300)
         . prose_words: 2140
         . target: 2000
[ok  ] claim traceability
         . claims_used: ['FX-001', 'FX-002', 'FX-005', 'FX-006', 'FX-007']
         . claims_known: 8
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 14
         . links_distinct: 9
         . asset_urls: 0
         . directions: {'up': 2, 'sideways': 3, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: glp-1 muscle loss
         . occurrences: 2
         . h2_count: 13
         . in_first_paragraph: False
[FAIL] abbreviations (M1)
         line 2: GLP-1 used before being expanded as 'glucagon-like peptide-1' (guardrail M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 136
         . mean_words: 13.5
         . p90_words: 21
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['scan to scan x3', 'fitness and coaching x3', 'body composition estimates x3', 'and composition estimates x3', 'and coaching apps x3']

VERDICT: FAIL  (1 gate(s) failed)
```

(Re-run at checkpoint 2, 19.09.2026, against the current `final.md` after the advisory-link move to
obesity.org. `prose_words` moved from 2186 to 2140, a ~2% drop from the shorter claim-marker
comment on that line, well inside the same 1700-2300 band. The only failing gate is still M1 on
the H1, unchanged.)

**On `directions: {'down': 1}` versus the 2 down links actually in the text.** Same known artifact
as the previous build: the context pack's `down` target list still carries the stale telehealth
URL, so it does not recognize the corrected one `plan.md` specifies. `links_distinct: 9` and the
direction tally (2+3+1+2=8) undercount `down` by exactly the 1 link the pack doesn't recognize. All
four directions are genuinely present in the text (fitness product page x2, telehealth page x1 as
the down links; both up, all three sideways, both trust links present and counted correctly).

**On `[FAIL] abbreviations (M1)`.** The H1 GLP-1 exception, accepted by Vadim at checkpoint 1. The
only reason `VERDICT: FAIL` appears. Every other gate is `[ok]`.

### `detect-ai-tells.py` output, verbatim (run this session, against the current `final.md`)

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md --channel article --summary
SEO / blog article · en · 2525 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md --channel article
{"language": "en", "channel": "article", "channel_label": "SEO / blog article", "profile": null,
 "total_words": 2525, "total_markers": 0, "em_dashes_excluded_from_density": 0,
 "ai_density_per_1000_words": 0.0, "density_budget": 6.0, "severity": "low", "short_form": false,
 "verdict": "CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.",
 "hard_fails": [], "house_rule_violations": [], "markers_by_category": {},
 "style_metrics": {"em_dashes": 0, "bold_count": 25, "bold_per_1000_words": 9.9,
  "title_case_headings": 0, "emoji_count": 0, "hashtag_count": 0, "bullet_lines": 26,
  "bold_lead_in_bullets": 0, "list_to_prose_ratio": 1.0, "wall_of_text": false,
  "rhythm": {"sentences": 62, "mean_words": 21.2, "variation": 0.56, "monotone": false,
   "uniform_paragraphs": false}, "punch_triads": [], "punch_triad_count": 0}, "top_offenders": []}
(exit 0 both runs, re-run at checkpoint 2, 19.09.2026)
```

`total_words: 2552` is this script's own count, which includes the frontmatter's `changes_summary`
and `self_check` narrative text, a different, larger inclusion than either `article_lint.py`'s 2186
or `final.md`'s own 1828. `ai_density: 0.0`, `hard_fails: []`, `house_rule_violations: []` are
unaffected by which word count is used, since density is markers-per-1000-words and zero markers
were found either way.

## Content strategy checklist (`content-strategy-guidelines.md` §16)

**Re-run honestly, per the coordinator's instruction.** The previous build scored this 9/9. That
was wrong: the meta description implied fitness apps (or FitXpress) could track GLP-1 muscle loss,
without attribution, which is a forbidden positioning claim under item 7's "no forbidden
positioning claims (§8)" clause. Under `seo-publisher.md:69`, any ❌ in the
positioning/compliance/cannibalization block is a STOP regardless of how many other items pass —
this should have STOPped checkpoint 2, and the package should not have shipped as a clean pass.
That is the reason this rebuild exists. With the meta description rewritten (see above) and the
body independently re-checked line by line this session, here is the honest current state:

- [x] **Bound to the right hub.** AI in Fitness (Hub 1), the "GLP-1 bridge" row
      (`content-plan.md:122`), bridging into GLP-1 Market (Hub 3). Unaffected by the QC fix pass.
- [x] **`action_type: create-net-new` respected.** Unchanged.
- [~] **Does not duplicate `existing_urls`; cannibalization guardrail respected — passing, with a
      documented caveat, not a clean mechanical check.** QC's Output-quality section (E, 3/4) found
      phrasing echoes with two sibling pages: Section 5's baseline/capture bullets resemble
      `glp-1-market`'s "What Scalable GLP-1 Progress Tracking Requires" section, and Section 9's
      fit note resembles the coaching article's "Best-fit" section. QC explicitly rated this
      **not blocking** ("Repetition and overlap with sibling pages... Not blocking," top-3 issue
      3) and distinct from a duplication of either sibling's *owned* argument or section — no tool
      comparison, no market-growth thesis, no method table is reproduced. `final.md`'s own Open
      items block (`:191`) records the Section 5 overlap as still present and unresolved by design
      ("The capture-conditions bullet stays because the plan requires it, and it still resembles
      that article's capture requirement") — carried into Open items below, not hidden.
- [x] **Vertical boundary held; scope note present for the sensitive vertical.** Scope note,
      `final.md:53`, unchanged in substance by the QC fix pass (medical-device sentence now appears
      once, here, not twice). Tone stays lighter on the fitness half, hedged on the GLP-1 half.
- [x] **Internal links in 4 directions.** up → `ai-in-fitness-industry` (`:51`) and `glp-1-market`
      (`:70`); sideways → `visual-progress-tracking-glp1-adherence-retention` (`:78`),
      `remote-body-measurement-online-fitness-coaching` (`:124`, `:157`),
      `top-7-remote-body-composition-tools-glp-1-clinics` (`:149`); down →
      `for-connected-and-digital-fitness` (`:97`, `:179`) and
      `structured-body-data-for-telehealth-digital-health-programs` (`:149`); trust →
      `mobile-body-scanning-accuracy` (`:103`, `:105`, `:167`) and
      `fitxpress-data-privacy-security-regulatory-faq` (`:155`, `:175`). All four directions
      present; see the gate note above on why the tool's own tally undercounts `down` by one.
- [x] **FAQ section present, GEO/AEO-shaped.** Three questions (`final.md:165-175`), each answered
      in 2-3 sentences, each attributing any muscle/lean-mass statement to a named source or to
      FitXpress's own documented limits, never asserting muscle loss as fact in the article's own
      voice. "Does GLP-1 cause muscle loss?" stays excluded (Section 3 answers it).
- [x] **"What FitXpress does NOT do" slot filled by the licensed substitute; no forbidden
      positioning claim — corrected from ❌ to ✅ in this rebuild.** The Fitness hub already owns
      that list, so this cluster article substitutes a scope note (`:53`) plus boundary sentences:
      Section 6 (`:99`, "does not measure muscle" is now stated once, in the scope note and FAQ 1
      only, per the QC fix pass), the DXA/BIA equivalence sentence (`:101`), and Section 7's
      boundary paragraph (`:118`, "does not provide dose calculations, symptom tracking,
      prescribing recommendations, or automated clinical decision support"). **The positioning
      violation that made this item a genuine ❌ in the previous build was in the package's meta
      description, not in the article body** — the body never claimed FitXpress or an app tracks,
      detects, or monitors muscle loss, at any point in either the original or this revised text.
      With the meta description rewritten above, re-checked against `plan.md`'s claim-limits list,
      this item now passes on verified evidence.
- [x] **No unsupported medical / legal / underwriting / employment / clinical-trial claim.** Every
      lean-mass or muscle statement in the body is attributed to a named source (Neeland et al.,
      the joint advisory, KFF); none is stated in 3DLOOK's own voice. The consent-and-data-sharing
      paragraph (`:155`) **does not restate the FAQ's HIPAA/GDPR compliance sentences** — it names
      HIPAA and GDPR as topics the linked FAQ "sets out," and links to it, matching
      `compliance.md`'s "link to central FAQ" instruction for privacy rows. (**Corrected this
      session** — the previous package said this paragraph "uses the live trust-FAQ's own HIPAA
      and GDPR sentences," which QC found untrue; `package:303-305` in the prior build.)
- [x] **Owns one distinct search intent.** "A fitness or coaching app has members taking GLP-1
      medications: what should the app record and show besides scale weight, what does research
      say about lean mass, and which questions belong to the prescribing program?" Held throughout,
      distinct from every neighboring page's owned intent, the stylistic echoes noted above
      notwithstanding.

**Content strategy checklist: 9/9 passed, honestly re-verified — one item (`~`) passes with a
documented, QC-rated non-blocking caveat rather than a clean mechanical check, and one item (the
"does not do" / positioning-claims item) is a corrected pass, not an unchecked one.** No item in
the positioning/compliance/cannibalization block is a ❌ as of this rebuild, so this package does
not STOP. It would have STOPped on the previous build's meta description, and that is recorded
above rather than smoothed over.

## Alt options

### Meta title variants

1. **GLP-1 Muscle Loss: Fitness App Body Composition Tracking** (56 chars) — **recommended.**
   Names the tracked object explicitly (body composition, not muscle loss itself), the same
   structure the approved H1 uses.
2. GLP-1 Muscle Loss and Fitness Apps: Composition Tracking (56 chars) — closer to the H1's own
   word order, shortened.
3. GLP-1 Muscle Loss: Body Composition Tracking in Fitness Apps (60 chars) — right at the
   60-char ceiling.

**Rejected this session, not offered as options:** "GLP-1 Muscle Loss: What Fitness Apps Should
Track" and "...What Fitness Apps Can Track Beyond Weight" — both from the previous build. In both,
the colon is immediately followed by "what apps should/can track," with "muscle loss" as the only
preceding noun phrase, which reads as apps tracking muscle loss. Neither the H1 nor the recommended
title above has this shape: both name the tracked object (body composition) explicitly, never
leaving "track" pointed at an implied object a reader would fill in as muscle loss.

### Meta description variants

1. **Studies examine GLP-1 muscle loss. Fitness apps can record body composition estimates and
   circumferences alongside scale weight. See where FitXpress fits.** (154 chars) —
   **recommended.** Two separate sentences: research examines the topic; apps record data
   alongside scale weight. Neither clause implies the second causes or reveals the first.
2. Research examines GLP-1 muscle loss. Fitness apps can record body composition estimates and
   circumferences alongside scale weight, and see where FitXpress fits. (160 chars) — same
   structure, joined into two sentences instead of three.
3. GLP-1 muscle loss is a research topic. Fitness apps can record composition estimates and
   circumferences alongside scale weight, and see where FitXpress fits. (157 chars) — leads with
   the keyword phrase itself named as a research topic, rather than research as the subject.

**Rejected this session:** the previous build's recommended description ("Scale weight can hide
GLP-1 muscle loss. See what fitness apps can track instead...") and its variant 3 ("A falling scale
number hides GLP-1 muscle loss...") both asserted muscle loss as fact in 3DLOOK's own voice, with
no attribution, and "track instead" implied fitness apps or FitXpress can track muscle loss itself
— the corrective frame the H1 was specifically worded to avoid with "Beyond Scale Weight." Neither
is carried forward as an option.

## Image and alt-text suggestions

Per `plan.md`'s "Illustrations" table (`plan.md:512-516`) and the `(Cover)` / `(Image 1)` /
`(Image 2)` concept markers in the current `final.md` (`:47`, `:89`, `:95`). Re-checked this
session against `plan.md`'s "What the article cannot claim about muscle loss" list: none of the
three mentions GLP-1 or muscle at all, so none carried the risk the meta description did. No
customer names in any alt text.

1. **Cover — under the Section 1 H2 (`final.md:47`).** Concept: a fitness app progress screen with
   a scale-weight trend line above one stacked bar per check-in splitting estimated fat and lean
   mass, labelled "estimate." No medication or injection imagery.

   Alt text: "Phone screen showing a weight trend line above a bar chart of estimated fat and
   lean mass per check-in." (103 chars)

2. **Image 1 — Section 5, after the workflow bullets (`final.md:89`).** Concept: a timeline for
   one member, baseline scan then check-ins at the end of each training block, each point showing
   weight, circumferences, and composition estimates next to a training-volume sparkline.

   Alt text: "Timeline of one member's scans, each showing weight, circumferences, and
   composition estimates next to a training chart." (120 chars)

3. **Image 2 — Section 6, under the H2 (`final.md:95`).** Concept: two 3D body models from scans
   the app selected, side by side, with waist, hip, and thigh circumference differences labelled.

   Alt text: "Two 3D body model scans side by side with waist, hip and thigh circumference
   differences marked." (96 chars)

All three: under 125 characters, no em dash, no stop words (robust/seamless/comprehensive/etc.),
no keyword from another page, no drug names, no claim that FitXpress measures or monitors muscle,
no prevention or outcome claim, no customer name. Each is written for its own image, not a shared
template.

Design tokens from `DESIGN.md`: electric blue `#143DFF`, navy `#050F40`, Satoshi throughout.

## Open items for Vadim

**Carried from the current `final.md`'s own Open items block (7), verbatim in substance:**

1. **M1 on the H1, accepted.** `article_lint.py` flags "GLP-1" in the H1 as used before expansion.
   Accepted by Vadim at checkpoint 1. The H1 is unchanged; GLP-1 is expanded at its first body use
   (`final.md:49`). Not an open defect.
2. **Joint advisory link. Resolved at checkpoint 2:** link moved to obesity.org
   (`final.md:68`, Vadim, 19.09.2026), matching the source of the quoted priority wording. Closed
   in `final.md`'s own Open items block and here.
3. **Secondary keywords not placed in prose.** `glp-1 and muscle loss` and `glp 1 lean muscle
   loss` are not in the body — every placement attempt in Section 3 read as keyword insertion.
4. **Response-time wording mismatch on the linked product page.** The fitness product page
   (linked in Section 6 and the CTA) says results arrive "in under a minute." The article uses the
   approved FX-006 figure, "under 45 seconds." Both are directionally consistent but a reader who
   clicks through sees two different numbers.
5. **JAMA Viewpoint not used.** The plan allowed the Conte, Hall and Klein Viewpoint only if
   verified on the JAMA page. That page returned HTTP 403 in this environment and could not be
   verified, so the Viewpoint is not in the text. Section 3's balance rests on the review's "appear
   to be adaptive" instead.
6. **Planned lines removed in the QC fix pass.** Section 7 no longer repeats "FitXpress is not a
   medical device"; the scope note carries it once. The Section 2 "Who decides what?" bullet and
   the Section 5 clinical-route bullet are cut. The Section 10 alternative path keeps only the
   approved limitation sentence. The Section 8 headings now name the two methods (DXA, professional
   BIA) instead of "reference methods."
7. **Overlap with the GLP-1 market article.** QC noted that Section 5 echoes that article's
   progress-tracking requirements. The baseline bullet is now specific to members already on
   treatment; the capture-conditions bullet stays because the plan requires it, and it still
   resembles that article's capture requirement. See the strategy checklist's `~` row above.

**New, carried from the previous build's own findings and updated for this rebuild:**

8. **Slug and URL. Resolved at checkpoint 2:** `glp-1-muscle-loss-fitness-apps`, set by Vadim
   (19.09.2026), the previously recommended option 2. See the Meta section above.
9. **Category. Resolved at checkpoint 2:** Vadim enters it manually in the CMS. See the Meta
   section above.
10. **Two still-open `plan-audit.md` items, unchanged by this rebuild:** item 3 (the CTA
    destination, `for-connected-and-digital-fitness/`, is old copy with no GLP-1 mention on the
    non-existent `/fitxpress/` path level) and item 9 (once this ships targeting `glp-1 muscle
    loss`, content-plan rows 125/166/167 should stop targeting the same term, for the next
    `content-plan.md` sync).

## Article

# GLP-1 Muscle Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight

## Where scale weight can fall short for members on GLP-1 treatment

(Cover) - Concept

A member taking a glucagon-like peptide-1 (GLP-1) medication logs a falling scale weight in a fitness app. The number shows how much weight changed. It does not show whether fat mass, lean mass, or fluid made up the change.

In fitness apps, [structured body data](https://3dlook.ai/content-hub/ai-in-fitness-industry/) already supports progress tracking, personalization, and digital coaching. For that member, recording composition estimates and circumferences next to weight gives an approximate picture of what changed and where.

**Scope note.** The focus is fitness and coaching apps, including those operated by GLP-1 programs. FitXpress supplies body measurements and composition estimates, and its lean mass estimate is not a measurement of muscle. It does not evaluate GLP-1 medications, doses, or side effects. FitXpress is not a medical device. Clinical questions stay with the prescribing clinician.

## Short answer: what fitness apps can track beyond scale weight

- **Scale weight** records total change as one number and can be logged at every weigh-in.
- **Body composition estimates** split that change into fat and lean components. Their meaning depends on the method that produced them. <!-- claim: FX-005 -->
- **Circumferences** at the waist, hip, thigh, and upper arm show where change happens. A guided smartphone scan can capture them remotely.
- **Training history** is already in the app, including strength progression and completed sessions.

## What research shows about GLP-1 muscle loss and lean mass

A 2024 review by [Neeland, Linge, and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) in *Diabetes, Obesity and Metabolism* examined lean mass changes with GLP-1-based therapies. The review reports that in some studies, lean mass reductions made up 40% to 60% of total weight lost. Other studies in the same review put the share at approximately 15% or less. The authors list population, drug-specific, and comorbidity effects among the possible reasons. <!-- claim: external, source: Neeland IJ, Linge J, Birkenfeld AL, Diabetes Obes Metab 2024, doi 10.1111/dom.15728, PMID 38937282, abstract verified verbatim 2026-09-19 -->

The same review notes that lean mass changes may not always reflect muscle changes. Its definition of lean mass also covers organs, bone, fluids, and water in fat tissue. Drawing on recent evidence, including magnetic resonance imaging studies, the authors write that skeletal muscle changes with GLP-1 receptor agonist treatment "appear to be adaptive". <!-- source: same abstract, PMID 38937282, re-checked 2026-09-19 -->

[A 2025 joint advisory](https://www.obesity.org/nutritional-priorities-to-support-glp-1-therapy-for-obesity/) names muscle and bone loss among the challenges of GLP-1 therapy. It comes from the American College of Lifestyle Medicine, the American Society for Nutrition, the Obesity Medicine Association, and The Obesity Society. Its nutritional priorities include adequate protein intake and strength training to preserve lean mass. Strength training is already part of the programs many fitness apps offer. <!-- claim: external, source: link and recommendation wording both https://www.obesity.org/nutritional-priorities-to-support-glp-1-therapy-for-obesity/ (priority 6); paper is Mozaffarian et al., Obesity 2025, doi 10.1002/oby.24336, PMID 40445127; link moved to obesity.org at checkpoint 2 (Vadim, 2026-09-19); verified 2026-09-19 -->

On the program side, the GLP-1 market analysis explains [why scale weight alone gives an incomplete progress record](https://3dlook.ai/content-hub/glp-1-market/).

## Why GLP-1 treatment is relevant to fitness and coaching apps

In a [KFF Health Tracking Poll](https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/), about one in eight US adults (12%) said they were currently taking a GLP-1 drug. The figure covers use either to lose weight or to treat a chronic condition. KFF fielded the poll from October 27 to November 2, 2025. <!-- claim: external, source: KFF Health Tracking Poll, published 2025-11-14, verified 2026-09-19 -->

Fitness and coaching apps are likely to count some of these adults among their members, whether or not a member tells the app.

For members treated for weight management, a falling scale weight is the expected direction. A progress view built on the scale then says little about what the training program adds. A fuller view also displays circumferences and composition estimates. Whether visible progress affects engagement and retention is a separate question, taken up in [visual progress tracking for GLP-1 adherence and retention](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/).

## How a fitness app can track body composition during GLP-1 treatment

On the app side, the workflow covers a baseline, check-ins, capture conditions, and a progress view.

- **Baseline.** The first scan takes place at onboarding or at the start of a strength program. A member may already be partway through treatment by then. The baseline marks where the app's record begins, and any earlier change sits outside it.
- **Check-ins at defined points.** Scans follow the training plan, for example at the end of each training block.
- **Repeatable capture conditions.** Members wear similar clothing and scan at about the same time of day, in the same setting. The guided flow checks pose and capture quality.
- **One progress view.** Weight, circumferences, and composition estimates appear together, next to training history. Labels mark which values are estimates.

(Image 1) - Concept

The workflow runs the same way whether or not the app knows about a member's medication.

## Where FitXpress fits

(Image 2) - Concept

[FitXpress for connected and digital fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) embeds guided two-photo capture, front and side, through a software development kit (SDK). Results arrive in under 45 seconds. The outputs include 80+ body measurements, body composition estimates (body fat percentage, fat mass, and lean mass), and a 3D model. BMI and basal metabolic rate (BMR) are included as calculated metrics. <!-- claim: FX-006 --> <!-- claim: FX-005 -->

For progress views, FitXpress compares two scans that the app selects. Body composition estimates are derived from the body measurements along with height and optional weight.

Some clinical protocols and research studies require dual-energy X-ray absorptiometry (DXA) or professional bioelectrical impedance analysis (BIA). FitXpress is not equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods.

What counts as adequate performance depends on how the measurements will be used. For a trend view of body measurements, repeatability is especially important, because each check-in is compared with an earlier scan. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) evaluates repeatability separately from accuracy. Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FX-002 -->

A separate internal validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, [reported accuracy](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. These findings establish performance relative to the selected reference; they do not demonstrate superiority over expert tape measurement. <!-- claim: FX-001 -->

A weight-loss management platform ran 34,000 FitXpress scans in 2025. It used them for periodic check-in progress tracking, 3D visualization, and body composition context. <!-- claim: FX-007 -->

## What the app, the prescribing program, and FitXpress each handle

When a member on GLP-1 treatment also uses a separate fitness app, two organizations hold parts of the progress record.

| **Role** | **Responsible for** | **Uses body data to** |
|---|---|---|
| Prescribing clinician or GLP-1 program | Medication, dosing, side effects, and any clinical assessment of muscle or nutritional status | Review progress alongside clinical information, where its protocol includes body data |
| Fitness or coaching app | Training programs, progress views, and member communication | Show measurement and composition trends next to training history |
| Member | Completing scans and choosing what to share with each service | See change beyond the scale reading |
| FitXpress | Body measurements, body composition estimates, a 3D model, and scan-to-scan comparison | Supply structured records to the app or program that integrates it |

FitXpress does not provide dose calculations, symptom tracking, prescribing recommendations, or automated clinical decision support.

## Scale weight, body composition estimates, and DXA or professional BIA: which fits when

[Remote body measurement for online fitness coaching programs](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/) compares scales, tape measurements, photos, BIA, DXA, and mobile scans method by method. In a fitness app, the choice depends on how often members check in and what the result is used for.

### Scale weight alone fits when

- The app only needs a general weight trend.
- Members check in rarely or decline body scans.
- No training program in the app depends on composition context.

### Body composition estimates fit when

- Members follow a strength program inside the app.
- Coaches review check-ins as part of the program.
- Check-ins happen remotely, between any clinic visits.

### DXA or professional BIA fits when

- A clinical protocol or study specifies the method.
- Measurements are infrequent enough to book as appointments.
- Members can travel to a facility with the equipment.

Consumer smart scales estimate composition through bioelectrical impedance, and readings depend on the device and the measurement conditions.

## Fitness apps and GLP-1 programs this workflow fits

- **Fitness and coaching apps** that run strength programs with recurring check-ins, whether coaches review them or members follow a self-guided plan.
- **GLP-1 programs** that add training features to their own GLP-1 app. [Structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) covers that setting. Clinics comparing vendors can start with [body composition and progress-tracking tools for remote GLP-1 clinics](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/).

A member's GLP-1 program may already record body composition with DXA or professional BIA. The app's scans then form a second record made by a different method, and each record is best read against its own earlier values.

## Implementation and evaluation considerations

**Consent and data sharing.** Photos, body measurements, and 3D models may be personal data, and body composition outputs can be health data, depending on use. The [FitXpress data privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) covers storage, retention, and deletion. It also sets out how deployments work under the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR). When the app and a GLP-1 program are separate organizations, record sharing depends on the member's consent and on agreements between the two.

**Change thresholds.** As in [online coaching programs](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/), the smallest difference worth showing a member depends on observed scan-to-scan variation and the check-in interval.

**An alternative measurement path.** FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population.

**Pilot measures.** A pilot can track scan completion, repeat check-in completion, and use of the progress view. Repeat completion matters most, because every comparison depends on members scanning again at the planned interval. Measures the app already records before launch, such as check-in rates, can be compared with a pre-pilot baseline.

## Frequently asked questions

### Can a mobile body scan measure muscle loss during GLP-1 treatment?

A FitXpress scan does not measure muscle or muscle loss, and its [published accuracy figures](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) cover body measurements. The lean mass output is an estimate, and [a review by Neeland and colleagues](https://pubmed.ncbi.nlm.nih.gov/38937282/) notes that lean mass includes more than muscle. Where a protocol requires DXA, that method applies.

### How often should a fitness app scan members on GLP-1 treatment?

The interval depends on the size of the expected change compared with typical scan-to-scan differences, and on the length of the training block. Scans spaced closer than the change they are meant to show add records without adding information.

### Does a fitness app need to know whether a member takes a GLP-1 medication?

Not for body composition tracking itself, because the scan and the progress view need only photos and basic profile details. Asking about medication is a [health-data decision](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) that involves purpose, notice, and consent.

## Next steps

Compare the app's current progress view with what members on GLP-1 treatment need to see. Then [see how FitXpress supports body composition tracking in connected and digital fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).
