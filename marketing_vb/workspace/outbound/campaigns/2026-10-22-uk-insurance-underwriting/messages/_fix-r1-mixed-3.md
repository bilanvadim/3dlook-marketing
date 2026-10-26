# Fix round 1 — mixed-3 (2026-10-26)

QC scored the campaign 12/20 (report: workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting.md). Same rules go to all seven batches. Edit `messages/_batch-mixed-3.md`, then run split-messages until exit 0.

## Rules for this round

1. **Compliance: exactly one compliance sentence per pair, verbatim, in Message 2 before the call line.** It is either the GDPR line or the boundary sentence, as your per-person list says. The list names every pair that changes; pairs not listed already carry the right one. Referral, partnership and medical carry the boundary sentence; technical-integration carries the GDPR line. If it pushes M2 over 550, shorten the other M2 sentences, never the compliance sentence.
   - GDPR line: In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.
   - Boundary sentence: FitXpress is not a medical device and does not make underwriting decisions.
2. **M1 question:** built from this person's own title and work, in your own words, about something this person owns. No run of five words from the card's lane "Question targets".
3. **Rule and lane text is not copy.** Each listed sentence is rewritten in plain words for that person, or deleted.
4. **Number filler goes.** A sentence whose only job is to carry a number is deleted. The pair's number then comes from the M1 product sentence written with the digit form "2 photos", or from an approved figure inside a sentence that does real work for that person.
5. **80+ body measurements never opens Message 2.** Open on the value line.
6. **Message 2 value line:** continues this person's own M1 question with something new for them (the evaluation, the record, the integration, the threshold). One or two sentences, before the compliance sentence.
7. **One company, no shared openings:** no two people share the first four words of M2, the call line, the first six words of the M1 product sentence or the first five words of the M1 question. Where the list says "reword yours", change that person and leave the other.
8. **Name the company and FitXpress in every Message 1.** The company may be its common short name (Vitality, Guardian, Hannover Re).
9. Change only what the list names, plus what a change forces. Re-read every changed message in full before split-messages. Keep the hooks, the account facts and everything QC called clean.

## Per person


### Michael Williams · michael-williams-0901a823 · Shepherds Friendly · referral
- QC: "keeps its current route for anyone who does not scan" is rule text: rewrite.

### Sam Chivers · samuelchivers · Shepherds Friendly · referral
- QC: "SMF24 responsibility" is a regulator reference: remove.

### David Piggin · david-piggin-a6039a27 · The Exeter · underwriting
- M1 question repeats card question-target wording («gap between declared and estimated»): write a new question from this person's own title and work.

### Lara Harkins · lara-harkins-27835b21a · The Exeter · underwriting
- QC: "never a correction of declared weight" is rule text: rewrite.

### Lloyd Williams · lloyd-williams62 · Munich Re UK Life Branch · reinsurance
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Adrian Stevenson · adrian-stevenson · Munich Re UK Life Branch · reinsurance
- QC: M2 is one sentence restating the lane note, then "Open slot:": write a real value line that continues his question.

### Matt Bone · matt-bone-4b127a4a · Munich Re UK Life Branch · reinsurance
- QC: three-item list in M2 ("which cases, which candidate thresholds, and how a flag compares"): one or two points. M2 value line is one thin sentence: add one that continues this person's own M1 question.

### James Norton · james-norton-591741b2 · Munich Re UK Life Branch · reinsurance
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Madhu Sridharan · sridharanmadhusudhanan · Munich Re UK Life Branch · reinsurance
- QC: presumptive "will want the evidence before the product. So here is…": rewrite.

### Anna Currie · anna-c-6b5a7226 · RGA UK · reinsurance
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Emma Jones · emma-jones-99a3834b · RGA UK · reinsurance
- QC: "with UK protection as the example" is an account-fact instruction turned into copy: rewrite the question. M2 value line is thin: add one that continues her question.

### Rebecca Abayakoon · rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345 · RGA UK · reinsurance
- QC: "taking UK protection as the example" is an account-fact instruction turned into copy: rewrite the question. M2 value line is thin: add one that continues her question.

### Mike Evans · mike-evans-9760a310a · RGA UK · reinsurance
- M1 question repeats card question-target wording («declared and estimated weight would»): write a new question from this person's own title and work.
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Dean Scotson · deanscotson · RGA UK · technical-integration
- QC: presumptive "you review the data flows of any evaluation a client insurer runs": rewrite.

### Sue Kissane · sue-kissane-859216121 · Cirencester Friendly Society · underwriting
- M1 question repeats card question-target wording («gap between declared and estimated»): write a new question from this person's own title and work.

### Karl Pickering · karl-pickering-1918555 · LV= · technical-integration
- QC: "35 years" is not an approved number (and the bio says 35+): drop the figure.
