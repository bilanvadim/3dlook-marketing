---
qc_date: 2026-10-19
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/messages/ (re-check after fix rounds 1-2; sample: amy-mushlin-884504, alexandra-yurkovic-9162212, akallarakuzhi; _check.json; siblings read in _batch-vida-health-1/2, _batch-included-health-1/2/3, _batch-omada-health-1; other companies sampled in _batch-crossover-health-1, _batch-emed-1, _batch-mdlive, _batch-wondr-health)
track: outbound
artifact_type: messages
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report (re-check r2): message-sequencer, 2026-10-19, us-employer-obesity-care

**Artifact:** `workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/messages/` (367 people, 734 messages)
**Total: 14/20, marginal** (first QC: 13/20)

**Verdict.** The two fix rounds cleared every item they named:
- the "so" result lines are gone across all 14 batches;
- the disclaimer M2s of the four named people are gone;
- the named twin pairs are mostly resolved;
- the gate's product-sentence repeat notes fell from 37 to 7.

The failure classes are still there outside the fix lists, because the lists covered named sentences and not the patterns behind them:
- card rules copied into copy;
- card question targets reused as questions;
- same-company openers;
- stock call shapes.

The deletion-only fixes also left a few M2s with nothing in them. Recommendation: no regeneration. Run a round 3 that targets the patterns campaign-wide (list under Top 3).

**Scoring basis.**
- Scored against card-messages.md and the _profiles files. Limits, signature, bans, detector and completeness are taken from the gate as fact. The gate's `hard` list is empty.
- D is not capped for the missing `product:` field. That comes from the script template, the same ruling as the first QC.
- notify.py was not run, because this QC run had no shell tool.

## Status of the first QC's top issues

| # | First-QC issue | Status | Evidence |
|---|---|---|---|
| 1a | Vida operations twins (amy / erin-mynaugh / molliemcgill / josephmurad) | **Partly fixed** | Amy↔Mollie M2: fixed. Amy↔Erin M1 product sentence: **still twins** ("…on any phone at a check-in, and the record gets 80+ body measurements" / "…from any phone and the check-in record gets 80+ body measurements"). Amy M2 line 1 "timestamped record at each check-in" still matches Erin ("timestamped result for the check-in") and Shane ("One SDK across employer clients gives each check-in a timestamped result"). Amy's "One SDK serves every client" is Shane's line too. |
| 1b | Included Health clinical (alexandra / jordana-blair, plus 5 "sample result" closers) | **Mostly fixed** | Hook, product sentence and CTA now differ. Only diana-malone keeps "sample result". The central question is still the same one in new words: what body data a clinician wants as the visit starts. **New twin:** anishmehtamd M2 "a waist reading and a 3D model of the member's own scan give a complex-care clinician…" / tony-yuan-md M2 "A waist reading and a 3D model from the member's own scan reach the clinician…". |
| 1c | Omada technical (akallarakuzhi / terry-miller / marty-lynch) | **Partly fixed** | The "fields, IDs and timestamps" twin is gone. The "A call can/could/would [verb] …" shape is still in spencer, sunilkayiti, patrick-curry and marty-lynch (4 of the 5 cited). **New shared shape:** Ashok and Terry both open M2 by turning their M1 question into a noun phrase ("Clearing a new measurement type for your pipeline…" / "Taking a new member data type into your models…"). |
| 2 | Card rule sentences used as copy | **Fixed for the 4 named people, not campaign-wide** | Alexandra, tony-yuan-md and anishmehtamd no longer carry disclaimers. Amy's "phone as the only hardware" and her topic-line question are gone. About 30 restatements remain across the batches (see A). |
| 3 | M2 does not carry the person forward; ungated "so" | **Partly fixed** | "so" benefits: **fixed** (zero matches in the batches). Alexandra's M2 now continues her question but asks it again ("Which measure should come first?"). Ashok's M2 now has 2-4 weeks and one call ask, but the value line does not follow from his question (see B, E). |
| first QC, D | Summaries misreport soft notes; crossover summary contradicts itself | **Not fixed** | _summary-crossover-health-1 still reads "clinical 13 … clinical 12". It still says "about 11 M1s" for «two photos return…», and _check.json now shows 4. |
| first QC, E | Hook template "Your path from X to Y stood out." | **Not fixed** | About 20 "…stood out." / "…caught my eye." hooks across the batches: eMed ×6, Crossover ×5, Included Health ×7, Omada ×3. |

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5
- **Card rules restated as copy remain outside the fix lists** (card: "Card lines are targets").
  - _batch-wondr-health l.44, lisa-talamini M2 value line: "Body composition values from the scan are estimates for the care team… It never diagnoses or decides anything about a member." This is the same failure as Alexandra's original M2. Her fix1 item covered only her M1.
  - _batch-omada-health-1 l.107, kevin-masci M2: "two scans the care team picks, and the scan informs the clinical team without deciding anything about a member."
  - _batch-mdlive l.109/117, abhishekmehramd: the restatement is in both M1 and M2.
  - _batch-included-health-1 l.241/249, heather-washington-md: "the physician compares two scans the care team picks" appears in both M1 and M2, and her proof field is that rule.
  - Vida: "care team picks/decides" appears in 8 sequences (ashish-nag, josephmurad, claudia-ryan, tracy-rodriguez, letal-yerganjiev, hersh-ranpura, dosbo, mohamed-elassy).
- **Card question targets reused almost word for word as M1 questions.** The first QC raised this for Amy, and the class persists:
  - Omada: chunalex, changheidi, may-wu, jill-belinky, seanbmilligan, steve-cook.
  - Vida: makara-fairman, davidcarlson1, brent-hartman, jessica-vollendorf, jasonmacaleer.
  - Included Health: codyyashinsky, austin-aldrich, jeremy-gross.
  - Wondr: rubenrodarte. His whole pair is the operations lane reworded ("finish at the same check-in … no device logistics for that step"; "One SDK can serve every employer client … timestamped record").
- **Same-company opener (first three words) repeats.** The card forbids them and the gate does not check:
  - "Noticed your background": Crossover ×3 (sumeet-batra, steve-roey, maria-popow), eMed ×3 (lindayaccarino, ryan-adams, eddiemaria), Wondr ×2 (lisa-talamini, rubenrodarte).
  - "Your path from": Crossover ×2 (scott-shreeve, kendramulvey).
  - "Your focus on": Vida ×2 (ashish-nag, wbryansmithphd).
- **"Never the same ask twice"** (Rules): alexandra M2 "Which measure should come first?" asks her M1 question again.
- **Stock call shapes** that fix1 named, still present outside its items:
  - Omada-1: about 10 "A call can/could/would …";
  - MDLIVE: "I can show/go through … on a call" ×5;
  - Crossover: "Want (a look at) a sample result?" ×2 (sreelata-kintala, steve-roey).

### B. Factual accuracy: 4/5
- All numbers are card numbers. No client names. The compliance line is verbatim in all three sampled non-referral M2s. Article choice is correct for all three (GLP-1 market / none / privacy FAQ).
- **Fixed proof lines not used as plain sentences** (Rules: "used as written, each a plain sentence of its own"):
  - "112,100 scans in 2025 across all 3DLOOK customers is the scale behind it." (shane-giuliani, pbabington; tomkazer "…behind the capture");
  - codyyashinsky "…is a line that fits an RFx answer.";
  - the 100+ line joined to other clauses at josephmurad, annabelliu, holly-morganti, mac-davis01, abhishekmehramd.
- **Speed phrase where speed is not the point:**
  - erin-mynaugh M2 (her question is about the client report);
  - dyan-hes M2, where it is now the whole value line (see E).
- **akallarakuzhi M2:** "Clearing a new measurement type for your pipeline fits a typical basic integration, which takes 2-4 weeks." This ties the typical figure to his case. The card says "do not present it as this company's timeline". It also answers a governance question with an integration timeline.
- **For the coordinator, not scored:** two Crossover lines read as moving part of onsite screening to the phone. The card says "never replaces onsite screening".
  - cristy-d M2: "a phone scan done beforehand could shorten the measuring step";
  - hanna-arch M1: "…and which could move to a phone?".

### C. Brand & tone: 2/3
- "so" benefits: fixed. Amy's three-part run-on: fixed. Ashok's "familiar ground": fixed.
- **alexandra M1 still opens on the third-person aphorism** "An internist at heart builds care models around what clinicians can act on." Her bio says "passionate about making it easier for individuals to access the care supports"; it does not say this.
- **Presumed reactions** (card word traps):
  - rachelstein211 "Teams that weigh a capture tool usually want to see the member flow first.";
  - ginovillani "Partners usually want something they can show";
  - holly-morganti "Consultants want clear answers on devices and measures.";
  - soniaramsey "Consultants like a concrete output to review."

### D. Format & structure: 2/3
- **Fix-round residue that would ship as is:**
  - cristy-d M1: "With FitXpress an employee can also scan on their own phone. With FitXpress the measuring step moves…";
  - josephmurad M1: "Inside Vida's app, a guided two-photo scan returns … inside the app";
  - atersakyan M2: "…sit in the same record as the timestamp. Each record carries a timestamp…";
  - diana-malone M1: "ready when the clinician joins Included Health" (reads as a hire).
- **alexandra:** M1 "and BMI calculated" is still card shorthand. M2 "Waist and BMI … is the moment I had in mind" does not parse.
- **Stale metadata:** amy-mushlin-884504.md "Context used" still says "Hook: path from Anthem…" and "M2 speed phrase", but the copy has neither. The summaries were not regenerated after either round (see the status table).

### E. Output quality: 3/4
- **What improved:**
  - Each named M2 now has a person-specific line.
  - Gate product-sentence repeats fell from 37 notes to 7 notes (24 people).
  - Most M1s are strong: a specific hook, the account fact, a number and an answerable question. Ashok's M1 now has the Omada weigh-in fact.
- **Hollow M2s left by deletion-only fixes:**
  - dyan-hes (eMed CMO): the value line is only "The scan returns 80+ body measurements, under 45 seconds from the photos to structured results." It does not touch her question about what clinicians look at beyond weight.
  - billcampbellsales: only "3DLOOK has worked with 100+ clients."
  - bonnie-grenis: only the 112,100 line.
- **Sampled M2s:**
  - amy: usable, but still twinned with Erin/Shane and repeats 80+ from her M1;
  - alexandra: asks her M1 again and adds no fact;
  - akallarakuzhi: one sentence that does not follow from his question, then "Time that suits you?".

## Top 3 issues (priority for improver)

1. **Fix lists cover sentences, not patterns. Three classes survive campaign-wide:**
   - card-rule restatements (about 30, including the disclaimer-only M2s of lisa-talamini, kevin-masci and abhishekmehramd);
   - card question targets reused as questions (15+);
   - "care team picks/decides" lines.

   The next round needs a campaign-wide pattern scan, not coordinator-picked items.
2. **Same-company repeats the gate does not see:**
   - M1 openers: "Noticed your background" ×3 at Crossover and eMed, plus repeats at Wondr and Vida;
   - Amy↔Erin↔Shane at Vida (product sentence and M2 line 1);
   - the new anishmehtamd↔tony-yuan-md M2 twin;
   - the "A call can/could/would …" shape (Omada) and "I can show … on a call" (MDLIVE).
3. **Deletion without replacement hollowed M2s and left patch residue.**
   - M2s: dyan-hes, billcampbellsales, bonnie-grenis;
   - residue: cristy-d, josephmurad, atersakyan, diana-malone;
   - akallarakuzhi's M2 does not follow from his question, and alexandra's asks the same thing twice.

   The summaries and Amy's context header are stale.

## Coordinator review

```
agreement: ✅ agree
top_issue: the fix lists covered named sentences only; a campaign-wide pattern scan (coordinator, 2026-10-19) still finds 82 paraphrase twins, 54 M1 questions near the card topics, 45 repeated hook templates, 44 card-rule restatements, 13 M2s with no value line of their own, 9 proof lines buried in longer sentences.
```
