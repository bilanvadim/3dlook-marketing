---
qc_date: 2026-11-02
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/messages/ (130 pairs, after fix rounds 1 and 2)
track: outbound
artifact_type: messages
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-11-02 (EU insurance underwriting, after fix rounds 1 and 2)

**Artifact:** all 130 pairs (`all-pairs.md`, current text verbatim), the three samples, `_check.json` (0 hard, soft notes only) and the four `_summary-mixed-*.md`.
**Total: 14/20, marginal.** Lane choice, compliance lines, number discipline and the Never lines are clean. Three things are not:
- Same-company sameness the card forbids: hook frames, M2 openers and CTA lines.
- Card question targets used as the question with the noun phrases kept.
- 14 M1s that lost "what comes back" when round 1 cut the shared scan sentences.

This needs a targeted round 3 of about 90 line edits. No regeneration.

I scored against `card-messages.md` and `_profiles-mixed-1..4.md` only. Limits, signature, bans, detector and completeness come from the gate, and I took them as fact. I did not flag the items the coordinator accepted: the easy out after the link, the verbatim compliance line and the 3.5% sentence repeating, and "Hi Carole,".

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence, 3/5

**A1. M1 no longer says what comes back (card "What the scan is": "Message 1 makes clear what comes back"; a single label is never enough).** These M1s give "2 photos", "a record" and "a flag" but never the weight estimate, BMI or what the gap is between. Most came from round 1's R2 (shared scan runs), where content was cut instead of reworded. Three of them are P1 (Carl, Matthew, Ross). MSG-1 puts the strongest specific in M1.
- carl-christensen-66bba028: "FitXpress sends the insurer's systems a timestamped record. The insurer sets the threshold for a flag."
- ginger-turner-b867284: "one timestamped record reaches the insurer's systems. Any flag depends on the insurer's own threshold."
- darrendempsey: "A scan starts from 2 photos and ends as a timestamped record, with the threshold flag as one of its fields."
- holger-krebs-547b0865: "A step of 2 photos could sit beside the health answers there. Alte Leipziger's threshold decides whether the broker sees a flag"
- r3425: "FitXpress could feed those rules with a build record from 2 photos, flagged only above a threshold the insurer sets."
- rensengelen: "The scan would add 2 photos there, and NN's own threshold decides whether a flag is raised."
- diana-glenewinkel-317329179: "FitXpress could add build evidence there from 2 photos, and the company's own threshold decides whether a flag is raised."
- karen-o-flaherty-qfa-sia-3b798555: "One timestamped record goes back to the insurer's systems, and a flag shows only above the threshold the insurer chooses."
- adrien-givaudan-658600190: "each applicant's 2 photos yield one timestamped record, and the flag shows only above the insurer's threshold."
- lyonsmichelle: "FitXpress takes 2 photos and raises a flag only above the insurer's threshold."
- sebastian-strasser-bb5a238a: "A flag is raised only when the gap crosses the insurer's own threshold." ("the gap" is never defined)
- matthew-tinney-44598094: "flags a gap only above a threshold Royal London Ireland sets." (gap undefined)
- erik-guth%c3%b6rl-332347245: "flags a gap only above a threshold CosmosDirekt sets." (gap undefined)
- claire-donohoe-fca-85394717: "It also returns 80+ body measurements, and a flag appears when a gap crosses the threshold Aviva sets." (the "also" has nothing before it, 80+ leads, and the gap is undefined)

**A2. Same-company repeats (card: "Wording, hook, structure, easy-out target and closer never repeat at one company"; "No two people at one company share an opener … a Message 2 opener or a closer").**
- M1 hook frame "career move from X to Y":
  - SCOR France ×3: manuel-plisson-812978a "you moved from inclusive underwriting to…", antoine-moll-6373042 "your move from biometric risk calculators to…", elsa-renouf-helfen-93a9283b "your path runs from business acceptance to…"
  - Zurich Life Ireland ×4, in two twin pairs:
    - michael-vesey-1125772ab "Noticed your path from propositions actuary to Head of…" and niall-walsh-447b5686 "Your move from actuarial operations to Head of…"
    - laura-corrigan-78467483 "With a technical underwriting background and now Head of New Business at Zurich Life Ireland" and cormac-frawley-53932253 "With a security engineering background and now Head of Data Protection at Zurich Life Ireland"
  - Irish Life ×3: kelvingillen "you moved from CIO roles to…", richard-l-6b832012 "Noticed your move from enterprise architecture at Uisce Éireann to…", lauren-mccormack1 "Noticed your path from proposition delivery to…"
  - Hannover Re ×2: margot-wilson-889156b "Noticed your path from underwriting leadership at AMP to…", susanne-buchholz-628198bb "You moved from Senior Underwriter to…"
- "Noticed …" opener:
  - a.s.r. 3 of 4: angelique-r-072a756 "Noticed your work…", marnomiddelbos "Noticed you trained…", gert-lokhorst-9331648 "Noticed you wrote…"
  - Gen Re 3 of 7: andres-webersinke-2921085 "Noticed your role…", simon-fallais-phd-b06a5323 "Noticed your background…", teppert "Noticed overlap…"
  - Gen Re's other three open on "Quick…": carstengiese "Quick thought on", upasdika "Quick note on", carina-betz-180b82106 "Quick one for"
- Munich Re Germany "Quick …" ×4: albansenn "Quick note on", volker-homola-ba2a49164 "Quick one on", wolfgang-mörlein-1ab715209 "Quick idea for", thomas-gei%c3%9fler-902a60157 "Quick thought for"
- Swiss Re "You [verb] … at Swiss Re." ×4 (title read back as the hook):
  - ashish-agarwal-0219716 "You head technology and data for L&H Solutions at Swiss Re."
  - dan-lacurezeanu-857672b "You run product and delivery for Magnum at Swiss Re."
  - charpentier-carole-84a43aa "You manage the underwriting rules in Magnum at Swiss Re."
  - rainer-helfenstein-aab817135 "You lead the Swiss Re L&H market for the Netherlands."
- Swiss Re "[Note/Thought] for the [title] at Swiss Re:" ×3: velina-peneva "For the CEO of Life & Health Reinsurance at Swiss Re:", augusto-diaz-leante-919422 "Note for the head of L&H Continental Europe at Swiss Re:", sergio-lopez-jimenez-fia "Thought for the head of L&H research and forecasting at Swiss Re:"
- "Your bio says / centres / talks":
  - Swiss Re: claude-schwarz-55b61112 "Your bio says you led…", ianlong "Your bio centres on…"
  - Munich Re: fabian-schmitt-748430154 "Your bio says you love…", roland-schneider-529b65b9 "your bio talks about…"
- M2 openers:
  - Munich Re ×3, same frame "A (first) client evaluation can [run in shadow / stay small / be light]: shadow mode, …": christoph-henschel-a7961466, roland-schneider-529b65b9, fabian-schmitt-748430154
  - NN ×2, "A shadow evaluation …": rensengelen, remco-de-mol-392b5a6
  - a.s.r. ×3, "[label]: Smart Scales has approximately 3.5% …": angelique-r-072a756 "For the guidance:", marnomiddelbos "The estimate has a stated error:", andr%c3%a9-rozemuller-1407171b "On the numbers:". The 3.5% sentence may repeat; this opener frame may not.
  - Swiss Re ×2: augusto-diaz-leante-919422 "One client could try a shadow design with no effect on cases." and rainer-helfenstein-aab817135 "One Dutch insurer could try this in shadow mode and leave decisions untouched."
  - Zurich ×2, same argument: michael-vesey-1125772ab "A broker journey can carry the step, and the evaluation measures completion." and niall-walsh-447b5686 "web and mobile SDKs can carry the step in a broker journey. A broker test would measure completion."
- Swiss Re M1 shared phrase "a threshold set well above the estimate's error": claude-schwarz-55b61112 "A flag appears only above a threshold the insurer sets, well above the estimate's error." and charpentier-carole-84a43aa "A flag is raised only above a threshold set well above the estimate's error."
- CTA line before the link repeated at one company:
  - "Calendar:"
    - Aviva Ireland ×3: brian-o-malley-8a67a837, claire-donohoe-fca-85394717, jean-larkin-b3b55333
    - Alte Leipziger ×2: holger-krebs-547b0865, karsten-vogel-alh
    - Munich Re Automation Solutions ×2: r3425, georgefox1
    - NN ×2: rensengelen, remco-de-mol-392b5a6
    - SCOR Germany ×2: thomas-trompetter-8326aa22a, fouzia-boussetta-845a321
  - "Call:" at Irish Life ×3: patricia-smith-b8747827, shay-browne-34a99a19, richard-l-6b832012
  - "A call:"
    - Irish Life ×2: brendan-lambe-8820b92b, siobhanbuckley
    - SCOR France ×2: adrien-givaudan-658600190, marvin-dewkurun-5474a363
- Closer "…, a pointer helps.":
  - Zurich: michael-vesey-1125772ab "If broker journeys sit elsewhere, a pointer helps." and niall-walsh-447b5686 "If innovation work sits elsewhere, a pointer helps."
  - LV 1871: jakob-limbach-160729309 "If the BU journey sits elsewhere, a pointer helps." and sandrajohn "If another person runs the simplified check, a pointer helps."
  - Volkswohl: erik-schwarz-588b15214 "If adviser testing sits elsewhere, a pointer helps." and carina-gervens-547a04279 "If someone else owns the BU application journey, a pointer helps."
- Closer "[X] may [sit/own], tell me who / point me there":
  - Irish Life ×3: patricia-smith-b8747827, richard-l-6b832012, shay-browne-34a99a19
  - SCOR ×4: st%c3%a9phanie-haas-maret-4a822573, jennifer-coleman-761b6b5b, redmond-murphy-87343727, manuel-plisson-812978a
- SCOR M1 "statement, then the same thing as a question":
  - st%c3%a9phanie-haas-maret-4a822573 "A new evidence source needs controls before it reaches a client's rules." / "Which controls would a remote build record need to pass before it appears in a client's rules?"
  - jenny-mcdonnell-82a4a61b "A new evidence source needs acceptance criteria in a client treaty." / "What acceptance criteria would a remote evidence source have to meet in a client treaty?"

**A3. Card question targets and lane values used as copy, noun phrases intact (card: "Lane notes are instructions to the writer; none of their sentences goes into a message").** The topic being from the card is fine. Keeping the card's wording is not, and it makes the same question appear across companies (MSG-7).
- Band edges, about 9 people: "At which band edges would a gap between declared and estimated weight change the outcome / a build rating / an outcome in your guidance / an AOV acceptance outcome / a rule outcome in Magnum?"
  - Word-for-word with the card: florian-kreutzkam, noel-finnegan-6b9694a, susanne-buchholz-628198bb, gert-lokhorst-9331648, charpentier-carole-84a43aa
  - Close variants: thomas-lay-b3173484, elsa-renouf-helfen-93a9283b, luisaljimenez, jean-larkin-b3b55333
- Verbatim twins: erik-guth%c3%b6rl-332347245 and carina-betz-180b82106, "How is build checked today on cases that never see a doctor's examination?"
- Verbatim twins: steven-wiseman-9126719a and andr%c3%a9-rozemuller-1407171b, "How does your medical guidance treat a declared weight against a doctor's weighing?"
- "…need to know about [a software weight / such an] estimate before it enters referral rules?": albansenn, ralf-woltmann-592970163, angelique-r-072a756
- "How far above the estimate's error would a (referral) threshold have to / need to sit…?": dr-gabriele-teichmann-222665a, johnschoonbee, marnomiddelbos
- "…need to see in a shadow evaluation before any result / flag reaches a case?": mark-cree-12207b26, margot-wilson-889156b, claude-schwarz-55b61112, antoine-moll-6373042
- "test a new remote evidence source with (one) German client": carstengiese, thomas-trompetter-8326aa22a, markus-unterkofler
- "asked (you) about remote build evidence?": volker-homola-ba2a49164, upasdika, steven-hardy-1b8b261b, jennifer-coleman-761b6b5b
- "How does [Company] review a new data processor for the new-business journey?", with only the company name swapped: richard-l-6b832012, amirfattah, cormac-frawley-53932253
- "test a new (application) step with brokers / advisers before it goes live": laura-mongan-65b6b934, paulanthonycourtney, joe-charles-2049565, niall-walsh-447b5686, erik-schwarz-588b15214. Four of these are Dublin insurers.
- "measure drop-off": brian-o-malley-8a67a837, patricia-smith-b8747827, laura-corrigan-78467483
- "the broker's risk check or the direct online journey/application": jakob-limbach-160729309, carina-gervens-547a04279
- "weigh build loadings against the cost of (collecting) evidence": marcel-beißer-b9b8b617b, siobhanbuckley
- "How does an SDK step (usually) enter the e-application / a web or mobile application journey?": denis-eivers-13b13a105, michael-ewers-21973193
- Card "Use:" wording pasted into the body:
  - carl-christensen-66bba028 "Magnum is the engine where a build referral rule would sit"
  - keyvanizadi "The MIRA Digital Suite looks like the place a build flag would be tested"
  - fabian-van-lancker "How would a new evidence step be added so that each insurer can switch it on through one integration?"
  - klaus-strumberger-0699538 "What do insurer clients ask Morgen & Morgen for at the point of sale?"
  - dr-gabriele-teichmann-222665a "you sit behind what a software estimate may be used for"
- Partnership M2 value pasted: klaus-strumberger-0699538 "Integration runs through an API and web and mobile SDKs, with one timestamped record per applicant returned to the platform." and r3425 "…with one timestamped record per applicant returned to the platform."

**A4. Company not named in M1:** fabian-van-lancker. His M1 says "Spotted that your platform gives brokers…" and never names vers.diagnose, though the card says "vers.diagnose by name".

**A5. Referral M2 has no value line and opens on the call** (card referral lane: "a value line that continues their question, the call offer…"):
- claudia-stewart-duijndam-32109536 "A call could cover how…"
- diana-glenewinkel-317329179 "A call could show where…"
- claire-donohoe-fca-85394717 "A call could show how the step enters a review…"
- karsten-vogel-alh "A short call could show what…"
- tomasverhoeven "A call would let me show…"
- georgefox1 (partnership) "A call could show how the step arrives…"

**A6. Referral M1 central question is a routing question, not about the person's own work:**
- john-mccormack-b27ba76a "who would own the review of a step added after the health questions?" His M2 then asks for a pointer a second time.
- nicole-heidemeyer-a861a910a "In operations, who reviews a new step before it enters the application?"

### B. Factual accuracy, 4/5

- Clean:
  - Every number is from the approved list.
  - 3.5% is in M2 only, in allowed lanes, with "not a scale reading".
  - No client, price, pilot or trial term appears.
  - No other prospect, reinsurer or platform is named in another's copy. Own products appear only to their own teams (Magnum, MIRA, hr | QUIRC/ReFlex, AI Assistant/Velogica, ALLFINANZ, M&M Office).
  - No former employer that is an account is named.
  - Compliance line by lane is correct in all 130 pairs.
- Company fact not in the card:
  - remco-de-mol-392b5a6 M1 "On AOV acceptance, build is weighed beside the health answers". His question and M2 are also about NN AOV cases. The NN bullet covers ORV only.
- Implies a reinsurer position:
  - annamazerant "At Swiss Re, a remote build record is one such route for non-medical applications." (card: never imply an insurer or reinsurer uses FitXpress)
- Offers an asset the card does not list:
  - cosima-escher-b6786a208 M2 "A one-page design for one client would describe shadow mode…" (MSG-5: cold messages do not offer materials)
- Suspicion by implication (card: no message implies applicants misstate):
  - francesca-tamma-556a0225 "whether a photo step changes … how people fill in height and weight?"
  - carstengiese "build is whatever the applicant declares"
- Against the referral-trigger boundary:
  - jan-müller-nrw M2 "can feed an automated flow directly". The next sentence then says outputs stay away from the case.
- Speed claim misused (card: own plain sentence, only where speed is the point):
  - ginger-turner-b867284 "The record arrives under 45 seconds… A client evaluation can therefore run alongside a live journey" (speed does not imply this)
  - Speed is not the point for reinsurer client heads: thomas-trompetter-8326aa22a "Start small, with one client. The scan returns 80+ body measurements, under 45 seconds…" and upasdika, the same sentence
  - Speed joined to the API clause instead of standing alone: dan-lacurezeanu-857672b "FitXpress comes as a REST API … and returns its record under 45 seconds…" and michael-ewers-21973193 "…under 45 seconds from the photos to structured results, through a REST API or the SDKs."
- Mechanics or actor wrong:
  - teppert M1 "A build step would feed data you own." (Gen Re does not own the insurer's application data)
  - teppert M2 "The record would sit in a client's data next to 80+ body measurements" (the record contains them)
  - carina-betz-180b82106 M2 "without touching your current route" (a reinsurer has no application route)
  - dr-georg-bechler-799a1615a M2 "the BMI estimate" (BMI is calculated)
  - tomasverhoeven M2 "If AOV acceptance sits elsewhere" (his M1 and the Achmea facts are ORV)
- Profile mismatches for Vadim. These are list-side, so I did not score them against the writer:
  - laura-corrigan-78467483: headline "Business Lines, Head of New Business, GI Ireland" (general insurance), but the copy says "Head of New Business at Zurich Life Ireland, you run the point of sale where evidence is asked".
  - michael-ewers-21973193: headline "CTO bei Munich Re Markets GmbH", which is not the L&H unit. The question "How does an SDK step usually enter a web or mobile application journey?" is off-persona for him.
- Sourcing: not applicable (outbound).

### C. Brand & tone, 2/3

- "let" / "lets": the terminology guardrail says `let` → `allow`, but the gate passed both of these, which looks like a detector gap.
  - tomasverhoeven M2 "A call would let me show"
  - r3425 M1 "ALLFINANZ lets authorised underwriters build, test and publish rules"
- Presumed reaction (the agent's judgment ban 8; round 2 R10 fixed only Steven Wiseman's):
  - cormac-frawley-53932253 "you would see a body-photo step as a data processor question first"
  - caroline-doory-51770315 "suggests you know these journeys well"
  - ralf-woltmann-592970163 "you may see where a software estimate could add evidence"
  - erik-schwarz-588b15214 "That gives you a view on what advisers enter"
  - dr-georg-bechler-799a1615a "suggests a view on how data moves between steps"
  - finja-dumstorff-321383275 "you hold the link between a tariff and the application"
- Comma splices in easy outs, hard for second-language readers:
  - patricia-smith-b8747827 "Application analytics may sit with someone else, tell me who."
  - richard-l-6b832012 "…another team, tell me whose."
  - shay-browne-34a99a19 "…the better owner, point me there."
  - st%c3%a9phanie-haas-maret-4a822573 "…a separate maintainer, tell me who."
  - jennifer-coleman-761b6b5b "…may own this, tell me who."
  - redmond-murphy-87343727 "…may be the right place, tell me."
  - manuel-plisson-812978a "…another owner, point me there."
- Wrong or unidiomatic English:
  - marcel-beißer-b9b8b617b "Product development and actuarial work sit in one reference at Allianz Leben" ("Referat" translated as "reference")
  - jenny-mcdonnell-82a4a61b "with a pricing actuary past"
  - upasdika "Quick note on Europe from your Life/Health seat at Gen Re."
  - michael-ewers-21973193 "…to CTO at Munich Re Markets is a wide move."
  - ginger-turner-b867284 "Each applicant sends two photos from the application"
- Idioms (card: "no idioms"):
  - brian-o-malley-8a67a837 "has to earn its place"
  - susanne-buchholz-628198bb "familiar ground"
  - niall-walsh-447b5686 "on your desk"
  - "Grab a time / slot": elaine-morales-glynn-192896214, erik-guth%c3%b6rl-332347245, kelvingillen, tomasverhoeven
- Third-person address by title reads as a merge field:
  - carina-betz-180b82106 "Quick one for an Underwriting Manager, Life/Health at Gen Re in Cologne."
  - thomas-gei%c3%9fler-902a60157 "Quick thought for the Chief Underwriter at Munich Re Germany."
- Long sentence: dr-gabriele-teichmann-222665a M1, second sentence about 45 words (card: short sentences, one idea each).
- Unanswerable M1 questions. They ask about "the estimate's error" while 3.5% may only appear in M2:
  - Questions: dr-gabriele-teichmann-222665a, johnschoonbee, marnomiddelbos, simon-fallais-phd-b06a5323 ("beyond the estimate's own error")
  - Statements: claude-schwarz-55b61112 and charpentier-carole-84a43aa ("well above the estimate's error")

### D. Format & structure, 2/3

- **`Proof point:` headers are stale in about 39 per-person files.** They name a number the pair no longer carries, left over from round 2's R6 deletions. For example:
  - carl-christensen-66bba028 "80+ body measurements, under 45 seconds": neither is in the copy
  - andres-webersinke-2921085 "100+ clients": absent
  - charpentier-carole-84a43aa "112,100 scans": absent
  - Others: rainer-helfenstein-aab817135, mirjam-jonker-heidolph-42866877, ronan-scully-3953a57a, mark-cree-12207b26, annette-seitz-5b2baa146, sergio-lopez-jimenez-fia, adrien-givaudan-658600190, lucie-aubry-0b760630, marcel-beißer-b9b8b617b, steven-wiseman-9126719a, fabian-schmitt-748430154, christian-helmes-5537a994, siobhanbuckley, thomas-gei%c3%9fler-902a60157, st%c3%a9phanie-haas-maret-4a822573, christoph-henschel-a7961466, steven-hardy-1b8b261b, shay-browne-34a99a19, fouzia-boussetta-845a321, laura-corrigan-78467483, christopher-curran-3ab8b12, emiliegale, sebastian-strasser-bb5a238a, eoinlynam, finja-dumstorff-321383275, rwcastellini, volker-homola-ba2a49164, carstengiese, david-ibl, benjamin-brummer-b4ba6124a, jennifer-coleman-761b6b5b, christian-langenstra%c3%9f-826419379, laura-mongan-65b6b934, remco-de-mol-392b5a6, erik-schwarz-588b15214, brian-o-malley-8a67a837
- Summaries were not regenerated after the fix rounds:
  - `_summary-mixed-1.md` says "Openers, questions, easy-out targets and closers are distinct". The Swiss Re and Munich Re repeats under A2 contradict this.
  - `_summary-mixed-2.md` lanes sum to 31 for 30 people.
- Bare landing link on its own line with no sentence (card: "the sentence around it differs each time"): annette-seitz-5b2baa146, karsten-vogel-alh, caroline-doory-51770315, nicole-heidemeyer-a861a910a, christian-langenstra%c3%9f-826419379, annamazerant, carina-gervens-547a04279. In the first four, the link sits between the value line and the compliance line.
- M1 body paragraphs with 3 sentences (the agent's template allows at most 2): christoph-henschel-a7961466, roland-schneider-529b65b9, albansenn, michael-ewers-21973193, luisaljimenez, susanne-buchholz-628198bb, von-kielpinski, rolf-kulemann-61052443
- No `product:` frontmatter in the per-person files. I did not apply the hard D ≤ 1 rule: this is the known `split-messages` template gap, a system issue, as in the 2026-10-26 QC.

### E. Output quality, 3/4

- **Strong:**
  - Lane-to-persona fit.
  - Several hooks only a researcher who read the profile would write:
    - rolf-kulemann-61052443: his headline quote tied to hr | ReFlex
    - gabriela-heyne-86a182118: BIPRO against M&M Office
    - von-kielpinski: hr | QUIRC follow-up logic
    - holger-krebs-547b0865: e-Risiko in the advice meeting
    - klaus-strumberger-0699538: the 20 October redesign
  - Good questions:
    - manuel-plisson-812978a: automated rules or referral
    - darrendempsey: API call or data connector
    - francesca-tamma-556a0225: a behavioural-research angle, minus the B note
  - Good M2s:
    - steven-wiseman-9126719a: "suits one use: referral on a large difference"
    - roland-schneider-529b65b9: "only the weight estimate and BMI matter for build"
    - mirjam-jonker-heidolph-42866877: what she would see on the file
- **Cross-company twins.** Round 2 targeted these, but they survive. This part of the campaign fails the 60%-unique override:
  - Technical-integration M1 quartet: caroline-clinton-b8a45738, mathias-schniebs-a9a053297, koos-van-der-veen-9653a110, larskietzer. All four say "A photo step would/could [enter / connect / join] as an SDK in the web [journey/form] [or … API call]. It sends / starts from 2 photos and returns a Smart Scales weight estimate, a BMI from the declared height and a threshold flag, as one timestamped record." The gate's "call ask in Message 1?" note fires on these same four, plus darrendempsey.
  - Their CTA "A call to go / walk through the (REST) API (and SDKs):" also appears in darrendempsey and gabriela-heyne-86a182118 (6 in total).
  - Underwriting M2 first sentence, verbatim: thomas-lay-b3173484, sandrajohn and colette-houton-86233219, "A shadow evaluation would count flags per candidate threshold and compare them with build evidence collected separately." Near-identical: noel-finnegan-6b9694a and dana-rienh%c3%b6fer-28a064258 ("…show(s) agreement with build evidence collected separately"). These five share one M2 skeleton: shadow sentence / 3.5% / compliance / "[label]:" + landing / call / pointer.
  - Speed sentences:
    - karen-o-flaherty-qfa-sia-3b798555 and joe-charles-2049565 (two Dublin insurers): "The scan record is back under 45 seconds from the photos to structured results"
    - upasdika and thomas-trompetter-8326aa22a (two German reinsurer teams): "The scan returns 80+ body measurements, under 45 seconds from the photos to structured results." This is the agent prompt's example sentence word for word.
  - Easy out: claudia-stewart-duijndam-32109536 (Achmea) and rensengelen (NN), "Or point me to the owner of ORV acceptance."
  - M2 opener: dr-gabriele-teichmann-222665a and angelique-r-072a756, "For the guidance: Smart Scales has…"
  - M1 opener "Your headline pairs X with Y": marc-schanbacher-83b243170, mirjam-jonker-heidolph-42866877, ginger-turner-b867284. Ginger's headline does not say "L&H reinsurance systems".
- **Thin M2s**, mostly left by round 2's R6 deletions. One generic line, or one that does not continue the M1 question:
  - fouzia-boussetta-845a321: "The in-force view matters to the new-business side, which decides first where the step applies." This names another team and drops her in-force question.
  - carl-christensen-66bba028: "A first look could feed the record into rules in test mode for one client…"
  - charpentier-carole-84a43aa: "In test, you can see how often each candidate threshold flags before any rule changes."
  - volker-homola-ba2a49164: "With one client, shadow mode would set flag counts…"
  - jennifer-coleman-761b6b5b: "A design for one client evaluation is short:…"
- **Bolted-on 112,100 survived round 2.** Both M1s say "two photos" in words, so the R6 recipe applies: "2 photos" into M1, drop the line.
  - velina-peneva "…a clear first test. 112,100 scans in 2025 across all 3DLOOK customers."
  - redmond-murphy-87343727: the same line as its own paragraph
- **Easy out given to P1 buyers.** The card's easy out is "for people who are not the buyer".
  - Sharpest: andres-webersinke-2921085, the Global CUO, gets "If life guidelines sit with someone else, please point me there."
  - Others: thomas-lay-b3173484 ("A short no helps me too."), elsa-renouf-helfen-93a9283b, noel-finnegan-6b9694a, colette-houton-86233219, luisaljimenez, thomas-gei%c3%9fler-902a60157, sandrajohn, steven-hardy-1b8b261b, carl-christensen-66bba028, lauren-mccormack1, michael-vesey-1125772ab, carina-gervens-547a04279, antoine-moll-6373042
- **Echo questions** (the M1 says X, then asks about X): ginger-turner-b867284 "A new data source needs approval before it feeds them." / "How does a new data source get approved…", ianlong "a build-evidence field would need tracking…" / "Where would a build-evidence field live…", plus the two SCOR entries under A2.

## Top 3 issues (priority for improver)

1. **Same-company sameness, in the categories the card names:**
   - Hook frames: career-move at SCOR France, Zurich, Irish Life and Hannover Re; "Noticed" at a.s.r. and Gen Re; "You [verb] at Swiss Re"; "Note for the [title]".
   - M2 openers at Munich Re, NN, a.s.r., Swiss Re and Zurich.
   - CTA lines: "Calendar:" and "Call:" at Aviva, Alte Leipziger, MRAS, NN, SCOR and Irish Life.
   - Closers: "a pointer helps" and "tell me who".
   - About 60 entries under A2. The gate does not count hook frames or CTA lines.
2. **"What comes back" missing from 14 M1s** (A1), introduced by round 1's cut of shared scan runs. This includes three P1s (carl-christensen-66bba028, matthew-tinney-44598094, r3425) and four "flag/gap" M1s with no subject.
3. **Card wording as copy, now cross-company:** about 40 central questions keep the card's noun phrases (A3). There are verbatim twins across companies: the tech M1 quartet, the underwriting M2 trio, the medical and data-processor questions, and two speed sentences. The four Card-Use pastes are Carl, Keyvan, Fabian VL and Klaus.

## System notes (not scored against the agent)
- Round 2's R6 deleted M2 number sentences, but nothing reran the `Proof point:` headers or the summaries. A fix round should end by regenerating both, or the script should write them.
- Round 1's R2 forced shared scan runs out, and writers dropped content instead of rewording it. Round 3's rule should say "reword, do not drop: keep the weight estimate and the declared-weight gap".
- Gate gaps:
  - `let` / `lets` passed twice (tomasverhoeven, r3425).
  - The "call ask in Message 1?" false positives on "API call" are a usable fingerprint of the shared tech template.
  - A word-order-insensitive check on card question targets would catch the A3 list. This is the same recommendation as the 2026-10-26 QC.
- `notify.py` was not run: this QC session has no Bash. The coordinator should send:
  `QC: message-sequencer → 14/20 (marginal). Top issue: same-company repeats in hook frames, M2 openers and CTA lines (about 60 entries), and 14 M1s that lost "what comes back" in round 1. File: workspace/_quality/outbound/2026-11-02-message-sequencer-eu-insurance-underwriting.md`

## Coordinator review

```
agreement: ✅ agree. 14/20 is fair. My full read found the same three clusters, but I underrated hook frames and CTA lines because my scan counts word runs, not frames. A1 is my own round-1 rule: "vary the scan sentence" led writers to cut parts instead of rewording them.
top_issue: same-company sameness in frames the gate cannot count (hook frame, M2 opener, CTA label, closer) plus card question targets kept as the question; round 3 is built by script from sections A-E of this report.
```

Coordinator actions on the list-side notes (B): laura-corrigan-78467483 (GI Ireland, general insurance) and michael-ewers-21973193 (Munich Re Markets GmbH: savings, retirement and investment reinsurance) are FAIL on the business-line rule, standing decision 4. SEND is now 128, and both are named to Vadim at the checkpoint. System notes: the Proof point headers and summaries are refreshed in round 3, and the gate gaps (`let`, card question targets) are proposed to Vadim, not applied.

**After this QC (coordinator, 2026-11-02):** Round 3 was built by script from sections A-E of this report as `messages/_fix-r3-<batch>.md` (125 people) and sent to the same four writers. All four rewrote their batch in one pass. I then read all 256 messages myself, which led to round 4: the Munich Re / Swiss Re flag-sentence skeleton (6/14 and 13/16) and the stock easy outs ("I would gladly speak with them" ×3 at three companies, "welcome on the call instead"). I made 9 line edits myself. Verified mechanically, with no second QC:
- gate 0 hard;
- 0 identical questions campaign-wide, 0 card question phrases, 0 P1 easy outs, 0 same-company CTA, closer or M2-opener repeats;
- 0 stale Proof point headers;
- compliance line correct by lane, 3.5% only in M2 of the allowed lanes;
- no other account named, no Never term.

Open gate gaps, proposed to Vadim: "two photos" does not count as a number (the root of the bolted-on numbers); `let` is not detected; "diagnose" inside "vers.diagnose" hard-fails (Fabian Van Lancker's M1 says "your platform" for that reason); there is no check for card question targets.
