---
qc_date: 2026-10-07
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/hypothesis.md (+ companies.csv)
track: outbound
artifact_type: hypothesis
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-07

**Artifact:** `workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/hypothesis.md` + `companies.csv`
**Total: 17/20** — good

Code had already checked limits, signature, bans, the detector and completeness, so those are taken as fact. This report scores the judgment calls, the fit to the persona and the copy rules.

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
- **"Use as many contacts as possible" holds at company level.** Every function at an IN account gets a lane (l.204). The OUT reasons fit Vadim's five allowed categories, and the borderline exclusions have their own open questions with defaults: GymBeam and the retailers (OQ1), Oviva (OQ2) and TATOI (OQ7).
- **Apollo decision 3 is applied inconsistently.** `apollo_topup=no` on Vivafit (160 LI staff; export has only a partner-owner, a technical director and 4 club owners), maju (77 staff, CEO only) and Nutrimed (79 staff; the only contact is held for an identity check, so the account could end up empty). Head-office digital, product and clinical people are missing at all three, and decision 3 (l.409) makes that a `yes`. Read-this-first #5 (l.27) also says each row's `notes` gives the flag and its reason. The notes for Nutrimed, maju, SATISFEAT and Vivafit say only "apollo_topup=no." (csv l.9, 14, 16, 21).
- **The person-level standard is uneven.**
  - Nanda Zwart (row 27, l.84; her headline says "Eigenaar bij Het 1 op 1 dieet") is OUT as an "unrelated business". Four other 1:1 Diet consultants are IN as referral, and one-person cells such as `Dsign.`, `LM2S Consulting` and `Balance Centrum` were aliased.
  - ludo glav (MAJU owner, no page, l.133) is OUT. Mihalis Atsalakis (Nutrimed owner, no page, l.139) is IN with an identity check.

### B. Factual accuracy — 4/5
- Every copy-facing product number comes from `proof-points.md` and its wording: 2 photos, "under 45 seconds from the photos to structured results", 80+ body measurements, 96-97% (body measurements only), §1.2 repeatability, 38-210 kg, 34,000 anonymised with no geography, 112,100 as 3DLOOK-wide scale, 100+ clients. No client is named. Market figures have links (WHO 59%, Euronews and service-public for France).
- **Validation criteria vs csv (l.416):** the text says "`icp_fit` high (10) or medium (12)", but `companies.csv` has high 9, medium 13. Step 2 will check against the wrong numbers.
- **Weakly sourced company facts the copy may use:**
  - FX2 (l.327), "the same company runs FITOMAT smart gyms", is inferred from a shared officer on implisense. The export lists FITOMAT as a separate LinkedIn page (founded 2022, 35 staff).
  - VF1 (l.330), "members book classes in the VivaFit app", has no App Store entry, unlike the other apps. The csv itself notes vivafit.pt redirects to the group and the LinkedIn site field is a "vivafitsoon" placeholder.
- **Unsourced OUT basis:** "its app is a shop" (GymBeam, l.58) and "app is shop and loyalty" (BioTechUSA, l.61). No GymBeam or BioTechUSA source is in Sources (l.463). The export About text alone supports the verdict (D2C e-commerce; supplement maker and shops). The app claim is unchecked.
- **Source mismatch (csv l.10):** "zanadio after the aidhere acquisition" cites `femtechinsider.com/sidekick-health-acquires-pink/`, an article about the PINK! deal. The fact is not copy-usable (SK1 bans deals), so the impact is low.
- **Internal inconsistencies:**
  - l.420 "1 reply on 67 sends" (boilerplate from the prompt) contradicts l.186 "73 accepted, 4 replies" (matches `metrics-final.json`).
  - The re-entry precedent is dated 2026-09-28 in l.25 and 2026-09-27 in csv l.10.
- **Sourcing:** 3 external market links, 7 external account links and about 15 named account sites. Proportionate for an outbound hypothesis.

### C. Brand & tone — 3/3
- No issues. Zero em/en dashes in either file. No banned words outside the ban list itself (l.372). Claims discipline is intact: no eligibility, diagnosis or treatment framing (l.362, l.371); "team compares scans it selects"; person-first language; compliance lines verbatim from `compliance.md` §9, limited to A/B/D product/clinical/ops/tech.

### D. Format & structure — 3/3
- No issues. The frontmatter is complete and parseable: `product`, `profile`, `market`, `use_case`, `cap_per_group`, `referral_call: yes`, `banned_terms`. The `titles` block is present. Every template section is there. The section titles match `CARD_SECTIONS`, so lanes, the facts table, the asset table and decisions all reach the messages card, and the verdict table and open questions reach the validate card. `companies.csv` has 22 rows, Continental-Europe `hq_country`, and aliases written with ` - ` where the alias parser would split on `/`.

### E. Output quality — 3/4
- **Copy rules, question in M1 and call in M2:**
  - **What holds:** l.358 states the rule for every lane, referral included, and explicitly overrides step 5 of the M1 template ("quick chat?"). `referral_call: yes` turns on the gate's hard checks (question in M1, no link in M1, calendar link in every M2). Product, clinical, referral and partnership lanes restate it.
  - **Gaps:**
    - The `operations` lane (l.295) says nothing about M1 or M2. The `technical-integration` lane (l.296) says only "Message 2 links the FAQ". The global rule and the card's Sender block cover both, but the lane text alone would read as no call.
    - A call ask in M1 is only a soft flag in the gate (`outbound_pack.py` l.1742), so the prose rule carries that weight.
    - In the referral lane (l.298), the M1 question "who at head office owns the client app" and the M2 easy out "or point me to whoever runs the client app at head office" are the same ask twice.
- **RNPC presupposes an app it does not have.** The csv (l.2) records "No client app found (App Store FR)". But the RNPC question themes (l.337), the referral easy out (l.298) and the segment A angle "in its app" (l.273) all assume one. The no-app fact is not in "What the accounts already record" (l.289: "Everyone else: nothing verified"), and the sequencer reads only that section, not csv notes. 27 RNPC referral messages are at risk. Dietplus (site 403) and Naturhouse are unknown.
- **The off-ICP line is drawn unevenly.**
  - GymBeam, BioTechUSA, HSNG, MM Sports and Body & Fit OUT is defensible against `icp-detail.md`: no FX segment covers supplement or sportswear e-commerce, and §8 lists fitness apps, coaching, training and subscription platforms, not retail.
  - AMRA Medical (MRI analytics) is IN as "partnership only" (l.18, l.45). It matches no segment, and the 10-06 UK hypothesis explicitly cited a Vadim scope decision for partnership-only accounts. This one cites none.
  - Meanwhile GymBeam's "Director of B2B, Strategic Partnerships ... in Nutrition and Fitness" is OUT with the rest of GymBeam. OQ1 does not mention a partnership-only option.

## Top 3 issues (priority for improver)

1. **RNPC copy will assume an app RNPC does not have.** The csv records no RNPC client app, but the RNPC question themes, the referral easy out and the segment A angle all assume one. The fact never reaches the messages card, putting 27 referral messages at risk. Add an RNPC writer note under "What the accounts already record", and the same for Dietplus and Naturhouse while their apps are unknown.
2. **Apollo top-up ignores decision 3 at Vivafit, maju and Nutrimed.** These three get `apollo_topup=no` with head-office product, digital and clinical people missing, and the notes give no reason, though l.27 says every row has one. Nutrimed's only contact is pending an identity check.
3. **The off-ICP and identity standards are applied unevenly.** AMRA is IN as partnership-only with no segment or scope decision behind it, while GymBeam's B2B/partnerships director is OUT. Nanda Zwart, a self-declared 1:1 Diet owner, is OUT as an "unrelated business". ludo glav is OUT while Mihalis Atsalakis, the same no-page owner case, is IN. Also fix the icp_fit counts at l.416 (10/12 vs actual 9/13).

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: RNPC's angle (29 people, 27 referral) and the Dietplus/Naturhouse question themes assume a client app the artifact's own companies.csv says RNPC lacks, and the fact never reaches the messages card; Apollo top-up was left off at Vivafit, maju and Nutrimed against Vadim's decision 3, and the junk/IN calls (Nanda Zwart, ludo glav vs Mihalis Atsalakis, AMRA) are uneven against "use as many contacts as possible". Fixes go to a fresh hypothesis-generator with only hypothesis.md, companies.csv and this report (no resume: the first pass ran 426K tokens).
```
