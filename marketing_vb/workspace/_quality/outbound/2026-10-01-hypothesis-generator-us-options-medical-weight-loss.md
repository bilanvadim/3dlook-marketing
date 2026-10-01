---
qc_date: 2026-10-01
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-10-01

**Artifact:** `workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/hypothesis.md`
**Total: 16/20** (good)

I scored this against the following sources:
- the hypothesis-generator prompt
- icp-detail.md §1 (and :597)
- proof-points.md
- accuracy-formulations.md §1.1-1.4
- compliance.md §9
- use-cases/fx-telehealth-weight-loss.md
- the approved base `2026-09-29-us-obesity-medicine/hypothesis.md`
- `sales-nav-raw/export-1.csv`
- `scripts/outbound_pack.py` CARD_SECTIONS (lines 727-732)

The messages card carries four sections: `Use case`, `Message angle`, `Rules for steps 3-5` and `Vadim's decisions`. It also carries the use-case file verbatim (lines 853-856). `Target buyer persona` goes only to the validate card.

The 30-company criterion does not apply here. Limits, signature, bans, the detector and completeness were taken as passed. notify.py was not run because this QC session has no shell.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 5/5
- No issues. It covers one hypothesis and every template section. Every export row has a verdict, matched on URL. The registry check and lessons from Nick's earlier campaigns are both in (lines 21, 62-70). The Message 1 gate is kept and the titles block is present. The standing decisions match the base and cardiometabolic files (lines 159-171).
- The export checks out against the CSV: 7 rows, 5 at Options, 133 staff, founded 2014. Titles, bios and former employers match the export.

### B. Factual accuracy: 3/5
- **The core premise has an unreconciled data point.** Line 25 says that "the telehealth page does not mention one" (a body composition test). Line 57 quotes the same telehealth page offering "Labs and metabolic analysis". Options' own name for its test is "Metabolic InBody Test" (line 56), and line 146 says "metabolic scan" is Options' name for that test. The app also syncs devices that may report body fat, and the app vendor sells a body-fat scale (line 58). Telehealth patients may already get a remote body composition step. The artifact flags this as "not verified" but never connects the "metabolic analysis" wording to the test.
- Line 91 (objection, validate card): "a typical basic integration takes 2-4 weeks". This figure is not in proof-points.md. It comes from icp-detail.md:597, which licenses it for the technical-integration angle only, and this campaign has no technical lane (line 70). It also contradicts the artifact's own line 139, "No other number". I did not apply the hard cap for numbers outside proof-points.md, following the 2026-09-29 QC precedent (the figure was licensed before and the code cards it for the technical angle only).
- Line 19, "no payer or employer contracts drive it", does not match line 155 ("Options' employer clients") or the `/employers/` page read at line 217.
- Line 59 credits "KFF Health News (June 2026)" but links Fierce Healthcare, "via search", so the source was not opened.
- Line 60, "Options publishes patients who lost more than 140 lbs", has no source link. Line 36 argues the $2M+ threshold from 2024 scale (39 clinics), even though 11 are open now.
- Clean on product claims:
  - The compliance line (line 140) is verbatim from compliance.md §9.
  - The FDA and MDR sentences are verbatim from the FAQ.
  - 96-97% / 1.5-2.0 cm and repeatability `< 1 cm` follow accuracy-formulations §1.1-1.2.
  - The validation population is 38-210 kg.
  - Speed is stated only as "under 45 seconds from the photos to structured results".
  - The 112,100 and 34,000 lines carry no client name and no geography.
- Sourcing: about 25 external URLs, mostly Options' own pages (used as evidence about Options), plus PMC, The Lancet, the Zenoti story and Google Play. Two are marked "via search" and were not opened.

### C. Brand & tone: 2/3
- Line 125 is in the `Message angle` section, which is carded as "Company facts the copy may use". It gives the writer two corrective-negation shapes: "fat lost, not just pounds" and the quotable "Real Medical Team, Not Just an App". The second is also counterproductive: it is Options' own line against apps, quoted to Options in a pitch for an in-app scan.
- Otherwise clean. Person-first language, the traps ("comprehensive", "objective", "metabolic scan", "Fat Burners") and the ban on replacement framing are all handled (lines 143-146).

### D. Format & structure: 3/3
- No issues. The frontmatter is complete and the path is correct. The titles block has one title per line. The Use case is one sentence (long, as in the base).

### E. Output quality: 3/4
- **The lane angles imply the gap that the Rules forbid.**
  - Line 120 (`online-intake`, messages card) sets up the contrast "In clinic, the free consultation starts with a body composition test. Online, intake starts with a health questionnaire and a video visit. A scan at online intake gives telehealth starters a baseline body record".
  - Line 119 says the scan "gives video visits a structured body record".
  - Line 141 forbids writing or implying that telehealth patients "lose the clinic test". The sequencer gets both instructions, so the likely copy is the forbidden one. It would reach the CEO and the growth lead of a company that may already offer "metabolic analysis" on telehealth (see B).
- **The general Rules do not stop promises of retention, engagement or ROI.** Line 143 lists what the scan does not do (diagnose, dosing, muscle, weight loss) but not retention. Only the `online-intake` lane bans it (line 120). The messages card also carries fx-telehealth-weight-loss.md verbatim, and its hero line is "boost retention, reduce drop-off, and prove program ROI". So the Castle and Tarnawa sequences have no explicit guard against promising retention.
- **Copy instructions are placed where the writer will not see them.** Line 79 ("Do not expand 'NCO' in copy") and line 80 ("write to the growth and operations role in his headline") sit in `Target buyer persona`, which the messages card does not carry. They reach the writer only if the validator copies them into `flags`.
- Line 142 bans "fewer clinics", "consolidation", "moving patients to telehealth", "new CEO" and "new leadership". Frontmatter `banned_terms` (line 9) gates only "closed", "closure" and "closing". So the campaign's main reputational risk is enforced by judgment, not by the gate.
- Persona fit for Del Cecato: line 80 makes new-patient conversion his KPI, but line 120 bans conversion claims. His lane offers nothing tied to his KPI. That is honest, but it is weak.
- The titles block (lines 111-112) adds "Senior Director" and "Clinic Director". Line 98 says the pull exists to find the COO, the CMO and a technology lead.
- Strong otherwise:
  - the closure evidence is dated and counted (16 pages, 11 open clinics)
  - the "never mention closures" discipline
  - consistent facts across all five people
  - stop conditions
  - falsified and inconclusive thresholds sized to 5 invites at 15.9%
  - the honest framing as an account play, not a pilot

## Top 3 issues (priority for improver)

1. Lines 119-120 against line 141: the `telehealth-body-record` and `online-intake` angles rest on a contrast between clinic and online care. That contrast implies telehealth patients lack a body composition step, which the Rules forbid. The premise is also unverified: the telehealth page offers "Labs and metabolic analysis" (line 57), and Options calls its body composition test "Metabolic InBody Test" (line 56).
2. Line 143: the general Rules have no ban on promising retention, engagement or ROI; it exists only in the `online-intake` lane (line 120). Meanwhile the carded use-case file's hero line is "boost retention, reduce drop-off, and prove program ROI".
3. Line 125: the carded "Company facts the copy may use" hand the writer "fat lost, not just pounds" and "Real Medical Team, Not Just an App". Both are corrective negations, and the second is Options' anti-app line, quoted back to it in an app pitch. Lines 79-80 also hold per-person copy flags in a section the messages card does not carry.

## coordinator_review

```
agreement: ✅ agree
top_issue: lanes 119-120 imply the telehealth body-data gap that Rule 141 forbids, on an unverified premise ("Labs and metabolic analysis" / "Metabolic InBody Test")
action: all three top issues and the small points sent back to hypothesis-generator in the same run (Vadim waived checkpoints for this campaign 2026-10-01); re-checked before hypothesis-gate --stamp
```
