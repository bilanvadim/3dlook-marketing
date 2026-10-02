---
qc_date: 2026-10-02
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-08-14-au-digital-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-10-02, au-digital-fitness (upgrade of the 2026-08-17 approval)

**Artifact:** `workspace/outbound/campaigns/2026-08-14-au-digital-fitness/hypothesis.md`
**Total: 15/20** (good)

**Scored against:** the hypothesis-generator prompt · the approved 2026-08-17 version · `companies-verified.csv` (26 rows) and `companies.md` · `compliance.md` §1, §9 · `proof-points.md` · `accuracy-formulations.md` §1.1-1.4 · `icp-detail.md` §8 and :597 · `audience.md` §3 · the 07-27 AU and 08-07 US post-mortems · the 09-29 cardiometabolic hypothesis (decision 4 wording) · `outbound_pack.py` CARD_SECTIONS (:729-737) and `apollo-pull.py` targets (:255-274) · the 10-02 Virta QC for calibration.

**What reaches the message writer:** `Use case`, `Rules for steps 3-5`, `Message angle` (including "What each account already has" and the company facts) and `Vadim's standing decisions`.

**Taken as given:** Vadim's standing decisions. Limits, bans, the detector and completeness are checked by code.

**Limits of this QC:** this session has no web tool, so no source was re-fetched. Verdicts are judged on the quoted evidence and on internal consistency. It has no shell either, so notify.py was not run.

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
- **Done as briefed:** all 26 companies re-checked, with per-company facts, seven lanes, Rules, a titles block, the frontmatter keys and every standing decision. The approved strategy is kept and every change is listed (lines 422-431). The 08-17 open questions are resolved or carried over (line 409).
- **Two HQ checks are shallow, and both decide which profile owns the company:**
  - The Fast 800 (line 90): the Perth head office rests on a single aggregator (Dealroom). The legal entity and app publisher are UK (Healthlab Online Limited). Line 416 cites the Companies House officers page but never says what it shows. Open question 9 (line 406) treats Perth as settled and only asks about UK staff, never about which profile owns the account.
  - Defeat Diabetes (line 91): the HQ comes from an unnamed "business listing". `companies.md` row 18 still says "not verified".
- **Line 358 is stale.** It says `companies-verified.csv` has no `icp_fit` or `hq_country` and that the Fast 800 row needs its domain fixed. The CSV now has both columns, `exclude` on exactly AUFIT-01, 04, 08, 09, 10, 19 and 22, and `website` = thefast800.com.

### B. Factual accuracy: 3/5
- **The compliance line is not verbatim from `compliance.md`, and it is filed as a Vadim decision.**
  - Line 305: "We encrypt data in transit and at rest, and delete photos after processing or within 30 days." This is the §9 US line with the HIPAA clause cut. Every claim is FAQ-backed (§3, §5), and line 305 says openly that the line is derived.
  - However, the sentence exists nowhere in `compliance.md`, and §9 / "SEO and pages" says only verbatim statements are pre-approved.
  - Decision 4 (line 349) reads "Every other lane carries exactly one, the neutral sentence in Rules", under "Built in, not open questions". Vadim's 2026-09-29 decision (`us-cardiometabolic/hypothesis.md:332`) was "the US variant verbatim from `compliance.md`".
  - The new sentence would go into every non-referral Message 2 without sign-off. It is not among the 10 open questions.
- **dorsaVi's OUT reason is inconsistent (line 83).** The main reason, the pivot, comes from an aggregator (TipRanks) quoting an ASX use-of-funds line. The second reason, "camera-based human measurement is its own product (adjacent to the competitor exclusion)", would also exclude VALD. VALD stays IN (line 93) and carries VAL4 "HumanTrak 3D movement analysis" (line 284).
- **Vitruvian (line 92):** the only source is August 2025, and its headline says the product "resurfaces with update". OUT still holds: the CSV shows a pre-launch holding site on 2026-10-02, and line 326 makes pre-launch an anti-case. The verdict should cite that, not the 14-month-old article.
- **Carded "already has" entries with no source** (the verdict table quotes none of them):
  - Sweat "step and hydration trackers" (244)
  - Digital Wellness "weight sync from health apps" (241)
  - 12WBT "weigh-ins" (245)
  - Fernwood "FWD tracks workouts, habits and milestones" (249)
  - Xyris "an old 'measures' screen was retired in 2024" (251)
- **"2-4 weeks" is listed under "Numbers only from `proof-points.md`" (line 307).** It actually lives in `icp-detail.md:597`. It is not capped: the card injects it from there, and earlier QCs licensed it.
- **Clean on the focus items:**
  - Eucalyptus to Hims & Hers (Business Wire, closed 2026-06-02).
  - Catapult (its own fact sheet, "Boston (Head)").
  - Centr (Wikipedia, backed by Athletech).
  - Perx (CB Insights, consistent with a US-payer business).
  - Sleepfit HELD (App Store date, a stale partner brand, no news).
  - All 13 partial-overlap accounts are quoted with a link, and the count (12 + Sweat) agrees in lines 29, 140, 252, 310 and 389.
  - Post-mortem figures check out: 38/220, 5/38, 22 vs 202, 3/28, 1/80, 45%, 0/60.
  - Accuracy and repeatability wording matches `accuracy-formulations.md` §1.1, §1.2 and §1.4. The speed wording is verbatim.
  - No client is named outside ban instructions. The 34,000 line has no name and no geography.
  - No Australian-law claim is made, and the TGA question gets only the UK/EU MDR sentence (line 178).
- **Sourcing:** about 70 external URLs, mostly primary: App Store listings with release numbers, company pages, the Sweat Zendesk API, Business Wire, the Catapult fact sheet.

### C. Brand & tone: 2/3
- **The use-case sentence (line 119, carded verbatim) keeps the gap framing and the "so" benefit construction.** "so an Australian app ships the body-scan feature its wearable and nutrition data already implies". The same card bans both in Rules (lines 310, 316), and line 142 says every card line was rewritten as a capability. The sentence was edited in this upgrade, yet that clause stayed.
- Line 123 (not carded): "body measurement still arrives by hand or by appointment". "By hand" is a terminology hard ban, and the clause is a gap framing.
- **Otherwise clean:** person-first wording, the Kic rule, no before-and-after, no outcome promises. The "objective", "seamless" and "comprehensive" traps appear only as bans.

### D. Format & structure: 3/3
- No issues. The frontmatter is complete (`product`, `profile`, `market`, `status`, `use_case`, `cap_per_group: 50`, `banned_terms`). The titles block has one title per line. Every template section is present, including the Message 1 gate. The path is correct.

### E. Output quality: 3/4
- **Some carded lane lines fail for part of their lane:**
  - `wellbeing-programs` (line 262) says "between in-person assessments", but only AIA has one. Nothing in-person is verified at Springday (digital assessments, SPD3) or at Sonder.
  - `clinical` (line 261) says "next to the waist, weight, HbA1c, glucose or lab data the program already records". That covers Vively, Everlab and Digital Wellness, whose waist data line 239-241 marks "never claim either way".
- **The last row of "What each account already has" (line 252)** puts "No body measurement, scan or composition feature found" in the **Verified** column, for Kic, 28, Emily Skye FIT, Fitaz, VALD and Sonder. That hands the writer an absence as a verified fact.
- **Three hooks lean toward banned framings:**
  - HAP3 (line 274), "already includes body-scan … partners", invites setting the scan against the scanner.
  - SND3 and SND4 (line 289), "a published Trust Centre" and "medically accredited", invite compliance and medical wording that line 305 bans.
  - AIA4 (line 275), "two-step verification", puts "verification" next to an insurer.
- **Inherited and not re-tested:** 8 IN companies have zero feature criteria (`companies.md`: Kic, 12WBT, Fitaz, The Fast 800, Defeat Diabetes, Fitstop, Xyris, Sonder). The feature screen on line 62 requires at least one. This is covered by "kept as approved", but it is not stated.
- **Strong otherwise:** a real displacement search (26 releases, a help-centre API), "not verified" kept apart from "verified", the 9amHealth/Signos precedent applied, honest floors (17% acceptance, inconclusive below 15 accepts), and live-asset checks with retired wording fenced off (lines 291-298).

## Top 3 issues (priority for improver)

1. **The compliance line (line 305) is not verbatim from `compliance.md`, and decision 4 (line 349) presents it as built in.** Vadim's 09-29 decision required the `compliance.md` variant verbatim. Either get Vadim's sign-off on the cut sentence as a new open question, or carry no compliance line in AU cold copy until then.
2. **Carded lines that will produce errors or gap framing:**
   - the use case's "so … ships the body-scan feature its … data already implies" (119);
   - "between in-person assessments" for Springday and Sonder (262);
   - waist in the `clinical` line for Vively, Everlab and Digital Wellness (261);
   - an absence under "Verified" (252);
   - the HAP3, SND3/SND4 and AIA4 hooks.
3. **Profile-deciding HQ evidence is thin:**
   - The Fast 800: one aggregator against a UK legal entity, and OQ9 asks the wrong question.
   - Defeat Diabetes: an unnamed listing.
   - dorsaVi: the second reason contradicts VALD IN.
   - Line 358 is stale against the current CSV.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: a derived compliance sentence was presented as Vadim's standing decision; it becomes an open question (default: no compliance line in AU cold copy) and all 14 fixes go back to hypothesis-generator before the list is stamped.
```
