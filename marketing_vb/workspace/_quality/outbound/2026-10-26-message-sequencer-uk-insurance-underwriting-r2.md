---
qc_date: 2026-10-26
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/messages/_batch-{aviva,legal-general,royal-london,mixed-1,mixed-2,mixed-3,mixed-4}.md
track: outbound
artifact_type: messages
total_score: 15/20
status: good
coordinator_review: pending
---

# QC Report — message-sequencer — 2026-10-26 (after fix rounds 1 and 2)

**Artifact:** the seven `_batch-*.md` files (176 people, 352 messages) and `_check.json` (0 hard failures).
**Total: 15/20 — good.** Up from 12/20. The big problems are fixed: compliance policy, the claim errors, regulator mentions and same-company closers. What is left is a long tail of line edits, about 60 entries. No regeneration is needed. One more targeted pass would fix it.

I scored against `card-messages.md`, the `_profiles-*.md` files, the `_fix-r1` rules, the `_fix-r2` lists and the coordinator's compliance policy. Limits, signature, bans, detector and completeness come from the gate and I took them as fact.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## Issues from the previous QC: status

- **Fixed.**
  - Compliance: every one of the 176 pairs has exactly one compliance sentence (176 matches, no pair has both). It follows the policy: boundary sentence in referral, partnership and medical; GDPR line in technical-integration. tariq-surty-8911101 now has the GDPR line.
  - Claim errors: karl-pickering-1918555 ("35 years"), william-stratton-8ab764104, leeellisone, paul-yarham-945164a0, daryl-warren-a773a64a, saitejokiran, riccardorossilbs, helena-ashton-mbcs-4775788.
  - Wording: kylie-irwin-385398154 "plus" and joel-manstoff "X, not Y".
  - Regulator mentions: samuelchivers (SMF24) and dave-evans-bb20a920 (ICO).
  - Former employers: martin-boniface-jones-371173112 and justin-farrow-226782108.
  - Grammar: denise-bates-06945338, sarah-barrell-133690131, anilgirdhari, sally-james-75186623, arslanhannani and "wherever the journey wants it".
  - Same-company closers at VitalityLife and Pacific Life Re, and the Swiss Re and Munich Re 3.5% M2 openers.
  - M1s now name the company for simon-evans-9296844b, alana-paterson-barker-fia-cera-5a759315, andrew-graham-2398a8ba and tim-knaust-1b852a55.
  - The Royal London and Exeter product-sentence clusters.
  - 80+ no longer opens any M2.
  - Every M1 names FitXpress.
  - Most earlier thin M2s now carry a value line: adrian-stevenson, matt-bone-4b127a4a, lloyd-williams62, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, richard-stadon-64b7029, hannah-cook-73585829, pete-martin-5b401069, anilgirdhari.
- **Not fixed.**
  - david-waters-05719b114 and tsmithfia still ask the card's question "Has any client (insurer) asked you about remote build evidence?".
  - danny-essam-43242013's M1 still does not name iPipeline.

## What was wrong (specific)

### A. Adherence — 4/5
- **Card question targets survive with only the verb inflection or word order changed** (23 people). This gets past round 1's five-word-run check without meeting its intent, which was "in your own words, built from this person's title":
  - remote build evidence: david-waters-05719b114, tsmithfia, natalie-kelly-447331a, hannah-cook-73585829
  - "SDK step enter the e-application": steve-lister-87b0671, tariq-surty-8911101, karl-pickering-1918555
  - "reach the underwriting workbench": jon-oneal, james-norton-591741b2
  - "review a new data processor (for the new-business journey)": rebecca-mcgeoch-186807134, johnunderwood2, spiterimichael, deanscotson
  - "build guidance treat declared and measured weight": gill-salton-414848180, tom-green-240a9222, bethan-shepherd-12a39763
  - "new evidence step added to the journey": danny-essam-43242013, kylie-irwin-385398154
  - "test a new remote evidence source with clients": lynn-baillie-b468427
  - "sit in the build section of the rules you support": andrea-gregory-76144635
  - the card's list of journey points (adviser-keyed, client declaration, direct): scott-reid-950a3410, gary-beyer-37995610 (all three points), pippa-barber-nee-keefe-487b64b6
- **Lane-note or rule text still in the body** (14 people):
  - "The flag is a referral trigger…", verbatim: craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a, pearsben. Round 2's rule 4 named this text. It survived because none of these five was on a round-2 per-person list.
  - "gaps large enough to cross a build band": john-redmond-884597a, brian-kemp-0467b898. brian-kemp also has the card rule "adds evidence to cases that get no screening".
  - Medical lane note "on gaps that would change a build rating": tom-green-240a9222, sue-kissane-859216121.
  - Card angle "with the [company's] rules and underwriters deciding": benhowe, teamsandell.
  - Reinsurance M2 value "a design the team could run with one client": claire-nolan-01708830, tsmithfia.
  - Partnership target and M2 value pasted: andrew-doran-7a154617 ("one integration several insurers could switch on" and "API and web and mobile SDKs, … one timestamped record per applicant returned to the platform"), danny-essam-43242013 (the same in both messages).
- **Company not named in M1** (card and round 1 rule 8): sandi-sohal-2853aa13 (Pacific Life Re), danny-essam-43242013 (iPipeline, carried over).
- **Shared central question or argument at one company** (card: no shared central question; one topic serves at most a fifth of a company):
  - Royal London: craig-paterson-970183a and dominic-pagan-4077583 both ask where "a second source of build evidence" would help or touch first.
  - VitalityLife: gareth-alan-williams-7709b658 and stuart-jackson-bb8a035b both ask adviser-keyed vs client.
  - Scottish Widows: three of ten ask how a new input or step is tested before it goes live: laura-vaughan-b7ba132b2, kerriecross, scott-innes-98b84830.
  - UnderwriteMe: andrew-doran-7a154617 and saitejokiran share the "one integration, several insurers" argument.
- Persona drift, low: beccacooke's hook is platform product work, but her question is about adviser feedback.

### B. Factual accuracy — 4/5
- Every number is from the approved list. All 3.5% uses are in M2, in the allowed lanes, with "not a scale reading". There is one speed sentence per company at most. No client, price or trial term is named. I spot-checked the Never lines (AIG, Iress, merger and Wiltshire, colleagues' appointments, former employers that are accounts here, Healthcheck, platform names) and all hold. The outbound compliance override is met.
- Wording errors on approved facts:
  - victoria-francis-09949480 M2: "the evaluation measures it. It returns the record, under 45 seconds…" ties the speed claim to the evaluation.
  - caitlin-stronach M2: "112,100 scans … show it runs at volume" adds a claim to the fixed line, which round 2's rule 3 bans.
- Product mechanics described wrongly:
  - tariq-surty-8911101 M1: "2 photos and a Smart Scales estimate go in". The estimate is an output.
  - anilgirdhari M1: "FitXpress would supply 2 photos".
  - brian-kemp-0467b898 M1: "takes 2 photos and a Smart Scales estimate".
- daryl-warren-a773a64a M2: the evaluation would show "how many of those would change a loading". The card's evaluation counts flags and agreement only.
- Sourcing: not applicable (outbound).

### C. Brand & tone — 2/3
- **Contorted sentences from the fix rounds:**
  - 3.5% reframes: drdeborahasmith and denise-bates-06945338 ("the stated error is approximately 3.5% mean absolute error", which says error twice).
  - "FitXpress is/would be 2 photos", the pattern the coordinator flagged in four other messages: pippa-barber-nee-keefe-487b64b6, jack-southcott-30959929.
  - Speed sentence opening on an unclear "It": louise-cowan-692b9b123 (opens M2 with "It returns a structured record… structured results"), gary-beyer-37995610, steve-smith-85b45976.
  - Dangling references:
    - justin-farrow-226782108: "On those cases", with no cases named
    - jenni-phillips-98892a24: "a candidate for that pipeline", with no pipeline named
    - lloyd-williams62: "one timestamped record back, flagged where…"
    - helen-croft-underwriting: "from 2 photos and with one timestamped record"
    - anilgirdhari M2: "would show acceptance how often…"
    - riccardorossilbs: "One structured record results."
  - Other awkward lines:
    - hannah-spiro-27b12b106: "For the judging, whoever … is who to ask", and "the page below" sits after the calendar link
    - scott-innes-98b84830: "An evaluation can hold the whole record, BMI … included, away from live cases"
    - teamsandell: "is the lens an application change gets judged through"
  - Dangling modifiers: tom-green-240a9222 ("With medical underwriting management in your background, declared weight looks different…"), samuel-njoroge-ba-hons-dipcii-dldu-amus-9b571672 ("Run in shadow, the record allows you…").
  - The question repeats the hook: manjudevinatarajan, lucy-luscombe-837866b2.
- **Voice slip that reads as if Katerina works there** (the same construction the previous QC flagged for two others): james-blaney-85456b60 ("from the quality assurance side of Royal London underwriting"), hannah-spiro-27b12b106 ("from the innovation engagement desk at Aviva"), kaj-makaswaran-64a176188 ("from the underwriting services side at iPipeline").
- **Presuming what the reader knows or thinks:**
  - sue-kissane-859216121: "you will know…"
  - lara-harkins-27835b21a: "you will have seen…"
  - fi-wynn-72936a4: "Advisers will want to see the step for themselves"
  - carrie-johnson-81744515: "The number to watch is…", the same move as the previous QC's "Completion is the measure that matters"
  - benhowe: "usually runs through the COO"
- **Triples** (card bans them):
  - amy-higgs-a1960563: "journey, rules and systems"
  - sally-james-75186623: "one set of cases, a few candidate thresholds, and a count"
  - tim-knaust-1b852a55: "one client, results kept out of decisions, flag counts"
  - réka-halász-9a72b585: "2 photos per applicant, outputs kept out of decisions and flag counts"
  - hai-luc-67306367: "structured, timestamped, one per application"
- **Label lead-ins** (the pattern the coordinator removed in round 2): kerriecross ("The proposal from FitXpress:"), scott-innes-98b84830 ("What FitXpress offers:"), ricky-dgama ("A candidate for your pipeline:").
- Register: pete-martin-5b401069 "Fancy a conversation?" is too casual for the formal CEO tone the card asks for.

### D. Format & structure — 2/3
- **Summaries were not regenerated after the fix rounds, and now contradict the artifact:**
  - `_summary-mixed-2.md` says the compliance line "sits only in the three technical-integration pairs". Its lanes still sum to 37 for 35 people.
  - `_summary-mixed-3.md` says referral people have "boundary sentence used instead in most", and lists samuelchivers as an "SMF24 hook". Its lanes still sum to 39 for 35.
  - `_summary-legal-general.md` still says underwriting 8, and still mentions a repeated 3.5% sentence for David, Jenni and Andrew that is no longer in their messages.
- **`proof:` lines are stale in about 35 entries.** They list facts the pair no longer carries, which misleads anyone auditing the facts. Examples:
  - 3.5%: david-banks-9b750391, jenni-phillips-98892a24, andrew-greatbanks-9712b03b
  - speed: pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, gary-m-3b7b913b, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, kathrynconniff, rachel-l-2387142a, fi-wynn-72936a4, amy-higgs-a1960563, andrew-newton-a1bb7115b, kaj-makaswaran-64a176188, ricky-dgama
  - 80+: sara-denyer-b81a2a92, john-redmond-884597a, brian-kemp-0467b898, nicky-mcrae-a4a3b5206, sebbowden, james-blaney-85456b60, lorna-miller-714608aa, stuart-jackson-bb8a035b, fareeha-brownless-nee-hasani-84b7b413
  - 112,100: martin-boniface-jones-371173112, james-ayland-6181bab5, damian-mapplebeck-99103818, malexandratou, richard-stadon-64b7029
  - 100+: hai-luc-67306367, sdavis2, scott-wallace-b608b49b, william-stratton-8ab764104
- The hard rule "no `product:` frontmatter, so D ≤ 1" is not applied. This is the known `split-messages` template gap, a system issue, as in the previous QC.

### E. Output quality — 3/4
- **Strong:**
  - Compliance is clean and balanced inside each company. At Aviva, for example, 11 pairs carry the GDPR line and 10 the boundary sentence.
  - Most company facts are used well, and every previously praised line kept its strength. Some M2s, such as david-piggin's, got thinner (see below).
  - Good new lines:
    - fareeha-brownless-nee-hasani-84b7b413: question on which point to protect from an added step
    - jamie-welch-12b73b62: "the case file holds one number from the applicant"
    - richard-stadon-64b7029: "A worked record is easier to judge than a description"
    - hannah-cook-73585829: M2 continues her question
    - vicki-livingstone-259a7098: the one-page proposition question
    - stuart-jackson-bb8a035b and ricky-dgama: M2s that answer their own questions
- **Lost substance after round 2 deleted speed sentences.** M2 is now one generic sentence, or opens on something never introduced:
  - david-waters-05719b114, james-sims-846a9251 ("Flags can be seen in a shadow evaluation without any effect on cases."), nicky-le-roux-7b8b758, rachel-l-2387142a, kaj-makaswaran-64a176188, amy-higgs-a1960563
  - andrew-newton-a1bb7115b (opens on "Shadow means…")
  - kathrynconniff (only the lane note is left)
  - Thin for other reasons: sharon-a-powell-2a919aab, david-piggin-a6039a27, jack-southcott-30959929, anna-graham-fia, michael-williams-0901a823, malexandratou, alana-paterson-barker-fia-cera-5a759315
  - beccacooke's M2 does not continue her question.
- **Fixed lines kept as stranded sentences** with no job, since M1 already carries "2 photos". Round 2 removed the labels, but the sentences now sit as non sequiturs:
  - 112,100: ceri-davies-11b175165, daniel-musty-23a73716, alana-paterson-barker-fia-cera-5a759315, tim-knaust-1b852a55, adrianhhill, steve-smith-17111a95, james-hetherington-461ba352
  - 100+: robert-arbuckle-b4aa3669, jane-lyle-a6a2b5182, réka-halász-9a72b585, gareth-alan-williams-7709b658, simon-evans-9296844b, andrew-doran-7a154617, jane-tarbuck-11487341
  - Number bolted on: catherine-bowen-walker-llm-cipp-e-63050134 ("and the step needs 2 photos, front and side"), because her M1 has the word form "two photos".
- **Shared skeletons inside a company, not raised in the previous QC.** Every M1 opener uses the frame "[As title / -ing role] at [Company], you [decide/know/see/weigh/set]…":
  - Munich Re, all 6: adrian-stevenson, matt-bone-4b127a4a, sridharanmadhusudhanan, lloyd-williams62, jonathan-carnell-26526b205, james-norton-591741b2
  - RGA UK, all 6: mike-evans-9760a310a, anna-graham-fia, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, deanscotson
  - LV=, "…at LV= means you…", 4 of 5: lucy-luscombe-837866b2, gareth-hurst-b2053a148, rachel-haig-993536223, karl-pickering-1918555
  - The Exeter, 5 of 6: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, suzy-esson-996a5875, lara-harkins-27835b21a
- **Other shared lines inside a company:**
  - Same M2 value line, from the proposition lane note: louise-cowan-692b9b123 and beccacooke ("…insurer's systems only, and completion is measured in the evaluation")
  - Same M2 skeleton: james-hetherington-461ba352 and riccardorossilbs ("The step could be offered / would be available through web and mobile SDKs…"); john-redmond-884597a and brian-kemp-0467b898
  - Same ~20-word M1 run: carrie-johnson-81744515 and fi-wynn-72936a4 ("calculates BMI from the declared height and flags a gap with the estimated weight only above a threshold Royal London sets")
  - VitalityLife closers that differ only trivially: nicky-le-roux-7b8b758 "Could we speak?" and james-ayland-6181bab5 "Could we speak about it?"; andrew-smith-51224b38 "Shall we speak?" and fareeha-brownless-nee-hasani-84b7b413 "Shall we talk?"
- **Campaign-wide templates** (allowed across companies, worth knowing): the pricing question appears near-identically for daryl-warren-a773a64a, hai-luc-67306367, paul-yarham-945164a0, denise-bates-06945338 and lucy-luscombe-837866b2. The IP vs life and CI question is near-identical for paul-young-708558b0 and steve-smith-17111a95.

## Top 3 issues (priority for improver)

1. **Card text as copy is still the biggest gap.**
   - 23 M1 questions are card targets with the verb inflected or the word order swapped (under A).
   - 14 bodies carry lane-note text. "The flag is a referral trigger" appears verbatim in craig-paterson-970183a, kathrynconniff, gareth-hurst-b2053a148, mike-evans-9760a310a and pearsben.
   - The five-word-run check is easy to beat this way. A lemmatised or word-order-insensitive check would catch it.
2. **Contorted sentences and thin M2s from the fix rounds** (under C and E):
   - drdeborahasmith and denise-bates-06945338 ("error is … error")
   - pippa-barber-nee-keefe-487b64b6 and jack-southcott-30959929 ("FitXpress is 2 photos")
   - victoria-francis-09949480 and louise-cowan-692b9b123 (speed sentence on "It")
   - james-blaney-85456b60, hannah-spiro-27b12b106 and kaj-makaswaran-64a176188 (voice slip)
   - Eight M2s emptied when the speed sentence was deleted: david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, rachel-l-2387142a, kaj-makaswaran-64a176188, amy-higgs-a1960563, andrew-newton-a1bb7115b, kathrynconniff.
3. **Same-company sameness the gate does not count:**
   - The M1 opener frame at Munich Re (6/6), RGA UK (6/6), The Exeter (5/6) and LV= (4/5)
   - 15 stranded 112,100 or 100+ sentences
   - The four shared central questions under A
   - Missing company names: sandi-sohal-2853aa13, danny-essam-43242013

## System notes (not scored against the agent)
- The fix rounds did not regenerate the `_summary-*.md` files or the `proof:` lines. A fix round should end by rerunning both, or the summaries should come from the script.
- Round 2's rule 4 only reached "the listed people". Five people with the verbatim referral-trigger text were on no per-person list. The gate's "card wording as copy" note already counts `«flag is a referral trigger…»` ×5, so that list could be generated from the note.
- `notify.py` was not run because this QC session has no Bash. The coordinator should send: `QC: message-sequencer → 15/20 (good). Top issue: card text as copy, with 23 near-verbatim card questions and "The flag is a referral trigger" in 5 M2s. File: workspace/_quality/outbound/2026-10-26-message-sequencer-uk-insurance-underwriting-r2.md`

## Coordinator review

agreement: ✅ agree
top_issue: Card question targets survived as paraphrases (verb or word order changed) past my five-word check; round 3 asks for questions built from the person's own title, plus the opener frames at Munich Re, RGA UK, LV= and The Exeter.

Coordinator notes (2026-10-26): round 3 built by script from this report (`_fix-r3-<batch>.md`, 123 people); praise and the allowed cross-company templates were excluded. Vadim paused the list widening (WEAK review, innovation/transformation and data/AI pools) until his command and asked to finish the 176 and commit.
