---
qc_date: 2026-10-16
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: nick
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-16

**Artifact:** `workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md` and `people-compact.csv` (384 rows: 359 from the export, 25 from Apollo, 5 of them outside the US). Vadim asked for maximum use of the list, so a wide SEND is intended. Code already checked limits, bans, the detector and completeness, and those results are taken as fact here.
**Total: 18/20**, excellent. Fix the small items below before message-sequencer runs.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Two named card cases are missing from the report.** Verdict-table rows 15 and 18 tell the validator to release Roukoz Abou Karam (Goodpath) and Dr. Jennifer Frangos (Vida, `clinical` P2) "only if current". Neither is in `people-compact.csv` or `people-raw.csv`, so the check could not run. The summary never says so, and Vadim is not told that the release path was closed upstream.
- **`people-raw.csv` was read even though the prompt forbids it.** The read was limited to 7 conditional rows and 2 Patrick Lawrence rows, and it is disclosed (summary l.12). It was also needed: the compact view hides Kristin Grunzweig's headline "Director of Client Success @ Vida Health | Client Relations" because it "says no more than the title", yet that headline is the only proof of her company. No deduction for the read itself. The `compact` rule that hides company-naming headlines needs fixing.
- **Two card instructions were not carried out: the repeat displacement search and the job-change checks by name.** The agent has no web tool, and it said so as Top concern #1 and #2 and as question 5. This is a pipeline gap, not the agent's fault. Someone has to run both checks before import.
- **Followed correctly:**
  - All 7 identity collisions and 3 held duplicates are FAIL with 2-5 word reasons.
  - Scott Paddock is P1 `product`. Allison Treftz and the Naturally Slim rows are regrouped to their canonical companies.
  - Michael Becker is `referral` with the employer line. Gary Earl is `referral` as an advisor. Steven Watts is flagged as never-name.
  - The cap holds: Included Health has 96, under 100.
  - Every row has `wave` = 1.

### B. Factual accuracy — 5/5
- **Every count in Stats checks out against `decisions.md` and the card:**
  - 384 = 367 PASS + 7 WEAK + 10 FAIL.
  - 344 export PASS = 342 IN + 2 confirmed conditional, plus 23 Apollo PASS.
  - P1 43 = the card's 36 + 7 Apollo.
  - P2 107 = 94 − Ennesser − Anderson + 15 Apollo.
  - Merger-account exposure is 137/367 (96 + 41).
- **Row quotes check out:**
  - Kristin Grunzweig's headline (raw l.340).
  - Joe Ennesser's one-line profile, "Chief Operations Officer at Crossover Health" (raw l.354).
  - Patrick Lawrence's ProMed / veEDIS history (compact l.121, l.235).
  - Matthew Noble's UK roles: Caldicott Guardian, Responsible Officer.
  - The 11 thin profiles in Top concerns are exactly the `empty-profile` PASS rows, apart from Kristin, who is covered separately.
- **No product numbers, no 3DLOOK client names.** The reasons in `decisions.md` contain no Premise, Firefly, merger or acquisition wording. Dave Minns' title "(acquisition of Bright.md Inc.)" was stripped from his reason (l.102).
- **Observations, no deduction:**
  - Section "Где разошёлся с раскладкой карточки" (l.45) does not fully reconcile with the card's lane totals. Export rows carry `product` 27 against the card's 29, and `technical-integration` 42 against the card's 41. The listed moves explain at most one of the product gaps.
  - "Montreal-based / London-based on Goodpath's US program" (l.381-382) is an inference written as fact.

### C. Brand & tone — 3/3
- No banned words. The em dashes are in the template headings, plus one in Russian prose (summary l.459). The register is plain and factual, which fits an internal checkpoint.

### D. Format & structure — 3/3
- The frontmatter is complete: `product: fitxpress`, `profile: nick`, `campaign`, `created`, `stage`, `status`.
- `decisions.md` is pipe-delimited, has a reason on every PASS and WEAK row, and has no `|` inside any reason.
- All template sections are present. The two extra sections (Apollo assignment, divergences from the card) are useful.

### E. Output quality — 3/4
- **The geo rule was invented, and a `geo:katerina` row went to SEND.** The card has no geography rule. The agent made one: "the US company stays with nick, unless the person works in a business on another profile's market".
  - Under that rule, Samantha Wu (`samantha-wu-md`, London, flag `geo:katerina`, l.382), Christelle Younes (Montreal) and Rajan Bhuyan (Bengaluru) are PASS.
  - The rule is explained in Top concerns, but the numbered questions (l.468-472) ask about geo only for Noble and Pugh. Vadim is never asked to confirm the rule that sent Wu.
- **The promote command uses the wrong pool for Cameron Pugh.** He is in pool G (geo) in the table (l.439), but the command puts him under `--pool C` (l.449).
- **Some row signals are not addressed:**
  - Josh Bruce (`josh-bruce-70227426`, P2, l.234) is "Onsite Medical Director" at Crossover, but his headline and his only listed roles say "Chiropractor at SportsPlus". That is another employer, which points to a stale or dual role. His reason says only "(chiropractor)", and he is not on the job-change list.
  - `dr-garima-sharma-3a512516` (P1) has `first_name` = "Dr. Garima" in `people-validated.csv`, so the greeting would read "Hi Dr. Garima". The summary does not flag it.
- **The WEAK table gives no recommendations.** The agent itself writes that Joe Ennesser "looks like a collision" and that Marcia Upson's "profile is most likely stale". Both still get a ready one-line `promote` command in pool C, with no "not recommended" note.
- **The referral reasons are formulaic.** About 100 of the 174 say only "sales referral", "finance referral" or "account-side referral". That is acceptable under standing decision 3, and the agent itself flags that the writer needs separate questions per sub-role (l.460).
- **The rest is strong:**
  - The extra Crossover client-name catches beyond the card: Barry Giglio's headline names Applied Materials, and Steven Chang's earlier role was at Applied Materials.
  - The reasoned verdict that the two Patrick Lawrence profiles are one person.
  - The coverage gaps after Apollo: no medical director at Digbi, no CMO at Goodpath.
  - The conditional confirmations are disclosed with a fallback: "if that is not enough for Vadim, both go to WEAK".

## Top 3 issues (приоритет для improver)

1. **Geo decisions need Vadim's explicit yes.** Add a numbered question that confirms the company-level geo rule for `samantha-wu-md`, `christelle-younes-15a7b812a` and `rajan-bhuyan`, or move `samantha-wu-md` to WEAK next to Noble and Pugh, since all three carry the same `geo:katerina` flag. Also fix the pool label in the Pugh promote line (C → G).
2. **Row hygiene before message-sequencer runs.** Put `josh-bruce-70227426` on the job-change list, because his headline names SportsPlus. Normalise `first_name` for `dr-garima-sharma-3a512516` to "Garima".
3. **Close the open card items in the summary.**
   - State that Abou Karam and Frangos were not in the input.
   - Add a take or drop recommendation to each WEAK row, including "do not promote" for Ennesser and Upson.
   - Complete the lane-divergence list (export rows: product 27 vs the card's 29, technical-integration 42 vs 41).
   - For the pipeline owner: the displacement re-check and the job-change checks must run before import. The validator has no web tool.

## Coordinator review

agreement: ✅ agree
top_issue: the invented geo rule (Wu/Younes/Bhuyan PASS, Noble/Pugh WEAK) goes to Vadim as one explicit question at the checkpoint. Row hygiene: Garima first_name fixed by the coordinator; Josh Bruce kept PASS (the export's Experience lists the Crossover role first, SportsPlus concurrent; logged in decisions.md). The 5 conditional WEAK stay out under Vadim's OQ3 answer (send only if the role is confirmed). Displacement was re-checked on the web by the hypothesis agent the same day (2026-10-16, none found); the job-change check on thin profiles needs web or Apollo credits and goes to Vadim as a choice.
