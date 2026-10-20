---
slug: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
stage: edit (Review 1 rewrite, revision 2)
written: 2026-10-20
by: seo-editor
input: draft.md (revision 2), writer-notes.md
output: final.md (status edited)
authority: review-1-decisions.md (incl. section A) > plan.md > context pack > review-1.md
---

# Editor report

## Round 2 (publish fix pass, 2026-10-20)

Per the coordinator, after `article_package.py assemble` hit its STOP rule: added `gate_m1_note` to the final.md frontmatter, the documented H1 exception (precedent 2026-09-21-glp-1-patient-progress-record-body-data), and renamed `## Frequently asked questions` to `## FAQ` (house format). No other change to the prose. Re-run: `article_lint.py` reports FAIL on the accepted M1 only, the detector is CLEAN and the 24 locked strings are intact. The new frontmatter line moved every body line down by one, and the L-numbers in this report are updated to match.

## Round 3 (QC fix pass, 2026-10-20)

QC scored 16/20, ship with notes (`workspace/_quality/seo/2026-09-19-glp-1-fitness-apps-body-composition-tracking.md`). Findings 1 and 2 are applied, in Section 5 only. Point 3, cutting the scope note to one sentence, was declined by the coordinator because decisions §6 keeps the scope note verbatim.

- **Finding 1, the 34,000-scan paragraph (L123).** It already sat directly before the pilot paragraph, so nothing moved. It gained one bridge sentence after its two locked sentences: "Before an app commits to periodic check-ins at that scale, it needs to know whether its own members come back for repeat scans." The paragraph still has no link and no landing link, and its locked sentences are verbatim.
- **Finding 2, the pilot paragraph (L125).** Its generic last sentence ("Measures the app already records, such as check-in rates, can be compared with their pre-launch levels.") became a two-sentence decision rule. The rule is built from the cadence and review-of-differences logic in Section 4 and the plan's pre-launch comparison, and it carries no numbers: "That interval is set before launch, long enough for the expected change to exceed observed scan-to-scan variation. The app team also sets in advance the repeat-completion level, measured against the app's pre-launch check-in rates, that justifies a wider rollout."
- **Gates after round 3.**
  - `article_lint.py` reports FAIL on the accepted M1 only.
  - The detector is CLEAN, 0.0 per 1,000 words.
  - Sentence length: 94 sentences, mean 15.3, p90 22, 1 over 25, 0 over 35.
  - The 24 locked strings are each present once, word for word.
  - Landing links sit at 15.5%, 62.9% and the CTA.
- **Length after round 3.** 1,616 prose words without the concept lines (target 1,600). The lint count with the concept lines is 1,795, inside the lint's 1,360-1,839 band but above the editor's ±10% band (1,760). Section 5 now runs 538 words against the plan's 430.
- The figures in "Gates on final.md" and "Section lengths" below are from round 1. The ones above replace them.

## Gates on final.md

| Gate | Result |
|---|---|
| `article_lint.py` | PASS on every gate except M1 on "GLP-1" in the H1 (accepted known failure, Vadim 2026-09-19). Verdict line reads FAIL (1 gate). |
| Sentence length | 92 sentences, mean 15.1, p90 22, over 25: 1 (1.1%, the locked first sentence of T-PRIVACY-ROLES, 26 words), over 35: 0 |
| `detect-ai-tells.py --channel article` | CLEAN, 0.0 per 1,000 words, no hard fails, no house-rule violations, zero soft markers |
| Locked text | 24 locked strings checked by script, each present exactly once, word for word (link markup stripped before comparing, see judgment call 1) |
| Length | 1,572 prose words without the three concept lines (target 1,600); lint count 1,751 with them (band 1,360-1,839; the editor's ±10% band 1,440-1,760 also holds) |

Section lengths, prose without concept lines (plan in brackets): Section 1 275 (300), Section 2 204 (240), Section 3 192 (190), Section 4 252 (270), Section 5 492 (430), FAQ 113 (130), Next steps 31 (40).

## What changed against draft.md

Eight edits. Nothing locked was reworded or moved out of its section.

1. **Section 1, down link (L61).** "Body composition tracking for fitness apps places circumferences and composition estimates on the same timeline as weight and training." became "With [body composition tracking for fitness apps](…), circumferences and composition estimates sit on the same timeline as weight and training history." The anchor now reads as part of the sentence and stops being the grammatical subject of a product claim. Position 15.8% of the body.
2. **Section 2, joint advisory (L71).** "An app that offers workouts does not, by itself, fulfill all of that guidance." became "An app that offers workouts can support one part of that guidance." See judgment call 5.
3. **Section 3 lead-in (L77).** "and what the app does not conclude" became "and which conclusions the app avoids".
4. **Section 4, review of differences (L101).** Added one practical sentence: "Smaller differences can stay in the record without a callout in the member's view." It says what the app does, does not restate table rows 2 or 3, and carries no figure.
5. **Section 5, P1 (L109).** "GLP-1 programs that run their own member app use the same integration." hedged to "can use". The optional top-7 sentence and link are cut (judgment call 4).
6. **Section 5, P3a (L115).** Order changed: the paragraph now opens on "Repeatability is especially important for a progress view, because each check-in is compared with an earlier scan." and the framework sentence follows. The locked lead and FXS-REPEAT stay last, in order.
7. **Section 5, P4 (L121).** "Each record is read against its own earlier values." became "Each record is best read against its own earlier values." It is a recommendation, so it is now stated as one.
8. **Section 5, P6 (L125).** "Measures the app already records before launch, such as check-in rates, can be compared with a pre-pilot baseline." became "Measures the app already records, such as check-in rates, can be compared with their pre-launch levels." "Baseline" now has one meaning in the article (the first scan).

## Judgment calls

**1. Privacy FAQ link inside the locked T-PRIVACY-ROLES sentence (L113). Kept on "applicable lawful basis".**
- The words are unchanged; a link is markup, not copy. The locked-text script compares with link markup stripped, and QC should do the same.
- Decisions G4 asks for the privacy FAQ link "once, mid-paragraph" in this paragraph, and the plan asks for it "on a content phrase". Lawful basis is what the FAQ actually explains (controller and processor roles), so the anchor describes the target.
- The only unlocked words in the paragraph are the lead-in clause "When a member's treatment runs through a separate prescribing service", which does not describe the FAQ.
- A separate pointer sentence would add a sentence about another page and lengthen Section 5, which is already over its budget.

**2. KFF sentence (L57). Writer's 25-word version kept, without "about one in eight".**
- Decisions §6 requires one sentence that says the figure describes US adults generally, not fitness app members. "12%" is the precise figure. "About one in eight" says the same thing again and takes the sentence to 28 words.
- The "X, not Y" shape stays. It is a scope limit on a statistic that the top-authority file asks for in so many words; it is precise and not dismissive. The rewrites I tried either added an unverified claim about the poll's design or used a second negation.
- Re-checked on kff.org 2026-10-20: "About one in eight adults (12%) say that they are currently taking a GLP-1 drug", published Nov 14, 2025.

**3. "strength training" in the joint-advisory sentence (L71). Kept.**
- We attribute a recommendation to four named societies, so their term is the safe one. The obesity.org release (re-checked 2026-10-20) reads "adequate protein intake and strength training to preserve lean mass", and the word "resistance" does not occur on the page.
- The decisions file's "resistance training" paraphrases the reviewer's paraphrase. It is a description of what to say, not a "Text to place" line. Its intent (training as part of broader nutritional and medical management) is met.
- It also ties the paragraph to the article's own "strength program" thread. Carried as an FYI open item in case the reviewer wants her word back.

**4. Section 5 length (507 words in the draft, 492 now, plan 430). Cut the optional top-7 sentence; kept the second-record pair.**
- The top-7 page is a vendor comparison for GLP-1 clinics. In the paragraph that names FitXpress and links the landing, a pointer to a list of alternatives works against the evaluation CTA. It also brought in a new actor ("clinics comparing vendors") off the app-team thread.
- Its AEO job (prompt 565495617300, a GLP-1 clinic tracking body composition remotely) is still carried by "GLP-1 programs that run their own member app can use the same integration." in the paragraph that names FitXpress (3DLOOK). Assistants already cite the top-7 page 15 times, and all four link directions remain without it.
- The second-record pair (L121) stays. It is the only place the article says how the app's scan record relates to a provider's DXA or BIA record. No linked page makes that GLP-1-specific point, and it turns the method guardrail into practice.
- About 270 of the 492 words are locked text (T-BODY-PROGRESS, T-RECORDS-ACTORS, T-PRIVACY-ROLES, the A3 lead, FXS-REPEAT, the P3b short form, T-REPEAT-SCOPE with T-VALIDATION, R2, T-34K). Further cuts would have to come from required content. The article as a whole sits at 1,572 against 1,600.

**5. Joint-advisory last sentence, stacked negation.** The reviewer's "does not, by itself, fulfill all of that guidance" has the shape guardrail M2 lists ("do not, on their own, …"). It is not locked: decisions §6 describes what to say and gives no text to place. "An app that offers workouts can support one part of that guidance." keeps the meaning (the app's part is partial), adds no claim that app workouts meet the advisory, and drops the double negative. FYI open item.

**6. Section 1 down link is in the reframe paragraph (L61), directly after the weight-chart paragraph (L59), not inside it.** The plan's wording says "in the weight-chart paragraph". The two stay separate, because merging them makes a five-sentence block in the opening. What decisions A2 requires is met: Section 1, first 30% (15.8%), anchor from the landing map.

**7. Coaching article linked twice (L101, L121). Kept.** The plan's link table places it in both, and the two links do different jobs: change thresholds in Section 4, the method-by-method comparison in Section 5. Citation dedup otherwise: KFF, obesity.org and PubMed (Section 2) each once in the body. PubMed appears again in FAQ 1, inside locked R3.

## Locked text against the rules

No locked sentence breaks a hard rule, so nothing is flagged as an open item from locked text. Points checked:
- T-PRIVACY-ROLES, sentence 1, runs 26 words. It is the only sentence over 25 words and sits within the gate's allowance (1.1% against 6%).
- FXS-POPULATION sentence 1 has two negative clauses joined by "and". This is the limitation formulation Vadim approved verbatim (accuracy-formulations §5), with each clause stating one fact. It is not a nested negation.
- T-REPEAT-SCOPE and T-VALIDATION use "validated", "peer-reviewed" and "third-party" only to disclaim them. The detector licenses that form.
- In R1, "its lean mass estimate is not a measurement of muscle" is a product boundary, the licensed "X is not Y" case.
- "customer" appears once, in the A3 lead "real-world customer dataset". That is the canonical repeatability wording, and the word is used in its contract sense.

## Coordinator's specific checks

| Check | Result |
|---|---|
| Nothing says or implies FitXpress or a scan detects, reveals, tracks or measures muscle or muscle loss | Pass. Every "muscle" in the body is attributed research (L69, L71), a negative boundary (L55, L73, L119, L131), the table's "avoid concluding" column (L83), or a "no muscle definition" instruction in a concept line |
| No "split into fat and lean" | Pass, no "split" anywhere |
| H1 frames muscle loss as the app team's concern | Pass: "GLP-1 Muscle Loss Concerns for Fitness Apps: Tracking Body Change Beyond Scale Weight" (L45) |
| No "organization(s)" where the actor is known | Pass, the word does not occur |
| "FitXpress tracks a member over time" never appears | Pass. The only "track" with a person as object is the locked negative "3DLOOK does not track individuals" (L111) |
| 34,000-scan paragraph: no link, not with a landing link | Pass: its own paragraph (L123), no link of any kind |
| P3a, P3b, P3c are three separate paragraphs | Pass: L115, L117, L119, consecutive. Framework link on P3a and P3b, none on P3c |
| Fitness landing in Section 1, Section 5 and the CTA | Pass: L61 at 15.8% ("body composition tracking for fitness apps"), L109 at 64.5% ("body scanning for fitness apps"), L139 (CTA, the v2 sentence). H1 and title do not use the landing's primary keyword |

## Review 1, item by item

"Satisfied" means the text meets the item as the decisions file rules it.

| # | Review item | Where in final.md | Status |
|---|---|---|---|
| A1 | Cross-cluster bridge: app team's decisions as the thread | L61 reframe, L77 lead-in, L93 "On the app's side", L111 "The app company links…" | Satisfied |
| A2 | Separate from the fitness hub: less general scanning, more on what the app shows, compares and routes | Sections 3-4 (L75-L103). General scanning is reduced to Section 5 P1 (L109) | Satisfied |
| A3 | Separate from GLP-1 content: market and adherence brief, linked | L63, one sentence each | Satisfied |
| A4 | One contextual product link where integration is discussed; keep the CTA | L109, L139 (and L61 per decisions A2) | Satisfied |
| A5 | Value for a product buyer: example progress view and decision table | Table L81-L85, Image 1 concept L89 | Satisfied |
| C1 | Headline must not suggest the article identifies muscle loss; keep the muscle-loss question prominent | H1 L45, Section 2 H2 L65, FAQ 1 L129 | Satisfied as amended (decisions §1). The reviewer's literal H1 is an open item |
| C2 | Explain what estimates depend on; no "split" | L87, T-ESTIMATES verbatim | Satisfied |
| C3 | App-specific table | L81-L85, verbatim with A1 "Allow" | Satisfied |
| C4 | Separate measurement evidence from composition evidence; approved repeatability sentence; not externally validated | L115 (FXS-REPEAT), L117, L119 (T-REPEAT-SCOPE, T-VALIDATION) | Satisfied |
| C5 | 34,000-scan proof point: keep only with source, count, period, permission | L123, own paragraph, no link | Satisfied as amended (decisions §5: source, count and period confirmed in brand-assets). Customer permission is an open item |
| S1 | Why this is a fitness-app question; KFF one sentence or omitted, scoped | L57 (KFF), L59 (strength program, disconnected record) | Satisfied |
| S2 | Condense the research; lean mass vs muscle; joint advisory as broader management that app workouts alone do not fulfil | L67-L73 | Satisfied. Wording differs from the paraphrase (judgment calls 3, 5), FYI open item |
| S3 | GLP-1-aware progress view: table and illustrative screen | L75-L89 | Satisfied |
| S4 | Comparable check-ins: baseline, cadence, capture, review, alternative path; new-baseline sentence | L91-L103, T-BASELINE at L95 | Satisfied |
| S5 | Where FitXpress fits and pilot: outputs, Body Progress, integration responsibilities, limits, pilot metrics | L105-L125 | Satisfied |
| S6 | Short FAQ; keep the muscle-loss question; cut answers that repeat the body | L127-L135, two questions. "How often" moved to Cadence (L97) | Satisfied |
| S7 | Condense roles, "which method fits when", programs and implementation; method comparison belongs in the coaching article | Roles table and "fits when" H3s gone. One sentence plus link at L121. Privacy L113, thresholds L101, pilot L125 | Satisfied |
| P1 | DXA and BIA not grouped as equivalent references; protocol names its method; muscle-function sentence | No "reference method" anywhere. R2 at L121, FAQ 1 L131 ("Where a protocol requires DXA, that method applies."), T-MUSCLE-FUNCTION at L73 | Satisfied |
| P2 | Say whether weight is entered or synced | T-WEIGHT-SOURCE at L87. No Smart Scales, per decisions G2 | Satisfied as amended |
| P3 | Body Progress: company links scan IDs; 3DLOOK does not track the person | T-BODY-PROGRESS at L111 | Satisfied |
| P4 | Privacy: lawful basis, notices, permissions, agreements; consent in some workflows | T-PRIVACY-ROLES at L113; FAQ 2 ending at L135 | Satisfied |
| P5 | "two organizations" becomes "the fitness app company and the prescribing provider may each hold different records" | T-RECORDS-ACTORS at L113; no "organization" in the article | Satisfied |
| P6 | Image 1 illustrative progress view, Image 2 capture to results, no muscle imagery | Cover L49, Image 1 L89, Image 2 L107 | Satisfied |
| R1 | Retain as net-new P1 with the progress-view example as the centerpiece | Section 3 | Satisfied |
| R2 | Incoming links from the AI in Fitness hub and the GLP-1 market article | Not article copy (decisions §H) | Not satisfied in the text, by design. Open item (CMS work) |

**Summary: 25 review items. 24 satisfied in final.md, 4 of them as amended by the decisions file (C1, C5, P2, and S2 with a wording note). 1 not satisfied in the text by design (R2, incoming links), carried as an open item.**

Decisions-file rows not covered by a review item: §A1 "Allow" (L84) satisfied. §A2 three landing links satisfied. §A3 three paragraphs satisfied. §5 placement rule satisfied. §6 opening (no "Short answer" H2, scope note verbatim at L55) satisfied. §6 length (1,400-1,800) satisfied at 1,572. §G1 no "reference methods" satisfied. §G6 cover rule satisfied.

## Open items (also in final.md frontmatter `open_items`)

1. **H1 (decisions §1, for Vadim).** The reviewer's verbatim H1, "GLP-1 and Fitness Apps: Tracking Body Change Beyond Scale Weight", is a one-line swap. It removes the primary keyword from the H1, so gate 7 fails unless the primary keyword changes too.
2. **34,000 scans (decisions §5, for Vadim).** The reviewer asks for the customer's explicit permission to describe the use publicly, and the 19.09 decision covers the anonymized mention. If sign-off is wanted and not given, the two T-34K sentences (their own paragraph, L123) cut cleanly.
3. **Incoming links (decisions §H, CMS work for Assel or the site editors).** After publication, add contextual links into this article from `ai-in-fitness-industry` and `glp-1-market`.
4. **M1 on "GLP-1" in the H1.** Accepted known failure. `article_lint.py` reports FAIL on that gate alone.
5. **FYI, wording that differs from the decisions file's paraphrase.** No action unless the reviewer wants her words back.
   - "strength training" stands where the decisions file says "resistance training". It is the advisory's own term.
   - "An app that offers workouts can support one part of that guidance." replaces "does not, by itself, fulfill all of that guidance", which is the M2 stacked-negation shape.
   - The meaning is the same in both cases, and no claim is added.

## Checked, not flagged

- **Landing response time.** v2 carried an open item on "under a minute". The live fitness landing (fetched 2026-10-20) says "processed in under 45 seconds" in three places, which matches the article. It also says "full scan flow takes under a minute, with processing typically under 40 seconds". That mix is a matter for the landing page, not for this article, and the v2 item is retired.
- **Internal URLs.** All seven linked URLs return 200 (sequential curl, 2026-10-20). The cut top-7 URL also returns 200. The target slug `glp-1-muscle-loss-fitness-apps` returns 404, as expected for an unpublished page.
- **Secondary keywords.** `glp-1 and muscle loss` and `glp-1 app` are not placed. Neither fits a sentence that needs those words (plan: "only if natural").
