# Fix list, round 3 — `fitstop` — 2026-10-12

Second QC: 13/20 (`workspace/_quality/outbound/2026-10-12-message-sequencer-au-sport-fitness.md`). The round-1 and round-2 fixes stand. Edit at sentence level: only the people and sentences below.

Read the card's "Coordinator decisions 2026-10-12" again: **rules 20-24 are new** (fixed proof lines stand alone with no label; the speed phrase only where speed is the point and never right after an output noun; "the brand decides where it is shown" only at workplace programmes; the card's own words are not copy; one wording per person for each M2 part, no bare "Or" opening an easy out, two people at one club get different easy-out targets).

Swaps to avoid (the second QC found these after round 2): replacing "ran" with a label; replacing one stock speed sentence with another; replacing one closer sentence with a single new one that everybody then gets; copying the card's rule wording ("member side", "a plain yes") into the copy. When you drop a speed phrase or a proof line, the pair must still cite a number (80+ body measurements is enough).

"Thin M1s" and "product-lane card question" items: give that person a line only they could get (their club, role or a brand fact) and a question of their own, not the card's lane question.

## From the second QC (verbatim)

- **"plus":** richard-hallam M1.
- **Easy outs:**
  - Twins: adam-stevens/jamie-biondi, kevin-kensley/milan-sekulic, jonpepper/paul-emanuel.
  - Member-app target down from 8: bruce-mcconnel, bentoleafoa, adam-stevens, chandell-fretwell, jesse-malseed, jamie-biondi, lachlan-russo, lauren-nash.
- **Closer twins:** bentoleafoa/nebojsa-vujic/brenna-dillon, josephine-tuah/mark-vaiao.
- **jasmine-brierley:** rule 13 (M1); label + reworded line (M2).
- **Other:** card residue lachlan-russo, emilene-lawrance; link claim andrew-papadopoulos; rule 2 nebojsa-vujic.

## From the coordinator's scan (new checks for rules 11 and 20-24 included)

- COMPANY Fitstop: M1 central question near-twin of ameer-madhanpall-2b1563129 (0.80); brenna-dillon-64b6a227a
- COMPANY Fitstop: M1 central question near-twin of brenna-dillon-64b6a227a (0.80); ameer-madhanpall-2b1563129
- RULE  card wording as copy (rule 23): sam-seaton-98411b16b M2
- RULE  plus connector: richard-hallam-14a09765 M1

## When you are done

Re-run `python3 /tmp/claude-1006/-home-vadim-prod/199d83ab-a920-4bc3-8636-0ed06f0c7b1f/scratchpad/scan.py <full path of the campaign dir> --only fitstop` until the block for your batch is "none" (or every remaining line is explained in the summary), then `python3 scripts/outbound_pack.py split-messages --campaign 2026-10-11-au-sport-fitness --in messages/_batch-fitstop.md` until exit 0. Append a "Round 3" note to the summary (people touched, what changed; correct any count in the summary that is now wrong) and stop.
