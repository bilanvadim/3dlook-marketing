---
qc_date: 2026-10-06
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/ (all 8 _batch-*.md read in full, 8 _summary-*.md, _check.json; baselines 2026-10-06-message-sequencer-uk-weight-management.md (11/20) and -r2.md (13/20))
track: outbound
artifact_type: messages
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report (round 3): message-sequencer, 2026-10-06, uk-weight-management

**Artifact:** `workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/` (223 people, 8 batches)
**Total: 15/20, good (r2: 13/20 marginal; baseline: 11/20 failed).**

**Verdict.** Approve after one targeted line pass on the person_ids below. No regeneration needed. Round 3 fixed every off-scan referral question, the Roczen-roadmap clones, the elliottsilver storage line and the unused card themes. Non-mandated near-duplicates are down from 48 to 1. What is left is the part of the round-3 rule the gate cannot see. Themes may repeat, but at LighterLife the question **structure** now repeats: 29 of about 65 referral M1s are "Who decides…" or "Who looks after…" about the client's online account. Across all four large pools the M2 closer has become one family: "[a role / title / team / name] is enough / plenty / all I need".

**Scoring basis.** Same as r2. Scored against `card-messages.md` and `_profiles-*.md`. Limits, signature, bans, detector and completeness come from the gate and are taken as fact. The missing `product:` in split files is not capped. The new rule comes from r2's coordinator_review: a theme may repeat, but wording, hook, structure and closer may not, and every question must ask who owns something a scan plugs into, tied to the person's role.

## Scores

| # | Category | Score | Max | r2 |
|---|----------|-------|-----|----|
| A | Adherence | 4 | 5 | 3 |
| B | Factual accuracy | 4 | 5 | 4 |
| C | Brand & tone | 2 | 3 | 2 |
| D | Format & structure | 2 | 3 | 2 |
| E | Output quality | 3 | 4 | 2 |

## r2 findings, item by item

**Fixed**
- Product-lane 15-minute ask: laura-newson (RH1:59), rebecca-ryan (RH1:197).
- juli-mey M2 no longer opens with the accuracy figure (ML1:113).
- jan-badger and georgina-walsh M2s no longer open "Thank you for reading" (LL1:97, :608).
- anjal / eltrent shared frame (ML1:475, :619). phebe "you will appreciate" and veronica-barry "you know people by name" are gone.
- pipyoung, shweta-sidana and roselle-herring 3-sentence paragraphs.
- sophie-edwards (ML1:41) and dr-george-sanders (ML1:17): the embellishment and the volume-as-evaluation framing are gone.
- grace-bajo and olivia-potter flattery.
- The "online programme owner" fallback for ann-mcclean, natalie-bellis and natalie-cowie.
- **LighterLife off-scan questions, all 20.** Every one is now about the online account or programme. "Separately" / "separate thing" appears 0 times.
- **Reset Health:**
  - "We build a guided two-photo scan" ×9 is gone.
  - The roadmap question ×11 is gone.
  - The card themes are now used for siri-steinmo, velawson, sean-patrick-mcgowan and dr-adam-barker.
- The finance / supplier route is now used for natalie-cowie (LL1:585) and lyn-obeney (LL2:70).
- The r2 shared-question pairs are all separated: alice-fletcher/benjamin-sabri, benjamin-sabri/dr-nik, louisa-flannery/emelia-judge, idalia/katrina, nicola-lyons/jaishri/louise-thackeray, stephen-young/natalie-shields, anne-matterface/lorraine-addyman, paul-anthony-brown/sharon-henshaw, veronica-barry/sally-harris and bev-robinson/helen-litherland.
- All five r2 exact closer pairs.
- elliottsilver storage line (mixed-1:82 now gives photo deletion only). chiaulingchow "chase by phone". alexnancekievill "engineer".
- The LL3 fact is no longer sent to sandra-undefined or samantha-ireland.
- emily-costelloe tricolon. donna-earle-swaby "keep your name out of it". The ann-mcclean, joanna-bhart and nikki-cook apologetic lines.
- laurensien third person (RH1:239).
- matthew-buckley "make sense" ×2.
- Identical sentences jessicaravenscroft/thomas-curtis and davidplans/imogen-bole.
- The head-office trio "100+ clients" sentence, and sonel-patel's M2 repeating her M1.
- Counterweight: veronica-wessels/zuheirah opener, mzwandile/warren M2s, bhavyanshi/katrina M1s.
- **MoreLife batch 2: all 11 off-list themes.** This covers grace-shiplee, amalia-kyriacou and beverley-ambler, the three risky ones. Batch 1's georgia-apsitis and julie-hearn are fixed too.
- The MoreLife CV-recitation opener and the 15 product-sentence pairs.

**Partly fixed**
- **erin-connors (mixed-1:149-151).** The inference from 34,000 is gone, but the replacement sentence is a new claim problem (see B).
- **Summaries.** They are more honest, but still wrong in places (see D).
- **Reset Health hook formula.** "[background] raises a question" survives in dr-sarah-oldfield RH1:327 ("frames this question") and dr-claudia-ashton :351 ("raised one question"). It has been replaced by two new formulas (see E).
- **sharon-henshaw (LL1:521):** "Your hospital background suggests familiarity with how evidence gets weighed". This is the same presumption in new words.
- **nicola-gornall (LL2:377):** "courses have been your field".
- **LighterLife M2 skeleton.** "Which role/team at LighterLife…" is gone, but a "[reframe marker]: [same question]" M2 has replaced it (see E).
- **Gate near-duplicates.** 48 non-mandated pairs are down to 1: tristandummer RH1:621 / imogen-bole RH2:87. Neither RH summary reports it.

**Not fixed**
- "so" introducing a benefit, a card:141 word trap the detector misses:
  - emily-costelloe ML1:127
  - keisha-c ML1:171
  - angelina-spathopoulou ML1:337
- anne-marie-tinto, "careful checking" and "Careful people start small" (LL2:248, :258).
- jackie-cook tour-manager analogy (LL2:195).
- nazila-bahrami, "Couldn't help but ask someone BANT registered." (CW:91).
- justin-slabbert CW:17 and annabellhiggs CW:63 still share "112,100 scans were run in 2025 across all 3DLOOK customers." word for word.
- annabellhiggs CW:53 and elliot-mcewan CW:193 both still open "Wanted to reach out".
- dr-faye-bentley still says "adults only" in two consecutive sentences (ML2:279, :281).

## The four claims the coordinator asked about

1. **erin-connors M2, mixed-1:151, "the support team opens a timestamped record only for scans it selects". Change it.**
   - The card's sentence is "the team compares the scans it selects" (card:61, :139).
   - "Opens a record only for scans it selects" reads as if a record exists only for selected scans. In fact every scan's measurements and 3D model are stored indefinitely by default (CLAUDE.md §12).
   - "Only" also implies an access limit the product does not enforce.
   - This is the same family as r2's elliottsilver storage line, but milder.
   - Fix: use the card sentence verbatim.
2. **ann-mcclean M1, LL1:237, "When something new is tried with a small set of LighterLife clients online, who arranges it?" Change it.**
   - It is not a direct adoption ask. But she is a unit owner, and "a small set of LighterLife clients" includes her own clients, so it invites "try it with mine".
   - A pilot process is not something a scan plugs into, so it fails the round-3 rule. The writer's own grid calls it "who arranges a small client trial".
   - Her M2 (:245, client requests about the online account) is fine.
   - **Same problem, stronger: anne-marie-tinto M2, LL2:258.** "Careful people start small: a guided scan in a web page for a few clients first. Who would sponsor that?" She is a LighterLife Mentor in Scarborough, so this is a pilot proposal to a unit.
3. **lyn-obeney supplier route (LL2:68-78): OK.**
   - It follows the card's assigned theme (card:103), fits an accounts role and points at the client's online account.
   - There is no LL3 and no "part I know least about".
   - "Accounts at LighterLife UK Limited sees how suppliers join the company" is a light presumption that fits her title. No change needed.
4. **natalie-cowie, "which role takes the proposal to the Board" (LL1:585): acceptable.**
   - It is grounded in her bio ("partnering with Boards") and is on the card's finance route.
   - Two small points:
     - Escalating to the Board overstates the size of a white-label scan decision.
     - Her M2 (:591, "owns a business case for an addition to the client account") is the better question and could lead M1.
   - "point to a long view of the business" (:583) is mild flattery. Not a blocker.

Also from round 3: sonel-patel's "small trial" (LL2:32, :40) is a pilot ask to the head-office Head of Programme Online. That is legitimate in her lane, and it states no trial terms (card:143). Low risk.

## New in round 3 (specific)

### A. Adherence: 4/5
- **Round-3 rule, structure and closer clauses: not met in the three large pools.** Details and pairs are under E. The summaries say the opposite:
  - `_summary-lighterlife-1`:7 says "wording, hook, structure and closer do not [repeat]".
  - `_summary-reset-health-1`:13 says "wording and closer all different".
  - `_summary-morelife-1`:12 says "wording, hooks, closers and M2 openers unique".
- **LighterLife unit / territory mentions.** The LL2 writer note says "Never mention units, territories", and card:132 adds "never mention franchise terms":
  - christine-smith LL2:358, "You ran LighterLife Shipley before becoming a consultant."
  - sandra-undefined LL2:123, "Your headline carries your own name on LighterLife Aberdeen and Shire".
  - carol-graves LL1:305, "now your own company within LighterLife"
  - bridget-egglesfield LL1:566, "in both an owner role and a hands-on one"
- **Pilot asks to unit people:** ann-mcclean LL1:237 and anne-marie-tinto LL2:258 (above).
- **Questions not about something a scan plugs into:**
  - natalie-bellis M2 LL1:538, "which team answers it" (client support)
  - bridget-egglesfield LL1:568, "Who helps clients when an online step needs a hand?" (help desk)
  - kelly-saunders M2 LL1:262, "who structures an online session from start to finish?"
  - marion-holder M2 LL2:438, "one team… or of several?" (probes the org chart)
- **raquelsanchezwindt (clinical lane)** has no 15-minute ask in either message (RH2:11, :19). The card's clinical recipe ends "then a 15-minute ask".
- LighterLife rules otherwise hold:
  - "app" appears 0 times in LighterLife copy.
  - No message mentions other units, owners or counsellors.
  - No message suggests head office knows about it.
  - LL3 is used only for head-office people (tina-horsnell).

### B. Factual accuracy: 4/5
- erin-connors mixed-1:151 (above).
- **New unverified claims about LighterLife's systems.** Card:56 says "nothing … verified, describe the capability":
  - julie-johnson LL1:142, "the client account has grown in layers". This is also a negative observation (card:123).
  - joanna-bhart LL1:106, "Clients reach a LighterLife group session through a web page".
  - heather-pearle-van-pelz LL2:481, "lighterlife.com is where clients sign in for them".
  - karen-burr LL1:182 and :188 presume a "session leader's view" of client accounts. That edges toward the Mentor monitoring that card:51 keeps out.
  - kim-stares LL2:178 assumes her QA team tests web features.
- **Overclaims about the person:**
  - samantha-ireland LL2:411, "you now shape strategy for LighterLife". Her own summary (`_summary-lighterlife-2`:49) says no head-office role is established.
  - margaret-campbell LL1:51, "when a client is on their own with the programme". Sent to a Counsellor, it implies a support gap (card:123).
- **ML2 fact drift:** dr-george-sanders ML1:7, "research roots going back to 1999". ML2 says origins in research, with programmes since 1999.
- Sourcing holds:
  - Every number is in proof-points.md.
  - No client is named and there is no verification framing.
  - The PronoKal UK body-composition rule (mixed-1:395) holds, and so does the BL1 health-MOT boundary (:440).
  - Pharmacy2U appears only with RH2 (RH1:31).

### C. Brand & tone: 2/3
- **"so"-benefit ×3, not fixed:** ML1:127, :171, :337.
- **Presumption openers, new in round 3:**
  - cherie-trutwein ML1:635, "suggests you see how people first meet a programme"
  - angelina-spathopoulou ML1:329, "gives you a practical eye for tools"
  - elaine-wright LL2:515, "An office manager sees which tools earn their place"
  - victoria-simpson ML2:92, "means you see what adults meet on screen"
  - m-ghezal ML2:58, "Evidence comes first for someone with research assistant experience"
  - catherine-webb RH1:691, "suggests a good view of how services run"
- **Hollow hooks.** These say "a move/path I wanted to ask about", then never ask about it:
  - peteryeekk RH1:601
  - tiago-grohmann RH1:673
  - amanmohammad RH1:637 ("worth asking about")
- **Non-sequitur "so I will be direct/short":**
  - sandra-undefined LL2:123
  - veronica-wessels CW:125
  - lauren-dolphin RH2:275 ("so I will keep this short")
- **naomibrosnahan CW:30** addresses the CEO in the third person: "Counterweight's CEO is a registered dietitian with a PhD". This is the class of laurensien's r2 issue.
- **Nagging M2 tags:**
  - "Last try:" (lauren-dolphin RH2:285)
  - "Asking again, briefly:" (dawn-sheppard LL1:451)
  - "Plain question once more:" (sally-harris LL1:625)
  - "One line, since I have asked a lot already" (maxine-phillips-smith LL1:296)
  - "Sorry to add to your inbox." (chad-haefele ML1:445)
- **Small lapses:**
  - davinaa RH2:199, "that is your headline"
  - joanna-bhart LL1:110, "A first name is all I seek."
  - dianne-bishop LL2:455 repeats "Dianne," right after the greeting.
  - areesha-r ML1:601, "In a trial, a scan means two phone photos…", which does not parse.
  - philip-bazire mixed-1:395, "The doctor… compares the scans it selects"

### D. Format & structure: 2/3
- **3-sentence paragraphs (new):** veronica-wessels CW:125, erin-connors mixed-1:141.
- **Summaries misreport:**
  - `_summary-reset-health-1`:8-10 says the only near-duplicate is the GDPR line and "Nothing else left". The gate still lists tristandummer / imogen-bole, and `_summary-reset-health-2` omits it too.
  - `_summary-morelife-2`:10 says "morelife-1 still has older near-duplicate product sentences". That contradicts the gate (0) and `_summary-morelife-1`:13.
  - The uniqueness claims are listed under A.
- **Stale proof metadata.** The proof lines for elliottsilver (mixed-1:68), napala (:91), rebecca-tessier (:114) and erin-connors (:135) say "compliance line verbatim", but none of those M2s carries it.
- **M2s with no ask, which read as orphans:**
  - paulinehills LL2:540, "If it is a department, that works too."
  - maxwell-leary ML2:304, "Happy with just a team name."
  - sohnia-akram ML2:372, "A role is enough, thank you."
  - prestonsarah ML2:219
- dr-faye-bentley "adults only" ×2 (carried over).

### E. Output quality: 3/4
The senior, clinical, technical, partnership and Habitual/Medicspot/PronoKal copy is good. barbara-mcgowan, davidplans, thomas-godec, alasdair-yorke, joanna-bruce-mbe and kate-sykes could all be kept as reference examples. Every referral question is now on-scan and tied to the person's role. The remaining weakness is template shape, not content.

- **LighterLife question stems.**
  - "Who decides…" opens the central question in 18 M1s: LL1 :182, :322, :426; LL2 :89, :125, :144, :197, :250, :269, :305, :360, :379, :394, :413, :483, :515, :532, :587.
  - "Who (at LighterLife) looks after…" opens it in 11 more: LL1 :108, :218, :392, :462; LL2 :51, :163, :286, :322, :432, :500, :551.
  - In LL2 that is 22 of 31 referral M1s.
  - Tightest twins:
    - liz-hayward LL2:229 / lee-godwin LL2:464. Both are customer service advisors at head office, and they share hook and question: "Customer service hears what clients wish the web account did. Suppose a client asked…" vs "Customer service advisors hear what clients want from their online account. Should a client ask…". Highest priority.
    - judyhoskins LL2:144 / carole-brand :394 / amanda-walton :305: "Who decides what a client can [do / add] [in their online account / online]".
    - nikki-cook LL2:89 / dianne-bishop :449 / veronica-barry M2 LL1:555: "what clients [are asked to] bring to the session/group".
    - siobhan-barron LL2:286 / jennifer-bell :500: "Who looks after how … clients … their journey".
    - M2s lorraine-kessock-philip LL2:59 / amanda-walton :313 / jennifer-bell :506: "between-session side / online side between groups / home side of the online programme".
    - M2s carole-brand LL2:402 / deborah-rice :593: question and closer twin, "new features… A team is a fine answer" vs "sets the features… A team is fine".
    - Openers margaret-campbell LL1:51 / amanda-walton LL2:303: "the days between sessions".
    - "earn their/a place": elaine-wright LL2:515 / samantha-ireland :413.
- **Same M2 skeleton across the referral lane:** "[reframe marker]: [M1 question restated]". About 20 of 34 LL1 M2s use it, for example "Another way in:", "Put another way:", "Reframing:", "Shorter:", "Easy version:", "Plainly:", "Narrowing it down:" and "Different wording, same point:". Reset Health and MoreLife have the same pattern (siri-steinmo RH1:407, tristandummer :627, sean-patrick-mcgowan :571, richard-ruff ML1:679).
- **Closer family. Exact or near repeats inside one company:**
  - Reset Health: jasoncya RH2:76 / charlotte-williams :152, "A role title is enough." (exact). Seven of 14 RH2 M2s end "[role / title / team] is enough / plenty".
  - Counterweight:
    - idalia-stach CW:82 / zuheirah-toffar :320, "I will take it from there." (exact).
    - "…is all I need" in bjorn-ronaasen :116, mayuri-bhagat :252 and katrina-campbell-wareham :303.
    - "…is plenty" in bhavyanshi-chaudhary :235 and nuhaa-van-der-ross :354.
  - LighterLife:
    - judy-monk LL2:326 / susan-murray LL2:169, "Thank you for reading." (exact).
    - karen-burr LL1:190 / veronica-barry :557, "I will write / send that team a short note."
    - ali-robbins LL1:504 / bridget-egglesfield :574 / christine-smith LL2:362, "…is plenty".
    - john-moore LL1:34 / louise-platt LL2:349, "Even half an answer / a rough idea helps."
  - Medicspot (6 people): rajan-mistry mixed-1:291 "A name is plenty." / laura-r :331 "A name or a team is plenty." / rob-farrow :257 "A name is all I need."
  - MoreLife: dr-faye-bentley ML2:287 "A role is plenty." / sohnia-akram :372 "A role is enough, thank you." / victoria-simpson :100 "A role would do."
- **Reset Health hooks:**
  - RH2 opens 12 of 14 referral M1s with a CV list: "[employer A], [employer B], now Reset Health…".
  - emelia-judge RH2:123 / benjamin-sabri :237 are twins: "…: three [different] settings".
  - RH1 has its own formula, "[A] to [B]: a path I wanted to ask about" (above).
- **Reset Health central questions:**
  - Malaysia pool: "Which London team…" ×5, in peteryeekk RH1:601, kelly-m :655, jasoncya RH2:66, davinaa :199 and sharon-priya :218.
  - peteryeekk / kelly-m are a twin pair: "London team that scopes new… features" / "which London team scopes it", plus M2 :609 / :663. Kelly runs the Malaysia business, so the two will compare.
  - "Which clinical lead…" ×3: charlotte-williams RH2:142, george-hamlyn-williams :161, dr-nik RH1:709.
  - tiago-grohmann RH1:673 / shweta-sidana RH2:47: "who decides what [information] a [clinician / mentor] sees before a [check-in / session]".
  - "…Thank you." tails five times in referral M2s: velawson :427, kelly-m :663, catherine-webb :699, dr-nik :717, alexandra-gyurkó :735.
- **MoreLife:**
  - "Who owns programme design for adult[s / services]…" in beverley-ambler ML2:128, daniella-hall :111, maxwell-leary :298 and stephen-young :196. M2s beverley :134 / dr-faye-bentley :287 / stephen-young :202 repeat it as well.
  - "holds the pen": traceyhorowitz ML2:168 / dr-faye-bentley :281.
  - Client-services hooks: meena-yates ML2:7 / jaishri-patel :245 / eltrent-summers ML1:617, "[questions] probably reach / tell client services first".
  - Lifestyle-leader openers: louise-thackeray ML2:330 / sohnia-akram :364.
  - Pilots vs trials: phoebeorango ML1:547/:553 / areesha-r :601/:607.
  - Between-session steps: anjal ML1:481 / emily-saunders :517.
  - App onboarding: cherie-trutwein ML1:637 / julie-hearn :565.
  - "additions to the adult app": anthony-hardley ML1:259 / nadine-heywood :319 / chad-haefele :439.
  - Pilot asks to two service managers, peers under card:106: matthew-buckley ML1:195 / georgia-miller :151.
- **Counterweight:**
  - bjorn-ronaasen CW:108 / kelsey-kolbee :261 share the CW2 sentence and "I am trying to [reach / find] [whoever / who] at the UK head office … for it".
  - About 10 of the 11 South Africa M1s follow one skeleton: "[title hook]. [CW fact], and I am trying to find / would like to find who at the UK head office owns X."
  - "…is why I am writing": olga-wojadzis :159 / hannahpaigeguthrie :278.

## Per-company mail-merge risk
- **LighterLife: MEDIUM (r2: MEDIUM, different cause).** No verbatim clones and no off-scan asks remain. Two question stems, one M2 skeleton and one closer family carry about half the pool. Owners who compare notes will see variations of one template.
- **Reset Health: MEDIUM (r2: HIGH in the referral pool).** The roadmap and "We build" clones are gone. Left: the RH2 CV hook ×12, "Which London team" ×5 in a 7-person Malaysia pool, and the peteryeekk/kelly-m twin.
- **MoreLife: LOW-MEDIUM (r2: MEDIUM).** The programme-design stem ×4, the client-services hooks and the two pilot pairs.
- **Counterweight: LOW-MEDIUM (unchanged).** The South Africa skeleton, plus two r2 leftovers (112,100 sentence, "Wanted to reach out").

## Top 3 issues (priority for improver)

1. **Claims and LighterLife rules, fix first:**
   - erin-connors mixed-1:151: use the card sentence.
   - ann-mcclean LL1:237 and anne-marie-tinto LL2:258: replace the pilot asks with an account/programme owner question, and drop "careful" (:248).
   - Drop the unit/territory mentions: christine-smith LL2:358, sandra-undefined :123, carol-graves LL1:305, bridget-egglesfield :566.
   - Drop the unverified system claims: julie-johnson LL1:142, joanna-bhart :106, heather-pearle-van-pelz LL2:481, karen-burr LL1:182/:188.
   - samantha-ireland LL2:411: remove the strategy overclaim.
2. **Break the twins named under E,** starting with the peers who sit together:
   - liz-hayward / lee-godwin
   - peteryeekk / kelly-m
   - carole-brand / deborah-rice
   - meena-yates / jaishri-patel
   - louise-thackeray / sohnia-akram
   - matthew-buckley / georgia-miller
   - beverley-ambler / daniella-hall / maxwell-leary / stephen-young
   - bjorn-ronaasen / kelsey-kolbee
   - jasoncya / charlotte-williams
   - idalia-stach / zuheirah-toffar
   - judy-monk / susan-murray
   - justin-slabbert / annabellhiggs (112,100)
   - annabellhiggs / elliot-mcewan ("Wanted to reach out")
   - tristandummer / imogen-bole (gate)

   Then vary the "Who decides / Who looks after" stem in at least half of the LighterLife M1s. Replace the "[X] is enough / plenty" closer in referral M2s with a closer that differs inside each company.
3. **Cleanup:**
   - "so"-benefit ×3 (ML1:127, :171, :337)
   - nazila-bahrami CW:91
   - jackie-cook LL2:195
   - naomibrosnahan CW:30, third person
   - dr-faye-bentley ML2:279/:281
   - 3-sentence paragraphs: veronica-wessels CW:125, erin-connors mixed-1:141
   - Content-free M2s: paulinehills, maxwell-leary, sohnia-akram, prestonsarah
   - raquelsanchezwindt 15-minute ask
   - Correct the RH and ML2 summaries and the stale "compliance line" proof fields in mixed-1.

**System notes (not the agent's fault):**
- The near-duplicate check works at sentence level, so it cannot see stems ("Who decides what a client can…") or short closers ("A role title is enough."). A per-company check would catch what this round left:
  - an n-gram check on the first 6 words of each M1 question
  - a check on the last sentence of each M2
- card:104 lists "new service bids" as a MoreLife theme, while card:127 bans mentioning commissioners' tenders. annaalla (ML1:403, :409) follows card:104. Settle which rule wins.
- The juli-mey "pricing word" note is a false positive on "tier" (ML1:103). Confirmed.
- The gate counts in the brief check out: 0 hard, 168 no-calendar, 4 GDPR pairs, 1 real near-duplicate pair and 1 false pricing note.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: what is left is line-level: erin-connors "only for scans it selects" (storage misread), trial/sponsor asks to unit owners (ann-mcclean, anne-marie-tinto), named units and unverified claims about LighterLife's systems, samantha-ireland's unestablished strategy role, plus question stems and a closer family that repeat inside each pool. One targeted line pass sent to the same message-sequencers (cross-batch pairs pinned to one batch), verified by the gate and by grep on the named lines, no fourth QC. Card conflict card:104 "new service bids" vs card:127 tenders ban: the ban wins for this campaign (conservative default), raised with Vadim.
```
