---
product: fitxpress
profile: katerina
market: UK
campaign: 2026-09-01-uk-erakulis-similar
step: 4-icp-validator
created: 2026-09-12
---

# ICP Validation Summary — 2026-09-01-uk-erakulis-similar

ICP applied: `icp-detail.md` **§8 Connected & Digital Fitness** (FitXpress set) plus the
2026-07-22 **IT & Technical Roles** policy, read against the `hypothesis.md` persona block
(rewritten 2026-09-12, status approved).

## Stats

- Total reviewed: **98**
- **Excluded by registry: 0** (`outbound-registry.py check --profile katerina` → 98 clear,
  0 must-exclude; output at `people-checked.csv`, every row carries a person LinkedIn URL)
- **PASS: 9** (priority 1: 5, priority 2: 3, priority 3: 1)
- **WEAK: 17** — candidates for Vadim's manual review
- **FAIL: 72** — all on persona or on name-collision grounds, none on the registry

### By company

| Company | Rows | PASS | WEAK | FAIL | Read |
|---|---:|---:|---:|---:|---|
| Nutracheck | 31 | 4 | 3 | 24 | Only company where the export reached a real product org (MD, Head of Data Product, PM, Partnerships) |
| Medicspot | 22 | 2 | 3 | 17 | Founder/CEO plus CTO co-founder reached; the other 17 are coaching, support, HR and warehouse |
| Infohealth Ltd (NowPatient) | 19 | 0 | 6 | 13 | Dispensing-pharmacy roster, not an app product org — see Top concerns |
| Coopah | 10 | 2 | 1 | 7 | Head of Product and co-founder both reached; the rest is runner support |
| Fiit | 8 | 1 | 2 | 5 | MD reached; two rows are probable "Fiit" keyword collisions |
| WithU | 8 | 0 | 2 | 6 | Engineering leadership only; the rest is audio/video content production |
| **Total** | **98** | **9** | **17** | **72** | |

Name-collision artefacts that survived the pre-filter: **3 probable** (Jessica Swales,
Simon Knight, emma Armour), plus **2 mis-attributions** where the person's real employer
looks different from the `company_name` (Ian Carrington → Cardlytics; Rajan Mistry → job
seeking, no Medicspot signal). All five are FAIL or WEAK-with-verify; none is in the PASS set.

## Top concerns

1. **The list does not clear the hypothesis's own contact floor.** `hypothesis.md`
   Validation criteria require **≥40 contacts passing ICP validation** (target 60+).
   PASS is 9; PASS + WEAK is 26. The hypothesis was not falsified at step 2 — it cleared
   the 15-company floor at 10 proceeds — but it is failing here, one step later, on the
   contact side. This needs a decision before step 5, not after.
2. **Infohealth Ltd returned the pharmacy, not NowPatient.** Nineteen rows: three
   pharmacists, a dispenser, a pharmacy assistant, a counter assistant, a senior pharmacist
   manager, a logistics manager. Zero product, growth or retention titles. `companies.md`
   already warned that NowPatient has no standalone LinkedIn page and trades under its
   parent; this contact set is what that warning looks like in practice, and it half-confirms
   the hypothesis's own "pure dispensing pharmacy" anti-case. The two bare `Director` rows
   are the only owner-level shots and both are unverified.
3. **Seniority mix is thin and the `seniority` column is unreliable.** 61 of 98 came in as
   `other` and only 17 as `director/head` or `founder/ceo`. Reading the actual titles moved
   rows in both directions: `Managing Director` at Fiit (product leader) and `Head of Data
   Product` were under-read, while `Head of Brand`, `Marketing Director` and `Head of
   Performance Marketing` are director-grade but sit on the hypothesis's explicit
   "Not the buyer: marketing" line.
4. **Two companies have no PASS at all.** WithU produced only engineering leadership
   (Director of Engineering, Lead Backend Engineer) and six content-production roles.
   Infohealth produced none. If both stay unreachable, the sequence effectively runs on
   four companies.
5. **The asymmetry the hypothesis flagged is visible in the PASS set.** Only Medicspot and
   NowPatient sit in flavour 4, where Yazen is a nameable reference. Six of the nine PASS
   rows are at Fiit, Nutracheck and Coopah, where reason #2 of the hypothesis says we have
   no nameable reference in that shape — step 5 has to carry those on the churn argument and
   integration speed alone.
6. **`location_country` is unusable in this export** (96 of 98 say "United Kingdom",
   including a row whose summary places her in Texas) and `location_city` carries the country
   string for all 98. Neither column contributed to any decision here; every geo judgement
   came from the company, not the row.

## Sample of decisions

### PASS examples (5)

1. **Ryan Sherreard — Head of Product — Coopah** → priority 1
   - Reason: the exact primary persona, owner of the roadmap and the build-vs-buy call
   - Suggested angle: `build-vs-buy`
2. **Dr Zubair A. — Founder & CEO — Medicspot** → priority 1
   - Reason: at 34 employees the founder still owns product and takes the meeting directly
   - Suggested angle: `differentiation-ltv`
3. **Daniel Hutson — Managing Director — Nutracheck** → priority 1
   - Reason: CEO-equivalent at a 36-person subscription app, owns the paid-tier retention curve
   - Suggested angle: `differentiation-ltv`
4. **Oliver Brooks — CTO & Co-founder — Medicspot** → priority 2
   - Reason: the co-founder hat gives real purchasing authority, so this is a PASS rather than the plain-CTO WEAK
   - Suggested angle: `technical-integration`
5. **Daisy Ford — Partnerships Manager — Nutracheck** → priority 3
   - Reason: ICP §8 names the innovation and partnerships team as a buyer, but this is manager grade
   - Suggested angle: `partnership-integration`

### FAIL examples (5)

1. **Jessica Swales — Hair And Makeup Artist — "WithU Group"** → FAIL
   - Reason: name-collision artefact, not an employee of the WithU training app
2. **Helen Flook — Pharmacy counter assistant — Infohealth Ltd** → FAIL
   - Reason: dispensing-counter role with no product or purchasing involvement
3. **John White — Marketing Director — Nutracheck** → FAIL
   - Reason: director-grade, but the hypothesis names marketing explicitly under "Not the buyer"
4. **Chloe Whylie — Fitness Instructor — Fiit** → FAIL
   - Reason: fitness programming, named explicitly in the hypothesis as not the buyer
5. **Martin Green — System Support Specialist — Medicspot** → FAIL
   - Reason: IT support is a hard FAIL under the 2026-07-22 IT-roles policy (infrastructure, not product)

### WEAK examples (3, for shape)

1. **Daisy Blackwood — Director of Engineering — WithU** — IT policy: evaluator and champion,
   not the economic buyer. If included, she is a P3 `technical-integration` row.
2. **Rajive Patel — Director — Infohealth Ltd** — bare "Director" at a 53-person business;
   plausibly owner-level, remit unstated, worth a manual check.
3. **Simon Knight — Owner — Fiit** — "Owner" is not a plausible title at VC-backed Fiit
   Technology Ltd; probable keyword collision, verify the profile first.

## Recommendations

- **Re-run Sales Navigator on titles, not on company keywords.** The export was built
  company-first and returned whole headcounts, so 72 of 98 rows were never candidates. A
  title-filtered search (Product / Growth / Retention / Engagement / Founder) across the same
  10 companies plus the 4 Vadim already worked would produce a better list at a fraction of
  the review cost.
- **Search the company by LinkedIn company URL, never by name string.** "Fiit" and "WithU"
  are both short, common tokens; the collisions (ONE FIIT, FIIT Institute, "WithU Group")
  all came from name matching. `companies-verified.csv` already carries a confirmed
  `linkedin_url` for every row except NowPatient — use it as the key.
- **Resolve NowPatient's entity before spending any more credits on it.** Searching
  Infohealth Ltd returns the pharmacy. Either find the product org under a different entity
  or drop the company from this campaign.
- **The four companies Vadim has already worked (Second Nature, Numan, Voy, CheqUp) are the
  ones with real product organisations.** Their absence, not the collisions, is why the
  contact count is short — Voy alone is 501-1,000 people. Worth confirming whether "already
  outreached" blocks a second, product-org-targeted pass.
- **Fiit's "ONE FIIT" B2B repositioning is a live ambiguity**, flagged in `companies.md` and
  visible here (a finance coordinator filed under ONE FIIT). Confirm which side of the
  business the consumer app now sits in before step 5 writes to James Charalambous.

## Vadim — please confirm

1. **WEAK group (17 people): in or out?** They split into three piles:
   - 8 engineering/technical (Head of Engineering, Director of Engineering, 2 tech leads,
     3 senior engineers, 1 lead backend) → per the 2026-07-22 policy these are P3
     `technical-integration` rows, evaluators and champions, not buyers.
   - 5 unverified owner-level (2 Infohealth directors, the Infohealth "Senior Partner"
     conflict, Simon Knight at Fiit, Ian Carrington's advisor seat) → each needs a
     30-second LinkedIn check before contact.
   - 4 adjacent commercial (Head of Operations at Medicspot, 2 partnerships/product rows,
     Coopah partnerships) → real but off-persona.
2. **Priority 3 (1 person, Daisy Ford at Nutracheck): in or out?** One row, so this costs
   almost nothing in closelyhq credits either way.
3. **The floor question, and it is the real one: 9 PASS against a stated floor of 40.**
   Even including all 17 WEAK the list reaches 26. Options as I see them: (a) re-run Sales
   Navigator title-first on the same companies, (b) re-open the four already-worked companies
   for product-org contacts only, (c) run the sequence at this size and accept it is a pilot
   rather than the campaign the hypothesis scoped, (d) fold into a pan-European pass on
   `olena`, which `hypothesis.md` already names as the falsification route. I did not pick
   one — that is your call, and the answer changes what step 5 is asked to write.
