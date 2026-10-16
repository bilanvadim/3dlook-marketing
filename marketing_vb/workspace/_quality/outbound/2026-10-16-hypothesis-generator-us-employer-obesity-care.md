---
qc_date: 2026-10-16
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-16

**Artifact:** `workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/hypothesis.md`
**Total: 15/20** — good (one point above marginal; the fix list below should run before message-sequencer)

**What I scored against:**
- `icp-detail.md` §1, §4, the universal exclusions (l.558-565) and the IT roles section (l.569-604)
- `proof-points.md`, `accuracy-formulations.md` §1.1-1.2, `compliance.md` l.101
- `audience.md` §1
- the agent prompt
- `outbound_pack.py` CARD_SECTIONS (l.745-753)
- the 10-02 and 10-11 hypothesis QCs
- Vadim's 2026-10-16 instructions (use the whole list, cap 100, Apollo top-up allowed)

**What reaches the message writer:** Use case, Message angle, Outreach language, Rules and both decisions sections. The account table and the persona go only to the validator.

**Taken as fact:** limits, signature, bans, the detector and completeness.

**Limits of this QC:**
- No web tool, so I did not re-fetch the external sources.
- No shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **What holds:**
  - One hypothesis, every template section, the `titles` block and the Message 1 gate (l.252, l.293).
  - Sourced evidence (l.102-105) and lessons from earlier campaigns (l.109-112).
  - Five open questions, each with a default.
  - cap 100 and Apollo top-up match Vadim's instructions.
- **l.334 ("Vadim's decisions 2026-10-16", item 2, goes verbatim into both cards) puts the agent's reading under Vadim's name.** Vadim did not say "engineering and security" lanes or "Crossover is held … not forced". The 10-11 QC flagged the same pattern.
- **l.144 credits IT and infrastructure roles to Vadim's 2026-10-16 instruction.** The real basis is standing decision 3 (l.342), which overrides `icp-detail.md` l.582-584 (IT support and InfoSec are FAIL there).
- **The prompt's "target, not sentence" rule (prompt l.112-116) is broken at l.257.** The line hands writers a quoted phrase: "the program compares scans it selects". The 10-11 QC flagged the near-identical "members compare scans they choose".

### B. Factual accuracy — 3/5
- **Reply history contradicts itself:**
  - l.27 and l.304 say all four Sept/Oct campaigns have "one reply each".
  - l.109 says `2026-10-01-us-options-medical-weight-loss` "has none on file".
  - The metrics basis (l.304) rests on the wrong version.
- **The central pattern (l.24, l.103) overstates "weight the member enters":**
  - "Digbi's app sync" is smart-scale sync through phone health apps (the artifact's own l.88).
  - "MDLIVE's reported results" is a marketing phrase, "patients who reported weight loss" (l.90). It does not establish how weight is captured, and l.90 itself says the parent's program includes connected scales.
  - That leaves eMed as the only verified self-logged-weight account, yet the mismatch-flag angle rests on eMed, Digbi and Wondr (l.310, l.328).
- **The Omada row contradicts its own source.** l.84 cites that healthy-BMI members "can enter weights manually", then rules "members weigh on the Omada scale" (same row, l.198, l.256). The rule is conservative, but the stated reason is wrong.
- **Copy-facing claims are clean:**
  - Rules numbers (l.255) come from `proof-points.md`. The exception is 2-4 weeks from `icp-detail.md` l.597, which earlier QCs licensed.
  - The US compliance line (l.253) is verbatim from `compliance.md` l.101, and the SOC 2 and FDA sentences (l.155) are verbatim.
  - Smart Scales is labelled beta, traced to `how-it-works.md` l.19 and `tech-spec.md` l.12.
  - No client names. The 34,000, 112,100 and 100+ lines use the locked wording.
- **Arithmetic checks out:**
  - 302 + 5 + 42 + 3 + 24 = 376 reconciles per group.
  - Lanes 167/46/36/32/26 = 307.
  - Tiers 30/74/36/167 = 307, and P4 per account sums to 167.
- **Sourcing:** about 60 external links, mostly primary (help centers, App Store IDs, company releases, Lancet, PLOS, MedCity, Axios). There are no vendor blogs except the competitor page, which is used as evidence. I could not verify them without web access (Omada's "1M+ members", the BGH 67%/10%, the Firefly and Premise dates).

### C. Brand & tone — 2/3
- **The cards steer writers toward eligibility, which `audience.md` §1 forbids ("implying eligibility decisioning"):**
  - Use case l.98: "at the check-ins its employer rules require … a flag when it disagrees".
  - l.194: "coverage reviews".
  - Question topics: l.237 "how operations runs eligibility at scale", l.238 "how GLP-1 utilization reviews are documented", l.239 "how the continuation checkpoint is documented".
  - The disclaimers (l.257, l.259) are present, but the targets point at the decision itself.
- **Hard-ban forms in carded text:**
  - l.268 "so a leak fails the gate" uses "so" to introduce a result.
  - Corrective negation at l.268 ("targets, not copy") and l.334 ("not forced").
  - l.225 uses "plus" as a connector.
- The Use case's first sentence runs about 80 words and goes verbatim to writers told "short sentences".
- **What holds:** person-first language (l.265), no banned words outside the ban lists, and claims discipline written into the Rules (l.256-260).

### D. Format & structure — 3/3
- The frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `referral_call`, `banned_terms`), the path is correct and the `titles` block has one title per line.
- Minor: "Use case (1 sentence)" holds two sentences (l.98).

### E. Output quality — 3/4
- **Strong:**
  - A row-level verdict for all 376 people, with identity collisions argued.
  - Aliases regrouped to canonical names, so the registry never records Doctor On Demand, Naturally Slim or Forbes Business Council.
  - A per-account table of what each company has, what is not verified and what to offer.
  - A displacement search, honest limits (l.105), metrics sized on Nick's history and a frank risk list (the Mass.gov Vida item).
- **The mismatch flag is an instruction writers cannot follow:**
  - The eMed, Digbi and Wondr offers lead with a weight cross-check against logged weight (l.86-88).
  - The Rules forbid implying logged weights are wrong or that members misreport (l.200, l.256).
  - At a continuation checkpoint with a weight-loss rule, the only reading a buyer takes is "verify weight for coverage", which l.259 forbids.
  - OQ4 (l.328) asks about beta status, not this conflict.
- **The referral lane is 167 of 307 (54%), and its targets do not cover it:**
  - l.212 gives question targets only for commercial and client, finance and strategy, and advisors.
  - Creative and production, customer service and experience, and unclear "VP"/"Director" roles (l.132) get none.
  - Under the artifact's own rule that a topic repeats for at most about a fifth of a company (l.233), the topic lists are too short: eMed 4 topics for 34 people, Vida 4 for 38, MDLIVE 4 for 33, Wondr 4 for 23, Digbi 3 for 7, Goodpath 2 for 9.
  - Included Health (96 people) has one facts bullet (l.222).
- **Coined phrases repeat in carded sections and will be copied:**
  - "structured, timestamped record" (l.98, 194, 210)
  - "no device to ship" / "nothing to ship" (l.98, 208, 210, 264)
  - "the body-measurement part of a check-up" (l.98, 195; this is Included Health's entire angle across 96 people)
  - "scans it selects" (l.209, 257)
  - This is the mechanism behind the 10-07 and 10-11 failures.
- **The merger exclusion is applied unevenly:**
  - Included Health acquired Firefly (agreement 2026-07-28) and launched new health plans on 2026-10-01, yet it defaults IN with 96 people (31% of the send).
  - OQ2 (l.326) justifies this by quoting only half of the exclusion reason. It cites "ICP shifting" and drops "sales cycle stalls" (`icp-detail.md` l.564).
  - Crossover (merger closed 2026-03-12) is held, but OQ1 (l.325) recommends releasing it too. That would put 138 of 349 people at merger-touched accounts.
- **Smaller gaps:**
  - l.161 caps Included Health Apollo additions "at its cap (4)", while l.50 says Included Health gets no top-up.
  - The `titles` block (l.163-185) pulls engineering titles for paid enrichment while l.144 cites 0 replies from 60 technical invites. Goodpath and eMed already have CTOs in the export.
  - The block also lists member-experience, outcomes and implementation titles, which the verdict table's top-up column never asks for.

## Top 3 issues (priority for improver)

1. **The weight cross-check angle for eMed, Digbi and Wondr cannot be written cleanly.**
   - It sells a flag on logged weight while banning any implication of misreporting (l.86-88 vs l.200, l.256).
   - The carded targets pair it with eligibility, continuation and utilization checkpoints (l.98, l.194, l.237-239), against `audience.md` §1 and l.259.
   - The evidence that these accounts rely on member-entered weight is overstated for Digbi and MDLIVE (l.24, l.103 vs l.88, l.90).
2. **The referral lane (167 people) lacks question targets for three listed sub-roles (l.132, l.212), and the per-account topic lists fall short of the artifact's own repeat rule (l.233-241).**
   - Coined phrases repeat in carded sections ("structured, timestamped record", "nothing to ship", "body-measurement part of a check-up").
   - l.257 hands writers a quoted copy phrase. The 10-11 QC flagged both mechanisms.
3. **The merger exclusion and the decisions section are applied unevenly.**
   - Included Health (an acquirer, 96 people) defaults IN on a half-quoted exclusion reason (l.326), while OQ1 recommends releasing Crossover too.
   - l.334 records the agent's interpretation as Vadim's decision in a carded section.
   - The reply-history contradiction (l.27, l.304 vs l.109) skews the metrics basis.

## Coordinator review

agreement: ✅ agree
top_issue: the Smart Scales weight-check angle (eMed, Digbi, Wondr) contradicts the hypothesis's own "never imply members misreport" rule and ties the scan to eligibility/coverage checkpoints; checked against l.86-88, l.196-202, l.254-260. Also confirmed: "Vadim's decisions" item 2 holds the coordinator's own reading of «максимально використай весь список» (my prompt wording), not Vadim's words. All three top issues and the smaller items went to a fresh hypothesis-generator fix round (author was at ~380K tokens) before Vadim's checkpoint.
