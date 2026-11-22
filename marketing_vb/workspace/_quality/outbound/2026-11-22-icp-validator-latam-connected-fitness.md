---
qc_date: 2026-11-22
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 17/20
status: good
coordinator_review: pending
---

# QC Report — icp-validator — 2026-11-22 — latam-connected-fitness

**Artifact:** `workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/icp-validation-summary.md`, `.../decisions.md`
**Total: 17/20** — good

The list has 210 rows: PASS 160 (P1 19, P2 80, P3 21, P4 40), WEAK 17 and FAIL 33. I scored it against `card-validate.md`, `people-compact.csv` and the seven coordinator rulings.

**What I verified:**
- Every number in Stats and in the group table matches `decisions.md`: tier splits, the angle split 48/38/25/25/17/7, PASS/WEAK/FAIL and P1-P4 for each group, and the FAIL causes 17+9+5+1+1.
- All seven rulings are applied:
  - Central America is FAIL (Pizarro);
  - Sarasti and Cardenas pass, because they are Colombia-based;
  - SportClub and Bluefit one-club rows are P4;
  - BIGG Chile is P4;
  - the Cia Athletica English titles are P4;
  - Smart Fit stays under the cap at 45;
  - Face Doctor appears nowhere.
- The identity work is strong. The validator caught EVO and BIGG Desarrollos before the domains were fixed. It also caught:
  - Scarcella: the title says "Diretor regional", the headline says "Gerente Regional", so he is P4;
  - Antunes: the headline says CFO;
  - D'Elia: probably left;
  - Loaiza: regrouped;
  - Bottini: held.

**Weak spot:** rows with the same evidence got different verdicts, mostly among empty-profile executives.

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
- **The card's P1 rule is skipped at two chains, and no reason is given.** It says chain CEOs and founders get P1 "only where the export has no product or technical owner".
  - It was applied at six chains: Action Black, Pratique, Selfit, BIGG, Cia Athletica and Panobianco.
  - Academia Gaviões 24h has no such owner either; its only head-office people besides him are two P3 tech heads. Yet Leandro Aguiar (decisions 92) is P2.
  - Bodytech Colombia is the same; only Maldonado and Socarras, both P3. Yet Gigliola Aycardi (decisions 71) is P2.
  - Under the reading used at Action Black and BIGG, a CTO is not a "technical owner". By that reading both should be P1, or the reason should say why not (for example, the empty profile).
- **Duplicate-CEO FAILs go beyond the card's closed FAIL list.**
  - Vadim's standing decision 2 allows FAIL only for these reasons: wrong company, people who left, identity collisions, duplicates, location and function.
  - Bruno Rangel (Bodytech, decisions 94) and Vladimir Martins (Pratique, 78) are FAIL "duplicate/conflicting CEO claim".
  - The same evidence at Gaviões (Medeiros, Nawate) and Panobianco (Brasileiro) is WEAK "probably a franchisee". The card makes a franchisee P4 referral.
  - Bodytech franchises: Fagundes is its Diretor Executivo de Franquias.
  - Both men are under "Not offered as a pool" (summary line 252), so Vadim can add them only by name.
- **Facts from outside the two input files.**
  - Felipe Marcon's "(Jardim das Américas)" (decisions 63) is the `company_name` in `people-checked.csv` and `people-raw.csv`.
  - Mariano Patrone's "no company page" (decisions 56) is the empty `company_linkedin_url` there.
  - `people-compact.csv` carries neither. Either the validator opened a file the prompt excludes, or the coordinator's brief carried these facts; the summary does not say which. The facts are correct.
- **Done right:**
  - pools are in the first report;
  - registry handling is correct;
  - Apollo empty-profile rows are handled per ruling 2 (Fontarolli, Serville, Waltricke, Lati);
  - PPL-1 route-in gaps are named by chain;
  - card-rule P1s say so in the reason.

### B. Factual accuracy — 4/5
- **Four reasons claim a scope the rows do not show.** Karina Rocha, Tamiris Losso, Amanda Ferrari and Gabrielle Weiss (decisions 188, 193-195) all say "unit scope".
  - Their rows show no scope.
  - Losso and Ferrari carry the same headline as Elisangela Ornellas (P2): "Gerente de Operações na Bodytech Company".
  - The P4 verdict fits the "scope must be shown" rule, but the reason should say "scope not shown", as Tiago Serville's does (decisions 121).
- Summary line 248 lists Renato Salinas among "Directors with only 'Director' as title". His title is "Presidente".
- Summary line 16 counts three function FAILs as "empty or unverifiable": Loya (supply), Fiorella Godoy (customer service) and Ventura (new-unit rollout). The total is right; the category is wrong.
- Gigliola Aycardi's PASS rests on knowledge from outside the file ("on public record, co-founder"). The reason discloses this, and it matches public sources.
- Nothing is invented: no people, companies or numbers. All counts were re-tallied and match.

### C. Brand & tone — 3/3
- No issues. Em dashes appear only in template headings (summary lines 10, 219, 262) and in one empty table cell (line 47). `decisions.md` has none. No banned words.

### D. Format & structure — 3/3
- The frontmatter is complete: `product`, `profile`, `campaign`, `created`, `stage`, `status`.
- All six template sections are present, and SEND, WEAK and pools use the template tables.
- `decisions.md`: the pipe format is correct and FAIL reasons are 2-5 words.
- P4 is used because the card defines it. The prompt's "priority 1-3" is the known pipeline gap from the AU QC on 2026-11-20.

### E. Output quality — 3/4
- Usable after about 15-20 minutes of row fixes (see the table below).
- The Top concerns are strong:
  - name collisions;
  - five thin chains, named with counts;
  - SportClub is 9/11 referral;
  - product managers are concentrated at a few companies;
  - two stale profiles.
- The pools cover every senior role.
- Points off for two reasons:
  - same evidence, different verdicts among empty-profile executives (section 4 below);
  - Pool B's remedy does not reach its own FAIL members.

## Checks the coordinator asked for

### 1. P1 for chain CEOs and founders: card rule vs PPL-1
- The P1s follow the card. 12 of 19 P1s are founders, CEOs or a CPO:
  - six chain executives, under the no-owner rule;
  - six group B founders, CEOs or CPOs, under the group B rule.
- The card says its rules beat the learnings, so this is not a deduction.
- "Technical owner" is read the same way throughout: a fitness technical director, not a CTO. That is why the CEOs at Bluefit, Bodytech Company and Allp Fit are P2, and those at Action Black and BIGG are P1.
- **Misses:**
  - Gaviões and Bodytech Colombia (see A).
  - Ruben Baquero (decisions 35) is P1 on his title alone. "Head office" is asserted, but his row has only "Director Fitness en Spinning Center Gym", with no earlier roles. The card's P1 needs "visible scope". Axel Mendoza, with the same title at Sport City, went to P4 on location.
- The summary does not report the C-level share of P1 (the validator's P1 tier historically replied 2/200). Tiers only set the order, so this costs little.

### 2. Regional managers: P2 vs P4
Consistent with the card:
- **P2 operations:**
  - Diretora Regional Meirelles, under the card's "regional directors" in the operations lane;
  - operations managers whose history shows a promotion above regional: Jefferson Cunha, Adriana Assunção, Elisangela Ornellas, Bruna Ramalho, Patricia Rocha.
- **P4:**
  - the regional manager Edson Santos (Bluefit);
  - Scarcella, on his headline;
  - operations managers with no scope shown: Isadora Melandes, Tiago Serville, and the four Bodytech rows.

The only flaw is the "unit scope" wording in B.

### 3. Partnerships lane for P4 staff at software platforms
- **Felipe Savioli** (P4 partnerships, decisions 171) follows the card's literal rule: "everyone at group B except technology owners".
- **Adriano Oliveira** (P4 technical-integration, decisions 173) departs from it. He is an infrastructure coordinator, not a technology owner, so the card puts him in partnerships. If he stays in the tech lane, the sequencer should know he is a referral-level ask.
- **Delcio Pinto** (P2 partnerships, decisions 174) is inconsistent with the rows around him:
  - his headline names a non-PM function ("Coordenador de Educação"), as Savioli's does, yet he stays at P2 while Savioli drops to P4;
  - he also ranks above Fitco's head of customer success (Andrea Ruiz, P3);
  - the card's P2 is "product managers and owners of the member app", and client education is neither.
- Card gap for the sequencer: P4 staff in the partnerships lane will get a "decides what the app offers gyms" pitch. Neither the card nor the summary marks them as referral-level asks.

### 4. WEAK vs FAIL among empty-profile senior titles

| Evidence | WEAK | FAIL | Consistent? |
|---|---|---|---|
| CEO/owner title, no verified CEO in the export | Trombini, F. Storchi, Casallas, Brasileiro, Medeiros, Nawate | Cotu Shega (Megatlon), Renato Salinas (Smart Fit Chile) | **No.** Cotu Shega's twin claim at Megatlon (Storchi) is WEAK, and her reason does not cite her headline. Salinas has the same evidence as Casallas; if the reason is a conflict with the CEO Cono Sur, it should say so. |
| CEO title next to a verified CEO | — | Rangel, Martins | **No.** These are likely franchisees, which the validator made WEAK at Gaviões and Panobianco. Neither is pooled. |
| Persona-function title | Villa Aguilar, Freire, Aguiar de Albuquerque | Fiorella Godoy (Bodytech Colombia) | **No.** Customer service is not a Not-the-buyer function, and the card puts customer-experience heads at P3 (Salvadori is P3). Her row has the same headline pattern as Villa Aguilar's, at the same chain, which is one of the thinnest. |
| Bare Director / Dirección / Directivo | Ardisson (CSO/CVO headline) | Amaya, Anaya, Campos, Mac, Cunha, Miguel, Palencia, vero al | Yes. The rule is: no function means FAIL. These are pooled in B. |
| Function on the Not-the-buyer list | — | Loya (supply), Ventura (rollout) | Yes. |
| Club GM on Sales Navigator | — | Castelar, Morgana Teixeira | Yes under ruling 2, but they are not pooled. |

**Pool B is internally inconsistent:**
- Its remedy says "accept an empty profile with a persona title as referral". Its 8 FAIL members carry bare Director or Presidente titles.
- Its 18 people include 10 who are already in the WEAK table.

## Per-person findings

| person_id | Now | Suggested | Why |
|---|---|---|---|
| `fiorella-godoy-a644792a9` | FAIL | WEAK (P3 CX, or referral) | See table 4. Thin chain, same evidence as `jorge-villa-aguilar-0129521ab`. |
| `bruno-rangel-b3147a3aa`, `vladimir-martins-309576266` | FAIL | WEAK referral, "likely franchise unit" | Same reasoning as `gustavo-medeiros-785897330`, `ana-carolina-nawate-aba079367`, `vilma-brasileiro-694677439`. |
| `cotu-shega-53280b100` | FAIL "second CEO claim" | WEAK, or a reason that cites the health-professional headline | `fernando-storchi-303121124` makes the same claim at the same company, and he is WEAK. |
| `renato-salinas-5a300a304` | FAIL "unverifiable" | WEAK, or a reason that names the conflict with `cristián-deppe-alcalde-9b934621` | Same evidence as `cesar-casallas-8178b07b` (WEAK). Also fix his "Director" label in Pool B. |
| `leandro-aguiar-a86b7039b` | P2 | P1 under the card rule, or state why not | Gaviões has no product or technical owner. |
| `gigliola-aycardi-batista-b1a5b21b6` | P2 | P1 under the card rule, or state the empty profile as the reason | Bodytech Colombia has no product or technical owner. |
| `ruben-baquero-48b325b3` | P1 | P2, or state the scope evidence | P1 on his title alone (PPL-1). "Head office" is not in the row. |
| `delcio-lu%c3%ads-pinto-04b4aa49` | P2 | P3 | Client education, not the member app; it ranks him above `andrea-ruiz-cs-kam` (P3). |
| `adriano-oliveira-cloud` | P4 technical-integration | P4 partnerships, or keep and flag for the sequencer | Under the card's group B rule he is not a "technology owner". |
| `karina-borba-rocha-580152220`, `tamiris-losso`, `amanda-ferrari-6b21251aa`, `gabrielle-weiss-86962b152` | P4 "unit scope" | P4 "scope not shown" | The verdict is right; the reason claims a scope the rows do not show. |

**Lower priority** (for the account-facts round):
- `diego-tavares-b117183a`: "Multiunidades & Franquias" can read as head-office franchise operations. Compare Fagundes (P2) and Aguiar de Albuquerque (WEAK as a franchise director). Ruling 4 may cover him; worth a look.
- `gigio-mazzoni-ba358797`: P1 with no headline. His earlier role, "Socio at Estudio Mazzoni y Asociados", follows the same professional-firm pattern that made Bottini WEAK on a page shared with BIGG Desarrollos. The coordinator's bigg.fit Apollo search could confirm him the way it confirmed Bottini.
- `diogoevangelista`: his title string is identical to his Triways Treinamentos role. The only Bodytech link is the Apollo domain match.

If the main table is applied, SEND stays at about 160 and WEAK grows by 5: Godoy, Rangel, Martins, Cotu Shega, Salinas.

## Pipeline finding (not scored)

Two judgments needed facts that `people-compact.csv` does not carry:
- `company_name`, when it differs from the group (a franchise unit name such as "Academia Bluefit Jardim das Américas");
- a missing company page.

Fix: `outbound_pack.py compact` should emit both, as `flags` (for example `unit-page:…`, `no-company-page`). Then the validator does not need to open `people-checked.csv`.

## Top 3 issues (priority for improver)

1. **Same evidence, different verdicts among empty-profile executives:**
   - Rangel and Martins are FAIL, while Medeiros, Nawate and Brasileiro are WEAK;
   - Cotu Shega is FAIL, while Storchi at the same company is WEAK;
   - Salinas is FAIL, while Casallas is WEAK;
   - Godoy is FAIL, while Villa Aguilar at the same chain is WEAK.

   Three of these FAILs (Rangel, Martins, Cotu Shega) are in no pool.
2. **The card's P1 rule is skipped at Gaviões (Leandro Aguiar) and Bodytech Colombia (Gigliola Aycardi), and no reason is given.** Ruben Baquero is P1 on his title alone, with "head office" not in the row.
3. **Pool B's remedy does not reach its own FAIL members:** the remedy says "persona title", but its 8 members have bare Director or Presidente titles. Its count of 18 double-lists 10 people already in the WEAK table.

Notify: not sent. This QC run had no shell, so the coordinator sends the notification.

## Coordinator review
agreement: ✅ agree (the off-input facts — Marcon's unit, Patrone's missing page — came from the coordinator's brief, not from excluded files)
top_issue: same evidence, different verdicts among empty-profile executives; the 5 FAILs QC names (Rangel, Martins, Cotu Shega, Salinas, Godoy) go to Vadim together with the 17 WEAK, not silently re-decided
