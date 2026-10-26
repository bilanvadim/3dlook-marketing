# Fix round 3 — legal-general (2026-10-26)

QC after round 2: 15/20 (report workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md). This is the last round before Vadim. Each item is a one-line or two-line edit. Same rules for all seven batches. Edit `messages/_batch-legal-general.md` with Edit per message.

## Rules for this round

1. **M1 question from the card's targets** (even with the verb or word order changed) is rewritten from this person's own title and work, in your own words, about something they own. It must not share its central question with a colleague at the same company.
2. **Card lane text in copy** ("The flag is a referral trigger…", "gaps large enough to cross a build band", "on gaps that would change a build rating", "with the society's rules and underwriters deciding", "a design the team could run with one client", "one integration several insurers could switch on") is replaced by a plain value line for that person.
3. **M1 opener frame.** Where the list says the opener uses the "[title] at [company], you decide/know/see…" frame, open differently: on a fact from the person's path, on the company's own fact, or on the subject of their question. Hook phrases from the template are allowed. At most two people per company keep the same frame.
4. **Stranded fixed lines** ("112,100 scans…", "3DLOOK has worked with 100+ clients.") with no job in that M2 are deleted. If the pair then needs a number, write "2 photos" (digit) in the M1 product sentence.
5. **Thin M2:** one or two sentences that continue this person's own M1 question with something new for them, before the compliance sentence. Do not reintroduce the speed line.
6. **Plain English:** no dangling "it" / "those cases" / "that pipeline" without a referent, no triples, no label lead-ins ("What FitXpress offers:"), no "from the … side of [company]" (reads as if Katerina works there), no presuming what the reader knows ("you will know", "you will have seen"), formal register (no "Fancy").
7. **Keep:** exactly one compliance sentence per pair as now, hooks, account facts, the 3.5% wording ("approximately 3.5% mean absolute error under evaluated conditions" + "not a scale reading" in one sentence, said once, without "error" twice), the call line.
8. **Metadata:** update each changed person's `Proof point` line in `## Context used` to the facts the pair now carries, and correct `_summary-legal-general.md` (lane counts that add up, compliance split, no stale notes).
9. Re-read every changed message in full in the batch file. Run split-messages until exit 0, then stop.

## Per person


### Michael Spiteri · spiterimichael · Legal & General · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "review a new data processor (for the new-business journey)": rebecca-mcgeoch-186807134, johnunderwood2, spiterimichael, deanscotson

### Tariq Surty · tariq-surty-8911101 · Legal & General · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "SDK step enter the e-application": steve-lister-87b0671, tariq-surty-8911101, karl-pickering-1918555
- Product mechanics described wrongly:: tariq-surty-8911101 M1: "2 photos and a Smart Scales estimate go in". The estimate is an output.

### Gary M. · gary-m-3b7b913b · Legal & General · referral
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama

### Steve Davis · sdavis2 · Legal & General · referral
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 100+: hai-luc-67306367, sdavis2, scott-wallace-b608b49b, william-stratton-8ab764104

### Nicki Plews · nicki-plews-b037aa2b · Legal & General · proposition
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama

### Sara Denyer · sara-denyer-b81a2a92 · Legal & General · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413

### Jenni Phillips · jenni-phillips-98892a24 · Legal & General · underwriting
- Contorted sentences from the fix rounds: › Dangling references: jenni-phillips-98892a24: "a candidate for that pipeline", with no pipeline named
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 3.5%: david-banks-9b750391, jenni-phillips-98892a24, andrew-greatbanks-9712b03b

### John Redmond · john-redmond-884597a · Legal & General · underwriting
- Lane-note or rule text still in the body: "gaps large enough to cross a build band": john-redmond-884597a, brian-kemp-0467b898. brian-kemp also has the card rule "adds evidence to cases that get no screening".
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413
- Other shared lines inside a company:: Same M2 skeleton: james-hetherington-461ba352 and riccardorossilbs ("The step could be offered / would be available through web and mobile SDKs…"); john-redmond-884597a and brian-kemp-0467b898

### David Banks · david-banks-9b750391 · Legal & General · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 3.5%: david-banks-9b750391, jenni-phillips-98892a24, andrew-greatbanks-9712b03b

### Brian Kemp · brian-kemp-0467b898 · Legal & General · underwriting
- Lane-note or rule text still in the body: "gaps large enough to cross a build band": john-redmond-884597a, brian-kemp-0467b898. brian-kemp also has the card rule "adds evidence to cases that get no screening".
- Product mechanics described wrongly:: brian-kemp-0467b898 M1: "takes 2 photos and a Smart Scales estimate".
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413
- Other shared lines inside a company:: Same M2 skeleton: james-hetherington-461ba352 and riccardorossilbs ("The step could be offered / would be available through web and mobile SDKs…"); john-redmond-884597a and brian-kemp-0467b898

### Scott Wallace · scott-wallace-b608b49b · Legal & General · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 100+: hai-luc-67306367, sdavis2, scott-wallace-b608b49b, william-stratton-8ab764104

### Nicky McRae · nicky-mcrae-a4a3b5206 · Legal & General · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413

### Pippa Barber · pippa-barber-nee-keefe-487b64b6 · Legal & General · proposition
- Card question targets survive with only the verb inflection or word order changed: the card's list of journey points (adviser-keyed, client declaration, direct): scott-reid-950a3410, gary-beyer-37995610 (all three points), pippa-barber-nee-keefe-487b64b6
- Contorted sentences from the fix rounds:: "FitXpress is/would be 2 photos", the pattern the coordinator flagged in four other messages: pippa-barber-nee-keefe-487b64b6, jack-southcott-30959929.
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama

### Hai Luc · hai-luc-67306367 · Legal & General · proposition
- Triples: hai-luc-67306367: "structured, timestamped, one per application"
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 100+: hai-luc-67306367, sdavis2, scott-wallace-b608b49b, william-stratton-8ab764104

### Bethan Shepherd · bethan-shepherd-12a39763 · Legal & General · underwriting
- Card question targets survive with only the verb inflection or word order changed: "build guidance treat declared and measured weight": gill-salton-414848180, tom-green-240a9222, bethan-shepherd-12a39763

### Andrew Greatbanks · andrew-greatbanks-9712b03b · Legal & General · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 3.5%: david-banks-9b750391, jenni-phillips-98892a24, andrew-greatbanks-9712b03b
