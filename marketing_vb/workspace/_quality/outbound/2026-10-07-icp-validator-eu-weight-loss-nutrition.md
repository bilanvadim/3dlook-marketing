---
qc_date: 2026-10-07
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: olena
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-07

**Artifact:** `workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md`, `people-compact.csv` (245 rows: 171 export, 74 Apollo). Scope: "as many as possible", FAIL only for the card's reasons. Limits, signature, bans, detector and completeness were taken as fact from the code check.
**Total: 17/20** — good (approve after minor fixes)

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Nadia Battery** (decisions line 244) is P2 `operations` "by title". Her headline says "Responsable d'exploitation dernier échelon (vitrine du groupe)", which means front-line operations at two group-owned Paris clubs. The card's lane rule says "unit staff and anyone below lead level → `referral`", whatever the title. This is the one head-office/unit lane call that goes against the card.
- Lane deviations from the card's title map are explained row by row but not in the summary. Simon Aurik (CMO, line 234), Giulia Marinelli (VP Marketing, line 239) and Susanne Burger (line 198) went to `product` as "growth leads", although marketing is not on the card's `product` list. Barbara Vos (Product Manager, line 181) and Nathalie Dourdoigne (CEO, line 176) went to `referral`. All five can be defended. The 10-06 QC asked for exactly this kind of one-line note in the summary.
- An unstated reading of approval §10: three Apollo additions in Iceland (Saemundur Oddsson P1, Sigga Ingadottir, Hordur Bjarnason; lines 190, 196, 194) PASS, while §10 says "outside Continental Europe are OUT". Treating Iceland as in-market is the right call for an Icelandic account that the card routes to `olena`. The summary should still say so.
- Everything else follows the card:
  - The 13 fail-by-name rows and the 8 registry rows are FAIL with registry wording.
  - All 13 identity checks are resolved.
  - The CLP split (product 6, operations 4, referral 2, clinical 1) matches verdict row 5 exactly.
  - Frontmatter is present and pools come with a `promote` command.
  - No FAIL contradicts "as many as possible": every one of the 41 is a registry hit, a card name-fail, a real duplicate, junk, or a non-Continental-Europe Apollo row under §10.

### B. Factual accuracy — 3/5
- **Summary line 282 (and Stats line 17, "P4 = referral from franchise units"):** "110 of 194 are franchise-unit owners (RNPC 27, Dietplus 23, BODYHIT 20, fitbox 11)". The four networks add up to 81. Nine of the 110 `referral` rows are head-office staff below lead level: Celia Z., Shadi Marie Le Maout, Bas Harmsen, Fabrice G., Hordur Bjarnason, Hanna Blisnjuk, Silvia Ojeda Valenzuela, Antonia Schulz and Barbara Vos.
- **Damien Cacaret** (decisions line 173): "General Manager at RNPC head office in Paris" is P1. The compact gives only an Apollo title, a Paris location and investor/startup history (50 Partners, Autonomia). Nothing in it says "head office". The only founder row in the compact (Remy Legrand, Apollo) is in Marseille.
- **Pool A** (summary line 271) states "These are the account's own executives, not a local subsidiary" for all four people, and uses it to ask for a reading of §10. That holds for Ruben Visser (Virtuagym VP Finance & Ops history) and Taylor Ling (Fabulous co-founder). For Arnaud Souchon (Keepcool "Managing Director", Mauritius), the compact equally fits a local master franchise. This is the same "inference written as fact to argue an exception" that the 10-06 QC flagged (Cape Town). It is recurring.
- Every count was re-derived from `decisions.md` and it holds:
  - PASS 194 / WEAK 10 / FAIL 41.
  - Tiers 33/44/7/110.
  - Angles 110/57/14/6/5/2.
  - All 20 group totals.
  - FAIL breakdown 8+5+5+20+3.
  - All 41 FAILs are accounted for in the pools paragraph.
- The 5 Apollo duplicates are real: four share slug hashes with export rows, and Sophie Prunier has an identical Boehringer/MSD history.
- No proof-point numbers appear. "300+ clubs" and "50+ clinics" come from the card.

### C. Brand & tone — 3/3
- No issues. Internal artifact, no banned words. The only dashes are the template heading (line 290) and Damien Rollin's verbatim title (line 115).

### D. Format & structure — 3/3
- Frontmatter has `product: fitxpress`, `profile`, `campaign`, `created`, `stage` and `status`. This fixes the gap flagged on 10-05 and 10-06.
- All template sections are present, and the WEAK table adds a useful Angle column.
- `decisions.md` follows the `|` schema with wave 1. FAIL reasons are 2-5 words.
- P4 is used and disclosed (summary line 288).

### E. Output quality — 4/4
- The specific checks hold:
  - Brand-name collisions from Apollo are caught: Fabulous 6/6 FAIL (Nigeria, plastic surgeon, cake shop, company page, India, Malaysia), Nutrimed Argentina/Thailand FAIL, Metabolic Balance Australia ×2 and the Monaco restaurant FAIL. No PASS at those accounts relies on a collision.
  - Unit staff go to `referral` across RNPC, Dietplus, BODYHIT, fitbox, Naturhouse, NUTRIADAPT, Vivafit and 1:1 Diet.
  - Good calls against literal titles: Nathalie Dourdoigne ("CEO", headline "Coach personnel chez dietplus") → `referral`, and Clement Fave (president of his own Keep Cool franchise) → `referral`.
  - Rick Reinhard is held with a cross-check: Idstein's fitbox owner is Jan Sasse.
- The summary finds things nobody asked for:
  - Percent-encoded Apollo IDs that re-imported 4 export people, with a concrete code fix.
  - Greeting traps (Thierry Bernabe, "DIETPLUS la roche sur foron", malformed Isabel Barreto).
  - The card-vs-compact gap on Nanda Zwart's headline.
  - An honest admission that the Vivafit product/operations split is inferred by elimination, and that Thibaut Loriot may be a club.
- Small misses that do not cost a point:
  - **Virginie Bourgerie** (decisions line 141) is WEAK. The compact puts her current position on the BODYHIT page, with Body'minute only as an earlier role. The card header says "stay IN unless the check fails", and Dennis Krebs and Gunnar Mau PASS on a weaker version of the same evidence. The summary's "the card flags her headline" (line 256) does not mention that the compact has no headline. The agent did catch that same gap for Nanda. Under "as many as possible" this is PASS `referral`.
  - ludo glav's reason (lines 54, 254) argues "not among the three founders Apollo found". That count includes Julie Coudry, whom the agent itself holds as not tied to maju.
  - Sami B. is listed in SEND with the title "Incubated Startup" (summary line 238), and there is no note for the sequencer to use his headline "Co-founder and CEO at Fabulous".

## Top 3 issues (приоритет для improver)

1. **Unsupported claims written as fact, the second run in a row.** "RNPC head office in Paris" (Damien Cacaret, P1), "account's own executives, not a local subsidiary" (Pool A, used to argue a §10 reading), and "110 franchise-unit owners" (really 101; 9 are head-office staff). The prompt should require that a reason or concern says "inferred from title/location" when the compact does not state it.
2. **Head-office vs unit lane:** Nadia Battery (front-line operations at group-owned clubs) is `operations` P2. The card puts unit staff in `referral` regardless of title. Thibaut Loriot (empty Apollo profile, Annecy, "Direction générale") is the same risk and is already flagged.
3. **Over-hold and unstated readings:** Virginie Bourgerie is WEAK, but the compact shows her current position at BODYHIT and the card default is stay IN. The summary should also state the Iceland reading of §10 and the five title-map deviations in one line each.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

```
agreement: ✅ agree
top_issue: readings written as fact for the second campaign running (Cacaret "RNPC head office", Pool A "own executives", 110 vs 101 unit people), plus two lane calls against the card (Nadia Battery operations → referral, Virginie Bourgerie WEAK → PASS referral); sent back to the same icp-validator for a fix round before Vadim's checkpoint. Apollo percent-encoded duplicates it flagged are now normalised in extract-people and registry check (decoded comparison, person_id unchanged).
```
