---
qc_date: 2026-10-21
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/messages/
track: outbound
artifact_type: messages
total_score: 15/20
status: good
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Same-company collisions and cross-company lane templates plus value-less M2s; fix round 1 regenerates every M2 from per-person grids with per-batch fix files (_fix-1-*.md); card generator still appends the banned 2-4 weeks line (system gap)"
---

# QC Report — message-sequencer — 2026-10-21

**Artifact:** `workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/messages/` (4 batches, 92 people in scope; Circle Health's 2 people excluded)
**Round 1 total: 10/20** — failed. Re-score after three fix rounds: **15/20 — good** (see the last section).

Scored against `card-messages.md` and the `_profiles-*.md` files. The coordinator's list (verbless fact fragments, standalone "100+ clients" ×21, stock closers ×21, "15 minutes" ×~25, ", so" ×1, Nicolas Haffner's employer) is **counted in** and not repeated below. Everything below is on top of that list.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 1 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 2/5
Four explicit card rules are broken many times, not once:
- **"No two people at one company share an opener, a central question, a closing ask or a product sentence"** (card, Rules for steps 3-5; repeated at the top of every profiles file). About 25 same-company collisions, listed per batch below.
- **"Lane notes … never copy" / "Account facts … never copied word for word"**: lane wording appears verbatim in about 30 messages ("nothing to ship, stock or install" ×11, "standardized, timestamped body record … for the team to review" in all 12 clinical people, "a partner capability … has a place in what they offer" ×2). Account facts are copied word for word in 9.
- **Campaign rule "technical-integration: … No integration-time figure"** (and "No integration time … figures"): "a basic integration typically takes 2-4 weeks" in 4 M2s. The card contradicts itself here (its proof-points block offers the 2-4 weeks line), but the card says the campaign rules decide. See Coordinator notes.
- **M1 template "never reuse the same hook in a batch"**: mixed-2 uses "Noticed your background" ×7, "Came across your work" ×5, "Quick thought" ×4, "Got me thinking" ×3, "Quick note" ×3.
- **Easy out "for people who are not the buyer"**: given to CEOs, founders and owners (mixed-3 ×4, plus magdalena-winnicka, leo-glauberman, lea-paradzik).
- **M2 template: "one or two sentences of concrete value … This is the core of the message."** About 15 M2s have no value line at all: a label, a number, the GDPR line and a closer.

### B. Factual accuracy — 3/5
- All numbers come from proof-points, no client is named, the repeatability sentence is verbatim everywhere, and the compliance lines match their lanes. That keeps B above 2.
- `vinsensius-vega`, `sroze`, `arian-vassili`, `simon-lindgren-269102a4` M2: "2-4 weeks". The number is in proof-points but this campaign bans it.
- `ionhaab` M2: "Founder to founder". Olena is not a founder, so this is false about the sender.
- `leonhardfriedrich18` M1: "with an MSc in digital health". The profile says "studying Msc Digital Health".
- Assets the card does not confirm: `serge-weydert` "the Aeon app" ×2 (the card says customer portal), `svenjaeschke` and `vinsensius-vega` "the Ahead app" (card: online health report), `tangsergio` "the Axo Longevity app" (card: member platform), `andrea-grandits-42782b101` "the Mavie Work app".
- Details attached to the anonymised 34,000-scan platform with no source: `nlenten` ("run in the member's own app or through a web link"), `onnohuyghe` ("each member using their own phone inside the programme's app").
- `natalia-trpchevska`: offers "body composition estimates" to AYUN, whose on-site body composition analysis is on the card's Never list. This comes close to the second-device framing.
- Sourcing: not applicable (outbound).

### C. Brand & tone — 1/3
- Triple parallelisms (the M1/M2 template bans them): `pauline-sauvaget` and `alice-conques` ("needs nothing to ship or install, runs the same way on any phone, and returns…", the same sentence at two companies), `joelgrajcer` ("tests, explains and coaches"), `svenjaeschke` ("a baseline, a plan and referrals"), `victoria-sobulska-b5b7a0167` ("takes two photos, returns 80+ … and is white-label"). The lane-note triple "ship, stock or install" adds 6 more.
- Fragment openers that a second-language reader stumbles on: "Got me thinking, your line about…" (`svenjaeschke`, `khadija-benmansour-2535b7a8`, `fabio-benevolo-399b832`), "Made me think, your From Science To People line" (`michal-pohludka-56223939`), "Noticed your background, from…" (7 in mixed-2).
- The speed phrase is tacked onto the end of the product sentence as a dangling clause, "returns 80+ body measurements, under 45 seconds from the photos to structured results", which reads as if the measurements take under 45 seconds. This happens in 21 messages: `lukas-mayrl-7093029b`, `lea-paradzik` (M2), `serge-weydert`, `ionhaab`, `maximeberthelot`, `jürgen-mehrtens-116303b1`, `alexandre-hollard`, `dennishermann`, `andrew-mccarthy-impact-entrepreneur`, `peterpaul-deleeuw`, `kate%c5%99ina-vrbov%c3%a1-22bb7620a`, `khadija-benmansour-2535b7a8`, `joanna-bensz-205b315`, `magdalena-winnicka-b08972313`, `massimo-pietracaprina-a528951`, `oliks`, `gemmafrenchman`, `hannah-whitcombe-b2b35866`, `peter-roland-737ab34`, `bruno-marco-dufort-224358162`, `eddy-van-b323a9a`.
- Stock M2 lead-ins beyond the coordinator's 3 "For scale:": an "offer" label opens 11 M2s in mixed-2 alone ("A short offer:", "Plain offer:", "My offer is short.", "Here is the offer:", "Offer in one line:"…, ids in mixed-2 below); "Some scale for context:" ×2, "Scale for context:", "For a founder, scale matters:", "For growth work, scale helps.", "Numbers help a decision like this."; "For a [role], repeatability matters." ×3.

### D. Format & structure — 2/3
- `_summary-mixed-1.md`: the lane counts are wrong. It says product 12 and technical 6; the actual numbers are 13 and 5.
- `_summary-mixed-2.md`: the lane counts are wrong (product 19, technical 5, clinical 5; actual 21 / 4 / 4), and the line ends in an unfinished "… see grid".
- mixed-3: in 6 M2s the GDPR line comes after the calendar link (`bruno-marco-dufort-224358162`, `marioaichlseder`, `vinzenzweber`, `elisabetta-tata-reggio-07b31847`, `haif-rood`, `guentherpatterer`). It also drops ", with a DPA that includes SCCs": that is the §2 sentence, not the §9 UK/EU line the card names, so it differs from the other three batches.
- Hard rule "no `product:` frontmatter → D ≤ 1" **not applied**. The per-person files come from `outbound_pack.py split-messages`, and the batch format is set by the card. That is a system gap, not something the agent chose (see Coordinator notes).

### E. Output quality — 2/4
- The rubric's 60% uniqueness check fails for whole lanes, across companies:
  - Clinical: all 12 clinical people use one M1 sentence. Of those, `leanne-verdonck-a643b474`, `kevin-najafi-685254303` and `dariusz-soldacki-md-phd-a178b819` have about 90% identical M2s ("The team chooses which scans to … / repeatability / not a medical device / Open to a call?"). `puntschuh`, `roman-walser-154512255`, `jkhennigs` and `pr-jerome-salomon` share both an M1 and an M2 template.
  - Technical: `vinsensius-vega`, `arian-vassili` and `simon-lindgren-269102a4` have the same first two M1 sentences word for word; `sroze` shares the first. The "web, native, or both?" question appears 3 times.
  - Partnership: `alejandragimenezg` and `ash-patel-20647b161` have the same M1 and M2 except for the company fact.
  - Founder/CEO product M2 ("[For X], FitXpress is white-label through API or SDKs… 100+ clients. GDPR. Open to a short call?"): `seithe`, `ertanwittwer`, `maximeberthelot`, `jürgen-mehrtens-116303b1`, `alexandre-hollard`, plus `peterpaul-deleeuw` and `svenjaeschke`.
  - Empty profiles: `magdalena-winnicka-b08972313` and `leo-glauberman-56657316` are mirror copies.
  - Operations: the central question "what do members ask between check-ins" appears 7 times (`pierre-gimat`, `janlukasschmitz`, `dimitri-vogel`, `alice-conques`, `peter-roland-737ab34`, `hannah-whitcombe-b2b35866`, `kate%c5%99ina-vrbov%c3%a1-22bb7620a`).
- The GDPR line (about 150 of 550 characters) sits in about 65 M2s. The rule says "at most one", so it is optional. Combined with no value line, it makes the M2s read as boilerplate.
- The best pairs (`vinzenzweber`, `evakuttichova`, `bdebever`, `julien-montier`, `pauldupuy89`, `cezarneaga`, and the `alexandre-hollard` M1) show what the persona fit should look like.

---

## Findings per batch (for the fix round)

### mavie-work (17)
- `janine-wagenlechner` M1 and `doris-busek-baum-7606b4131` M1: same product sentence at one company ("nothing to ship, stock or install", lane note copied, a triple).
- `janine-wagenlechner`: the M1 hook "Couldn't help but ask," is not followed by a question. The M2 says "Teams run the guided sequence" (members run it, and the wording is lane copy). The M2 has no value line.
- `christophbodenstein` M1 and `johanna-resch-connect` M1: same product sentence at Mavie Next (web link, no app build, 80+).
- `drmeghabhola` M2 and `johanna-resch-connect` M2: same construction at Mavie Next ("If a … needs a body record step").
- `ondrejgandel` M2 and `victoria-sobulska-b5b7a0167` M2: same central argument ("ready part").
- `ondrejgandel` M1 and `vera-brockherde-9a8240126` M1: same product sentence ("a scan … a member app can ask for", lane copy).
- `lukas-mayrl-7093029b` M1 and `vedran-bijelac-00472714a` M1: same central question (what decides a new feature or element joining the Mavie offer).
- Openers at one company: 8 of 17 are "you went from X to Y" career recaps (`lukas-mayrl-7093029b`, `ondrejgandel`, `lea-paradzik`, `drmeghabhola`, `christophbodenstein`, `victoria-sobulska-b5b7a0167`, `johanna-resch-connect`, `doris-busek-baum-7606b4131`).
- `jasmin-cohen2`: the hook (#ThereIsNoBodyB) is stated and dropped, and the M1 has no Mavie Work fact. The M2 opens with "For growth work, scale helps."
- `vedran-bijelac-00472714a` M2: "Numbers help a decision like this." M1: no Mavie fact.
- `victoria-sobulska-b5b7a0167` M1: "partner part" is unclear, plus the triple above. The question ("Which Mavie venture has its members at home most of the time?") has nothing to do with her work.
- `andrea-grandits-42782b101` M2: "whoever owns the Mavie Work app" refers to an app the card does not confirm. She is product P2, so the easy out is not needed.
- `lea-paradzik`: the M2 easy out goes to the owner herself (Head of Product, MavieMe). M1 calls MavieMe "an app"; the card describes home tests and online consultations. The M2 also has the speed phrase as a dangling clause.
- `doris-busek-baum-7606b4131`: writes "Mavie work" in lower case. The M2 has no value line.
- `vera-brockherde-9a8240126` M1: "shown only where the programme chooses" is the 3D-model rule sentence, applied to measurements. The M2 has no value line.
- `nicolas-haffner-a5783460` M1: "80+ body measurements as estimates". Body measurements are not estimates; body composition is.
- `drmeghabhola`: the Covid-facilitator hook is unrelated to her product role. The M2 phrase "without a capture flow of its own" is unclear.

### mixed-1 (32)
- **Aeon:** `puntschuh` and `serge-weydert` use the same opener ("Noticed your background:"). `serge-weydert` and `pablo-tano-a39a15164` ask the same question (build or bring in). `puntschuh` and `drfelixharder` ask the same question (what the team or physician wants from a member between retests) and have overlapping M2s. `serge-weydert` says "Aeon app" twice. `granitalaj`: the bio hook is dropped, the M1 copies the lane note, and the M2 has no value line.
- **CARE Preventive:** `ionhaab` M2 says "Founder to founder". `pauline-sauvaget` M1 has the triple and is identical to `alice-conques`. `julien-montier` M1 asks two questions in one. `ertanwittwer` uses the opener template "Quick thought as [title] of [company]", shared with `ismaël-emelien-a0286922b`. The card says the brand is written "care"; all 5 write "CARE Preventive".
- **Lucis:** `maximeberthelot` and `philippine-breuil-a0aa41119` ask the same question (what brings members back during the 12 months). `sylvain-pace-it-engineer` and `mauryhugo` ask the same question (which parts of the app you work on). `mauryhugo` and `leo-tuil` open their M2s the same way ("If the Lucis app/roadmap ever gets a capture step"). `pierre-gimat` and `leo-tuil` use the same close ("point me to whoever owns the member app"). `bdebever` and `marwanmashra` share a product sentence ("REST API with API-key authentication. Two photos go in, and 80+ … come back"). `philippine-breuil-a0aa41119`, `sylvain-pace-it-engineer` and `pierre-gimat` share the core sentence "a guided two-photo scan returns 80+ body measurements".
- `leo-tuil` M1: the AirStrip hook is dropped, and there is no Lucis fact and no line on why it matters for members (referral M1 requires both).
- `mauryhugo` M1: "the people who shape how Lucis looks and feels" addresses one person as a group, with no Lucis fact.
- `merodriguezmd` M1: "made me think of one thing", and the thing never comes.
- **YEARS:** `jkhennigs` and `sebastian-kuss` share a product sentence and ask a similar question. `janlukasschmitz` and `dimitri-vogel` ask the same question (what members ask between check-ins) and close the same way. 4 of 6 questions are "what do you want … between check-ins" (`jürgen-mehrtens-116303b1`, `leonhardfriedrich18`, `jkhennigs`, `sebastian-kuss`). `leonhardfriedrich18`: the MSc claim above, plus "this is your kind of input". `dimitri-vogel` M2: "Worth seeing how it looks on a phone." then a number, with no value line.
- **Zoī:** `ismaël-emelien-a0286922b` and `pr-jerome-salomon` both open the M2 with "I would be glad to show". `alice-conques`: the triple, the flattery "you think in systems", and a question that nearly duplicates `janlukasschmitz`'s. `pr-jerome-salomon`: "Hi Jerome," for a professor who is a former DG for Health, with the accent dropped (Jérôme). `alexandre-hollard` M2: no value line, the founder template, and no link back to his "reports nobody opens" theme.

### mixed-2 (35)
- **Hook reuse in one batch:** "Noticed your background" in `dennishermann`, `octavia-seymour`, `onnohuyghe`, `sophie-agosta`, `kevin-najafi-685254303`, `gemmafrenchman`, `peter-roland-737ab34`. "Came across your work" in `vinsensius-vega`, `alejandragimenezg`, `leanne-verdonck-a643b474`, `dariusz-soldacki-md-phd-a178b819`, `simon-lindgren-269102a4`.
- **"Offer" label opening the M2:** `svenjaeschke`, `octavia-seymour`, `andrew-mccarthy-impact-entrepreneur`, `onnohuyghe` (says "My offer is short." and then makes no offer), `mariana-wohlfahrtova-0555b276`, `sophie-agosta`, `magdalena-winnicka-b08972313`, `joelgrajcer`, `massimo-pietracaprina-a528951`, `leo-glauberman-56657316`, `henrik-forsberg-96637ba3`.
- **2-4 weeks (campaign ban):** `vinsensius-vega`, `sroze`, `arian-vassili`, `simon-lindgren-269102a4`. The same four have identical technical M1s.
- **Clinical M2 copies:** `leanne-verdonck-a643b474`, `kevin-najafi-685254303`, `dariusz-soldacki-md-phd-a178b819`. Their M1 lane sentence is shared with `mariana-wohlfahrtova-0555b276`.
- **Partnership copies:** `alejandragimenezg` and `ash-patel-20647b161` (both messages, with lane-note wording).
- **Empty-profile copies:** `magdalena-winnicka-b08972313` and `leo-glauberman-56657316`. Both M1s use "As director / As owner, …", and both M2s give the decision-maker an easy out.
- **Account fact copied word for word:** `dennishermann` ("Once a baseline exists, members book follow-up tests"), `henrik-forsberg-96637ba3` and `ash-patel-20647b161` (the same reminder sentence, at one company), `joelgrajcer`, `sophie-agosta`, `joanna-bensz-205b315`, `onnohuyghe` ("frames the check as yearly", the card's analyst phrasing), `kevin-najafi-685254303`, `wschleuter` (M2).
- **Lane note copied:** `dennishermann` (M2), `kate%c5%99ina-vrbov%c3%a1-22bb7620a`, `peter-roland-737ab34`, `hannah-whitcombe-b2b35866`.
- **Ahead:** `dennishermann` and `nlenten` ask the same question (what a member does between baseline and follow-up). `svenjaeschke` has the triple. "Ahead app" appears in `svenjaeschke` and `vinsensius-vega`. `nlenten` M2 adds unsourced detail about the 34,000-scan platform.
- **Axo:** `octavia-seymour` and `alejandragimenezg` share a company sentence ("repeats the check every six months"). `octavia-seymour` and `tangsergio` ask the same question (what keeps a member opening the app between check-ins). `octavia-seymour` writes "a D2C member". `tangsergio`: "Axo Longevity app", the hook is dropped, and the M2 opens "For a product owner, repeatability matters."
- **Concierge Medicine Europe:** `wschleuter`, `kate%c5%99ina-vrbov%c3%a1-22bb7620a` and `mariana-wohlfahrtova-0555b276` share one product sentence (member opens a web link and does a guided scan on the phone).
- **Longevity Center:** `joanna-bensz-205b315` and `magdalena-winnicka-b08972313` have the same product sentence. All 3 questions are "at home between visits". `magdalena-winnicka-b08972313` M1 has no company fact. `dariusz-soldacki-md-phd-a178b819` M1 has no company fact either (only his role path). `joanna-bensz-205b315` says "quarterly check-ins"; the card says annual programmes or quarterly. Her M2 "across every site" sits close to the card's "any site count" Never.
- **Preventicum:** `gemmafrenchman` and `leo-glauberman-56657316` share a product sentence and ask a similar question (keeping clients in touch between assessments). `hannah-whitcombe-b2b35866` M2: "the point is little to run" is unclear English.
- **Macromo:** `oliks` and `michal-pohludka-56223939` share a company sentence (personal plan and yearly retest). `oliks` M1: "Quick one, from a Head of Product who has also shipped…" reads as if the sender is the Head of Product. `michal-pohludka-56223939` M2 opens "Scale for context:".
- `massimo-pietracaprina-a528951` M1: "Noticed overlap with your years at IEO and Humanitas" is a non sequitur. Those were HR director roles, and the sentence implies a clinical overlap.
- `kevin-najafi-685254303` M1: hooks a co-founder and COO on his "junior doctor training", and calls measurements "estimates".
- `fabio-benevolo-399b832` M2: "For a CIO". He is General Manager now.
- `khadija-benmansour-2535b7a8` M2: "For a founder, scale matters:".
- `peterpaul-deleeuw` M1: opens with an aphorism that presumes his view ("the useful part of AI is usually the structure it returns").

### mixed-3 (8 in scope)
- Easy out given to the buyer, all in the same "If X sits with someone else, point me to them. Otherwise…" template: `marioaichlseder` (CEO), `haif-rood` (CEO), `guentherpatterer` (CEO & Founder), `elisabetta-tata-reggio-07b31847` (GM). `bruno-marco-dufort-224358162` uses the same template.
- In 6 M2s the GDPR line comes after the calendar link, in the §2 wording (ids under D).
- `bruno-marco-dufort-224358162`: the M1 copies the lane note and has the dangling speed phrase. The M2 opens "Some scale for context:" and has no value line.
- `haif-rood` M2: "Some scale for context:" and no value line.
- `eddy-van-b323a9a`: M1 "another thing a portal can offer" is weak, plus the dangling speed phrase. M2: "For scale, one platform ran…".
- `natalia-trpchevska`: body composition estimates offered against AYUN's Never line, plus the lane sentence.
- `vinzenzweber`: no issues.

---

## Top 3 issues (priority for the improver)

1. **Same-company collisions and lane templates repeated across companies.** About 25 same-company pairs break the card's "no shared opener / central question / closing ask / product sentence" rule. Five lane templates (clinical M1+M2, technical M1, partnership, founder product M2, empty-profile) repeat almost word for word across companies. A forwarded screenshot reads as a mail merge.
2. **Card and lane-note text pasted into copy, and M2s with no value line.** About 30 messages copy lane notes or account facts word for word, including 21 dangling speed-phrase clauses and 11 "ship, stock or install". About 15 M2s are only a label, a number, the GDPR line and a closer. The M2 needs regenerating per person, not patching.
3. **Rule and fact errors:** "2-4 weeks" ×4 against the campaign ban; "Founder to founder" (`ionhaab`); the MSc claim (`leonhardfriedrich18`); the sender ambiguity (`oliks`); the IEO/Humanitas non sequitur (`massimo-pietracaprina-a528951`); apps the card does not confirm (Aeon, Ahead, Axo, Mavie Work); easy outs given to 7 buyers.

## Coordinator notes (system-level, not scored against the agent)
- `card-messages.md` contradicts itself on integration time. The campaign rules say "No integration-time figure", while the proof-points block (appended by the card generator from icp-detail.md) offers "2-4 weeks". The generator should drop that block when the hypothesis bans it.
- The `split-messages` gate does not compare same-company sentences beyond the GDPR line, and its near-duplicate flags are mostly that intended line (about 75 of 80 soft notes). The real collisions listed above passed silently.
- Per-person message files carry no `product:` frontmatter by script design, so the QC hard rule cannot be met by the agent.

## Coordinator review

agreement: ✅ agree
top_issue: same-company collisions + lane templates + value-less M2s → fix round 1 (all M2 regenerated per person, named M1s rewritten), same four agents, per-batch fix files built by script from this report and the coordinator scan.

---

## Re-score after fix rounds (2026-10-21)

I re-read all four batch files (92 people; Circle Health is out of mixed-3) against `card-messages.md` and the `_profiles-*.md` files, after rounds 1-3 (`_fix-1/2/3-*.md`), and scored from scratch. The round-1 score above stays for the record.

**Total: 15/20 — good.** Approve after the blocking line fixes in issue 1 below. Nothing needs regenerating.

| # | Category | Round 1 | Re-score | Max |
|---|----------|---------|----------|-----|
| A | Adherence | 2 | 4 | 5 |
| B | Factual accuracy | 3 | 3 | 5 |
| C | Brand & tone | 1 | 2 | 3 |
| D | Format & structure | 2 | 3 | 3 |
| E | Output quality | 2 | 3 | 4 |
| | **Total** | **10** | **15** | **20** |

### Why these scores
- **A 4/5.** Fixed:
  - the "2-4 weeks" line is gone;
  - easy outs go only to non-buyers;
  - every M2 has a value line or a concrete technical next step;
  - the M1 hook phrases are no longer reused within a batch;
  - lane notes are no longer pasted into the copy.

  Not 5:
  - 8 same-company collisions remain at sentence level, plus 6 at argument or opener level;
  - the card's "112,100 … (its own sentence)" rule is broken in 4 messages;
  - 2 partnership-lane M2s have no easy out.
- **B 3/5.** Every round-1 fact error is fixed: the sender, the MSc, the apps the card does not confirm, the 34K deployment details, AYUN body composition, and Nicolas now at Mavie Med.

  New: when the fix rounds rewrote the 112,100 fragments as clauses, several now credit the number to the flow being pitched:
  - "The same flow ran 112,100 scans";
  - "That sequence handled 112,100 scans";
  - "the flow behind the 112,100 scans";
  - "The tool has volume behind it".

  Proof-points clears 112,100 only as 3DLOOK-wide scale, "never attributed to one platform". The count covers both products, so "the same flow" overstates FitXpress volume. That is one class of wrong attribution, in 6 messages, so B stays at 3.
- **C 2/3.** Fixed:
  - triples are down from 11 to 2;
  - the fragment openers and the dangling speed phrase are gone;
  - the ", so" is gone;
  - there are no banned words.

  Lapses:
  - the 2 triples;
  - a new formula that tells the reader what they know or will think ("…, which means you know …", "you will ask …", "you probably think about …"), in 16 M1s.
- **D 3/3.**
  - The summaries now count correctly: mixed-1 is 13/6/5/5/3, mixed-2 is 21/4/4/4/2, mixed-3 is 5/1/1/1.
  - mixed-3 puts the GDPR line before the link and uses the §9 wording.
  - The calendar link ends every message.
  - The frontmatter rule is still not applied (system gap).
- **E 3/4.** M2s now carry value specific to each person. The round-1 best pairs are intact, and there are new strong ones:
  - `peterpaul-deleeuw` (the Amberscript analogy);
  - `sroze` (the deletion question);
  - `arian-vassili` (the retention-window question);
  - `natalia-trpchevska` ("what counts as a real change");
  - `alexandre-hollard` (the M2 returns to his theme);
  - `elisabetta-tata-reggio-07b31847`.

  Still there:
  - cross-company templates (clinical M2 ×5, technical opener ×4, the partnership sentence, the founder tail ×3);
  - stock phrases: "a front and a side photo" in 21 of the 35 mixed-2 M1s, "alone" ×16, and the standalone "3DLOOK has worked with 100+ clients." ×17.

### Round-1 findings, one by one
**Coordinator's list:**
- Verbless fact fragments: fixed, but see the new 112,100 attribution issue under B.
- Standalone "100+ clients": partial. 21 became 17, and it still sits as the last sentence of the value paragraph.
- Stock closers: fixed (0).
- "15 minutes" / "20 minutes": fixed (0).
- ", so": fixed.
- Nicolas Haffner: fixed (now written as Mavie Med).

**Category level:**
- Same-company collisions (~25): partial. About 14 remain (listed below).
- Lane-note and account-fact copy (~30): mostly fixed. "Ship, stock or install" and "standardized, timestamped body record" are both at 0; 5 residual copies remain.
- 2-4 weeks: fixed.
- Hook reuse in mixed-2: fixed.
- Easy outs given to buyers (×7): fixed.
- M2s with no value line (×15): fixed, except for three thin ones (`oliks`, `michal-pohludka-56223939`, `magdalena-winnicka-b08972313`).
- Triples (×11): fixed, with 2 new ones.
- Fragment openers: fixed.
- Dangling speed phrase (×21): fixed. The 4 that remain are their own sentences.
- Stock M2 lead-ins: fixed. A softer repeatability lead-in survives in `leanne-verdonck-a643b474`, `tangsergio` and `fabio-benevolo-399b832`.
- Summary counts: fixed.
- mixed-3 GDPR placement and wording: fixed.
- Lane templates:
  - fixed: the clinical copies (leanne/kevin/dariusz), the identical technical M1s, the empty-profile mirror, and the operations question repeated 7 times;
  - partial: the partnership pair and the founder M2;
  - not fixed: the clinical M2 for puntschuh, drfelixharder, roman-walser, jkhennigs and pr-jerome-salomon.

**mavie-work:**
- Fixed: janine/doris product sentence; janine hook, "Teams" and value line; megha/johanna M2; ondrej/victoria "ready part"; ondrej/vera; jasmin; vedran; victoria; andrea; lea; doris; vera; nicolas "estimates"; megha.
- christophbodenstein/johanna M1: fixed in the M1, but the shared argument moved to their M2s.
- lukas/vedran question: fixed, but vedran now collides with ondrej and victoria (see below).
- Career-recap openers (×8): partial. They became "As [title] at Mavie (Next), you …" ×5.

**mixed-1:**
- Fixed:
  - Aeon: the shared opener, serge/pablo question, "Aeon app", granitalaj;
  - CARE: ionhaab, pauline/alice triple, julien, ertan/ismaël opener, the "care" brand;
  - Lucis: all 8 items;
  - YEARS: all items except dimitri's M2;
  - Zoī: ismaël/jerome M2, Jérôme's accent, alexandre.
- puntschuh/drfelixharder: question fixed, M2 **not fixed**.
- dimitri-vogel M2: partial (still thin).
- alice-conques: partial. The flattery became the presumptive "you will ask …".

**mixed-2:**
- Fixed:
  - hook reuse; "offer" labels; 2-4 weeks; identical technical M1s; clinical copies; empty-profile mirror;
  - lane-note copy; Ahead; Axo (but see the new octavia/andrew collision);
  - Preventicum; Macromo; massimo; kevin; fabio;
  - khadija (but see the new presumptive line); peterpaul.
- Account-fact copy:
  - fixed: dennis, henrik/ash, joel, onno, wschleuter;
  - partial: sophie, kevin;
  - **not fixed**: joanna (and magdalena now shares the same wording).
- Partnership pair (alejandra/ash): partial.
- Concierge Medicine Europe: partial (wschleuter/kate-vrbova).
- Longevity Center: partial. The company fact, "quarterly", "every site" and dariusz are fixed; the joanna/magdalena collision is **not fixed**.

**mixed-3:**
- Fixed: easy outs; GDPR line; bruno (but see the new 112,100 issue); haif (but see the new haif/eddy collision); eddy; natalia.
- vinzenzweber is still clean.

### New or remaining findings (with person_id)
**112,100 credited to the flow, or not in its own sentence (B; blocks import):**
- Credited to "the same flow / that sequence / the flow / the tool / the step": `janlukasschmitz`, `bruno-marco-dufort-224358162`, `pierre-gimat`, `magdalena-winnicka-b08972313`, `massimo-pietracaprina-a528951`, `khadija-benmansour-2535b7a8`.
- Joined to another clause, against "(its own sentence)": `ionhaab`, `pierre-gimat`, `wschleuter`, `magdalena-winnicka-b08972313`.

**Same-company collisions still present:**
- **mavie-work:**
  - `andrea-grandits-42782b101` M2 and `doris-busek-baum-7606b4131` M1+M2: a coach or adviser talks through the 80+ measurements at the next session.
  - `ondrejgandel`, `victoria-sobulska-b5b7a0167` and `vedran-bijelac-00472714a` M1 questions: all three ask what Mavie sources from partners.
  - `christophbodenstein` M2 and `johanna-resch-connect` M2: both pitch testing the scan with a first group of members through a link.
  - "As [title] at Mavie Next, you …" openers: `drmeghabhola`, `cezarneaga`, `johanna-resch-connect`. The same shape appears in `vera-brockherde-9a8240126` and `victoria-sobulska-b5b7a0167`.
- **mixed-1:**
  - `puntschuh` M2 and `drfelixharder` M2: body composition estimates, "chooses which scans to compare", then the device line.
  - `jürgen-mehrtens-116303b1` M2 and `leonhardfriedrich18` M2: "YEARS chooses which measurements / what members see".
  - `ertanwittwer` M2 and `pauline-sauvaget` M2: "care decides what each member sees / who sees the measurements".
  - `sylvain-pace-it-engineer` and `mauryhugo` M1 openers: both open on the doctor-reviewed plan in the Lucis app, and `leo-tuil` uses the same fact.
  - Zoī: 4 of 6 openers use "you know / you will / which means you" (`pauldupuy89`, `pr-jerome-salomon`, `alice-conques`, `emile-b-82bb9567`).
- **mixed-2:**
  - `octavia-seymour` and `andrew-mccarthy-impact-entrepreneur`: M1 both say "visit a lab twice a year", and M2 both use "something a member/person does alone".
  - `joanna-bensz-205b315` and `magdalena-winnicka-b08972313`: same M1 opener ("plan at home or in the centre", close to the card's wording) and the same product sentence ("FitXpress gives (each of them) 80+ body measurements from …").
  - `wschleuter` and `kate%c5%99ina-vrbov%c3%a1-22bb7620a` M1: link on a phone, front and side photo, 80+.
  - `sophie-agosta` and `sroze` M1: both open on sharing data with doctors, and share the identical clause "a front and a side photo give 80+ body measurements".
  - `peter-roland-737ab34` M1 and `henrik-forsberg-96637ba3` M2: "the scan needs only a phone" (minor).
- **mixed-3:**
  - `haif-rood` M2 and `eddy-van-b323a9a` M2: "would give Prescan client(s) something to do …".

**Cross-company templates and stock phrases (E):**
- Clinical:
  - M2: `puntschuh` and `pr-jerome-salomon` are near word for word; `roman-walser-154512255` and `jkhennigs` have the same shape.
  - M1: `jkhennigs` and `roman-walser-154512255` share "A member's home scan gives [your doctors] 80+ body measurements from two photos".
- Technical M1 opener formula "[Company] holds X, which makes Y the first question": `vinsensius-vega`, `sroze`, `simon-lindgren-269102a4`, `arian-vassili`.
- Partnership, `alejandragimenezg` and `ash-patel-20647b161`:
  - M1 both say "3DLOOK offers FitXpress, a phone scan … 80+ body measurements from two photos, to companies that build it into their own …";
  - M2 both say "A (short) call would show how … the scan. One platform ran 34,000 scans in 2025." followed by a pointer.
- Founder M2 tail "[Company] chooses/decides which measurements a member sees. 3DLOOK has worked with 100+ clients.": `maximeberthelot`, `jürgen-mehrtens-116303b1`, `alexandre-hollard`.
- Stock phrases:
  - "a front and a side photo" in 21 of 35 mixed-2 M1s, plus `bruno-marco-dufort-224358162`;
  - "alone" ×16 across batches;
  - the standalone "3DLOOK has worked with 100+ clients." ×17. In `mariana-wohlfahrtova-0555b276` it follows "Each doctor can choose whether a scan joins a visit at all" and has nothing to do with it.

**Tone (C):**
- Triples:
  - `wschleuter` M1: "open a link…, send a front and a side photo and get 80+…";
  - `arian-vassili` M1: "is called with an API key, takes … and returns …".
- Openers that tell the reader what they know or will think (the presumed-reaction judgment row on the bans card):
  - M1: `julien-montier`, `pauline-sauvaget`, `maximeberthelot`, `marwanmashra`, `sebastian-kuss`, `dimitri-vogel`, `pauldupuy89`, `pr-jerome-salomon`, `alice-conques`, `emile-b-82bb9567`, `octavia-seymour`, `lukas-mayrl-7093029b`, `janine-wagenlechner`, `natalia-trpchevska`, `marioaichlseder`;
  - M2: `khadija-benmansour-2535b7a8` ("Employers and insurers will ask…");
  - worst: `alice-conques` ("you will ask") and `pr-jerome-salomon` ("you know how preventive medicine is judged", written to a former DG for Health).

**Other minor findings (person level):**
- `ondrejgandel`, `victoria-sobulska-b5b7a0167` M2: partnership lane without the easy out the card asks for. Low priority for Ondrej, who is MD.
- Residual card copy:
  - `ertanwittwer` M1: "for long-term monitoring of values";
  - `ismaël-emelien-a0286922b` M1+M2: "helps the member put the recommendations into practice". The M2 repeats the M1 and adds nothing new;
  - `kevin-najafi-685254303` M1: "chat with the health team between check-ins".
- Claims the facts do not support:
  - `jasmin-cohen2` M2: "which shows that a phone scan can become an everyday step";
  - `leanne-verdonck-a643b474` M2: "A repeated scan is only useful if it agrees with the last one". A scan is there to show change; `natalia-trpchevska`'s wording is the right one;
  - `christophbodenstein` M1: "one that can be added quickly", an unquantified integration-speed claim;
  - `evakuttichova` M2 ("A habit is easier to keep when a person sees a record of it") and `gemmafrenchman` M2 ("keeps them in touch"): engagement claims with no source.
- Thin M2s:
  - `oliks`: "As the owner of the roadmap, you decide how much of this lands in the app.";
  - `michal-pohludka-56223939`;
  - `magdalena-winnicka-b08972313`.
- Wording:
  - `nlenten` M2 says "under Ahead Health's name" twice;
  - `janine-wagenlechner` M2 repeats the M1's "same steps on any phone";
  - `dimitri-vogel` M1: "suits the stretch";
  - `hannah-whitcombe-b2b35866` M1 opener restates her bio and then drops it.

### Top 3 remaining issues
1. **112,100 credited to the flow (6 messages) or not in its own sentence (4).** People: `janlukasschmitz`, `bruno-marco-dufort-224358162`, `pierre-gimat`, `magdalena-winnicka-b08972313`, `massimo-pietracaprina-a528951`, `khadija-benmansour-2535b7a8`, `ionhaab`, `wschleuter`. These are one-line fixes, but they block import: the number is 3DLOOK-wide across both products, and these lines present it as volume for the FitXpress flow.
2. **Same-company collisions still present.**
   - 8 at sentence level: puntschuh/drfelixharder, jürgen-mehrtens/leonhardfriedrich18, ertanwittwer/pauline-sauvaget, octavia-seymour/andrew-mccarthy, joanna-bensz/magdalena-winnicka, wschleuter/kate-vrbova, sophie-agosta/sroze, haif-rood/eddy-van.
   - 6 at argument or opener level: Mavie ×4, the Lucis openers, the Zoī openers.
3. **Cross-company templates and stock phrases.** The clinical M2 (puntschuh is close to pr-jerome-salomon), the technical opener formula ×4, the partnership sentence (alejandra/ash), "a front and a side photo" in 21 of 35 mixed-2 M1s, the presumptive openers ×16, and the bolted-on "100+ clients" ×17. These don't block import, but they are worth one more pass if there is time.

### Coordinator note (system)
- The gate still sees only the GDPR line among same-company near-duplicates, which is why issue 2 passed. It also cannot catch issue 1. A check for "112,100" that does not start its own sentence, or that sits next to flow/sequence/tool/step, would catch it.

### Coordinator review (re-score)
agreement: ✅ agree
top_issue: 112,100 credited to the pitched flow in 8 messages (my round-2 instruction 'keep the fact's own words inside your sentence' invited it) → fix round 4 deletes the figure there; 8 sentence-level same-company pairs and 3 thin M2s fixed in the same round, verified mechanically.
