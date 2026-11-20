# Fix round 1, batch mixed-2: 2026-11-19-au-connected-fitness (QC 11/20, Vadim chose a fix round, 2026-11-20)

Apply EVERY item below to `messages/_batch-mixed-2.md`, then run `split-messages` until exit 0, then stop. Edit only the named sentences and the inserts; leave every other sentence as it is. Do not rewrite whole messages.

Rules for this round (from the card; the QC list follows them):
- **Message 1 order:** company line, then ONE pain sentence, then the FitXpress fix sentence(s), then the question (Vadim 2026-11-18: Message 1 explains the pain and how the product solves it). A "pain insert" goes right before the first sentence that starts "FitXpress". The insert text may be used verbatim for every listed person (repeats at one company are allowed, Vadim 2026-11-20). If the message already says the same pain in other words, replace that sentence with the insert instead of having two.
- **Respect each company's Account facts Never line** in your insert (e.g. Fernwood: no "weight"; CSB: never describe what the app logs; One Playground: no coach "works from a weight entry").
- **Referral Message 2:** one value line that continues their Message 1 question, then the easy out as ONE plain sentence ("If X sits with head office, a pointer to whoever owns the member app would help."), then the soft ask on its own line. Never two closers ("A short call could cover it, or point me to..." followed by "Might be worth a quick chat?"). Never write as if the person already replied ("Your answer would...", "That tells me...").
- **The soft ask ("Might be worth a quick chat?" and the like) is always its own last paragraph**, never glued to the end of the previous one. Where the QC list says "soft ask on its own line", split it.
- **"3DLOOK has worked with 100+ clients" and "112,100 scans" only for founders, CEOs and managing directors**, and never bolted on as a stand-alone line; where QC says delete, delete.
- **Page URL:** about half of each company's Message 2s carry https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ on its own line, before the soft ask, with no label in front ("Details:", "Setup page:" are out). Where QC says "add the URL", add it that way.
- After `split-messages` passes, re-read every message you changed, in full.

QC's line-level fixes for this batch (person_id, current → replacement):

**Pain inserts (9 Message 1s):**
- CityFitness, `david-vonder-28817770`, and BlueFit, `matt-frost-`: insert "Weight alone misses change at the waist and in lean mass."
- KX Pilates, `francis-dowdle-13b43360` and `warren-ainsley-6519a666`: insert "Weight alone misses change at the waist and hip."
- Les Mills New Zealand: `anise-elliott-neilson`, `brent-nathan-ab97354`, `brett-sutton-43285123`, `donald-horsburgh-0498464` and `stephanie-campbell-4b2a7b19`. Insert "A weight figure leaves out change at the waist and in lean mass."

**Line fixes:**
- `joe-erskine-6ab72061`:
  - M1: "A thought on CityFitness and what members do between club visits." → "Across your region, CityFitness members check in on their training in the CityFitness app."
  - M2: "What members ask in your region would show what a progress view should carry, and a short call would help me get that right." → "Members in your region would take the scan on their own phones between visits, and CityFitness would choose which results appear."
- `jodie-preston-9053298a`:
  - M1: "A note on CityFitness in Auckland and what members do between visits." → "In Auckland, CityFitness members check in on their training in the CityFitness app."
  - M2: "Auckland members' questions are the best guide to what a progress view should show, and CityFitness would choose which scan results appear." → "Auckland members would scan at home between visits, and CityFitness would choose which results appear."
- `lisa-brown-9a2476136`:
  - M1: "Thought I'd share an idea for CityFitness operations on the member app." → "The CityFitness app is where members already check in on their training."
  - M2: "A new feature lands best when a club can see what it does for its members, and I can send that in a short call." → "Clubs would get it as a member-app feature, with nothing to install and CityFitness choosing which results appear."
- `mark-hurdle-781781315` M1: "Writing to CityFitness's National Director of Fitness about member progress." → "At CityFitness, the coach and personal-trainer review before a member's next programme block is where a measured record would sit."
- `stuart-davenport-952894`:
  - M1: "Thinking about the CityFitness member app, here is one idea." → "The CityFitness app is where members check in on their training."
  - M1: "What do members tell the clubs about tracking progress between visits?" → "How does a new member-app feature come before the CityFitness board?"
- `david-vonder-28817770` M1: "Noticed your headline pairs CIO and Chief Digital Officer, so I will keep this technical." → "Your headline pairs CIO and Chief Digital Officer, and the CityFitness app is where members check in on their training." Then insert the pain sentence.
- `andrew-hungerford-67673a33`:
  - M1: "A question about BlueFit Health Clubs and what members do between classes." → "BlueFit Health Clubs run inside the leisure centres BlueFit operates."
  - M1: "What do members at BlueFit ask about their progress between classes?" → "When a new member-app feature is planned at BlueFit, how does it reach the people who look after the centres?"
  - M2: "Your answer would shape what a progress screen shows, and a short call would help me get it right." → "The scan needs nothing in a centre: members take it on their own phones."
- `todd-mchardy-53676619`:
  - M1: "For BlueFit's Managing Director, a short note on the Health Club app." → "The BlueFit Health Club app got a brand-new interface and new workout content in late 2025."
  - M2: "The shortest version of the idea is a measured check-in inside the BlueFit app." → "At a first check-in, the member would see a measured record in BlueFit's own screens."
  - M2: "3DLOOK has worked with 100+ clients." → delete.
- `ryan-o-connor-bb716136` M1: "Came across your work at BlueFit across facility management and business development." → "Your BlueFit role spans facility management and business development."
- `brett-mcewin-70972ab7` M1: "Think of BlueFit Health Clubs, where classes and personal training already give members set points to check in." → "At BlueFit Health Clubs, classes and personal training already give members set points to check in."
- `lee-jeka-688a369b` M2: "A pilot can compare the two moments, with one member cohort scanning while a comparable cohort keeps the usual flow." → "A pilot would cover both: one member cohort scans at onboarding and at the first check-in, while a comparable cohort keeps the usual flow."
- `matt-frost-` M2: "3DLOOK has worked with 100+ clients." → delete.
- `brooke-daubney-59653a34` M1: "Noticed KX Strength began rolling out in January and KX Institute launched in July, a busy year for education and product at KX Pilates." → "Noticed KX Strength began rolling out in January next to the relaunched KX Signature, a busy year for the class ladder at KX Pilates."
- `francis-dowdle-13b43360`:
  - M1: "Thinking about how KX Pilates studio teams run progress between classes." → "KX Pilates members climb a class ladder from Basics to Advanced, booked in the KX Pilates app."
  - M2: "Studios tend to want to see what a feature does before it reaches members, and a short call can show that. 3DLOOK has worked with 100+ clients." → "Studios would get it as an app feature, with nothing to install and head office choosing what members see."
- `warren-ainsley-6519a666` M1: "Your background in software implementation and data is why this note on KX Pilates is technical." → "KX Pilates members book every class in the KX Pilates app, KX Strength included since January."
- `eloise-censor-a7983749` M2: "Their questions would show what a progress view should carry, and I would like to hear them on a short call." → "Members at your studios could take the scan at home and see the record in the KX Pilates app."
- `tevitas` M2: "Those questions show what a progress view should carry for a club's members." → "Members at your club would take it on their own phones between classes, with nothing to set up in the club."
- `anise-elliott-neilson`:
  - M1: "Came across your strategic partnerships work at Les Mills New Zealand." → "You run corporate partnerships at Les Mills New Zealand."
  - M2: "The pilot starts with one member cohort." → "A pilot would start with one member cohort, against criteria agreed beforehand."
- `brent-nathan-ab97354` M1: "Your 20-year technical path and the Les Mills New Zealand app update of 29 October make this an integration note." → "The Les Mills New Zealand app shipped more workout-history detail on 29 October."
- `donald-horsburgh-0498464` M1: "Quick note for the CIO at Les Mills New Zealand on the member app." → "The Les Mills New Zealand app has shipped three releases in 2026, the latest on 29 October."
- `stephanie-campbell-4b2a7b19` M1: "A thought on Les Mills New Zealand and its member app." → "Les Mills New Zealand added challenges, leaderboards and richer workout history to its app in 2026."
- **Soft ask on its own line** in 16 Message 2s:
  - jodie-preston, joe-erskine, lisa-brown, sam-wagstaff;
  - stuart-davenport, andrew-hungerford, leonie-s, ryan-o-connor;
  - aaronsmithkx, amy-cashman, eloise-censor, francis-dowdle;
  - kara-spice, brett-sutton, stephanie-campbell, tevitas.
