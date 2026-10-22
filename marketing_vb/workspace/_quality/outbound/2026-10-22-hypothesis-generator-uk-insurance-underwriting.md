---
qc_date: 2026-10-22
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: pending
---

# QC Report — hypothesis-generator — 2026-10-22

**Artifact:** `workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/hypothesis.md`
**Total: 16/20** — good

**Scored against:**
- `icp-detail.md` §3 (l.126-173) and the universal exclusions (l.558-565)
- `proof-points.md`, `accuracy-formulations.md` §1.4, `compliance.md` §9 (l.102), `tech-spec.md` l.12-13
- `audience.md` §5, `about-me.md` claims discipline
- the agent prompt and `outbound_pack.py` CARD_SECTIONS (l.745-753)
- the live landing text `workspace/pages/for-insurance-underwriting/published-live-2026-10-21.md`
- the 10-16 hypothesis QC, for calibration

**What reaches the message writer:** the Use case, Message angle (including Account facts and Content asset), Rules and both decisions sections. The persona and objections go only to the validator.

**Taken as fact:** limits, signature, bans, the detector and completeness.

**Limits of this QC:**
- No web tool, so the external sources were not re-fetched.
- No shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **What holds:**
  - One hypothesis covering every template section.
  - The `titles` block (l.92-119) and the Message 1 gate (l.170, l.211).
  - Sourced evidence, a registry check and lessons from earlier campaigns (l.63-68).
  - Six open questions, each with a default.
  - Dropping the CRO and CIO is argued (l.74).
- **Some ICP §3 buyer titles are dropped without a reason.** "Head of Digital Innovation / Digital Transformation Leader", "Product / Innovation Manager" and "Insurtech Strategy Team" (`icp-detail.md` l.134-136) do not appear in the titles block (l.92-119) or the tiers (l.84). l.74 gives reasons only for the CRO, CIO and distribution titles. The ICP's first trigger, "Digital transformation", points at exactly these people (l.160).
- **The 30-company target is out of reach of the named universe.**
  - The prompt asks for a list where 30 companies is a realistic goal.
  - The artifact names 18 insurers (l.37) but sets a target of 16-19, along with 7 reinsurers and 3 platforms, which is 28 at most.
  - It still says "about 30 in all" (l.35) and "target 30" (l.204).
  - Lowering the floor to 25 is argued (l.44). The headline target is not corrected to match.

### B. Factual accuracy — 4/5
- **Copy-facing claims are clean:**
  - Every number in the Rules (l.159) traces to `proof-points.md`.
  - The 3.5% figure comes with "under evaluated conditions" and "not a scale reading" (landing l.110). It is held to Message 2 in three lanes.
  - The validation population (l.81) matches `accuracy-formulations.md` §1.4.
  - The GDPR line (l.162) matches `compliance.md` l.102 word for word. The boundary sentence and the production line (l.161-162) match landing l.165 and l.175 word for word.
  - Smart Scales without "(beta)" follows `tech-spec.md` l.13.
  - No client is named. The 100+ and 112,100 lines use the locked wording.
- **Internal facts check out against the files:**
  - The July baseline (258 / 69 / 26.7% / 13 / 18.8%) matches `metrics-final.json`.
  - "12 of 13 to Message 1" matches `post-mortem.md` l.132.
  - The AIA replies match the 08-14 `responses-summary.md`.
  - No insurer, reinsurer or platform slug appears in any registry.
- **UnderwriteMe's product is named two ways.** l.41 and l.46 call it the "Protection Platform". The carded Rules at l.165 call it the "Decision Platform" and license writers to name it to UnderwriteMe.
- **One quote is stretched.** "When enabled for the deployment" (l.159) is applied to 80+ body measurements as well. The landing applies it only to body composition estimates and the 3D model (l.76). 80+ measurements is listed there without that condition (l.78-82). The rule is conservative but misquotes the source.
- **The success-metric denominators assume 30 companies** ("8 of 30", l.223). The named universe tops out at 28.
- **Sourcing:**
  - About 45 external links, mostly primary or trade press: FOS decision PDFs, BMJ Open, NHS Digital, the FCA market study, Healthcare & Protection, Cover, IFA Magazine, Hannover Re and Munich Re pages.
  - No vendor blogs.
  - The undated Hannover Re page and the 2016 Iress item are labelled as such.
  - None of it is used in copy (l.58, l.159).

### C. Brand & tone — 2/3
- **What holds:**
  - No banned words outside the ban list.
  - The Rules enforce `about-me.md` claims discipline: no decisions, no replacement of GP reports or nurse screenings, never covert (l.156).
  - The Rules enforce `audience.md` §5 "Don't": "fraud" is banned and applicants are never treated as suspects (l.157).
  - The Rules hold UK idiom and ban US terms (l.154).
- **Hard-ban forms appear in carded text:**
  - The Rules contain the corrective "X, not Y" form "Defensibility, not accuracy." (l.158), in the section that goes to the sequencer word for word.
  - The decisions sections, which go to both cards, contain "company-named profiles are held, not failed" (l.191) and the heading "built in, not open questions" (l.186).
  - l.200 has "so one insurer's Message 2s…".
- **The Use case (l.53) is a single sentence of about 78 words.** It goes word for word to writers whose Rules ask for "formal, short, specific" (l.150).

### D. Format & structure — 3/3
- The frontmatter is complete (`product`, `profile`, `market`, `created`, `status`, `use_case`, `cap_per_group`, `banned_terms`).
- The path is correct, and the `use_case` file exists.
- The `titles` block has one title per line.
- The Use case is one sentence.

### E. Output quality — 3/4
- **Strong:**
  - An accurate map of the UK point-of-sale chain: insurers, London life reinsurers and adviser platforms. The reasons for a wider or narrower cut are argued (l.43-47).
  - Precise anti-cases: group risk, PMI, over-50s, annuities, closed books, the Chesnara acquisition.
  - Honest limits: height is not checked, hosting is in the US, there is no insurer reference, and there is a disability limitation (l.59, l.231-237).
  - Prospects are never named in each other's copy (l.165).
  - Falsification criteria are set (l.227).
  - Account facts are deferred to a fresh round after step 2.
- **The landing link is allowed in every lane, `reinsurance` included (l.146, l.152), even though the page names reinsurer prospects.**
  - Landing l.29-32 cites Gen Re and Munich Re.
  - Landing l.32 credits a 2020 LIMRA figure to "Gen Re, Next Gen Underwriting Survey".
  - The artifact found this itself (OQ6, l.246) but marks it "not blocking" and does not ask whether to withhold the link.
  - The result: Gen Re UK and Munich Re UK underwriters, and every insurer, get a page that names those reinsurers. Gen Re UK gets a statistic misattributed to its own survey. This goes against the artifact's own rule at l.165.
- **The core evidence works against the product's stated error, and nothing addresses it.**
  - l.58 rests the case on an average understatement of 1.5-2.1 kg.
  - Smart Scales' about 3.5% MAE is about 2.5-3 kg at typical adult weights, larger than that average gap.
  - The objection answer (l.77) and the lane targets (l.130-131) say nothing about which size of gap the flag can separate from estimate error.
  - Chief underwriters and medical officers are the P1 audience, and they will raise this first.
- **Coined phrases sit in carded sections and will be copied:**
  - "Second source of build evidence" appears in l.127, l.155 and l.157, and is also the landing's H2 (l.25).
  - The five-part list (two photos, weight estimate, BMI from declared height, flag, timestamped record) appears in l.127 and l.155, with the instruction "Name these parts".
  - At Aviva- and L&G-sized pools this collides with the artifact's own no-repeat rules (l.138, l.164) and the 600-character limit. It is the mechanism behind the 10-07 and 10-11 failures cited at l.68.

## Top 3 issues (priority for improver)

1. **The landing link is allowed in the `reinsurance` lane and to insurers (l.146, l.152, l.200), though the page names Gen Re and Munich Re and misattributes a LIMRA figure to Gen Re (landing l.29-32).** This breaks the artifact's own cross-naming rule (l.165). OQ6 (l.246) flags the mislabel but asks no question about withholding the link.
2. **The evidence's average weight understatement (l.58: 1.5-2.1 kg) is smaller than the estimate's stated error (about 3.5% MAE).** Neither the objections (l.77) nor the lane targets (l.130-131) say which size of gap the flag can separate from estimate error. That is the first question P1 chief underwriters and CMOs will ask.
3. **Carded copy-steering and coverage gaps:**
   - The phrase "second source of build evidence" and the five-part list are repeated in carded Rules and Message angle (l.127, l.155, l.157), against the artifact's own no-repeat rules.
   - ICP §3 innovation and digital-transformation titles are missing from the pull without a stated reason.
   - The universe tops out at 28 while the target and metric denominators say 30 (l.35, l.37, l.204, l.223).
   - UnderwriteMe's product is named two ways (l.46 vs l.165).

## Coordinator review

agreement: ✅ agree
top_issue: issue 1 checked against the live text: landing l.29-32 cites Gen Re and Munich Re, and l.32 labels a 2020 LIMRA link as "Gen Re, Next Gen Underwriting Survey". Citing a reinsurer's public research is not the same as naming a prospect in another prospect's copy, but sending the misattribution to Gen Re UK is a real defect. Vadim allowed the landing link in Message 2 on 2026-10-22 without this fact, so the lane scope of the link goes back to him (default: link for insurers and platforms, none in the reinsurance lane until Asel relabels l.32). Issues 2-3 go to a fresh hypothesis-generator fix round before his checkpoint.

update 2026-10-22 ~12:35 UTC: live landing re-fetched (curl). l.32 now reads "LIMRA, automated and accelerated underwriting study" with the LIMRA link, so issue 1 is resolved on the page. Vadim's decision stands for every lane, reinsurance included. The remaining landing note is the US idiom (carrier ×7, paramedical ×4, face amount ×2).
