# Fix round 3 — mixed-4 (2026-10-26)

QC after round 2: 15/20 (report workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md). This is the last round before Vadim. Each item is a one-line or two-line edit. Same rules for all seven batches. Edit `messages/_batch-mixed-4.md` with Edit per message.

## Rules for this round

1. **M1 question from the card's targets** (even with the verb or word order changed) is rewritten from this person's own title and work, in your own words, about something they own. It must not share its central question with a colleague at the same company.
2. **Card lane text in copy** ("The flag is a referral trigger…", "gaps large enough to cross a build band", "on gaps that would change a build rating", "with the society's rules and underwriters deciding", "a design the team could run with one client", "one integration several insurers could switch on") is replaced by a plain value line for that person.
3. **M1 opener frame.** Where the list says the opener uses the "[title] at [company], you decide/know/see…" frame, open differently: on a fact from the person's path, on the company's own fact, or on the subject of their question. Hook phrases from the template are allowed. At most two people per company keep the same frame.
4. **Stranded fixed lines** ("112,100 scans…", "3DLOOK has worked with 100+ clients.") with no job in that M2 are deleted. If the pair then needs a number, write "2 photos" (digit) in the M1 product sentence.
5. **Thin M2:** one or two sentences that continue this person's own M1 question with something new for them, before the compliance sentence. Do not reintroduce the speed line.
6. **Plain English:** no dangling "it" / "those cases" / "that pipeline" without a referent, no triples, no label lead-ins ("What FitXpress offers:"), no "from the … side of [company]" (reads as if Katerina works there), no presuming what the reader knows ("you will know", "you will have seen"), formal register (no "Fancy").
7. **Keep:** exactly one compliance sentence per pair as now, hooks, account facts, the 3.5% wording ("approximately 3.5% mean absolute error under evaluated conditions" + "not a scale reading" in one sentence, said once, without "error" twice), the call line.
8. **Metadata:** update each changed person's `Proof point` line in `## Context used` to the facts the pair now carries, and correct `_summary-mixed-4.md` (lane counts that add up, compliance split, no stale notes).
9. Re-read every changed message in full in the batch file. Run split-messages until exit 0, then stop.

## Per person


### Andrew Newton · andrew-newton-a1bb7115b · Guardian Financial Services · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: andrew-newton-a1bb7115b (opens on "Shadow means…")

### Richard Stadon · richard-stadon-64b7029 · Guardian Financial Services · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 112,100: martin-boniface-jones-371173112, james-ayland-6181bab5, damian-mapplebeck-99103818, malexandratou, richard-stadon-64b7029

### Jane Tarbuck · jane-tarbuck-11487341 · Guardian Financial Services · underwriting
- Fixed lines kept as stranded sentences with no job, since M1 already carries "2 photos". Round 2 removed the labels, but the sentences now sit as non sequiturs:: 100+: robert-arbuckle-b4aa3669, jane-lyle-a6a2b5182, réka-halász-9a72b585, gareth-alan-williams-7709b658, simon-evans-9296844b, andrew-doran-7a154617, jane-tarbuck-11487341

### Helen Croft · helen-croft-underwriting · SCOR UK · reinsurance
- Contorted sentences from the fix rounds: › Dangling references: helen-croft-underwriting: "from 2 photos and with one timestamped record"

### Hannah Cook · hannah-cook-73585829 · SCOR UK · reinsurance
- Card question targets survive with only the verb inflection or word order changed: remote build evidence: david-waters-05719b114, tsmithfia, natalie-kelly-447331a, hannah-cook-73585829

### Gill Salton · gill-salton-414848180 · SCOR UK · reinsurance
- Card question targets survive with only the verb inflection or word order changed: "build guidance treat declared and measured weight": gill-salton-414848180, tom-green-240a9222, bethan-shepherd-12a39763

### Anil Girdhari · anilgirdhari · SCOR UK · reinsurance
- Product mechanics described wrongly:: anilgirdhari M1: "FitXpress would supply 2 photos".
- Contorted sentences from the fix rounds: › Dangling references: anilgirdhari M2: "would show acceptance how often…"

### Ricky D'Gama · ricky-dgama · SCOR UK · reinsurance
- **Label lead-ins** (the pattern the coordinator removed in round 2): kerriecross ("The proposal from FitXpress:"), scott-innes-98b84830 ("What FitXpress offers:"), ricky-dgama ("A candidate for your pipeline:").
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama

### Ben Pears · pearsben · Holloway Friendly · referral
- Lane-note or rule text still in the body: "The flag is a referral trigger…", verbatim: craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a, pearsben. Round 2's rule 4 named this text. It survived because none of these five was on a round-2 per-person list.

### Danny Essam · danny-essam-43242013 · iPipeline UK · partnership
- Card question targets survive with only the verb inflection or word order changed: "new evidence step added to the journey": danny-essam-43242013, kylie-irwin-385398154
- Lane-note or rule text still in the body: Partnership target and M2 value pasted: andrew-doran-7a154617 ("one integration several insurers could switch on" and "API and web and mobile SDKs, … one timestamped record per applicant returned to the platform"), danny-essam-43242013 (the same in both messages).
- **Company not named in M1** (card and round 1 rule 8): sandi-sohal-2853aa13 (Pacific Life Re), danny-essam-43242013 (iPipeline, carried over).

### Kaj Makaswaran · kaj-makaswaran-64a176188 · iPipeline UK · partnership
- **Voice slip that reads as if Katerina works there** (the same construction the previous QC flagged for two others): james-blaney-85456b60 ("from the quality assurance side of Royal London underwriting"), hannah-spiro-27b12b106 ("from the innovation engagement desk at Aviva"), kaj-makaswaran-64a176188 ("from the underwriting services side at iPipeline").
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: david-waters-05719b114, james-sims-846a9251 ("Flags can be seen in a shadow evaluation without any effect on cases."), nicky-le-roux-7b8b758, rachel-l-2387142a, kaj-makaswaran-64a176188, amy-higgs-a1960563

### Tim Smith · tsmithfia · Hannover Re UK Life Branch · reinsurance
- Card question targets survive with only the verb inflection or word order changed: remote build evidence: david-waters-05719b114, tsmithfia, natalie-kelly-447331a, hannah-cook-73585829
- Lane-note or rule text still in the body: Reinsurance M2 value "a design the team could run with one client": claire-nolan-01708830, tsmithfia.

### Andrea Gregory · andrea-gregory-76144635 · Hannover Re UK Life Branch · reinsurance
- Card question targets survive with only the verb inflection or word order changed: "sit in the build section of the rules you support": andrea-gregory-76144635

### Lynn Baillie · lynn-baillie-b468427 · Gen Re UK · reinsurance
- Card question targets survive with only the verb inflection or word order changed: "test a new remote evidence source with clients": lynn-baillie-b468427
