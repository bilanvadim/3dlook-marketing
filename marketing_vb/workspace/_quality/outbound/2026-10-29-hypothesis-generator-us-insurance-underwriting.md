---
qc_date: 2026-10-29
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-29

**Artifact:** `workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/hypothesis.md`
**Total: 17/20** — good

**Scored against:** `icp-detail.md` §3 (l.126-173), `proof-points.md`, the agent prompt, and the UK and EU twins and their QCs (16/20, 15/20). Claims were also checked against `compliance.md` §9-10, `accuracy-formulations.md` §1.4, the landing text of record, `audience.md` §5, the registry, `outbound_pack.py` CARD_SECTIONS (l.779-787), `outbound-pipeline.py` l.225 and `metrics-final.json` for 07-21 and 08-07.
**Taken as fact:** limits, signature, bans, detector, completeness.
**Limits of this QC:** there was no web tool, so external URLs were not re-fetched. There was no shell, so notify.py was not run.
**What goes to the writer:** Use case, Message angle, Rules for steps 3-5, Vadim's standing decisions and the Message 1 gate bullet. Coordinator notes (l.283) sit in an H2 that no card picks up.

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
- **What holds:**
  - One hypothesis, every template section, a `titles` block and the Message 1 gate (l.201, l.239).
  - Registry checked. The `ladder` collision is real: the global registry (l.816) assigns it to nick.
  - Dated web sources and lessons from four earlier campaigns.
  - Every ICP §3 buyer title is placed or argued out (l.85). This fixes the gap both twins' QCs marked down.
  - MetLife and the five health plans, which are ICP §3 examples, are excluded with reasons (l.17, l.55).
- **The landing was taken from the 10-21 text of record without a live check** (l.18). l.304 says both twins' hypotheses were read, yet the UK twin's l.333 records a live re-fetch on 2026-10-22. The result is a stale risk and a stale open question (see B).
- **Lemonade is not addressed.** It is an ICP §3 insurtech example (icp-detail l.171) and does not appear in the cut, the reserve list or the anti-cases.

### B. Factual accuracy — 4/5
- **What holds:**
  - Every number that can reach copy is in `proof-points.md` and uses the locked wording (l.190): 2 photos, under 45 seconds, 80+, ~3.5% with "under evaluated conditions" and "not a scale reading", 100+ clients, 112,100 scans.
  - "When enabled for the deployment" now attaches only to the 3D model, which fixes the UK QC's misquote.
  - The compliance line (l.193) and the production line (l.192) match the landing (l.165, l.175) word for word.
  - The validation population (l.93) matches `accuracy-formulations.md` §1.4.
  - The arithmetic holds: 3.5% of 80 and 100 kg is 2.8 and 3.5 kg; 0.74/29.23 is 2.5%; 6% is 1.7× the mean error.
  - The HIPAA scope argument (l.26, l.273) is correct, and it agrees with `compliance.md` §9 l.103 for insurance.
- **Stale attribution:** Risk 6 (l.264) and OQ10 (l.279) say the landing's "9 vs 27" line credits Gen Re.
  - The UK twin's hypothesis (l.333) and its QC coordinator update record a live re-fetch on 2026-10-22: the line credits LIMRA.
  - The likely cause is that the page's `TODO.md` l.42 was never ticked.
  - OQ10 asks Asel for a fix that is already done.
- **Scope claims rest on mismatched sources:**
  - Zinnia's only source (l.302) is titled as an annuities-processing release, used for a life new-business and underwriting claim (l.45, l.53).
  - The claim that Foresters' US limit reaches $2M (l.39, l.50, l.71) rests on Insurance Business's Canadian edition (`/ca/`, l.297), with no US source.
- **Minor internal numbers:**
  - "248 sent" (l.75): `metrics-final.json` shows 245 invites sent out of 248 contacts.
  - "About 1.2% of import rows" (l.75, l.249) divides by import rows, which `metrics-final.json` says not to do. l.243 nevertheless claims "Denominators as in metrics-final.json".
  - The 1.2% matches 6 replies over the three later nick campaigns that have a responses summary (492 rows). The other three imports (201 rows) are left out.
- **Sourcing:** about 30 external links, mostly primary, government or trade press (Gen Re, Munich Re, LIMRA, CDC/NCHS, USDA ERS, RAND, Cornell LII, NAIC, NY DFS, SEC, BusinessWire). There are no vendor blogs. The one aggregator (altss.com, Hexure) is flagged "to confirm" by the agent itself.

### C. Brand & tone — 3/3
- No banned words. The carded text (Use case, angle, lanes, Rules, decisions) has no corrective "X, not Y" forms, which the twins' QCs marked down, and no "so" introducing a benefit.
- Claims discipline holds:
  - It never decides, rates or replaces the exam (l.187).
  - Applicants are never suspects, and "fraud" is banned (l.188, l.10). This meets the `audience.md` §5 "Don't".
  - No accuracy figure leads or appears in Message 1 (l.189).
  - The US idiom rule bans UK and EU terms (l.185).
- Noted only, not scored, since bans are taken as fact: "by hand" (a terminology hard ban) appears at l.104, in the persona section that goes to the validate card, and at l.285 (not carded).

### D. Format & structure — 3/3
- The frontmatter is complete: product, profile, market, created, status, use_case, cap_per_group, referral_call and banned_terms.
- The path is correct.
- The `titles` block has one title per line.
- The Use case is one sentence of about 45 words.

### E. Output quality — 3/4
- **What is strong:**
  - The error-vs-gap section (l.69) and Risk 3 (l.261) state the weak point plainly, including the landing's +3.3% sample flag.
  - The falsification criteria are set by group (l.255).
  - The US-suffixed row names (l.230) carry over the EU fix.
  - The location rule keeps the twins' London and EU teams out (l.99).
  - The never-list of ownership links (l.169) is precise.
  - The lane notes are written as targets, and the five-part "What the scan is" list appears only once in the cards (l.186).
- **The pull will be noisy and the estimate does not count it** (l.104, l.107-144):
  - "New Business", "Individual Life", "Term Life" and "Disability Income" match individual and DI underwriters, case managers, new-business specialists and wholesalers. l.100 FAILs all of them.
  - The title exclusions are business-line only (Annuity, Group, P&C…) and apply only to the 11 multi-line carriers.
  - The same exclusions are not applied to the Swiss Re, Gen Re and SCOR pages. Their large US P&C underwriting staffs match every underwriting line, CUO included.
  - The "15 to 60 rows per carrier" estimate does not account for this.
- **The backstop claim at l.168 is false for four names.** It says never-list names that are not accounts "are also in `banned_terms`". Manulife, Dai-ichi, Sumitomo and Roper (l.169) are not in l.10.
- **Possible stock phrase:** "cases that never see a paramedical exam" in the carded Use case (l.61) is echoed in the underwriting lane as "cases that never see an exam" (l.156). This is the same mechanism as the UK "second source" phrase.
- **OQ10 is a stale task** (see B).

## Top 3 issues (priority for improver)

1. **Sales Navigator pull noise** (l.104, l.131-134, l.107-127):
   - The broad business-line title lines pull the individual underwriters, case managers and wholesalers that l.100 FAILs.
   - The P&C and line exclusions skip the reinsurer pages (Swiss Re, Gen Re, SCOR), whose US P&C underwriters match every underwriting line.
   - The volume estimate is understated, and step-4 validation cost goes up.
2. **Stale landing fact** (Risk 6 l.264, OQ10 l.279):
   - The "9 vs 27" label already credits LIMRA, per the live re-fetch on 2026-10-22 recorded in the UK twin's l.333 and its QC.
   - The file claims every fact was sourced on 10-29 (l.15) and that both twins were read (l.304).
3. **Backstop and source gaps:**
   - Manulife, Dai-ichi, Sumitomo and Roper are missing from `banned_terms`, against l.168's own claim.
   - Zinnia's life new-business claim rests on an annuities-processing release (l.302).
   - Foresters' US limit rests on a Canadian-edition source (l.297).
   - Lemonade (ICP §3) is not addressed.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

agreement: ✅ agree
top_issue: the Sales Navigator title block is too loose: "New Business", "Individual Life", "Term Life", "Disability Income" pull individual underwriters, case managers and wholesalers that the persona rejects, and the line-of-business exclusions skip Swiss Re / Gen Re / SCOR, so their US P&C underwriters match every underwriting title. Stale landing fact confirmed by the coordinator with a live fetch on 2026-10-29: the "9 vs 27 days" line now credits "LIMRA, automated and accelerated underwriting study", so Risk 6 and OQ10 are wrong. Fix round goes to a FRESH hypothesis-generator with every QC point (pull titles + exclusions for reinsurers, landing fact, never-list names into banned_terms, Zinnia and Foresters sources, Lemonade argued in/out, 245 invites, reply-rate wording, the "never see a paramedical exam" phrase). Verified by gate + grep, no second QC unless the cut changes.
