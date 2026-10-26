# Fix round 1 — mixed-4 (2026-10-26)

QC scored the campaign 12/20 (report: workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting.md). Same rules go to all seven batches. Edit `messages/_batch-mixed-4.md`, then run split-messages until exit 0.

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


### Richard Stadon · richard-stadon-64b7029 · Guardian Financial Services · underwriting
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Hannah Cook · hannah-cook-73585829 · SCOR UK · reinsurance
- QC: M2 value line is one thin sentence: add one that continues this person's own M1 question.

### Anil Girdhari · anilgirdhari · SCOR UK · reinsurance
- QC: "from the acceptance side of SCOR's treaty work" reads as if Katerina works there; M2 has no value line (only compliance + CTA): add one that continues the M1 question.

### Sarah Barrell · sarah-barrell-133690131 · Holloway Friendly · referral
- QC: "from the operations side of Holloway Friendly" reads as if Katerina works there: rewrite.

### Danny Essam · danny-essam-43242013 · iPipeline UK · partnership
- QC: "Saw the news on…" frames the September 2025 rollout as news: drop the news framing.

### Helena Mbcs · helena-ashton-mbcs-4775788 · iPipeline UK · technical-integration
- QC: "per policy" cuts the approved form: write "per the insurer's policy".
