---
qc_date: 2026-11-05
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/messages/_dump-r0.md (277 pairs, round 0)
track: outbound
artifact_type: messages
total_score: 12/20
status: marginal
coordinator_review: pending
---

# QC Report: message-sequencer, 2026-11-05 (US insurance underwriting, round 0)

**Artifact:** all 277 pairs in `_dump-r0.md`, read in full, together with the card, `_check.json` (0 hard notes, soft notes only), the summaries and grids.

**Total: 12/20, marginal.** The research layer is strong:
- Hooks are real; I checked AAIM, AHOU, SEHOUA, endocrinologist, customer authentication and supervision programs against the profiles.
- Account facts are mapped to people per `Use:`.
- Number discipline is clean. 3.5% appears 29 times, all in M2 of allowed lanes with "not a scale reading".
- No clients, competitors or cross-prospect names. The decision boundary holds.

The copy layer fails the card's same-company rules at scale:
- Closers and easy outs are near-identical.
- The product sentence is one stock list.
- Card question targets and lane values are pasted as copy.
- Owners and P1 buyers get easy outs that send them to the owner of their own remit.

This needs a targeted fix round driven by rules. A regeneration would throw away good research.

I scored against `card-messages.md` and `_profiles-mixed-*.md` only. Limits, signature, bans, detector and completeness come from the gate, and I took them as fact. As instructed, I did not score these as defects:
- the template lead-ins themselves (I only judged whether they repeat inside one company);
- the verbatim compliance line repeating;
- own-product names in own copy.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence, 2/5

The card says: "Wording, hook, structure, easy-out target and closer never repeat at one company". It also says: "No two people at one company share an opener, a central question, an easy-out target, a Message 2 opener or a closer". The agent prompt adds: "if the note says opener repeated inside one company, fix it: that is your zone".

The gate surfaced most of the repeats listed below as soft notes. The writers listed them and left them in place. For example, `_summary-mixed-1.md` says "the product sentence and easy-out phrasing are the part that reads similar". **Campaign-wide: fix by rule, not by list.**

**A1. Easy out and closer, one frame.**
- "point me" appears 139 times in 277 M2s.
- By company:
  - Principal: 12/13 "Or point me to whoever…"
  - SCOR: 10/10
  - Swiss Re: 9/9
  - MassMutual: 8/9
  - Sammons: 10/14
  - Thrivent: 6/8
  - The Standard: 6/8, three of them the identical sentence "If … sits with/belongs to someone else, point me to whoever owns it." (jeffrey-nattis-35a8964, jody-pfeifer-70629215, rajesh-mondkar-12a1293a)
  - Mutual of Omaha: 4/8 "If … sits with someone else, point me to whoever runs/manages/owns it"
- Prudential swapped the verb but kept one frame, "If X sits elsewhere, …", ×5: michael-farrell-5611685, brian-pemberton-09ba289, ashley-destito-a636194b, karnatrautman, vikrambalwani.

**A2. Bare CTA labels repeated at one company.**
- Sammons: "Call:" ×6 (kory-petoske-15a70194, christie-brammer-92b2a467, courtney-jacobson-certified-falu-almi-acs-6a4b9096, matt-webster-389321228, norma-davis-9064212b, katrishaneisse), "Calendar:" ×3 (beth-abbott-1b495925, nicole-duncan-falu-flmi-airc-acs-03992313, elizabeth-alexander-5a6a0b235), "Slot:" ×2 (pat-grashel-46202a8b, mattrise).
- Penn Mutual: "Calendar:" ×3 (micheleohler, sharon-garner-certified-falu-flmi-8a587980, jacqueline-fallon-977295173).
- Link lead-in "The use case in brief:" at RGA ×3 (jacqueline-waas-05a79145, nathan-hill-24b77626, braam-kruger-35771576) and Hannover ×2 (brian-hiserote-640575b3, kevin-bettis-certified-falu-flmi-ara-acs-airc-a7809a25).

**A3. Product sentence is one stock list.** The card says: "which other parts appear, in what order and in what words, varies between people at one company", and "No stock label for the scan or the record repeats". The list "a Smart Scales weight estimate, BMI from the declared height, and a flag when the gap crosses the carrier's threshold, as one timestamped record" appears at:
- RGA 11/11
- John Hancock 12/13: "BMI from the declared height" in all but katie-kermode
- Hannover 8/10
- Securian 7/7
- Symetra 6/7
- Principal about 11/13
- Transamerica about 9/11
- Gen Re 5/6
- Zinnia 5/6
- iPipeline 3/3

Penn Mutual and Sammons run one skeleton instead: "FitXpress adds/takes 2 photos to/in the e-application and returns a Smart Scales weight estimate with a flag above a threshold [Co] sets" (14/14 and 13/14). The gate counted 106 cases of "BMI from the declared height" and 150 cases of "a Smart Scales weight estimate", flagged as card wording.

Openers that recur inside SCOR (5/10), Swiss Re (4/9) and MassMutual (3/9):
- "We built a step of 2 photos…": SCOR, Swiss Re, MassMutual.
- "2 photos in the e-application give/add…": MassMutual 5/9, Swiss Re 3/9.

**A4. Lead-in repeats inside one company.** The lead-ins are your template, so I counted only within-company repeats.
- "Noticed…":
  - Northwestern Mutual 7/13: julia-oleson-547066106, tim-ranfranz-falu-fmli-81559b1a, judy-finney-md-1882a34, gregory-soltner-do-dbim-falu-flmi-210a6632, chris-yiannias-000427116, jonathan-mcallister-a91a5647, allysonschrader. Four of these are MDs with one frame, "Noticed you/your [specialty] … before insurance medicine".
  - Prudential 6/13: matthewburrill, brian-pemberton-09ba289, david-wexler-47978554, ashley-destito-a636194b, dan-manley-b15759, naishami-patel-do-6788267.
  - Transamerica 6/11: tracy-regier-72866a38, tricia-wood-a730745, andrew-vigar-falu-flmi-74579219, sgjense, virginiagreene, ben-wadsley-62460413. Three of these are a standalone "Noticed … before Transamerica."
  - Principal 5/13: terry-huisman-91231b48, kris-vanderkooy-md-dbim-flmi-aa751b122, mariancoffey, jeff-kruger-9a130b24, heatherdawson33.
- "Quick [note/thought/one]":
  - Penn Mutual ×3: michael-clark-61006a107, amzadhossain, sharon-garner-certified-falu-flmi-8a587980
  - Swiss Re ×3: eric-hoerr-certified-falu-flmi-071b77b1, cynthia-landry-922908a2, samrat-dua
- "Your headline pairs X with Y": Hannover ×2 (seanconrad, kevin-bettis-…). This is the same frame the 2026-11-02 EU QC flagged.

**A5. Card wording as copy (card: "Lane notes, targets and rule sentences are never pasted"; agent rule 11).**

Question targets kept as the question:
- "What would you need to know about a software (weight) estimate before it enters/touches accelerated rules?" ×15: michael-clark-61006a107, matt-webster-389321228, naishami-patel-do-6788267, brandon-may-do-dbim-ms-4288a5150, katie-kermode-md-428495330, kris-vanderkooy-md-dbim-flmi-aa751b122, mark-vincent-0946a624, timothy-steffen-md-dbim-469092256, michael-k-469910295, elena-a-s-4a902718b, timothy-tse-md-mba-1b328a3b, robert-lund-56708349, lara-shemtob-md-b41456236, harry-stanger-6423021b3, michael-moore-a2568a26.
- "How far above the estimate's error would a threshold have to sit" ×10: norma-davis-9064212b, jill-fallon-944a9812, judy-finney-md-1882a34, elaine-szewc-80785530b, virginiagreene, anjali-masand-md-dbim-44966a7a, rhonda-steffel-heling-30b798a6, gina-guzman-67396b148, shona-murray-283910134, paulobpinho.
- "agents and BGAs" ×7: micheleohler, elizabeth-alexander-5a6a0b235, ericskaiser, john-dieck-a2310036, lindsayhackney, kyle-o-donnell-a7b9918, beth-denning-2a1706159.
- "agent-assisted … or the applicant's own section after the hand-off" ×9: brent-ricci-7b922a132, kevin-hill-2429849, bryantfuller, jamie-lane-4b923091, kelly-halverson-2a8a467, alycia-bellody-055726335, matt-mylroie-48780994, david-mcnamara-jd-cfp%c2%ae-5b584912, ericpahlfsa.
- "build credits … evidence cost" ×7: billbellpml, katrishaneisse, ernest-armijos-270aa9378, russell-kolmin, nathan-hill-24b77626, jonathan-applewhite-fsa-5b826911, brian-rock-fsa-cera-maaa-25203b142.
- "At which build-chart edges…" ×17 and "How does your team check build on those files today?" ×12. The full list is in the gate's "card question target as the question" and "M1 question repeated" notes.
- Keerthi-mandala's question is the card target nearly word for word: "on the risk side … API and advisor channels included".

Lane M2 values pasted:
- "counts flags per candidate threshold … build evidence collected another way / independently": 61 cases of "candidate threshold" and 30 of "collected another way/independently". Inside one company:
  - RGA ×6: colin-deforge-0639701, michaelhillunderwriter, nick-sontheimer-b01084178, dave-rengachary, braam-kruger-35771576, jacqueline-waas-05a79145
  - John Hancock ×4: helen-colberg-05a71153, laurie-borowski, jordanjonassen, andrew-langemeier-falu-flmi-b7398813a
  - Protective ×4: shawn-fourez-72628142, bradgabel, russell-kolmin, stephen-lininger-392aa332
  - Pacific Life ×4: jenniferglessner, tj-doan-a8042597, tristan-fontugne-5477b89, matt-winegar-68303421
  - MassMutual ×4: warnershue, jason-paine-a0a76416, lynn-brown-0b27474, kathleen-coughlin-38415319
- "results to the carrier's systems only" appears as "[Co]'s systems only" ×27:
  - Protective ×3: frances-freeman-69582136, lindsayhackney, kennethbyrd
  - Lincoln ×3: katie-klod-76b65219, jonathan-applewhite-…, mike-hamilton-6029653
  - John Hancock ×3: ericskaiser, jasvinder-khera-10bbb620a, christopherlintecum
  - Ameritas ×2: kyle-o-donnell-a7b9918, lynn-saddoris-mba-b188749
- The "What it is not" rule sentence, "keeps its current route for anyone who cannot or does not scan", appears ×18:
  - Principal ×4: frank-mikalonis-594b3816, hermanbob, mike-sir-84b7b610, heatherdawson33
  - Prudential ×3: david-wexler-…, salene-hitchcock-gear-a8207a12, karnatrautman
  - Sammons ×3: beth-abbott-… (M1 and M2), christie-brammer-…, courtney-jacobson-…
  - Penn Mutual ×2: micheleohler, velezjacqueline
  - Pacific Life ×2: victoria-liu-fsa-fcia-98519a14, john-dieck-…
  - Others: christopherlintecum, kevin-hill-…, jamie-lane-…, jean-pfundtner-58626076
- The agent prompt's own example sentence, "It returns 80+ body measurements, under 45 seconds from the photos to structured results.", is used as the M2 value line ×4: karnatrautman, malenoir, ashwath-muralidharan-945a415, hale-laura. The card says 80+ is "secondary, never the lead", and "It" has no antecedent five days after M1.

**A6. Easy out given to buyers and owners.** The card's easy out is "for people who are not the buyer". Almost every P1 got one. The sharpest cases point the owner to the owner of their own remit:
- jamie-lane-4b923091, VP Head of NB Ops **and Enterprise Shared Services**: "Or point me to whoever owns shared services"
- kennethbyrd, head of protection NB ops: "point me to whoever runs Online Part II"
- anthony-perez-6083812a: M1 says "Build guidance for accelerated cases sits with the chief underwriting officer"; M2 then says "The team that maintains build guidance is welcome too"
- gretchen-dinucci-74b33b45, Chief Underwriter: "If someone else owns the build chart"
- tim-ranfranz-…, Chief Life Underwriter: "The owner of the build chart is equally welcome"
- warnershue, Head of Underwriting: "whoever maintains the build chart"
- rebecca-severson-certified-falu-flmi-ara-acs-5536552b, Chief Underwriter: "If the build chart is owned elsewhere"
- mike-derrig-65213323, Chief Underwriter: "If someone else owns the Swift chart"
- Chief medical directors:
  - kris-vanderkooy-…: "whoever writes Principal's build guidance"
  - ronelle-moe-7a4a70280: "whoever owns medical guidance on term"
  - michael-moore-a2568a26: "Whoever owns medical guidance for accelerated rules"
  - marianne-cumming-9b85442b: "The person who maintains build guidance may be the better contact"
  - shona-murray-283910134: "If someone else sets build guidance for WriteFit"
- michael-ash-dollowitch, Chief Underwriter IDI: "The owner of IDI evidence rules would also be a good contact"
- nate-berns-61472a216, whose team built the model: "whoever runs the owner-case rules"

**A7. M1 does not say what comes back** (card "What the scan is": "Message 1 makes clear what comes back"):
- rebecca-severson-…: FitXpress is never named; there is no weight estimate. "Two photos in the e-application can raise a flag when a weight gap crosses a threshold"
- seanconrad: "It runs on 2 photos…", where "It" has no antecedent and FitXpress is not named in M1
- pattiarellano: "records a timestamped entry"; no product name, no estimate
- pete-kaczmar-78a6816: "runs on 2 photos in the e-application and a threshold flag"; what is flagged is never said
- beth-abbott-1b495925: "2 photos in the e-application with a flag above a threshold"

**A8. Account-fact `Use:` mapping.** Mostly followed. Deviations:
- beverley-sloley-flmi-mba-ba112027 was due "a consistent, documented decision" but got the holdouts question (see B).
- russell-kolmin was due the term application but got the Velocity checklist.
- roger-hofer-79065019 was due post-issue review but got build-chart edges.
- jason-paine-a0a76416 and kathleen-coughlin-38415319 did not get the January 2026 DI update.
- spflan was due "where a build referral rule sits" but got build-chart edges.

### B. Factual accuracy, 4/5

**Clean:**
- Every number is from the approved list. 3.5% only in M2 of `underwriting`, `medical` and `reinsurance`.
- No client, competitor, pilot, price or trial term.
- No prospect is named in another prospect's copy. Own products appear only to their own team (Aura Next, Velogica/SMART/SOLEM, Magnum/Life Guide, ReFlex, alitheia, SOURCE, TPP, iGO Evolve/Novera/Resonant/XRAE).
- No former employer that is an account is named. Hartford, Lincoln and MetLife are avoided where Never asks.
- Corebridge is absent. Laura Cutshall is at Hannover with no SCOR or Velogica. "Hi Jim," is correct.
- No "verify", decision or suspicion claims.

**Never line hit:**
- kennethbyrd: Protective Never lists "executive changes". The copy says "Quick note on your move from 2nd VP of new business operations to heading protection new business."
- Also check gina-guzman-67396b148, "Your step up from medical director to chief medical director at Munich Re Life US". The global Never covers appointments, and Munich Re's covers "the 2025 leadership change".

**Prospect process asserted without a card fact:**
- beverley-sloley-…: "How do the program's random holdouts or post-issue reviews treat build today?" Ameritas facts do not mention holdouts.
- neal-hasty-a8b356231: the same presumption at Transamerica.
- scott-delisi-4a855b7: "Disability income applications at Ameritas rest on the height and weight the applicant types". There is no Ameritas DI fact.
- mike-sir-84b7b610: "A DI application asks the client for declared height and weight, and nothing else measures build". This is wrong where Principal's DI amounts call for exams.
- matt-winegar-68303421: "new business repricing at Pacific Life depends on what is known about build at issue".

**Underwriting logic a senior UW will catch.** M1 says the accelerated file has no build evidence; M2 then compares against build evidence "already" on it:
- laurie-borowski: "build evidence the program already holds"
- andrew-vigar-falu-flmi-74579219: "the build evidence already collected"
- warnershue: "already on the cases"
- jason-paine-a0a76416: "you already hold"
- lynn-brown-0b27474: "already on the case"
- eric-hoerr-…: "the client already holds"
- jacqueline-waas-05a79145: "already on the same files"

The card means independently collected evidence (holdouts, paramed cases).

**Mechanics garbled:**
- kris-vanderkooy-…: "a flag only refers gaps that sit well above it [the threshold]"
- bradgabel: "…not a scale reading, which puts any threshold well above it"
- cynthia-landry-922908a2: "The flag refers gaps…, read against build guidance in Life Guide". This edges toward implying that Swiss Re uses it.
- tasha-boland-fsa-cera-4632a3109: "the evaluation question is placement", which is the wrong term.

**Persona slip:** mary-bates-491652139, an SVP of Risk Management, gets "For an R&D read".

**Sourcing:** not applicable (outbound).

### C. Brand & tone, 2/3

**Hard ban passed by the gate:** michael-celi M1, "FitXpress is 2 photos **plus** a Smart Scales weight estimate…". The card rule is "no 'plus' as a connector".

**Corrective negation:** jeffrey-noren-00a879231 M2, "completion is measured in the evaluation, not assumed."

**Sender misattribution (campaign-wide frame).** The phrase grammatically makes Nick the holder of the role or side:
- matt-webster-389321228: "Wanted to reach out as Chief Medical Director at Sammons."
- vicki-garrett-54256920: "Wanted to reach out as Swiss Re Americas' US facultative underwriting manager…"
- dave-loparco-3604241ab: "Couldn't help but ask, as head of US underwriting risk management…"
- lindsayhackney: "Quick idea for you, from someone who began in customer authentication"
- elena-a-s-4a902718b: "As VP, Medical Director at Hannover Re US, modernizing medical assessment is part of your remit"
- "from the X side" ×11:
  - alycia-bellody-055726335: "from the agent side"
  - timothy-tse-md-mba-1b328a3b: "from the medical side"
  - christopher-hall-898635277: "from the privacy side"
  - jamal-b-70b7b32a: "from the security side"
  - tim-lyons-7098023 and timothy-nash-1815973: "from the vendor review side"
  - todd-lukens-7a0aa4: "from the new-business side"
  - robert-reynolds-77626a8: "from the individual life side"
  - brian-rock-fsa-cera-maaa-25203b142: "from product development"
  - vrai-productmanager: "from the system-of-record side"
  - roger-hofer-79065019: "from the corporate underwriting side"

**Title read back as the address (merge-field feel)** ×13:
- michael-clark-61006a107: "Quick thought for a CMO at Penn Mutual"
- joel-larson-31339b223: "Quick note for a chief underwriter"
- sheila-macdonnell-a762b22b, kevin-hill-2429849, nate-berns-61472a216, eric-hoerr-…, cynthia-landry-…, samrat-dua, michael-moore-…, kathleen-coughlin-…, ed-sheehan-36768718a, harry-stanger-…, jill-fallon-…

**Presumed reaction (agent judgment ban 8):**
- jean-pfundtner-58626076: "you know what a Declaration of Insurability leaves out"
- rhonda-steffel-heling-…: "you weigh evidence that is not a measurement"
- seanconrad: "probably crosses your desk"
- jonathan-applewhite-…: "is likely weighing"
- mark-barnum-b3041619: "you know the files where…"
- anjali-masand-…: "you know how build charts get used"
- smitha-jagalur-b61b1a131: "you know what an added step costs"
- mike-bauer-582a2481: "you would see where a new flag lands"
- thomas-ferguson-33b4521b: "you see how a new input gets tried"

**Dismissive register near suspicion.** "whatever the applicant types/declares/enters" appears ×12: gretchen-dinucci-…, judy-finney-…, mariancoffey, tj-doan-…, timothy-steffen-…, jason-paine-…, kevin-m-o-hanlon, timothy-tse-…, jennifer-dalton-9408a339, mike-derrig-…, nathan-brown-b1698990, and "build is whatever height and weight get typed". Two lines read as a slight on the carrier's own program:
- alex-crawford-17205223: "faster accelerated files leave fewer moments where anyone looks at build"
- shawn-fourez-72628142: "more files where nobody measures build"

**Broken English:**
- frank-mikalonis-594b3816: "Thought I'd pass this on something relevant to…"
- gretchen-dinucci-…: "which build-chart edges would such a gap move a class at?"
- robert-shourds-falu-flmi-7904aaa4: "From a risk and excellence background, the useful output is a count"
- james-atkins-flmi-falu-a919a564: "a 2 photos step"
- georgette-chekiri: two near-identical questions in one M1
- kelly-halverson-2a8a467, andy-gordon-0b813423 and ericpahlfsa: "FitXpress returns a structured record, under 45 seconds from the photos to structured results". "Structured" appears twice; andy-gordon's whole value line is this sentence.
- Sentence-initial numeral "2 photos in the e-application give…" about ×13 (MassMutual, Swiss Re, SCOR). This is gate-driven; see the system notes.

**Idioms:**
- ericskaiser: "has to earn its place"
- david-moon-045b748: "earns its place"
- terry-huisman-91231b48: "earns its keep"

### D. Format & structure, 2/3

- **Calendar link glued to the redirect clause, so the link reads as the person to be pointed to:** "Or point me to whoever owns shared services: https://meetings…". Cases:
  - tj-doan-a8042597, mark-vincent-0946a624, john-dieck-a2310036, david-mcnamara-jd-cfp%c2%ae-5b584912, tristan-fontugne-5477b89, matt-winegar-68303421
  - victoria-liu-fsa-fcia-98519a14, shawn-fourez-72628142, lindsayhackney, jamie-lane-4b923091, kennethbyrd

  This is a different issue from the accepted "easy out after the link".
- **Bare URL with no sentence around it** (card: "the sentence around it differs each time"):
  - landing: pete-kaczmar-78a6816, neal-hasty-a8b356231, virginiagreene, michaelhillunderwriter, dave-rengachary
  - FAQ: tricia-wood-a730745, sgjense, ron-hollowell-92b1861b, dbelanger1
- **M1 body paragraphs of 3-4 sentences** (agent template: ≤ 2). This is batch-wide in the Prudential and Northwestern Mutual batch (e.g. bryan-flynn-21866b9, michael-farrell-5611685, salene-hitchcock-gear-a8207a12, dupe-adewunmi) and the Ameritas, Guardian and Lincoln batch (e.g. jennifer-black-b1034649, helena-roberts-7b87a694, rachael-maurer). The M2 layout also differs by batch: compliance line, CTA and link in one paragraph in some, separate lines in others.
- **No `product:` frontmatter in per-person files.** I did not apply the hard D ≤ 1 rule. This is the known `split-messages` template gap, as in the 2026-10-26 and 2026-11-02 QCs.

### E. Output quality, 2/4

**Strong.** Hooks that only someone who read the profile could write:
- marianne-cumming-9b85442b: past AAIM president
- tim-ranfranz-… and bradgabel: AHOU
- susan-l-mayer-falu-flmi-07601824: SEHOUA
- michael-k-469910295: endocrinologist
- lindsayhackney: customer authentication, but see C

Questions a senior reader would answer:
- danielgarant: agreement scored on the holdouts as control
- rmackillop: large gap routed to an underwriter or to the at-home check
- vipulethos: request at submission or event afterwards
- chriscella: Resonant or XRAE
- tracey-schifferdecker-55584a72: build evidence on a fit-credit case
- jessica-lenhard-fsa-4b216047: SCOR's human-final stance
- james-mcardle-590a9663: the next ReFlex question
- jennifer-johnson-certified-falu-clu-flmi-b5155b42: an Aura Next reflexive question

M2s that continue the question:
- helena-roberts-7b87a694: compare against the measurements Lincoln already orders
- joel-weiner-md-facp-flmi-18b07151: "The use we suggest is narrow"
- mike-derrig-65213323: "Small differences are left alone"

**Weak.** A pair at Principal, Sammons, SCOR, Swiss Re, RGA or MassMutual reads as one template with a swapped hook. In M2, the value line comes from the lane note, followed by the identical compliance line, a bare CTA label and "Or point me to whoever…". In M1, the stock product list comes before a card-target question. At those companies M2 falls below the 60%-unique override, and M1 sits at about the line. Forwarded inside a company, these read as a mail merge, which MSG-7 warns about. Thin M2 value lines:
- andy-gordon-0b813423: the speed sentence only
- ronelle-moe-7a4a70280: the 3.5% sentence only
- jim-teague (teague-jim-481208a): "For applicants it is a short step"
- brian-rock-…: M2 drops his M1 build-credit question

## Top 3 issues (priority for improver)

1. **Same-company sameness in the slots the card names, left in place after the gate surfaced it.** Fix these by rule:
   - Easy out and closer: "Or point me to whoever…" (139 in 277 M2s; Principal 12/13, SCOR 10/10, Swiss Re 9/9, MassMutual 8/9, Sammons 10/14).
   - Bare CTA labels: Sammons "Call:" ×6 / "Calendar:" ×3 / "Slot:" ×2; Penn "Calendar:" ×3.
   - The stock product list: "Smart Scales weight estimate, BMI from the declared height, flag…, one timestamped record" (RGA 11/11, John Hancock 12/13, Securian 7/7).
   - "Noticed" lead-ins: Northwestern Mutual 7/13, Prudential 6/13, Transamerica 6/11, Principal 5/13.
   - Link lead-ins: RGA and Hannover.
2. **Card wording as copy.** Roughly 75 central questions keep the card's targets: medical ×25, BGAs ×7, agent-assisted/own section ×9, build-credit ×7, plus the build-chart-edge and "check build today" twins. Lane M2 values are pasted ("candidate threshold" 61, "collected another way" 30, "systems only" 27). The rule sentence "current route for anyone who cannot or does not scan" appears ×18, and the prompt's "It returns 80+ body measurements…" ×4. The fix round needs "reword, do not drop" so that M1 keeps the weight estimate and the gap.
3. **Lines that a senior US underwriter or medical director would find off:**
   - Easy outs to P1s and owners that point to the owner of their own remit: jamie-lane-4b923091, kennethbyrd, anthony-perez-6083812a, gretchen-dinucci-74b33b45, tim-ranfranz-falu-fmli-81559b1a, the chief medical directors (kris-vanderkooy-…, ronelle-moe-…, michael-moore-…, marianne-cumming-…) and the rest of A6.
   - Sender-misattribution frames: matt-webster-389321228, vicki-garrett-54256920, dave-loparco-3604241ab, lindsayhackney, and "from the X side" ×11.
   - "Build evidence already on the file", contradicting the accelerated premise: laurie-borowski, andrew-vigar-…, warnershue, jason-paine-…, lynn-brown-…, eric-hoerr-…, jacqueline-waas-….
   - One Never-line hit: kennethbyrd, Protective "executive changes".

## System notes (not scored against the agent)

- **Lessons from the EU twin were not carried over.** The 2026-11-02 EU QC and its rounds 3-4 fixed exactly these frames:
  - P1 easy outs
  - "Calendar:"/"Call:" labels
  - card question targets
  - "Your headline pairs"
  - "Quick note for the [title]"
  - the 80+ example sentence

  The coordinator verified "0 P1 easy outs, 0 same-company CTA/closer repeats" there, but none of it reached this card or the gate. Put these into the card's Rules, or better into `check-messages` as hard notes, before round 1.
- **Gate gaps:**
  - `plus` passed (michael-celi).
  - Lead-ins are compared on the first three words only, so "Noticed your…" and "Noticed you…" escape.
  - No check for easy outs on P1s or owners.
  - No check for a link glued to a redirect clause.
  - "two photos" still does not count as a number. That produces sentence-initial "2 photos…" and "a 2 photos step".
  - Soft "M2 easy out shared" and "M1 product sentence shared" notes for one company should be hard at ≥ 3.
- **`notify.py` was not run:** this QC session has no Bash. The coordinator should send:
  `QC: message-sequencer → 12/20 (marginal). Top issue: same-company sameness the gate surfaced and writers left (139 "point me" closers, stock product list, bare CTA labels) + card question targets/lane values as copy; easy outs to P1 owners. File: workspace/_quality/outbound/2026-11-05-message-sequencer-us-insurance-underwriting.md`

## Coordinator review

```
agreement: ✅ agree
top_issue: same-company sameness in easy-outs, CTA labels and the product list, plus card question targets and lane value lines pasted as copy; fixed by one rule-based round sent to the same ten writers.
```

Coordinator notes (2026-11-05):
- Confirmed by my own scan before this report: Principal 12/13 «Or point me to», Sammons «Call: URL Or point me…» on one line, «The use case in brief:» ×5, «plus» (michael-celi), «not assumed» (jeffrey-noren), the doubled «structured» speed sentence ×3, the shared 3.5% sentence at Protective ×4. Cross-account names, other prospects' products and Never items: clean except the two appointment hooks QC found.
- Two causes are mine, not the writers': (1) my batch prompt asked for the numeric «2 photos» in M1, a lesson from the EU twin that the gate fix 94dbbf7 (it counts «two photos» as the number) had already made unnecessary; it produced sentence-initial «2 photos» and «a 2 photos step». (2) The EU twin's round-3/4 rules (no P1 easy outs, no CTA labels, no card targets as questions) were not carried into this card or prompt.
- The light-hook lead-ins come from Vadim's Message 1 template; only within-company repeats are fixed.
