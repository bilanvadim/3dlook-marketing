# Fix round 3 — mixed-3 (2026-10-26)

QC after round 2: 15/20 (report workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md). This is the last round before Vadim. Each item is a one-line or two-line edit. Same rules for all seven batches. Edit `messages/_batch-mixed-3.md` with Edit per message.

## Rules for this round

1. **M1 question from the card's targets** (even with the verb or word order changed) is rewritten from this person's own title and work, in your own words, about something they own. It must not share its central question with a colleague at the same company.
2. **Card lane text in copy** ("The flag is a referral trigger…", "gaps large enough to cross a build band", "on gaps that would change a build rating", "with the society's rules and underwriters deciding", "a design the team could run with one client", "one integration several insurers could switch on") is replaced by a plain value line for that person.
3. **M1 opener frame.** Where the list says the opener uses the "[title] at [company], you decide/know/see…" frame, open differently: on a fact from the person's path, on the company's own fact, or on the subject of their question. Hook phrases from the template are allowed. At most two people per company keep the same frame.
4. **Stranded fixed lines** ("112,100 scans…", "3DLOOK has worked with 100+ clients.") with no job in that M2 are deleted. If the pair then needs a number, write "2 photos" (digit) in the M1 product sentence.
5. **Thin M2:** one or two sentences that continue this person's own M1 question with something new for them, before the compliance sentence. Do not reintroduce the speed line.
6. **Plain English:** no dangling "it" / "those cases" / "that pipeline" without a referent, no triples, no label lead-ins ("What FitXpress offers:"), no "from the … side of [company]" (reads as if Katerina works there), no presuming what the reader knows ("you will know", "you will have seen"), formal register (no "Fancy").
7. **Keep:** exactly one compliance sentence per pair as now, hooks, account facts, the 3.5% wording ("approximately 3.5% mean absolute error under evaluated conditions" + "not a scale reading" in one sentence, said once, without "error" twice), the call line.
8. **Metadata:** update each changed person's `Proof point` line in `## Context used` to the facts the pair now carries, and correct `_summary-mixed-3.md` (lane counts that add up, compliance split, no stale notes).
9. Re-read every changed message in full in the batch file. Run split-messages until exit 0, then stop.

## Per person


### Jonathan Sandell · teamsandell · Shepherds Friendly · referral
- Lane-note or rule text still in the body: Card angle "with the [company's] rules and underwriters deciding": benhowe, teamsandell.
- Contorted sentences from the fix rounds: › Other awkward lines: teamsandell: "is the lens an application change gets judged through"

### Michael Williams · michael-williams-0901a823 · Shepherds Friendly · referral
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315

### Sam Chivers · samuelchivers · Shepherds Friendly · referral
- Summaries were not regenerated after the fix rounds, and now contradict the artifact:: `_summary-mixed-3.md` says referral people have "boundary sentence used instead in most", and lists samuelchivers as an "SMF24 hook". Its lanes still sum to 39 for 35.

### Steve Smith · steve-smith-85b45976 · Shepherds Friendly · proposition
- Contorted sentences from the fix rounds:: Speed sentence opening on an unclear "It": louise-cowan-692b9b123 (opens M2 with "It returns a structured record… structured results"), gary-beyer-37995610, steve-smith-85b45976.

### Suzy Esson · suzy-esson-996a5875 · The Exeter · referral
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a

### Toby Bainbridge · toby-bainbridge-063483a · The Exeter · proposition
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a

### Jack Southcott · jack-southcott-30959929 · The Exeter · proposition
- Contorted sentences from the fix rounds:: "FitXpress is/would be 2 photos", the pattern the coordinator flagged in four other messages: pippa-barber-nee-keefe-487b64b6, jack-southcott-30959929.
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315

### David Piggin · david-piggin-a6039a27 · The Exeter · underwriting
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a

### Ed Lyon · ed-lyon-803766210 · The Exeter · underwriting
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a

### Lara Harkins · lara-harkins-27835b21a · The Exeter · underwriting
- Presuming what the reader knows or thinks:: lara-harkins-27835b21a: "you will have seen…"
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a

### Lloyd Williams · lloyd-williams62 · Munich Re UK Life Branch · reinsurance
- Contorted sentences from the fix rounds: › Dangling references: lloyd-williams62: "one timestamped record back, flagged where…"
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### Adrian Stevenson · adrian-stevenson · Munich Re UK Life Branch · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### Matt Bone · matt-bone-4b127a4a · Munich Re UK Life Branch · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### Jonathan Carnell · jonathan-carnell-26526b205 · Munich Re UK Life Branch · medical
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### James Norton · james-norton-591741b2 · Munich Re UK Life Branch · reinsurance
- Card question targets survive with only the verb inflection or word order changed: "reach the underwriting workbench": jon-oneal, james-norton-591741b2
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### Madhu Sridharan · sridharanmadhusudhanan · Munich Re UK Life Branch · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2

### Anna Currie · anna-c-6b5a7226 · RGA UK · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Emma Jones · emma-jones-99a3834b · RGA UK · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Rebecca Abayakoon · rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345 · RGA UK · reinsurance
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Mike Evans · mike-evans-9760a310a · RGA UK · reinsurance
- Lane-note or rule text still in the body: "The flag is a referral trigger…", verbatim: craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a, pearsben. Round 2's rule 4 named this text. It survived because none of these five was on a round-2 per-person list.
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Anna Graham · anna-graham-fia · RGA UK · reinsurance
- Lost substance after round 2 deleted speed sentences. M2 is now one generic sentence, or opens on something never introduced:: Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Dean Scotson · deanscotson · RGA UK · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "review a new data processor (for the new-business journey)": rebecca-mcgeoch-186807134, johnunderwood2, spiterimichael, deanscotson
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson

### Ben Howe · benhowe · Cirencester Friendly Society · referral
- Lane-note or rule text still in the body: Card angle "with the [company's] rules and underwriters deciding": benhowe, teamsandell.
- Presuming what the reader knows or thinks:: benhowe: "usually runs through the COO"

### John Underwood · johnunderwood2 · Cirencester Friendly Society · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "review a new data processor (for the new-business journey)": rebecca-mcgeoch-186807134, johnunderwood2, spiterimichael, deanscotson

### Sue Kissane · sue-kissane-859216121 · Cirencester Friendly Society · underwriting
- Lane-note or rule text still in the body: Medical lane note "on gaps that would change a build rating": tom-green-240a9222, sue-kissane-859216121.
- Presuming what the reader knows or thinks:: sue-kissane-859216121: "you will know…"

### Samuel Njoroge · samuel-njoroge-ba-hons-dipcii-dldu-amus-9b571672 · Cirencester Friendly Society · underwriting
- Contorted sentences from the fix rounds:: Dangling modifiers: tom-green-240a9222 ("With medical underwriting management in your background, declared weight looks different…"), samuel-njoroge-ba-hons-dipcii-dldu-amus-9b571672 ("Run in shadow, the record allows you…").

### Karl Pickering · karl-pickering-1918555 · LV= · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "SDK step enter the e-application": steve-lister-87b0671, tariq-surty-8911101, karl-pickering-1918555
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: LV=, "…at LV= means you…", 4 of 5: lucy-luscombe-837866b2, gareth-hurst-b2053a148, rachel-haig-993536223, karl-pickering-1918555

### Gary Beyer · gary-beyer-37995610 · LV= · proposition
- Card question targets survive with only the verb inflection or word order changed: the card's list of journey points (adviser-keyed, client declaration, direct): scott-reid-950a3410, gary-beyer-37995610 (all three points), pippa-barber-nee-keefe-487b64b6
- Contorted sentences from the fix rounds:: Speed sentence opening on an unclear "It": louise-cowan-692b9b123 (opens M2 with "It returns a structured record… structured results"), gary-beyer-37995610, steve-smith-85b45976.

### Lucy Luscombe · lucy-luscombe-837866b2 · LV= · proposition
- Contorted sentences from the fix rounds:: The question repeats the hook: manjudevinatarajan, lucy-luscombe-837866b2.
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: LV=, "…at LV= means you…", 4 of 5: lucy-luscombe-837866b2, gareth-hurst-b2053a148, rachel-haig-993536223, karl-pickering-1918555

### Gareth Hurst · gareth-hurst-b2053a148 · LV= · underwriting
- Lane-note or rule text still in the body: "The flag is a referral trigger…", verbatim: craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a, pearsben. Round 2's rule 4 named this text. It survived because none of these five was on a round-2 per-person list.
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: LV=, "…at LV= means you…", 4 of 5: lucy-luscombe-837866b2, gareth-hurst-b2053a148, rachel-haig-993536223, karl-pickering-1918555

### Rachel Haig · rachel-haig-993536223 · LV= · underwriting
- Shared skeletons inside a company, not raised in the previous QC. Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weig: LV=, "…at LV= means you…", 4 of 5: lucy-luscombe-837866b2, gareth-hurst-b2053a148, rachel-haig-993536223, karl-pickering-1918555
