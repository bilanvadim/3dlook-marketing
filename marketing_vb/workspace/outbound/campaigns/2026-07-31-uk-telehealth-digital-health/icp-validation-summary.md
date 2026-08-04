---
product: fitxpress
profile: katerina
market: UK
campaign: 2026-07-31-uk-telehealth-digital-health
step: icp-validator
created: 2026-08-04
status: draft
---

# ICP Validation Summary — 2026-07-31-uk-telehealth-digital-health

Validated all 187 contacts in `people-raw.csv` against the hypothesis buyer personas (Head of Clinical Operations / CMO-Medical Director / Head of Member Engagement-Product) and `icp-detail.md` segments 1, 8, and the IT-role policy. Full per-contact detail is in `people-validated.csv`.

## Headline numbers

| Verdict | Count | % of total |
|---|---|---|
| PASS | 60 | 32% |
| WEAK | 32 | 17% |
| FAIL | 95 | 51% |
| **Total** | **187** | **100%** |

**PASS by priority:**

| Priority | Count | Definition |
|---|---|---|
| P1 | 16 | Primary buyer title at High/Medium-High fit company (Head of Clinical Ops, Medical Director, CMO-equivalent, Founder/CEO at a named target, Head of Member Engagement/Product) |
| P2 | 18 | Senior adjacent-function title at High/Medium-High fit company, or primary-tier title at a Medium fit company |
| P3 | 26 | Exploratory tier — senior decision-makers at Low/Low-Medium/thematic-stretch fit companies (Thriva, Hertility, Physitrack, Sweatcoin), IT C-suite entry points (CTO/VP Eng), and CFO-equivalent (Finance Director) roles |

**Message angle distribution (across PASS + WEAK, n=92):**

| Angle | Count |
|---|---|
| member-engagement | 40 |
| clinical-operations | 16 |
| technical-integration | 14 |
| digital-transformation | 14 |
| weight-management | 2 |
| compliance | 3 |
| preventive-health | 3 |

`member-engagement` dominates because the campaign's widened hypothesis (digital health / connected fitness / weight-management, beyond pure GLP-1) pulled in a lot of product/growth/partnerships titles rather than pure clinical-ops titles. `clinical-operations` is concentrated in the two highest-fit companies (Vira Health, Peppy) plus Newson Health and Healthier Weight/Tonic.

## PASS/WEAK/FAIL by company

| Company | Fit (companies.md) | Total contacts | PASS | WEAK | FAIL |
|---|---|---|---|---|---|
| Zoe | High | 38 | 8 | 12 | 18 |
| Vira Health | High | 13 | 12 | 1 | 0 |
| Peppy | Medium-High | 18 | 10 | 4 | 4 |
| Newson Health | Medium-High | 5 | 4 | 1 | 0 |
| Healthier Weight | Medium-High | 2 | 1 | 1 | 0 |
| Tonic Weight Loss Surgery | Medium | 2 | 2 | 0 | 0 |
| Physitrack (incl. Champion Health variant row) | Low-Medium | 10 | 6 | 2 | 2 |
| Thriva | Low-Medium | 7 | 5 | 2 | 0 |
| Hertility (incl. 1 UCL-titled founder/CEO row) | Low-Medium | 10 | 5 | 4 | 1 |
| The Body Coach | Medium-Low | 7 | 4 | 2 | 1 |
| Sweatcoin | Low (model mismatch) | 15 | 3 | 3 | 9 |
| ONE FIIT / "Fiit"-adjacent noise, VC firms, non-target/noise entities | n/a | ~60 | 0 | 0 | ~60 |

**Coverage note:** Vira Health converts almost entirely to PASS (12/13) — the highest-quality company in the export by a wide margin, consistent with its High-fit rating and B2B2C model where most senior titles are genuine product/clinical/partnership decision-makers. Zoe has the most raw contacts (38) but the lowest PASS conversion rate of the 6 core target companies (21%) because most of its LinkedIn footprint is engineering/design/HR/creative roles rather than clinical or product-strategy roles — the CPO, CEO, Head Nutritionist, and Precision Health Director are the real entry points. Sweatcoin, per instructions, was scored strictly and converted only 3 genuinely senior product/growth leads out of 15.

## Top concerns

1. **This export is heavily polluted with CloselyHQ fuzzy-match noise.** Of 95 FAIL verdicts, roughly 63 are either explicit `NOISE:`-prefixed rows or unrelated small businesses fuzzy-matched on the word "Zoe," "Peppy," or "Fiit" (shop owners, tarot readers, meat-processing plants, homestays, coffee shops, babywear brands, across ~25 countries). This is a data-quality signal for `company-researcher`/`people-extractor`: a "Zoe"/"Peppy"/"Fiit" keyword search on Sales Navigator without a hard company-domain filter pulls in enormous noise. Recommend tightening the source query (filter by company LinkedIn URL/domain, not name string) before the next campaign export.
2. **"ONE FIIT" (onefiit.com, a boutique reformer-pilates studio chain) is a different company from Fiit (fiit.tv, the connected-fitness app in companies.md's excluded/no-contacts list) but was not flagged as noise.** All 4 ONE FIIT contacts (Rhian Cowburn, James Charalambous, Gede Foster, Harsh Kumar) were scored FAIL on individual merit — no clear body-scanning integration use case for a boutique studio chain — but flag this to Vadim/company-researcher in case ONE FIIT itself (not Fiit) merits separate research as a UK connected-fitness-adjacent company.
3. **Two "Thriva"-adjacent and "Zoe"-adjacent decoy entities exist that are easy to confuse with the real target company**: "Thriva Solutions" (Vishal Shah, CMO) is a distinct company from Thriva (thriva.co), and "Thriva Manufacturer" is an unrelated India-based entity. Similarly "ZOE INC," "Zoe LLC," "Zoe, LLC," "Zoe ltd," and "Zoe inc." are all distinct US/other entities from Zoe (joinzoe.com). All were correctly excluded here but worth a standing exclusion note for future exports of this campaign.
4. **Dr Helen O'Neill (row 67) has a dual affiliation** — her CSV title/company fields show "Associate Professor... UCL," but her bio confirms she is Founder & CEO of Hertility Health. Classified PASS P3 (Hertility, exploratory tier) on the strength of the bio, but flagging for Vadim's review since the structured fields disagree with the free-text bio — worth confirming which LinkedIn identity she uses for outreach before message-sequencer drafts anything.
5. **UK Finance Director / CFO-equivalent titles were treated as PASS P3** (Charlotte Armitage at Hertility, James Aubrey at Thriva, James Hodgkiss at Newson Health) on the basis that "Financial Director" is the standard UK-English term for CFO, per the seniority heuristic's explicit inclusion of "CFO" as a P3 buyer. "Head of Finance" titles (Elisa Pearlman at Peppy, Chris Grindrod at Zoe) were kept WEAK since that phrasing doesn't confirm top-financial-officer status. Flag this distinction to Vadim in case he wants Finance Director titles excluded entirely from outreach.
6. **Company-wide fit skew**: Peppy and Zoe converted a large fraction of PASS/WEAK to non-clinical adjacent functions (Design, Legal, PR, HR, Engineering) rather than primary clinical/product buyers — a reminder that a "High fit" company rating doesn't mean every LinkedIn contact from it is a good outreach target. The actual primary buyers at these two companies are a short list: Zoe (Julie Pons CPO, Jonathan Wolf CEO, Federica Amati Head Nutritionist, Bob K. Peng Precision Health Director), Peppy (Gregor Young CPO, Dr Mridula Pore CEO, Aaron Barnett/Gwen Davies/Laura Carter-Penman/Lindsay Holleran — clinical services/ops directors).

## 5 PASS examples

1. **Julie Pons — Chief Product Officer, Zoe** (P1, weight-management). High-fit company with an explicit weight-management vertical; CPO owns the exact product-roadmap decision this campaign's angle targets.
2. **Dr Frances Yarlett — Medical Director, Vira Health** (P1, clinical-operations). Primary co-sign clinical buyer at the campaign's top-fit target — B2B2C menopause platform with a named clinical-programs structure.
3. **Lindsay Holleran — Head of Clinical Operations, Peppy** (P1, clinical-operations). Exact title match for this campaign's primary buyer persona ("Head of Clinical Operations, owns check-in cadence and verification workflow").
4. **Louise Newson — Founder, Director and Menopause Specialist, Newson Health** (P1, clinical-operations). Top decision-maker explicitly named as a buyer in companies.md; private cash-pay clinic with a longitudinal patient relationship and an existing symptom-tracking app (Balance) to extend.
5. **Hamish Grierson — CEO & Co-Founder, Thriva** (P3, preventive-health). Exploratory-tier PASS: Thriva is Low-Medium/thematic-stretch fit (blood biomarkers, not body composition), but the CEO/Founder is a legitimate decision-maker for a partnership/product-expansion pitch pairing biomarkers with body-composition data.

## 5 FAIL examples

1. **"NOISE: Zoe" rows (multiple, e.g. Joanna Heywood, GEOFFREY SAMETA, Geronimo Olivera)** — CloselyHQ fuzzy-matched unrelated small-business owners across Zambia, Argentina, and elsewhere; explicitly flagged as fake rows per instructions.
2. **Marie Ekeland — Founder & CEO, 2050** — a VC/investment fund, explicitly listed as a non-target company type; also France-based with no UK operations.
3. **Rhian Cowburn — Head of Commercial, ONE FIIT** — ONE FIIT (onefiit.com) is a boutique reformer-pilates studio chain, a materially different business from Fiit (fiit.tv); no clear body-scanning integration use case for a small studio franchise.
4. **Rebecca Bowsher — Fractional Head of People, The Body Coach** — HR function; explicitly a FAIL category regardless of company fit, since HR does not own product/clinical/integration decisions.
5. **Rishi Singhal — Visiting Professor of Bariatric Surgery, Birmingham City University** — despite genuine bariatric-surgery relevance to the campaign's clinical theme, the company field is an academic institution, not one of the 15 researched target companies; his real private-practice affiliations (Priory/Spire) aren't on the target list either.

## Recommendations for message sequencing

1. **Sequence P1 contacts first** (16 contacts) — concentrated at Vira Health (5), Peppy (4), Newson Health (2), Zoe (3), Healthier Weight (1), Sweatcoin excluded from P1 by design. These map directly to the hypothesis's three named buyer personas.
2. **P2 (18) next** — mostly senior adjacent-function leaders at the same core companies (Chief of Staff, Product Marketing, Ops, Commercial/Partnerships directors) plus the two Tonic Managing Directors. Good co-sign/multi-thread targets alongside P1 contacts at the same company (e.g., Vira Health: pair Dr Frances Yarlett P1 with Robert Nutley/Rhona Macdonald/Emily Turner P2 for a multi-threaded account approach).
3. **P3 (26) treat as exploratory/lower-cadence** — this tier includes the thematic-stretch companies (Thriva, Hertility, Physitrack) where the pitch needs a product-expansion frame ("pair body composition with your existing biomarker/hormone/rehab data"), the Sweatcoin senior leads (model-mismatch, low expected reply quality), IT C-suite entry points (CTO/VP Engineering — use `technical-integration` angle, expect delegation rather than direct reply), and UK Finance Director/CFO-equivalent roles (budget-gatekeeper framing, not a primary pitch).
4. **WEAK contacts (32) — hold, do not include in this campaign's initial send.** They skew toward Design/Creative, HR-adjacent, Engineering (non-C-suite), and mid-manager roles. Per policy they are not auto-FAIL because some (especially the `technical-integration`-tagged engineering leads) could become internal champions — but they should only be activated as a second-wave/referral tactic if a P1/P2 contact at the same company goes cold, not sequenced now.
5. **Before sending, confirm two open items with Vadim:** (a) the Dr Helen O'Neill dual-affiliation (UCL vs. Hertility CEO) — confirm which identity to message; (b) whether UK "Financial Director" titles should count as CFO-equivalent P3 buyers going forward, since this affects 3 contacts in this campaign and will recur in future UK exports.
6. **Data-quality feedback loop:** flag to `company-researcher`/`people-extractor` that Sales Navigator exports keyed on company-name strings ("Zoe," "Peppy," "Fiit") without a domain/LinkedIn-URL filter produced ~63 unusable noise rows (34% of this export) — tightening the query would meaningfully shrink validator overhead on the next campaign.

---

**Next step:** Vadim final-approves this validation in Telegram before `message-sequencer` drafts the 2-message LinkedIn sequences for the 60 PASS contacts (P1 → P2 → P3 cadence).
