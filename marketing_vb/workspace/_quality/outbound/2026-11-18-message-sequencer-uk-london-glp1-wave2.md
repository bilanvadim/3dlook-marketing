---
qc_date: 2026-11-18
agent: message-sequencer
artifact: second-wave pairs of 2026-11-18-uk-london-glp1-pharmacies-2 (B2, 37) + 2026-11-18-uk-london-glp1-connections-2 (A2, 5), 42 pairs, read from the coordinator's company-grouped file pairs-w2-all.md (first-wave A1/B1 rows as context)
track: outbound
artifact_type: messages
product: fitxpress
total_score: 11/20
status: failed
coordinator_review: pending
---

# QC Report — message-sequencer — 2026-11-18 (London GLP-1, second wave, A2 + B2)

**Artifact:** all 42 new pairs (A2 5, B2 37), scored against both cards, `brief-w2.md`, `fix-common.md` (F1-F6), the r4 QC report and the second-wave decisions block.
**Total: 11/20, failed.** Under decision 6, a score below 12 stops the run.

The mechanics are clean, and the gates confirm it. Every Message 1 also carries pain, then mechanism, then value. The account decisions hold: no GPhC point at My London Pharmacy, Day Lewis, HeliosX or PPRX; Quincy is never named; liveness appears once per pair in the approved sentence.

Three things fail. First, the wave's headline rule: 33 of the 42 new pairs repeat wording that a colleague at the same company was already sent, or that another new colleague uses. This happens at 19 of the 20 companies with more than one person. Second, 19 lines invent, contradict or overstate a company fact, including a factual error about Saxenda. Third, the writers fell back on lane templates, so whole paragraphs are near-identical across companies.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 2/5
- **Roster rule broken (brief "Roster first" + F2).** Several new pairs reproduce a pair that was already sent, almost word for word:
  - Mark McGuire's three-sentence fix is Tim Rendell's.
  - Martyn K.'s fix and ask are Christopher Tufts's, down to "A call works if not."
  - Thomas Curtis's fix is Laura Falvey's.
  - Mo Umar's threshold sentence and closer are Ruth Pointon's.
  - Michael Whitman's ask is Aanisah's with two words changed.
  - Scott McDougall's fix is Andy Boysan's, and his ask is Philip Hawkins's.
- **Company lines repeat facts a first-wave colleague already led with:** Camran (= Omar), Barry (= Niamh), Oliver Brooks (= Elaine), Ryan (= Kevin Joshua), Rishi (= Dalia/Ana), Avtar (= Parvinder), Abbas (= Gabriel). John Foreman and Nikita open with the same first words as Sanjay and Caleum.
- **New colleagues collide with each other:** Day Lewis Sam/Rupa/Mark (one company line ×3), Second Nature (four Mounjaro-programme lines, two "and little else" pains), Everest (ask shape), Juniper Erin/Catherine (pain).
- **r4 traps are back, although the brief says they still apply:**
  - Mounjaro + NHS line at Second Nature (Chris Edson).
  - A staff-consistency line at Numan (Mo).
  - Product lane with no SDK or API (Rebecca, Yousef).
  - GP letter outside Use (Jay).
  - "Whatever the …" = Danielle at Numan (Qaiser).
  - Redundant "clinician sees … flagged for a clinician" (Shimal, Paul, Mo, Rebecca, Kathryn).
- **Message 1 has two questions** in 4 cases (Catherine, Mo, Ugnė, Rebecca), and no question at all at Thomas Curtis.
- Ryan's ask is "in London" although Juniper is London: yes, so it should be at their office.
- Held: no GPhC point at the off accounts; My London Pharmacy has no regulatory context; Abbas is not tied to Quincy; the A2 Message 2 closes follow the A rule; B2 Message 2s never name the dates.

### B. Factual accuracy — 3/5
- Numbers all come from the card list. No client is named, no accuracy figure appears, and the data forms are correct. Decisioning is clean: no "only flagged" wording, nothing per patient, no "weighs".
- **Factual error:** Nicholas Sears says "NowPatient's range runs beyond the GLP-1 medicines to Saxenda". Saxenda is liraglutide, which is a GLP-1 medicine.
- **Contradicts the bullet:**
  - Yousef at My London Pharmacy: "the weight arrives as a figure the patient declares". Every patient there sends a photo and a video. On an account with a regulator matter on record, this also reads as a remark on its review file.
  - Paul at PrivateDoc, which asks for a scales photo: a stated-weight pain next to the GPhC point (R3).
  - Amish at NowPatient, which runs a video eligibility check: a declared-figure pain next to the GPhC point.
- **Invented process, staff or method:**
  - Kuldip: "between branch visits a weight the patient reports", inside the GPhC sentence.
  - Sam: "read from a message or a photo … by whoever reads it".
  - Mo: "depends on how consistently each image is read". Numan's photo step is implied to be weaker.
  - Erin: "Juniper's included, a typed weight is a text field with no check behind it".
  - Thomas: "a GLP-1 decision starts from the weight and BMI a patient declares".
  - Ryan: "nothing in the journey records…" and "moves the weight check into the consultation".
  - Mike: "has to run for every patient", "a request to the patient and a wait".
  - Avtar: "usually means asking for extra evidence".
  - Gurdev: a camera-roll pain at an in-branch account.
  - Catherine: "typed into a form" at Juniper.
  - Nicholas Faulkner: "a clinician's note".
- **Outside the bullet:**
  - Rupa: "Run as a family business" (touches ownership, a Never).
  - Nicholas Faulkner: "to delivery".
  - Jay: the GP letter (ruled outside Use in r4).
- **HeliosX:** Barry's "asks patients for photos once checkout is done" drops "to confirm their identity", so the photos read as weight evidence (r4 Phill trap).
- **Implied customer:** Rizwan's "Rowlands keeps one timestamped structured record per check" is in the present tense.

### C. Brand & tone — 2/3
- Plain English. No banned words or dashes, patients are never suspects, and there are no corrective negations.
- **Openers that tell the reader what his question is (F1):**
  - Qaiser: "which makes what the phone camera can return an engineering question".
  - Alex: "an integration question before anything else".
  - Mike: "On the operations side of…".
- **Lines aimed at the reader's own staff:** Sam ("whoever reads it"), Mo ("how consistently"), Aisha ("the prescriber has to accept").
- **Grammar:**
  - "The patient produces it" with no referent (Waqqass, Amish, Nikita).
  - Nikita's misplaced "between…" phrase.
  - Stacked appositives: "FitXpress, made by 3DLOOK, which I run," (Rupa); also Kathryn and Qaiser.
  - "Wegovy tablets and injection and Mounjaro" (Rizwan).
  - "in the same layout" (Mark).
  - "only that patient's own figure" (Kuldip).

### D. Format & structure — 2/3
- Links, signatures and caps are clean (gates). The A2 London-link closes are self-contained. Paul's call line "If you prefer a phone call" leans on the meeting line (G1, minor).
- **One-question rule:** two questions in four Message 1s, and none in Thomas's.
- **"I'm in London … 30 minutes in London"** in 10 Message 1s: Ryan, Paul, Jay, Alex, Rebecca, Thomas, Mike, Chris Edson, Michael, Rosie. The r4 minor item (Chris Chan) has spread.
- **Three value points in a Message 2** (the card says one or two): John, Omar, Avtar, Nikita, Scott, Katy.

### E. Output quality — 2/4
- The Message 1 value is there and specific, and most lanes fit. Several pairs fail the outbound 60%-unique check across companies.
- **Technical template:** Martyn ≈ Katy ≈ Camran ≈ Jay ("2 photos on the patient's phone, camera-roll picker disabled, pose and framing guid… on screen. The API returns … timestamped structured record … beside the declared figures"). Nicholas Faulkner ≈ Alex Nancekievill (the same two sentences).
- **Compliance template:** Waqqass ≈ Amish (first sentence and fix almost identical). "The patient produces it from 2 photos" appears ×6 (Jeff, Waqqass, Amish, Nikita, Rizwan, Rishi/Chris Edson variants).
- **Referral template:** Ugnė ≈ Michael. The fix sentence, the Message 2 value point ("Scan records sit on random identifiers."), the easy out and "A call can also be booked here" are all shared. Rupa's ask = Ugnė's word for word.
- **Clinical Message 2:** "Smart Scales gives a software estimate of weight, … a clinician reads … beside the declared figure" (Thomas = Rosie; also Kuldip, Nicholas F, Catherine).
- **Other repeated lines:**
  - "BMI is calculated from the height the patient supplies" ×7; Kathryn's sentence = Scott's.
  - "where it would sit" in 10+ asks.
  - "how far apart the two figures may be before a case goes to a clinician" (Abbas = Rizwan).
- **Message 2 repeats Message 1:** Mark, Jeff, Mo, Qaiser, Mike, Rosie, Thomas.
- **Message 1s that don't hold together:**
  - Jeff: Summary Care Record → "A photo in a file".
  - Erin: FitXpress is never named in either message.
  - Ryan: a two-sentence fix with no threshold or capture detail.

## Top 3 issues (priority for improver)

1. **Same-company sameness against the first wave (33 of 42 pairs, 19 of 20 companies).** Writers had `existing-sent-pairs.md`, a roster table and F2, and still reproduced sent paragraphs (Mark/Tim, Martyn/Christopher, Thomas/Laura, Scott/Andy, Michael/Aanisah). The roster-by-prompt approach does not work at this density. A mechanical same-company n-gram check would catch all of these. Run it per company against `existing-sent-pairs.md` and the new batch, flagging any shared run of 6+ words in Message 1 or a shared Message 2 value sentence. It belongs in `outbound_pack.py check-messages` before the next write.
2. **Claims about a company's own method, staff or facts.** These are Yousef, Paul and Amish (contradicting the bullet, two of them next to GPhC), Kuldip, Sam, Mo, Erin, Thomas, Ryan, Mike, Avtar and Gurdev (invented), Rupa, Nicholas F and Jay (outside the bullet), Barry (identity dropped), Rizwan (implied customer) and Nicholas Sears (the Saxenda error).
3. **Lane templates across companies.** The technical, compliance, referral and clinical-Message 2 families above, plus "BMI is calculated…" ×7.

## Global fixes

- **W1 rewrite by company, not by lane.** For each company, list the sent rows first, then rewrite every flagged new row against them. Several bullets are exhausted by the first wave: Second Nature (9 people), Juniper (9), Numan (9), Doctor Care Anywhere (10), Reset (8), HeliosX (7), Day Lewis (7), SimplyMeds (3). Where that happens, the new row takes the question form for "not stated" accounts, or a bullet fact no colleague used. Otherwise the coordinator drops the lowest-priority person (for example one of Sam or Rupa, two referral asks to two Executive Directors at Day Lewis).
- **W2 claims (R2/R3 again):** pains about the method in general. Never "the journey", "the file", "the prescriber has to accept" or a reporting step at that company. Where the bullet shows a photo, video or scales step, never use the stated-weight pain next to GPhC.
- **W3 templates:** no sentence of 8+ words shared with a pair at another company in this wave. The fastest fixes are the four families in E.
- **W4 ask:** one question per Message 1. Drop "I'm in London" where the ask already says "in London", and keep "at your office" for London: yes accounts (Ryan, Abbas).
- **W5 Message 2:** at most two value points, none already in the same pair's Message 1.

## Per-person fix list

Format: **Name (wave):** "exact sentence" → what to change. Company groups follow the artifact order. People not listed need no change.

**Britannia Pharmacy**
- **Gurdev Channa (B2):** "In remote monitoring, a photo from a camera roll carries no proof of when it was taken." → Check is *in branch*. A camera-roll pain invents a photo monitoring step (F5). Use the in-branch pain (weight checked at a visit), without Tim's or John's "snapshot".

**Chana Chemist**
- **Kuldip Chana (B2):** "GPhC guidance expects prescribers to verify independently the weight, height or BMI a patient declares, and between branch visits a weight the patient reports is only that patient's own figure." → It invents a between-visit reporting step (r4 Sunil trap) and glues it to the GPhC point, which reads as a shortfall. Keep GPhC as its own sentence (or drop it), and make the pain the in-branch point with no reporting claim. "only that patient's own figure" is a tautology.

**Chemist Click**
- **Abbas K. (A2):** "Online, Chemist Click sells Mounjaro and Wegovy injections and oral GLP-1 tablets." → This is Gabriel's sent fact; fronting "Online," only dodges F2. Lead with the Harrow/Watford pharmacy (Use) or the question form.
- **Abbas K. (A2):** "At 3DLOOK we make FitXpress, which takes that step into the consultation: 2 photos on the patient's phone in the same session, with camera-roll uploads switched off." → Echoes Gabriel's sent "adds a weight step inside the consultation: 2 photos on the patient's phone … with camera-roll uploads switched off". Change the wording and the order of parts.
- **Abbas K. (A2):** "…and Chemist Click chooses how far apart the two figures may be before a case goes to a clinician." → Word for word the same as Rizwan's (Rowlands). Vary one.
- **Abbas K. (A2):** "Could we meet for 30 minutes to see where it would fit?" → London: yes, so name his office (Harrow or Watford).

**Chemist4U**
- **Martyn K. (B2):** "A weight typed into a consultation form arrives with no figure to check it against." → Echoes James O'Loan's sent "a weight typed into an online form is only a number". Use a different pain shape.
- **Martyn K. (B2):** "FitXpress is an SDK that opens a capture inside the consultation: … The API returns a timestamped structured record with a Smart Scales weight estimate and BMI beside the declared figures, flagged where the gap passes the threshold Chemist4U sets." → Near-verbatim of Christopher Tufts's sent fix, and the template shared with Katy H. Rewrite both the order and the words.
- **Martyn K. (B2):** "If you are in London from 23 to 25 November, could we spend 30 minutes on the integration? A call works if not." → Christopher's sent ask and closer. Write a new ask.

**Day Lewis Pharmacy** (GPhC off; re-plan the four together)
- **Sam Patel (B2):** "Weight management at Day Lewis Pharmacy happens in its pharmacies." → Same company line as Rupa and Mark. Each needs its own line (see W1).
- **Sam Patel (B2):** "A weight read from a message or a photo has to be judged by whoever reads it." → Invents a message/photo step and points at the reader (F5, staff trap). Use the in-branch pain.
- **Sam Patel (B2):** "Inside the session the patient uses their phone for 2 photos, …" → At a branch service, say it is a remote option between visits; "the session" is undefined here.
- **Sam Patel (B2):** "Could I have 30 minutes at your office on one of those days, or a pointer to whoever runs the service?" → "Could I have 30 minutes at your office" is Rachna's sent ask, and the easy out duplicates Rupa's. Write a new ask.
- **Sam Patel (B2):** Message 2 "If a colleague runs the service, I would be glad to hear who. A call can also be booked on my calendar:" → Same easy out as Rupa; "A call can also be booked" is shared with Ugnė and Michael. Vary.
- **Rupa Patel (B2):** "Run as a family business, Day Lewis Pharmacy offers its weight service face to face in its pharmacies." → Cut "family business" (outside the bullet, touches ownership). The rest repeats Sam's and Mark's line.
- **Rupa Patel (B2):** "A check that needs a branch visit asks the patient to travel for it." → Same point as Shimal's pain. Differentiate one of them.
- **Rupa Patel (B2):** "FitXpress, made by 3DLOOK, which I run, is a remote capture." → Stacked appositives. Restructure the sentence.
- **Rupa Patel (B2):** "Could you give me 30 minutes at your office, or point me to whoever runs the weight service?" → Word for word Ugnė's ask (Numan). Write a new ask.
- **Rupa Patel (B2):** Message 2 "If the weight service sits with a colleague, an introduction is all I would ask." → "an introduction is all I would ask" = Michael Whitman's. In "To book a call instead", "instead" can read as call vs meeting (R6); drop it.
- **Shimal P. (B2):** "Any check that needs the patient in a branch ties the timing of a follow-up to the visit slot." → Same point as Rupa's. Keep one.
- **Shimal P. (B2):** "…the clinician gets a Smart Scales weight estimate and BMI … Any gap above the threshold Day Lewis sets goes to a clinician…" → Redundant; cut one clinician.
- **Mark McGuire (B2):** "Day Lewis Pharmacy delivers its weight service through its branches." → Same line as Sam and Rupa.
- **Mark McGuire (B2):** "For a remote check, what ends up in the review file tends to vary from case to case." → ≈ Tim's sent "a remote check between visits has little to go on".
- **Mark McGuire (B2):** "3DLOOK, which I run, makes FitXpress as a remote option between visits. The patient takes 2 photos on their phone, guided for pose and framing, and the pharmacist sees a Smart Scales weight estimate and BMI next to the declared figures. A gap above the threshold Day Lewis sets is flagged for review, and each check is saved as one timestamped record in the same layout." → This is Tim Rendell's sent fix, three sentences, nearly word for word. Rewrite it in full. "in the same layout" is unclear.
- **Mark McGuire (B2):** "Could I have 30 minutes at your office to show where it would fit beside a branch visit?" → The opening is Rachna's (and Sam's).
- **Mark McGuire (B2):** Message 2 "BMI is calculated from the height the patient supplies, and it appears beside the Smart Scales estimate." → The second half repeats Message 1, and the sentence is the wave's most repeated Message 2 line. Swap the value point.

**Doctor Care Anywhere**
- **Oliver Brooks (B2):** "Weight-loss patients at Doctor Care Anywhere get a WhatsApp health coach." → Elaine's sent fact (health coach). The bullet is exhausted at 10 people; use an angle no colleague led with (the edited-image review) or W1.
- **Oliver Brooks (B2):** "Could we spend 30 minutes at your office on where it would sit?" → ≈ Elaine's sent "Could we spend 30 minutes at your office on that?". Write a new ask.
- **Oliver Brooks (B2):** "FitXpress goes in as an SDK for the capture, 2 photos on the patient's phone with the camera-roll picker disabled, and an API for the result." → The mid-list appositive is hard to parse. Split the sentence.
- **Jeff Hadaway (B2):** "A photo in a file shows a person, and a weight read from it is an estimate made by eye." → The 4th by-eye pain at DCA (Patrick, Anushka, Elaine; flagged in r4), and a non sequitur after the Summary Care Record line. Use a different pain.
- **Jeff Hadaway (B2):** Message 2 "If a call would help, my calendar is here:" → Kristien's sent closer, word for word. Write a new closer.
- **Jeff Hadaway (B2):** Message 2 "BMI is calculated from the height the patient supplies and shown next to the Smart Scales estimate." → Repeats Message 1 and is the template line. Swap the value point.

**Everest Pharmacy**
- **Waqqass Sheikh (B2):** "The pharmacy sets the threshold above which a gap is flagged for a clinician, and the patient produces it from 2 photos on their phone with camera-roll uploads off." → "it" points to the threshold. The whole fix paragraph ≈ Amish's (NowPatient). Rewrite.
- **Waqqass Sheikh (B2):** "…could we meet for 30 minutes, or speak by phone?" → Same ask shape as Aisha's "…or talk by phone?". Change one of them.
- **Aisha Suleman (B2):** "Everest Pharmacy offers weight-loss treatment nationwide through Everslim, with virtual consultations." → Same fact as Waqqass's opener (Everslim online). One of the two can take the face-to-face branches half of the bullet, without numbers.
- **Aisha Suleman (B2):** "When a weight is typed into a consultation, it is only a number the prescriber has to accept." → "the prescriber has to accept" points at their prescribers. Make it about the method.

**Green Light Pharmacy**
- **John Foreman (B2):** "Green Light Pharmacy offers weight management through its London branches." → Same first three words and verb as Sanjay's sent line (F2). Change the opening.
- **John Foreman (B2):** Message 2 "Photos are deleted after processing or within 30 days, per the pharmacy's policy." → Sanjay's sent Message 2 point, same words. Swap it, which leaves two value points.
- **John Foreman (B2):** "FitXpress adds a record for the weeks between visits: each check is one timestamped structured record, …" → "record … record" is redundant. Minor.

**HeliosX**
- **Kathryn Ganz (B2):** "FitXpress, from 3DLOOK, which I run, is an SDK that keeps that step inside the session." → ≈ Rebecca's (Reset) "FitXpress, from 3DLOOK, keeps that check inside the session". "the patient has to find and finish" invents patient effort. Vary both.
- **Kathryn Ganz (B2):** "Could I have 30 minutes at your office to look at where it would sit in the journey?" → Same target as Nicholas Faulkner's "where it would sit in the MedExpress flow". Change one.
- **Kathryn Ganz (B2):** Message 2 "BMI is calculated from the height the patient supplies, and scan records sit on random identifiers." → Word for word Scott's (The Independent Pharmacy). Vary one.
- **Barry Pace (B2):** "MedExpress asks patients for photos once checkout is done." → Niamh's sent fact. Without "to confirm their identity", the photos read as weight evidence (r4 Phill trap). Use a different line (W1).
- **Barry Pace (B2):** "HeliosX sets the threshold, a gap above it is flagged for a clinician, and each check is saved as one timestamped record." → ≈ Niamh's sent "HeliosX sets the threshold, a gap above it goes to a pharmacist". Vary. The fix never says the 2 photos are on the patient's phone in the session; add it.
- **Nicholas Faulkner (B2):** "Wherever a weight is judged by eye, the integration has little to store except a clinician's note." → The same by-eye point as Jess's sent pain, and "a clinician's note" invents what is stored. "from consultation to delivery" in the line before is outside the bullet.
- **Nicholas Faulkner (B2):** "At 3DLOOK we ship FitXpress as an SDK with an API. The API returns a Smart Scales weight estimate and BMI as structured fields beside the declared weight, from 2 photos taken in the session with the camera-roll picker disabled." → Near-identical to Alex Nancekievill's two sentences. Vary.

**IQ Doctor**
- **Camran Khan (A2):** "Before a prescriber reviews a GLP-1 order, IQ Doctor requires evidence such as BMI photos." → Omar's sent line, reordered. Use the unused drug range or the question form.
- **Camran Khan (A2):** "At 3DLOOK we make FitXpress as an SDK for the capture: 2 photos on the patient's phone inside the session, camera-roll picker disabled, pose and framing guidance on screen." → The opener is Omar's sent "At 3DLOOK we make FitXpress"; the rest is the technical template (Jay, Martyn, Katy). Vary.

**Juniper**
- **Ryan Nolan (A2):** "Juniper's UK service sells Mounjaro and Wegovy." → Kevin Joshua's sent fact. "UK service" hints at Eucalyptus's other countries (Never). See W1.
- **Ryan Nolan (A2):** "When a weight is only stated by the patient, nothing in the journey records how or when it was confirmed." and "…moves the weight check into the consultation itself." → Together they describe Juniper's journey and imply its check sits outside the consultation (not stated). Make both general.
- **Ryan Nolan (A2):** The fix is two sentences with no threshold, guidance or camera-roll. Add parts to reach three or four sentences.
- **Ryan Nolan (A2):** "I'm in London 23 to 25 November. Could we meet for 30 minutes in London?" → London: yes, so 30 minutes at their office, and drop the second "in London".
- **Erin Chuah (B2):** "In any GLP-1 product flow, Juniper's included, a typed weight is a text field with no check behind it." → Not a company line from the bullet, and it states Juniper's own method ("no check behind it"). Same point as Sarah-Jane's sent pain and Catherine's. Use a company line plus a general pain.
- **Erin Chuah (B2):** FitXpress is named in neither message. Name it.
- **Erin Chuah (B2):** "Through the API, each check comes back as one structured record: …" → Same parts and order as Sarah-Jane's sent fix. Reorder.
- **Catherine Bell (B2):** "How does a weight reach the clinical record at Juniper once a patient declares it?" → A second question in Message 1, and the same how-question Gianluca was sent.
- **Catherine Bell (B2):** "A figure typed into a form can only be taken at face value." → Implies a form at Juniper (not stated) and is the same point as Erin's.
- **Catherine Bell (B2):** "Juniper sets the threshold for how far apart the two figures may be, …" → ≈ Gianluca's "Juniper sets a mismatch threshold" (the r4 Juniper threshold pile-up). "how far apart the two figures may be" is shared with Abbas and Rizwan.
- **Catherine Bell (B2):** "Could we have 30 minutes at your office to look at where that fits?" → ≈ Sarah-Jane's sent "Could we take 30 minutes at your office to look at where it would sit?".

**My London Pharmacy** (no regulatory context)
- **Yousef Yaghoubi (B2):** "In a remote consultation the weight arrives as a figure the patient declares, and the review file has little to set it against." → Contradicts the bullet (every patient sends a photo and a short video for a visual assessment), and on this account it reads as a remark on its file. Use what a cross-check and a record add to the photo-and-video step (Use), in words Yvonne was not sent, or the patient journey alone.
- **Yousef Yaghoubi (B2):** The lane tag is product, but there is no SDK or API in either message. The hypothesis has him as director and superintendent. Add the SDK clause, or retag.

**NowPatient**
- **Nicholas Sears (B2):** "NowPatient's range runs beyond the GLP-1 medicines to Saxenda, Mysimba and orlistat." → Factual error: Saxenda (liraglutide) is a GLP-1 medicine. Correct the line.
- **Nicholas Sears (B2):** "On any video call, a weight is judged by eye from whatever the camera shows." → Rajive's sent pain ("a visual judgement"). Use a different pain.
- **Nicholas Sears (B2):** "It comes from 2 photos the patient takes on their phone during the consultation, guided on screen for pose and framing." → "guided on screen for pose and framing" is Rajive's sent wording. Vary it. "gives the pharmacist" should match the bullet's clinicians.
- **Amish Patel (B2):** "NowPatient sells Mounjaro, Wegovy and Foundayo, and GPhC guidance expects … At a distance, a declared figure carries no record of how or when it was confirmed." → NowPatient runs a video eligibility check, so a declared-figure pain next to GPhC implies it does not confirm weight (R3). Drop GPhC and use the patient-journey reason (the app, per Use).
- **Amish Patel (B2):** "NowPatient sets the threshold above which a gap is flagged for a clinician. The patient produces it from 2 photos…" → "it" has no referent, and the paragraph ≈ Waqqass's. Rewrite.

**Numan** (never imply the in-app photo is weaker)
- **Qaiser Mazhar (B2):** "Numan's patients start in an app, which makes what the phone camera can return an engineering question." → Joe's sent fact (app). The clause tells a CTO what his question is (F1) and is hard to parse.
- **Qaiser Mazhar (B2):** "Whatever the capture method, an image reaches the back end as a file, and nothing in it is a number a system can compare." → "Whatever the…" = Danielle's "Whatever the route" (flagged in r4); the point = Joe's sent "nothing numeric".
- **Qaiser Mazhar (B2):** "In the app the patient takes 2 photos in the session with the camera-roll picker disabled, and the API returns a Smart Scales weight estimate and BMI next to the declared figures." → ≈ Jamie's sent fix. Reorder and reword.
- **Qaiser Mazhar (B2):** "My London dates are 23 to 25 November. Could we have 30 minutes at your office to look at where it would sit in the app?" → ≈ Ruth's sent "My London days are…" and James King's "Could we have 30 minutes at your office". "to look at where it would sit in the app" is the fix-round example, copied.
- **Qaiser Mazhar (B2):** Message 2 "The SDK runs inside the app flow, and the API sends the results to Numan's own systems." → Repeats Message 1. Use an unused value point.
- **Mo Umar (B2):** "How is a weight review run at Numan today? Any check built on reading an image depends on how consistently each image is read." → Two questions in Message 1. The second sentence is about Numan's reviewers and implies a weaker photo step; this trap was already cut from James King at Numan. Rewrite.
- **Mo Umar (B2):** "Inside the consultation the patient takes 2 photos on their phone, …" (= Danielle's sent words) and "A gap above the threshold Numan sets is flagged for a clinician, …" (= Ruth's sent sentence). Rewrite the fix.
- **Mo Umar (B2):** Message 2 "To arrange a call, use this link:" → Ruth's sent closer. The "BMI is calculated…" point repeats Message 1 and Ruth's Message 1. Swap both.
- **Ugnė Kerševičiūtė (B2):** "Who owns the weight programme at Numan?" → A second question, and no company line from the bullet.
- **Ugnė Kerševičiūtė (B2):** "Weight confirmed at a distance often rests on what a person reads from a photo." → The 5th by-eye pain at Numan; "often" is an unsupported market claim.
- **Ugnė Kerševičiūtė (B2):** "I run 3DLOOK, which makes FitXpress for that step. The patient takes 2 photos on their phone in the session, a Smart Scales weight estimate and BMI appear beside the declared figures, and any gap past a threshold Numan sets goes to a clinician." → The same fix as Michael Whitman's, and the Message 2 is his too (random IDs, "belongs to a colleague", "A call can also be booked here"). Rewrite her pair and Michael's apart.

**PPRX**
- **Omar Kadir (B2):** Message 2 has three value points (server-side, BMI, boundary). Optional: drop one.

**Pharmica**
- **Rishi Krishna (B2):** "Pharmica sells Mounjaro and Wegovy online from central London." → Dalia's and Ana's sent fact. The Wegovy pill is the unused part of the bullet. "nothing in the session gives a clinician anything to read it against" is clumsy.

**PrivateDoc**
- **Paul Marshall (A2):** "PrivateDoc sells Wegovy, Mounjaro and liraglutide online, and GPhC guidance expects … At a distance, a weight a patient states has nothing independent beside it." → PrivateDoc asks for a scales photo, so a stated-weight pain contradicts the bullet and, next to GPhC, implies a shortfall (R3). Drop GPhC and lead with the patient journey.
- **Paul Marshall (A2):** "At 3DLOOK we make FitXpress for the weight step of the patient journey." (= Chris Chan's sent "…for this step") and "A gap above the threshold PrivateDoc sets is flagged for a clinician." (= Chris Chan's, word for word). Rewrite. "in the same consultation" repeats "as part of the consultation", and the record is missing (leadership lane).
- **Paul Marshall (A2):** "I'm in London 23 to 25 November. Would you have 30 minutes for me in London?" → "in London" twice, and ≈ Dara's sent ask.
- **Jay Jetley (B2):** "PrivateDoc accepts a recent GP letter as an alternative to photos." → r4 ruled GP letters outside Use. See W1.
- **Jay Jetley (B2):** "Evidence in different forms leaves different things in a file." → Chris Chan's sent "what goes into the review file differs from case to case".
- **Jay Jetley (B2):** "Through an SDK, FitXpress runs a guided capture inside the consultation: … The API returns one timestamped structured record per check, … a gap above the threshold PrivateDoc sets comes back flagged for a clinician." → The technical template (Camran, Martyn, Katy) plus Chris Chan's threshold clause. Vary.
- **Jay Jetley (B2):** "I'm in London 23 to 25 November. Could we have 30 minutes in London to look at where it would sit in the flow?" → "in London" twice.

**Reset Health**
- **Alex Nancekievill (B2):** "In the Roczen app, a weight step is an integration question before anything else." → Rochelle's sent fact (the Roczen app), also used by Rebecca. It tells a CTO what his question is (F1).
- **Alex Nancekievill (B2):** "3DLOOK, which I run, ships FitXpress as an SDK with an API. The API returns a Smart Scales weight estimate and BMI beside the declared figures, from 2 photos taken in the session with the camera-roll picker disabled." → Nicholas Faulkner's sentences, with the same parts and order as Rochelle's sent fix. Vary.
- **Alex Nancekievill (B2):** "…could we spend 30 minutes in London on where it would sit in the app?" → Same target as Rochelle's sent "a look at the app flow". "My London dates … in London" is redundant.
- **Rebecca Ryan (B2):** "Does a weight check at Reset Health stay inside the Roczen app?" → A second question, and the third Reset line on the Roczen app.
- **Rebecca Ryan (B2):** Product lane with no SDK, API or camera-roll in either message (r4 Ruth trap). Add them. "FitXpress, from 3DLOOK, keeps that check inside the session." ≈ Kathryn's sentence.
- **Rebecca Ryan (B2):** "I'm in London 23 to 25 November. Which day would suit 30 minutes in London to look at where it would sit?" → "in London" twice, and the "where it would sit" template.
- **Thomas Curtis (B2):** "For a prescriber at Reset Health, a GLP-1 decision starts from the weight and BMI a patient declares." → States Reset's prescribing process (not stated; r4 Alice "starts from" trap). Make it general or a question.
- **Thomas Curtis (B2):** "From 2 photos the patient takes on their phone in the session, a clinician sees a Smart Scales weight estimate and BMI beside the declared figures. A gap beyond the threshold Reset Health sets is flagged for a clinician, who makes the call on what it means, …" → Laura Falvey's sent fix almost word for word, in the same lane. Rewrite.
- **Thomas Curtis (B2):** "I'll be in London 23 to 25 November, and I would value 30 minutes in London to hear how weight is handled in your clinical work today." → Not a question; make the ask a question. "in London" twice.
- **Thomas Curtis (B2):** Message 2 "Smart Scales gives a software estimate of weight, which a clinician reads beside the declared figure." → Rosie's Message 2, and a repeat of his Message 1. Swap it.

**Rowlands Pharmacy**
- **Rizwan Ali (A2):** "Rowlands keeps one timestamped structured record per check, …" → The present tense with the company name reads as if Rowlands already uses FitXpress. Make it conditional, or "the pharmacy".
- **Rizwan Ali (A2):** "The patient produces it from 2 photos …, and Rowlands decides how far apart the two figures may be before a case goes to a clinician." → The compliance template, plus Abbas's sentence word for word. Vary.
- **Rizwan Ali (A2):** "Rowlands sells Wegovy tablets and injection and Mounjaro." → Double "and". Minor.

**Second Nature** (the sent rows use up the bullet; see W1)
- **Mike Gibbs (B2):** "On the operations side of Second Nature's Mounjaro programme, a weight check has to run for every patient." → Aanisah's sent fact. "has to run for every patient" invents a process, and the opener frames his role (F1).
- **Mike Gibbs (B2):** "Wherever a typed weight needs confirming, the check becomes a request to the patient and a wait for the reply." → Invents an operational step. Use the general typed-weight point.
- **Mike Gibbs (B2):** "Inside the programme the patient takes 2 photos on their phone, with pose and framing guided on screen, …" → Katherine's sent "takes 2 photos on their phone inside the programme, guided for pose and framing on screen". "Second Nature sets the threshold, and a gap above it is flagged for a clinician." = Chris Edson's clause and Barry's. Rewrite.
- **Mike Gibbs (B2):** "Could we have 30 minutes in London to go through where it would sit in delivery?" → Katherine's sent ask. Message 2 "Capture guidance for pose and framing stays on screen throughout." repeats his Message 1.
- **Chris Edson (B2):** "At Second Nature, a Mounjaro programme runs next to NHS digital weight management." → The Mounjaro + NHS line r4 flagged at Richard; both halves were sent (Aanisah, Richard).
- **Chris Edson (B2):** "…built from 2 photos the patient takes on their phone in the session, …" → Sophie's sent words. "Could we spend 30 minutes in London on how it would sit in the patient journey?" ≈ Richard's sent ask.
- **Michael Whitman (B2):** "Second Nature has a Mounjaro programme, and I'm trying to find who owns it." → Aanisah's sent line.
- **Michael Whitman (B2):** "A typed weight goes into a record as a number and little else." → Aanisah's sent pain; "and little else" is also Rosie's.
- **Michael Whitman (B2):** "Could we have 30 minutes in London, or could you introduce me to whoever owns the programme?" → Aanisah's sent ask with two words changed. His fix and Message 2 = Ugnė's (see Numan).
- **Rosie Carr (B2):** "Weight is part of the clinical side of Second Nature's Mounjaro programme." → The fourth new Mounjaro-programme line, and it says nothing.
- **Rosie Carr (B2):** "A declared weight gives a clinician what the patient reports and little else to read it against." → "and little else" = Michael's. "The patient takes 2 photos on their phone in the session, and the clinician sees…" = Michael's sentence.
- **Rosie Carr (B2):** "Could we spend 30 minutes in London on what a clinician can and cannot read from the estimate?" → Richard's and Chris's frame ("Could we spend 30 minutes in London on…"). Message 2 = Thomas's and repeats her Message 1.

**SimplyMeds Online**
- **Avtar Sagoo (B2):** "Mounjaro and Wegovy are the two weight-loss medicines SimplyMeds Online sells." → Parvinder's sent fact, and "the two" asserts a complete list from snippets. Use the question form in a shape Kuljeet was not sent.
- **Avtar Sagoo (B2):** "Online, confirming a declared weight usually means asking for extra evidence, and that evidence arrives in a different shape each time." → "usually" is an unsupported market claim, and the line implies SimplyMeds asks for evidence. "Online," is Parvinder's sent opener. "with … the camera roll switched off" = Parvinder's. Message 2 has three points; trim to two.

**The Family Chemist**
- **Nikita Dhain (B2):** "The Family Chemist sells Wegovy, Mounjaro and Foundayo online from Nottingham." → The first four words are Caleum's sent line (F2).
- **Nikita Dhain (B2):** "FitXpress leaves the pharmacy one timestamped structured record per check, and a gap above the threshold the pharmacy sets between a Smart Scales weight estimate and the declared weight goes to a clinician. The patient produces it in the consultation itself, with 2 photos on their phone, guided for pose and framing, with no uploads from the camera roll." → The "between…" phrase is misplaced, "it" has no referent, and "with … with" is clumsy. "a gap above the threshold the pharmacy sets" is Tannaz's and Sunny's sent clause. Rewrite.
- **Nikita Dhain (B2):** Message 2 "3DLOOK has worked with 100+ clients." → Tannaz's sent Message 2 point. Swap it, which leaves two points.

**The Independent Pharmacy**
- **Scott McDougall (B2):** "FitXpress runs inside the pharmacy's own flow through an SDK or API, at the assessment stage: the patient takes 2 photos on their phone with the camera roll switched off, and a Smart Scales estimate and BMI appear next to the declared figures. A gap above the pharmacy's own threshold goes to a clinician, and each check is saved as a timestamped structured record." → Andy Boysan's sent fix, almost word for word. Rewrite.
- **Scott McDougall (B2):** "If you are in London on 23 to 25 November, could we meet for 30 minutes, or arrange a call if not?" → Philip's sent "…could we meet for 30 minutes, or would a call suit you better?". Message 2 has three points, and its first sentence = Kathryn's.

**Well Pharmacy**
- **Katy H. (B2):** "FitXpress is an SDK that adds a capture step to that flow, …" → = Christopher's sent opener (Chemist4U). "The API returns a timestamped structured record with a Smart Scales weight estimate and BMI beside the declared figures" = Martyn's. No change is needed if Martyn and Camran are rewritten; otherwise vary. Message 2 has three points; trim to two.

No per-person change: none of the 42 is fully clean. Omar Kadir's change is optional, and Katy H.'s depends on Martyn's and Camran's rewrites.

## Coordinator review

(filled in by the coordinator after the auto-run)
