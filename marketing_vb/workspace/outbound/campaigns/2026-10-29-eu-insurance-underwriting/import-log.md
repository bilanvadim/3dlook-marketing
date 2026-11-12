# Closely.io import — 2026-10-29-eu-insurance-underwriting

Rebuilt 2026-11-12 (widening, Vadim «апрув») by `outbound_pack.py build-import` from people-validated.csv (send == SEND) and `messages/`. 177 people, 0 skipped.

Sequence: connection request with no note → Message 1 right after acceptance → Message 2 five days later.

| File | People | When |
|---|---:|---|
| `closelyhq-import.csv` | 177 | full list: the 128 of 2026-11-02 (already in closely, byte-identical) + 49 new |
| `closelyhq-import-widening-2026-11-12.csv` | 49 | **import this one**: the new people only (widening 29 + «додай усіх» 20), cut by LinkedIn URL |

## After the import

```
scripts/outbound-registry.py record --campaign 2026-10-29-eu-insurance-underwriting --profile olena
```

The 128 imported on 2026-11-02 must not be uploaded again; closely gets only `closelyhq-import-widening-2026-11-12.csv`.
