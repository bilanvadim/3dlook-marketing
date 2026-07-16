# People Extraction Log — 2026-07-16-au-telehealth

- **Source files:** 1 CSV (Telehealth_Australia - Sheet1.csv, provided by Vadim)
- **Raw rows total:** 443 (640+ lines in file, multi-line values merged by parser)
- **After dedup (by LinkedIn URL):** 439
- **After C-level filter:** skipped (per pipeline design — filtering happens in icp-validator)
- **After company-match filter:** skipped (all contacts kept; company shortlist not pre-filtered)
- **Final: 439 people across 14 companies**

## Companies

| Company | Contacts |
|---------|----------|
| Medibank group (Medibank + Health Solutions + Private) | 195 |
| Bupa Australia | 117 |
| HCF group (HCF Australia + HCF + HCF Eyecare) | 100 |
| Mosh | 14 |
| InstantScripts | 6 |
| Medmate | 2 |
| qoctor / Qoctor | 3 |
| Hopstep | 1 |
| Amplar Health | 1 |

## Seniority distribution

| Level | Count |
|-------|-------|
| C-Level | 98 |
| VP | 2 |
| Director | 134 |
| Manager | 135 |
| Individual Contributor | 70 |

## Notes
- All contacts have LinkedIn URLs — 100% enrichment
- All contacts are in Australia
- 98 C-Level contacts is strong for an outbound campaign
- The CSV already includes company descriptions and fit analysis — data quality is high
- No email addresses available (expected — this is a LinkedIn-first campaign)
