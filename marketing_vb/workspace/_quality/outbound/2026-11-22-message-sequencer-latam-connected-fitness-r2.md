---
qc_date: 2026-11-22
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/messages/_all-pairs.md
track: outbound
artifact_type: messages
round: 2 (after fix round 1; round 1 = 12/20)
total_score: 15/20
status: good
coordinator_review: pending
---

# QC Report: message-sequencer, round 2, 2026-11-22

**Artifact:** `messages/_all-pairs.md` (189 pairs, 20 companies, profile katya), read in full (4,970 lines). `messages/_check.json`: 0 hard. Its soft list only covers repeats inside one company, so the cross-company check below was done by hand.
**Total: 15/20, good (was 12/20).** Verdict: sendable after about 16 line edits plus 3 mechanical sweeps. Another writer round is not needed.

Allowed repeats were not counted: the boundary line, the §1.2 repeatability sentence (both card forms), the data-handling sentences, the SDK/API description, the 100+ clients line, the product core, and any repeat inside one company. "Strict" below means the same sentence word for word at two companies. "Near" means 1-3 words differ, or only the company name is swapped.

## Scores

| # | Category | Score | Max | R1 |
|---|----------|-------|-----|----|
| A | Adherence | 4 | 5 | 3 |
| B | Factual accuracy | 4 | 5 | 3 |
| C | Brand & tone | 2 | 3 | 2 |
| D | Format & structure | 2 | 3 | 2 |
| E | Output quality | 3 | 4 | 2 |

## What was wrong (specific)

### A. Adherence: 4/5
- Every round-1 rule target is met. Every M1 (189/189) has a pain line. There are 0 writer notes, 0 «the chain», 0 «A plan block can end…», 0 easy outs to buyers and 0 broken boundary lines. Every pilot names all its parts.
- **Speed wording is not its own sentence in 22 pairs.** The card says "as its own plain sentence". The typical form is «The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.» Round 1 named only 6 such pairs. Five were fixed; Bárbara's is still there, and the other 21 were never named. Ids are in §3.
- **Cross-company rule (fix rule 4):** strict repeats of M1 questions dropped from 27 pairs to 0. Elsewhere, 4 strict groups (8 pairs) remain, and the rewrites settled into new stock phrases per batch (§2).
- Card question targets are still pasted almost word for word: priscila-aguiar «At what point in a member's first months does the app ask for a check-in?»; beatriz-manganaro-luciano «Where in a member's first months does the app ask for a first check-in?»; daniel-martins-tognini and luissalvadori «What does the app show members about body change between assessments?». Most of the near-identical cross-company questions in §2 come from the same card targets.
- Pre-existing, missed by round 1: 21 M1s open with a line about the person and carry no company line from Account facts (card M1 part 1). That is 10 at Allp Fit, 8 at Bodytech Company, and weldon-neto, matheus-gonzaga and doménica-castagnetto. The gate accepts them because they name the company. Your call.

### B. Factual accuracy: 4/5
- All numbers are from the card list. No client names, accuracy figures or countries. Repeatability appears only in M2 (16 times, both card forms). «No integration fee» appears only in M2, and 2-4 weeks only in the technical lane.
- **Name form:** all 6 Next Fit M1s spell the brand «Nextfit» (9 times). The card says: "Name forms for Message 1: Next Fit (the brand; the row is spelled Nextfit)". This was already there in round 1, which missed it.
- **Facts not in Account facts (5):**
  - carolina-corona «At Grupo Smart Fit, studio progress is often counted as sessions attended, with no body measurement beside it.»
  - danila-de-marchi «A plan in the SportClub app has no body measurement beside it…». Training plans live in a separate vendor app; the SportClub app listing has no workouts.
  - gerardo-diaz «SportClub plans run month to month…»
  - esteban-lozada «Today a body check needs a visit to the club.» and felipe-pavas «…while a body check still needs a visit to the club.» Action Black is plan branch, and no assessment was found.
- **Partly fixed:** guido-giambruni M1 «a check-in that needs no club visit or trainer slot» still implies an in-club measurement at BIGG (plan branch).
- **Card conflict, needs your ruling:** 10 SportClub M1s say plans carry no body measurement, but the card's own Training SportClub entry lists body-composition tracking. The writers followed the card's plan-branch targets.
- Sourcing: does not apply to outbound. Only 3DLOOK links (page and calendar) are used, as the card requires.

### C. Brand & tone: 2/3
- 0 banned words, dashes, «plus», «so», corrective negation and label lead-ins (round 1: about 95). 0 openers that read as if Kateryna works there (round 1: 13). No Portuguese words, no British spelling.
- **Rule 7 created a robotic double in 10 of 12 Bluefit M1s**, e.g. «Bluefit members compare their in-club assessments in the app Bluefit members use». This is the same defect round 1 flagged as «Members use the app members use», and talita still has it.
- Verbless or colon openers: thalita «Quick idea for the platform side of the Smart Fit App.», jefferson «One observation for someone who runs operations across Smart Fit clubs in Rio.», marco-storchi «Quick thought for Megatlon's operations: …», stefanoviudes «Caught my eye: …». Fragments: viviane «For club teams, nothing to install.», marco-storchi «Nothing to ship or install.»
- Garbled: brunoamaralsilva «Billing for Smart Fit plans meets the app wherever a plan adds a feature.» Odd body phrasing: robertarosario «How much of a new member's body does the app capture during joining today?»
- «glad … glad» back to back: jorge-villa-aguilar and oscar-maldonado, «I am glad to be pointed to … I would be glad to go through it on a call.»

### D. Format & structure: 2/3
- The gate passes. In all 189 pairs the link sits alone after a full sentence, and the calendar line comes last.
- Layout still differs by batch. mixed-1 and mixed-4 put the easy out and the call on one line. mixed-5 puts them on consecutive lines with no blank line, and in 5 pairs glues the page line onto the boundary paragraph. This is cosmetic.
- Per-person files have no `product:` frontmatter. Not capped, same as round 1.

### E. Output quality: 3/4
- About 165 pairs can go as they are. Strong ones: alessandra-mattos-sekeff (manifesto), eduardoliedbraun (sensors), luizurquiza (brand concept now in English), tadeu (Frequência Premiada), felipe-pavas (consents in the app), gigliola and jorge-villa (November App Bodytech update), maganhotte and josé-eduardo (registration step, Tecnofit Partners).
- What is left is about 30 minutes of editing including the sweeps. Across companies the campaign now reads templated because of the new stock forms (§2), but no single recipient sees that.

## 1. Round-1 issues: fixed vs remaining

| Round-1 issue | R1 count | Now | Left (person_ids) |
|---|---|---|---|
| M1 without a method pain line | 32 | 0 missing | 4 weak: the pain is just "no measurement from the member's own phone" (diego-palacio, german-ariel-garcia-pf, amanda-ferrari, natasha-valencia) |
| Strict cross-company M1 questions | 8 groups / 27 pairs | 0 | none strict; near groups in §2 |
| Cross-company closers and page lines (mixed-2 and others) | 35+ pairs | 1 strict closer | andersonfranconeves / dudunetto |
| Writer notes / meta | 5 | 0 | – |
| «the chain» / «A plan block…» / pasted card targets | 10 / 10 / ~60 | 0 / 0 / 6 close copies | priscila-aguiar, beatriz-manganaro-luciano, daniel-martins-tognini, luissalvadori, xioma, bruramalho |
| Easy outs to buyers | 5 | 0 | ruling needed: cesar-casallas (founder) and fernando-storchi (founder & CEO) are referral lane by Vadim's WEAK pick and keep an easy out |
| Pilot incomplete | 8 | 0 | minor: doménica-castagnetto (no first check-in scan), igor-souza (criteria not said to be set before the start) |
| Boundary line form | 8 | 0 | – |
| Another company's fact («registers») | 3 | 0 | – |
| Card pain target stated as company fact | 12 | 0 | (new, different slips listed under B) |
| App names / «the club's app» / «chain's own app» | 8 | 0 | – |
| Product claims beyond the card | 8 | 0 | – |
| Label lead-ins before links | ~95 | 0 | – |
| Openers that read as Kateryna working there | 13 | 0 | – |
| «point me to X: <link>» | 13 | 0 | – |
| Portuguese words / British spelling | 2 / 2 | 0 / 0 | – |
| Speed wording not its own sentence | 6 named | 1 named left | b%c3%a1rbara-valente-01898386 (plus 21 never named, §3) |
| Robotic «app members use» | 1 named | still there, and spread | talita-araujo plus 9 more Bluefit (§2) |
| BIGG in-club visit implied | 1 named | partly fixed | guido-giambruni |

Of about 150 named lines, all but 3 are fixed (bárbara-valente, talita-araujo, guido-giambruni).

## 2. New defects introduced by the round

**Strict repeats across companies (4 groups, 8 pairs):**
- «I would be glad to show it on a call.»: andersonfranconeves (Allp Fit) / dudunetto (Bodytech Company)
- «FitXpress needs no hardware to ship or install.»: patr%c3%adcia-rocha-772971210 (Bluefit) / guido-giambruni-295a2a1a2 (BIGG)
- «Nothing ships to the clubs.»: leandro-ascen%c3%a7%c3%a3o-4b773b117 (Smart Fit) / felipe-pavas-7b69692bb (Action Black)
- «A pilot could run in one club.»: max-trombini-600b14a (Cia Athletica) / priscila-aguiar-33695076 (Gaviões)

**Stock easy-out phrases, one per batch, repeated across companies.** The fix rule produced these:
- mixed-4: «…, I am glad to be pointed to them / its owner / the … lead.» 17 pairs at all 6 companies. Near-identical pairs: samuel-h-cruz / jorge-villa-aguilar («If the member app sits with another team (at head office), I am glad to be pointed to its owner.»); leandro-aguiar / carla-trigueiro (national training vs technical lead).
- mixed-5: «…, I would value a pointer to that person / the right person.» 7 pairs at Selfit, Fitco, Sport City and Megatlon. Near-identical pairs: weldon-neto / fernando-storchi; diego-brayner / gabriel-ramos.
- mixed-3: «…, a pointer (to them) would help.» 12 pairs at Panobianco, BIGG and Spinning Center, the same form as about 16 at Smart Fit. Near-identical pairs: vilma-brasileiro / martin-bottini; thyago-alves-carneiro / SportClub adrian-anaya and pablo-fedelich (only «help» vs «be enough» differs).
- «…, a name would help.»: cesar-casallas (Spinning Center) / viviane-roque (Cia Athletica).

**Wording from the fix rules turned into copy:**
- Rule 10 wording, «Criteria are set before the start, and the scan opens to more members only if they are met.», appears in 6 Smart Fit pairs. In 6 Allp Fit pairs it differs only by a leading «The». «We (would) count scan completion, retakes, onboarding completion, and day-30 and day-90 retention.» is shared the same way: Smart Fit ×3, Allp Fit ×4.
- Rule 7 wording led to the 10 Bluefit doubles «Bluefit members … in the app Bluefit members use». It also led to «A call would show how it fits the app Panobianco members use.» ×10 (one company, so allowed, but heavy).

**New stock closer family: «I would be glad to … on a call.»** 42 pairs at 8 companies. Beyond the strict repeat above, one pair is near-identical: phillippoliveira and luissalvadori «…talk through the pilot…» / fernandoduartemenezes «…talk through a pilot…». Another: SportClub ×12 «A short call is the easiest way to go through the details.» / Selfit ×3 «…go through it.»

**Opener template «Your path … at X caught my eye.»** 7 pairs: robertarosario, stefanoviudes, weldon-neto, matheus-gonzaga, doménica-castagnetto, ggarciacardone, josé-antonio-suárez.

**Near-identical M1 questions across companies (mostly card targets with the name swapped):**
- moisés-alves-ramos (Pacto) / alexandre-leandro-manarim (Next Fit) / rafaelalaurencini (Tecnofit): «Which (member-app) features … do gyms ask X for most (often)?»
- vanessaugioni (Next Fit) / maganhotte (Tecnofit): «How does/would X try a new (partner) capability with a few gyms first?»
- rafael-panobianco / josé-antonio-suárez (Sport City) / cristián-deppe (Smart Fit): «How would/does the app team try a new feature with one/a small group of members first?»
- cesar-casallas / rafael-lucena: «What does your team (at CT - SP) see of a member's progress between assessments?»
- felipe-manoel (Cia) / felipe-marcon (Bluefit): «How do members at your unit ask about / raise body change between assessments?»
- camilo-sarasti (Smart Fit) / yfagundes (Next Fit): «Would 3D progress fit a higher (membership) plan…?»
- ricardoferamaral (Allp Fit) / fcastromit (Panobianco): «Which moment in a new member's first weeks would…?»
- fernandoduartemenezes (Selfit) / alessandra-mattos-sekeff (Bluefit): «Where/When in a (new) member's first months would a (first) body check-in fit best…?»

**Other near repeats:** «A pilot can/could start with one plan.» (camilo-sarasti / ggarciacardone); «This page describes/explains how fitness apps use it.» (Allp Fit / melina-de-souza-barbosa); the mixed-5 pilot frame «We would count scan completion and retakes, then compare onboarding completion…» (fernandoduartemenezes, mayoralexander, ggarciacardone).

**New fact slips and awkward lines:** see B and C (carolina-corona, danila, gerardo, esteban, felipe-pavas, brunoamaralsilva, robertarosario, jorge-villa / oscar-maldonado glad/glad).

## 3. Line-level fixes by batch

**MUST** = fix before sending. **REC** = recommended: near repeats and polish, your call under the "identical" rule. Sweeps can be done by script; check M2 stays ≤ 700 characters.

**Sweeps (all batches)**
- S1 MUST: «Nextfit» → «Next Fit» in the M1s of alexandre-leandro-manarim, douglas-waltricke-42579a152, kevin-marques-916400151, thais-ferreira-gomes, vanessaugioni-146b92188 and yfagundes (9 occurrences).
- S2 MUST: «in/through the app Bluefit members use» → «in the app they use» wherever the subject is already "Bluefit members": igor-souza-865563150, marcellepm, bruramalho, patr%c3%adcia-rocha-772971210, diego-tavares-b117183a, edson-santos-b26281209, felipe-marcon, higor-duarte-9a4a96430, nayanarosa, talita-araujo-0816b73a.
- S3 MUST if the card rule holds: «…, under 45 seconds from the photos to structured results.» → split it off as its own sentence, e.g. «… 80+ body measurements. Each scan takes under 45 seconds from the photos to structured results.» Ids: adriana-assun%c3%a7%c3%a3o-68a731b6, flavia-campos-de-souza-97587a30b, fernando-sebo-benitez-31693810, leandro-ascen%c3%a7%c3%a3o-4b773b117, marcela-gonçalves-meirelles-0a2694125, marcelo-schwed, thaypfx, b%c3%a1rbara-valente-01898386, tamiris-losso, guirocha79, guido-giambruni-295a2a1a2, xioma, marcela-palencia-rodríguez-5706a5288, viviane-roque, rodrigo-alaminos-a172481a7, yfagundes, jorge-villa-aguilar-0129521ab, felipe-pavas-7b69692bb, adriano-madureira-23710121, eduardoliedbraun, gabriel-ramos-24a16221a, marco-storchi-68112a15b.

**smart-fit-1**
- MUST `carolina-corona-4784b217` M1: «At Grupo Smart Fit, studio progress is often counted as sessions attended, with no body measurement beside it.» → not in Account facts; use the Smart Fit App and in-club exam fact.
- REC `leandro-ascen%c3%a7%c3%a3o-4b773b117` M2: «Nothing ships to the clubs.» → strict repeat with felipe-pavas; fixing it there instead is enough.
- REC `daniel-martins-tognini-432b02aa`, `luissalvadori` M1: «What does the app show members about body change between assessments?» → card target pasted; reword. `beatriz-manganaro-luciano` M1: «Where in a member's first months does the app ask for a first check-in?» → card target pasted.

**smart-fit-2**
- MUST `brunoamaralsilva` M1: «Billing for Smart Fit plans meets the app wherever a plan adds a feature.» → garbled; say plainly what billing touches when a plan adds an app feature.
- MUST `robertarosario` M1: «How much of a new member's body does the app capture during joining today?» → reads as body talk; ask what body data the app records at joining.
- REC `thalita-miranda-3a7a47137` «Quick idea for the platform side of the Smart Fit App.», `jefferson-cunha-173793127` «One observation for someone who runs operations…», `stefanoviudes` «Caught my eye: …» → verbless or colon openers.

**mixed-1 (Allp Fit, Bodytech Company)**
- MUST `dudunetto` (or `andersonfranconeves`) M2: «I would be glad to show it on a call.» → strict cross-company repeat; reword one.
- REC Allp Fit pilots `ricardoferamaral`, `cristianogfontes`, `douglas-cassimiro`, `gabriel-moura-c`, `guilherme-messias-68b34b353`, `jeanpcpierre`: «The criteria are set before the start, and the scan opens to more members only if they are met.» → Smart Fit's sentence plus «The»; give Allp Fit its own wording (one form is enough, since repeats inside one company are allowed).
- REC `melina-de-souza-barbosa` M2: «This page explains how fitness apps use it.» → near Allp Fit's «describes/shows»; vary.
- REC (coordinator) 18 M1s with no Account-facts line: bruno-ciolli, cristianogfontes, douglas-cassimiro, emerson-maida, fabianoveloso, gabriel-moura-c, guilherme-messias, guilherme-th%c3%a9, thaypfx, luana-luiza; bárbara-valente, elisangela-ornellas, marcelo-vianna, ricardo-fagundes, diogoevangelista, karina-borba-rocha, melina-de-souza-barbosa, tamiris-losso.

**mixed-2 (SportClub, Bluefit, Pacto)**
- MUST `danila-de-marchi-0433a0178` M1: «A plan in the SportClub app has no body measurement beside it…» → plans are not in the SportClub app; write «a training plan members follow…».
- MUST `gerardo-diaz-50b033152` M1: «SportClub plans run month to month» → not in Account facts; delete the clause.
- REC `matiashotano` M1: «the member app is where plans, access and benefits reach members» → plans sit in a separate app.
- REC `igor-souza-865563150` M2: «against agreed criteria» → add «set before the start».
- REC `felipe-marcon` M1 question → near felipe-manoel (Cia); vary. `moisés-alves-ramos-83b35995` M1 «Which member-app features do gyms ask Pacto for most often?» → name-swap of Next Fit's and Tecnofit's question; vary.
- COORDINATOR: 10 SportClub M1 pain lines vs Training SportClub's body-composition tracking (B).

**mixed-3 (Panobianco, BIGG, Spinning Center, Tecnofit)**
- MUST `guido-giambruni-295a2a1a2` M1: «FitXpress adds a check-in that needs no club visit or trainer slot» → BIGG publishes no in-club measurement; drop the visit/slot contrast. M2: «FitXpress needs no hardware to ship or install.» → strict repeat with Bluefit patricia-rocha; reword.
- REC `cesar-casallas-8178b07b` M2: «If the member app sits with another team at Spinning Center, a name would help.» → near viviane-roque; reword one. COORDINATOR: founder with an easy out in the referral lane.
- REC `vilma-brasileiro-694677439` or `martin-bottini-3a789014` M2 easy out → near-identical; vary one. `thyago-alves-carneiro-dos-santos-1b9436128` M2 → one word from SportClub; vary.
- REC M1 questions: `rafael-panobianco-466a721a8` (↔ josé, cristián), `cesar-casallas-8178b07b` (↔ rafael-lucena), `fcastromit` (↔ ricardoferamaral), `rafaelalaurencini` and `maganhotte` (name swaps with Next Fit and Pacto) → vary.

**mixed-4 (Cia Athletica, Gaviões, Next Fit, Bodytech Colombia, Action Black, Pratique)**
- MUST S1 (Next Fit spelling).
- MUST `esteban-lozada-3876a9b8` M1: «Today a body check needs a visit to the club.» → Action Black is plan branch; use a plan pain.
- MUST `felipe-pavas-7b69692bb` M1: «…while a body check still needs a visit to the club.» / «FitXpress removes that visit.» → same issue. M2: «Nothing ships to the clubs.» → strict repeat with Smart Fit; reword.
- MUST `priscila-aguiar-33695076` M1: «At what point in a member's first months does the app ask for a check-in?» → card target pasted; own words. M2: «A pilot could run in one club.» → strict repeat with max-trombini; reword one.
- MUST `jorge-villa-aguilar-0129521ab`, `oscar-maldonado-90796aa` M2: «I am glad to be pointed to … I would be glad to go through it on a call.» → glad/glad; change one verb.
- REC «…, I am glad to be pointed to …» in 17 pairs at 6 companies → one wording per company.
- REC `natasha-valencia-11562a1a2` M1: «a body check from the member's own phone would add a measurement to it» → the pain is just the product's absence; name the method's limit. `yfagundes` M1: «a gym with a higher plan has little body data to build it on» → awkward. `viviane-roque` M2: «For club teams, nothing to install.» → fragment.
- REC questions: `vanessaugioni-146b92188` (↔ maganhotte), `alexandre-leandro-manarim` (↔ moisés), `yfagundes` (↔ camilo), `felipe-manoel-88a23634` (↔ felipe-marcon).

**mixed-5 (Selfit, Fitco, Sport City, Megatlon)**
- REC «…, I would value a pointer to that person.» (weldon-neto, diego-brayner, matheus-gonzaga, andrea-ruiz, gabriel-ramos, axel-mendoza, fernando-storchi) → stock across 4 companies; vary per company. COORDINATOR: fernando-storchi is founder & CEO with an easy out (referral lane).
- REC `fernandoduartemenezes` M2: «I would be glad to talk through a pilot on a call.» → near Smart Fit; vary. M1 question → near alessandra (Bluefit).
- REC Selfit `eduardoliedbraun`, `diego-brayner-b7976167`, `matheus-gonzaga-aa094420`: «A short call is the easiest way to go through it.» → near SportClub's ×12; vary.
- REC `ggarciacardone` M2: «A pilot could start with one plan.» → near camilo. The pilot frame «We would count scan completion and retakes, then compare…» is shared by fernandoduartemenezes, mayoralexander and ggarciacardone; vary.
- REC «…caught my eye.» openers (weldon-neto, matheus-gonzaga, dom%c3%a9nica-castagnetto, ggarciacardone, jos%c3%a9-antonio-su%c3%a1rez-l%c3%b3pez-38b2282ab). weldon, matheus and doménica also lack an Account-facts line.
- REC `dom%c3%a9nica-castagnetto` M2 pilot: add the scan at the first check-in. `marco-storchi-68112a15b` M1: «Quick thought for Megatlon's operations:» (colon opener), «with no device and no club visit» (Megatlon publishes no assessment); M2: «Nothing to ship or install.» (fragment).
- Cosmetic: add a blank line between the easy out and the call line; move the page line off the boundary paragraph.

## 4. Verdict

**Sendable after about 16 line edits plus 3 sweeps.**
- The 16 MUST lines: carolina-corona, brunoamaralsilva, robertarosario, dudunetto/andersonfranconeves, danila, gerardo, guido ×2, esteban, felipe-pavas ×2, priscila ×2, jorge-villa, oscar-maldonado, and one of leandro/felipe-pavas.
- The sweeps: S1 Next Fit spelling and S2 Bluefit double are required; S3 speed sentence is required if you hold the card rule.
- The near-identical stock phrases (REC, about 30 lines) are not strict defects under Vadim's rule. Vary at least the mixed-4 «glad to be pointed» (17 pairs) and the mixed-5 «value a pointer» (7) if you want each company to read on its own.
- A third writer round is not recommended. This round showed that batch-wide rules turn into new batch-wide stock phrases. Edit these lines directly instead.

## Top 3 issues (priority for improver)

1. **Fix rules become copy.** Rule 7 produced «the app Bluefit members use» ×10. Rule 10 produced «Criteria are set before the start…» ×12 at two companies. The easy-out rule produced one stock phrase per batch («glad to be pointed», «value a pointer», «a pointer would help»). Fix rules should give a target, never a sentence, and the gate should flag near-identical sentences (name swapped or ≤ 3 words different) across companies, not only strict ones.
2. **Card checks no gate runs:** speed wording as its own sentence (22 misses), the Message 1 name form (Next Fit ×6), and the company line from Account facts (21 M1s open with a person line).
3. **Facts outside Account facts in pain lines:** an in-club body check at Action Black, a plan in the SportClub app, "month to month", Smart Fit studio claims. Also the card's own SportClub conflict between plan-branch targets and the training app's body-composition tracking.

## Notes for coordinator
- Gate gaps: there is no cross-company check for near-identical sentences; no check that speed wording stands alone; no check of the M1 name form against Account facts (Nextfit vs Next Fit).
- Card inconsistency: the Rules line allows only the page sentence for repeatability («Repeated scans typically differ…»), while the §1.2 block prefers «For most evaluated measurements…». Both appear in the copy (stefanoviudes, ruben-baquero, weldon-neto use the second). Neither is wrong, but the card should pick one.
- Easy outs in the referral lane for founders: cesar-casallas (Spinning Center founder) and fernando-storchi (Megatlon founder & CEO). Rule 6 and the lane disagree.
- notify.py not run: this QC session has no shell tool.

## Coordinator review

agreement: ✅ agree
top_issue: round rules became batch stock phrases (easy outs, criteria sentence, Bluefit "app Bluefit members use"); coordinator line pass applied all 16 MUST + sweeps S1-S3 + per-company easy-out wording in mixed-4/mixed-5, SportClub pain lines rewritten to the method level (Training SportClub has body-composition tracking, so "no body measurement" was false), Next Fit alias added to companies.csv for the gate; gate 0 hard; non-mandated cross-company twins 4 (all product-description fragments).
