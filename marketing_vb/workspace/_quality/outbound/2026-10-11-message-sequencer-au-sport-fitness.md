---
qc_date: 2026-10-11
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-11-au-sport-fitness/messages/ (read in full: _batch-fernwood-fitness-1/-2, _batch-fitstop, _batch-jetts-fitness, _batch-bft, _batch-mixed-1..5, _batch-ubx, _batch-anytime-fitness-australia, each against its _profiles file; _check.json; _coordinator-scan-2026-10-11.txt; _summary-jetts-fitness, _summary-bft)
track: outbound
artifact_type: messages
total_score: 10/20
status: failed
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-11, au-sport-fitness

**Artifact:** `workspace/outbound/campaigns/2026-10-11-au-sport-fitness/messages/` (325 people, 650 messages, 12 batches)
**Total: 10/20, failed.**

**Verdict.** The M1 side mostly holds. Questions come from the topic banks and stay within quota at all four big brands. App rules hold (no "your app" at BFT, Anytime, Snap or JHT). Evolt, EGYM and scanners are never mentioned. Pool A and pool C are handled, and no claim is made about earlier threads. The main risk did happen, but on the M2 side:
- **BFT:** 10 of 20 referral M2s end on the same easy out ("…or a pointer to whoever owns/runs/looks after member experience at BFT"). 7 of them carry the same "[label]: the scan returns 80+ body measurements, under 45 seconds…" line. The gate logged 58 near-duplicate pairs inside BFT. The writer's `_summary-bft.md` calls this "stable by design".
- **Jetts:** about 22 of 27 referral M2s share one argument and no value line: "a (ten-minute) call to show the member's side of the scan on a phone, and you tell me if it fits [club]". The near-duplicate detector cannot see this because the wording changes; the structure does not.
- **KX, REVL, Genesis and UBX referral M2s** use the same short skeleton: "short call to show what a member sees + 100+ clients + pointer + one-line question".
- On top of that: about 20 M2s ask a unit owner to judge whether the scan fits their club (a pitch to a unit), three card notes leaked into copy, one Plus Fitness owner hears "Viva", and one pool-B person is addressed by the other employer's CEO title.

**Recommendation.** Regenerate the referral M2s for BFT and Jetts from a per-person grid that assigns each person a value line tied to their own M1 topic, an easy-out target and a closer form before writing. Line-fix everything else from the list below. Keep the M1s, except the ids listed.

**Scoring basis.** Scored against `card-messages.md` and the `_profiles-*.md` files. Limits, signature, bans, detector and completeness are taken from the gate as fact. The missing `product:` in the split per-person files comes from the script template and is not capped (same ruling as the 2026-10-07 report). notify.py was not run: this QC run had no shell tool.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 1 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence: 2/5
- **Per-brand variation (check 1).**
  - **Themes:** within quota at Fernwood (max 6/35), Jetts (5/27) and BFT (4/20). At Fitstop the "what has training changed" question runs 7/32: richard-hallam, paul-collins, kevin-kensley, kelly-wade, kendall-winslow, paul-emanuel, chandell-fretwell. That is slightly over the ~6 cap.
  - **Closers and M2 arguments:** fail at BFT and Jetts (see Verdict).
  - **Opener repeats inside one company:**
    - Fitstop: "Noticed you own a Fitstop." is word for word in bruce-mcconnel and brenna-dillon. "Wanted to reach out about Fitstop X" appears in chris-janke and josephine-tuah. Nine Fitstop M1s open with "Noticed".
    - BFT: the BF4 sentence is near-identical in kirsten-lea, zoe-clark, luan-scherman and st-leonards-body-fit-training.
    - Fernwood: "Noticed your background" ×3 (binish-mobeen, mary-papazoglou, cheryl-williams), "Quick note" ×3 (ric-caldwell, suzanne-herniman, moby-malik), "You run both" ×2 (melissa-mcglinn, tedy-ferreira).
- **Unit owners asked to judge fit for their own club** (franchise rule "never pitch a unit to adopt anything"):
  - Jetts: aaron-dearie, sarah-dwyer, jetts-gym-mount-hutton, sam-bhandari, mel-george, catherine-hanly.
  - Other brands: jason-clark (BFT), jamie-ward-smith (UBX), gym-genesis, brentonwilliamson (Genesis), rachel-macedo, benny-russell, marvin-mangubat (Vision).
  - Fernwood M2s that describe the club rolling it out: jessica-pupillo, steve-brookes, jessie-anderson, tedy-ferreira, guneet-cheema, melissa-jones.
- **Vadim's decisions (check 4):**
  - No Evolt, EGYM or scanner mention: holds.
  - Pool A greetings need no name: holds, though the style varies ("Hi there," vs "Hi Fernwood Tuggeranong team,").
  - Pool C easy out points to Australia: holds for marcello-jimenez, dinda-fauziah and kylie-kerr.
  - No first-introduction wording at the waived brands, and no FWD or Fernwood app: holds.
  - **Fails:**
    - mark-grey-014635154 M1 addresses him as CEO ("a CEO's view of Anytime Fitness Australia"). That title is at Collective Health and Wellness, and pool B copy must not assert an employer beyond the IN brand.
    - gh-undefined-218583350 M2 says "someone else at Viva", but Plus Fitness people never hear Viva.
    - BFT Hindmarsh: scott-bumpstead and steve-grace get different M1 questions but the same M2 ask (a pointer to member experience at BFT).
  - **Sweat (damien-mavroudis-9865154a):** the topic follows the card (strength programs) and there is no reference to Adam Koch or an earlier message. But the body is the standard product-lane CEO pitch: in-app, "white-label through an SDK", "at which point … would a scan fit". The only change from a CEO pitch is the noun.
- **Rules missed:**
  - arshad-hussein-14358a231 M1 never names Plus Fitness or Rockdale.
  - seanmolam (equ) is in the partnerships lane but got technical-lane content: the deletion line, "2-4 weeks" (which the card restricts to technical-integration) and the technical FAQ link in place of the partnership asset.
- **Before/after framing at women's brands:** the Fernwood challenge M2s of melissa-robinson, michelle-baker and moby-malik put a scan at the start and end of a challenge, side by side. The topic bank allows strength and confidence only. alex-fenton-mathews (STRONG) M1 does the same with an event.
- stacey-flentje M2 makes the scan the check before a class step-up, which drifts into decisioning.

### B. Factual accuracy: 3/5
- **No invented numbers or clients.** Every number is from the card: 80+, under 45 s, 112,100, 34,000, 100+, 2-4 weeks, 30 days, plus prospect dates.
- **Unsupported claims about the client base or about prospects:**
  - hayden-lambley-robinson: "100+ clients, mostly through the same SDK route"
  - mark-grey: "for most the first step was a single integration point"
  - liana-nio: "100+ clients on exactly this kind of member-facing capture". The 100+ figure covers both products, so this is a misattribution.
  - matknipe-3b382111: "Studio owners tell us time is the limit". This invents feedback.
  - katelyn-farmer: "34,000 scans … so the flow holds up at volume"
  - paul-brown-a4058616a: asserts that Marrickville clients "come back to a program that kept moving"
  - garry-mortlock: "It runs as a white-label page on the Mr Vitamins website". This reads as a live deployment.
  - chris-caldwell: "Every kind of fitness shows up differently in the body data"
- **Locked 112,100 line changed to "3DLOOK ran 112,100 scans"**, which moves the scans from customers to 3DLOOK: andrewbaildon, peter-reed, rebeccacarson2, sean-hodges, sarahbroadhottot, jeremy-saville.
- **Data handling (check 2):** no "tracks" anywhere, and no self-serve promise is stated outright. The gaps:
  - The "within 30 days" option loses "per the customer's policy" in joe-w, clint-sellen, seanmolam, angelo-konstantinou, davidnedved, ccarpinteri, ben-lister and brettcondron.
  - robmitchelllinkedin says "deleted within 30 days at most", which drops the immediate-deletion option.
  - "Records can be deleted by scan ID" and "stored and deletable by scan ID" (ccarpinteri, ben-lister, brettcondron, darrellnewing, davidnedved M2, angelo M2) drop "on the customer's request". This wording comes from the card's own lane note, so the card needs fixing too.
- **Placement:**
  - 8 technical-lane M1s carry the deletion line while their M2 already links the FAQ. This repeats the 2026-10-07 M1 defect, and in AU it is not a compliance default.
  - adriana-ampuero (a Fernwood referral) gets the deletion line plus "the integration detail" in M2. Neither belongs there.
- **Prospect data placed next to ours:**
  - simonjelliott (SiSU) M1 names the self-serve health checks and then "A member could **also** take…".
  - jaynevaiao: "sit beside the coach's own numbers".
- **Implied churn or poor measurement:**
  - The JT3 note bans implying members leave, yet jay-williams and david-upton do.
  - christy-vu and arshad-hussein say members "drift in and out".
  - kirsten-lea suggests coaches "note by eye".
  - jonpepper M1 says reviews "run a little differently from site to site".

### C. Brand & tone: 1/3
- **"so" introducing a benefit** (card word trap; the gate missed it): shaun-pickering, alissa-o-flaherty, katelyn-farmer, tj-groot, josh-muriwai, sam-merza, paul-brown, jonpepper, josephine-tuah, brooke-price, zaac-schembri.
- **Corrective negation or "rather than":**
  - damientampling: "a question about fit, not a pitch"
  - emily-crawford: "Rather than a pitch"
  - scanlan-karen: "Instead of a long pitch"
  - mel-george: "more useful than a pitch"
  - sienna-ettingshausen: "Not a buyer question, just…"
- **Presumed reaction as an M2 template** (about 30). Shapes like "Founders usually ask…", "Group trainers tend to like…", "You will know…":
  - mixed-5: nathan-james, simonjelliott, danielle-monroy, josh-muriwai, dainmoreton, sam-merza, ccarpinteri, ben-lister, nathan-robertson, dr-toby-ford
  - BFT: liana-nio, jason-clark, laura-carroll, steve-grace, anthonyhoangbft
  - Fitstop: bentoleafoa, paul-emanuel, mark-vaiao, rhianna-buchanan
  - elsewhere: jasondavidcormier, mitch-hannam, jamesduffy26, matt-eikenhout, lilian-fathallah, bianca-latorre, michelle-baker
- **Dangling "as [role]" openers that make Vadim the owner or director:** danny-pearson, matt-rees, damientampling, dan-bova, jon-davie, michael-nysten, steve-hobart, lauren-nash, emilene-lawrance, luke-skoric.
- **Card notes copied into copy** (prompt rule 11):
  - barry-mcdonald M2: "A scale reference, in its own sentence:"
  - zaac-schembri M2: "the 3D model is shown only where Virgin Active chooses"
  - michaeljordanubx M2: "Any comparison covers only scans the member picks:"
- **No banned words** (gate).

### D. Format & structure: 2/3
- The batch format matches the card, and the gate exited 0.
- `_summary-fernwood-fitness-2.md` is missing.
- dr-toby-ford is greeted as "Hi Dr Toby,".
- leah-libunao M2 opens "Thanks for reading." on a message that is only sent after silence.
- brendon-levenson M2 asks two questions plus a closing question.
- The split files carry no `product:` frontmatter. This is the script template and is not capped.

### E. Output quality: 2/4
- The M1s are mostly specific, with real hooks from bio and role and topic-bank questions.
- About 110 referral M2s (BFT, Jetts, KX, REVL, Genesis, UBX) carry no value line. They fail the outbound uniqueness override.
- **Product sentence repeated inside companies:**
  - Fernwood: "3DLOOK has worked with 100+ clients" ×13 and "The scan returns 80+ body measurements, under 45 seconds…" ×11.
  - REVL: "100+ clients" ×8.
  - KX: "100+ clients" ×6.
- **Call length (check 3).** 34 M2s name a length: 15 min ×17, ten min ×14, twenty min ×3. The card never asks for one.
  - The lengths are not consistent within one network: Fitstop has adam-stevens at ten minutes and sam-seaton at twenty.
  - At Jetts, "ten minutes" is part of the repeated M2 skeleton.
  - At Anytime, "15-minute call" ×7 is a repeated closer.
  - Verdict: a problem, though not a rule breach. Either drop the length or use one length campaign-wide, in no more than about a fifth of a company's M2s.

## Top 3 issues (priority for improver)

1. Referral M2 collapses into one skeleton per brand (BFT closer, Jetts argument, KX/REVL/Genesis/UBX "show what a member sees"). The prompt needs a pre-writing variation grid for M2, not only for M1, and the summary must not rationalise soft notes as "by design".
2. M2s ask unit owners to judge fit for their own club. The card's franchise rule must reach M2: the referral M2 value line must be about their members, not about adoption.
3. Judgment bans at scale: presumed-reaction M2 openers, "so"-benefit, dangling "as [role]" openers, and three leaks from card notes. Rule 11 and rule 8 of the prompt are not enforced by the gate, so the writer needs a self-check list.

## Coordinator review

agreement: ✅ agree (my own regex scan found the same call-length, deletion-in-M1 and repeated-proof-sentence defects; the M2 skeleton at BFT and Jetts is structural and invisible to the gate)
top_issue: referral M2s collapsed into one argument per brand at BFT (10 of 20 same easy out, 7 same product line) and Jetts (~22 of 27 "short call to show the member side, you tell me if it fits"): the 2026-10-06/10-07 failure moved from M1 to M2.
status: below 12, not shown to Vadim as a sample. On Vadim's instruction (2026-10-11, «після кволіті контролера все запиши, закоміть і запуш, я вже завтра продовжу») the fix round was NOT run today; the plan is in the campaign's STATUS.md.
