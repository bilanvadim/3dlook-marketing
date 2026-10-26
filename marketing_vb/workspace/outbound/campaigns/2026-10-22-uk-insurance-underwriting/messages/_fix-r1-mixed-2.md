# Fix round 1 — mixed-2 (2026-10-26)

QC scored the campaign 12/20 (report: workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting.md). Same rules go to all seven batches. Edit `messages/_batch-mixed-2.md`, then run split-messages until exit 0.

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


### Tom Green · tom-green-240a9222 · Scottish Widows · underwriting
- QC: presumptive "you will have a view": rewrite.

### Denise Bates · denise-bates-06945338 · Swiss Re UK · reinsurance
- QC: dangling modifier ("As Head of … at Swiss Re, build loadings are part of your world"): fix the grammar.

### Dave Evans · dave-evans-bb20a920 · Swiss Re UK · technical-integration
- QC: presumptive "shape how Swiss Re UK reviews data sharing", and "ICO" is a regulator reference: remove both.

### Deborah Smith · drdeborahasmith · Swiss Re UK · medical
- M1 question repeats card question-target wording («a software weight estimate before»): write a new question from this person's own title and work.

### Alana Paterson-Barker · alana-paterson-barker-fia-cera-5a759315 · Swiss Re UK · reinsurance
- QC: "keeps its current route for anyone who does not scan" is rule text: rewrite. M1 does not name the company.

### Vicki Livingstone · vicki-livingstone-259a7098 · Swiss Re UK · reinsurance
- M1 never names FitXpress: name it in the product sentence.

### Andrew Graham · andrew-graham-2398a8ba · Swiss Re UK · reinsurance
- QC: M1 does not name the company: name Swiss Re.

### Tim Knaust · tim-knaust-1b852a55 · Swiss Re UK · reinsurance
- QC: M1 does not name the company.

### Sai Tejo Kiran · saitejokiran · UnderwriteMe · partnership
- QC: "a marketplace of partners" is not in the UnderwriteMe account bullet: remove.

### Riccardo Rossi · riccardorossilbs · UnderwriteMe · partnership
- QC: "easy to embed" is an integration-effort claim: remove.

### Kylie Irwin · kylie-irwin-385398154 · UnderwriteMe · partnership
- QC: "SDKs plus an API": no "plus" as a connector. Also "suggests you weigh…" presumes a reaction: rewrite.

### Pete Martin · pete-martin-5b401069 · UnderwriteMe · partnership
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Will Miller · will-miller-78139133 · UnderwriteMe · technical-integration
- QC: presumptive "any data … passes through you": rewrite.

### Steve Smith · steve-smith-17111a95 · Zurich UK · underwriting
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.
