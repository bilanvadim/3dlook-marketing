---
qc_date: 2026-10-26
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/messages/
track: outbound
artifact_type: messages
total_score: 12/20
status: marginal
coordinator_review: pending
---

# QC Report — message-sequencer — 2026-10-26

**Artifact:** `workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/messages/`. I read all seven batch files (aviva 21, legal-general 19, royal-london 18, mixed-1 28, mixed-2 35, mixed-3 35, mixed-4 20 = 176 people, 352 messages), the three named per-person files, `_check.json` and the seven summaries. Grep checks ran across every per-person file.
**Total: 12/20 — marginal.** Run one targeted fix round. Nothing needs regenerating.

I scored against `card-messages.md`, the `_profiles-*.md` files and `.claude/agents/outbound/message-sequencer.md`. Limits, signature, bans, detector and completeness come from the gate and I took them as fact.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- **Compliance line (prompt rule 7: required for insurance ICP, exactly one per pair).** 74 of 176 pairs have neither the GDPR line nor the boundary sentence. The boundary sentence is allowed in any lane. The batches followed opposite policies: mixed-1 put a compliance line in 28/28 pairs, while legal-general has one in 2/19.
  - legal-general (17): david-banks-9b750391, pippa-barber-nee-keefe-487b64b6, nicki-plews-b037aa2b, sara-denyer-b81a2a92, jenni-phillips-98892a24, john-redmond-884597a, hai-luc-67306367, tariq-surty-8911101, jennyreeve, gary-m-3b7b913b, sdavis2, crissaunders, brian-kemp-0467b898, scott-wallace-b608b49b, nicky-mcrae-a4a3b5206, bethan-shepherd-12a39763, andrew-greatbanks-9712b03b
  - mixed-2 (31): every pair except dave-evans-bb20a920, will-miller-78139133, rebecca-mcgeoch-186807134, drdeborahasmith
  - aviva (9, all referral): marina-belezina-2451b0, arslanhannani, manjudevinatarajan, joel-manstoff, amanhayer, hannah-spiro-27b12b106, paul-welsh-a27b7a61, harriet-granville-jones-innovation, suzanne-lawson-2368623
  - royal-london (7): craig-paterson-970183a, dominic-pagan-4077583, robin-goodwin-039aa5271, fi-wynn-72936a4, leeellisone, goodwinjoshua, malexandratou
  - mixed-3 (3): ann-marie-o-dea-72104a24, michael-williams-0901a823, elizabeth-cook-2019
  - mixed-4 (7): alex-yates-78568889, lynn-baillie-b468427, tsmithfia, helen-croft-underwriting, ricky-dgama, danny-essam-43242013, kaj-makaswaran-64a176188
  - tariq-surty-8911101 is in the `technical-integration` lane, and the card's note for that lane puts the UK compliance line in M2. It is missing.
- **Card question targets pasted as M1 questions.** The card says lane notes "never copy", and prompt rule 11 says the same. 32 people got a question target verbatim:
  - "At which build band edges…" (11): alex-yates-78568889, adrianhhill, sue-kissane-859216121, sara-denyer-b81a2a92, szymon-marszalek, james-whitty-05a1545a, david-piggin-a6039a27, ceri-davies-11b175165, nikolai-harrowing-5246b353, mike-evans-9760a310a, eric-walker-4471a7b2
  - "…on cases that never see a nurse screening?" (8): sabrina-lane-406a0b65, craig-paterson-970183a, james-sims-846a9251, ed-lyon-803766210, richard-stadon-64b7029, michael-jackson-2417835b, daniel-musty-23a73716, andrew-smith-51224b38
  - "What would the … team need to see in a shadow evaluation before any output reached a case?" (6): ryan-parsons-15497b81, michelle-cross-88958422, nicky-le-roux-7b8b758, kerriecross, jenni-phillips-98892a24, andrew-newton-a1bb7115b
  - "Has any client asked about remote build evidence?" (4): adrian-stevenson, david-waters-05719b114, tsmithfia, anna-graham-fia
  - "test a new remote evidence source" (3): mala-thurston-22a0b499, claire-nolan-01708830, sridharanmadhusudhanan
  - Lane-note or rule text pasted into the body:
    - drtarungupta M2: "Its defensible use is a referral threshold set well above that…"
    - lara-harkins-27835b21a M2: "never a correction of declared weight"
    - "keeps its current route for anyone who does not scan": alana-paterson-barker-fia-cera-5a759315, michael-williams-0901a823, fareeha-brownless-nee-hasani-84b7b413
    - the account-fact instruction "with UK protection as the example" turned into the question: emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345
- **Same-company rules that were left unfixed.** The card says no two people at one company share an M2 opener or a closer. `_summary-mixed-1.md` says "Not fixed further".
  - VitalityLife closers:
    - "Would a call suit?": paul-yarham-945164a0, beccacooke, james-ayland-6181bab5
    - "Shall we talk?": gareth-alan-williams-7709b658, fareeha-brownless-nee-hasani-84b7b413, simon-evans-9296844b
    - "Open to a call?": lorna-miller-714608aa, kathrynconniff, rachel-l-2387142a
  - Pacific Life Re closer "Worth a call to look at it?": killian-farrelly-96422a60, david-waters-05719b114
  - M2 opener "Smart Scales has approximately 3.5%…":
    - Swiss Re: drdeborahasmith, andrew-graham-2398a8ba
    - Munich Re: jonathan-carnell-26526b205, sridharanmadhusudhanan
- **Company not named in M1** (card: "Name the company in every Message 1"): simon-evans-9296844b, alana-paterson-barker-fia-cera-5a759315, andrew-graham-2398a8ba, tim-knaust-1b852a55, danny-essam-43242013. The gate's other five "no company line" notes are short brand names and I accepted them: Vitality, Guardian, Hannover Re.
- **Different facts per person at one company** (prompt rule 3). At Aviva, 15 of 21 pairs rest on "2 photos" alone. The six that differ are sue-hendry-a8415a17 and michelle-cross-88958422 (3.5%), victoria-francis-09949480 (speed), and tom-parkinson-03190190, steve-lister-87b0671, jon-oneal (API/SDK).

### B. Factual accuracy — 2/5
- The rubric's outbound override makes a compliance mention required for insurance ICP. 74 pairs (42%) have none; the person_ids are listed under A.
- **Hard cap, B ≤ 2.** karl-pickering-1918555 M1 says "Your 35 years in regulated financial services". The number is not on the card's list, and his bio says "35+", so it is also misquoted. It is a one-line fix, but the rule is literal.
- Claims the card does not support:
  - william-stratton-8ab764104 M2: "Fields can be adjusted during an evaluation". No such capability is in the card.
  - leeellisone M2: "one record per applicant … and nothing else"
  - paul-yarham-945164a0 M2: "The applicant provides 2 photos and nothing else". The applicant also declares height.
  - daryl-warren-a773a64a M1: "The timestamped record stays with Aviva". 3DLOOK keeps outputs until they are deleted, and data handling may only use compliance.md forms.
  - saitejokiran M1: "UnderwriteMe is both a platform and a marketplace of partners". This is not in UnderwriteMe's account bullet.
  - riccardorossilbs M2: "easy to embed". This is an integration-effort claim.
  - helena-ashton-mbcs-4775788 M2: "per policy" cuts the approved form "per the insurer's policy".
- danny-essam-43242013 M1 opens "Saw the news on…" about the 2025-09-01 Advanced Underwriting rollout. That presents a 13-month-old item as news.
- Low severity: two Pacific Life Re messages name former employers that are now part of Aviva, an account in this campaign. martin-boniface-jones-371173112 names "Friends Life UK" and justin-farrow-226782108 names "Norwich Union Healthcare". The card's Never list did not mention either.
- **Clean:**
  - All 27 uses of the 3.5% figure are in M2, in underwriting, medical or reinsurance lanes, with "not a scale reading" in the same sentence.
  - The speed phrase is always used whole. The 112,100 and 100+ wordings are exact.
  - No client, price, trial term or other prospect is named.
  - Every Never line holds: no AIG Life, merger, Alula or Iress; Magnum and Life Guide appear only for Swiss Re; Decision and Protection Platform only for UnderwriteMe; the Dynamic Underwriting Benefit only for szymon-marszalek, kept apart from the Healthcheck.
- Sourcing: not applicable (outbound).

### C. Brand & tone — 2/3
- "plus" used as a connector, which the detector missed: kylie-irwin-385398154 M2 ("SDKs plus an API").
- Corrective "X, not Y": joel-manstoff M1 ("a mindset, not a project").
- Triple: matt-bone-4b127a4a M2 ("which cases, which candidate thresholds, and how a flag compares").
- Presumed reaction or presumptive lines:
  - harriet-granville-jones-innovation: "you will have seen many evidence tools" and "The honest answer is"
  - sridharanmadhusudhanan: "will want the evidence before the product. So here is…"
  - kylie-irwin-385398154: "suggests you weigh…"
  - mala-thurston-22a0b499: "client insurers will look to their reinsurer"
  - dave-evans-bb20a920: "shape how Swiss Re UK reviews data sharing"
  - deanscotson: "you review the data flows of any evaluation a client insurer runs"
  - will-miller-78139133: "any data … passes through you"
  - tom-green-240a9222: "you will have a view"
- Grammar and voice:
  - denise-bates-06945338: dangling modifier ("As Head of … at Swiss Re, build loadings are part of your world")
  - sarah-barrell-133690131 ("from the operations side of Holloway Friendly") and anilgirdhari ("from the acceptance side of SCOR's treaty work") read as if Katerina works there
  - sally-james-75186623: "Our FitXpress"
  - arslanhannani: "a flag above a gap Aviva sets"
  - "wherever the journey wants it": gareth-alan-williams-7709b658, stuart-jackson-bb8a035b
- Regulator references (the card says no regulator, and FCA/PRA are banned): samuelchivers ("SMF24 responsibility"), dave-evans-bb20a920 ("ICO").
- Otherwise the register fits a CEO writing to a chief underwriter: formal, short, British English, no enthusiasm words.

### D. Format & structure — 2/3
- Summary lane counts do not add up:
  - `_summary-mixed-2.md` sums to 37 for 35 people.
  - `_summary-mixed-3.md` sums to 39 for 35. The real split is underwriting 9, reinsurance 10, referral 7, proposition 5, technical-integration 3, medical 1.
  - `_summary-legal-general.md` sums to 18 for 19. Underwriting is 9, not 8.
- `_summary-mixed-2.md` and `_summary-mixed-4.md` give length as the reason the compliance line is missing. The M2s involved have room:
  - pete-martin-5b401069: 203/550
  - ricky-dgama: 243
  - steve-smith-17111a95: 260
  - scott-wallace-b608b49b: 265
  - claire-nolan-01708830: 275
  - tim-knaust-1b852a55: 290
  - alex-yates-78568889: 413, with room for the 77-character boundary sentence
- The hard rule "no `product:` frontmatter, so D ≤ 1" is **not applied**. The per-person files come from the `split-messages` template, which is a system gap (as on 10-21 and 10-23).

### E. Output quality — 3/4
- **Strong:**
  - Hooks mostly come from the profiles, and allowed company facts are used well: nick-rice-59394882 (Guardian "where does build sit on that list"), david-banks-9b750391 (L&G January rework), sue-hendry-a8415a17 (Aviva June change, no hint of replacing nurse screening), benhowe (Cirencester change without the banned word).
  - Good lines: andrew-graham-2398a8ba (Magnum), damian-mapplebeck-99103818 (engines without naming them), goodwinjoshua ("the threshold also sets referral volume"), david-piggin-a6039a27, matt-bone-4b127a4a's M1 question.
  - Referral easy outs vary well.
- **Mail-merge risk at the big accounts:**
  - Royal London product sentence repeated ("FitXpress takes two photos in the application and flags a gap between declared and estimated weight above a threshold Royal London sets"): sebbowden, malexandratou, william-stratton-8ab764104, robert-arbuckle-b4aa3669, caitlin-stronach, goodwinjoshua, james-sandell-4686b59, craig-paterson-970183a.
  - The Exeter product sentence repeated: toby-bainbridge-063483a, david-piggin-a6039a27, ed-lyon-803766210, lara-harkins-27835b21a, jack-southcott-30959929.
  - The identical GDPR paragraph is in every Pacific Life Re M2 (12) and about 17 VitalityLife M2s. The rubric's 60%-unique check is out of reach by design; I judged the free text.
- **Number-gate filler:**
  - "The scan takes 2 photos." added to M2: laura-vaughan-b7ba132b2, claire-nolan-01708830, vicki-livingstone-259a7098, tim-knaust-1b852a55, fraser-ballantine-b4204527, david-russell-10548311a.
  - "80+ … can stay unused / a rule set can ignore / can go unused": kerriecross, helen-sutherland-thomas-223335123, ryan-parsons-15497b81.
- **80+ body measurements leads the M2 value line** (card: "secondary, never the lead"): gareth-jenkins-26010578, scott-reid-950a3410, stuart-jackson-bb8a035b, steve-smith-85b45976, toby-bainbridge-063483a, gary-beyer-37995610, pippa-barber-nee-keefe-487b64b6, lyonskate81, caroline-smith-78180535.
- **M2 with no value line, or one restated lane note:**
  - anilgirdhari: only the two compliance sentences and the CTA
  - one thin value sentence: adrian-stevenson, matt-bone-4b127a4a, lloyd-williams62, james-norton-591741b2, mike-evans-9760a310a, anna-c-6b5a7226, emma-jones-99a3834b, rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345, richard-stadon-64b7029, hannah-cook-73585829, pete-martin-5b401069, steve-smith-17111a95
- **M1 never names the product** ("Two photos in the application give…"). Sample: mala-thurston-22a0b499, david-waters-05719b114, james-sims-846a9251, nicky-le-roux-7b8b758, lorna-miller-714608aa, denise-bates-06945338, natalie-kelly-447331a, fraser-ballantine-b4204527, adrian-stevenson, anna-graham-fia.
- **The three named files:**
  - alex-yates-78568889:
    - M1 uses the allowed Protect fact and keeps LV= and The Exeter out.
    - The question is the card target, verbatim.
    - The M2 3.5% sentence is correct.
    - There is no compliance mention, although the boundary sentence fits.
  - adrian-stevenson:
    - The M1 question is verbatim.
    - The product is never named.
    - M2 is one sentence that restates the lane note, then the GDPR line, then "Open slot:".
  - carrie-johnson-81744515:
    - Good fit for a protection P&L owner, with a journey question.
    - The hook stretches the occupation-class refresh into "how much a case's terms rest on what is declared".
    - "Completion is the measure that matters" is presumptive.
    - 525/550.

## Top 3 issues (priority for improver)

1. **Compliance mention missing in 74/176 pairs, and the batches split on policy.** Add the boundary sentence in referral and partnership lanes, and the GDPR line where the lane allows it. tariq-surty-8911101 must get the GDPR line. The person_ids are under A.
2. **Card text used as copy.** 32 M1 questions are the lane question targets verbatim (under A). Lane or rule sentences also sit in M2 for drtarungupta, lara-harkins-27835b21a, alana-paterson-barker-fia-cera-5a759315, michael-williams-0901a823, fareeha-brownless-nee-hasani-84b7b413, emma-jones-99a3834b and rebecca-abayakoon-certified-falu-bcom-snrassoc-anziif-669b345.
3. **Same-company rules the gate pointed at but the writer left.**
   - VitalityLife (9) and Pacific Life Re (2) shared closers.
   - Swiss Re and Munich Re shared "Smart Scales has…" M2 openers.
   - Five M1s without the company name.
   - Royal London and The Exeter product-sentence clusters.
   - The claim and number lines: karl-pickering-1918555, william-stratton-8ab764104, leeellisone, daryl-warren-a773a64a, saitejokiran, paul-yarham-945164a0, kylie-irwin-385398154 "plus".

## System notes (not scored against the agent)
- The card says the compliance line is "at most one per pair", while `message-sequencer.md` rule 7 and the rubric make it required. Proposed card wording: "exactly one per pair: the GDPR line in the lanes that allow it, the boundary sentence in referral and partnership".
- `detect-ai-tells.py` missed "SDKs plus an API".
- The gate's "card wording as copy" is a soft note, so the 32 verbatim questions passed.
- Half of the "no company line" notes are false positives on short brand names.
- `notify.py` was not run because this QC session has no Bash. The coordinator should send the notification.

## Coordinator review

agreement: ✅ agree
top_issue: Compliance policy split across batches because the card says "at most one per pair" while message-sequencer rule 7 says exactly one; fix round 1 assigns one form per person by script (referral/partnership/medical → boundary sentence, technical-integration → GDPR line, the rest balanced so neither form passes two thirds of a company).

Coordinator notes (2026-10-26):
- Agreed on all three top issues. My own pre-QC scan had found the GDPR line in two referral pairs (pearsben, sarah-barrell-133690131) and the number-gate filler; both are in round 1.
- Not taken: the hook lead-ins («Noticed your», «Quick note», «Caught my eye») are allowed by Vadim's Message 1 template (2026-07-21), so they stay.
- The card-question check in round 1 uses 5-word runs from the card's Question targets, minus generic UK phrases ("at the point of sale"): 48 people, not QC's 32.
- System fix to propose to Vadim: card rule "Compliance line. At most one per pair" → "exactly one per pair: the GDPR line or the boundary sentence", matching rule 7 and the rubric.
