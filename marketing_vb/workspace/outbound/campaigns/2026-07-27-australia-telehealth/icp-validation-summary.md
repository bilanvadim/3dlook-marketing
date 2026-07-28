# ICP Validation Summary — Australia Telehealth Outbound

**Campaign:** 2026-07-27-australia-telehealth
**Product:** FitXpress
**Profile:** vadim (Vadim Bilan, Australia)
**Date:** 2026-07-27
**Pipeline:** icp-validator (batch 1 via Conductor + batches 2-4 via scoring script)

## Stats

| Category | Count | % |
|----------|-------|---|
| **Total reviewed** | 443 | 100% |
| **PASS** | 186 | 42% |
| — Priority 1 (C-level perfect fit) | 55 | 12% |
| — Priority 2 (Director/Head strong fit) | 97 | 22% |
| — Priority 3 (Supporting role) | 34 | 8% |
| **WEAK** | 38 | 9% |
| **FAIL** | 219 | 49% |

## By Segment

| Segment | PASS | WEAK | FAIL | Total |
|---------|------|------|------|-------|
| Enterprise (Medibank, Bupa, HCF) | 156 | 36 | 190 | 382 |
| Digital Health (Mosh, InstantScripts, etc.) | 30 | 2 | 29 | 61 |

## By Angle (for message-sequencer)

| Angle | Count |
|-------|-------|
| digital-health-strategy | 80 |
| product-integration | 40 |
| member-retention | 29 |
| clinical-operations | 28 |
| operational-scale | 18 |
| technical-integration | 10 |
| wellness-programs | 7 |
| executive-outcomes | 7 |
| data-privacy | 5 |

## Top 10 Priority 1 Contacts

| Name | Title | Company | Angle |
|------|-------|---------|-------|
| David Koczkar | Chief Executive Officer | Medibank | executive-outcomes |
| Lorraine Thomas | CEO & MD | HCF Australia | executive-outcomes |
| Yash Sodhi | Chief Strategy Officer | Medibank | digital-health-strategy |
| Shona Sundaraj | Group Medical Director | Medibank | clinical-operations |
| Andrew Wilson | Group Chief Medical Officer | Medibank | clinical-operations |
| Dr Jonathan Brown | Medical Director - BUPA Medical | Bupa Australia | clinical-operations |
| Milosh Milisavljevic | Group Lead - Chief Customer Officer | Medibank | member-retention |
| Emma Harrington | Chief of - Member Experience | HCF Australia | member-retention |
| David Lumb | Chief Officer, Member Growth | HCF Australia | member-retention |
| James Taylor | Chief Product Officer | Mosh | product-integration |

## Top Concerns

1. **49% FAIL rate** — nearly half the list is non-decision-makers (Branch Managers, Practice Managers, Dentists, Pharmacists, Store Managers, etc.). The Sales Nav export captured too broadly.
2. **WEAK group (38 contacts)** — titles with ICP signal but function mismatch (analytics, insights, design, HR-adjacent). Vadim should manually review before including.
3. **Enterprise dominates** — 156 PASS from Big 3 insurers vs 30 from digital health. Digital health segment may need its own targeted export.
4. **Priority 3 (34 contacts)** — supporting roles (IT managers, partnership managers, etc.). Consider excluding to save Closely.io credits.

## Recommendations for Vadim

1. **Include:** All 186 PASS contacts (priorities 1-3)
2. **Manual review:** 38 WEAK contacts — see `people-validated.csv`, filter `decision=WEAK`
3. **Exclude:** 219 FAIL contacts
4. **Next step:** Run message-sequencer with priority+angle enrichment for personalized messaging
5. **Future campaigns:** Tighter Sales Nav filters — exclude Branch Manager, Practice Manager, Store Manager, Pharmacist, Dentist, and all retail/operations titles upfront. This would save 200+ credits and reduce noise.
