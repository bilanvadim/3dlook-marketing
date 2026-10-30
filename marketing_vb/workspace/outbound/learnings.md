---
version: 2026-10-30
data: workspace/outbound/learnings/data-2026-10-29.md
analysis: workspace/outbound/learnings/2026-10-30-pooled-analysis.md
next_review: 2026-12-01
---

# Outbound learnings

What past campaigns showed, and what every new campaign does with it. Built from the pooled
numbers of all mature campaigns, not from one campaign. Every rate keeps its denominator.

## How to use

- **hypothesis-generator** reads this whole file before writing. The hypothesis gets
  `learnings: <version>` in its frontmatter and a `## Learnings applied` section that names
  the IDs below it follows and the ones it departs from, each with one line why.
  `outbound-pipeline.py hypothesis-gate` fails a hypothesis created after 2026-10-30 without both.
- **icp-validator** gets `## People` verbatim in its validate card.
- **message-sequencer** gets `## Messages` verbatim in its messages card.
- **Tiers.** `[confirmed]`: follow it unless the hypothesis says why not. `[directional]`: the
  default; departing from it needs a one-line reason. `[watch]`: being measured, do not act on it.
- This file changes only through `/outbound learnings-apply` after Vadim approves a monthly
  proposal. Numbers come from the data file named above; do not recompute them here.

## Hypotheses

**HYP-1 [confirmed] Reply rate is flat; message work did not move it.** Replied per accepted:
July before the agents 39/305, agent pilot 36/285, pipeline v2 32/252 (12.6–12.8%). Targets for
a new hypothesis: replied/accepted at the pooled level (113/884) and positive/accepted at the
pooled level (34/574). Do not promise more on the strength of a new angle alone.

**HYP-2 [confirmed] Sender and market decide most of the variance.** Compare a new campaign with
its own sender's baseline, not with the pooled one:

| sender | accepted / invites | replied / accepted | positive / accepted |
|---|---|---|---|
| katerina (UK) | 282/940 (30.0%) | 50/282 (17.7%) | 17/159 (10.7%) |
| nick (USA) | 192/777 (24.7%) | 24/192 (12.5%) | 5/104 (4.8%) |
| olena (Europe) | 256/948 (27.0%) | 22/256 (8.6%) | 2/157 (1.3%) |
| katya (Israel, LatAm) | 94/254 (37.0%) | 9/94 (9.6%) | 5/94 (5.3%) |
| vadim (Australia) | 60/338 (17.8%) | 8/60 (13.3%) | 5/60 (8.3%) |

Katerina is the only CEO and the only UK sender, so title and market cannot be separated (OPEN-2).

**HYP-3 [confirmed] Australian invites are accepted least.** Vadim's AU lists: 60/338 accepted,
against 824/2919 for every other sender. Size an AU list for that rate: about 1.6 times the
invites for the same number of accepted.

**HYP-4 [no evidence] Segment does not predict reply rate.** GLP-1 telehealth 72/576, clinical
obesity care 8/87, digital fitness 14/98, online pharmacy 19/123 replied per accepted; the
intervals overlap. Do not choose or drop a segment on past reply rates. Clinical obesity care
has the fewest positives (3/87): `[watch]`.

**HYP-5 [directional] LatAm accepts most and replies least.** Accepted 56/127 and 28/47 (the
second still running); replied 5/56. A LatAm hypothesis plans for many accepted and few answers.

**HYP-6 [directional] Lanes that drew no reply.** `virtual-care` 0/94, `retention` 0/53,
`weight-management` 0/42, `digital-transformation` 0/39 people contacted. Do not reuse these
angles as written. A hypothesis that needs one rewrites it and marks it as a test.

## People

**PPL-1 [directional] Seniority runs backwards.** C-level and founders replied to 5/344
invites, everyone below them to 37/1064. The validator's P1 tier: 2/200; P3 and P4 together:
29/671. Keep decision-makers on the list, but do not give P1 for title alone, and give every IN
account at least one route-in below C-level (programme, clinical, practitioner or partnerships
lead) when the export has one. Part of the gap is C-level people not accepting strangers'
invites; the rates are per invite.

**PPL-2 [directional] The referral ask is a way in.** `referral` lane: 21/475 replied; buyer
lanes: 21/958. Referral replied at least as often as buyer lanes in 5 of the 6 campaigns that
had both. A non-buyer at an IN account in a relevant function is a referral-lane PASS, not a FAIL.

**PPL-3 [directional] Functions that do not answer.** Per person contacted: marketing 0/52,
retention / CRM / growth 0/44, non-clinical operations 0/55, engineering 1/90. Partnerships, BD
and sales: 6/83, the highest. Clinical operations titles count as clinical, not operations.
Do not fill an account's cap with marketing, CRM or engineering people.

**PPL-4 [directional] Who the positive repliers were.** Of 34 positive repliers, 3 were C-level.
The rest: coaching lead, Tier 3 practitioner lead, obesity consultant, dietitian, clinical
operations lead, head of commercial, regional partnerships manager, director of clinical
programmes, senior director of clinical research, GM health and wellbeing.

**PPL-5 [watch] Stale contacts.** 5/72 repliers had left the company on the list.

## Messages

**MSG-1 [directional] Message 1 carries the campaign.** In pipeline v2, 23 of 32 replies came
on Message 1; Message 2 replied/sent fell from 15/259 in the pilot to 8/192. The strongest
product specific and the number go in Message 1, not saved for Message 2.

**MSG-2 [watch] The call ask in Message 2** (rule since 2026-10-07): 2/49 so far, immature
campaigns included. No change before the December review.

**MSG-3 [no evidence] Length within the limits.** Message 1 under 350 characters 19/581,
350–449 20/702, 450–549 3/140 replied. Do not trim for its own sake.

### What people ask back

**MSG-4 [directional] "How is this different from what we already use?"** 4/34 positive
repliers asked it (a smart scale, a clinic body-composition device, a BMI-from-photo app). Where
the campaign rules allow, say once what the scan gives that a device in the clinic does not
(two photos at home, 80+ body measurements, a 3D model, between visits), using only the facts
in the card. Never name the device or its maker.

**MSG-5 [watch] "Send me something I can share."** 4/34 positive repliers asked for a one-pager
or materials. Do not promise materials in a message until the reply kit exists (proposal P2).

**MSG-6 [directional] Compliance and platform questions** (FDA / CE 1, iOS and Android 1) are
answered from `brand-assets/product-info/compliance.md` §9 and the product facts, never improvised.

**MSG-7 [directional] Sounding automated.** 2/72 repliers asked whether the message was
automated or who was writing. Openers that could fit any company read as a template.

## Open questions

- **OPEN-1** Does the Message 2 call ask beat the old Message 2? December, once the campaigns
  started after 2026-10-07 have 15+ replies.
- **OPEN-2** Is Katerina's lead the CEO title or the UK market? Only Vadim can set up the test
  (a UK list from another profile, or a non-UK list from Katerina).
- **OPEN-3** Does AU acceptance recover after a profile change (proposal P1)?
- **OPEN-4** Insurance underwriting (UK, EU, US) is the first large non-weight-loss segment.
  Compare with HYP-1 and HYP-2 in December.
- **OPEN-5** Do positive replies become meetings and deals? Needs a HubSpot join.

## Change log

| version | what changed | source | approved |
|---|---|---|---|
| 2026-10-30 | First version: 19 mature campaigns, 3,257 invites, 113 replies | learnings/2026-10-30-pooled-analysis.md | Vadim, 2026-10-30 («роби всі кроки») |
