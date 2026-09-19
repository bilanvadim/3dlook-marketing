---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
product: fitxpress
status: ready_for_review
created: 2026-09-19
hub: AI in Fitness (Hub 1), bridge into GLP-1 Market (Hub 3)
cluster: GLP-1 bridge
action_type: create-net-new
priority: P1
author: Assel Sekerova
word_count: 2164
source_final: "final.md (status: edited, 2026-09-19)"
lint_verdict: "FAIL on 1 gate (abbreviations M1, H1 only) — accepted by Vadim at checkpoint 1, not an open defect. All other gates PASS."
---

# Publish Package — 2026-09-19-glp-1-fitness-apps-body-composition-tracking

## Meta

**Title:** GLP-1 Muscle Loss: Fitness App Body Composition Tracking (56 chars) — **recommended**
**Description:** Scale weight can hide GLP-1 muscle loss. See what fitness apps can track
instead, body composition estimates and circumferences, and where FitXpress fits. (154 chars)
**Slug:** `glp-1-fitness-apps-body-composition-tracking` (derived — see note below, not sourced
from `plan.md`)
**URL:** `https://3dlook.ai/content-hub/glp-1-fitness-apps-body-composition-tracking/`
**Category:** Content Hub — AI in Fitness (Hub 1), GLP-1 bridge into GLP-1 Market (Hub 3)

The H1 is fixed by Vadim's checkpoint-1 decision and is not a meta title candidate: "GLP-1
Muscle Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight" (86 chars, far over
the 60-char meta budget). The meta title is a separate, shorter string built to carry the same
primary keyword. Recommended title is 56 chars, so `| 3DLOOK` is not appended (the rule allows
the suffix only at ≤49 chars without it, and 56 is already over that). The keyword `glp-1 muscle
loss` occupies the first 18 characters.

**Finding: the task's premise that "the slug and URL come from plan.md's 'Article meta' section"
does not hold.** I read that section in full (`plan.md:518-522`) — it lists estimated word count,
tables/visuals, and CTA placement only. No slug or URL field exists there, or anywhere else in
`plan.md` or `plan-audit.md`. The only slug-shaped value in either file is the frontmatter
`slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking`, which is the dated workspace
folder name — the task explicitly says this is not the published slug.

I derived `glp-1-fitness-apps-body-composition-tracking` by stripping the date prefix and
changing nothing else, following the precedent set by the one sibling page built under the same
recent pipeline: workspace `2026-08-26-remote-body-measurement-online-fitness-coaching` published
at `remote-body-measurement-online-fitness-coaching` (date stripped, nothing else changed;
confirmed live per `plan.md` internal link and `published-articles-inventory.md`). It also fits
the `/content-hub/` path every sibling page in this cluster uses (`ai-in-fitness-industry`,
`glp-1-market`, `remote-body-measurement-online-fitness-coaching`,
`top-7-remote-body-composition-tools-glp-1-clinics`,
`visual-progress-tracking-glp1-adherence-retention`). This is inferred, not sourced — flagged as
an open item below for Vadim to confirm or override before CMS entry.

## SEO checklist

- [x] **Primary keyword in H1 and 1-2 H2 (gate 7 softened 2026-09-11, not a first-paragraph
      gate).** `glp-1 muscle loss` appears exactly twice in the body: the H1 (`final.md:36`) and
      the Section 3 H2 "What research shows about GLP-1 muscle loss and lean mass"
      (`final.md:58`). Not in the first paragraph by design — the plan keeps the exact phrase out
      of prose and uses plain words ("lean mass," "members on GLP-1 treatment") instead
      (`plan.md:110-111`). `article_lint.py` keyword-placement gate: ok, 2 occurrences, 13 H2s.
- [x] **Meta title ≤ 60 chars, primary keyword in the first half.** Recommended title 56 chars,
      keyword in the first 18 characters. Counted with Python, not by eye (see Meta section).
- [x] **Meta description 140-160 chars.** Recommended description 154 chars, counted with
      Python. Keyword appears once. Does not repeat the meta title or the H1.
- [x] **Every number traces to `approved_claims` (nothing invented).** Five internal claim
      markers in the body: FX-005 (`final.md:53`, `:96`), FX-006 (`:96`), FX-002 (`:104`), FX-001
      (`:106`), FX-007 (`:108`) — the same 5 IDs the frontmatter's `claims_verified` field lists.
      Three external figures, each with a source comment: the Neeland range (`:60`), the same
      review's lean-mass-vs-muscle point (`:62`), the joint advisory's priority wording (`:64`),
      the KFF poll figure (`:70`). I checked the two figures that carry the highest
      misstatement risk against the canon directly, not just against the gate's boolean:
      - Repeatability (`final.md:104`): "typical scan-to-scan differences remained below 1 cm" —
        matches `accuracy-formulations.md` §5's approved short form exactly.
      - Accuracy (`final.md:106`): "approximately 96-97%, with a typical absolute error of
        1.5-2.0 cm depending on the body part" — matches §5's short form; hyphens, not en dashes.
        Both paragraphs add the word "internal" to the lead sentence; §5's own note licenses this
        exactly ("where the surrounding copy could be read as implying outside validation, put it
        back... per editorial guardrail #3").
      - The two benchmarks are never in the same paragraph; no ISO 8559 figure anywhere
        (grepped, zero hits); no per-measurement figures; `FX-003` (`95%+ repeatability
        consistency`, `publishable: false`) grepped, zero hits. `article_lint.py` claim
        traceability and accuracy-discipline gates: both ok.
- [x] **No banned words.** Grepped the article body (`final.md:36-182`) against the full list
      (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry,
      realm, unlock, unleash, revolutionary, game-changing, cutting-edge): zero hits.
      `detect-ai-tells.py` hard-bans pass confirms independently (see verbatim output below).
- [x] **Word count within ±10% of target.** Target is 2,000 (`plan.md:14`, `:520`). The
      frontmatter's own `word_count: 2031` is +1.55%. I independently counted the article body
      only (H1 through "Next steps," excluding frontmatter and the Open items block) two ways —
      `wc -w` (2,163 words) and a Python split on the same slice (2,164 words) — both land at
      +8.15% to +8.2%, still inside the ±10% band. `article_lint.py`'s own `prose_words: 2223`
      figure is 3.4% over the ceiling of its own 1700-2300 band's midpoint math only because it
      counts through the end of the file, including the "Open items (for Vadim, not for
      publication)" block appended after the `---` separator — the task brief flags this
      explicitly, and I confirm it: that block alone is about 220 words of editor's notes, not
      article prose. On every count that excludes it, the article is within target.
- [x] **Intro hook in the first two sentences.** `final.md:42`: "A member taking a
      glucagon-like peptide-1 (GLP-1) medication logs a falling scale weight in a fitness app."
      then "The number shows how much weight changed." The tension the rest of the article
      resolves (a falling number that does not say what changed) is stated before the third
      sentence.
- [x] **CTA placement per plan; type matches intent.** Plan: primary CTA in Section 12 only, the
      fitness page also linked once in Section 6, evaluation-framed for MOFU (`plan.md:162-167`,
      `:522`). Final.md matches exactly: Section 6 (`:108`) and Section 12 (`:182`) both link
      `https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/`, and the Section 12 anchor
      is the plan's own anchor text verbatim: "see how FitXpress supports body composition
      tracking in connected and digital fitness apps." Secondary link (Section 9, `:152`) uses
      the corrected telehealth URL `structured-body-data-for-telehealth-digital-health-programs`,
      not the stale URL in the context pack — matching `plan.md`'s explicit correction, not the
      pack (plan-audit §3, Open item 4).
- [x] **No generic AI patterns (triple parallelism, em-dash rhetoric).** `detect-ai-tells.py`:
      CLEAN, `ai_density_per_1000_words: 0.0`, `punch_triad_count: 0`, zero em dashes. See
      verbatim output below.
- [x] **Terminology guardrails.** Grepped the article body directly: zero em/en dashes, zero
      `objective` about our own conclusions, zero `the reader`/`the audience`/`the following
      sections`/`see below`, zero `this article`/`this guide`, zero `by hand`, zero `let` as a
      permission verb, zero `plus` as a connector, zero `positioned as` anywhere. No
      presumed-reader-reaction phrasing and no behavior attributed to concepts found on a manual
      read of all 12 sections. "So" appears in the body but not introducing a benefit (checked
      each instance by hand).
- [x] **Terminology, sync 2026-09-14.** IEEE: not mentioned at all, so the two-phrase rule and
      the no-standalone-logo rule are moot. `80+ body measurements` used correctly (`:96`); BMI
      and BMR are explicitly called "calculated metrics" in the same sentence (`:96`), never
      "measurements"; "body composition" is consistently "estimates," never a measurement.
      Content-plan labels (`hub`, `cluster`, `pillar`, `bridge`, `supporting content`): zero hits
      in any H1/H2/H3, meta title, or anchor text — the only matches for "hub" in the raw body
      are inside `content-hub` URL paths, which is the licensed site-section exception.
      `buyer`/`customer`: neither word appears anywhere in the article body.
- [x] **Abbreviations (M1 + exception).** GLP-1, DXA, BIA, SDK, BMR, and HIPAA/GDPR all expand at
      first body use, verified by grep and line order: GLP-1 (`:42`), SDK (`:96`), BMR (`:96`),
      DXA and BIA together (`:100`), HIPAA and GDPR (`:158`). MRI's full name is used once
      (`:62`) and the acronym itself is never used bare, so there is nothing to expand. BMI, CEO,
      UK, US, EU are correctly left bare throughout. **One accepted exception, per Vadim's
      checkpoint-1 ruling:** the H1 (`final.md:36`) opens with "GLP-1" before any expansion can
      appear, so `article_lint.py`'s abbreviations gate fails on that line
      (`line 2: GLP-1 used before being expanded... (guardrail M1)`). This is the article's only
      lint failure, it is accepted as a known failure per Vadim, 2026-09-19, and it is not counted
      as an open defect here (`plan.md` §"Checkpoint 1," item 5).
- [x] **Medical framing.** "FitXpress is not a medical device." appears exactly twice, verbatim,
      in its current canonical direct form (`final.md:48`, scope note; `:121`, role-split
      section). Zero instances of "positioned as" anywhere in the body (grepped).
- [x] **Links on meaningful anchors; external sources neutral and non-vendor.** All 17 markdown
      links use descriptive anchor phrases, no bare URLs. External sources: two PubMed records
      (peer-reviewed journal abstracts, `pubmed.ncbi.nlm.nih.gov`), the KFF Health Tracking Poll
      (`kff.org`, a nonpartisan research organization) — all three are neutral, non-commercial,
      non-vendor sources, matching `plan.md`'s source list exactly.
- [x] **AI-tells detector actually run — verbatim output below, not estimated.** Ran
      `detect-ai-tells.py` myself this session with `--channel article --summary` and again
      without `--summary` for the full JSON. Both transcripts are pasted below, unedited.
- [x] **Images / alt-text suggestions provided below**, one per illustration, no shared template.

**SEO checklist: 16/16 passed** (the abbreviations item carries one explicitly accepted exception
that does not count against it, per Vadim's checkpoint-1 ruling). Note for whoever reads the
"After: notify Вадиму" line in this agent's own instructions: that template says "SEO checklist:
{N}/10" — the actual checklist in this same prompt has 16 items, not 10 (it grew past the earlier
Terminology-sync and Ai-tells-detector additions). I am reporting 16/16 against the checklist as
literally written, not against the stale "/10" in the notify template.

### `article_lint.py` output, verbatim (run this session)

```
$ python3 scripts/article_lint.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2572
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.51
[ok  ] prose length
         prose words 2223 vs target 2000 (band 1700-2300)
         . prose_words: 2223
         . target: 2000
[ok  ] claim traceability
         . claims_used: ['FX-001', 'FX-002', 'FX-005', 'FX-006', 'FX-007']
         . claims_known: 8
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 13
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
         . sentences: 146
         . mean_words: 13.1
         . p90_words: 21
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['the prescribing clinician x3', 'scan to scan x3', 'body measurements and x3', 'and composition estimates x3']

VERDICT: FAIL  (1 gate(s) failed)
```

**On `directions: {'down': 1}` versus the 2 down links actually in the text.** The article links
two down/BOFU destinations (the fitness product page, `:108` and `:182`, and the telehealth page,
`:152`). The gate only recognizes 1, because its context-pack `down` target list still carries the
old telehealth URL (`for-telehealth-and-weight-loss`), while `plan.md` correctly told the writer
to use the live URL the GLP-1 hub actually links
(`structured-body-data-for-telehealth-digital-health-programs`) — a mismatch `plan-audit.md`
already flagged as Open item 4. This is a context-pack reporting artifact, not a missing link:
`links_distinct: 9` and the direction counts (2+3+1+2=8) undercount by exactly the 1 down link the
pack doesn't recognize, matching 9 distinct URLs. All four directions are genuinely present in the
text.

**On the `[FAIL] abbreviations (M1)` line.** This is the H1 GLP-1 exception, accepted by Vadim at
checkpoint 1 (`plan.md` line 39-42: "прийняти як відомий збій... Do not reshape the H1 to satisfy
it"). It is the only reason `VERDICT: FAIL` at the bottom of this output. Every other gate is
`[ok]`.

### `detect-ai-tells.py` output, verbatim (run this session)

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md --channel article --summary
SEO / blog article · en · 2572 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/final.md --channel article
{"language": "en", "channel": "article", "channel_label": "SEO / blog article", "profile": null,
 "total_words": 2572, "total_markers": 0, "em_dashes_excluded_from_density": 0,
 "ai_density_per_1000_words": 0.0, "density_budget": 6.0, "severity": "low", "short_form": false,
 "verdict": "CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.",
 "hard_fails": [], "house_rule_violations": [], "markers_by_category": {},
 "style_metrics": {"em_dashes": 0, "bold_count": 25, "bold_per_1000_words": 9.7,
  "title_case_headings": 0, "emoji_count": 0, "hashtag_count": 0, "bullet_lines": 27,
  "bold_lead_in_bullets": 0, "list_to_prose_ratio": 0.93, "wall_of_text": false,
  "rhythm": {"sentences": 72, "mean_words": 19.9, "variation": 0.51, "monotone": false,
   "uniform_paragraphs": false}, "punch_triads": [], "punch_triad_count": 0}, "top_offenders": []}
(exit 0 both runs)
```

`total_words: 2572` here (versus `prose_words: 2223` from `article_lint.py`) is this script's own
word count, which includes the frontmatter's `changes_summary` and `self_check` YAML text — a
different, larger inclusion than `article_lint.py`'s. Both figures are larger than the true
article-prose count (~2,163-2,164) for the same reason: neither strips non-prose blocks
(frontmatter narrative fields, the Open items block) before counting. `ai_density: 0.0`,
`hard_fails: []`, `house_rule_violations: []` are unaffected by which word count is used, since
density is markers-per-1000-words and zero markers were found either way.

## Content strategy checklist (`content-strategy-guidelines.md` §16)

- [x] **Bound to the right hub.** AI in Fitness (Hub 1), filed as the "GLP-1 bridge" row
      (`content-plan.md:122`), bridging into GLP-1 Market (Hub 3). `plan.md:6-7`,
      `plan-audit.md` §2.
- [x] **`action_type: create-net-new` respected.** Family `Create net-new`, verbatim, no
      qualifier, gate reads GO (`plan-audit.md` §2, "Gate reading"). Confirmed a standalone
      article at checkpoint 1, not a section in GLP-1 Market (`plan.md` line 34: "окрема
      стаття").
- [x] **Does not duplicate `existing_urls`; cannibalization guardrail respected.**
      `plan-audit.md` §2's adjacent-rows table names exactly what each neighboring page owns and
      how this article stays clear of it (the fitness hub's broad overview, the coaching
      article's method table and pilot list, the GLP-1 hub's market thesis, the tools listicle's
      vendor evaluation, the Visual Progress page's engagement argument). I re-checked the
      article body against that table directly: no method table (Section 8 explicitly avoids
      rebuilding it, `final.md:146` links out instead), no market-growth argument (Section 3
      links up to it instead, `:66`), no tools comparison (Section 9 links out, `:152`), no
      engagement/retention argument stated as fact (Section 4 poses it as "a separate question,"
      links out, `:74`). `changes_summary` in `final.md`'s own frontmatter records the near-
      duplicate cuts made during editing (line 22).
- [x] **Vertical boundary held; scope note present for the sensitive vertical.** Scope note,
      `final.md:48`: fitness and coaching apps only, does not evaluate GLP-1 medications, doses,
      or side effects, not a medical device, clinical questions stay with the prescribing
      clinician. Tone is lighter on the fitness half and hedged on the GLP-1 half throughout,
      matching `plan.md`'s instruction (`plan-audit.md` §2 "Actors").
- [x] **Internal links in 4 directions.** up → `ai-in-fitness-industry` (`:46`) and `glp-1-market`
      (`:66`); sideways → `visual-progress-tracking-glp1-adherence-retention` (`:74`),
      `remote-body-measurement-online-fitness-coaching` (`:146`),
      `top-7-remote-body-composition-tools-glp-1-clinics` (`:152`); down →
      `for-connected-and-digital-fitness` (`:108`, `:182`) and
      `structured-body-data-for-telehealth-digital-health-programs` (`:152`); trust →
      `mobile-body-scanning-accuracy` (`:104`, `:106`, `:170`) and
      `fitxpress-data-privacy-security-regulatory-faq` (`:158`, `:178`). All four directions
      present; see the note above on why the gate's own tally undercounts `down` by one.
- [x] **FAQ section present, GEO/AEO-shaped.** Three questions (`final.md:168-178`), each
      answered in 2-4 sentences, each linking out rather than repeating body content. "Does GLP-1
      cause muscle loss?" is deliberately excluded (Section 3 already answers it, per
      `plan.md:496-497`).
- [x] **"What FitXpress does NOT do" slot filled by the licensed substitute.** The Fitness hub
      already owns that list (`plan-audit.md` §5), so per `editorial-rewrites.md` §7 this cluster
      article substitutes a scope note (`final.md:48`) plus boundary sentences inside "Where
      FitXpress fits" (`:98`, "does not measure muscle"; `:100`, the DXA/BIA equivalence
      sentence). Section 7 additionally carries a role-split table and its own boundary
      paragraph (`:121`) — more coverage than the minimum, not less. No forbidden positioning
      claim found anywhere in the body (re-grepped this session, zero "positioned as").
- [x] **No unsupported medical / legal / underwriting / employment / clinical-trial claim.**
      Every lean-mass or muscle statement is attributed to a named source in the sentence that
      carries it (Neeland et al., the joint advisory, KFF) — none is stated in the article's own
      voice. FitXpress's own claims stay inside "estimates," never "measures" or "monitors"
      muscle (checked by grep: zero instances of FitXpress claiming to measure, monitor, or
      detect muscle). The one compliance paragraph (`:158`) uses the live trust-FAQ's own HIPAA
      and GDPR sentences and links to the FAQ rather than restating it further, matching
      `compliance.md`'s "link to central FAQ" instruction for privacy rows.
- [x] **Owns one distinct search intent.** "A fitness or coaching app has members taking GLP-1
      medications: what should the app record and show besides scale weight, what does research
      say about lean mass, and which questions belong to the prescribing program?" — stated once
      in `plan.md:70-74` and held throughout; distinct from every neighboring page's intent per
      the adjacent-rows table above.

**Content strategy checklist: 9/9 passed.** No item in the positioning/compliance/cannibalization
block is a ❌, so this package does not STOP.

## Alt options

### Meta title variants

1. **GLP-1 Muscle Loss: Fitness App Body Composition Tracking** (56 chars) — **recommended.**
   Keyword first, names both halves of the bridge (GLP-1 side, fitness-app side) without
   implying the product tracks muscle itself.
2. GLP-1 Muscle Loss: What Fitness Apps Should Track (49 chars) — shorter, leaves room for a
   brand suffix, but drops "body composition" from the title string itself.
3. GLP-1 Muscle Loss: What Fitness Apps Can Track Beyond Weight (60 chars) — closest to the H1's
   own "Beyond Scale Weight" framing; right at the 60-char ceiling.

### Meta description variants

1. **Scale weight can hide GLP-1 muscle loss. See what fitness apps can track instead, body
   composition estimates and circumferences, and where FitXpress fits.** (154 chars) —
   **recommended.** States the hook (scale weight hides the real change), names the two concrete
   things the article covers, closes on a soft, evaluation-framed pointer to the product. No
   claim that FitXpress measures muscle.
2. GLP-1 muscle loss can hide behind a falling scale number. See what fitness apps can track
   instead, and where FitXpress fits in the workflow. (140 chars) — shorter, less specific about
   what "instead" means.
3. A falling scale number hides GLP-1 muscle loss. See what fitness apps can track beyond weight,
   and how FitXpress supports body composition tracking. (148 chars) — leads with the same hook,
   closes on the exact CTA-anchor phrasing used in Section 12 of the article.

## Image and alt-text suggestions

Per `plan.md`'s "Illustrations" table (`plan.md:512-516`) and the `(Cover)` / `(Image 1)` /
`(Image 2)` concept markers left in `final.md` (`:40`, `:86`, `:94`) for the designer. No Yazen
in any alt text, per Vadim's instruction — none of the three concepts names a customer.

1. **Cover — under the Section 1 H2 (`final.md:40`).** Concept: a fitness app progress screen
   with a scale-weight trend line above one stacked bar per check-in splitting estimated fat and
   lean mass, labelled "estimate." No medication or injection imagery.

   Alt text: "Phone screen showing a weight trend line above a bar chart of estimated fat and
   lean mass per check-in." (103 chars)

2. **Image 1 — Section 5, after the workflow bullets (`final.md:86`).** Concept: a timeline for
   one member, baseline scan then check-ins at the end of each training block, each point
   showing weight, circumferences, and composition estimates next to a training-volume
   sparkline.

   Alt text: "Timeline of one member's scans, each showing weight, circumferences, and
   composition estimates next to a training chart." (120 chars)

3. **Image 2 — Section 6, under the H2 (`final.md:94`).** Concept: two 3D body models from
   scans the app selected, side by side, with waist, hip, and thigh circumference differences
   labelled.

   Alt text: "Two 3D body model scans side by side with waist, hip and thigh circumference
   differences marked." (96 chars)

All three: under 125 characters, no em dash, no stop words (robust/seamless/comprehensive/etc.),
no keyword from another page, no drug names, no claim that FitXpress measures or monitors muscle,
no prevention or outcome claim. Each is written for its own image, not a shared template.

Design tokens from `DESIGN.md`: electric blue `#143DFF`, navy `#050F40`, Satoshi throughout.

## Open items for Vadim

**Carried from `final.md`'s own Open items block (4), verbatim in substance:**

1. **M1 on the H1, accepted.** `article_lint.py` flags "GLP-1" in the H1 as used before
   expansion. Accepted by Vadim at checkpoint 1 (`plan.md` line 39-42). The H1 is unchanged; GLP-1
   is expanded at its first body use (`final.md:42`). Not an open defect — listed here only so
   the acceptance travels with the package, per the task brief's instruction.
2. **Joint advisory link.** The article keeps one link, to the paper's PubMed record
   (`final.md:64`). The priority wording actually quoted ("adequate protein intake and strength
   training to preserve lean mass") comes from The Obesity Society's obesity.org summary, not the
   PubMed abstract itself. Swap the link to the obesity.org release if you want the exact quoted
   wording to sit at the link target.
3. **Secondary keywords not placed in prose.** `glp-1 and muscle loss` and `glp 1 lean muscle
   loss` are not in the body — every placement attempt in Section 3 read as keyword insertion.
   The primary keyword sits in the H1 and the Section 3 H2 only, as planned (`plan.md:110`).
4. **Response-time wording mismatch on the linked product page.** The fitness product page
   (linked in Section 6 and the CTA) says results arrive "in under a minute." The article uses
   the approved FX-006 figure, "under 45 seconds" (`final.md:96`). Both are directionally
   consistent (45 seconds is under a minute) but a reader who clicks through sees two different
   numbers for the same claim.

**New, from this pass:**

5. **The published slug and URL are not sourced, they are derived.** See the "Finding" note in
   the Meta section above. `plan.md`'s "Article meta" section does not contain a slug or URL
   field. I derived `glp-1-fitness-apps-body-composition-tracking` by stripping the date from the
   workspace folder name, on the precedent of the one sibling page built the same way
   (`remote-body-measurement-online-fitness-coaching`). Please confirm before CMS entry, or
   correct it if a different slug was decided outside these two files.
6. **The category suggestion is inferred, not sourced.** I wrote "Content Hub — AI in Fitness
   (Hub 1), GLP-1 bridge into GLP-1 Market (Hub 3)" from `plan.md`'s hub/cluster fields. Neither
   file names a CMS-side category taxonomy, so this is a description of the article's place in
   the content strategy, not a confirmed CMS category value.
7. **Two open items from `plan-audit.md` §10 are still open and relevant to publication timing,**
   though neither blocks this package: item 3 (the CTA destination, `for-connected-and-digital-
   fitness/`, is old copy with no GLP-1 mention and sits on the non-existent `/fitxpress/` path
   level — a reader clicking through from this article lands on a generic page) and item 9 (once
   this ships targeting `glp-1 muscle loss`, content-plan rows 125, 166 and 167 should stop
   targeting the same term, a note for the next `content-plan.md` sync).

## Article

# GLP-1 Muscle Loss and Fitness Apps: Tracking Body Composition Beyond Scale Weight

## Where scale weight can fall short for members on GLP-1 treatment

(Cover) - Concept

A member taking a glucagon-like peptide-1 (GLP-1) medication logs a falling scale weight in a fitness app. The number shows how much weight changed. It does not show whether fat mass, lean mass, or fluid made up the change.

Recording composition estimates and circumferences next to weight gives an approximate picture of what changed and where.

For an app team, the choice turns on two questions: what the app records beyond scale weight, and where the app's role ends. An overview of [structured body data for progress tracking in fitness apps](https://3dlook.ai/content-hub/ai-in-fitness-industry/) covers the wider category, including personalization and digital coaching.

**Scope note.** The focus is fitness and coaching apps, including those operated by GLP-1 programs. FitXpress supplies body measurements and composition estimates, and its lean mass estimate is not a measurement of muscle. It does not evaluate GLP-1 medications, doses, or side effects. FitXpress is not a medical device. Clinical questions stay with the prescribing clinician.

## Short answer: what fitness apps can track beyond scale weight

- **Scale weight** records total change as a single number.
- **Body composition estimates** split that change into fat and lean components. Their meaning depends on the method that produced them. <!-- claim: FX-005 -->
- **Circumferences** at the waist, hip, thigh, and upper arm show where change happens. A guided smartphone scan can capture them remotely.
- **Training history** is already in the app. Strength progression and completed sessions put the composition trend in context.
- **Who decides what?** The app runs training and progress views. Medication and clinical decisions stay outside the app.

## What research shows about GLP-1 muscle loss and lean mass

A 2024 review by [Neeland, Linge, and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) in *Diabetes, Obesity and Metabolism* examined lean mass changes with GLP-1-based therapies. The review reports that in some studies, lean mass reductions made up 40% to 60% of total weight lost. Other studies in the same review put the share at approximately 15% or less. The authors list population, drug-specific, and comorbidity effects among the possible reasons. <!-- claim: external, source: Neeland IJ, Linge J, Birkenfeld AL, Diabetes Obes Metab 2024, doi 10.1111/dom.15728, PMID 38937282, abstract verified verbatim 2026-09-19 -->

The same review notes that lean mass changes may not always reflect muscle changes. Its definition of lean mass also covers organs, bone, fluids, and water in fat tissue. Drawing on recent evidence, including magnetic resonance imaging studies, the authors write that skeletal muscle changes with GLP-1 receptor agonist treatment "appear to be adaptive". <!-- source: same abstract, PMID 38937282, re-checked 2026-09-19 -->

[A 2025 joint advisory](https://pubmed.ncbi.nlm.nih.gov/40445127/) names muscle and bone loss among the challenges of GLP-1 therapy. It comes from the American College of Lifestyle Medicine, the American Society for Nutrition, the Obesity Medicine Association, and The Obesity Society. Its nutritional priorities include adequate protein intake and strength training to preserve lean mass. Strength training is the part of that priority a fitness app already delivers. <!-- claim: external, source: Mozaffarian et al., Obesity 2025, doi 10.1002/oby.24336, PMID 40445127; recommendation wording verbatim from https://www.obesity.org/nutritional-priorities-to-support-glp-1-therapy-for-obesity/ (priority 6), verified 2026-09-19 -->

On the program side, the GLP-1 market analysis explains [why scale weight alone gives an incomplete progress record](https://3dlook.ai/content-hub/glp-1-market/).

## Why GLP-1 treatment is relevant to fitness and coaching apps

In a [KFF Health Tracking Poll](https://www.kff.org/public-opinion/poll-1-in-8-adults-say-they-are-currently-taking-a-glp-1-drug-for-weight-loss-diabetes-or-another-condition-even-as-half-say-the-drugs-are-difficult-to-afford/), about one in eight US adults (12%) said they were currently taking a GLP-1 drug. The figure covers use either to lose weight or to treat a chronic condition. KFF fielded the poll from October 27 to November 2, 2025. <!-- claim: external, source: KFF Health Tracking Poll, published 2025-11-14, verified 2026-09-19 -->

Fitness and coaching apps are likely to count some of these adults among their members, whether or not a member tells the app.

For members treated for weight management, a falling scale weight is the expected direction. A progress view built on the scale then says little about what the training program adds. Circumferences and composition estimates, shown next to training history, can make that contribution easier to see. Whether visible progress affects engagement and retention is a separate question, taken up in [visual progress tracking for GLP-1 adherence and retention](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/).

## How a fitness app can track body composition during GLP-1 treatment

On the app side, the workflow covers a baseline, check-ins, capture conditions, a progress view, and a route for clinical questions.

- **Baseline.** The first scan takes place at onboarding or at the start of a strength program. It uses the same guided capture as every later scan.
- **Check-ins at defined points.** Scans follow the training plan, for example at the end of each training block.
- **Repeatable capture conditions.** Members wear similar clothing and scan at about the same time of day, in the same setting. The guided flow checks pose and capture quality.
- **One progress view.** Weight, circumferences, and composition estimates appear together, next to training history. Labels mark which values are estimates.
- **A route for clinical questions.** Questions about medication, side effects, or muscle health go to the member's clinician. The app's own content stays on training and progress.

(Image 1) - Concept

Two parts of this workflow are hard to repair later: the baseline and the capture conditions. A baseline skipped at onboarding cannot be taken afterwards, and scans taken in different clothing or settings stay hard to compare.

The workflow runs the same way whether or not the app knows about a member's medication.

## Where FitXpress fits

(Image 2) - Concept

The FitXpress software development kit (SDK) embeds guided two-photo capture, front and side, in the app. Results arrive in under 45 seconds. The outputs include 80+ body measurements, body composition estimates (body fat percentage, fat mass, and lean mass), and a 3D model. BMI and basal metabolic rate (BMR) are included as calculated metrics. <!-- claim: FX-006 --> <!-- claim: FX-005 -->

For progress views, FitXpress compares two scans that the app selects. Composition estimates apply established formulas to model-generated measurements and profile values, such as height and optional weight. The lean mass figure is an estimate and does not measure muscle.

Reference methods for body composition include dual-energy X-ray absorptiometry (DXA) and professional bioelectrical impedance analysis (BIA). FitXpress is not equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods.

What counts as adequate performance depends on how the measurements will be used. For a trend view, repeatability is especially important, because each check-in is compared with an earlier scan. Accuracy against a reference is evaluated separately.

Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy. <!-- claim: FX-002 -->

A separate internal validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. The [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the validation population these figures apply to. <!-- claim: FX-001 -->

A weight-loss management platform ran 34,000 FitXpress scans in 2025. It used them for periodic check-in progress tracking, 3D visualization, and body composition context. [FitXpress for connected and digital fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) describes the in-app user flow and integration. <!-- claim: FX-007 -->

## What the app, the prescribing program, and FitXpress each handle

When a member on GLP-1 treatment also uses a separate fitness app, two organizations hold parts of the progress record.

| **Role** | **Responsible for** | **Uses body data to** |
|---|---|---|
| Prescribing clinician or GLP-1 program | Medication, dosing, side effects, and any clinical assessment of muscle or nutritional status | Review progress alongside clinical information, where its protocol includes body data |
| Fitness or coaching app | Training programs, progress views, and member communication | Show measurement and composition trends next to training history |
| Member | Completing scans and choosing what to share with each service | See change beyond the scale reading |
| FitXpress | Body measurements, body composition estimates, a 3D model, and scan-to-scan comparison | Supply structured records to the app or program that integrates it |

FitXpress is not a medical device. It does not provide dose calculations, symptom tracking, prescribing recommendations, or automated clinical decision support. Medication and treatment decisions stay with the prescribing clinician.

## Scale weight, body composition estimates, and reference methods: which fits when

Each method answers a different question, and one program can use more than one.

### Scale weight alone fits when

- The app only needs a general weight trend.
- Members check in rarely or decline body scans.
- No training program in the app depends on composition context.

### Body composition estimates fit when

- Members follow a strength program inside the app.
- Coaches review check-ins as part of the program.
- Capture conditions can be kept similar from one scan to the next.
- The app labels estimates and explains their limits.

### A reference method fits when

- A clinical protocol or study requires DXA or professional BIA.
- A clinician needs an assessment of muscle health or function.
- The result feeds a clinical decision.

Consumer smart scales estimate composition through bioelectrical impedance, and readings depend on the device and the measurement conditions. [Remote body measurement for online fitness coaching programs](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/) compares scales, tape measurements, photos, BIA, DXA, and mobile scans method by method.

## Fitness apps and GLP-1 programs this workflow fits

- **Subscription fitness apps** with strength programs, recurring check-ins, and members who may be taking GLP-1 medications.
- **Coaching platforms** where human coaches review member check-ins.
- **GLP-1 programs** that add training features to their own GLP-1 app. [Structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) covers that setting. Programs comparing vendors can start with [body composition and progress-tracking tools for remote GLP-1 clinics](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/).

Fit is lower for apps without a check-in cadence or a training program, and for apps with no defined use for composition data.

## Implementation and evaluation considerations

**Consent and data sharing.** Photos, body measurements, and 3D models may be personal data, and body composition outputs can be health data, depending on use. When the app and a GLP-1 program are separate organizations, record sharing depends on the member's consent and on agreements between the two. The [FitXpress data privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) covers storage, retention, and deletion. It also sets out how deployments work under the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR).

**Change thresholds.** The app team sets the difference between two scans that is worth showing to a member. That threshold should reflect observed scan-to-scan variation and the interval between check-ins.

**An alternative path.** FitXpress was not specifically trained on data representing people with physical disabilities. Its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. For those members, the app can offer manual measurements or a weight-only progress view.

**Pilot measures.** A pilot can track scan completion, repeat check-in completion, use of the progress view, and clinical questions routed out of the app. Measures the app already records before launch, such as check-in rates, can be compared with a pre-pilot baseline.

## Frequently asked questions

### Can a mobile body scan measure muscle loss during GLP-1 treatment?

A FitXpress scan does not measure muscle or muscle loss. It estimates lean mass from body measurements and profile values, and [a review by Neeland and colleagues](https://pubmed.ncbi.nlm.nih.gov/38937282/) notes that lean mass includes more than muscle. Where a protocol requires a reference method such as DXA, that method applies. The [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out how scan results are evaluated.

### How often should a fitness app scan members on GLP-1 treatment?

The interval depends on the size of the expected change compared with typical scan-to-scan differences, and on the length of the training block. A scan at the end of each block ties the comparison to the training completed. The prescribing clinician or GLP-1 program sets any clinical schedule separately.

### Does a fitness app need to know whether a member takes a GLP-1 medication?

Not for body composition tracking itself, because the scan and the progress view need only photos and basic profile details. Asking about medication is a health-data decision that involves purpose, notice, and consent. The [FitXpress privacy and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) explains how long scan records are kept and how deletion works.

## Next steps

Compare the app's current progress view with what members on GLP-1 treatment need to see. Then [see how FitXpress supports body composition tracking in connected and digital fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).
