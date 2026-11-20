---
qc_date: 2026-11-20
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-11-19-us-connected-fitness/icp-validation-summary.md + decisions.md
track: outbound
artifact_type: icp-validation
total_score: 17/20
status: good
coordinator_review:
  agreement: "✅ agree"
  top_issue: "Near-identical rows got different verdicts and the WEAK recommendations bent Not-the-buyer; all per-person findings confirmed against people-raw.csv and sent back to the validator (fix round 2026-11-20). headline_if_new drops headlines similar to the title (Ryan Mott 'VP, Data Product'): code fix proposed to Vadim."
---

# QC Report — icp-validator — 2026-11-20 — us-connected-fitness

**Artifact:** `workspace/outbound/campaigns/2026-11-19-us-connected-fitness/icp-validation-summary.md`, `.../decisions.md`
**Total: 17/20** — good

The list has 351 rows: 83 PASS (P1 12, P2 32, P3 39), 15 WEAK and 253 FAIL. I scored it against `card-validate.md`, `people-compact.csv` and the seven coordinator rulings. Every number in Stats checks out against `decisions.md`: tiers, WEAK, location 8, collisions 13, group counts and angle counts. All seven rulings are applied. The weak points:
- verdict and tier drift between near-identical rows;
- two WEAK recommendations that break the card's "never SEND" rule for Not-the-buyer functions.

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
- **Not the buyer: the card says these people are "a skipped pool ... never SEND".** Two WEAK people are recommended for SEND anyway, while identical profiles went to FAIL plus a pool:
  - `daniellepeckskamp`: headline "Retention & Lifecycle ... Marketing | Braze Certified". The same kind of profile, `mirelacialai`, went to pool E.
  - `alisa-aguirre`: Head of Customer Success. Pool B takes `oaktownolivia`, `luanaperez`, `megan-johns-72b40818a` and `amartanna-cpa-ca`, and the summary says it "applied Not the buyer" to them.
- **Ruling 4 is only partly applied.** It sends parent-level product leaders without Trainerize in the profile to WEAK. Only the three VP+ people went WEAK (`finn-hegarty-2871037`, `thekellycard`, `tristanalexander`). The five product directors went FAIL into pool A: `elizabeth-gray-94237a106`, `kendall-wilson-aba17628`, `jenniferannpelton`, `doug-reeder-3247511`, `zekebrustkern`.
- **The single-app P1 rule is a reinterpretation.** "CPO or VP Product at a single-app company gets P1" treats the company type as the "profile scope" the card asks for. It is disclosed in the Tier notes and tiers only set the order, so there is no extra deduction.
- **Done right:**
  - only the two input files were used;
  - the registry, the Location rule and rulings 2, 3, 5, 6 and 7 are applied;
  - the P4 → 3 mapping is disclosed;
  - every account has a route-in below C-level wherever the export has one;
  - the pools are in the first report.

### B. Factual accuracy — 4/5
- `meghiggins21`: her P1 rests on "consumer fitness product behind her (SoulCycle product, WeWork on-demand)". WeWork On Demand is workspace booking, not fitness. Only SoulCycle supports the claim, and nothing shows her current Peloton scope.
- `bmaloley`: the reason states "(the fitness app, not Ladder Life)" as fact. The summary's own concern says this is unconfirmed. If the reason reaches copy, an unverified identity becomes a claim.
- `paul-manley-69851845`: the FAIL reason says "name collision", but his headline is "Owner | Videographer at TONAL", so he is a contractor. The FAIL stands, but the ruling-2 count of 13 is off by one.
- Pool G mixes rationales. `jamesrdrake` (SVP DTC, commerce, not C-level) and `markwatterson` (FAILed for the commercial-equipment unit, not for company size) would not get in under "lift the under ~500 staff limit for CEO/C-level".
- **Verified correct:**
  - the registry inventory for the nine re-contacted companies;
  - the three August collisions: `brad-herr-0354b723`, `jeff-yake-b8267b1`, `wanda-williams-a32a82117`;
  - the fake-profile calls on `stephanie-wilder986` and `ashley-flores-a20a70287`;
  - `arturo-garza-b567ab6b` as an MLM coach;
  - `marietta-p-9144112` vs `hariumapathy`;
  - the three Trainerize PMs outside the US.

### C. Brand & tone — 3/3
- No issues. No banned words. The three em dashes are in headings the template prescribes.

### D. Format & structure — 3/3
- The frontmatter is complete (`product`, `profile`, `campaign`, `created`, `stage`, `status`) and all five sections are present.
- `decisions.md` uses the pipe format, and the FAIL reasons are 2-5 words.
- Minor: pool A says 6 people but names 5.

### E. Output quality — 3/4
- About 15 minutes of fixes, listed below.
- The Top concerns section is strong, especially three points:
  - the August registry collisions that inflate the Echelon and Future post-mortem counts;
  - the card's CX contradiction behind pool B;
  - Trainerize's product team sitting outside the US.

## Per-person findings

| person_id | Now | Suggested | Why |
|---|---|---|---|
| `cristal-beckstrom` | PASS P3 product | FAIL into pool F, or say why not | Her title is "Commercial Senior PM" with hardware/NPI scope, on an iFIT page that includes FreeMotion (club equipment). The commercial unit sent `markwatterson` ("commercial equipment unit CEO") and Peloton's `mitchellpavao` to FAIL. If "Commercial" only means a business-side PM, P3 stands under the card's hardware line, but the reason should say which. |
| `ben-schultz` | PASS P2 | WEAK (check whether he left) | The headline leads with "the future of our food system". His latest prior role is "Co-Founder at Mez Foods", and his current title repeats an earlier Peloton role. `jordanannis` got WEAK on a similar signal (PPL-5). |
| `theodorelui` | PASS P3 referral | Treat him the same way as pool D | He has the same function as `lindsay-pontello` and `barbarathornethomsen`, who are both FAIL. Pool D asks Vadim to "allow a referral lane for corporate strategy", a lane Ted already has. They should be all referral or all pool. |
| `yi-hsin-chang-1113286` | FAIL | WEAK | Director of Product Development at BODi, in LA, with an empty profile: the same function, company and city as `nate-a-silva` (WEAK). `sarahnovello` and `heather-guymon-b1425814` got WEAK on the same evidence. |
| `daniellepeckskamp` | WEAK, recommended | FAIL into pool E | Lifecycle and retention marketing is Not the buyer. The retention lane drew 0/53. Treat her like `mirelacialai`. |
| `alisa-aguirre` | WEAK, recommended | Move to pool B (keep the BodySpec note) | A customer-success head is the pool B profile, and Vadim decides pool B as a group. |
| `meghiggins21` | P1 | P2 | See B. `nickcaldwell`, `tworetzky` and `eugenekwak` are P2 because "no app scope shown", which is also true of her current role. |
| `john-santo-096310149` | P1 | P2, or raise `jshottan` to P1 | The summary's own rule says P1 at a hardware company needs app scope in the profile. His profile shows only the CPTO title and Santo Design Group. Tonal's CPCO got P2 under the same rule. |
| Pool A | 5 directors FAIL | WEAK per ruling 4; add `keegan-dowling-ba8aaa7`, `ericreimers`, `laurietaylorkemp` | The card names "the partnerships or integrations head" as a group C buyer (P2), so ABC's partnership owners belong to the same route to Trainerize. |

Lower-priority checks before Message 1:
- `emilybaldwin3`: her title has no level and her headline names her own franchise. Linking her to the subscription team behind August's interested reply is an inference.
- `bmaloley`: confirm his identity, as the summary already asks.

If all the suggestions are applied, SEND goes from 83 to 81 or 82, depending on how Ted Lui and pool D are resolved.

## Pipeline finding (not scored: the agent could not see this)

`headline_if_new` in `scripts/outbound_pack.py` (lines 752-761) drops headlines that carry information. It drops three kinds:
- headlines that contain the title as a substring (`t in bare.lower()`);
- headlines cut at "at" or "@", which loses the `| ...` segments after the company;
- near-matches (ratio > 0.8), even when one word changes the function.

Compared with `people-raw.csv`:
- `ryan-mott-51660a11`: the raw headline is "VP, Data Product". His P1 should be P3 (data product scope). The app's VP Product is Ben Gammon, who is in the registry.
- `bogatzproductmanager`: the headline ends "| Onboarding & Activation". Under the card that is P2 (onboarding is named), not P3.
- `trent-ward-12b992b2`: the headline reads "... | Wattbike, Ergatta, FORME and CLMBR". Per `companies.md`, Ergatta joined TRNR on 2026-03-11. That puts 7 SEND at one parent, 6 of them founders or C-level. The account-facts round should know, and copy should not mention the deal.
- `mmasters1` ("Senior Director, FP&A") and `mike-camphouse-090b95b2` ("Production Manager at Icon Health and Fitness"): the FAILs are right by luck.
- `yi-hsin-chang-1113286`: the headline ends "at Product Partners", Beachbody's legal entity. That confirms his identity.

## Top 3 issues (priority for improver)

1. **The Not-the-buyer rule is bent in the WEAK recommendations.** `daniellepeckskamp` and `alisa-aguirre` are recommended for SEND, while identical profiles went to pools E and B.
2. **Near-identical rows get different verdicts:**
   - `theodorelui` vs `lindsay-pontello` (this undercuts pool D's premise);
   - `yi-hsin-chang-1113286` vs `nate-a-silva`;
   - `cristal-beckstrom` vs `markwatterson` and `mitchellpavao`;
   - `ben-schultz` vs `jordanannis`.
3. **P1 calls break the summary's own rule.** `meghiggins21` rests on a misread of WeWork On Demand, and `john-santo-096310149` is P1 while `jshottan` and `nickcaldwell` are P2. A separate code fix is needed for `headline_if_new`, which gave `ryan-mott-51660a11` a P1 his real headline does not support.

Notify: not sent. This QC run had no shell, so the coordinator sends the notification.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
