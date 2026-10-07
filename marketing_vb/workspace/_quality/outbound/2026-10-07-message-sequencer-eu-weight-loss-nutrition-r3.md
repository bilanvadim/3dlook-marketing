---
qc_date: 2026-10-07
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/ (all 7 _batch-*.md read in full against card-messages.md and _profiles-*.md; _check.json 2026-10-07T16:14:01)
track: outbound
artifact_type: messages
round: 3
previous_report: workspace/_quality/outbound/2026-10-07-message-sequencer-eu-weight-loss-nutrition-r2.md (12/20)
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report (round 3): message-sequencer, 2026-10-07, eu-weight-loss-nutrition

**Artifact:** `workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/` (209 people, 418 messages, 7 batches)
**Total: 13/20, marginal** (round 1: 10, round 2: 12).

**Verdict: not ready for Vadim's review yet. One more pass of line fixes is needed. Do not regenerate.**

- **What got fixed:** almost all of the round-2 line-level fixes landed.
  - The 30 doubled speed phrases are gone. So are daphne's "5M+", massimo's "38-210 kg values" and the dropped §1.2 hedges.
  - ingo's writer-note leak is gone. So are the "dietitian's screen" promises, the "lets", the unit pitches and the "club's own app" lines.
  - 209/209 Message 1s end on a question (checked by regex).
- **What still blocks sending:**
  1. **jmhellendoorn's Message 1 contains a link** (MX2:402). The card says Message 1 carries no link. The gate only looks for the calendar link in Message 1 (`outbound_pack.py`:1739), so this one passed.
  2. **11 easy outs reuse the card's example sentence** ("if this sits with head office, point me to whoever looks after client follow-up there"). That breaks the round-3 rule. One of them is verbatim (sandrine MX3:453).
  3. **The compliance-sentence rule is broken twice:**
     - salvatoretipaldi (`product` lane) has a data-retention line as his only Message 2 value line (MX2:526).
     - aminelaadhari has the deletion sentence in Message 1 (MX4:485), and his Message 2 carries the GDPR line as well.
  4. **6 Message 2s repeat Message 1 or have no value line.**
  5. **The speed phrase has a new subject variant, 12 times in MX4:** "A client / member / user is done in under 45 seconds from the photos to structured results". Two BODYHIT Message 2s say "Capture to output takes … from the photos to structured results". That doubled range is the round-2 defect again, with "output" in place of "results", so the coordinator's "result(s)" check does not catch it.
- **Mail-merge risk:**
  - **BODYHIT is still HIGH**, with about 16/22 people in at least one twin.
  - **The Dietplus Message 2s got worse.** 15/27 now open in one of five stems ("Body composition estimates come from the same photos", "The scan also returns / It also returns", "The same capture … any phone", "The record is …", "Each … timestamp").
  - **maju (3/3), Fabulous (3/3 speed-only Message 2s) and NUTRIADAPT (5/6 speed-only Message 2s)** read as templates.

**Scoring basis.** Same as rounds 1 and 2:
- Scored against `card-messages.md`, `_profiles-*.md`, the r2 report and the coordinator's round-3 rules.
- The coordinator's mechanical results are taken as fact: the gate, 0 speed+results doublings, 0 "5M+" and the "let" count.

Abbreviations: RN = `_batch-rnpc.md`, DP = `_batch-dietplus.md`, BH = `_batch-bodyhit.md`, MX1-MX4 = `_batch-mixed-1..4.md`. Numbers are line numbers in the batch file.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## Round-2 line-level fixes: verification

**Resolved:** every r2 fix not listed below. That includes:
- all 30 doubled speed phrases
- johanna's "processed" and pavlína's "straight away"
- daphne's 5M+ and massimo ×3
- the §1.2 hedge at victor, nuno, manel and fumi
- ellie and manuela now carry the repeatability sentence
- ingo's leak and "so"
- every "lets"
- the colon-before-link pattern ×7
- the dietitian-screen lines ×5
- the unit pitches ×8
- "the club's own flow" ×4
- natálie and matthias now name their company
- jacques-ley, sigga, jessica and miguel no longer stack two compliance sentences
- the data lines at hélène, cristine, corentin and justine-fendeler
- the "it"-for-a-person lines ×3
- the RN and DP pairs listed in r2
- vanda, nadia, florence and satisfeat

**Not resolved, or resolved in a way that adds a new defect:**

| person_id | r2 item | Now |
|---|---|---|
| saemundur-oddsson-md-148867115 | MX1:44, restore §1.2 verbatim | It reads "For most measurements, repeated scans produced typical differences of less than 1 cm". That passes the "most" check but is not the §1.2 sentence: "evaluated", "showed" and "scan-to-scan" are missing. |
| simonegibertoni / rebecca-chia-lung-chang-v-23bb2b394 | question twin | Still twins (MX2:30 "How do guests stay in touch with the clinic once a stay ends?" vs :219 "How is contact with a guest arranged once they leave?"), and lorenzoamaglio :72 joins them. |
| paulo-cudjo-26b060157 / bas-harmsen | "What do gyms ask … most" | Still twins: MX2:558 / :653 "… do [gyms/enterprise clubs] ask Virtuagym for most in the … app?" |
| justine-fendeler-89925a182 | MX3:593, closer twins sandrine | Both still carry the card example: sandrine :453 verbatim, justine :593 with one word changed. |
| jan-sasse-0bb55a49 (fitbox closers) | 12 closers on one stem | 11 were rewritten, but the one kept (MX1:453) is the card example sentence, and 3 new pairs appeared (see the MX1 fixes). |
| thomas-hervé-7b6003213 | RN:519, value line twins nathalie-moreau | The new line "The capture asks for two photos, front and side." repeats his Message 1 (:511). |
| stéphanie-teixeira-44975716b | BH:176, value line after the call offer | The order is still call offer → accuracy line → link. |
| susanne-burger-0a75032a | MX1:175, presumption (r2 C list) | "Scale is the useful fact for a commercial lead." is still there. |
| salvatoretipaldi | MX2:526, add the FAQ link (technical lane) | **The r2 premise was wrong.** `_profiles-mixed-2.md` puts him in the `product` lane. The writer added a data-retention sentence, which round 3's rule does not allow in `product` (see the must-fix list). |

## The four phrases the coordinator asked about

- **"The 3D model stays a view each gym chooses to show" (pbraam MX2:469).**
  - It is not an invented claim: it restates the card's rule at card:151.
  - It is a card instruction used as copy, though (card:158).
  - "stays" assumes context Paul was never given.
  - It is also a CEO's only value line. Replace it.
  - The same rule sentence appears in **24 messages**. fitbox alone has 7 of 15.
- **"BMI and BMR as calculated values"** (raphaëla BH:84, rebecca-chia MX2:225, rebecca-becky-brown MX2:389, timonahuijs MX2:621, asger MX3:205), and "BMI and BMR are calculated from the same (two) photos" ×5.
  - **Accurate.** See card:154, `how-it-works.md`:18 ("derived from model") and the body_measurement_terms rule.
  - No defect.
- **"a white-label member app"** appears only in Virtuagym copy (MX2:461, 518, 556, 632, 670, 689). It is VG1 verbatim. No defect.
- **"Between visits to RNPC Caen, a client can scan from home" (christine-fremond RN:231).** No prospect fact is invented, but there are two small problems:
  - The present-tense "can" reads as if the scan is already offered at Caen.
  - The line twins nathalie-moreau RN:91 ("Between consultations at the RNPC centre in Verrières le Buisson, a client can take two photos…").

## What was wrong (specific)

### A. Adherence: 3/5

- **Message 1 carries a link:** jmhellendoorn MX2:402 (the FAQ URL). It also repeats in Message 2 (:410).
- **Round-3 rule "easy outs never reuse the card's example sentence": broken 11 times.**
  - Verbatim, or with one noun swapped:
    - damien-cacaret RN:62
    - thierry-bernabe RN:502
    - jan-sasse MX1:453
    - celiazouggagh MX2:246
    - fabrice-g MX2:678
    - clgabriel MX3:69
    - nandazwart MX3:184
    - sandrine MX3:453
    - justine-fendeler MX3:593
    - clément MX4:83
    - patricia-cavalleri MX4:539
  - "whoever looks after" appears in 25 easy outs across the set.
- **Round-3 rule "at most one compliance sentence; product, operations and technical-integration keep only the GDPR line":**
  - salvatoretipaldi MX2:526 uses a data-retention line as his value line, with no GDPR line.
  - aminelaadhari MX4:485 has the deletion sentence in Message 1 (card:152: compliance only in Message 2), plus the GDPR line in his Message 2 (:495).
- **Round-3 rule "Message 2 never repeats Message 1 and carries a value line":**
  - Repeats Message 1:
    - thomas-hervé RN:519
    - giuliamarinelli MX2:602 ("front photo and a side photo")
    - tomlionelfuller MX3:355 (3D view, already in :347)
    - elisa-stoosz MX4:39 ("the club chooses what to show" and "two photos", both already in :31)
  - No value line:
    - christine-fremond RN:239 (only "3D model included")
    - amandine-poirier DP:492 ("covers the capture and the 3D model")
- **Card:144 uniqueness** still fails at BODYHIT, the Dietplus Message 2s, CLP, Liva, Naturhouse, maju and NUTRIADAPT (table below).
- **Ownership question in Message 1:** barbara-vos MX3:151, "does a new client-facing tool like this ever reach your desk?" The card says the pointer belongs only in Message 2's easy out.

### B. Factual accuracy: 4/5

- **Speed phrase with the person as the subject, ×12 (MX4):**
  - Affected:
    - florence :17
    - yann :127
    - valerie-delage :169
    - robert :255
    - eliška :321
    - romana :341
    - mihalis :429
    - taylorling :515
    - vitor :557
    - vanda :599
    - matthias :685
    - qnko :231 ("Each capture is done")
  - "A client is done in under 45 seconds" turns the photos-to-results time into the person's total time.
  - proof-points allows one public definition, with no variants.
- **Doubled range:** sylvie-plichta BH:130 and ines-h BH:469, "Capture to output takes under 45 seconds from the photos to structured results".
- **The anonymised 34,000 proof is embellished again** (round 2 removed "all from phone photos"):
  - jacques-ley DP:59: "… on a two-photo capture. The same record could reach Dietplus clients …". This also implies the other platform's record reaches Dietplus.
  - jessica-bartlett MX3:320: "with a two-photo capture".
  - anna-dhervillers BH:377: "…, and a 3D model comes with each scan" sits in the same sentence as the 34,000.
- **An integration is stated as if it already exists:**
  - jc-heyneke MX2:297: "FitXpress plugs into BariBuddy through an SDK".
  - taylorling MX4:507: "white-label in the Fabulous app".
- **A display promise at a no-app account:** beatrice-mailly RN:579, "open a 3D model with the client on screen". Round 2 fixed this class at 5 RNPC people.
- **The repeatability sentence is not verbatim:** saemundur MX1:44 (above).
- **What holds:**
  - No client names, prices, medication, prospect figures, app mentions at no-app accounts, "5M+", "HIPAA" or certification claims.
  - Every 112,100, 100+, GDPR, medical-device and 38-210 kg sentence is cited correctly.
  - The data-deletion wording is accurate where it appears.

### C. Brand & tone: 2/3

- **Tricolons:**
  - patrick-gaytte RN:7
  - damien-rollin BH:258 ("a phone, two photos, 80+ body measurements")
  - nadia-battery MX4:95
  - ulrike-kaiser MX1:394 ("Nothing to ship, stock or install": lane text copied, flagged in r2)
  - robin MX2:133
  - victor MX2:339
  - wilconap MX2:326
  - hannahpearman MX3:393
- **Presumed reaction:**
  - susanne MX1:175
  - florence MX4:7 ("the side that decides how new services reach clubs")
  - tomcoenders MX3:7 ("a new tool must run the same")
  - fntneves MX3:773 ("a new module has to fit the stack")
  - josecarlosalves MX3:748 ("makes a simple conversation")
  - khalil MX4:181
  - jc-heyneke MX2:297
  - valeriadinatale MX2:183
  - shadi MX2:265
- **Dangling modifier:** nick-van-schijndel MX2:480 ("As Chief Product Officer at Virtuagym, the member-app roadmap is your area") and simonaurik MX2:537.
- **Idiom:** ericleddin MX1:125, "Fancy 15 minutes".
- **Awkward:**
  - christine RN:242: "whoever it is, I would take their name"
  - mattijs MX2:640: "A partner's own brand can sit on it"
- **hélène-bellod DP:327** opens on her receptionist and garage-secretary roles, which reads like a comment on her CV.
- **"Let me" ×4** (cristine DP:513, MX4:321, :409, :537). The detector accepts it. It is listed only for completeness.

### D. Format & structure: 2/3

- **jmhellendoorn:** Message 1 has a URL (template: Message 1 carries no link).
- **silviaojedavalenzuela MX2:433:** "My calendar is here:" is a bare link label with no call offer. Round 2 fixed this same defect at rebecca-becky-brown and simonaurik.
- **bc-katarina MX4:267/:275:** "Hi Bc. Katarina," puts an academic title into the greeting.
- **Stale `hook:`/`proof:` metadata:**
  - daphne DP:566 still cites "5M+ points per model".
  - "30-day deletion" is listed at justine-fendeler, miguel, fntneves, sigga and tobias, although no message text carries it.
  - Not sent, but the next writer or QC reads it as the cited proof.

### E. Output quality: 2/4

- **Good:**
  - RNPC now reads person by person.
  - The clinical-lane set is clean: jean-jacques, massimo, fumi, ellie, manuela, manel.
  - Reference-grade or close to it:
    - annemarie MX3:103
    - frédéric-julien MX3:416-420
    - corinne-brunet RN:71
    - gunnar MX1:538
    - fntneves MX3:773-775
    - scarlett MX1:421
- **Thin Message 2s.** About 60 Message 2 value lines are a bare proof number or one feature sentence. That meets the rule, not the template's purpose.
- **Mail-merge per company:**

| Company | People | Risk | Twins (one side to rewrite in the fixes below) |
|---|---|---|---|
| BODYHIT | 22 | **HIGH** | 11 career-path openers ("path / move / route … to BODYHIT"), 6 "member services" closers, 12 named pairs (BH fixes) |
| Dietplus | 27 | **MEDIUM-HIGH** (Message 2 openers regressed) | 15/27 Message 2s in 5 opener stems; 8 career-change openers; "Dietplus [town] follows … every week" ×3 |
| maju | 3 | **HIGH** | 3/3 people paired (opener, product sentence, speed-only Message 2) |
| NUTRIADAPT | 6 | MEDIUM | 5/6 Message 2s carry the speed phrase as the value line |
| Fabulous | 3 | MEDIUM | 3/3 Message 2s: "show the capture" + speed |
| Clinique La Prairie | 13 | MEDIUM | questions ×3, Message 2 opener "guest takes … from a link" ×3, "A guest could take a scan" ×3, 3D-view ×2, "scale" ×2 |
| Liva | 9 | MEDIUM | fumi/ellie on one skeleton; lise/lisa LV2 verbatim |
| Naturhouse | 8 | MEDIUM | 4 closers on the card skeleton; a question twin; a 3D-view twin |
| Het 1 op 1 Dieet | 8 | MEDIUM | OD1 restated as the opener in 6/8 |
| fitbox | 15 | MEDIUM | 6 pairs; "chooses to show" ×7 |
| RNPC, Ysonut, Vivafit, Keepcool, Virtuagym, FitForMe | | LOW-MEDIUM | isolated pairs |
| Sidekick, Nutrium | | LOW | none blocking |

## Line-level fixes per person_id

### Must-fix before sending (about 35 people)

1. **jmhellendoorn** MX2:402: remove the FAQ URL from Message 1. Message 2 (:410) keeps it.
2. **Card-example easy outs.** Each needs a different ask that names a role, not "whoever looks after X there":
   - damien-cacaret RN:62
   - thierry-bernabe RN:502
   - jan-sasse-0bb55a49 MX1:453
   - celiazouggagh MX2:246
   - fabrice-g MX2:678
   - clgabriel MX3:69
   - nandazwart MX3:184
   - sandrine-bagnols-naturhouse-96b54967 MX3:453
   - justine-fendeler-89925a182 MX3:593
   - cl%c3%a9ment-fav%c3%a9-169b7b178 MX4:83
   - patricia-cavalleri-35bb3466 MX4:539
3. **Compliance sentences:**
   - salvatoretipaldi MX2:526: replace the data line with a product value line. If a compliance sentence is wanted, use the GDPR line.
   - aminelaadhari MX4:485: drop "photos are deleted after processing or within 30 days" from Message 1.
4. **Message 2 repeats Message 1 or has no value line:**
   - thomas-hervé-7b6003213 RN:519
   - christine-fremond-67577a7a RN:239
   - amandine-poirier-423b16350 DP:492
   - giuliamarinelli MX2:602
   - tomlionelfuller MX3:355
   - elisa-stoosz MX4:39
5. **Speed phrase (mechanical).** Replace "A client/member/user is done in under 45 seconds…" with "It takes under 45 seconds from the photos to structured results." at:
   - florence-bernard-colombat-3845361b0 :17
   - yann-malaud :127
   - valerie-delage-1b9a0a145 :169
   - robert-buschbacher-23440b217 :255
   - eliška-čížková-56b490248 :321
   - romana-krčmářová-157704b7 :341
   - mihalis-atsalakis-86826521 :429
   - taylorling :515
   - vitor-costa-a0a645224 :557
   - vanda-lopes-a599a360 :599
   - matthias-vidal- :685
   - qnko-qnkov-423869260 :231

   Do the same for "Capture to output takes …" at sylvie-plichta-77069a164 BH:130 and ines-h-344686185 BH:469. Watch the new twins this creates: yann/valerie, vitor/vanda and eliška/romana share the sentence. Keep the speed line in only one of each pair.
6. **Proof embellishment:**
   - jacques-ley-8a5818148 DP:59: use the bare 34,000 sentence and drop "The same record could reach Dietplus clients".
   - jessica-bartlett-0a3076106 MX3:320: drop "with a two-photo capture".
   - anna-dhervillers-491a8628b BH:377: put the 3D model in its own sentence.
7. **saemundur-oddsson-md-148867115** MX1:44: use §1.2 verbatim: "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."
8. **silviaojedavalenzuela** MX2:433: add a call offer.
9. **jc-heyneke** MX2:297: change "plugs into" to "could plug into". Same tense fix at **taylorling** MX4:507.
10. **beatrice-mailly-358a82273** RN:579: drop "on screen".

### Twins: rewrite the second-named person in each pair

**RN**
- louisdenazelle :151 / **justine-desprez-372b3b266** :551: "You moved from X to directing an RNPC centre".
- céline-terpreau-4546ba102 :271 / **sandra-fontalba-5a22a5136** :431: "doctor's recommendation … the GP stays informed".
- laurent-dagieu-627022249 :471 / **beatrice-mailly-358a82273** :571: "two photos on their phone, and the dietitian receives 80+ body measurements". thierry :491 and thomas-hervé :511 use the same stem.
- paul-de-castries-2a823146 :179 / **gwénaëlle-queguiner-08996a136** :419: Message 2 = "show how a capture looks/works" + 34,000. nadège :319 and cécile :539 follow the same shape.
- nicolas-charpentier-87901546 :139 / **cécile-troisgros-8a8b16263** :539: "Fifteen minutes would (be enough to) show a live scan".
- nathalie-moreau-a029a231 :91 / **christine-fremond-67577a7a** :231: "Between [consultations/visits] at RNPC X, a client can …".
- patrick-gaytte-8b009b122 :7: tricolon.
- justine-desprez :559: "A dietitian can read the output quickly" is an ease claim with no source.

**DP (Message 2 openers first)**
- hélène-bellod-642366172 :337 / **angelique-rodrigues-b07a852a5** :471 / **johanna-yung-19b890330** :557: "Body composition estimates come from the same (two) photos" (gate flag).
- gaelle-aveline-330b867b :184 / **jeanne-guigui-963698150** :381: "The scan also returns …".
- katerina-abaeva-298212190 :404 / **valéry-leprevots-04a9ab35b** :534: "It also returns …".
- magali-le-gendre-8296b2120 :138 / **samya-mikou-8833a2140** :314 / **daphne-cierniak-100558425** :578: "The same capture / guided sequence … any phone".
- anne-rita-urzetta-terver-b32691b8 :205 / **cristine-baumert-040781353** :513 / **nathalie-dourdoigne-15b574173** :599: "The record is …".
- jeanne-guigui :373 / **daphne-cierniak** :570 / **jesahelle-lauverjat-ab8025162** :260: "Dietplus [town] follows (each) client(s) every week" (gate flag).
- benjaminhoresnyi :109 / **hélène-bellod** :331: "How does a first assessment run / first visit begin".
- natacha-alonso-valckx-35888b100 :17: "On the coach's side" implies a coach view at a no-app account. The speed phrase hangs off "compared at the weekly visit".
- Career-change openers ×8 (benjamin, magali, gaelle, katia, hélène, fabien, angelique, samya): move at least four to a DP1 or role hook. Rewrite hélène :327 first.
- daphne :566: clean the stale "5M+" from the metadata.

**BH**
- sylvie-plichta :130 / **ines-h** :469: identical Message 2 opener (also in the must-fix list).
- raphaëla-capelle-88a711196 :84 / **juline-boulanger-368487141** :492 / **jan-alan-96385423a** :312: Message 2 opens "3DLOOK has worked with 100+ clients" (gate flag).
- hassatou-diallo-92b459170 :446 / **corentin-bernard-47b65723b** :289: "A 3D model comes with every/each scan".
- corentin :289 / **antoine-cormier-266bb1433** :423: "a member picks (which) two (scans) to compare".
- anna-dhervillers :369 / **ines-h** :461: product sentence (gate flag).
- françois-xavier-quéré-82a0a517b :191 / **ines-h** :463: "members ask … most".
- fredericferet :9 / lila-sodano-139852256 :214 / **jan-alan** :306: "how a new service reaches / a club or member hears about something new".
- patricia-gouedard-411015132 :99 / **anna-dhervillers** :369: "… is why I am writing / is what made me write".
- julie-lacoste-5aa27584 :53 / **stéphanie-teixeira-44975716b** :168: both hooks are "sales administration".
- patricia-gouedard :99 / **julie-lacoste** :53: "turns … photos into 80+ body measurements".
- françois-xavier :189 / lila :212 / **quentin-fabre-08164b27b** :346: "for a (main) manager of a BODYHIT club".
- lila-sodano :226 / **damien-rollin** :272: "If … chosen elsewhere". damien-rollin :258 is also a tricolon.
- stéphanie-teixeira :176: move the accuracy line before the call offer.
- Career-path openers ×11: move at least five to BH1 or a question-led opener.

**MX1 (fitbox)**
- jan-sasse :453 / **sanja-kuche-80203822b** :576: "If [head office] …, a pointer to whoever looks after … is just as welcome/good".
- patrik-von-rochow-a5a303192 :528 / **rick-reinhard-37615b262** :722: "If it is for the central team".
- dennis-krebs-a30048235 :601 / **antonia-schulz-b1b86021b** :697: "owns the member journey".
- rolf-haberlah-1682a5ba :463 / **denise-neudeck-1252302ab** :611: "… stood out."
- ulrike-kaiser-75086b22b :396 / **rolf-haberlah** :467: "How do new services (usually) reach …".
- ulrike-kaiser :402 / **denise-neudeck** :621: identical speed sentence (gate flag).
- sanja-kuche :571 / **denise-neudeck** :621: "A [brief/quick] call … show (you) the scan".
- roland-wingert-wingert-ab6397350 :638 / **rick-reinhard** :711: "Which (progress) updates … members between sessions".
- ulrike-kaiser :394: lane-text tricolon.
- "chooses to show" ×7: keep at most two of ingo :369, rolf :465, jean-maurice-pohl-ab2806bb :498, gunnar-mau-06111972 :548, sanja :563, antonia :684, rick :717.
- FX1 restated ×4 (ingo :367, jan :442, jean-maurice :488, ilija-bozic-b7165532a :659): keep two.
- **Sidekick:**
  - susanne-burger-0a75032a :175: presumption.
  - ericleddin :125: "Fancy".
  - kevin-johnston-0708537 :327 / **todd-peavey-5a00703** :352: "white-label through API or SDKs" in Message 2 (minor).

**MX2**
- simonegibertoni :30 / **rebecca-chia-lung-chang-v-23bb2b394** :219 / **lorenzoamaglio** :72: the after-stay question.
- massimo-caprino-8bab5 :15 / arnaud-marche-923259123 :57 / **lorenzoamaglio** :78: Message 2 opens "The/A guest takes the scan/photos/it from a link…".
- lorenzoamaglio :70 / **rebecca-chia** :217 / **shadi-marie-le-maout-13488758** :257: "A guest could take a scan …".
- simonegibertoni :36 / **erick-ribeiro-919337183** :204: "the 3D model (would be) a view the clinic chooses to show".
- valeriadinatale :183 / **shadi-marie-le-maout** :265: the "scale evidence / scale in view" value line.
- olga-donica-19753744 :114 / **erick-ribeiro** :198: "What would … need to show/see before … new …".
- paulo-cudjo-26b060157 :558 / **bas-harmsen** :653: still twins from r2.
- bas-harmsen :659 / **fabrice-g** :678: "point me to whoever looks after that/it".
- silviaojedavalenzuela :431 / **hanna-blisnjuk-4b7748160** :450: "whoever looks after (the) BariBuddy (app)".
- victor-keunen :339 / **jmhellendoorn** :402: "… is your field."
- nick-van-schijndel :480 / **simonaurik** :537: dangling "As [title] …" opener.
- pbraam :469: replace the card-rule line with a real value line.
- robin-mauras-cartier-42555216 :133: list of three after a colon. victor-keunen :339 has the same pattern.

**MX3**
- sandrine :453 / **justine-fendeler** :593: identical closers (also in the must-fix list). cynthia-piraud-221506b3 :476 and nawel-tazdait-85750320a :522 sit on the same skeleton: vary two of the four.
- joffrey-pelachale-21aa68263 :535 / **justine-fendeler** :583: "have at/in hand … weekly visit/consultation".
- fr%c3%a9d%c3%a9ric-julien-190b9932 :426 / **cynthia-piraud** :472: "the centre chooses (whether) to show (it)".
- fumi-f-29a048153 :220-222 / **ellie-heath-6704b422** :370: same opener fact and same product sentence for two clinical people at Liva.
- lise-svendsen-tune-56436a73 :270 / **lisa-bolting-6296379** :295: LV2 verbatim (gate flag).
- tomcoenders :7 / **annemarie-kuiper-8bb33b56** :103: "At Het 1 op 1 Dieet each client has/works with a personal consultant".
- barbara-vos-0a7159109 :149 / **nandazwart** :172: OD1 restated as the opener.
- barbara-vos :151: replace the "reach your desk" ownership question.
- diogoalves92 :633 / **manuela-abreu1** :679: what a dietitian has or needs before / in an appointment (minor).

**MX4**
- julien-jané :657 / **matthias-vidal-** :677: "maju app … designed with dietitians".
- julien-jané :657 / **ludo-glav-9a14582a** :697: "add a body record/view to the maju app … SDK".
- maju Message 2s 3/3 speed (:665, :685, :705): keep it in one.
- marc-sarazin-6599b149 :141 / **qnko-qnkov-423869260** :223: "a (guided) web page could/can ask a client for two photos and return 80+ body measurements".
- florence-bernard-colombat :11 / **nadia-battery-497153a0** :97: new services reaching clubs / coaches.
- patricia-cavalleri :539 / **renato-monteiro-8b638621** :581: "point me to whoever looks after/runs member experience".
- NUTRIADAPT Message 2 speed-only (martanoskova :299, eliška :321, romana :341, natálie-černá-aa961a146 :385, daniel-hůlka-5068921a5 :407): keep two.
- Fabulous Message 2s (samibh :473, aminelaadhari :493, taylorling :515): keep the speed line in one, and vary the "show the capture" openers.
- bc-katarina-grich-ba159944 :267/:275: greet her as "Hi Katarina,".
- nadia-battery :95: tricolon.

## Top 3 issues (priority for improver)

1. **The round-3 easy-out rule was ignored, and Message 1 got a link.**
   - 11 easy outs reuse the card's example sentence. sandrine's is verbatim, and sandrine and justine-fendeler are identical.
   - jmhellendoorn's Message 1 contains the FAQ URL.
   - Neither is caught by any gate.
2. **Rule breaches introduced by the fixes themselves:**
   - The compliance sentence at salvatoretipaldi (data line in `product`) and aminelaadhari (data line in Message 1).
   - 6 Message 2s that repeat Message 1 or carry no value.
   - The speed phrase with the person as the subject ("A client is done in under 45 seconds …") ×12, plus "Capture to output takes … to structured results" ×2.
   - The 34,000 line embellished again ×3.
   - saemundur's §1.2 sentence paraphrased.
3. **Mail-merge remains:**
   - BODYHIT: about 16/22 people in pairs, 11 career-path openers.
   - Dietplus Message 2s regressed: 15/27 in 5 opener stems.
   - maju 3/3; Fabulous and NUTRIADAPT Message 2s are speed-only.
   - CLP has three twin families; fumi and ellie at Liva are one skeleton.

**System notes (not the agent's fault):**
- **Gate:**
  - `check-messages` tests Message 1 only for the calendar link (`outbound_pack.py`:1739). Make any `https?://` in Message 1 a hard failure.
  - Add hard checks for:
    - the card's easy-out sentence ("if this sits with head office" + "whoever looks after … there")
    - "output" in the speed-doubling check
    - "is done in under 45 seconds"
    - a deletion/retention sentence in Message 1
- **Card:**
  - card:78 still hands writers the full easy-out sentence. Round 3's rule cannot work while the card shows it as the example. Name the target only.
  - card:151 "The 3D model is a view the club or clinic chooses to show" is being copied as copy (24 messages). Mark it as a writer note.
- **The r2 report put salvatoretipaldi in the technical lane by mistake** (the profile says `product`). The writer's fix for that wrong premise produced this round's data-line breach.
- **The coordinator's round-3 mechanical checks** (speed + "result(s)", "most", "let") all pass. They test the wording of the fixes, not the rules behind them. The defects in Top 3 sit outside those regexes.
- **notify.py was not run** (no shell tool in this session). Text for the coordinator to send:
  `QC: message-sequencer → 13/20 (marginal), round 3 (r2 12/20) | Top issue: 11 easy outs reuse the card example sentence + FAQ link in jmhellendoorn M1; BODYHIT/Dietplus-M2/maju still templated | File: workspace/_quality/outbound/2026-10-07-message-sequencer-eu-weight-loss-nutrition-r3.md`

## Coordinator review

```yaml
coordinator_review:
  agreement: agree
  top_issue: "Each fix round introduces new card-instruction leaks: the easy-out example sentence (card:78) and the 3D-model rule (card:151) are written as sentences, so writers copy them; the speed phrase gets re-wrapped ('is done in under', 'capture to output takes') whenever a writer is told to make it verbatim."
  notes:
    - "Coordinator's r3 mechanical check missed 'output' doublings, 'is done in under 45 seconds', the FAQ URL in M1 and the easy-out example sentence; the checker now covers them for round 4."
    - "Round 4 = the 'Must-fix' and 'Twins' lists only, by person_id, then a coordinator mechanical check, no fourth opus QC (each QC round ~300K tokens)."
    - "Gate/card proposals (URL in M1 hard fail, easy-out example check, speed variants, deletion line in M1; card:78 and card:151 as writer notes) go to Vadim, not applied here."
```
