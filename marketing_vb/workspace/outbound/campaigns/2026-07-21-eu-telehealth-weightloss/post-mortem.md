---
product: fitxpress
campaign: 2026-07-21-eu-telehealth-weightloss
profile: olena
analyzed: 2026-09-02
metrics_source: metrics-final.json (closely.io /v1/drill/campaigns/137970/*, pulled 2026-09-02T21:10Z)
evidence_tier: "facts-only (4 replies) + cross-campaign corpus census (1,207 sent message-1 texts, 5 campaigns)"
status: draft — awaiting Vadim
---

# Campaign Post-Mortem — 2026-07-21-eu-telehealth-weightloss

## TL;DR (3 строки)

1. **Acceptance was normal (73/292, 25.0% — exactly the target), and then the campaign died at the first message: 1 reply out of 67 people who got message 1 (1.5%).** The other four campaigns averaged 40/299 (13.4%) on the same step (one-sided Fisher p = 0.0017). 0 interested, 0 questions, 3 declines, 0 qualified leads.
2. **The reason is in the text, and it is measurable without touching the reply data: 307/307 message-1 texts sent in this campaign contained zero product specifics** — no "45 seconds", no "80+ measurements", no accuracy figure, no proof point, no named metric. In UK it was 80% / 94% / 32%; in Israel 57% / 78% / 49%; in US 100% / 68% / 0%. All 307 openers came from a pool of 72 interchangeable phrases ("Quick note on something in your space.") and all 307 closed with one of 4 identical meeting asks. Same length as UK (398 vs 377 chars), different payload.
3. **The hypothesis was never tested, so it should not be retired — the message should be.** The cheapest possible re-test already exists: 63 people accepted Olena's invite, received the empty message and stayed silent. They are now 1st-degree connections. Rewrite message 1 and send it to those 63 — same list, same profile, same geo, one variable changed.

## Hypothesis vs reality

| Metric | Target | Actual | Verdict |
|--------|--------|--------|---------|
| Acceptance rate | ≥ 25% | **25.0%** — 73/292 invites | ✓ (on the nose) |
| Reply rate | ≥ 5% | **3.4%** on messages sent (4/119) · **5.5%** on accepted (4/73) · **6.0%** on people messaged (4/67) | ✗ (see denominator note) |
| Positive replies | ≥ 12 | **0** — 0 interested + 0 question, of 4 replies | ✗ |
| Qualified leads | ≥ 4 | **0** | ✗ |
| CPL | — | undefined (0 qualified leads); spend not recorded for this campaign | n/a |

**Denominator note — this is the one place where the choice of denominator flips a verdict.** The
spec formula (`replies / accepted`) gives 4/73 = 5.5% and would score reply rate as a pass. It is a
false pass: only 67 of the 73 accepters were actually messaged, and 0 of the 4 replies carried
interest. On the denominator that describes what actually happened — people who received a
message — it is 4/67 (6.0%), and on Closely's message-event denominator 4/119 (3.4%). Verdict is ✗
on all three because the qualified-lead count is 0 regardless.

**Funnel, from `metrics-final.json` only:**

```
307 contacts imported
 └─ 474 profile visits, 56 post likes (warm-up ran)
 └─ 292 connection requests sent (no note — connection_message payload was "")   1 error
     └─  73 accepted (25.0%)
         └─  67 got message 1  →  1 reply  (1.5%)
             └─  52 got message 2  →  3 replies (5.8%)
                 └─   4 replies from 4 people (5 reply rows; Alex Hill replied twice)
                     └─   0 interested · 0 question · 3 decline · 2 other/unclear (both Alex Hill)
```

Campaign is still `active`: 158 contacts in flight, 6 accepters not yet messaged, 15 messaged people
not yet followed up. A re-pull after the ladder drains moves these denominators by under 5% and
cannot change any verdict above.

## Что работало

### Acceptance — and only acceptance

25.0% (73/292) with **no connection note** is mid-pack against the other four campaigns (Israel
30.6%, UK 26.7%, AU 17.3%, US 15.9%). Whatever is wrong with this campaign is not the target list's
willingness to connect and not the invite. This is a fact from 292 events, not an inference.

### Best-performing message angle / segment / persona — cannot be stated

**4 replies. Below the 5-reply floor, so no angle, segment or persona verdicts are made here**, and
none should be lifted from this file into the next hypothesis. Two further reasons, independent of
sample size:

- Closely's per-contact export in `metrics-final.json` is aggregate. There is **no per-angle or
  per-company denominator** for who was messaged, so even a "2/5 (40%)" style figure is not
  constructible for any subsegment.
- The 5 rows in `responses-classified.csv` all say `which_message_replied_to = 1`, but Closely's
  step counters put 1 reply on the message-1 step and 3 on the message-2 step. **The
  `which_message_replied_to` field in `responses-raw.csv` is not trustworthy** and should not be
  used to attribute anything. Fix the export before the next post-mortem.

## Что не работало

### The message-1 body — this is the whole finding

Not derived from the 4 replies. Derived from two independent measurements.

**(a) Cross-campaign census of the text that was actually sent** (source: each campaign's
`closelyhq-import*.csv`, i.e. the exact strings Closely delivered; N = 1,207 message-1 texts):

| Campaign | msg1 with "45 sec" | with "80+ measurements" | with accuracy figure | distinct openers | **msg1 reply rate** |
|---|---|---|---|---|---|
| **EU 07-21 (this one)** | **0/307 (0%)** | **0/307 (0%)** | **0/307 (0%)** | **72/307 (23%)** | **1/67 (1.5%)** |
| UK 07-31 | 245/308 (80%) | 289/308 (94%) | 98/308 (32%) | 287/308 (93%) | 6/54 (11.1%) |
| Israel 07-23 | 123/215 (57%) | 167/215 (78%) | 105/215 (49%) | 207/215 (96%) | 27/175 (15.4%) |
| US 08-07 | 124/124 (100%) | 84/124 (68%) | 0/124 (0%) | 123/124 (99%) | 5/37 (13.5%) |
| AU 07-16 | 14/253 (6%) | 0/253 (0%) | 0/253 (0%) | 252/253 (100%) | 2/33 (6.1%) |

EU vs the other four combined: 1/67 vs 40/299, one-sided Fisher **p = 0.0017**. EU vs UK alone,
p = 0.030. The two campaigns whose message 1 carried no product numbers (EU 0%, AU 6%) are also the
two lowest msg1 reply rates. Five campaigns is a small comparison set and geo/profile/list differ
across them — but the content gap here is not marginal, it is 0% vs 68-100% on every specific.

**(b) What all 307 EU message-1 texts actually were.** 307/307 shared one identical product
sentence: *"We've built a mobile body scanning layer at 3DLOOK: two phone photos produce structured
body measurements and composition data that drop straight into the patient record."* That sentence
appears in 0/900 message-1 texts sent in the other four campaigns. Around it:

- **Openers promise specificity and deliver none.** Ten phrases cover 196/307 (64%) of the sends:
  "Noticed your background in digital health." (25), "Circling back after connecting." (24 — in the
  *first* message), "Quick note on something in your space." (23), "Wanted to reach out on something
  concrete." (22), "Quick one on GLP-1 program retention." (21), "Thought I'd share something
  specific to your program." (18), "Got me thinking about your patient journey." (17, and it has no
  subject). Only 135/307 (44%) named the company at all, against 246/308 (80%) in UK.
- **The only number in the whole message is the length of the meeting being requested.** 33% of
  message-1 texts contain a numeral, and in every case it is "10 minutes" / "15 minutes".
- **4 distinct closing sentences across 307 messages**, all four a meeting ask: "Might be worth a
  quick chat?" (87), "Worth a quick chat to explore?" (80), "Could be worth 10 minutes to compare
  notes?" (80), "Open to a quick chat?" (60). UK had 153 distinct closers over 308 sends, and 38% of
  them were not a meeting ask at all — 11% offered documentation, the rest asked a low-friction
  question ("Does structured body data come up anywhere in your stack?") or stopped on a statement.
- **Everything of substance was back-loaded into message 2**, which arrived on day +5: GDPR line
  307/307, a booking link 307/307, "45-second" 20%, a customer reference 57%. The 3 of 4 replies
  that Closely attributes to a step landed on the message-2 step.
- 7 salutations began with a title pulled raw from a name field: "Hi Dr. med. Yalda," / "Hi Prof.
  Dr. Pia,".

**Directional only, N=4:** within this campaign, msg2 (which does carry specifics) drew 3/52 (5.8%)
against msg1's 1/67 (1.5%) — same people, same list, same sender, so the confounds are removed, but
Fisher p = 0.22. It is a hint, not a result. Note that the msg2 denominator is *conditional on having
ignored msg1*, which biases it downward, so the true gap is likely wider than the numbers show.

### Cheap corroboration from the UK campaign, not from ours

UK's list was **worse** on paper: 118 of 309 threads (38%) were explicitly the weak tier — Graphic
Designer, Photographer, Member Services, Field Manager, "M&A, Capital Markets, Legal" at Slimming
World. Ours was 173 WEAK of 306 (57%) but with 132 PASS including 4 P1 and 59 P2 at real
weight-management accounts. UK still returned 4 interested + 2 questions + 1 referral. And one UK
decline (Sergio Millán Rodríguez, Zoe) declined while calling the accuracy claim "genuinely
impressive" — a prospect quoting the specific back at us. Nothing in our message was quotable.
**List quality does not explain the reply gap. It points back at the text.**

### Pattern in negative responses — none can be claimed

3 declines out of 67 messaged (4.5%). Two were one-line ("Not interested", "Hi! Thank you but I'm not
interested."), one soft ("not interested at the moment"). No hostility, no opt-out demands, no
GDPR/privacy complaint — notable given a cold no-note invite into 12 European jurisdictions, and worth
recording as a fact: **the approach carries no reputational cost, it just carries no message.**
Three people is not a pattern and no segment conclusion is drawn from them.

### List construction — step 2 never ran, and it is visible in the list

`companies.csv` does not exist; the tracker records this campaign as `[skipped: companies]`. The list
came straight from `people-raw.csv` → `people-validated.csv` → `contacts_filtered.csv`, with one
filter rule: **drop FAIL** (455 validated − 148 FAIL = 307 imported, exactly). Consequences that a
company step would have caught, all verifiable from the sent list, none of them inferred from
replies:

- **57 distinct company strings for 307 contacts, with the same account appearing under variants:**
  Terveystalo × 6 spellings (`Terveystalo`, `Suomen Terveystalo Oyj`, `Suomen Terveystalo OYJ`,
  `Suomen Terveystalo`, `Oulun Terveystalo`, `Iin Hyvinvointi ja Terveystalo Oy`), Qare × 3
  (`Qare`, `Qare.fr`, `Access Sante & Qare`), `Sidekick Health` / `SidekickHealth`, `mySugr` /
  `mySugr GmbH`, `myDiabby` / `myDiabby Healthcare`. Per-account send caps are impossible under this.
- **Terveystalo alone was 120/307 (39%) of the campaign** — an account the hypothesis itself called
  "an outlier account, not the core of this campaign", whose best contacts were graded P3.
  Finland was 133/307 (43%) of a campaign whose hypothesis named 8 countries; the sent list actually
  spanned 12, having picked up Kosovo (15), Poland (7), Belgium (3) and Spain (3) along the way.
- **29 of 57 companies (37 contacts) are not traceable to anything named in `hypothesis.md`.** Among
  them: **APHP** (Assistance Publique – Hôpitaux de Paris — a public hospital system, an explicit
  anti-case in our own hypothesis, contacted person is a paediatrician), **TamCAM** (a
  maternal/child-health research centre — the one decline the classifier already flagged as off-ICP),
  individual dietitians/nutritionists at `Larate` and `Mehilainen`, board members
  (`Styremedlem` at Edda.ai, `Member of the Supervisory Board` at Holi), and two rows whose company
  field is a person's name (`Annette`, `Armin Armagnac`).
- **Three open questions in `hypothesis.md` were never answered and shipped anyway:** the 170-contact
  Terveystalo problem (shipped 120), Kosovo scope (shipped 15 hellocare.ai contacts), Iceland
  (shipped 8).
- **173 WEAK contacts were sent without the manual review** `icp-validation-summary.md` said they
  needed ("candidates for Vadim's manual review").

### People we shouldn't have included

Company-level, on documented ICP grounds rather than on a reply:

| Entity | Why | Registry action |
|---|---|---|
| APHP (Assistance Publique – Hôpitaux de Paris) | Public hospital system = anti-case in this campaign's own hypothesis; contact was a paediatrician | global company registry — permanent |
| Tampere Center for Child, Adolescent and Maternal Health Research (TamCAM) | Maternal/child-health research centre, not a weight-management or telehealth program. Off-ICP for FitXpress segments 1-2 | global company registry — permanent |
| `Annette`, `Armin Armagnac` | Company field holds a person's name; the account is unverified | fix upstream, don't send again until resolved |
| Individual dietitians / nutritionists (Larate, Mehilainen) | ICs, not buyers, at organisations we did not qualify | person-level, this cycle |
| Board / supervisory-board members (Edda.ai, Holi) | No operational ownership of a product roadmap | person-level, this cycle |

Alex Hill (Sidekick Health) — **stale list, not a refusal.** He left Sidekick. Keep Sidekick Health
as a live target (it is a named pure-play account) and source a Product or Clinical-Ops replacement.

## Learnings → next hypothesis

### Confirm

- **A no-note connection request into continental EU telehealth accepts at ~25%** (73/292). This
  campaign, Israel and UK all landed in the 25-31% band within ten days of each other. Keep the
  no-note invite.
- **Continental EU health prospects do not react badly to cold outreach** — 3 soft declines, 0
  opt-outs, 0 privacy complaints out of 67 messaged. GDPR anxiety is not the blocker it was assumed
  to be in `hypothesis.md`.
- **Warm-up steps ran fine at this volume** — 474 profile visits, 56 post likes, 0 errors, 1 invite
  error out of 293. No platform-limit problem to solve.

### Reject

- **"Outcome framing" implemented as "no verifiable specifics" is rejected.** 0/307 messages carried
  a number, a proof point or a named metric; 1/67 replied. This is the single actionable learning of
  the campaign.
- **A fixed pool of interchangeable openers is rejected.** 72 distinct openers over 307 people, top
  ten covering 60%, and every one of them a promise of specificity ("something specific to your
  program") followed by boilerplate.
- **A meeting ask as the only CTA in message 1 is rejected** — 307/307 here, from a pool of four
  phrasings, versus UK where 38% of 308 closers asked a question or offered documentation instead.
- **"Drop FAIL, send everything else" is rejected as a list rule.** It shipped a public hospital
  system, a paediatric research centre, two unverified company names and 39% of the campaign into one
  P3 outlier account.

### New hypotheses to test

- **H1 (highest value, near-zero cost).** The 63 accepted-and-silent contacts are now 1st-degree
  connections. A rewritten message 1 — one hard specific (45 seconds / 80+ measurements / the
  accuracy formulation verbatim from `accuracy-formulations.md`), one company-specific line, a
  low-friction question instead of a meeting ask — will beat 1/67. Same people, same list, same
  sender, one variable. If it beats ~6/63 we have our answer about the message; if it does not, the
  vertical hypothesis is genuinely in question for the first time.
- **H2.** A Europe campaign restricted to the pure-play weight-loss/obesity accounts named in
  `hypothesis.md` (Wellster, Oviva, Sidekick, Liva, Nederlandse Obesitas Kliniek, The Body Clinic,
  myDiabby) with a hard cap of 5 contacts per company will outperform this campaign's reply rate.
  Untested: 39% of the send went to one out-of-thesis account.
- **H3.** A low-friction question CTA in message 1 outperforms a meeting ask in EU health. Directional
  support from UK only (38% of UK msg1 closed on something other than a call), needs a clean split
  to confirm.
- **H4.** The compliance angle needs a persona rule, not a title match. The compliance message went
  to Oviva's **Head of Privacy (Senior Legal Counsel)**, who replied "Not interested". n=1, so this
  is a hypothesis: privacy/legal counsel are governance reviewers, not program buyers; route the
  regulatory angle to the CMO / clinical program owner and mention compliance as a de-risker.

## Recommendations for next campaign

1. **Rewrite message 1 before another EU invite goes out.** Minimum bar: one specific from
   `brand-assets/product-info/proof-points.md` (accuracy wording verbatim from
   `accuracy-formulations.md`), one line that could only have been written to that company, and a CTA
   that is answerable without a calendar. Delete the "mobile body scanning layer at 3DLOOK: two phone
   photos produce structured body measurements and composition data" sentence from the corpus — it
   was sent 307 times and drew 1 reply.
2. **Run H1 on the 63 silent connections first.** It is the only clean experiment available, it costs
   no invite credits, and it decides whether the EU telehealth/weight-loss thesis gets another list
   built for it. Do not build a new list before this returns.
3. **Do not re-run this list.** Rebuild from step 2 with a real `companies.csv`: canonicalise company
   names, cap contacts per account (5), and resolve the geo/scope questions (Kosovo, Iceland) before
   import rather than after.
4. **Make the WEAK tier a gate, not a label.** 173 WEAK contacts went out with no review. Either
   review them or stop sending them; sending them unreviewed means the tier carries no information.
5. **Do not send until message 1 is checked mechanically.** A one-line check on the import CSV before
   it reaches Closely: does every `message_1` contain at least one product specific, and is the
   opener unique enough. 307/307 would have failed. This is `message-sequencer` / `closelyhq-importer`
   work, not judgement work.
6. **Fix the reply export.** `which_message_replied_to` disagreed with Closely's own step counters on
   3 of 4 replies. Take step attribution from the step counters until the export is fixed.
7. **Verdict on the hypothesis: not retired, not re-run as-is.** Nothing here falsifies "European
   telehealth platforms with weight-management programs want verified body measurements" — that pitch
   was never delivered. What is falsified is this message and this list. Retire both.

## Updates to `CLAUDE.md`

One proposed diff. **Not applied — this needs Vadim's call, because it touches the positioning rule
in section 3.**

Section 3 currently reads:

```
- В outbound: hero message — про outcome, не про точность
```

This campaign is what that line looks like when an agent reads it literally: 0/307 message-1 texts
contained a number, an accuracy figure or a proof point, and 1/67 people replied. The campaigns that
put the specifics in message 1 (UK 97% accuracy-bearing, Israel 49%, US 100% with "45 seconds")
replied at 11-15%, and one UK prospect declined while calling the accuracy claim "genuinely
impressive". Proposed wording:

```
- В outbound: hero message — про outcome, не про точность. Но «не про точность» относится
  к value proposition, а не к доказательствам: message 1 обязан содержать минимум один
  проверяемый specific (45 seconds · 80+ measurements · формулировка точности дословно из
  accuracy-formulations.md). Outcome-фрейминг без конкретики = 2026-07-21-eu-telehealth-weightloss:
  0/307 сообщений с числом, 1/67 ответов.
```

If the diff is accepted, the same rule belongs in the `message-sequencer` prompt (all copies) as a
hard requirement on message 1, not as a style preference.

## Updates to the exclusion registry

**Already written** (`python3 scripts/outbound-registry.py reply --campaign
2026-07-21-eu-telehealth-weightloss --profile olena`, 2026-09-02 — 4 classified replies, 4 registry
people updated, 0 unmatched):

| Person | Company | `reply` |
|---|---|---|
| Philipp Sauer | Oviva | decline |
| Janne Kanervisto | Terveystalo | decline |
| Peter Csonka | TamCAM | decline |
| Alex Hill | Sidekick Health | other/unclear |

The remaining 303 people stay `reply: null` / `status: csv_generated`, which is what makes the
6-month release rule applicable to them.

`responses-classified.csv` was missing a `linkedin_url` column, so the registry writer matched 0 of 4
on the first run. The column has been backfilled from `responses-raw.csv`. **Every future
`responses-classified.csv` needs it** — without a URL the reply outcomes silently do not land, and
the 6-month release rule has nothing to release.

**Recommended, not written** (company-level exclusions are Vadim's call and go through the registry
writer, never by hand):

- `global-company-registry.json` — permanent, ICP grounds: **APHP** (public hospital system,
  anti-case), **TamCAM** (maternal/child-health research centre, off-ICP).
- `olena-registry.json` — person-level, this cycle: the two person-named company rows (`Annette` /
  Francois-Xavier Trancart, `Armin Armagnac` / Augustin Chatenet) pending company verification;
  individual dietitians/nutritionists (Larate, Mehilainen); board/supervisory-board members
  (Edda.ai, Holi).
- **Alex Hill → inactive at Sidekick, Sidekick Health stays a live target.** Do not let a stale
  contact exclude a named pure-play account.
- **Nothing else should be excluded on the strength of this campaign.** 63 people accepted an invite
  and were then sent a message with no content in it. Excluding them would be recording our own
  message failure as their disinterest — they are the re-test population in H1, not a burn list.
