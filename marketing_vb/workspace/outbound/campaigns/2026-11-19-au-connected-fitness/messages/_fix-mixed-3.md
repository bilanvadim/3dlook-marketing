# Fix round 1, batch mixed-3: 2026-11-19-au-connected-fitness (QC 11/20, Vadim chose a fix round, 2026-11-20)

Apply EVERY item below to `messages/_batch-mixed-3.md`, then run `split-messages` until exit 0, then stop. Edit only the named sentences and the inserts; leave every other sentence as it is. Do not rewrite whole messages.

Rules for this round (from the card; the QC list follows them):
- **Message 1 order:** company line, then ONE pain sentence, then the FitXpress fix sentence(s), then the question (Vadim 2026-11-18: Message 1 explains the pain and how the product solves it). A "pain insert" goes right before the first sentence that starts "FitXpress". The insert text may be used verbatim for every listed person (repeats at one company are allowed, Vadim 2026-11-20). If the message already says the same pain in other words, replace that sentence with the insert instead of having two.
- **Respect each company's Account facts Never line** in your insert (e.g. Fernwood: no "weight"; CSB: never describe what the app logs; One Playground: no coach "works from a weight entry").
- **Referral Message 2:** one value line that continues their Message 1 question, then the easy out as ONE plain sentence ("If X sits with head office, a pointer to whoever owns the member app would help."), then the soft ask on its own line. Never two closers ("A short call could cover it, or point me to..." followed by "Might be worth a quick chat?"). Never write as if the person already replied ("Your answer would...", "That tells me...").
- **The soft ask ("Might be worth a quick chat?" and the like) is always its own last paragraph**, never glued to the end of the previous one. Where the QC list says "soft ask on its own line", split it.
- **"3DLOOK has worked with 100+ clients" and "112,100 scans" only for founders, CEOs and managing directors**, and never bolted on as a stand-alone line; where QC says delete, delete.
- **Page URL:** about half of each company's Message 2s carry https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ on its own line, before the soft ask, with no label in front ("Details:", "Setup page:" are out). Where QC says "add the URL", add it that way.
- After `split-messages` passes, re-read every message you changed, in full.

QC's line-level fixes for this batch (person_id, current → replacement):

**Pain inserts (7 Message 1s):**
- Your Reformer: `emma-stallworthy`, `lizzie-russell-157109122`, `melissa-blakelock-109460283`. Insert "Between check-ins, body progress often rests on a weight entry and photos that are not measured."
- Hapana: `sasharoyal`, `tais-marmentini-654890125`. Insert "In a member app, progress between check-ins often rests on a weight entry and photos that are not measured."
- Fitness Cartel: `darren-mellor-a81123141`. Insert "Between PT sessions and classes, a weight entry leaves out waist and lean mass change."
- Fernwood: `sue-mckenna-0685aa120`. Insert "Between sessions, body change is hard to compare without a record taken the same way each time." Fernwood copy has no "weight".

**Line fixes:**
- `amynicol1`:
  - M1: "Between check-ins, body progress often rests on a weight entry and photos nobody measures." → "Body change between check-ins is hard to compare when every reading is taken a different way."
  - M2: "3DLOOK has worked with 100+ clients." → delete.
- `lionel-key-0b69a71`:
  - M1: "Wanted to reach out about CSB's Move With Us app, where progress check-ins run with the brand's dietitians. Between them, body progress tends to rest on a weight entry and photos nobody measures." → "CSB's Move With Us app runs progress check-ins with the brand's dietitians. Body change between check-ins is hard to compare when every reading is taken a different way."
  - M2: "A short call could cover it, or point me to whoever owns the Move With Us app." → "If someone else owns the Move With Us app, a pointer would help."
- `ryan-briggs-6b234740` M1:
  - "Noticed you carry both product and the scrum rhythm for the Move With Us app at CSB, which calls for a concrete one." → "You carry both product and the scrum rhythm for the Move With Us app at CSB."
  - "It gives a program's check-in a measured record where progress otherwise rests on weight and photos." → "It gives a program's check-in a measured record taken the same way each time."
- `diana-williams-b39b456`:
  - M1: "Between sessions, body progress often rests on a weight entry and photos nobody measures." → "Between sessions, body change is hard to compare without a record taken the same way each time."
  - M2: "A feature like this reaches members only through whoever runs the apps at Fernwood. A pointer there would help." → delete.
  - M2: "A short call could cover it, or point me to whoever owns the apps." → "If the apps sit with someone else at Fernwood, a pointer would help."
- `lauren-channon-847212b7`:
  - M1: "Between sessions, progress often rests on a weight entry and photos nobody measures." → "Between sessions, body change is hard to compare without a record taken the same way each time."
  - M2: "A short call could cover your view from the club, or point me to whoever owns the member app at head office." → "If the member app sits with head office, a pointer to whoever owns it would help."
- `ami-schultz-a1a15835b`:
  - M1: "Body change between sessions often reaches a trainer as a weight entry and photos nobody measures." → "Between sessions, a weight entry and photos leave out waist and lean mass change."
  - M2: "Your answer would tell me where a measured record could fit in a member's week." → "Members would take the scan at home, between visits."
  - M2: "Happy to talk it through, or you could point me to the owner there." → "If that sits outside your club, a pointer to the app owner would help."
- `cade-raymond-b62890350`:
  - M1: "Quick note from one who knows trainer sessions from the inside: you moved from personal training into running a club at Planet Fitness Australia." → "You moved from personal training into running a club at Planet Fitness Australia, so you know the trainer sessions from the inside."
  - M2: "A call could cover it, or a name at the support office would do as well." → "If it sits outside your club, a name at the support office would help."
- `emily-elle-mosca`:
  - M1: "Brief one, given the trainer and marketing mix in your background at Planet Fitness Australia." → "You bring training and marketing to running a club at Planet Fitness Australia."
  - M2: "How members track their week is the piece I would learn from you." → "Members would take the scan on their own phones, between visits."
  - M2: "A short call could cover it, or a pointer to them would do." → "A pointer to them would help."
- `jonathon-alcock-206118220` M2: "A short call could cover how it works for members, or point me to whoever owns the member app there." → "A pointer to whoever owns the member app there would help."
- `melissa-cannavo-a8331b16b` M2: "A short call could cover a club's view, or a pointer to the app owner there would do." → "A pointer to the app owner there would help."
- `sameer-ali-7a9586232`:
  - M2: "Your read of what members ask would help me judge where a measured record fits." → "Members would take the scan at home, between trainer sessions."
  - M2: "A short call could cover it, or a pointer to them would do." → "A pointer to them would help."
- `adamfaludi`:
  - M1: "Turning something messy into something clear and scalable is how you describe your work, and progress between check-ins is one such topic: a weight entry and photos nobody measures." → "You describe turning something messy into something clear and scalable. Between check-ins, member progress often rests on a weight entry and photos that are not measured."
  - M1: "What do Hapana's gyms ask for most around member progress?" → "What do gyms and studios on Hapana ask for most around member progress?"
  - M2: "That question usually lands with product. A pointer would help as much as a view from your side. A short call could cover how the scan works for a gym's members, or point me to whoever owns the member app roadmap at Hapana." → "For a gym's members, the scan would run inside the branded member app, with the gym choosing what members see. If the member app roadmap sits with product, a pointer to its owner would help."
- `sasharoyal` M2: "A short call could cover it, or point me to whoever owns product planning at Hapana." → "If product planning sits elsewhere at Hapana, a pointer would help."
- `benjamincochrane` M1: "Noticed the full-stack and product mix in your background, which calls for a technical angle on the branded member app Hapana ships." → "Your background mixes full-stack and product, so here is the technical side of a scan in the branded member app Hapana ships."
- `jasellis` M1: "Your remit as CTO covers the Your Reformer At Home app, digital services and AI initiatives, which calls for a technical angle." → "Your remit as CTO covers the Your Reformer At Home app, digital services and AI initiatives."
- `allie-mairs-a44271341` M2: "A short call could cover how it works, or point me to whoever owns the app." → "If the At Home app sits with product, a pointer to its owner would help."
- `melaniewebster2` M2: "A short call could cover it, or point me to whoever owns the At Home app." → "If the At Home app sits with someone else, a pointer would help."
- `melissa-blakelock-109460283` M2: "3DLOOK has worked with 100+ clients." → delete.
- `john-mcclory`:
  - M1: "Quick thought for a club general manager at Virgin Active Australia." → "Virgin Active Australia's app sets weekly visit goals and milestones for members."
  - M2: "A short call could cover it, or point me to whoever owns the Virgin Active Australia app." → "A pointer to whoever owns the Virgin Active Australia app would help."
- `upsonpaul` M2: "A short call could cover how it works for members, or point me to whoever owns the Virgin Active Australia app." → "If the app sits with product, a pointer to its owner would help."
- `liam-cole-672411208` M2: "A short call could cover it, or point me to whoever owns the TotalFusion app at head office." → "A pointer to whoever owns the TotalFusion app at head office would help."
- `matt-butler-6754b5a7`:
  - M1: "TotalFusion Platinum Newstead" → "TotalFusion Newstead". Platinum is a membership level the card says never to name.
  - M2: "Members at Newstead would tell us more than any pitch about whether a scan belongs in the TotalFusion app." → "Members at Newstead would take the scan at home between classes."
  - M2: "A call could cover it, or point me to the owner of the app at head office." → "A pointer to the owner of the app at head office would help."
- `thiago-meneses-b65088244` M1: "Program Director and Head of Training and Development at TotalFusion puts the coach's next step with you. Between sessions, body change often reaches a coach as a weight entry and photos nobody measures." → "Training and development at TotalFusion puts the coach's next step with you. Between sessions, a weight entry and photos leave out waist and lean mass change."
- `kristy-lee-roodenburg-088566349` M1: "Your programming already runs through the member's phone. Between sessions, body change tends to reach a coach as a weight entry and photos nobody measures." → "Between sessions, a weight entry and photos leave out waist and lean mass change."
- `jay-meyer-246167321` M2: "A short call could cover it, or point me to whoever owns the app." → "A pointer to whoever owns the app would help."
- `darren-mellor-a81123141` M2: "It returns 80+ body measurements, under 45 seconds from the photos to structured results." → delete.
- **Optional, cross-company stock line:** change "photos nobody measures" → "photos that are not measured" (the card's own wording, without the dig) in:
  - cade-raymond, emily-elle-mosca, jonathon-alcock, melissa-cannavo, sameer-ali;
  - benjamincochrane, aaron-sealy-664835b8, b56180b1, john-mcclory, upsonpaul;
  - helen-mob-healey-00b89678, liam-cole, matt-butler, brad-wharakura;
  - jay-meyer, allie-mairs, melaniewebster2.
