# Fix round 2 for batch mixed-2 (coordinator, 2026-11-10, from opus QC 10/20)

Edit the sentences named below, and apply the rules to every pair in your batch. Work in your batch file, re-split, and run the gate until exit 0. Then re-read EVERY changed pair in full yourself (not only the gate) and reply with the person_ids you changed and anything you could not fix.

## Rules for every pair in this round (opus QC 10/20, 2026-11-10; the same list goes to every batch)

1. **Form claims.** At Bradesco Vida e Previdência, BBVA Seguros México, Brasilseg, Seguros Banorte, HSBC, MAG Seguros, and AXA (present tense), the copy never states as a fact that the company's form or journey asks, takes or records height and weight ("height and weight are stated", "the applicant's own entries supply height and weight", "a stated weight", "typed in"). Say that no exam or nobody measures the applicant, and ask how height and weight are recorded. At AXA, "have asked" is the furthest the copy may go. Icatu (its DPS guide says the DPS can ask), Allianz Brasil (the DPS is mandatory; the complementary declaration asks), Azos (the quote asks) and MAPFRE México (the Solicitud Única asks) may say what their own bullet says, no more.
2. **Message 2 order.** Value line(s) that continue THIS person's own Message 1 question → the compliance line → an easy out as its own sentence naming a function at the company → last paragraph: one call-offer sentence ending with the calendar link, nothing after the link. No label before any link ("Overview:", "Calendar:", "Call:", "Privacy FAQ:", "Use case in brief:", "Landing page for the use case:"): a link sits at the end of a full sentence.
3. **No bolt-ons.** 80+ body measurements, the speed sentence or a scale line is never the value line. The speed sentence stays its own plain sentence, only where speed is the point of the person's question. No pair may repeat Message 1's content as its Message 2 value.
4. **Evaluation offers.** Any test, evaluation, pilot or "first look" names all four parts from the card (who scans: applicants whose weight the insurer measures anyway; what the estimate is compared with: that measured weight; what is counted: agreement with the measured weight, flags per candidate threshold and how many of them match a gap between declared and measured weight, completion and retakes; what it does not touch: acceptance, extra premiums and routing). Otherwise make no offer. No live pilots, no small groups of brokers or proposals, no counting after issue.
5. **Numbers** only from the card's list. No years of experience or other figures.
6. **Greeting** is "Hi <first name>," with the first name only (Fábio, Júlio Cezar, Bernardo, Pedro).
7. **Every Message 1** carries the 2 photos and the flag at the insurer's threshold.
8. **technical-integration Message 2** carries one or two of the card's data-handling sentences, verbatim.
9. **Plain English for second-language readers.** No idioms ("wrong desk", "Not your call?", "Not yours?", "like-for-like", "in the loop", "send me their way", "come to mind", "grab a time"), no dangling "It", "this", "them", "Or", "If not" at the start of a sentence whose referent is unclear, no fragments, no hook that is not a sentence.
10. **Questions are the person's own.** Never paste a lane-note question target from the card; write each question from the person's title and their Use anchor. At one company no two people get the same question or the same M2 argument, even in other words.
11. **After your edits,** scan your own batch for any phrase that now appears in three or more pairs at one company and vary it; a removed stock phrase tends to be replaced by a new one.

## Message 2s in this batch with text after the calendar link (rule 2)

guilhermelissandre, fabio-morita, manuel-matamoros-arreguin-4a225066, aldono, efrainb, oscar-ruiz-césar-a0120214, dominique-hierro-116a1943, jesus-spinola-grandio-80462345, lorena-cruz-vega-1153825a, cesarcastilloarroyo, andres-amtzs, susana-granados-049025309, thiago-affonso-borsari-29456365, júlio-cezar-oliveira-oliveira-393b5444, gustavo-oliveira-guga-969114145

## Per-person items from QC (sentence quoted as it stood in the dump; target, not a replacement sentence)

### fabio-morita (Fábio Ohara Morita, Allianz Brasil, underwriting)
- M1: "Hi Fábio Ohara," (both messages) / "At which BMI bands would a gap ... change the premium or the route to a medical exam?"
  - problem: Surname in greeting; lane-note question
  - target: "Hi Fábio"; question in own words from the July conditions

### mariafernandarossi (Maria Fernanda Piccolo Rossi, Allianz Brasil, referral)
- M2: "For a transformation team: the step is 2 photos inside the existing journey, and Allianz keeps its current route ..."
  - problem: Repeats M1; "For X:" opener
  - target: Value on how a step moves through transformation work

### josemilson-silva-132851b (Josemilson Silva, Allianz Brasil, technical-integration)
- M1: "FitXpress is that step: 2 photos in the application, a Smart Scales weight estimate and one timestamped record returned by API."
  - problem: No flag
  - target: Add the flag at the insurer's threshold
- M2: "...and the right contact there works just as well." / "If you prefer a call, a slot is here:"
  - problem: [minor] Vague function; "prefer" over what
  - target: Name the function

### eduard-folch (Eduard Folch Rue, Allianz Brasil, referral)
- M2: "Or, if the broker experience in Allianz Life is run by someone else, ..."
  - problem: Dangling "Or,"
  - target: Easy-out that stands on its own

### javier-bernat-a16397162 (Javier Bernat, Allianz Brasil, referral)
- M1: "Reading about Legacy, ..., one point stood out." / "...carry whatever height and weight the applicant gives." / "What would a broker need to see before offering a step like that to applicants?"
  - problem: Dangling modifier; "whatever" reads as distrust of applicants; broker question same as Eduard's
  - target: Grammatical hook; neutral "stated"; a Legacy question Eduard does not get
- M2: "For brokers on Legacy: ..." / "Whoever runs sales support for Vida Individual is equally welcome on that call."
  - problem: Same opener as Eduard; not an easy-out, and it refers to a call not yet offered
  - target: Different opener; a real easy-out to a function

### caio-souza-787b8215 (Caio Souza, Allianz Brasil, proposition)
- M1: "Each Vida Individual application opens with the DPS, and with no exam in the loop the applicant supplies height and weight."
  - problem: Unsupported; idiom; M1 has no flag
  - target: Only "DPS is mandatory"; add the flag
- M2: "...under 45 seconds from the photos to structured results, into the application through API or SDK." / "...for that call."
  - problem: 45-second line embedded; refers to a call not yet offered
  - target: Speed as its own sentence; fix the easy-out

### manuel-matamoros-arreguin-4a225066 (Manuel Matamoros Arreguin, MAPFRE México, referral)
- M1: "FitXpress brings 2 photos into that form"
  - problem: [minor] Photos cannot go into a handwritten form
  - target: The step sits alongside the application
- M2: "For growth in individual life: the applicant completes one added step ..."
  - problem: Repeats M1; "For X:" cluster
  - target: Value tied to how planning sees the handwritten application

### aldono (Alejandro D., MAPFRE México, technical-integration)
- M1: "Your Data & AI remit overlaps with something we built: a life application mostly yields stated answers today."
  - problem: [minor] Contorted
  - target: Plain

### felipe-octavio-gutierrez-manjarrez-a87b5224 (Felipe Octavio Gutierrez Manjarrez, MAPFRE México, technical-integration)
- M2: "For infrastructure planning: a REST API and an SDK, ..."
  - problem: No data-handling sentence
  - target: One or two verbatim data-handling sentences

### miguel-angel-c-3a0a49195 (Miguel Angel C., MAPFRE México, referral)
- M2: "...a dated record is ready for issue." / "If agent onboarding for life is run by another team, ..."
  - problem: [minor] Hints at deciding issue; easy-out off topic
  - target: Record sits on the file; easy-out to the life application owner

### juanorp (Juan Ortiz Perez, MAPFRE México, proposition)
- M2: "For the actuarial trade-off: the scan returns 80+ body measurements, under 45 seconds ..."
  - problem: Bolted on; 45-second line embedded; the M1 restates the lane note (minor)
  - target: Value tied to the trade-off

### efrainb (Efrain Baldenebro Ortiz, AXA Seguros México, technical-integration)
- M1: "FitXpress is an SDK and API step: 2 photos ..., a Smart Scales weight estimate, and one timestamped structured record ..."
  - problem: No flag
  - target: Add the flag

### oscar-ruiz-césar-a0120214 (Oscar Ruiz César, AXA Seguros México, referral)
- M2: "On getting a step into production: FitXpress comes as an SDK and a REST API, ..."
  - problem: Same as Jose de Jesus's M2
  - target: Value tied to his transformation question

### estelle--hascoet (Estelle Hascoët, AXA Seguros México, referral)
- M1: "...on life applications with a medical questionnaire, height and weight are stated by the applicant."
  - problem: Present tense; AXA's current form was not seen
  - target: Use "have asked", or ask
- M2: "A small point on the applicant's path: the photos are taken in the application itself, ..."
  - problem: Same as Maritere's
  - target: Value tied to her friction question

### beltrando-pini-59318630 (Beltrando Pini, AXA Seguros México, proposition)
- M2: "Agents only adopt a step that stays quick. ..." / "Open to a call? Calendar:"
  - problem: [minor] Presumptuous; 45-second line embedded; label
  - target: Plain wording

### tonantzintapia (Tonantzin Tapia Garduno, AXA Seguros México, proposition)
- M1: "On life applications without an exam, height and weight are stated by the applicant." / extra-premium question
  - problem: Present tense for AXA; pasted question
  - target: "Have asked"; question from the reserves angle
- M2: "...allowing flags at a candidate threshold can later be counted against the extra premiums they relate to."
  - problem: Ungrammatical; implies live flags reviewed after the fact
  - target: Grammatical value via the four-part evaluation on measured cases

### dominique-hierro-116a1943 (Dominique Hierro, RGA Mexico, referral)
- M1: "How does RGA Mexico decide which new evidence topics to bring to client insurers?"
  - problem: Close to Lorena's; not her Use
  - target: Question on who would run a client evaluation
- M2: "The first conversation with a client stays short: ..." / "If this belongs with whoever leads underwriting for client insurers, point me to them."
  - problem: Value same as Jesus and Lorena; easy-out identical to Jesus's
  - target: New value; new easy-out

### jesus-spinola-grandio-80462345 (Jesus Spinola Grandio, RGA Mexico, reinsurance)
- M2: "Open to a call? Calendar:"
  - problem: [minor] Label
  - target: Sentence

### lorena-cruz-vega-1153825a (Lorena Cruz Vega, RGA Mexico, reinsurance)
- M2: "For a new client conversation: one timestamped record and a flag at the insurer's own threshold, nothing more."
  - problem: Same as Jesus's; no one-client evaluation (the reinsurance M2 value)
  - target: One-client four-part design

### cesarcastilloarroyo (Cesar Castillo, RGA Mexico, reinsurance)
- M1: "Got me thinking: RGA Mexico's AURA Next platform and its advice on which digital evidence sources to use."
  - problem: [minor] Fragment
  - target: Full sentence

### carolyn-pritchard-9151b621 (Carolyn Pritchard, RGA Mexico, reinsurance)
- M1: "Under FitXpress, the applicant takes 2 photos, ...; the insurer's systems take it in through one integration."
  - problem: [minor] Odd preposition; "it" unclear
  - target: Plain

### luis-pi%c3%b1%c3%b3n-2053b7145 (Luis Pinon, Seguros Banorte, referral)
- M1: "Your Underwriting Manager title at Seguros Banorte suggests you know which life cases arrive with only stated height and weight." / "Which stated height and weight cases get a second look ...?"
  - problem: Breaks a Never; presumptuous
  - target: Ask how recorded and who owns the questionnaire
- M2: "For regional underwriting: one timestamped record per applicant, and a flag only above the threshold ..."
  - problem: Repeats M1; same opener as Andres
  - target: Value tied to the new question

### eduardo-guti%c3%a9rrez-rojo-712930103 (Eduardo Gutierrez Rojo, Seguros Banorte, referral)
- M1: "In an app purchase, height and weight are stated answers unless something measures them."
  - problem: Breaks a Never; the M2's embedded 45-second line is a minor fix too
  - target: Ask how recorded

### thiago-affonso-borsari-29456365 (Thiago Affonso Borsari, Brasilseg, technical-integration)
- M1: "...and in an app journey the application is where height and weight are stated."
  - problem: Breaks a Never
  - target: Say nobody measures; ask how recorded

### júlio-cezar-oliveira-oliveira-393b5444 (Júlio Cezar Oliveira Oliveira, Brasilseg, referral)
- M1: "Hi Júlio Cezar Oliveira," / "...where nobody measures the applicant, height and weight are stated."
  - problem: Surname; breaks a Never
  - target: "Hi Júlio Cezar"; keep "nobody measures" (the question already asks how recorded)
- M2: "Speed matters for a sales network. FitXpress returns a timestamped record, under 45 seconds ..."
  - problem: Not tied to his question
  - target: Value tied to how height and weight are recorded

### gustavo-oliveira-guga-969114145 (Gustavo Oliveira (Guga), Brasilseg, referral)
- M2: "One application, two places: the same step works in the app and at a branch, ..."
  - problem: Repeats M1
  - target: New value on the same step in app and branch
