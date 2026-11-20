---
qc_date: 2026-11-20
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-19-au-connected-fitness/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 16/20
status: good
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Same evidence, different verdicts across tech and junior-PM rows; moot for SEND because Vadim took every WEAK and every pool («беремо всіх», 176 to send). Not applied: P1 to P2 for Jessica Farrow (she runs LES MILLS+, the app itself, so the second reason holds); the four club head coaches without a pool are left out (not offered to Vadim). Card gap (lanes not in card-validate.md) proposed as a code fix, not applied."
---

# QC Report — icp-validator — 2026-11-20 — au-connected-fitness

**Artifact:** `workspace/outbound/campaigns/2026-11-19-au-connected-fitness/icp-validation-summary.md`, `.../decisions.md`
**Total: 16/20** — good

The list has 265 rows: 116 PASS (P1 18, P2 64, P3 6, P4 28), 26 WEAK and 123 FAIL (61 registry). I scored it against `card-validate.md`, `people-compact.csv` and the coordinator rulings.

Every number in Stats matches `decisions.md`:
- tier, angle and WEAK-by-angle splits;
- PASS per company and the "No PASS (6)" list;
- the 14/12 WEAK split.

All coordinator rulings are applied: the platform lane, the seven re-grouped rows judged on the target role, Karin Pennington FAIL, and Genesis club GMs at referral only. The identity work is good: Genesis Currumbin, Jeannie Mattinson (Oxigen), James Graham (junior history for an interim CEO title), Jessica Buxton (marketing career), Melanie Webster (events background) and Darren Mellor (Evolt). The weak points are rows with near-identical evidence that got different verdicts, and one FAIL whose reason misreads the tech limit.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **The cap rule is applied to one person only.** The prompt says people over a cap go to WEAK "over the cap". Micayla Wright (LMI Head of Engineering, over the two-tech limit) got WEAK. Michael Heyns, Alex Hopkins and Andrew Flavell, over the same limit, got FAIL. Heyns and Hopkins have the same Xplor DevOps background as Wright.
- **PPL-1 departures are not explained in the reason.** Nicole Grainger, Matt Towe and Kristy-Lee Roodenburg are P1 on the title alone (no headline, or a headline that repeats the title). James Brennan and Brad Wharakura have the same title, "National Group Fitness Manager", and got P2. The tiers follow "one P1 per company", which is not the card's rule. Tiers only set the order, so the cost is small.
- **PPL-2 departure for club head coaches is not stated.** Ashley Googe (Head Coach at Cessnock Genesis, full profile), Emma Jones, Amie Hession and Andres Galvis are FAIL "club head coach". The card says a non-buyer in a relevant function at an IN account is a referral PASS. None of them is in a pool, so Vadim cannot promote them.
- **Done right:**
  - only the two input files and the rulings are used;
  - registry FAILs are left as written;
  - technical-integration is at most two per company and never alone at an account;
  - pools with a working `promote` line are in the first report;
  - PPL-1 gaps are listed by company.

### B. Factual accuracy — 4/5
- `donald-horsburgh-0498464`: FAIL "CIO, empty profile, second tech". The card allows two tech contacts per company, and Les Mills New Zealand has one tech PASS (Brent Nathan). The TECH pool's fix, "Raise the two-tech-contacts limit at Les Mills International", does not apply to him because he is at a different company.
- The TECH pool says 7 people but names 6.
- Summary line 36 calls Amy Cashman a franchisee. She is a Product Engagement Partner in KX's product and education team, and `decisions.md` has this right.
- `jessica-farrow-1a000423`: the reason says she "owns the subscription app itself". It leaves out the "Social Strategy" half of her title (a Not-the-buyer function) and her TikTok client-partner and WBD agency background.
- `lee-calvert-328b047b`: the reason says "a commercial head, which the partnerships lane covers at every group". The card names only partnerships and BD titles. Head of Corporate is corporate membership sales, and the card puts membership sales under Not the buyer.
- No invented companies, numbers or people. All counts are verified.

### C. Brand & tone — 3/3
- No issues. No banned words and no em dashes. The only hit for "navigat" is "Sales Navigator".

### D. Format & structure — 2/3
- The frontmatter is complete: `product`, `profile`, `campaign`, `created`, `stage`, `status`.
- The template section "Vadim — please confirm" is missing. It was replaced by "Questions for Vadim are in the coordinator's report", which may be a coordinator edit, but the artifact does not have it.
- SEND and WEAK are prose cells and bullets, not the template tables (person · title · P · angle).
- `decisions.md`: the pipe format is correct and the FAIL reasons are 2-5 words.

### E. Output quality — 3/4
- Usable after about 15-20 minutes of row fixes (table below).
- The Top concerns are strong:
  - 23% of the list was already messaged;
  - 6 Planet Fitness Australia club GMs point to an MD who was already messaged;
  - Les Mills International is 15% of the list;
  - the Evolt note for step 5.
- The pools are complete for senior roles.

## Per-person findings

| person_id | Now | Suggested | Why |
|---|---|---|---|
| `donald-horsburgh-0498464` | FAIL | WEAK (technical-integration) | He is within the two-tech limit at LMNZ. An empty profile next to a Head of Technology with a CIO past is a valid WEAK reason (possible leaver). "Second tech" is not a valid reason. |
| `mheyns`, `alex-hopkins-0a1a6959`, `andrew-flavell-dr-eng-59a3a9` | FAIL | WEAK "over the cap" | Same treatment as `micayla-wright-a5a306155`, per the prompt's cap rule. |
| `elliot-smith-b4b3a1244` vs `rhea-s-66014110` | FAIL "junior" vs PASS P2 | Same verdict for both | Elliot: APM, headline "Product Manager/Owner", earlier Technical Systems Analyst at LMI. Rhea: BA/Product Owner, earlier customer support manager and BA. They are at the same level. With 12 LMI product people already in SEND, putting both in PRODUCT-ADJ is cleaner. |
| `tori-clapham-902869195` | WEAK | PASS P2 product | Her headline names Peaches' studios and Online, which is the second confirmation the empty-profile rule asks for. `chris-hole` is PASS on less: "Director" plus a freelance marketing and loyalty background, nothing tying him to Peaches beyond the export. |
| `kara-spice-36b619240` | WEAK referral | PASS P4 referral | Her headline confirms "Managing Director of KX Pilates New Zealand". Franchisees with similar evidence (`mackenzie-pirlo-1008a3b0`, `eloise-censor-a7983749`) are PASS P4. |
| `jessica-farrow-1a000423` | P1 | P2 | See B. LES MILLS+ product calls sit with Cam Adams (P1) and Amber Taylor. |
| `lee-calvert-328b047b` | PASS P2 partnerships | WEAK, or move to the COMMERCIAL pool | The summary's own COMMERCIAL pool says "commercial heads" are not yet accepted (Llori Valenzuela and Lee Hanrahan are FAIL). Lee Calvert is in on the same criterion. |
| `paul-mercer-87835919a` | FAIL "club fitness director" | WEAK | An exact persona title ("Fitness Director") with an empty profile is the validator's own WEAK rule (`mark-hurdle-781781315`). "Club" is inferred and not in the row. |
| `nicole-grainger-433b5610a`, `matt-towe-a3a845308` | P1 | P2, or state the second reason | P1 on the title alone (PPL-1). `james-brennan-593a2923` has the same title and a richer profile, and he is P2. |

Lower-priority checks (for the account-facts round, which re-checks P1s and roles):
- `kate-rawnsley-shirtcliff-07926923` (WEAK) vs `asmithnz` (FAIL): same function at GymMaster, and the card puts platform sales under Not the buyer. If she stays WEAK, the summary should say she is a referral ask only.
- `matthewkane`: his headline is all Orange Gorilla and OG01. Barre Body appears only among his other roles, so "co-decides the offer" is inferred.
- `jordan-checker-876b6516b`: "Founder" with no headline. His other role is Founder at INCHECK FIT, and Revo's operating founder (Andrew Holder) was already messaged. Check whether he is still involved and what INCHECK FIT does.
- `riley-woodcock`: the headline "Commercial Operations Leader | Multi-Site Business & Franchise Management" reads as operations and franchise management. Under the card that is referral, not P2 product.
- `warren-ainsley-6519a666`: he worked at AIA Australia (a live thread). Like the Evolt note, copy must not mention it.

If the main table is applied, SEND goes from 116 to 117 or 118 (Tori Clapham and Kara Spice in; Lee Calvert and possibly Rhea Sands out), and WEAK grows by about 5.

## Pipeline finding (not scored)

`card-validate.md` does not carry the hypothesis "Lanes" section. Yet the validator used:
- P4 for referral ("because the hypothesis lane note says so");
- a `programs` lane;
- "commercial heads" in partnerships.

All three come from `hypothesis.md` lines 179-184 and appear nowhere in the card. Either the validator read `hypothesis.md` against its prompt, or the coordinator passed the lanes in the brief, and the summary does not say which. The fix: `outbound_pack.py card --for validate` should include the lane names and their P levels. The prompt's "priority 1-3" should also allow P4, or the card should state the mapping.

## Top 3 issues (priority for improver)

1. **Same evidence, different verdicts:**
   - over-limit engineers: Wright WEAK vs Heyns, Hopkins and Flavell FAIL;
   - Elliot Smith vs Rhea Sands;
   - Tori Clapham and Kara Spice WEAK despite confirming headlines, vs Chris Hole PASS;
   - Lee Calvert PASS vs the COMMERCIAL pool;
   - Paul Mercer vs Mark Hurdle.
2. **Donald Horsburgh's FAIL misreads the two-tech limit** (he would be the second of two allowed), and the TECH pool's remedy does not reach him. The pool count (7) does not match the names (6).
3. **Undeclared departures from PPL-1 and PPL-2:**
   - title-only P1s (Grainger, Towe, Roodenburg, Farrow);
   - club head coaches FAILed with no pool, so Vadim cannot promote them.

Notify: not sent. This QC run had no shell, so the coordinator sends the notification.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
