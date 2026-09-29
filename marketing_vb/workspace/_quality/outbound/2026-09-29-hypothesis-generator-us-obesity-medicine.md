---
qc_date: 2026-09-29
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-09-29

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/hypothesis.md`
**Total: 15/20** (good)

Scored against icp-detail.md, proof-points.md, compliance.md, accuracy-formulations.md, audience.md, the 2026-08-07 post-mortem and responses summary, and the hypothesis-generator prompt. Limits, bans, detector and completeness were taken as passed by code. notify.py was not run: this QC session has no shell.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 4/5
- The artifact covers every template section. It keeps the Message 1 gate line, has a clean `titles` block, reads the prior campaign and supports its evidence with sources.
- Post-mortem recommendation #2 (at most 15 invites per company, at least 10 companies) is never mentioned. Line 170 sets `cap_per_group: 20` so that Form Health and knownwell can each send 19, which puts 58% of invites (line 23) into two accounts. The post-mortem blamed exactly this pattern (48% into two accounts) for the last campaign's weak result. The concentration may be unavoidable, but the documented rule had to be named and a decision made on it.
- Line 113 says the campaign "applies the P3 half" of the icp-detail IT section. The same line also moves Director / Senior Director of Engineering into wave 2. icp-detail.md line 576 lists those titles as WEAK, not PASS P3, so this is an undeclared promotion.
- Lines 84 and 113 cite `nick`'s 0/60 `technical-integration` result only as grounds to drop engineers below director. Post-mortem line 107 shows 22 of those 60 were PASS-level. The same evidence therefore counts against sending lane D cold to leaders (lines 110 and 179), and the hypothesis does not say so.

### B. Factual accuracy: 3/5
- **The central premise is stated as fact without verification.** Line 24 says "a home scale that reports weight only", line 37 "a connected home scale that reports weight", line 76 "A scale reports weight" and line 177 "The home scale gives weight". Weight-only is confirmed for Form Health alone (line 48). FlyteHealth, knownwell and Enara are each described as shipping a "smart scale" (lines 50, 49, 53), and the artifact never checks whether those scales report body fat by BIA. On `nick`'s last campaign, the only evaluation question compared FitXpress with a Withings Body Pro scale. The post-mortem (H4, rec. 8) files that under "smart-scale / BIA". The hypothesis cites that reply at line 86 but still writes lanes A and B on the weight-only premise. Only the waist-circumference part of the gap is supported.
- Enara specifically: lane A (line 176) opens with "The practice already measures body composition in clinic". The cited Enara source (line 53) says only "monthly body composition tests" and "smart scale that connects to the Enara app". Nothing places those tests in a clinic.
- **Compliance, US/FDA (lines 122 and 204).** The answer to the "HIPAA? FDA?" objection pairs "FitXpress is not a medical device." with the FDA non-clearance line. compliance.md scopes the short form to the UK/EU MDR assessment (§1). Its FDA ready answer (§10) also carries "3DLOOK makes no representation as to whether clearance is required", and the hypothesis drops that clause. Given flatly to a US CMO in reply to "FDA?", the short form reads as a US device determination that the FAQ deliberately does not make. This is not a hard fail: the artifact contains no "HIPAA compliant", no "SOC 2 certified" and no FDA-cleared wording, and the BAA line is verbatim from compliance.md §9.
- Uncited numbers and claims outside copy: line 40 "Ilant Health (41, $22M+ raised)". The only funding source listed is the $15M Series A (line 278). Lines 53 and 255 say Enara's CMO is "a past president of the Obesity Medicine Association", with no source given.
- What holds: every copy number in Rules (line 203) comes from proof-points.md. "Under 45 seconds from the photos to structured results" and the §1.2 repeatability sentence are verbatim. The 2-4 weeks figure comes from icp-detail.md and is licensed by `outbound_pack.py` for lane D. The 34,000-scan proof carries no name and no geography (line 202). Client names appear only as a ban list. Market statistics and payer thresholds are kept to context (lines 74 and 203). Sourcing: about 20 external URLs from primary or trade sources, none from vendor blogs, apart from one Withings case study used as evidence about a prospect.

### C. Brand & tone: 2/3
- Line 70 (Use case, which goes into the agent cards verbatim) has "so" introducing a result: "…in under 45 seconds, so the body-composition part of the obesity record continues…". This is the terminology-guardrails §2.9 ban. The detector regex misses it because the verb is "continues".
- Line 176 (lane A, which seeds the copy) has the same construction: "…in the practice's own app, so virtual patients stay in the same record."
- Otherwise strong. The person-first language rule (line 207), the "comprehensive" and "objective" traps (line 208) and the no-replacement framing (line 205) match audience.md segment 1 "Don't".

### D. Format & structure: 3/3
- No issues. The frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `banned_terms`), the path is correct and every template section is present. The `titles` block has one title per line.

### E. Output quality: 3/4
- High value overall. The verdict table covers each company. It catches the IntelliHealth / Intellihealth homonym by matching on LinkedIn URL (line 56). Waves and reserve pools are set so Vadim decides at the checkpoint. Lanes are assigned per person, the honest-limits objections are strong (lines 118-123), and the falsification and inconclusive criteria are explicit (line 248).
- Edits are still needed before the sequencer uses it. The weight-only premise has to be qualified for FlyteHealth, knownwell and Enara before lanes A and B go into cards. The Use case "1 sentence" (line 70) runs about 95 words and is carded verbatim. It also uses "in under 45 seconds" instead of the one public definition.

## Top 3 issues (priority for improver)

1. The core thesis, "the virtual record is weight only" (lines 24, 37, 76, 176-177), is verified for one account out of four with home scales. The named "smart scales" may already report body fat, and `nick`'s own prior evaluation question (Withings Body Pro) points that way. Lanes A and B and the company-fact lines would then be wrong in message 1. Enara's "in clinic" body composition (line 176) has no support in its source.
2. US compliance: "FitXpress is not a medical device." is given as an answer to "FDA?" (lines 122 and 204), without the UK/EU MDR scope and without the FAQ's "no representation as to whether clearance is required".
3. Documented learnings are overridden without saying so: cap 20 with 58% in two accounts, against the post-mortem's "≤15 per company" (line 170); Director of Engineering moved from WEAK to P3 (line 113); lane D sent cold although the 0/60 result included 22 PASS-level engineers.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the "virtual record is weight only" premise was checked for one account of four; sent back to hypothesis-generator with all six QC items before the list was stamped.
```
