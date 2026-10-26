# Fix round 1 — mixed-1 (2026-10-26)

QC scored the campaign 12/20 (report: workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting.md). Same rules go to all seven batches. Edit `messages/_batch-mixed-1.md`, then run split-messages until exit 0.

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


### Szymon Marszalek · szymon-marszalek · VitalityLife · underwriting
- M1 question repeats card question-target wording («gap between declared and estimated»): write a new question from this person's own title and work.

### Paul Yarham · paul-yarham-945164a0 · VitalityLife · underwriting
- QC: "The applicant provides 2 photos and nothing else" is wrong (height is declared too): remove it.

### Gareth Alan-Williams · gareth-alan-williams-7709b658 · VitalityLife · proposition
- QC: "wherever the journey wants it": rewrite plainly.

### Fareeha Brownless · fareeha-brownless-nee-hasani-84b7b413 · VitalityLife · proposition
- QC: "keeps its current route for anyone who does not scan" is rule text: rewrite.

### Stuart Jackson · stuart-jackson-bb8a035b · VitalityLife · proposition
- QC: "wherever the journey wants it": rewrite plainly.

### Simon Evans · simon-evans-9296844b · VitalityLife · proposition
- QC: M1 does not name the company: name VitalityLife.

### Mala Thurston · mala-thurston-22a0b499 · Pacific Life Re · reinsurance
- QC: presumptive "client insurers will look to their reinsurer": rewrite.

### Martin Boniface-Jones · martin-boniface-jones-371173112 · Pacific Life Re · reinsurance
- QC: "Friends Life UK" is now part of Aviva, an account here: do not name it.

### Justin Farrow · justin-farrow-226782108 · Pacific Life Re · reinsurance
- QC: "Norwich Union Healthcare" is now part of Aviva, an account here: do not name it.

### Caroline Smith · caroline-smith-78180535 · Pacific Life Re · reinsurance
- M2 opens on 80+ body measurements (secondary, never the lead): open on the value line for this person's question.
