# Fix list, round 1 — `omada-health-1` — 2026-10-19

QC scored the campaign 13/20 (`workspace/_quality/outbound/2026-10-19-message-sequencer-us-employer-obesity-care.md`).
Top issue: people at one company share sentences. Fix **only the sentences listed below**, in `messages/_batch-omada-health-1.md`,
then run `split-messages` until exit 0 and stop. Do not touch sentences not listed, other people, or other batches' files.

Rules for every rewrite (the card rules still hold):
- **Twins:** change the product specific or the sentence structure, not one or two words. Rotate: two photos (front and
  side); a guided capture on any phone; 80+ body measurements, waist and hip among them; body composition estimates
  with BMI and BMR calculated; a 3D model; white-label API and SDKs; nothing to install for the member. The person who
  is not listed keeps their sentence, so yours must also differ from theirs.
- **Call sentences:** tie the call to this person's own Message 1 question. No stock "A call could cover / would show /
  I can show… on a call" shapes; no minutes.
- **No "so" introducing a result or benefit.** No card rule restated as copy (estimates, who picks the scans, what the scan
  does not decide, "the phone as the only hardware"). Do not add data-handling, storage, deletion or decision sentences.
- Every Message 1 still names the company inside a sentence about it, keeps one product specific and ends on a real
  question. Every pair still cites one number. No new numbers; fixed proof lines verbatim and no more of them than now;
  the speed phrase whole and only where speed is the point. The compliance line stays verbatim where it is.
- This list quotes sentences to locate them. Never paste a quoted fragment, a card line or a rule from this list into a message.

## Items


### akallarakuzhi
- "so" introducing a result (M1): «You built the analytics and AI practice at OneTrust before Omada, so vendor data feeds are familiar ground.». Rewrite without "so" (two sentences, or "allowing…").
- "so" introducing a result (M2): «A call could cover the field list, IDs and timestamps, so your pipeline team can judge the load before anyone builds.». Rewrite without "so" (two sentences, or "allowing…").
- QC: M1 has no Omada account fact. Add one, per the card's Omada rule (waist, hip and the 3D model next to the weigh-ins Omada already runs).
- QC: M2 is a call agenda with no fact. Give it a value line that continues his M1 question and carries the 2-4 weeks figure for a typical basic integration (the card allows it in technical-integration M2).

### alisonmegliola
- twin (M1): «Body composition comes as estimates for the care team.». near-identical to kevin-masci-pharm-d-32b81b68 (omada-health-1): «Body composition values are estimates for the care team.». Rewrite this sentence; the other person keeps theirs.
- card rule restated as copy (M1): «Body composition comes as estimates for the care team.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.
- card rule restated as copy (M2): «Coaches could point a member to the same 3D model at each check-in, and the care team chooses which scans sit side by side.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### changheidi
- card rule restated as copy (M2): «With the phone as the only hardware, the shipping side of that step is empty.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### chunalex
- card rule restated as copy (M2): «The phone is the only hardware for this step, and a member can finish it anywhere.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### danielleburns
- twin (M1): «A guided phone scan at a check-in adds a timestamped waist and hip reading plus 80+ body measurements to the engagement picture at Omada.». opening «a guided phone scan…» shared by 4 people at Omada Health. Rewrite this sentence; the other person keeps theirs.

### danika-harrison-570372
- card rule restated as copy (M2): «A white-label capture step in the Omada app would let members take the scan at a check-in, and the program picks which scans reach the progress chart.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### ellerycook
- "so" introducing a result (M2): «The care team would choose which scans to compare, so the flow needs one extra step at the check-ins you already run.». Rewrite without "so" (two sentences, or "allowing…").
- card rule restated as copy (M2): «The care team would choose which scans to compare, so the flow needs one extra step at the check-ins you already run.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### kathryn-wintermantel-8b6a4732
- twin (M1): «A check-in scan returns 80+ body measurements, under 45 seconds from the photos to structured results.». near-identical to ellerycook (omada-health-1): «It returns 80+ body measurements, under 45 seconds from the photos to structured results.». Rewrite this sentence; the other person keeps theirs.

### kevin-masci-pharm-d-32b81b68
- card rule restated as copy (M1): «Body composition values are estimates for the care team.». Delete the restatement. If the message then has no product specific, add one from the rotation list instead; never a new data-handling, storage, deletion or decision sentence.

### mhannan313
- twin (M2): «A call would show what it looks like:  If another leader owns client reviews or the member app, point me to them.». opening «a call would show…» shared by 7 people at Omada Health. Rewrite this sentence; the other person keeps theirs.

### mmunsell
- "so" introducing a result (M1): «You came to commercial operations at Omada from corporate development at Salesforce, so systems are your lane.». Rewrite without "so" (two sentences, or "allowing…").

### shariyar
- coordinator: "numbers need a clean source" implies Omada's data is not clean (the card bans implying what a prospect's data lacks). Rewrite that sentence to state an Omada fact only.

### stanislav-b-b302704
- twin (M1): «Scan records at 3DLOOK carry random IDs, and a BAA covers qualifying enterprise deployments.». near-identical to patrick-curry-healthcare (omada-health-1): «Scan records carry random IDs and a BAA is available for qualifying enterprise deployments.». Rewrite this sentence; the other person keeps theirs.
- twin (M2): «A call could cover what your IT review needs first.». opening «a call could cover…» shared by 4 people at Omada Health. Rewrite this sentence; the other person keeps theirs.

### steve-cook-7768298
- twin (M1): «A two-photo phone scan at a check-in returns waist and 80+ body measurements with no device to ship.». near-identical to holly-morganti-a279ab4 (omada-health-1): «A two-photo phone scan returns waist, hip and 80+ body measurements, and there is no device to ship for that step.». Rewrite this sentence; the other person keeps theirs.

### terry-miller-b1333a62
- QC: his M2 offers the same call as Ashok Kallarakuzhi's ("fields, IDs and timestamps"). Rewrite his call sentence around his own M1 question.
