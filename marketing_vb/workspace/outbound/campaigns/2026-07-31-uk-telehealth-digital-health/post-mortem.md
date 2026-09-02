---
product: fitxpress
profile: katerina
market: UK
campaign: 2026-07-31-uk-telehealth-digital-health
analyzed: 2026-09-02
status: awaiting_vadim_review
sample_tier: "5-14 replies → directional observations only, N printed next to every claim"
denominator_source: metrics-final.json (Closely event counters). `outbound-registry.py status` sent-column NOT used.
---

# Campaign Post-Mortem — 2026-07-31-uk-telehealth-digital-health

**Sample size and what that permits.** 13 replies from 13 people (17 rows). That puts this
campaign in the **5-14 band**: directional observations, usable as hypotheses for the next
campaign, not as decisions. Every claim below is tagged `[FACT]` (real denominators, holds at
any N), `[DIR N=x]` (directional, N=x) or `[N=1]` (single instance, not a pattern). Send- and
accept-level numbers are `[FACT]` because their denominators are in the hundreds; anything
sliced by angle, persona or segment is `[DIR]` at best.

---

## TL;DR (3 строки)

1. **The 13.8% reply rate is a denominator artifact, not a messaging win.** It divides replies
   by *message events*, and this campaign has sent only 1.36 messages per accepted person
   because its larger half (Closely 139205) is 12% complete and has barely started its Message-2
   step. On the like-for-like denominator — replies per accepted person — UK is 13/69 = 18.8%
   and Israel is 34/186 = 18.3%. Same rate, a quarter of the reach. `[FACT]`
2. **The volume gap and the reply rate are the same fact.** The hypothesis's own filters yielded
   15 companies; 218 of 311 drafts (70%) then went to the two lowest-fit companies on that list
   (Slimming World fit=1, Huma fit=2), and those two produced 9 of 13 replies. Israel had 43
   companies including four national HMOs. This was a hypothesis-design ceiling, arithmetically
   predictable on day one, not an execution shortfall. `[FACT]`
3. **What actually earned meetings is narrow and reusable: owner-persona + role-specific hook +
   explicit time ask.** All 3 interested replies came from that combination (50 of 311 drafts).
   The 246 drafts using technical-integration, member-engagement or digital-transformation
   produced 10 replies and **zero** interested. `[DIR N=13]`

---

## Hypothesis vs reality

| Metric | Target | Actual | Verdict |
|--------|--------|--------|---------|
| Acceptance rate | ≥ 30% | **26.7%** (69/258) | ✗ overall — but the ICP-validated list hit 31.7% (26/82) and the account-depth list dragged it to 24.4% (43/176) |
| Reply rate | ≥ 5% | **5.0%** on invites (13/258) · 18.8% on accepted people (13/69) · 13.8% on message events (13/94) | ✓ on every denominator; the hypothesis never named one, which is why the figure has been quoted three different ways |
| Positive replies | ≥ 4 | **5 people** interested+question (3 interested + 2 question) · 4 `interested` **rows** = 3 unique people (Abraham Morse has 2 rows) | ✓ |
| Qualified leads | ≥ 2 | **2** (Moein Kafi/Huma, Carolyn Pallister/Slimming World). Abraham Morse is a relationship, not a lead — his own words: "Vira does not seem to have a need for it at this time" | ✓ exactly at target |
| Negative reply rate | — | **0%** (0/13) across 258 invites | ✓ no brand damage |
| CPL | — | **not computable** — no cost inputs exist in the workspace (Closely seat, Sales Nav seat, hours). Needs one number from Vadim to become a metric |

### The campaign is not finished, and the comparison table hides it `[FACT]`

| Closely campaign | Scope | Invites | Accepted | Msg events | msg/accepted | Replies | Contacts still active |
|---|---|---|---|---|---|---|---|
| 139077 "UK telehealth 4/08/26" | broad ICP list, 15 companies | 82 | 26 (31.7%) | 48 | 1.85 | 4 | 11 / 84 — effectively done |
| 139205 "UK telehealth Huma+Slimming world" | 2 accounts, PASS + WEAK | 176 | 43 (24.4%) | 46 | 1.07 | 9 | **187 / 213 — ~12% complete** |

Both are `status: active`. Israel is `finished`. **A checkable prediction:** when 139205's
Message-2 step runs against its current 43 accepted contacts, campaign message events go to
~134 and the headline rate falls to ~9.7% *with zero change in performance*. If we re-quote
13.8% next month it will look like decay that never happened.

### Cross-campaign, on the denominator that survives sequence length `[FACT]`

| Campaign | Invites | Accept% | Msg events | msg/accepted | Replies | **Replies / accepted person** | State |
|---|---|---|---|---|---|---|---|
| Israel | 608 | 30.6% | 432 | 2.32 | 34 | **18.3%** (34/186) | finished |
| **UK (this one)** | **258** | **26.7%** | **94** | **1.36** | **13** | **18.8%** (13/69) | active |
| US fitness | 245 | 15.9% | 67 | 1.72 | 6 | **15.4%** (6/39) | active |
| AU telehealth | 220 | 17.3% | 61 | 1.61 | 5 | **13.2%** (5/38) | active |
| EU weightloss | 292 | 25.0% | 119 | 1.63 | 4 | **5.5%** (4/73) | active |

UK's real standing: **tied with Israel at the top, roughly 1.2-1.4x US/AU, and 3.4x EU
weightloss** — while EU weightloss remains the one genuine outlier that needs explaining. UK is
not 1.7x better than Israel at messaging. It is equally good at a quarter of the scale, which is
a different and more actionable finding: the messaging is not the bottleneck, supply is.

No prior `post-mortem.md` exists in any campaign folder, so the comparison above is built
directly from each campaign's `metrics-final.json`. This is the first post-mortem in the set.

---

## Что работало

### Best-performing message angle `[DIR N=13]`

Denominator caveat first: per-angle **send** counts do not exist. Closely reports events per
campaign, not per angle. The table uses **drafts written** as the denominator, and only 258 of
311 drafts became invites and 94 became messages, so these are share-of-drafts vs
share-of-replies, not reply rates. Directional only.

| Angle | Drafts | Replies | Interested | Outcome shape |
|---|---|---|---|---|
| virtual-care | 11 | 1 | **1** | Moein Kafi, Field CEO, Huma — unprompted call ask |
| clinical-operations | 18 | 1 | **1** | Abraham Morse, Director Global Clinical Programs, Vira Health — demo booked |
| weight-management | 21 | 2 | **1** | Carolyn Pallister interested; Sue Thompson declined |
| technical-integration | 93 | 6 | 0 | 2 question, 1 referral, 1 maybe-later, 2 decline |
| digital-transformation | 49 | 2 | 0 | 1 maybe-later, 1 decline |
| member-engagement | 104 | 1 | 0 | 1 maybe-later (a forward to the PR team) |

**The three owner-facing angles — virtual-care, clinical-operations, weight-management — are 50
of 311 drafts (16%) and produced 3 of 3 interested replies (100%).** The three
non-owner-facing angles are 246 drafts (79%) and produced 0.

Sample reply (virtual-care, the cleanest lead in the campaign): «Hi Katerina, sound interesting.
Let's have short call. I'm keen on understanding more of your product.»

Hypothesis why: these three angles were the only ones whose opening line named a business
outcome the recipient personally owns — a virtual-care programme, a clinical programme's
measurement consistency, a research/evidence programme. The other three named a *capability*
(an API, a progress view, a project stream) and left the recipient to work out whether it was
theirs to act on.

### The opener mechanic that produced meetings `[DIR N=13]`

Two structurally different opener families ran in this campaign, and the difference in *what
kind* of reply they produce is sharper than the difference in reply count:

| Opener close | Drafts | Replies | Interested | What came back |
|---|---|---|---|---|
| Explicit time ask ("Worth 15 minutes?") | 176 | 7 | **3** | all 3 meetings, plus 2 declines and 2 maybe-later |
| Question about their world ("Does structured body data come up in Huma's pipeline?") | 85 | 4 | 0 | 2 technical questions, 1 referral upward, 1 decline |
| Statement, no ask | 47 | 2 | 0 | 1 maybe-later, 1 decline |

The soft-question close is the better *engagement* device and the worse *pipeline* device. It
reliably gets an engineer to answer a question about their own stack, and then someone has to
escalate. The time ask converts or it doesn't, and it produced 3 for 3 of the interested
replies.

**Message 1 does essentially all the work: 12 of 13 people replied to the opener; only Moein
Kafi replied to Message 2.** `[FACT]` The two-step sequence is sufficient — do not lengthen it
on the strength of this campaign.

Reusable opener spec, taken from the three that converted (`messages-batch2/4fec588f4b08.md`,
`messages-batch2/223f0357ba58.md`, `messages/deeb8e662104.md`):
- Line 1 names the recipient's actual scope in their own words ("leading Nutrition, Research &
  Health at Slimming World puts you close to the evidence question this raises").
- One capability block, unchanged across every message: two smartphone photos · under 45 seconds ·
  80+ measurements plus body composition · 96-97% against manual measurement.
- One sentence connecting it to a programme *they* own, not to a use case in general.
- Explicit time ask. No hedging.
- Median 319 characters in 4 short paragraphs (batch2) vs 480 characters in one block (batch1).

### Best-converting company segments `[DIR N=13, treat as hypothesis]`

Fit score did not predict replies, and it did not predict quality either:

| company-researcher fit | Companies | Replies | Interested |
|---|---|---|---|
| 5 / 4 | Zoe, Vira Health, Peppy, Newson, Healthier Weight | 3 | 1 (Vira — and he says Vira has no need) |
| 3 | Tonic, Fiit, Flo, The Body Coach | 0 | 0 |
| 2 | Huma, Hertility, Physitrack, Thriva | 5 | 1 (Huma) |
| 1 | Sweatcoin, Slimming World | 5 | 1 (Slimming World) |

Read this as "fit_score was not a useful predictor here", **not** as "low fit is good" — fit=1/2
companies also absorbed 216 of 311 drafts, so per-invite performance is not established. What is
established: the highest-fit company in the list (Zoe, fit=5, 20 drafts) returned a
roadmap-level no from its Engineering Director — «body scanning API integration doesn't currently
align with ZOE's product vision and roadmap» — and a conditional internal forward. `[FACT]`

### Account-based targeting — the Huma signal, assessed `[DIR N=4 responders]`

**Huma produced four responders, not three.** Sadeq N. Yazdi, filed in step 8 as "Unknown (no
thread_file)", resolves to **Huma, Back End Developer, London, WEAK list, technical-integration
angle**, thread `messages-batch2-weak/b0d03de87537.md`. Cause of the miss: he has two LinkedIn
profiles in the Sales Nav export (`/in/sadeq-n-yazdi` and `/in/sadeq-n-yazdi-6930162b6`); the
validator gave one row FAIL and the other WEAK, and the import CSV paired the WEAK row's
`person_id` with the FAIL row's URL. The reply arrived on the FAIL row's `person_id`, which has
no thread. One of the campaign's 5 positive replies was nearly lost to a duplicate-profile ID
collision. `[FACT]` — resolved in `responses-classified.csv`.

So: **51 contacts at one account → 4 replies (7.8% of contacts, 31% of the whole campaign's
replies)**, from 4 distinct stakeholders:

| Person | Tier | Reply | What it was worth |
|---|---|---|---|
| Moein Kafi, Field CEO | PASS | interested | The lead. Unprompted call ask |
| Hojat Modaresizadeh, Senior SWE | WEAK | referral | «Reach out to one of the Field CEOs» — redundant, pointed at Moein who had already replied |
| Ali BahaAbadi, Senior Android Eng | WEAK | question | Will share internally; asked iOS-or-Android-only. Free internal champion path |
| Sadeq N. Yazdi, Back End Dev | WEAK | question | Wants material for "the managers" — **plus the campaign's only build-vs-buy intel: «we already have some similar features»** |

Honest read of account-based targeting: multi-threading an engineering-heavy account produces a
chorus of replies that all converge on the same single decision-maker, and in this case that
decision-maker replied on his own anyway. Genuine value: the build-vs-buy objection we would
never otherwise have heard, and two internal champions. Genuine cost: 20 WEAK invites, and 3 of
4 responders cannot buy. **Worth repeating, but on owner titles — Huma had 4 Field CEOs, 1
Deputy Field CEO, a Field CTO and 2 Heads of Engineering in the PASS tier. There was no need to
message backend engineers to reach four stakeholders.** `[FACT]`

### Best-performing personas (titles) `[DIR N=13]`

All 3 interested replies came from programme owners, from 3 different companies and 3 different
angles:
- Field CEO (Huma) — owns virtual-care programme delivery.
- Director, Global Clinical Programs (Vira Health) — owns cross-market measurement consistency.
- Head of Nutrition, Research & Health (Slimming World) — owns the evidence programme.

Two of the three are not in `hypothesis.md`'s three named personas (Head of Clinical Ops, CMO,
Head of Member Engagement/Product). Not one of the three named personas produced an interested
reply. `[DIR N=13]`

Individual-contributor engineers (6 of 13 repliers): 2 questions, 1 referral, 1 maybe-later, 2
declines, **0 interested, 0 meetings**. They reply, and every reply needs an escalation step.

---

## Что не работало

### Worst-performing angle: member-engagement `[DIR N=13]`

104 drafts — the largest single block in the campaign, and the hypothesis's central bet
("longitudinal engagement + trustworthy in-program progress", the whole differentiation from the
2026-07-08 UK campaign) — returned **1 reply**, and that reply was Lysette Mazur (Corporate
Affairs) forwarding us to Slimming World's PR team.

Hypothesis why, in order of how much I believe it:
1. **Mis-targeted, not mis-written.** 51 of the 104 member-engagement drafts went to the
   Slimming World WEAK tier, whose profiles are franchise consultants and HQ digital staff. The
   angle was aimed at a retention owner and delivered to people who own neither retention nor a
   budget.
2. **"Members drop off at month 2-3" is our framing of their problem, not theirs.** Nobody's job
   title says "month-2 drop-off". The three angles that worked each named an artifact the
   recipient owns (a programme, a protocol, a research dataset).
3. Cannot be separated from (1) with this data. Re-test the angle on owner titles before
   discarding it.

### Worst-performing use of volume: technical-integration on IC engineers `[DIR N=13]`

93 drafts, 6 replies (46% of all campaign replies), 0 interested, 0 meetings. The clearest single
illustration is Scott Lyons, Senior Data Engineer at Slimming World, who read an API pitch as a
personal tool: «sounds interesting but I'm not sure it's something I would have a use for in my
personal time». `[N=1 — an illustration, not a pattern]`

### Pattern in negative responses

**There isn't one: 0 of 13 replies were negative.** `[FACT]` Zero irritation across 258 invites.
The four declines were all polite and two paid the product a compliment («genuinely impressive»
on accuracy, from Zoe).

The nearest thing to a pattern in the declines, at N=4 and therefore not a pattern: two of the
four are *role* misses rather than *company* misses (Scott Lyons reading it as a personal tool;
Joanna Armstrong leaving Slimming World in two weeks) and only one is a real company-level no
(Zoe's roadmap). Wrong-person declines outnumber wrong-company declines 2:1 here — consistent
with everything else in this post-mortem pointing at persona selection rather than company
selection as the weak link. `[DIR N=4 — flag, do not act on yet]`

### Companies / people we shouldn't have included

**Slimming World — 165 of 311 drafts (53% of the campaign), fit_score 1.** `[FACT]`
- It fails the hypothesis's own sub-segment definition: the campaign was scoped to "remote-first
  longitudinal programs" and "private/cash-pay D2C providers running ongoing remote programs".
  Slimming World is the UK's largest **in-person franchise group** weight-management business.
  company-researcher scored it 1/5 and wrote the honest reason: "included for completeness".
- The Sales Nav pull was 691 profiles of which **526 (76%) failed validation** — 273+ of them
  titled some spelling of "Consultant" (self-employed franchisees), plus 44 District Managers and
  26 Team Developers. `[FACT]`
- Its 67 PASS titles are the HQ digital team — Digital Designer, Senior Digital Editor, Lead
  Engineer, Product Manager, Solutions Architect — not programme owners.
- Outcome: 5 replies, 3 declines, 1 PR forward, 1 real signal.
- **But do not blanket-exclude it.** The one real signal, Carolyn Pallister, is live and her
  interest is framed around the *research programme*, which is a use case we were not selling.
  See H4 below.

**19 of 92 batch1 contacts (21%) were not in the UK** — US 9, Poland 3, Spain 2, Netherlands /
Qatar / Portugal / Czechia / Sweden 1 each. `[FACT]` The hypothesis's anti-cases say "US-only or
non-UK-operating platforms (geo discipline: katerina = UK only)"; the filter was applied to
company HQ and never to person location, and that is a gap in the rule, not sloppiness in the
execution. It matters because **all four batch1 repliers were located outside the UK**: Abraham
Morse (US), Daniel Sleeper (US), Sergio Millán Rodríguez (Spain), Kamil Wyszynski (Poland),
while all nine batch2 repliers were UK-based. `[DIR N=4 — do not act on the direction, act on the
ambiguity]` Enforcing person-level UK strictly would have deleted the campaign's only booked
meeting. This needs Vadim's ruling, not a cleanup.

**39-49 people were recorded as contacted but never were.** `[FACT]` 307 people in
`katerina-registry.json`, 297 contacts in Closely, **258 invites actually sent**. The registry's
6-month release rule will hold at least 39 people hostage who never received anything.

---

## Learnings → next hypothesis

### Confirm — carry into core ICP

- **UK private digital-health / telehealth is receptive.** 18.8% of accepted people replied
  (13/69), 0 negatives across 258 invites, one meeting booked. Tied with Israel, our best market
  to date, on the like-for-like denominator. `[FACT]`
- **Programme-owner personas convert; the campaign's three named personas did not.** Add **Field
  CEO / Field CTO** (regional P&L owners at RPM platforms) and **Director of Clinical Programs**
  as named FitXpress telehealth personas. 3/3 of the interested replies. `[DIR N=13]`
- **Message 1 carries the campaign** (12/13 replies) and **the explicit time ask converts** (3/3
  interested). Keep the 4-paragraph, ~320-character, role-specific opener with an unhedged
  15-minute ask. `[FACT / DIR N=13]`
- **The capability block is doing its job** — nobody in 13 replies queried the accuracy claims,
  and two volunteered compliments on them. Keep it byte-identical.

### Reject

- **member-engagement as a campaign's lead angle** on anything but a retention owner. 104 drafts
  → 1 PR forward. Re-test only on owner titles. `[DIR N=13]`
- **technical-integration as a primary opener.** Keep it as a *second* touch after an owner
  engages, or as the answer to an engineer the owner delegates to. As a first touch it buys
  replies that cannot buy: 93 drafts, 6 replies, 0 meetings. `[DIR N=13]`
- **Bulk Sales Nav pulls on consumer-brand employers without a title whitelist.** 526 wasted
  validations on one company. `[FACT]`
- **In-person franchise weight-management brands** for the longitudinal-remote-progress angle.
  `[FACT — definitional, not statistical]`
- **fit_score as a priority signal for send order.** It predicted neither replies nor quality
  here. `[DIR N=13]`

### New hypotheses to test

- **H1 — Angle by authority, not by profile keywords.** Assign the owner-facing angle to every
  owner title and never assign technical-integration as a first touch. Predicted effect:
  interested-per-100-drafts rises from 1.0 (3/311) toward 6 (3/50), acceptance is unchanged,
  total reply count *falls* because the engineer chorus disappears. **This hypothesis predicts a
  worse reply rate and a better pipeline — score it on interested, not replies.**
- **H2 — Account depth works, but only above a title-density floor.** Repeat account-based
  targeting on 6-8 UK accounts that each have ≥8 owner-persona titles, 10-15 owner contacts
  each, zero IC engineers. Huma cleared that floor (4 Field CEOs + Deputy Field CEO + Field CTO +
  2 Heads of Engineering in PASS); Slimming World did not.
- **H3 — The 50-500 employee band is the binding UK volume constraint and it excluded our best
  account.** Huma is 501-1,000+ and scored fit=2 largely on size; it produced 4 of 13 replies and
  the campaign's cleanest lead. Test 50-2,000 for UK.
- **H4 — "Research / clinical evidence owner" is an unrecognised buyer.** Carolyn Pallister's
  interest was explicitly about adding "a verified data point to the research programme" — an
  evidence use case, not member engagement. Test a research/outcomes-evidence angle on Heads of
  Nutrition / Research / Clinical Evidence / Outcomes at large weight-management and
  digital-health brands. Includes the brands we would otherwise exclude on programme-mechanic
  grounds. `[N=1 — a lead worth chasing, explicitly not a finding]`
- **H5 — Non-UK-located executives at UK-HQ companies reply at least as well as UK-located
  ones.** 4/4 batch1 repliers were abroad. `[N=4, very weak]` Do not build a campaign on this;
  do record `location_country` on every contact so the next two campaigns can answer it.

---

## Recommendations for next campaign

1. **Report replies per accepted person as the headline metric.** Add `messages_per_accepted` and
   `reply_rate_on_accepted_pct` to `metrics-final.json` and stop leading with
   `reply_rate_on_messages_sent_pct` — it moves with sequence progress, not performance, and it
   has already produced one wrong conclusion about this campaign.
2. **Never compare an active campaign to a finished one without printing the state.** Add
   `status` and `pct_contacts_finished` to every cross-campaign table. Israel `finished` vs
   139205 at 12% complete is not a fair fight in either direction.
3. **Compute contact supply at hypothesis time, before Step 2.** `companies × owner-titles per
   company ≥ invite target`, written into the hypothesis. 15 companies × ~6 reachable owners = 90.
   The 258-invite target was unreachable on 2026-07-31 and everything downstream — Slimming World,
   the WEAK tier, 526 failed validations — was a patch for a gap that arithmetic would have shown
   on day one. If supply is short, the honest options are widen the band (H3), widen geo, or
   accept a 90-invite campaign — not backfill with depth on off-thesis accounts.
4. **Get Vadim's ruling on person-level geo, then write it into the rule.** Recommendation:
   geo-discipline binds the **company's market**, person location is recorded but not filtered,
   and any non-profile-geo person gets flagged in the campaign summary. Rationale: the buyer of a
   UK programme is whoever owns it, and the strict reading would have deleted our only booked
   meeting.
5. **Title whitelist before any Sales Nav pull on a consumer brand.** Franchise/consultant
   patterns (`Consultant`, `District Manager`, `Team Developer`, `Owner`) are cheap to exclude
   pre-pull.
6. **Two-step sequence stays two steps.** 12 of 13 replies came on Message 1.
7. **Fix the responses join: `person_id` OR normalized LinkedIn slug.** Duplicate LinkedIn
   profiles cost us the identity of a positive reply this round.
8. **Add `linkedin_url` to the `responses-classified.csv` schema** — `outbound-registry.py reply`
   joins on it and silently recorded 0 of 13 outcomes until it was patched by hand today.
9. **Release the never-contacted.** 39+ registry rows are being held under the 6-month rule
   without ever having received an invite.
10. **Answer the two open questions this week** (Ali BahaAbadi, Sadeq N. Yazdi — both Huma, both
    holding an internal share-out) and **confirm whether the 8/31 Vira Health demo happened.**
    Today is 2026-09-02 and nothing in the workspace records the outcome.

---

## Updates to `CLAUDE.md`

Proposed diffs — **not applied.** CLAUDE.md is Vadim's to change.

**1. §11 Метрики — name the denominator.** This is the concrete cause of TL;DR #1.

```diff
- - **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
+ - **Outbound:** acceptance rate (accepted / invites sent), **reply rate = replies / accepted
+   connections** (per person, the like-for-like figure across campaigns), positive reply rate,
+   qualified leads, передано в sales (per-product).
+   Replies / message *events* is a secondary diagnostic only: it falls as a sequence progresses
+   even when nothing changes, so it cannot be compared between an active and a finished campaign.
+   Denominators come from `metrics-final.json` (Closely event counters), never from the `sent`
+   column of `outbound-registry.py status` — that counts import rows.
```

**2. §5 — geo-discipline is ambiguous between company market and person location.**

```diff
- Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна).
+ Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна):
+ правило біндиться на **ринок компанії**, а не на локацію людини. Локація людини пишеться
+ в `location_country`, не фільтрує, але виноситься у звіт кампанії.
```
*(Pending Vadim's ruling per recommendation 4. This campaign messaged 19 non-UK people out of 92
in batch1 and got its only booked meeting from one of them.)*

**3. §4 FitXpress ICP, telehealth & weight-loss segment — add the personas that actually
converted.**

```diff
- - **Telehealth & weight loss / GLP-1:** ... Buyer: Founder/CEO / Chief Medical Officer / Head of Clinical Operations / Head of Member Engagement
+ - **Telehealth & weight loss / GLP-1:** ... Buyer: Founder/CEO / Chief Medical Officer / Head of
+   Clinical Operations / Head of Member Engagement / **Field CEO or Field CTO (regional P&L owner
+   at RPM platforms) / Director of Clinical Programs / Head of Nutrition, Research & Evidence**
```
*(Evidence: 3/3 interested replies, `[DIR N=13]`. The three previously-named personas produced 0.
Recommend applying the first two now and holding "Research & Evidence" until H4 is tested.)*

The 50-500 employee band (H3) lives in the hypothesis template and `icp-detail.md`, not in
CLAUDE.md — no diff needed here.

---

## Updates to the exclusion registry

**Already written** — `python3 scripts/outbound-registry.py reply --campaign
2026-07-31-uk-telehealth-digital-health --profile katerina` recorded all 13 outcomes onto
`katerina-registry.json` (`replies_recorded_on: 2026-09-02`): 4 decline, 3 interested, 3
maybe-later, 2 question, 1 referral. Required one input fix first — `linkedin_url` was missing
from `responses-classified.csv`, so the join matched 0 of 13 (see recommendation 8).

**People to exclude permanently** — declined, no reopen signal, no referral:

| Person | Company | Why |
|---|---|---|
| Sue Thompson | Slimming World | «isn't something that would have a place with us currently» |
| Scott Lyons | Slimming World | Read it as a personal tool; explicitly not a wrong-department case |
| Joanna Armstrong | Slimming World | Leaving the company in two weeks; no successor named. **Exclude the person, not the seat** |
| Sergio Millán Rodríguez | Zoe | Roadmap-level no on behalf of the company |

**Do not exclude — live or door-open:** Moein Kafi (Huma, live lead), Carolyn Pallister (Slimming
World, live), Abraham Morse (Vira Health, relationship), Ali BahaAbadi + Sadeq N. Yazdi (Huma,
awaiting our answers), Hojat Modaresizadeh (Huma, referred us upward), Kamil Wyszynski
(Physitrack, «happy to stay connected» — the most explicit door-open in the set), Lysette Mazur
(Slimming World, PR forward), Daniel Sleeper (Zoe, internal share).

**Company-level, for `global-company-registry.json`:**

| Company | Recommendation | Why |
|---|---|---|
| **Zoe** | 9-12 month cooldown | Engineering Director declined on product vision and roadmap; that is a company-level no with a time dimension, not a person miss. fit=5, so re-approach when the roadmap moves — not sooner |
| **Slimming World** | do **not** globally exclude; tag "off-thesis for remote-longitudinal angle" | fit=1, in-person franchise model, 76% of the Sales Nav pull unusable. But Carolyn Pallister is live and the research/evidence angle (H4) is untested. Excluding the company would kill the campaign's second-best lead |
| **Huma** | keep open, promote | 4 responders from 51 contacts, the cleanest lead, and the only build-vs-buy intel we got. Also the reason to test H3 — it sits above the 50-500 band that nearly kept it out |
| **Vira Health** | keep open, 6-month nurture | Buyer engaged personally, company has no stated need. Relationship, not pipeline |
| **Physitrack** | keep open, 3-4 month nurture | Explicit "stay connected" from a Principal Technical PM |

**Registry hygiene, needs a decision not a script run:** 307 rows recorded vs 258 invites sent.
At least 39 people carry a `csv_generated` status and a 6-month hold for outreach they never
received. Recommend releasing rows with no corresponding Closely send event rather than aging
them out. I have not touched them — the registry has one writer and this needs a flag on the
`record` step, not a manual edit.

---

## Two anomalies — assessed

**Abraham Morse's «Nick» sign-off is not a cross-account send.** `nick-registry.json` contains no
trace of Abraham Morse or Vira Health; the contact exists only under `katerina-registry.json`,
and both his replies arrived on the Katerina thread in Closely campaign 139077. There is no
evidence in our data of a send from Nick's account. Remaining explanations are on his side: he
signs personally as Nick, or he misdirected a reply. **Action: one human message to confirm who
is on the 8/31 call — not a systems investigation.** `[FACT — negative finding]`

**Vira Health's geo is in scope; the person's is the open question.** `companies.csv` lists Vira
Health (Stella) as UK / London, fit=4, so the anti-case "US-only or non-UK-operating platforms"
is not violated. `people-validated.csv` puts Abraham Morse in the **United States**. The campaign
never had a person-level geo rule to violate — see recommendation 4. `[FACT]`

**Huma's three responders are four.** Sadeq N. Yazdi resolved to Huma via a duplicate-profile ID
collision (see "Account-based targeting" above). The account-based read is in that section: real
value, real cost, and repeatable only on owner titles. `[FACT]`

---

## Data corrections made during this analysis

Both inside this campaign folder, both non-destructive:

1. `responses-classified.csv` — added a `linkedin_url` column (joined from `responses-raw.csv`,
   0 rows unmatched) so `outbound-registry.py reply` can join. Without it the mandatory Step 9
   registry write silently recorded 0 of 13 outcomes.
2. `responses-classified.csv` — Sadeq N. Yazdi's company changed from "Unknown (no thread_file)"
   to Huma, with the resolution and thread path recorded in the cell. Categories, summaries,
   confidences and drafts are untouched.

Neither the classifier's judgement nor any other file was modified. A pre-edit copy of the
original is in the session scratchpad.
