---
qc_date: 2026-10-22
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-22

**Artifact:** `workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/hypothesis.md` (+ `companies.csv`)
**Total: 15/20** — good (bottom of the band)

**Scored against:**
- `icp-detail.md` §1 (l.11-75), §5, IT roles (l.597)
- `proof-points.md`, `accuracy-formulations.md` §1.1-1.2, `messaging.md` l.71, `compliance.md` l.101, `tech-spec.md`, `how-it-works.md`
- `audience.md` §1 (l.36-40)
- the agent prompt and `outbound_pack.py` CARD_SECTIONS (l.745-753) and the five-gram check (l.1679-1705)
- the export `sales-nav-raw/export-1.csv` (47 rows, read row by row for the people named in the verdicts)
- `2026-07-27` post-mortem (15.9%), `2026-08-07` post-mortem (0/60 technical), the `2026-09-29` and `2026-10-16` reply files

**What reaches the message writer:** the Use case, Message angle (lanes, question topics, Account facts, content asset), Outreach language, Rules and both decisions sections. The persona, objections and verdict table go only to the validator. The five-gram copy check covers only Rules and the `- **lane**` notes. It does not cover Use case, "Angle by shape" or Question topics.

**Taken as fact:** limits, signature, bans, the detector and completeness.

**Limits of this QC:**
- No web tool, so the cited live pages (Gameday, Hone, Maximus help center, Marek archive) were not re-fetched. Account facts were checked against the "already captures" table, the export and `companies.csv`.
- No shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- The template, titles block, Message 1 gate, decisions block and open questions are all present. The registry is clean (verified: no hit in `exclusions/` or any other campaign). The earlier-campaign lessons check out: 15.9% = 39/245, 0/60 technical, the knownwell MA-appointment reply, the eMed pharmacist reply.
- The prompt says to write targets, not finished sentences. The card still carries copy-shaped sentences in sections the five-gram check does not cover (see E).
- Vadim's decision is to top up through Apollo. The plan adds 46-58 people (l.162-171), up to 25 of them at Gameday. The question topics (l.193-199) cover only the 43 export people. Nothing tells writers how to give the Apollo additions distinct questions.
- §1 and `audience.md` §1 lead with repeatability (`< 1 cm`). The rotation list (l.233) leaves it out, so it appears only in an objection answer and the Rules numbers list.

### B. Factual accuracy — 3/5
- Product claims are backed: two photos, under 45 seconds, 80+, composition estimates, 3D model, "96-97% accuracy against expert manual measurement" (`messaging.md` l.71), 38-210 kg, the US compliance line verbatim (`compliance.md` l.101), the fixed proof lines, "any phone" (`tech-spec.md` l.73). "2-4 weeks" (l.123, l.224) comes only from `icp-detail.md` l.597. The pipeline card licenses it, so it does not trigger the cap, but the hypothesis gives no source for it.
- l.23 and l.180 (messages card) say all five telehealth accounts run "a portal, labs and check-ins". l.77 lists DudeMeds check-ins as "Not verified: never claim". Writers get the claim and the ban side by side.
- Marek is IN on a June 2025 archive and one third-party GLP-1 listing (l.75). The live site was not checked from a US IP. Yet the product lane note (l.184) and two Marek topics (l.198) build on the "monthly coach check-in" as a current fact. This should be conditional or carry a re-check gate before import.
- l.16 says "13 `Company_name` values". The export has 12. Row 1 (l.47) counts `Gameday Men's Health` (16) including Gameday N., who is also row 7, so the alias counts sum to 21 against Send 20.
- l.203 "membership model" is in no row of the verified captures table (l.72).
- l.39 says "LaSara ... publish no size", but `companies.csv` l.6 says "about 12 (team page on site)". l.39 gives Maximus "50,000+ clients", which `companies.csv` l.4 does not record.
- Validator-check gap (l.60): Ampy T. (export l.152, "COO, no clinic named") and the held Alissa T. (export l.287, Partner at a Gameday clinic and at Lobbie) share the surname Tyler and both have Texas education. The plan messages Ampy while Alissa is held, and the possible link is not flagged.

### C. Brand & tone — 2/3
- l.180, messages card: "...lets the clinician or coach see body change..." This is a copy-ready sentence carrying the `let` guardrail word, in a section the five-gram check skips.
- l.188 lane note: "no hardware to buy, place or service" is a triple parallel and tagline-shaped.
- l.206 Account fact quotes Marek's "Guided Optimization". Account facts are meant to be reused, but l.234 bans "optimization".
- l.100 "each clinic owner what his clinic runs". Several clinic-operator contacts are women (e.g., Shelley G., Megann G., Sommer R., Mistie S.).

### D. Format & structure — 3/3
- Frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `banned_terms`, `referral_call`). The path is correct and all template sections are present. `companies.csv` has six rows that match the verdict table.
- Nit: "Use case" (l.83) is four sentences against the template's one.

### E. Output quality — 3/4
- Strong research and account specificity: Maximus-domain trap, Lobbie conflict, Justin P.'s bio flagged, sister brand, displacement check.
- **Internal contradiction on the Gameday angle.** l.227 says never to set the in-clinic scan next to ours and never to imply what equipment lacks. Yet several card lines do exactly that:
  - l.83 "At Gameday it complements the in-clinic scan".
  - l.181 the Gameday angle.
  - l.193 topic (5) "which body measurements the clinic records beyond the in-clinic scan".
  - l.195 Mark L./Gina D. "beyond the scale and the in-clinic scan".
  These run through about half of the campaign, and the writer, gate and QC will fight over them.
- **Sensitive-topic gaps:**
  - l.197: Nick B.'s topic invites "the photo step hair patients already use", against l.225, which bans hair loss as a topic.
  - l.196: Nicholas D. ("how the brand shows member progress visually, the 3D model as the link") is marketing creative built on member bodies. That is before-and-after territory under l.225 and a privacy problem.
  - "GLP-1" is used in l.199, l.205, l.207 and l.208, which the "any drug or compound name" ban (l.225) and the "Never: drugs" lines (l.205, l.208) leave ambiguous.
  - `banned_terms` (l.10) misses HRT, ED, menopause/estrogen (Hone serves women) and the ED drug names. The prose rule covers them, but the code check does not.
- **Gameday topic banks are not distinct:**
  - (1)≈(10): the member's view of his progress between scans or visits.
  - (2)≈(6): continuity when a member misses a visit or is away.
  - (4)≈(11): bringing members back and keeping in touch.
  - (7) is given to two people (Justin P., Ron N.), against "one each". It also matches network Shea F. (l.194). Justin has one open clinic; the second is "in progress" (export l.129).
  - (5)≈ the clinical pair (l.195) ≈ (12) Jason A.
- Judgement on the account mix:
  - Gameday grows to about 45 of about 88 invites (l.164, l.259). Its clinics are independently owned, run a network-wide vendor stack, and already scan in person. The last in-clinic chain got no reply (l.94).
  - FitXpress is API/SDK only and has no hosted flow, so nothing explains how one clinic would deploy it. That makes the "pilot at a Gameday clinic" metric (l.268) implausible. The Lobbie channel, the real path to clinics, sits only in Open question 1.
- Metrics: the positive-reply target of 2 (l.265) is higher than the expected total replies (2% of 88 ≈ 1.8, l.264). Falsification needs 3+ P1/P2 replies (l.270), which this volume cannot produce.
- Minor:
  - "CMO" (l.47, l.164) is ambiguous between medical and marketing at the Apollo step.
  - Daniel W. ("Partnerships & Client Experience") sits in `referral`, though §1 names member-experience directors as buyers.
  - The objection answer at l.120 ("the phone capture needs no visit") sets ours next to Hone's add-on (validator card only).

## Top 3 issues (priority for improver)

1. Gameday angle vs Rule l.227: l.83, l.181, l.193 (5) and l.195 put our capture next to the in-clinic scan or imply it lacks something. Either rewrite these lines as home and between-visit topics that do not mention the scan, or restate l.227 so that "complement, never compare" is the actual rule.
2. Sensitive-topic gaps: l.197 (hair), l.196 (brand creative from member bodies), GLP-1 vs "any drug" (l.225 against l.199, l.205 and l.208), and `banned_terms` without HRT, ED, menopause or ED drug names.
3. Topic coverage: dedupe the Gameday pairs (1)/(10), (2)/(6), (4)/(11), (7)/Shea F., (5)/clinical/(12). Split (7) between two people. Add a rule or slots for the 46-58 Apollo additions (l.162-171).

## Coordinator review

```
agreement: ✅ agree
top_issue: The Gameday angle sets our capture next to the in-clinic scan against the hypothesis's own rule l.227. The deployment path for independently owned clinics on an API/SDK product is missing. Spot-checks confirm l.181, l.193 and l.195 against l.227, and the Ampy Tyler / Alissa Tyler link (both at Gameday). Fixes go to a fresh hypothesis-generator with hypothesis.md, companies.csv and this report; the first pass ran 314K tokens, so no resume.
```
