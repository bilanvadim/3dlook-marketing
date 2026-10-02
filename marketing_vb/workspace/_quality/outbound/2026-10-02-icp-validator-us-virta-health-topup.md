---
qc_date: 2026-10-02
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-02-us-virta-health/icp-validation-summary.md (section "Apollo top-up (2026-10-02)") + decisions.md (rows 40-69)
track: outbound
artifact_type: icp-validation
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-02 (Apollo top-up, round 2)

**Artifact:** `workspace/outbound/campaigns/2026-10-02-us-virta-health/icp-validation-summary.md` (lines 132-176), `decisions.md` (lines 40-69)
**Scored against:** `card-validate.md` and `people-compact.csv` (68 rows). Code had already checked completeness, identity and the counts (68 decisions; 50 PASS, 14 WEAK, 4 FAIL; SEND 50 = cap), so they were not rechecked. The raw Apollo file `sales-nav-raw/apollo-2026-10-02.csv` was read only to confirm doubts that the compact rows already raise.
**Total: 15/20** (good)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- The loop was followed. Every one of the 30 rows has a decision and `wave` is 1 on all of them. Over-cap people are WEAK with "Over the cap (50)". FAIL is used only for the categories the card allows (card line 132): Jamie Anderson has left, Wael Asano is a duplicate, Lola Morris is an identity collision.
- The cap cut ignores the card's P4 order. Card line 71 says "Order inside P4: commercial leaders first". The card's commercial group (line 72) explicitly includes client success and partnerships roles. Despite that, three commercial leaders were put over the cap:
  - Kristen Weeks, Head of Customer Success and Partnerships (decisions line 53)
  - Lindsay Johnson, Head of Partnerships With Unions, Labor and Trusts (line 54)
  - Keenan Jarvis (line 55)

  Meanwhile two chiefs of staff and a VP Marketing kept seats (lines 48, 49, 52), and the card does not rank those roles at all. The agent's own proposed order (summary line 170: "commercial, executive office and marketing, sales…") contradicts the cut it made.

### B. Factual accuracy — 3/5
- No proof-point numbers, client names or product claims appear. The arithmetic checks out (37+13=50; 58 = 50+8; 64 = 50+14; 18 not sent = 14 WEAK + 4 FAIL across 7 pools).
- **Lisa Chen is PASS (decisions line 51) on an identity the agent itself treated as unconfirmed for Wael Asfour.** Three compact rows carry the same title, "Head of Commercial Innovation" (compact lines 66-68). For Asfour, the agent says sharing that title with Lisa Chen leaves "the current role unconfirmed" (summary line 163). The same fact applies to Lisa Chen, and the doubt was applied to one side only. Her headline also names no Virta role ("Graduated from the Sauder School… limited partner"). Michael Ahlberg was made WEAK on exactly that ground (line 61). The raw Apollo rows confirm the doubt: Chen (raw line 30) and Asfour (raw line 28) list the same three earlier roles in the same order: Industry Marketing Lead - Education at Google, Manager at Accenture, Sales Associate at St. Jude Medical. One of the two profiles copies the other.
- **Meredith Loring is PASS (decisions line 49) although her row shows her title as an earlier role.** Compact line 64 has title "VP, Chief of Staff" and earlier_roles "VP, Chief of Staff at Virta Health". This is the same pattern the agent used to FAIL Jamie Anderson: "the Virta GC role sits among earlier roles" (summary line 152). Her headline is also stale ("…100 million people by 2025!"). In the raw row (line 26), the current role is "Advisor at Virta Health". She is still at Virta, so this is not a FAIL. But her current role is unconfirmed, which makes her WEAK by the agent's own Wael Asfour standard.
- Decisions line 41 (Amit Shah) states "senior owner of operations across care delivery, enrollment and implementation". His compact row (line 41) shows only "President" and a Colorado council seat, so the remit is an inference written as fact. This reason column feeds the hooks, which for Apollo rows come from "title plus a Virta fact" (card line 148).
- Minor: summary line 154 says Lola Morris has "no Virta role", but her row's title is CEO at Virta. What the agent means is that no Virta role appears in her history.

### C. Brand & tone — 3/3
- No issues. This is an internal report with no banned words and no em dashes in the round-2 section. The questions block (lines 173-176) is entirely in Ukrainian, so the language switch flagged in round 1 does not recur.

### D. Format & structure — 2/3
- The frontmatter is stale. Line 7 reads `hypothesis ef8c85316ae24aa3`, but the card the agent read is `8d5710479b811dba` (card line 3; `.hypothesis-lock.json` scope_hash). Nothing in the frontmatter marks round 2.
- The file opens with round-1 figures: Stats say "To send 37" and "WEAK 0", and the confirm block asks about 37 people. Only a sentence at line 134 says these describe round 1. The combined 50/14/4 figures first appear at line 136.
- Minor: the FAIL reason in decisions line 67 is 6 words, over the 2-5 the prompt allows.

### E. Output quality — 3/4
- Correct and well argued:
  - Jamie Anderson FAIL: Midi Health is in the headline, and the Virta GC role is listed as an earlier one.
  - Wael Asano FAIL as a duplicate (same id suffix, empty profile), and keeping Asfour is reasoned.
  - Lola Morris FAIL as a collision with Sami Inkinen.
  - Michael Ahlberg WEAK rather than FAIL.
  - Four junior title-token rows WEAK.
  - Jennifer Arensdorf is `operations`, not `clinical`, reasoned from her talent-development background.
  - Neha Shevade and Christine Vonderach are P3 `technical-integration`.
  - Concerns name the missing clinical/research head and the P4 import order.
- The six over-cap reasons are circular: "ranked below the six new P4s kept" (decisions lines 53-60) gives no rule. With no checkpoint before import, this cut is the final one, and nobody can tell from the file why Ryann Donohue beats Kristen Weeks.
- New peer clusters are not flagged for message-sequencer:
  - Laura Walmsley, Kristen Larson and Leana Balasco are all ex-Personify Health, and Walmsley and Larson are both ex-Virgin Pulse (compact lines 42, 8, 2).
  - Amit Shah and his chief of staff Shravya Gupta are both on SEND.
  - Neha Shevade and the two Directors of Engineering she likely manages are both on SEND.
  - Colin Daw and Holly Anderson both sit on enrollment.

## Top 3 issues (priority for improver)

1. **The last cap seats were chosen with no stated rule and against card line 71.** Two of the six P4 seats went to unconfirmed profiles: Lisa Chen (identity) and Meredith Loring (current role). Clean commercial leaders were left over the cap: Kristen Weeks and Lindsay Johnson. Recommended swap, cap unchanged at 50: Lisa Chen and Meredith Loring to WEAK, Kristen Weeks and Lindsay Johnson to PASS P4 `referral`.
2. **Identity doubts were applied unevenly.** The "shares the title" doubt was used on Wael Asfour but not on Lisa Chen. The "title among earlier roles" test was used on Jamie Anderson but not on Meredith Loring. The headline-without-Virta test was used on Ahlberg but not on Chen.
3. **Housekeeping:** the stale hypothesis hash in the frontmatter, round-1 totals at the top of the file, unflagged peer clusters (the Personify trio, President plus chief of staff), and an inferred remit written as fact in Amit Shah's reason.

**Note for the coordinator:** `hypothesis.md` line 365 ("run without checkpoints", default 1) copies the agent's over-cap list word for word. If the swap is applied, that line and `people-validated.csv` must change together.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: two of the last cap seats went to profiles with an unconfirmed current Virta role; the swap (Lisa Chen, Meredith Loring → WEAK; Kristen Weeks, Lindsay Johnson → PASS) is sent back to the validator and to hypothesis-generator for the people table and the no-checkpoint defaults block.
```
