---
qc_date: 2026-10-07
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/ (all 7 _batch-*.md read in full against card-messages.md and _profiles-*.md; samples andresantos-nutrium.md, arnaud-marche-923259123.md, massimo-caprino-8bab5.md; _check.json 2026-10-07T15:57:48)
track: outbound
artifact_type: messages
round: 2
previous_report: workspace/_quality/outbound/2026-10-07-message-sequencer-eu-weight-loss-nutrition.md (10/20)
total_score: 12/20
status: marginal
coordinator_review: done
---

# QC Report (round 2): message-sequencer, 2026-10-07, eu-weight-loss-nutrition

**Artifact:** `workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/` (209 people, 418 messages, 7 batches)
**Total: 12/20, marginal** (round 1: 10/20, failed).

**Verdict.**
- Round-1 Top 3 got fixed or mostly fixed:
  - philippe-l's hook is gone.
  - The 100+ wording is right everywhere.
  - The RN2 contradiction, the 20-minute figure and the round-1 writer-note leaks are gone.
  - jean-jacques now carries the repeatability sentence.
  - Link hygiene is fixed in all 8 messages.
  - RNPC and Dietplus no longer read as one template.
  - 209/209 M1s end on a question (checked by regex).
- **Two new defects came in with the rewrites:**
  1. **The speed phrase was bolted onto "Results arrive…".** That gives "Results arrive in under 45 seconds from the photos to structured results" in **30 messages**. Round 1 flagged this pattern in only 2 messages.
  2. **New factual slips:**
     - daphne-cierniak: "Each 3D model is built from 5M+ points" uses a source-data figure as if it described the output.
     - massimo: "Values … from 38 to 210 kg".
     - 6 repeatability sentences drop the §1.2 hedge "for most measurements".
- **Mail-merge risk is still high** at:
  - BODYHIT: about 18/22 people sit in at least one twin.
  - fitbox: 12/12 referral M2s end on "whoever looks after member experience".
  - Vivafit: 6/6 M2s carry only the speed phrase.
- **Recommendation: line fixes, not regeneration.**
  - Do the speed-phrase and fact fixes mechanically.
  - Then rewrite twins only for the people listed below.

**Scoring basis.** Same as round 1:
- Scored against `card-messages.md`, `_profiles-*.md` and the coordinator rules given to the writers.
- Limits, signature, bans, detector and completeness are taken from the gate as fact.
- The `_summary-*.md` files are stale and were ignored.

Abbreviations: RN = `_batch-rnpc.md`, DP = `_batch-dietplus.md`, BH = `_batch-bodyhit.md`, MX1-MX4 = `_batch-mixed-1..4.md`. Numbers are line numbers in the batch file.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## Round-1 items: verification

| Round-1 item | Status | Evidence |
|---|---|---|
| philippe-l-2914a1130 obesity-story hook | **Resolved** | DP:32 is a role hook (DP1), and nothing comes from the bio. |
| RNPC skeleton | **Mostly resolved** | "A guided scan … from a link the centre sends" is gone. Closers vary. The 112,100 sentence appears ×3 in different words. Residual twins are listed under RN below. |
| Dietplus skeleton | **Mostly resolved** | The "client follow-up there" closer is gone. DP1 is restated in 8/27 messages (round 1: about 18). Residual twins are listed under DP. |
| BODYHIT skeleton | **Not resolved** | The twins moved but did not go away (see the per-company table). sylvie :136 and lila :226 have identical closers, and the gate flags them too. |
| "100+ clients use FitXpress" ×14 | **Resolved** | All 30 occurrences read "3DLOOK has worked with 100+ clients". |
| quentin-fabre: "20 minutes", lowercase name | **Resolved** | He now has a new twin (see BH). |
| ivan-dombes: RN2 contradiction | **Resolved** | RN:591 |
| Writer-note leaks | **Moved, not resolved** | jacques-ley and sophie-canoen are clean. **ingo-huppenbauer MX1:373** now says "a capability the fitbox team can switch on for every studio at once, with nothing to ship". That is the card:39 writer note again. |
| jean-jacques-houben: repeatability, two compliance lines | **Resolved** | DP:82 and DP:95. However, **ellie-heath** and **manuela-abreu1**, both in the clinical lane, have no repeatability sentence (card:74). |
| Link hygiene (8 people) | **Resolved** | Every URL ends its line. A new minor issue is listed under D. |
| CLP / Nutrium / Liva M2s that were only call + GDPR | **Resolved, but thin** | Every M2 has a non-compliance line. Several are thin: a bare proof number or a "timestamped" line. arnaud :57 and marc :162 repeat M1. |
| "you (will) know" presumption ×26 | **Resolved** | None left. Lighter presumptions replaced some of them (see C). |
| "lets" ×3 | **Not resolved** | There are now 4: lila BH:220, scarlett MX1:415, nawel MX3:510 and diogo MX3:631. The detector still misses them. |
| Two compliance lines in one M2 | **Resolved for GDPR + MD** | The new stacking is a data-retention sentence plus the GDPR line (see A). |
| Gate soft "company not named" | **Not resolved** | natálie-černá MX4:375 and matthias-vidal- MX4:673 still have no company line in M1. |

## Per-company skeleton (round 2)

| Company | People | Mail-merge risk | Main residual twins |
|---|---|---|---|
| RNPC | 30 | LOW-MEDIUM | See the RN fixes below. |
| Dietplus | 27 | LOW-MEDIUM | See the DP fixes below. |
| BODYHIT | 22 | **HIGH** | 5 opener stems, 4 product-sentence stems, 4 question twins, 3 M2 twins, and 2 closer families ("a name is enough" ×4; "If this sits with head office, point me to whoever … there" ×3). |
| fitbox | 15 | **HIGH** (new; round 1 did not read this part) | "whoever looks after member experience" closes 12/12 referral M2s, which copies the card's example. "caught my eye" opens 6/15 M1s. ingo :367 and rick :707 share a question (gate flag). |
| Vivafit | 6 | **HIGH** | Each M2's only value line is the speed phrase. "in the club's own flow" appears ×3. |
| NUTRIADAPT | 6 | MEDIUM | pavlína :361 / natálie :383: "The scan is / A scan is two photos, front and side". M2 openers "Results [arrive/take/come back] in under 45 seconds" ×3. |
| Clinique La Prairie | 13 | MEDIUM | simone :30 / rebecca-chia :219: same question. arnaud :49 / marc :154: same product sentence. rebecca-chia :225 / celia :246: same M2 opener (gate flag). 10/13 M2s follow the same shape: [one line] / GDPR / call. |
| Virtuagym | 13 | MEDIUM | pbraam :469 / giulia :602 / bas :659: "Gyms could offer it under their own brand". The question "What/Which … do gyms/clubs ask … for most" appears ×5 (hugo :501, paulo :558, giulia :596, bas :653, fabrice :672). |
| Sidekick | 13 | LOW | saemundur :36 / todd :340: "Our guided two-photo scan returns 80+ body measurements and…". The SK1 and partnership twins are fixed. |
| Het 1 op 1, Liva, Naturhouse, Nutrium, Ysonut, Keepcool | | LOW | Isolated pairs only (see the fixes). |

## What was wrong (specific)

### A. Adherence: 3/5

- **Card:144 uniqueness** still fails at BODYHIT, fitbox, Vivafit and NUTRIADAPT, and in isolated pairs at CLP and Virtuagym (table above).
- **Writer-note leak (card:35/:39):** ingo-huppenbauer MX1:373.
- **Clinical lane without the repeatability sentence (card:74):** ellie-heath MX3:370-382 and manuela-abreu1 MX3:677-689.
- **"Name the company in every Message 1" (card:144):** natálie-černá MX4:375 and matthias-vidal- MX4:673.
- **Coordinator rule "M2 value line that M1 did not use":**
  - It repeats M1 at arnaud MX2:57, marc MX2:162, florence MX4:17, nadia MX4:103, denise MX1:617 and natálie MX4:383.
  - There is no value line at all at philippe-monlauzeur RN:119 and thierry-bernabe RN:499.
- **Coordinator rule "at most one compliance sentence; referral none":**
  - **Data-retention sentence plus the GDPR line in one M2:** jacques-ley DP:67/:70, sigga MX1:148/:150, jessica MX3:330/:332, miguel MX3:708/:710.
  - **Data-retention line used as a referral value line:**
    - hélène DP:337
    - cristine DP:513
    - corentin BH:289 (a segment C club, where card:152 allows no compliance line at all)
    - justine-fendeler MX3:589
- **"Never pitch a unit to adopt anything" (card:149):**
  - louisdenazelle RN:153
  - laurent-dereudre RN:299
  - jeanne DP:373
  - amandine DP:484
  - hélène DP:331
  - rolf MX1:463
  - séverine MX3:560
  - nadia MX4:93
- **Units shown as owning the app or the flow:** "the club's own (app) flow" at clement MX4:73, patricia-cavalleri MX4:523, paulo-rocha MX4:609 and diana MX4:631. The Keepcool and VivaFit apps belong to the networks. Round 1 flagged the same pattern at BODYHIT.
- **Outcome framing (card:155):** françois-xavier BH:191 asks about "a member who has missed a few sessions". This is the adherence framing that round 1 removed at Dietplus.
- **Technical lane without the FAQ link (card:76):** salvatoretipaldi MX2:526.

### B. Factual accuracy: 3/5

- **daphne-cierniak DP:578: "Each 3D model is built from 5M+ points."**
  - In `proof-points.md`:59, "Points in source 3D model" belongs to the Dataset Generation Protocol. `how-it-works.md`:23 and :70 tie it to the source data and the reference scanner. It does not describe the model a scan returns.
  - It is also not in card:154's list of citable numbers.
  - This is a misattributed number, sent to a franchisee.
- **massimo MX2:15: "Values are measurements and estimates …, from 38 to 210 kg."**
  - 38-210 kg is the weight range of the people covered (`proof-points.md`:70, `faq.md`:17). It is not a property of the values.
- **The repeatability hedge is dropped in 6 messages.**
  - Affected: massimo MX2:7, saemundur MX1:44, victor MX2:347, nuno MX2:583, manel MX4:211 and fumi MX3:230.
  - They read "Typical scan-to-scan differences are less than 1 cm". §1.2 says "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm", and CLAUDE.md requires that wording verbatim.
  - Round 1 passed this wording, and that was a miss.
- **Speed variants the card bans:**
  - johanna DP:557, "Photos are processed in under 45 seconds", is a processing-only variant (proof-points Speed row).
  - pavlína MX4:361, "the specialist gets the results straight away", is a speed claim with no verbatim phrase.
- **Embellished anonymised proof:**
  - anna-dhervillers BH:375: "34,000 scans …, all from phone photos". Round 1 removed this same addition at damien-cacaret.
  - dennis-krebs MX1:592: "on the same sequence".
  - célestine MX3:495: "3DLOOK ran 112,100 scans". The card's subject is the customers; round 1 fixed this at fredericferet.
- **Minor:**
  - fumi MX3:230, "the values are estimates": body measurements are measurements.
  - gummiv MX1:244 "The integration is small" and ruben-visser MX2:689/:697 "should take little effort" / "Rollout is light" are effort claims the card does not support.
  - **A practitioner screen is promised** at nicolas RN:139, corinne-malitte RN:219, nadège RN:319, cynthia RN:399, cécile RN:539 and justine-fendeler MX3:583. They say "dietitian's view/screen/side" or "on screen". `how-it-works.md`:48 says the host app owns result display, and RNPC/Naturhouse have no host app.
- **What holds:**
  - No client names, prices, medication or prospect figures.
  - No "app" in RNPC, Dietplus, Naturhouse or Ysonut copy.
  - The GDPR, MD, 34,000, 112,100 and 100+ sentences are cited correctly.
  - The photo-deletion and scan-ID statements match compliance.md: no "not stored" and no "no personal data".
  - 96-97% never opens an M2 and never shares a sentence with body composition.

### C. Brand & tone: 2/3

- **The notable round-1 lapse (philippe-l) and the "you know" ×26 pattern are gone.** The lapses that remain are lighter and lower in density.
- **"let" (terminology ban; detector miss):** lila BH:220, scarlett MX1:415, nawel MX3:510, diogo MX3:631.
- **"so" introducing a benefit:** samya DP:314 ("so every client records the same way", which also implies inconsistent capture today) and ingo MX1:363.
- **Presumed reaction:**
  - tobias MX1:202, "A question product teams ask first is…"
  - patrik MX1:519, "A product person will want to see it"
  - stéphanie BH:168, "how little setup a BODYHIT studio wants"
  - florence MX4:7, "has to work the same way in every club"
  - susanne MX1:175, "Scale is the useful fact for a commercial lead"
- **Flattery:** patrik MX1:509 "a good lens for this", dennis MX1:582 "a good person to ask", lise MX3:270 "a good mix for this question", julien MX4:653 "a clear idea".
- **Tricolons:**
  - thierry RN:499, "15 minutes, a live scan, your questions"
  - amandine DP:492
  - paulo-cudjo MX2:564
  - tobias MX1:202 (four fragments)
  - arnaud MX2:49 (a four-item list after "ship, stock or install")
- **"it" referring to a person ("the coach … scans it selects"):** natacha DP:17, nathalie-peron DP:247, sophie-canoen DP:427. Round 1 fixed this at manuela.
- **Hard for second-language readers:**
  - massimo MX2:9: "Which of the four pillars would look at…" (a pillar looking at something).
  - vanda MX4:587: "gives them" has no antecedent.
  - yann MX4:127: "from the link to results in under 45 seconds from the photos to structured results".

### D. Format & structure: 2/3

- **The doubled "results" in the speed phrase appears in 30 messages.** Round 1 flagged it at 2.
  - RN: patrick :15, damien-cacaret :57, philippe-monlauzeur :111, laurent-dereudre :291 ("within under"), cynthia :391, sophie-prunier :459, justine :559
  - DP: natacha :17, damien-haessler :161, valéry :534 ("The wait for structured results is … to structured results"), johanna :557
  - BH: raphaëla :84
  - MX4:
    - florence :17
    - elisa :39
    - clement :81
    - nadia :103
    - yann :127
    - valerie-delage :169
    - qnko :231
    - bc-katarina :275
    - marta :297
    - eliška :319 ("gets structured results … to structured results", the exact round-1 defect)
    - romana :339
    - daniel :405
    - mihalis :427
    - patricia-cavalleri :531
    - vanda :595
    - julien :661
    - ludo :701
  - robert MX4:253, "show how the capture works … in under 45 seconds", reads as if the demo takes 45 seconds.
- **The calendar URL follows a proof sentence that ends in a colon**, so it reads as the source of the number:
  - RN: paul :179, karine :259, nadège :319, fannysoleil :359, gwénaëlle :419, sandra :439
  - MX4: qnko :231
- **The value line comes after the link or the pointer:** stéphanie BH:176 and quentin BH:354 (call → accuracy → link), lars MX4:451, matthias MX4:683.
- **No call-offer wording, only a bare link label:** rebecca-becky-brown MX2:393 ("My calendar:") and simonaurik MX2:547 ("Slot here:").
- The missing `product:` in the split files is not capped (script format, as in round 1).

### E. Output quality: 2/4

- **Good:**
  - The RNPC and Dietplus rewrites now read person by person.
  - Reference-grade or close to it:
    - gunnar-mau MX1:538 (trainer handover question)
    - justine-desprez RN:553
    - corinne-brunet RN:71-73
    - sandra-fontalba RN:433
    - jc-heyneke MX2:297-299
    - fntneves MX3:771-775
    - andresantos MX3:604-608
  - Every M2 has the calendar link, and every referral M2 has an easy out.
- **Still templated:** BODYHIT, fitbox and Vivafit (table above). A screenshot forwarded between two franchisees in any of these three networks will read as a mail merge.
- **Thin M2 value lines.** About 40 M2s carry only a proof number, "timestamped", or the speed phrase. That meets the coordinator's rule, but not the M2 template's purpose ("value … for their world").
- **The 30 doubled speed phrases read machine-made.** They need a mechanical fix before import.

## Line-level fixes per person_id

### RN (`_batch-rnpc.md`)

- **Doubled speed phrase:** patrick-gaytte-8b009b122 :15, damien-cacaret :57, philippe-monlauzeur-71bb9645 :111, cynthia-grosbois-4a6017135 :391, sophie-prunier-b86a73136 :459, justine-desprez-372b3b266 :559.
- **laurent-dereudre-58961710a:**
  - :291 "within under 45 seconds" is ungrammatical.
  - :291 "Noticed you run an RNPC centre" says nothing.
  - :299 "what the team would learn" is a unit pitch.
- **philippe-monlauzeur-71bb9645:** :119 the M2 needs a value line.
- **thierry-bernabe:**
  - :499 the M2 needs a value line, and "15 minutes, a live scan, your questions" is a tricolon.
  - :493 the question twins karine-le-meaux-53858983 :253. This round-1 twin was not fixed.
  - :491 "Two photos from the client give" twins nadège-pilat-b97256110 :311 ("…add").
- **delphine-thierry-7041a4a5 :331 / ivan-dombes-0b8031399 :591:** both M1s open "RNPC offers free follow-up afterwards".
- **céline-terpreau-4546ba102 :282 / ivan-dombes-0b8031399 :602:** both close "a pointer is welcome".
- **louisdenazelle:**
  - :151 the "Noticed your …" opener twins thomas-hervé-7b6003213 :511.
  - :153 the question makes the centre the adopter.
- **thomas-hervé-7b6003213:** :519 the M2 value line twins nathalie-moreau-a029a231 :99 (same sequence on any phone).
- **fannysoleil:**
  - :351 "one of the centres" mentions other centres (card:144).
  - :353 the "from welcome to goodbye" question twins valérie-guigou-0a831b57 :193 ("from arrival to departure").
- **The link hangs off a proof sentence ending in a colon:** paul-de-castries-2a823146 :179, karine-le-meaux-53858983 :259, nadège-pilat-b97256110 :319, fannysoleil :359, gwénaëlle-queguiner-08996a136 :419, sandra-fontalba-5a22a5136 :439.
- **The M2 promises a dietitian's screen:** nicolas-charpentier-87901546 :139, corinne-malitte-46b601122 :219, nadège-pilat-b97256110 :319, cynthia-grosbois-4a6017135 :399, cécile-troisgros-8a8b16263 :539.
- **christine-fremond-67577a7a:** :231 "clients who live far from RNPC Caen" is not in the profile.

### DP (`_batch-dietplus.md`)

- **daphne-cierniak-100558425:** :578 drop the 5M+ sentence (misattributed and not in card:154). **Fix first.**
- **johanna-yung-19b890330:** :557 "Photos are processed in under 45 seconds" is a banned processing-only variant. Use the verbatim phrase.
- **Doubled speed phrase:** natacha-alonso-valckx-35888b100 :17, damien-haessler-099693121 :161, valéry-leprevots-04a9ab35b :534.
- **"it" for a person:** natacha-alonso-valckx-35888b100 :17, nathalie-peron-6878ab92 :247, sophie-canoen-loucheur-982357314 :427.
- **natacha-alonso-valckx-35888b100 :11 / magali-le-gendre-8296b2120 :132:** the "What do clients in [place] do between two [visits/sessions]?" question twins.
- **damien-haessler-099693121:**
  - :151 the opener twins nathalie-peron-6878ab92 :239 ("Dietplus [town]: … a free first assessment, then weekly sessions"). This round-1 twin was not fixed.
  - :155 the question mirrors amandine-poirier-423b16350 :486.
  - :164 the closer twins sophie-canoen-loucheur-982357314 :430 ("whoever defines/sets the coaching method").
- **magali-le-gendre-8296b2120 :128 / hélène-bellod-642366172 :327:** the opener stem "Dietplus [town] comes after…" twins.
- **isabel-barreto-ma-b-isabel-b2-ab1756101 :226 / philippe-l-2914a1130 :42:** identical M2 opener "3DLOOK has worked with 100+ clients." (gate flag).
- **jacques-ley-8a5818148:** :67 drop the data-retention sentence; the GDPR line at :70 is the one allowed sentence. Give the M2 a value line instead.
- **hélène-bellod-642366172:**
  - :331 the question asks the unit where the tool would fit.
  - :337 the data line has no place in a referral M2.
- **cristine-baumert-040781353:** :513 replace "Outputs can be deleted by scan ID" with a value line for a centre.
- **samya-mikou-8833a2140:** :314 drop "so every client records the same way".
- **jeanne-guigui-963698150:**
  - :373 "a possible addition to the weekly visit" is a unit pitch.
  - :381 "shown next to a 3D model" is a display claim.
- **amandine-poirier-423b16350:**
  - :484 "with a possible answer attached" is a unit pitch.
  - :492 is a tricolon.

### BH (`_batch-bodyhit.md`)

- **sylvie-plichta-77069a164 :136 / lila-sodano-139852256 :226:** identical closers, and chloetraina :44 uses the same stem. Give each a different ask.
- **killian-chotard-758672167 :145 / ines-h-344686185 :459:** identical product sentence; angelo-phirate-86767131b :390 is near.
- **killian-chotard-758672167 :147 / ines-h-344686185 :461 / quentin-fabre-08164b27b :348:** "What can a member … look at/open between/after sessions" twins.
- **killian-chotard-758672167 :159 / quentin-fabre-08164b27b :358:** "forward me to whoever picks new services for…" twins.
- **stéphanie-teixeira-44975716b :176 / quentin-fabre-08164b27b :354:** identical accuracy sentence, and the link sits detached after it.
- **hassatou-diallo-92b459170 :444 / juline-boulanger-368487141 :490:** the M2 value line twins (gate flag).
- **sylvie-plichta-77069a164 :124 / hassatou-diallo-92b459170 :438:** "How do you introduce a new tool…" twins.
- **françois-xavier-quéré-82a0a517b:**
  - :191 drop the missed-sessions framing.
  - :191 twins anna-dhervillers-491a8628b :369 ("keep in touch/contact with members").
  - :197 the M2 opener twins jan-alan-96385423a :312.
- **julie-lacoste-5aa27584 :55 / audrey-boussin-473997223 :237:** the "review/walk a member through progress" questions twin.
- **chloetraina :30 / damien-rollin :258:** the "Came across your work in X before BODYHIT Y" openers twin.
- **Opener stems:**
  - jan-alan-96385423a :304 / angelo-phirate-86767131b :390, "Quick idea for"
  - patricia-gouedard-411015132 :99 / ines-h-344686185 :459, "Quick reaction to your"
  - virginie-bourgerie-978a4720b :323 / anna-dhervillers-491a8628b :367, "Wanted to reach out about"
- **Product stems:**
  - stéphanie :168 / hassatou :436 / damien-rollin :258, "FitXpress needs…"
  - sylvie :122 / audrey :235, "FitXpress turns…"
- **"a name is enough":** julie :67, françois-xavier :203, damien-rollin :272, angelo :404. damien-rollin and angelo share the whole clause.
- **lila-sodano-139852256:** :220 "lets".
- **corentin-bernard-47b65723b:** :289 drop the data line (segment C allows no compliance line).
- **anna-dhervillers-491a8628b:** :375 drop "all from phone photos".
- **raphaëla-capelle-88a711196:** :84 doubled speed phrase.
- **stéphanie-teixeira-44975716b:** :168 "how little setup a studio wants" is a presumption.

### MX1 (Sidekick, fitbox)

- **ingo-huppenbauer:**
  - :373 remove the card:39 writer note.
  - :363 drop "so".
  - :367 the question twins rick-reinhard-37615b262 :707.
- **fitbox closers:** rewrite all but one of:
  - jan-sasse-0bb55a49 :449
  - rolf-haberlah-1682a5ba :474
  - jean-maurice-pohl-ab2806bb :499
  - patrik-von-rochow-a5a303192 :524
  - gunnar-mau-06111972 :549
  - sanja-kuche-80203822b :572
  - dennis-krebs-a30048235 :597
  - denise-neudeck-1252302ab :622
  - roland-wingert-wingert-ab6397350 :645
  - ilija-bozic-b7165532a :668
  - antonia-schulz-b1b86021b :693
  - rick-reinhard-37615b262 :718
- **fitbox "caught my eye":** keep one of scarlett-schwarz-418ab09a :413, jan-sasse-0bb55a49 :436, gunnar-mau-06111972 :534, denise-neudeck-1252302ab :607, antonia-schulz-b1b86021b :678, rick-reinhard-37615b262 :703.
- **ulrike-kaiser-75086b22b :388 / rolf-haberlah-1682a5ba :459:** "Noticed your … background" twins. rolf :463 also frames the unit as the decider.
- **denise-neudeck-1252302ab:** :617 the M2 repeats M1 (80+ body measurements).
- **dennis-krebs-a30048235:** :582 flattery; :592 drop "on the same sequence".
- **patrik-von-rochow-a5a303192:** :509 flattery; :519 presumption.
- **scarlett-schwarz-418ab09a:** :415 "lets".
- **saemundur-oddsson-md-148867115:**
  - :44 restore "For most evaluated measurements…" (§1.2).
  - :36 the product sentence twins todd-peavey-5a00703 :340.
- **tobias-gerdes:** :202 presumption and a four-item list.
- **gummiv:** :244 "The integration is small".
- **sigga-ingadottir-2b404639:** :148 drop the data-retention sentence or the GDPR line at :150, not both.

### MX2 (Clinique La Prairie, FitForMe, Virtuagym)

- **massimo-caprino-8bab5:**
  - :15 fix the 38-210 kg sentence ("The scan covers people from 38 to 210 kg.", as in ellie and manuela).
  - :7 restore the §1.2 hedge.
  - :9 a pillar cannot look at a record.
- **arnaud-marche-923259123:**
  - :57 the M2 value line repeats M1.
  - :49 is an over-long list.
  - :49 twins marc-sabatin :154.
- **marc-sabatin:** :162 the M2 repeats M1.
- **simonegibertoni :30 / rebecca-chia-lung-chang-v-23bb2b394 :219:** the "stay in touch after a stay" questions twin.
- **rebecca-chia-lung-chang-v-23bb2b394 :225 / celiazouggagh :246:** identical M2 opener.
- **victor-keunen :347 and nuno-ax-figueiredo :583:** restore the §1.2 hedge.
- **pbraam :469 / giuliamarinelli :602 / bas-harmsen :659:** "Gyms could offer it under their own brand" twins.
- **hugobraam :501 / paulo-cudjo-26b060157 :558 / giuliamarinelli :596 / bas-harmsen :653 / fabrice-g :672:** the "What do gyms/clubs ask … for most" question family; split at least three of them.
- **salvatoretipaldi:** :526 add the FAQ link (technical lane).
- **ruben-visser-6a3b0b43:** :689 / :697 make no effort claims.
- **paulo-cudjo-26b060157:** :564 tricolon.
- **rebecca-becky-brown :393 and simonaurik :547:** add an actual call offer.

### MX3 (Het 1 op 1, Liva, Naturhouse, Nutrium)

- **ellie-heath-6704b422 and manuela-abreu1:** add the §1.2 repeatability sentence (clinical lane, card:74).
- **fumi-f-29a048153:** :230 restore the hedge; "values are measurements and estimates".
- **jessica-bartlett-0a3076106 :330 and miguelsolino :708:** keep only one compliance-type sentence per M2.
- **justine-fendeler-89925a182:**
  - :589 replace the data line with a value line.
  - :593 the closer twins sandrine-bagnols-naturhouse-96b54967 :453 (the card example verbatim).
  - :583 "on screen".
- **célestine-fischer-287a67252:** :495 make the customers the subject of the 112,100 sentence.
- **nawel-tazdait-85750320a :510 and diogoalves92 :631:** "lets".
- **linda-ramaaker :128 and séverine-bertrand-0a6a2a352 :560:** the questions ask the unit how it would adopt the tool.

### MX4 (Keepcool, Ysonut, Metabolic Balance, NUTRIADAPT, Nutrimed, SATISFEAT, Fabulous, Vivafit, maju)

- **Doubled speed phrase (17):** see D. Use the bare verbatim sentence, for example "It takes under 45 seconds from the photos to structured results." Also fix yann-malaud :127 and robert-buschbacher-23440b217 :253.
- **pavlína-dědečková-9a57b2b9:**
  - :361 drop "straight away".
  - :361 twins natálie-černá-aa961a146 :383.
- **natálie-černá-aa961a146:**
  - :375 name NUTRIADAPT and add a line only NUTRIADAPT gets.
  - :383 the M2 repeats M1.
- **matthias-vidal-:**
  - :673 name maju and add a line only maju gets.
  - :683 the value line comes after the link.
- **manel-nieto-96907736:** :211 restore the §1.2 hedge.
- **Vivafit M2s:** give patricia-cavalleri-35bb3466 :531, vitor-costa-a0a645224 :553, renato-monteiro-8b638621 :573, vanda-lopes-a599a360 :595, paulo-rocha-315452115 :617 and diana-sousa-99943934b :639 different value lines. Keep the speed phrase in at most two of them.
- **"the club's own (app) flow":** clément-favé (cl%c3%a9ment-fav%c3%a9-169b7b178) :73, patricia-cavalleri-35bb3466 :523, paulo-rocha-315452115 :609, diana-sousa-99943934b :631.
- **vanda-lopes-a599a360:** :587 "them" has no antecedent.
- **nadia-battery-497153a0:**
  - :93 unit pitch.
  - :103 the M2 repeats M1.
  - :107 the closer twins clément :83.
- **florence-bernard-colombat-3845361b0:** :7 presumption; :17 the M2 repeats M1.
- **satisfeat-larsbeckmann:** :451 move the value line before the call offer.

## Top 3 issues (priority for improver)

1. **Speed phrase pasted into "Results arrive…" in 30 messages**, plus the banned variants at johanna DP:557 ("processed") and pavlína MX4:361 ("straight away"). Fix mechanically before import. The rule "verbatim or none" made writers append the phrase to sentences that already said "results".
2. **Factual slips introduced by the rewrites:**
   - daphne-cierniak DP:578 "built from 5M+ points" (source-data figure presented as the output).
   - massimo MX2:15 "Values … from 38 to 210 kg".
   - The §1.2 hedge dropped in 6 repeatability sentences.
   - ellie-heath and manuela-abreu1 in the clinical lane without the repeatability sentence.
   - The ingo-huppenbauer MX1:373 writer-note leak.
3. **Franchise templates remain at BODYHIT (about 18/22 people in twins), fitbox (12/12 referral closers on "whoever looks after member experience") and Vivafit (6/6 M2s with only the speed phrase).** Rewrite only the listed people. RNPC and Dietplus need only the residual pairs.

**System notes (not the agent's fault):**
- **Gate:**
  - Add a hard check that rejects the speed phrase when "result(s)" appears earlier in the same sentence, and when "processed"/"straight away"/"within under" appear.
  - Add a §1.2 check: "less than 1 cm" without "most" should fail.
  - The detector still misses "lets".
- **Card:**
  - card:78 still gives the pointer as a full example sentence ("whoever looks after client follow-up there"; "member experience at fitness networks"). fitbox copied it 12 times. Name the target and drop the sentence.
  - Add "5M+ points" to card:154's exclusions explicitly, or keep the figure out of the card's proof-points excerpt.
  - The lane text "Nothing to ship, stock or install" is copied verbatim into 5 M1s across companies (arnaud, marc, victor, ruben, ulrike), and it is a tricolon. Mark it as a writer note.
- **Coordinator rule clarification:** say whether the data-retention sentence ("photos are deleted after processing or within 30 days", "deletable by scan ID") counts as a compliance sentence. Writers used it as a free value line in 8 product, ops and referral M2s.
- **notify.py was not run** (this session has no shell tool). Text for the coordinator to send:
  `QC: message-sequencer → 12/20 (marginal), round 2 (was 10/20) | Top issue: speed phrase doubled ("Results arrive … to structured results") in 30 messages + daphne "5M+ points" misattribution; BODYHIT/fitbox/Vivafit still templated | File: workspace/_quality/outbound/2026-10-07-message-sequencer-eu-weight-loss-nutrition-r2.md`

## Coordinator review

```yaml
coordinator_review:
  agreement: agree
  top_issue: "The doubled speed sentence in 30 messages was caused by the coordinator's own round-1 rule ('verbatim phrase or no speed figure'): writers bolted the phrase onto existing 'Results arrive…' sentences. Round-3 instruction: the phrase never shares a sentence with 'result(s)'."
  notes:
    - "Default taken for round 3: a data-retention/deletion sentence counts as a compliance sentence (at most one per M2; product/operations keep only the GDPR line; referral has no data line as its value line)."
    - "fitbox referral easy outs copied the card's example pointer ('whoever looks after member experience'), the same card-example leak as Dietplus in round 1: card line 78 should give the pointer target, not a sentence."
    - "Coordinator stem grep (first five words, >=3 per company) missed BODYHIT's mixed opener/question/closer twins and fitbox's M2 closers because it counted only the last M2 sentence and pairs of 2 were under threshold."
```
