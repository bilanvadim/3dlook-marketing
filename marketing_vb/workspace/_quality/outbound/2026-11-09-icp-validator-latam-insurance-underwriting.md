---
qc_date: 2026-11-09
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/icp-validation-summary.md; workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: katya
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report — icp-validator — 2026-11-09

**Artifact:** `icp-validation-summary.md` + `decisions.md` (478 rows in two batches: BBVA 247, the rest 231)
**Scored against:** `card-validate.md` and `people-compact.csv`. I read all 478 decisions and checked every non-BBVA row against the compact file, along with every BBVA row that has an insurance word. Limits, completeness and cap are taken from code as fact.
**Total: 14/20**, marginal. The counts reconcile, and the line, location and duplicate rules hold. Three defects pull the score down:
- The two batches read the card's "life scope must be visible" rule differently. Three of the four BBVA PASSes rest on the looser reading.
- The coordinator's note behind WEAK recommendation 2 is false against the compact file.
- Several pairs of people inside the rest batch have the same evidence but different decisions.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What held up (checked, no action)

- **Counts reconcile.** The totals are 70 / 21 / 387 and P1/P2/P3 is 8/24/38. I recounted the angles from decisions.md: 26+18+9+8+8+1 = 70. I checked the group rows for Azos, Icatu, Bradesco (9 WEAK), RGA, both Swiss Re rows, Hannover Re, SCOR, Brasilseg and Banorte.
- **Line rules hold.** All of these FAIL:
  - health: :259, :288, :361, :398
  - Auto/RE: :284, :328, :452, :453
  - reinsurer P&C: :270, :330
  - Daños: :275, :381, :384
  - pensions: :336, :443
  - fleet, agro and marine: :290, :462, :320, :292
  - claims :387, fraud :366, CRO team :427
- **Location.** Four Brazil-located people sit in Mexico reinsurer rows and FAIL: Passos :309, Zimmer :315, Caproni :357, Souza Rocha :419. Madrigal :417 also FAILs. That matches the summary's 5.
- **Tech deputies FAIL when their chief is in the export:** Kojima :276, Arias :365, Gonçalves :340, Gargiulo :283, Vieyra :267, Pineda :359, Méndez :311.
- **PPL-1 route-in.** These accounts have a P2 below C-level: BBVA (Nacul), Icatu (Saile, Ietto + 5), MAPFRE (Gonzalez Mendez), MAG (Figueiredo, Cunha), Azos (Reis, Bobis…), Swiss Re Mexico (Antonio F, Fentanez), Hannover Re (Urbano), AXA (Tapia) and Allianz (Rossini Ruz). Bradesco, Banorte, Brasilseg, SCOR and RGA have no P2. Their candidates are WEAK, and the summary names the gaps (l.170). Handled correctly.
- **Good calls:**
  - Morita gets P1 on "Life" in his headline, not on his title (:265).
  - Gonzalez Mendez passes with the headline as his second confirmation (:472).
  - The two Jose Loureiro profiles are split (:266 / :325).
  - Moncada and Rodriguez Venegas go to pool H rather than being dropped.
- **The summary is open about its weak spots:** the seniority-pull diagnosis, the HSBC 0 row, the tech share and the implied-scope concern.

## What was wrong (specific)

### A. Adherence — 3/5
- **The two batches apply the card's life-scope rule differently.** The card says "A bare product title at a multi-line insurer returns auto, home and health owners; life scope must be visible". It puts heads of product without life scope at P3, and its P2 actuarial seat needs life scope.
  - BBVA batch: Liliana R. (:36, "Directora de Producto de Seguros y Función Actuarial", no line shown) is PASS P2. Felipe Orozco (:185, Director Técnico, line not named) is PASS P2 `underwriting`.
  - Rest batch, same kind of evidence:
    - Juan Ortiz Perez (:473, MAPFRE Director Actuarial): WEAK
    - Abelardo Filho (:459, Bradesco Superintendente Técnico): WEAK
    - Francisco Cerdeira (:424, Banorte Gerente Actuarial): FAIL
    - Almeida Braga (:386, Icatu Diretor de Produtos, no line): P3
  - The summary flags Liliana and Felipe (l.173) but leaves them at P2.
- **Data owners outside the card's `technical-integration` list.** The card's lane covers CTOs, architects, CISOs, DPOs and digital-channel tech owners. Its pre-filter drops "IT staff other than CTO, CISO and data protection titles".
  - Javier Camacho (:201, data-operations subdirector) passes P3 in the BBVA batch. Emmanuel Hinojosa (:413, "Subdirector de datos", AXA) FAILs in the rest batch.
  - Five more data or engineering heads pass with no departure stated: Lissandre :264, Oliva Carneiro :282, Alejandro D. :281, Raul Lobo :370, Luan Noé :303.
  - That makes 18 of 70 in `technical-integration`, against PPL-3 (engineering replied 1/90).
- **Standing decision 4 ("company-named profiles are held for Vadim") is overridden, and nothing says so.** These are FAIL: `swiss-re-58142234` :269, `filial-brasilia-048523254` :402, `bbf-asociados-0496181b3` :404, `mais-proteção-consultoria-e-corretora-de-seguros-6a35a02b7` :410, `all-music-produções-bb76b6335` :416, `inde-consultores-de-riesgo-2b174b337` :418. The cost is small, but it is Vadim's rule, and ruling 8 should have stated the departure.
- **Wrong lane for Marco Giorgetti (:322).** He is MAG's executive operations director, passed as the COO fallback, and sits in `underwriting`. The card's underwriting lane covers underwriting and acceptance heads and managers, so he would get the underwriting Message 2 with the 3.5% line. The fallback itself is also arguable: the card allows it "where no underwriting owner is found", and MAG's chief actuary (:446) used to head underwriting risk.
- **Location counts are missing.** The card asks for counts of US, Spain and other-country FAILs. The summary implies zero but doesn't state it.

### B. Factual accuracy — 3/5
- **Summary l.126 is false against the input.** It says "every Apollo row carries this flag". In people-compact.csv only 6 of the 58 Apollo rows (:422-479) carry `empty-profile`: :423 Granados, :428 Sosa, :450 Gliosci, :472 Gonzalez Mendez, :474 Imuro, :478 Ponce De Leon. For these six, the flag means Apollo returned a single role, which is the same weak signal as an empty Sales Navigator profile. WEAK recommendation 2 (l.178) rests on this premise.
- **Recommendation 2 goes beyond the decisions it summarises:**
  - **Julio Ponce De Leon:** the summary says "the row is its Mexico L&H office → P2". Decisions :478 says "line not shown (P&C or L&H)", and nothing in the card says the Hannover Re Mexico row is L&H only.
  - **Claudia Rodríguez Gomez:** the summary recommends P1 reinsurance. Decisions :383 says "P&C staff would FAIL", and "Director Suscripción" names no line either.
  - **Juan Ortiz Perez:** the summary recommends P2 proposition. Decisions :473 says life scope is not shown at a multi-line insurer, and the card's P2 actuarial seat requires it.
- **Felipe Orozco's reason (:185) cites "an earlier insurer role (Aseguradora Interacciones)" as support.** Compact :328 shows that role was Director Comercial, a sales role the card excludes.
- The stats, group table and pools match decisions.md. There are no product claims or proof-point numbers in scope.

### C. Brand & tone — 3/3
- No issues. Each reason is one specific sentence, with no banned words. The em dashes are in template headings (l.10, 124, 175) and in "WEAK — recommended" (l.178), all in an internal document.

### D. Format & structure — 2/3
- The frontmatter is complete: product, profile, campaign, created, stage, status.
- **Six SEND rows break the table.** Their titles contain an unescaped `|`, which shifts the P and Angle columns: Denis Nesi l.80, Marcela Gueiros l.90, Pier Ietto l.91, Humberto Sardenberg l.98, Alejandro D. l.110, Eduardo Gutierrez Rojo l.118.
- WEAK rows in decisions.md differ by batch. The BBVA batch fills in angle and wave (:34, :103); the rest batch leaves them blank.

### E. Output quality — 3/4
- The pools, the gaps by account and the four questions are ready to use as written.
- The rest is not ready as-is. Vadim would have to re-judge about 10 rows that the batches decided differently. Three of them are on the SEND list at BBVA, where Sandra Nacul is the only clean pass.
- Splits on the same evidence inside the rest batch:
  - **Icatu actuarial.** Ligia Abreu (:434, Superintendente Executiva Atuarial, no line) is PASS P2. Leonardo Hijino (:433, Gerente Atuarial, no line, same company) is FAIL. Pool E (l.162) proposes to "accept company-wide actuarial at Icatu", which is the basis Ligia has already passed on.
  - **Ney Ferraz Dias (:274) is WEAK.** His own reason allows two readings, Auto/RE CEO or group multi-line CEO. Under the rule the batch applied to Folch :376, Bernat :382 and Miguel Angel C. :380, both readings mean FAIL.
  - **Victor Reis (:464, Coordenador de Subscrição) is P2.** Every other coordinator is P3: Jimmy Monte :435, Beatriz Helena :430, Dayana Mello :444.
  - **César Saut vs Jose de Medeiros.** Saut (:421, empty profile, VP corporativo) is WEAK. Jose de Medeiros Carvalho Filho (:379, empty profile, Diretor Executivo, same company) is FAIL.
  - **Caraco Dudemaine vs Correa.** Daniel Caraco Dudemaine (:360, Director, previously ran AXA's transformation office) is FAIL. Eduardo Correa (:286, Executive Director, previously in products) is WEAK.
- **Borderline P2 route-ins:**
  - Alexandra Rossini Ruz (:333) covers reinsurance, underwriting governance and global programs at multi-line Allianz, with no life line. Held to the standard applied to Abelardo, she would be WEAK.
  - Tonantzin Tapia (:471) works on reserves, not pricing or the application.

## Top 3 issues (priority for improver)

1. **The two batches judged implied scope differently.** The BBVA batch passed Liliana R. (`liliana-r-1052a38`, P2), Felipe Orozco (`felipe-orozco-8287b5142`, P2) and Javier Camacho (`javier-camacho-237241158`, P3 tech). On the same kind of evidence, the rest batch held `juanorp` and `abelardo-filho-39486487` WEAK and failed `francisco-cerdeira-mora-1766a3116` and `emmanuel-hinojosa-aguilar`. Fix: when two batches run, the coordinator should reconcile scope-dependent calls across them before writing the summary. The shared rulings covered bank staff but not "insurer-wide scope with no line" or "data owner".
2. **The coordinator's note and WEAK recommendation 2 misstate the evidence.** The note says every Apollo row carries `empty-profile`; in fact 6 of 58 do. The recommendation also assigns P1 or P2 that decisions.md does not support: `julio-ponce-de-leon-9907a3126` (no L&H evidence), `claudia-rodríguez-gomez-5a6253162` (P1 with no line shown), `juanorp` (P2 with no life scope).
3. **Same title, different decision inside the rest batch:**
   - `l%c3%adgia-abreu-6871b9147` is PASS P2 and `leonardohijino` is FAIL.
   - `ney-ferraz-dias` is WEAK, while `eduard-folch`, `javier-bernat-a16397162` and `miguel-angel-c-3a0a49195` are FAIL.
   - `victor-ribeiro-reis` is P2, while `jimmymonte` and the other coordinators are P3.
   - Separately, six company-named profiles (`swiss-re-58142234`, `filial-brasilia-048523254` and four more) are FAIL although standing decision 4 says they are held for Vadim.

## Coordinator review

```
agreement: ✅ agree
top_issue: the two parallel batches had no shared ruling for "insurer-wide scope with no line" and "data owner", so BBVA passed on evidence the rest batch held; my own summary note on Apollo empty-profile was false (6 of 58, not all) and recommendation 2 assigned tiers decisions.md did not support.
```

Fixes applied by the coordinator the same day, without a second QC: 19 rows reconciled to one ruling each (marked "(QC reconciliation 2026-11-09)" in decisions.md; v1 list kept), the Apollo note and recommendation 2 rewritten (two takes, the rest only after a web check of the line), the SEND/WEAK tables rebuilt with `|` stripped from titles, location counts stated (US 0, Spain 0, other 0). Result: PASS 70 → 62, WEAK 21 → 34, FAIL 387 → 382; technical-integration 18 → 11. Lesson for two-batch runs: give both batches rulings for implied scope and data owners up front.
