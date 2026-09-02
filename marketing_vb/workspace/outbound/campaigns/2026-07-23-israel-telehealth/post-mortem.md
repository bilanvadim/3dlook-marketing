# Campaign Post-Mortem — 2026-07-23-israel-telehealth

- **Profile:** katya (Kateryna Boichuk) | **Product:** FitXpress | **Market:** Israel
- **Analyst pass:** 2026-09-02, on `metrics-final.json` (pulled 2026-09-02T21:10Z) + `responses-classified.csv` (22 rows / 18 unique people, re-classified today on complete data)
- **Written hypothesis:** none. See "No hypothesis existed" below — this is a finding, not a missing input.

## TL;DR (3 строки)

1. **The headline numbers are not this campaign's.** `metrics-final.json` merges two Closely campaigns: `138170` (" Israel telehealth, 24/07 test from agents ", created 2026-07-24, copy = this folder's `messages/*.md`) and `125317` ("Israel top wellness use case c-level", created **2026-04-04**, GPT1/GPT2/GPT3 copy that exists nowhere in this folder). The folder's own campaign is **127 invites → 38 accepted (29.9%) → 73 messages → 4 replies (5.5% on messages sent), 0 interested.** The 608/186/432/34 funnel is 79% April campaign.
2. **All 4 qualified leads came from the April campaign, and they have been sitting unworked for 95-144 days** (replies dated 2026-04-11 → 2026-05-30, first surfaced 2026-09-02). Two of them handed over personal email addresses. Nothing in this directory shows a sales handoff.
3. **The one hard, well-powered learning:** the first message after acceptance replies at **27/175 (15.4%)**, every follow-up at **6/257 (2.3%)** — a ~7x gap across 432 messages. Second- and third-touch messages are near-worthless in this market. The second learning, directional: **6 of 18 repliers (33%) answered "wrong person / not my scope"** — a list problem, not a copy problem, and 8 of them had already declined in April yet were re-imported in July because `katya-registry.json` was empty.

## Measurement integrity — read this before any number

Three defects change what can be claimed. All three are verifiable in the files.

**1. `metrics-final.json` merges an unrelated April campaign into this folder.**

| Closely id | `created_at` | Name | Copy source | Invites | Accepted | Msgs | Replies |
|---|---|---|---|---|---|---|---|
| `125317` | **2026-04-04** | "Israel top wellness use case c-level " | custom columns `GPT1`/`GPT2`/`GPT3` + `about`/`headline`/`company_about` enrichment — **not in this folder** | 481 | 148 (30.8%) | 359 | 30 |
| `138170` | **2026-07-24** | " Israel telehealth, 24/07 test from agents " | `message_1`/`message_2` columns matching `closelyhq-import.csv` and `messages/b01-1.md` verbatim | 127 (+2 errors) | 38 (29.9%) | 73 | 4 |

Proof it is a different campaign, not an earlier batch of this one: (a) `created_at` is 3.5 months before `LAUNCH.md`; (b) its import mapping is `custom_6711: GPT1, custom_6712: GPT2, custom_19666: 'GPT3 '` against `linkedin`/`full_name`/`headline` columns, versus `138170`'s `message_1`/`message_2`/`first_name`/`last_name`/`company`; (c) its sample copy — *"Noticed Clalit is committed to innovative health solutions... FitXpress to help health funds leverage AI-powered body measurements"* — is not any of the 215 files in `messages/`, and it uses "AI-powered body measurements" with no outcome attached, which `context-pack.md` bans; (d) 14 of its 15 in-folder replies are dated before the folder's own campaign was created.

Israel is the only campaign in the account with this defect. `2026-07-31-uk-telehealth-digital-health` also merges two ids, but both were created 2026-08-04/05, days after that folder — plausibly one launch split in two.

**2. 15 of 18 classified repliers never received this folder's copy.** Every per-reply note in `responses-classified.csv` and `responses-summary.md` that says *"Said yes to msg1's chat ask"* and cites a `messages/*.md` thread is wrong for the `125317` rows. Those people answered April's GPT copy; the `messages/*.md` file was written in July for the same person and may never have been delivered. Concretely: **Ron Weksler and Ben Ron did not see the member-engagement message** they are credited with responding to. This invalidates angle-level attribution for 15 of 18 repliers — see "Worst-performing angle" for what that costs us.

It also resolves the mismatch the classifier flagged as unexplained: **Hedva Voliovitch's "I have never worked at Madaness insurance company"** is a response to April's copy, whose company field came from a `company_about` enrichment column, not from our `people-validated.csv` (which correctly says Maccabi). Our `messages/b02-25.md` is not the message she is objecting to. Data hygiene issue in the April list, not in ours.

**3. Denominators do not line up with this folder's people files.**
- `people-to-sequence.csv` = 215 people; `closelyhq-import.csv` = 215 rows but only **190 with a LinkedIn URL** (`LAUNCH.md` names only 8 as missing — it undercounts by 17). Closely saved 186 and skipped 29 as `invalid linkedin_url value` / `invalid last_name value`. Of the 186 saved, only **130 entered the campaign and 127 got an invite** — 59 of our 215 (27%) never received anything.
- Conversely, `125317` held 484 saved contacts, of which only 15 repliers appear in this folder's people files at all. 20 further raw replies were correctly dropped by the classifier for exactly that reason.
- Practical effect: **per-segment reply rates cannot be computed.** Numerators come from one population, denominators from another. Everything below is either (a) within-replier composition (N=18, no denominator needed), or (b) explicitly flagged as an approximation.

**4. Two smaller corrections to the inputs.**
- `responses-summary.md` says "10 declines from 8 unique people" (and the brief inherited it). The CSV has **10 decline rows across 9 unique people** — its own prose lists 9 names. Ilan Marcuschamer, Hedva Voliovitch, Inbal Rush, Amir Sheinfeld, Yael Wolff Sagy (2 rows), Ariel Braverman, Etti Rosenberg, Gali Atar, Netanel Friedman.
- The `note` field inside `metrics-final.json` says the registry `sent` column "overstated this campaign by up to 2x". Direction and magnitude are both wrong here: registry `sent` = 190 vs 608 actual, i.e. **understated by 3.2x**, precisely because two campaigns are merged. (It does overstate elsewhere — EU weightloss 307 vs 292.) Worth fixing the wording so the next analyst is not misled.

## No hypothesis existed

There is no `hypothesis.md` in this directory. `outbound-registry.py status` records the campaign as `9 · metrics ... [skipped: hypothesis,companies,sales-nav]` — three pipeline steps were skipped, and the hypothesis was one of them. `context-pack.md` was used instead: it supplies ICP segments A-F, approved claim ids FX-001..FX-008, banned claims, the HMO procurement note and the katya tone note — but **no numeric target for acceptance, reply rate or lead count, and no statement of what the campaign was trying to prove.**

That is itself the most consequential process finding: there was nothing to measure against, so nothing could fail, so nobody looked at the campaign for six weeks while four warm HMO leads went cold. Every verdict in the next table is therefore scored against a **retro-fitted baseline** — the median of the four other agent-built campaigns in the account. A retro-fitted baseline is not a target and cannot be used to say the campaign "hit" anything; it only says whether this campaign is normal for us.

## Hypothesis vs reality

Scored on the folder's own campaign (`138170`), the only one whose copy and list this directory actually owns. Baseline = median of the 4 other agent campaigns.

| Metric | Target | Baseline (median, n=4) | Actual (`138170`) | Verdict |
|--------|--------|------------------------|-------------------|---------|
| Acceptance rate | none stated | 21.2% | **38/127 (29.9%)** | ✓ vs baseline — best of the five |
| Reply rate on messages sent | none stated | 8.6% | **4/73 (5.5%)** | ✗ 4th of five |
| Reply rate on accepted | none stated | 14.3% | **4/38 (10.5%)** | ✗ 4th of five |
| Positive replies (interested + question) | none stated | 2.5 | **1** (Guy Sade, question) | ✗ |
| Qualified leads (interested) | none stated | 2.5 | **0** | ✗ |
| Negative / hostile replies | none stated | 0 | **0** | ✓ |
| CPL | none stated | — | **not computable** | — |

For completeness, the merged figure that the brief quotes, and the April campaign on its own:

| Funnel | Merged (`metrics-final.json`) | `125317` April (not ours) | `138170` July (ours) |
|---|---|---|---|
| Invites sent | 608 | 481 | 127 |
| Accepted | 186 (30.6%) | 148 (30.8%) | 38 (29.9%) |
| Messages sent | 432 | 359 | 73 |
| Replies | 34 | 30 | 4 |
| Reply rate on msgs | 7.9% | 8.4% | 5.5% |
| Reply rate on accepted | 18.3% | 20.3% | 10.5% |
| Replies classified in this folder | 18 people | 15 people | 3 people |
| Interested | 4 | **4** | **0** |

**CPL cannot be computed.** Missing: Closely seat cost for Apr-Aug, the LinkedIn Premium/Sales Nav line for the katya profile, and the agent run cost for steps 3-8. With 4 interested against unknown spend, any CPL number would be invented. To get it next time, record three figures in `hypothesis.md` at launch: tool cost/month, seat cost/month, and campaign duration.

## Что работало

### Best-performing message *step* (the one finding with real statistical power)

Not an angle — a position in the sequence. Reply events are attributable to steps in `metrics-final.json` by graph position (a `message` step whose `prev_step_id` is a `condition` is a first touch; one whose parent is a `post_reaction` is a follow-up).

| Step position | Sent | Replies | Rate |
|---|---|---|---|
| First message after acceptance | **175** | **27** | **15.4%** |
| All follow-ups (+3d, +5d, both campaigns, all branches) | **257** | **6** | **2.3%** |
| Connection-request note | 608 | 1 | 0.2% |

Consistent in both campaigns independently: April 24/137 (17.5%) first vs 5/222 (2.3%) follow-up; July 3/38 (7.9%) first vs 1/35 (2.9%) follow-up. This is level **15+** (N=432 messages, 33 replies) and it is copy-independent — it holds across two entirely different message sets. It is the most transferable thing this campaign produced.

Corroborated by the raw data from the other direction: **20 of 22 reply rows are `which_message_replied_to = 1`.** Only Guy Sade and Patti Zohar replied to message 2.

### Best-converting company segments

**Level: 15+ for composition, but there is no valid denominator — treat as description, not as a rate.**

All 18 repliers sit in two segments: `context-pack.md` **segment C (Health Plans / HMOs)** with 16, and **segment B (RPM/telehealth vendors)** with 2 (both TytoCare).

| Company | Repliers | Interested | Question | Maybe-later | Decline |
|---|---|---|---|---|---|
| Clalit Health Services | 8 | 1 | 1 | 2 | 4 |
| Maccabi (both spellings) | 7 | **3** | 0 | 0 | 4 |
| TytoCare | 2 | 0 | 1 | 0 | 1 |
| Meuhedet Health Services | 1 | 0 | 0 | 1 | 0 |

**Segment does not discriminate here.** Segment C produced all 4 interested *and* 8 of 9 declines, because 16 of 18 repliers were segment C. Maccabi 3/7 interested vs Clalit 1/8 is directional at best (N=7 and N=8, level 5-14) and both leaned on the same April copy. Leumit (10 sequenced) and every tier-2/tier-3 company except TytoCare produced **zero replies** — that is a fact about 0 events, not a finding about those companies.

The honest version: the two statutory giants, Clalit and Maccabi, are where the entire signal is, and the entire signal came from an April campaign whose copy we do not have.

### Best-performing personas (titles)

**Level: 15+ (N=18 repliers). This is the strongest list-quality finding, and it has an unusually clean property: the `buyer_role` labels were assigned by `icp-validator` on 2026-07-23, blind to the April outcomes it is being scored against.**

Within-replier composition by the `buyer_role` label in `people-to-sequence.csv`:

| `buyer_role` label | Repliers | Interested | Maybe-later | Question | Decline |
|---|---|---|---|---|---|
| **Champion** | 8 | **4** | 2 | 0 | 2 |
| Influencer | 7 | **0** | 0 | 1 | 6 |
| Decision maker | 1 | 0 | 0 | 0 | 1 |
| Not relevant (validated-only, not sequenced) | 2 | 0 | 1 | 1 | 0 |

**All 4 interested carry the Champion label; 0 of 7 Influencers and 0 of 1 Decision-maker did.** Six of seven Influencer repliers declined.

Base-rate note, flagged as an approximation because the denominator is our 215-person list while most numerators came from April's 484-person list: Champions were 59/215 (27%) of our list but 8/18 (44%) of repliers and 4/4 of interested; Influencers were 112/215 (52%) of the list but 0/4 of interested; Decision-makers were 44/215 (20%) and produced 1 reply. If that survives replication, the Decision-maker cohort — the most senior HMO names — is the least responsive third of the list, and the Champion cohort is worth over-weighting.

What "Champion" actually meant in practice, for the 4 who converted:

| Person | Title | Company | Why it works |
|---|---|---|---|
| Olchov Zhanna | Medical Director, Maccabi Health Service | Maccabi | Org-wide clinical authority, not one department |
| Yaron Sheffer | Head of Strategy & Business Development | Clalit | Cross-cutting; evaluating partnerships is the job |
| Ron Weksler | Board Member | Maccabi | Board-level, judges relevance himself |
| Ben Ron | Marketing Director, Maccabi Optic | Maccabi | Member-facing/commercial, owns engagement |

Hypothesis why: three of the four hold **cross-cutting mandates** (organisation-wide clinical, strategy/BD, board) and the fourth owns **member-facing engagement**. FitXpress is a horizontal data layer; only people whose remit crosses departments can see where it lands. Sample replies: *"Yes, with a pleasure"* (Zhanna), *"Yes sure"* (Sheffer), *"Please send me some more information to my email so I can see if it's relevant"* (Weksler), *"Do you have a presentation on that matter you can mail me?"* (Ben Ron).

Caveat that kills the simple version: **"Board Member" is not a persona.** Three board members replied — Ron Weksler (interested), Hedva Voliovitch (decline), Yael Shaham/Ben Atar (maybe-later, "outside my role"). 1/3. Do not build a next campaign on board seats.

### Other things that worked

- **Acceptance, on its own merits.** 29.9% for the folder's campaign and 30.6% merged — best of the five campaigns in the account either way. A no-note connection request into Israeli HMOs converts about 3 in 10. That is a real, repeatable asset.
- **Tone and compliance discipline.** 0 negative/hostile replies out of 22 rows (LinkedIn has no unsubscribe event, so that is the only available signal). Several declines were warm (*"I appreciate you reaching out and wish you success with the initiative"*). The katya voice and the `israel_procurement_note` instruction not to push urgency were followed and cost us nothing.
- **The one substantive engagement with our own copy** was Guy Sade (Senior Director, Account Management, TytoCare) asking *"Does your product has FDA / CE approvals?"* at message 2. That is a buying-committee question from the RPM/telehealth segment and the only evidence in this campaign that the folder's copy can start a real conversation.

## Что не работало

### Worst-performing angle — and why we cannot name it

**Level: <5 for the folder's copy. Angle attribution is not available and must not be faked.**

The campaign has no A/B structure: all 215 `messages/*.md` files carry a different hand-built hook. Grouping them into themes gives at most 4 reply events per theme, and — decisively — **only 3 of 18 repliers received any of this folder's copy at all.** Anything computed across the 18 attributes April's GPT copy to our July files.

What the folder's copy actually produced, all 3 rows, as facts:

| Person | Our angle (from `messages/`) | Outcome |
|---|---|---|
| Guy Sade — Sr Director Account Mgmt, TytoCare | API / integration ("expanding the remote exam kit with new modules") | question (FDA/CE), at message 2 |
| Netanel Friedman — Head of Finance / FP&A, TytoCare | API / integration | decline: *"not something that's relevant to our current priorities or business model"* |
| Yael Shaham / Ben Atar — recorded as Board Member, Clalit (`b01-4.md`) | member engagement at population scale | maybe-later: *"this is outside my role at Clalit, so I'm not the right person"* |

Two of our three repliers said, in different words, *wrong person*. An API/integration angle went to a **finance** lead. A board-level population-health angle went to someone who says she is not in that role. That is 2/3 (level <5 — quote it, do not generalise it) and it points the same direction as the 18-person analysis below.

One observation that argues against over-investing in bespoke hooks, offered strictly as a hypothesis: the single most generic message in the whole set — Zhanna's *"Caught my eye - the potential for mobile body scanning in Maccabi Health care Services's telehealth programs"*, essentially a mail-merge line — belongs to the campaign's best reply. She was on the April list too, so we cannot even be sure she read it. **The next campaign should stop guessing and run two named variants with a recorded split**, which this campaign made impossible.

### Pattern in negative responses

**Level: 15+ (N=18 repliers, 9 declines + 1 role-mismatch maybe-later). This is the finding to act on.**

Zero of 22 rows are hostile. The 9 declines are polite, and their *stated reasons* cluster hard:

| Stated reason | People | Quotes |
|---|---|---|
| **Wrong person / not my scope** | **6 of 18 (33%)** | *"This isn't related to my position in Clalit"* (Yael Wolff Sagy); *"Not my subject"* (Gali Atar); *"I'm working in a lab that does blood tests... No need for AI, or any physical check"* (Inbal Rush); *"this is outside my role at Clalit"* (Yael Shaham/Ben Atar); *"I have a hard time seeing any relevance"* (Ariel Braverman); *"Not relevant for me at the moment"* (Ilan Marcuschamer) |
| Company-level fit | 1 | *"not relevant to our current priorities or business model"* (Netanel Friedman, TytoCare) |
| No capacity / already has a programme | 1 | Etti Rosenberg, who described Clalit's own burnout/wellbeing survey work |
| Bad record on our side | 1 | Hedva Voliovitch, denying an employer we never attributed to her (April's data) |
| No reason given | 2 | *"No, thank you"* (Amir Sheinfeld, and Yael Wolff Sagy's first line) |

**One third of everyone who replied told us we had the wrong person.** Not one decline disputed the product, the claims, the accuracy numbers, or the price. That is a targeting failure, and it is a *good* outcome to discover, because targeting is the cheapest thing in the pipeline to fix.

**Answering the specific question — did the accepted-but-declined group share a title pattern? Yes, and it is sharp:**

| Title cohort | Repliers | Interested | Declines |
|---|---|---|---|
| Head/Director of **one specific department** (virology lab, child development services, cardiac rehab centre, occupational-health nursing, research & information) | 6 | **0** | **6** |
| Data & AI delivery | 1 | 0 | 1 |
| Finance / FP&A | 1 | 0 | 1 |
| Board member | 3 | 1 | 1 |
| Medical Director (org-wide) | 1 | 1 | 0 |
| Strategy & BD | 1 | 1 | 0 |
| Marketing | 1 | 1 | 0 |
| Account management | 1 | 0 | 0 |

**Six of nine declines are narrow departmental heads, and departmental heads produced zero positive replies.** Approximate base rate, same denominator caveat as above: **89 of 215 sequenced people (41%) were narrow departmental or clinical unit heads.** Nearly half the list was people whose job has no room for a horizontal body-data layer, and they answered by saying so.

Why the highest acceptance rate and the highest absolute decline count go together: both are downstream of the same thing. Departmental heads at statutory HMOs are flattered by a connection request from a BD person and accept it (30% acceptance), then discover the message is about something outside their remit and politely close it. **Acceptance rate is not a quality signal in this market — it measures LinkedIn politeness, not fit.** Reply-per-accepted is the metric to steer by, and there Israel (10.5% for our campaign) sits below UK (18.8%), US (15.4%) and AU (13.2%).

### Companies / people we shouldn't have included

- **8 people who had already declined in April were re-imported in July.** All 8 April decliners who had a LinkedIn URL — Ilan Marcuschamer, Hedva Voliovitch, Inbal Rush, Amir Sheinfeld, Yael Wolff Sagy, Ariel Braverman, Etti Rosenberg, Gali Atar — are present in `closelyhq-import.csv`. Marcuschamer and Braverman are literally rows 1 and 2 of `138170`'s import sample in `metrics-final.json`. Root cause is documented in our own `context-pack.md`: *"exclusions... status: empty — no prior campaigns, no excluded companies/people yet for this profile"* — the April campaign was never recorded in `katya-registry.json`, so `icp-validator` had no way to know. Not the validator's fault; a registry gap.
- **The 4 April interested were re-invited cold too** (Zhanna, Ben Ron, Sheffer, Weksler are all in the July import). Re-approaching someone who said *"Yes, with a pleasure"* four months earlier with a fresh cold opener is worse than not contacting them.
- **89 of 215 narrow departmental/clinical unit heads** (see above) — not company exclusions, a title filter that should have run.
- **25 of 215 import rows had no LinkedIn URL** and were dead on arrival; Closely skipped 29 rows outright.
- **`Yael Shaham` / `/in/yael-ben-atar-8aba53228` is a bad record, not just a name change.** The URL slug says `yael-ben-atar`, our files say "Yael Shaham", Closely says "Yael Ben Atar", and her reply says she is not in the role we assigned her ("Board Member"). The slug agrees with Closely, so **our name and probably our title are the wrong ones** — she received a board-level message on the strength of an incorrect record. Needs a manual profile check before any re-approach.
  - Separately: `/in/yaelsagy` recorded as "Yael Wolff" and replying as "Yael Wolff Sagy, PhD" is a **benign** fuller-name variant (the slug matches "Sagy"), not a mismatch. The brief merged these two Yaels into one issue; they are different people with different problems.
- **Assi cicurel and Patti Zohar exist only in `people-validated.csv`, not in the sequence or the import** (no LinkedIn URL on file), and both are `icp_fit: none` / `buyer_role: Not relevant`. They replied to April's campaign. Their outcomes will not be written to the registry (confirmed below) and both are `confidence: low` with no thread on disk. Do not act on them without a manual LinkedIn check — but note the irony that the two "not relevant" people produced a question and a maybe-later while 112 Influencers produced six declines.

### The process failure that cost the most

Four people said yes in April and May. They were surfaced on 2026-09-02. **Latency: 144 days (Zhanna, 2026-04-11), 133 (Ben Ron, 04-22), 127 (Sheffer, 04-28), 95 (Weksler, 05-30).** Two supplied direct email addresses — `benr@mor.org.il`, `Wekslerrs@gmail.com` — and got no reply. `responses-summary.md` names the mechanism: the earlier pull read Closely's *inbox listing*, which surfaced 4 rows; the per-campaign contact drill surfaced 22. A reply-detection method that misses 80% of replies, on a pipeline with no scheduled reply check, is how four HMO leads in a market of four buyers go cold. There is no handoff artifact of any kind in this directory.

## Cross-campaign comparison

No prior `post-mortem.md` exists anywhere in `workspace/outbound/campaigns/` — **this is the first one in the account**, so there are no previous learnings to confirm or contradict. Comparison is against the raw metrics of the other four campaigns.

As the brief framed it (merged Israel number):

| Campaign | Invites | Accept% | Msgs | Replies | Reply% on msgs |
|---|---|---|---|---|---|
| Israel (merged) | 608 | 30.6% | 432 | 34 | 7.9% |
| EU weightloss | 292 | 25.0% | 119 | 4 | 3.4% |
| UK digital health | 258 | 26.7% | 94 | 13 | 13.8% |
| US fitness | 245 | 15.9% | 67 | 6 | 9.0% |
| AU telehealth | 220 | 17.3% | 61 | 5 | 8.2% |

Corrected — Israel split, and with the two denominators that actually compare:

| Campaign | Invites | Accept% | Msgs | Msgs per accepted | Replies | Reply% on msgs | **Reply% on accepted** | Interested (classified) |
|---|---|---|---|---|---|---|---|---|
| **Israel `138170` (ours, 24/07)** | **127** | **29.9%** | **73** | 1.9 | **4** | **5.5%** | **10.5%** | **0** |
| Israel `125317` (April, not ours) | 481 | 30.8% | 359 | 2.4 | 30 | 8.4% | 20.3% | 4 |
| EU weightloss | 292 | 25.0% | 119 | 1.6 | 4 | 3.4% | 5.5% | 0 |
| UK digital health | 258 | 26.7% | 94 | 1.4 | 13 | 13.8% | **18.8%** | 4 |
| US fitness | 245 | 15.9% | 67 | 1.7 | 6 | 9.0% | 15.4% | 1 |
| AU telehealth | 220 | 17.3% | 61 | 1.6 | 5 | 8.2% | 13.2% | **6** |

Three things fall out:

1. **"Half of all replies in the account" belongs to the April campaign, not to agent work.** Of 34, 30 are `125317`'s. Agent campaigns produced 4 (Israel), 13 (UK), 6 (US), 5 (AU), 4 (EU).
2. **"Reply rate on messages sent" is a misleading league table** because it is diluted by how many follow-ups a campaign sent — and follow-ups reply at 2.3%. Israel sent 2.32 messages per accepted contact, UK 1.36. On reply-per-accepted, Israel merged (18.3%) and UK (18.8%) are level; UK's apparent 13.8%-vs-7.9% advantage is largely an artifact of sending fewer follow-ups. **Adopt reply-per-accepted as the headline reply metric.**
3. **AU is the most efficient campaign in the account and nobody has noticed**: 6 interested from 220 invites and only 38 accepted (2.7 interested per 100 invites) versus UK 1.55 and Israel 0.66 (floor — see caveat). AU's list was small and well-chosen. It deserves the next post-mortem more than the volume campaigns do.

Caveat on Israel's interested count: 4 is a **floor, not a total.** ~16 of the 34 reply events belong to `125317` contacts who are in none of this folder's files and were never classified. The true Israel interested count is ≥4 and unknown, and it lives in the April campaign either way.

## Learnings → next hypothesis

### Confirm

- **Israeli statutory HMOs accept connection requests at ~30%** — the best top-of-funnel in the account, replicated independently across two campaigns four months apart (30.8% / 29.9%). Segment C is a real market; keep it in core ICP.
- **The first message after acceptance is where the campaign lives: 27/175 (15.4%) vs 6/257 (2.3%) for all follow-ups.** N=432 messages. Copy-independent.
- **The `buyer_role: Champion` label predicts positive outcomes; `Influencer` and `Decision maker` do not.** 4/4 interested were Champions; 6/7 Influencer repliers declined. The labels were assigned blind to the outcomes, which makes this an unusually clean validation of `icp-validator`'s scoring. Directional (18 repliers, 4 interested) but worth acting on now.
- **Cross-cutting mandates convert, narrow departmental scope does not.** Medical Director (org-wide), Head of Strategy & BD, Marketing Director: 3 of 4 interested. Departmental/clinical unit heads: 0/6 positive, 6/6 decline.
- **The katya tone and the HMO procurement guidance are correct.** 0 hostile replies in 22, warm declines, no complaints. Keep `israel_procurement_note` as written.
- **`context-pack.md`'s banned-claims list earned its keep.** Guy Sade's FDA/CE question was answerable inside the approved boundary precisely because the constraint was written down before it was needed.

### Reject

- **Acceptance rate as a success metric.** In this market it measures politeness. It moved *inversely* to lead quality: highest acceptance in the account, highest absolute declines, zero interested from our own copy.
- **Narrow departmental/clinical unit heads at HMOs** — Head of Virology, Head of Child Development Services, Director of a rehabilitation centre, Occupational Health Director of Nursing, Head of Research & Information. 41% of the list, zero positives, and the most common reply we got was "not my subject." Add a title filter.
- **Finance / FP&A titles as a first touch.** 1/1 decline on business-model grounds. N=1, so this is not a conclusion — but pairing a finance title with an API-integration angle was a clear mistake and should not repeat regardless.
- **"Board Member" as a target persona.** 1 interested / 1 decline / 1 maybe-later. Unpredictable; also the cohort where our records were worst.
- **Follow-up sequences of 2-3 messages as currently written.** 257 follow-ups bought 6 replies. Either rewrite them completely or cut to a single follow-up and spend the sending capacity on new first touches.
- **Reply detection via Closely's inbox listing.** It surfaced 4 of 22.

### New hypotheses to test

- **H1 — Champion-only list.** A 100-person Israel list restricted to `buyer_role: Champion` with cross-cutting titles (Medical Director org-wide, Head of Strategy/BD/Innovation/Digital, Head of Member Engagement, Marketing/member-facing directors) will produce ≥3 interested per 100 invites, versus 0.66/100 for this mixed list. Explicitly excludes single-department clinical and lab heads.
- **H2 — First-touch concentration.** Reallocating follow-up capacity into first touches raises interested-per-100-invites without lowering reply-per-accepted. Test: one follow-up maximum, and the +5d message rewritten to add new information rather than restating message 1 with a calendar link.
- **H3 — Named copy variants with recorded assignment.** Two variants only — (a) member-engagement/retention, (b) verification/audit-readiness (the `context-pack.md` line for HMOs; it was written for 27 people in this campaign and appears in **zero** of the 22 replies — though delivery cannot be confirmed, since only 73 of the folder's messages were sent) — assigned in the import CSV and recorded in `hypothesis.md`, so the next post-mortem can actually name a winning angle. This campaign could not.
- **H4 — Personalisation depth is not the lever.** The campaign's best reply came from its most generic hook. Test a mail-merge-grade opener against a hand-built one within the same title cohort; if there is no difference, step 7 of the pipeline can be cheapened dramatically.
- **H5 — Innovation-arm entry beats direct departmental entry.** `context-pack.md` already flags Clalit Innovation (Tech.Mate) and Maccabi Health Tech/MDClick as preferred entry points, and the one Clalit Innovation physician who replied asked a genuine top-of-funnel question. Only 11 people got an innovation/pilot angle. Test segment E properly with 30-40 contacts.
- **H6 — Speed of reply handling dominates copy quality.** Four leads decayed for 95-144 days. A campaign with a 48-hour reply-check SLA will convert more of the same replies than any copy change. Measure: time-to-first-response per reply.

## Recommendations for next campaign

1. **Work the four April leads today, before anything else.** Deck to `benr@mor.org.il` (Ben Ron) and `Wekslerrs@gmail.com` (Ron Weksler); calendar link to Olchov Zhanna and Yaron Sheffer. Open by acknowledging the delay — four months of silence needs naming, not glossing. These are the only qualified HMO leads the account has in Israel.
2. **Answer Guy Sade (TytoCare) inside the banned-claims boundary** — not FDA-cleared, not a medical device, HIPAA-compliant/GDPR-aligned, audit-ready. `responses-classified.csv` has an approved draft. This is the only live conversation the folder's own copy created.
3. **Split `metrics-final.json`.** Move `125317` out of this folder into its own retro-documented campaign directory, or at minimum add per-campaign rate blocks so nobody quotes the merged funnel again. Fix the `note` field's "overstated ... by up to 2x" wording. Then have `closely-pull.py` refuse to merge Closely campaigns whose `created_at` differs from the folder date by more than ~14 days without an explicit override.
4. **Register `125317` in `katya-registry.json` and write its outcomes** so April's 8 decliners and 4 interested stop being invisible. Without this, the next Israel campaign re-contacts them again — and `reply` will silently drop Assi cicurel and Patti Zohar, whose only campaign is that one.
5. **Add a title filter to `icp-validator` before the next Israel list**: exclude Head/Director of a single clinical department, lab, or ward unless there is separate evidence of budget or cross-department scope. That is 41% of this list and it produced nothing but declines.
6. **Never launch without `hypothesis.md` again.** This campaign skipped hypothesis, companies and sales-nav, and the missing hypothesis is why it ran six weeks without review. Suggested hard gate: `outbound-pipeline.py` refuses to generate an import CSV when `hypothesis.md` is absent, rather than recording `[skipped: hypothesis]` and continuing.
7. **Fix the import before sending, not after.** 25 of 215 rows had no LinkedIn URL, Closely skipped 29, and only 130 of 186 saved contacts entered the campaign. Add a pre-launch assert: every import row has a resolvable LinkedIn URL, or the row is dropped and counted in `LAUNCH.md` honestly.
8. **Switch the scoreboard to reply-per-accepted and interested-per-100-invites**, and record messages-per-accepted alongside. On the current metric, sending more follow-ups looks like performance.
9. **Schedule reply pulls.** Weekly `closely-pull.py` per live campaign, using the per-campaign contact drill (not the inbox listing), with an alert when an `interested` row is older than 48 hours.
10. **Manually verify `/in/yael-ben-atar-8aba53228`** before re-approach — our name and title for that record disagree with both the URL slug and her own reply.
11. **Post-mortem AU telehealth next.** 6 interested from 220 invites, the best lead efficiency in the account, and no analysis of why.

## Updates to `CLAUDE.md`

Israel is already an active outbound market for the katya profile but is absent from the geo/compliance sections — `context-pack.md` raised this on 2026-07-23 as `geo_compliance_flag` and it is still open. Concrete diff for Vadim to approve (I have not edited `CLAUDE.md`):

```diff
  §4 Geo expansion
+ Israel — active outbound (profile: katya) and social since 2026-07-21. Buyers are the four
+ statutory HMOs (Clalit, Maccabi, Meuhedet, Leumit) plus telehealth/RPM vendors (TytoCare,
+ K Health, Datos, Biobeat) and private insurers (Harel, Migdal, Phoenix).
+ Connection acceptance runs ~30% (two campaigns, 2026-04 and 2026-07) — the highest of any
+ market we run, and NOT a quality signal: steer on reply-per-accepted, not acceptance.

  §12 Compliance summary
+ Israel: HIPAA/GDPR framing is not sufficient on its own — Israel has its own Privacy
+ Protection Law. Outbound to Israeli health organisations has been running since 2026-04
+ without this being confirmed. ACTION FOR VADIM: confirm or document the position.
```

ICP additions, if the Champion finding replicates in one more campaign (not yet — 4 interested is not enough to rewrite core ICP):

```diff
  Segment C — Health Plans / HMOs / Employer Wellness
    buyer_titles: CHRO, Head of Wellness/Wellbeing, CMO, VP Population Health, ...
+   VALIDATED 2026-09 (Israel, n=18 repliers, 4 interested): titles with a cross-cutting
+   mandate convert — Medical Director (organisation-wide), Head of Strategy & Business
+   Development, Marketing/member-facing directors.
+   DO NOT TARGET: heads/directors of a single clinical department, lab or ward (virology,
+   child development, rehabilitation centre, occupational-health nursing, research &
+   information). 41% of the Israel list, 0 positive replies, 6 declines, and their stated
+   reason was consistently "not my subject / not related to my position".
+   Board seats are unpredictable (1 interested / 1 decline / 1 wrong-role of 3).
```

## Updates to the exclusion registry

**Not written.** My spec requires `outbound-registry.py reply` after analysis; the task scope for this run restricts writes to the campaign directory, and that command writes `workspace/outbound/exclusions/katya-registry.json`. I ran it as a dry-run only:

```
$ python3 scripts/outbound-registry.py reply --campaign 2026-07-23-israel-telehealth --profile katya --dry-run
reply (dry-run): 2026-07-23-israel-telehealth -> katya
  18 classified replies, 16 registry people updated, 2 not matched by URL
    [dry-run] would write workspace/outbound/exclusions/katya-registry.json (78811 bytes)
```

**Vadim or the orchestrator must run it without `--dry-run`.** Until then the 6-month release rule (`reply = no_reply` frees a company) has nothing to work with for this campaign. The 2 unmatched are Assi cicurel and Patti Zohar — no LinkedIn URL in our files, never in the import, therefore not in the registry; they are only recoverable by recording `125317` (recommendation 4).

**Exclude — declined, do not re-contact (9 people).** All Tier 1. Eight of these already declined in April and were re-imported in July; that must not happen a third time.

| Person | Title | Company | Basis |
|---|---|---|---|
| Ilan Marcuschamer | Director of Cardiac Rehabilitation Center | Clalit | *"Not relevant for me at the moment"* |
| Hedva Voliovitch | recorded as Board Member | Maccabi | Closed the door; also a bad company record on the April list |
| Inbal Rush | Head of Virology Department | Maccabi | Workflow mismatch — lab, *"no need for AI, or any physical check"* |
| Amir Sheinfeld | Head of Data & AI Delivery | Maccabi | *"No, thank you"* |
| Yael Wolff Sagy, PhD | Head of Research & Information, Strategic Planning Wing | Clalit | *"This isn't related to my position in Clalit"* |
| Ariel Braverman | Occupational Health, Director of Nursing | Clalit | *"I have a hard time seeing any relevance"* |
| Etti Rosenberg | Founder & Director, IOSMC Method | Clalit | Has her own wellbeing programme; not taking collaborations |
| Gali Atar | Head of Child Development Services | Maccabi | *"Not my subject"* |
| Netanel Friedman | Head of Finance / Sr Director FP&A | TytoCare | Business-model mismatch — person-level only, see below |

**Do NOT exclude — nurture (3 people).** Shelly Shumilov Klipper (Meuhedet — left the role, onboarding elsewhere; check her new employer in 2-3 months and re-approach role-specifically), Patti Zohar (Clalit — said she would consult stakeholders and revert; check back 4-6 weeks, `confidence: low`, verify manually), Yael Shaham/Ben Atar (Clalit — verify the record first, then ask her who the right owner is rather than closing her out).

**Do NOT exclude — active (5 people).** Olchov Zhanna, Ben Ron, Yaron Sheffer, Ron Weksler (interested, awaiting handoff), Guy Sade (open question).

**Company-level exclusions: none.** Nothing here justifies excluding a company. Clalit and Maccabi each produced both interested and declined people and remain the two most important accounts in the market — the declines are person-level scope mismatches. TytoCare: Netanel Friedman's *"not relevant to our... business model"* is the closest thing to a company-level signal, but Guy Sade at the same company is asking product questions, so exclude the person, not the account. Nothing goes into `exclusions/global-company-registry.json` from this campaign.

**Registry gap to close:** `context-pack.md` recorded `katya-registry.json` as *"empty — no prior campaigns"* on 2026-07-23 while Closely campaign `125317` had been running against the same Israeli HMOs since 2026-04-04. Whatever produces that registry does not see campaigns launched outside the pipeline. That gap, not the copy and not the ICP, is what caused this campaign's worst outcome.
