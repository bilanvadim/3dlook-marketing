# Closely.io Import — 2026-08-07-us-digital-fitness (batch1)

- Rows: 124
- Skipped: 0
- Estimated daily send: ~30-50 connection requests / day
- Estimated campaign duration: ~3-4 days to send all connection requests
- Sequence: note-less invite → Message 1 (сразу после принятия) → Message 2 (+5 дней)
- Closely.io credits needed: ≈ 124 connection requests + 124×2 messages

## Batch composition
- 67 contacts drafted in this run (from `people-validated-msg-batch1-missing.csv`)
- 57 contacts drafted in a prior run (already present in `messages-batch1/`)
- 1 contact (784558785580, Emily Yeung) appeared in both the existing folder and the missing list — regenerated with identical content, not double-counted. 58 pre-existing files + 66 net-new files = 124 unique person_ids.

## Verification performed
- `messages-batch1/` contains exactly 124 `.md` files, one per person_id in `people-validated-msg-batch1.csv`.
- Every row in `closelyhq-import-batch1.csv` has a non-empty `linkedin_url` (124/124 confirmed via grep).
- No duplicate `contact_id` values (124 unique).
- Every row's Message 2 carries the `nick` profile's calendar link (https://meetings.hubspot.com/nick-omelchak), 124/124.
- Message 1 ≤ 600 chars / Message 2 ≤ 550 chars per the outbound templates (spot-checked across angles: member-engagement, weight-management, digital-transformation, technical-integration).

## Skipped people
- None.

## Vadim — next steps
1. Открой https://app.closelyhq.com/
2. Импортируй `closelyhq-import-batch1.csv`
3. Настрой sequence в Closely: запрос в друзья БЕЗ note; Message 1 — сразу после принятия; Message 2 — через 5 дней
4. Настрой расписание (recommended: 30-50 connections/day, business hours US market)
5. Запусти кампанию
6. Ответь боту в Telegram «started» — мы начнём считать дни до первого checkpoint
