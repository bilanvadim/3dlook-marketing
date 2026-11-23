---
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
workspace: 2026-09-21-ai-body-scanning-telehealth-documentation
product: fitxpress
stage: seo-editor
round: Review 1 (EDIT round)
input: v1/final.md + review-1.md + review-1-decisions.md + context pack (FX-013..FX-016 added 2026-11-23)
output: final.md
date: 2026-11-23
verdict: PASS (article_lint 10/10, detector CLEAN 0.0)
previous_report: none (v1 has no editor-report.md; v1 notes are in v1/final.md frontmatter)
---

# Editor report: telehealth documentation, Review 1 round

`review-1-decisions.md` is applied item by item (A to M) to `final.md`, starting from `v1/final.md`. A body diff against v1 touches only those items. These parts are byte-identical to v1:
- S3 "Why record consistency is under pressure now"
- the intro, the scope note, "At intake" and "Before clinician review"
- S7 paragraphs 1 and 3
- the last paragraph of S8
- "Who this fits", FAQ 1-3 and Related reading

N (package deliverables) and the open questions in V belong to seo-publisher, and are listed under Open items. meta.md, publish-package.md, plan.md and v1/ were not touched. Nothing was committed.

## Result per decision

| ID | Status in decisions | Result |
|---|---|---|
| A | ACCEPT, VERBATIM | H1 is now "How AI Body Scanning Supports More Consistent Telehealth Documentation". A `title:` field with the same text was added to the frontmatter (v1 had none). Byline "By Assel Sekerova" and the slug are unchanged. The H1 has no landing primary keyword and keeps "telehealth documentation". |
| B | ACCEPT, VERBATIM | The sentence is its own paragraph directly after the scope note, at 9.1% of prose words (9.4% by `_cta_placement`). The link sits on the reviewer's anchor, and there is no extra action-label line. **Gate M1 failed on "API/SDK"** (`line 18: API used before being expanded…`, same for SDK). Per B's fallback, the terms are expanded at this first use: "application programming interface and software development kit (API/SDK) integration". No other word changed. |
| C | ACCEPT, CHANGED | "What the scan generates" lists the five items in the decision's order. The technical bullet keeps v1's `compliance.md` §3 list and adds: "Not every technical field appears in every API response, in the Admin Panel, or in the program's record system." It does not say which fields appear where. "in under 45 seconds" is unchanged. The next paragraph keeps the measurement / calculated / estimate distinction. |
| D | ACCEPT | Three H3s unchanged. S4 lead: "The program controls that workflow: scan scheduling, the integration, which patient a scan belongs to, documentation requirements, and clinical review." In "Between visits", Body Progress compares two scans the program selects, using their scan IDs. FitXpress keeps no patient timeline, and 3DLOOK does not determine whether two scans belong to the same person. Each sentence has one negation. All carry FX-016. |
| E | ACCEPT | H2 kept. The two-sentence lead says the capabilities work together and API/SDK is primary. **E1** "API/SDK integration" covers four things: capture in the program's own app; outputs via the API or SDK; the customer maps results into its record systems; connecting to an EHR or updating a medical record is integration work on the customer's side. It also carries the in-sentence landing link, anchor "body scanning API for telehealth platforms", at 41.9%. That link replaces v1's "structured body data for…" link and is not a CTA. **E2** opens with the canon line and "It does not replace API/SDK integration or an EHR." Then: seven FX-013 bullets, the FX-014 availability (selected clients, credentials from 3DLOOK, no public sign-up), and the launch-post link. No client or integration tab names, no Clothes Detector. |
| F | ACCEPT | H2 is now "Fragmented inputs and structured records, side by side". All six rows and both columns are kept, and the five structured-column cells are rewritten verbatim. "quicker to read" is gone. The hedge "any gain depends on how much was missing before" and the recalculation sentence are kept. |
| G | ACCEPT | Added "FitXpress is not a clinical diagnostic tool." The other required boundaries were already in v1: medical device, clinician review, DXA/BIA/scales, and high-impact decisions. New closing paragraph: using FitXpress does not by itself make a workflow compliant with HIPAA, GDPR or telehealth documentation rules, and compliance stays with the program and its legal advisors. |
| H | ACCEPT, CHANGED | S8 opens with "Photos are deleted immediately after processing or within 30 days, depending on the customer agreement and instructions." (FX-015). Kept from v1: output retention (now "…or a deletion request applies"), deletion by scan identifier, the anonymized-ID sentence, the HIPAA/BAA sentence, and the FAQ link. The GDPR sentence is now the canonical verbatim form ending "under GDPR." No certification claims. 155 words (v1 145). |
| I | ACCEPT | The five measures are kept in order. Added a numbered five-step framework, verbatim order, one line each. FX-012 is kept where v1 has it. No numbers or outcome claims. |
| J | ACCEPT, target per decision | Closing CTA in Next steps: "Then [book a demo of FitXpress for telehealth intake](landing URL)." This replaces the pricing deep link and is at 84.5%. There is no other promotional text. Touchpoints: B early CTA, E1 contextual link, Next steps closing CTA. |
| K | ACCEPT | The four questions are unchanged word for word. FAQ 4 opens with "Comparability depends on a consistent capture protocol and on the receiving system. Each Body Progress comparison uses two entries the program picks by scan ID." The dataset sentence, the below-1-cm sentence and the framework link sentence are character-for-character v1. FAQ 5 is added verbatim. |
| L | ACCEPT | Checked: no new "AI" (only the H1 and v1's note-taking passages), no "objective", no "What changed" heading. Also none of: client count, roadmap feature, new statistic, patient-history or identity-matching feature. Body composition is called estimates throughout. |
| M | ACCEPT | Each of the seven URLs appears at least once: landing x3 (B, E1, closing), Admin Panel post, privacy FAQ, accuracy framework, hub x2 (S4 + Related reading), engagement, and pharmacy guide (S4 "At intake"). All 11 anchors are distinct. The pharmacy link is kept as a link only. Primary keyword: 4 occurrences (H1, S1 H2, S7, S8). |

## What changed beyond the literal instruction, and why

- **B, M1 expansion** (authorized fallback, see table). Because B now expands API and SDK, E1 uses them bare. v1's S5 expansions moved to B.
- **C, where BMR is expanded.** The decision's list drops v1's bullet sentences on BMR and on body fat, lean mass and fat mass. The BMR expansion (M1) and those three examples moved into the distinction paragraph. That paragraph now has three short sentences in place of v1's one compound sentence. No content is lost.
- **D, positive half of the timeline sentence.** "FitXpress does not keep a patient timeline; that history sits in the program's records." The clause after the semicolon states where the history lives, so the sentence is not a bare denial. Its one negation is kept.
- **E, the record point placed in the lead.** "Either one leaves a timestamped record the program can retrieve months after capture" applies to both routes, so it sits in the H2 lead and not under one H3. This is the "say it once" the decision asks for.
- **E, other choices:**
  - The lead re-uses v1's FX-001 point ("teams that do not want to build a dashboard of their own").
  - v1's homepage link on "FitXpress" is kept.
  - v1's paragraph "The timing of an entry matters… in the same shape every time." is cut. It repeated the record point and claimed "the same shape every time", which F now qualifies.
- **E2 H3 is "FitXpress Admin Panel for scan management"**, not the bare "FitXpress Admin Panel". The detector's house rule flags an H2+ heading when every word over three letters is capitalised. The bare product name tripped it ("Title Case headings: 1"), and the lint hard-bans gate failed. "for scan management" echoes B's "scan-management tools" and FAQ 5's "scan-data management".
- **E2 anchor** reworded to "Admin Panel launch announcement", which the decision allows. The phrase "FitXpress Admin Panel" had become a 3x repeat.
- **E2 CSV** is expanded as "comma-separated values (CSV)". Terminology §1 exempts only the listed commonly known abbreviations. "scan IDs" stays bare: that is `compliance.md` §4's wording and the live pages' usage.
- **F, one reading paragraph.** v1's two paragraphs under the table are merged. Two sentences are cut because they restated table rows in prose: "Manual re-entry falls where…" and "Entries stay comparable over time because…". The corrections hedge survives as "Correction handling stays with the program's record system." FX-003 is no longer cited in S6; it is still cited in S5 and S8.
- **G, split into two sentences and placed as S7's closing paragraph.** The decision gives two clauses joined by a semicolon. Joined, they ran to 37 words, so they are split per editorial-rewrites §8. In paragraph 2 they made the decision paragraph a list of disclaimers. As the closing paragraph they lead into S8. **HIPAA and GDPR are now first used in S7**, so they are expanded there (M1). As a result, S8's HIPAA sentence drops its expansion ("deployments governed by HIPAA"), and S8's GDPR sentence becomes exactly the canonical form.
- **H wording:** "depending on the customer agreement and instructions" avoids "customer agreement and the customer's instructions". "or a deletion request applies" is `compliance.md` §3 wording for the decision's "or a deletion request says otherwise".
- **I:** two sentences are cut because they duplicated the new steps: "Each of those is something the program measures in its own systems." (step 4) and "Baselines taken before launch make the second reading worth having." (step 1). The lead-in "The pilot itself follows this order:" avoids "five measures … five steps".
- **K, FAQ 4 first sentence.** "the capture protocol" became "a consistent capture protocol". The Body Progress sentence is worded differently from S4 on purpose: the first draft ("The program compares scans it selects in Body Progress, by scan ID.") was a 0.67 near-duplicate of the S4 sentence.

## Deviations from VERBATIM lines

1. **B:** "API/SDK" became "application programming interface and software development kit (API/SDK)". This is the decision's own fallback after M1 failed. Every other word, the link and the anchor are the reviewer's. The sentence is 33 words (gate allows up to 6% over 25 and one over 35). If the reviewer wants the bare form, M1 has to waive "API/SDK" at that position.
2. **E2 H3 heading:** "for scan management" was added (Title Case gate, see above). The decision gives the H3 name in quotes, but the item is not marked VERBATIM.
3. **I steps:** the decision's phrases, each capitalised and ending with a full stop. Step 4 reads "within the program's own systems", as in the decision.

No other VERBATIM text was changed. These are verbatim, checked by string match on the rendered text: the H1, the F H2 and table cells, the GDPR sentence, the FAQ 5 question and answer, and the FAQ 4 dataset, below-1-cm and framework-link sentences.

## Passes on the changed text

- **Hard bans / detector:** CLEAN. No hard_fails and no house_rule_violations after the H3 fix.
- **Judgment rows (terminology Part 3):**
  - No `we/our`, `you`, `buyer`, `organization`, "rather than", or cluster labels.
  - All 7 "hub" hits are `content-hub` URLs.
  - Every `customer` names a contract, deployment responsibility or legal role: E1 mapping and EHR work, E2 API keys, S8 agreement, request and GDPR, and the verbatim FAQ 5.
  - "is not a replacement for…" (FAQ 5) and "does not replace API/SDK integration or an EHR" are product boundaries, said once each.
- **Abbreviations:** API, SDK (B), BMR (S2), EHR (E1), CSV (E2), and HIPAA and GDPR (S7) are expanded at first use. DXA, BIA and BAA are as in v1. BMI is bare.
- **Accuracy discipline:** the only figure is still "below 1 cm" in FAQ 4, with its dataset condition and the framework link in the same answer, unchanged.
- **Self-check** (also in the final.md frontmatter). Fixed after the first apply:
  - S6 restated the table in prose.
  - The G sentences read as a disclaimer inventory inside the decision paragraph.
  - Clunky wording: "customer … customer's", "five … five", and "the program's own" x6, now x4.
- **Residual, accepted:**
  - B (33 words) and the G compliance sentence (29 words) are over 25 words because of required expansions.
  - "API/SDK integration" appears 3 times in prose, each required (B, the S5 lead, the canon line).
  - "body composition estimates" appears 3 times, and each use is the canon category name.

## Gate outputs (final.md, after all edits)

`python3 scripts/article_lint.py workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md --report` (exit 0):

```
workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2437
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.46
[ok  ] prose length
         prose words 2169 vs target 2100 (band 1785-2415)
         . prose_words: 2169
         . target: 2100
[ok  ] claim traceability
         . claims_used: ['FX-001', 'FX-002', 'FX-003', 'FX-004', 'FX-005', 'FX-006', 'FX-007', 'FX-008', 'FX-009', 'FX-011', 'FX-012', 'FX-013', 'FX-014', 'FX-015', 'FX-016']
         . claims_known: 16
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 11
         . links_distinct: 8
         . asset_urls: 0
         . directions: {'up': 1, 'sideways': 3, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: telehealth documentation
         . occurrences: 4
         . h2_count: 11
         . in_first_paragraph: False
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 146
         . mean_words: 12.8
         . p90_words: 20
         . over_25: 2 (1.4%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['program s own x4', 'the admin panel x3', 'body composition estimates x3', 'api sdk integration x3']

--- shape (descriptive, not gated) ---
prose words 2169 across 11 H2 sections
      218  Where telehealth documentation loses consistency
      160  Short answer: what a structured body-data record con
      133  Why record consistency is under pressure now
      270  Where body data enters a telehealth workflow
      251  Where FitXpress fits: capture, records, and the Admi
      206  Fragmented inputs and structured records, side by si
      165  What FitXpress does not do
      155  Data handling, retention, and access
      236  How to evaluate documentation consistency in a pilot
       58  Next steps
      305  FAQ
  links 11 total, 8 distinct, by direction: {'up': 1, 'sideways': 3, 'down': 1, 'trust': 2}
  primary keyword 'telehealth documentation': 4 occurrences
  claim markers 38: {'FX-001': 6, 'FX-002': 4, 'FX-003': 3, 'FX-004': 1, 'FX-005': 2, 'FX-006': 7, 'FX-007': 1, 'FX-008': 1, 'FX-009': 1, 'FX-011': 1, 'FX-012': 1, 'FX-013': 1, 'FX-014': 1, 'FX-015': 1, 'FX-016': 7}
  approved but uncited: FX-010

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

`python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-21-ai-body-scanning-telehealth-documentation/final.md --channel article --summary` (exit 0):

```
SEO / blog article · en · 2437 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

**Landing-link placement.** First, my count with `article_lint.prose_words` on the text before each link:

| Link | Prose words before it | Position |
|---|---|---|
| B early CTA | 197 of 2,169 | 9.1% |
| E1 contextual link | 908 of 2,169 | 41.9% |
| Next steps closing CTA | 1,832 of 2,169 | 84.5% |

Second, `article_package._cta_placement` on the body: `ссылки на лендинг на [9.4, 42.1, 83.7]% тела; ранний ≤30%: да; финальный в последней H2: НЕТ`. The early link is well inside 30%. On the "НЕТ" for the closing link, see Open item 2.

| Measure | v1 | Review 1 round |
|---|---|---|
| Prose words (target about 2,150-2,300) | 1,867 | 2,169 |
| Sentences / mean / p90 | 126 / 12.9 / 20 | 146 / 12.8 / 20 |
| Over 25 / over 35 | 0 / 0 | 2 / 0 |
| Detector | CLEAN 0.0, rhythm 0.41 | CLEAN 0.0, rhythm 0.46 |
| Links total / distinct | 10 / 9 (incl. pricing) | 11 / 8 (pricing removed per J) |
| Claim IDs cited | 11 | 15 (FX-013..FX-016 added; FX-010 still unused) |
| Section words, S1 / S2 / S4 / S5 / S6 / S7 / S8 / pilot / FAQ | 185 / 139 / 219 / 193 / 216 / 120 / 145 / 216 / 230 | 218 / 160 / 270 / 251 / 206 / 165 / 155 / 236 / 305 |

## Open items

1. **Closing CTA target (Vadim, decisions open question 1).** Next steps links the telehealth landing (canon §5 + landing-map rule 4). If Vadim picks the reviewer's `https://3dlook.ai/pricing/#bd-modal-personalized`, only the URL changes, and the anchor already names the demo.
2. **Package mechanical check on the closing CTA will report "НЕТ".** `_cta_placement` looks for a landing link inside the *last* H2. In this article the last H2 is the FAQ, which follows Next steps (v1 order, frozen by the decisions). The closing CTA is in Next steps, as J requires. The publisher should treat this as a known structural false negative, or the coordinator can decide to move the FAQ above Next steps. Moving it changes section order, which this round did not allow.
3. **B wording vs the reviewer.** Her sentence now carries the M1 expansion (see Deviations 1). Tell her in the change log.
4. **E2 heading.** "FitXpress Admin Panel for scan management" instead of the bare name, because of the Title Case house rule. If the bare name is required, it needs a detector exception for product names.
5. **Package must be rebuilt (seo-publisher, N).** meta.md and publish-package.md still describe v1:
   - the old H1/title
   - the pricing CTA
   - four FAQs (FAQPage JSON-LD must now have five, with text from final.md)
   - S6's old H2
   - the old link map: pricing out, E1 landing anchor and Admin Panel anchor changed
   The claim table needs FX-013..FX-016. Meta title: 60 characters or fewer, with "telehealth documentation", without "remote patient monitoring for weight loss".
6. **Product (decisions open question 2).** Which technical fields appear in the API response and which in the Admin Panel. The article states only that not every field appears everywhere.
7. **Product (decisions open question 3).** Is the Admin Panel still "selected clients, no public sign-up"? The launch post was last updated 2026-07-08. The article states FX-014 as the launch post does.
8. **For awareness, 3D model.** C lists "a 3D model" as a generated output, per the decision, `compliance.md` §3 and `tech-spec.md` line 12 ("predicted 3D model" in the API return). The fitness refresh removed the base 3D model for a fitness-plan reason (Pro plan), which does not apply to an API article. No change is proposed.
9. **Carried from v1** (decisions V item 4): three inbound-link spots on `glp-1-market` and `the-potential-of-ai-in-telehealth`, and illustrations (the Doc's Illustrations tab is empty).

## Inputs

I read these in full: `review-1-decisions.md`, `review-1.md`, `v1/final.md` (identical to `final.md` at start), and the context pack, including FX-001..FX-016 and the link targets. I also read:
- `hard-bans-card.md`
- `terminology-guardrails.md` Parts 1-2
- `editorial-rewrites.md` §1-8
- `compliance.md` §1-10
- `tech-spec.md` lines 25-27, 57-71 and 12
- `roadmap.md` rows 16 and 19
- `landing-map.md`
- `blog-style-guide.md` §5-6
- the fitness refresh `editor-report.md`, for its shape

`plan.md` was skimmed for targets only. `plan-audit.md` was not read.

## Coordinator addendum (2026-11-23, after the editor run)

- **Section order fix (mechanical, no wording change):** `## FAQ` moved above `## Next steps` (Related reading stays under Next steps). v1 was the only FitXpress article with the FAQ after Next steps (house order elsewhere: FAQ → Next steps, e.g. the fitness refresh, occupational-health intake, GLP-1 progress record). `article_package.py checklist` failed `cta_placement` because the closing CTA was not in the last H2 (`blog-style-guide.md` §5: closing CTA at the end). After the move: 19/19, lint PASS. The reviewer's J ("final demo CTA after the pilot discussion") still holds.

## QC fix pass (2026-11-23)

Input: `workspace/_quality/seo/2026-11-23-ai-body-scanning-telehealth-documentation-review-1.md`, "Fixes" plus the `coordinator_review` rulings. Applied to `final.md` after the coordinator's FAQ move. Sentences were found by text. Nothing outside these fixes changed.

| Fix | Where | Result |
|---|---|---|
| 1 | S6, paragraph under the table | **Applied.** The double hedge is now one sentence: "How much less of the record needs rebuilding inside the consultation depends on how much was missing before." The correction sentence is **kept, not cut**, and moved after the FX-005 sentence as "Corrections to an entry are made in the program's record system." It now follows "each entry shows the figures from that day", so "an entry" has its antecedent. It also answers where a wrong figure gets fixed. |
| 2 | S7, paragraph 2 | **Applied.** "FitXpress is not a clinical diagnostic tool." now opens the paragraph, and the "does not independently determine" sentence (FX-006) follows it. |
| 3 | S7, closing paragraph | **Applied.** "The program and its legal advisors remain responsible for compliance." |
| 4 | S5, E1 | **Applied.** (a) "The page on the FitXpress [body scanning API for telehealth platforms](…) describes what an integration covers." The anchor and URL are unchanged. (b) "Connecting them to an electronic health record (EHR), or updating a medical record, is the program's integration work." The FX-016 marker stays. |
| 5 | S5, E1 | **Applied.** "The program decides how those results map into its own record systems." Unchanged, per the ruling: FAQ 5, "the customer's API keys" and "selected FitXpress clients". |
| 6 | S4, "Between visits" | **Applied.** "FitXpress does not keep a patient timeline; the program links each scan ID to its own patient record." An FX-016 marker now sits directly on this sentence. |
| 7 | (coordinator) | Not mine. No external source was added. |
| 8 | Pilot section | **Applied.** "None of them is a result to expect in advance, which is why the baseline comes first. The pilot follows this order:" |
| 9 | S4, "Before clinician review" | **Applied.** "The clinical team retrieves the record in one place ahead of the consultation." |

Side effects:
- "stay(s) with" now appears 3 times in the body (scope note, "Before clinician review", S7 final decisions), and all three are v1 text.
- "customer" remains only in contract or legal contexts and in the verbatim reviewer text (FAQ 5).

Gates after the pass:
- `article_lint.py --report`: **PASS**, all 10 gates ok.
  - 2,181 prose words (was 2,169; band 1785-2415).
  - Sentence length: 146 sentences, mean 12.9, p90 20, over_25 = 2 (1.4%), over_35 = 0, near-duplicate pairs none.
- Detector (article channel): **CLEAN**, density 0.0/1000, rhythm 0.46.
- `article_package.py checklist`: **19/19**, STOP-rule OK. CTA placement is [9.4, 42.0, 97.7]% of the body, and the closing CTA is in the last H2.

`final.md` frontmatter: `word_count` is now 2181, and `changes_summary` has a new "QC fix pass" line. meta.md, publish-package.md, git, Docs and Slack were not touched.
