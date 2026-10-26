# Fix round 3 — royal-london (2026-10-26)

QC after round 2: 15/20 (report workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md). This is the last round before Vadim. Each item is a one-line or two-line edit. Same rules for all seven batches. Edit `messages/_batch-royal-london.md` with Edit per message.

## Rules for this round

1. **M1 question from the card's targets** (even with the verb or word order changed) is rewritten from this person's own title and work, in your own words, about something they own. It must not share its central question with a colleague at the same company.
2. **Card lane text in copy** ("The flag is a referral trigger…", "gaps large enough to cross a build band", "on gaps that would change a build rating", "with the society's rules and underwriters deciding", "a design the team could run with one client", "one integration several insurers could switch on") is replaced by a plain value line for that person.
3. **M1 opener frame.** Where the list says the opener uses the "[title] at [company], you decide/know/see…" frame, open differently: on a fact from the person's path, on the company's own fact, or on the subject of their question. Hook phrases from the template are allowed. At most two people per company keep the same frame.
4. **Stranded fixed lines** ("112,100 scans…", "3DLOOK has worked with 100+ clients.") with no job in that M2 are deleted. If the pair then needs a number, write "2 photos" (digit) in the M1 product sentence.
5. **Thin M2:** one or two sentences that continue this person's own M1 question with something new for them, before the compliance sentence. Do not reintroduce the speed line.
6. **Plain English:** no dangling "it" / "those cases" / "that pipeline" without a referent, no triples, no label lead-ins ("What FitXpress offers:"), no "from the … side of [company]" (reads as if Katerina works there), no presuming what the reader knows ("you will know", "you will have seen"), formal register (no "Fancy").
7. **Keep:** exactly one compliance sentence per pair as now, hooks, account facts, the 3.5% wording ("approximately 3.5% mean absolute error under evaluated conditions" + "not a scale reading" in one sentence, said once, without "error" twice), the call line.
8. **Metadata:** update each changed person's `Proof point` line in `## Context used` to the facts the pair now carries, and correct `_summary-royal-london.md` (lane counts that add up, compliance split, no stale notes).
9. Re-read every changed message in full in the batch file. Run split-messages until exit 0, then stop.

## Per person


### Amy Higgs · amy-higgs-a1960563 · Royal London · referral
- Triples: amy-higgs-a1960563: "journey, rules and systems"
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: david-waters-05719b114, james-sims-846a9251 ("Flags can be seen in a shadow evaluation without any effect on cases."), nicky-le-roux-7b8b758, rachel-l-2387142a, kaj-makaswaran-64a176188, amy-higgs-a1960563

### Myrto (Myrsini) A. · malexandratou · Royal London · referral
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 112,100: martin-boniface-jones-371173112, james-ayland-6181bab5, damian-mapplebeck-99103818, malexandratou, richard-stadon-64b7029
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315

### Fi Wynn · fi-wynn-72936a4 · Royal London · proposition
- Presuming what the reader knows or thinks:: fi-wynn-72936a4: "Advisers will want to see the step for themselves"
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama
- Other shared lines inside a company:: Same ~20-word M1 run: carrie-johnson-81744515 and fi-wynn-72936a4 ("calculates BMI from the declared height and flags a gap with the estimated weight only above a threshold Royal London sets")

### Carrie Johnson · carrie-johnson-81744515 · Royal London · proposition
- Presuming what the reader knows or thinks:: carrie-johnson-81744515: "The number to watch is…", the same move as the previous QC's "Completion is the measure that matters"
- Other shared lines inside a company:: Same ~20-word M1 run: carrie-johnson-81744515 and fi-wynn-72936a4 ("calculates BMI from the declared height and flags a gap with the estimated weight only above a threshold Royal London sets")

### Ceri Davies · ceri-davies-11b175165 · Royal London · underwriting
- Fixed lines kept as stranded sentences with no job, since M1 already carries "2 photos". Round 2 removed the labels, but the sentences now sit as non sequiturs:: 112,100: ceri-davies-11b175165, daniel-musty-23a73716, alana-paterson-barker-fia-cera-5a759315, tim-knaust-1b852a55, adrianhhill, steve-smith-17111a95, james-hetherington-461ba352

### Dominic Pagan · dominic-pagan-4077583 · Royal London · underwriting
- Shared central question or argument at one company: Royal London: craig-paterson-970183a and dominic-pagan-4077583 both ask where "a second source of build evidence" would help or touch first.

### Robert Arbuckle · robert-arbuckle-b4aa3669 · Royal London · underwriting
- Fixed lines kept as stranded sentences with no job, since M1 already carries "2 photos". Round 2 removed the labels, but the sentences now sit as non sequiturs:: 100+: robert-arbuckle-b4aa3669, jane-lyle-a6a2b5182, réka-halász-9a72b585, gareth-alan-williams-7709b658, simon-evans-9296844b, andrew-doran-7a154617, jane-tarbuck-11487341

### William Stratton · william-stratton-8ab764104 · Royal London · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 100+: hai-luc-67306367, sdavis2, scott-wallace-b608b49b, william-stratton-8ab764104

### Damian Mapplebeck · damian-mapplebeck-99103818 · Royal London · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 112,100: martin-boniface-jones-371173112, james-ayland-6181bab5, damian-mapplebeck-99103818, malexandratou, richard-stadon-64b7029

### Jane Lyle · jane-lyle-a6a2b5182 · Royal London · underwriting
- Fixed lines kept as stranded sentences with no job, since M1 already carries "2 photos". Round 2 removed the labels, but the sentences now sit as non sequiturs:: 100+: robert-arbuckle-b4aa3669, jane-lyle-a6a2b5182, réka-halász-9a72b585, gareth-alan-williams-7709b658, simon-evans-9296844b, andrew-doran-7a154617, jane-tarbuck-11487341

### Craig Paterson · craig-paterson-970183a · Royal London · underwriting
- Lane-note or rule text still in the body: "The flag is a referral trigger…", verbatim: craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a, pearsben. Round 2's rule 4 named this text. It survived because none of these five was on a round-2 per-person list.
- Shared central question or argument at one company: Royal London: craig-paterson-970183a and dominic-pagan-4077583 both ask where "a second source of build evidence" would help or touch first.

### Seb Bowden · sebbowden · Royal London · underwriting
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413

### Caitlin Stronach · caitlin-stronach · Royal London · proposition
- Wording errors on approved facts:: caitlin-stronach M2: "112,100 scans … show it runs at volume" adds a claim to the fixed line, which round 2's rule 3 bans.

### James Blaney · james-blaney-85456b60 · Royal London · underwriting
- **Voice slip that reads as if Katerina works there** (the same construction the previous QC flagged for two others): james-blaney-85456b60 ("from the quality assurance side of Royal London underwriting"), hannah-spiro-27b12b106 ("from the innovation engagement desk at Aviva"), kaj-makaswaran-64a176188 ("from the underwriting services side at iPipeline").
- `proof:` lines are stale in about 35 entries. They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:: 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413
