---
qc_date: 2026-11-18
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-18-uk-london-glp1-pharmacies-2/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 15/20
status: good
coordinator_review: pending
---

# QC Report — icp-validator — 2026-11-18 — B2 (uk-london-glp1-pharmacies-2)

**Artifact:** `workspace/outbound/campaigns/2026-11-18-uk-london-glp1-pharmacies-2/icp-validation-summary.md`, `.../decisions.md`
**Total: 15/20** — good (bottom of the band; three SEND rows must change before import)

Scored against `card-validate.md`, `people-compact.csv`, `already-sent.md` and the coordinator rulings relayed with the task. Stats re-counted from `decisions.md`: PASS 40 / WEAK 25 / FAIL 6; P1 6, P2 18, P3 16; angles 11/9/6/6/5/3; the 10 re-invites split 6/2/2. All match.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- The empty-profile rule is broken six times. The prompt's flag table says `empty-profile` means no PASS without a second confirmation. `decisions.md` lines 19, 33, 65, 67, 71 and 72 PASS on "title and company". The first wave held this exact pattern as WEAK: Derek Pollard and Robert Rukwira at Numan, Jane Wilkins, Kamran Raja and Karim Nassar, all with a headline that named the company.
- Six FAILs are on function alone (lines 23, 31, 46, 47, 51, 62: engineering, IT, delivery). Standing decision 4 and people-level rule 9 allow FAIL only for the wrong company, leavers, collisions and duplicates, plus the business-line and location rules. None of the six fits, so they should be WEAK. Nobody is sent either way, but FAIL should read 0 and WEAK 31.
- Done right: the full cycle (decisions, apply-decisions, skipped, summary). PPL-1 held: all six P1s are owners below C-level of a lane the first wave left open. The covered-lane ruling and the re-invite ruling were applied and listed.

### B. Factual accuracy — 3/5
- Summary lines 84 and 117 credit two decisions to a "coordinator ruling": empty profiles PASS on title alone, and HeliosX data people are "referral at best". Neither ruling is in the card or among the rulings relayed with this task (covered lane, the 10 re-invites, the three name mappings). That gives a rule break an authority nobody can trace.
- Reset Health CTO pair (lines 11, 13): the reason calls Liles's title the likely stale one because of his "agency background". The fractional signal is Nancekievill's ("CTO (Fractional) at Psyomics"). Liles and Yousaf Ahmad both moved from Tribal Worldwide to Reset, which looks like the current build team. A Group CTO and a CTO can both be current, so the "one is stale" premise is unproven and the reasoning points the wrong way.
- Yousef Yaghoubi (line 57): the reason calls him "superintendent" next to Yvonne Lim, whom `already-sent.md` lists as Superintendent Pharmacist at the same pharmacy. A pharmacy business has one superintendent, so one of the two claims is stale. This is not flagged. His profile's current role is Strategic Advisor at Farmeci.com.
- Correct and verified:
  - The Karim N. duplicate: first-wave `karim-nassar-370a55106` ("Pharmacy Owner at Simple Online Pharmacy", Motherwell) against this row, whose bio is the Simple Online co-founder.
  - Per-company counts against `already-sent.md`, and the Doctor Care Anywhere total of 10.
  - "Nobody outside the UK": the raw `Location` is United Kingdom for all 71 rows. The Australia and UAE values in `location_country` of `people-checked.csv` are the companies' HQs.

### C. Brand & tone — 3/3
- No issues. Internal document; the only em dashes are in template headings.

### D. Format & structure — 3/3
- The frontmatter is complete and every template section is there. The pools are regrouped by lane, with the reason stated.
- Minor: `status: awaiting_review` contradicts line 12 ("the SEND list below is final"). A2 uses `final_no_checkpoint` for the same situation.

### E. Output quality — 3/4
- Strong: the Karim N. duplicate catch, both stale-title pairs (Day Lewis CIOs, Reset CTOs), and the "HeliosX 14 of 16 outside the title list" concern. The P1s are exactly the lanes the first wave left open: HeliosX product, Numan operations, Second Nature clinical, Well digital, and Everest and NowPatient operations.
- Fonzie Campos (line 67) is PASS although the summary calls him "the riskiest of the six". His profile is empty, with no photo and a self-written "Co-Founder at Numan" headline only, and Numan reaches 10 people with this wave. The first wave kept this exact Numan pattern out.
- Alan Souter (line 19) is PASS P2 on an empty profile, with no photo and a headline that only repeats his title. Nothing but the company-page attachment ties him to John Bell & Croyden.
- Lane edges are inconsistent:
  - Cecilie Pérez (Head of UX Research, line 36) is a PASS referral, while this file holds data, insights, strategy and CX people at covered accounts as WEAK.
  - Jay Jetley (VP Engineering, PrivateDoc, line 35) is P2, but Nicholas Faulkner (VP Engineering, HeliosX, line 52) is P3, though no tech person had been sent at either account.

## Cross-campaign consistency (A2 vs B2)

- **Juniper:** B2 adds Erin Chuah (P3) and Catherine Bell (P2); A2 adds Ryan Nolan and Deniz Ekmekci (P3 each). With six first-wave sends, Katerina writes to 10 Juniper people. Three of the four new ones sit in Eucalyptus group functions (expansion, international). Neither summary shows the combined number.
- **PrivateDoc:** Jay Jetley (P2, B2) and Paul Marshall (P2, A2) go out the same day, making five people there with the first wave.
- **Covered-lane priority:** B2 drops to P3 when the lane is taken (Amish Patel, John Foreman, Nikita Dhain). A2 keeps Rizwan Ali at P2 next to the first-wave MD by relabelling a Deputy MD as `operations`.
- **Owner-lane angle:** `compliance` in B2, `leadership` in A2. Each matches its own first-wave campaign, so writers inside one campaign are not misled. Flag only.

## Top 3 issues (priority for improver)

1. Fonzie Campos and Alan Souter are in SEND on empty profiles with no second confirmation, credited to a "coordinator ruling" nobody can trace.
2. Six FAILs on function alone break standing decision 4; they should be WEAK.
3. Yousef Yaghoubi: the superintendent conflict with Yvonne Lim is not flagged, his current role is elsewhere, and P2 is too high.

## Per-person fix list

**Change before import (SEND 40 → 37):**

| person_id | Now | Fix | Why |
|---|---|---|---|
| fonzie-campos-b9029020a | PASS P3 compliance | WEAK | Empty profile, no photo, self-headline only; Numan at 10; first-wave Numan empties kept out |
| alan-souter-5b62085 | PASS P2 operations | WEAK (PASS P3 only if the coordinator confirms him on the John Bell & Croyden site or Companies House) | Empty profile, no photo, headline = title |
| cecilieperez | PASS P3 referral | WEAK, data/insights/UX pool | Consistency with lines 17, 27, 28 |
| yousef-yaghoubi-b9a25986 | PASS P2 product | PASS P3; writer note: "founder" only, no superintendent or current-role claim | Superintendent conflict with Yvonne Lim; current role Strategic Advisor at Farmeci.com |
| jay-jetley-232a0013 | PASS P2 technical-integration | PASS P3 | Matches Faulkner; PPL-3 engineering 1/90; PrivateDoc's CEO is in A2 the same day |

**Label and reason fixes, no send impact:**

| person_id | Now | Fix | Why |
|---|---|---|---|
| yousaf-ahmad-00100240, cordell-jopson-724b301a2, thestgman, dean-chittem-ceng-miet-4189b01b, caroline-salvi-8a607121, phillipisle | FAIL | WEAK, same reason | Standing decision 4 |
| karim-nassar | WEAK, "send only if the first invite is unaccepted" | WEAK with no condition, or FAIL as a duplicate once the coordinator confirms | The condition means a second invite to the same man. His current company is ChorePocket; he is NED at Simple Online |
| alexnancekievill, andrew-liles | PASS P3 / WEAK | Keep; rewrite both reasons; coordinator confirms which CTO is current | The reasoning is inverted (see B) |
| amish-patel-96b103259 | PASS P3 | Keep; replace "title and company only" with the confirming fact | Headline "Director at Infohealth Ltd." (NowPatient's operator); same URL contacted in Sept/Oct |
| gurdev-channa-ab79a244 | PASS P2 | Keep; same | Headline "Owner, Britannia Pharmacy"; only contact; same pattern as Jane Wilkins, who was sent in wave 1 |
| john-foreman-9555022ba | PASS P3 | Keep; same | Headline "Founding Director at Greenlight Healthcare Limited - an employee owned Group" |
| nikita-dhain-440013339 | PASS P3 | Keep; same | Headline names The Family Chemist; same surname as first-wave Clinical Director Sunny Dhain |
| erinchuah | PASS P3 | Keep; writer note | Her live headline reads "Head of Product Expansion @ Hims & Hers", so Juniper's no-deal line applies. `compact` dropped this headline (the gap noted in the 11-17 QC) |
| Summary lines 84, 117 | "coordinator ruling" | Quote the ruling or remove the attribution | Traceability |

**Confirmed as judged:** the six P1s (Kathryn Ganz, Mo Umar, Rosie Carr, Katy H., Aisha Suleman, Nicholas Sears), Thomas Curtis P2, all WEAKs for data, insights, CX and strategy, both Day Lewis CIOs, Brett Bowers and Sharon Hart. No WEAK must go. One optional promote: Tom Hodgson (VP International, HeliosX, former CCO of Verifymy, a verification business) as a P3 referral.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
