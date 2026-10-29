# Sales Navigator pull — 2026-10-29-eu-insurance-underwriting

Profile: **olena** · generated 2026-10-29 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (32)

- Irish Life Assurance
- Zurich Life Ireland (Zurich Life)
- New Ireland Assurance
- Aviva Ireland (Aviva)
- Royal London Ireland (Royal London)
- Acorn Life
- AXA Life Europe
- Allianz Lebensversicherungs-AG (Allianz / Allianz Deutschland)
- Alte Leipziger Lebensversicherung
- Swiss Life Deutschland
- HDI Lebensversicherung
- LV 1871
- Die Bayerische
- Hannoversche Lebensversicherung
- Volkswohl Bund
- Europa Lebensversicherung
- CosmosDirekt
- Dialog
- Nationale-Nederlanden
- a.s.r.
- Achmea
- Allianz Nederland Leven (Allianz Nederland)
- Scildon
- Swiss Re Switzerland (Swiss Re)
- Munich Re Germany (Munich Re)
- Hannover Re Germany (Hannover Re)
- SCOR France (SCOR)
- Gen Re Germany (Gen Re)
- RGA Ireland
- vers.diagnose
- Morgen & Morgen
- Munich Re Automation Solutions

## 2. Current job title (37 titles)

Paste into «Current job title» (Boolean):

```
"Chief Underwriting Officer" OR "Chief Underwriter" OR "Head of Underwriting" OR "Underwriting Director" OR "Director of Underwriting" OR "Underwriting Philosophy" OR "Underwriting Development" OR "Development Underwriter" OR "Underwriting Rules" OR "Underwriting Research" OR "Underwriting Manager" OR "Head of Underwriting Solutions" OR "Automated Underwriting" OR "Client Underwriting" OR "Underwriting Innovation" OR "Head of Life and Health" OR "Head of Life & Health" OR "Chief Medical Officer" OR "Medical Officer" OR "Head of New Business" OR "Head of Protection" OR "Protection Proposition" OR "Protection Pricing" OR "Risikoprüfung" OR "Antragsprüfung" OR "Gesellschaftsarzt" OR "Biometrie" OR "Medisch adviseur" OR "Acceptatie" OR "Chief Product Officer" OR "Head of Product" OR "Head of Innovation" OR "Digital Transformation" OR "Insurtech" OR "Chief Technology Officer" OR "Data Protection Officer" OR "Datenschutzbeauftragter"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-10-29-eu-insurance-underwriting/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-10-29-eu-insurance-underwriting
```
