# Fix round 2 for batch icatu-seguros (coordinator, 2026-11-10, from opus QC 10/20)

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

none

## Per-person items from QC (sentence quoted as it stood in the dump; target, not a replacement sentence)

### rachel-ferreira-bonel-85583a73 (Rachel Ferreira Bonel, Icatu Seguros, technical-integration)
- M2: "Handling, in short."
  - problem: [minor] Fragment
  - target: Full sentence or drop

### bernardocarneiro (Bernardo Carneiro, Icatu Seguros, technical-integration)
- M1: "...through links sent by email or WhatsApp, which is the stack a capture step would join."
  - problem: Rodrigo Pádova's anchor; a link flow is not a "stack"
  - target: Anchor on an SDK step in the application stack
- M2: "Calendar for a technical call:" / "send me their way"
  - problem: Label; idiom
  - target: Call offer as a sentence; plain easy-out

### andreolivacarneiro (André Oliva Carneiro, Icatu Seguros, technical-integration)
- M2: "Along with weight and BMI, the record carries 80+ body measurements, ..."
  - problem: No data-handling sentence; says "weight", not "weight estimate"; nearly the same as Ligia's
  - target: One or two verbatim data-handling sentences; value tied to his question

### eduardo-correa-6a5bb89 (Eduardo Correa, Icatu Seguros, referral)
- M1: "A short phone step handles it: ..."
  - problem: Suggests the step measures the applicant
  - target: Say what comes back, without "handles it"
- M2: "The use case on one page:"
  - problem: Label; the link opens the M2
  - target: Value first; link introduced by a sentence

### rodrigopadova (Rodrigo Pádova, Icatu Seguros, proposition)
- M2: "A scan returns a weight estimate and BMI, under 45 seconds from the photos to structured results."
  - problem: [minor] 45-second line not its own sentence
  - target: Speed as its own plain sentence

### luciana-bastos-83b96a23 (Luciana Bastos, Icatu Seguros, proposition)
- M2: "For a product team, the shape of the result matters. The scan returns 80+ body measurements, under 45 seconds ..."
  - problem: Bolted on; same template as three colleagues
  - target: Value tied to "which cases rely on the DPS alone"

### iagoduartesimões (Iago Duarte Simões, Icatu Seguros, referral)
- M1/M2: "...Icatu defines which gaps count." / "Overview of the use case:"
  - problem: [minor] M1 never names the flag; label
  - target: Name the flag; link introduced by a sentence

### antonio-carlos-almeida-braga-656229135 (Antonio Carlos Almeida Braga, Icatu Seguros, proposition)
- M1: "Thought I'd share a question from Icatu's July range update: ... all through the same life application." / "As the range widens, how do you decide which evidence a case needs?"
  - problem: The update is not a question; "same life application" is unsupported; question is Luciana's
  - target: Plain statement of the July widening; a question only he gets
- M2: "The record also holds 80+ body measurements, ... when enabled for the deployment." / "Landing page for the use case:" / "A call could settle it:"
  - problem: Bolted on; "when enabled for the deployment" belongs to the 3D model; label; dangling
  - target: Value tied to his question; link sentence; closer with a clear object

### sergio-egidio-31321b170 (Sergio Egidio, Icatu Seguros, referral)
- M1: "...Icatu's DPS guide already lists height and weight among its questions."
  - problem: Beatriz's anchor; overstates "can ask"
  - target: Anchor on his commercial seat and DPS route rules
- M2: "A short read on the use case:" + link
  - problem: No value line
  - target: Value tied to his quote-to-issue question

### césar-saut-5444563b4 (César Saut, Icatu Seguros, referral)
- M1: "Couldn't help but ask. Icatu's life journey routes each applicant to the DPS or to a tele-interview, and on both paths height and weight are stated." / "Which part of Icatu's life business does your remit reach most directly?"
  - problem: Nearly the same as Rafael Saile's M1; fragment hook; bare question about his remit
  - target: Anchor on his corporate VP seat; a question about his own work
- M2: "3DLOOK has worked with 100+ clients." / "Overview:" / "A call is the simplest way:"
  - problem: Scale line bolted on; label; dangling
  - target: Value tied to his question; the scale line may follow it

### beatriz-helena-150154b8 (Beatriz Helena, Icatu Seguros, proposition)
- M1: "Product discovery on the DPS is where this starts." / "That step is 2 photos, ..."
  - problem: "this" and "That step" have no referents
  - target: Name the step and the product
- M2: "A step needs 2 photos, front and side, and BMI comes from the height the applicant declared." / "I can walk you through it on a call:"
  - problem: Same as Priscilla's M2 and closer; repeats M1
  - target: Value tied to her DPS-wording test question

### marcela-gueiros (Marcela Gueiros, Icatu Seguros, proposition)
- M1: "It fits Casa do Corretor, ..."
  - problem: [minor] Unclear "It fits"
  - target: Plain link from her background to the journey
- M2: "The portal already clears pending items through links sent by email or WhatsApp."
  - problem: Third use of Rodrigo Pádova's anchor
  - target: Value tied to where in Casa do Corretor the step sits

### rafael-saile-90296635 (Rafael Saile, Icatu Seguros, underwriting)
- M1: "What would you need to see in a shadow evaluation before any output reached a case?"
  - problem: Lane note pasted
  - target: Own wording from his acceptance title
- M2: "Not your call? Point me to..." / "Call, if useful:"
  - problem: Pun beside a call offer; fragment label
  - target: Plain easy-out; call offer as a sentence

### leonardohijino (Leonardo Hijino, Icatu Seguros, proposition)
- M2: "...where Icatu's rules decide whether an exam still follows." / "If numbers would help your view, grab a time:"
  - problem: Suggests the scan removes exams; promises numbers
  - target: The record adds to the case and replaces nothing; no promise of figures

### l%c3%adgia-abreu-6871b9147 (Ligia Abreu, Icatu Seguros, proposition)
- M1: "I wondered what that changes for the evidence a case needs."
  - problem: Same idea as Antonio Carlos and Luciana
  - target: Sentence specific to the actuarial view of larger sums
- M2: "Besides weight and BMI, the record carries 80+ body measurements, ..." / "A one-page view of the use case:" / "A call to go through it:"
  - problem: Nearly André's M2; bolted on; labels
  - target: Value tied to her price question; sentences instead of labels

### jimmymonte (Jimmy Monte, Icatu Seguros, underwriting)
- M1: "...before the case sees a note."
  - problem: [minor] A case cannot "see"
  - target: A gap above the threshold raises a flag on the case

### priscilla-teixeira-58140031 (Priscilla Teixeira, Icatu Seguros, proposition)
- M1: "Your work on life rates overlaps with something I am looking at." / "...and the DPS can ask about height and weight."
  - problem: Vague hook; same wording as Leonardo
  - target: Hook on pricing for the older entry age
- M2: "The scan needs 2 photos, front and side, and calculates BMI ..." / "Or send me to..." / "Happy to walk through it on a call:"
  - problem: Same as Beatriz; dangling "Or"
  - target: Value tied to her older-age extra-premium question

### pierietto (Pier Ietto, Icatu Seguros, underwriting)
- M1: "...and the rating rules work from what is stated." / "Smart Scales estimates weight, BMI uses the declared height, and a flag fires above a threshold Icatu sets." / BMI-bands question
  - problem: Asserts Icatu's rating rules; product sentence same as Rafael Saile's; lane-note question
  - target: Ask how declared height and weight move the rate (his Use); own product sentence
- M2: Opener "Smart Scales has approximately 3.5% mean absolute error under evaluated conditions and is not a scale reading."
  - problem: Identical opener to Jimmy's
  - target: Different opener; the 3.5% sentence may follow it

### humberto-sardenberg (Humberto Sardenberg, Icatu Seguros, proposition)
- M1: "Where would a two-photo step sit in an AI-first journey, ...?" / "...its own BMI figure"
  - problem: Same placement question as Marcela; "its own" is ambiguous
  - target: A question only he gets, on AI-first products
- M2: "The scan returns its record, under 45 seconds ... The experience stays inside Icatu's application." / "Use case in brief:"
  - problem: Template; label
  - target: Value tied to his new question

### ingrid-pereira-39a8882b (Ingrid Pereira, Icatu Seguros, proposition)
- M2: "The scan returns BMI and a weight estimate, under 45 seconds ..." / "Easiest is a call:"
  - problem: Template; fragment
  - target: Value tied to her broker-testing question

### bernardo-dieckmann-8a399678 (Bernardo Dieckmann, Icatu Seguros, underwriting)
- M1: "Where do Icatu's acceptance rules put the line between the DPS, the tele-interview and an exam, and what part do height and weight play?"
  - problem: Lane note pasted
  - target: Own wording
- M2: "Short version of the use case:" + link
  - problem: No value line
  - target: Value tied to his line-drawing question
