---
qc_date: 2026-10-05
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-10-05, latam-health-weightloss

**Artifact:** `workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/hypothesis.md`
**Total: 15/20** (good)

**Sources I scored against:**
- the hypothesis-generator prompt;
- icp-detail.md §1, §4, §5, the Geo lines, and :597 (2-4 weeks);
- proof-points.md and accuracy-formulations.md §1.1, §1.2 and §1.4;
- compliance.md §1, §7 and §10;
- audience.md §1 and §4;
- use-cases/fx-wellness-rewards.md ("Biometric screening angle") and use-cases/fx-telehealth-weight-loss.md;
- `scripts/outbound_pack.py` (`OWNER`, `calendar_link`, `CARD_SECTIONS` at :729-737, `build_card`);
- the Israel `metrics-final.json` and `post-mortem.md`;
- `sales-nav-raw/export-1.csv`, by targeted search of the rows behind the hooks and verdicts I checked;
- the 2026-10-02 Virta QC report, for calibration.

**What reaches the message writer:** the messages card carries:
- `Use case`;
- `Message angle`, which includes the fact table and the per-person table;
- `Rules for steps 3-5`;
- both `decisions` sections.

The validate card carries the persona, the verdict table, the anti-cases, the decisions and the open questions. "Read this first" and "Why this is plausible" reach neither card.

**Taken as given:**
- Vadim's standing decisions and the defaults he left: English copy, no compliance line, no LGPD claim.
- Limits, bans, the detector and completeness.

**Limits of this QC:**
- This session has no web tool. I did not re-fetch Agência Gov, Olhar Digital, Vitat, the franchise listings or the App Store pages. Source fidelity is judged on the artifact's own quotes, the URLs and the export.
- This session has no shell, so notify.py was not run.

**Verified clean:**
- **Counts:** 84 + 3 + 34 + 89 + 1 = 211. Tiers 15/5/14/50 = 84, with 84 rows in the per-person table. The per-account sends add up (Vidalink 18, Nilo 13, Liti 8).
- **Israel metrics** match `metrics-final.json` and `post-mortem.md` exactly: 38/127, 29.9%, 4/73, 15.4%, 2.3%, 432 messages, 6 of 18.
- **Sender:** `OWNER["katya"]` is "Kateryna", and the calendar link resolves through `calendar_link`.
- **icp-detail.md quotes:** the §1 phrases are real, and no segment lists South America.
- **Compliance:** the medical-device sentence (line 202) is verbatim from compliance.md §1. The eligibility answer (line 203) matches §7.
- **Client names:** none appear anywhere. The 34,000 and 112,100 lines are worded as cleared.
- **Copy numbers:** every number in the Rules comes from proof-points.md, plus 2-4 weeks for the technical lane.
- **Hooks checked against the export:** Rappi, Betterfly, Mercado Livre, GrowthHackers, will bank, Geekie, SiLex and Rabbot. Also Hospital Samaritano, the "Strategic Advisor at Nilo Saúde" headline, "Vidalinker" and "Gerente de Implantação". All are on the rows.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 4/5
- **The 2026-10-02 card-leak lesson is declared applied but is only half applied.** Line 142 says "Instructions below are written as instructions". The fact table that copy may use (lines 276-291) still carries about eleven instruction parentheticals inside the fact strings:
  - VL2 "(never '100%')";
  - OM2 "(never cite eating disorders)";
  - GS3 and AX2 "(the year only as a year)";
  - LT2 "(never 'visceral')";
  - LT4 "(release 4.56.0, 2026-10-02; never name the drug or the pharma partner)";
  - MG3 "(name only; never its formula)";
  - EM2 "(paraphrase; never quote figures)";
  - EM3, GL1 and AM1.

  None of these phrases is gated. This is the same pattern that leaked last week: a qualifier sitting next to a fact.
- **Alessi Soncini (line 322) has no company fact.** Line 297 requires one company fact in every Message 1.
- **The corporate-health boundary (line 260) is presented as taken "from fx-wellness-rewards.md", but it changes the source in two ways:**
  - it drops A1c;
  - it drops the source's "the copy must say so", leaving it unclear whether the copy states the boundary.

### B. Factual accuracy: 3/5
- **The Vidalink CEO's hook misstates his own bio (line 301).**
  - The hook says "co-founded BCG's São Paulo office".
  - His export row (csv :101) says "I helped establish BCG's first office in Brazil".
  - "Helped establish" became "co-founded", and a city was added that the row does not give. A Message 1 to a P1 CEO would tell him something about himself that he did not write.
- **"No franchisor executive is in the export" (lines 28 and 209) is stated as fact, but one row is unresolved.**
  - Gabriela Biazus's row (csv :892) reads "Sócia-fundadora at Magrass". It names no unit and has no company page. Every other franchisee row names its unit.
  - The validator check (line 189) is framed only as "confirm she owns a unit". There is no branch for the other reading, unlike the Emagrecentro rule at line 191.
  - The same assumption runs through the HELD accounts. Lines 80-81 say "every row is a unit owner". Two rows are ambiguous:
    - Flaminio Dalul (csv :585): "Sócio proprietário at Siluets Franchising", with no unit named;
    - aline caio (csv :1109): "Diretor" on the Lipocenter franchisor page.
  - Open question 5 therefore reaches Vadim with a premise that has not been checked.
- **The displacement search is overstated.** Lines 27 and 121 say "a search of each IN account's site". Three sites could not be read on the day: gesmed.com.br and atrys.com.br did not resolve, and emagrecentro.com.br returned 403.
- **Instituto Lumiere (line 85) is OUT partly because it "already offers tetrapolar bioimpedance".**
  - Line 427 says measuring by another route is overlap, and overlap stays IN.
  - The single-site rule (line 430) requires "no app of their own", but the verdict says Lumiere has a nutrition plan in an app.
  - The verdict therefore rests on a reason the artifact itself rejects. It affects 1 person.
- **The GLP-1 market claims are sourced but slightly stretched.** They are context only and reach no card.
  - **Olhar Digital (line 129):** the URL slug says EMS "announces prices" of the first national semaglutide pen. The artifact says it "reached pharmacies in June 2026", which the slug does not support. I could not open the article to confirm it.
  - **"Brazil's GLP-1 market opened in 2026" (line 26)** does not fit the artifact's own figures. 25 pens are registered and only 14 of them in 2026, so 11 came earlier. Liraglutide generics are already in `banned_terms` (Olire, Biomm).
  - **Faithful on the focus items:** the Conitec request (September 2026, agrees with the URL), the 70% price fall and the 25/14 pens all cite the one Agência Gov page. The Vidalink "primeiro benefício corporativo focado em canetas emagrecedoras" is quoted and attributed as Vidalink's own claim (VL1).
- **The overlap evidence itself is properly sourced and hedged:**
  - Liti: App Store quote, Bloomberg Línea 2023, Vitat 2023/2024, with "still part in 2026" marked not verified;
  - Magrass Club: franchise listing 09/2026;
  - Emagrecentro: PMC9332815, App Store, Portal do Franchising.
- **Sourcing:** about 40 external URLs, mostly primary: company sites, App Store listings, a government news agency, PMC and trade press. The Lancet Commission line is reused from another campaign's verification, and the artifact says so.

### C. Brand & tone: 2/3
- **Line 252 (messages card) says Liti's "kit has included a tape measure".** `tape measure` is in this file's own `banned_terms`. The line is context the sequencer reads, and it invites the word into Liti copy.
- **LT2 (line 284), a fact copy may use, contains `visceral`**, also a banned term, inside its parenthetical.
- Otherwise clean. Apart from the template-mandated H1, there are no em or en dashes. There are no banned words. The wording is person-first ("people living with obesity").

### D. Format & structure: 3/3
- No issues.
- The frontmatter is complete: `product`, `profile`, `market`, `created`, `status`, `use_case`, `cap_per_group` and `banned_terms`. The path is correct.
- Every template section is present, the titles block has one title per line, and the Message 1 gate is kept.

### E. Output quality: 3/4
- **The per-person table breaks the artifact's own Vidalink and employer rules.** Lines 255 and 410 say never connect the scan to the prescription, the audit or the balance, and never route body data toward HR. The sequencer gets the per-person question verbatim, and it will follow that over a general rule.
  - **Line 301, Luis Gonzalez (CEO, P1):** "Does a phone body record belong inside Peso Saudável, next to the prescription the employee already validates in the app?" A body record next to a pen-benefit prescription reads as BMI verification for the benefit. That is eligibility drift, which the artifact names as Risk 4 (line 493) and audience.md §1 forbids.
  - **VL1 and VL2:** VL1 itself contains the balance and the prescription validation. It is the Message 1 fact for Luis Gonzalez, Karen Ribeiro and Alessandro Dourado da Silva. VL2, the AI prescription audit, is the fact for Jorge Sousa and Aline Dos Santos. Line 303 adds "without touching the prescription check", which still ties the scan to the check.
  - **Line 307, Daniela Junqueira:** she is paired with VL5 (HR's real-time data) and asked how scan outputs "fit the data platform behind Vidalink's real-time reporting". That routes body data toward HR reporting.
  - **Line 320, Fernanda Maluf:** she is paired with OM3 (the Corporate Portal for HR) and asked "which physical-health indicators does [a company] ask for first?" That frames the employer as the one asking for body data.
- **Overlap leaks into implied lack, which line 408 forbids.**
  - **Line 355, Fernando Vilela (Liti, P1):** "a guided phone capture with circumferences and a 3D model ... alongside the scale readings the health team already gets". This is the banned pattern of listing their data and then adding ours. It also presents circumferences as new to Liti, while the artifact's own evidence (Vitat) says the kit carried a tape measure and the app shows "o progresso das suas medidas".
  - **Line 252:** the Liti card line foregrounds "waist and hip included", against its own next sentence.
  - **Lines 114 and 253:** Magrass is pitched as "done the same way in every unit". That implies units measure differently today, while the same lines say "never question how units measure". Unlike Emagrecentro (EM2), no Magrass source makes that point.
  - **Line 327, Thiara:** her question presupposes that AppGES records body measurements, which line 117 marks as not verified.
- **Line 386 declares all 14 Magrass rows one peer group, yet two pairs of asks repeat each other:**
  - Rafaela Klein (line 377) and Gabriela Biazus (line 383), both nutritionists, both asking for HQ's nutrition lead;
  - Fabricio Pires (line 375) "technology partnerships" and Renata Assuncao (line 384) "innovation projects".
- **"As a general resource" appears three times (lines 390-392).** It is ungated instruction wording that can be pasted into copy.
- **Strong otherwise:**
  - all 211 rows accounted for;
  - aliases tested against the raw cells, and name collisions failed by name;
  - the Luciana Ito ex-Vidalink trap caught;
  - Sírio-Libanês kept off Ribeiro's hook so he does not share one with Martins;
  - honest limits (no LatAm proof, US/EU training data, no bioimpedance comparison);
  - metrics sized for a language barrier.

## Top 3 issues (priority for improver)

1. **Lines 301, 303, 307 and 320 contradict lines 255 and 410 in the card the sequencer follows:**
   - the Vidalink CEO's question puts the scan "next to the prescription";
   - VL1 and VL2 carry the prescription, balance and audit into five Message 1s;
   - two questions route body data toward HR reporting or the HR portal.
2. **Overlap turns into implied lack:**
   - Fernando Vilela's question (line 355) lists Liti's scale readings and then adds circumferences;
   - the Liti card line foregrounds waist and hip (line 252);
   - Magrass is pitched as "the same way in every unit" (lines 114 and 253).
3. **Facts and franchise reads that do not hold up:**
   - the CEO's BCG hook is misquoted (line 301);
   - "No franchisor executive is in the export" (lines 28 and 209) is asserted while Gabriela Biazus's "Sócia-fundadora at Magrass" row is unresolved, and the validator has no branch for it;
   - the same unit-owner assumption is applied to ambiguous Siluets and Lipocenter franchisor-page rows;
   - about eleven instruction parentheticals remain inside fact strings, the leak vector from 2026-10-02.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the Vidalink lane put the scan next to the pen prescription (eligibility risk) and eleven fact strings carried paste-able instruction wording; all 21 fixes go back to hypothesis-generator together with Vadim's 2026-10-05 widening ("всі крім шуму").
```
