# Fix list, round 3 — `fernwood-fitness-1`, `fernwood-fitness-2` — 2026-10-12

Second QC: 13/20 (`workspace/_quality/outbound/2026-10-12-message-sequencer-au-sport-fitness.md`). The round-1 and round-2 fixes stand. Edit at sentence level: only the people and sentences below.

Read the card's "Coordinator decisions 2026-10-12" again: **rules 20-24 are new** (fixed proof lines stand alone with no label; the speed phrase only where speed is the point and never right after an output noun; "the brand decides where it is shown" only at workplace programmes; the card's own words are not copy; one wording per person for each M2 part, no bare "Or" opening an easy out, two people at one club get different easy-out targets).

Swaps to avoid (the second QC found these after round 2): replacing "ran" with a label; replacing one stock speed sentence with another; replacing one closer sentence with a single new one that everybody then gets; copying the card's rule wording ("member side", "a plain yes") into the copy. When you drop a speed phrase or a proof line, the pair must still cite a number (80+ body measurements is enough).

"Thin M1s" and "product-lane card question" items: give that person a line only they could get (their club, role or a brand fact) and a question of their own, not the card's lane question.

## From the second QC (verbatim)

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

## From the coordinator's scan (new checks for rules 11 and 20-24 included)

- RULE  card wording as copy (rule 23): angela-williams-4948535b M2
- RULE  label before fixed line (rule 20): ann-wilkesmann-6aa477119 M2
- RULE  label before fixed line (rule 20): ric-caldwell-9a994444 M2
- RULE  label before fixed line (rule 20): susan-oliver-am-03788737a M2
- RULE  label before fixed line (rule 20): tedy-ferreira M2

## When you are done

Re-run `python3 /tmp/claude-1006/-home-vadim-prod/199d83ab-a920-4bc3-8636-0ed06f0c7b1f/scratchpad/scan.py <full path of the campaign dir> --only fernwood-fitness-1` until the block for your batch is "none" (or every remaining line is explained in the summary), then `python3 scripts/outbound_pack.py split-messages --campaign 2026-10-11-au-sport-fitness --in messages/_batch-fernwood-fitness-1.md` until exit 0 (and the same for fernwood-fitness-2). Append a "Round 3" note to the summary (people touched, what changed; correct any count in the summary that is now wrong) and stop.
