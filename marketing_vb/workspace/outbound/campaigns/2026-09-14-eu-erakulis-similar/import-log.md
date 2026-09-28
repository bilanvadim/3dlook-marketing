# Closely.io Import — 2026-09-14-eu-erakulis-similar (olena)

- **Rows:** 125 in three files, 0 skipped
  - `closelyhq-import.csv` — **wave 1, 106** (product / retention / technical-integration / insurer-prevention)
  - `closelyhq-import-wave2.csv` — **wave 2, 12** referral asks (Welltech 2, BetterMe 1, Yazio 2, Freeletics 3, Lifesum 3, Fastic 1). Start after wave 1 at the same company has gone out.
  - `closelyhq-import-wave2-kilo.csv` — **Kilo wave 2, 7** referral asks. Start **one week after** Kilo's wave 1 (Renata Roze) goes out, regardless of acceptance.
- **Gate:** `outbound-pipeline.py check-import --file` → exit 0 on all three (identity + both messages present).
- **Sequence:** connection request with no note → Message 1 right after acceptance → Message 2 +5 days.
- **Daily send:** ~30-50 connection requests/day → wave 1 takes ~3-4 working days.
- **Before sending:** confirm Mohammad A. (Lifesum) and Cristina G. (Kilo) still hold those roles.

## Vadim — next steps

1. app.closelyhq.com → import `closelyhq-import.csv` on Olena's account, sequence as above, launch.
2. When wave 1 is out: import `closelyhq-import-wave2.csv`; a week after Kilo's wave 1: `closelyhq-import-wave2-kilo.csv`.
3. After import, update the exclusion registries:

```bash
python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/outbound-registry.py record \
    --campaign 2026-09-14-eu-erakulis-similar --profile olena
```

(`record` reads the campaign's import CSV; check with `--dry-run` that it counts all 125, since the wave-2 rows are in separate files.)

**Built:** 2026-09-28 from `people-approved.csv` (125 SEND, v4) + `messages/{person_id}.md`.
