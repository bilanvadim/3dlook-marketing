# Fix round 3 — aviva (2026-10-26)

QC after round 2: 15/20 (report workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md). This is the last round before Vadim. Each item is a one-line or two-line edit. Same rules for all seven batches. Edit `messages/_batch-aviva.md` with Edit per message.

## Rules for this round

1. **M1 question from the card's targets** (even with the verb or word order changed) is rewritten from this person's own title and work, in your own words, about something they own. It must not share its central question with a colleague at the same company.
2. **Card lane text in copy** ("The flag is a referral trigger…", "gaps large enough to cross a build band", "on gaps that would change a build rating", "with the society's rules and underwriters deciding", "a design the team could run with one client", "one integration several insurers could switch on") is replaced by a plain value line for that person.
3. **M1 opener frame.** Where the list says the opener uses the "[title] at [company], you decide/know/see…" frame, open differently: on a fact from the person's path, on the company's own fact, or on the subject of their question. Hook phrases from the template are allowed. At most two people per company keep the same frame.
4. **Stranded fixed lines** ("112,100 scans…", "3DLOOK has worked with 100+ clients.") with no job in that M2 are deleted. If the pair then needs a number, write "2 photos" (digit) in the M1 product sentence.
5. **Thin M2:** one or two sentences that continue this person's own M1 question with something new for them, before the compliance sentence. Do not reintroduce the speed line.
6. **Plain English:** no dangling "it" / "those cases" / "that pipeline" without a referent, no triples, no label lead-ins ("What FitXpress offers:"), no "from the … side of [company]" (reads as if Katerina works there), no presuming what the reader knows ("you will know", "you will have seen"), formal register (no "Fancy").
7. **Keep:** exactly one compliance sentence per pair as now, hooks, account facts, the 3.5% wording ("approximately 3.5% mean absolute error under evaluated conditions" + "not a scale reading" in one sentence, said once, without "error" twice), the call line.
8. **Metadata:** update each changed person's `Proof point` line in `## Context used` to the facts the pair now carries, and correct `_summary-aviva.md` (lane counts that add up, compliance split, no stale notes).
9. Re-read every changed message in full in the batch file. Run split-messages until exit 0, then stop.

## Per person


### Steve Lister · steve-lister-87b0671 · Aviva · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "SDK step enter the e-application": steve-lister-87b0671, tariq-surty-8911101, karl-pickering-1918555

### Manju Devi · manjudevinatarajan · Aviva · referral
- Contorted sentences from the fix rounds:: The question repeats the hook: manjudevinatarajan, lucy-luscombe-837866b2.

### Jon O'Neal · jon-oneal · Aviva · technical-integration
- Card question targets survive with only the verb inflection or word order changed: "reach the underwriting workbench": jon-oneal, james-norton-591741b2

### Victoria Francis · victoria-francis-09949480 · Aviva · proposition
- Wording errors on approved facts:: victoria-francis-09949480 M2: "the evaluation measures it. It returns the record, under 45 seconds…" ties the speed claim to the evaluation.

### Hannah Spiro · hannah-spiro-27b12b106 · Aviva · referral
- Contorted sentences from the fix rounds: › Other awkward lines: hannah-spiro-27b12b106: "For the judging, whoever … is who to ask", and "the page below" sits after the calendar link
- **Voice slip that reads as if Katerina works there** (the same construction the previous QC flagged for two others): james-blaney-85456b60 ("from the quality assurance side of Royal London underwriting"), hannah-spiro-27b12b106 ("from the innovation engagement desk at Aviva"), kaj-makaswaran-64a176188 ("from the underwriting services side at iPipeline").

### Daryl Warren · daryl-warren-a773a64a · Aviva · proposition
- daryl-warren-a773a64a M2: the evaluation would show "how many of those would change a loading". The card's evaluation counts flags and agreement only.

### Sally James · sally-james-75186623 · Aviva · underwriting
- Triples: sally-james-75186623: "one set of cases, a few candidate thresholds, and a count"
