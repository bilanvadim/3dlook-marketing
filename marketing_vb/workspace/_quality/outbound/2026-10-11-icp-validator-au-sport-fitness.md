---
qc_date: 2026-10-11
agent: icp-validator
artifact: workspace/outbound/campaigns/2026-10-11-au-sport-fitness/icp-validation-summary.md; workspace/outbound/campaigns/2026-10-11-au-sport-fitness/decisions.md
track: outbound
artifact_type: icp-validation
product: fitxpress
profile: vadim
total_score: 18/20
status: excellent
coordinator_review: done
---

# QC Report — icp-validator — 2026-10-11

**Artifact:** `workspace/outbound/campaigns/2026-10-11-au-sport-fitness/icp-validation-summary.md` + `decisions.md`
**Inputs scored against:** `card-validate.md` and `people-compact.csv` (342 rows: 316 export, 26 Apollo). Scope: Vadim's "maximum use of the list", so a wide SEND is intended. Limits, signature, bans, detector and completeness were checked by code and are taken as fact here.
**Total: 18/20** — excellent. Fix the five points below before message-sequencer runs.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **The card's rule "directors at head office whose unit is unclear: P2 `product`" is applied unevenly.**
  - Jon Davie (decisions l.84), Martin Oliver (l.213) and Emily Crawford (l.278) get `product` P2. All three are empty profiles.
  - Michael Nysten (l.308) is also "World Gym director with no unit named", at the same company as Jon Davie with the same title and the same empty profile. He gets `referral` P4.
  - The same evidence also leads to `referral` for Andrea F. (l.41), Clow John (l.66) and Matt Rees (l.38).
  - The split matches the card's forecast counts, but the reasons are identical and the outcomes differ. None of this appears under "Lane calls beyond the card". Only Brendon Li On Wing and Josh Mildren do.
- **Card rules the agent followed correctly:**
  - All 7 `registry:` rows are FAIL with the registry wording.
  - The 3 HOLD rows (Eamon H., Nikita Fernandes, Rhys Holleran) are not sent. They are recorded as FAIL with a "HOLD:" reason because the tool allows only PASS, WEAK or FAIL.
  - The duplicates (Bec Kirkup, Thomas Hepburn), the collision (Jack Revens) and the parody profile (K Potassium) fail exactly as the card says.
  - All 11 company-named and no-name profiles are WEAK.
  - Of the two Burn profiles, Melissa is PASS and Mel is WEAK, which keeps the card's one-profile-per-person rule.
  - The Collective Wellness checks (Mark Grey, Lauren Anliev) and the current-role checks (Tim Horskins, Peter Reed) end in WEAK.
  - The top-up marketing heads go to `member-experience` P2, as the card says.
  - Per-account totals reconcile with the verdict table for Fernwood 38, Jetts 30, BFT 23, UBX 18, Genesis 8, ASN 7 and World Gym 6.

### B. Factual accuracy — 5/5
- I checked the counts against `decisions.md`, and every count holds: PASS 308 (P1 58, P2 33, P3 10, P4 207), WEAK 20, FAIL 14, `send=SEND` 308.
- The "50 PASS rows from the export carry empty-profile" figure also holds: 69 flags, minus 14 on WEAK or FAIL rows, minus 5 in the top-up.
- The concerns quote the rows correctly: Zoe Skanavis's "Marketing Coordinator" headline, Harry Konstantinou's World Gym directorship, Chris Caldwell's Fitstop NED seat, and the 7 GMs plus 3 social/marketing managers at Anytime.
- No product numbers and no client names.
- Observation only, no deduction: some reasons say "on his/her row" for evidence that came from the card, not from the compact row. Harry Konstantinou (l.158) has title "Director" and an empty headline, yet the reason says "CEO and MD". Melissa Jones (l.295) has a row that shows Baby Spa, not Fernwood. Rhianna Buchanan's reason (l.168) is labelled "per card", which is the honest form.

### C. Brand & tone — 3/3
- No banned words. The only em dashes are in the template headings. The register is plain and fits an internal checkpoint.

### D. Format & structure — 3/3
- The frontmatter is complete (`product: fitxpress`, `profile: vadim`, `stage`, `status`).
- `decisions.md` is pipe-delimited and has a reason on every PASS and WEAK row.
- All template sections are present. The SEND table lists all 101 P1-P3 rows and groups the P4 rows by account, which is a sensible compression.

### E. Output quality — 3/4
- **Zoe Skanavis (`zoeskanavis`, l.321) is PASS P2 despite a stale-role signal.** Her headline reads "Content Creator, Personal Trainer, Marketing Coordinator". The agent's own concern says one Vision marketing title "is probably stale". The card's stop condition is "a profile shows the person has left (drop)". James Duffy (`jamesduffy26`) gets the same `member-experience` ask at the same 17-person account.
- **Some alias rows carry the other employer's senior title into the SEND file, and the summary does not warn the writers.**
  - Kylie Falconer (`kylie-falconer-8b2b70123`, l.137) is "Chief Executive Officer" in the KX Pilates group. Selina Bridge, KX's real CEO, is messaged too. Kylie's reason does not say that her CEO title belongs to Bare & Wilde.
  - Scott Bumpstead (`scott-bumpstead`, l.13) is "Chief Executive Officer" in BFT. His reason does explain it.
  - Jonathan Pepper (`jonpepper`) is "Founder and Managing Director" in Fitstop.
  - Philip Grasso, Ben Seymour, Anthony Hoang and Tom Bayford are "Founder".
  - Mike Knights and Andrew Baildon are "Managing Director" in Jetts.
- **Damien Mavroudis (`damien-mavroudis-9865154a`, l.72) is P1 at Sweat, a registry-held brand, with a known duplicate-CEO conflict.** The problem is noted under concerns ("the job-change check must settle it before send") but is not among the numbered questions for Vadim.
- **Greeting hygiene is not flagged.** In `people-validated.csv`, `first_name` = "Anthony Dickens" (`anthony-dickens-fernwood-fitness-23bb4225`) and "Catijn (Kate)" (`catijnschierbeek`, who goes by Kate). Some names are all caps or lowercase: NATHAN (`nathan-james-fitnesscartel`), LEIGH (`leigh-j-24a0b1a0`), sarina (`sarina-sham-64b20321`), mel (`mel-antila-17171a165`), travis (`travis-spencer-83a2aa370`). The script parses names, but the checkpoint summary is where Vadim would see this.
- **Some row signals are unaddressed.**
  - Matt Eikenhout (`matt-eikenhout-154a3ba3`, P1, l.198) has the headline "National Manager Supp Society", and his reason ignores it.
  - Nina Al-Bahrani (`nina-al-bahrani-65bb73123`, l.138) passes her card-mandated current-role check on the same title cell that triggered the check: empty profile, headline is a Surrey degree. Peter Reed and Tim Horskins, on the same kind of evidence, went WEAK.
  - Two referral asks go into the same studio, with no note: BFT Hindmarsh (Scott Bumpstead l.13, Steve Grace l.156) and BFT Fitzroy (sarina sham l.80, Valentin U. l.223).
- **No PASS is a name collision, a non-AU person outside the card's rule, a person at an OUT account, or anyone on the HOLD list.** The only non-AU PASS is Michael Ramsey (US), which the card sanctions. The one junk-looking PASS, `thomas-hepburn-09084559` ("Preparing for the Zombie apocalypse", no roles), is kept because the card mandates it. The agent correctly raised it as question 6.
- **The rest of the summary is strong.** The pools A-D come with names, angles and `promote` commands. NovoFit Open question 11, the Eamon H. HOLD and the FLG sale stop condition are all carried forward. The never-mention pairs and the Apollo-quality notes are specific.

## Top 3 issues (приоритет для improver)

1. **Stale-role and duplicate-CEO PASSes need a gate before send.**
   - `zoeskanavis`: move to WEAK until the job-change check, and keep `jamesduffy26`.
   - `damien-mavroudis-9865154a`: add it as a numbered question for Vadim, or WEAK it until the job-change check confirms Sweat as current.
   - `matt-eikenhout-154a3ba3`: verify the "Supp Society" headline.
2. **Apply the "director, unit unclear" lane rule one way.**
   - Either move the empty-profile `jon-davie-70660122`, `martin-oliver-4a5508138` and `emily-crawford-4835ba212` to `referral` P4, which is safer because product-lane copy misreads a franchisee director.
   - Or move `michael-nysten-791685333`, `andifiorenza`, `clow-john-29144a18` and `matt-rees-9067779` to `product` P2.
   - Either way, add one line to the summary.
3. **Writer handoff for alias titles and names.**
   - Add a Top-concerns line: "alias rows carry the other employer's title; never address by title".
   - Append "CEO title is Bare & Wilde" to the reason for `kylie-falconer-8b2b70123`.
   - Normalise `first_name` for `anthony-dickens-fernwood-fitness-23bb4225` (Anthony) and `catijnschierbeek` (Kate), plus the 5 casing cases, before message-sequencer runs.

## Coordinator review

agreement: ✅ agree
top_issue: stale-role and duplicate-CEO PASSes (zoeskanavis, damien-mavroudis-9865154a, matt-eikenhout-154a3ba3) and the uneven "director, unit unclear" lane; both go into one validator fix round together with Vadim's checkpoint answers, plus the first-name clean-up and the alias-title note for writers.
