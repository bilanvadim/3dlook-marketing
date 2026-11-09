---
qc_date: 2026-11-09
agent: message-sequencer
artifact: /tmp/claude-1006/-home-vadim-prod/2ca059ad-021c-4c25-8a41-8a2f129a1701/scratchpad/widen/dump/new-*.md (108 new pairs, 16 companies)
track: outbound
artifact_type: messages
campaign: 2026-10-22-uk-insurance-underwriting
step: messages (widening 2026-11-09)
total_score: 12/20
status: marginal
coordinator_review: done
---

# QC Report — message-sequencer — 2026-11-09 (UK insurance widening, 108 new pairs)

**Artifact:** `scratchpad/widen/dump/new-*.md` (all 16 files read in full; existing-<company>.md read as context)
**Total: 12/20** — marginal. A fix round is enough; full regeneration is not needed. About 45 of the 108 pairs need an edit, mostly at Aviva, L&G and Royal London.

What holds up: no Never-list breach anywhere (no AIG Life, Iress, iPipeline, merger, colleague appointment, or account-employer named). Former employers were filtered correctly (Amanda Weston's AIG Life and Nick Telfer's British Friendly left out). 3.5% appears only in underwriting/medical/reinsurance M2s, always with "not a scale reading". The GDPR line appears only in permitted lanes. No M1 links. Landing URL use is under half per company. No M2 assumes a reply. Most technical-integration questions are credible: juangr (feature switch for a share of cases), alanpich (observability, versioning), lee-hope (SDK vs back-end API), russellwjohnston (monitoring a vendor estimate), stuart-mckellar and mike-lytheer (DPIA before a shadow run), angelaluget (AI use guidance), leemwilson (evidence vs rule input). No message implies training on client data.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- Widening rules 1 and 3 (no cell repeats or closely paraphrases another cell at the same company, old or new) are broken many times. The new M2 value lines converge on "a shadow evaluation counts flags per candidate threshold": Aviva 10/25 new (≈19/46 with existing), Royal London 11/20 (≈20/38), Pacific Life Re 6/10 (≈14/22), L&G ≈8/20. The card limits one topic to about a fifth of a company's people.
- Lane notes copied almost word for word into questions, which the card says never to do: steven-morrison, matthew-wilton, gary-williams, daniel-smith, harpreetsarna, vikki-larkin, daniel-simpson, hannah-leech. In dave-roberts' M2 the flag lane note is pasted as a sentence.
- Bolt-on numbers (writer rule 7). "3DLOOK has worked with 100+ clients" appears in daniel-simpson and david-brownlow. "80+ body measurements" is unrelated to the question it follows in emese, nick-telfer, martyn-luke and pete-sanderson.
- L&G question-topic concentration: about 10 of 39 people are asked what gets a step into scope or the programme (simon, kannan, andy-bergin, prakash, cheryl, james-mcmillan, choi, plus existing Jenny Reeve, Gary M., Pippa).

### B. Factual accuracy — 3/5
- No invented numbers or clients. All numbers come from proof-points.md.
- matthew-wilton M2 proposes "a look-back on past applications" that counts flags per threshold. That cannot be done: past applications have no photos, so there is nothing to flag after the fact.
- In 8 M1s the flag is attached to the estimate (or to BMI) instead of the declared-vs-estimated gap ("a Smart Scales weight estimate, flagged only above the insurer's threshold"). This reads as a weight cut-off, which edges toward decisioning: markmbird, 74lancater, david-stewart, cheryl-hinton, kannansundarraj, andy-bergin, kristiansc, donna-cowell. About 25 more M1s say only "a flag above the threshold" and never say what is compared. That is lower priority, because the 2026-10-26 set did the same.
- Unsupported claims about how prospects work inside: james-appleton ("A shadow run needs few sign-offs"), himal-patel (a reinsurer's enterprise architecture "decides how any new evidence source would reach a client insurer's application"), judit-f (how L&G Retail routes vendor review), vicki-wharton (implies a record reaches Royal London only when a flag is raised).
- hannahrothery "The test is cheap" makes a cost claim in cold copy.
- chris-miller-uk paraphrases the AI-training line and drops the compliance.md caveat. The card says data-handling sentences use compliance.md forms only.
- Lane fit (list-level, not the writers' fault): david-brownlow is "Global Head of L&H Data Operations & Solutions", and widening item 3 excludes data operations heads. This needs a coordinator decision.

### C. Brand & tone — 2/3
- No banned words, dashes or corrective negation (code-checked; none found by reading either).
- Royal London: 17 of 20 new M1s open with the same impersonal one-line maxim that names neither the person nor the company ("Technology investment decisions rest on clear facts about each component.", "Group strategy weighs protection against the group's other lines."). Placed side by side they read as a template (MSG-7). Royal London's own fact (income protection occupation class refresh) appears in none of them.
- Triple parallels: dan-turner M1 (two of them); the simon/kannan/prakash M2 lists; charlesking001/hannahrothery M2; paulrmburu M2.
- Presumed reaction: harpreetsarna ("you would ask what a software estimate ... can and cannot be used for"). Cliché: louise-m ("Optional steps live or die by the route that stays open.").
- Clunky or contorted sentences: amanda-weston question, ashley-murray opener, jonathan-saggers M2, richard-whaley M2, alanpich ("Your record is API platforms."), matthew-barclay M1 and M2, alan-dott (addressed in the third person), gideoncheok ("The build is an API"). Dangling modifiers in msasaki, juangr, emma-coleman, damion-m, darren-wing.

### D. Format & structure — 2/3
- Known (strict-new.txt): 19 M2s with no call offer next to the link, and emma-denby with the calendar link not last. Seen beyond that list: weak or terse call lines in tasneem ("Call link, whenever suits:"), adrian-nye ("Or a call:"), harpreetsarna and paulrmburu ("Call, or point me…"), himal-patel ("if a call is easier than email"), sophie-hadfield ("A call on journey placement is open."), damion-m and nic-herbert (imperative "Walk through the integration…").
- The boundary sentence is not kept verbatim: james-mcmillan adds a colon clause, jonathan-saggers adds ", and it refers only gaps…".
- The speed figure is folded into a longer sentence, though the card requires its own plain sentence: maria-c, alistair-hargreaves, emese, nick-telfer, martyn-luke, pete-sanderson.
- nathan-tomlinson: the easy-out starts with "Or" before any call offer has been made.

### E. Output quality — 2/4
- Sameness at the same company, new against old, beyond what scan-r0 caught: maria-c's question = existing Victoria Francis; tasneem question + M2 = existing Aman Hayer; james-appleton = existing Suzanne Lawson; nathan M2 triad = existing Suzanne; dan-tinson M2 opening = existing Nick Austin; alistair easy-out target = existing Manju Devi; gary-williams closer = existing Michelle Cross; markmbird "your architects" = existing Michael Spiteri; sarah-farquharson "a pointer works just as well" = existing Amy Higgs; richardedwardpurcell question = existing Réka Halász and Mala Thurston; kristiansc question = existing Sai Tejo Kiran.
- Sameness among the new people: Aviva "As <title> for Insurance, Wealth and Retirement" ×3; "reaches you as a X question" ×2; "FitXpress adds a build record:" ×4; "a small one/case/item" hook ×4; "bets" hook used for both Group Strategy people; same easy-out target for megumi and nathan; non-scanner-route topic ×3 (louise-m, ashley-murray, msasaki). L&G: simon/kannan/prakash M2 triads; simon and kannan share the same easy-out ("product owner … I would welcome the pointer"); andy-bergin and kannan ask near-identical questions; markmbird and judit both ask about "new data processor" review. Royal London: same easy-out target for charul/shikha (vendor review), etienne/minoka (protection strategy) and leemwilson/russell (model governance/risk); finlay and daniel-thomson share the "What would X need to show to be included / earn a place" skeleton. Pacific Life Re: charles/hannah M2 twins; alan-dott/daragh "report flagged cases at each candidate threshold".
- Referral fit is mostly right (questions about the person's own work). Exceptions that slide into "who": james-appleton ("whose sign-off takes longest"), phil-quarmby ("who signs off its place"), james-jarman ("Who would define the schema" in technical-integration), chris-miller-uk ("with a named owner?").
- M2 value lines that do not continue the M1 question: tasneem (a flag count is not a commercial measure), ritwik-samsi (partner vs in-house question, answered with API facts), martyn-luke and nick-telfer (80+ measurements after an adviser-testing or features question).

## Top 3 issues (priority for improver)

1. **The M2 value line has turned into one template.** "Shadow evaluation counts flags per threshold" appears in about 35 of 108 new M2s, and in about half of all messages at Aviva, Royal London and PLRe once the 10-26 set is counted. Referral and proposition people need value lines built on their own M1 question.
2. **The flag is misdescribed.** In 8 M1s it is attached to the estimate or to BMI, and about 25 more do not say what is compared. matthew-wilton's "look-back on past applications" is impossible.
3. **Same-company skeletons.** The Royal London maxim opener ×17. At Aviva: "As <title> for IWR", "FitXpress adds a build record:", the "small one" hook, and the non-scanner route ×3. At L&G: the SDK/API/evaluation triad ×3 and the product-owner easy-out ×2. Plus about 11 central questions, easy-outs or closers that repeat an existing 10-26 message.

## Fix list

Known findings from strict-new.txt and scan-r0.txt are not repeated here except where this list adds a new party or a new defect.

```
christhompsonx | M1 | "Your AI strategy and product remit takes in any software that returns an estimate, and protection has one such case at Aviva." | contorted opener, "one such case" has no clear referent | plain opener from his AI remit
christhompsonx | M1 | "No underwriting decision is made by it." | stiff passive tacked on | fold the boundary into the product sentence or drop
msasaki | M1 | "As IT Director for Insurance, Wealth and Retirement, any capture step in a protection application reaches you as an integration question." | dangling modifier; "As <title> for IWR" opener shared with juangr and david-montgomery; "reaches you as a X question" shared with david-c | distinct opener structure, grammatical subject
msasaki | M2 | "If the scan step is unavailable, the application continues by Aviva's usual route, which the insurer keeps for anyone who does not scan." | third Aviva message on the non-scanner route (louise-m, ashley-murray); "Calls go over a REST API" reads like the call offer | different technical value line
juangr | M1 | "As CIO for Insurance, Wealth and Retirement and Group Deputy CIO, any application step arriving from outside meets your estate first." | dangling modifier; same "As <title> for IWR" skeleton | distinct opener
david-montgomery-34918b9 | M1 | "As COO for Insurance, Wealth and Retirement you run the operations behind protection applications, including referrals that go to an underwriter." | third "As <title> for Insurance, Wealth and Retirement" opener at Aviva | different opening structure
david-montgomery-34918b9 | M1 | "FitXpress adds a build record to cases with no medical evidence: 2 photos, a Smart Scales weight estimate and a flag past a threshold Aviva sets." | "FitXpress adds a build record" opens 4 Aviva product sentences | vary product-sentence structure
david-montgomery-34918b9 | M2 | "A shadow run shows the operating load before any decision: how many cases a flag reaches at Aviva's threshold, with outputs kept out of decisions." | near-twin of bharataheer M2 (operating load, shadow run); "decision" twice | distinct value line
bharataheer | M1 | "Your headline runs from operating model design to AI-enabled transformation, and the protection application is a small case of both." | "protection is a small one/case/item" hook shared with megumi, nathan, ashley-stevens | distinct hook
bharataheer | M1 | "On point-of-sale cases with no medical evidence, FitXpress adds a build record: 2 photos, a weight estimate from Smart Scales, and a timestamped flag when the gap from declared weight passes Aviva's threshold." | same "adds a build record:" frame as 3 other Aviva people | vary product sentence
bharataheer | M2 | "The operating load of a step like this shows in a shadow run: Aviva's threshold gives a count of flags and the handling they would need." | near-twin of david-montgomery M2; shadow-run count template | value line from his operating-model question
dan-turner-90632435 | M1 | "Your bio covers regulatory, technology and operational programmes, and a point-of-sale evidence step touches all three." | triple parallel, repeated in the question ("technology, process and adviser guidance") | one or two items per sentence
megumi-takenoshita-7862486 | M1 | "Group strategy decides where Aviva places its bets, and point-of-sale evidence in protection is a small one." | "bets" hook = nathan-tomlinson (same team); "small one" skeleton | distinct hook
megumi-takenoshita-7862486 | M2 | "If strategy for protection new business sits elsewhere, point me to whoever leads it." | same easy-out target as nathan-tomlinson | different role target
amanda-weston-b9a81146 | M1 | "When you assess a partner capability, how much weight does what it adds for adviser firms carry?" | contorted; "weight" pun in a weight-estimate message | plain question on how she assesses partners
maria-c-2627b715 | M1 | "Where on the intermediary journey would advisers expect a two-photo step for the client to sit?" | same central question as existing Victoria Francis (placement, adviser vs client) | question on another part of her intermediary-websites remit
gary-williams-93932815 | M1 | "How does build get treated on income protection against life and CI?" | near-verbatim lane-note question target | own wording from his product-and-underwriting title
gary-williams-93932815 | M2 | "I can walk through the design:" | same closer as existing Michelle Cross ("I can walk through a design here:") | fresh closer
louise-m-b23b3116 | M1 | "How would you decide which applicants are offered an optional step, with the usual route kept open for the rest?" | repeats the opener; same topic as ashley-murray question and msasaki M2 | distinct question
louise-m-b23b3116 | M2 | "Optional steps live or die by the route that stays open." | cliché; value line near-twin of ashley-murray M2 | different value line
ashley-murray-6233b9bb | M1 | "Propositions and change sit together in your title, and so do the practical questions of a new retail step." | contorted; "your title joins" skeleton = gary-williams | plain opener
ashley-murray-6233b9bb | M2 | "The usual route stays for anyone who does not scan, and Aviva decides where the step is offered." | near-twin of louise-m M2 | distinct value line
tasneem-harnekar | M1 | "Which commercial measure would you hold a new evidence step to first?" | same central question as existing Aman Hayer ("Which measures … judge whether a referral step earns its place?") | distinct question
tasneem-harnekar | M2 | "The first measure is a count from a shadow run: how many cases the step flags at a candidate threshold." | near-twin of existing Aman Hayer M2; a flag count is not a commercial measure | value line that actually meets her question, no new numbers
tasneem-harnekar | M2 | "Call link, whenever suits:" | no call-offer sentence | plain call offer
nathan-tomlinson-27aa0881 | M1 | "From engagement work at Strategy& to leading Group Strategy, you see which bets are cheap to test. Protection offers one." | "bets" hook = megumi | distinct hook
nathan-tomlinson-27aa0881 | M2 | "The evaluation design is short to read and gives group strategy a clear test: one set of cases, Aviva's threshold, no effect on any decision." | triad near-twin of existing Suzanne Lawson ("a shadow run, Aviva's threshold, no effect on any case") | distinct value line
nathan-tomlinson-27aa0881 | M2 | "Or point me to whoever sets protection strategy for new business." | dangling "Or" before the call line; target = megumi | easy-out after the call offer, distinct target
ashley-stevens-a07701ba | M1 | "What does a small point-of-sale step have to show to enter a transformation backlog?" | "What does X have to show before/to Y" = existing Harriet Granville-Jones and Hannah Spiro | different question shape
james-appleton-63083aa5 | M1 | "In delivering an innovation test inside protection, whose sign-off takes longest to get?" | "who" question; near-same as existing Suzanne Lawson ("who in protection usually sponsors a first test?") | question about his own delivery work
james-appleton-63083aa5 | M2 | "A shadow run needs few sign-offs, as the step runs alongside live cases and its outputs do not enter decisions." | asserts Aviva's internal approval burden (DPO, procurement still apply) | drop the claim
alistair-hargreaves-aaa09741b | M1 | "From a customer strategy view, which parts of the protection application feel heaviest to clients today?" | repeats the opener ("which protection steps clients find heavy") | opener and question carry different points
alistair-hargreaves-aaa09741b | M2 | "The step itself is short: it returns a timestamped record, under 45 seconds from the photos to structured results." | third Aviva copy of this sentence (maria-c, existing Victoria Francis); speed not its own sentence | different value line
alistair-hargreaves-aaa09741b | M2 | "Whoever owns the protection application experience could judge it faster, if you would point me to them." | same easy-out target as existing Manju Devi | distinct target
dan-tinson-b2a9a15b | M1 | "For cases Aviva decides at the point of sale, FitXpress adds a build record: 2 photos, a Smart Scales weight estimate, and a flag when the gap from declared weight crosses a threshold Aviva sets." | "adds a build record:" frame ×4 at Aviva | vary product sentence
dan-tinson-b2a9a15b | M2 | "A shadow run on Aviva's own threshold would show how many cases a flag reaches and what record sits behind each one." | opens identically to existing Nick Austin M2 | reword
david-c-26bb0418 | M1 | "Risk business partnering across UK Life, Health and Protection means a new evidence step reaches you as a control question." | "reaches you as a X question" = msasaki | distinct opener
david-c-26bb0418 | M1 | "FitXpress adds a build record: 2 photos, a Smart Scales weight estimate, and a flag past a threshold Aviva sets, on one timestamped record." | "record" twice; "adds a build record:" frame ×4 | vary, one "record"
david-c-26bb0418 | M2 | "A call is open here:" | "is open here" closer ×3 at Aviva (christhompsonx, louise-m); weak offer | fresh call-offer sentence
kelly-mhasal-b22b6129 | M2 | "An evaluation would give assurance the same view: every flag in a count, with the threshold used written beside it." | "the same view" has no referent; clunky | plain value line
kelly-mhasal-b22b6129 | M2 | "If control testing for protection belongs to someone else, tell me who." | target close to david-c (control framework / risk owner) | distinct target
adrian-nye-6b2422158 | M2 | "Or a call:" | not a call-offer sentence; dangling "Or" | plain call offer
markmbird | M1 | "Data strategy with control at its centre is the lens a new application step would meet first at Legal & General." | contorted | plain opener
markmbird | M1 | "FitXpress is a small one: an SDK step takes 2 photos and returns one structured, timestamped record, with a Smart Scales weight estimate flagged above the insurer's threshold." | flag attached to the estimate, not the declared-vs-estimated gap | state the flag is on the gap
markmbird | M1 | "How would a new data processor in the new-business journey be reviewed under your data control model?" | same topic as judit-f question and existing Michael Spiteri (vendor review) | distinct question
markmbird | M2 | "I can take your architects through the field layout:" | "your architects" = existing Michael Spiteri closer | fresh closer
74lancater | M1 | "For those decided at the point of sale, FitXpress adds one record: from 2 photos it produces a Smart Scales weight estimate, flagged only above the insurer's threshold." | flag attached to the estimate | state the flag is on the gap
james-jarman-3249891 | M1 | "Who would define the schema for a record like that before it landed in Retail's data estate?" | who-owns-X question | question about his own data estate
david-stewart-080a6435 | M1 | "FitXpress would supply one at the point of sale: a Smart Scales weight estimate and BMI from the declared height come from 2 photos, flagged above the insurer's threshold in one timestamped record." | flag attached to estimate/BMI | state the flag is on the gap
judit-f-29664635 | M1 | "An information security review is where a new vendor in the new-business journey is decided first, and Legal & General Retail routes that through your function." | asserts L&G's internal routing | open from her remit without asserting process
judit-f-29664635 | M2 | "Your reviewers can take it from a call:" | unclear closer | plain call offer
emese-simoradik-msc-asa-cera | M2 | "It returns 80+ body measurements, under 45 seconds from the photos to structured results." | bolt-on 80+ unrelated to the placement question; speed not its own sentence | value line on the placement question
simonsheldonconsulting | M2 | "The step is built to stay small in a change portfolio: an SDK and a REST API, one record per applicant, and an evaluation that keeps outputs out of live cases." | triad near-twin of kannansundarraj and prakash-rautaray M2 | distinct value line
simonsheldonconsulting | M2 | "If the protection application belongs to a product owner, I would welcome the pointer." | same target and phrase as kannansundarraj | distinct target
kannansundarraj | M1 | "The step would be small: an SDK takes 2 photos in the application and returns a timestamped record with a Smart Scales weight estimate, flagged only above the insurer's threshold." | flag attached to the estimate (near-twin already known) | state the flag is on the gap
kannansundarraj | M1 | "What does a delivery programme need from a new vendor before it is in scope?" | near-same central question as andy-bergin | distinct question
kannansundarraj | M2 | "Scope stays modest: an SDK and a REST API, one record per applicant on a random identifier, and an evaluation that runs apart from live cases." | triad twin of simon and prakash | distinct value line
kannansundarraj | M2 | "If the portfolio's product owner should see this first, I would welcome the pointer." | twin of simonsheldonconsulting easy-out | distinct target
prakash-rautaray-a9b32219 | M2 | "For a change calendar the shape matters: an SDK step for web and mobile, one record back to Legal & General's systems, and an evaluation before anything goes live." | third triad twin (same title as kannansundarraj) | value line on his change-rhythm question
cheryl-hinton-86598b1a | M1 | "One worth a look for protection is FitXpress, which takes 2 photos in the application and returns one timestamped record, with a Smart Scales weight estimate flagged above the threshold the insurer sets." | flag attached to the estimate | state the flag is on the gap
cheryl-hinton-86598b1a | M2 | "If the sponsor you have in mind sits in protection, I would be glad of the name." | presumes she has a sponsor in mind | neutral easy-out
martin-todd-755a0420 | M2 | "The evaluation reports how many cases a candidate threshold would flag and how many applicants complete the photo step, ahead of any live use." | near-twin of steven-morrison M2 and existing Nicki Plews | distinct value line
steven-morrison-90425586 | M1 | "How do build-related changes in terms after application show up in the feedback your team gets?" | near-verbatim lane-note question target | own wording from his product-management remit
steven-morrison-90425586 | M2 | "Product teams can see the effect before launch: the evaluation measures how many applicants complete the photo step and how many cases a threshold would flag." | twin of martin-todd M2 | distinct value line
andy-bergin-389278109 | M1 | "The step is an SDK that takes in 2 photos and sends back a Smart Scales weight estimate and a timestamped record, flagged only above the insurer's threshold." | FitXpress not named in M1; flag attached to the estimate | name the product; flag on the gap
matthew-wilton-49408544 | M1 | "At which build band edges would a gap like that change the outcome on a case?" | near-verbatim lane-note question | own wording
matthew-wilton-49408544 | M2 | "The first step would be a look-back on past applications: for each candidate threshold, how many cases it would flag, set beside build evidence held independently of the scan." | impossible: past applications carry no photos, so no flags exist to count | prospective shadow evaluation
richard-whaley-2a4459132 | M1 | "On which declared builds did you most often wish something measured sat beside them?" | implies FitXpress supplies a measurement (it is an estimate); clunky | reword without "measured"
richard-whaley-2a4459132 | M2 | "You would want the estimate's size up front." | wrong noun (error, not size); presumes his reaction | reword
jonathan-saggers-4ab31918 | M2 | "A risk view would start from what the flag leaves alone." | contorted | plain value line
jonathan-saggers-4ab31918 | M2 | "FitXpress is not a medical device and does not make underwriting decisions, and it refers only gaps above a threshold the insurer sets." | boundary sentence not verbatim | keep the boundary sentence verbatim; second point in its own sentence
james-mcmillan-b2795b59 | M2 | "FitXpress is not a medical device and does not make underwriting decisions: the insurer's own rules and underwriters decide what a flag means." | boundary sentence not verbatim | verbatim, separate sentence
donna-cowell-insurance | M1 | "It comes from 2 photos, with BMI calculated from the declared height, and carries a flag above the threshold Legal & General sets." | no weight estimate; reads as a BMI threshold, not a declared-vs-estimated gap | say what the flag compares
donna-cowell-insurance | M1 | "Pricing is in your background too." | bolt-on sentence | fold into the opener or drop
charulscott | M1 | "Technology investment decisions rest on clear facts about each component." | RL maxim opener (17/20): impersonal, no person, no Royal London | open from her remit with something only Royal London-specific
charulscott | M1 | "What does an architecture review at Royal London need to see before a new SDK step enters the application journey?" | near-same as shikhamerchant question and existing James Sandell | distinct question
charulscott | M2 | "If vendor review sits with another team, point me to them, or take a call yourself:" | same easy-out target as shikhamerchant (vendor review); "take a call yourself" awkward | distinct target, plain call offer
phil-quarmby-b41b4b71 | M1 | "A group data platform onboards sources one at a time, and each needs an owner." | RL maxim opener | personal, Royal London-specific opener
phil-quarmby-b41b4b71 | M1 | "How does a new source reach the group data platform, and who signs off its place there?" | second clause is a who-owns question | keep the question on his own work
etienneburger | M1 | "Group strategy weighs protection against the group's other lines." | RL maxim opener | personal, Royal London-specific opener
etienneburger | M2 | "If protection strategy sits with someone closer to the business, point me to them, otherwise a call:" | same easy-out target as minoka | distinct target
sarah-farquharson-a6066a34 | M1 | "Performance work in protection new business starts with where time goes between application and decision." | RL maxim opener | personal opener
sarah-farquharson-a6066a34 | M2 | "If performance for new business sits with a colleague, a pointer works just as well:" | "a pointer works just as well" = existing Amy Higgs | fresh easy-out wording
lee-hope-2086a73 | M1 | "Group architecture standards decide how a vendor step joins an adviser application." | RL maxim opener | personal opener
daniel-thomson-uk | M1 | "Product and proposition leaders decide what goes into the application journey, and what stays out." | RL maxim opener | personal opener
finlay-boyd-99a63539 | M1 | "Commercial planning for protection depends on how many cases reach an underwriter." | RL maxim opener; unsupported claim | personal opener
finlay-boyd-99a63539 | M1 | "What would a new evidence step need to show, in commercial insight terms, to be included in the plan?" | same "What would X need to show to …" skeleton as daniel-thomson-uk | distinct question shape
julieclapperton | M1 | "Distribution strategy has to weigh what each application step asks of an adviser." | RL maxim opener | personal opener
shikhamerchant | M1 | "Leading digital and AI architecture means deciding which components enter the reference design." | RL maxim opener | personal opener
minoka | M1 | "Strategy for protection includes the cases decided at the point of sale, where build is declared and no medical evidence supports it." | RL maxim opener | personal opener
minoka | M2 | "I would welcome a conversation on where it belongs on that list." | presumes FitXpress is on her watch list | neutral call offer
vicki-wharton | M1 | "Operations that are automating work depend on data arriving ready to use." | RL maxim opener | personal opener
vicki-wharton | M2 | "Where a flag is raised, the record reaches Royal London's systems as data." | implies only flagged cases return a record (every applicant gets one) | correct the record/flag relation
vicki-wharton | M2 | "An underwriter reads the file directly." | vague, adds nothing | drop or make specific
chris-miller-uk | M1 | "Every source that feeds a decision falls inside a group data and AI remit, including a weight estimate from a vendor." | RL maxim opener | personal opener
chris-miller-uk | M1 | "How would your office classify a record like that: as a new source in the group data inventory, with a named owner?" | leading yes/no with an embedded who-owns | open question on his data inventory practice
chris-miller-uk | M2 | "3DLOOK does not train its models on production data from deployments." | paraphrase of the compliance.md AI-training line with the caveat dropped | use the compliance.md form
leemwilson | M1 | "A data and AI strategy has a position on vendor estimates held on a case file." | RL maxim opener | personal opener
maureen-duckworth-1ba98623 | M1 | "Product management for protection owns the application as a product, step by step." | RL maxim opener | personal opener
russellwjohnston | M2 | "Data science questions are welcome on a call. If model risk is owned elsewhere, point me there:" | same easy-out target as leemwilson (model governance) | distinct target
sophie-hadfield-718b22111 | M1 | "A head of proposition decides where in the journey a protection step belongs." | RL maxim opener | personal opener
sophie-hadfield-718b22111 | M2 | "Either placement can be compared in an evaluation, with live cases left alone." | M2 opener "Either" = lee-hope M2; thin | distinct value line
sophie-hadfield-718b22111 | M2 | "A call on journey placement is open." | clunky call offer | plain call offer
daniel-smith-64507433 | M1 | "At which build band edges would that gap change the outcome on cases with no nurse screening?" | near-verbatim lane-note question; "band edges" appears 4 times in the pair | own wording, one "band edges"
vikki-larkin-b850a8aa | M1 | "Build loadings are set with only declared weight behind many cases." | RL maxim opener; unsupported claim about RL practice | personal opener
vikki-larkin-b850a8aa | M1 | "How does the team weigh the cost of build evidence against the loadings it supports?" | near-verbatim lane-note (pricing) | own wording
richard-basham-jones-7678a617 | M1 | "Service leaders with a digital agenda see where an application causes calls." | RL maxim opener | personal opener
ritwik-samsi-11442b11 | M2 | "The integration is one API with web and mobile SDKs, returning one record per applicant." | does not continue his partner-vs-in-house question | value line on that choice
dave-roberts-421a6540 | M2 | "For your team a flag is a referral trigger on large gaps only, set above the estimate's error, and the underwriter decides." | lane note pasted as copy | own wording
nick-telfer-191b2419 | M2 | "For a specialist team the scan returns 80+ body measurements, under 45 seconds from the photos to structured results." | bolt-on 80+; "for a specialist team" ties nothing; does not continue his question | value line on build-dependent features
nick-telfer-191b2419 | M2 | "A call is easy to fit in:" | near-same closer as dave-roberts ("A call is easy to arrange:") | fresh closer
harpreetsarna | M1 | "As a doctor and Chief Medical Officer, you would ask what a software estimate of weight can and cannot be used for before it touches a VitalityLife application." | presumed reaction; question is a near-verbatim lane note | open from his remit
harpreetsarna | M2 | "Call, or point me to whoever leads underwriting philosophy:" | terse, not a call-offer sentence; CMO is the buyer, easy-out unneeded | plain call offer
jonathan-manning-64b26339 | M2 | "Delivery effort is learned in the evaluation, where completion for the photo step is measured and the record goes to LV= systems only." | clunky; does not answer his scheduling question | value line on scheduling
jonathan-manning-64b26339 | M2 | "If a call is simpler, book here:" | "simpler" than what | plain call offer
martyn-luke-22623548 | M2 | "For planning, the scan returns 80+ body measurements, under 45 seconds from the photos to structured results." | bolt-on 80+ (twin already known); does not continue the adviser-testing question | value line on adviser testing
annabel-banks-dataandbiprofessional | M2 | "I can take your questions on a call, or be pointed to the right reviewer:" | clunky passive | plain call offer, easy-out separate
stephanie-richards77 | M2 | "Calendar here, or point me to whoever owns the adviser application journey:" | "Calendar here" is not a call offer | plain call offer
emma-coleman-072400219 | M1 | "As a Life Development Underwriter at Zurich, a build rule is one of the inputs you could be asked to shape." | dangling modifier; muddled | grammatical opener
emma-coleman-072400219 | M2 | "A live rule can be reviewed against what the flag did, and shadow counts by threshold would give a baseline first." | clunky | plain value line
pete-sanderson | M2 | "For queue planning, the scan returns 80+ body measurements, under 45 seconds from the photos to structured results." | 80+ unrelated to queue planning (twin already known) | value line on the operating measure he picks
ali-law-b65291 | M2 | "A REST API returns the record to the underwriting workbench as structured data." | asserts direct workbench delivery, which depends on The Exeter's integration | state what the API returns, not where it lands
damion-m-41537a21 | M1 | "With SQL, SSIS and Power BI behind you, a new feed at Shepherds Friendly is a modelling question before anything else." | dangling modifier | grammatical opener
damion-m-41537a21 | M2 | "Walk through the integration with me:" | imperative, not a call offer | plain call offer
daniel-simpson-340ab860 | M1 | "Product and rating roles before Shepherds Friendly put evidence cost and loadings side by side in your view of income protection." | contorted | plain opener
daniel-simpson-340ab860 | M1 | "How would you weigh the cost of extra build evidence against the loadings it could change?" | near-verbatim lane-note (pricing) | own wording
daniel-simpson-340ab860 | M2 | "An evaluation shows how many cases carry a flag at each threshold, which is the volume your cost question turns on." | attributes Katerina's question to him | neutral reference
daniel-simpson-340ab860 | M2 | "Commercial terms are easier to cover on a call than in a message." | volunteers pricing talk in cold copy | drop
daniel-simpson-340ab860 | M2 | "3DLOOK has worked with 100+ clients." | bolt-on number | drop
nic-herbert-aa587a170 | M2 | "Walk through the integration on a call:" | imperative fragment | plain call offer
darren-wing-05376920 | M1 | "Over thirty years in financial services IT, change and incident management included, means you know what a new component in the application asks of service management." | ungrammatical subject | grammatical opener
kristiansc | M1 | "One such step is FitXpress, which takes two photos in the application and returns a timestamped record to the platform with a Smart Scales weight estimate, flagged only above the insurer's threshold." | flag attached to the estimate | state the flag is on the gap
kristiansc | M1 | "What does a partner step need to show before UnderwriteMe's product operations would take it to insurers?" | same central question as existing Sai Tejo Kiran | question on product operations once live
alanpich | M1 | "Your record is API platforms." | clunky; "record" collides with the product's record | plain opener
alanpich | M2 | "SDK detail covers web and mobile." | fragment | plain technical line
paulrmburu | M2 | "Call, or point me to whoever runs insurer relationships on the platform:" | terse, not a call-offer sentence | plain call offer, easy-out separate
himal-patel-0020901 | M1 | "Enterprise architecture at Pacific Life Re decides how any new evidence source would reach a client insurer's application and the systems behind it." | overclaims a reinsurer EA's control over client insurers | scope to his own estate
himal-patel-0020901 | M2 | "Diary link, if a call is easier than email:" | LinkedIn, not email; weak offer | plain call offer
hannahrothery | M2 | "The test is cheap: one client, a shadow evaluation, and flag counts at each candidate threshold with no effect on any case." | near-twin of charlesking001 M2; "cheap" is a cost claim | distinct value line, no cost wording
richardedwardpurcell | M1 | "How do you decide which insurtech ideas are worth taking to an insurer?" | same central question as existing Réka Halász and Mala Thurston | distinct question
matthew-barclay-63a65412a | M1 | "Your background in financial risk and model development suggests a first question about inputs, for Pacific Life Re's clients." | contorted | plain opener
matthew-barclay-63a65412a | M2 | "An evaluation reads as inputs and agreement:" | contorted | plain value line
alan-dott-b28527131 | M1 | "The Director of Underwriting at Pacific Life Re sees how many client cases are decided at the point of sale with build only declared." | addresses the recipient in the third person | second person
daragh-b-8075581a | M2 | "A shadow evaluation would report flagged cases at each candidate threshold, with nothing touching a live case." | near-twin of alan-dott M2 and existing David Waters | value line from his risk-framework question
emma-denby-4836a78 | M1 | "What would you need to see in flagged cases to judge the evidence informative?" | stiff | plain question
gideoncheok | M2 | "The build is an API with web and mobile SDKs, and one timestamped record per applicant returns to the platform." | "build" reads as body build here | other noun
david-brownlow-ca-chartered-insurer-dippfs-b285b116 | M2 | "3DLOOK has worked with 100+ clients." | bolt-on number | drop
david-brownlow-ca-chartered-insurer-dippfs-b285b116 | M1 | "You moved from finance at Hannover Re's UK branch to lead L&H data operations and solutions globally, which puts a new evidence source in front of you as a data question first." | list-level: data operations heads are excluded by widening item 3; global remit | coordinator: confirm keep or drop
```

## Coordinator review

agreement: ✅ agree — my own full read of Royal London and Aviva found the same layers (maxim openers, one evaluation value line, easy out glued to the calendar link), and the strict-gate diagnostic confirmed the call-line defects.
top_issue: One M2 value line (shadow evaluation counts flags per threshold) carried ~35 of 108 new pairs, on top of the 10-26 set; fixed by per-company quotas and a value line tied to each person's own M1 question (fix-rules-r1 C2), plus per-batch fix files built by script from this list, strict-new.txt and scan-r0.txt.
