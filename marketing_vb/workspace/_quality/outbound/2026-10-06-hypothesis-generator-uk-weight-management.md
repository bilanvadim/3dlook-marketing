---
qc_date: 2026-10-06
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-06-uk-weight-management/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-10-06, uk-weight-management

**Artifact:** `workspace/outbound/campaigns/2026-10-06-uk-weight-management/hypothesis.md`
**Total: 16/20** (good)

**Scored against:**
- the hypothesis-generator prompt;
- icp-detail.md §1, §5, universal exclusions and :597;
- proof-points.md, accuracy-formulations.md and compliance.md §9;
- export-summary.md;
- Vadim's 2026-10-06 scope: only junk and non-UK rows go OUT, and Apollo tops up accounts that are missing staff;
- `global-company-registry.json`, `katerina-registry.json` and the 2026-09-01 `closelyhq-import.csv`;
- the 2026-10-05 LatAm QC report, for calibration.

Limits, bans, detector and completeness were taken as given.

**Limits of this QC:** this session had no web tool and no shell. Web sources were judged on the artifact's own quotes and URLs, and notify.py was not run.

**Verified clean:**
- **Counts reconcile everywhere:**
  - 125 IN + 41 OUT = 166, summed row by row over the 64-row table;
  - the OUT breakdown is 25 + 9 + 1 + 5 + 1;
  - lanes are 76/13/12/11/7/6, tiers are 14/22/13/76, and every per-account lane split matches;
  - LighterLife has 43 people, plus 7 Apollo places under the cap = 50.
- **Medicspot five:** all five are in the 2026-09-01 `closelyhq-import.csv`, which confirms they were already contacted.
- **Registry:** `voy` is marked manually_excluded, and `body-clinic` and `healthhero` are listed as covered by olena.
- **July baseline matches `metrics-final.json`:** 69 accepted, 26.7% acceptance, 18.8% replies per accepted.
- **Copy text:** the GDPR line is verbatim from compliance.md §9 (:102), and the repeatability and validation-scope wording comes from accuracy-formulations.
- **Fact table:** the 2026-10-05 lesson was applied. Writer notes sit in their own column, not inside the fact strings.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 4/5
- **Philip Bazire is OUT, which goes against "only junk and non-UK out" (line 67).** He is based in the UK and is Medical Director of PronoKal UK. Medical Director is a buyer title in icp-detail.md §1. The reason given is "Barcelona headquarters, Olena's geo", but PronoKal is not in `global-company-registry.json`. The scope did not call for a "non-UK parent company" rule, and the default should have been IN. It is raised as Open question 3, but with the wrong default.
- **Reset Health's Apollo flag is "no" (line 63), against "top up companies that are missing staff".** Reset Health has 29 of 61 LinkedIn staff in the export. The artifact's reason is that the key titles are already in the list. Its own titles block (lines 192-235), however, asks for CMO/Medical Director, Head of Nutrition/Dietetics, CCO and Head of Research, and none of those titles is on the export rows. The artifact notes that search is free (line 26).
- **Line 381 rewrites Vadim's instruction as "where the list does not reach decision-makers" and raises no open question about it.** Perspectum's top-up is limited to "6 at most" (line 100) with no reason given.
- **Lane mismatch:** Dr George Sanders (line 159) is put in `product`. The artifact's own lane-by-title rule (line 173) maps research and evaluation leads to `clinical`.

### B. Factual accuracy: 3/5
- **The LighterLife angle assumes an app that the artifact's own research did not find.**
  - Lines 161, 247 and 305 state "Head office owns the client app", and every unit referral asks who owns it.
  - Line 442 says: "no LighterLife app on the UK App Store (search 2026-10-06)".
  - This affects 43 people, the largest group.
- **ML2 (line 279), "about 20 years", has no source.** The export (export-summary :9) gives MoreLife's founding year as 1999, which is 27 years ago. This fact can reach 36 MoreLife people.
- **"A typical basic integration takes 2-4 weeks" is filed under "Numbers only from proof-points.md" (line 338), but it is not in proof-points.md.** It comes from icp-detail.md:597. I did not apply the cap: the figure is in a file the agent was given, and the 2026-10-05 QC took the same view. The source label is still wrong.
- **The Medicspot sale is described as "weight-loss business" (line 65) and "GLP-1 business" (line 139).** The cited HTN URL says DCA acquired Medic Spot Limited, the company itself. This is context only.
- **Sourcing:** about 25 external URLs, mostly primary: trade press, NHS Lothian, Companies House, company sites and App Store listings. Market figures are kept out of copy (line 138).

### C. Brand & tone: 3/3
- No issues. There are no em or en dashes. Banned words appear only inside the rule that bans them (line 343). The wording is person-first, and no instruction wording sits inside the fact strings.

### D. Format & structure: 3/3
- No issues. The frontmatter is complete: product, profile, market, created, status, use_case, cap_per_group and banned_terms. The path is correct, every template section is present, the `titles` block has one title per line, and the Message 1 gate is kept.

### E. Output quality: 3/4
- **CW3 (line 283) contradicts the overlap rules.** It is a fact the copy may use, and it gives members "weekly readings". Line 255 says not to name what the Counterweight app records, and line 326 says never to list a prospect's records and then describe the scan. CW3 invites exactly that pairing.
- **The uniqueness rule for LighterLife is probably not workable** (lines 241, 324). Each of the 43 LighterLife people must get their own question, and 41 of them get the same referral ask ("who at head office owns X"). The artifact offers about 12 themes (line 305) and no per-person assignment. Questions will either repeat or become contrived.
- **Some IN rows have no plausible link to the use case:** Archvale (GP-practice succession) and a triage midwife at NW Anglia, whose context is pregnancy and is barred by the artifact's own rules. Keeping them in matches "maximum contacts", and both are flagged under Open question 7. Low cost.
- **Strong otherwise:**
  - name collisions are failed by name, and the Companies House check rules out the wrong Counterweight;
  - the unregistered 2026-09-01 send was caught, with a record step for the coordinator;
  - the GPhC constraint is turned into a hard "never verification" rule;
  - risks and the falsification test are honest.

## Top 3 issues (priority for improver)

1. **The LighterLife "client app" premise is not backed by the artifact's own evidence (B; lines 161, 247, 305 vs 442).** It shapes the copy for 43 people. The angle should be based on "programme / member tools", or the app should be confirmed first.
2. **The scope was applied unevenly (A).**
   - Bazire (UK-based, PronoKal UK, in no registry) is defaulted OUT (line 67).
   - Reset Health gets no Apollo top-up even though 32 of its 61 staff are missing and the titles it searches for are absent (line 63).
   - The top-up rule was quietly rewritten at line 381.
3. **The fact table contradicts the copy rules (E/B).**
   - CW3's "weekly readings" pairs Counterweight's own data with the scan (line 283 vs 255, 326).
   - ML2's "about 20 years" has no source and conflicts with the 1999 founding year (line 279).
   - The 2-4 weeks figure is labelled as coming from proof-points.md (line 338).

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the LighterLife angle (43 people) rested on a head-office client app the artifact's own sources could not find, and Vadim's top-up rule was narrowed to decision-makers (Reset Health left out); fixes 1-4 go back to a fresh hypothesis-generator together with the coordinator's free Apollo search counts (MoreLife and LighterLife would pass cap 50: a question for Vadim, cap unchanged).
```
