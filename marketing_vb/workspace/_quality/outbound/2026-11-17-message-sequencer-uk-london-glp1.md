---
qc_date: 2026-11-17
agent: message-sequencer
artifact: all SEND pairs of 2026-11-17-uk-london-glp1-connections (A, 72) + 2026-11-17-uk-london-glp1-pharmacies (B, 44)
track: outbound
artifact_type: messages
total_score: 7/20
status: failed
coordinator_review: done
---

# QC Report — message-sequencer — 2026-11-17 (London GLP-1, A + B)

Scores: Adherence 2/5 · Factual accuracy 1/5 · Brand & tone 1/3 · Format 1/3 · Output quality 2/4 = **7/20 (failed)**.

Done right: no GPhC point at the 8 "off" accounts; the photo quote only where allowed; no first-contact frame, no past-contact reference, no liveness/clothing/accuracy number, no client named; B M2s never name the London days; unconfirmed offices say "in London"; asks name the actual office; M1 asks are clear.

## Top 3
1. Decisioning: 9 people are told only flagged cases reach a clinician (worst: Phill, HeliosX, M1 "route only the unusual cases to the clinical team").
2. Same-company sameness across A and B: 23 of 31 multi-person companies share a company line or an M2 value point; verbatim at Pharmulous, near-verbatim at Superdrug, Pyramid, Pharmacy+Health, PillSorted, Numan, Reset, Rightangled, DCA. Root cause: A and B written without a shared per-company record.
3. A M2 meeting line not removable: 25 of 41 call lines start "Or / Otherwise / instead", 11 more lean on "too / also / better / simpler"; meeting line without ask or dates at Chris Chan, Dara, Amir, Abdullah, Craig, Doruk. Plus invented account facts (PillSorted "for women"; HeliosX photos confirm identity, not weight; Henrik "technical director", "as are you by your profile"; Chris Bland "retakes at the counter"; Jess / Phill review-queue inferences) and "2-4 weeks" ×5 (not on the number list).

Other: speed sentence "The scan returns 80+ body measurements, under 45 seconds…" ×21 (speed must be its own plain sentence; 80+ never leads; once per company); GPhC point next to the account's own check (Luis DCA, Gary Avicenna); Never breaches (Sanjay Green Light "as group superintendent", James O'Loan "pharmacy group", Carl St Helens questionnaire description); scan in M1 longer than one clause (Anushka, Mubin, Caleum, Rachael, Christopher, James King); Joel (Peak) never asks whether Peak offers medicated weight loss; presumed photo steps ("retakes included" Ricardo, Amit; Glenn "no need to open every image"); overclaims (Joshua "FitXpress … does that"; Rachael "last piece of a clinical record … do that"); Danielle (Numan) camera-roll point implies their in-app step is weaker. B tone: 10 career-move openers, ~15 "you own / you are accountable / is yours"; auditor framing to superintendents (Tim, Melissa, Mir); grammar (Dara, Anushka, Phill, Carl, Julie, Chris Chan M2); telling people what they think (Alice, Chloe, James King, Abdullah); "Hi Dr Tim," / "Hi Dr Laura,"; no A M1 names 3DLOOK.

## Global fixes
- G1 (A only) removable meeting line: the call line stands alone (no "Or", "Otherwise", "instead", "too", "also", "better", "simpler"); the meeting line holds the dates, the ask and the London link. Fix the meeting line at Chris Chan, Dara, Amir, Abdullah, Craig, Doruk.
- G2 decisioning: no "only"/"no need" wording about clinical review; a gap above the threshold is flagged to a clinician and nothing implies other cases skip review (Jainil, Sunil, Alyza, Caroline, Mohamed, Sophie, Phill M1+M2, Yvonne, Kuljeet).
- G3 speed sentence: its own plain sentence, 80+ never leads, at most once per company.
- G4 remove "2-4 weeks" (Jamie, Calum, Tyanko, Caleum, Murdo).
- G5 B openers: no career-move/headline openers, no "you own / you are accountable / is yours".
- G6 write each company as one roster, A and B together, distinct company line, reason and M2 value point per person.

## Per-person fix list
- Avicenna — Gary (A): M1 drop "sets eligibility on a qualifying BMI" next to the GPhC line; M2 value point other than the record; G1. Glenn (B): M1 reason other than the GPhC verify line; M2 drop "no need to open every image"; G5.
- Chemist4U — James O'Loan (A): M2 remove "pharmacy group", value point other than the threshold; M1 company line without "online-only". Ricardo (A): M1 remove "retakes included"; M2 remove "One number…" and "built for volume"; G3. Christopher (B): M1 company line without "online-only"; G5.
- Day Lewis — Tim (A): greeting; M1 drop "what the review file holds"; M2 value other than the threshold; G1. Rachna (B): cut career line and "carry the weight" pun; company line other than "clinician reviews BMI"; G5. Mir (B): drop "look at the protocol together"; M2 remove "as a secondary output"; G5.
- Doctor Care Anywhere (re-plan all 8 together) — Kavita (A): company line other than "wider care"; M2 value other than the Smart Scales estimate. Sweta (A): company line other than the full-body photo; M2 different value; G1. Patrick (A): M2 value other than Smart Scales; G1. Luis (A): M1 remove the GPhC line or change the company line; M2 rewrite; G1, G3. Laura O'riordan (A): company line Kavita does not have; cut "At board level the point is simple"; G1. Anushka (A): grammar, one-clause scan; M2 new value; G1. Kristien (B): company line other than full-body photo review; M2 value other than flagged cases + record; G3. Elaine (B): change "asks each weight-loss patient for a full-body photo"; M2 rewrite, drop "engineer-friendly"; G5.
- Hollowood — Jainil (A): M1 remote option between visits, not photos "taken in the consultation"; company line other than Sunil's; G2. Sunil (A): M2 value other than the threshold; G2.
- Juniper — Alyza (A): company line other than coaching; M2 cut duplicate threshold and Smart Scales; G1, G2. Sarah-Jane (A): M2 rewrite; G1, G3. Kevin Joshua (A): company line other than coaching, reason other than the GPhC line; M2 value other than the threshold. Patrick Jaffe (A): change "timestamped weight record", company line other than coaching; G1. Alice (A): cut "As a doctor you will care"; M2 value other than threshold and Smart Scales; G1. Gianluca (A): G1.
- Kamsons — Chris Bland (A): M2 remove "retakes at the counter".
- LIVVE — Melissa (A): drop the auditor framing.
- Numan — Danielle (A): M2 drop the camera-roll point; company line other than Ruth's and Joe's; G1. Jamie (A): G4; M2 value other than the API. Ruth (A): company line other than in-app photo + ID. Bryony (A): M2 new value, no repeated "flag gaps"; G1. James King (B): change company line, reason and M2 value (all shared with Bryony); G5. Joe (B): company line other than head-to-knee photo; M2 value other than camera-roll and API; G5.
- Paydens — Caroline (A): company line other than "booked as in-person appointments"; G2.
- Peak — Joel (A): ask whether and how Peak offers medicated weight loss.
- Pharmacy+Health — Jane (B): change company line and reason (near-verbatim with Fiona); M2 value other than speed. Nick (A): company line other than "monthly after face-to-face"; G3. Mark (A): M2 replace "A new service lands easily…" with a lane value point.
- Pharmalogic — Mubin (A): one-clause scan; M2 no repeated flag.
- Pharmica — Calum (A): remove the anniversary-to-SDK non sequitur; G4. Dalia (A): G1. Ana (B): company line other than "sells … online"; M2 value other than pose and framing.
- Pharmulous — Amel (B): new company line (verbatim with Mohamed); M2 value other than the threshold. Mohamed (A): cut "Reviewing video is time spent by a person"; G1, G2.
- PillSorted — Zeinab (B): remove "GLP-1 care for women" and the third-person opener. Alister (B): company line other than Mohammad's video-on-scales line; G3. Mohammad (A): M2 lane value instead of boilerplate; G3.
- PillTime — Leighton (A): M2 add a lane value point. Peter (B): company line other than "free online assessment"; G5. Wayne (B): G3, G5. Murdo (B): G4, G5.
- PrivateDoc — Dara (A): fix "allows patients confirm", dated ask last; G1. Chris Chan (A): M2 meeting line; G1. Ruchira (B): company line other than the three-photo line.
- Pyramid — Raj (B): new company line (near-identical to Amir's). Amir (A): G1.
- Quick Meds — Ahsan (A): M2 introduce/explain the threshold. Tyanko (A): G4.
- Reset — Laura Falvey (A): greeting; M2 one question, no repeat of M1. Barbara (B): change company line and reason; M2 new value; G5. Rochelle (A): M2 no three-item list; G1. Ciara (A): company line other than the Roczen app, drop "puts weight"; G1, G3. Oliver (A): soften "each route needs weight confirmed with the same confidence"; G1; closer not shared with Ciara.
- Rightangled — Aida (B): new company line (near-verbatim with Abdullah). Abdullah (A): cut "the setting owners tend to ask about first"; G1. Doruk (A): G1.
- Rightdose — Kasim (A): M2 lane value; G3.
- Rowlands — Nigel (B): M2 real value line. Stephen (B): G5.
- Second Nature — Richard (B): company line other than Mounjaro + NHS; M2 value other than speed and camera-roll; G3. Katherine (A): drop "eligibility step", company line other than Mounjaro + NHS; G1. Sophie (A): replace the generic opener; G1, G2. Aanisah (A): M2 value other than the threshold; G1. Tamara (A): G1, G3.
- SheMed (re-plan all 5 together) — Rachael (A): cut "last piece of a clinical record" and "do that"; M2 value other than record + 100+; G1. Sarah Davidson (A): company line other than "quiz and blood test"; G1, G3. Puja (A): M2 no repeat of M1, fix "sit for 30 minutes"; G1. Olivia (B): company line other than "quiz and blood test". Chloe (B): cut the presumed reaction and the "quiz and blood test" line; G3.
- SimplyMeds — Kuljeet (B): change company line and reason (shared with Parvinder); M2 value other than the threshold; G2, G5. Parvinder (A): greeting; fix "decide what an estimate… may flag"; M2 no repeat of M1.
- St Helens — Carl (A): remove the questionnaire description and the garbled clause.
- Superdrug — Rachel (B): new company line and ask (near-verbatim with Craig); appointment fact allowed. Amit (A): remove "retakes included"; G1, G3. Craig (A): M2 meeting line needs an ask.
- The Family Chemist — Caleum (A): one-clause scan; G4. Tannaz (B), Sunny (B): G5.
- The Independent Pharmacy — Philip (B): company line other than "after an online assessment" (Andy has it); G3.
- TribElle — Julie (A): fix the fragment; M2 drop "small practice"; G1, G3. Sahithi (A): M2 drop "small team"; G1.
- HeliosX — Stuart (B): photos confirm identity (not weight), cut "would change that sequence"; G5. Phill (B): rewrite, cut "route only the unusual cases", "behind the scenes", "that queue is yours"; G2. Jess (B): cut inferred review and "scarce" claims. Niamh (B): M2 value other than the threshold. All four share the post-checkout upload line: vary it.
- Medino — Alessandro (B): fix the garbled ask; G5. Henrik (B): cut "as are you by your profile" and "technical director".
- Chemist Click — Joshua (B): cut "does that"; G5. Gabriel (B): M2 remove the retakes presumption; G5.
- Green Light — Sanjay (B): remove the superintendent reference.
- Asda — Faisal (B): G5.
- My London Pharmacy — Yvonne (B): G2.
- NowPatient — Rajive (A): G1.
- No change: Bilal, Hira (Oushk), Karen (Paydens), Darryl (Peak). Strong ones to keep near as is: Darryl, Hira, Karen, Christian, Robin, Karim, Sara Amiry, Manjit, Andy.

## Coordinator review
- agreement: agree; the decisioning lines and cross-campaign sameness are the real risks, both caused by the coordinator's batch plan (A and B written blind to each other).
- top_issue: decisioning claims (G2).
- decision: QC < 12 → no import; fix round run as company rosters (A+B together) by fresh writers, with the current pairs + this list as input. Added coordinator rule: every A M1 names 3DLOOK once ("at 3DLOOK", "I run 3DLOOK"), since connections may not remember it.
- red flag sent to Vadim in chat 2026-11-17.
