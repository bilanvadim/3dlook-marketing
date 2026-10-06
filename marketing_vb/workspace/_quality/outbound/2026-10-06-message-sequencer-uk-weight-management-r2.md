---
qc_date: 2026-10-06
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/ (all 8 _batch-*.md read in full, 8 _summary-*.md, _check.json; baseline workspace/_quality/outbound/2026-10-06-message-sequencer-uk-weight-management.md)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report (round 2): message-sequencer, 2026-10-06, uk-weight-management

**Artifact:** `workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/` (223 people, 8 batches)
**Total: 13/20, marginal (was 11/20, failed).** This needs a targeted rework, not a regeneration. Senior, clinical, technical and partnership copy is now in good shape. The referral copy still breaks the card's central rule (card:35, card:122) in three places:
- LighterLife batch 2 replaced the old off-scan questions with new ones.
- Reset Health's referral pool asks "who owns the Roczen roadmap" 11 times.
- MoreLife batch 2 drifted off the theme list.

**Scoring basis.** Scored against `card-messages.md` and `_profiles-*.md`. Limits, signature, bans, detector and completeness are taken from code. D is not capped for the missing `product:` in the split files (same treatment as the baseline).

## Scores

| # | Category | Score | Max | Baseline |
|---|----------|-------|-----|----------|
| A | Adherence | 3 | 5 | 2 |
| B | Factual accuracy | 4 | 5 | 3 |
| C | Brand & tone | 2 | 3 | 2 |
| D | Format & structure | 2 | 3 | 2 |
| E | Output quality | 2 | 4 | 2 |

## Baseline findings, item by item

**Fixed**
- Reset Health executive and clinical CTA collisions: all ten M1/M2 CTAs named in the baseline are now distinct.
- raquelsanchezwindt's copy of barbara-mcgowan's product sentence is gone, and so is her "one-page overview".
- Lane recipes:
  - FAQ link in M2 for garethbartley (RH1:490), yousaf-ahmad (:512) and alasdair-yorke (:549).
  - Repeatability sentence for barbara-mcgowan (:157), dr-sarah-oldfield (:339), dr-claudia-ashton (:363) and thomas-curtis (:387).
- The company is now named in every M1: deborah-evans, dr-claudia-ashton, andrew-liles, laurensien.
- Speed wording is verbatim everywhere I checked.
- `_summary-reset-health-2.md` exists.
- "100+ clients use FitXpress (today)" is gone in all 9. Every instance now reads "3DLOOK has worked with 100+ clients".
- davidplans M2 splits the 96-97% sentence from body composition (RH1:179-181).
- 112,100 sits in its own sentence (justin-slabbert, annabellhiggs, dr-george-sanders).
- Removed: "22 practitioners" (juli-mey), "the same minute" (matthew-buckley), and david-wong's 34,000 embellishment.
- chiaulingchow M1 now says "could add" instead of describing an existing integration.
- Compliance line: MoreLife has it in 3 M2s (sophie-edwards, grant-westermann, susan-brennan), Reset Health in 2 and mixed in 2. This matches the card's "at most one" ruling.
- Removed from copy:
  - All 4 writer-note leaks.
  - All 3 dangling "as [title]" openers.
  - The 4 tricolons.
  - edna-moneypenny's "help pages".
  - justin-slabbert's "platform worth building on".
- Lowercase greetings (ann, natalie, nikki).
- LighterLife "Who at head office…": 0 in LighterLife copy, down from 58. LL1 "30 years" is down to about 9 in 68.
- Head-office trio: "Grab a slot", the shared speed sentence and the shared "Open to 15 minutes" are gone.
- Counterweight South Africa pool: product sentences are now distinct. "Noticed your background" appears 0 times. The repeated "Came across your work as a registered dietitian" is gone.
- Reset Health: "Noticed" is down from 17 to 2, and "Wanted to reach out" from 3 to 0.
- MoreLife:
  - The GDPR paragraph is down from 11 to 3.
  - "Grab 15 min" is no longer shared.
  - The patient-app question (×3) and the programme-design question (×4) clusters are broken up.
  - The baseline's "you have/know" opener formula and its "X is the thread" M2 formula are both gone.
- Referral M2s no longer carry the speed line.

**Partly fixed**
- Product-lane explicit 15-minute ask: racheldreycroft is fixed. laura-newson has it only in M2 (M1 :59 "Is a short call worth setting up?"). rebecca-ryan has it nowhere (M1 :197, M2 :207).
- juli-mey M2 (ML1:113) still opens with the accuracy figure, now behind a lead-in clause. card:137 says it "never opens Message 2".
- jan-badger and georgina-walsh (both therapists) now word the question differently ("owns the online programme" vs "coordinates online delivery"). Both M2s still open "Thank you for reading" (LL1:99, :660).
- anjal-panamparambil-saji and eltrent-summers no longer match exactly but share one frame: "needs a front and a side photo and [gives back/returns] 80+ body measurements" (ML1:477, :621).
- "you know / you will know" is mostly gone. Still present in phebe-oyinkansola-alabi ("you will appreciate", ML1:367), nicola-gornall ("you know how a course is sequenced", LL2:411) and veronica-barry ("you know people by name", LL1:595).
- 3-sentence paragraphs: most are fixed. pipyoung M1 still has 3 (mixed-1:162).

**Not fixed**
- sophie-edwards M2 (ML1:41) still embellishes the anonymised line: "34,000 scans in 2025, and each followed the same guided sequence on the person's phone".
- dr-george-sanders M2 (ML1:17) still offers volume as evaluation evidence: "One data point for your evaluation work: 112,100 scans…".
- grace-bajo "is a good aim" (ML1:421) and olivia-potter "that is a clear path" (ML1:583) are unchanged.
- The "online programme owner" fallback is still in ann-mcclean M2 (LL1:265), natalie-bellis M2 (LL1:586) and natalie-cowie (LL1:635, :641).
- **LighterLife batch 2 still buys uniqueness with off-scan questions.** The old topics are gone and new ones of the same kind took their place (see E).
- **Reset Health referral product line.** "We build a guided two-photo scan…" still appears in 9 M1s: dr-adam-barker :524, sean-patrick-mcgowan :561, peteryeekk :599, tristandummer :617, amanmohammad :635, kelly-m :653, tiago-grohmann :671, catherine-webb :689, dr-nik-adzrul-ariff :707.

## What is wrong now (specific)

### A. Adherence: 3/5
- **The gate's own near-duplicate notes were left in place and misreported.** `_check.json` lists 52 "near-duplicate sentence" notes inside one company: LighterLife 21, Reset Health 12, MoreLife 19, Counterweight 0. Only 4 of them are the mandated verbatim compliance line. card:122 makes the rest the agent's to fix.
  - `_summary-lighterlife-2` says they are "shared sentence prefixes only; the sentences themselves differ". That is false. Example: kim-stares :194 and amanda-walton :331 share "3DLOOK's FitXpress returns 80+ body measurements from two photos".
  - `_summary-morelife-1` reports only the compliance-line notes and leaves out 15 product-sentence pairs.
  - `_summary-reset-health-1` calls 10 notes "a few".
- **Reset Health referral pool: the same central question 11 times.** "Who owns the Roczen (app/product) roadmap / what goes into Roczen / product lead":
  - Batch 1: siri-steinmo :401, velawson :419/:428, dr-adam-barker :524/:531, sean-patrick-mcgowan :561/:567, peteryeekk :597, tristandummer :615/:623, amanmohammad :633, kelly-m :651/:659.
  - Batch 2: imogen-bole RH2:93, emelia-judge :131, lauren-dolphin :273/:283.
  - The answer, Rochelle Morris (CPO) and Rebecca Ryan (Head of Product), is already on the list.
  - card:105 gives these people their own themes, and those themes were not used: behaviour-change design (siri-steinmo), the psychology team's view of body data (velawson), commercial propositions (sean-patrick-mcgowan) and the finance route (dr-adam-barker, partly used).
- **Shared central questions elsewhere:**
  - Reset Health:
    - alice-fletcher RH2:38 and benjamin-sabri :245, "clinical additions to Roczen".
    - benjamin-sabri RH2:235 and dr-nik-adzrul-ariff RH1:713, the London clinician who reviews new tools. Both are in the 6-person Malaysia pool and both open "Your work as a…".
    - louisa-flannery RH2:112 and emelia-judge :121, coach feedback.
  - Counterweight: idalia-stach :74/:82 and katrina-campbell-wareham :297/:303, programme design, with near-identical M2s.
  - MoreLife:
    - nicola-lyons ML2:179, jaishri-patel :247 and louise-thackeray :332, all "who collects feedback".
    - stephen-young ML2:196 and natalie-shields :383, professional development.
  - LighterLife:
    - anne-matterface LL1:74 and lorraine-addyman :352, online programme development.
    - paul-anthony-brown LL1:390 and sharon-henshaw :559, outside partners.
    - veronica-barry LL1:597 and sally-harris :671, online session materials.
    - bev-robinson LL1:223 and helen-litherland :428, what a client sees after sign-in.
- **Exact shared closing asks inside one company:**
  - "I will approach them directly.": donna-earle-swaby LL1:303 and veronica-barry :605.
  - "One line is enough.": sharon-henshaw LL1:567 and marion-holder LL2:478.
  - "A pointer is plenty.": velawson RH1:428 and tristandummer :623. They also share the question.
  - "I would like to ask them directly.": nicola-lyons ML2:185 and louise-thackeray :338.
  - "…is enough for me.": idalia-stach CW:82 and veronica-wessels :133.
- **The card's assigned themes were not used.** card:103 gives Natalie Cowie and Lyn Obeney the finance/procurement route.
  - natalie-cowie gets the generic online-programme question.
  - lyn-obeney (an accounts assistant) is asked who owns the medication service, and her M2 says "the part of LighterLife I know least about" (LL2:80).
  - The baseline wrongly listed Lyn's cost-centre ask as off-scan. The card allows that ask for her.
- rebecca-ryan (product lane) has no 15-minute ask in either message (RH1:197, :207).

### B. Factual accuracy: 4/5
- **New, compliance-adjacent.** elliottsilver M2 (mixed-1:80): "Photos are deleted… which keeps the scan out of the stock and storage questions." Measurements, body composition and 3D models are stored indefinitely by default (CLAUDE.md §12). Telling a Head of Strategy and Operations that storage questions do not arise is the "processed, not stored" claim in another form.
- sophie-edwards (ML1:41) and dr-george-sanders (ML1:17) are carried over (see above).
- chiaulingchow M2 (RH1:87), "no photos to chase by phone", presumes a current manual process at Reset Health, which card:123 rules out.
- alexnancekievill M2 (RH1:450) promises "15 minutes with an engineer" through Katerina's calendar.
- erin-connors M2 (mixed-1:147-149): "For scale: 34,000 scans… that means a body record the support team can look at" draws a conclusion the number does not support.
- **LL3 fact sent to people who may not be at head office.** card:86 says "Head-office people only".
  - sandra-undefined (LL2:133, Foodpacks) is a unit.
  - samantha-ireland (LL2:449) is listed in Llangamarch, Wales, and her profile does not establish a head-office role.
- **Sourcing.** No number falls outside proof-points.md, no client is named and there is no verification framing. NHS, children, pregnancy, Pharmacy2U, PronoKal (no body composition) and the BL1 health-MOT boundary (mixed-1:436) all hold.

### C. Brand & tone: 2/3
- **"so" introducing a benefit**, a card:141 word trap the gate missed:
  - emily-costelloe ML1:129: "…, so a practitioner can open a session…"
  - keisha-c ML1:173: "…, so a dietitian can compare…"
  - angelina-spathopoulou ML1:339: "…white-label, so a programme's own screens carry it."
- **New tricolon.** emily-costelloe M2 (ML1:137): "no kit to send out, a guided capture that is the same each time, and under 45 seconds…"
- **Reads as covert to a franchisee.** donna-earle-swaby M2 (LL1:301): "You can keep your name out of it."
- **Presumed knowledge and flattery:**
  - carol-graves LL1:329: "makes me think you notice process"
  - sharon-henshaw LL1:565: "suggests you have seen partner conversations begin"
  - anne-marie-tinto LL2:268/:278: "careful checking… where careful people start"
  - plus grace-bajo, olivia-potter, phebe-oyinkansola-alabi, nicola-gornall and veronica-barry (above).
- **Apologetic M2 tics:**
  - ann-mcclean LL1:263: "Last note on this, I promise."
  - joanna-bhart LL1:118: "I should have kept my first note shorter"
  - nikki-cook LL2:91: "That is my product in one line."
- **Strained analogies:** jackie-cook (tours, LL2:211/:219) and nicola-gornall (syllabus, LL2:419).
- laurensien M1 (RH1:239) refers to "Reset Health's governance lead" in the third person when she is that lead.
- nazila-bahrami (CW:91): "Couldn't help but ask someone BANT registered."

### D. Format & structure: 2/3
- **Paragraphs with 3 sentences:**
  - pipyoung M1 (mixed-1:162), not fixed
  - shweta-sidana M1 (RH2:47), new
  - roselle-herring M2 (mixed-1:38), new
- **Summaries misreport the gate** (see A).
- **`_summary-morelife-2` is stale against the copy.**
  - It calls grace-shiplee and victoria-simpson "contract-manager titles".
  - It says traceyhorowitz gets a "supplier question", but the copy asks who sets the brief for new digital features.
- dr-faye-bentley M1 (ML2:279-281) says "adults only" in two consecutive sentences.
- matthew-buckley M1 (ML1:197) says "make sense" twice in a row.

### E. Output quality: 2/4
- **The three baseline samples.**
  - barbara-mcgowan is now strong. M2 carries repeatability and the estimates boundary.
  - chiaulingchow is better: M2 gives an operational value line. The "chase by phone" presumption remains.
  - dr-george-sanders still has the volume-as-evaluation M2.
  - The non-referral copy as a whole would score 3/4.
- **LighterLife batch 2: about 16 of 31 referral questions are about topics a phone scan never touches:**
  - missed-session catch-up (nikki-cook :93)
  - Foodpacks orders (sandra-undefined :133)
  - larger text for older clients (judyhoskins :154/:162)
  - the join link (jackie-cook :211)
  - group size (siobhan-barron :308)
  - newcomer introductions (amanda-walton :329)
  - announcements to group leaders (christine-smith :392)
  - group swaps (carole-brand :428)
  - phone-only clients (marion-holder :468)
  - travelling clients (dianne-bishop :487)
  - prospect-facing website copy (heather-pearle-van-pelz :525)
  - the taster session (jennifer-bell :544)
  - group placement (elaine-wright :563)
  - programme length (paulinehills :582)
  - centre vs online (deborah-rice :639, carried over)
  - stage moves (lorraine-varndell :291)

  Batch 1 adds four more: group timetable (patricia-lyon :466), online help desk (bridget-egglesfield :616), client messaging (angel-collins :371) and data and reporting (pat-ashmore :502).

  Four messages say outright that the question has nothing to do with the product: "Separately," (lyn-obeney :74, amanda-walton :331), "is a separate thing" (sandra-undefined :133) and "My reason for asking is separate" (lee-godwin :508).

  "Which role at LighterLife sets the limit?" or "owns the rule?" (siobhan-barron :320, carole-brand :438) reads to a franchisee as probing operations. That is the reconnaissance risk the baseline named.
- **LighterLife M2 skeleton.** About 14 batch-2 M2s follow "[topic] is my example / the topic." then "Which role/team at LighterLife [verb]?":
  - "Which role at LighterLife…": jackie-cook :219, anne-marie-tinto :280, siobhan-barron :320, amanda-walton :341, carole-brand :438, jennifer-bell :554.
  - "Which team at LighterLife…": judyhoskins :164, lorraine-varndell :299, louise-platt :381, christine-smith :402, heather-pearle-van-pelz :535, elaine-wright :573, paulinehills :592, edna-moneypenny :611.
- **Reset Health hook formula.** "[your background] prompted/raises a question", "is the reason for this note" or "is why I am writing" opens 13 M1s:
  - Batch 1: dr-sarah-oldfield :327, siri-steinmo :399, alexnancekievill :438, yousaf-ahmad :502, peteryeekk :597, amanmohammad :633, tiago-grohmann :669.
  - Batch 2: raquelsanchezwindt :7, shweta-sidana :47, jasoncya :64, emelia-judge :121, davinaa :197, benjamin-sabri :235.
- **Identical sentences at Reset Health:**
  - "Results arrive in under 45 seconds from the photos to structured results." appears in jessicaravenscroft :111 and thomas-curtis :387, with "results" twice.
  - "FitXpress returns 80+ body measurements and a 3D model from two photos." appears in davidplans :171 and imogen-bole RH2:85.
- **Shared proof sentences in peer groups:**
  - "3DLOOK has worked with 100+ clients." in the head-office trio: sarah-kelly LL1:17, tina-horsnell LL2:17, sonel-patel :38.
  - "112,100 scans were run in 2025 across all 3DLOOK customers." in justin-slabbert CW:17 and annabellhiggs :63.
  - sonel-patel M2 (:38) repeats her M1 (:30) and adds only the client count. She is the Head of Programme Online, the owner most LighterLife referral asks point to.

## Per-company mail-merge risk (coordinator's question)

- **LighterLife: MEDIUM (was HIGH).**
  - Fixed: the head-office skeleton and the product line.
  - Still a merge: the M2 skeleton (×14), 21 gate-flagged near-duplicate sentences and off-scan questions in about 20 of 65 referral pairs.
  - Coordinator's count of 4 opener pairs is verified: joanna-bhart :108 / lorraine-kessock-philip :49, tina-horsnell :7 / lyn-obeney :70, lorraine-varndell :289 / amanda-walton :329, louise-platt :371 / carole-brand :428. It undercounts LL1-fact openers: margaret-campbell :51 / dawn-sheppard :483 and julie-johnson :150 / sally-harris :669.
- **Counterweight: LOW-MEDIUM (South Africa pool was HIGH).**
  - "Quick reaction to your" (tommie-wt-breedt :210, nuhaa-van-der-ross :346) is verified.
  - Also:
    - "Wanted to reach out" (annabellhiggs :53, elliot-mcewan :193).
    - "I am looking for the person at Counterweight Ltd in the UK who owns" (veronica-wessels :125, zuheirah-toffar :312).
  - The two Reporting Co-ordinators in the same South Africa office get near-twin M2s: mzwandile-mahlangu :337 "To make it easier: one name or one team… is enough." and warren-ras :388 "Easy to answer: one name or team…".
  - The two diabetes coaches get near-twin M1s: bhavyanshi-chaudhary :227 and katrina-campbell-wareham :295 (CW2 sentence, then "I wonder who [owns its digital side / designs it]").
- **Reset Health: HIGH in the referral pool (26). The executive and clinical team is now clean.**
  - Roadmap question ×11.
  - "We build a guided two-photo scan" ×9. The coordinator counted 4; the gate lists 6 pairs.
  - Hook formula ×13.
  - "Your work as a" ×2 is verified (benjamin-sabri, dr-nik-adzrul-ariff). It sits in the 6-person Malaysia pool on top of a shared question.
- **MoreLife: MEDIUM.**
  - Batch 1: 7 product-sentence near-pairs with one word swapped:
    - julie-hearn :567 / suki-sabine :387
    - richard-ruff :675 / phoebeorango :549
    - evie-comber :657 / phebe-oyinkansola-alabi :367
    - olivia-potter :585 / angelina-spathopoulou :333
    - cherie-trutwein :639 / areesha-r :603
    - anjal-panamparambil-saji :477 / eltrent-summers :621
  - Batch 2 swapped one formula for another:
    - A bare CV-recitation opener in about 11 of 23 M1s. Examples: "came before your" (hamish-burdge :75, sophie-dalpra :228) and "before joining MoreLife" (m-ghezal :58, nicola-lyons :177).
    - "[X] sits with / belongs to someone at MoreLife" in georgia-froude :151, jaishri-patel :253, sohnia-akram :372 and areesha-r ML1:609.

## MoreLife batch 2 referral themes (coordinator's question)

card:104 limits MoreLife to: the adult patient app, Tier 3 programme design, outcome reporting, workplace programmes, programme evaluation, client-services systems, new service bids, practitioner tools and digital inclusion. card:65 sets the lane default as the patient app or programme design.

- **grace-shiplee, research collaborations with universities (:43).** Outside the list. It also points straight at the founding university, which card:74 says never to name. Move her to programme evaluation or outcome reporting.
- **amalia-kyriacou, waiting lists (:315).** Outside the list, and the same off-scan class the baseline flagged at LighterLife (paulinehills). It is also an NHS capacity topic, which card:127 keeps out. Change it.
- **beverley-ambler, health check service lead (:128).** Outside the list, and the riskiest of the three. The NHS Health Check is a commissioned screening that includes BMI. Routing a body scan to its lead implies screening or BMI use, which card:125 rules out. It is the same boundary BL1 draws for health MOTs. Change it.
- Also off-list and unrelated to the scan:
  - venue booking (daniella-hall :111/:117)
  - career development (stephen-young :196) and CPD (natalie-shields :383), which are the same question
  - allocating staff to groups (sohnia-akram :366)
  - the stop-smoking/weight link (helen-campbell-white :349)
  - GP referrer relationships (sophie-dalpra :230, close to card:127)
  - re-joiners (hamish-burdge :77)
  - issue escalation (victoria-simpson :94)
- **On theme:** nikola-smith (practitioner screen), m-ghezal (evidence review), traceyhorowitz (digital feature brief), prestonsarah (digital service lead), phillippa-sellstrom (programme changes), dr-faye-bentley (adult priorities).
- In batch 1: georgia-apsitis (referrals into adult services, :279) and julie-hearn (outreach, :567) are off-list too.

## Top 3 issues (priority for improver)

1. **Rewrite the off-scan referral questions:**
   - LighterLife: the 16 batch-2 person_ids listed under E, plus patricia-lyon, bridget-egglesfield, angel-collins and pat-ashmore.
   - MoreLife: the 10 listed above, starting with beverley-ambler, amalia-kyriacou and grace-shiplee.

   Every question should lead to someone who could put a scan in the online account, between-session use, programme content or a technology partnership. Drop the "Separately…" decoupling (lyn-obeney, amanda-walton, sandra-undefined, lee-godwin). Break the LighterLife M2 "Which role/team at LighterLife…" skeleton.
2. **Reset Health referral pool (26).**
   - Give each person a distinct question. Use card:105's themes for siri-steinmo, velawson, sean-patrick-mcgowan and dr-adam-barker, and stop routing 11 people to the roadmap owner.
   - Rewrite the 9 "We build a guided two-photo scan" sentences and the 13 "[background] prompted/raises a question" hooks.
   - Separate alice-fletcher/benjamin-sabri, benjamin-sabri/dr-nik-adzrul-ariff, louisa-flannery/emelia-judge and velawson/tristandummer.
   - Fix the jessicaravenscroft/thomas-curtis and davidplans/imogen-bole identical sentences.
3. **Claims and cleanup:**
   - elliottsilver storage line (mixed-1:80).
   - sophie-edwards "each followed the same guided sequence" (ML1:41).
   - dr-george-sanders "data point for your evaluation work" (ML1:17).
   - "so"-benefit ×3, the emily-costelloe tricolon, grace-bajo/olivia-potter flattery, donna-earle-swaby "keep your name out of it".
   - 3-sentence paragraphs: pipyoung, shweta-sidana, roselle-herring.
   - rebecca-ryan 15-minute ask.
   - Clear the 48 non-compliance near-duplicate notes in `_check.json` and make the summaries report what is left honestly.

**System notes (not the agent's fault):**
- The near-duplicate check now works and caught 52 pairs. Because it is soft, the writers ignored it and the summaries played it down. Make "near-duplicate sentence" inside one company a hard fail, with the compliance line exempt.
- **card:21 and card:102-105 conflict.** card:21 sets the referral default as "a short ask for the owner of the app roadmap". card:102-105 gives one unique question per person, but the theme lists predate the Apollo top-up (Reset Health: 4 themes for 26 referral people).
  - This conflict is the source of the roadmap clones at Reset Health.
  - The theme lists are thin, so writers fill gaps with operational trivia. That is the source of the off-scan asks at LighterLife and MoreLife.
  - The theme lists should be regenerated for the post-top-up headcount.
- The detector does not catch mid-sentence ", so [benefit]".
- The `juli-mey` "pricing word" note is a false positive on "tier".
- **The coordinator's counts check out:**
  - "head office" appears in 10 pairs, all in the South Africa and Malaysia pools as card:182 requires (7 Counterweight, 3 Reset Health), and 0 times in LighterLife copy.
  - There are 0 writer-note leaks, 0 "use FitXpress/today" and 0 lowercase greetings.
  - The repeated-opener counts are right as far as they go but undercount (see the per-company section).

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: referral questions drifted off the scan (LighterLife batch 2, MoreLife batch 2) and cloned at Reset Health ("who owns the Roczen roadmap" ×11). Root cause is partly the coordinator's round-1 instruction ("no two people share a theme") against card themes of 2-4 per company for 30-60 referral people; round 3 states the rule: the theme may repeat, wording, hook, structure and closer may not, and every question must touch something a body scan plugs into. elliottsilver's "keeps the scan out of the stock and storage questions" is a stored-data misstatement (measurements and 3D models are stored, compliance.md) and is fixed first.
```
