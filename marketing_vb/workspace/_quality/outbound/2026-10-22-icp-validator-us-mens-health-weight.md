---
qc_date: 2026-10-22
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: nick
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-22

**Artifact:** `icp-validation-summary.md` + `decisions.md` (result: `people-validated.csv`, `skipped-detail.md`)
**Scored against:** `card-validate.md`, `people-compact.csv` (78 rows: 44 Sales Navigator, 34 Apollo), plus the coordinator's facts: the six decision-3 medical directors are Quimbo, Flottmann, Threlkeld, Peterson, Carman and Barr; Haleem Mohammed is the HQ global CMO; the registry check is clear for all 78; and an outside fetcher also got 403 from marekhealth.com. Code already checked the mechanics, and that is taken as fact.
**Total: 16/20**, good. Every card P1/P2/P3 row and lane is matched, and every count reconciles. The defects are elsewhere:
- the decision-3 count is wrong, and it produces a question that has no basis;
- two WEAKs go against the card;
- the Hone reasons will not keep step 5 apart.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Two WEAKs contradict the card.** Yash Kothari (decisions l.66) and Tyler Dyck (l.75) are WEAK for being "outside the title filter".
  - Card l.73 says "Not the buyer: only the OUT and held rows". The standing decision at l.174 gives "a lane for every function at an IN company".
  - The title filter (card l.86) decides who gets pulled. It is not a validation rule.
  - Both people already qualify as PASS P3 `referral`. Pool D (summary l.129) asks for a hypothesis change to create that rule, but the rule already exists.
- **Decision 5 is read in the broader direction without asking Vadim.** Vadim's answer was "LaSara and DudeMeds stay IN (one founder-CEO each)" (card l.167). Jonathan Hancock is PASS P1 under the reading "keep decision, not a cap".
  - That reading is plausible, because the DudeMeds top-up names co-founders (card l.130).
  - The problem is where it was raised: only as a Top concerns bullet (l.144), not among the four confirm questions. If Vadim approves "SEND (68)", he approves Hancock without having been asked.
- **Lane changes, verdict:**
  - **Hancock → `operations`: good call.** It follows his COO title, and it keeps two co-founders at a tiny company off one `product` skeleton.
  - **Alba Mertira → `operations` P1: defensible.** She is a co-founder, was Head of Growth at Keeps, and card l.126 maps Hone growth and retention to `operations`. It is also disclosed (l.142).
    - But it lifts her from the card's marketing → `referral` slot straight to P1.
    - It also makes her the third Hone co-founder on P1 `operations` (see E).
- **Followed correctly:**
  - The prompt loop was followed: `decisions.md`, then apply-decisions and skipped, then the summary, with the pools in the first report.
  - Card placements were respected:
    - Stephen M. sits at HQ and Ampy T. at a clinic.
    - Ampy's constraints are carried.
    - Gameday Norcross is FAIL.
    - Jaci S. and the 4 thin Gameday profiles are WEAK under the `empty-profile` rule. The card itself asked for that check by name (l.36).
  - P4 is mapped to P3 `referral`, and this is disclosed.

### B. Factual accuracy — 3/5
- **The decision-3 set is wrong (summary l.29).**
  - The agent counts Elizondo as a medical director, although its own reason (decisions l.56) calls him a family nurse practitioner and Director of Clinical Services.
  - It moves Threlkeld and Peterson out as "owners", although their titles read "Owner and Medical Director" and "Medical Director/Owner".
  - The correct set is Quimbo, Flottmann, Threlkeld, Peterson, Carman and Barr: 6 of 6, exactly at the cap.
  - So the "7 against 6" case and the fallback "Carman would go to WEAK" have no basis, and Q4 (l.156) asks Vadim a question that does not exist.
  - Elizondo sits outside decision 3. He is the same profile as Pool F (clinic NPs), and the summary should say so.
- **The Pool F credits are wrong (l.131).** The summary says "about 26" remain under the 60 cap. `apollo-log.md` shows 38 credits consumed, because the 4 skipped rows were charged too. So 22 remain.
  - This is the same pattern the 2026-10-21 QCs caught: a number the agent did not have, stated as fact.
- **The Maximus coverage line contradicts itself (l.138).** It says Apollo found "none of the planned … growth … roles", then says it "added only a growth PM".
- **Checked and correct:**
  - The counts reconcile:
    - PASS 68 (21 / 30 / 17), WEAK 9, FAIL 1.
    - By group: Gameday 30 (HQ 11 + clinics 19), Hone 24, Maximus 7, Marek 4, DudeMeds 2, LaSara 1.
    - By angle: 14 / 12 / 10 / 10 / 10 / 7 / 5.
    - All 78 match `people-compact.csv`.
  - Haleem Mohammed is treated as HQ, P1 `clinical`, which matches the coordinator.
  - Every reason checks against the compact file. Examples: Hudnall's franchise history, Flottmann's telemedicine role, the Ron Noonan NJ clinics, and the Hot Springs pair.
  - No product numbers and no client names appear.

### C. Brand & tone — 3/3
- No issues. The em dashes appear only in template headings. The register is plain and specific.

### D. Format & structure — 3/3
- The frontmatter is complete: `product: fitxpress`, `profile: nick`, `campaign`, `created`, `stage`, `status`.
- `decisions.md` is pipe-delimited, every row has `wave` = 1, and the FAIL reason runs 5 words.
- All template sections are present. The headings are translated to English, which is acceptable.

### E. Output quality — 3/4
- **Step 5 will collapse into one skeleton at Hone (24 PASS, 35% of SEND).** The reasons inside each lane are nearly identical, and most of these Hone profiles have no headline or bio, so the reason is the sequencer's only hook. Its rule 2 needs different hooks and facts per person at one company.
  - `operations` P1: Seth Franz, "owns how the retest cycle runs" (l.20), and Stuart Blitz, "owns the operations behind the retest cycle" (l.67). Both are co-founders. Alba (l.61) makes a third co-founder on the same lane and priority.
  - `product` P1: Saad Alam (l.16) and Alex Treco (l.68) both get "the build-vs-buy call", the phrase from the prompt's own example.
  - `technical-integration` P3: Clark, Marhefka and Jerreck (l.12, l.14, l.24) all read "technical lane, P3 per card", word for word.
  - `operations` P2: Malocu (l.27) and Ayush S (l.62) both own "retention between retests".
  - Concern l.139 flags the density, but it names no trim list. "Vary copy by lane" does not help when 7-8 people share a lane.
- **The Marek gate is only in prose.** Decision 8 is still open: the coordinator confirms that an outside fetcher also got a 403.
  - Turner, Daru, Kling and Rose still have `send` = SEND in `people-validated.csv`. With one import file, nothing stops them from going out.
  - Flagging it (l.137, Q1) was right. A hold marker in the file was needed.
- **Pool F is shown with no recommendation.** Decision 7 counts success only as an HQ conversation, and clinic staff only point to HQ. 45 clinic NPs add little to that. Only 22 credits remain, not 26.
- **Gaps in the coverage and carry-over notes:**
  - The owner-gap concern (l.138) misses Hone. The card's Hone top-up asked for a chief medical officer or medical director first (l.126), and none was found.
  - Card l.71 bans using "the Hone founder's page" health story. Saad's reason (l.16) and the carry list (l.146-147) carry only Justin P.'s ban.
- **What holds:**
  - 7 of 9 WEAKs hold: Jaci, the 4 thin Gameday profiles, Julie Caputo, and Memo Canli.
  - The HQ/clinic split is clear in the SEND table.
  - The Hot Springs pair is put in different lanes and flagged.
  - The former-employer ban is extended correctly to Higgins (hims & hers), Mertira (Keeps) and Nyquist (AgelessRx).
  - Both unrun pre-import checks (Marek, displacement) are named first in Top concerns.

## Top 5 issues (приоритет для improver)

1. **Hone reasons will produce one skeleton in step 5.**
   - The duplicated reasons are Seth/Stuart (+ Alba) on P1 `operations`, Saad/Treco on "build-vs-buy", the three verbatim P3 tech reasons, and Malocu/Ayush.
   - Each same-lane pair at one company needs a distinct reason.
   - The density concern needs a concrete trim list. Candidates are the three P3 product generalists (Nyquist, Hung, Smith) and one of Clark/Marhefka.
2. **The decision-3 count is wrong.** Recount as 6 of 6 using the coordinator's set. Drop Q4 and the "Carman → WEAK" fallback. Mark Elizondo as an NP clinical director outside decision 3, the same profile as Pool F.
3. **Marek's 4 PASS sit as SEND while decision 8 is still open.** Both checks returned 403. They need a hold in the file, not only in prose, until a fetch from a US IP succeeds.
   - Pipeline issue for the improver: the card gives web re-checks (Marek, displacement) to a validator whose prompt limits it to reading two files. The check belongs to the coordinator before validate, or its result belongs in the card.
4. **Two WEAKs and one buried decision go against the card.**
   - Yash Kothari and Tyler Dyck are already PASS P3 `referral` under card l.73 and the standing lane rule. Pool D misstates that rule as missing.
   - The broader reading of decision 5 (Hancock) belongs among the confirm questions, not only in Top concerns.
5. **Factual slips and missing bans.**
   - 22 credits remain, not 26 (`apollo-log.md`: 38 consumed).
   - The Maximus "no growth role" line contradicts its own next clause.
   - The Hone founder's health-story ban (card l.71) is missing from Saad's reason.
   - Hone's missing medical lead is missing from the owner-gap concern.

## Notes outside the score
- **Memo Canli's question may not need asking.** The `geo:katya` flag maps the UAE to katya. CLAUDE.md §5 lists katya's outbound market as South America + Mexico, with Israel finished; the Gulf appears only in her social market. Check the flag's mapping before Vadim answers Q2.
- **Gameday's `company_slug` is broken.** In `people-validated.csv` it is a concatenation, `gameday-mens-health-gameday-mens-health-…-greater-madison-area`, on all 36 Gameday rows. This is code-side, but check it before import.
- **notify.py was not run.** This QC session has no shell tool, so the coordinator has to send the Telegram notice.

## Coordinator review

```
agreement: ✅ agree
top_issue: Several things are wrong in the decision files themselves.
- The decision-3 count is wrong: the Apollo pick was exactly 6 clinic medical directors (Quimbo, Flottmann, Threlkeld, Peterson, Carman, Barr), and Elizondo is an NP outside the cap.
- Marek's 4 people are marked SEND while decision 8 is open. They become WEAK with a decision-8 hold reason; after the US check they are added back with `promote`.
- Yash and Tyler go to PASS P3 referral under the standing rule.
- The Hone reasons need one distinct hook each before step 5.
The fixes go back to the same icp-validator (91K context, so resuming is cheap). The Gameday company_slug concatenation is how aliases are written: build-import and the registry use the canonical slug, as in 2026-10-16.
```
