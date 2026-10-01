---
qc_date: 2026-10-01
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-01

**Artifact:** `workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/icp-validation-summary.md`, `decisions.md`
**Scored against:** `card-validate.md` + `people-compact.csv` only (the agent's inputs). Limits, signature, bans, detector and completeness are taken as fact from the code checks. Not marked down, per the coordinator: the job-change check (no web, no role dates; the coordinator confirmed in the 09-28 export that both Clinic Directors still list Options as current) and the missing checkpoint question (Vadim waived checkpoints on 2026-10-01).
**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was checked and holds

- **The persona fit is exact.** All five decisions match the card's persona table (card lines 35-39) on tier and lane: Castle P1 `at-home-scan`, Tarnawa P1 `at-home-scan`, Del Cecato P2 `program-feature`, Hicks and Foy P3 `referral`. Everyone is wave 1, with no WEAK and no FAIL. That is correct, because card decision 2026-09-29 #7 keeps thin or stale profiles and #3 keeps FAIL for the wrong company only.
- **The stats recount correctly** from `decisions.md` and `people-validated.csv`: P 2/1/2, angles 2/1/2, 5 of 50 cap, 0 registry flags (the `flags` column is empty on all five compact rows), 0 skipped (`skipped-detail.md`).
- **The two OUT people are accounted for.** Summary line 30 explains why Osborne and Ortega are not in the compact list and cites the verdict table and decision 2026-10-01 #1.
- **The agent read the rows against the card.** It did not copy the card. Line 57 notes that Del Cecato's only earlier role in the row is "Retail Sales Manager at GNC", against the card's growth and sales-strategy reading. Line 58 notes that Foy's row headline now reads "Healthcare Sales & Operations Leader". Both are real signals the card did not state.
- `card-messages.md` line 37 carries Tarnawa's "clinical register", so the plain `at-home-scan` tag in `decisions.md` line 3 loses nothing downstream.

## What was wrong (specific)

### A. Adherence — 5/5
- No issues. Only the two inputs were used. `decisions.md` follows the pipe schema exactly, with no `|` inside reasons. `apply-decisions` and `skipped` ran, and their outputs exist. The template sections are all present. Renaming "please confirm" to "decisions on record" (line 61) is the right adaptation under the waiver.

### B. Factual accuracy — 4/5
- **Line 52, "they go in with `promote` ... with no new round", is wrong about the pipeline.** `promote` only edits rows already in `people-validated.csv` and fails with "nobody by that name in people-validated.csv" for anyone else (`outbound_pack.py:1230-1232`). A newly pulled COO, CMO or technology lead needs the registry check, `compact`, a decisions row and `apply-decisions`, which is a new round. Card line 98 says "added with `promote`". The agent repeated that and added "no new round", when it should have flagged it.
- **Line 56 states an inference as fact.** "Options Health Coach and the telehealth stack sit with the COO, CMO or technology lead" is not in the card. The hypothesis leaves ownership open, and the referral lane asks exactly that question ("who at Options looks after the Health Coach app and the telehealth program?", `card-messages.md` line 39). "The two `referral` asks are the only route to them" ignores Castle, who is P1 in the same send list, is their direct superior, and is the card's first named buyer (card line 31).
- No proof-point numbers appear in the artifact. Every PASS reason traces to the card or the compact row, and no client or role is invented.

### C. Brand & tone — 3/3
- No issues. The prose is plain and each reason answers "why is he here" in one sentence. The em dashes at lines 10, 44 and 61 are template headings.

### D. Format & structure — 3/3
- No issues. The frontmatter has `product: fitxpress`, `campaign`, `profile`, `step`, `date` and `checkpoint`. The prompt template asks for no `status:`. With zero pools, prose in place of the pools table is right. `decisions.md` matches the schema.

### E. Output quality — 3/4
- **Two of the card's three pre-send stop conditions are missing.** Card line 74 lists three. The summary hands over only the person-level one (line 58). The account-level two are left out: Options announcing a sale, merger or wider shutdown, and Options already running a phone scan or having signed a scanning vendor. This is a one-account campaign triggered by clinic closures, so those two checks can cancel all five sequences at once. The validator cannot run them, which is why it has to name them as still open. Foy's job-search headline is itself a weak signal of account health that the summary could have connected to the closures.
- The `promote` route at line 52 is not runnable as written (see B). The coordinator would find out at the moment Vadim adds people.
- The rest is ready to use. Line 59's note on "five parallel sequences to one account" is useful guidance for message-sequencer, and `card-messages.md` line 35 already asks for it.

## Top 3 issues (priority for improver)

1. Do not describe `promote` as a way to add people who are not in `people-validated.csv`. People pulled after validation need registry check → `compact` → decisions row → `apply-decisions`. When the card says otherwise (card line 98), flag it and do not extend it. This is the same family as the issue at the top of the 09-29 cardiometabolic QC: a `promote` path presented as working when it does not run. Pipeline fix outside the agent: the hypothesis template and `card` should say "new pull = re-validate the new rows".
2. Mark ownership claims that the card does not make as inferences (line 56: the app and telehealth stack "sit with the COO, CMO or technology lead"). Do not call the referral lane "the only route" when a P1 CEO is in the same send list.
3. In the summary, list every card stop condition the validator could not run, not only the person-level one. For a single-account campaign, the shutdown, sale, merger and displacement checks matter most.

## coordinator_review

```
agreement: ✅ agree
top_issue: the "add new people with promote" instruction came from the coordinator's own decisions block (card line 98), not the validator; promote only edits existing rows (outbound_pack.py:1230-1232)
action: fixed in hypothesis.md, card-validate.md and the summary (registry check → compact → decisions row → apply-decisions); "only route" reworded; the three pre-send stop conditions checked by the coordinator on the web 2026-10-01 and recorded at the end of icp-validation-summary.md, all clear
```
