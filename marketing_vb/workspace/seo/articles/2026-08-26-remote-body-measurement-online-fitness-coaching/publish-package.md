---
slug: remote-body-measurement-online-fitness-coaching
product: fitxpress
status: ready_for_review
created: 2026-08-31
revision: 2
checkpoint: "2 (second re-run) - final text + meta, regenerated after external review round 2"
source_draft: draft-v4-revision2.md
review_source: review2-comments.md
governing_ruling: "Vadim, 2026-08-31: «всі формулювання тут точні і бери як головний істочнік» - Review 2 wordings are the primary source for this article and outrank the internal guardrail files on wording"
known_exception: "detector hard fails x2 (positioned_as) - approved, see the declaration block below"
supersedes: "publish-package-v2-20260831.md (written against draft-v3-revision1.md, pre-review-2 text)"
---

# Publish Package: remote-body-measurement-online-fitness-coaching (revision 2)

> **Second re-run of checkpoint 2.** The 2026-08-31 morning package was built on `draft-v3-revision1.md`.
> External review round 2 (`review2-comments.md`, 20 numbered corrections) then rewrote claim sentences,
> reversed the medical-device decision, cut the FAQ from 7 questions to 5, added two external sources and
> took the article down 9.3% in length, so that package no longer describes the text it was written for.
> It is preserved verbatim at `publish-package-v2-20260831.md` and is superseded by this file.
>
> **Single source for the body: `draft-v4-revision2.md`.** `draft-v3-revision1.md` and `draft-v2-final.md`
> are history.
>
> **STOP after this file. Do not publish until Vadim approves the text and the meta together.**

---

## 0. DECLARED EXCEPTION - read before publishing

**This article ships with a known, approved guardrail exception. It is not an oversight.**

`detect-ai-tells.py` returns **`VERDICT: HARD FAILS (2)`** on the final text. Both fails are the same
category, `positioned_as`, and both are the phrase **"FitXpress is not positioned as a medical device"** at
line 19 (scope note) and line 146 (`What FitXpress does not do`).

- That phrasing is **required by review item 1** and is covered by Vadim's ruling of 2026-08-31,
  «всі формулювання тут точні і бери як головний істочнік».
- It is **banned** by `brand-assets/content-strategy/terminology-guardrails.md` (Part 2 §2.10) and by
  CLAUDE.md §6 / §15 hard requirement #7, which prescribe the direct form "FitXpress is not a medical
  device". Revision 1 followed the guardrail; the ruling reversed that.
- **The two hard fails do not trigger a STOP** and did not send the text back to `seo-editor`. Nothing
  outside the `positioned_as` category fails: `house_rule_violations: []`, no em dashes, no banned words,
  no other hard category.
- Whoever publishes should know the house detector will keep flagging this article until the guardrail file
  and the detector's allowlist are reconciled (open item B1).

Full detector output, run in this session, is in section 2. It is quoted, not estimated.

---

## 1. Meta

**Recommended title (57 chars):**
Online Fitness Coaching Programs: Remote Body Measurement

**Recommended description (150 chars):**
Online fitness coaching programs can capture client body data from a guided two-photo scan. See how it fits check-ins and what a pilot should measure.

**Slug:** `remote-body-measurement-online-fitness-coaching` (unchanged; matches the draft frontmatter and the
working folder).

**Category:** AI in Fitness (Hub 1, `ai-in-fitness-industry`), sub-category / tag: Digital Coaching.
Recommended URL, matching the pattern of the adjacent articles in this hub:
`https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/`. Not confirmed against a
live CMS taxonomy list, so flag it if the hub uses a different taxonomy field.

**Brand suffix:** not applied. `| 3DLOOK` is allowed only when the title is 49 chars or fewer without it;
the recommended title is 57.

### What changed against the morning package, and why

The morning recommendation was *"Online fitness coaching programs can capture client body data from a
guided phone scan. See how it fits check-ins and what a pilot should measure."* (146 chars).

1. **"what a pilot should measure" survives, and it was checked against the final structure, not assumed.**
   The article still carries a dedicated `## How to evaluate a pilot` section with seven instrumented
   measures, and the section still leads on scan completion and retake rates. The pointer is accurate.
2. **"guided phone scan" became "guided two-photo scan".** Review items 4 and 5 spent two corrections on
   making sure nothing in the article implies a phone measures a body or that Smart Scales is hardware. The
   article's own words are "the client takes two photos, front and side". The description now uses the same
   mechanism wording, which costs 4 characters and removes the last place in the metadata where a reader
   could infer direct measurement.
3. **Nothing promised.** No outcome, no engagement or retention effect, no "precise weight" (review item 6
   reserved "precise" for a calibrated scale, and the description does not use the word at all), no
   audience-reaction claim of the "clients trust" kind that review 1 stripped from the body. The verbs are
   "can capture" and "see how it fits", both of which the article delivers on.
4. **Head term at character 1.** `online fitness coaching programs` (100/mo, US, difficulty unmeasured)
   opens both the title and the description, appears once in the description, and the description does not
   restate the title.

**Head term vs H1.** The H1 and the `content-plan.md` row (line 75) use *"Remote Body Measurement for
Online Fitness Coaching Programs"*, which puts the head term in the last four words. The recommended title
reorders to front-load it; title tags do not have to match H1 verbatim. Variant 3 keeps the exact H1
wording if title/H1 consistency should win.

---

## 2. AI-tells detector, actually run on the final text

Command as specified, run by me in this session against `draft-v4-revision2.md`:

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/2026-08-26-remote-body-measurement-online-fitness-coaching/draft-v4-revision2.md \
    --channel article --summary
SEO / blog article · en · 2750 words
AI density: 1.09/1000 (budget 6.0) -> low
VERDICT: HARD FAILS (2) — fix every hard_fails entry and the house-rule violations; the rest of the draft is sound (density 1.1/1000 (budget 6.0)).

HARD FAILS:
  [positioned_as] x2: 'not positioned as' (L19)

TOP SOFT MARKERS:
  2x 'not positioned as' (L19)
  1x 'rather than' (L25)
```

JSON form of the same run (no `--summary`), the fields the checklist asks for verbatim:

```
"total_words": 2750
"total_markers": 3
"ai_density_per_1000_words": 1.09
"density_budget": 6.0
"severity": "low"
"hard_fails": [{"category": "positioned_as", "count": 2,
                "hits": [{"marker": "not positioned as", "line": 19, ...}]}]
"house_rule_violations": []
"markers_by_category": {"positioned_as": 2, "corrective_contrast": 1}
"style_metrics": {"em_dashes": 0, "bold_count": 13, "title_case_headings": 0, "emoji_count": 0,
                  "bullet_lines": 16, "list_to_prose_ratio": 0.4, "wall_of_text": false,
                  "punch_triads": [], "punch_triad_count": 0,
                  "rhythm": {"sentences": 79, "mean_words": 25.4, "variation": 0.51,
                             "monotone": false, "uniform_paragraphs": false}}
```

Exit code 0 on both runs (the script exits 0 and reports the verdict in its payload). No permission prompt
and no workaround: the `settings.json` fix from 2026-08-26 is holding, so this is a measurement.

**Reading the output.** Every hard fail is in the `positioned_as` category (section 0). The summary prints
only the first line for a repeated marker; the second occurrence is at L146, confirmed by grep:

```
$ grep -n "positioned as" draft-v4-revision2.md
19:*Scope note: ... FitXpress is not positioned as a medical device and does not make clinical or eligibility decisions.*
146:FitXpress is not positioned as a medical device. It does not diagnose conditions, ...
```

The single soft marker, `corrective_contrast` at L25 ("caused by placement rather than body change"), is
review item 14's own mandated wording and was left as written. Density fell inside budget by a wide margin
(1.09 against 6.0) and the rhythm checks pass (variation 0.51 against the 0.35 monotone threshold,
`uniform_paragraphs: false`, zero punch triads).

**Nothing fails outside `positioned_as`.** If it had, this package would say STOP instead of shipping.

### Supplementary mechanical checks (my own greps on the body of `draft-v4-revision2.md`)

| Check | Result |
|---|---|
| Em dash / en dash | 0 |
| `±` character | 0 |
| `DEXA` | 0 (DXA throughout, expanded at first use in running text) |
| `GLP-1` / `glucagon` | 0 (review item 2) |
| Banned words (leverage/utilize/utilizing/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/unleash/game-changer/revolutionary/cutting-edge/disrupt/best-in-class/most accurate) | 0 |
| `the reader` / `the audience` / `the following sections` / `see below` | 0 |
| `this article` / `this guide` / `our content` | 0 |
| `by hand` | 0 |
| `objective` | 0 |
| `let` / `lets` (banned verb) | 0 |
| `plus` as a connector | 0 (word absent entirely) |
| `so` (any occurrence, including the benefit shape) | 0 (word absent entirely) |
| `, not ` corrective negation | 0 |
| `rather than` | 1 (L25, review item 14's mandated wording; soft, licensed) |
| `we` / `our` / `us` / `you` / `your` | 0 |
| Presumed audience reaction phrases | 0 |
| `positioned as` | 2 (L19, L146) - the declared exception |
| FX-004 markers (`ISO 8559`, `0.40 cm`, `1,152`, `14 companies`, `multi-company`) | 0 |
| Named competitors (Prism, Bodygram, Size Stream, Mirrorsize, Styku, Naked Labs) | 0 |

### Length, recounted rather than inherited

| Measure | Value | Method |
|---|---|---|
| Body words, tables included | **2,644** | `sed -n '13,$p'` (H1 to end), HTML comments stripped, `wc -w` |
| Body words, table rows excluded | 2,348 | same, minus lines beginning `|` |
| Detector tokenisation | 2,750 | `detect-ai-tells.py` |

The frontmatter's `word_count: 2644` matches my independent count exactly, and it now carries its method on
the same line, which is what review item "Length and repetition" asked for. The three-way disagreement the
reviewer flagged in v3 (frontmatter 2,582 vs reviewer ~2,980 vs detector 3,015) cannot recur: v3's number
was a table-excluded count being compared against table-included ones.

### Frontmatter: production notes gone, verified

The draft's frontmatter is now nine keys and nothing else: `slug`, `product`, `title`, `author`, `date`,
`status`, `word_count`, `claims_verified`, `review_source`. `changes_summary`, `self_check` and
`revision_note` are absent, along with all detector commentary and any discussion of reviewer conflicts.
That material lives in `changelog-revision2.md` and `log.md`, which is where the review told it to live.

### External sources, verified independently of the draft

Both sources review 2 named are present, in one paragraph of the method-comparison section (L77), on
descriptive anchors, with the journal named in the sentence:

| Anchor | URL | Used for |
|---|---|---|
| "study of altered hydration status and bioelectrical impedance" | `pubmed.ncbi.nlm.nih.gov/32182203/` | 140 subjects, four successive 500 mL water intakes, body fat mass overestimated by 2.08-7.92% (males) and 3.4-9.4% (females) |
| "methodology review of DXA in athletes and active people" | `pubmed.ncbi.nlm.nih.gov/25029265/` | few studies detail their scanning protocol; a standardized protocol proposed as the condition for detecting small changes |

Both are peer-reviewed journals indexed in PubMed, i.e. neutral high-quality third-party sources, not
vendor blogs. Neither is used to attack the method it describes and neither is presented as validating
FitXpress. **This closes the "zero external sources" gap** that had been open since 2026-08-26 and was
capping `quality-controller` category B at 3.

### BOFU link, re-checked in this session

```
$ curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/
200
```

HTTP 200, empty redirect target, so no 404 and no redirect. It is also the exact URL named in
`content-plan.md` line 75 for this row. **The BOFU URL path debt is closed for this article** and is not
re-listed as an open item.

---

## 3. Checklists

Every item below was checked against `draft-v4-revision2.md` in this session. Nothing is carried over from
the morning package on trust.

### 3.1 SEO checklist (15 points)

1. ✅ **Primary keyword in H1, first paragraph, 1-2 H2.** `online fitness coaching programs` appears 4
   times: H1 (L13), intro paragraph 1 sentence 2 (L15, "Remote body measurement is how online fitness
   coaching programs close that gap"), the H2 at L21 ("The measurement problem in online fitness coaching
   programs"), and FAQ question 1 (L152). Exactly one H2 carries it, inside the 1-2 band, no stuffing.
2. ✅ **Meta title 57 chars (limit 60), head term at character 1**, so the first-half rule is satisfied
   trivially.
3. ✅ **Meta description 150 chars**, inside the 140-160 band and under the 155 ceiling set for this task.
   Head term once, at character 1. Does not restate the title.
4. ✅ **All numbers trace to approved claims or to a cited source.** Every numeral in the body was
   extracted and mapped. Product figures: `80+`, `under 45 seconds` (FX-005), `96 to 97%` (FX-001),
   `1.5 to 2.0 cm` (FX-002), `less than 1 cm` (FX-003), `approximately 3.5%` (FX-006), `30 days` (FX-007),
   `9+ years` / `150K+` / `30K+` / `430K+` (FX-008). External figures: `140` subjects, `500 mL`, `2.08%`,
   `7.92%`, `3.4%`, `9.4%`, all from PMID 32182203 and attributed in the sentence. FX-004 is absent, so it
   is never combined with FX-001/FX-003. Remaining numerals are neutral scenario references (week eight,
   six-week block, twelve-week challenge, half an inch, two photos, four stages). The invented "two hundred
   remote clients" from v3 is gone (review item 11), and so is the illustrative "1.4 cm" from v2.
5. ✅ **No banned words.** Zero matches across the CLAUDE.md §6 list plus `utilize`/`utilizing` and the
   anti-positioning pair `best-in-class` / `most accurate` (table in section 2).
6. ❌ **Word count outside the plan's target band.** Body is 2,644 words including tables (2,348 excluding
   table rows; detector 2,750). `plan.md` "Article meta" states "Estimated words: ~2,000 (range
   1,900-2,300)", so ±10% of the target is 1,800-2,200 and the article is 20% above the top of that band on
   the table-included count, 7% above on the table-excluded count. It **is** inside the `context-pack.md`
   band ("1,800-2,800 words typical for a P1 supporting article in this hub"). Marked ❌ against the literal
   rule rather than re-defining the target to make it pass, as both earlier packages did. **What changed
   this round:** review 2 asked for a 10-15% cut and got 9.3% as shipped (2,916 → 2,644), or 13.3%
   excluding the 118 words of citations the same review commissioned. Two reviews have now added required
   content (the coaching-stage table, the pilot-metrics section, two evidence sentences) to an article whose
   plan estimate predates both. Recommendation: Vadim accepts the length, or asks for a further trim, which
   would now mean cutting reviewer-mandated content.
7. ✅ **Intro hook inside the first 2 sentences.** Sentence 1 (L15): "Managing a large remote roster means
   nobody is in the room to put a tape measure around a client's waist, and the measurement still has to
   happen." Sentence 2 names the mechanism and the head term. Review item 11's rewrite kept the hook and
   dropped the invented number.
8. ✅ **CTA placement and type match the intent.** MOFU evaluation link at the end of `Where FitXpress
   fits` (L87, "Programs at the comparison stage can review how FitXpress supports remote progress tracking
   for coaching programs before scoping a build"); BOFU line in the conclusion (L176, "Explore FitXpress
   for connected and digital fitness, or book a demo"). `plan.md` H2.12 specifies exactly this pair,
   evaluation stepping to direct, demo-only with no self-serve trial. Both CTA URLs return HTTP 200.
9. ✅ **No generic AI patterns.** Detector: 0 em dashes, 0 punch triads, 0 title-case headings, sentence
   variation 0.51 against a 0.35 monotone threshold, `uniform_paragraphs: false`, `wall_of_text: false`,
   density 1.09/1000 against a 6.0 budget. The v3 three-clause intro sentence a human reviewer might have
   heard as a triad was rewritten in this round and is now two clauses plus a separate sentence.
10. ⚠️ **Terminology guardrails: every hard ban clear except the one declared exception.** Zero em dashes,
    zero `objective`, zero reader/audience/below references, zero `this article`, zero `by hand`, zero
    `let`, zero `plus` connector, zero `so` connector (the word is absent entirely), zero presumed
    reactions, zero behaviour attributed to concepts, zero corrective negation, zero `we/our/you`. Links sit
    on descriptive anchors. **`positioned as` appears twice**, which is a hard ban in
    `terminology-guardrails.md` Part 2 §2.10 and is the exception declared in section 0, ruled by Vadim on
    2026-08-31 in favour of the reviewer's wording. Marked ⚠️ rather than ✅ so the departure stays visible,
    and not ❌ because it is an authorised instruction rather than a drafting slip.
11. ✅ **Abbreviations (M1 plus the 2026-08-25 exception).** Expanded at first use in running text: BMR
    (L33), BIA and DXA (L65), API and SDK (L83), HIPAA, GDPR and AWS (L101), CTO (L140). Left bare,
    correctly: BMI (L33), CEO (L140). `DEXA` zero. `GLP-1` no longer appears at all, so the abbreviation it
    used to require is moot. **Nuance, recorded not hidden:** BIA and DXA appear first inside the section
    heading at L63 and are expanded in the first sentence beneath it, because the heading is the reviewer's
    verbatim wording. A mechanical M1 check will see the heading first.
12. ⚠️ **Medical framing: the reviewer's wording, not the guardrail's.** The article says "FitXpress is not
    positioned as a medical device" twice (L19 scope note, L146 boundary section), plus the intended-use
    sentence "It does not diagnose conditions, make clinical decisions, or determine treatment eligibility"
    and the conditional reference-method boundary. CLAUDE.md §6 and `terminology-guardrails.md` require the
    direct form "FitXpress is not a medical device". Review item 1 required this exact phrasing, calling the
    guardrail-based refusal "unacceptable because the corporate instruction takes precedence", and Vadim
    ruled for the reviewer. Marked ⚠️ for the same reason as item 10: the boundary is stated and complete,
    the wording departs from the internal rule by instruction. See section 0 and open item B1.
13. ✅ **Links on meaningful anchors; third-party sources are neutral and high-quality.** 7 links, all on
    descriptive anchors, no bare URLs, no "click here". 5 internal `3dlook.ai`, **2 external peer-reviewed
    PubMed citations** (table in section 2). No vendor blogs. This is the first version of this article with
    any external source, which closes the gap that capped `quality-controller` category B.
14. ✅ **AI-tells detector genuinely run**, both forms, output quoted verbatim in section 2 with the
    density, severity, hard fails and house-rule violations reproduced as the checklist requires. No
    estimate anywhere in this package. The verdict is HARD FAILS (2) and both fails are the declared
    exception, which is stated in section 0 rather than buried here.
15. ✅ **Images / alt text suggestions** provided in section 6, refreshed for the final section set (the
    FAQ block shrank, two evidence sentences landed inside the comparison section). `visual-brief` still
    runs after approval per CLAUDE.md §9, so these are directional, not a brief.

**Result: 13 ✅, 2 ⚠️ (items 10 and 12, the same authorised exception counted twice), 1 ❌ (item 6, word
count against the plan estimate).** Scored the way the checklist is written, that is **14/15 passed** with
the two ⚠️ counted as passing-by-ruling and item 6 the single failure.

**Honest arithmetic, stated rather than smoothed over:** without Vadim's ruling, items 10, 12 and 14 would
all be ❌, that would be four failures including one in the positioning block, and this package would say
STOP. The ruling is what makes it shippable, which is why it is quoted in the frontmatter and declared in
section 0.

### 3.2 Content strategy checklist (9 points, `content-strategy-guidelines.md`)

1. ✅ **Correct hub.** AI in Fitness (Hub 1, live at `content-hub/ai-in-fitness-industry/`, published
   2026-07-31), Digital coaching cluster, exactly as `content-plan.md` line 75 and `plan.md` record. The
   up-link at L17 points at that hub.
2. ✅ **action_type respected.** `create net-new` with `existing_urls: []` on the row. Nothing was refreshed
   or sectioned into an existing page.
3. ✅ **No duplication of existing_urls; cannibalization guardrail held.** The row's guardrail is "Targets
   coaches/platform workflows, not generic apps. BOFU → `/fitxpress/for-connected-and-digital-fitness/`."
   Every section serves a coach or platform workflow: the measurement problem, the outputs, the workflow,
   reading the results, the method comparison, integration, pilot evaluation, best fit and limits. The hub's
   broad overview is referenced in a single clause and not restated. This round **strengthened** the
   guardrail: removing the GLP-1 clause (review item 2) took out the one string that pointed at another
   cluster's territory. The legacy `ai-body-scanning-for-fitness` page sits on its own `content-plan.md`
   row (line 81, Review / decide, P2), so it is a separate decision on a different URL, not a breach by this
   article. Carried as open item B2.
4. ✅ **Vertical boundary held; scope note present.** The scope note is the third block under the H1 (L19)
   and names the layer and the non-clinical boundary. Zero `GLP-1`, zero wellness-rewards language, zero
   underwriting, employment or clinical-trial framing. Fitness owns digital coaching, progress visibility
   and engagement, which is exactly the ground the article stands on.
5. ✅ **Internal links in all 4 directions**, counted from the link extraction in section 2: **up ×1**
   `content-hub/ai-in-fitness-industry/` (L17), **sideways ×1** `content-hub/body-scanning-technology-comparison/`
   (L79), **trust ×1** `content-hub/mobile-body-scanning-accuracy/` (L97), **down ×2**
   `fitxpress/for-connected-and-digital-fitness/` (L87 mid-article evaluation, L176 conclusion CTA, two
   different anchors, both plan-sanctioned). 1/1/1/2 verified by URL count.
6. ✅ **FAQ section present and GEO/AEO-friendly.** **5 questions** (down from 7 this round: review 2
   removed "How do clients take the measurements?" and "What body data does it capture?" as body restatements).
   Answer lengths measured: 3, 3, 2, 2, 2 sentences, all inside the 2-5 rule. The two boundary FAQs
   `plan.md` required (cannot replace scale/BIA/DXA; the coach decides) both survive.
7. ✅ **"What FitXpress does not do" present; no banned positioning claims.** Present at L144, followed by
   the positive scoping sentence. Checked against the §8 ban list: no "most accurate", no guaranteed
   compliance, no automatic fraud detection, no underwriting/hiring/clearance decisioning, no standalone
   medical authority, and **no universal replacement claim** (the reference-method boundary is conditional:
   "not equivalent to DXA, BIA, or a calibrated scale where a workflow or protocol requires those reference
   methods"). No named competitors. **Heading-level note for CMS:** the section is an H3 inside `Best-fit
   coaching programs and limitations`, because the reviewer's section order has no standalone slot for it.
   Anyone generating a table of contents or Article schema from H2s should know the boundary block sits one
   level down.
8. ✅ **No unsubstantiated medical / legal / underwriting / employment / clinical-trial claims.** Compliance
   is framed entirely on data-privacy grounds (HIPAA, GDPR, encryption, retention, blurring), all under
   FX-007 and the public FitXpress Privacy Policy. Review 2 tightened two legal statements rather than
   expanding them: the consent language became the approved controller/processor split (item 10), and the
   Smart Scales discrepancy sentence became a configurable capability instead of an automatic flag (item 3).
   **Record-keeping gap, declared not hidden:** the controller/processor sentence is new to this article's
   claim set and is not yet in `context-pack.md` approved_claims or `product-info/compliance.md`. It arrived
   as approved reviewer wording under Vadim's ruling, so it is substantiated for this article; the missing
   entry is carried as open item I3.
9. ✅ **Owns one distinct search intent:** how a remote coaching program captures and compares client body
   data across check-ins, and how to evaluate that as a build. Distinct from the hub's broad overview, from
   the accuracy framework, from the technology comparison, and from the GLP-1 and telehealth clusters (now
   more so, with the GLP-1 reference removed).

**Result: 9/9 passed. No ❌.**

### 3.3 STOP-rule arithmetic, stated explicitly

- SEO checklist: **1 ❌** (item 6, word count) plus 2 ⚠️ that are the declared, authorised exception.
  Threshold is 2 or more ❌ per checklist. **Not triggered.**
- Strategy checklist: **0 ❌**. Not triggered.
- Positioning / compliance / cannibalization auto-STOP: **not triggered.** The medical-device wording is an
  instruction from the corporate review, ruled on by Vadim, and the boundary it states is complete. The two
  compliance rewrites narrow what is claimed. The legacy-page overlap is a task on a different URL.
- Detector hard fails: **2, both `positioned_as`, both the declared exception.** The task's own STOP
  condition ("any fail outside the `positioned_as` category") is **not** met, verified against the JSON
  `hard_fails` array, which contains one entry with one category.
- **Nothing returns to `seo-editor`.** What remains is Vadim's approval and two decisions that live outside
  this text.

---

## 4. Open items

The five items below are the complete list from `changelog-revision2.md` §"Open items for Vadim", carried
**verbatim** (blockquoted, including the source file's own punctuation) and split by whether they gate
publishing. Nothing was added to the list and nothing was dropped from it.

### 4A. Blocks publishing

**B1. The "positioned as" exception has to be recorded somewhere other than this package.**
*(positioning / tooling; the article text itself is settled by Vadim's ruling)*

> 1. **`terminology-guardrails.md` still bans "positioned as".** This article ships the corporate wording by
>    ruling, but the guardrail file and the detector are unchanged, so the next article and the next detector
>    run will hit the same conflict. Either record the corporate exception in the guardrail file and add an
>    allowlist entry to `detect-ai-tells.py`, or treat this article as a one-off. Not touched without a
>    decision, since both are sources of truth.

Why this gates publishing rather than sitting in the follow-up pile: publishing puts a live article on
3dlook.ai that fails the house detector on a hard category. That is fine as a decision and bad as a
surprise. What is needed before the article goes live is one line from Vadim confirming the exception is
knowingly accepted, and a choice between recording it in `terminology-guardrails.md` plus an allowlist
entry in `detect-ai-tells.py`, or treating this article as a one-off and leaving both files untouched. No
text change either way: the wording is ruled.

**B2. The older `ai-body-scanning-for-fitness` page: redirect or rescope.**
*(cannibalization, a task on a different URL)*

> 5. **Older `ai-body-scanning-for-fitness` page** (Review 1 item 1): still a separate content-ops decision.
>    Verified 2026-08-31 as live, published 2024-06-12, updated 2026-07-08, H1 "Revolutionizing Fitness
>    Tracking…" — which uses a CLAUDE.md §6 banned word. It sits on its own `content-plan.md` row (line 81,
>    Review / decide, P2), so no cannibalization with this article's row (line 75).

Why this gates publishing: the moment this article goes live there are two URLs in the same hub against
overlapping intent, and the older one carries a banned word in its H1. This article does not breach its own
guardrail (checklist 3.2 item 3), so the decision is about the other page: 301 it here, or rescope it and
keep both. Either is a content-ops task, not an edit to this text.

### 4B. Informational / follow-up, does not gate this article

**I1. Claim records still carry the pre-review wording.**

> 2. **`context-pack.md` claim records still carry the older wording** — FX-006 as `±3.5%`, FX-007 naming
>    SSE-S3. The article now says "approximately 3.5% average prediction error under evaluated conditions"
>    and "encrypted in transit and at rest on AWS". CLAUDE.md §1 and §12 carry the old forms too.

Publisher's note: the article is the corrected version in both cases, and the corrections came from the
reviewer. The risk is the next writer inheriting `±3.5%` and `SSE-S3` from the records and this article
reading like the outlier.

**I2. Repeatability convention.**

> 3. **`about-me.md` locks repeatability as `< 1 cm`;** the reviewer's mandated sentence spells "less than
>    1 cm". Reconcile at source rather than per article.

Publisher's note: the shipped text says "less than 1 cm" twice (body L97, FAQ L162) and `< 1 cm` zero times.
Either answer is a two-string edit; the point is that the two sources disagree and the next article hits it
again.

**I3. The controller/processor statement has no claim record.**

> 4. **The controller/processor statement is new to this article's claim set.** It came from the review as
>    approved wording; it is not in `context-pack.md` approved_claims and has no proof-point entry. Worth
>    adding to `product-info/compliance.md` so the next article can use it without a fresh ruling.

Publisher's note: substantiated for this article by the ruling, so it is not a ❌ on checklist 3.2 item 8,
but it is a legal-role statement with no entry behind it, which is worth fixing before it is reused.

### 4C. Closed this round, recorded so nobody reopens them

- **BOFU URL path debt: closed.** `/fitxpress/for-connected-and-digital-fitness/` re-verified live in this
  session (HTTP 200, no redirect, section 2), and it is the URL named in `content-plan.md` line 75. Linked
  twice, both links good.
- **Sideways-link omission: closed.** `content-hub/body-scanning-technology-comparison/` at L79 gives the
  article all four link directions (1 up / 1 sideways / 1 trust / 2 down).
- **Zero external sources: closed.** Two peer-reviewed PubMed citations at L77, both neutral high-quality
  third-party sources. This was the gap capping `quality-controller` category B at 3.
- **Medical-device wording conflict: closed as a decision** (was the morning package's item 4A.1). Vadim
  ruled for the reviewer on 2026-08-31. What remains is the tooling reconciliation, B1, not the wording.
- **`GLP-1` in the boundary section: closed**, zero occurrences (review item 2).
- **`±` and `DEXA`: closed**, zero occurrences.
- **Frontmatter production notes: closed**, verified key by key in section 2.
- **Detector estimated instead of run:** closed for the second package in a row. Run twice here, output
  quoted, exit codes stated.
- **Three-way word-count disagreement: closed.** One number in the frontmatter with its method on the same
  line, independently recounted in section 2.

---

## 5. Alt options

### Meta title variants

1. **Online Fitness Coaching Programs: Remote Body Measurement** (57 chars) - **RECOMMENDED.** Head term at
   character 1, keeps the secondary phrase `remote body measurement` (difficulty 26) intact in the string,
   reads as the same topic as the H1.
2. **Online Fitness Coaching Programs: Remote Body Data Workflow** (59 chars). Head term still at character
   1, and "Workflow" is the truer label for the final article, which is now a workflow, a coaching-stage
   table, a method comparison and a pilot-evaluation section. Costs the `remote body measurement` phrase
   match.
3. **Remote Body Measurement for Online Fitness Coaching Programs** (60 chars). The exact
   `content-plan.md` line 75 and H1 wording. Use if title/H1 consistency should beat front-loading; the head
   term lands at character 29, inside 60 but not front-loaded.

### Meta description variants

1. **Online fitness coaching programs can capture client body data from a guided two-photo scan. See how it
   fits check-ins and what a pilot should measure.** (150 chars) - **RECOMMENDED.** Head term first, exact
   capture mechanism, then the two blocks the reviews built up (check-in fit, pilot measurement). No promised
   outcome, no retention effect, no "precise", no audience-reaction claim.
2. **Online fitness coaching programs can capture client body data from a guided two-photo scan. See how it
   fits check-ins and where the data stops.** (143 chars). Same opening, and it carries the article's
   stated-limits posture into the SERP instead of the pilot pointer. Use if the limits are the more useful
   promise for this buyer.
3. **Online fitness coaching programs need client records that compare across weeks. See how a guided
   two-photo scan fits check-ins, with its limits stated.** (151 chars). Leads on comparability, which is the
   actual argument of the article's second section. Softest hook of the three.

**Rejected on purpose:** anything built on "clients trust", "visible progress", "retention gains" or
"precise weight". Review 1 deleted the first three claims from the body and review 2 item 6 reserved
"precise" for a calibrated scale, so a meta tag promising any of them would advertise a claim the article
does not make.

---

## 6. Images / alt text suggestions

Refreshed for the final section set. No visual brief exists yet: `visual-brief` runs after Vadim approves
this package (CLAUDE.md §9), so these are directional. `DESIGN.md` tokens only, electric blue `#143DFF`,
navy `#050F40`, Satoshi. No clinical or lab imagery anywhere, this is the non-clinical Fitness vertical. No
ranked or scored leaderboard of methods: the comparison is by role, not by winner.

1. **Hero / OG image.** Split composition: a smartphone in guided-capture pose (front and side silhouette
   outline with an on-screen framing guide) beside a two-model side-by-side progress comparison. Two photos,
   not a scanning beam or a body-tracking mesh overlay, because review items 4 and 5 spent two corrections
   removing any suggestion of direct measurement.
   **Alt:** "Smartphone capturing a guided two-photo body scan beside a side-by-side 3D progress comparison
   for an online fitness coaching program."
2. **Five-output diagram, at "What remote body measurement provides".** The five outputs as five distinct
   labelled items, visually grouped by kind: model-generated measurements, software-derived composition
   estimates, calculated metrics, predicted weight, 3D model. Keep the four kinds visually distinct; the
   whole section exists to stop them being read as one number type. Label the predicted weight as software,
   not as a scale.
   **Alt:** "Five outputs from a two-photo body scan: model-generated measurements, software-derived body
   composition estimates, calculated metrics, a software-predicted weight, and a 3D model."
3. **Workflow visual, at "How it fits the coaching workflow".** Four numbered steps matching the list:
   baseline at onboarding, structured outputs generated, results in the coach's view, comparison at each
   check-in. Draw the cadence as configurable (monthly / six-week / twelve-week), since the section's closing
   line is that the cadence stays the program's own.
   **Alt:** "Four-step remote body measurement workflow: baseline capture at onboarding, structured outputs
   generated, results in the coach's view, and comparison at each check-in."
4. **Coaching-stage decision table, at "How coaches can use the results".** Render the four-row table as a
   graphic with the "Limitation" column given the same visual weight as the other three, not set as fine
   print. That column is the point of the section, and the paragraph beneath it now opens on the limitation
   directly (review item 16).
   **Alt:** "Table of four coaching stages with the data reviewed, the possible coach action, and the
   limitation at each stage: onboarding, recurring check-in, apparent plateau, and program completion."
5. **Method comparison table, at "Comparison with scales, tape measurements, photos, BIA, and DXA".** The
   seven-row comparison rendered, keeping consumer smart scale and professional BIA on separate rows and
   keeping the "Limitation to disclose" column visible. Do **not** mark a winning row. If the two cited
   studies are surfaced visually, attribute them in the graphic as published research, since they describe
   BIA and DXA behaviour and are not evidence about FitXpress.
   **Alt:** "Comparison of client self-report, home tape measurement, consumer smart scale, professional
   BIA, DXA, progress photos, and mobile body scan, showing what each provides and its limitation for a
   coaching program."
6. **Pilot-evaluation visual, at "How to evaluate a pilot".** The seven process measures in the article's
   order, with the first two (scan completion, retake rate) visually gated ahead of the rest and engagement
   or retention last. Do not draw an upward trend line or a percentage: the section's argument is that these
   are measured against the program's own baseline, not promised.
   **Alt:** "Seven pilot measures for a remote body measurement rollout, ordered from scan completion and
   retake rates through coach review time to engagement or retention measured against a baseline."

---

## 7. Article (CMS-ready)

Body of `draft-v4-revision2.md` from the H1 to the last line, with the YAML frontmatter removed and every
`<!-- claim: FX-00X -->` and `<!-- source: ... -->` annotation stripped. **Verified by diff:** the only
differences between this text and the draft body are the 11 lines that carried those HTML comments, with no
other character changed, no double spaces and no trailing whitespace left behind. Headings, tables,
emphasis, bold and markdown links are otherwise byte-identical to the approved draft.

Zero production notes, zero revision commentary, zero detector commentary, zero reviewer-conflict discussion
reach this section, as review 2 requires. 2,644 words, 2 tables, 5 FAQ items, 7 links (5 internal, 2
external), 0 em dashes.

# Remote Body Measurement for Online Fitness Coaching Programs

Managing a large remote roster means nobody is in the room to put a tape measure around a client's waist, and the measurement still has to happen. Remote body measurement is how online fitness coaching programs close that gap: a guided smartphone scan covers the measurement component of an intake or a check-in without an in-person appointment.

The operational question is narrower than the technology question. Capture has to fit the check-in cadence a program already runs, outputs have to land in the coach's daily tool, and the limits of the data have to be clear before a progress screen is built on them. Wider background on structured body data across fitness products sits in the [AI in the fitness industry](https://3dlook.ai/content-hub/ai-in-fitness-industry/) hub.

*Scope note: a fitness progress and intake layer for coaching programs, non-clinical. FitXpress is not positioned as a medical device and does not make clinical or eligibility decisions.*

## The measurement problem in online fitness coaching programs

Coaching delivered remotely runs on data the coach never collects in person: a weight read off a home scale, a progress photo taken in whatever light the room offers, sometimes a tape measure wrapped around the client's own waist at a height no two weeks match. How each figure was produced goes unrecorded.

Comparison is where that becomes expensive. A coach adjusting a program at week eight needs both records to have been made the same way. Body weight varies with hydration, food timing, and which scale was used; a self-reported figure records the reading and none of those conditions. A tape held half an inch higher can produce an apparent difference caused by placement rather than body change. What is missing is comparability: records captured the same way each time, at the points where somebody makes a decision.

## What remote body measurement provides

In coaching, remote capture usually means a guided smartphone scan: the client takes two photos, front and side, and software returns a structured record in under 45 seconds. Five outputs come back:

- Model-generated body measurements, 80+ of them, produced from the 3D model the software builds out of the two photos.
- Software-derived body-composition estimates, including body fat percentage, lean mass, and fat mass.
- Calculated metrics such as BMI and basal metabolic rate (BMR), computed from scan outputs and entered profile values.
- A predicted weight from Smart Scales, a software-based predicted-weight output and not a physical scale, with approximately 3.5% average prediction error under evaluated conditions.
- The 3D model itself, which makes a side-by-side visual comparison between two check-ins possible.

Those data types are not interchangeable. A waist circumference is model-generated from the two photos; a body fat percentage is software-derived by applying a formula to model outputs, carrying that formula's assumptions along with the scan's conditions. Composition estimates read best as a trend, and they draw the most attention on a client-facing progress screen, which argues for showing circumference trends beside them.

## How it fits the coaching workflow

The workflow attaches to a cadence that exists: a baseline at the start, then follow-up scans at the check-in points already on the calendar.

1. **Baseline at onboarding.** The client completes the profile step, then follows an on-screen flow to take two photos, front and side, with guidance that corrects framing and pose. Weight is optional in supported workflows, since Smart Scales predicts a figure from the photos; where a self-reported weight is also supplied, the platform can compare the two values and configure discrepancy logic, though an automatic flag is not universal across fitness implementations. BMI depends on height and weight both being available.
2. **Structured outputs generated.** Processing returns the five outputs as structured data.
3. **Results appear in the coach's view.** Outputs land in the coaching platform where clients are reviewed, which, depending on how results are stored and displayed, can remove the parallel spreadsheet and the manual entry of tape figures.
4. **Comparison at each check-in.** A follow-up scan lines up against the baseline: the coach sees which measurements moved and by how much, and the client sees the two 3D models side by side.

The cadence stays the program's own, whether that is monthly check-ins, six-week training blocks, or one scan at each end of a twelve-week challenge.

## How coaches can use the results

Structured data earns its place only if it changes something a coach does. Four stages cover most programs, each supporting a different action and stopping at a different limit.

| Coaching stage | Data reviewed | Possible coach action | Limitation |
| :- | :- | :- | :- |
| Onboarding | Baseline measurements and 3D model | Establish the starting record | Does not prescribe a program |
| Recurring check-in | Measurement and composition trends | Review progress with other client data | Small changes require context |
| Apparent plateau | Weight and regional measurements | Investigate different progress signals | Cannot determine the cause |
| Program completion | Full longitudinal comparison | Summarize progress | Avoid causal conclusions |

Interpretation is where the limits bite. A scan records a measurement difference between two check-ins; confirming a physical change means weighing that difference against scan-to-scan variation and the conditions of each capture. Nothing in the record says whether a training block, a diet change, or sleep produced the movement. FitXpress supplies the record, and the coach makes the call.

## Comparison with scales, tape measurements, photos, BIA, and DXA

Remote coaching programs draw on six other measurement methods, two of which, professional bioelectrical impedance analysis (BIA) and dual-energy X-ray absorptiometry (DXA), require the client to attend a facility.

| Method | What it provides | Limitation to disclose | Where it fits a coaching program |
|--------|------------------|------------------------|----------------------------------|
| Client self-report | Weight and rough circumferences | Varies by scale, timing, and technique | Low-stakes check-ins |
| Tape measurement at home | Circumferences | Placement varies between sessions | Motivated clients |
| Consumer smart scale | Weight, and an impedance-based composition estimate | Weight varies with device quality and calibration; composition estimates depend on hydration and electrode placement | Daily weight trend at home |
| Professional BIA | Weight and segmental composition estimates | Requires an in-person visit; results depend on device and preparation protocol | Periodic in-person assessment |
| DXA | Reference-grade body composition and regional distribution | Clinic-based and appointment-bound; access and cost depend on the provider | Occasional reference reads |
| Progress photos | Visual change | Lighting, pose, and framing vary; not inherently standardized or quantitative | Motivation and qualitative review |
| Mobile body scan | Measurements, composition estimates, calculated metrics, a predicted weight, and a 3D model | Depends on capture conditions; not a clinical reference method | Standardized intake and progress across a remote roster |

A connected scale gives a direct weight reading, and a calibrated scale remains the right instrument where a precise weight matters. Professional BIA is quicker to run and sensitive to hydration state: a [study of altered hydration status and bioelectrical impedance](https://pubmed.ncbi.nlm.nih.gov/32182203/) in the Libyan Journal of Medicine measured 140 subjects after four successive 500 mL water intakes and found body fat mass overestimated relative to baseline by 2.08% to 7.92% in males and 3.4% to 9.4% in females. DXA is a reference method for body composition in clinical and research settings, and a [methodology review of DXA in athletes and active people](https://pubmed.ncbi.nlm.nih.gov/25029265/) in the International Journal of Sport Nutrition and Exercise Metabolism reports that few studies detail their scanning protocol, proposing a standardized one (rested, overnight-fasted, minimal clothing, consistent positioning) as the condition for detecting small changes with confidence.

Access separates them. DXA and professional BIA require facility access; home scales do not. What none of the three delivers is standardized, comparable capture of circumferences and composition across a whole roster at every check-in, the constraint a coaching program works inside. Differences between scanning approaches, including two-photo capture, video, and hardware booths, are set out in [2-Photo vs Video vs Hardware body scanning](https://3dlook.ai/content-hub/body-scanning-technology-comparison/).

## Where FitXpress fits

FitXpress is the body-data capture and scan-to-scan comparison layer inside a coaching product, integrated through an application programming interface (API) or a software development kit (SDK) that handles guided capture, processing, and the structured output.

3DLOOK provides the capture flow, the five outputs, and the comparison data across scans; the platform builds what the coach and the client see, from program logic and scheduling to how results are presented.

Programs at the comparison stage can review how [FitXpress supports remote progress tracking for coaching programs](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) before scoping a build.

## Accuracy, repeatability, privacy, and implementation

### Accuracy and repeatability

The better question is narrower: accurate enough for which decision? For a coach, that decision is whether a client's waist is trending down across eight weeks and whether the program should change.

Internal validation against expert manual measurements showed approximately 96 to 97% accuracy, with typical absolute error of 1.5 to 2.0 cm, measured as agreement with a manual reference under consistent capture conditions. That condition is why capture guidance matters more in production than a headline figure.

Repeatability carries more weight than one-off accuracy for progress tracking. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm, which makes a modest real change more likely to be distinguishable from capture variation. What counts as accurate depends on the reference method, the capture protocol, the population measured, and the intended workflow, all four set out in the [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/).

### Privacy and consent

Client body data needs a stated privacy posture before the first scan. FitXpress complies with the Health Insurance Portability and Accountability Act (HIPAA) and aligns with General Data Protection Regulation (GDPR) principles. Data is encrypted in transit and at rest on Amazon Web Services (AWS) infrastructure; photos are deleted immediately after processing or retained for up to 30 days by the business client's configuration, and retained photos are automatically blurred.

In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR. That split leaves the coaching program to establish an appropriate legal basis, provide the required notice, and obtain consent where consent is required or relied upon.

### Implementation

**Integration scope.** Scope the first build to one capture point and one comparison view; the platform team owns display, storage, and the progress screen.

**Capture protocol.** Production conditions are not lab conditions: clients scan in odd lighting, in loose clothing, holding the phone at the wrong angle. On-screen guidance and retake prompts do more for real-world results than a headline accuracy figure, which makes capture testing with real clients the first thing to schedule.

**Change thresholds.** Decide in advance what size of change the program treats as meaningful, based on measured scan-to-scan variation. A smaller difference cannot be confidently distinguished from expected scan-to-scan variation, which leaves open whether a real change occurred. Mobile scanning is intended for longitudinal trends across weeks and months; very small short-term changes sit below what it resolves reliably.

**Model maturity.** Behind the outputs are 9+ years of training data, including 150K+ photos, 30K+ 3D scans, and 430K+ measurements, the context a technical buyer asks for during diligence.

## How to evaluate a pilot

A pilot answers process questions before commercial ones. Seven measures are worth instrumenting, each read by the platform from its own data:

- Scan completion and retake rates.
- Usable baseline-to-follow-up comparisons.
- Coach review time per client at a check-in.
- Scheduled check-in completion.
- Support requests generated by the scan step.
- Client use of the progress view.
- Engagement or retention against the program's pre-pilot baseline.

The first two govern everything after them: a high retake rate is a finding about capture guidance, to be fixed before the later measures read as anything. Review time is the measure most often skipped and the one an operations lead asks about first, since coach hours can become the constraint on how many clients a program serves well.

Engagement and retention sit at the end of that list on purpose. A pilot can test whether a progress view moves them against a baseline the program already has; treating that movement as a given defeats the point of running one.

## Best-fit coaching programs and limitations

Remote body measurement fits coaching businesses that deliver remotely and bill on a recurring basis, and its value grows with roster size and the length of the client relationship.

- Online coaching programs running subscription memberships with regular check-ins.
- Digital coaching platforms serving many coaches at once, where measurement consistency has to hold across the base.
- Hybrid personal-training studios extending coaching between in-person sessions.
- Corporate fitness coaching delivered to distributed employees.

Evaluation usually sits with the founder or CEO, the chief product officer, or the head of growth or engagement, with a product manager or chief technology officer (CTO) handling integration.

A solo coach with a handful of local, in-person clients gains little from remote capture, and a program with no recurring revenue has fewer check-ins to standardize.

### What FitXpress does not do

FitXpress is not positioned as a medical device. It does not diagnose conditions, make clinical decisions, or determine treatment eligibility. Software-derived body-composition estimates are not equivalent to DXA, BIA, or a calibrated scale where a workflow or protocol requires those reference methods.

What FitXpress does is narrower: it captures structured body data remotely, standardizes how a coaching program measures clients, and supports comparison from one scan to the next.

## FAQs

**What is remote body measurement for online fitness coaching programs?**

It is capturing a client's body data from their own smartphone, without an in-person appointment. From two photos, front and side, software returns 80+ model-generated body measurements, software-derived body-composition estimates, calculated metrics such as BMI and BMR, a predicted weight, and a 3D model in under 45 seconds. Those are different kinds of output, and knowing which is which matters when a coach reads a trend.

**Can it replace a smart scale, BIA, or DXA?**

No. A connected scale gives a direct weight reading, with a calibrated scale the right instrument where a precise weight matters; BIA and DXA are in-person methods for body composition. A mobile scan complements all three by adding a comparable remote record across scans.

**How accurate and repeatable is it?**

Accuracy depends on the decision, the reference method, the capture protocol, and the population measured. Internal validation put typical absolute error at 1.5 to 2.0 cm; for comparing check-ins, the more relevant figure is scan-to-scan differences of less than 1 cm for most evaluated measurements.

**Is client body data private?**

FitXpress is HIPAA-compliant and GDPR-aligned, with encryption in transit and at rest and photos either deleted immediately or retained for up to 30 days by the business client's configuration. In most enterprise deployments the coaching program acts as controller, responsible for the legal basis, the required notice, and consent where consent is the basis relied upon.

**Does the coach or the tool decide anything?**

The coach decides. FitXpress provides structured body data and scan-to-scan comparison; it makes no recommendations and no program decisions.

## Conclusion and next steps

Remote body measurement changes one operational thing for a coaching program: inconsistent self-reports and progress photos become a structured record captured from the client's own phone, comparable from one check-in to the next, with its limits written down where coaches can see them.

What a program builds on that record is a product decision, and the honest way to find out whether it lands is to instrument the pilot, starting with completion and retake rates. Explore [FitXpress for connected and digital fitness](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/), or book a demo to walk through the workflow with the 3DLOOK team against a specific program.
