---
qc_date: 2026-11-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-19-eu-connected-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-19 (EU connected fitness, olena)

**Artifact:** `workspace/outbound/campaigns/2026-11-19-eu-connected-fitness/hypothesis.md`
**Total: 15/20** — good, at the bottom of the band. Fixes 1 and 2 need to land before step 2, because fix 1 changes which companies company-researcher admits.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

## Answers to the three judgment questions

**1. Does the sub-segment (gym chains, corporate fitness networks, club-app platforms) still fit the page? Only partly.**
- The page is written for apps. The H1 says "for fitness apps". How it works names "A connected-fitness platform, workout app or coaching app" (page l.87). The Problem section covers app retention only (Adjust 24% to 7%, Kidman 70%, page l.69-81), and the pilot counts "Free-to-premium conversion" (page l.322). Clubs appear in the comparison column and in one sentence (page l.213).
- Hyp l.81 says "The page's argument is the club device". That misreads the source the segment choice rests on. Group C, the page's literal audience, is demoted to re-contact. That is defensible, since `olena` sent to 125 of them on 09-14, but it means the page's wording has to be adapted for clubs. In three places it was not:
  - **"check-in".** In a gym member app, check-in means entering the club (QR at the door). The use case (l.86) reads "at onboarding and at each check-in, between club visits", and the pilot (l.202) reads "at the first check-in". A club product lead will read both as club entry, which contradicts "no club visit". No rule tells writers what the word means for group A.
  - **Retention.** Line 202 says "For clubs, retention means membership retention". Day-30 and day-90 membership retention is often fixed by minimum terms or notice periods at European chains. The row schema (l.266-270) has no field for contract term. This is the 11-05 underwriter failure the prompt warns about, and it sits in the lane that carries the HYP-6 test.
  - **The IN gate for group A** (l.258-264) asks for an app, not for a progress, assessment or training-plan feature inside it. An app that only handles access and booking passes. The page's premise is "The scan runs inside check-ins the program already has" (page l.85). The US sibling requires an app that "already runs a progress check-in", and the LatAm sibling requires a published body assessment. Here `body_metrics=none` is recorded but does not fail the row.
- **Group B.** Urban Sports Club, Gymlib and MyClubs are access and booking marketplaces, and Funxtion is a content platform. That makes them the hypothesis's own anti-case (l.231). B's IN criterion, "member-facing corporate network product" (l.261), still lets them through. The club-software white-label vendors (Virtuagym, Resamania, Trainingym, bsport, Eversports) fit the partnership thesis. The aggregators do not.
- **Across profiles.** The same page gets three readings today. The US sibling excludes gym chains outright (`2026-11-19-us-connected-fitness/hypothesis.md` l.29-31). LatAm makes chains primary, with evidence that they run assessments in the club. EU makes chains primary without that evidence. Vadim should decide which reading is right.

**2. Is the buyer persona the owner of the member app? By definition yes, but the pull will not reliably reach that person.**
- Line 117 names "the head-office owner of the member app and its check-in journey", and the titles at l.138-153 are product and digital roles. Three gaps:
  - **"Self-run" is never checked.** The group A header says "self-run member app", but step 2 only checks for a store listing. At mid-size and franchise chains, the branded app is often a white-label from club software with no in-house product owner. Pulls there will return CEO, MD and Head of Fitness, so the campaign's weight drifts to the routing persona (the `training` lane). The 150-250 PASS target (l.283) depends on product people existing at these chains.
  - **The partnership lane misfires at operators.** The `partnership` lane also covers "partnerships or BD heads at operators" (l.184), but its question targets are about distributing features to partner clubs. At an operator, partnerships sells corporate memberships.
  - **Minor:** "Digital Experience Manager" from icp-detail §8 l.306 is missing from the titles.

**3. Are the Rules written as targets? Mostly yes.**
- Targets are labelled "(a target; ...)" (l.179, 198, 199). Lane notes are declared non-copy (l.177). Quoted lines are limited to canonical copy (l.220). The easy-out is written as a target (l.186).
- Four targets are written as sentences that writers will copy:
  - l.198: "a typed weight and progress photos that are not measured, or a body-composition check that happens only at a device in the club, where each repeat needs a club visit. Change in waist or lean mass that a weight figure does not show."
  - l.199: "the check-in its app already has, with a structured body record it owns, in its own brand."
  - l.207: "(between visits, on the member's own phone, in the company's brand, a structured record back to the app)". This is a ready-made list.
  - l.182: "at which step a scan would fit, onboarding or the first check-in". This is a ready-made question.

## What was wrong (specific)

### A. Adherence — 4/5
- **Inputs used:**
  - The learnings IDs and numbers match `learnings.md`: 0/53, 0/44, 1/90, 6/83, 256/948, 22/256, 2/157, 3/140 and 14/98.
  - The registry figures check out: 15 `olena` companies, 125 + 61 = 186 sent.
  - The 10-07 figure "107 of 158 referral" and both device-objection replies (Clinique La Prairie, Dietplus) match the CSVs.
- **The brief is covered:**
  - M1 order: l.197.
  - M2 call and calendar: l.201.
  - No client names: l.212.
  - HYP-6 marked as a test: l.203 and l.295.
  - Re-contacts carry history: l.57-77.
  - Zing Coach, Verv and Erakulis are out: l.225.
- **The pilot design is described in full (l.202), as the prompt requires, but was not checked against the club buyer.** Retention under minimum terms and "first check-in" read as club entry are not handled.
- **The HYP-6 test cannot work as measured.** The measure (l.288) is all member-app replies per 50 contacted. Retention may appear only in M2, and MSG-1 says 23 of 32 replies come on M1. A reply cannot be attributed to the retention framing.
- **Open Q3 contradicts its own rule.** It recommends a 700-character M2. M2 in `member-app` and `partnership` must carry the whole pilot (about 400 chars), the compliance line (103 or 139 chars), the call offer with a 47-char link, and a value line. That comes to roughly 690-740 characters before the optional proof line or page URL.

### B. Factual accuracy — 3/5
- **What is clean:**
  - Every number allowed in copy (l.204) is in proof-points.md or verbatim on the page.
  - The 112,100 and 100+ wordings are correct, and there is no accuracy percentage.
  - No client is invented. Erakulis is correctly excluded by name; QC confirmed it is missing from the registry.
- **Line 199 lets writers claim "guided capture with ... voice prompts" as a current capability.** roadmap.md l.27 says voice guidance is "Web ready; iOS/Android in testing", and for native apps the copy must say "coming". Club member apps are native. The page carries the same claim, so the page has the bug too. The 11-17 coordinator precedent is that roadmap.md wins over the brief.
- **Line 81** misstates the page's argument, as covered in question 1.
- **Line 106** says "no EU hosting". That is stronger than compliance.md §1: "Hosting configuration depends on the deployment environment and the customer agreement." It is an internal note, but it will steer how replies are handled.
- **Line 226** promises a date for each deal, but NonStop Gym, Aspria and Rhythmsports have none.
- **Noted, not scored:** the GDPR line (l.210) uses the page's wording. That wording differs from the canonical sentence in compliance.md §2, and compliance.md says that if another repo file disagrees, compliance.md wins. Following the page is defensible under the brief, but the conflict should be an Open question rather than resolved silently.
- **Sourcing:** 31 external sources, primary where possible (annual reports, investor decks, filings). All context figures carry URLs and are banned from copy. The SATS figure is hedged. QC had no web access and could not re-verify the deal dates or market figures.

### C. Brand & tone — 3/3
- No issues. There are no em or en dashes, and banned words appear only inside the rule that bans them (l.219).

### D. Format & structure — 3/3
- No issues. The frontmatter is complete (product, profile, market, status, use_case with an existing `fx-digital-fitness.md`, cap_per_group 50, banned_terms, learnings 2026-10-30). The `titles` block is present, every template section is in place, and Account facts is a placeholder as the prompt requires.
- **Minor gap in `banned_terms`:** it leaves out Life Fitness, Matrix, Withings, Oura, Polar and Suunto, which Anti-cases exclude (l.227, l.233). Line 218 lets former employers be named unless they are device makers, and the code will not catch these.

### E. Output quality — 2/4
- **Strong:**
  - The re-contact table, with exclusions per person.
  - The deal-target list.
  - The honest "not found" on a churn figure (l.99).
  - The set of objections and answers.
  - Function exclusions grounded in data.
- **Weak where it counts:**
  - Group A admission does not require the feature the use case plugs into.
  - "Check-in" and retention are not adapted for clubs.
  - Group B mixes real partners with marketplaces the hypothesis excludes elsewhere.
- That adds up to 30+ minutes of edits, plus a decision from Vadim on clubs versus apps for this page.

## Top 3 issues (priority for improver)

1. **Group A against the page.**
   - Add an IN condition that the member app already runs a progress, assessment or training-plan journey (`body_metrics=none` fails or is held).
   - Add a rule defining "check-in" in club copy as a progress check-in, never next to club entry or visits.
   - Ask Vadim whether access-only low-cost chains stay.
   - Line 81 should stop calling the club device the page's argument.
2. **The pilot and the HYP-6 test for clubs.**
   - Day-30 and day-90 membership retention under minimum terms: add contract term to the row `notes`.
   - Measure HYP-6 on M2-stage replies in the `member-app` lane only.
   - Resolve the conflict between the 700-character M2 cap and the full pilot design.
3. **Claims, group B and sample-like targets.**
   - Voice prompts: allowed for web flows only, and "coming" for native apps (roadmap.md l.27). Flag the same line on the live page to Vadim.
   - Reconcile Urban Sports Club, Gymlib, MyClubs and Funxtion with anti-case l.231 and with B's IN criterion.
   - Rewrite l.198, l.199, l.207 and l.182 as topic targets.

## Not done in this run
- **notify.py was not sent:** this QC session had no shell. The coordinator sends it.
- **Not re-verified on the web:** deal dates and market figures.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
