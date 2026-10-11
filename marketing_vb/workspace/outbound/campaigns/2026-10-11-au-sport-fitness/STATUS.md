---
product: fitxpress
profile: vadim
campaign: 2026-10-11-au-sport-fitness
stage: 5 · messages written, QC failed (10/20), fix round pending
updated: 2026-10-11
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
| 5 messages | 325 people / 650 messages in 12 batches; gate passes (0 hard, 321 soft); **QC 10/20 failed** | `messages/`, `card-messages.md`, `messages/_coordinator-scan-2026-10-11.txt` |

SEND by lane: referral 225, product 39, partnerships 22, operations 16, member-experience 13,
technical-integration 10. Largest groups: Fernwood 36, Fitstop 33, Jetts 30, BFT 23 (cap 50).

## Tomorrow: the fix round (QC report `workspace/_quality/outbound/2026-10-11-message-sequencer-au-sport-fitness.md`, fix list by batch with person_ids)

1. **Card first, before any writer runs** (edit `hypothesis.md`, then `card --for messages`):
   - technical-lane data note: "deletable by scan ID" → deletion by scan identifier **on the customer's request**; photos deleted immediately after processing or within 30 days **per the customer's policy**; the deletion line goes in M2 only, never M1, and only in the technical-integration lane;
   - call length: one rule campaign-wide. Default proposed: **no call length** (34 M2s name 10/15/20 minutes today). Ask Vadim if he wants one fixed length instead;
   - give the speed sentence as a target shape, not one sentence to copy (it repeats 22× and 12×);
   - add an M2 variation rule: every referral M2 carries a value line tied to that person's own M1 topic, its own easy-out target and closer; never ask a unit owner to judge whether it fits their club.
2. **Regenerate the referral M2s** of `_batch-bft` (20) and `_batch-jetts-fitness` (23 ids in the report), keeping M1s. Then line-fix every other batch from the report's list, sending **the same rule list to every batch** (2026-10-07 lesson). Batch order for shared brands: fernwood-fitness-1, then -2 reading it. Write the missing `_summary-fernwood-fitness-2.md`.
3. `check-messages` over the whole campaign + rerun `_coordinator-scan` (scratch checker: call length, deletion in M1, speed variants, first-five-words per company, shared sentences ≥5 per company); then a second opus QC. Below 12 → stop and tell Vadim.
4. Vadim's checkpoint on a sample, then `build-import` → `outbound-registry.py record` (dry run first; pass `--waive-companies`-equivalent context: the six brands are already in vadim's registry) → commit + push.

## Open items for Vadim (not blocking the fix round)

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
