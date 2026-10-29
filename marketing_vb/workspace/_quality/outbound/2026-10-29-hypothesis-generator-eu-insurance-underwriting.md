---
qc_date: 2026-10-29
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-29

**Artifact:** `workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/hypothesis.md`
**Total: 15/20** — good

**Scored against:** `icp-detail.md` §3 (l.126-173) and universal exclusions (l.558-565), `proof-points.md`, the agent prompt, the UK twin and its QC (16/20), `compliance.md`, the landing text of record, `outbound-registry.py`, `outbound_pack.py` (card code), `outbound-pipeline.py` PROFILE_GEO.
**Taken as fact:** limits, signature, bans, detector, completeness.
**Limits:** no web tool, so external URLs were not re-fetched. No shell, so notify.py was not run.
**Hard-rule note:** the rule "a number not in proof-points caps B at 2" was applied to copy-facing numbers (Rules l.191). All of them trace to `proof-points.md`. Market figures are sourced research, which the prompt requires, and the Rules keep them out of copy.

**The caller's four checks:**
- **Market facts sourced per country.** Germany and the Netherlands: yes. Ireland: partly, because its point-of-sale mechanism rests on a UK analogy. No UK figure is reused.
- **Country cut justified.** Yes for IE, DE and NL, and for leaving out France. Belgium is honestly deferred. The Nordics, CH and AT are cut without a source.
- **Registry and UK-overlap rules workable.** The person-level and location rules work. The waiver wording is imprecise. Naming rows after parent companies creates a cross-profile slug problem for Nick.
- **Rules and lane notes leaking into copy.** The persona and objection answers stay out of the messages card (`outbound_pack.py` l.785-786), and the lane notes are written as targets. One angle phrase, two corrective forms and two coordinator notes are still carded.

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
  - One hypothesis covering every template section, with the `titles` block and the Message 1 gate (l.205, l.239).
  - Registry check done (l.20) and dated web research (l.285-296).
  - Lessons from four earlier campaigns, checked against the files:
    - The July baseline (292 / 73 / 25.0% / 4 / 5.5%) matches `metrics-final.json`.
    - The Erakulis forward request and the 10-07 "inconsistency" decline match their `responses-summary.md`.
    - English only matches the 09-14 decision (erakulis hypothesis l.275).
- **The UK QC findings are fixed:**
  - The gap-vs-error question is answered (l.71, l.91).
  - The compliance line is aligned with `message-sequencer.md` l.119-120 ("ровно одна").
  - The universe and the target now agree: 32 named, 26-30 IN.
- **ICP §3 titles dropped without a reason:**
  - "Insurtech Strategy Team", "Population Health Director" and "Compliance & Fraud Prevention Team" (icp-detail l.136-139) are dropped.
  - l.88 argues out only the CRO, CIO and distribution heads.
  - The UK twin argued out population health and compliance. That reasoning was not carried over, and `Insurtech` left the pull without a word.
- **One number has no source link**, against the prompt's "Каждое число — со ссылкой":
  - Volkswohl Bund, "BU new business up 60% in 2025" (l.42).
  - No source for it appears in l.285-296.

### B. Factual accuracy — 3/5
- **What holds:**
  - Every copy-facing number (l.191) is in `proof-points.md`.
  - The compliance lines match `compliance.md` l.102 and landing l.165, and the production line matches landing l.175.
  - The 3.5% figure always carries its qualifiers.
  - No UK market figure is reused (no HSE, BMJ Open, FOS or Swiss Re THW numbers), so l.15 holds.
  - DE and NL rest on local primary or trade sources: the Die Bayerische guide, LV 1871, RKI, the Verbond declaration, NN, MoneyView, vers.diagnose and Alte Leipziger.
- **Ireland's mechanism is borrowed from the UK by analogy:**
  - l.23 says applications "in these three markets" are decided at the point of sale, and l.53 says "Ireland is the UK model in the EU".
  - The Irish sources (CCPC, BPFI, the Laya form) show that cover is required and that height and weight are declared. They do not show point-of-sale decisions without evidence.
  - No Irish source covers instant decisions, non-medical limits or the broker channel.
- **l.53 overreaches:** "46,358 mortgages were drawn down in 2025 (BPFI), each with an underwritten life application".
  - BPFI drawdowns include switchers and top-ups.
  - The CCPC quote on the same line states the age and health exemption.
- **The Irish height-and-weight evidence sits on hosts that look like staging:** `integration01.layalifeinsurance.ie` and `integration03.layahealthcare.ie` (l.287).
- **The RKI link has an unusual form:** `https://www.rki.de/obesity` (l.290). Both links need a canonical URL before anyone relies on them.
- **Unsourced company descriptors are handed to step 2:**
  - Scildon's 2025 Lifestyle Hypotheek ORV and Allianz NL as the carrier behind Dazure (l.44).
  - LV 1871 "Quick Risk" (l.42).
  - Munich Re as co-developer of vers.diagnose (l.46, l.56).
- **Two German in-force counts are not reconciled** (l.54): 14.3M BU policies (M&M) against 5.63M standalone plus 11.11M riders (F&B).
- **The metrics contradict their own premise:** l.243 says "targets sit below her July baseline", but l.249 sets 8% replies per accepted against a 5.5% baseline.
- **Sourcing:** about 40 external links, mostly primary or local trade press, and no vendor blogs. The AI Act date is flagged by the agent itself for a check against EUR-Lex (l.295).

### C. Brand & tone — 2/3
- **What holds:**
  - No banned words and no dashes.
  - Claims discipline matches `about-me.md` and the `audience.md` §5 "Don't": no decisioning, applicants never suspects, "fraud" banned (l.10, l.188-189).
- **Corrective "X, not Y" forms in carded text:**
  - l.187 "(a target, not wording)" in Rules.
  - l.239 "Kept as a failure, not a note", in the gate bullet that `outbound_pack.py` l.918-922 copies into the messages card.
  - The UK QC marked down the same kind of lapse.
- **Coordinator notes sit in carded Rules:** l.197 "(Replaces the UK card's "at most one"…)" and l.202, the Dora waiver instruction. The sequencer receives both word for word.

### D. Format & structure — 3/3
- The frontmatter is complete: product, profile, market, created, status, use_case, cap_per_group, banned_terms and referral_call.
- The path is correct and the `titles` block has one title per line.
- The Use case is one 37-word sentence (the UK one ran 78).

### E. Output quality — 3/4
- **What is strong:**
  - The error-vs-gap section (l.71) and Risk 3 (l.261) state the weak point plainly, including the landing's +3.3% sample flag (landing l.114).
  - The location rule (l.102) closes the overlap with the UK twin.
  - Two claims hold against the code:
    - `check --profile olena` does not see katerina's people, since it loads only the profile's own URLs (`outbound-registry.py` l.548).
    - Apollo has no location filter (l.236).
  - The DORA first-name trap is caught (l.202).
  - PROFILE_GEO["olena"] covers all five HQ countries (`outbound-pipeline.py` l.94-99).
  - olena has already worked Germany (three earlier `companies.md`), so the new-geo check in icp-detail l.563 is not triggered.
- **Parent-company row names take global slugs away from Nick:**
  - l.46 and l.233 name the group B rows `Swiss Re`, `Munich Re`, `Hannover Re` and `SCOR`.
  - `record` writes import company names to the global registry as covered by olena (`outbound-registry.py` l.453-469). After that, `check` excludes those companies for every other profile (l.617-620).
  - The UK twin used `-uk` names (`swiss-re-uk`, `gen-re-uk`, `rga-uk` in the registry) to avoid exactly this.
  - OQ2 (l.272) promises that "the US parents stay open for Nick" but gives no row name for Gen Re or RGA. It says nothing about the other four.
- **The waiver is described as narrower than it is:**
  - l.234 reads "`--waive-companies "Aviva,Royal London"` for Ireland-located people only".
  - The flag applies to the whole company (`outbound-registry.py` l.586-611). The Ireland limit holds only through the step-4 location rule, and the file does not say so.
- **The two Allianz rows have no split rule:**
  - Allianz Lebensversicherungs-AG (l.42) and Allianz Nederland Leven (l.44) are likely to export under one LinkedIn company.
  - Nothing covers how they are split for cap_per_group, the several-people rule (l.199) and the location rule.
- **A UK copy-steering phrase is carried over unchanged:**
  - "a second source of build evidence inside the application" sits in the carded angle paragraph (l.154).
  - That paragraph is outside the five-word card-wording check, which covers only Rules and lane-note lines (`outbound_pack.py` l.1742-1749).
  - The UK `closelyhq-import.csv` contains "second source" on 15 lines, and the UK QC had flagged this phrase.
- **The never-list has no mechanical backstop:**
  - It names Generali, Dazure, Bank of Ireland, BarmeniaGothaer and the Laya sale (l.170).
  - None of these is in `banned_terms` (l.10).
- **German pull noise is not estimated:**
  - Under geography Germany, the English `Underwriting Manager`, `Head of Underwriting` and `Head of Product` lines at Allianz, HDI, Munich Re and Hannover Re will mostly return P&C staff. German life underwriting sits under Risikoprüfung.
  - There is no volume estimate, despite the prompt's warning about validation cost.
- **Part of the exclusion list is unsourced:**
  - The Nordics, CH and AT are cut as "smaller individually underwritten markets" without a source (l.57).
  - The Helvetia Baloise merger excludes two companies, not a market.

## Top 3 issues (приоритет для improver)

1. **The group B rows use parent-company names** (`Swiss Re`, `Munich Re`, `Hannover Re`, `SCOR`; l.46, l.233).
   - `record` (`outbound-registry.py` l.453-469) will register those slugs to olena globally. `check` will then exclude them for Nick (l.617-620).
   - This contradicts OQ2 (l.272) and reverses the UK twin's `-uk` naming without saying so.
   - A row-naming decision is needed before step 2.
2. **Ireland is argued by analogy to the UK** (l.23, l.53), with no Irish source for point-of-sale decisions.
   - BPFI's "each with an underwritten life application" overreaches.
   - The Laya evidence sits on staging-looking hosts (l.287).
   - The Volkswohl Bund +60% (l.42) has no source.
3. **Carded copy-steering and missing backstops:**
   - "second source of build evidence" is still in the carded angle (l.154; 15 lines of the UK import).
   - Corrective forms and coordinator notes are in carded text (l.187, l.197, l.202, l.239).
   - The never-list names (Generali, Dazure, Bank of Ireland, BarmeniaGothaer) are not in `banned_terms`.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

agreement: ✅ agree
top_issue: reinsurer HQ rows named after the bare parents (`swiss-re`, `munich-re`…) would register the group slug to olena; registry match is slug equality, so only a future nick row with the same bare name is blocked, but the UK twin's convention was a location suffix. Fix round goes to a FRESH hypothesis-generator with every QC point (row naming with a country suffix and no parentheses, Irish point-of-sale sourcing, BPFI overreach, staging-host evidence, Volkswohl +60%, card copy-steering lines 154/187/197/202/239, never-list names into banned_terms, the smaller points). Verified by gate + grep, no second QC unless the fix round changes the cut.
