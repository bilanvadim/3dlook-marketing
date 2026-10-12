# Fix list, round 3 — `anytime-fitness-australia` — 2026-10-12

Second QC: 13/20 (`workspace/_quality/outbound/2026-10-12-message-sequencer-au-sport-fitness.md`). The round-1 and round-2 fixes stand. Edit at sentence level: only the people and sentences below.

Read the card's "Coordinator decisions 2026-10-12" again: **rules 20-24 are new** (fixed proof lines stand alone with no label; the speed phrase only where speed is the point and never right after an output noun; "the brand decides where it is shown" only at workplace programmes; the card's own words are not copy; one wording per person for each M2 part, no bare "Or" opening an easy out, two people at one club get different easy-out targets).

Swaps to avoid (the second QC found these after round 2): replacing "ran" with a label; replacing one stock speed sentence with another; replacing one closer sentence with a single new one that everybody then gets; copying the card's rule wording ("member side", "a plain yes") into the copy. When you drop a speed phrase or a proof line, the pair must still cite a number (80+ body measurements is enough).

"Thin M1s" and "product-lane card question" items: give that person a line only they could get (their club, role or a brand fact) and a question of their own, not the card's lane question.

## From the second QC (verbatim)

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

## From the coordinator's scan (new checks for rules 11 and 20-24 included)

- COMPANY Anytime Fitness Australia: sentence shared by 3: "3dlook has worked with 100+ clients."; georgieisabellajones
- COMPANY Anytime Fitness Australia: sentence shared by 3: "3dlook has worked with 100+ clients."; mark-grey-014635154
- COMPANY Anytime Fitness Australia: sentence shared by 3: "3dlook has worked with 100+ clients."; richard-peil-b8a35513b
- RULE  bare Or sentence (rule 24): mark-grey-014635154 M2
- RULE  brand-decides note (rule 22): aaron-o-meara-629130307 M1
- RULE  brand-decides note (rule 22): georgieisabellajones M2
- RULE  card wording as copy (rule 23): jordan-smith-9b116082 M2
- RULE  card wording as copy (rule 23): leah-libunao-8007751a5 M2
- RULE  card wording as copy (rule 23): richard-peil-b8a35513b M1
- RULE  card wording as copy (rule 23): winona-dufrier-277a43230 M1
- RULE  label before fixed line (rule 20): marcello-jimenez-26920a63 M2
- RULE  plus connector: clancy-izzard-11318031b M1
- RULE  speed after output noun (rule 21): tom-teasdale-065853124 M1

## When you are done

Re-run `python3 /tmp/claude-1006/-home-vadim-prod/199d83ab-a920-4bc3-8636-0ed06f0c7b1f/scratchpad/scan.py <full path of the campaign dir> --only anytime-fitness-australia` until the block for your batch is "none" (or every remaining line is explained in the summary), then `python3 scripts/outbound_pack.py split-messages --campaign 2026-10-11-au-sport-fitness --in messages/_batch-anytime-fitness-australia.md` until exit 0. Append a "Round 3" note to the summary (people touched, what changed; correct any count in the summary that is now wrong) and stop.
