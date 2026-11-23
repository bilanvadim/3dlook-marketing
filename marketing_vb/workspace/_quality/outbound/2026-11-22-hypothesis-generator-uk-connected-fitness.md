---
qc_date: 2026-11-22
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-22-uk-connected-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-22 (UK connected fitness, katerina)

Saved by the coordinator from the QC agent's final message (the agent could not write report files).

**Artifact:** `workspace/outbound/campaigns/2026-11-22-uk-connected-fitness/hypothesis.md`
**Total: 16/20** — good. Approve after the fixes below. It is the strongest of the five sibling files: most defects flagged in the EU, AU and US reports are fixed. Five items still need edits before step 2, and Open questions 2 and 7 decide whether the gate can be met at all.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## Brief checklist

- **Carried over and correct:** only new people (l.29, 107, 311); companies without a contract return with their history, customers stay out (l.24, 266); no £ or $ figures, "no integration fee" once in Message 2 only (l.242); page URL in about half of Message 2s, never in Message 1 (l.243); 900/700 (l.9, 230); Message 1 pain → mechanism → outcome, M1 asks, M2 calls (l.231, 236); easy out for non-buyers only (l.237); marketplaces, aggregators, content-only platforms, device makers, in-club scanner vendors and phone-scan apps out (l.269-272); deal targets of the last ~12 months out, acquirers stay in, deals never mentioned (l.267).
- **Repeats rule:** the 2026-11-20 rule is applied (l.222, 252, 300, 319). No "fifth" ratio left.
- **Re-contact:** no time window (l.291, 321).
- **Geo:** UK product decisions; Ireland → olena, US → nick, AU/NZ → vadim; Northern Ireland stays with katerina (l.43, 274, 414).
- **Product claims** from the live page (l.130-133); data roles from compliance.md §9 UK line and §1/§10 (l.247-248, 135).
- **Repeatability wording deviates from the brief (l.241):** only the page form is allowed. Add the accuracy-formulations §1.2 form ("For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.") as preferred; the gate accepts both (`MANDATED_STEMS`).
- **Lane notes parse.** QC traced the regex by reading (no shell); two targets are under the 4-content-word floor: leadership "how the company decides on a new member feature" (l.218) and technical-integration "review of a new data processor" (l.219).

## Registry check (katerina-registry.json)

The re-contact table (l.97-107) matches the registry exactly: The Body Coach 6, Sweatcoin 6 (2026-07-31); Nutracheck 7 (Daisy Ford maybe-later 2026-10-01), Coopah 3, Fiit 3, WithU 2 (2026-09-01); Nuffield Health 1 (2026-09-27). NowPatient 6 and Medicspot 5 match. Global registry 538 companies. None of the fresh candidates is in any profile's registry (only Virgin Active Australia, vadim). Minor: every katerina campaign has `send_confirmed: false`, so "People sent" means imported.

## Earlier QC findings: fixed or repeated

- **Fixed:** progress-journey gate for group A; "check-in" rule in club copy; `term=` for retention; aggregators out of B; voice prompts out; pilot design ~250 characters; HYP-6 read on M2-stage `member-app` replies with a minimum N; no 3-month rule; lane-note format; "the program compares scans it selects"; repeats rule; "only new people"; franchise rows OUT by default; CEO/Founder/MD in titles; GDPR wording from compliance.md; Life Fitness, Matrix, Withings, Oura in banned_terms.
- **Repeated:** pain list vs training-plan-only apps (LatAm E); routing limbo for platforms with a foreign parent (US: Centr, F45); concentration math not done (US); medical-device clause mandatory in fitness copy with no Open question (LatAm C); a corrective "X, not Y" in card text (AU C); "so" banned only before a benefit, l.260 (matches hard-bans-card.md l.50, narrower than CLAUDE.md §6); "Digital Experience Manager" and "Product Manager" (icp-detail §8) dropped without a departure line at l.394 (EU, US).

## What was wrong (specific)

### A. Adherence — 4/5
- Every brief item carried over; registry and learnings figures right (HYP-2 282/940, 50/282, 17/159; HYP-6 0/53; PPL-3 0/44 and 1/90; MSG-1 8/192).
- Four defects already flagged in sibling reports return (list above).
- l.241 allows only the page repeatability form.
- Web budget used up (25/25, l.412); the not-verified list is honest.

### B. Factual accuracy — 4/5
- **Clean:** every copy number is in proof-points.md or on the live page (two photos, 80+, "under 45 seconds from the photos to structured results", <1 cm, 100+ in the l.108 wording, 112,100 as 3DLOOK-wide scale, day-30/day-90 only inside the pilot); Adjust and Kidman banned from copy; no client named; hosting wording matches compliance.md §1.
- **l.142:** "Katerina's acceptance and reply rates are the strongest of the five senders (HYP-2)" — wrong for acceptance: katya 37.0% vs katerina 30.0% (learnings.md l.38, 41). Reply and positive rates are the highest.
- **l.31, l.123:** "UK operators were the buyers in 2026's European deals" includes PureGym/NonStop, "date not confirmed".
- **l.54, l.372:** the énergie financial-partner search is undated and treated as a live risk; its HCM article ID (337130) sits well before 2024 items (Membr 352593), so it is probably years old.
- **l.85:** Glofox → olena on its Dublin HQ while Membr → nick on its US parent. Glofox's parent is ABC Fitness (US). The two rules do not match.
- **Sourcing:** ~60 external links, mostly primary or trade press; market figures kept out of copy.
- **Web spot-check NOT done** (no web tools in the QC session): Third Space (KSL, Permira, £700m), Holmes Place Germany, Aspria, PureGym/NonStop, the ONE FIIT pivot, HQs of Fitr, PT Distinction and My PT Hub are not re-verified.

### C. Brand & tone — 2/3
- No dashes; no banned words outside the rule that bans them (l.260).
- **l.245-246:** "FitXpress is not a medical device." mandatory in every Message 2 of four lanes for gym and app readers. audience.md §3 (fitness): "Don't: medical, diagnostic, or clearance language… lighter and less clinical." LatAm dropped it. Needs an Open question, not a silent default.
- **l.233:** pain topic "training metrics that show the work done, not the body change it is for" is a corrective "X, not Y" that goes to the card.
- **l.260:** "so" banned only before a benefit (minor).

### D. Format & structure — 3/3
- Frontmatter complete in the EU keys; `titles` block, Account facts placeholder, every template section, Learnings applied with IDs.
- Minor: Simply Gym is in `banned_terms` (l.15) and in the step-2 names (l.67), yet l.415 says "none of today's candidates is in the list".

### E. Output quality — 3/4
- **Strong:** honest gate count (12-19 vs 20) up front (l.32); known-links table (l.253); `term=` and `public_contract=` flags; Third Space held; device and appointment on the page's terms (MSG-4); re-contact history exact; HYP-6 decision rule with minimum N.
- **Pain topics vs the likeliest IN accounts:** the A gate (l.45, l.329) admits training-plan-only apps with `body_metrics=none` (PureGym, The Gym Group, Virgin Active, Fitness First), but every A pain topic at l.233 assumes a weight log, photos, tape or a device; the one that fits is limited to C. Writers will invent a pain or use a false one.
- **The gate is not set up for Vadim to decide:** the 9-13 A estimate includes the public leisure operators (Open question 2); the "no" count (~6-10 A, 9-16 total) is not shown. Fresh C apps are excluded from the gate (l.91) although l.88 calls C the page's literal audience; Open question 7 offers only "C on top". l.343 "at least 60 people reach PASS" vs l.353 floor of 100 invites.
- **Honest widening options (not verified):** the full top-20 operator list of the 2026 Evolve report the file cites; more UK online-coaching platforms with client check-ins (e.g. Kahunas, PT Minder); more trust/private leisure operators if Open question 2 is yes; counting fresh C toward the gate as an explicit option.
- **Routing limbo (l.85):** Membr → nick "if his campaign takes it", but nick's list is closed; Glofox → olena, whose list does not include it. Both end up with no profile.
- **Concentration:** PureGym, The Gym Group, Virgin Active, David Lloyd and Nuffield Health at 50 each = up to 250 invites, the whole 150-250 target (l.206, 353, 365). No split given.
- **Minor:** one titles block for A, B and C (l.168-204); "Head of Fitness", "Head Coach", "Head of Personal Training", "Managing Director" also exist at club or franchise-unit level and l.162 has no rule for club-level holders of head-office titles. Village Gym (l.58) has no deal-status check.

## Top 3 issues (priority for improver)

1. **Pain topics vs the group A gate:** open the training-metrics pain to group A training-plan apps, rewritten without the corrective "X, not Y"; or make `body_metrics=none` rows need an Account facts line naming a body-data step.
2. **Make the gate decidable:** expected fresh A+B count under Open question 2 yes and no; "count fresh C apps toward 20" in Open question 7; concrete widening sources; l.343 vs l.353; invite split for the five large accounts.
3. **Routing, facts and carried-over defects:** one parent rule for Membr and Glofox; fix l.142 and l.31/l.123; Simply Gym across l.15/67/415; re-date énergie; Open question on the medical-device clause; §1.2 repeatability form; declare the "Digital Experience Manager"/"Product Manager" departures; lengthen the two short question targets.

## Not done in this run

- notify.py not sent (no shell in the QC session).
- Web spot-check not performed (no web tools in the QC session).
- `question_targets` not executed by QC (traced from outbound_pack.py l.1965, l.1988-2009).

## Coordinator review

```
agreement: ✅ agree
top_issue: the group A pain topics assume a body log that the likeliest IN operators (training-plan apps) do not have; fix together with a decidable step-2 gate before research
```

- `question_targets()` run by the coordinator on the file text: **15 targets parse** (not 20/18 as traced), so lane notes are readable by `outbound_pack.py`; the two short targets QC named are among those dropped.
- Routing: one parent rule (product decisions follow the parent that runs the product) is applied in the fix round; Membr and Glofox are not `katerina`'s either way.
- Medical-device clause and the short-list gate go to Vadim at the hypothesis checkpoint, with the other open questions; the fix round runs on a fresh hypothesis-generator after his answers (v1 snapshot `hypothesis-v1-2026-11-22.md`).
