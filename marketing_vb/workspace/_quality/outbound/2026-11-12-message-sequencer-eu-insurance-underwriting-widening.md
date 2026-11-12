---
qc_date: 2026-11-12
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/messages/ (widening 2026-11-12, 30 new pairs, read verbatim from the coordinator's dump)
track: outbound
artifact_type: messages
total_score: 10/20
status: failed
coordinator_review: done
---

# QC Report: message-sequencer, 2026-11-12 (EU insurance underwriting, widening, 30 new pairs)

**Artifact:** I read the 30 new pairs verbatim (`new-dump.md`) and judged them against the 84 pairs already sent at the same 11 company families (`existing-add.md`, all read). Rules come from `card-messages.md` in full: Rules, lanes, Account facts, Vadim's decisions 2026-11-12, both templates. I checked every claim about a person against the Bio and Experience in `pool-*.md`.

**Total: 10/20, failed.** These parts are clean:
- lane choice;
- the compliance line (30 of 30 correct by lane, in M2 only, one per pair);
- numbers and 3.5% placement;
- Never lines and former employers.

Three things fail:
- **Item 6 of 2026-11-12** says nothing may repeat anyone already contacted. Nine of the 11 companies break it, mostly through the M1 product sentence. The 12 new Swiss Re pairs also repeat each other: 11 of 12 closers share one shape, 6 of 12 hooks are career paths, and the CTA labels repeat.
- **The 2026-11-02 A1 defect is back.** 8 M1s never say what the flag compares, so "a flag above the insurer's threshold" reads as a cutoff on the weight itself.
- **Claims and rules:**
  - Five claims about people that their profiles do not support, and one actor error.
  - Two market statements that item 4 forbids.
  - One speed sentence that misstates what the 45 seconds cover.
  - Easy outs on both new P1s.

**Recommendation:** do not regenerate all 30.
- Rewrite the 12 Swiss Re pairs as one block. Assign each person a hook type, an M2 opener, an easy-out target and a CTA, checked against the 16 already sent.
- Line-edit the other 18 (about 35 edits).

The limits, signature, link placement, bans, detector and completeness come from the gate (0 hard), and I took them as fact. Items I did not flag:
- the verbatim compliance line, the 3.5% sentence and the data-handling forms repeating;
- the gate's note "Gen Re Germany not named" for Sara Fenelon. She is named through "Gen Re's", so this is a gate limitation;
- the gate's note on "the insurer sets the threshold" as card wording. Saying who decides is card-required content, so the sentence itself is fine (Jeffrey Krook's M2). The defect is the company-name tail "a threshold [Company] sets" repeating inside one company (A2).

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 1 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence, 2/5

**A1. The M1 never says what the flag compares.** The card's "What the scan is" asks for "a flag when the gap crosses the threshold the insurer sets". The 2026-11-02 coordinator note said: "keep the weight estimate and the declared-weight gap". These 8 M1s mention no declared weight and no gap anywhere:
- Claudia Szwillus (P1): "The insurer's threshold decides when a flag is raised, in one timestamped record."
- Declan O'Neill: "Its own threshold decides when a flag is raised."
- Jude Devins: "Two photos taken in the application return a Smart Scales weight estimate and a flag above the insurer's threshold."
- Martijn Reijerse: "2 photos in the application give a Smart Scales weight estimate, with a flag above the insurer's threshold."
- Aisling Bradfield and Pia Burghartz have the same sentence word for word: "A flag appears only above the insurer's threshold."
- Marco Spagnuolo: "the insurer's own threshold decides if a flag is attached."
- Ueli Konrad: "Small gaps raise nothing, and only a gap above the insurer's threshold sets a flag." The gap is never defined.

A weaker form appears in 11 more M1s: declared build is mentioned, but the flag is not tied to it. These are Sara, Raphael, Lisa, Gianfranco, Yosra, Ariane, Daniel, Enzo, Klemens, Luiz and Michael. Pavel Cerny's version is also wrong on the mechanics: "A flag appears at the threshold the insurer has chosen."

**A2. Repeats against colleagues already contacted.** Item 6: "Nothing may repeat anyone already contacted there."
- **Alte Leipziger (Juliane Kania):** "A step of 2 photos would put a Smart Scales weight estimate beside it. A flag appears only when the gap to the declared weight crosses a threshold Alte Leipziger sets…" This is a splice of two sent M1s:
  - Holger Krebs: "A step of 2 photos could sit beside the health answers there … crosses a threshold Alte Leipziger sets"
  - Karsten Vogel: "a flag appears only when the gap to the declared weight crosses…"
- **Aviva Ireland (Kate Campbell):**
  - Hook: "As Director of Strategy and Governance at Aviva Life and Pensions Ireland, …" This is the third "as [title] at Aviva Life (&) Pensions" hook, after Brian O'Malley and Jean Larkin.
  - Product sentence: "a flag appears only when its gap to the declared weight crosses a threshold Aviva sets" repeats Mark Cree's "A flag appears only where the gap to the declared weight crosses a threshold Aviva sets" (also Jean Larkin, Claire Donohoe).
  - M2: "The rules and the underwriters stay in charge of every decision." is close to Claire Donohoe's "Aviva's threshold and rules stay in control".
- **Gen Re (Sara Fenelon):**
  - M1: "Many applications your client insurers decide see no examination or weighing, and build is declared." Compare Carsten Giese, "many point-of-sale applications your clients decide see no examination, and build is declared", and Andres Webersinke, "Many of their applications see no doctor's examination or weighing".
  - Closer: "Whoever briefs clients on new tools in your team could join instead." has the same frame as Simon Fallais' "Whoever sets research priorities on evidence could join instead."
  - M2: "no output reaches a case" is close to Ulrich Pasdika's "nothing reaches a case".
- **Hannover Re (Raphael Rimelin):**
  - "A flag shows only above the insurer's own threshold, in one timestamped record." Steven Hardy has "flags a gap above the insurer's own threshold, in one timestamped record". Susanne Buchholz and Henning Von Kielpinski also end on "in one timestamped record".
  - The hook "after an actuarial career" is the second career-route hook here, after Margot Wilson.
- **Irish Life:**
  - Paul Clerkin: "FitXpress ships as a REST API and web and mobile SDKs." is close to Richard L.'s "FitXpress is a REST API with web and mobile SDKs:".
  - Mark Rodgers: "Which identifier would tie such a record to the case in your data model?" has the same skeleton as Brendan Lambe's "In your architecture, where would such a record enter the underwriting system?"
- **Munich Re:**
  - Declan O'Neill's hook "Your bio pairs actuarial work with product and system development" uses the frame of Mirjam Jonker-Heidolph's "Your headline combines…".
  - Declan's argument (ideas move toward client tests, and a build record is a candidate) is Roland Schneider's: "your bio talks about moving ideas from experimentation into real solutions. A build record for Munich Re L&H faces that step too."
  - Declan's M2 "A shortlisted idea needs a small, defined first step: one insurer, …" is close to Roland's "One insurer, shadow mode and a handful of thresholds would make a small first evaluation."
  - Sebastian Soika: "FitXpress adds 2 photos to the application and returns a Smart Scales weight estimate" is close to Volker Homola's "FitXpress puts 2 photos into the application and returns a Smart Scales weight estimate" and to Fabian Schmitt's.
- **NN (Jeffrey Krook):**
  - "a flag comes back when its gap to the declared weight crosses NN's threshold" repeats Koos van der Veen's "a flag when the gap to the declared weight crosses NN's threshold".
  - The closer "please point me to them" is close to Rens Engelen's "please point me their way".
- **New Ireland:**
  - 5 of the 7 New Ireland M1s now end on "a threshold New Ireland sets": Noel Finnegan and Paul Courtney (sent), Lisa, Marie and Myra (new). This stock tail is what sits behind the gate's "the insurer sets the threshold" note.
  - Myra's "in one timestamped record" is Noel's tail.
  - Marie's closer "If experience monitoring sits with another actuary, please name the role." repeats Denis Eivers' "If a different role delivers the e-application, please name it."
  - Lisa's M2 completion line is close to Paul Courtney's "measure how many applicants finish the photo step".
- **SCOR:**
  - Gianfranco Raffaele Tommasi repeats sent phrases three times:
    - "Today build on applications with no examination is a declared value." is close to Adrien Givaudan's "build on cases with no examination is a declared value" (also Antoine Moll).
    - "a flag set by the insurer's threshold" appears word for word in Antoine Moll and Roberto Castellini.
    - "FitXpress turns 2 photos in the application into…" repeats Lucie Aubry's "FitXpress turns 2 photos into…".
  - Yosra Jemai: "A flag shows only above the insurer's threshold, in one timestamped record." is close to Adrien Givaudan's "A flag shows only when the gap … crosses the insurer's threshold, in one timestamped record."
  - Aisling Bradfield's closer "If a colleague leads research with clients, please name them." has the frame of Stephanie Maret's "If someone else maintains the evidence rules, please name them."
  - Sophie Chapelain:
    - Her CTA "To talk it over on a call:" is close to Adrien Givaudan's "To talk it through:".
    - Her "nothing else sits beside it" is close to Stephanie Maret's "a declared build and nothing else".
  - Martijn Reijerse: "FitXpress comes as a REST API and web and mobile SDKs" is close to Marvin Dewkurun's "FitXpress runs as a REST API with web and mobile SDKs".
- **Swiss Re, new pairs against the 16 sent:**
  - **Pia Burghartz has Francesca Tamma's central question and M2 argument:** adding a photo step and completion. Francesca's question is "How would your team test whether adding a photo step changes completion?" and her M2 says "compare completion with and without the step". Pia's M2 is "An evaluation measures completion against the client's current journey and shows where applicants drop out."
  - **Ueli Konrad:**
    - His question "How would data-driven underwriting judge such a flag after it has run in shadow beside today's rules?" is close to Claude Schwarz's "…allow you to judge a build flag before it touches a case?"
    - His hook "As head of … at Swiss Re, you decide…" is Markus Unterkofler's "As head of … at Swiss Re, you work with…".
  - **Michael Kamm:** "Whether a flag is raised rests on the insurer's threshold." repeats Augusto Diaz-Leante's "Whether a flag is raised rests on one comparison".
  - **Claudia Szwillus:**
    - "The insurer's threshold decides when a flag is raised" is close to Carl Christensen's "…decides whether a flag is raised".
    - Her question "Would you want a build flag to reach underwriters as a referral or as a note…?" uses the frame of Carl's "Would you place such a flag inside the rules of Magnum, or in the data feeding them?"
  - **Marco Spagnuolo:** "the insurer's own threshold decides if a flag is attached" is close to Rainer Helfenstein's "The insurer's own threshold decides whether…".
  - **Pavel Cerny:** "Managing L&H underwriting for CEE at Swiss Re means working through…" uses the frame of Dan Lacurezeanu's "Delivering Magnum at Swiss Re means deciding…".
  - **Ariane Ehlers and Pia Burghartz:** their "your bio" / "your headline" hooks repeat Claude Schwarz, Ian Long and Ginger Turner.
  - **Ariane's M2** "An answer could start with a test on one client's applications" is close to Carl's "A one-client test could run…". **Roman's M2** "leaves every case untouched" is close to Augusto's "keeps cases untouched".
  - **Klemens Binswanger:** "Your remit for underwriting across Continental Europe at Swiss Re" is close to Augusto's "Continental Europe L&H is your territory at Swiss Re".
  - **Stock record label:** "in one timestamped record" or "as one timestamped record" appears in Claudia, Enzo and Klemens (new) and Ginger (sent). The card says: "No stock label for the scan or the record repeats across people at one company."
  - **Question topic quota:** "how would you judge or test a new build source" now covers about 7 of 28 Swiss Re people. Sent: Claude Schwarz, Velina Peneva, Anna Mazerant. New: Daniel, Ueli, Klemens, Luiz. The card allows "at most about a fifth".

**A3. Repeats among the 12 new Swiss Re pairs.** The card says: "No two people at one company share an opener, a central question, an easy-out target, a Message 2 opener or a closer."
- **Closer:** 11 of 12 use one skeleton, "[the role who does X] could join / take this / weigh in [instead / in your place / as well]":
  - Claudia, "could weigh in instead"
  - Roman, "is welcome too"
  - Ariane, "is welcome in your place"
  - Daniel, "could join the call as well"
  - Enzo, "could take this instead"
  - Klemens, "would also do"
  - Luiz, "could take this instead"
  - Michael, "could join in your place"
  - Pavel, "could join instead"
  - Pia, "could join instead"
  - Ueli, "could join the call in your place"

  Marco is the only exception. Across the whole batch, about 19 of 30 closers use this shape.
- **Easy-out target:**
  - Claudia's "The underwriting lead for one of your markets" is the same target as Klemens' "An underwriting lead who covers a single market".
  - Roman's "The market underwriter who joins your client visits" and Ariane's "The L&H underwriter who handles your clients' questions" point at the same kind of person.
  - Daniel's "The data scientist who prepares model inputs" is close to Enzo's "Whoever specifies the inputs of those tools".
- **Hook:**
  - Career path, 6 of 12:
    - Claudia: "from risk assessor to heading…"
    - Daniel: "Your move from L&H R&D to heading…"
    - Enzo: "after a path through computational chemistry and IT"
    - Luiz: "your route from products actuary to market head"
    - Marco: "after leading in-force solutions for EMEA"
    - Michael: "From underwriter to underwriting manager…"
  - The 2026-11-02 QC's top issue was this same frame.
  - "Caught my eye" twice: Ariane and Daniel.
  - Enzo ("You lead the team that builds … at Swiss Re, after …") and Marco ("You head a conversational AI solution at Swiss Re, after …") share one skeleton.
- **CTA:**
  - Claudia "Shall we talk it over on a call:" against Pavel "Talk it over on a call:".
  - "slot" three times: Roman "Book a slot for a call:", Luiz "Choose a call slot here:", Michael "A call slot is here:".
  - Pia "Calendar for a call with me:" is close to Ueli "My calendar, for a call:".
  - Batch-wide, 13 of 30 CTAs end in "… on a call:".
- **M2 opener shape:** "[An actuary / A manager / A model input / Shadow reports] [reads / can judge / needs] …: …" appears in Luiz, Michael, Daniel and Ueli. A colon-led first sentence appears in 6 of 12. Lower severity: "flag counts per threshold" is the M2 value in 8 of 12, which the reinsurance lane expects, but 4 of them keep the card phrase "candidate threshold".

**A4. Easy out given to P1 buyers.** The card gives an easy out "for people who are not the buyer", and round 4 of 2026-11-02 ended at 0 P1 easy outs. Both new P1s have one:
- Claudia: "The underwriting lead for one of your markets could weigh in instead."
- Klemens: "An underwriting lead who covers a single market would also do."

**A5. Card question target kept with its noun phrase** (2026-11-02 A3). Sebastian Soika asks "Do clients raise remote build evidence with you, or would Munich Re have to bring it up?" The card's target is "whether any client has asked about remote build evidence", and three sent questions already cover it: Volker Homola, Steven Hardy and Ulrich Pasdika.

**A6. Item 4: no market facts outside IE/DE/NL.**
- Sara: "Many applications your client insurers decide see no examination or weighing, and build is declared." Her clients are French insurers.
- Luiz: "Many applications are decided without an examination, and build is declared." It follows "market head for L&H Italy and Iberia", so it reads as a statement about that market.

**A7. Lane value missing from the M2.**
- The reinsurance lane asks for "a shadow evaluation design the team could run with one client". Three M2s lack it:
  - Marco: SDK and API only.
  - Michael: "A manager can judge the step by what the team sees…"
  - Yosra: channel choice only.
- The referral easy out should point to "whoever owns risk assessment or the new-business journey". Kate's points elsewhere: "If protection strategy sits with a product owner, a name is enough for me."

### B. Factual accuracy, 3/5

- **Clean:**
  - Every number comes from the card.
  - 3.5% appears only in M2 of the reinsurance lane (Raphael, Sophie, Daniel), with "not a scale reading" in the same sentence.
  - No client, price, pilot or trial term appears.
  - No other prospect is named.
  - No former employer that is an account is named (Declan's MRAS and Irish Life, Sara's and Jude's SCOR, Yosra's Gen Re, Luiz's Munich Re).
  - No Never term appears.
  - The compliance line is correct by lane in all 30 pairs.
- **Speed misstated:** Pia's M2 says "The step runs in under 45 seconds from the photos to structured results." The step includes the applicant taking the photos. The card's figure runs from the photos to the results, with the scan or its result as the subject (agent rule 12).
- **Claims about people that the profiles do not support:**
  - **Juliane Kania:** "your route led to heading retail life at Alte Leipziger". Her headline is "Bereichsleitung FO Privatkundengeschäft Leben" and her bio says Kundenservice and Support Excellence. That is an operations unit inside private-customer life, not the retail life business. "nursing and medical review at MDK Nordrhein" also merges two jobs: she nursed at Uniklinik Düsseldorf and was a team lead at MDK.
  - **Declan O'Neill:** "where ideas are shortlisted for client tests" is not in his bio. His question "What would put a remote build record on that shortlist?" rests on it.
  - **Roman Lerch:** "takes you into many insurers' point-of-sale journeys". His profile is the title only (client management). His M2 adds "The market underwriter who joins your client visits", which is also invented.
  - **Sebastian Soika:** his M2 mentions "your client workshops". The seminar fact belongs to Munich Re's German client programme, not to his Austria, CEE, Greece, Cyprus and Israel team.
  - **Marco Spagnuolo:** "Where a conversational tool meets an application". His bio is about in-force retention, and nothing places his assistant in an application journey. The question rests on that premise.
- **Wrong actor:**
  - Michael Kamm's M1 says "When your underwriters work a non-medical case".
  - His M2 says "what the team sees: a referral flag only on large gaps".
  - Cases inside a cedant's non-medical limits do not reach a reinsurer's underwriters, and the flag goes to the insurer.
- **Record misdescribed:** Enzo's M2 says "The fields are few: a declared weight and an estimated weight…". The record carries 80+ body measurements and BMI, and Mark Rodgers' M2 in this same batch says so.
- **Data-handling sentence reworded:** Martijn's M2 says "Photos are removed after processing or within 30 days, as the insurer's policy sets." The card says "Only the forms in compliance.md". The gate noted an overlap with Marvin Dewkurun's sent pair; that overlap is compliance wording and acceptable, but the paraphrase is not.
- **Market statements (item 4):** Sara and Luiz, see A6.
- **List-side, for Vadim** (not scored against the writer):
  - **Marco Spagnuolo:** the validator wrote "in-force retention, not new-business underwriting".
  - **Daniel Meier:** the validator wrote "risk modelling likely means the capital model". If so, the M1 line "build enters a model as one declared value" does not fit.
  - **Ariane Ehlers:** the coordinator found that Christophe Heck heads L&H France, BeNeLux & Switzerland since 2026-01-12. Her "market head" seat may now sit under him.
- Sourcing: not applicable (outbound).

### C. Brand & tone, 1/3

- **Three-item lists** (a hard ban in the template):
  - Kate's M2: "which cases take part, who sets the threshold, and that no output reaches a case". It is also not parallel.
  - Declan's M2: "one insurer, its own non-medical applications, and outputs kept away from every case".
  - Ariane's M2: "the step runs, flags are counted at each candidate threshold, and nothing reaches a case".
- **Presumed view or presumed reaction:**
  - Kate: "you see where protection is heading"
  - Michael: "you know a non-medical case from the inside"
  - Raphael's M2: "An actuary will want the denominator"
  - Ueli: "you decide which signals a solution carries"
  - Gianfranco: "means deciding which fields a product can use"
- **Idioms** (the card says "no idioms"):
  - Mark: "each new record needs a home"
  - Sara's M2: "can tell the story"
  - Jeffrey: "have to clear in IT"
  - Kate: "where protection is heading"
- **Title used as the address, which reads as a merge field** (2026-11-02 C): Myra: "Quick one for the Head of Strategic Change at New Ireland."
- **Contorted or wrong English:**
  - Sara: "Many applications your client insurers decide see no examination…" is a garden-path sentence. "before it put a photo step" has the wrong tense.
  - Sebastian: "…means many different insurers."
  - Pavel: "the guideline meets a declared build"
  - Jude: "owns the systems a new application step meets"
  - Enzo: "A tool takes build as an input from whatever the application records, and on cases with no examination that is a declared value."
  - Raphael: "before it enters a build loading discussion"
  - Ariane's question: "Which question from a client insurer about build on non-medical applications have you not yet had a good answer to?"
  - Marie's M2: "Every case in an evaluation yields a dated record, … for the cases the insurer picks." It says both every case and the cases the insurer picks.
  - Marco: "An applicant's 2 photos come back as a Smart Scales weight estimate"
  - Roman: "It raises a flag only when…". "It" could be the insurer or the estimate.
  - Klemens: "goes back with a flag" does not say where. His question has "insurers' non-medical limits differ from one client to the next", which says the same thing twice.
  - Gianfranco: his question is two questions. His M2 has "An analytics product needs history, and an evaluation starts it".
- **M2s that read as a reply:**
  - Ariane: "An answer could start with…" answers a question she never sent.
  - Mark: "Linking it to a case is a mapping exercise." The "it" has nothing to refer to inside M2.
- **Questions a stranger cannot answer well:**
  - Michael: "which evidence do they miss most?"
  - Ariane's question (above).
  - Marco's question, which rests on the unsupported premise in B.
  - Pavel: "how is a declared weight treated on cases with no examination?" The answer is obvious.

### D. Format & structure, 2/3

- The gate passes limits, signature, link placement and bans (0 hard).
- Two `proof:` lines in the writer batch are stale:
  - Marie's says "BMI from declared height", which is not in her copy.
  - Ueli's says "timestamped record", which is not in his copy.
  - If `split-messages` copies these into the `Proof point:` headers, refresh them.
- Mark Rodgers' M1 body is one paragraph of 3 sentences, with the product inside the hook paragraph. The template puts the hook first, then the product.
- Claudia's CTA "Shall we talk it over on a call:" is a question that ends in a colon before the link.
- I did not check `product:` frontmatter. The per-person files were not in my input, and the missing field is the known `split-messages` template gap, as on 2026-11-02.

### E. Output quality, 2/4

- **Strong:**
  - Questions:
    - Sophie Chapelain: would the estimate count as a reason for referral by itself, or only next to other evidence.
    - Claudia: referral or note, with an M2 that continues the question.
    - Paul Clerkin: an SDK in the page or a request from the back end.
    - Mark Rodgers: which identifier ties a record to a case.
    - Lisa Plunkett: which cases to keep outside a photo step.
    - Marie Murphy: whether a new evidence field belongs in the application at all.
    - Jude Devins: the insurer's own application or the broker's tool, tied to the broker-only fact.
  - M2s:
    - Pavel: "A client's guideline text does not change in an evaluation."
    - Klemens: "fits inside one client's own rules, whatever its limits are".
    - Jeffrey: "the flag is one field among them".
- **The Swiss Re block reads as a mail merge (A3).** Side by side, 11 of 12 closers and 6 of 12 hooks share a shape.
- **Cross-company twins** (the rubric's 60%-unique override):
  - **The technical M1 template is back** (the 2026-11-02 "tech quartet"):
    - Paul Clerkin: "FitXpress ships as a REST API and web and mobile SDKs."
    - Jeffrey and Jude: "FitXpress is a REST API with web and mobile SDKs."
    - Martijn: "FitXpress comes as a REST API and web and mobile SDKs:"
    - Richard L. (sent) has the same sentence.
  - **One product sentence in four people:** "FitXpress adds 2 photos to the application and returns a Smart Scales weight estimate" is word for word in Sebastian and Sophie, and nearly so in Claudia and Aisling. Jean Larkin (sent) has it too.
  - **Raphael and Yosra share one sentence:** "A flag shows only above the insurer's [own] threshold, in one timestamped record."
  - **One question at three reinsurers:**
    - Sara: "What would a client insurer of yours need to see before it put a photo step in front of its applicants?"
    - Luiz: "what would you ask a client insurer to show before it adds a photo step to an application?"
    - Raphael: "What would you want a client insurer to show about the estimate before…"
  - **Two actuary M2s:**
    - Raphael: "An actuary will want the denominator: flags counted out of all cases…"
    - Luiz: "An actuary reads a flag rate against its base: how many cases a threshold flags, out of how many in total."
  - **Behavioural trio:** Pia, Aisling and Francesca Tamma (sent) all get the photo step and completion. Lisa's M2 "The evaluation measures completion, showing where applicants leave." is close to Pia's M2.
  - **Easy outs:**
    - Myra's "If protection new business processes sit with another owner, please point me there." is close to Kelvin Gillen's (Irish Life, sent) "If protection new business sits in another team, please point me there."
    - Paul Clerkin and Jude both start "If a delivery lead owns the …".
    - Martijn's "…, please say so." is close to Ashish Agarwal's (sent).
  - **Questions:**
    - Ueli's question is close to Roberto Castellini's (SCOR, sent) "judge a build flag in a shadow evaluation".
    - Aisling's is close to Annika Schilling's (Gen Re, sent) "What would underwriting research want to examine first about…".
- **Account facts unused.** Only Lisa uses one, New Ireland's protection range. Facts the card allows and the writer did not use:
  - Magnum for Ueli. His headline names it, and the card allows it to Swiss Re's team.
  - Life Guide for Klemens, Michael and Pavel.
  - MIRA for Declan and Sebastian.
  - e-Risiko for Juliane.
  - The ORV page for Jeffrey.
  - AI Assistant and Velogica for Gianfranco and Martijn.

  The hooks rest on titles and career paths instead, which is why they converge.

## Top 3 issues (priority for improver)

1. **Same-company repeats (item 6).**
   - The M1 product sentence echoes a sent colleague at 9 of 11 companies: Alte Leipziger, Aviva, Gen Re, Hannover Re, Irish Life, Munich Re, NN, SCOR and Swiss Re.
   - Inside the new Swiss Re dozen: closers 11/12, career hooks 6/12, repeated CTA labels, and two central questions taken from sent colleagues (Pia from Francesca Tamma, Ueli from Claude Schwarz).
   - The writer checked questions against the sent pairs but not the product sentence, hook frame, closer or CTA.
2. **A1 regression and P1 easy outs.**
   - 8 M1s have no declared weight and no gap.
   - Two of those sentences are word-for-word twins (Aisling, Pia), and one belongs to a P1 (Claudia).
   - Both P1s get an easy out.
3. **Claims beyond the profile or the card:**
   - Juliane's role, Declan's shortlist, Roman's point-of-sale journeys, Sebastian's workshops and Marco's premise.
   - Michael's wrong actor.
   - Pia's speed sentence, Enzo's "few fields" and Martijn's data-handling paraphrase.
   - Sara's and Luiz's market statements.

## System notes (not scored against the agent)

- The gate counts word runs, not frames. A frame check against `existing-add.md` would catch most of A2 and A3. It would compare the first four words of the hook, the closer skeleton "[role] could join / take this instead", and the CTA label. The 2026-11-02 QC made the same recommendation.
- Two mechanical soft checks would catch A1 and A4:
  - an M1 that has "threshold" but no "declared" fails;
  - any easy out on a P1 fails.
- A check on the subject of "under 45 seconds" would catch "The step runs in…".
- `notify.py` was not run because this QC session has no Bash. The coordinator should send:
  `❌ QC: message-sequencer → 10/20 (failed). Top issue: widening pairs repeat sent colleagues' product sentences at 9 of 11 companies, and the 12 new Swiss Re pairs repeat each other (closer 11/12, career hook 6/12); 8 M1s lost the declared-weight gap. Recommend: rewrite the Swiss Re 12 as a block, line-edit the other 18. File: workspace/_quality/outbound/2026-11-12-message-sequencer-eu-insurance-underwriting-widening.md`

## Coordinator review

agreement: ✅ agree. My own pre-QC pass had cleared exact twins only; the frame repeats against sent colleagues and the A1 regression were not caught by me.
top_issue: The writer checked central questions against existing-add.md but not product sentences, hook frames, closers or CTAs. Fix round 1 rewrites the Swiss Re block from a grid that checks all of these against the 16 sent pairs, and line-edits the other 18.
list-side: Marco Spagnuolo moved PASS → WEAK (in-force retention, not new business); Daniel Meier kept (L&H R&D background); Ariane Ehlers kept at P3 (title possibly reshaped under Christophe Heck).
