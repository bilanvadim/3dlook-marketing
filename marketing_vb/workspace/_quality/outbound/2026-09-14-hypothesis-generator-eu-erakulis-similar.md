---
qc_date: 2026-09-14
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-09-14-eu-erakulis-similar/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 13/20
status: marginal
coordinator_review: |
  agreement: ✅ agree. Verified NowPatient=53 (UK companies-verified.csv:5), icp-detail.md:563 licensed markets (US/UK/EU-EEA, no Ukraine), and the flavour sums (6-13 / 2-6); fixes sent back to hypothesis-generator as targeted edits, not a regeneration
  top_issue: the size gates (validated ≥15 / stop <10 / metrics floor 10) leave 10-14, the author's own most likely outcome, undefined; step 2 would guess
---

# QC Report — hypothesis-generator — 2026-09-14

**Artifact:** `workspace/outbound/campaigns/2026-09-14-eu-erakulis-similar/hypothesis.md`
**Total: 13/20** — marginal

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Vadim's standing decisions are carried over correctly:
  - ICP floor stays at 50 (L18, L39); the 25 floor was not imported.
  - No client names (L248).
  - No pricing (L249).
  - The only proof is 34K with no geography (L124, L248); UK Meds 7.5K is not used.
- The author's transcript shows the required reading was done: registry status was run, and the 07-21, US, AU and UK campaigns, ICP §8, competitors.md and the message-1 template were read.
- The prompt says the segment should be narrow enough that 30 companies is realistic. The author's own estimate is 7-13 at 50+ (L78), and the validation bar of 15 (L190) sits above that estimate.
- The Ukraine proposal (L97, L258) argues from script mapping and profile coverage. It never cites the ICP universal exclusion on markets not licensed for compliance (`icp-detail.md:563`), and that exclusion is the rule Vadim is actually being asked to waive.

### B. Factual accuracy — 2/5
- **3DLOOK claims are clean.**
  - 80+, under 45 seconds, the body-composition outputs, the 34,000 figure, photo deletion, encryption, the GDPR roles sentence and "FitXpress is not a medical device." all match `proof-points.md` / `yazen.md` / CLAUDE.md §12 verbatim.
  - Erakulis is not in `case-studies/`, but Vadim confirmed it as a client (UK `STATUS.md`). The hard fail does not apply.
- **112,100 (L263) is listed but not cleared.** The figure appears verbatim at `proof-points.md:113` (Aggregate table, source "Internal", next to ARR) and `overview.md:35`.
  - Vadim's 2026-09-12 decision licenses two anonymised facts only: 34K with no geography, and 7.5K as "a UK online pharmacy".
  - The artifact asks about 112,100 (Open question #6) and does not use it, which is correct. "Anonymous by construction" is the author's argument, not a clearance.
- **Sourcing.** 33 external URLs. The author had no WebFetch and never curled a source, so every citation comes from a search-result summary and no page was opened. Spot-check against the author's own search results:
  - Supported:
    - RevenueCat 68% annual / ~30% cancelled in month one (L111).
    - EuropeActive 75.5M / +5.8% / €39.1B (L114).
    - Welltech 810 employees / 220M installs (L118).
    - Foodvisor Jan 2026 / 22 and Fitatu Jul 2025 / 56 (L170-171).
    - Lifesum 67 / "60+" (L271).
  - **L117, Kilo "€404 million consolidated revenue in 2025".** The cited PR Newswire release is dated 12 Nov 2025 (mirror `bebeez.eu/2025/11/12`), so it cannot report a closed 2025. Treat it as unverified, probably a forecast.
  - **L127, Freeletics "reported to be testing phone-camera rep counting".** No search result in the transcript contains this. L133 then escalates it to "Freeletics already runs camera computer vision in its workout flow", which is the premise of the build-objection answer.
- **Internal numbers wrong:**
  - L116, "six companies of 27-36 people". NowPatient has 53 (`2026-09-01-uk-erakulis-similar/companies.md:38`), and the UK `STATUS.md` says five plus a pharmacy.
  - L78, totals. The flavour estimates (L55, L56, L64, L76) sum to 6-13 at 50+ and 2-6 near-misses, not 7-13 and 3-8. The 3-8 is repeated at L256.
- **L140, unsourced legal claim.** "The regulation that applies is GDPR... No country-level rule changes the case." It contradicts Open question #7 (Article 9, EU AI Act).
- **Anti-case facts without URLs:**
  - "Freeletics under Infront since 2022" (L173, L270): true per the author's search, but no link.
  - "Yazio's corporate majority owner" (L173): unnamed and unsourced.
- L133 says Erakulis went "live in weeks". Nothing sources that for Erakulis. The only internal basis is the generic "2-4 weeks for basic integration" (`icp-detail.md:597`), and the artifact does not cite it.
- L139 DiGA "class I or IIa" matches the search summary, but is likely outdated: the 2024 DigiG extended DiGA to class IIb. Low impact, the anti-case holds either way.
- **Geo and registry checks, all clean:**
  - No proposed target is UK-, US- or AU-HQ as proposed.
  - Simple (L61) is flagged as a London conflict with a conditional route to `katerina`.
  - ZAVA, Juniper, WeightWatchers and Second Nature are correctly treated as out of market.
  - None of the 13 named companies has a hit in `olena-registry.json` or `global-company-registry.json`.
  - Erakulis is absent as a company. The 4 string hits are the UK campaign slug inside notes, so the claim at L166 is correct.
- Internal facts verified:
  - 07-21 funnel (`post-mortem.md:15-24,157,171,246`).
  - 54 olena slugs.
  - 15.4-18.8% reply range, 48% of invites in two accounts, the Chief Subscription & Content Officer reply (US `post-mortem.md:25-30`).
  - English-only replies and template.
  - `PROFILE_GEO` gap (`outbound-pipeline.py:93-97`).

### C. Brand & tone — 2/3
- L271: "verify by hand". This is a hard ban in `terminology-guardrails.md` (use "manually").
- The corrective "X, not Y" construction recurs: L55, L78, L124, L146, L168, L264.
- No em dashes, no banned words from messaging.md. The register is direct and short-sentence. It is an internal document, so these weigh lightly.

### D. Format & structure — 2/3
- Frontmatter is complete (`product`, `profile`, `market`, `created`, `status`) and the path is correct.
- Deviations from the prompt template:
  - Use case (L106) is 3 sentences against "1 sentence".
  - "Why plausible" has 4 reasons against 3.
  - Heading is "Open questions" instead of "Open questions for Vadim".
- The H3 titles "Sub-segment: …" and "Target buyer persona: …" do get hashed by `hypothesis-gate` (`SCOPE_HEADINGS` substring match), so the scope lock covers the near-miss rule and the HQ table.

### E. Output quality — 3/4
- Strong, specific and usable:
  - Binding near-miss file rule (L40).
  - HQ resolution table (L92-102).
  - Invite caps built from measured failures (L157-160).
  - The message-1 gate closes the 07-21 cause (L205-210).
  - Open questions are decision-shaped, and the channel-conflict question (#5) is a genuine catch.
- **Step 2 cannot act on list size without guessing.**
  - Validated needs 15 or more (L190), stop is under 10 (L191), falsified is under 10 and under 18 with near-misses (L217), and the success-metrics floor is 10 (L237).
  - At 10-14 companies, the author's own most likely outcome, the list is neither validated, stopped nor falsified.
- L195 says blocked rows are not counted as verified, while L271 keeps Lifesum on the main list after a manual check. Whether it counts toward the threshold is undefined.
- L219 falsifies the segment when reply rate is under 5%, with no minimum accepted count and no time window. At about 10-14 accepted invites, 0 replies would falsify it.
- L211 says "positive across the sequence" while L242 says "of accepted": two denominators for the same metric.

## Top 3 issues (priority for improver)

1. **Validation criteria contradict the author's own sizing.**
   - The bar is 15 or more at 50+ (L190) against a realistic 7-13 (L78).
   - The 10-14 band is undefined across L191, L217 and L237.
   - The reply-rate falsification (L219) has no minimum sample.
   - Step 2 will hit the undefined case first.
2. **Two third-party claims do not hold up against the author's own search results.**
   - Kilo's €404M "in 2025" (L117) comes from a release dated 12 Nov 2025.
   - Freeletics camera rep counting (L127) appears in no result, and L133 hardens it into "already runs camera computer vision" to support the build objection.
3. **Wrong internal numbers and one unsourced legal claim.**
   - "Six companies of 27-36" (L116): NowPatient is 53.
   - Flavour totals (L78, L256): the estimates sum to 6-13 and 2-6.
   - "No country-level rule changes the case" (L140) contradicts Open question #7.

## Coordinator review

