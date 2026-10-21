---
qc_date: 2026-10-21
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: katya
total_score: 16/20
status: good
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Source labels were inferred from empty profiles (compact has no source column); fixed in round 2 from a script-built source map, along with 5 Fleury FAIL->WEAK and Fernanda Araujo P1->P2 (PASS 32 / WEAK 13 / FAIL 59, verified by script)."
---

# QC Report — icp-validator — 2026-10-21

**Artifact:** `workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md` and `people-compact.csv` (104 rows: 40 Sales Navigator, 64 Apollo; the compact file has no source column). Code already checked limits, bans, the detector and completeness, and those results are taken as fact here.
**Total: 16/20**, good. The decisions hold. Two things need fixing before Vadim reads the report: the source labels, and four Fleury FAILs that should be WEAK.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Four borderline people at Fleury are FAIL, not WEAK.** The prompt says: "Человек на грани — WEAK". Gustavo Stuani Guimarães, Marcos Vignal, João Paulo Maramaldo and Jefferson Andreatti (decisions l.4, 11, 23, 75) are all "business-unit director, Lifecare unconfirmed". The agent's own pool A text (summary l.90) says they are in scope if Open question 4's "B2C business unit" means Fleury's patient-facing units, and the card keeps that unit. The agent rated an unstated unit as FAIL, but Aline Amorim Martinez, whose headline names orthopedics, ophthalmology and fertility, got WEAK. The two calls are inconsistent. Pool A and the promote command make the impact smaller, but these four belong in the WEAK table.
- **Followed correctly:**
  - The loop and outputs follow the prompt: `decisions.md`, `apply-decisions`, `skipped`, then a summary with pools and a `promote` command in the first report.
  - Open question 4 is applied as written: 8 Fleury PASS, all group product or digital roles.
  - Occupational-medicine coordinators are held out as an anti-case (summary l.94).
  - Humanolab and Lonvida people outside the campaign geo are kept under Open question 9 and flagged.
  - Ana Betancourt (brand and content) is on the `referral` lane under the standing decision.
  - Every row has `wave` = 1.

### B. Factual accuracy — 3/5
- **The data source is guessed, labelled as fact, and wrong in three places.** `people-compact.csv` has no source column, so the agent decided "Apollo row" from empty profiles:
  - Arlei José Frigieri (WEAK table l.79, decisions l.15 "per Apollo") is a Sales Navigator row. He is in the export block (compact l.15) and not in `apollo-candidates.csv`.
  - Cindy Pan (summary l.106, "Apollo did the same at ... Lonvida") is a Sales Navigator row (compact l.29). The stats line l.16 ("3 Apollo rows at Care Club and Lonvida") repeats the error.
  - Elizabeth Zoe (Alpharetta, US) is an Apollo row (`apollo-candidates.csv` l.33), but she is counted among the 11 people the "Fleury company page was attached to" (l.106).
  - "Four Apollo people at Med-Rio and Care Club are WEAK" (l.109): three of them are from Apollo.
- **"11 people who are not there ... and placeholder names" (l.106) goes further than the evidence.** Wesley Oliveira, Marcos Ponce and Ewaldo Mário Russo have plausible names and empty profiles. Nothing in the input shows they are not at Fleury. The stats line (l.16), "collisions or empty, unconfirmed profiles", is the accurate wording.
- **"pulled by company" (l.105) is only half right.** Apollo searched Fleury with a 70-title filter (apollo-log). What the pull missed is the Lifecare keyword, not a title filter. The concern itself is valid: no title or headline in the compact file says Lifecare or longevidade. Apollo also returned 0 for those keywords on 2026-10-21.
- **Checked and correct:**
  - The counts add up: 32 PASS (17/8/7), 8 WEAK, 64 FAIL (15 + 1 + 48), 73 Fleury rows, 22 senior people skipped, and the angle split of 20/5/4/2/1.
  - Facts in the PASS reasons match the compact file and the card. Examples: three PMs came from Saúde iD, Centeni runs two cycles a year, and Marina Andrade's headline names lifestyle medicine.
  - No product numbers and no 3DLOOK client names appear.

### C. Brand & tone — 3/3
- No banned words. The em dashes are in the template headings only. The register is plain and specific, which fits an internal checkpoint.

### D. Format & structure — 3/3
- The frontmatter is complete: `product: fitxpress`, `profile: katya`, `campaign`, `created`, `stage`, `status`.
- `decisions.md` is pipe-delimited. FAIL reasons are 2-5 words. Each PASS and WEAK row has a one-sentence reason with no `|`.
- All template sections are present. Question 4 is repurposed sensibly: the cap does not bind, so it asks about a Fleury re-pull.

### E. Output quality — 3/4
- **Edgar Gil Rizzatti's FAIL reason does not match his title.** The reason (decisions l.14) says "BU president, labs and hospitals". His title is "Presidente da Unidade de Negócios Médico, Técnico, de Hospitais e Novos Elos". The agent treats Novos Elos as a possible home for Lifecare when it puts Aline Amorim in WEAK. That would make Rizzatti the BU head above it. Pool B does list Novos Elos, so Vadim sees it, but the reason row is misleading.
- **Fernanda Araujo, a Group PM at a group of thousands, is P1 (l.68).** The card gives PMs P1-P2 only at companies under ~200 people. At Fleury, with no link to Lifecare, P2 is the fitting level.
- **The pool A `promote` command (l.99-101) names two of the five people with no reason given.** It leaves out Gustavo Stuani Guimarães, and the text explains only why Andreatti and Linhares are weak.
- **Observation, no deduction:** the people data shows regenerative signals. Santiago Ficcadenti co-founded BeStemcells. Lonvida's CMO also runs Beliah Medical Spa ("Medicina R…"). Step 2 already flagged the regenerative risk at both companies in `companies.csv`. A line in Top concerns would help message-sequencer stay on the diagnostics-and-follow-up line.
- **Strong points:**
  - The Lifecare gap is flagged first, with the card's own keyword rule.
  - Timeless people sit at the parent Choiz, and the report says messages must be about Timeless.
  - The Humanolab HQ conflict is raised against the card's rule "CEO and CPO location first". `companies.csv` records `product_hq=CO` from the site line "Estamos activos en Colombia", but the CEO is in San Francisco and the COO and President are in the US. The agent read the card's rule correctly, and the conflict comes from step 2.
  - The WEAK table names the two likeliest Lifecare owners.

## Top 3 issues (приоритет для improver)

1. **Source labels.** Correct the WEAK row for `arlei-josé-frigieri-32066125` and the "Apollo did the same" sentence: Arlei and Cindy Pan come from Sales Navigator, and Elizabeth Zoe comes from Apollo. Pipeline fix: `outbound_pack.py compact` should carry a `source:apollo|salesnav` flag, so the validator stops guessing provenance from empty profiles.
2. **Borderline means WEAK.** Move Gustavo Stuani Guimarães, Marcos Vignal, João Paulo Maramaldo and Jefferson Andreatti from FAIL to WEAK. The agent itself says Open question 4 may keep them. This also makes them consistent with Aline Amorim Martinez.
3. **Fleury reason and priority calibration.** Rizzatti's FAIL reason leaves out Novos Elos, the line the report itself treats as Lifecare's possible home. Fernanda Araujo should be P2, not P1: the P1 rule for PMs covers companies under ~200 people, and Fleury has thousands.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
