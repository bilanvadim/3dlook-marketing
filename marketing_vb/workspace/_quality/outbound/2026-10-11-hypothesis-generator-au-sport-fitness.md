---
qc_date: 2026-10-11
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-11-au-sport-fitness/hypothesis.md (+ companies.csv, hooks-by-company.md)
track: outbound
artifact_type: hypothesis
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-11

**Artifact:** `workspace/outbound/campaigns/2026-10-11-au-sport-fitness/hypothesis.md` + `companies.csv` + `hooks-by-company.md`
**Total: 14/20** — marginal

Code had already checked limits, signature, bans, the detector and completeness, so those are taken as fact. This report scores the judgment calls, the fit to the persona and the copy rules. Scoring is against `icp-detail.md` §8, `proof-points.md`, `export-summary.md` and Vadim's 2026-10-11 instruction («максимально використовуй контакти в списку», plus the waiver for six brands).

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **What holds:**
  - It is one hypothesis, with a complete frontmatter, a `titles` block and the Message 1 gate (l.491).
  - Sourced evidence (l.270-273), registry checks (l.20) and an alias and identity regime are all in place.
  - Every OUT category has a stated reason, and the borderline calls go to Open questions with defaults.
- **The prompt's "target, not sentence" rule (agent prompt l.112-116) is stated (l.281, 489) but not applied.**
  - l.482 hands writers a quoted copy phrase: "members compare scans they choose".
  - Lane notes and themes reuse the same coined labels (details in E).
- **The "Vadim's decisions 2026-10-11" item 1 (l.531) is presented as Vadim's own list,** but its OUT categories ("single sites", "a US HQ") are the agent's reading of a one-line instruction. This section goes verbatim into the agent cards.

### B. Factual accuracy — 3/5
- **Copy-facing product claims are clean.**
  - They use 2 photos, "under 45 seconds from the photos to structured results", 80+ body measurements, body composition estimates, 96-97% (body measurements only), §1.2 repeatability, 34,000 / 112,100 / 100+ in the locked wording (l.485-486), and the 16-78 / 150-220 / 38-210 scope.
  - "Any phone" (l.379) and "REST API with API-key authentication" (l.382) trace to `tech-spec.md` and `compliance.md` l.64, not to `proof-points.md`. That is acceptable.
  - "Switched on for every club at once" (l.366) is an implementation claim with no source.
- **"Launched … in September 2026" facts are not established, and these facts are cleared for copy.** Affected: UB2 l.408, RV1 l.411, YG1 l.413, PF1 l.420, VA1 l.421, and the evidence line l.272.
  - The App Store date in `companies.csv` is the last-update date. The same field shows 2026-10-07 for KX's 2017 app (id1313242517), 2026-10-08 for STRONG (id1663390750) and 2026-07-01 for Love Athletica (id1373821500).
  - Virgin Active Australia's app id6747742254 is lower than FWD by Fernwood's id6752467563. FWD was live by 2026-07-06 (csv l.2), so the Virgin app record predates FWD's, and "launched in September 2026" is very unlikely.
  - VA1 goes to Virgin Active's Experience Director. A wrong launch date in a message to the person who owns that app costs credibility.
- **BFT's app is published by Xponential Fitness LLC (US)** (csv l.4).
  - BF1 (l.404) and "Apps verified" (l.374) still treat it as the brand's own app.
  - Anytime gets "never 'your app'" for exactly this reason (l.374, l.419). The same logic is not applied to BFT's 23 people.
- **Mislabelled OUT reason:**
  - Nutrition Plus Ltd (l.159) is an Indigenous children's charity, not a "product-only nutrition" brand.
  - Its row is Louise Ormerod, who also appears at Juice Plus (l.168), so it is a duplicate. The outcome (OUT) is unaffected.
- **One context figure has no source:** STRONG Pilates "120+ studios in 15 countries" (l.273). The prompt requires a link for every number.
- **Sourcing:** 15 external links for ownership and status, 3 market-evidence links and App Store IDs per account. Proportionate.

### C. Brand & tone — 2/3
- **l.267 (Use case, goes verbatim into the cards):** "…can add a guided two-photo scan …, so a member records 80+ body measurements…" uses "so" to introduce the result. That is a hard ban under CLAUDE.md §6, and the artifact bans it itself at l.488.
- The same Use case sentence runs about 80 words.
- No em or en dashes, and no banned words outside the ban lists. Claims discipline holds: no diagnosis, eligibility or tracking language (l.481-483), no compliance wording in AU cold copy (l.484), and no client names.

### D. Format & structure — 3/3
- No issues with format. The frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `referral_call`, `banned_terms`). The path is correct and every template section is present.
- Validation counts match the csv (high 19, medium 21). Lanes sum to 293 and tiers to 293.

### E. Output quality — 2/4
- **The referral lane (208 of 293, 71%) will collapse into one skeleton per brand.**
  - **Question themes (l.445-451):** 4 generic themes serve every club and studio owner across all brands, and two of them overlap (member progress between sessions, and what members ask about progress). Referral counts per brand: Fernwood 37, Fitstop 32, Jetts 26, BFT 20, UBX 14, KX 12, Viva/Plus 11, REVL 9, Vision PT 9. There is no brand-specific theme.
  - **Company facts per brand:** Fitstop has 1 (FS1), BFT 1 (BF1), Jetts 1 for units (JT2 is head-office only), Fernwood effectively 1 (see below). l.474 requires "one line that could only have been written to that company", so 32 Fitstop messages share one line.
  - **`hooks-by-company.md` has no hooks.** It is a roster of names, lanes and identity flags. Nothing per person (own club names, multi-site, a headline background such as S&C coach, physio or instructor) is surfaced as a target.
  - **l.475 bans "unit counts".** Writers will read this as also banning the person's own clubs, which is the one natural per-person anchor for multi-site owners (Guneet Cheema 4 clubs, Valentin U. 5, Daniel Collins 5, Justine Rosham 3).
- **Fernwood (38, the largest group) gets contradictory instructions.**
  - FW1 (l.401) is the FWD/member-app angle already used on the 2026-08-14 head-office people. l.388 requires different angles.
  - FW1 names FWD's "progress tracking". l.478 bans naming the prospect's own tooling and then saying what the scan returns.
  - The segment A angle is a "body-progress record" (l.366), and FW1's note says never pitch progress as new.
  - Net result: 37 referral messages lean on FW2 alone.
- **Coined phrases will act as the copied sample:**
  - "between sessions" 7× (l.301, 366, 367, 378, 380, 449)
  - "progress moment" 3× (l.368, 378, 380)
  - "same guided sequence" 2× (l.304, 379)
  - "body-progress record" (l.366)
  - the quoted "members compare scans they choose" (l.482)
  - This is the same mechanism as the 10-07 easy-out sample.
- **The IN/OUT line is drawn unevenly against "maximum use".**
  - **The 43 nutrition OUTs are right:** product-only brands, distributors and contract manufacturers, with no programme that follows a person and no §8 fit. But:
    - **ASN** is IN (7 people; l.75, 120, 164, 176). Mr Vitamins (l.93, 202; stores with certified nutritionists) and Go Vita (l.79; retail health-store group) have the same in-store-advice model and are OUT. ASN's own note (l.443, "never tie the scan to supplements or results") leaves it no honest angle, so it is a stretch that spends Vadim's profile.
  - **Equipment suppliers are split.**
    - NovoFit plus The Fitness Generation get 5 partnership messages at one 44-person supplier (l.74, 150; csv l.38).
    - Life Fitness Australia and Johnson Health Tech Australia (l.129, 166) are OUT for "no member software", which NovoFit lacks too.
  - **Ownership logic runs both ways.**
    - The Lift Brands APAC CEO, based in Australia (l.133), is OUT to `nick`, where an Australian APAC CEO will never be targeted.
    - BFT (US-published app), Planet Fitness, Virgin Active and STRONG stay IN on "Australian head office runs the Australian business" (l.28, l.574).
  - **Possible Anytime head-office people are OUT as name-alikes.** These are "Collective Health and Wellness" CEO Mark Grey (l.230) and ZENKIN director Lauren Anliev, "Director at ZENKIN and Collective Wellness CO" (l.192). They were marked OUT without the identity check the 37 alias rows got, while Anytime is a declared head-office gap (OQ4, l.576).
  - **Mosh, Eamon H.:** the default is IN (l.575) while a CPO and Medical Director thread with a CEO call is live. That is one referral of upside against the risk of an uncoordinated touch on an open deal.
- **Smaller gaps:**
  - The Message 2 asset table (l.455-460) has no row for segment E `product` and `operations`: ASN 3 and Your Reformer 3. Your Reformer sits in segment E "partnership ask" (l.45), but its people are product and operations.
  - Nothing forbids naming an alias person's cell employer (Coles, CBRE, Prosperiti Disability Services, City of Greater Geelong). l.487 only governs former employers.
  - The SiSU Head of Compliance (Quality & Regulatory) and the Viva Leisure Chair are both referral. These are high-risk, low-yield touches.

## Top 3 issues (priority for improver)

1. **The referral question bank is too thin for 208 people.**
   - It has 4 generic themes (2 overlapping), 1-2 copy facts per franchise brand, and a hooks file without hooks.
   - The fix: per-brand theme targets (6-8 each for the 9 brands with ≥9 referral people), a per-theme quota, 2-3 more facts per big brand, per-person anchors in `hooks-by-company.md`, and a l.475 carve-out for the person's own clubs.
2. **Copy-usable facts carry unverified "launched September 2026" claims** (UB2, RV1, YG1, PF1, VA1) built on last-update dates. VA1 is very likely wrong. BFT's app is US-published but is treated as the brand's own.
3. **Fernwood's instructions contradict each other** (FW1 is a repeat angle, collides with l.478, and conflicts with the segment A angle). Coined phrases ("between sessions", "progress moment", the quoted l.482 phrase) will be copied across lanes. On top of that, the IN/OUT line is uneven: ASN vs Mr Vitamins/Go Vita, NovoFit vs Life Fitness/JHT, Lift Brands APAC vs BFT/PF/VA, the Collective Wellness name-alikes, and the Mosh default.

## Coordinator review

agreement: agree (5 of 5 top issues accepted; issue 2 to be verified by iTunes releaseDate before any month stays in copy)
top_issue: referral lane (208 of 293 people) has 4 generic themes and 1-2 copy facts per big brand: will collapse into one skeleton per brand, the 2026-10-06 and 2026-10-07 failure.
decisions_taken_by_coordinator (pending Vadim's approval of the hypothesis): one rule for in-store supplement retail (ASN goes OUT with Mr Vitamins and Go Vita, offered to Vadim as a pool); one rule for distributors (NovoFit capped at CEO plus founding director if it stays IN); Lift Brands APAC CEO moved into OQ2 under the AU-head-office default; Collective Health and Wellness / ZENKIN people get an identity check; Mosh (Eamon H.) held until the thread owner says yes.
action: fix round by a fresh hypothesis-generator (not a resume of the 415K-context author), then hypothesis-gate, then Vadim's checkpoint.
