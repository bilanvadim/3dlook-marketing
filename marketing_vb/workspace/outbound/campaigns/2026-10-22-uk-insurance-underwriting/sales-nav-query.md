# Sales Navigator pull — 2026-10-22-uk-insurance-underwriting

Profile: **katerina** · generated 2026-10-22 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (23)

- Aviva — https://uk.linkedin.com/company/aviva-plc
- Legal & General — https://www.linkedin.com/company/legal-&-general
- Royal London — https://uk.linkedin.com/company/royallondon
- Liverpool Victoria (LV=) — https://uk.linkedin.com/company/lv
- Zurich UK — https://www.linkedin.com/company/zurich-insurance-company-ltd
- VitalityLife — https://uk.linkedin.com/company/vitalityuk
- Scottish Widows — https://uk.linkedin.com/company/scottish-widows
- Guardian Financial Services — https://uk.linkedin.com/company/guardian-financial-services
- The Exeter — https://www.linkedin.com/company/exeter-family-friendly
- Cirencester Friendly Society — https://uk.linkedin.com/company/cirencesterfriendly
- Holloway Friendly — https://uk.linkedin.com/company/holloway-friendly
- British Friendly — https://uk.linkedin.com/company/british-friendly-society
- Shepherds Friendly — https://uk.linkedin.com/company/shepherds-friendly-society
- Swiss Re UK — https://www.linkedin.com/company/swiss-re
- Munich Re UK Life Branch — https://www.linkedin.com/company/munich-re
- Hannover Re UK Life Branch — https://www.linkedin.com/company/hannover-re
- Gen Re UK — https://www.linkedin.com/company/gen-re
- RGA UK — https://www.linkedin.com/company/rga-reinsurance-group-of-america-incorporated
- SCOR UK — https://www.linkedin.com/company/scor
- Pacific Life Re — https://www.linkedin.com/company/pacific-life-re
- UnderwriteMe — https://www.linkedin.com/company/underwriteme
- Iress UK — https://www.linkedin.com/company/iress/
- iPipeline UK — https://www.linkedin.com/company/ipipeline/

## 2. Current job title (32 titles)

Paste into «Current job title» (Boolean):

```
"Chief Underwriting Officer" OR "Chief Underwriter" OR "Head of Underwriting" OR "Underwriting Director" OR "Director of Underwriting" OR "Underwriting Philosophy" OR "Development Underwriter" OR "Underwriting Development" OR "Underwriting Rules" OR "Underwriting Research" OR "Underwriting Manager" OR "Head of Underwriting Solutions" OR "Client Underwriting" OR "Automated Underwriting" OR "Chief Medical Officer" OR "Medical Officer" OR "Head of New Business" OR "Head of Protection" OR "Protection Director" OR "Protection Proposition" OR "Protection Pricing" OR "Head of Life and Health" OR "Chief Product Officer" OR "Head of Product" OR "Head of Innovation" OR "Innovation Director" OR "Innovation Manager" OR "Underwriting Innovation" OR "Digital Transformation" OR "Insurtech" OR "Chief Technology Officer" OR "Data Protection Officer"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-10-22-uk-insurance-underwriting/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-10-22-uk-insurance-underwriting
```
