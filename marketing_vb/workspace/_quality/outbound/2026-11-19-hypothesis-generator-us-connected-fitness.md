---
qc_date: 2026-11-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-19-us-connected-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-19

**Artifact:** `workspace/outbound/campaigns/2026-11-19-us-connected-fitness/hypothesis.md`
**Total: 17/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Every item in Vadim's brief is applied. M1 has 4 parts with one question and no call or link (l.454-460). M2 has the call and the calendar link (l.509-513). No client names (l.530-532). Retention appears only as the marked `membership` TEST (l.394-399, 605-610). The 9 non-customer companies return (l.331-351). Zing Coach and Verv stay out (l.359, 590).
- Vadim's 2026-11-19 decision (only new people; anyone nick has already messaged stays out) is not recorded under "Vadim's standing decisions". Open Q6 (l.732-736) still asks it, citing the Katerina re-invite precedent. The default matches the decision, but the question is stale.
- Sibling files exist and were not reconciled. `2026-11-19-au-connected-fitness/hypothesis.md` l.92 routes "Centr and F45 (US head office, `nick`)". This file leaves Centr unassigned and out of the seed list (l.323-324, 670), and excludes F45 as a gym chain (l.580-581). Both companies currently belong to no profile.
- §8 buyer-title departures are only partly declared. "Head of Growth" is named (l.146, 618-620). "VP User Engagement / VP Engagement / Retention" and "Digital Experience Manager" from `icp-detail.md` §8 are dropped without a line.

### B. Factual accuracy — 4/5
- Product claims match the live page and `proof-points.md`: 2 photos, 80+, the canonical "under 45 seconds from the photos to structured results", 100+ clients, 112,100 scans 3DLOOK-wide, the pilot design, Pro-plan 3D tools, estimates wording, and the repeatability sentence verbatim from the page or `accuracy-formulations.md` §1.2. There is no accuracy %, no fabricated client and no anti-positioning.
- The page says RTPV comes "with voice prompts" (page l.100). The roadmap marks native voice guidance as still in testing, and the Rules correctly ban it (l.486-487). The page-vs-roadmap mismatch is not raised for Vadim.
- l.577-579: ClassPass is grouped as "employer-paid, with no member check-in". ClassPass is mainly a consumer credit subscription, so the stated reason is wrong for it. The out decision still holds on the no-check-in ground.
- l.314: Aaptiv is seeded in group D with no flag. August's `companies.csv` row 22 records its Feb 2026 pivot to employer MSK (AaptivMSK). By this file's own anti-case (l.577), that is employer wellness.
- **Exclusions evidence.** Noom and WW are evidenced through `competitors.md` l.21/58 (Prism runs inside Noom and WW "AI Body Scanner"; verified 2026-10-15). They are also out a second time as §1 GLP-1 programs, so this is defensible. Tempo rests on a 2023 Business Wire release (l.87). FitnessAI rests on an undated press release (l.89). Neither has a 2026 check that the scan is still live, or that Tempo still trades. They should be "step 2 re-checks", not a hard out.
- Research figures (Peloton churn 2.2%/1.8%, -9%/+7%, Adjust 24%→7%, JMIR 70%) are all linked and kept out of copy (l.73-74, 80-82, 519-521). QC could not open the links (no web access).

### C. Brand & tone — 3/3
- No em or en dashes. None of the banned words appear. "plus" appears only inside a quote (l.64). Claims discipline is canonical: "FitXpress is not a medical device.", estimates rather than measurement for body fat, no compliance-cert wording, no "free" pilot (l.502). No issues.

### D. Format & structure — 3/3
- The frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group: 50`, `learnings: 2026-10-30`, `banned_terms`). Every template section is present. There is a `titles` block and an Account facts placeholder, and `## Learnings applied` cites the IDs. No issues.

### E. Output quality — 3/4
- **Infeasible uniqueness rule.** l.548-550 says no two people at one company may share "the pain", "the order of Message 1's parts" or "a Message 2 value point". The pain list is closed at 5 options (l.461-466). Message 1 has 4 parts with the question last (6-24 orders). Peloton is expected to return 60-120 rows at cap 50 (l.225-226). Writers will either break the rule or invent pains outside the approved list. The rule also contradicts the ratio rule at l.425 ("one topic ... about a fifth of a company's people").
- **August failures, fixed vs only flagged.**
  - Fixed: the technical lane is removed (l.120); WEAK is marked fill only (l.117-119); the campaign covers one segment (l.125); a title pull with an Apollo top-up replaces company-only pulls (l.122-124).
  - Only flagged, with the default left as it was: concentration (cap 50, so Peloton and iFIT can take up to 100 of 200-300 SEND; l.298-299, 693; Q7) and acceptance (headline is Q8 only).
  - Risk 1 (l.691-692) diagnoses a low acceptance rate after 150 invites but gives no pause or stop action. The post-mortem proposed: below 20% at 150 or more invites, stop and check the profile.
- l.219: the boolean `NOT Retention` / `NOT Growth` also drops combined owners such as "Head of Subscription & Retention". The post-mortem (l.187-190) named that as the best predictor of a reply.
- l.686-687: the `membership` TEST will hold about 5-15 people (few CSO or Head of Membership roles exist). It has no minimum N and no decision rule, so the HYP-6 rewrite cannot be read.
- **Rules as targets.** Mostly yes. Only canonical lines are quoted, and l.374-375 and 561-562 say lane notes are not copy. Two exceptions are sentence-shaped and will be pasted:
  - The "angle for every lane" paragraph (l.377-384), e.g. "FitXpress turns that check-in into a measured record inside the company's own app".
  - The five pain clauses (l.461-466).
- The seed list is thin for the 30-company floor. It has about 33-34 seeds, several already flagged in August: Caliber possibly under $1M, FitOn and obé borderline on revenue, Aaptiv pivoted.

## Top 3 issues (priority for improver)

1. **Fix the per-company uniqueness rule (l.548-550).** Make it ratio-based (no pain, order or value point used by more than about a fifth of a company's people). Otherwise it is impossible at Peloton and iFIT scale with a closed list of 5 pains and 4 parts.
2. **Close the two August failures that are only flagged.**
   - Put a concrete stop rule in Risk 1: below 20% acceptance after 150 invites, pause and check Nick's profile.
   - Make the Q7 recommendation explicit as the expected-SEND math: up to 100 of 200-300 SEND go to two accounts at cap 50.
   - Drop `Retention` from the NOT list, or add "Subscription & Retention" style titles, so the persona August flagged is not filtered out.
3. **Reconcile with the sibling campaigns and today's decision.**
   - Centr and F45: the AU file routes both to nick. Add Centr to the seed list and state F45's status explicitly.
   - Record Vadim's 2026-11-19 "only new people" decision and close Q6.
   - Fix the ClassPass rationale and flag Aaptiv's pivot.
   - Move Tempo and FitnessAI to step-2 re-checks.

## Coordinator review

- agreement: ✅ agree (17/20). Q6 is already answered: Vadim 2026-11-19 «Ні, тільки нові люди» — record it as a Vadim's decisions block in the fix round. Centr/F45 routing is a cross-campaign gap: settle in all four files at once.
- top_issue: the per-company uniqueness rule (l.548-550) cannot hold at Peloton/iFIT scale — make it ratio-based before step 5; plus the cap-50 concentration risk in two accounts.
