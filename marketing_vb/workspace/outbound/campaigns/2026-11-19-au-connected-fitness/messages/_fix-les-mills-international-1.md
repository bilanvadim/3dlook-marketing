# Fix round 1, batch les-mills-international-1: 2026-11-19-au-connected-fitness (QC 11/20, Vadim chose a fix round, 2026-11-20)

Apply EVERY item below to `messages/_batch-les-mills-international-1.md`, then run `split-messages` until exit 0, then stop. Edit only the named sentences and the inserts; leave every other sentence as it is. Do not rewrite whole messages.

Rules for this round (from the card; the QC list follows them):
- **Message 1 order:** company line, then ONE pain sentence, then the FitXpress fix sentence(s), then the question (Vadim 2026-11-18: Message 1 explains the pain and how the product solves it). A "pain insert" goes right before the first sentence that starts "FitXpress". The insert text may be used verbatim for every listed person (repeats at one company are allowed, Vadim 2026-11-20). If the message already says the same pain in other words, replace that sentence with the insert instead of having two.
- **Respect each company's Account facts Never line** in your insert (e.g. Fernwood: no "weight"; CSB: never describe what the app logs; One Playground: no coach "works from a weight entry").
- **Referral Message 2:** one value line that continues their Message 1 question, then the easy out as ONE plain sentence ("If X sits with head office, a pointer to whoever owns the member app would help."), then the soft ask on its own line. Never two closers ("A short call could cover it, or point me to..." followed by "Might be worth a quick chat?"). Never write as if the person already replied ("Your answer would...", "That tells me...").
- **The soft ask ("Might be worth a quick chat?" and the like) is always its own last paragraph**, never glued to the end of the previous one. Where the QC list says "soft ask on its own line", split it.
- **"3DLOOK has worked with 100+ clients" and "112,100 scans" only for founders, CEOs and managing directors**, and never bolted on as a stand-alone line; where QC says delete, delete.
- **Page URL:** about half of each company's Message 2s carry https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ on its own line, before the soft ask, with no label in front ("Details:", "Setup page:" are out). Where QC says "add the URL", add it that way.
- After `split-messages` passes, re-read every message you changed, in full.

QC's line-level fixes for this batch (person_id, current → replacement):

**Insert the pain sentence** "A weight entry on its own leaves out waist and lean mass change." into these 26 Message 1s:
- alex-hopkins-0a1a6959, andrew-flavell-dr-eng-59a3a9, cam--adams, carlo-tonin;
- charlotte-lovell, derek-tomes-687445145, elinor-quayle-b3bb2113;
- elliot-de-lautour-063048a0, elliot-smith-b4b3a1244, gemma-lynskey-60413028;
- james-graham-25b12b42, jeremycarreon, keryn-mckenzie-714b9554;
- kim-walker-9978336, lacey-churcher-84519360, lisa-osborne-24996268;
- llori-valenzuela-79580b1, malcolm-black-onzm-3a221238, marina-nola-0796a1;
- mheyns, micayla-wright-a5a306155, sally-berlin-8793099;
- sam-hambling, sophie-hall-5b165273, steven-renata-44133bb, tom-o-connor-78b60b30.

alysha-kennedy and amberataylor get their pain line through the fixes below.

- `gandalf-archer-1bb8876` M1: "A program director sees progress at each plan's end." → delete.
- `alysha-kennedy` M1: "Every new LES MILLS+ launch carries plans and challenges that give members a reason to check progress." → "LES MILLS+ carries monthly workout plans, challenges and progress tracking. A weight entry on its own leaves out waist and lean mass change."
- `lacey-churcher-84519360` M1: "New workouts land in LES MILLS+ every month, each with plans and challenges around it." → "LES MILLS+ ships roughly monthly, with workout plans and challenges around the workouts."
- `james-graham-25b12b42`:
  - M1: "LES MILLS+ streams on web and mobile, and on TV. One capability has to travel across screens." → "LES MILLS+ streams on web, mobile and TV, and a body check-in would sit on the member's phone."
  - M2: "On members' asks, a one-cohort pilot would show what they do with a first scan." → "A one-cohort pilot would show what members do with a first scan."
  - M2: "112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `jeremycarreon` M1: "LES MILLS+ Premium carries the full library, plans and challenges, the natural home for a 3D progress view." → "LES MILLS+ Premium carries the full library, plans and challenges, and Base a lighter collection."
- `sam-hambling`:
  - M1: "…which suits adding a body model through an SDK." → "…which suits adding a body scan through an SDK."
  - M1: "FitXpress is a pre-trained body model behind web and mobile SDKs and an API:" → "FitXpress is a white-label body scan delivered as web and mobile SDKs with an API:"
  - M1: "How would your team weigh a pre-trained body model against building one in-house?" → "How would your team weigh a ready-made scan SDK against building body measurement in-house?"
- `amberataylor` M1:
  - "Your background in digital product and engagement makes this a fair question for LES MILLS+, which already carries monthly workout plans, challenges and progress tracking." → "LES MILLS+ already carries monthly workout plans, challenges and progress tracking, close to your background in digital product and engagement."
  - "A measured body record is one more input for that screen." → "A weight entry on its own leaves out waist and lean mass change."
- `adam-lazarus-2a24a247`:
  - M1: "and LES MILLS+ now has Premium and Base memberships to build for." → "and LES MILLS+ has Premium and Base memberships to build for."
  - M2: "112,100 scans in 2025 across all 3DLOOK customers." → "At the first check-in, the member would see that record in LES MILLS+'s own screens."
- `marina-nola-0796a1` M1: "LES MILLS+ now has two memberships, Premium and Base, to shape." → "LES MILLS+ has two memberships, Premium and Base, to shape."
- `tom-o-connor-78b60b30` M1: "FitXpress, a white-label body scan, could join it." → "FitXpress, a white-label body scan, could join them."
- `malcolm-black-onzm-3a221238` M2: "If the link is thin, a pilot with one member cohort is a light way to look at it. 3DLOOK has worked with 100+ clients." together with "Happy to be pointed to whoever owns the LES MILLS+ app." → "If the member app sits outside your music and media work, a pointer to whoever owns LES MILLS+ would help."
- `gemma-lynskey-60413028` M2: "If early notice matters, a small pilot on one member cohort would give a clear picture of what is coming. 3DLOOK has worked with 100+ clients." → "A scan like this would start with one member cohort, which leaves time to plan the communication before any wider release."
- `phillip-mills-0784428` M2: "112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `cam--adams` M2: "It returns 80+ body measurements, under 45 seconds from the photos to structured results." → "The scan returns 80+ body measurements, under 45 seconds from the photos to structured results."
- **Bolted proof line, delete** "3DLOOK has worked with 100+ clients." from these Message 2s:
  - `alice-huangxin-liang-977558b4`;
  - `chris-richardson-bb6a3aa1`;
  - `gandalf-archer-1bb8876`;
  - `keryn-mckenzie-714b9554`.
- **URL:** add the page URL alone on a line before the soft ask in 6 more Message 2s. This brings LMI from 12 of 39 to about half. Suggested:
  - jason-paris-3404565, phillip-mills-0784428;
  - lisa-osborne-24996268, gandalf-archer-1bb8876;
  - james-graham-25b12b42, derek-tomes-687445145.
