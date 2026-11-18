---
qc_date: 2026-11-18
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-18-uk-london-glp1-connections-2/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 17/20
status: good
coordinator_review: pending
---

# QC Report — icp-validator — 2026-11-18 — A2 (uk-london-glp1-connections-2)

**Artifact:** `workspace/outbound/campaigns/2026-11-18-uk-london-glp1-connections-2/icp-validation-summary.md`, `.../decisions.md`
**Total: 17/20** — good

Six connections, all PASS (P2 4, P3 2). Scored against `card-validate.md`, `people-compact.csv`, `already-sent.md` and the relayed rulings. Under standing decision 3, every connection at an IN company gets a lane in A, so six out of six PASS is correct in principle. The questions are priority and redundancy.

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
- Rizwan Ali (`decisions.md` line 4) is given an `operations` lane "the first wave did not cover" and kept at P2. A Deputy MD sits in the MD's lane, and the first wave covered that lane with Nigel Swift (B). Second-wave decision 2 says a covered lane lowers priority, so P3.
- Done right: every company gets lane reasoning against `already-sent.md`. Both people re-judged on new titles are named, with the old verdict (Deniz FAIL on 11-17, Rizwan dropped after the 11-17 QC). PPL-1 held (no P1). The empty WEAK and pool sections are correct.

### B. Factual accuracy — 4/5
- Ryan Nolan (line 6): "runs the markets outside Australia including the UK GLP-1 programme" is inferred from the headline "VP International @ Euc". Nothing in the data says he runs Juniper UK, and Juniper UK's MD (Alice Pan) was already written to. If this lands in copy, it misattributes a role.
- Verified correct:
  - Paul Marshall's identity quote ("CEO PrivateDoc, Co-Founder and Board member kwiboo") and Camran Khan's role at iQ Doctor (profile summary).
  - Abbas K.'s mapping and the Quincy risk.
  - First-wave lanes per company.
  - Deniz in London (her first-wave connection record).

### C. Brand & tone — 3/3
- No issues.

### D. Format & structure — 3/3
- The frontmatter is complete and all sections are present.
- Minor: `status: final_no_checkpoint` is not a template value, and B2 uses `awaiting_review` for the same situation. Align them.

### E. Output quality — 3/4
- Deniz Ekmekci (line 7) is a P3 referral whose referral target is Ryan Nolan, who gets his own message the same day. That makes the route-in redundant. With B2's Erin Chuah and Catherine Bell, Juniper reaches 10 people from Katerina across both waves. The summary asks writers to differentiate the two messages, but that does not fix the redundancy.
- Otherwise ready: the right owner lanes at PrivateDoc, iQ Doctor and Chemist Click, and a correct currency risk on Abbas.

## Cross-campaign consistency (A2 vs B2)

See the B2 report: the combined Juniper load (10), PrivateDoc getting two P2s on the same day, the covered-lane priority applied differently (B2 drops to P3, A2 relabels the lane), owner angle `leadership` (A2) vs `compliance` (B2), and the different status values.

## Top 3 issues (priority for improver)

1. Deniz Ekmekci is a referral to someone already written to directly; Juniper reaches 10 people across waves.
2. Rizwan Ali's lane is relabelled to dodge the covered-lane rule; he should be P3.
3. Ryan Nolan's UK remit is an inference stated as fact, and it could leak into copy.

## Per-person fix list (SEND 6 → 5)

| person_id | Now | Fix | Why |
|---|---|---|---|
| paulcmarshall | PASS P2 leadership | Keep | New CEO lane; identity confirmed by profile summary |
| camrankhan | PASS P2 technical-integration | Keep | First wave reached the CEO only |
| abbas-k-6506431b0 | PASS P2 leadership | Keep | Coordinator mapping; never name Quincy |
| rizwan-ali-85342856 | PASS P2 operations | PASS P3 leadership | Same lane as first-wave MD Nigel Swift. Copy carries no retail framing (the 11-17 drop reason) |
| rnolan94 | PASS P3 leadership | Keep; rewrite the reason without the UK-programme claim | Inferred remit |
| deniz-ekmekci-6876917a | PASS P3 referral | WEAK | Her referral target gets a direct message the same day; Juniper at 10 |

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
