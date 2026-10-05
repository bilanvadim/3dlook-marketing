---
qc_date: 2026-10-05
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: katya
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-05

**Artifact:** `workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md`, `people-compact.csv` (176 rows). Counts and identity were taken as fact from the code check.
**Total: 13/20** — marginal (targeted rework, not regeneration)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 1 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- The author prompt (`icp-validator.md` line 47) says `empty-profile` is "не PASS без второго подтверждения; обычно FAIL или WEAK". 21 `empty-profile` rows are PASS. For most of them the only support is the company page on the row. Lines 51-52 of the same prompt say a company export puts the real page on every row, so the page alone does not confirm identity.
- The agent saw this. Top concerns (summary line 307) says the 21 "нічим не відрізняються від WEAK-пулу «ідентичність»", but it left the call to Vadim. This run has no checkpoints, so nobody will make that call, and the inconsistent line ships. The prompt says "Ты судишь".
- Everything else follows the card. All six branches are resolved as the card wrote them, advisors are held under the card's "held, not failed" rule, the 7 FAILs are by name, pools come with promote commands, and `--force` is used where flags need it.

### B. Factual accuracy — 3/5
- The basis the summary gives for the 21 is wrong for at least 4 of them. Line 307 says they "йдуть за опорою на сторінку компанії на рядку". Milena Espinha, lisete espindola and Mônica Melli are re-grouped Lipocenter rows. Card row 19 shows 4 Lipocenter rows with no page, and one of those is the company-named row. Elaine Tadiello is a re-grouped Siluets row with no page (card row 18). Alejandro Gorissen and Silvia Lima are re-grouped from AxisMed rows, and card row 5 shows two AxisMed rows with no page.
- Several reasons state a role at a unit that the row does not show: "Owner of a Lipocenter unit" (Milena, lisete), "Administrative director at a Lipocenter unit" (Mônica), "General manager at a Siluets unit" (Elaine, Regiane). The row gives only a title and a group. An inferred remit is written as fact.
- No proof-point numbers appear in this artifact, and no invented clients or companies were found.

### C. Brand & tone — 3/3
- No issues. This is an internal artifact, and no banned words were found.

### D. Format & structure — 1/3
- `icp-validation-summary.md` has no frontmatter, so `product:` is missing. Under the hard rule, D cannot go above 1. Every earlier icp-validator summary carried `product: fitxpress` (QC reports 09-29, 10-01, 10-02). The prompt template is silent on frontmatter, which is why D is 1 and not 0.
- The sections follow the template, and `decisions.md` matches the schema.

### E. Output quality — 3/4
- **One-line line, inconsistent.** The same evidence gets opposite decisions, depending only on whether the card named the person for a check:
  - "Empresária" or "Proprietário" alone: Meire Satelite (Siluets), Sandra Baldassari and Cristiane Aguilar (Lipocenter) are PASS. Tami Bianca ("Empresario") and Regina Alves Ribeiro ("Sócio"), on Magrass unit pages, are WEAK.
  - A generic title alone: Carlos Coelho ("Executivo", RWE) is PASS. Renan Schonton ("Chefe", Vidalink) is WEAK for "nothing on the row confirms".
  - No company page: Renata Assuncao is WEAK partly for "no company page". The four no-page rows above are PASS.
- **A consistent line that holds up:** for an `empty-profile` row, PASS needs one of these: a title specific to the account, a headline, a surname tie, or a card default naming the person. A company page alone, a generic owner title alone, or no page means WEAK. Under that line, every current WEAK stays WEAK and 10 PASS move to WEAK. aline caio, Viviane Lins and Wesley Denardin stay PASS on the card's branch defaults. Adrielle Dalul stays on the surname tie and Simone Martins on her headline. Regiane, Susana Augusto, Daniele Araujo and Janiel Zioti stay on specific titles. Abilio Costa stays as named by the card.
- **Franchise handling: correct.** Units go `referral` P4, as the card says. Gabriela Biazus is held under the card's explicit "if neither can be shown, hold". The defaults for Flaminio Dalul, aline caio and Emagrecentro are applied, and the zero-buyer gap is put in front of Open question 3. One miss: Adrielle Dalul's "Diretor executivo de vendas" reads as a franchisor-level sales role. It is assumed to be a unit role and is not flagged as a possible HQ person, although Viviane Lins was flagged.
- **Advisor WEAKs: correct.** On all three rows the Nilo or Liti seat appears only in `earlier_roles`, and the compact list cannot show whether it is current. Graziela Heusser Azeredo is rightly PASS, since the seat is her current title.
- **Lipocenter as a group:** all 6 PASS are `empty-profile`, franchisor status is unverified, and no app is verified. The whole group's send rests on unconfirmed identities. After the flips, 3 rows remain.

## Decisions to reverse (PASS → WEAK)

| Person | Group | Why |
|---|---|---|
| Milena Espinha | Lipocenter | empty profile, no company page (same ground as Renata Assuncao) |
| lisete espindola | Lipocenter | empty profile, no company page |
| Mônica Melli | Lipocenter | empty profile, no company page |
| Elaine Tadiello | Siluets | empty profile, no company page |
| Alejandro Gorissen | Atrys Brasil | empty profile on an AxisMed row (brand sold 2020), likely no page |
| Silvia Lima | Atrys Brasil | same |
| Carlos Coelho | RWE Telemedicina | "Executivo" only (same ground as Renan Schonton) |
| Meire Satelite | Siluets | "Empresaria" only (same ground as Tami Bianca) |
| Sandra Baldassari | Lipocenter | "Empresária" only (same) |
| Cristiane Aguilar | Lipocenter | "Proprietário" only (same ground as Regina Alves Ribeiro) |

Verify before keeping: Fabrícia Dias (N2B, re-grouped, probably the no-page N2B row). No WEAK should move to PASS.

## Top 3 issues (priority for improver)

1. The one-line line is inconsistent, and the agent deferred it. 21 `empty-profile` PASS rest on the company page, which the author prompt rejects as confirmation, while identical Magrass and Vidalink rows are WEAK. In a no-checkpoint run, the agent has to make this call itself, not list it as a concern.
2. The stated basis is false for at least 4 rows ("опора на сторінку компанії" where there is no page), and unit roles are written as fact.
3. The summary has no frontmatter (`product:` missing), a regression from every earlier icp-validator run.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

```
agreement: ✅ agree
top_issue: the PASS/WEAK line for one-line profiles depended on whether the card named the person, not on the evidence on the row; the validator now applies one rule to every empty-profile row (10 PASS → WEAK), fixes reasons that overstate the row, and adds the summary frontmatter.
```
