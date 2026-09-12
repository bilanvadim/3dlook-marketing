# Closely.io Import — 2026-09-01-uk-erakulis-similar

- **Rows:** 26
- **Skipped:** 0
- **Estimated daily send:** ~30-50 connection requests / day
- **Estimated campaign duration:** ~1-2 weeks
- **Sequence:** connection request (no note) → Message 1 (immediately after acceptance) → Message 2 (+5 days)
- **Closely.io credits:** ~78 (26 connection requests + 26 × message 1 + 26 × message 2)

## Recipients by tier and angle

| Tier | Count | Primary personas |
|---|---|---|
| PASS-P1 (5) | Founder/CEO, Head of Product at small apps (32–36 employees). Build-vs-buy and differentiation-LTV decision-makers. | danielhutson1 (Nutracheck), drzubairahmed (Medicspot), james-charalambous-9b955328 (Fiit), ryan-sherreard (Coopah), pete-cooper-coopah (Coopah) |
| PASS-P2 (3) | CTO/Co-founder or Head of Data Product. Technical integrator and product ownership angles. | oliverbrooks (Medicspot), eleanor-bennett-a3229957 (Nutracheck), jack-yaxley-b8132892 (Nutracheck) |
| PASS-P3 (1) | Partnerships Manager. Partnership and integration angle. | daisy-ford-4350b7373 (Nutracheck) |
| WEAK-P3 (17) | Engineering leads, senior engineers, compliance leads, operations, investors, other specialists. Evaluators and champions, not direct buyers. | 17 people across Medicspot, Infohealth Ltd (NowPatient), Fiit, Coopah, WithU |

## No skipped people

All 26 approved contacts (9 PASS + 17 WEAK) have message files and passed validation:
- Message 1: ≤ 600 chars
- Message 2: ≤ 550 chars  
- Both messages present
- All LinkedIn URLs populated
- Identity fields (name, company, title) complete

## Valdim — next steps

1. Open https://app.closelyhq.com/
2. Import `closelyhq-import.csv`
3. Configure the sequence:
   - **Connection request:** no note (invite only)
   - **Message 1:** immediately after connection acceptance
   - **Message 2:** +5 days after Message 1
4. Set sending schedule (recommended: 30–50 requests/day, business hours per profile geography)
5. Launch campaign
6. Reply to Telegram bot "started" to mark campaign checkpoint

## After import: update exclusion registries

```bash
python3 /home/vadim_prod/3dlook-marketing/marketing_vb/scripts/outbound-registry.py record \
    --campaign 2026-09-01-uk-erakulis-similar \
    --profile katerina
```

This updates:
- `/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/exclusions/katerina-registry.json`
- `/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/exclusions/global-company-registry.json`

---

**Build timestamp:** 2026-09-12T11:45:00Z  
**Source files:**
- people-approved.csv (26 records, 9 PASS + 17 WEAK)
- people-raw.csv (identity data, emails, companies, titles)
- messages/{person_id}.md (26 message pairs)

**Validation:** ✓ python3 scripts/outbound-pipeline.py check-import --campaign 2026-09-01-uk-erakulis-similar
