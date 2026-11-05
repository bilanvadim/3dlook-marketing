---
qc_date: 2026-11-05
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/messages/_dump-r2.md (277 pairs, after fix rounds 1-2)
track: outbound
artifact_type: messages
total_score: 12/20
status: marginal
coordinator_review: pending
---

# QC Report: message-sequencer, 2026-11-05 (US insurance underwriting, after fix rounds 1-2)

**Artifact:** `messages/_dump-r2.md`, all 277 pairs read in full. Scored against `card-messages.md` (Rules, Account facts, templates) and `_fix-r1-rules.md`. Gate facts from `_check.json` (0 hard, soft only) taken as given.

**Total: 12/20, marginal.**

What the rounds fixed:
- No bare CTA labels.
- No "point me" closer family.
- No P1 easy outs. I checked all 37 P1s.
- No appointment hooks.
- Lead-in words are unique inside every company.

Research and number discipline are still clean. The score stays at 12 for three reasons:
- The fixes produced new stock forms.
- Several companies still read as a mail merge on the company-fact sentence and the M2 value line.
- The evaluation-design line most underwriting and reinsurance M2s now carry often contradicts itself.

This needs one more targeted round on the people named below, not a regeneration.

Not scored as defects:
- The template lead-ins (only repeats inside one company count).
- The mandated compliance line.
- "a Smart Scales weight estimate".
- Own products in own copy.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence, 3/5

**A1. Card question targets survive as reworded clones (fix rule 6; card: targets are "never copy").** The topic was allowed to stay, but the object and frame did too, mostly in the card's phrase "a gap between declared and estimated weight" (20 uses).

- **Build-chart edge question, 13 people, one per company** ("Where on the build chart would a gap between declared and estimated weight change a (risk) class?"):
  - gretchen-dinucci-74b33b45, matthewburrill, tim-ranfranz-falu-fmli-81559b1a, mike-link-679151134, terry-huisman-91231b48, bradgabel, anthony-perez-6083812a, eric-flender-b4b198172, warnershue, kurtis-stewart-50446643, rebecca-severson-certified-falu-flmi-ara-acs-5536552b, cathy-allocco-58672618.
  - mike-derrig-65213323 keeps "edges of the chart" and in M2 "chart edges".
  - tim-ranfranz and bradgabel are both past AHOU presidents. They get the same hook ("Noticed your time as (president of) AHOU") and nearly the same question, so they are the two readers most likely to compare.
- **Shadow-evaluation question, 10 people** ("What would a shadow evaluation have to show before any output reaches a case?"): chris-feldges-falu-flmi-mba-acs-501083a5, bryan-flynn-21866b9, laurie-borowski, cody-schiffer-falu-flmi-53b84385, stephen-lininger-392aa332, jennifer-black-b1034649, daniel-dan-buchholz-certified-falu-clu-flmi-acs-3613a216, kathleen-coughlin-38415319, thomas-ferguson-33b4521b, tony-fung-9129169. Variants: tracy-regier-72866a38, kory-petoske-15a70194.
- **Medical target "how build guidance treats a declared weight against an exam weight", near-verbatim:** sheila-macdonnell-a762b22b, christine-kor-aronski-14784125, michael-moore-a2568a26, susan-sucha-219b9016a, joel-weiner-md-facp-flmi-18b07151, marianne-cumming-9b85442b.
- **Other targets or Use lines pasted:**
  - elena-a-s-4a902718b: "questions … to a software weight estimate before a carrier's accelerated rules used it". This is the frame fix rule 6 names.
  - ronelle-moe-7a4a70280: "where no paramed happens".
  - regina-rosace-m-d-faap-dbim-33836715: M1 "defensible", M2 "may and may not be used".
  - michael-hogan-1849132a: the Zinnia Use line word for word.
  - cynthia-landry-922908a2: the Swiss Re Use line.

**A2. Fix-rule and card wording pasted as copy.** `_fix-r1-rules.md`: "never paste a phrase from this file".
- "build (evidence) gathered separately", fix rule 7's own words, 7 people: gretchen-dinucci-74b33b45, bryan-flynn-21866b9, kari-turtinen-31a178133, beverley-sloley-flmi-mba-ba112027, jacqueline-waas-05a79145, michaelhillunderwriter, rmackillop.
- The referral lane note "whoever owns underwriting rules or the new-business journey" as the easy out, 7 people: ashley-destito-a636194b, teesun, ernest-armijos-270aa9378, frances-freeman-69582136, scott-delisi-4a855b7, patrick-d-sullivan-5812b78, robert-reynolds-77626a8.
- The card rule sentence "Speed is the point": john-dieck-a2310036.
- "a threshold set well above the estimate's error", the medical lane note: brandon-may-do-dbim-ms-4288a5150, jonathan-mcallister-a91a5647, michael-k-469910295, michaelcliftlifeunderwriting.

**A3. Fix rule 8 broken.** "returns 80+ body measurements, under 45 seconds from the photos to structured results" is the form the rule forbids. Found ×4: karnatrautman, kelly-halverson-2a8a467 (opens "Completion follows effort."), andy-gordon-0b813423, ericpahlfsa.

**A4. Company not named in M1.** The card says: "Name the company in every Message 1." Missing ×9:
- kelly-halverson-2a8a467, laura-cutshall-25543627, gay-kemmis-76523410, katie-kahl-15049526, michael-celi. Each has a product name but no company.
- michaelcliftlifeunderwriting also never names FitXpress, which the fix-round scope requires.
- eric-flender-b4b198172, sgjense and mark-brann-ab79a322 have no line only that company could get. Eric's M1 could go to any reinsurer.

**A5. Fix rule 1 (easy outs) still broken.**
- **Easy out sends the owner to the owner of their own remit:**
  - seanconrad (head of data analytics): "whoever handles client analytics".
  - michaelhillunderwriter (VP Fac UW Strategy and Data Analytics): "whoever runs analytics intake".
  - nick-sontheimer-b01084178 (managing actuary, pricing): "whoever leads [pricing studies]".
  - jeffrey-nattis-35a8964 (Director of Medical Underwriting): "another team own the comparison of declared and measured weight".
  - salene-hitchcock-gear-a8207a12 (President, Individual Life): journey placement "belong to a colleague".
  - brian-pemberton-09ba289 (VP NB Underwriting): "new business underwriting for term lives with a different team".
  - daniel-dan-buchholz-…: "An analyst … could join instead".
  - james-atkins-flmi-falu-a919a564 (SMART's named contact): "who owns SMART's data feeds".
  - jacqueline-waas-05a79145: "build guidance sits with another owner".
- **Easy-out verb repeated at one company:**
  - Pacific Life: "tell me who" (ernest-armijos-270aa9378, matt-winegar-68303421) and point/pointer (teesun, tristan-fontugne-5477b89).
  - RGA: "join" and "whoever leads them" (michaelhillunderwriter, nathan-hill-24b77626, nick-sontheimer-b01084178).
  - Hannover: "welcome" ×2 (renee-mcclintic-falu-flmi-hiaa-acs-66954113, seanconrad).
  - SCOR: "a name there" ×2 (brooke-morgan-of-cincinnati, ashley-hunt-768031272).
  - Sammons: "introduction / introduced" (pat-grashel-46202a8b, christie-brammer-92b2a467).
  - Principal: "better home / better fit" ×3 (frank-mikalonis-594b3816, hermanbob, mike-sir-84b7b610).
  - Securian: "introduction" (jeffrey-noren-00a879231, brian-rock-fsa-cera-maaa-25203b142).
  - The Standard: "pointer / point me" (teague-jim-481208a, rajesh-mondkar-12a1293a).

**A6. Fix rule 5: the title read back, in new forms.**
- mindi-work-046a345: "given Emerging Solutions in your title".
- mariancoffey: "from years as a disability income regional VP".
- christine-kor-aronski-14784125: "your remote medical director role".
- pete-kaczmar-78a6816: "Your remit at Ameritas is national accounts and partners".
- lynn-brown-0b27474, vicki-garrett-54256920, ashley-destito-a636194b, seanconrad, silke-lavallee ("in your headline").
- **Campaign pattern in the Ameritas, Guardian and Lincoln batch.** All 34 M1s drop the template's light hook. About 12 replace it with "[your function] at [Company] does X", which describes the reader's own job back to them:
  - kyle-o-donnell-a7b9918, lynn-saddoris-mba-b188749, smitha-jagalur-b61b1a131, micah-pace-36b1b721, smarkw, deborah-lineberry-a6b713202, ericpahlfsa, patrick-d-sullivan-5812b78, scott-delisi-4a855b7, don-kidd-00a43852.

**A7. Fix rule 10:** justintallen and warnershue have 3-sentence first paragraphs.

**A8. Account-fact `Use:` mapping slips:**
- mike-bauer-582a2481 was due the fluidless physical. He got kurtis-stewart's "own build chart" hook.
- mark-brann-ab79a322 was due workbench evidence ordering.
- kenny-membreno-582a091a and ryanphawkins were due data handling. Kenny got the online-quote fact that bbrunick and jeffrey-einhorn also got.
- josh-heidemann-6a89a34 and cody-schiffer were due build-chart angles.

### B. Factual accuracy, 3/5

**Clean:**
- Every number is from the list. 3.5% appears only in M2 of allowed lanes, always with "not a scale reading".
- Exactly one compliance line per pair.
- No clients, competitors, pilots or trial terms.
- No prospect is named in another prospect's copy.
- Every Never line is respected. I checked former employers, sister companies, vendors and figures.
- Corebridge is absent. Laura Cutshall has no SCOR or Velogica.

**Product and data statements that are wrong or unsourced:**
- pattiarellano M2: "a second source for height and weight". The card says FitXpress "does not check height".
- keerthi-mandala M2: "keeps the data in Ladder's systems only". 3DLOOK stores records on AWS. The approved claim is that results are returned only to the carrier.
- tasha-boland-fsa-cera-4632a3109 M2: "the shift in class placement". This implies the flag moves a class.
- mark-barnum-b3041619 M2: the record on the file includes "the photos".
- allysonschrader M1: the record is "sent … when the gap crosses", but there is one record per applicant.
- deborah-lineberry-a6b713202 and emroczek: "no separate app for the applicant", which is not in the card.
- jonathan-applewhite-fsa-5b826911: "WealthProtector … keeps product design close to the application". The Use line says "without detail".
- nick-sontheimer-b01084178 M1: "pricing data at RGA, where a shadow evaluation of build evidence produces counts". This reads as if RGA runs one.
- samrat-dua: "Magnum is offered in three forms". This is a count, and the Never line covers figures of any kind. Minor.

**Underwriting logic a senior US underwriter would catch:**
- **Evaluation design that contradicts itself.** The new stock M2 line compares flags with exam-case build. The phrase appears 44 times.
  - Three cases restrict the comparison to files that by definition have no exam:
    - tristan-fontugne-5477b89: "agreement with exam-based build … limited to accelerated cases"
    - shawn-fourez-72628142: "against build from exam cases, limited to accelerated files"
    - eric-hoerr-certified-falu-flmi-071b77b1: "On accelerated client cases with no paramed … build measured on the client's exam cases"
  - The same population mismatch, worded more loosely: gretchen-dinucci-74b33b45, amy-rider-falu-flmi-ab466944, andrew-vigar-falu-flmi-74579219, warnershue, russell-kolmin, davidmchien.
  - The coherent version already exists. Scan the holdouts or exam cases and compare estimate against measured weight: danielgarant, mary-bates-491652139, helen-colberg-05a71153, andrew-langemeier-falu-flmi-b7398813a, michael-ash-dollowitch, heather-milligan-b602601a.
- terry-huisman-91231b48: "the regional build chart". Build charts are not regional.
- terri-drahn-9743a099: asks a VP to state where her fluidless chart separates preferred from standard. That is a chart value, asked for in a cold DM.
- donna-rogers-98304012: "a fluidless file where no recent physical exists". That file is outside the program the hook just described.
- gregory-soltner-do-dbim-falu-flmi-210a6632: "Who reviews a build gap on those files today". No gap exists today.
- mike-link-679151134: Quick Quote comes before the application, so a declared-vs-estimated gap cannot make a Quick Quote case "more complex".
- michaelcliftlifeunderwriting: "the figures behind [the build section] … are the declared height and weight". This conflates the chart with the applicant's entries.

### C. Brand & tone, 2/3

Gate-clean: no banned words, no dashes, no "plus", no corrective negation beyond the mandated one.

**Condescending or presumptive lines:**
- rhonda-steffel-heling-30b798a6: "If thresholds are decided above your seat".
- kelly-halverson-2a8a467: "Completion follows effort."
- christopherlintecum: "Any step added to a digital application is judged on completion."
- john-dieck-a2310036: "is where the application has to feel short".
- victoria-liu-fsa-fcia-98519a14: "where the buying experience gets shortest".
- mark-brann-ab79a322: "I can also go straight to whoever supports client e-applications". This reads as going around him.

**A colleague invited to a call that does not exist:**
- elizabeth-alexander-5a6a0b235, daniel-dan-buchholz-…: "join instead".
- michaelhillunderwriter, nathan-hill-24b77626: "join (too)".
- renee-mcclintic-…, seanconrad: "welcome (on the call) too".

**Broken English:**
- thomas-ferguson-33b4521b, tony-fung-9129169, shane-banks-2a7a2852: "by more than the carrier set". One sentence pasted at three companies.
- brian-pemberton-09ba289: "Could we look at …, with my calendar at [link]", with no question mark.
- kyle-o-donnell-a7b9918: "forward me their way".
- dave-rengachary: "your lead of underwriting".
- samrat-dua: "an API and SDKs step".
- scott-corbett-6b32469: "the record serves documentation as one dated entry".
- deborah-lineberry-a6b713202: "The step lives inside the application … over TLS".
- frank-mikalonis-594b3816: "If owners' questions about steps are useful to you".
- scott-delisi-4a855b7: "What advisors say is what the evaluation would capture first, as completion".
- teesun: "A neighbor of that work".
- "a step of two photos" ×17.

### D. Format & structure, 2/3

- **Calendar link run on, no colon** ("my calendar is here https://…"): tracy-regier-72866a38, andrew-vigar-falu-flmi-74579219, colin-deforge-0639701, dave-rengachary, susan-l-mayer-falu-flmi-07601824, elena-a-s-4a902718b.
- **FAQ sentence with no final period:** dhru-swadia-50b57469, samrat-dua.
- **Filler after a link:**
  - scott-delisi-4a855b7: "if useful."
  - michelle-visconti-44752189: "for anyone who wants it."
  - andy-gordon-0b813423, jonathan-applewhite-…: "for reference."
  - pete-kaczmar-78a6816: "in more detail."
  - emroczek: "in a few lines."
- **Sentence that opens with a bare URL:** laura-mckiernan, nicholelmyers, rmackillop, katie-kahl-15049526, paul-greene-40b337a4.
- **Landing link after the call line,** so the call no longer closes the message: Transamerica ×6 (neal-hasty-a8b356231, tricia-wood-a730745, andrew-vigar-…, sgjense, virginiagreene, christine-kor-aronski-…, ben-wadsley-62460413), RGA ×6, Hannover ×6.
- **No `product:` frontmatter in per-person files.** This is the known `split-messages` gap and is not applied, as in round 0.

### E. Output quality, 2/4

**Strong.** These M1s a senior reader would answer, and their M2s continue the thread:
- danielgarant: agreement scored on the holdouts.
- harry-stanger-6423021b3: an estimate informing the paramed order.
- brandon-smithhart-b6184485: a referral rule or an item on the underwriter's screen.
- michael-farrell-5611685: from the Just Ask quote to the application.
- nate-berns-61472a216: the owner-case build line.
- mark-barnum-b3041619 (M1).
- chriscella, vipulethos, rmackillop, jordanjonassen.
- don-kidd-00a43852: referrals in the capacity plan.
- ernest-armijos-270aa9378, marty-johnson-a25b8ab8, jennifer-johnson-certified-falu-clu-flmi-b5155b42, michael-ash-dollowitch.

**Weak: mail merge when forwarded inside one company.** The company fact is card-assigned to several people. The near-verbatim wording is not allowed: "Wording, hook, structure … never repeat at one company".
- **Munich Re 7/7.** Every M1 opens on "…alitheia at Munich Re Life US…".
  - "draws on EHRs and a growing suite of data sources", verbatim: pattiarellano, brad-heltemes-109a342b.
  - "can be used whole or in parts": jennifer-dalton-9408a339, shane-banks-2a7a2852.
- **Northwestern Mutual: 11 of 13 M1s state "no medical tests".**
  - "accelerated approvals (there) carry no medical tests" ×7: nicole-lund-4055466, jaime-pulsfus, brandon-may-do-dbim-ms-4288a5150, judy-finney-md-1882a34, chris-yiannias-000427116, jonathan-mcallister-a91a5647, allysonschrader.
  - The four MD openers share one skeleton: "[clinical background]. … approvals carry no medical tests, and weight comes from the client's … entry."
  - MD M2s repeat "declared weight left / stays as entered": brandon-may, joel-weiner-md-facp-flmi-18b07151, jonathan-mcallister.
- **Prudential:**
  - "PruFast Track … removes (medical) exams and lab work" ×3: bryan-flynn-21866b9, joel-larson-31339b223, naishami-patel-do-6788267.
  - "FitXpress adds / would add two photos, a Smart Scales weight estimate and a flag": david-wexler-47978554, ashley-destito-a636194b.
- **MassMutual:**
  - M2 "compared with paramedical exam cases" 5/9: warnershue, jason-paine-a0a76416, tasha-boland-…, lynn-brown-0b27474, kathleen-coughlin-38415319.
  - jason-paine and kathleen-coughlin are in the same DI team and share both the M1 opener and the M2.
- **Thrivent:**
  - Online quote, then the financial professional, ×3 tech heads: kenny-membreno-582a091a, jeffrey-einhorn, bbrunick.
  - "some need a paramed, some do not": ryanphawkins, rhonda-steffel-heling-30b798a6.
  - "… is open at" in 4/8 call lines.
- **Protective, Online Part II:**
  - "personalized link": justintallen, jamie-lane-4b923091.
  - "disclosures … height and weight among them": kennethbyrd, russell-kolmin, lindsayhackney.
- **Guardian:**
  - Same opener fact ("health questionnaire and other data") and the same exam-case M2: robert-shourds-falu-flmi-7904aaa4 and anthony-perez-6083812a, the two top underwriters.
  - "term, whole and universal life + a step added": greg-faux-51396437, beth-denning-2a1706159.
- **Others:**
  - Securian: "clients who do not qualify move to traditional underwriting with labs", verbatim: gay-kemmis-76523410, brian-rock-…
  - Pacific Life: "PAL+ routes each application to the least invasive method": tj-doan-a8042597, alanbub.
  - Mutual of Omaha: unisex build charts (timothy-tse-md-mba-1b328a3b, anjali-masand-md-dbim-44966a7a); "own build chart" (kurtis-stewart-50446643, mike-bauer-582a2481).
  - Principal: "Online Part B (there) is completed by the client" (mariancoffey, mike-sir-84b7b610); "When owners / key employees ask … first?" (frank-mikalonis-594b3816, hermanbob).
  - John Hancock: exam-case M2 ×4 (helen-colberg-05a71153, laurie-borowski, andrew-langemeier-…, jordanjonassen).
  - SCOR: "The step and its record are described at" (patrick-scanlon-8774a417b, stacy-stauffer-falu-flmi-b922b384, jessica-lenhard-fsa-4b216047).

**New stock forms, campaign-wide:**
- **Passive booking lines** ("X is open at / can be booked at"), 69 of 277. Some no longer clearly offer a call:
  - colin-deforge-0639701: the offer only applies "If a client raises it".
  - michael-k-469910295: "A short exchange … can start from".
  - braam-kruger-35771576: "A discussion … can start at".
  - dupe-adewunmi: "time for it is open at".
  - brooke-morgan-of-cincinnati: "A walk through the API is open at".
  - matt-winegar-68303421, david-elias-ph-d-005aa8b, vicki-garrett-54256920, karnatrautman, courtney-jacobson-certified-falu-almi-acs-6a4b9096, susan-sucha-219b9016a ("is possible at").
  - teague-jim-481208a: "Your region's view would shape the call".
- **Product-sentence rotation across companies in one batch** (Mutual of Omaha, Thrivent, The Standard, Munich Re). Fine inside each company, but these are mail-merge blocks.
  - "FitXpress takes two photos in the e-application, returns a Smart Scales weight estimate with BMI from the declared height, and flags a gap past the carrier's threshold in one timestamped record." appears verbatim ×4: marty-johnson-a25b8ab8, jean-pfundtner-58626076, jeremy-horner-b549853, greg-dewey-982920221.
  - The "estimates weight with Smart Scales … then flags" block ×3, the "turns two photos into … the carrier sets the gap" block ×4, and the "by more than the carrier set" block ×3 repeat the same way.

## Top 3 issues (priority for improver)

1. **Same-company mail merge on the company-fact sentence and the M2 value line.**
   - Munich Re 7/7 "alitheia at Munich Re Life US".
   - Northwestern Mutual 11/13 "no medical tests", ×7 verbatim.
   - Prudential "PruFast Track removes exams and lab work" ×3.
   - MassMutual exam-case M2 5/9.
   - Thrivent tech trio.
   - Protective Online Part II ×5.
   - Guardian robert-shourds-… / anthony-perez-…
   - Securian gay-kemmis-… / brian-rock-…

   Rule for the next round: the same Account fact may serve several people, but each must state it from a different clause of the source, or not state it and ask about it instead.
2. **Card targets and rule wording survived as clones and became new stock.**
   - Build-chart edge question ×13 (incl. AHOU pair tim-ranfranz-… / bradgabel).
   - Shadow "what would it have to show" ×10.
   - declared-vs-exam guidance ×6.
   - "gathered separately" ×7, from the fix rule itself.
   - Referral "whoever owns underwriting rules or the new-business journey" ×7.
   - "80+ body measurements, under 45 seconds…" ×4.
   - Passive booking lines ×69, several of which no longer offer a call.
3. **Lines a senior underwriter or medical director would stop at.**
   - Self-contradicting evaluation design: tristan-fontugne-…, shawn-fourez-…, eric-hoerr-…, plus loose versions at 6 more.
   - Product and data errors: pattiarellano (height), keerthi-mandala (data "in Ladder's systems only"), tasha-boland-… (class shift).
   - Logic slips: terry-huisman-… (regional build chart), terri-drahn-… (asks for chart values), donna-rogers-…, gregory-soltner-…
   - Nine M1s without the company name: kelly-halverson-…, mark-brann-…, eric-flender-…, laura-cutshall-…, gay-kemmis-…, michaelcliftlifeunderwriting (no FitXpress either), katie-kahl-…, michael-celi, sgjense.

## System notes (not scored against the agent)

- **Gate:**
  - "no company line" fires on the full legal name. It flags 76 people, of whom 67 name the company in short form ("Principal", "Guardian's", "Sammons"). The 9 real misses are buried among them. Accept short names and make a true miss hard.
  - The gate already surfaced the within-company near-duplicates in round 2: Penn, Sammons, Protective, Transamerica, NWM, Prudential, SCOR, Swiss Re. Writers left them. Make "near-duplicate sentence" hard at one company for any sentence other than the compliance line.
  - Add hard patterns for "gathered separately", "80+ body measurements, under 45" and "whoever owns underwriting rules or the new-business journey".
- **Card:** fix rule 7 gave writers the exam-case comparison without saying that the scan must run on those exam or holdout cases. Without that, "limited to accelerated files" reads as a contradiction. Give one approved shape: scan the holdouts or paramed cases, then compare the estimate with measured weight.
- **`notify.py` was not run:** this QC session has no Bash. The coordinator should send:
  `QC: message-sequencer → 12/20 (marginal). Top issue: same-company mail merge on company-fact sentences (Munich Re 7/7, NWM 11/13) + card targets cloned (build-chart ×13, shadow ×10) + self-contradicting exam-case M2 (44 uses). File: workspace/_quality/outbound/2026-11-05-message-sequencer-us-insurance-underwriting-r1.md`

## Coordinator review

```
agreement: ✅ agree
top_issue: new layer after rounds 1-2: same-company mail merge on the account-fact sentence, card targets surviving as clones, and a self-contradicting exam-case comparison that my own fix rule 7 introduced.
```

Coordinator notes (2026-11-05):
- Round 0 slots are confirmed cleared (labels, «point me», P1 easy outs, appointment hooks, lead-in repeats). Same score from a fresh reader on a deeper layer, not a stalled fix.
- Rule 7 of `_fix-r1-rules.md` was mine and incomplete: it named the comparison population without saying the scan must run on those exam or holdout cases. Round 3 gives one approved shape.
- Round 3 is narrow (scripted per-person lists from this report), then mechanical verification without a third QC, as in the EU twin (rounds 3-4).
