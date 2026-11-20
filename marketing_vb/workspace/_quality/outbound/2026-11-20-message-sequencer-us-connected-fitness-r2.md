---
qc_date: 2026-11-20
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-11-19-us-connected-fitness/messages/ (109 pairs after fix round 1; scored from scratchpad messages-dump-r1.txt + _check.json, gate 0 hard / 28 soft)
track: outbound
artifact_type: messages
product: fitxpress
round: 2
total_score: 14/20
status: marginal
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Line-edit pass sent to the four batch agents (P1 + cheap P2). Coordinator rulings: membership-lane pilots stay (mirelacialai, daniellepeckskamp); buyers (founders, CEOs, CPOs, co-owners, P1 owners) get no easy out, per the card's 'easy out only for non-buyers' (16 in mixed-3). Gate gaps (M1 cross-company twins, M2 repeating M1, 'described on this page:' label) proposed to Vadim, not applied."
---

# QC Report: message-sequencer, round 2 (US connected fitness, 109 pairs)

**Artifact:** all 109 pairs after the fix round, read company by company. Scored against `card-messages.md`, `_profiles-*.md` and the four `_fix-*.md` briefs.

**Rule applied:** Vadim's change of 2026-11-20. At one company, the same pain, argument, question topic, Message 2 value point or easy-out target may repeat when it fits the person. The "about a fifth" ratio is withdrawn. Scored here: near-verbatim twin sentences between colleagues at one company, copy that does not fit the person, and the other checks. Findings dropped under this rule are listed in their own section below.

**Total: 14/20, marginal (round 1: 11/20). No regeneration needed.** The round fixed the serious problems:
- every Message 1 now names FitXpress or 3DLOOK (109/109);
- the data claims and "no club visit" are gone;
- the capture-match questions are gone;
- the repeatability sentence now appears only in allowed lanes (15/15);
- no "no integration fee" line sits directly after a pilot;
- all "The page for this use case:" labels are gone.

What remains:
- about 8 pairs with wrong content (claims, or Message 2 repeating Message 1);
- about 10 same-company wording twins, mostly in the product sentence.

**The campaign is sendable after one line-edit pass of about 18 lines** (P1 list at the end).

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

The rule change removed about 9 findings but no category score. The scores rest on the content defects, the wording twins, the Message 2 repeats and the missing summaries, and all of those remain.

## Dropped under the 2026-11-20 rule change

These were in the first version of this report. They rested only on shared topics, shared product nouns or the ratio rule, so they are no longer scored and are out of the fix list:
1. Tonal: the shared "members ask about results" argument in amartanna, josephrodonis and tanysha-smith. It is a topic shared across the three, and the Use line assigns it.
2. Peloton:
   - the colon-form count (8/18) and "Peloton's own screens" ×3, which are shape and a product phrase;
   - meghiggins21 in the "record the work done" trio. Her sentence differs. eugenekwak ≈ yasminkothari stays because their clause is near-verbatim.
3. Centr: "FitXpress from 3DLOOK" ×3, which is a product name form. Also nicholasjrobinson ≈ productobsessedlaura, where only the product-noun tail matches and the verbs differ.
4. MyFitnessPal: the colon-frame count (6/8), and the shared question topic of oaktownolivia and vptaylo.
5. Ergatta + IS: the identical payload nouns in 8/8, and luanaperez ≈ tom-aulet, where only the noun tail matches.
6. Trainerize: the doug-reeder / laurietaylorkemp conditional ("If Trainerize's …"), which is the same shape in different words.
7. Repeated easy-out targets ("progress experience" and the like).
8. Moved from P1 to P2: the Tonal and Ergatta/IS closers. The shared part is the easy-out idiom; only amartanna ≈ josephrodonis is near-verbatim.

## Vadim's rules and hard checks (held)

- **No $:** 0 in 109 pairs.
- **"There is no integration fee.":** 9 uses, all in Message 2, once per pair, as its own sentence, placed with the SDK point and never directly after a pilot. The pairs are nickcaldwell, joeli-spencer, ericreimers, tom-aulet, longdnguyen, jmcluff, bentbartlett, js531 and keith-kraker.
- **Page URL:** 58 of 109 Message 2s and none in Message 1. Every company is at about half: Peloton 9/18, Trainerize 6/11, BODi 6/11, MyFitnessPal 5/8, Tonal 4/7, Echelon 3/6, iFIT 3/5, Ergatta+IS 4/8, Centr 3/5, Everfit 3/5, Lose It! 2/4, Caliber 2/4, and the small accounts 1 of 2 or 3.
- **Calendar line** is last in all 109.
- **Numbers** all come from the list. The 100+ line is always "3DLOOK has worked with 100+ clients". The repeatability sentence is verbatim, with nothing added, and only in the product, coaching or science lanes.
- **Wording:** no em dash, "plus", "so" or British spelling. Nothing about clubs. "Between sessions" appears only where the facts allow it (lisa-privitera, gabe-madonna).
- **Account facts Never lines:** no breach found.

## What was wrong (specific)

### A. Adherence: 3/5

- **Message 2 repeats Message 1:**
  - **New:**
    - bethraewendt: Message 1 has "with pose and framing guidance"; Message 2 says "The 2 photos come with pose and framing guidance during capture".
    - howens: Message 1 has "a timestamped record with its processing status"; Message 2 says "The API returns each record with its processing status beside the timestamp".
    - john-santo-096310149: Message 2 "The SDK and the API together are the recommended setup, and the screens before and after the capture carry Echelon's wording and brand. It returns 80+ body measurements…" restates Message 1's SDK, fixed-capture and screens question.
  - **Unchanged:**
    - zekebrustkern: processing status in both messages.
    - thekellycard (P1): "A client finishes the check-in inside the trainer's branded app. The scan returns 80+ body measurements…" restates Message 1.
- **Fix-brief rule 10 ("a fix must not create a new shared phrase")** was broken in about 12 places. The same-company ones are listed under E.
- **howens still has two pain lines:** "A strength program can change the waist while the weight stays put…" and "A program progress screen in the BODi app shows the work done, and the body change is the half with no place on it."
- **Summaries:**
  - `_summary-*.md` is still missing for peloton, mixed-2 and mixed-3.
  - `_summary-mixed-1.md` still says "product 20".

### B. Factual accuracy: 4/5

- **Pain stated about the company in a way that contradicts its Account facts.** BODi members type measurements into the app, and Trainerize tracks body stats, tape measurements and body fat.
  - ashlei-mitchell-0a302a220: "BODi's progress screens read from program data, and most of that is the work members did." and "…the body change behind them is missing from the data."
  - howens: "A program progress screen in the BODi app shows the work done, and the body change is the half with no place on it."
  - doug-reeder-3247511: "Workout adherence and habits track the work done, and the body change it is for stays outside the data."
  - Lighter cases:
    - longdnguyen: "Nothing in that set is a measurement of the body itself." Weight is in that set.
    - lisa-privitera: "the trainer's view of progress comes from what the member reports". This is not in the Echelon bullet.
- **Consistency claims beyond the repeatability sentence:**
  - bethraewendt Message 1: "…back in one timestamped record, the same way each time."
  - bethraewendt Message 2: "…which keeps each tester session set up the same way."
  - matt-lehrer-67664014 Message 2: "…the same timestamped record, comparable from one check-in to the next." This sits directly before the repeatability sentence and is the card's Message 2 target text.
- **Tracking or ownership nuance:**
  - matt-lehrer: "FitXpress can record where the body stands at each check-in". This is close to "FitXpress tracks"; make the body scan the subject.
  - mikefarrell: "…coming back through the API for BODi to keep." This is mild, because 3DLOOK also stores measurements.
- **Number wording drifts from the list form:**
  - justin-fauci: "We ran 112,100 scans in 2025 across all 3DLOOK customers."
  - jenny-parker-28b93516: "Across all 3DLOOK customers, there were 112,100 scans in 2025."
  - The figure itself is right.
- **Unsupported:** js531: "RP Strength's apps are paid products". This is not in the RP bullet. It is low risk.
- **Sourcing:** n/a. No compliance line is needed for this ICP, and none is used.

### C. Brand & tone: 2/3

- **Label before a link (new form, missed by the gate):** stephanie-saunders writes "The setup is described on this page:" directly above the URL.
- **Sentences opening with a digit** (this moved from annakatedavis to three new places):
  - doug-reeder: "2 guided photos on the client's phone return…"
  - amartanna-cpa-ca: "2 photos from the member's phone go to the API…"
  - nicholasjrobinson: "2 photos from a member's phone are enough…"
- **Stiff or garbled phrasing:**
  - **Stock pain wording:** "the waist and the fat and lean mass move/shift" ×6: luanaperez, alisa-aguirre, js531, keith-kraker, gabe-madonna, joncilley.
  - **howens:** "return a timestamped record with its processing status, including 80+ body measurements" reads as if the status contains the measurements.
  - **prasanna-swaminathan:** "FitXpress comes back through the API as one timestamped record" makes the product the record. His form pain also sits between "in-game metrics" and "Next to those metrics", which breaks the reference.
  - **luanaperez:** "3DLOOK's FitXpress would allow the app to add a body scan in which 2 guided photos yield…"
  - **megan-johns:** "inside the Centr app: from 2 photos taken in the Centr app".
  - **tanysha-smith:** "adds a body scan to the Tonal app in two steps".
  - **finn-hegarty:** "a record that carries the trainer's brand", which follows "under the trainer's brand" in the same Message 1.
  - **thekellycard:** "A call would allow me to show…" (unchanged from round 1).
  - **billy-hulbert:** "the partner's own app" (unchanged from round 1).
- **No banned words, no hype, peer register held.**

### D. Format & structure: 2/3

- Three of four `_summary` files are missing, and the fourth has a wrong count (see A).
- **Message 2 still carries 3 points:**
  - karl-mahrenholz: setup, capture fixed with own screens, and processing status.
  - greg-nuckols-92545595: derivation, NDA and repeatability.
- **No Account-facts company line in Message 1** (title or headline restatement only): nicholasrwilley, mikefarrell, danaehirsch, megan-johns-72b40818a.
- **Gate:** 0 hard. All 28 soft notes are card-wording repeats, and they are mostly cross-company. The ones that matter are listed under E.

### E. Output quality: 3/4

The hooks, questions and Message 2 value points are person-specific at almost every company. Under the new rule, what still matters is the near-verbatim sentences between colleagues.

**Question (2): mail merge or acceptable product wording?**
- **"80+ body measurements and fat and lean mass estimates"** (72 occurrences) and **"one timestamped record"** (49 of 109 Message 1s): acceptable product wording. They are the guardrail forms of the outputs and are not defects.
- **What reads as a mail merge when a pair is forwarded is the whole sentence** with the same lead-in, the same verb and the same order: "[The/A] member takes 2 (guided) photos on their own phone, and [the API returns] one timestamped record with 80+ body measurements…". A shared noun tail under a different verb or frame is fine.
- **Fix:** keep the nouns, and per twin change the lead-in and verb to what this person sees (the girths a coach reads, or where the record lands: Tia, the weekly plan, the Weight Log).

**Same-company wording twins (to fix):**
- **Tonal (7).**
  - **Pain:**
    - maureen-key: "home photos and tape differ in pose and light between check-ins"
    - josephrodonis: "Home photos and tape differ in pose and light from one check-in to the next"
  - **Product sentence:**
    - jshottan: "After 2 guided photos on the member's phone, the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates."
    - maureen-key: "The API returns it as one timestamped record with 80+ body measurements and fat and lean mass estimates, after the member's 2 guided photos in the Tonal app."
    - tanysha-smith: "Two guided photos in the Tonal app are all the member provides, and the API returns one timestamped record with 80+ body measurements."
    - josephrodonis: "…take 2 guided photos on their own phone with FitXpress, and one timestamped record with 80+ body measurements and fat and lean mass estimates comes back through the API."
  - maureen-key and josephrodonis share both the pain and the product clause, so that pair reads as one template.
- **iFIT (5):**
  - daniellepeckskamp: "The member takes 2 photos on their own phone, and one timestamped record with 80+ body measurements comes back through the API."
  - sarah-miles-product: "A member takes 2 photos on their own phone, and the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates."
  - danaehirsch: "A member shoots 2 photos on a phone, and the API sends back one timestamped record with 80+ body measurements."
- **Centr (5):**
  - andrew-sugerman: "…Centr's members take 2 photos on their own phone and the API returns one timestamped record with 80+ body measurements…"
  - megan-johns: "…from 2 photos taken in the Centr app, the API returns one timestamped record with 80+ body measurements and fat and lean mass estimates."
- **BODi (11):**
  - marietta-p: "…has the member take 2 guided photos, front and side, on their own phone, and the platform gets back 80+ body measurements and fat and lean mass estimates."
  - stephanie-saunders: "A member takes 2 guided photos, front and side, on their own phone inside the BODi app, and the program gets back 80+ body measurements and fat and lean mass estimates…"
- **MyFitnessPal (8):**
  - ruth-sylvia: "FitXpress adds a body scan to that view: 2 guided photos from the member's phone return 80+ body measurements…, under MyFitnessPal's own brand."
  - christina-to: "FitXpress is a body scan for apps: 2 guided photos from the member's phone return 80+ body measurements and a timestamped record, under the app's own brand."
  - meganstaggoverton is close: "2 guided photos, front and side, from the member's phone return 80+ body measurements…"
- **Trainerize (11):**
  - ericreimers: "…: 2 guided photos on the client's phone, 80+ body measurements and a timestamped record back through the API…"
  - keegan-dowling: "…: 2 guided photos, 80+ body measurements, one timestamped record per scan."
  - These two are both partnership people.
  - doug-reeder: "2 guided photos on the client's phone return 80+ body measurements…" ≈ kendall-wilson: "2 guided photos from the client's phone return 80+ body measurements and fat and lean mass estimates…"
- **Echelon (6):**
  - heidi-jones-ny: "The member takes 2 photos on their own phone, and one timestamped record with 80+ body measurements comes back through the API."
  - john-santo: "The member takes 2 guided photos on their own phone, and Echelon gets one timestamped record with 80+ body measurements and body composition estimates."
- **Peloton (18):**
  - eugenekwak: "A check-in built on training metrics records the work done, and the body change it is for stays unmeasured."
  - yasminkothari: "Lifts record the work done, and the body change it is for needs its own record."
  - Minor:
    - theodorelui ≈ kavitajv: "…and what returns to the [company/platform] depends on that app."
    - laurarivera-uxresearch ≈ lindsay-pontello: "…tell me who and I will start there." / "…just say who and I will go there."
- **Everfit (5), optional:**
  - longdnguyen: "A client takes 2 photos on their own phone, and one timestamped record with 80+ body measurements comes back through the API…"
  - bogatzproductmanager: "The client takes 2 photos on their own phone, and the SDK and API return one timestamped record with 80+ body measurements…"
- **Clean:** Ergatta + IS, Lose It!, Caliber, MacroFactor, Future, Fitbod, RP, Ladder, Carbon, Hydrow, Trainwell, Jefit.

**Next stock forms created by the fix round.** These are mostly cross-company, so their visibility for sending is low. The gate's cross-company check covers Message 2 only, so it misses all the Message 1 ones.

1. **Exact cross-company Message 1 sentences:**
   - heidi-jones-ny = daniellepeckskamp: "The member takes 2 photos on their own phone, and one timestamped record with 80+ body measurements comes back through the API." longdnguyen has the same sentence with "A client".
   - heidi-jones-ny = nicholasrwilley: "A separate scanning app puts the member and the result under another brand, and what comes back to the platform depends on that app."
   - an-li-5662b365 = jakequan: "A progress photo shows visible change and gives the next check-in nothing measured to compare."
   - trent-ward = andrewzey: "A weigh-in gives one total and says little about where the body changed."
   - prasanna = jake-grundstein: "A check-in form holds only what the member enters."
   - megan-johns = justin-fauci: "A check-in form holds only what the member types in."
   - josephrodonis = robert-benjamin: "Home photos and tape differ in pose and light from one check-in to the next."
   - taylor-smyrnos = bansal-nitin: "Tape and photos taken at home differ in pose and light between check-ins."
   - zekebrustkern = ashlei-mitchell, opener: "FitXpress returns one timestamped record per scan through the API:"
2. **Pain wording converged on two card targets:**
   - "home photos and tape differ in pose and light" ×14.
   - "body weight can hold while the waist and the fat and lean mass move" ×5, all in mixed-3.
3. **The new card question target pasted ×7.**
   - The frame "Around a capture that stays fixed, which screens would [X] want in its own [brand/look]?" is identical in howens, doug-reeder and karl-mahrenholz. Close variants: joncilley, john-santo, deepakmm, rkekelis.
   - In 5 of them (joncilley, doug-reeder, karl, howens, deepakmm), Message 1 never explains "fixed capture" before asking, so a cold reader meets internal jargon. That is a fit problem, not a ratio problem.
4. **Message 2 "same record + a second figure":**
   - tanysha-smith: "…a later scan gives them a second figure to set beside the first."
   - megan-johns: "…a second scan later gives them a figure to set beside the first."
   - elizabeth-palmer: "A second scan gives a coach a figure to set against the first."
5. **Speed sentence:** "[The scan/FitXpress/It] returns 80+ body measurements, under 45 seconds from the photos to structured results." ×14, one per company. It is always fused to the 80+ clause, so 14 Message 2s restate Message 1's number. cole-shipley's whole Message 2 value is this sentence.
6. **Pilot skeleton:** "A pilot could compare [metric] between a cohort that scans at [X] and a comparable cohort on the usual flow, against success criteria agreed before it starts" ×6, cross-company. Acceptable.
7. **Stub Message 2s:**
   - andrewzey (P1): the repeatability sentence only.
   - barbarathornethomsen: "There were 112,100 scans in 2025 across all 3DLOOK customers." only.
   - alessandra-gotbaum: "The scan needs only the member's phone. 3DLOOK has worked with 100+ clients."
   - jenny-parker and justin-fauci: 112,100 tacked onto an unrelated sentence.

**Question (3), non-buyers and fit:**
- **CX heads** (oaktownolivia, amartanna, megan-johns, luanaperez, alisa-aguirre): role-true, no pilot, easy outs present.
- **Pool D Peloton:** all have easy outs, and no pilot pitches.
- **maureen-key and daniellepeckskamp:** fixed.
- **Misfits left:**
  - tanysha-smith (Head Coach): easy out "send me to the owner of onboarding".
  - The Head Coaches josephrodonis and tanysha-smith still get API mechanics ("the API returns / comes back through the API").
  - prasanna (CTO): easy out "whoever owns integrations on the app side", which is likely himself.
  - billy-hulbert (commerce partnerships): an SDK spec in Message 2.
- **mirelacialai and daniellepeckskamp** (membership lane, pool E) get pilot pitches. The lane allows this, but fix rule 7 says subscription people get no pilot pitch; see P3.

## Round-1 fix list: status

Of 55 items: 36 fixed, 12 fixed but with a new problem, 7 partial.

**Peloton**
1. Product named: FIXED (18/18). Colon form and "Peloton's own screens" are no longer scored.
2. tworetzky grammar: FIXED, NEW PROBLEM. The new line is the card pain near-verbatim: "A weigh-in gives one total, often self-reported, and where the body changed stays unknown."
3. bethraewendt question: FIXED, NEW PROBLEM. Message 2 repeats the pose guidance, and the consistency claims are new.
4. decide/pilot questions: FIXED.
5. theodorelui, sarah-rodenberg, joncilley claims: FIXED.
6. joncilley question: FIXED. "fixed capture" is unexplained (fit, P2).
7. sarah = brad Message 2: FIXED.
8. Fee, processing status, no hardware: FIXED.
9. joeli-spencer company line: FIXED.
10. Closers: FIXED. Minor residue: laurarivera ≈ lindsay-pontello.
11. mirelacialai plan wording: FIXED.
12. personalized / "growing": FIXED.

**mixed-1**
1. ashlei named: FIXED, NEW PROBLEM. Her pain contradicts BODi's typed-measurement fact, and her opener equals zekebrustkern's (cross-company).
2. elizabeth-gray / howens strength sentence: FIXED. howens still has two pain lines: PARTIAL.
3. brandoncowley Message 2: FIXED.
4. Capture-match questions: FIXED, NEW PROBLEM. howens, doug-reeder and karl now share an identical frame, and "fixed capture" is unexplained.
5. "The scale so far" ×3: FIXED. jenny-parker's 112,100 is still a stub (P2).
6. Trainerize "what the client enters": FIXED.
7. finn-hegarty pain: FIXED.
8. mikefarrell and vjmuthuraman: FIXED.
9. BODi Message 2 "capture fixed" ×3: FIXED.
10. kendall-wilson and marietta-p questions: FIXED.
11. ruth-sylvia Message 2: FIXED.
12. vptaylo: FIXED. The shared question topic is no longer scored.
13. jenniferannpelton Message 2: FIXED.
14. doug-reeder and laurietaylorkemp remit: FIXED.
15. Smaller items: PARTIAL. christina-to still says "under the app's own brand", and the summary count is not fixed. The rest is fixed.

**mixed-2**
1. Tonal "point to": FIXED. tanysha's product sentence is still ≈ josephrodonis's: PARTIAL.
2. iFIT product sentence: FIXED, NEW PROBLEM. danaehirsch, daniellepeckskamp and sarah-miles now share one sentence.
3. productobsessedlaura: PARTIAL. "so", the company line and the product sentence are fixed. The question is still the card target with "body" added: "Would a body scan belong at onboarding or at the first check-in for Centr members?" (P2).
4. danaehirsch Message 2 and "the iFIT app": FIXED.
5. heidi-jones-ny "end to end": FIXED, NEW PROBLEM. Her Message 1 sentences equal daniellepeckskamp's and nicholasrwilley's.
6. jondwang build vs integrate: FIXED.
7. john-santo question: FIXED, NEW PROBLEM. His Message 2 now repeats his Message 1.
8. Card pains: jshottan and kevin/joe FIXED. lisa-privitera ≈ longdnguyen is still near-verbatim across companies: PARTIAL (P2).
9. elizabeth-palmer: FIXED.
10. Pilot items: FIXED.
11. "comparable from one check-in to the next": FIXED, NEW PROBLEM. "a second figure to set beside the first" is now in tanysha, megan-johns and elizabeth-palmer.
12. Closers: FIXED. The Tonal "A call would show …, or send me to …" frame is P2.
13. Smaller items: FIXED.

**mixed-3**
1. jessventicinque quote: FIXED.
2. matt-lehrer: FIXED. Residue: "comparable from one check-in to the next".
3. trent-ward "no club visit": FIXED.
4. Ergatta/IS product sentence: FIXED. The shared payload nouns are not scored; luanaperez's sentence is awkward (C).
5. alisa-aguirre: FIXED. Her pain now ≈ luanaperez's across companies (P2).
6. "The page for this use case:": FIXED, NEW PROBLEM. A new label appears at stephanie-saunders.
7. deepakmm and rkekelis questions: FIXED.
8. Fee after pilot: FIXED.
9. corydavisprofile = justin-fauci: FIXED.
10. Pilot twins: FIXED, NEW PROBLEM. A cross-company skeleton appears ×6 (acceptable).
11. greg-nuckols lane: FIXED. His Message 2 still has 3 points: PARTIAL.
12. andrewzey addition: FIXED, NEW PROBLEM. His Message 2 is now one stub sentence.
13. Stubs: PARTIAL. justin-fauci's 112,100 is still a stub, in "We ran…" wording.
14. jakequan: FIXED, NEW PROBLEM. His pain equals an-li's exactly.
15. Smaller items: FIXED. New problems: alessandra-gotbaum's Message 2 is two stubs, and digit-first sentences moved to three other pairs.

## Per-company verdict

| Company | n | Verdict |
|---|---|---|
| BODi | 11 | 4 edits: ashlei pain, howens (pain + Message 2), marietta/stephanie twin, stephanie label |
| Trainerize | 11 | 4 edits: doug pain, zeke Message 2, kelly Message 2, eric/keegan or doug/kendall twin |
| Tonal | 7 | 3 edits: maureen/joe pain, one product sentence of maureen/jshottan and one of joe/tanysha, tanysha easy out |
| Peloton | 18 | 2 edits: beth (Message 2 + claims), eugene/yasmin twin; optional: cole and barbara stub Message 2s |
| Echelon | 6 | 2 edits: john-santo Message 2, heidi product sentence |
| iFIT | 5 | 1-2 edits: danielle (and danae or sarah-miles) |
| MyFitnessPal | 8 | 2 edits: ruth/christina twin, christina brand |
| Centr | 5 | 1 edit: andrew/megan twin |
| Ergatta + IS | 8 | Sendable. Optional: prasanna easy out, luana sentence, alessandra Message 2 |
| Everfit | 5 | Sendable. Optional: longdnguyen ≈ bogatz |
| Lose It!, Caliber, MacroFactor, Future, Fitbod, RP, Ladder, Carbon, Hydrow, Trainwell, Jefit | 30 | Sendable. Optional: andrewzey Message 2, matt-lehrer Message 2, justin 112,100 |

## Top 3 issues (priority for improver)

1. **Content defects in about 8 pairs** (B):
   - pains that contradict the Account facts: ashlei-mitchell, howens, doug-reeder;
   - bethraewendt's consistency claims;
   - Message 2 repeating Message 1: bethraewendt, howens, zekebrustkern, john-santo, thekellycard.
2. **Near-verbatim product sentences between colleagues**, in about 10 pairs at Tonal, iFIT, Centr, BODi, MyFitnessPal, Trainerize and Echelon. The fix round changed the frame of the sentence but kept its wording ("[member] takes 2 photos on their own phone, and the API returns one timestamped record with 80+ body measurements…").
3. **Fit:**
   - "fixed capture" is asked about cold in 5 Message 1s;
   - tanysha's easy out goes to onboarding;
   - the Head Coaches get API mechanics;
   - prasanna is pointed to himself;
   - several Message 2s are stubs (andrewzey, barbarathornethomsen, alessandra-gotbaum, cole-shipley).

## Prioritized fix list

**P1: before sending (one line-edit pass, about 18 lines):**
1. **ashlei-mitchell-0a302a220:** replace "BODi's progress screens read from program data, and most of that is the work members did." and "the body change behind them is missing from the data" with a general method pain. BODi members type measurements, so do not deny body data.
2. **howens:** keep one pain line and drop "A program progress screen in the BODi app shows the work done, and the body change is the half with no place on it." Fix "a timestamped record with its processing status, including 80+ body measurements". Give Message 2 a value point other than processing status (scan ID, or waist/hip on the progress screen).
3. **doug-reeder-3247511:** replace "Workout adherence and habits track the work done, and the body change it is for stays outside the data." Trainerize tracks body stats and tape.
4. **bethraewendt:** drop ", the same way each time" (Message 1). Replace Message 2 "The 2 photos come with pose and framing guidance during capture, which keeps each tester session set up the same way." with a value point Message 1 did not use.
5. **zekebrustkern, thekellycard, john-santo-096310149 Message 2s:** each gets one value point that its Message 1 did not use.
   - zeke: scan ID to client profile.
   - kelly: the measurements a trainer would see, or the pilot.
   - john-santo: scan ID, or waist/hip next to personal bests.
   - Also change kelly's "A call would allow me to show…".
6. **Tonal:**
   - Re-word the pain of maureen-key or josephrodonis (same home-tape sentence).
   - Rewrite one product sentence of maureen-key / jshottan and one of josephrodonis / tanysha-smith.
   - tanysha-smith's easy out: the coaching programs or the progress experience, not onboarding.
7. **iFIT:** rewrite daniellepeckskamp's product sentence. It equals heidi-jones-ny's and ≈ sarah-miles's. Optionally rewrite danaehirsch's.
8. **Echelon:** rewrite heidi-jones-ny's or john-santo's product sentence ("The member takes 2 (guided) photos on their own phone, and …").
9. **Centr:** rewrite the product sentence of andrew-sugerman or megan-johns.
10. **BODi:**
    - Rewrite the product sentence of marietta-p or stephanie-saunders.
    - Drop "The setup is described on this page:" (stephanie-saunders).
11. **MyFitnessPal:**
    - Rewrite the product sentence of ruth-sylvia or christina-to.
    - christina-to: "under the app's own brand" → "under MyFitnessPal's brand".
12. **Trainerize:** rewrite one of ericreimers / keegan-dowling. Optionally rewrite one of doug-reeder / kendall-wilson.
13. **Peloton:** remove "the body change it is for" from eugenekwak or yasminkothari.

**P2: cheap, same pass if time allows:**
- **Unexplained "fixed capture" in the question:** joncilley, doug-reeder, karl-mahrenholz, howens, deepakmm. Add a few words of setup in Message 1, or ask about "the onboarding and results screens around the capture".
- **Stub Message 2s:**
  - cole-shipley: speed line only.
  - barbarathornethomsen: 112,100 only.
  - andrewzey: repeatability only. Tie it to the weekly review.
  - alessandra-gotbaum: two stubs.
  - justin-fauci: "We ran 112,100…" → the listed form, or drop.
- **Exact cross-company Message 1 twins** (see "Next stock forms" 1). Low visibility.
- **Misfits:** prasanna's easy out; the Head Coaches' API wording; billy-hulbert's SDK-spec Message 2.
- **Closers:** amartanna ≈ josephrodonis ("A call would show …, or send me to whoever runs …").
- **Digit-first sentences:** doug-reeder, amartanna-cpa-ca, nicholasjrobinson.
- **matt-lehrer:**
  - drop ", comparable from one check-in to the next";
  - "FitXpress can record where the body stands" → "a body scan records where the body stands".
- **Garbled lines:** luanaperez, megan-johns, tanysha-smith "in two steps", prasanna-swaminathan, finn-hegarty (quoted under C).
- **Trim to 2 points:** karl-mahrenholz and greg-nuckols Message 2s.
- **productobsessedlaura:** her question is still the card target.

**P3: coordinator, card and gate (not the agent's fault):**
- **Gate gaps:**
  - Identical Message 1 sentences across companies are not checked.
  - Message 2 repeating Message 1 is not checked (beth, howens, zeke, john-santo, kelly).
  - The label check misses "The setup is described on this page:".
- **Card seeds:**
  - The Peloton Use line carries "(the work done, not the body change it is for)", which seeds the eugenekwak / yasminkothari twin.
  - The new product question target is pasted ×7, and "fixed capture" reads as jargon to a cold reader.
  - The speed fact is always fused to "returns 80+ body measurements," and so repeats Message 1's number.
- **Rule conflict:** fix-brief rule 7 ("subscription marketing: no pilot pitch") versus the membership lane's Message 2 targets, for mirelacialai and daniellepeckskamp. Decide which wins. Mirela has no pointer easy out.
- **Easy out for buyers:** 54 Message 2s say "point/send me to whoever …", including P1 CPOs and founder-CEOs (chris-muir, andrewzey, jessventicinque, thosniles, tom-aulet, trent-ward). Decide whether buyers get an easy out.
- **Summaries:** add `_summary-peloton/-mixed-2/-mixed-3.md`, and fix "product 20" in `_summary-mixed-1.md`.

## Coordinator review

(filled in by the coordinator)
