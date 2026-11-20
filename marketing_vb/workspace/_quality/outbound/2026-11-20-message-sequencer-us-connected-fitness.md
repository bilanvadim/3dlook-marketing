---
qc_date: 2026-11-20
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-11-19-us-connected-fitness/messages/ (109 pairs, 4 batches: peloton, mixed-1, mixed-2, mixed-3; scored from the coordinator dump messages-dump.txt + _check.json)
track: outbound
artifact_type: messages
product: fitxpress
total_score: 11/20
status: failed
coordinator_review:
  agreement: "⚠️ agree on direction, counts overstated"
  top_issue: "Product unnamed and one product-sentence skeleton are real, but checked against the files: 5 pairs name FitXpress/3DLOOK nowhere (not 11; 8 more only in M2), the '2 photos ... return 80+' skeleton is in 38/109 M1s (not ~90%), though 2 photos + 80+ sit in all 109 and 'timestamped record' in 78. Vadim chose a fix round (2026-11-20); card target fixed; gate gained product-name, cross-company M2, label and British-spelling checks (suite 230/0)."
---

# QC Report: message-sequencer, 2026-11-20 (US connected fitness, 109 pairs)

**Artifact:** all 109 pairs, read company by company. Scored against `card-messages.md` and the four `_profiles-*.md` files. Limits, signature, bans, detector and completeness are taken from the gate as fact.
**Total: 11/20, failed.** The failure does not come from invented numbers. Every figure is from the list, the 100+ line always reads as "3DLOOK has worked with 100+ clients", there is no $ figure, and the URL and calendar rules hold everywhere. The score comes from four other problems:
1. The Peloton batch mostly never names the product.
2. Same-company sameness is high.
3. Card target wording is pasted as copy across the campaign.
4. There is a cluster of claim and Never-line slips.

**Recommendation:** regenerate the Peloton batch, and run a fix round on mixed-1, mixed-2 and mixed-3 from the lists at the end.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence: 2/5

- **No product name in Message 1 (card part 3, "how FitXpress fixes it").**
  - 11 pairs never say FitXpress or 3DLOOK in either message: meghiggins21, eugenekwak, laurarivera-uxresearch, joncilley, yasminkothari, bethraewendt, tworetzky, barbarathornethomsen, sarah-rodenberg, lindsay-pontello (Peloton), and ashlei-mitchell-0a302a220 (BODi).
  - brad-fagan-8382a888 names it only in the Message 2 compliance line.
  - These Message 1s pitch "A body scan inside the Peloton app could…" with no vendor.
- **The same-company ratio rule is broken** (details under E): Peloton questions, Tonal argument, iFIT, Centr and Caliber product sentences, BODi Message 2 value, Trainerize pain.
- **Card target wording is pasted as copy** (prompt rule 11): pain targets, question targets and Message 2 value targets. Full list under "Card wording as copy" below.
- **Account facts Never lines broken:**
  - **jessventicinque:** "Fitbod is moving toward helping members understand their data and interpret their progress inside the app." This is the CEO's TechRadar quote with one comma changed (Never: "his quotes verbatim").
  - **matt-lehrer-67664014, Message 2:** "Capture happens on the member's phone between sessions". The Hydrow bullet does not allow "between sessions".
  - **"no club visit"**, an off point for every account: theodorelui ("with no hardware and no club visit"), sarah-rodenberg ("The scan needs no hardware and no club visit"), trent-ward-12b992b2 ("with no hardware and no club visit").
  - **jakequan:** "The body change it is for needs its own measurement." This implies Future lacks body data. Future runs lab body-composition scans, and its bullet says never to imply that.
  - **Held:** no other prospect is named anywhere; nothing about the Interactive Strength holding, ticker or deal; no ABC club software in Trainerize copy; no company figures; no Tony Horton; nothing about re-contact history.
- **Lane rule:** greg-nuckols-92545595 (lane `leadership`) carries the repeatability sentence. The card allows it only in `product`, `coaching` or `science`. His Account facts ask for a science-led angle, so re-lane him or drop the sentence.
- **Message 2 repeats Message 1:**
  - jenniferannpelton: "Capture runs with pose and framing guidance…" after Message 1's "with pose and framing guidance".
  - ruth-sylvia-a1238417: waist, hip, fat and lean mass are already in Message 1.
  - longdnguyen: "One integration would reach every coach's clients" repeats Message 1's "one integration that puts a body check-in in front of every coach's clients".
  - alessandra-gotbaum: pose guidance again.
  - prasanna-swaminathan-6bbb4713 and ryan-mott-51660a11: processing status again.
- **Summaries:** `_summary-*.md` is missing for peloton, mixed-2 and mixed-3 (prompt step 5).

### B. Factual accuracy: 3/5

- **Numbers:** all from the list.
  - 100+ is correct in all 15 uses.
  - 112,100 is correct in form and never tied to fitness.
  - The repeatability sentence is verbatim in 14 of 15. **andrewzey** adds a claim to it: "…less than 1 cm for most evaluated measurements, which makes the change between two weekly reviews comparable."
  - No accuracy %, no client names, no $.
- **The capture is promised as stylable, but the capture layer is fixed.** 7 Message 1 questions ask what the capture must match:
  - joncilley: "How closely would a branded capture need to follow the Strength+ look to feel native?"
  - doug-reeder-3247511: "What does the branded client app need a new capture to look like?"
  - karl-mahrenholz: "What would a body capture have to match in Cal AI's design…?"
  - howens: "What would a capture inside BODi's app have to match in the app's design?"
  - john-santo-096310149: "What would a white-label capture have to match in the Echelon app's design?"
  - deepakmm: "…in the look of the CLMBR and FORME apps?"
  - rkekelis: "…in the look of the Body Metrics screen?"
  - Four of these pairs then say "the capture layer stays fixed" in their own Message 2: karl, john-santo, deepakmm, rkekelis.
  - The card lists this as a question target. This is a card defect too; fix it at the source.
- **Data location and ownership claims go too far:**
  - theodorelui: "the scan and its record sit on Peloton's side". Measurements are also stored by 3DLOOK.
  - heidi-jones-ny: "this is one that Echelon would own end to end".
  - joncilley: "Everything runs on the member's own phone". Processing is server-side.
  - elizabeth-palmer-97820997: "with the API returning it linked to the client profile". The platform links the record through the scan ID.
  - The "belong to X" lines (andrew-sugerman, jondwang, tom-aulet-85493127) stay inside the card's white-label ownership target.
- **Consistency claims beyond the repeatability sentence:**
  - becca-valente: "a guided scan keeps the capture the same"
  - oaktownolivia: "which keeps check-ins comparable from one to the next"
  - zekebrustkern: "guided capture keeps that variance down"
- **Unsupported claims:**
  - elizabeth-palmer: "Coaches on Everfit ask the platform to record more for their clients." It is invented, and it answers her own question.
  - karl-mahrenholz: "MyFitnessPal members know that flow". Cal AI is a standalone app.
  - shayne-k-jessop: "the progress it sees is training metrics". The bullet says the AI coach also uses health data.
  - mikefarrell: "which shows the log is a feature members use"
  - jacob-wax: "Strength and running are both growing parts of the Peloton app"
  - matt-lehrer: "FitXpress shows what the block changed" (causal).
  - danaehirsch: treats iFIT Pro, a membership, as an app ("runs inside iFIT Pro", "into iFIT Pro today?").
- **Pilot read as free:** "There is no integration fee." sits right after the pilot design in keith-kraker (same paragraph), nicholasjrobinson, jmcluff and js531. The card says "never say or imply that the pilot is free".
- **Plan wording:**
  - mirelacialai: "3D Body Progress tracking and 3D Goal Visualization are Pro plan features". This reads as a Peloton plan; name it FitXpress's.
  - jmcluff: compares free-to-premium conversion with no 3D tools in the paid plan.
- **Sourcing:** n/a. No compliance line is required for this ICP. The two pairs that use it (brad-fagan, greg-nuckols) use it verbatim.

### C. Brand & tone: 2/3

- **Broken sentence:** tworetzky, "One number from a weigh-in, often self-reported, leaves open where the body changed stays unknown."
- **Banned "so" introducing a benefit:** productobsessedlaura, "…workout history, so that record would land on the screen members use for progress."
- **British spelling in an American English campaign:**
  - "personalised": nickcaldwell, becca-valente, bentbartlett
  - "standardised": prasanna-swaminathan
  - "white-labelled": finn-hegarty
- **Stiff or awkward phrasing:**
  - "the waist and the fat and lean mass move/shift" in about 8 Message 1s.
  - "A call would allow me to…" (lindsay-pontello, thekellycard).
  - "an app like BODi's" (marietta-p).
  - "the partner's own app" (billy-hulbert).
  - "the record returns 80+ body measurements" (john-ybarra).
  - A sentence opening with a digit: "2 guided photos inside the Caliber app return…" (annakatedavis).
- **"the company's own" instead of the brand name:** karl-mahrenholz, christina-to.
- **No hype, no thanks openers, peer register.** This is good.

### D. Format & structure: 2/3

- `_summary` is missing for 3 of 4 batches. `_summary-mixed-1.md` says "product 20"; the batch has 23 product people.
- **No Account-facts company line in Message 1, only a title restatement:**
  - kelsey-van-ackeren: "Your growth background puts onboarding close to your work…"
  - megan-johns-72b40818a: "You run customer experience at Centr…"
  - danaehirsch: "As Director of Product Partnerships you see…"
  - nicholasrwilley (headline-only line).
- **Message 2 overloaded** (the card allows one or two value points):
  - chris-muir: 4 points
  - greg-nuckols: 4 points
  - karl-mahrenholz, shayne-k-jessop, justin-fauci, jshottan, thekellycard: 3 points each
- **Two pain lines in one Message 1:** howens, zekebrustkern, lisa-privitera, andrew-sugerman.
- **Missing easy out for non-buyers:** maureen-key (individual contributor), daniellepeckskamp (manager).
- **Upstream:** ryan-mott-51660a11 has lane `data`, which is not a card lane.
- **Frontmatter:** the per-person files carry no `product:` frontmatter. That format is fixed by the card's Output format and `split-messages`, so the hard rule was not applied to the agent. It belongs to the script owner.
- **Held:** URL never in Message 1. URL in about half of each company's Message 2s (Peloton 9/18, Trainerize 6/11, BODi 6/11, MFP 5/8, Tonal 4/7, Echelon 4/6, iFIT 3/5, Ergatta+IS 4/8, Centr 3/5, Everfit 3/5). Calendar always last. "No integration fee" ×12, Message 2 only, once per pair.

### E. Output quality: 2/4

The pairs are company-specific and readable. Hooks come from the Account facts, the pain → mechanism → question flow works, and the Account-fact "Use" assignments were followed. The campaign still reads as one template. The per-track 60% uniqueness bar fails for several Message 2s.

**Same-company sameness, per company:**
- **Peloton (18):**
  - The product sentence is a colon list "…: 2 photos, 80+ body measurements, [fat and lean mass estimates], … through the API, in Peloton's own screens" in 14/18. The exceptions are eugenekwak, bethraewendt, sarah-rodenberg and jacob-wax. "in Peloton's own screens" appears 4 times.
  - Questions about how Peloton decides, pilots or rolls out a feature, ×5: theodorelui, tworetzky, barbarathornethomsen, sarah-rodenberg, kavitajv. sarah-rodenberg's "which teams carry the rollout?" is close to a bare who-owns question.
  - Question twin: bethraewendt "What do testers point to when you ask how they know their body is changing?" = laurarivera-uxresearch "…how they know they are progressing, what do they point to?"
  - "record(s) the work done" ×3: meghiggins21, eugenekwak, yasminkothari.
  - Company line twin: cole-shipley "Peloton's app tracks classes, stats and progress" = joeli-spencer "Peloton's app already tracks classes, stats and progress".
  - Message 2 twin: sarah-rodenberg = brad-fagan "…ships as web and mobile SDKs with iOS and Android support."
  - Message 2 value overuse:
    - timestamp + processing status ×3: eugenekwak, yasminkothari, jacob-wax
    - no hardware ×4: joncilley, theodorelui, sarah-rodenberg, joeli-spencer
    - "There is no integration fee." identical ×3: nickcaldwell, kavitajv, joeli-spencer
  - Closers in the shape "If [X] sits with another team / is elsewhere, point me to …" ×6: theodorelui, cole-shipley, barbarathornethomsen, sarah-rodenberg, kavitajv, lindsay-pontello. "sits with another team" is word for word in barbara and lindsay. The easy out "progress experience/screen" appears ×3.
- **Trainerize (11):**
  - "what the client enters" pain ×3: jenniferannpelton, thekellycard, zekebrustkern. Zeke's version is also a pain stated about Trainerize: "a client's check-in data is mostly what the client enters".
  - Separate-app twin: finn-hegarty ≈ keegan-dowling, "A separate scanning app [would put / puts] the client and the result under another brand".
  - Closer twin: ericreimers = finn-hegarty, "Calendar for a call, or a pointer to whoever …".
- **BODi (11):**
  - "November 19 release made … faster": robcanning, mikefarrell.
  - Question twin: robcanning "How does your team test a new onboarding step before it reaches every member?" ≈ vjmuthuraman "Before a new onboarding step ships to everyone, how is it judged at BODi?"
  - Training-metrics pain ×3: jeffrey-scott, howens, ashlei-mitchell.
  - "show(s) visible change" ×2: jenny-parker, brandoncowley.
  - Message 2 "capture fixed + BODi's own screens" ×3: nicholasrwilley, mikefarrell, jenny-parker.
  - The product sentence is the same skeleton with a swapped verb in 11/11.
- **MyFitnessPal (8):**
  - oaktownolivia and vptaylo share the pain (home tape) and the question target (what members do when they log measurements).
  - ruth-sylvia ≈ vptaylo Message 2: "waist and hip changes from one [body scan / check-in] to the next".
- **Tonal (7):**
  - One argument for three people, "a member asks about results, so here is a record to point to":
    - amartanna-cpa-ca: "gives a post-program question a number to point at"
    - josephrodonis: "that record is what a coach could point to"
    - tanysha-smith: "an answer to point to" + "what do you point them to?"
  - Product sentence twin: josephrodonis ≈ tanysha-smith.
  - Question target twin (judging a block): maureen-key, jenna-moore.
- **Echelon (6):** good spread. Only "FitXpress is a…" ×2 (patmatthews, john-santo).
- **iFIT (5):** 3/5 share one product sentence: "FitXpress adds a body [scan/check-in] to the iFIT [app/onboarding flow]. The member takes 2 [guided] photos on their own phone, and [the API returns] one timestamped record with 80+…" (stephanie-raterman, shayne-k-jessop, daniellepeckskamp).
- **Ergatta + Interactive Strength (8, one family):**
  - The product sentence "FitXpress [verb]: 2 guided photos on the member's phone … return 80+ body measurements and fat and lean mass estimates as one timestamped record" appears in 8/8.
  - "Ergatta's game-based programs": alessandra-gotbaum, tom-aulet.
  - "The page for this use case:" ×4: prasanna, tom-aulet, deepakmm, trent-ward.
- **Centr (5):**
  - nicholasjrobinson ≈ productobsessedlaura, near word for word: "FitXpress adds a body scan [inside/to] the Centr app under Centr's [own] brand. The member takes 2 photos on their own phone, and the API returns one timestamped record with 80+ body measurements and body composition estimates." megan-johns uses the same skeleton.
  - Company line twin: jrafferty ≈ productobsessedlaura, "Centr's app (already) tracks results and workout history".
- **Caliber (4):**
  - "At 3DLOOK we built FitXpress" ×2: annakatedavis, chris-muir.
  - Product sentence: jmcluff ≈ chris-muir.
  - "The page for this use case:" ×2.
- **Future (3):** "2 guided photos on the member's phone" skeleton ×3. "The page for this use case:" ×2.
- **Lose It! (4):** "The page for this use case:" ×2. Otherwise fine.
- **Everfit, MacroFactor, Fitbod, RP, Ladder, Carbon, Hydrow, Trainwell, Jefit:** fine on spread.

**Cross-company twins inside one batch** (the batch could see these; a reviewer reads them as a mail merge):
- **mixed-1:**
  - ericreimers = brandoncowley, the whole Message 2 body: "Web and mobile SDKs cover iOS and Android. There is no integration fee."
  - elizabeth-gray = howens = jshottan (mixed-2): "On a strength program the weight total can hold while waist and fat and lean mass move."
  - "The scale so far is 112,100 scans…" ×3: jenniferannpelton, jenny-parker, vptaylo.
- **mixed-2:**
  - heidi-jones = danaehirsch, the whole Message 2 body: "Web and mobile SDKs cover iOS and Android, and the screens are white-label."
  - andrew-sugerman ≈ jondwang, Message 2: "The scan and its record would belong to …" + the 100+ line.
  - lisa-privitera = longdnguyen: "A coach setting the next block from weight, photos and notes has no measured change to compare."
  - kevin-j-custer = josephrodonis: "A progress photo shows visible change, with no measurement to compare at the next check-in."
  - Pilot sentence ×3: maureen-key ≈ daniellepeckskamp ≈ nicholasjrobinson.
- **mixed-3:**
  - luanaperez = alisa-aguirre, Message 1: "At 3DLOOK we built FitXpress, a body scan inside the app: 2 guided photos return …". Their Message 2 "concrete answer from waist and hip" lines are twins too.
  - justin-fauci = corydavisprofile, Message 2 sentence 1.
  - Pilot twins: trent-ward ≈ js531; jmcluff ≈ jake-grundstein.
  - "The page for this use case:" is the label on all 17 URLs in the batch.

**Card wording as copy (coordinator item 2), my reading:**
- **Real leaks:**
  - Pain targets pasted:
    - "On a strength program … the weight total can hold while waist and fat and lean mass move": 3 identical, about 9 near.
    - "the body change it is for" ×9.
    - "where the body changed stays unknown" ×9.
    - "has no measured change to compare" ×5.
    - "A check-in form holds only what the member enters/types in" ×9.
    - "what comes back to the platform depends on that app" ×5.
  - Question targets pasted:
    - "What does a [X] member see at the first check-in beyond weight and workouts?": kendall-wilson, marietta-p, jrafferty, annakatedavis.
    - "Would a scan belong at onboarding or at the first check-in?": productobsessedlaura.
    - "How does a partner capability get into [app] today?": heidi-jones, danaehirsch, jasonbhwang, brad-fagan, laurietaylorkemp, billy-hulbert.
    - "How does the team test a new onboarding step": meghiggins21, robcanning, kelsey-van-ackeren, bogatzproductmanager.
  - Message 2 targets pasted:
    - "comparable from one check-in to the next": tanysha-smith, lisa-privitera, megan-johns, elizabeth-palmer, matt-lehrer.
    - "could review girths and lengths" ×5.
    - "the member app's progress experience" (the card's easy-out example) ×6.
    - "It would start as a pilot before any rollout" (andrew-sugerman).
- **Not a defect in itself:** "on the member's phone" ×33 is a product fact. The problem is that it sits in the same slot of the same product sentence; fix the skeleton, not the phrase.
- **Mostly acceptable:** "at the first check-in" ×13. Most uses are inside the pilot design, where it is the design's content. The leak is the 5 questions listed above.

**Numbers bolted on (item 4):**
- 112,100 as a stub after an unrelated value line:
  - "The scale so far is …" ×3: jenniferannpelton, jenny-parker, vptaylo.
  - "For scale: …" ×3: alessandra-gotbaum, justin-fauci, andrewzey.
- "3DLOOK has worked with 100+ clients. There is no integration fee." as a two-stub paragraph: jmcluff, js531, bentbartlett. The 100+ meaning is correct everywhere.
- The speed sentence (×14) is mostly added where speed is not the point. Examples: cole-shipley's whole Message 2 is that one sentence; thekellycard's Message 2 repeats Message 1's 80+.

**Persona fit (item 6):**
- **Pool B CX heads** (oaktownolivia, amartanna, megan-johns, luanaperez, alisa-aguirre): the asks are role-true, but luanaperez and alisa-aguirre are twins.
- **Pool D:**
  - The user research pair is role-true but twinned.
  - The strategy people are pushed into five process questions.
  - kavitajv's easy out to the paid plan does not fit program management.
- **Tonal Head Coaches:** the questions are coaching-true. Both get API mechanics ("comes back through the API") and share the "point to" argument. tanysha-smith's easy out to "the owner of onboarding" is off for a coach.
- **Trainerize parent level:** the asks are role-true, with easy outs on all P3s. But two Message 1s assert a Trainerize remit the profiles do not show:
  - doug-reeder: "Product line management at Trainerize is where that would be packaged"
  - laurietaylorkemp: "Partner Solutions puts you where new capabilities enter Trainerize's trainer and client apps"
- **Other misfits:**
  - maureen-key (individual-contributor programming specialist) gets a retention pilot and no easy out.
  - brandoncowley (PM) gets "no integration fee".
  - jenny-parker (production VP) gets white-label screens and the scan count.
  - billy-hulbert (affiliate partnerships) gets an SDK spec.
  - corydavisprofile (developer co-founder) gets the easy out "whoever handles integrations", which is likely himself.

## Top 3 issues (priority for improver)

1. **The product is unnamed in 12 Message 1s.** 11 pairs never say FitXpress or 3DLOOK (10 Peloton + ashlei-mitchell). The Peloton batch wrote hypothetical "a body scan inside the Peloton app could…" lines. The gate passes them because "body measurements" counts as a product specific. Add "FitXpress or 3DLOOK named in Message 1" to `check-messages`.
2. **The campaign is one template.**
   - The product sentence is the same skeleton ("FitXpress [verb]: 2 guided photos on the member's phone return 80+ body measurements and fat and lean mass estimates as one timestamped record") in roughly 90% of Message 1s. It is 8/8 in the Ergatta/IS family, 11/11 at BODi and 3/5 at iFIT.
   - Card pain, question and value wording is pasted verbatim, with identical sentences across 3+ people.
   - Same-batch cross-company Message 2 bodies are word for word (Eric = Brandon, Heidi = Danaé, Andrew S ≈ Jonathan W, Justin ≈ Cory).
   - "The page for this use case:" labels all 17 mixed-3 URLs.
3. **Claim and Never-line slips:**
   - 7 questions promise a stylable capture; 4 of those pairs contradict their own Message 2's "capture layer stays fixed". The card's question target causes this.
   - Data location and ownership overreach (Ted, Heidi, Jon).
   - Fitbod CEO quote; Hydrow "between sessions"; "no club visit" ×3.
   - "No integration fee" placed against the pilot ×4.
   - tworetzky's broken pain sentence.

## Fix list per batch (priority order)

### Peloton (regenerate, or rewrite at least 15/18)
1. Name FitXpress (and/or 3DLOOK) in Message 1 of the 11 listed under A, in varied forms rather than "FitXpress adds…" ×11. Break the colon-list product skeleton in at least 8.
2. **tworetzky:** "One number from a weigh-in, often self-reported, leaves open where the body changed stays unknown." → rewrite (broken grammar).
3. **bethraewendt:** "What do testers point to when you ask how they know their body is changing?" → same question as laurarivera-uxresearch; give Beth a different target, e.g. what a repeatable check-in would let a study compare.
4. **Questions:** keep at most 3 of the 5 decide/pilot/rollout ones (theodorelui, tworetzky, barbarathornethomsen, sarah-rodenberg, kavitajv). Move the rest to the strength or running push. Sarah's "which teams carry the rollout?" is near a bare who-owns.
5. **theodorelui:** "the scan and its record sit on Peloton's side, with no hardware and no club visit." → drop "sit on Peloton's side" and "no club visit". **sarah-rodenberg:** drop "and no club visit". **joncilley:** "Everything runs on the member's own phone" → capture runs on the phone; results come back through the API.
6. **joncilley:** "How closely would a branded capture need to follow the Strength+ look to feel native?" → ask about the onboarding and results screens around a fixed capture.
7. **sarah-rodenberg = brad-fagan:** "…ships as web and mobile SDKs with iOS and Android support." → change one value point.
8. **"There is no integration fee."** ×3 (nickcaldwell, kavitajv, joeli-spencer): keep 2 at most. Processing-status Message 2 ×3 (eugenekwak, yasminkothari, jacob-wax): swap one. "No hardware" ×4: drop 2.
9. **joeli-spencer:** "Peloton's app already tracks classes, stats and progress" = cole-shipley's line → reword Joeli's.
10. **Closers:** 6 use "If … sits with another team / elsewhere, point me to …". Vary 3; barbarathornethomsen and lindsay-pontello share the exact words. kavitajv's easy out → onboarding or partner integrations, not the paid plan.
11. **mirelacialai:** "are Pro plan features" → "are features of FitXpress's Pro plan".
12. **nickcaldwell:** "personalised" → "personalized". **jacob-wax:** drop "growing".

### mixed-1 (Trainerize, BODi, MyFitnessPal)
1. **ashlei-mitchell-0a302a220:** no product name anywhere → name FitXpress in Message 1.
2. **elizabeth-gray-94237a106 and howens:** "On a strength program the weight total can hold while waist and fat and lean mass move." → card text, identical to each other and to jshottan; rewrite both in own words. howens: keep one pain line.
3. **brandoncowley:** Message 2 "Web and mobile SDKs cover iOS and Android. There is no integration fee." = ericreimers → new value point for Brandon (no fee line for a PM).
4. **karl-mahrenholz, howens, doug-reeder:** the capture-match questions → ask about the screens around the fixed capture. karl's Message 2 already says it is fixed.
5. **"The scale so far is 112,100 scans in 2025 across all 3DLOOK customers."** ×3 (jenniferannpelton, jenny-parker, vptaylo) → keep at most one.
6. **Trainerize "what the client enters" ×3:** re-target thekellycard ("A check-in form holds only what the client enters, and body shape stays outside it.") and zekebrustkern ("…a client's check-in data is mostly what the client enters…", also a pain stated about Trainerize).
7. **finn-hegarty:** "A separate scanning app would put the client and the result under another brand." ≈ keegan-dowling → re-target Finn's pain.
8. **BODi:**
   - mikefarrell: "BODi's November 19 release made typing measurements faster, which shows the log is a feature members use." ≈ robcanning's line and an inference → drop the release fact or the inference.
   - vjmuthuraman: "Before a new onboarding step ships to everyone, how is it judged at BODi?" ≈ robcanning's question → new question.
9. **BODi Message 2 "capture fixed + BODi's own screens" ×3** (nicholasrwilley, mikefarrell, jenny-parker): swap two. Jenny Parker (production) gets a program-side point.
10. **kendall-wilson and marietta-p:** card question target verbatim ("…see at the first check-in [today] beyond weight and workouts?") → reword both.
11. **ruth-sylvia-a1238417:** Message 2 repeats her Message 1 and ≈ vptaylo's → new value point for a P1 (pilot or the scan ID).
12. **vptaylo:** same pain and question target as oaktownolivia → re-target.
13. **jenniferannpelton:** Message 2 repeats Message 1's pose guidance → new value point.
14. **doug-reeder and laurietaylorkemp:** soften the asserted Trainerize remit ("if Trainerize's product line sits with you…").
15. **Smaller items:**
    - finn-hegarty closer = ericreimers closer; "white-labelled" → "white-labeled".
    - tristanalexander ≈ ashlei-mitchell: "chart waist and thigh changes from one record to the next".
    - karl-mahrenholz: "MyFitnessPal members know that flow" → drop. "the company's own" → name MyFitnessPal (karl, christina-to).
    - kelsey-van-ackeren: add an Account-facts company line.
    - marietta-p: "an app like BODi's" → "the BODi app".
    - Fix the summary count (product 23).

### mixed-2 (Tonal, Echelon, iFIT, Centr, Everfit)
1. **Tonal "point to" argument ×3:** re-target tanysha-smith (the program she leads and what a block shows), and remove "point to/at" from amartanna-cpa-ca or josephrodonis. Rewrite tanysha-smith's product sentence (≈ josephrodonis).
2. **iFIT:** rewrite the product sentence of 2 of stephanie-raterman, shayne-k-jessop, daniellepeckskamp.
3. **Centr:**
   - productobsessedlaura: rewrite the product sentence (≈ nicholasjrobinson).
   - productobsessedlaura: "…, so that record would land on the screen members use for progress." → banned "so". The company line ≈ jrafferty's.
   - productobsessedlaura: "Would a scan belong at onboarding or at the first check-in?" → card target, and "scan" without "body".
4. **danaehirsch:** Message 2 "Web and mobile SDKs cover iOS and Android, and the screens are white-label." = heidi-jones → change Danaé's. Also say "the iFIT app", not "iFIT Pro", as the place the scan runs.
5. **heidi-jones-ny:** "this is one that Echelon would own end to end" → "under Echelon's brand".
6. **jondwang:** Message 2 ≈ andrew-sugerman's → make it build versus integrate (his Message 1 topic).
7. **john-santo-096310149:** "What would a white-label capture have to match in the Echelon app's design?" contradicts his Message 2 → ask about the surrounding screens.
8. **Card pain pasted verbatim:**
   - jshottan: the strength-program sentence.
   - lisa-privitera = longdnguyen: "A coach setting the next block from weight, photos and notes has no measured change to compare."
   - kevin-j-custer = josephrodonis: the progress-photo sentence.
   - Rewrite one of each pair; rewrite jshottan's.
9. **elizabeth-palmer-97820997:**
   - "Coaches on Everfit ask the platform to record more for their clients." → invented; replace it with a fact from the bullet.
   - "with the API returning it linked to the client profile" → "Everfit links it through the scan ID".
10. **Pilot:**
    - maureen-key ≈ daniellepeckskamp ≈ nicholasjrobinson → vary.
    - maureen-key: swap the pilot for a coaching value point and add an easy out. daniellepeckskamp: add an easy out.
    - nicholasjrobinson: move or drop "There is no integration fee." after the pilot.
11. **"comparable from one check-in to the next"** (tanysha-smith, lisa-privitera, megan-johns, elizabeth-palmer) → own words in at least 2.
12. **Closers** "Open to a call? / Worth a call? Or point me to whoever runs the member app's progress experience." (amartanna, megan-johns, danaehirsch) → vary 2.
13. **Smaller items:**
    - shayne-k-jessop: soften "the progress it sees is training metrics"; trim Message 2 to 2 points.
    - becca-valente: "keeps the capture the same" → drop; "personalised" → "personalized".
    - longdnguyen: Message 2 repeats Message 1.
    - jrafferty: generic opener "3DLOOK built FitXpress as a body scan that runs inside a company's own app." → open on Centr.
    - maureen-key ≈ jenna-moore: vary one question.

### mixed-3 (small apps, Ergatta + Interactive Strength)
1. **jessventicinque:** "Fitbod is moving toward helping members understand their data and interpret their progress inside the app." → paraphrase away from the CEO's quote.
2. **matt-lehrer-67664014:**
   - Drop "between sessions" from "Capture happens on the member's phone between sessions…".
   - "FitXpress shows what the block changed" → non-causal wording.
3. **trent-ward-12b992b2:** drop "and no club visit".
4. **Ergatta/IS family:** rewrite the product sentence in at least 4 of 8 (luanaperez, tom-aulet, an-li, bentbartlett). Vary "Ergatta's game-based programs" (alessandra-gotbaum vs tom-aulet).
5. **alisa-aguirre:** Message 1 product sentence = luanaperez's, and the Message 2 "concrete answer" line ≈ hers → rewrite both of Alisa's.
6. **"The page for this use case:"** on all 17 URLs → drop the label or vary it. Fix first in the Ergatta/IS ×4, Caliber ×2, Lose It! ×2 and Future ×2.
7. **deepakmm and rkekelis:** capture-match questions contradict their Message 2 → re-ask about the screens.
8. **Pilot read as free:** separate "There is no integration fee." from the pilot in keith-kraker (same paragraph), jmcluff and js531.
9. **corydavisprofile:** Message 2 first sentence = justin-fauci's → change one.
10. **Pilot twins:** trent-ward ≈ js531; jmcluff ≈ jake-grundstein → vary.
11. **greg-nuckols-92545595:** repeatability in the leadership lane → re-lane to science (as the Account facts intend) or drop. Trim Message 2 to 2 points.
12. **andrewzey:** drop ", which makes the change between two weekly reviews comparable" after the verbatim sentence.
13. **Stubs:** "For scale: 112,100…" ×3 and "3DLOOK has worked with 100+ clients. There is no integration fee." ×3 → tie each to the value line, or drop.
14. **jakequan:** "Workout reports describe the work done. The body change it is for needs its own measurement." ≈ ryan-mott's line and implies Future lacks body data → rewrite.
15. **Smaller items:**
    - prasanna: "standardised" → "standardized". bentbartlett: "personalised" → "personalized".
    - prasanna and ryan-mott: Message 2 repeats Message 1's processing status.
    - alessandra-gotbaum: Message 2 repeats pose guidance and is off the leadership targets.
    - Caliber "At 3DLOOK we built FitXpress" ×2 → vary chris-muir's. Trim chris-muir's Message 2 to 2 points.
    - annakatedavis: do not start a sentence with "2".
    - corydavisprofile: drop the integrations easy out.
    - john-ybarra: "the record returns" → "the scan returns".
    - jmcluff: tie conversion to 3D tools in the paid plan.
    - ryan-mott: lane `data` is not a card lane.

### For the coordinator / script owner (not the agent's fault)
- Card question target "what a white-label capture would have to match in the app's design" conflicts with "capture layer stays fixed". Rewrite the target to ask about the surrounding screens.
- Gate gap 1: `check-messages` passes a Message 1 with no product or company name. Add a check for FitXpress or 3DLOOK in Message 1.
- Gate gap 2: the gate does not catch identical full Message 2 bodies across companies inside one batch (Eric = Brandon, Heidi = Danaé). Add a check for that.
- Gate gap 3: "card wording as copy" misses the strength-program pain sentence, which appears 3 times verbatim.
- The per-person file format has no `product:` frontmatter (CLAUDE.md §10.4).

## Coordinator review

(filled in by the coordinator)
