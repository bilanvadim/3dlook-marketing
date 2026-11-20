---
qc_date: 2026-11-20
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-11-19-au-connected-fitness/messages/ (174 pairs; scored from scratchpad messages-dump.txt + messages/_check.json, gate 0 hard)
track: outbound
artifact_type: messages
product: fitxpress
total_score: 11/20
status: failed
coordinator_review: done (see Coordinator review)
---

# QC Report: message-sequencer, 2026-11-20 (AU + NZ connected fitness, 174 pairs)

**Artifact:** all 174 Message 1 and Message 2 pairs, read company by company. Scored against `card-messages.md`, where the Account facts Use and Never lines count as hard rules, and against `messages/_profiles-*.md`. The gate's results (limits, signature, bans, detector, completeness) are taken as given.

**Rule applied:** Vadim's rule of 2026-11-20. Colleagues at one company may share a pain, question, value point, easy out or whole sentence. None of the `_check.json` soft flags ("near-duplicate sentence", "same sentence at one company", "closing ask repeated") is scored. The cross-company stock lines below are a different finding.

**Total: 11/20, failed.**

**What holds:**
- Every Message 1 names the company and FitXpress, asks one question, has no call ask and no link.
- Every Message 2 ends on a soft ask.
- Numbers come only from proof points, and the repeatability sentence is verbatim.
- No client, prospect, owner or scanner is named, and there is no compliance line.
- Retention appears only as a pilot count, in the product, programs and partnerships lanes.
- No paid tier is mentioned where Account facts say there is none.

**Where it fails:**
1. **About 88 of 174 Message 1s have no pain line.** The card's order is company line → pain → fix → question (Vadim 2026-11-18). By batch: mixed-4 36 of 42, LMI 28 of 39, mixed-2 9 of 30, mixed-1 8 of 28, mixed-3 7 of 35.
2. **Six Account facts Never lines are broken, and four Use lines are stretched past their scope.**
3. **The referral Message 2 closers are broken in three ways:**
   - 18 have a double closer with a broken sentence ("A short call could cover it, or point me to…" followed by "Might be worth a quick chat?");
   - about 8 read as if the person had already replied;
   - about 12 have no value line.

**Recommendation: rewrite Message 1 for the people without a pain line, not the whole campaign.** These are mainly mixed-4 and LMI. Either regenerate those Message 1s or insert the per-company sentence listed below. Then do a line-edit pass on about 70 lines. Re-run `split-messages` afterwards, because the inserts add about 60-80 characters to each Message 1.

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
- **The pain line is missing in about 88 Message 1s.** The lists are in the batch sections. Example: `winterjade` M1 goes company line → product → question. The referral lane also requires "a short pain and fix".
- **Six Never lines are broken:**
  - **Fernwood ("weight"):** `diana-williams-b39b456` and `lauren-channon-847212b7` M1 both say "a weight entry and photos nobody measures".
  - **CSB ("never describe what the app logs: weekly measurements, progress photos, weight"):**
    - `amynicol1`;
    - `lionel-key-0b69a71`;
    - `ryan-briggs-6b234740`.
  - **One Playground:** `atmerriman` says "A coach setting a member's next block works from a weight entry". The Rules say the pain is never about the company's coaches, and the One Coach app records measurements.
- **Four Use lines are used past their scope:**
  - KX Institute is "for education and instructor-facing people only", but `brooke-daubney-59653a34` is in product.
  - The Genesis AUSactive award and the recovery spaces are "for head-office readers", but three club GMs got them:
    - `bec-giles` (award);
    - `luke-koulaxizellis-54515195` (award);
    - `clay-williams-75bb18205` (recovery spaces).
- **Referral Message 2s have no value line continuing the question:**
  - joe-erskine, jodie-preston;
  - eloise-censor, tevitas;
  - andrew-hungerford;
  - lisa-brown, francis-dowdle;
  - samantha-jane, john-l-scott;
  - ami-schultz, sameer-ali, emily-elle-mosca.
- **The page URL is short of "about half of each company":**
  - LMI 12 of 39;
  - Genesis 1 of 9;
  - REVL 0 of 2;
  - One Playground 0 of 2.

### B. Factual accuracy: 3/5
- **Numbers are clean.** All come from proof points. The repeatability sentence, "3DLOOK has worked with 100+ clients" and 112,100 use the approved wording. There is no accuracy claim and no client name.
- **Product claim not on the live page:** `sam-hambling` M1 says "FitXpress is a pre-trained body model behind web and mobile SDKs".
- **Wrong about the company:**
  - At CSB, the three Message 1s tell the Move With Us team that its check-ins rest on weight and unmeasured photos. Account facts say the app logs weekly measurements, so the reader will know it is wrong.
  - At One Playground, `atmerriman` has the same problem.
- **Pilot design rewritten as two arms (onboarding vs first check-in):** `brettandrewlewis`, `matt-muller-19769920b`, `lee-jeka-688a369b`. The page's design is one cohort at onboarding and at the first check-in, against a comparable cohort.
- **"two scans they choose":** `tammy-hembrow-3a7739241` and `penelope-hoess-b5410633` M2. The program selects the scans, not the member.
- **Invented or unsupported claims:**
  - `gandalf-archer-1bb8876`: "A program director sees progress at each plan's end." His profile is empty and flagged for neutral copy.
  - `alysha-kennedy`: "Every new LES MILLS+ launch carries plans and challenges". Not in Account facts.
  - `lacey-churcher-84519360`: "New workouts land in LES MILLS+ every month". Not in Account facts.
  - `james-graham-25b12b42`: "One capability has to travel across screens", right after TV. This implies the scan runs on TV.
  - `cade-raymond-b62890350`: "Quick note from one who knows trainer sessions from the inside". This gives Vadim a PT background.
  - `lauren-nolan-416261b7`: "Studio members get a progress check without much to measure beyond a weight figure". This describes the company's members and its check.
- **Self-answering question:** `jeremycarreon` M1 calls Premium "the natural home for a 3D progress view" and then asks which level it belongs in.

### C. Brand & tone: 2/3
- **No banned words, dashes or AI signatures (gate).** The voice is plain.
- **Stock hooks with nothing specific after them (about 25):**
  - "Made me think about the CIO and CISO seat" (rob-waldron);
  - "Got me thinking about the core CRM side" (lucmccann);
  - "Writing to CityFitness's National Director of Fitness" (mark-hurdle);
  - "For BlueFit's Managing Director, a short note" (todd-mchardy);
  - "Quick note for the CIO" (donald-horsburgh);
  - "…is why this note on KX Pilates is technical" (warren-ainsley);
  - "…make this an integration note" (brent-nathan);
  - "Came across your work" (ryan-o-connor, anise-elliott-neilson). This is the template's banned opener in all but name.
  - "…which calls for a technical angle / a concrete one" (benjamincochrane, jasellis, ryan-briggs).
- **One cross-company stock line:** "photos nobody measures" appears in about 25 Message 1s at 10 companies. At three of them it is pinned on the company's own trainers or coaches: ami-schultz, thiago-meneses, kristy-lee-roodenburg.
- **Body framing:** Barre Body `matthewkane` "how waist and hip change" breaks the card's "framed around strength and posture, never shape".

### D. Format & structure: 2/3
- The gate passed limits, signature and completeness.
- **36 Message 2s glue the soft ask onto the end of the last paragraph:** almost all of mixed-1 and most of mixed-2. The agent prompt says the CTA goes on its own line.
- In mixed-3, Message 1s put the question inside the product paragraph.

### E. Output quality: 2/4
- **Strong pairs, usable as models:**
  - nicole-grainger, michael-cunico (M1);
  - sarah-ostergaard, jason-paris, phillip-mills;
  - b56180b1 (Isak), aaron-sealy;
  - cassie-green, matt-towe;
  - jordan-mccreary, kalen-coughlan, brett-sutton.
- **CityFitness openers carry no company fact:** 5 of 8 Message 1s could be sent to any gym after a name swap (MSG-7).
- **Message 2s written as if the person replied:**
  - mayank-badamia: "That tells me…";
  - andrew-hungerford: "Your answer would shape…";
  - ami-schultz and sameer-ali also;
  - rikki-feliciak, samantha-jane and john-l-scott also.
- **Message 2 openers that brush off the question:**
  - claireseidler: "Any answer fits the same setup.";
  - stephen-defries: "Whatever members ask for,".
- **Bolted-on proof lines:** 100+ or 112,100 standing alone in a Message 2 whose Message 1 already carries 80+. In about 14 pairs.
- **Questions that do not fit the person's role:**
  - `stuart-davenport-952894` is a board director whose headline is another business.
  - `andrew-hungerford-67673a33` is listed as Asset Manager in the web check.
  - Both were asked what members say about progress.
- **Message 2s that pitch a pilot to a referral person:** malcolm-black-onzm and gemma-lynskey.

## Top 3 issues (priority for improver)

1. **Message 1 without a pain line, about 88 of 174.** The writer treats "company line + product + question" as complete. Make the pain a required slot for every lane, technical-integration included.
2. **Account facts Never and Use lines read as soft.** The breaches are:
   - Fernwood "weight" (2);
   - CSB "what the app logs" (3);
   - One Playground coaches (1);
   - KX Institute (1);
   - Genesis award or recovery spaces for club GMs (3).

   The pain sentence has to be chosen per company against its Never list.
3. **Referral Message 2 closers.** They have a call offer and a pointer request in one broken sentence, then a second soft ask. Some read as if the person replied, and some have no value line. One closer is enough: a pointer line, then the soft ask.

## Line-level fixes by batch

Format: `person_id` M#: "current" → "replacement". "Insert" means add the sentence directly before the "FitXpress …" sentence of Message 1.

### messages/_batch-les-mills-international-1.md

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

### messages/_batch-mixed-1.md

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

### messages/_batch-mixed-2.md

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

### messages/_batch-mixed-3.md

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

### messages/_batch-mixed-4.md

**Pain inserts (36 Message 1s).** Each sentence is chosen against that company's Never list:

| Company | People | Sentence to insert |
|---|---|---|
| Barre Body | `siobhanwhitby` | "Strength and posture change between classes is easy to feel and hard to record." |
| Jetts Fitness | `ben-mason-86563b22`, `eddieswinnen`, `samantha-jane-a3012b166` | "Between sessions, a weight entry leaves out waist and lean mass change." |
| Studio Pilates | `john-l-scott-8380a045`, `tanya-winter-b9b52524`, `winterjade` | "Between classes, a weight entry leaves out waist and lean mass change." |
| Sweat | `bettykarikis`, `claireseidler`, `robert-ware-5b867a48` | "A weight figure on its own leaves out waist and lean mass change." |
| Peaches Pilates | `chris-hole`, `teah-foot-3065b5244`, `tori-clapham-902869195` | "Between classes, a weight entry leaves out waist and lean mass change." |
| CONDITN | `daniel-capilli-b27623308`, `jordan-mccreary-5456aba4` | "A weight figure leaves out change at the waist and in lean mass." |
| Revo | `jordan-checker-876b6516b`, `kalen-coughlan-a0a626177`, `kayla-braithwaite-a34753209` | "Between club visits, a weight entry leaves out waist and lean mass change." |
| The Yard | `jessica-buxton-a7722883`, `tiarne-bova-b65456247` | "A weight entry leaves out how waist and hip change as a block runs." |
| GymMaster | `asmithnz`, `kate-rawnsley-shirtcliff-07926923` | "A weight entry leaves out waist and lean mass change." |
| Tammy Fit | `amy-hembrow-b435634a` | "Workout counts show effort, and they leave body change out." (no weight wording) |
| STRONG Pilates | `carl-planicka-14b39b421`, `kat-hegarty-097099b6` | "Between classes, a weight entry leaves out waist and lean mass change." |
| REVL | `jake-hendry-877168224` | "A weight entry misses how waist and hip change across a block." |
| One Playground | `danielbowden411` | "A weight entry leaves out waist and lean mass change." |
| Fluidform | `penelope-hoess-b5410633` | "A weight entry leaves out waist and lean mass change." |
| Clubworx | `emilysmart` | "In a member app, a weight entry leaves out waist and lean mass change." |
| Gym Mate | `bdquinney` | "In a member app, a weight entry leaves out waist and lean mass change." |
| Gravl | `julian-gargicevich` | "Between sessions, body change is hard to see without a measured record." |
| Vision PT | `damian-glynn-vision-personal-training-b0027016` | "At a plan change, a weight entry leaves out waist and hip change." |
| KIC | `emily-robinson-9b7a2011a` | "Between programs, body change is hard to compare without a record taken the same way each time." (no weight wording) |
| Fitstop | `riley-woodcock` | "Between sessions, body change is hard to compare without a record taken the same way each time." |
| UBX | `johncuskelly` | "Between club sessions, a weight entry leaves out waist and lean mass change." |

**Line fixes:**
- `atmerriman` M1: "A coach setting a member's next block works from a weight entry that leaves out waist and hip change." → "A weight entry on its own leaves out waist and hip change."
- `matthewkane` M1: "A weight entry between those check-ins leaves out how waist and hip change." → "Strength and posture change between those check-ins is easy to feel and hard to record."
- `jessica-buxton-a7722883` M1: "The THE YARD GYM app first appeared in April." → "The Yard's app first appeared in April."
- `danielbowden411` M1: "…opened its Zetland superboutique this month…" → "…opened its Zetland superboutique in November…"
- `asmithnz` M1: "GymMaster shipped AI assistant features for club staff this month." → "GymMaster shipped AI assistant features for club staff in November."
- `james-mccreary` M2: "For context, there were 112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `kat-hegarty-097099b6` M2: "There were 112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `claireseidler` M2: "Any answer fits the same setup." → "A body record could sit next to the program's weekly structure, in Sweat's own screens."
- `samantha-jane-a3012b166` M2: "That route matters here, because any new member feature reaches your club through head office." → "A new member feature would reach your club from head office, with nothing to install."
- `john-l-scott-8380a045` M2: "That path decides how any member feature would land in the studios, and the scan would be shown only as Studio Pilates chooses." → "A feature like this would reach the studios through the SP app, shown only as Studio Pilates chooses."
- `tammy-hembrow-3a7739241` M2: "If they belong there, 3D Body Progress tracking and 3D Goal Visualization on the Pro plan give members a side-by-side view of two scans they choose." → "If they belong there, 3D Body Progress tracking on the Pro plan shows a side-by-side view of two scans the program selects." Goal Visualization is dropped because the brand's Never line bars shape wording.
- `penelope-hoess-b5410633` M2: "…give members a side-by-side view of two scans they choose." → "…give members a side-by-side view of two scans the program selects."
- `teah-foot-3065b5244` M1: "Operations and partnerships at Peaches Pilates covers how new capabilities reach members of Peaches Online." → "You head operations and partnerships at Peaches Pilates." Her profile is empty, so the copy stays title-based.
- `tiarne-bova-b65456247` M1: "A scan inside the app would give members a measured body record next to it." → "A scan inside the app would give members a measured body record next to that training."
- **URL:** add it to one REVL Message 2 (cassie-green or jake-hendry) and one One Playground Message 2 (atmerriman or danielbowden411). Both companies have none now.

## Notes for the coordinator
- **Gate soft flags I did not score** under the 2026-11-20 rule: all `near-duplicate sentence`, `same sentence at one company` and `closing ask repeated` entries. The 9 `pricing word` flags are tier and pilot wording at accounts where Account facts list a paid tier, so they are fine.
- **notify.py was not sent.** This run had no shell tool. Text to send: `QC: message-sequencer → 11/20 (failed) ❌ | Top issue: ~88 of 174 Message 1s have no pain line; 6 Account-facts Never breaches (Fernwood weight, CSB app logs, One Playground coaches) | Recommend: regenerate pain-less M1s (mixed-4, LMI) + line-edit pass | File: workspace/_quality/outbound/2026-11-20-message-sequencer-au-connected-fitness.md`

## Coordinator review

agreement: ✅ agree. Spot-checked: cam--adams, sally-berlin, claireseidler and carl-planicka go from a company fact straight to the product with no pain line.
top_issue: Message 1 without a pain line in about half the pairs (Vadim 2026-11-18 rule). Vadim chose a fix round (2026-11-20, «Раунд правок»): per-batch `messages/_fix-<batch>.md` built from this list, the same five writers, then gate and a coordinator read of every changed pair; no second full QC unless the read finds a new pattern. Before the round the coordinator had already removed all 70 link labels (URL on its own line).
