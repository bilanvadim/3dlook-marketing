---
qc_date: 2026-10-12
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-11-au-sport-fitness/messages/ (second QC, after the 2026-10-12 fix round; read in full: all 12 _batch-*.md, _check.json, _coordinator-scan-2026-10-12.txt, all 12 _summary-*.md, card-messages.md incl. "Coordinator decisions 2026-10-12" rules 1-19 and the technical lane data note; fix lists sampled: _fix-jetts-fitness, _fix2-fernwood-fitness-1)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
previous_qc: workspace/_quality/outbound/2026-10-11-message-sequencer-au-sport-fitness.md (10/20)
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-12, au-sport-fitness (second QC)

**Artifact:** `workspace/outbound/campaigns/2026-10-11-au-sport-fitness/messages/` (325 people, 650 messages, 12 batches)
**Total: 13/20, marginal** (was 10/20).

**Verdict.** The fix round closed nearly every finding QC1 named by person. Almost every M2 now has a value line, and no unit owner is asked to judge fit. There is no call length, no "pitch", no presumed reaction, no "so" benefit and no "ran 112,100". The data line is correct in all 7 technical M2s and appears nowhere else. Lanes, Viva, pool C and alias rules hold. But several defects were swapped rather than removed, which is the pattern the brief warned about:
- **The M2 skeletons came back in new words.**
  - Jetts: all 27 referral M2s run value line, then "A call [can/could/would] show [the member side / what a member sees]" (17), then "[target] may be the better contact/person/audience, and a name would be welcome" (17), then a day closer (11).
  - Fernwood: 28 of 36 closers are a yes/no "[Would/Is/Could] a call be useful/worthwhile?", with word-level twins. About 17 M2s also bolt on a capture sentence ("her phone guides each one").
  - Genesis/KX/REVL: the grid gave each person a closer form, but each form got a single sentence, so the same closer repeats.
  - BFT says "the member side" ×9 and "A plain yes" ×4. Writers turned the card's own words (rule 2 "members' side", rule 4 "a plain yes or no") into copy.
- **Label lead-ins replaced "ran".** 25 M2s put a label in front of the 112,100 line ("For scale:", "On volume:", "Scale, for context:", "The scale so far:"), and 2 do the same before the 100+ line. Round 3 removed labelled 100+ lines at Fernwood and mixed-1 only.
- **Speed phrase.** The banned pairing "80+ body measurements, under 45 seconds..." survives in 7 messages. Its replacement became a new stock sentence ("Taken on any phone, the scan returns body composition estimates, under 45 seconds...") in 6.
- **The card-note leak spread.** zaac-schembri's "shown only where Virgin Active chooses" is gone. But "shown only where the brand/club/studio chooses" or "X decides where it appears" now runs in about 30 messages outside the workplace programmes (where the card requires it).
  - Word for word at Anytime (×4) and at STRONG Pilates (×2).
  - Said to unit owners, it reads as if the club runs the scan.
- **Missed by QC1, still open.** Central questions repeat within BFT, Jetts and Fernwood, and several copy the topic-bank target line word for word. About 20 product-lane M1s end on the card's own question ("At which point in a member's year would a scan fit best, joining or a goal review?").

**Recommendation.** Do not regenerate. Run one more sentence-level round from the fix list below:
- Jetts, Fernwood and mixed-2: the M2 second paragraphs and closers.
- Every batch: strip the label lead-ins and the speed pairings.

First add these checks to the scan, or the next round will swap again (today's scan reported one hit for all 325):
- closer shape with the target noun removed;
- a label before a fixed proof line;
- "As [role]" whatever the subject;
- the speed phrase right after any output noun;
- similarity of central questions within one company;
- "shown only where … chooses".

**Scoring basis.** Scored against card-messages.md ("Coordinator decisions 2026-10-12" win) and the _profiles files.
- Taken from the gate as fact: limits, signature, bans, detector, completeness. Two "plus" connectors slipped past it and are listed below.
- Coordinator withdrawals honoured: two photos + 80+ in M1 is not counted, call length is "none", and the identity/role items stay with Vadim.
- The split files have no `product:` field. That is the script template, so it is not capped (same ruling as QC1).
- notify.py was not run: this QC run had no shell tool.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## QC1 findings: status by person_id

**Fixed**
- **Fit-judging or rollout wording:**
  - Jetts: aaron-dearie, sarah-dwyer, jetts-gym-mount-hutton, sam-bhandari, mel-george, catherine-hanly.
  - Other brands: jason-clark, jamie-ward-smith, gym-genesis, brentonwilliamson, rachel-macedo, benny-russell, marvin-mangubat.
  - Fernwood: jessica-pupillo, steve-brookes, jessie-anderson, tedy-ferreira, guneet-cheema, melissa-jones.
- **Themes and openers:**
  - Fitstop theme 7/32 → 3.
  - Openers bruce-mcconnel/brenna-dillon and chris-janke/josephine-tuah.
  - BFT BF4 sentence (kirsten-lea, zoe-clark, luan-scherman, st-leonards).
  - Fernwood "Noticed your background" (binish, mary, cheryl) and "Quick note" (ric, suzanne, moby).
- **Identity, lane and angle:**
  - mark-grey (CEO title and the "for most" claim), gh-undefined (Viva).
  - Hindmarsh pair scott-bumpstead/steve-grace now asks different things.
  - damien-mavroudis angle, arshad-hussein now names Plus Fitness Rockdale, seanmolam lane.
  - Before-and-after removed (melissa-robinson, michelle-baker, moby-malik, alex-fenton-mathews); stacey-flentje step-up removed.
- **B (claims and data):**
  - Claims removed: hayden-lambley-robinson, liana-nio, matknipe, katelyn-farmer, paul-brown, garry-mortlock, chris-caldwell.
  - "ran 112,100" removed: andrewbaildon, peter-reed, rebeccacarson2, sean-hodges, sarahbroadhottot, jeremy-saville.
  - Data line now has both halves: joe-w, clint-sellen, angelo-konstantinou, davidnedved, ccarpinteri, ben-lister, brettcondron. seanmolam and robmitchelllinkedin carry none; darrellnewing links the FAQ only.
  - No deletion line in any M1. adriana-ampuero cleaned.
  - Prospect-adjacent and deficit wording removed: simonjelliott "also", jaynevaiao, jay-williams/david-upton churn, christy-vu/arshad "drift", kirsten-lea "by eye", jonpepper site differences.
- **C:**
  - All 11 "so" benefits, 5 corrective negations and about 30 presumed-reaction openers.
  - The 10 dangling "as [role]" openers.
  - The 3 card notes (barry-mcdonald, zaac-schembri, michaeljordanubx).
- **D:** _summary-fernwood-fitness-2 now exists; dr-toby-ford, leah-libunao and brendon-levenson fixed.
- **E:**
  - A value line in almost every M2.
  - 100+ line now Fernwood 2, REVL 1, KX 1.
  - No call length anywhere.

**Not fixed, or fixed in form only**
- **BFT and Jetts M2 skeleton:** easy-out targets now vary and "you tell me if it fits" is gone, but each brand's M2 still reads as one template (see A and E).
- **melissa-mcglinn-8a264249 / tedy-ferreira:** "You run both" became "[Club] and [Club] are both yours" for the same pair.
- **"ran 112,100":** replaced by a label lead-in at peter-reed, rebeccacarson2, sean-hodges, sarahbroadhottot and jeremy-saville.
- **zaac card note:** gone for zaac, but the same phrase runs in about 30 other messages (see C).
- **Value line still missing or generic:** jonah-hales, timwest4, lisa-gratrix, jetts-gym-mount-hutton, katelyn-farmer, rachel-dillon, scott-freeman.

## What was wrong (specific)

### A. Adherence: 3/5
- **Rule 4, closer form and shape per company.** Twins:
  - Fernwood: jodie-sorensen/michelle-baker/ben-cook/susan-oliver-am ("…a call be useful?"); angela-williams/melissa-burn/fernwood-fitness-ballarat ("…worthwhile?"); emma-tilley/lydia-tanios ("Open to a (quick) call?"); suzanne-herniman/hayley-richey ("Could we have a (short) call").
  - Jetts: 11 "name a day" closers.
  - Genesis: gym-genesis/cameron-reid/mitchell-bird ("send two times"); brentonwilliamson/tom-bayford ("yes or no").
  - KX: james-trenerry/sophie-patient/divya-hegde ("yes or no … is enough"); bruno-gallucci/kelly-strybosch ("tell me a day … I will work/plan around it").
  - REVL: benseymour10/mark-jackson; jake-harris/adam-coombes.
  - Viva: shane-johnson/kane-schrader/gh-undefined ("A yes or no is enough").
  - Vision: daniel-collins/marvin-mangubat; victor-ramirez/rachel-macedo/jack-smith (named weekdays).
  - BFT: liana-nio/steve-grace/anthonyhoangbft/zoe-clark ("A plain yes").
  - Fitstop: bentoleafoa/nebojsa-vujic/brenna-dillon ("a call is easy to …"); josephine-tuah/mark-vaiao ("would show/cover the rest").
  - Anytime: marcello-jimenez/steve-hobart ("I would value a short call …, or a pointer"); jordan-smith/winona-dufrier ("I would be glad to …, or to be pointed").
- **Rule 3, easy-out wording:**
  - Jetts: "may be the better contact …, and a name would be welcome" ×17.
  - UBX: taylor-papangelou/cassie-maynard ("Whoever owns the (UBX Member) app at head office is the right person").
  - Fernwood: "leads FIIT30 programming" (melissa-robinson, souad-sakoua, mary-papazoglou).
  - Fitstop: adam-stevens/jamie-biondi ("I would follow your pointer"), kevin-kensley/milan-sekulic ("take it from here"), jonpepper/paul-emanuel ("tell me who and I will go"). The member-app target serves 8 of 32 (over a fifth).
  - Same-club pair with the same ask: lee-squire-a499641a and fernwood-fitness-ballarat-60a208251 (Fernwood Ballarat) both point to member experience at head office, in the same shape.
- **Rule 10, openers:**
  - UBX: "Noticed" 5/18; jonah-hales/davidnedved share "Noticed your background".
  - Anytime: richard-peil/clancy-izzard ("Noticed your background").
  - Fernwood: clow-john/hayley-richey ("Quick one on").
  - VAURA lilly-mills/brooke-young and Planet Fitness danielle-monroy/david-bennet (both "Noticed").
  - World Gym: jon-davie/michael-nysten ("(One) question for World Gym Australia").
- **Rule 11, "As [role],":** jeanette-loughlan, paul-divin, martin-oliver (Jetts); kyliekerr, suyesh-bajracharya (mixed-4). None is dangling, but the rule is absolute and the scan missed all five.
- **Rule 19:** scanlan-karen M1 never names Jetts (the summary admits it).
- **Central question shared at one company** (card "Several people at one company"; missed by QC1, untouched by the fix round):
  - BFT: sarina-sham/laura-carroll/matt-jones (sarina's is the topic-bank line verbatim); philip-grasso/adem-bek/anthonyhoangbft; scott-bumpstead/rhys-mathieson; sam-pirolo/kristy-ellis.
  - Jetts: david-upton/gary-wilson; brendon-levenson/angelique-woods; damien-ng/jetts-gym-mount-hutton; viran-kumar/paul-chau; lisa-gratrix/scanlan-karen/aaron-dearie; jetts-st-leonards/sam-bhandari. peter-tremain and jetts-st-leonards also share the opening sentence "Jetts Fitness clubs offer personal trainers and exercise physiologists".
  - Fernwood: anthony-dickens/fernwood-fitness-ballarat; ric-caldwell/kim-bullock; mark-m (bank line verbatim)/melissa-burn/cheryl-williams; clow-john (bank line verbatim)/mel-antila/steve-brookes.
- **Rule 2 drift** (a unit is told its club runs the scan):
  - luan-scherman M2 ("the North Lakes team could ask …"); thomas-hepburn-50949997 M1 ("for the club team to read"); mark-m M1 ("A PT could open a review …").
  - "Nothing installed in the studio/club" to unit owners: nebojsa-vujic, chinta-demasson, glen-souter. alissa-o-flaherty M1: "white-label for a club's own page".
  - brendon-li-on-wing: a referral person asked "where would a scan fit at The Yard Gym?".
- **Rule 13, site differences and similar:**
  - jasmine-brierley ("Two studios usually mean two sets of habits"); jack-smith-829760100 ("trainers who coach in different ways"); daniel-collins ("should feel the same"); adrian-haywood ("different member mixes").
  - lauren-anliev M1: "much of a member's training happens on their own" (the same idea was removed from marcello).
  - steve-hobart M1: "meets a new member only briefly".

### B. Factual accuracy: 4/5
- No invented number or client. Every number is in the card. The data line is correct in all 7 technical M2s and appears nowhere else.
- zanelle-marama123 M2: "The scale so far: 112,100 scans in 2025" presents a 2025 count as a running total. jasmine-brierley rewrites the locked line as "112,100 scans were taken".
- daniel-collins M1: "the scan reaches the trainer in under 45 seconds". The claim is photos to results, not delivery to a trainer.
- **100+ line with a clause attached** (rule 9):
  - david-aitchison ("…, and nothing needs to be installed in studios");
  - michael-ramsey ("…, and the setup for a brand app is one integration");
  - simonjelliott, rachel-dillon.
- **Link lead-ins that claim brands use it:**
  - "How connected fitness brands use it" and variants: elaine-jobson, brooke-price, andrew-papadopoulos, richard-peil, kane-bonke, zaac-schembri, andrewbholder.
  - garry-mortlock: "how others use body data".
- crystal-ford M2 invents a feature (the member reads only the few measurements she picks).
- mahamoud-fahour M2 says "each club's own app"; FL1 says FLG has apps per brand.
- **Reads as live at the prospect** (rule 9, last line): glen-souter M1, winona-dufrier M1 ("Members review …"), scanlan-karen M1, suzanne-herniman M1 ("… get 80+ body measurements beforehand").

### C. Brand & tone: 2/3
- **"plus" as a connector** (card word trap; the gate missed both):
  - richard-hallam M1: "80+ body measurements plus body composition estimates".
  - clancy-izzard M1: "plus a 3D model".
- **Card note copied into copy, now widespread.** "Shown (only) where the brand/club/studio chooses" and "X decides where it appears" run in about 30 messages outside the workplace programmes.
  - To unit people: paul-divin M1, crystal-ford M1 ("only if the club chooses"), kylie-falconer M1 ("only if the studio chooses"), clancy-izzard M1, aaron-o-meara M1 and M2.
  - Word for word at one company: Anytime (marcello-jimenez, clancy-izzard, aaron-o-meara ×2) and STRONG Pilates (kate-doyle-kwon, alex-fenton-mathews M1).
  - Also: laurabasta, serra-burmin, emily-crawford, michael-ramsey, suyesh-bajracharya/ben-stallworthy, kane-bonke, james-duffy, gh-undefined, dan-bova.
- **3D model led as the value** (writer note: never lead with it): richard-peil M2, mark-grey M2, tom-teasdale M2. The 3D model appears in 10 of 17 Anytime M2s.
- **Card wording as copy:** "member side/view" in about 25 referral M2s (BFT 9, UBX 10, Jetts); "a plain yes or no" in about 12 closers.
- **Card residue:** lachlan-russo ("with no event involved"), emilene-lawrance ("With no event needed"), james-trenerry ("The step up stays between her and the trainer").

### D. Format & structure: 2/3
- **Grammar:**
  - christy-vu M2 is a broken sentence that would go out as is: "a member can take a scan on their own phone gives 80+ body measurements …".
  - ric-caldwell M1 has an agreement error: "Where does one member's goals and check-in history sit".
- **Easy-out placement:**
  - Starts with "Or" with nothing before it: cameron-reid, linda-wisbey, sophie-patient, divya-hegde.
  - Pointer placed before any call offer, worded as if one came first: dinovanderent ("if you would rather"), jamie-ward-smith ("another good contact"), kylie-falconer ("would help too").
- **"Who" question in M1:** anthony-dickens, fernwood-tuggeranong, leah-libunao.
- **Summaries not accurate:**
  - Anytime says the 112,100 line stays only with Clancy and Marcello; lauren-anliev still has it.
  - Fitstop says the member-app target serves 6; it serves 8.
  - Every summary says "scan: no hits" or "nothing outstanding". That is true of the scan, not of the copy.

### E. Output quality: 2/4
- **What works:** M1s stay specific (bio and role hooks, topic-bank themes within quota), and M2s now continue each person's M1 moment.
- **One M2 template per brand.** At Jetts, Fernwood and Genesis/KX/REVL the value is nearly always "scan at home, set beside an earlier one she picks" (Jetts most of 27, mixed-2 about 24 of 29), followed by the same call + pointer + closer block.
- **Label lead-ins:** 27 (listed in the fix list).
- **Speed phrase:**
  - The banned pairing "80+ body measurements, under 45 seconds" survives in zanelle-marama123 M1, jonah-hales M2, el-finnigan M1, rob-lloyd M1, olivialuker M1, lilly-mills M1 and ben-hull M1.
  - New stock variant "… returns body composition estimates, under 45 seconds …": john-pirlo and guy-franklin (same company, nearly word for word), bruno-gallucci, ben-woolford-revl, tom-teasdale, davidnedved.
  - christie-gooden: "returns body measurements under 45 seconds".
  - Fernwood lydia-tanios/souad-sakoua: "Taken … phone, the scan is under 45 seconds …" (near-twins).
- **Card questions copied across companies** (not a same-company break, but card lines are targets, not copy):
  - "How often do goal reviews run at X, and what does the coach bring to them?": shami-sivan, glen-souter, clancy-izzard, nicholas-collins, divya-hegde, kyle-johnston, shaun-pickering.
  - "How do [clubs] run member check-ins or goal reviews today?": zanelle, brooke-price, jonah-hales, sean-hodges, john-pirlo, karen-lyle, tj-groot, josh-muriwai.
  - The product-lane "at which point in a member's year" question about 20 times.
- **Thin mixed-2 M1s** (opener + bare product line + question, with no "why it matters for this brand" line): nicholas-collins, bec-kirkup, divya-hegde, sarah-williams, jake-harris, wayne-markus, gym-genesis, kelly-strybosch.

## Fix list by batch (sentence-level unless noted)

**jetts-fitness**
- **All 27 referral M2s, second paragraph:** drop the block "A call [modal] show/cover [member view]" + "[target] may be the better contact, and a name would be welcome" + "tell me a day". Give each person their own call sentence, easy-out wording and closer shape, with no form for more than about a third of people.
- **Value line:** lisa-gratrix, jetts-gym-mount-hutton.
- **Rule 11:** jeanette-loughlan, paul-divin, martin-oliver.
- **Card note and club-run framing:** paul-divin M1, crystal-ford M1. Invented feature: crystal-ford M2.
- **Company name:** scanlan-karen M1.
- **Central-question twins (reword one side):** david-upton/gary-wilson, brendon-levenson/angelique-woods, damien-ng/jetts-gym-mount-hutton, viran-kumar/paul-chau, lisa-gratrix/scanlan-karen/aaron-dearie, jetts-st-leonards/sam-bhandari. Opening sentence: peter-tremain/jetts-st-leonards.
- **Other:** speed variant christie-gooden M2; link claims elaine-jobson, brooke-price.

**fernwood-fitness-1 / -2**
- **Closers:** rotate form across the 36 people and break the twins: jodie-sorensen, michelle-baker, ben-cook, susan-oliver-am, angela-williams, melissa-burn, fernwood-fitness-ballarat, emma-tilley, lydia-tanios, suzanne-herniman, hayley-richey, binish-mobeen, melissa-robinson, stacey-flentje.
- **Bolted capture sentence:** drop or vary it in jessica-pupillo, suzanne-herniman, adriana-ampuero (the "her phone guides" trio), michelle-baker, hayley-richey, melissa-mcglinn, moby-malik, mary-papazoglou, binish-mobeen, guneet-cheema.
- **Labels:** ric-caldwell, ann-wilkesmann, tedy-ferreira, susan-oliver-am, kim-bullock.
- **Same club (Ballarat):** lee-squire / fernwood-fitness-ballarat need different easy-out targets; the club also gets two speed sentences.
- **Openers:** melissa-mcglinn/tedy-ferreira, clow-john/hayley-richey, melissa-jones/jessie-anderson.
- **Central question:** anthony-dickens/fernwood-fitness-ballarat, ric-caldwell/kim-bullock, melissa-burn/cheryl-williams, mark-m and clow-john (topic-bank line verbatim). "Who" questions: anthony-dickens, fernwood-tuggeranong.
- **Other:**
  - Speed near-twins lydia-tanios/souad-sakoua.
  - Easy-out wording melissa-robinson/souad-sakoua/mary-papazoglou.
  - Live wording suzanne-herniman M1.
  - Grammar ric-caldwell M1.
  - Rule 2 mark-m M1.

**bft**
- **"Member side" in the call sentence:** keep it for at most 4 of these 9: scott-bumpstead, philip-grasso, jason-clark, sarina-sham, laura-carroll, kristy-ellis, anthonyhoangbft, matt-jones, adem-bek.
- **"A plain yes":** liana-nio, steve-grace, anthonyhoangbft, zoe-clark.
- **Labels:** zanelle-marama123 (also "so far"), valentin-u.
- **Speed and 100+:** speed pairing zanelle-marama123 M1; 100+ clause david-aitchison.
- **Central question:** sarina-sham/laura-carroll/matt-jones, philip-grasso/adem-bek/anthonyhoangbft, scott-bumpstead/rhys-mathieson, sam-pirolo/kristy-ellis.
- **Other:** value line katelyn-farmer; rule 2 luan-scherman M2; rule 14 steve-grace M1 ("besides your own coaching notes").

**ubx**
- **Openers:** jonah-hales/davidnedved; bring "Noticed" down to 3 (also dinovanderent, bianca-latorre, paul-duggan).
- **Value line:** jonah-hales M2, timwest4 M2.
- **Speed:** pairing jonah-hales M2; variant davidnedved M2.
- **Labels:** timwest4 (the label also opens the M2), bianca-latorre.
- **Easy outs:** twins taylor-papangelou/cassie-maynard; placement dinovanderent, jamie-ward-smith.
- **"Member's side/view"** in 10 closers: vary.
- **Rule 2 and live wording:** glen-souter M1, chinta-demasson M1.

**fitstop**
- **"plus":** richard-hallam M1.
- **Easy outs:**
  - Twins: adam-stevens/jamie-biondi, kevin-kensley/milan-sekulic, jonpepper/paul-emanuel.
  - Member-app target down from 8: bruce-mcconnel, bentoleafoa, adam-stevens, chandell-fretwell, jesse-malseed, jamie-biondi, lachlan-russo, lauren-nash.
- **Closer twins:** bentoleafoa/nebojsa-vujic/brenna-dillon, josephine-tuah/mark-vaiao.
- **jasmine-brierley:** rule 13 (M1); label + reworded line (M2).
- **Other:** card residue lachlan-russo, emilene-lawrance; link claim andrew-papadopoulos; rule 2 nebojsa-vujic.

**anytime-fitness-australia**
- **Grammar:** christy-vu M2 (broken sentence).
- **"plus":** clancy-izzard M1.
- **Openers:** richard-peil/clancy-izzard.
- **"Shown where the brand chooses" and 3D-model lead:** clancy-izzard, aaron-o-meara (M1, M2), marcello-jimenez, mark-grey, richard-peil, tom-teasdale.
- **Repeated M2 product sentence:** marcello-jimenez/steve-hobart.
- **Closer twins:** marcello-jimenez/steve-hobart, jordan-smith/winona-dufrier.
- **Labels:** lauren-anliev (the label also opens the M2), marcello-jimenez.
- **Other:**
  - Speed variant tom-teasdale M1.
  - Live wording winona-dufrier M1.
  - Deficit lauren-anliev M1, steve-hobart M1.
  - "Who" question leah-libunao.

**mixed-1**
- **Labels:** rebeccacarson2, sarahbroadhottot, jeremy-saville, sean-hodges, angela-tween, kane-schrader, shane-johnson (100+).
- **Closers:**
  - Twins: shane-johnson/kane-schrader/gh-undefined, daniel-collins/marvin-mangubat, victor-ramirez/rachel-macedo/jack-smith.
  - "and I will write to them": marvin-mangubat/kaillum-key.
- **Speed distortion:** daniel-collins M1. Rule 2: thomas-hepburn M1.
- **Rule 13:** jack-smith, daniel-collins, adrian-haywood (M1).
- **Card note:** jamesduffy26 M1, gh-undefined M2.
- **Viva member-app target:** used 3 times (angela-tween, arshad-hussein, shane-johnson); move one.

**mixed-2**
- **"Or" with nothing before it:** cameron-reid, linda-wisbey, sophie-patient, divya-hegde.
- **Closer twins:** gym-genesis/cameron-reid/mitchell-bird, brentonwilliamson/tom-bayford, james-trenerry/sophie-patient/divya-hegde, bruno-gallucci/kelly-strybosch, benseymour10/mark-jackson, jake-harris/adam-coombes.
- **Value lines:** keep the "beside an earlier set she picked" argument for at most a third per brand.
- **Speed variant:** john-pirlo/guy-franklin (near-twins, Genesis), bruno-gallucci, ben-woolford-revl.
- **Labels:** ianjensenmuir, luisa-helps, ben-woolford-revl.
- **Card note to a unit:** kylie-falconer M1.
- **Thin M1s:** nicholas-collins, bec-kirkup, divya-hegde, sarah-williams, jake-harris, wayne-markus, gym-genesis, kelly-strybosch.

**mixed-3**
- **Labels:** simon-rees, peter-reed, catijnschierbeek, brettcondron, connor-hill.
- **Rule 2:** brendon-li-on-wing (M1 question, M2 "needs nothing from the club beyond a place in the app"), alissa-o-flaherty M1.
- **Openers:** jon-davie/michael-nysten.
- **Other:** card question shaun-pickering; card note dan-bova.

**mixed-4**
- **Rule 11:** kyliekerr, suyesh-bajracharya.
- **Card note:**
  - Word for word at STRONG Pilates: kate-doyle-kwon, alex-fenton-mathews (M1).
  - Also emily-crawford, laurabasta (M1, M2), serra-burmin, michael-ramsey.
  - suyesh-bajracharya/ben-stallworthy ("Your Reformer decides what she/they see").
- **Other:** 100+ clause michael-ramsey; FLG app fact mahamoud-fahour.

**mixed-5**
- **Speed pairing:** el-finnigan, rob-lloyd, olivialuker, lilly-mills, ben-hull (all M1).
- **Value line:** rachel-dillon M2, scott-freeman M2.
- **100+ clause:** simonjelliott, rachel-dillon.
- **Openers:** lilly-mills/brooke-young, danielle-monroy/david-bennet.
- **Link claims:** kane-bonke, zaac-schembri, andrewbholder, garry-mortlock.
- **Card note:** kane-bonke M1.
- **Product-lane card question:** rachel-dillon, scott-freeman, nathan-james, matknipe, danielle-monroy, andrewbholder, chris-caldwell, jude-tarran, dr-toby-ford.
- **Other:** jude-tarran ("keeps every session comparable" reads as tracking); rule 14 simonjelliott M2 ("between screening events").

## Top 3 issues (priority for improver)

1. **Per-brand M2 skeletons came back in new words** (Jetts three-beat block in 27/27; Fernwood yes/no closer plus a capture sentence; mixed-2 closers rotated through four sentences; "member side" at BFT and UBX).
   - The grid assigned a closer form, but each form got one sentence.
   - The card's rule wording ("members' side", "a plain yes or no") became copy.
   - The grid needs a wording column, and the scan needs a closer-shape check with the target noun removed.
2. **Swaps on the fixed lines and the speed phrase.**
   - 27 label lead-ins replaced "ran".
   - 7 banned 80+ + speed pairings survive, and a new body composition + speed stock sentence appears in 6.
   - The scan cleared all of them. Fix rule: a fixed line stands alone or follows a full sentence, never a label; the speed phrase never follows an output noun directly.
3. **Card notes and topic-bank lines copied as copy.**
   - "Shown only where the brand chooses" appears in about 30 messages, word for word at Anytime and STRONG Pilates.
   - Central questions repeat within BFT, Jetts and Fernwood, several verbatim from the bank.
   - Both pre-date the fix round, and QC1 under-reported them.

## Coordinator review

agreement: ✅ agree (my scan was blind to the swaps: labels on fixed lines, stock speed sentences, the Jetts three-beat M2 block; after adding checks for rules 11 and 20-24 it finds the same Jetts block at 17/18/15/12 of 30)
top_issue: per-brand M2 skeletons came back in new words (Jetts 27/27), because each closer form in the grid got one sentence and the card's rule wording became copy.
status: 13/20, at or above the bar of 12. A third round at sentence level goes out first (card rules 20-24 added, `_fix3-*` lists = this fix list plus the upgraded scan), verified mechanically, then Vadim's sample checkpoint.
