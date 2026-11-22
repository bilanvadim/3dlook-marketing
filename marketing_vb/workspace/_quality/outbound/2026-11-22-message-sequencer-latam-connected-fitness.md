---
qc_date: 2026-11-22
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/messages/_all-pairs.md
track: outbound
artifact_type: messages
total_score: 12/20
status: marginal
coordinator_review: pending
---

# QC Report: message-sequencer, 2026-11-22

**Artifact:** `workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/messages/_all-pairs.md` (189 pairs, 7 batches, profile katya)
**Total: 12/20, marginal.** Rework at line level. Full regeneration is not needed.

Taken as fact from code: limits, signature, bans, detector, completeness (`_check.json`: 0 hard). Within-company repeats are not counted (Vadim 2026-11-20). Pilot and page-link shares are within about half at every company. The highest share is Fitco pilots 2/4 and Spinning Center links 4/7. Zero pilots at Panobianco, BIGG, Spinning Center, Tecnofit and Megatlon is allowed.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5
- **Message 1 has no pain line about the method in 32 of 189 pairs** (Vadim's 2026-11-18 rule). In those pairs the hook goes straight to the product. 16 of the 32 are in mixed-4, which is 16 of 33 in that batch. Examples: `douglas-waltricke-42579a152` «Nextfit's student app already shows each gym's members their workouts…» and then the product; `tadeu-pratique-05137521` «A body check-in could sit inside that loop.» Full list below.
- **Sentences repeated across different companies** (Vadim's defect rule), in 8 groups of M1 questions covering 27 pairs. For example, «At which point in a member's first months does the app ask for a check-in today?» appears at Smart Fit, Allp Fit, SportClub, Bluefit and Selfit. In mixed-2, the closer «If a short call helps, my calendar is here:» and the line «There is a short page on how FitXpress works inside a fitness app:» repeat across SportClub, Bluefit and Pacto (35 pairs). Other repeats: «Open to a short call?» at 4 companies; «A call can cover the design:» at 3; «FitXpress has web and mobile SDKs with supported iOS and Android integrations.» at 4 (Smart Fit, Pacto, Tecnofit, Fitco).
- **Card text leaking into copy.** Five writer-note sentences: `edgard-corona-5b25164` «This note stays on the product side.»; `itamar-hercolano-junior-53242a63` «The app side is separate from yours, so I will keep it short.»; `marcelo-gildin-03113298` «Mostly this belongs to the app owner.»; `mauricio-amaya-16644a91` «Your title does not name a function…»; `ronald-augusto-campos-836064252` «Dirección covers many areas…». The card word "the chain" shows up in 10 pairs. Card targets are pasted as sentences: «A plan block can end with nothing measured to compare with its start.» appears in 10 SportClub M1s, and the gate counts about 60 M1 questions that copy a card question target.
- **Buyers given an easy out (5).** Edgard Corona (founder), Diogo Corona (CEO), Antonio Maganhotte (P1 chair and co-founder), Alexandre Manarim (P1), Natasha Valencia (co-founder). Two regional CEOs, Camilo Sarasti and Cristián Deppe, are borderline. Every referral M2 has an easy out (no issue there).
- **Pilot design incomplete.** The card says «When offered, name all parts». The rule «if criteria are met, the scan goes live» appears in only 12 of 48 pilot M2s. Eight pilots count only scan completion and retention: max-trombini, priscila, douglas-w, vanessa, wilder, glauber, nicolas-loaiza and tadeu.
- **Boundary line form broken in 8 pairs.** Two say «The scan provides…» (matheus-gonzaga, axel-mendoza). Four open a paragraph with «It provides…» (savio, josenobile, gabriel-ramos, marco-storchi). In two, «It» follows a subject other than FitXpress (andersonbc, diego-brayner).

### B. Factual accuracy: 3/5
- No invented numbers, client names, accuracy figures or country mentions. Edgard Corona is correctly called founder, not CEO. Fast Treino, Wellhub, EVO, BlueUp, SuperBio, Performance Center and Meu Treino are all absent (no issue).
- **Facts carried over from another company's bullet (3).** «registers» is Tecnofit's help-center fact, but it appears for Smart Fit (`nathaliajlima` «body data reaches the profile only after someone registers an in-club exam»), Bluefit (`elson-terakado-data`) and Nextfit (`kevin-marques-916400151`).
- **A card pain target stated as a fact about the company's app (12).** «a weight entry or a photo» is written as what the app holds at Panobianco ×5, BIGG ×3, Spinning Center ×2 and Fitco ×1. At Spinning Center this **contradicts** Account facts: the app lists «control de evolución corporal» (cesar-casallas, ronald-augusto-campos). At Fitco it breaks «never as a gap» (josenobile).
- **App naming.** «the Spinning Center app» appears in 5 pairs; Account facts: «Never use the app names», and one app is called "Spinning Center App". Selfit M1 says «the chain's own app» for a vendor-built app (fernandoduartemenezes). Gaviões copy says «the club's app» twice.
- **Product claims beyond the card (8).** Examples: `luissalvadori` M1 «repeatable between scans» (unapproved repeatability wording, and in M1); `luana-luiza-402309185` «FitXpress returns the data to the profile, nothing more.» (implies 3DLOOK keeps nothing, which contradicts compliance.md); `diegomod` «a capability each gym can switch on»; `adrian-duque-32b348111` «FitXpress extends that valoración into the app». Full list below.
- Sourcing: 3DLOOK links only (page plus calendar), as the card requires. Not applicable for outbound.

### C. Brand & tone: 2/3
- No banned words, dashes or "not just" constructions (gate).
- **About 95 of 189 M2s close with a label before a link.** The gate lists about 60. It misses the 26 mixed-1 closers that end in «:» with the link on the next line, and 10 Smart Fit «Call: <link>» closers.
- **13 openers read as if Kateryna works at the prospect's company, or expose the prospecting.** Examples: «Quick thought as a co-founder of Action Black:» (diego-aguirre), «Wanted to reach out as a partner at Smart Fit.» (savio), «Had a thought as I looked at manager roles at Smart Fit.» (tiago).
- Presumed reaction: «Founders usually ask what it takes to start.» (maganhotte).
- Portuguese words outside the allowed list: «musculação» (nayanarosa); the tagline «A melhor parte do seu dia» quoted in copy (luizurquiza).
- British spellings: «randomised» (cristianogfontes), «personalised» (gigliola).

### D. Format & structure: 2/3
- The batch format matches the card's `@@@` spec, and the gate passed.
- Closing-line layout differs by batch: mixed-1 puts the link on its own line after «:»; mixed-3 runs the page line and the call line with no blank line between them.
- Summaries: the mixed-1 angle line contradicts itself («product 9 (incl. …) … product 8, operations 11 … see grid»). No summary reports the missing pain lines or the cross-company repeats. mixed-2 notes that SportClub reads alike but does not fix it.
- Per-person files have no `product:` frontmatter. The script generates these files and the writer's spec has no frontmatter, so I did not cap D for it. Flagged for the coordinator.

### E. Output quality: 2/4
- Strong company-specific M1s exist: Bluefit manifesto (alessandra), Selfit sensors (eduardoliedbraun), Smart Fit Social tab (pedro/ariane hooks), Frequência Premiada (tadeu), Bodytech Colombia November release (jorge-villa), Tecnofit Partners (jose-eduardo), Panobianco traditional-gym focus (fcastromit).
- Against that, about 120 pairs need an edit. The 10 SportClub M1s are near-identical in body; the writer's own summary says so. A native reader stumbles on: «Members use the app members use to follow their assessments.» (talita-araujo), «…add measurements to what the app members use shows.» (fernandoduartemenezes), «adds one members take on their own phone» (alvarosf, arianedt, edgard). 13 closers put the calendar link straight after «point me to whoever owns X:», so the link reads like that person's contact. This is well over 30 minutes of editing.

## Top 3 issues (priority for improver)

1. **M1 without a method pain line (32 pairs; mixed-4 16/33).** The writer prompt or card needs a pre-submit check per pair: is there a sentence that names what the current method lacks, about the method and not the company? The gate should look for a pain line before the product sentence.
2. **Cross-company repeats and pasted card wording.** Shared closers and page lines across SportClub, Bluefit and Pacto; M1 questions copied from card targets and identical at 3 to 5 companies; «A plan block can end…» ×10. The gate should make "identical sentence at two companies" a hard failure for M1 questions and closers, not just for whole M2s.
3. **Copy craft in closers and hooks.** About 95 label lead-ins, 13 openers that misread as Kateryna working there, 13 «point me to X: <link>» closers, 5 writer-note sentences. The gate misses «label:» followed by a link on the next line, «Call: <link>», and «The scan provides» or a paragraph-opening «It provides» in the boundary line.

## Line-level fixes by batch

Format: `person_id`: «exact sentence» → fix target. Repeat-label notes are grouped per batch to save space.

### smart-fit-1 (35)
- `edgard-corona-5b25164` M1: «This note stays on the product side.» → delete (writer note). «As founder, you see the whole club.» → odd phrase; open on a Smart Fit fact instead.
- `edgard-corona-5b25164` M2: «If this is not yours to weigh, a pointer to whoever owns member-app features at head office would help. Otherwise a call:» → founder: remove the easy out and keep a plain call offer.
- `diogo-corona-722153153` M2: «If a colleague owns member-app features, point me to them.» → CEO: remove the easy out. «The page on fitness apps:» → fold the link into a sentence.
- `camilo-sarasti-samper-3253071a` M1: «3D Body Progress compares the scans the chain selects.» → "the chain" is card wording; name Smart Fit. M2: «A call, or point me to the member-app owner: <link>» → the link must not follow «owner:»; for a regional CEO, decide whether an easy out is warranted.
- `cristián-deppe-alcalde-9b934621` M1: «From expansion to running a whole region is a big step.» → filler flattery. M2: «Rollout is simple to describe.» → vague; give a value point instead. Easy out to a regional CEO is borderline.
- `arianedt` M1: «The Social tab already runs groups, friend challenges and a ranking, which are natural moments for a check-in.» → add a pain line about the method (what the app shows about body change next to a challenge). «…the scans the chain selects.» → card wording. M2: «The page:» → label.
- `luissalvadori` M1: «…linked to the member profile, repeatable between scans.» → remove (repeatability only as the page sentence, in M2). M2: «A call, or a pointer to the member-experience lead: <link>» → he is the head of customer experience, so the easy out points at his own function; and the link follows a colon.
- `nathaliajlima` M1: «In the Smart Fit App, body data reaches the profile only after someone registers an in-club exam.» → not in Smart Fit Account facts; use a Smart Fit fact. «Analytics and martech at Neon and Neoway, then Smart Fit: a useful path for the data side.» → verbless opener.
- `itamar-hercolano-junior-53242a63` M1: «Your headline reads Chief Development Officer at Grupo Smart Fit.» → meta comment on a headline. M2: «The app side is separate from yours, so I will keep it short.» → delete (writer note). «The page:» → label.
- `marcelo-gildin-03113298` M2: «Mostly this belongs to the app owner.» → delete (writer note). «Details:» → label.
- `marcelo-schwed` M1: «A body check-in in a club needs the device and a booked slot.» → Smart Fit Never lists "the device"; make it generic or use the slot and the visit. M2: «…and the club decides where the scan sits.» → Smart Fit (head office) decides.
- `fernando-sebo-benitez-31693810` M1: «…you know each step has to be short.» → presumptive. «…needs the in-club device and a booked slot.» → same device issue as marcelo-schwed. M2: «A call, or a pointer to whoever owns assessments: <link>» → the link reads as the owner's address; restructure.
- `marcela-gonçalves-meirelles-0a2694125` M1: «…needs the device, a booked slot…» → same device issue. M2: «A call, or point me to whoever owns assessments: <link>» → restructure.
- `paola-c%c3%a1rdenas-damian-90198069` M1: «…you know every club type.» → presumptive. «…depends on the in-club device and a booked slot.» → same device issue. M2: «A call, or point me to the national training lead: <link>» → restructure.
- `leandro-ascen%c3%a7%c3%a3o-4b773b117` M2: «Call, or point me to the owner of the assessment protocol: <link>» → restructure.
- `alvarosf` M1: «For a Smart Fit product manager, one observation.» → clunky. «FitXpress, from 3DLOOK, adds one members take on their own phone…» → unclear pronoun. M2: «If a test is useful, keep it to one cohort.» → imperative. «Call: <link>» → label.
- `daniel-martins-tognini-432b02aa`, `liviabarboza`, `matheus-carvalho-09243113b`, `mauro-vieira-baa1b7248`, `nicolas-fernandes-3a8249113`, `phillippoliveira`, `cirodellavolpe`, `moreno-andrade`, `valter-sobral-93832941` M2: «Call: <link>» → a bare label as the closer; write a call offer.
- `nicolas-fernandes-3a8249113` M1: «FitXpress, from 3DLOOK: 2 photos on the member's phone, …» → no verb.
- `mauro-vieira-baa1b7248` M2: «A pilot fits how you work.» → presumptive.
- `moreno-andrade` M1: «After engineering leadership at Mercado Livre and iFood, a technical question.» → fragment.
- `cirodellavolpe` M1: «…a path that sees both sides.» → anthropomorphism. M2: «A plan-level pilot is easy to wire.» → overclaims ease.
- `flavia-campos-de-souza-97587a30b` M1: «…takes a device, a booked slot and a visit.» → same device issue. M2: «The pilot can start in one club or one cohort first.» → «The pilot» has not been introduced.
- `carolina-corona-4784b217` M2: «If the studios sit with someone else, point me to the digital lead for member experience.» → she directs the studios, so this easy out is misaimed. «Covered in more detail here:» → label.
- `lucas-flor%c3%aancio-74a73b18b` M1: «After technical education at head office, technical management is a closer view of the coaches.» → awkward. M2: «Details here:» → label.
- `miriane-bittar` M2: «A short page explains the flow:» → label. `gabrielacarvalhodasilva` M2: «A short page on how it works:» → label.
- `anapaulagulfier` M2: «The page:» → label. `emerson-guimar%c3%a3es-a7465aa1` M2: «The page:» → label; «…or take a call» → odd phrasing. `renato-salinas-5a300a304` M2: «The page on fitness apps:» → label.
- `guilherme-rodrigues-scarcella-418573187` M2: «Your teams would see the same record the member sees.» → a data-access claim not in the card; the chain decides who sees what.
- `mauro-vieira-baa1b7248`, `phillippoliveira` M1: «How does the app team test a new feature on one member cohort?» → identical at Sport City (josé); vary the wording across companies.
- `leandro-ascen%c3%a7%c3%a3o-4b773b117` M1: «How are assessments scheduled across the clubs today?» → identical at Panobianco and Sport City.
- `rooseveltjunior` M1: «At which point in a member's first months does the app ask for a check-in today?» → card target pasted verbatim, and identical at 4 other companies.
- `renato-salinas-5a300a304` M1: «What does your team see of a member's progress in the app today?» → identical at Bodytech and Bluefit.

### smart-fit-2 (15)
- `carolinaviaro` M1: «Plan tiers in the app are familiar ground.» → no pain line; add one. «…which compares scans the chain selects…» / «A chain can place both in a higher plan.» → card wording. M2: «For a premium tier the setup is short.» → vague. «The product page:» → label.
- `pedro-filgueiras` M1: «Groups, friend challenges and a ranking already give members moments to return to.» → no pain line; add one.
- `brunoamaralsilva` M1: «Your headline pairs product and engineering for payments and billing at Smart Fit, which makes this a question from that side.» → clunky. «A body progress view in a higher plan would reach billing as a plan feature.» → not a pain about the method. «…compares scans a chain selects» → card wording. M2: «The product page is here:» → label.
- `thalita-miranda-3a7a47137` M1: «Your background in IT business analysis and internal platforms at Smart Fit is the reason for this note. When a new capability joins the member app, the platform side decides how it connects.» → meta opener, and no pain line. M2: «The product page is here:» → label.
- `savio-niter%c3%b3i-4a368b1a4` M1: «Wanted to reach out as a partner at Smart Fit.» → reads as if Kateryna is a Smart Fit partner. «How do members at your club ask about body change between assessments?» → identical at Bodytech, Pratique and Sport City. M2: paragraph «It provides structured body data for coaching and program workflows.» → when it opens a paragraph it must start «FitXpress provides».
- `tiago-lofiego-serville-1710a7231` M1: «Had a thought as I looked at manager roles at Smart Fit.» → exposes the prospecting. M2: «The scan returns it in a structured form. It provides structured body data…» → says the same thing twice. «More on how it works is here:» → label.
- `stefanoviudes` M1: «What does the app show members about body change between assessments today?» → identical at 4 other companies. M2: «The measurements a trainer sees are waist, hip, chest, thigh and calf…» → reads as Smart Fit's current state; frame it as what the scan returns. «Happy to walk you through it:» → label.
- `isadora-melandes-9b4a48155` M2: «The scan returns structured data the team can read. It provides structured body data…» → says the same thing twice. «The product page is here:» → label.
- `isabel-tobon-7ba340182` M2: «For a partner capability the practical side is small.» → vague. «The product page is here:» → label.
- `adriana-assun%c3%a7%c3%a3o-68a731b6` M2: «For club teams the practical side is short.» → vague. «The product page is here:» → label. M1: «An assessment takes a device and a trainer's time at the club.» → same Smart Fit device issue.
- `jefferson-cunha-173793127` M1: «An in-club assessment needs a device and a slot in the schedule…» → same device issue.
- `rodrigolmartins` M1: «…and the in-club assessment adds body data when a member takes one.» → this is an observation, not a pain; state what the method lacks.

### mixed-1 (Allp Fit 13, Bodytech Company 13)
- **All 26 M2 closers** («Happy to shape the design on a call:», «Or a call:», «A call works too:», «Or we can talk here:» and so on, with the link on the next line) → label lead-ins the gate misses; put the link inside a closing sentence or after a question.
- `cristianogfontes` M1: no pain line (opener, then product, then question); add one. M2: «Counted: scan completion…» → fragment label. «randomised» → American spelling.
- `emerson-maida` M1: «Thought I'd share an idea from the partnerships side at Allp Fit.» → reads as if Kateryna is on Allp Fit's partnerships side. «A partner capability works for members when it sits inside the app they already use.» → not a pain about the method. M2: «The fitness page has more:» → label.
- `luana-luiza-402309185` M1: «Members who want a body check-in between club visits need a clear route to it.» → vague; name what the method lacks. M2: «FitXpress returns the data to the profile, nothing more.» → remove «nothing more» (implied data-handling claim).
- `gabriel-moura-c` M1: «Had a thought as a product owner at Allp Fit.» → reads as if Kateryna is the product owner. M2: «Counted:» → fragment label.
- `jeanpcpierre` M1: «Couldn't help but ask, as COO at Allp Fit.» → reads as if Kateryna is COO. «A body check-in that depends on a club visit adds work to club teams.» → operations lane: do not imply a staff burden.
- `marcelo-vianna-a99724115` M1: «Curious about your take, as COO of Bodytech Company with a product background.» → reads as if Kateryna is COO.
- `gabrielle-weiss-86962b152` M1: «Wanted to reach out, as an operations manager at Bodytech.» → reads as if Kateryna is the operations manager. M2: «A sense of scale: 112,100 scans…» → label.
- `karina-borba-rocha-580152220` M1: «Couldn't help but ask, from the operations side at Bodytech Company.» → same misreading. «…and a club has few measurements to show for it.» → pain about the club, not the method. M1 question is identical at Smart Fit, Pratique and Sport City.
- `amanda-ferrari-6b21251aa` M1: «Made me think, looking at operations at Bodytech Company.» → fragment; reads as if Kateryna is in operations there. M1 question is identical at Smart Fit and Bluefit. M2: «The fitness page:» → label.
- `alan-barcellos-28253019b` M1: «Thought I'd share a note for the operations and products manager at Bodytech Company.» → addresses him in the third person; no Bodytech fact. M1 question is identical at 4 other companies. M2: «Choose one plan and its members scan…» → imperative.
- `b%c3%a1rbara-valente-01898386` M2: «With a product background, you will see the fit quickly» → presumptive. «…the scan returns under 45 seconds from the photos to structured results.» → garbled; the speed wording must be its own plain sentence. «The fitness page:» → label.
- `luizurquiza` M1: «"A melhor parte do seu dia" frames Bodytech…» → Portuguese tagline; describe the concept in English. «A body check-in that needs a club visit stays inside the club.» → says nothing; state the pain. M2: «Measured:» → fragment. «…every member's choice not to scan stay untouched.» → grammar.
- `elisangela-ornellas-953a8824` M1: «…a body check-in that depends on a device and a trainer slot is hard to keep uniform.» → implies Bodytech measures inconsistently; reframe as a point about the method.
- `guilherme-messias-68b34b353` M1: «When a body check-in lives in each club, its timing and format vary by club.» + «How do you keep body check-ins consistent across units today?» → implies inconsistency at Allp Fit.
- `ricardoferamaral` M1: «A plan block in a member app often ends with nothing measured to compare against its start.» → card target near-verbatim. Only «now at Allp Fit» is company-specific; add one Account-facts line. The question is a card target and identical at 4 other companies.
- `andersonfranconeves` M1: «A member app can show workouts done but little about body change.» → generic; tie it to an Allp Fit fact (Allp Fit Home, «O topo é seu!»). M2: «…can be that tier…» → features are not a tier.
- `thaypfx` M2: «The pilot can start in one club…» → «The pilot» has not been introduced.
- `dudunetto` M1: «Between club visits it sits next to the in-club assessment.» → stray sentence with an unclear «it».
- `diogoevangelista` M2: «On repeats:» → label. «The fitness page has the detail:» → label.
- `guilherme-th%c3%a9` M1: «Capture is where a body scan succeeds or fails.» → not about the chain's method, and the question does not follow from it.
- `ricardo-fagundes-98219090` M2: «The yardstick is set before the pilot starts.» → idiom.
- `bruno-ciolli`, `fabianoveloso`, `melina-de-souza-barbosa` M2: «The fitness page covers this:» / «Details are on this page:» / «The fitness page explains the idea:» → labels.

### mixed-2 (SportClub 12, Bluefit 12, Pacto 11)
- **Closers across companies:** «If a short call helps, my calendar is here: <link>» and «There is a short page on how FitXpress works inside a fitness app: <link>» are identical at SportClub, Bluefit and Pacto → keep one wording per company.
- **SportClub M1** (`gustavo-pricolo-b9467690`, `adrian-anaya-03467993`, `diego-palacio-5910b910a`, `gerardo-diaz-50b033152`, `german-ariel-garcia-pf`, `gisela-ciccone-25804a20`, `maría-valeria-fernandez-pelayo-62b51036`, `matiashotano`, `pablo-fedelich-1a0994168`): «A plan block can end with nothing measured to compare with its start.» → card target pasted verbatim; write it in the writer's own words, and vary it by role.
- `gustavo-pricolo-b9467690`, `alessandra-mattos-sekeff` M1: «At which point in a member's first months does the app ask for a check-in today?» → card target verbatim, and identical across companies.
- `danila-de-marchi-0433a0178` M1: no pain line. «Would a body-scan capability from a partner have a place in what SportClub offers members?» → card target verbatim.
- `renata-cadenas-5b76ba180` M1: no pain line («FitXpress is a white-label body scan…» comes straight after the opener).
- `patricia-rocha` (`patr%c3%adcia-rocha-772971210`) M1: no pain line («Members get their assessment results on their phone…» and then the product).
- `talita-araujo-0816b73a` M1: «Members use the app members use to follow their assessments.» → robotic substitution of the card phrase.
- `nayanarosa` M1: «…a musculação and gymnastics teacher…» → Portuguese word. M1 question is identical at Smart Fit and Bodytech. M2: «Something for the training floor.» → idiom.
- `elson-terakado-data` M1: «Assessment results reach members' phones after someone registers them in the club.» → not in Bluefit facts (Tecnofit's fact).
- `edson-santos-b26281209` M2: «Point me to them if that is not you.»; `felipe-marcon` M2: «If that is not you, point me to that person.»; `higor-duarte-9a4a96430` M2: «If that is someone other than you…» → condescending; they are plainly not the head-office owner.
- `higor-duarte-9a4a96430` M2: «The decision on this sits with the national technical lead.» → states a Bluefit org fact that is not in the card.
- `matiashotano` M2: «This kind of decision sits with the owner of member-app features at head office. If that is another person, point me to them.» → garbled.
- `maría-valeria-fernandez-pelayo-62b51036` M2: «Why this fits a club.» → fragment. Speed wording merged into a clause.
- `gerardo-diaz-50b033152`, `bruramalho`, `diego-tavares-b117183a`, `patr%c3%adcia-rocha-772971210`: «…returns 80+ body measurements under 45 seconds from the photos to structured results» → the speed wording must be its own plain sentence.
- `pablo-fedelich-1a0994168` M2: «A note on track record:» → label. `german-ariel-garcia-pf` M2: «On consistency:» → label.
- `delcio-lu%c3%ads-pinto-04b4aa49`, `eduardoolivsantos`, `lailan-matos-776b99168`, `adriano-oliveira-cloud` M1: no pain line. Each goes from a fact about App Treino straight to the product.
- `diegomod` M2: «Think of it as a capability each gym can switch on.» → a per-gym toggle is not in the facts.
- `leonan-sihid-souza-81a174166` M2: «Start with one gym.» → imperative. «chosen by lot» → idiom.
- `elias-roberto-dos-santos-j%c3%banior-901624196` M1: «With a QA background, you know what a clean record looks like.» → presumptive.
- `lailan-matos-776b99168` M2: «FitXpress has web and mobile SDKs with supported iOS and Android integrations.» → identical at Smart Fit, Tecnofit and Fitco.

### mixed-3 (Panobianco 10, BIGG 7, Spinning Center 7, Tecnofit 6)
- **Repeats across companies:** «Open to a short call?» (Panobianco, BIGG, Spinning Center, Tecnofit), «The product page shows the flow:» (Panobianco, BIGG, Spinning Center) and «Overview:» in 9 or more pairs → vary by company; fold each link into a sentence.
- `celiamizukosi` M1: «…body change in between is a weight entry or a photo.»; `rafael-panobianco-466a721a8` M1: «Between two assessments, body change is a weight entry or a photo, with no measurements to compare.»; `rafael-lucena-46119741b` M1: «…a member's progress is often a weight entry or a photo.»; `vilma-brasileiro-694677439` M1: «…a progress photo or weight entry has no measurements next to it.»; `thyago-alves-carneiro-dos-santos-1b9436128` M1: «A plan block can end with only a weight entry…» → each is stated as a Panobianco app fact, which Account facts do not support. Make it a point about the method, or use the assessment-date fact.
- `celiamizukosi` M2: «Another angle for the brand side:» → label. M1 question is identical at 4 other companies.
- `rafael-panobianco-466a721a8` M2: «Easy to try small:» → label.
- `natalia-mayumi-ba61ba224` M2: «…and each club sees the same record.» → a data-access claim not in the facts.
- `vilma-brasileiro-694677439` M2: «If this sits with another team, the value is one structured record per scan…» → illogical conditional.
- `guirocha79` M1: «As COO you own how assessments run across the clubs.» → presumptive. The question is identical at Smart Fit and Sport City.
- `francisco-bosch-b0a07233` M1: «…the goal sits next to a weight entry or a photo, with no measurements.»; `martin-bottini-3a789014` M1: «The goal sits next to a weight entry or a progress photo, with no measurements to compare.»; `octaviobarticciotto` M1: «In the app, the goal sits next to a weight entry or a photo…» → not in BIGG facts (goals and plans only).
- `guido-giambruni-295a2a1a2` M1: «Process and data work shows in how BIGG's app picks each member's four blocks from their goal.» → garbled. «…because a measurement in a club needs a device and a visit.» → BIGG is in the plan branch with no published in-club measurement.
- `gigio-mazzoni-ba358797` M2: «A second point on the goal side.» → odd. `francisco-bosch-b0a07233` M2: «Or open a short call here:» → odd.
- `ruben-baquero-48b325b3`, `cesar-casallas-8178b07b`, `marcela-palencia-rodríguez-5706a5288`, `mauricio-amaya-16644a91`, `ronald-augusto-campos-836064252` M1: «the Spinning Center app» → Account facts say never use the app names; use "your app" or "the app members use".
- `cesar-casallas-8178b07b` M1: «Between valoraciones, the app can hold a weight entry or a photo, with no measurements to compare.»; `ronald-augusto-campos-836064252` M1: «A progress photo or a weight entry between two valoraciones has no measurements to compare.» → contradicts Account facts («control de evolución corporal» is in the app).
- `mauricio-amaya-16644a91` M2: «Your title does not name a function, and this touches the app and the training program.» → writer reasoning leaked, about an empty profile; delete. M1: «…under the chain's brand.» → card wording.
- `ronald-augusto-campos-836064252` M2: «Dirección covers many areas, and this one touches the training program and the member app.» → delete. «…and the chain decides where it sits.» → card wording.
- `marcela-palencia-rodríguez-5706a5288` M1: «The chain keeps its own brand and consent wording…» → card wording. «How often do members repeat their valoración, and what triggers a repeat?» → card target verbatim.
- `adrian-duque-32b348111` M1: «FitXpress extends that valoración into the app…» → overclaim; the scan is separate from the trainer's assessment.
- `xioma` M2: «For scale:» → label. `ruben-baquero-48b325b3` M2: «For the trainers:» → label. «valoración» and «valoraciones» throughout Spinning Center copy fall outside the card's allowed terms (avaliação física, evaluación física); coordinator to rule.
- `maganhotte` M2: «Founders usually ask what it takes to start.» → presumed reaction. «If your product lead is the right person, a pointer is enough.» → P1 chair and co-founder: remove the easy out.
- `josé-eduardo-hunzicker-antunes` M1: «FitXpress is that SDK:» → label. `rafaelalaurencini` M2: «On the product side:» → label.
- `andersonbc` M1: no pain line. M2: «For the review:» → label. «The recommended setup is the SDK with the API. It provides…» → «It» must follow FitXpress or the scan. «FitXpress has web and mobile SDKs…» → identical across companies.
- `rodolfo-jesus-506556203` M1: «Engineering leads decide how an SDK enters an app.» → generic and presumptive. M2: «Technical detail:» → label.

### mixed-4 (Cia Athletica 6, Gaviões 6, Nextfit 6, Bodytech Colombia 5, Action Black 5, Pratique 5)
- **No pain line in M1 (16).** Add a pain line about the method before or around the product sentence:
  - `jorge-alves-b60894127` «CiaOn already carries each member's weekly schedule and training evolution.»
  - `leandro-aguiar-a86b7039b` «…members see their avaliação física in the app they use and train at hours they choose.»
  - `alexandre-leandro-manarim` «The student app already shows workouts, load progress and assessment history.»
  - `douglas-waltricke-42579a152` «Nextfit's student app already shows each gym's members…»
  - `vanessaugioni-146b92188` «…a body measurement from the member's own phone is a candidate idea.»
  - `yfagundes` «…a gym could offer more in a higher plan.»
  - `gigliola-aycardi-batista-b1a5b21b6` «A body measurement record would sit naturally next to that plan.»
  - `jorge-villa-aguilar-0129521ab` «A body check-in with no device, no trainer slot and no club visit would add to that.» (also card wording)
  - `nicolas-loaiza-9134a1447` «These give members more reasons to open the app between visits.»
  - `oscar-maldonado-90796aa` «…a new data source would arrive through an SDK and an API.»
  - `rafaelsocarras` «App Bodytech is where members already see a monthly plan that adapts to their progress.»
  - `wilder-zapata-torres-81787a15` «At Action Black, members book, check in and follow their progress in the Action Black app.»
  - `natasha-valencia-11562a1a2` «One candidate for Action Black: a body check-in members take on their own phone.»
  - `esteban-lozada-3876a9b8` «At Action Black, the Action Black app already handles bookings and QR access.»
  - `tadeu-pratique-05137521` «A body check-in could sit inside that loop.»
  - `glaubermalta` «…both depend on clean records.» (also a non sequitur)
- `max-trombini-600b14a` M1: «Quick one as owner of Cia Athletica.» → reads as if Kateryna is the owner (and the profile is empty). M2: «Part of the new members scan…» → grammar.
- `diego-aguirre-bustamante-3227a22b5` M1: «Quick thought as a co-founder of Action Black:» → reads as if Kateryna is a co-founder.
- `alexandre-leandro-manarim` M2: «If this belongs with the founder, point me there.» → P1: remove the easy out. «Students would see something like this:» → label.
- `natasha-valencia-11562a1a2` M2: «If product ideas go through someone else, point me to the digital lead.» → co-founder: remove the easy out.
- `kevin-marques-916400151` M1: «In the student app, an assessment appears after the gym registers it.» → this is a Tecnofit fact; use a Next Fit fact.
- `michelle-mithie-tonelli-eugenio-338ab86a` M2: «FitXpress sits in the club's app…»; `rodrigo-alaminos-a172481a7` M1: «…in the club's app.» → the app is vendor-built; write "the app members use".
- `tadeu-pratique-05137521` M1: «…a habit loop members open daily.» → unsupported usage claim.
- `gigliola-aycardi-batista-b1a5b21b6` M1: «personalised» → American spelling. M1 question is identical at 4 other companies.
- Pilot M2s that count only completion and retention: `max-trombini-600b14a`, `priscila-aguiar-33695076`, `douglas-waltricke-42579a152`, `vanessaugioni-146b92188`, `wilder-zapata-torres-81787a15`, `glaubermalta`, `nicolas-loaiza-9134a1447`, `tadeu-pratique-05137521` → name all parts (retakes, repeat scans, onboarding completion).
- `priscila-aguiar-33695076` M2: «…for trainers' calls…» → ambiguous for second-language readers.
- Questions identical across companies: `viviane-roque` / `glaubermalta` «What would a check-in that runs outside the club change for club teams?»; `jorge-villa-aguilar-0129521ab` / `adriano-madureira-23710121` «How are assessments scheduled across your clubs today?»; `adolfo-mac-34749b230` «How do members at your club ask about body change between assessments?» → vary across companies.
- «A call can cover the design:» (`douglas-waltricke-42579a152`, `vanessaugioni-146b92188`, `nicolas-loaiza-9134a1447`, `tadeu-pratique-05137521`, `glaubermalta`) → same closer at Nextfit, Bodytech Colombia and Pratique.
- Labels in M1: `viviane-roque` «FitXpress makes that possible:», `rafaelsocarras` «FitXpress would add a measured side:», `felipe-pavas-7b69692bb` «FitXpress removes the visit:», `anderson-trindade-teixeira` «FitXpress adds measurements to that program:».
- Labels in M2: `richard-lati-8081a072` «The member view is shown here:», `adriano-madureira-23710121` «The member side is described here:», `anderson-trindade-teixeira` «See the member side here:», `adolfo-mac-34749b230` «One page covers the member side:», `wilder-zapata-torres-81787a15` «Happy to walk through it:», `rafaelsocarras` «Happy to walk through the setup:», `jorge-villa-aguilar-0129521ab` «For the member side, see:», `gigliola-aycardi-batista-b1a5b21b6` «The member journey is laid out here:».
- `thais-ferreira-gomes` M1: «…you decide how new capabilities reach the student app.» → presumptive. «…the student takes alone» → odd. `esteban-lozada-3876a9b8` M1: «…know what every SDK costs an app.» → presumptive.

### mixed-5 (Selfit 5, Fitco 4, Sport City 4, Megatlon 2)
- `fernandoduartemenezes` M1: «Between assessments, a record from the phone would add measurements to what the app members use shows.» → garbled. «FitXpress works inside the chain's own app and brand…» → the Selfit app is vendor-built (Whose-app ruling), and "the chain" is card wording. The question is a card target and identical across companies.
- `diego-brayner-b7976167` M1: «…under the chain's brand.» M2: «The record uses the chain's own consent wording and brand…» → card wording. «It provides…» follows «The record…». The closer puts the link after «at Selfit:».
- `matheus-gonzaga-aa094420` M2: «Continuing your question:» → it was Kateryna's question. «The scan provides structured body data…» → must be verbatim (only «FitXpress» may replace «It»). «A product page for fitness apps:» → label. The closer puts the link after «head office:».
- `axel-mendoza-874a586a` M1: «Wanted to reach out as Fitness Director at Sport City.» → reads as if Kateryna is the Fitness Director. M2: «The scan provides structured body data…» → not verbatim. «…and the club chooses where members see it.» → head office decides. The closer puts the link after «head office:».
- `josenobile` M1: «Wanted to reach out on SDK reviews: you spent years as a site reliability engineer before Fitco.» → non sequitur. «Studio apps on Fitco hold a weight entry or a progress photo with no measurements to compare.» → Fitco Use says never frame the weight, BMI and body-fat view as a gap. M2: paragraph «It provides…» → must start «FitXpress provides».
- `gabriel-ramos-24a16221a` M2: paragraph «It provides…» → «FitXpress provides». The closer puts the link after «at Sport City:». The M1 question is identical at Smart Fit and Panobianco.
- `marco-storchi-68112a15b` M2: paragraph «It provides…» → «FitXpress provides».
- `eduardoliedbraun` M1: «A check-in on the member's phone needs no device, no trainer slot and no club visit.» → card target near-verbatim. «How are physical assessments scheduled across Selfit clubs today?» → Selfit publishes no in-club assessment (thin branch), so avoid detail about how Selfit assesses.
- `weldon-neto-a61223178` M2: «…or you can point me to whoever owns the training program at head office: <link>»; `andrea-ruiz-cs-kam` M2: «…or to be pointed to whoever owns product at Fitco: <link>»; `fernando-storchi-303121124` M2: «…or point me to whoever decides member-app features: <link>» → the link reads as that person's contact; restructure.
- `ggarciacardone` M1: «Would you see 3D progress in a higher membership plan at Sport City?» → odd for second-language readers.
- `jos%c3%a9-antonio-su%c3%a1rez-l%c3%b3pez-38b2282ab` M2: «A product page for fitness apps:» → label. M1 question is identical at Smart Fit. («Hi José,» is correct per the card; the gate's greeting note can be ignored.)

## Notes for coordinator (gate gaps seen in this run)
- The gate misses «label:» followed by the link on the next line (26 in mixed-1) and «Call: <link>» (10 in smart-fit-1).
- The gate does not check the boundary line's form: «The scan provides…», or «It provides…» opening a paragraph.
- The gate treats identical M1 questions and closers at different companies as soft notes. Under Vadim's rule they are defects.
- notify.py was not run: this QC session has no shell tool.

## Coordinator review

agreement: ✅ agree (Edgard's writer note was also caught by the coordinator's own scan; 12 cross-company twins had already been reworded by the coordinator before QC)
top_issue: M1 without a pain line (32) and label/colon closers (~95); fix round 1 = per-batch `_fix-<batch>.md` (12 round rules + these named lines), the same 7 writers resumed
