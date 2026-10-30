---
product: fitxpress
type: pooled-campaign-analysis
analyzed: 2026-10-30
data: data-2026-10-29.md (scripts/outbound-learnings.py build, Closely snapshot 2026-10-29T23:37Z)
scope: 19 mature campaigns (3,257 invites, 884 accepted, 113 replied), 1,433 people at person level, 72 classified repliers
learnings_version: 2026-10-30
status: applied to learnings.md 2026-10-30 (Vadim: «роби всі кроки»); proposals P1–P6 await Vadim
---

# Pooled outbound analysis — 2026-10-30

Numbers come from `data-2026-10-29.md` in this folder. Every rate has its denominator, and
`[lo–hi]` is the 95% Wilson interval in percent. Evidence tiers follow campaign-analyzer:
**confirmed** = 15+ replies per side and intervals that do not overlap; **directional** =
fewer replies or overlapping intervals, but the same direction in most campaigns; **no
evidence** = we looked and nothing separates.

## TL;DR

1. **Reply rate has not moved in four months, and the pipeline is not why it varies.** Replied/accepted
   was 39/305 (12.8%) in July before the agents, 36/285 (12.6%) in the agent pilot, 32/252 (12.7%)
   in pipeline v2. Gates, cards and lanes made the messages safer and cleaner; they did not
   change how many people answer. The variance sits in **who sends to whom**: Katerina (UK)
   gets 50/282 (17.7%) [14–23] replies and 17/159 (10.7%) [7–16] positives per accepted; the
   other four senders together get 63/602 (10.5%) [8–13] and 17/415 (4.1%) [3–6]. Olena gets
   2 positives from 157 accepted.
2. **The people who answer are not the people we rank highest.** C-level and founders reply to
   5/344 (1.5%) [1–3] of invites, everyone below them to 37/1064 (3.5%) [3–5]. The validator's
   P1 tier: 2/200 (1.0%) [0–4]; P3 + P4: 29/671 (4.3%) [3–6]. The `referral` lane (non-buyers
   asked who owns the topic) out-replies the buyer lanes in 5 of the 6 campaigns that had both:
   21/475 (4.4%) [3–7] against 21/958 (2.2%) [1–3]. Positives come from practitioner and
   programme leads: coaching lead, Tier 3 practitioner lead, obesity consultant, clinical
   operations lead, head of commercial.
3. **Replies keep asking the same four things, and we have no ready answer to any of them**:
   how is this different from InBody / Withings / Technogym / a BMI-from-photo app (4 of 34
   positive repliers), send a one-pager or materials (4 of 34), FDA / CE status (1), iOS and
   Android (1). 5 of 72 repliers had left the company the list said they worked at.

## The funnel

| | invites | accepted | replied / accepted | positive / accepted |
|---|---|---|---|---|
| All 19 mature campaigns | 3,257 | 884 (27.1%) [26–29] | 113/884 (12.8%) [11–15] | 34/574 (5.9%) * |
| A · Jul 7–16, before agents (3) | 961 | 305/961 (31.7%) | 39/305 (12.8%) [9–17] | not classified |
| B · agent pilot, Jul 21–Aug 11 (5) | 1,189 | 285/1189 (24.0%) | 36/285 (12.6%) [9–17] | 15/285 (5.3%) [3–9] |
| C · pipeline v2, Sep 12–Oct 6 (10) | 901 | 252/901 (28.0%) | 32/252 (12.7%) [9–17] | 18/247 (7.3%) [5–11] |
| D · question in M1, from Oct 7 (1 mature) | 206 | 42/206 (20.4%) | 6/42 (14.3%) [7–28] | 1/42 (2.4%) |

\* positives exist only for campaigns with a folder (cohort A has none).

Positive per accepted rose from 15/285 (5.3%) to 18/247 (7.3%) between B and C. The intervals
overlap ([3–9] and [5–11]), so this is directional.

## Confirmed

**C1. Sender and market decide more than anything we control in the pipeline.**
Katerina: 50/282 (17.7%) [14–23] replied, 17/159 (10.7%) [7–16] positive per accepted. The
other senders: 63/602 (10.5%) [8–13] and 17/415 (4.1%) [3–6]. We cannot split CEO title from
UK market: Katerina is the only CEO and the only UK sender. Her best campaign,
`2026-10-06-uk-weight-management`, gave 11/45 (24.4%) replies and 8 positives.

**C2. Vadim's Australian invites are accepted least.** 60/338 (17.8%) [14–22] across both
mature AU campaigns, against 824/2919 (28.2%) [27–30] for every other sender. The immature
`2026-10-11-au-sport-fitness` so far: 9/84 (10.7%). Invites carry no note, so the list, the
market and the sender's profile are the only inputs. Replies after acceptance are normal:
8/60 (13.3%).

**C3. Pipeline changes did not move the reply rate** (TL;DR 1). Further work on message
mechanics should be judged against this flat 12.6–12.8% line, not assumed to help.

## Directional (act on as defaults, re-check monthly)

**D1. Seniority and priority run backwards.** See TL;DR 2. Holds without the UK
weight-management campaign: C-level 5/306 (1.6%) vs 11/358 (3.1%) for director/head. The
rates are per invite, so part of the gap is C-level people not accepting strangers. Of 34
positive repliers, 3 were C-level (CPO at Mosh, a subscription chief at iFIT, the founder of
Sensorial).

**D2. The referral ask works as a way in.** 5 of 6 campaigns with both lane types: referral ≥
buyer (one tie). Without UK weight-management: 12/307 (3.9%) [2–7] vs 19/903 (2.1%) [1–3]. 10
of the 34 positives are referrals, and most name a person. Nothing in the pipeline follows a
named referral up (proposal P3).

**D3. Some titles and lanes never answer.** By function (per contacted): marketing 0/52,
retention / CRM / growth 0/44, operations 0/55, engineering 1/90 (1.1%); partnerships / BD /
sales 6/83 (7.2%) [3–15] is the highest. Lanes with zero replies on 39+ people: `virtual-care`
0/94, `retention` 0/53, `weight-management` 0/42, `digital-transformation` 0/39. With 94 people
and no reply, the upper bound for `virtual-care` (4%) sits under the referral lane's rate.

**D4. Message 1 now does the work; Message 2 is fading.** Share of replies that came after
M2: 17/39 (43.6%) in July, 15/36 (41.7%) in the pilot, 8/32 (25.0%) in v2. M1 replied/sent:
20/294 (6.8%), 20/280 (7.1%), 23/234 (9.8%) [7–14]. M2: 17/272 (6.2%), 15/259 (5.8%), 8/192
(4.2%). Under the Oct-7 rule (call ask moved to M2), M2 so far: 2/49 (4.1%), immature
campaigns included. Judge the call-in-M2 rule in December, when cohort D has 15+ replies.

**D5. LatAm accepts most and converts least.** Katya's LatAm campaigns: 56/127 (44.1%)
accepted, 28/47 (59.6%) in the immature Everlab-like list; replies 5/56 (8.9%).

## No evidence (do not act on these)

- **Segment.** Reply per accepted does not separate between GLP-1 telehealth 72/576 (12.5%)
  [10–15], clinical obesity care 8/87 (9.2%) [5–17], digital fitness 14/98 (14.3%) [9–23] and
  online pharmacy 19/123 (15.4%) [10–23]. Digital fitness accepts less: 98/491 (20.0%) [17–24]
  against 576/2120 (27.2%) [25–29] for telehealth, but two of its four campaigns were Vadim's AU
  ones (C2).
- **Message 1 length.** Under 350 characters 19/581 (3.3%), 350–449 20/702 (2.8%), 450–549
  3/140 (2.1%). Keep the current limits.
- **Question mark in M1.** 1,421 of 1,433 Message 1 texts already carry one; there is no contrast to measure.

## What the replies say (72 people)

- 34 positive (11 interested, 13 question, 10 referral), 18 declines, 11 maybe-later, 9 unclear.
- **"How is this different from what we have?"** Calibrate (vs Withings Body Pro), Healthier
  Weight ("an app to calculate BMI from a photo?"), knownwell (separate MA visit + InBody),
  Clinique La Prairie (Technogym 360 / InBody). 4/34 positives.
- **"Send me something I can share."** Perspectum (one-pager), Reset Health (email info for
  the team), Welltech (materials for the product team), Huma (feature list for managers). 4/34.
- **Compliance and platform.** TytoCare: FDA / CE approval. Huma: iOS and Android or Android only.
- **Stale contacts.** 5/72 repliers no longer worked at the company (Sidekick, MyFitnessPal,
  9am, LighterLife, iFIT).
- **Authenticity.** "Is this an automated message?" (Counterweight), "It's you?" (BODYHIT). 2/72.
- **Not now.** 11 maybe-later, most with an open door and no date. Nothing re-contacts them.

## What changed in the system today

- `workspace/outbound/learnings.md` (version 2026-10-30): the rules above, by tier. The
  hypothesis-generator reads it and must say what it applied; the validate and messages cards
  carry its People and Messages sections verbatim.
- Reply outcomes written to the five profile registries (`outbound-registry.py reply`, 18
  campaigns). 23 replies of the July/Aug campaigns did not match a registry URL (07-21: 4,
  07-31: 13, 08-07: 6); those campaigns were recorded before URL normalisation.
- Monthly loop: `outbound-learnings.py monthly` on the 1st, then `/outbound learnings` →
  proposals → Vadim → `/outbound learnings-apply`.

## Proposals for Vadim (not applied)

- **P1. Australia sender.** C2 says the invites, not the messages, lose AU. Options: refresh
  Vadim's LinkedIn headline/photo for the AU audience, or send the next AU list from a profile
  with a sales title. Decision needed before more of `au-sport-fitness` goes out.
- **P2. One reply kit, four answers.** A one-pager (PDF link) per segment, plus approved short
  answers to: difference from InBody / smart scales / BMI apps, FDA / CE status (the §12 line
  exists), iOS + Android SDK. The classifier's `suggested_reply_draft` would cite them.
- **P3. Follow named referrals.** 10 referrals, most with a name. Proposed: the morning report
  lists each named referral once, and the next campaign of the same profile imports them.
- **P4. Re-contact maybe-later at 90 days.** 11 people. The registry releases `no_reply`
  after 6 months; maybe-later would come back at 3 with a short check-in.
- **P5. Olena's EU.** 2 positives from 157 accepted across four campaigns, while reply rate
  recovered to 10/76 (13.2%) in the last two. Worth a look at the profile and at which EU
  countries replied before the EU insurance campaign starts.
- **P6. Stale contacts.** 5/72 repliers had left. Sales Navigator lists are fresher than Apollo;
  the validator could drop people whose current role start is unknown in Apollo-sourced rows.

## Limits

- Person-level rates are per invite: Closely gives no per-person acceptance.
- `2026-07-27-australia-telehealth`, `2026-08-07-us-digital-fitness`,
  `2026-07-31-uk-telehealth-digital-health` and `2026-07-23-israel-telehealth` are funnel-only:
  their import files do not match what Closely loaded.
- Cohort A has no folder: messages, lanes and classified replies are unknown.
- Positive replies are not meetings. Whether any became a deal is in HubSpot, not here.
