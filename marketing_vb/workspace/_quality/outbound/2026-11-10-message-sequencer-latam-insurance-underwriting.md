# QC: step 5 messages, 2026-11-05-latam-insurance-underwriting (126 pairs, dump of 2026-11-10)

I read all of `card-messages.md` (704 lines) and all 126 pairs. I did not run `notify.py` and did not write a report file, as instructed. Frontmatter on the per-person files was not checked because the dump has none.

## 1. Score: 10/20, failed (rubric threshold for failed is under 12)

| | Score | Why |
|---|---|---|
| A. Adherence | 2/5 | Five card rules break across many pairs, not one-offs: question-bank discipline (sameness), lane notes pasted as copy (12), evaluation design (11), the flag missing from M1 (3), data handling missing from a technical-integration M2 (2). Some Use anchors went to the wrong person (5). |
| B. Factual | 2/5 | Hard cap: two numbers are not in the allowed list ("36 years", "Fifteen years"). On top of that, 21 pairs state what a form asks when the bullet says that form was not seen, not found, or only "has asked". There are also small slips, e.g. the September source describes the flow, but the message says it was "announced in September". |
| C. Brand & tone | 2/3 | No banned words or dashes. One line reads as distrust of applicants (javier-bernat). There are about 25 contorted sentences, idioms or dangling references, and one ungrammatical sentence. |
| D. Format | 2/3 | Lengths pass. Four greetings include a surname. In 47 M2s the easy-out runs on after the URL on the same line. 17 links or call offers are introduced by a label ("Overview:", "Calendar:"). |
| E. Output quality | 2/4 | 22 of 126 pairs can go as they are. 104 need a change: 83 substantive, 21 minor. Many M2s are bolted on, and the M2 skeleton plus several value sentences repeat from company to company (MSG-7 risk). |

By the rubric, failed means regenerate. My recommendation is narrower: run a fresh-writer fix round per company on the table below rather than a full regeneration. The claims and compliance layer is clean (see "What held").

**What held, all 126 pairs:**
- The decision line appears exactly once, in M2.
- 3.5% appears only in underwriting, medical or reinsurance M2s, always with "not a scale reading".
- 112,100 and 100+ go only to CEO or head-of-business readers.
- No DPS to Mexico-located readers.
- No prospect is named in another prospect's copy, and no country is mentioned to a reader in the other country.
- Nothing claims FitXpress decides, verifies, works with insurers, works in Latin America, was validated on local people, or keeps data with the insurer.
- The Bradesco mortgage DPS appears only in Almir's and Thiago Sousa's messages and is never attributed to Bradesco Vida e Previdência.
- HSBC is named correctly. Alexandra and Beltrando use "has asked" correctly.

## 2. Systemic findings (most important first)

1. **The copy states what a form asks when the source says it was not seen (21 pairs, plus 2 softer).**
   - Bradesco Vida e Previdência's own DPS (8): bernardo-castello, estevao-scripilliti, alessandro-malavazi, marcos-scherer-2688a128, jos%c3%a9-luiz-fontes, fernando-mendon%c3%a7a-8b47855, marcio-gliosci-39b634106, fabio-magalh%c3%a3es-.
   - BBVA VidaSegura (7): nachogarciacanton, sandra-nacul-méndez-60693736 ("the applicant's weight is simply stated"), liliana-r-1052a38, luis-hidalgo-50216b12b, fernando-campos-garcía-850716a3, h%c3%a9ctor-ju%c3%a1rez-lara-4a35a028, daniel-oliva-becerra-a9665996.
   - Brasilseg (2): thiago-affonso-borsari-29456365, júlio-cezar-oliveira-oliveira-393b5444.
   - Banorte (2): luis-pi%c3%b1%c3%b3n-2053b7145, eduardo-guti%c3%a9rrez-rojo-712930103.
   - AXA, present tense where the source only supports "has asked" (2): estelle--hascoet, tonantzintapia.
   - Softer, implied: HSBC (jose-antonio-palacio-junco-a8675576, "the declared weight"); Allianz (caio-souza-787b8215, "opens with the DPS").
   - Fix target: say that nobody measures the applicant, and ask how height and weight are recorded.

2. **Sameness inside one company (about 40 pairs).**
   - **Icatu M2 value lines:**
     - 80+ measurements as the value, 4 times (andreolivacarneiro and l%c3%adgia-abreu are nearly word for word).
     - The same "the scan returns X, under 45 seconds…, stays inside…" template, 4 times (rodrigopadova, humberto-sardenberg, ingrid-pereira-39a8882b, luciana-bastos-83b96a23).
     - Beatriz and Priscilla have the same M2 and the same closer.
     - Jimmy and Pier open M2 with the identical 3.5% sentence.
   - **Icatu M1 anchors reused:**
     - The DPS-guide line 5 times (leonardohijino and priscilla-teixeira-58140031 word for word).
     - Routing with "on both paths height and weight are stated" (césar-saut-5444563b4 is nearly identical to rafael-saile-90296635).
     - Pending items cleared by link, 3 times.
     - The product sentence of rafael-saile-90296635 and pierietto is the same.
   - **RGA:** the "client conversation is short: one record and the threshold" M2 appears 3 times. Dominique and Jesus share the same easy-out sentence, one word apart.
   - **"For [audience]:" M2 openers:** Allianz 7 of 8, AXA 6 of 7, MAPFRE 5 of 7.
   - **Azos:** 8 of 13 M1s open on career background. rodrigo-cteixeira and julia-martins-pm open almost the same way. The drop-off question appears 3 times.
   - **Bradesco questions:** the innovation-to-life handoff question 3 times, the criteria question 2 to 3 times, the DPS-to-exam question 2 times. Two openers share the shape "X came before Y". "The route stays" is the M2 value 5 times.
   - **BBVA:** the "second source" question 3 times, "is the reason for this note" 2 times, "For [area] at BBVA Seguros México, one point" 2 times.
   - **SCOR:** Rafael Zimmer and Francisco have the same question and the same M2 argument.
   - **Repeated 45-second sentence:** the identical sentence appears at MAG (2), Azos (2) and BBVA (2).

3. **M2 is not written for silence: the value line does not continue the person's M1 question (about 25 pairs).**
   - 80+ bolted on as the value (12).
   - No value line at all, just a link (sergio-egidio-31321b170, bernardo-dieckmann-8a399678) or a single bare sentence (eugenioguerimjr-198b8924).
   - M2 repeats M1 (gustavo-oliveira-guga-969114145, fabio-magalh%c3%a3es-, luis-pi%c3%b1%c3%b3n-2053b7145, joão-caproni-1ba34189).
   - A scale or speed line bolted on (ney-ferraz-dias, césar-saut-5444563b4, júlio-cezar-oliveira-oliveira-393b5444).

4. **Evaluation or test offers outside the four-part design (11).**
   - marco-giorgetti-824bbb23 would time live proposals. renatotfarias and heloisa-falcão offer live pilots. josefielloureiro offers a "first test".
   - These name only some of the four parts: carlos-am%c3%a9rico-pugliesi-figueiredo-1631bb14, rafael-lopes-ribeiro, nachogarciacanton, pedro-lopez-comision-de-honor-b50a0835, liliana-r-1052a38, fernando-campos-garcía-850716a3.
   - tonantzintapia counts flags afterwards against extra premiums, which implies live use and a check after issue.
   - Optional, all 10 full designs: none counts how many flags match a gap between declared and measured weight, although the card lists that under what is counted.

5. **Lane-note questions pasted almost word for word (12).** rafael-saile-90296635, pierietto, bernardo-dieckmann-8a399678, fabio-morita, felipe-orozco-8287b5142, acalazans, thiago-dos-santos-sousa-4a0bb722, pedropaulof, ana-bobis-382975a9, liliana-r-1052a38, tonantzintapia; juanorp turns the lane note into a statement. Across companies the questions are identical: felipe-orozco = acalazans, liliana-r = tonantzintapia.

6. **Plain-English problems for second-language readers.**
   - Labels in front of links or call offers (17), e.g. "Overview:", "Calendar for a technical call:", "Call:", "Privacy FAQ:".
   - Dangling "It", "them", "this", "If not", "Or" (about 15).
   - Contorted openers (about 10).
   - Idioms: "wrong desk", "Not your call?", "Not yours?", "like-for-like", "in the loop", "send me their way", "come to mind".
   - One ungrammatical sentence (tonantzintapia).

7. **Rule misses the script cannot see.**
   - M1 has no flag: josemilson-silva-132851b, caio-souza-787b8215, efrainb.
   - Technical-integration M2 has no data-handling sentence: andreolivacarneiro, felipe-octavio-gutierrez-manjarrez-a87b5224.
   - Numbers outside the allowed list: marco-giorgetti-824bbb23, larissa-althoff-71907094.
   - Surname in the greeting: fabio-morita, júlio-cezar-oliveira-oliveira-393b5444, bernardo-correa-ribeiro-73620394, pedro-lopez-comision-de-honor-b50a0835.
   - The 45-second line is not its own sentence in 10 pairs, or is used where speed is not the point (pedropaulof, luishenriquefontes).
   - The easy-out points to the reader's own function: liliana-r-1052a38.
   - Claims that go too far:
     - leonardohijino: "whether an exam still follows" (suggests the scan replaces exams).
     - eduardo-correa-6a5bb89: "handles it" (suggests the scan measures).
     - fernando-mendon%c3%a7a-8b47855: "one backlog item" (claims integration effort).
     - julia-martins-pm: "one more tap" (understates two photos).
     - marco-giorgetti-824bbb23 and dayana: imply the step is on every proposal or application.
     - javier-bernat-a16397162: "whatever height and weight the applicant gives".
     - luishenriquefontes: "The privacy FAQ answers the data questions" (the FAQ is written for US and EU law).

8. **Format.**
   - 47 M2s put the easy-out after the URL on the same line: MAG 9/9, Azos 13/13, BBVA 13/13, HSBC 1, Swiss Re 4/4, SCOR 4/4, Hannover Re 3/3. These are not repeated in the table below; one pass per company fixes them.
   - 15 more put the easy-out on the line after the link.
   - Target: the calendar link last, on its own line, with the easy-out above the call line.

## 3. Per-person fix list

[minor] marks a small fix. Where two people at one company collide, only one of them is listed for that point.

| person_id | Msg | Exact sentence | Problem | Target |
|---|---|---|---|---|
| guilherme-haraguchi | M1 | "...with a flag only when declared and estimated weight differ by more than Bradesco Seguros decides." / "How does a new step get tested in the app journey before it reaches life?" | Awkward; "reaches life" is unclear; same handoff question as felipeszuster | Flag in plain words; one question on his own app journey or Minhas Proteções that nobody else at Bradesco gets |
| guilherme-haraguchi | M2 | "The 80+ body measurements sit in it too and stay unused unless Bradesco Seguros wants them." / "Should someone else own it..." | Bolted on; "it" has no clear referent | Value that continues his app-journey question; easy-out with a clear referent |
| josefielloureiro | M1 | "When innovation proposes a new step for the life journey, which team picks it up first?" | Same question as felipeszuster | Question on his data remit |
| josefielloureiro | M2 | "A first test can stay small: Bradesco Seguros chooses where the step appears, and nothing reaches acceptance." / "If it sits elsewhere, a pointer to whoever owns the digital life application." | Test offer outside the design; same value as jos%c3%a9-luiz-fontes; easy-out is a fragment | Value tied to his new question, with no test offer; easy-out as a full sentence |
| ney-ferraz-dias | M1 | "Spotted something in your group remit at Bradesco Seguros:" | [minor] Odd idiom | Plain reference to his group CEO remit |
| ney-ferraz-dias | M2 | "For scale: 112,100 scans in 2025 across all 3DLOOK customers." | Label fragment; the scale line must be its own sentence and is not tied to his group-or-life question | Value on where the decision sits; if the scale line stays, as its own sentence |
| thais-polegato-1822003a | M2 | "If not, point me to whoever leads life acceptance rules." | [minor] Dangling "If not" | Easy-out with its own condition |
| dirlei-jordão-96246b40 | M1 | "Between insurance and investments in your remit at Bradesco Seguros, I would look at the insurance side: ..." | Contorted | Plain opener on the insurance side of his remit |
| dirlei-jordão-96246b40 | M2 | "Each scan returns one structured record per applicant, and Bradesco Seguros keeps its current route for anyone who does not scan." | Generic; "the route stays" cluster | Value tied to how the life side records height and weight |
| almir-ximenes-25a8aa4b | M1 | "Bradesco Seguros staff see what the applicant states." / "How do your reviewers handle height and weight on cases with no positive answer?" | Unclear sentence; the question assumes he leads the reviewers (his Use asks who reviews) | Question that does not assume ownership |
| caio-mastronell-86a67758 | M1 | "When a proposal moves from the DPS to an exam, what part do height and weight play?" | Takes Abelardo's DPS-to-exam topic | Question on his Use: which team decides the DPS route |
| caio-mastronell-86a67758 | M2 | "The applicant does 2 photos and nothing more, and the route stays Bradesco Seguros's own." | Ungrammatical; "the route stays" cluster | Value that continues the route-ownership question |
| marcos-scherer-2688a128 | M1 | "...the health declaration is part of that sale. On declaration cases height and weight are stated." | Breaks a Never: Bradesco Vida e Previdência's own DPS content was not found | Say nobody measures; ask where the Vida Viva DPS is filled in |
| marcos-scherer-2688a128 | M2 | "If I have the wrong desk, please point me to..." / "A call is the fastest way:" | Idiom; "fastest way" to what; does not continue his drop-off question | Completion measured in the evaluation; plain easy-out; closer with a clear object |
| felipeszuster | M1 | "It is a step of 2 photos that returns a weight estimate, ..." | [minor] "It" has no referent | Name the product as the subject |
| bernardo-castello | M1 | "...flow, announced in September, ..." / "Inside it, declaration cases rest on the applicant's own entries for height and weight." / "Where in the flow's criteria do height and weight sit today?" | Source describes the flow, not an announcement; breaks a Never; question duplicates Gabriel's | Describe the flow as how the company works; no claim about the DPS; question on his CEO seat and who owns the criteria |
| estevao-scripilliti | M1 | "On those, the applicant's own entries supply height and weight." | Breaks a Never | Say nobody measures, or drop the sentence |
| alessandro-malavazi | M1 | "...when Bradesco Vida e Previdência's automated flow hands a case to a specialist underwriter, height and weight on declaration cases are stated." | Contorted; breaks a Never | Plain sentence on the cases handed to specialists |
| alessandro-malavazi | M2 | "It returns 80+ body measurements, under 45 seconds from the photos to structured results." | Dangling "It"; 80+ leads; 45-second line not its own sentence; not tied to the handoff | Value on what a specialist sees at the handoff |
| pedropaulof | M1 | "...which puts declared height and weight into that pricing question." / "How do you weigh extra premiums tied to height and weight against the cost of evidence today?" | Implied DPS claim; lane-note question instead of his Use | Question on pricing Vida Viva's wider cover for older applicants |
| pedropaulof | M2 | "The scan runs under 45 seconds from the photos to structured results." / "Another team may set Vida Viva pricing rules, and a name there would help me just as much." | Speed is not the point for pricing; easy-out has the same shape as Thiago Sousa's | Value tied to his pricing question; easy-out with a different shape |
| marcio-gliosci-39b634106 | M1 | "As a Bradesco Seguros underwriting manager you handle life proposals decided on a declaration, with height and weight coming from the applicant's own entry." | Asserts his line (unknown after the 11-10 relane) and the DPS content | Ask about his work; assert neither |
| thiago-dos-santos-sousa-4a0bb722 | M1 | "Underwriting at Bradesco Seguros is your background." | It is his current job, not his background | Name his current role plainly |
| thiago-dos-santos-sousa-4a0bb722 | M2 | "...on a like-for-like basis." / "...the name of its underwriting rules owner would help just as much." | Idiom; easy-out shape same as Pedro's | Plain wording; a new easy-out shape |
| gabriel-nobre-soares-9165ab123 | M1 | "It works from 2 photos and a Smart Scales estimate, ..." | "It" has no referent | Name the product |
| gabriel-nobre-soares-9165ab123 | M2 | "...which a modelling team can store as inputs." | Suggests the estimate feeds models, beyond its use as a referral trigger | Value on where a threshold would sit in the acceptance criteria |
| fernando-mendon%c3%a7a-8b47855 | M1 | "In that journey, height and weight come from the applicant's own entry." | Breaks a Never | Say nobody measures |
| fernando-mendon%c3%a7a-8b47855 | M2 | "The SDK step is small enough to be one backlog item, ..." / "A call would settle it quickly:" | Unsupported integration-effort claim; dangling "settle it" | Value from SDK and record facts only; closer with a clear object |
| denisnesi | M1 | "FitXpress is an SDK step: 2 photos, a weight estimate, a flag above a threshold the insurer sets, one timestamped record by API." | Same colon-list as reisedilson | Different structure, leading with the photo capture his review sees |
| denisnesi | M2 | "Vendor reviews may run through someone else, and a coordinator's name would be as good." | Vague function; repeated easy-out shape | Name the function that runs security review |
| abelardo-filho-39486487 | M1 | "Below it, the applicant's declaration is the only source for them." | [minor] "them" (height and weight) not yet mentioned | Name height and weight |
| fabio-magalh%c3%a3es- | M1 | "Leading commercial teams in São Paulo and Rio came before your seat at Bradesco Vida e Previdência." / "...a life application with declared height and weight is one more form to fill." | Inverted "X came before Y" shape (as Campilho); DPS claim | Plain hook on his commercial remit; no DPS claim |
| fabio-magalh%c3%a3es- | M2 | "It is one more step of 2 photos for the applicant, and the route stays as it is for anyone who skips it." | Dangling "It"; repeats M1; no value | Value answering what the sales network needs |
| fernandocampilho | M1 | "Data and AI came before Bradesco Seguros technology in your career." | Inverted shape | Plain hook |
| fernandocampilho | M2 | "On integration: a REST API and SDKs." | Same opener as reisedilson | Opener tied to his proposal-platform or underwriting-system question |
| jos%c3%a9-luiz-fontes | M1 | "Launches in 2026 ... run from a product sold without a DPS to ..." / "Where a DPS stays, the applicant supplies height and weight." | "run from… to" idiom; breaks a Never | Plain list of the two launches; no DPS claim |
| jos%c3%a9-luiz-fontes | M2 | "...and Bradesco Vida e Previdência decides where it appears." | Same value as josefielloureiro | Value tied to his declaration-evidence question |
| rachel-ferreira-bonel-85583a73 | M2 | "Handling, in short." | [minor] Fragment | Full sentence or drop |
| bernardocarneiro | M1 | "...through links sent by email or WhatsApp, which is the stack a capture step would join." | Rodrigo Pádova's anchor; a link flow is not a "stack" | Anchor on an SDK step in the application stack |
| bernardocarneiro | M2 | "Calendar for a technical call:" / "send me their way" | Label; idiom | Call offer as a sentence; plain easy-out |
| andreolivacarneiro | M2 | "Along with weight and BMI, the record carries 80+ body measurements, ..." | No data-handling sentence; says "weight", not "weight estimate"; nearly the same as Ligia's | One or two verbatim data-handling sentences; value tied to his question |
| eduardo-correa-6a5bb89 | M1 | "A short phone step handles it: ..." | Suggests the step measures the applicant | Say what comes back, without "handles it" |
| eduardo-correa-6a5bb89 | M2 | "The use case on one page:" | Label; the link opens the M2 | Value first; link introduced by a sentence |
| rodrigopadova | M2 | "A scan returns a weight estimate and BMI, under 45 seconds from the photos to structured results." | [minor] 45-second line not its own sentence | Speed as its own plain sentence |
| luciana-bastos-83b96a23 | M2 | "For a product team, the shape of the result matters. The scan returns 80+ body measurements, under 45 seconds ..." | Bolted on; same template as three colleagues | Value tied to "which cases rely on the DPS alone" |
| iagoduartesimões | M1/M2 | "...Icatu defines which gaps count." / "Overview of the use case:" | [minor] M1 never names the flag; label | Name the flag; link introduced by a sentence |
| antonio-carlos-almeida-braga-656229135 | M1 | "Thought I'd share a question from Icatu's July range update: ... all through the same life application." / "As the range widens, how do you decide which evidence a case needs?" | The update is not a question; "same life application" is unsupported; question is Luciana's | Plain statement of the July widening; a question only he gets |
| antonio-carlos-almeida-braga-656229135 | M2 | "The record also holds 80+ body measurements, ... when enabled for the deployment." / "Landing page for the use case:" / "A call could settle it:" | Bolted on; "when enabled for the deployment" belongs to the 3D model; label; dangling | Value tied to his question; link sentence; closer with a clear object |
| sergio-egidio-31321b170 | M1 | "...Icatu's DPS guide already lists height and weight among its questions." | Beatriz's anchor; overstates "can ask" | Anchor on his commercial seat and DPS route rules |
| sergio-egidio-31321b170 | M2 | "A short read on the use case:" + link | No value line | Value tied to his quote-to-issue question |
| césar-saut-5444563b4 | M1 | "Couldn't help but ask. Icatu's life journey routes each applicant to the DPS or to a tele-interview, and on both paths height and weight are stated." / "Which part of Icatu's life business does your remit reach most directly?" | Nearly the same as Rafael Saile's M1; fragment hook; bare question about his remit | Anchor on his corporate VP seat; a question about his own work |
| césar-saut-5444563b4 | M2 | "3DLOOK has worked with 100+ clients." / "Overview:" / "A call is the simplest way:" | Scale line bolted on; label; dangling | Value tied to his question; the scale line may follow it |
| beatriz-helena-150154b8 | M1 | "Product discovery on the DPS is where this starts." / "That step is 2 photos, ..." | "this" and "That step" have no referents | Name the step and the product |
| beatriz-helena-150154b8 | M2 | "A step needs 2 photos, front and side, and BMI comes from the height the applicant declared." / "I can walk you through it on a call:" | Same as Priscilla's M2 and closer; repeats M1 | Value tied to her DPS-wording test question |
| marcela-gueiros | M1 | "It fits Casa do Corretor, ..." | [minor] Unclear "It fits" | Plain link from her background to the journey |
| marcela-gueiros | M2 | "The portal already clears pending items through links sent by email or WhatsApp." | Third use of Rodrigo Pádova's anchor | Value tied to where in Casa do Corretor the step sits |
| rafael-saile-90296635 | M1 | "What would you need to see in a shadow evaluation before any output reached a case?" | Lane note pasted | Own wording from his acceptance title |
| rafael-saile-90296635 | M2 | "Not your call? Point me to..." / "Call, if useful:" | Pun beside a call offer; fragment label | Plain easy-out; call offer as a sentence |
| leonardohijino | M2 | "...where Icatu's rules decide whether an exam still follows." / "If numbers would help your view, grab a time:" | Suggests the scan removes exams; promises numbers | The record adds to the case and replaces nothing; no promise of figures |
| l%c3%adgia-abreu-6871b9147 | M1 | "I wondered what that changes for the evidence a case needs." | Same idea as Antonio Carlos and Luciana | Sentence specific to the actuarial view of larger sums |
| l%c3%adgia-abreu-6871b9147 | M2 | "Besides weight and BMI, the record carries 80+ body measurements, ..." / "A one-page view of the use case:" / "A call to go through it:" | Nearly André's M2; bolted on; labels | Value tied to her price question; sentences instead of labels |
| jimmymonte | M1 | "...before the case sees a note." | [minor] A case cannot "see" | A gap above the threshold raises a flag on the case |
| priscilla-teixeira-58140031 | M1 | "Your work on life rates overlaps with something I am looking at." / "...and the DPS can ask about height and weight." | Vague hook; same wording as Leonardo | Hook on pricing for the older entry age |
| priscilla-teixeira-58140031 | M2 | "The scan needs 2 photos, front and side, and calculates BMI ..." / "Or send me to..." / "Happy to walk through it on a call:" | Same as Beatriz; dangling "Or" | Value tied to her older-age extra-premium question |
| pierietto | M1 | "...and the rating rules work from what is stated." / "Smart Scales estimates weight, BMI uses the declared height, and a flag fires above a threshold Icatu sets." / BMI-bands question | Asserts Icatu's rating rules; product sentence same as Rafael Saile's; lane-note question | Ask how declared height and weight move the rate (his Use); own product sentence |
| pierietto | M2 | Opener "Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading." | Identical opener to Jimmy's | Different opener; the 3.5% sentence may follow it |
| humberto-sardenberg | M1 | "Where would a two-photo step sit in an AI-first journey, ...?" / "...its own BMI figure" | Same placement question as Marcela; "its own" is ambiguous | A question only he gets, on AI-first products |
| humberto-sardenberg | M2 | "The scan returns its record, under 45 seconds ... The experience stays inside Icatu's application." / "Use case in brief:" | Template; label | Value tied to his new question |
| ingrid-pereira-39a8882b | M2 | "The scan returns BMI and a weight estimate, under 45 seconds ..." / "Easiest is a call:" | Template; fragment | Value tied to her broker-testing question |
| bernardo-dieckmann-8a399678 | M1 | "Where do Icatu's acceptance rules put the line between the DPS, the tele-interview and an exam, and what part do height and weight play?" | Lane note pasted | Own wording |
| bernardo-dieckmann-8a399678 | M2 | "Short version of the use case:" + link | No value line | Value tied to his line-drawing question |
| paula-cris-silva | M1 | "Your line about building tools that save people time for more time with people suits a capture step at MAG Seguros. That step should pass the same test." | Contorted | Plain hook on her architecture remit |
| paula-cris-silva | M2 | "The record carries 80+ body measurements and a timestamp, one per applicant." / "Walk through the architecture:" | Bolted on; label | Value on where the step plugs into the questionnaire's architecture |
| luishenriquefontes | M2 | "The scan returns its record under 45 seconds ..." / "The privacy FAQ answers the data questions: https://... I can walk your team through it ... https://... If vendor risk owns this, ..." | Speed is not the review point (same sentence as Dayana's); overclaims what the FAQ covers; two URLs in one run-on line | REST API/SDK plus data handling; neutral FAQ introduction; calendar link last, on its own line |
| marco-giorgetti-824bbb23 | M1 | "36 years in commercial and marketing roles in life insurance on your profile fit this note." / "MAG Seguros is now opening branches outside Rio and São Paulo, ..." / "Each proposal would carry 2 photos" | Number outside the allowed list; same "[years] fit this note" shape as Larissa; same branch sentence as Dayana; implies the step on every proposal | Hook on operations behind acceptance, no number; the insurer decides where the step is offered |
| marco-giorgetti-824bbb23 | M2 | "A first look could time that stage on a small group of proposals, with outputs kept out of decisions." | Live test outside the design; implies a speed result | Either the four-part design or no offer |
| eugenioguerimjr-198b8924 | M2 | "One integration could serve several journeys." | This is the whole value line, and it repeats M1 | Value tied to what a digital partner needs to see |
| larissa-althoff-71907094 | M1 | "Fifteen years building partnerships ... fit this note about MAG Seguros. A partner-led life sale has a health declaration that someone types in." | Number outside the allowed list; same shape as Marco; unclear second sentence | Hook on partner-sold life, no number |
| larissa-althoff-71907094 | M2 | "The record also carries 80+ body measurements." / "Happy to talk it over: ... Happy to be redirected..." | Bolted on; "Happy to" twice | Value tied to where the declaration is filled in |
| dayana-gon%c3%a7alves-s-bandeira-de-mello-37163433 | M1 | "...where income-loss, critical-illness and disability covers sell most." / "In each application the applicant takes 2 photos." | [minor] Fact says individual life with these covers sells most; implies every application | Keep "individual life with…"; the insurer chooses where the step is offered |
| carlos-am%c3%a9rico-pugliesi-figueiredo-1631bb14 | M2 | "The step gives the actuarial side a count: how many flags fire at each candidate threshold, measured in an evaluation." / "If someone else handles it, I mean whoever..." | Partial design; contorted | All four parts, or no offer; plain easy-out |
| rafael-lopes-ribeiro | M1 | "Caught my eye: your path from underwriting risk to Chief Actuary at MAG Seguros." | Same career-move hook as Carlos | Hook on Private Solutions risk and pricing |
| rafael-lopes-ribeiro | M2 | "A first read needs no change to pricing: scans on cases MAG already weighs, with outputs kept out of decisions." / "Not yours?" | Missing the comparison and what is counted; idiom | All four parts, or no offer |
| fabio-morita | M1 | "Hi Fábio Ohara," (both messages) / "At which BMI bands would a gap ... change the premium or the route to a medical exam?" | Surname in greeting; lane-note question | "Hi Fábio"; question in own words from the July conditions |
| mariafernandarossi | M2 | "For a transformation team: the step is 2 photos inside the existing journey, and Allianz keeps its current route ..." | Repeats M1; "For X:" opener | Value on how a step moves through transformation work |
| josemilson-silva-132851b | M1 | "FitXpress is that step: 2 photos in the application, a Smart Scales weight estimate and one timestamped record returned by API." | No flag | Add the flag at the insurer's threshold |
| josemilson-silva-132851b | M2 | "...and the right contact there works just as well." / "If you prefer a call, a slot is here:" | [minor] Vague function; "prefer" over what | Name the function |
| eduard-folch | M2 | "Or, if the broker experience in Allianz Life is run by someone else, ..." | Dangling "Or," | Easy-out that stands on its own |
| javier-bernat-a16397162 | M1 | "Reading about Legacy, ..., one point stood out." / "...carry whatever height and weight the applicant gives." / "What would a broker need to see before offering a step like that to applicants?" | Dangling modifier; "whatever" reads as distrust of applicants; broker question same as Eduard's | Grammatical hook; neutral "stated"; a Legacy question Eduard does not get |
| javier-bernat-a16397162 | M2 | "For brokers on Legacy: ..." / "Whoever runs sales support for Vida Individual is equally welcome on that call." | Same opener as Eduard; not an easy-out, and it refers to a call not yet offered | Different opener; a real easy-out to a function |
| caio-souza-787b8215 | M1 | "Each Vida Individual application opens with the DPS, and with no exam in the loop the applicant supplies height and weight." | Unsupported; idiom; M1 has no flag | Only "DPS is mandatory"; add the flag |
| caio-souza-787b8215 | M2 | "...under 45 seconds from the photos to structured results, into the application through API or SDK." / "...for that call." | 45-second line embedded; refers to a call not yet offered | Speed as its own sentence; fix the easy-out |
| thiago-affonso-borsari-29456365 | M1 | "...and in an app journey the application is where height and weight are stated." | Breaks a Never | Say nobody measures; ask how recorded |
| júlio-cezar-oliveira-oliveira-393b5444 | M1 | "Hi Júlio Cezar Oliveira," / "...where nobody measures the applicant, height and weight are stated." | Surname; breaks a Never | "Hi Júlio Cezar"; keep "nobody measures" (the question already asks how recorded) |
| júlio-cezar-oliveira-oliveira-393b5444 | M2 | "Speed matters for a sales network. FitXpress returns a timestamped record, under 45 seconds ..." | Not tied to his question | Value tied to how height and weight are recorded |
| gustavo-oliveira-guga-969114145 | M2 | "One application, two places: the same step works in the app and at a branch, ..." | Repeats M1 | New value on the same step in app and branch |
| luan-noe | M2 | "The scan returns its record under 45 seconds ..." / "Privacy FAQ: https://... Calendar: https://... If it is not you, ..." | Same sentence as Rafael Cló's; labels; run-on line | Different value; sentences instead of labels; calendar last |
| renatotfarias | M1 | "Quick thought after reading that Azos's Partner brokers sat down with the product team in September." | Rodrigo Teixeira's anchor | Anchor on the Partner broker program |
| renatotfarias | M2 | "A small group of Partner brokers could see the step first, with its outputs kept out of decisions. 3DLOOK has worked with 100+ clients." | Pilot offer outside the design; scale line bolted on | Value on testing with brokers, no pilot offer |
| ana-bobis-382975a9 | M2 | "For pricing, the useful part is the record: timestamped, structured, one per applicant, ..." | Generic; does not answer her question; the M1 lane-note question is a minor fix too | Value on what an evaluation counts for pricing |
| heloisa-falcão | M2 | "Trying it on a single cover would show where the photos help and where they add friction, ..." | Live test outside the design | No pilot offer |
| bernardo-correa-ribeiro-73620394 | M1 | "Hi Bernardo Correa," / "One step of a life application is filled in by typing: height and weight." / "...which step of the application do applicants leave most often?" | Surname; odd sentence; Thais Nakahira's topic, not his Use | "Hi Bernardo"; question on products shaped with Partner brokers |
| bernardo-correa-ribeiro-73620394 | M2 | "You may not own this, so I will keep it brief. The scan returns 80+ body measurements ..." | Bolted on | Value tied to his new question |
| rodrigo-cteixeira | M1 | "Your product years at QuintoAndar and now at Azos make you the right person to ask." | Nearly Julia Martins's opener; his roadmap Use unused | Hook on the 2027 roadmap |
| rodrigo-cteixeira | M2 | "Completion is measured in the evaluation, which shows the cost of the step before any roadmap decision." | Same argument as Thais Nakahira's (her Use) | Different value tied to the roadmap |
| victor-ribeiro-reis | M1 | "The step from actuary to underwriting coordinator at Azos matters here." | [minor] "step" clashes with the photo step | Plain hook |
| thais-nakahira | M1/M2 | "Your growth and CRM background before Azos suits this one." / "Open to comparing numbers on a call?" | [minor] Idiom; implies sharing figures | Plain wording |
| julia-martins-pm | M1 | "The product years at XP Inc. before Azos come to mind." | Idiom; repeats Rodrigo Teixeira | Plain hook on the quote screen |
| julia-martins-pm | M2 | "From the quote screen, the step is one more tap for the applicant ... The scan also returns 80+ body measurements." | Understates two photos; bolted on; ignores her "unsure of weight" question | Value tied to her question |
| acalazans | M1 | "At which BMI bands would that gap change acceptance or the route to a medical exam?" | [minor] Lane note, identical to Felipe Orozco's | Own wording from his no-exam rules |
| nachogarciacanton | M1 | "...and a stated weight is an input with no second source." | Breaks a Never (VidaSegura) | Say no exam measures |
| nachogarciacanton | M2 | "A second source can be judged on applicants whose weight the insurer already measures: scan them and compare the estimate with the measured figure." | Missing what is counted and what it does not touch; same argument as Fernando Campos | All four parts, or other value |
| pedro-lopez-comision-de-honor-b50a0835 | M1 | "Hi Pedro Lopez," / "BBVA Seguros México sells life applications where cover is sold with ..." / "How does the technical team decide which stated inputs need a second source?" | Surname; garbled; same question as Nacho | "Hi Pedro"; plain fact; question on who owns the persons-line rules |
| pedro-lopez-comision-de-honor-b50a0835 | M2 | "A technical team could start with cases that carry a measured weight and read how often the flag would fire." | Missing the comparison and what it does not touch | All four parts, or no offer |
| sandra-nacul-méndez-60693736 | M1 | "...and the applicant's weight is simply stated." | Breaks a Never | Remove; ask how recorded |
| sandra-nacul-méndez-60693736 | M2 | "The scan returns its record under 45 seconds ..." / "I mean whoever owns..." | Same sentence as Daniel Ordaz's; contorted | Different value; plain easy-out |
| liliana-r-1052a38 | M1 | "For life cover sold with no exam, height and weight are stated ..." / extra-premium question | Close to a Never (VidaSegura); pasted question, identical to Tonantzin's | Keep "nobody measures"; own question |
| liliana-r-1052a38 | M2 | "For actuarial work, the useful number is flags per candidate threshold, ..." / "Not yours? Whoever owns life product design would be the right contact." | Partial design; the easy-out points to her own function | All four parts; easy-out to the underwriting-rules owner |
| hunibert-tuch-a2468413 | M1/M2 | "...is the reason for this note." / "For a private banking relationship the record matters: ..., with 80+ body measurements behind it." | Same opener as Fernando Campos; bolted on | Different hook; value tied to his wealth-client question |
| luis-hidalgo-50216b12b | M1 | "For the CIO side of BBVA Seguros México, one point. Life applications sold with no medical studies carry stated height and weight." | Same opener as Daniel Oliva; breaks a Never | Different opener; no height-and-weight claim |
| luis-hidalgo-50216b12b | M2 | "Calendar for an architecture call:" | Label | Call offer as a sentence |
| fernando-campos-garcía-850716a3 | M1 | "...leaves weight as a stated figure." | Breaks a Never | Say no exam measures |
| fernando-campos-garcía-850716a3 | M2 | "If a data source fits, the first test is small: scans on cases the insurer already measures, compared with the measured weight." | Partial design | All four parts |
| felipe-orozco-8287b5142 | M1 | "At which BMI bands would that gap change acceptance or the route to a medical exam?" | [minor] Lane note | Own wording |
| isaac-flores-lira-856743189 | M1 | "The AI banking platform at BBVA México meets one life flow." | [minor] Unclear | Plain |
| h%c3%a9ctor-ju%c3%a1rez-lara-4a35a028 | M1 | "...life cover sold with no exam at BBVA Seguros México: height and weight are stated." | Breaks a Never | Remove the claim (the question already asks) |
| daniel-oliva-becerra-a9665996 | M1 | "For technology at BBVA Seguros México, one point. In the online life purchase, applicants state height and weight ..." | Breaks a Never; same opener as Luis Hidalgo | No claim; different opener |
| daniel-oliva-becerra-a9665996 | M2 | "Call: https://..." | Label | Sentence |
| manuel-matamoros-arreguin-4a225066 | M1 | "FitXpress brings 2 photos into that form" | [minor] Photos cannot go into a handwritten form | The step sits alongside the application |
| manuel-matamoros-arreguin-4a225066 | M2 | "For growth in individual life: the applicant completes one added step ..." | Repeats M1; "For X:" cluster | Value tied to how planning sees the handwritten application |
| aldono | M1 | "Your Data & AI remit overlaps with something we built: a life application mostly yields stated answers today." | [minor] Contorted | Plain |
| felipe-octavio-gutierrez-manjarrez-a87b5224 | M2 | "For infrastructure planning: a REST API and an SDK, ..." | No data-handling sentence | One or two verbatim data-handling sentences |
| miguel-angel-c-3a0a49195 | M2 | "...a dated record is ready for issue." / "If agent onboarding for life is run by another team, ..." | [minor] Hints at deciding issue; easy-out off topic | Record sits on the file; easy-out to the life application owner |
| juanorp | M2 | "For the actuarial trade-off: the scan returns 80+ body measurements, under 45 seconds ..." | Bolted on; 45-second line embedded; the M1 restates the lane note (minor) | Value tied to the trade-off |
| efrainb | M1 | "FitXpress is an SDK and API step: 2 photos ..., a Smart Scales weight estimate, and one timestamped structured record ..." | No flag | Add the flag |
| oscar-ruiz-césar-a0120214 | M2 | "On getting a step into production: FitXpress comes as an SDK and a REST API, ..." | Same as Jose de Jesus's M2 | Value tied to his transformation question |
| estelle--hascoet | M1 | "...on life applications with a medical questionnaire, height and weight are stated by the applicant." | Present tense; AXA's current form was not seen | Use "have asked", or ask |
| estelle--hascoet | M2 | "A small point on the applicant's path: the photos are taken in the application itself, ..." | Same as Maritere's | Value tied to her friction question |
| beltrando-pini-59318630 | M2 | "Agents only adopt a step that stays quick. ..." / "Open to a call? Calendar:" | [minor] Presumptuous; 45-second line embedded; label | Plain wording |
| tonantzintapia | M1 | "On life applications without an exam, height and weight are stated by the applicant." / extra-premium question | Present tense for AXA; pasted question | "Have asked"; question from the reserves angle |
| tonantzintapia | M2 | "...allowing flags at a candidate threshold can later be counted against the extra premiums they relate to." | Ungrammatical; implies live flags reviewed after the fact | Grammatical value via the four-part evaluation on measured cases |
| luis-pi%c3%b1%c3%b3n-2053b7145 | M1 | "Your Underwriting Manager title at Seguros Banorte suggests you know which life cases arrive with only stated height and weight." / "Which stated height and weight cases get a second look ...?" | Breaks a Never; presumptuous | Ask how recorded and who owns the questionnaire |
| luis-pi%c3%b1%c3%b3n-2053b7145 | M2 | "For regional underwriting: one timestamped record per applicant, and a flag only above the threshold ..." | Repeats M1; same opener as Andres | Value tied to the new question |
| eduardo-guti%c3%a9rrez-rojo-712930103 | M1 | "In an app purchase, height and weight are stated answers unless something measures them." | Breaks a Never; the M2's embedded 45-second line is a minor fix too | Ask how recorded |
| jose-antonio-palacio-junco-a8675576 | M1 | "...BMI from the declared height." / "If the gap to the declared weight crosses a threshold HSBC sets, ..." | Implies the individual-life questionnaire records height and weight (not seen); the M2 easy-out mismatch (branch sale vs digital application) is minor | Flag against any weight the applicant states; ask how the branch questionnaire records it |
| dominique-hierro-116a1943 | M1 | "How does RGA Mexico decide which new evidence topics to bring to client insurers?" | Close to Lorena's; not her Use | Question on who would run a client evaluation |
| dominique-hierro-116a1943 | M2 | "The first conversation with a client stays short: ..." / "If this belongs with whoever leads underwriting for client insurers, point me to them." | Value same as Jesus and Lorena; easy-out identical to Jesus's | New value; new easy-out |
| jesus-spinola-grandio-80462345 | M2 | "Open to a call? Calendar:" | [minor] Label | Sentence |
| lorena-cruz-vega-1153825a | M2 | "For a new client conversation: one timestamped record and a flag at the insurer's own threshold, nothing more." | Same as Jesus's; no one-client evaluation (the reinsurance M2 value) | One-client four-part design |
| cesarcastilloarroyo | M1 | "Got me thinking: RGA Mexico's AURA Next platform and its advice on which digital evidence sources to use." | [minor] Fragment | Full sentence |
| carolyn-pritchard-9151b621 | M1 | "Under FitXpress, the applicant takes 2 photos, ...; the insurer's systems take it in through one integration." | [minor] Odd preposition; "it" unclear | Plain |
| julianasobredaalves | M2 | "The record is one timestamped entry per applicant, ... 3DLOOK has worked with 100+ clients." | Thin; no one-client evaluation; not tied to her Magnum Go question | Value on where the flag sits next to Magnum Go's questions, or the four-part design |
| rafael-zimmer-b8268751 | M1 | "Came across your work heading program business for Latin America at SCOR, and we built FitXpress for ..." / "Does evidence on life declaration cases ever come up ...?" | Run-on; question same as Francisco's | Two sentences; question on who at SCOR supports Brazilian life insurers |
| rafael-zimmer-b8268751 | M2 | "If it has come up, a first conversation could be about which declaration cases ..." | Same argument as Francisco's; depends on the old question | Value tied to the new question |
| franciscomajos | M1 | "It is delivered as one timestamped record by API or SDK." | [minor] Ambiguous "It" | Name the subject |
| joão-caproni-1ba34189 | M2 | "If an insurer asks, the first step is finding where such a question lands inside Hannover Re, ..." | No value; repeats his question and the easy-out | Value on what the insurer would receive |
| bryan-urbano-b38a71106 | M1 | "...where helping clients design products needs evidence a pricing assumption can use." | [minor] Contorted | Plain |

**Applies to every M2 at MAG, Azos, BBVA, HSBC, Swiss Re, SCOR and Hannover Re (47 pairs, not repeated above):** move the easy-out above the call line and end on the calendar link alone. That includes rodrigo-cunha-94992676, whose message otherwise needs no change.

## 4. Pairs to send as they are: 22 of 126

| Company | As-is | Who |
|---|---|---|
| Bradesco | 1/23 | reisedilson |
| Icatu | 0/21 | (3 have minor fixes only: rachel, rodrigopadova, iago) |
| MAG | 1/9 | rodrigo-cunha |
| Allianz | 2/8 | guilhermelissandre, alexandra-rossini-ruz |
| Brasilseg | 0/3 | |
| Azos | 3/13 | rafael-clo, raul-lobo, juliawajs |
| BBVA | 2/13 | daniel-ordaz-palacios, xabier-beroiz-ripa |
| MAPFRE | 2/7 | robertogonzalezmend, ricardo-endo |
| AXA | 2/7 | maritere-torcida, jj-lunac |
| Banorte | 2/4 | andres-amtzs, susana-granados |
| HSBC | 0/1 | |
| RGA | 1/6 | keiko-imuro |
| Swiss Re | 3/4 | paulina-noyola, gmfentanez1402, antonioferramd |
| SCOR | 2/4 | claudia-rodríguez-gomez, yolanda-gutierrez |
| Hannover Re | 1/3 | julio-ponce-de-leon |

The MAG, Azos, BBVA, Swiss Re, SCOR and Hannover Re pairs in this list still need the closer moved so the calendar link comes last.

Sources: `/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/card-messages.md`, `/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/messages/_dump-2026-11-10.md`, `/home/vadim_prod/3dlook-marketing/marketing_vb/docs/quality-rubric.md`.
