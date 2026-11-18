---
qc_date: 2026-11-18
agent: message-sequencer
artifact: round-4 pairs of 2026-11-17-uk-london-glp1-connections (A, 72) + 2026-11-17-uk-london-glp1-pharmacies (B, 44), 116 pairs
track: outbound
artifact_type: messages
total_score: 12/20
status: marginal
coordinator_review: done
---

# QC Report — message-sequencer — 2026-11-18 (London GLP-1, round 4, A + B)

**Artifact:** all 116 round-4 pairs (A 72, B 44), scored against both cards, `brief-r4.md` and the 2026-11-17 QC report.
**Total: 12/20, marginal.** This is a big step up from 7/20. Every Message 1 now says what FitXpress does and what the pharmacy gets: 2 photos in the session, a Smart Scales estimate and BMI next to the declared weight, a flag above the pharmacy's threshold for a clinician, and a timestamped record. Decisioning is clean, and so are the GPhC-off accounts. The score is held down by three things: colleagues at the same company still share sentences, about fifteen lines claim things about a company's own method or staff, and four messages put the GPhC point next to the company's own check. The fixes are at line level, so no regeneration is needed. About 60 people need an edit.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- The brief's same-company rule ("no two share the pain sentence, the fix wording, the order of the parts, a Message 2 value point or a closer") is broken at 18 of 31 multi-person companies. Examples: Juniper (Alyza and Kevin Joshua share the identical fix sentence; the threshold clause is verbatim ×4), Superdrug (Craig and Rachel share the company line and the pain sentence), DCA (5 of 8 use the "judged by eye, no (second) figure" pain), Oushk (identical company line) and Reset (Oliver and Ciara).
- Traps from the first-draft QC came back:
  - Rachel and Craig near-verbatim again.
  - Richard's company line is again "Mounjaro + NHS", shared with Aanisah's "runs a Mounjaro programme".
  - The speed sentence is joined to 80+ again (Nick M2).
  - G1 "too" (Jamie M2).
  - "as a secondary output" is in 13 Message 2s (flagged at Mir last round).
- The brief's sample fix sentence ("takes 2 photos on their phone inside the consultation, guided for pose and framing, with camera-roll uploads switched off") is copied verbatim in 8 Message 1s: Kavita, Omar, Alyza, Kevin Joshua, Joel, Leighton, Faisal, Alessandro. The brief says never copy the samples.

### B. Factual accuracy — 3/5
- Numbers are all on the list. No client is named and no accuracy figure appears. Liveness is used only in the approved sentence. The data handling forms are correct except one.
- **Invented facts or claims about a company's own process or staff:**
  - James O'Loan: "puts the whole patient journey into one session on a phone".
  - Alice: "Juniper's GLP-1 care starts from a weight confirmed remotely".
  - Kristien M2: "the data stays with Doctor Care Anywhere". This is not an approved data form, and 3DLOOK processes and stores the records.
  - James King: "depends on who handled the case".
  - Amel: "what each clinician notes from it can differ".
  - Zeinab: "depends on who watches it".
  - Sweta: "a team doing that across many patients", "The programme team reads".
  - Sunil: "what a patient reports between visits arrives".
  - Julie: "depending on what each patient sent".
  - Kuljeet: "the superintendent's team".
  - Bilal: "which keeps the journey short".
  - Phill: "A photo has to be judged by eye" right after MedExpress, but their photos confirm identity, not weight.
- **Methods stated where the bullet does not state them:**
  - Superdrug, snippet-only, ask-never-state (Craig, Rachel, Amit): "photo or video of scales". It also sits next to the Never "photos of feet on scales".
  - Reset and SheMed, both "not stated" (Laura Falvey, Puja): "photo or video of scales".
  - Juniper (Sarah-Jane), Second Nature (Tamara), Elaine (DCA): typed-weight lines written about the company itself.
- **Contradicts the bullet:** Nigel says "For the online route, a typed weight is only a number", but Rowlands has the patient hold scales on camera and the pharmacist asks the weight.
- **Product misdescriptions:**
  - Tim: the estimate set "beside the last figure on file". Smart Scales compares with the declared weight, not a past measurement.
  - Gabriel: "a second reading". James King: "a second view of the same figure". Both imply a scale reading.
  - "one record per patient" (Stuart, Sunil, Kristien). It is one per check.
- **GPhC point next to the company's own check** (implies a shortfall, a Never for every account):
  - Mohammad (PillSorted): "a video on scales".
  - Bryony (Numan): "a clinician reading a photo or a video".
  - Wayne (PillTime): "The weight in a questionnaire…".
  - Nigel (Rowlands).
- **Facts outside the bullet's Use:** Murdo "NHS prescription pouching service", Ruchira M2 "GP letters", Ruth's company line on Numan's alternative routes.
- The sample traps the coordinator named were checked and are allowed by the bullets: Canada (Stuart, HeliosX CEO), Health Clinic route (Superdrug), programme for women (Juniper), refills (Second Nature), monthly (Kamsons, LIVVE, Pharmacy+Health).
- Decisioning is clean: no "only" or "no need" wording, and nothing says FitXpress verifies or decides. One soft case: Jess, "FitXpress … handles that inside the session", read as confirming weight.

### C. Brand & tone — 2/3
- Plain CEO English overall. No banned words or dashes. Patients are never suspects.
- Three Message 1s join unrelated clauses to "I run 3DLOOK" (Mir, Yvonne, Richard), e.g. "I run 3DLOOK, and a visual assessment rests on judgement by eye".
- Salesy closers that are fragments: "Worth a short call?" (Chris Bland), "Worth a call?" (Karim).
- The staff-blame lines listed under B also read as criticism of the reader's own team.

### D. Format & structure — 2/3
- Every Message 1 link is on its own line, and B Message 2s are clean of the London days. G1 holds for 39 of the 41 A London-link people. Jamie breaks it ("A short call works too"). Sweta's call line leans on the meeting line ("If you would rather talk by phone").
- 29 Message 2s glue the link onto the sentence, against the card's "Links are plain text on their own line". Mechanical fix: Gary, Omar, Rajive, Danielle, Jamie, Ruth, Bryony, Bilal, Hira, Mohamed, Mubin, Chris Chan, Dara, Oliver, Rochelle, Ciara, Laura Falvey, Puja, Sarah Davidson, Rachael, Sahithi, Julie, Tyanko, Ahsan, Glenn, Ruchira, Barbara, Olivia, Chloe.
- Nick M2: the speed sentence is not its own plain sentence.

### E. Output quality — 2/4
- Message 1 now carries value in the right order (pain → mechanism → what the pharmacy gets), and the lanes mostly fit:
  - Product people get SDK and API.
  - Clinical people get "clinician decides".
  - Branch services get the remote option between visits.
  - The exception is Ruth (product lane), who gets no SDK or API in either message.
- Template feel (MSG-7):
  - The copied sample sentence (×8).
  - The same Message 2 sentence at different companies: Patrick at DCA = Jainil at Hollowood; Glenn at Avicenna = Bilal at Oushk (the server-side sentence).
  - "by eye" in 27 lines.
- Message 2 repeats Message 1 in 7 pairs: Kevin Kyle, Gianluca, Stephen, Julie, Kristien, Sanjay, Niamh.
- Grammar errors that need a fix: Mubin, Julie, Mir, Rajive, Patrick Jaffe, Oliver, Olivia, Rochelle, Christian, Ahsan (see the list).
- Some Message 1s don't hold together: Stuart (Canada → camera-roll is a non sequitur), Abdullah (never says the photos give a weight estimate), Chris Bland (photos "before the monthly visit", when the Use is the online start).

## Top 3 issues (priority for improver)

1. **Same-company sameness across A and B (18 of 31 companies).** The roster plan is not making colleagues' sentences different. Worst cases: Juniper's identical fix sentence, Superdrug's Craig and Rachel (a repeat trap), DCA's by-eye pain ×5, Oushk's identical company line, Reset's Oliver and Ciara (pain and Message 2 value point), and shared Message 2 value points at PrivateDoc, PillTime, Pyramid, Chemist4U and Numan.
2. **Claims about a company's own method or staff, and the GPhC point next to its own check.** Staff lines: James King, Amel, Zeinab, Sweta. Method lines: James O'Loan, Alice, Superdrug ×3, Laura Falvey, Puja, Nigel. GPhC next to own check: Mohammad, Bryony, Wayne, Nigel. Data claim: Kristien.
3. **Product precision.** Tim's "last figure on file", Gabriel's "second reading", James King's "second view of the same figure", and "one record per patient" ×3. Plus 13 Message 2s with the spec-sheet phrase "as a secondary output".

## Global fixes

- **R1 sameness:** before editing, rebuild each company's roster table (person | pain sentence | fix order | Message 2 value points | closer) from the actual text. Fix every collision listed below.
- **R2 own method or staff:** describe the method in general, never "who handled the case", "what each clinician notes", "the team", or "what each patient sent". "Not stated" and snippet-only accounts get the typed-weight point or a question.
- **R3 GPhC:** where the company line names a GLP-1 service but the next sentence describes that company's own step, either drop the GPhC sentence or change the pain.
- **R4 mechanical:**
  - Put the 29 glued Message 2 links (list under D) on their own line.
  - Remove "as a secondary output" from Declan, Tim, Sarah-Jane, Danielle, Nick, Tyanko, Sophie, Caleum, Julie, Christopher, Christian, Barbara and Chloe.
- **R5 photo quote:** in Alyza, Mubin, Leighton, Sophie and Jane, the January 2026 quote sits directly before "2 photos". That reads as "two photos answer the GPhC", which ties the fix to GPhC. Keep the quote away from the fix, or use the verify form.
- **R6 B Message 2 closers:** Amel ("would rather"), Aida ("suits better") and Jane ("is easier") compare against a meeting that B Message 2s never offer.

## Per-person fix list (only people who need a change beyond R4)

- **Amiry & Gilbride**
  - Sara (A): M1 "nothing in the file shows where it has gone" is unclear ("it" = weight). Say what the file lacks.
- **Assured**
  - Kevin Kyle (A): M2 "the capture adds a structured record beside them" repeats M1's record. Pick an unused value point.
- **Avicenna**
  - Glenn (B): M1 "a check often relies on a photo from a camera roll" is an unsupported market claim at a questionnaire account. Use the typed-weight point.
- **Chemist4U**
  - James O'Loan (A): cut "which puts the whole patient journey into one session on a phone" (invented). "A weight typed into that session … the review file ends up holding whatever was entered" describes Chemist4U's own method and file. Make it general.
  - Ricardo (A): "a typed figure has nothing behind it" = Declan's "a figure with nothing behind it". Reword one.
  - Christopher (B): M2 80+ = Declan's Message 2 value point. Swap it.
- **Chemist Click**
  - Gabriel (B): "adds a second reading" implies a scale reading. Smart Scales is a software estimate.
- **Day Lewis**
  - Tim (A): cut "to set beside the last figure on file"; the comparison is with the declared weight. Company line "where a clinician takes the measurements" = Mir's line.
  - Mir (B): new company line (Tim has the clinician-measurements fact). "I run 3DLOOK, and between appointments the difficulty is…" is a non sequitur. "FitXpress puts 2 photos on the patient's phone" says the wrong thing.
- **Doctor Care Anywhere** (re-plan pains together)
  - Anushka (A): "judged by eye, with no second figure beside it" is near Patrick's sentence. Reword.
  - Kristien (B): the pain is the same sentence as Patrick's and Anushka's. "FitXpress gives the reviewer that figure" ≈ Patrick's "gives the clinician that second figure". M2: cut "the data stays with Doctor Care Anywhere" (not an approved form). "one structured record per patient" should be per check. M2 also repeats M1's record.
  - Elaine (B): "the figures around it are only what the patient types" describes DCA's method. It is also the 5th by-eye pain at DCA.
  - Laura O'riordan (A): "When a patient sends a photo from their camera roll" implies DCA accepts camera-roll uploads. Make it general; the wording is also near Kavita's and Luis's.
  - Luis (A): "now sit next to the injections" turns an undated page into news. The camera-roll pain is near Kavita's.
  - Sweta (A): "a team doing that across many patients" (their staff) and "The programme team reads" (invented role). M2 call line "If you would rather talk by phone" leans on the meeting line (G1).
- **HeliosX**
  - Phill (B): "A photo has to be judged by eye" after MedExpress reads as their photos checking weight (they confirm identity). Same pain as Niamh.
  - Stuart (B): the Canada line leads into an unrelated camera-roll pain, near Jess's sentence. "one timestamped record per patient" should be per check.
  - Jess (B): "FitXpress … handles that inside the session" reads as FitXpress confirming weight. Say what it returns.
- **Hollowood**
  - Sunil (A): "what a patient reports between visits arrives…" invents a reporting step. "one timestamped record per patient" should be per check.
- **Juniper**
  - Kevin Joshua (A): fix sentence identical to Alyza's (and the brief sample). Company line "Juniper prescribes Mounjaro and Wegovy" = Patrick Jaffe's.
  - Alyza (A): fix sentence identical to Kevin Joshua's. Photo quote (R5).
  - Patrick Jaffe (A): new company line. "A form field returns a figure" = Sarah-Jane's "A weight entered in a form". "where weight gets confirmed in the product around them" is unclear.
  - Sarah-Jane (A): "the product has nothing beside it to check it against" reads as Juniper's product (not stated).
  - Alice (A): cut "starts from a weight confirmed remotely" (invents a method). "The clinician sees … flagged for a clinician" is redundant.
  - Gianluca (A): M2 "on-screen guidance for pose and framing" repeats M1.
  - Threshold clause "a gap above the threshold Juniper sets is flagged for a clinician" is verbatim ×4 (Alyza, Sarah-Jane, Kevin Joshua, Alice). Vary it.
- **Kamsons**
  - Chris Bland (A): "Before the monthly visit" doesn't fit; the Use is the online start. "Worth a short call?" is a fragment.
- **Medino**
  - Christian (B): the company line "comes with the consultation" = Henrik's "includes the consultation". "with the camera-roll picker disabled so the images come from the consultation" dangles off the record sentence.
- **My London Pharmacy**
  - Yvonne (B): "I run 3DLOOK, and a visual assessment rests on judgement by eye" is a non sequitur.
- **NowPatient**
  - Rajive (A): "Weight judged on video is judged by eye" is a tautology.
- **Numan**
  - Ruth (A): the company line uses the alternative routes (outside Use). "the weight reaches the file as a figure someone read or typed" describes Numan's process. "Whatever the route" = Danielle's. Product lane but no SDK or API in either message.
  - Bryony (A): GPhC point followed by "A clinician reading a photo or a video is judging weight by eye" (Numan's own routes; R3).
  - James King (B): cut "depends on who handled the case" (their clinicians) and "a second view of the same figure". M2 "Smart Scales stays a software estimate" = Bryony's Message 2 value point.
  - Jamie (A): M2 "A short call works too" (G1).
- **Oushk**
  - Hira (A): company line "Oushk Pharmacy offers Mounjaro and Wegovy with maintenance plans" is identical to Bilal's.
  - Bilal (A): "which keeps the journey short" is unsupported.
- **Pharmacy+Health**
  - Mark (A): "A weight is easy to check at a visit; between visits a declared weight is a typed number" overlaps Nick and Fiona.
  - Nick (A): M2 speed joined to 80+ (G3). Make the speed its own sentence.
  - Jane (B): photo quote (R5). M2 "If a call is easier" (R6).
- **Pharmalogic**
  - Mubin (A): "a camera-roll photo adds that it carries no proof of when it was taken" is garbled. Pharmalogic is questionnaire, so use the typed-weight pain. Photo quote (R5).
- **Pharmulous**
  - Amel (B): cut "what each clinician notes from it can differ" (their clinicians). The company line is near the brief sample. M2 "If you would rather talk by phone" (R6).
- **PillSorted**
  - Mohammad (A): GPhC point next to "a video on scales has to be judged by eye", which is PillSorted's own step (R3).
  - Zeinab (B): cut "depends on who watches it" (their staff). The second half equals Mohammad's "file" clause.
  - Alister (B): "something a person has to sit down and watch" implies their staff's time.
- **PillTime**
  - Murdo (B): cut "which sits alongside its NHS prescription pouching service" (outside Use). M2 speed = Leighton's Message 2 value point.
  - Wayne (B): GPhC point next to "The weight in a questionnaire is the patient's own entry" (describes the method; R3).
- **PrivateDoc**
  - Ruchira (B): M2 speed and "Video consultations and GP letters stay available" are both Chris Chan's Message 2 value points. GP letters is outside Use.
- **Pyramid**
  - Raj (B): M2 "Camera-roll uploads are switched off" = Amir's Message 2 value point.
- **Quick Meds**
  - Ahsan (A): "At 3DLOOK we make FitXpress for it." is awkward.
- **Reset Health**
  - Ciara (A): "a declared weight is only a number to start from" = Oliver's pain. M2 "keeps its current route" = Oliver's Message 2. "What is in the file before a call differs" is about Reset's file.
  - Oliver (A): M2 "would decide … and keeps" mixes tenses.
  - Laura Falvey (A): "A photo or video of scales has to be judged by eye" invents a method at a "not stated" account, next to the GPhC point.
  - Rochelle (A): "In an app, a camera-roll upload…" reads as the Roczen app accepting uploads. M2 "whenever you pick here" is ungrammatical.
- **Rightangled**
  - Abdullah (A): M1 never says the photos give a Smart Scales weight estimate and BMI, so the value is implicit.
  - Aida (B): M2 "If a call suits better" (R6).
- **Rowlands**
  - Nigel (B): "For the online route, a typed weight is only a number" contradicts the bullet (scales on camera) and sits next to GPhC (R3).
  - Stephen (B): M2 "guidance on screen for pose and framing" repeats M1.
- **Second Nature**
  - Richard (B): the company line repeats Aanisah's "runs a Mounjaro programme" (a repeat trap). "I run 3DLOOK, and for an engineering team a declared weight is a field…" is a non sequitur and ≈ Katherine's "For a product team…".
  - Sophie (A): "A weight typed in at a distance is only a number as well" ≈ Aanisah's pain. Photo quote (R5).
  - Tamara (A): "At those moments a declared weight is a typed figure" states Second Nature's method (not stated). The refills fact itself is allowed.
- **SheMed**
  - Puja (A): "A photo or video of scales has to be judged by eye" implies a scales step at a "not stated" account.
  - Chloe (B): the third SheMed company line built on clinician review (Puja, Olivia). The camera-roll pain ≈ Sarah Davidson's.
  - Olivia (B): M2 "would decide … and keeps" mixes tenses.
- **SimplyMeds**
  - Kuljeet (B): "flagged for the superintendent's team" invents a team.
- **Superdrug**
  - Craig (A) and Rachel (B): the company line is near-verbatim ("with a face-to-face route at Health Clinics" / "with a Health Clinic route for in-person care"), and so is the pain sentence. "a photo or video of scales" states a snippet-only method next to the Never. Neither asks how BMI is confirmed for online patients (Use). Rachel's appointment fact is available to differentiate her.
  - Amit (A): "a video of scales has to be judged by eye" is the same point a third time. Change it.
- **TribElle**
  - Julie (A): "It is built as 2 photos on a phone" is garbled. "depending on what each patient sent" is invented. M2 "The record shows the declared weight beside a Smart Scales estimate" repeats M1.
- **Minor (fix if time):**
  - Sanjay (B): M2 "The pharmacist chooses when a patient is asked to scan" repeats M1's "When asked".
  - Niamh (B): M2 "A pharmacist reviews any gap" repeats M1.
  - Karim (B): "Worth a call?".
  - Darryl (A): "what your side handles".
  - Tyanko (A): M2 "The same call returns 80+" (API call or phone call?).
  - Chris Chan (A): M1 "I'm in London… Could we have 30 minutes in London?".

No per-person change (global R4/R5 items may still apply): Declan, Gary, Kavita, Patrick (DCA), Jainil, Omar, Manjit, Melissa, Danielle, Joel, Fiona, Calum, Dalia, Mohamed, Leighton, Dara, Amir, Kasim, Aanisah, Katherine, Sarah Davidson, Rachael, Parvinder, Carl, Andy, Sahithi, Faisal, Joshua, Rachna, Robin, Alessandro, Henrik, Joe, Ana, Peter, Tannaz, Sunny, Philip, Doruk, Caroline, Karen, Caleum.

## Coordinator review

- agreement: agree. Round 4 fixed what Vadim rejected (Message 1 now explains the pain and how FitXpress solves it; liveness in the approved sentence; caps 900). The remaining risks are same-company sameness (the brief's samples were copied) and claims about a company's own staff or method.
- top_issue: same-company sameness across A and B (R1).
- decision: 12/20 is marginal, so no import yet. Fix round 5 by the same five writers on their own company groups, with this report as input (R1-R6 and the per-person list). After it: the mechanical gate, a coordinator scan of the changed pairs against this list, then build-import.
