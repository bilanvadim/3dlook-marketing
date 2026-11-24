---
slug: 2026-09-21-glp-1-patient-progress-record-body-data
product: fitxpress
stage: seo-editor, Review 1 edit round
date: 2026-11-24
input: v1/final.md, review-1.md, review-1-decisions.md (wins), context pack (2026-11-24 additions)
output: final.md (edited in place)
---

# Editor report: Review 1

## Result

- Prose words: 1,988 → **2,207** (target about 2,100-2,250; lint band 1,785-2,415).
- `article_lint.py`: 10 of 11 gates ok. The one FAIL is gate 8 (M1), `line 2: GLP-1` in the H1, which is the documented title case (`gate_m1_note` kept). `article_package.py checklist` reads it that way: `lint_verdict` [x], **19/19, STOP-rule OK**.
- `detect-ai-tells.py --channel article`: **CLEAN**, ai_density 0.0/1000, hard_fails [], house_rule_violations [].
- R1-1 grep: **2 hits**, the RTPV sentence and the FAQ disability limitation. See R1-1 and Flags.
- CTAs: exactly two (early paragraph after the Short answer, closing line in Next steps). Both link to `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/`. Zero `/pricing/` or `/contact-us/` links.

## Per-item status

| Item | Status | Notes |
|---|---|---|
| R1-1 Capture log claims | **applied** (one marker deviation, one wording choice) | All five replacements are verbatim. The H3 "The capture log" is rewritten in the fixed order: status and the known gap (FXS-RECORD-STATUS); timestamps and the scan identifier (FXS-RECORD-STATUS); the program's log of capture instructions and manual fallback; the RTPV sentence once, verbatim (FXS-RTPV); the first-entry sentence unchanged. I also applied the coordinator addition in "What FitXpress does not do". **Wording choice:** the program-log sentence opens "What the program logs about…" because the gate counted "program's own" ×3. **Marker deviation:** the decision says to keep FXS-DELIVERY on the delivery sentence, but v1 had FXS-LIFECYCLE there. The sentence now carries FXS-DELIVERY and FXS-RECORD-STATUS. FXS-LIFECYCLE's technical-data list no longer describes the record (pack note). |
| R1-2 Landing link and two CTAs | **applied** | The early CTA is verbatim, in its own paragraph with the link inside the sentence. It has no action-label line and no FXS-CLIENTS. The "Where FitXpress fits" anchor and the closing CTA are verbatim. The landing links sit at 19.8%, 57.1% and 97.5% of body words (`cta_placement` ok). The landing keyword stays out of the title and H1. |
| R1-3 Photos and retention | **applied** | The bullet is verbatim. FXS-PHOTOS was added and FXS-LIFECYCLE kept. The H3 sentence "Photos are the input to the capture…" stays: the near-duplicate check did not pair it with the bullet, so I didn't use the allowed variation. |
| R1-4 Muscle-loss H2 | **applied with change** | The heading is verbatim, placed after the capture log and before Cadence. I changed the starting text in two ways: (a) "These figures support clinician review." moved from the start of paragraph 2 to the end of paragraph 1. It is the last sentence of FXS-MUSCLE-FIELDS, so claim order is unchanged, and it no longer reads "clinician review. A 2024 review". (b) I added serial commas in the section's lists (editorial-rewrites.md §6). The Neeland lines are attributed, with no figures and one sideways link. The M1 follow-on is verbatim: the FAQ H3 and answer use DXA and BIA, which are now expanded once, in the new H2. **Outside the touched sentences:** I cut v1's "An entry that carries them sits next to a weight figure in the file." from "The generated fields" because the new H2 states the same point. |
| R1-5 Speed wording | **applied** | Verbatim, FXS-SPEED kept. |
| R1-6 NDA line | **applied** | Verbatim, after the FXS-REPEAT sentence, with its own FXS-REPEAT marker. "Internal" and the framework link stay in the same paragraph. No percentage. |
| R1-7 BMI verification link | **applied** | Verbatim; the pharmacy guide link is kept. Transition: v1's "The decision itself stays…" became "The decision stays…", because the next sentence also uses "itself". |
| R1-8 Privacy section | **applied with change** (as decided) | Only "Deletion is by scan identifier on the customer's request." was cut. The HIPAA/GDPR expansion sentence, both canon sentences and the FAQ link are kept. |
| Coordinator addition | **applied** | "Its fields describe measured body change and what happened to each capture." |

**Frontmatter:** status edited, word_count 2207, claims_verified adds FXS-RECORD-STATUS, FXS-RTPV, FXS-PHOTOS, FXS-MUSCLE-FIELDS and FXS-MUSCLE-LIMITS. There is a new field `external_sources_used: [EXT-NEELAND]`; EXT-NEELAND has no claim marker because it is not in `approved_claims`. changes_summary and self_check are replaced. I reworded the `gate_m1_note` value from "flags" to "fails on" so the R1-1 grep no longer hits the frontmatter; the field itself is kept.

## Gate outputs

```
article_lint.py final.md
[ok  ] hard bans (detect-ai-tells)
[ok  ] prose length        prose words 2207 vs target 2100 (band 1785-2415)
[ok  ] claim traceability
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links      directions {'up': 1, 'sideways': 3, 'down': 1, 'trust': 2}
[ok  ] keyword placement
[FAIL] abbreviations (M1)  line 2: GLP-1 used before being expanded (H1, documented via gate_m1_note)
[ok  ] accuracy discipline
[ok  ] sentence length     mean_words 13.1, p90 20, over_25 0 (0.0%), over_35 0,
                           near_duplicate_pairs none,
                           repeated_phrases ['for glp 1 x4', 'scan to scan x3', 'mass and fat x3', 'lean mass and x3', 'and fat mass x3']
VERDICT: FAIL  (1 gate(s) failed)   -> checklist lint_verdict [x], 19/19, STOP-rule OK

detect-ai-tells.py --channel article final.md --summary
SEO / blog article · en · 2504 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN; hard_fails [], house_rule_violations []

grep -n -i -E "flag|clothing|obfuscation|pose|metadata|conditions of (the|each) capture" final.md
142: What the program logs about … During capture, Real-Time Pose Validation (RTPV) gives pose and framing guidance. <!-- claim: FXS-RTPV -->
220: FitXpress was not specifically trained on … This matters when a disability affects the standard standing pose or capture sequence. … <!-- claim: FXS-POPULATION -->
```

`article_package.py checklist` (read-only, run twice): 19/19, `cta_placement` [x], `links_live` 10 links, 0 failures, 0 warnings.

## Flags for Open items

1. `Relink when /fitxpress/for-glp-1-programs/ goes live: body composition tracking for GLP-1 programs → /structured-body-data-for-telehealth-digital-health-programs/`
2. `Relink when /fitxpress/for-glp-1-programs/ goes live: remote progress tracking for GLP-1 clinics → /structured-body-data-for-telehealth-digital-health-programs/`
3. `Relink when /fitxpress/for-glp-1-programs/ goes live: closing CTA "book a FitXpress demo" → /structured-body-data-for-telehealth-digital-health-programs/ (then {landing}#demo, rule 4)`
4. **Body sites (R1-4):** all four (waist, hips, thighs, upper arms) were checked against `tech-spec.md` "Circumferences". None needed replacing.
5. **Third-party source (R1-4):** EXT-NEELAND (Neeland, Linge, Birkenfeld 2024, PubMed 38937282) is used in the new H2, attributed and without figures. Asselya may strike it. If she does, both Neeland sentences go together and the paragraph opens on "FitXpress does not assess muscle strength…".
6. **R1-1 grep has a second hit that I did not remove.** It is the FAQ disability limitation (FXS-POPULATION): "This matters when a disability affects the standard standing pose or capture sequence." That sentence is verbatim canon (`accuracy-formulations.md` §5) and on the do-not-change list. It describes the person being scanned, not a record field. If the grep has to come back fully clean, the canon line needs Vadim's decision first.
7. **Consistency with the Telehealth Documentation article** (coordinator's open item). Its Version 2 still lists the `compliance.md` §3 technical data as part of the record. If the 2026-10-07 `tech-spec.md` level applies there too, that bullet should take the FXS-RECORD-STATUS wording before it goes live.
8. **Serial comma inside the VERBATIM strings.** The R1-1 and R1-3 bullets keep the reviewer's punctuation: "Gender, height and weight" and "Processing status, a timestamp and the scan identifier". The rest of the article and house style (`editorial-rewrites.md` §6) use the serial comma. Asselya decides.
9. **Repeated sentence kept by rule:** "Photos are the input to the capture" appears in the Short answer bullet and in "The submitted fields". The gate did not pair them, so the decision keeps both. Asselya may vary the H3 one.
10. **Edits beyond the item text, for Asselya's visibility:** the clinician-review sentence moved within the new H2. The v1 sentence "An entry that carries them sits next to a weight figure in the file." was cut. "itself" was dropped from v1's FAQ sentence. The capture-log sentence opens "What the program logs about…".
11. **Stale stage files:** `meta.md` and `publish-package.md` in the article dir date from v1 (2026-09-21). `meta.md` still describes a single CTA to the pricing modal. The publisher should regenerate both from this final.md.
12. **Known M1 title case** (GLP-1 in the H1, `gate_m1_note`) carries over as before.

## QC fix pass (2026-11-24)

Input: QC report `workspace/_quality/seo/2026-11-24-glp-1-patient-progress-record-body-data-review-1.md` (16/20) and the section "QC fix pass" in review-1-decisions.md. Where that section differs from the R1-4 quote block, it wins. Q3 and Q6 go to the publisher, not this stage.

| Item | Status | What changed in final.md |
|---|---|---|
| Q1 overclaim, new H2 | **applied, verbatim** | "A program answers it from fields the record already carries." → "The record already carries the fields a program reviews for that question." |
| Q2 Neeland sentences | **applied, verbatim** | Both sentences replaced with "…describes lean mass as a measure that includes organs, bone, and fluids as well as muscle. By that account, a change in lean mass may not reflect a change in muscle." The link, attribution and FXS-MUSCLE-LIMITS marker are unchanged. |
| Q3 grep note | publisher | Not edited here. The frontmatter line now says the coordinator amended the check and the publisher lists the disability-line hit in Open items. |
| Q4 RTPV bridge | **applied** | Added one sentence before the RTPV sentence: "The guidance given while the photos are taken is part of that protocol." It ties RTPV to "the same protocol" as guidance during capture. The RTPV sentence is verbatim, and there is no "rather than" and no corrective negation. |
| Q5 repetitions | **applied** | In "The submitted fields", "Photos are the input to the capture." became "The capture works from the two photos." The bullet keeps the reviewer's words. The paragraph now carries `<!-- claim: FXS-PHOTOS -->`. In "The generated fields", "Composition estimates describe what the change is made of." became "Composition estimates split body weight into fat and lean components." Now only the new H2 uses the "made of" framing. |
| Q6 meta description | publisher | Not edited here. |

**Frontmatter:** word_count 2230. changes_summary has a "QC fix pass" entry, and the R1-3 entry points to Q5. The grep line no longer says "listed for Open items"; it now says the publisher lists it (Q3). self_check is updated. I reworded a frontmatter mention of the old CTA target so that `grep pricing final.md` returns 0.

**Gates after the pass**

```
article_lint.py final.md
  prose words 2230 vs target 2100 (band 1785-2415)
  10 of 11 gates ok; [FAIL] abbreviations (M1) line 2: GLP-1 in the H1 (documented, gate_m1_note)
  sentence length: mean_words 13.1, p90 20, over_25 0 (0.0%), over_35 0, near_duplicate_pairs none
  VERDICT: FAIL (1 gate) -> article_package.py checklist: lint_verdict [x], 19/19, STOP-rule OK,
  cta_placement [x] (landing links at 19.6, 57.6, 97.6% of body), links_live 10 links, 0 failures, 0 warnings

detect-ai-tells.py --channel article final.md
  VERDICT: CLEAN, ai_density 0.0/1000, hard_fails [], house_rule_violations []

grep -n -i -E "flag|clothing|obfuscation|pose|metadata|conditions of (the|each) capture" final.md
  164: the capture-log paragraph with the RTPV sentence (allowed)
  242: FAQ disability limitation, "standard standing pose" (FXS-POPULATION canon, allowed per Q3)
```

**Status of the Flags above after this pass**
- Flag 5 (EXT-NEELAND): the sentence pair is now reworded. The coordinator's Q2 note adds the cross-page overlap to the Open item, and Asselya still keeps or strikes it.
- Flag 6 (second grep hit): the coordinator amended the check to allow it (Q3), and the publisher writes the Open items line.
- Flag 9 (repeated photo sentence): resolved by Q5.
- Flags 1-4, 7, 8, 10-12 still stand. Flag 10 now also covers the Q4 bridge sentence and the reworded composition sentence.
