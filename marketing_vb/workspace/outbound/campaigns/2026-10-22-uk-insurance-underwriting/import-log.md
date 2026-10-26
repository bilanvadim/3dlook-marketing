# Closely.io import — 2026-10-22-uk-insurance-underwriting

Built 2026-10-26 by `outbound_pack.py build-import` from people-validated.csv (send == SEND) and `messages/`. 176 people, 0 skipped.

Sequence: connection request with no note → Message 1 right after acceptance → Message 2 five days later.

| File | People | When |
|---|---:|---|
| `closelyhq-import.csv` | 176 | now, everyone at once |

## After the import

```
scripts/outbound-registry.py record --campaign 2026-10-22-uk-insurance-underwriting --profile katerina
```
