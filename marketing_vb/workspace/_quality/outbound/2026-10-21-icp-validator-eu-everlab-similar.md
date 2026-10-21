---
qc_date: 2026-10-21
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: olena
total_score: 17/20
status: good
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Commentary guessed facts (Apollo mode, segment) and missed Werlabs/Aeon owner gaps; sent back to the validator with the Apollo owner-level candidates; decisions themselves hold"
---

# QC Report — icp-validator — 2026-10-21

**Artifact:** `workspace/outbound/campaigns/2026-10-19-eu-everlab-similar/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md`, `people-compact.csv` (82 rows: 40 from Sales Navigator, 42 from Apollo) and the coordinator's four identity facts. Limits, bans, detector and completeness were checked by code and are taken as fact.
**Total: 17/20**, good. Every person decision can be defended, and all counts reconcile. The problems are in the commentary. One Top concern blames the wrong cause. The coverage concern misses two companies. The Mavie cut list removes the wrong people.

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
- **Two lanes go against the card's persona rule (card l.88: marketing and content are "not the buyer", so they get the `referral` lane).**
  - Vera Brockherde (decisions l.75): the reason itself says "content-side, so P3", yet she is on `product`. Her earlier role is "Content Product Manager at Mavie" (compact l.75).
  - Philippine Breuil (decisions l.43) is on `product` P3. Her title says Growth, but her headline is "Head of Marketing @ Lucis" (compact l.43). This one is a defensible middle call. Vera is not.
- **Followed correctly:**
  - The loop follows the prompt: `decisions.md`, then `apply-decisions` and `skipped` (both `people-validated.csv` and `skipped-detail.md` exist), then the summary with pools in the first report.
  - The four identity facts are applied: Jensen Taylor, Beck and Mesnage are FAIL. Pohludka is P2 via the parent studio. Dr.Dropin stays FAIL by registry.
  - The board member is FAIL (Jon Sintorn, card l.88).
  - Empty profiles are WEAK, except Lars Aar. He is FAIL because a second, real YEARS CEO exists, which the `empty-profile` flag rule allows.
  - Vadim's 10-19 decision beats OQ5 the right way. UK leaders (Seymour, Frenchman) are PASS, and local UK staff (Whitcombe, Patel) are WEAK, flagged in Top concerns l.114.
  - The Circle Health collision is reported exactly as card item 3 describes it, including the limit of `--waive-companies`.
  - Every row has `wave` = 1.

### B. Factual accuracy — 4/5
- **Summary l.111, "Выгрузка Apollo по компании, не по title", is wrong.** `apollo-log.md`: "companies 25, 40 titles". Apollo did use the title filter. Founding engineers and the founding designer most likely came in through a loose match on "Founder", so the fix is a title exclusion, not a switch to search by title. The agent did not have the log, but it stated a guess as fact. The 2026-10-21 LatAm QC flagged the same error ("pulled by company is only half right"), so this is now a repeated pattern.
- **Summary l.113 puts Longevity Center Poland in segment B.** Step 2 put it in segment C (`companies-verified.csv` l.13). The card lists four B companies: Aeon, YEARS, Prescan and Preventicum.
- **Summary l.112, Biolytica "её известный CEO — другой человек", has no support in the inputs.** The coordinator's fact was only "likely not a real executive". The suggestion to re-pull Biolytica through Apollo is fine without this claim.
- **Checked and correct:**
  - The counts reconcile: PASS 61 (28/20/13), WEAK 7, FAIL 14 (9 registry + 5), the angle split 35/10/8/3/3/2, and all 20 group counts (Mavie 16 = 26%).
  - 20 of 25 companies have a SEND, with the 5 empty companies named correctly.
  - The skipped list has 18 senior people out of 21.
  - The PASS reasons match the compact file and the card. Examples: Najafi is COO and Medical Director, Bruno came from Maximon, Axo uses partner labs (card segment A), and the released seven are named correctly.
  - No product numbers and no 3DLOOK client names appear.

### C. Brand & tone — 3/3
- No issues. The em dashes are in template headings only, plus one placeholder cell in the pools table (l.106). Code already checked bans. The register is plain and specific.

### D. Format & structure — 3/3
- The frontmatter is complete: `product: fitxpress`, `profile: olena`, `campaign`, `created`, `stage`, `status`.
- `decisions.md` is pipe-delimited. FAIL reasons are 2-5 words, and registry reasons are kept as written. PASS and WEAK reasons are one sentence with no `|`.
- All template sections are present. The Dr.Dropin pool lists 7 names where the template asks for 3-5, which is acceptable because all 7 are explained.

### E. Output quality — 3/4
- **The Mavie cut list (l.110) cuts by P3, which removes the wrong people.**
  - It drops Mavie Work's own Head of Engineering (Neaga) and Head of Operations (Busek-Baum).
  - It keeps Mavie Next venture-builder roles and an unnamed subsidiary: Gandel l.30, Bodenstein l.32, Sobulska l.34, Bijelac l.36. In the same paragraph, the agent says these roles are not Mavie Work. Per the prompt's multi-app rule, the buyer owns the specific product, and here that is the corporate-health line.
- **Lea Paradzik is P1 with the reason "MavieMe, the member app" (decisions l.72).** But l.110 treats MavieMe as a separate entity from Mavie Work GmbH. Nothing in the input links MavieMe to the corporate programme. P2 or a note would match the agent's own concern.
- **The coverage concern (l.113) and question 3 (l.120) leave out two companies with no owner-level person.**
  - Werlabs SEND is only the COO (P2) and the CTO (P3).
  - Aeon SEND is only VP Ops (P2) and VP AI (P3). Aeon is an actual segment B company.
  - The template names "в группе нет ни одного владельца продукта" as a concern. These two need an Apollo top-up more than Longevity Center Poland does.
- **Lucis is flagged but nothing is proposed (l.111).** 8 SEND go to a seed-stage startup. They include two `referral` founding engineers, while both founders, the Head of Ops and Product are already on the list. Question 4 asks about cutting Mavie only.
- **Priority logic is applied to one person only.** Gemma Frenchman is P2 "because Preventicum is fit 3" (decisions l.17). The card gives fit 3 to all seven released companies, yet Kuttichová and Slapal (Macromo, l.31, l.36) and Aichlseder (Hello Inside, l.25) are P1.
- **Strong points:**
  - The Mavie concentration is flagged first, with the three-entity split.
  - The UK-staff gap in the card is named precisely.
  - Pools state the exact registry mechanics.
  - The report fits on a page.

## Top 3 issues (приоритет для improver)

1. **Commentary states guesses as facts.** The Apollo concern says "by company", but Apollo used the 40-title filter (`apollo-log.md`). Longevity Center Poland is segment C, not B. The "known CEO" claim for Biolytica has no source. This is the second time today: the LatAm QC caught the same Apollo error. Pipeline fix: the card or compact should carry the Apollo search mode and each company's segment, so the validator stops guessing them.
2. **The coverage concern misses Werlabs and Aeon.** Neither has a CEO, founder, medical lead or product owner in SEND. Add both to the concern and to the Apollo top-up question. Aeon belongs there ahead of Longevity Center Poland.
3. **The Mavie cut order goes by entity, not by P3.** If Mavie is cut, Mavie Next and the subsidiary roles (Gandel, Bodenstein, Sobulska, Bijelac) go first. Keep Mavie Work's own Head of Engineering and Head of Operations. Make Lea Paradzik P2, or link MavieMe to Mavie Work. Also put Vera Brockherde on `referral` (content-side, card l.88), and either give Gemma Frenchman P1 or apply the fit-3 downgrade to all seven released companies.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
