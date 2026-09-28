# Closely.io Import — 2026-09-27-uk-bariatric-prequal

- **Rows:** 74
- **Skipped:** 0
- **Estimated daily send:** ~30-50 connection requests / day
- **Estimated campaign duration:** ~2-3 weeks (74 requests ÷ 35/day avg)
- **Sequence:** note-less invite → Message 1 (сразу после принятия) → Message 2 (+5 дней)
- **Closely.io credits needed:** ≈ 74 connection requests + 74×2 = 222 messages

## Campaign overview

- **Campaign:** 2026-09-27-uk-bariatric-prequal
- **Profile:** katerina (Katerina Galich, CEO)
- **Market:** UK
- **Product:** fitxpress
- **ICP:** UK bariatric pre-qualification (surgeons, operations directors, medical directors at private surgical weight-loss providers)
- **Contacts:** 74 validated + approved
- **Companies:** 15 (13 new to registry)

## Messages

All messages passed Vadim's 2026-09-28 approval checkpoint:

- **Connection note:** empty (note-less invite by design)
- **Message 1 (opener):** сразу после принятия запроса; avg 428/600 chars
- **Message 2 (follow-up):** +5 дней; avg 515/550 chars; includes compliance line (GDPR), article link, and calendar booking link

Messaging angles:
- consult-slots: 46
- glp1-bmi-history: 18
- one-record-two-jobs: 4
- pmi-preauth-pack: 1
- custom (finance/dietitian roles): 5

## Registry update

```
2026-09-27-uk-bariatric-prequal: 74 people (74 new), 15 companies (13 new) -> katerina
```

All 74 contacts and 15 companies now in `workspace/outbound/exclusions/katerina-registry.json` and `workspace/outbound/exclusions/global-company-registry.json`.

## Import gate result

```
✓ import CSV is sendable — 74 rows, identity and both messages present
Exit code: 0
```

All rows passed validation:
- All 74 have first_name, last_name, linkedin_url (primary identity fields)
- All 74 have both message_1 and message_2 present
- Message 1: all ≤600 chars
- Message 2: all ≤550 chars
- No empty required fields (email and connection_note are allowed to be empty)

## Special cases handled

- **Rishi Singhal (Healthier Weight)** and **Sandip Hindocha (Tonic):** explicitly cleared by Vadim on 2026-09-28 despite `company_same_profile` flag (new people, not the four excluded 07-31 contacts)
- **Finance and dietitian roles (5 people):** included at Vadim's 2026-09-28 checkpoint with custom angles (campaign-level override of persona exclusions)
- **Greg Jones and Marianne Sampson:** written as Optimise Weight Loss Surgery partners
- **Qutayba Almerie:** written in Phoenix Health bariatric capacity despite company field showing Circle
- **Debashis Ghosh:** message acknowledges his division (Breast/Plastics/etc.) and requests routing to the right division head

## Next steps for Vadim

1. Open https://app.closelyhq.com/
2. Import `closelyhq-import.csv` (74 rows)
3. Configure sequence in Closely:
   - Connection request: no note (by design)
   - Message 1: deliver immediately after connection acceptance
   - Message 2: deliver +5 days if no reply to Message 1
4. Set schedule: recommended 30-50 connections/day, business hours for UK market
5. Launch campaign
6. Reply to Telegram bot "started" to begin checkpoint tracking

## Files

- **Import CSV:** `/workspace/outbound/campaigns/2026-09-27-uk-bariatric-prequal/closelyhq-import.csv`
- **Registries updated:**
  - `/workspace/outbound/exclusions/katerina-registry.json` (74 new people)
  - `/workspace/outbound/exclusions/global-company-registry.json` (13 new companies)
- **Message approval:** `/workspace/outbound/campaigns/2026-09-27-uk-bariatric-prequal/messages/_summary.md`
