# Fix round 1, batch mixed-1: 2026-11-19-au-connected-fitness (QC 11/20, Vadim chose a fix round, 2026-11-20)

Apply EVERY item below to `messages/_batch-mixed-1.md`, then run `split-messages` until exit 0, then stop. Edit only the named sentences and the inserts; leave every other sentence as it is. Do not rewrite whole messages.

Rules for this round (from the card; the QC list follows them):
- **Message 1 order:** company line, then ONE pain sentence, then the FitXpress fix sentence(s), then the question (Vadim 2026-11-18: Message 1 explains the pain and how the product solves it). A "pain insert" goes right before the first sentence that starts "FitXpress". The insert text may be used verbatim for every listed person (repeats at one company are allowed, Vadim 2026-11-20). If the message already says the same pain in other words, replace that sentence with the insert instead of having two.
- **Respect each company's Account facts Never line** in your insert (e.g. Fernwood: no "weight"; CSB: never describe what the app logs; One Playground: no coach "works from a weight entry").
- **Referral Message 2:** one value line that continues their Message 1 question, then the easy out as ONE plain sentence ("If X sits with head office, a pointer to whoever owns the member app would help."), then the soft ask on its own line. Never two closers ("A short call could cover it, or point me to..." followed by "Might be worth a quick chat?"). Never write as if the person already replied ("Your answer would...", "That tells me...").
- **The soft ask ("Might be worth a quick chat?" and the like) is always its own last paragraph**, never glued to the end of the previous one. Where the QC list says "soft ask on its own line", split it.
- **"3DLOOK has worked with 100+ clients" and "112,100 scans" only for founders, CEOs and managing directors**, and never bolted on as a stand-alone line; where QC says delete, delete.
- **Page URL:** about half of each company's Message 2s carry https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ on its own line, before the soft ask, with no label in front ("Details:", "Setup page:" are out). Where QC says "add the URL", add it that way.
- After `split-messages` passes, re-read every message you changed, in full.

QC's line-level fixes for this batch (person_id, current → replacement):

**Pain inserts (8 Message 1s):**
- Fitness & Lifestyle Group: brettandrewlewis, joanne-power, luke-sampson-searle, lucmccann, rob-waldron. Insert "A weight entry or a progress photo leaves out waist and lean mass change."
- Viva Leisure: lee-hanrahan-74430824, stephen-defries-044202a2. Insert "A weight entry leaves out waist and lean mass change."
- Genesis: david-maskill-8b0836a5. Insert "Between visits, a weight entry leaves out waist and lean mass change."

**Line fixes:**
- `brettandrewlewis` M2: "Placement is easy to test. One cohort scans at onboarding, a second at the first check-in, and the pilot counts completion and retake rates for each, with the usual flow as comparison." → "A pilot would answer it: one member cohort scans at onboarding and at the first check-in, a comparable cohort keeps the usual flow, and completion and retake rates are counted."
- `matt-muller-19769920b` M2: "Both can be tested. One cohort scans at onboarding, another at the first check-in, and the pilot compares onboarding completion with the usual flow." → "A pilot covers both: one member cohort scans at onboarding and at the first check-in, and onboarding completion is compared with a cohort on the usual flow."
- `lauren-nolan-416261b7` M1: "Studio members get a progress check without much to measure beyond a weight figure." → "Between classes, a weight figure leaves out waist and lean mass change."
- `bec-giles` M1: "Noticed Genesis took the AUSactive 2026 Industry Innovation Award for Recovery." → "Members at participating Genesis clubs book classes and message their club in Genesis Connect."
- `luke-koulaxizellis-54515195` M1: "This stood out: Genesis took the AUSactive 2026 Industry Innovation Award for Recovery." → "Members at participating Genesis clubs book classes and message their club in Genesis Connect."
- `clay-williams-75bb18205`:
  - M1: "Had a thought on the recovery spaces Genesis has run since March 2025." → "Genesis Connect lets members book classes and message their club between visits."
  - M2: "From a coaching view, the useful part is that the record is timestamped and the trainer can review it. It returns 80+ body measurements, under 45 seconds from the photos to structured results." → "If members at your club ask about change between visits, a trainer could review the same timestamped record the member sees."
- `mayank-badamia-774783b4` M2: "That tells me where a feature like this would need to land first." → "A feature like this would reach the clubs from head office."
- `rikki-feliciak-226245b3` M2: "Knowing who hears first helps me aim this properly. The scan returns 80+ body measurements, under 45 seconds from the photos to structured results, and the brand keeps its own screens." → "The clubs would get it inside the member apps, with nothing to install and the brand's own screens."
- `niki-twitchett-b00a4a215` M2: "Their phones would do the capture, with nothing changing on your club floor." → "Members would take the scan on their own phones, with nothing changing on your club floor."
- `gordon-martin-cfe-b502295b` M2: "It would reach clubs as part of the app, in the brand's own look, with capture on the member's phone." → "A scan would reach the clubs as part of the member app, in the brand's own look, with capture on the member's phone."
- `stephen-defries-044202a2` M2: "Whatever members ask for, the delivery is an SDK and an API: web and mobile SDKs with supported iOS and Android integrations, under the Plus Fitness look." → "If progress is high on that list, delivery is web and mobile SDKs with supported iOS and Android integrations, under the Plus Fitness look."
- `michael-cunico-13b01017b` M2: "Next to the Coach, the coach and member would look at one timestamped record, and the brand chooses what each sees." → "Next to Club Lime Coach, a trainer and a member would look at one timestamped record, and the brand chooses what each sees."
- `lucmccann` M1: "Got me thinking about the core CRM side at Fitness & Lifestyle Group: a scan is just one more structured record on the member profile." → "On the core CRM side at Fitness & Lifestyle Group, a scan would be one more structured record on the member profile."
- `rob-waldron` M1: "Made me think about the CIO and CISO seat at Fitness & Lifestyle Group: a body scan in the member apps is an SDK step in onboarding, and how it enters the flow matters." → "For the CIO and CISO seat at Fitness & Lifestyle Group, a body scan in the member apps would be one SDK step in onboarding."
- `mackenzie-pirlo-1008a3b0` M1: "Got me thinking: the Genesis Connect app handles class bookings and messages to the club." → "The Genesis Connect app handles class bookings and messages to the club."
- `david-maskill-8b0836a5` M2: "Partner capabilities tend to move fastest through an SDK." → delete. It is a presumed reaction.
- **Soft ask on its own line.** Move the closing question to a separate line in 20 Message 2s:
  - george-reed, luke-sampson-searle, nicole-grainger, rikki-feliciak;
  - rob-waldron, brettandrewlewis, gordon-martin, lauren-jeffries;
  - lauren-nolan, nathan-elliott, niki-twitchett, stephen-defries;
  - bec-giles, clay-williams, david-maskill, james-brennan;
  - kyle-mackenzie, luke-koulaxizellis, mackenzie-pirlo, mayank-badamia.
- **Genesis URL (1 of 9):** add it to the Message 2s of david-maskill, james-brennan and kyle-mackenzie.
