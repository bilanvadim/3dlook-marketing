# ICP Validation Summary: 2026-09-27-uk-bariatric-prequal

Product: **FitXpress** · profile: **katerina (UK)** · validated 2026-09-28.
Input: `people-raw.csv`, 348 rows (345 from the three Sales Navigator exports plus 3 Phoenix
Health people Vadim added on 2026-09-28). Every row was checked against its full profile in
`sales-nav-raw/export-{1,2,3}.csv`, including Experience and Bio.
Output: `people-validated.csv`, which keeps the identity columns `first_name`, `last_name`,
`linkedin_url` and `person_linkedin_url`. All 348 rows have them filled.

Decision values: `PASS` (goes to message-sequencer), `WEAK` (needs Vadim's call),
`RESERVE` (fits, but the company is already over its cap; importer skips it because it is not PASS), `FAIL`.

## Stats

- Total reviewed: **348**
- PASS: **48** (priority 1: **18**, priority 2: **15**, priority 3: **15**). Persona: P1 44, P2 4, P3 0
- WEAK: **21**. These are for Vadim to review by hand
- RESERVE: **28**. They fit, but the company cap is reached (Spire 16, Circle 11, Practice Plus 1)
- FAIL: **251**
- Excluded by registry: **0**. `outbound-registry.py check` flagged 2 rows as `company already
  worked from katerina` (Rishi Singhal / Healthier Weight, Sandip Hindocha / Tonic). Under Vadim's
  decision 5, new people at these companies are allowed. Neither of them is one of the four
  permanently excluded people (Davies, Berrett, Franklin, Chadwick). So they were scored on
  ICP and not auto-failed. The flag is kept in the `exclusion_flag` / `exclusion_reason` columns.

### FAIL reasons

| Reason | N |
|---|---|
| Consultant in another specialty (ortho, urology, ENT, plastic, gynae, ophthalmology, cardiology, etc.) with no role in the weight-loss line | 145 |
| Excluded function or level: nurses/ward/theatre, dietitians, HR/TA, finance, marketing, procurement, governance, pharmacy, diagnostics, GP, students, investors, secretaries | 90 |
| `[No shortlisted company found in experience]`: no link to the shortlist in the full profile (1 of 12 went to WEAK, see below) | 11 |
| False `Streamline` match (Egypt, Saudi Arabia/Kabbani, Moldova, Angola) | 4 |
| Duplicate LinkedIn profile (Barrie Crabtree, second account) | 1 |

A note on the 12 `[No shortlisted company]` rows. The full profiles show a formal link to a
group in 5 cases: Yashin Ramkissoon (Circle Thornbury), Apurv Sinha (BMI Thornbury = Circle),
Shabin Joshi (Ramsay Woodland), Tom Cooper (a past podiatry job at Circle), and Rogan Corbridge
("Executive Board Member at Circle"). The first four are in the wrong specialty or the link is
in the past, so they are FAIL. Corbridge is **WEAK**: he is an ENT surgeon, but the Circle board
seat could be a group-level role. The other 7 have no link at all.

## Company breakdown

| Company | Flavour | PASS | P1/P2/P3 prio | WEAK | RESERVE | FAIL |
|---|---|---|---|---|---|---|
| Spire Healthcare | 3 | 8 | 2/4/2 | 3 | 16 | 80 |
| HCA Healthcare UK | 3 | 8 | 2/4/2 | 2 | 0 | 40 |
| Circle Health Group | 3 | 8 | 3/1/4 | 3 | 11 | 24 |
| Ramsay Health Care UK | 3 | 6 | 1/0/5 | 0 | 0 | 6 |
| Practice Plus Group | 3 | 5 | 1/3/1 | 4 | 1 | 13 |
| Cleveland Clinic London | 3 | 4 | 3/1/0 | 1 | 0 | 22 |
| National Obesity Surgery Centre | 1 | 2 | 2/0/0 | 0 | 0 | 1 |
| Streamline Surgical | 1 | 2 | 2/0/0 | 1 | 0 | 14 |
| Phoenix Health (returned by Vadim on 09-28) | 1 | 2 | 1/1/0 | 0 | 0 | 1 |
| Healthier Weight (re-entry, decision 5) | 1 | 1 | 1/0/0 | 0 | 0 | 0 |
| Nuffield Health | 3 | 1 | 0/1/0 | 0 | 0 | 6 |
| The Hospital Group (Transform) | 1/3 | 1 | 0/0/1 | 3 | 0 | 8 |
| The London Clinic | 3 | **0** | none | 2 | 0 | 25 |
| Tonic Weight Loss Surgery (re-entry) | 1 | **0** | none | 1 | 0 | 0 |
| The Bariatric Group | 1 | no people in the export | none | none | none | none |
| Other (primary employers without a link) | none | 0 | none | 1 | 0 | 10 |

**12 companies have at least 1 PASS.** That meets the floor of 12 exactly. It counts Phoenix and
Healthier Weight, and it counts Transform through a single priority-3 contact. See concern 1.

Caps: 8 per large group (Spire, Circle, HCA), fewer where the export had fewer good people. In
Spire and Circle, the next best candidates went to RESERVE: site Hospital Directors and
Directors of Clinical Services.

## Top 15 (send first)

1. **Danny Brown, CEO, Phoenix Health.** Bariatric-only provider, ex Bupa ops. Angle: consult-slots (private stream).
2. **Rishi Singhal, Medical Director, Healthier Weight.** Bariatric surgeon. Angle: glp1-bmi-history.
3. **Gavin Quinton, Managing Director, Streamline Surgical.** Angle: pmi-preauth-pack (Vitality partnership).
4. **Shaw Somers, Surgeon-Director (co-founder), Streamline Surgical.** Angle: glp1-bmi-history.
5. **Barrie Crabtree, General/Managing Director, NOSC.** Network operator across 17 hospitals. Angle: consult-slots.
6. **Christine Morley, Director, NOSC.** Angle: consult-slots.
7. **Dr Kathryn Oakland, Medical Director – Clinical Service Lines, HCA UK.** Owns the surgery service line.
8. **Richard Cohen, Medical Director / Chief of Surgery / Vice Chief Digestive Disease, Cleveland Clinic London.**
9. **Tim Wigmore, Medical Director (Commercial), Cleveland Clinic London.**
10. **Fiona Taylor, Director of Operational Efficiency, Divisional Director South, Spire.**
11. **Prof Lisa Grant, Group CNO & COO, Spire.**
12. **Debbie Craven, Operations Director NE & NW, Ramsay.**
13. **Charles Ranaboldo, Medical Director, Practice Plus** (ex Group MD Ramsay).
14. **Cliff Bucknall, Chief Medical Officer, HCA UK.**
15. **Paul Manning, CEO, Circle Health Group.**

The other priority-1 contacts are Beri Ridgeway (President, CCL), Sam Lock (National Director,
Circle) and Dan Fagan (Clinical Chairman, Circle).

## Top concerns

1. **The pool rests on hospital groups.** Flavour 1-2 accounts give 8 PASS in total (NOSC 2,
   Streamline 2, Phoenix 2, Healthier Weight 1, Transform 1 at priority 3). The other 40 are
   from flavour 3. The hypothesis itself expects slow enterprise cycles from these, and most of
   those contacts are site directors, not owners of the bariatric line. The Bariatric Group
   has no people in the export, and The London Clinic has no suitable contact.
2. **Optimise Weight Loss Surgery is a new flavour-1 account that is not on the list.** Greg
   Jones (in the file under Spire) and Marianne Sampson (under Circle) are both founding
   partners of Optimise Weight Loss Surgery / Thames Valley General Surgery. They are PASS at
   priority 2 in the persona "bariatric surgeon, founder/partner". Their messages should
   address them as Optimise, not as Spire/Circle employees. Also send to only one of the two
   first. Step 2 did not check this company.
3. **Phoenix Health.** Vadim returned it as a target on 09-28 (3 people: CEO PASS p1,
   Non-Clinical Director PASS p2, Director of Finance FAIL for finance). The NHS anti-case still
   applies to the message: the angle is only the private self-pay stream. Because Phoenix is
   back, Qutayba Almerie (bariatric surgeon, Programme Director of the bariatric fellowship at
   Phoenix) moved from WEAK to PASS p3. He is in the file under Circle.
4. **Hospital Directors and Directors of Clinical Services.** We don't know which Spire,
   Circle and Ramsay sites actually run bariatric surgery. The exceptions are Nuffield
   Guildford (evidence from step 2) and, indirectly, Spire Manchester and Parkway through the
   surgeons. Site-level PASS contacts are therefore priority 3. If Vadim wants to narrow these,
   he can keep only sites with a confirmed weight-loss service.
5. **Registry override.** `people-checked.csv` marks 2 people as EXCLUDE (`company already
   worked from katerina`). I did not FAIL them, because of decision 5. The importer or another
   check may block them on this flag. Vadim should confirm that this is intended.

## Sample of decisions

### PASS examples
1. **Danny Brown, CEO, Phoenix Health** → p1. Owner/operator of a provider that does only bariatric surgery. Angle: consult-slots.
2. **Kate Farrow, VP Network Optimisation, HCA UK** → p2. Owns network capacity and utilisation, so consult-slot waste is her metric.
3. **Grace P., Director of Development, HCA UK** → p2. Previously GI-surgery service manager at GSTT and a healthy-weight nutritionist.
4. **Tamara Gall, Clinical Director of General Surgery / Deputy MD, Practice Plus** → p2. Owns the surgical line where the sleeve operations sit.
5. **Martine Dempsey, Area Manager, Transform** → p3. Multi-clinic operations that include Transform Weight Loss intake, but under the cosmetic brand.

### FAIL examples
1. **Prof Ajay Mahajan, Consultant Plastic Surgeon, Spire.** Another specialty, no role in the weight-loss line.
2. **Victoria Jones, Director of Finance, Phoenix.** Finance is an excluded function.
3. **Edward Lunken / Tom Profumo, Streamline.** Investors (Perwyn, Active Partners) with no operational role.
4. **Nicole Alabaster, Lead Bariatric Dietitian, Streamline.** Dietitians are excluded by the hypothesis.
5. **"Streamline Trade & Marketing" (Egypt), Bilal Abbas (Kabbani, Saudi Arabia).** False substring match.

## WEAK: Vadim to decide (21)

The most arguable cases:
- **Sue Norton**: Head of Dietetics & Bariatric Patient Care / Head of Weight Management,
  Transform/Electiva. In practice she owns the bariatric pathway, but her title is dietitian.
- **Sandip Hindocha, Tonic**: his CMO title is at The Private Clinic. At Tonic he is a plastic surgeon (post-bariatric body contouring).
- **Bilal Alkhaffaf, Shaishav Dhage, Rajeev Parameswaran**: right specialty (bariatric/UGI/endocrinology with Oviva), but their leadership roles are in the NHS, not in the private group.
- **Julie Condon**: Interim Head of Pre-Assessment, Spire. This is exactly the intake step we target, but it is a site-level, nurse-lineage role.
- **Anthony Cartwright, Tahsin Zatman (Practice Plus)**: perioperative / pre-op assessment. Fits the baseline part of the story; they come after the pre-consult decision.
- **Dr Melanie Rendall**: Clinical Director of Psychological Services, Streamline. A clinical director at a flavour-1 provider, but psychologists are excluded.
- **Debashis Ghosh**: Divisional Director of Surgery, TLC. His division is breast/plastics/urology, not GI. He is the only senior contact at TLC.
- Also: Melanie Tan and Andrew Mikhail (P3 digital), Caroline Oleary and Kate Convery (Transform), Paula O'Brien (TLC), Paula Vrey (PPG), Sarah Ballis (HCA AHP), Jane Almond, Lorraine Kelly and Katrin Davis (Circle), Rogan Corbridge (Circle board).

## Recommendations (Sales Nav)

- For The London Clinic and Tonic, run a targeted search by name: TLC CEO/COO, the head of the GI/digestive division, and lead bariatric surgeon Ali Alhamdani; at Tonic, lead surgeon El-Hasani and an operations lead. For The Bariatric Group, pull partners and the practice manager.
- In hospital groups, the bariatric surgeons had to be found by hand. Next time search by keyword `bariatric OR "weight loss surgery"` in headline plus current company, and do not pull whole companies. About 70% of this export is consultants in other specialties.
- The substring match on `streamline/tonic/transform/hca` produces noise. Match on the company LinkedIn URL instead.

## Vadim, please confirm

1. **WEAK (21)**: include or exclude? My recommendation: include Sue Norton, Julie Condon and Bilal Alkhaffaf, drop the rest.
2. **RESERVE (28)**: keep them as a second wave for Spire and Circle, if the first 8 do not accept?
3. **Priority 3 (15, mostly site Hospital Directors)**: include them, or save Closely credits and send only p1-p2 (33)?
4. **Optimise Weight Loss Surgery (Greg Jones / Marianne Sampson)**: send as a new flavour-1 account without step-2 verification?
5. **Registry override** for Rishi Singhal (PASS) and Sandip Hindocha (WEAK): confirm this is per decision 5.

## Vadim's approval (2026-09-28)

Approved with changes: all 21 WEAK → PASS; finance + dietitian rows (5) FAIL → PASS; Optimise partners and the two `company_same_profile` rows (Singhal, Hindocha) confirmed; no extra pulls. Final: 74 PASS.
