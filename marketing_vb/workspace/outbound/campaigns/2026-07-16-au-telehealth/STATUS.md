# STATUS — 2026-07-16-au-telehealth

**This campaign was never sent.** Its `closelyhq-import.csv` holds 253 rows with
`first_name`, `last_name` and `linkedin_url` blank in every single one, so closely.io
could not have accepted it — and Closely has no campaign whose `contact_source` matches
its header.

The AU campaign that DID run is `2026-07-27-australia-telehealth` (Closely 138392, 220
invites → 38 accepted → 61 messages → 5 repliers). It was built from this folder's people
list, which is why contact overlap briefly mis-filed its replies here on 2026-09-02;
`closely-pull.py map-campaigns` now resolves it by the uploaded file's header instead.

What was moved to `2026-07-27-australia-telehealth/`: `responses-classified.csv`,
`responses-summary.md`, `post-mortem.md` (each carries a provenance note).
What is in `_misfiled-2026-09-02/`: this folder's copy of `responses-raw.csv` and
`metrics-final.json`, kept as the record of the mis-filing.

Still usable here: `people-validated-with-identity.csv` (439 rows, identity restored
2026-09-02) if this list is ever re-run. Any re-run needs messages regenerated — the 253
in `messages/` are the pre-2026-08 4-touch format and 253/253 break the current 600-char
cap and the em-dash ban.
