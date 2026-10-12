# Fix list — batch `jetts-fitness` — 2026-10-12

Rules for every person you touch: **"Coordinator decisions 2026-10-12" in `card-messages.md` (rules 1-19)**, plus the technical lane note on data handling. Every batch gets the same rules.

## Main job

Regenerate every **referral Message 2** in this batch. Keep the Message 1s, except the ids the QC list below names for an M1 problem.

Before you write, put a grid at the top of `messages/_summary-jetts-fitness.md`, one row per referral person:
`person_id | M1 topic (from their M1 question) | value line target (a few words) | easy-out target | closer form`.
Within the brand: no easy-out target for more than about a fifth of its referral people, no closer form for more than about a third, and no two value lines that make the same argument. Then write the Message 2s from the grid.

Then line-fix the other people named below.

Then read **every other Message 2** in the file against rules 1-6 (value line, no fit-judging by unit people, easy-out and closer variety per company, no call length, openings). Fix the ones that break a rule and list them in the summary. Leave Message 1s you were not asked to touch exactly as they are.

## From the QC report (only lines that name people in this batch)

- [A. Adherence: 2/5] **Unit owners asked to judge fit for their own club** (franchise rule "never pitch a unit to adopt anything"): › Jetts: aaron-dearie, sarah-dwyer, jetts-gym-mount-hutton, sam-bhandari, mel-george, catherine-hanly.
  → in this batch: aaron-dearie-30a57bb2, sarah-dwyer-98326b102, jetts-gym-mount-hutton-a069a2157, sam-bhandari-0a477a42a, mel-george-08516949, catherine-hanly-491a7018b
- [B. Factual accuracy: 3/5] **Locked 112,100 line changed to "3DLOOK ran 112,100 scans"**, which moves the scans from customers to 3DLOOK: andrewbaildon, peter-reed, rebeccacarson2, sean-hodges, sarahbroadhottot, jeremy-saville.
  → in this batch: andrewbaildon
- [B. Factual accuracy: 3/5] **Implied churn or poor measurement:** › The JT3 note bans implying members leave, yet jay-williams and david-upton do.
  → in this batch: jay-williams-739b4b401, david-upton-1867aa35
- [C. Brand & tone: 1/3] **"so" introducing a benefit** (card word trap; the gate missed it): shaun-pickering, alissa-o-flaherty, katelyn-farmer, tj-groot, josh-muriwai, sam-merza, paul-brown, jonpepper, josephine-tuah, brooke-price, zaac-schembri.
  → in this batch: brooke-price-59421a166
- [C. Brand & tone: 1/3] **Corrective negation or "rather than":** › scanlan-karen: "Instead of a long pitch"
  → in this batch: scanlan-karen
- [C. Brand & tone: 1/3] **Corrective negation or "rather than":** › mel-george: "more useful than a pitch"
  → in this batch: mel-george-08516949
- [D. Format & structure: 2/3] brendon-levenson M2 asks two questions plus a closing question.
  → in this batch: brendon-levenson-57821a68

## From the coordinator's scan (rules the gate does not check)

Each line: the rule or the repetition, then the person. For a company-level line (a sentence, opener or closer shared by several people, the speed phrase or the 100+ line over the cap), keep it for at most the cap and give the others their own wording from rule 7. Every pair of messages still cites at least one number.

- RULE  100+ attribution: elaine-jobson-gaicd-72a8a33 M2
- RULE  M2 >1 question: brendon-levenson-57821a68 M2
- RULE  call length: crystal-ford-a77975407 M2
- RULE  call length: jetts-oakleigh-6473a4155 M2
- RULE  call length: lisa-gratrix-02013031b M2
- RULE  call length: mel-george-08516949 M2
- RULE  call length: mike-knights M2
- RULE  call length: paul-divin-98a979100 M2
- RULE  call length: sarah-dwyer-98326b102 M2
- RULE  corrective negation: scanlan-karen M2
- RULE  drift/leave/by eye: jetts-oakleigh-6473a4155 M2
- RULE  drift/leave/by eye: mike-knights M2
- RULE  fit-judging: aaron-dearie-30a57bb2 M2
- RULE  fit-judging: sam-bhandari-0a477a42a M2
- RULE  fit-judging: sarah-dwyer-98326b102 M2
- RULE  pitch word: mel-george-08516949 M2
- RULE  pitch word: scanlan-karen M2
- RULE  presumed reaction: angelique-woods-16a39714 M1
- RULE  presumed reaction: sam-bhandari-0a477a42a M1
- RULE  ran 112,100: andrewbaildon M2
- RULE  so-benefit: brendon-levenson-57821a68 M1
- RULE  so-benefit: brooke-price-59421a166 M2
- RULE  so-benefit: david-upton-1867aa35 M1
- RULE  so-benefit: lisa-gratrix-02013031b M1

## People to touch (19)

aaron-dearie-30a57bb2, sarah-dwyer-98326b102, jetts-gym-mount-hutton-a069a2157, sam-bhandari-0a477a42a, mel-george-08516949, catherine-hanly-491a7018b, andrewbaildon, jay-williams-739b4b401, david-upton-1867aa35, brooke-price-59421a166, scanlan-karen, brendon-levenson-57821a68, elaine-jobson-gaicd-72a8a33, crystal-ford-a77975407, jetts-oakleigh-6473a4155, lisa-gratrix-02013031b, mike-knights, paul-divin-98a979100, angelique-woods-16a39714

## When you are done

Run `python3 scripts/outbound_pack.py split-messages --campaign 2026-10-11-au-sport-fitness --in messages/_batch-jetts-fitness.md` until it exits 0, update `messages/_summary-jetts-fitness.md` (people touched, what changed, anything you could not fix), and stop.
