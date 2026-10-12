---
product: fitxpress
profile: vadim
campaign: 2026-10-11-au-sport-fitness
stage: 6 · import built and recorded 2026-10-12; Vadim imports into closely.io
updated: 2026-10-12
---

# STATUS — 2026-10-11-au-sport-fitness (Vadim, Australia)

Vadim's fixed list «Au sport» (closely.io enrichment, Google Sheet
`1EPAaHNTPhg-nkWBoW2_iHEOaOMxSqLfxYm6JmcdxETU`, 386 people) plus a 26-person Apollo top-up.
His instruction: «максимально використовуй контакти в списку».
Stopped on Vadim's word on 2026-10-11 after the messages QC: «все запиши, закоміть і запуш,
я вже завтра продовжу».

## Where it stands

| Step | Result | Files |
|---|---|---|
| 1 hypothesis | approved 2026-10-11; QC 14/20 → fix round by a fresh agent; 44 accounts, 3 Vadim decision blocks (scope, approval, validation) | `hypothesis.md` (+ `-v1`, `-v2` snapshots), `companies.csv`, `hooks-by-company.md` |
| 2 companies | 45 verified (Genesis and Anytime sites block the VPS: warning only) | `companies-verified.csv`, `.hypothesis-lock.json` |
| 3 people | 342 = 316 from the export + 26 Apollo (Anytime 13, Vision PT 8, STRONG 5; 27 credits) | `sales-nav-raw/`, `apollo-*.csv`, `apollo-log.md`, `people-raw.csv` |
| registry | 7 already messaged from vadim → FAIL; company-level burn for Fernwood, Fitstop, Sweat, Mosh, KIC, Hapana **waived by Vadim** (46 rows) via the new `--waive-companies` flag | `people-checked.csv` |
| 4 validate | QC 18/20; Vadim approved + pools A, B, C promoted; **325 SEND**, 3 WEAK, 14 FAIL | `decisions.md`, `people-validated.csv`, `icp-validation-summary.md` |
| 5 messages | 2026-10-11: 650 written, QC 10/20. 2026-10-12 fix round: card rules 1-24 ("Coordinator decisions 2026-10-12"), three writer rounds (referral M2s regenerated at BFT, Jetts, KX, REVL, Genesis, UBX; sentence fixes elsewhere), QC2 13/20 after round 2, round 3 from the QC2 fix list verified mechanically: gate 0 hard / 79 soft (78 short company name), coordinator scan clean | `messages/`, `card-messages.md`, `messages/_fix*-2026-10-12.md`, `messages/_coordinator-scan-2026-10-12.txt`, QC `workspace/_quality/outbound/2026-10-12-message-sequencer-au-sport-fitness.md` |

SEND by lane: referral 225, product 39, partnerships 22, operations 16, member-experience 13,
technical-integration 10. Largest groups: Fernwood 36, Fitstop 33, Jetts 30, BFT 23 (cap 50).

## Next (2026-10-12)

**Vadim approved the texts on 2026-10-12** («1. апрув 2. та не треба 3. всіх беремо»; `hypothesis.md` → "Vadim's decisions 2026-10-12 (messages)"): no call length; Jason Clark, Matt Eikenhout and the six Fitness and Lifestyle Group people are sent; Eamon H. (Mosh) stays HOLD.

- `closelyhq-import.csv`: **325 rows, check-import exit 0**, one file, cap 50 per group held. The 11 pool A profiles got their LinkedIn display first name back for closely's identity column (`decisions.md`, last line); their greetings stay without a name.
- Registry: `outbound-registry.py record --profile vadim` done, 325 people, 44 companies (39 new). Mosh not recorded.
- **Vadim:** import `closelyhq-import.csv` into closely.io and start the campaign. Replies are pulled by the nightly cron.

### Fix round 2026-10-12 (done)

- Card: technical-lane data note rewritten (customer's policy / customer's request, M2 only); referral M2 described; "Coordinator decisions 2026-10-12" rules 1-19, then 20-24 after QC2.
- Round 1: one `message-sequencer` per batch from `_fix-<batch>-2026-10-12.md` (QC1 lines by person + coordinator scan); referral M2s regenerated from a per-person grid at BFT, Jetts, KX, REVL, Genesis, UBX; every other M2 read against rules 1-6.
- Round 2: bare / bolted speed sentences and gate near-duplicates (`_fix2-*`). A scan check on the "two photos + 80+" M1 core claim was tried and withdrawn (the core claim is allowed).
- QC2: 13/20. Fixed nearly every QC1 finding; found swaps (labels on fixed proof lines, stock speed sentences, the Jetts three-beat M2 block, card wording as copy).
- Round 3: `_fix3-*` = QC2 fix list + upgraded scan (labels, speed after an output noun, "brand decides" note, card wording, M2 phrase counts per company, central-question twins). Verified mechanically, no third QC.
- Coordinator scan script: scratchpad only (not in the repo); its last output is `messages/_coordinator-scan-2026-10-12.txt`.

## Open items for Vadim (closed 2026-10-12, kept for history)

- **Jason Clark** (BFT) owns BFT Ponsonby in **New Zealand**: keep in this AU send or drop?
- **Matt Eikenhout** (Viva): headline says National Manager Supp Society; QC says hold until his current role is confirmed.
- **Damien Mavroudis** (Sweat CEO): Adam Koch, messaged 2026-10-02, holds the same title; one is stale. Copy must not be the product-lane CEO pitch.
- **Fitness and Lifestyle Group** is in a sale process: stop condition, re-check before send (6 SEND).
- **Mosh**: Eamon H. stays HOLD until Katerina (who owns the live Mosh thread) says yes.
- NovoFit stays IN (Vadim 2026-10-11); EGYM never mentioned.

## Notes for the next coordinator

- One stage per session; start with `python3 scripts/outbound_pack.py next --campaign 2026-10-11-au-sport-fitness`.
- `apply-decisions` rebuilds `people-validated.csv` from `decisions.md`: re-running it drops the pool A-C promotions and the first-name fixes (Anthony, Kate, Nathan, Leigh, Sarina, Mel, Travis). If it must run again, repeat the `promote` commands and the name pass logged at the end of `decisions.md`.
- `outbound-registry.py check` for this campaign must carry `--waive-companies "Fernwood Fitness,Fitstop,Sweat,Mosh,KIC,Hapana"`.
- Gate false positive seen: "Plus Fitness" at a sentence start trips the "plus as a connector" ban.
