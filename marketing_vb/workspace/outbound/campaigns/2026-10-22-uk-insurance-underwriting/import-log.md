# Closely.io import — 2026-10-22-uk-insurance-underwriting

Built 2026-11-09 by `outbound_pack.py build-import` from people-validated.csv (send == SEND) and `messages/`. 284 people, 0 skipped.

Sequence: connection request with no note → Message 1 right after acceptance → Message 2 five days later.

| File | People | When |
|---|---:|---|
| `closelyhq-import.csv` | 285 | full list (the first 176 rows went into closely.io on 2026-10-26, text unchanged) |
| `closelyhq-import-widening-2026-11-09.csv` | 109 | the widening of 2026-11-09 (108 people) and Dorottya Norton (named referral): the only file to import now |

Widening approved by Vadim 2026-11-09 («апрув»), referral included on his word («додавай»). Built with `--force`: the gate still fails 6 messages of 2026-10-26 on «let», a rule added 2026-11-02, after they were sent. The widening file was cut from the full file by LinkedIn URL against the 2026-10-26 file; every one of the 176 earlier rows is byte-identical.

## Named referrals (drafts sheet → outbound-referrals.json)

- 2026-10-20T15:45:50+03:00: added:2026-10-22-uk-insurance-underwriting

## After the import

```
scripts/outbound-registry.py record --campaign 2026-10-22-uk-insurance-underwriting --profile katerina
```
