# Sales Navigator pull — 2026-10-29-us-insurance-underwriting

Profile: **nick** · generated 2026-10-30 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 0. Geography (manual, the script writes none)

Add the filter **Geography → United States** to the search. The reinsurers, John Hancock, Foresters and iPipeline have global company pages; without it the pull brings UK, EU and Canada staff (katerina's and olena's people, Canada FAILs).

## 1. Current company (32)

- Prudential Financial
- Northwestern Mutual
- MassMutual
- Guardian Life (Guardian)
- Lincoln Financial
- John Hancock
- Pacific Life
- Protective Life
- Transamerica
- Principal Financial
- Nationwide
- Securian Financial
- Corebridge Financial
- Symetra
- Penn Mutual
- Mutual of Omaha
- Ameritas
- Foresters Financial US (Foresters Financial)
- Sammons Financial (North American Company)
- Thrivent
- The Standard
- Ethos
- Ladder Life
- RGA US (Reinsurance Group of America)
- Gen Re US (Gen Re)
- Munich Re Life US (Munich Re)
- Hannover Life Re America (Hannover Re)
- SCOR Life Americas (SCOR)
- Swiss Re Americas (Swiss Re)
- iPipeline US (iPipeline)
- Zinnia
- Bestow

## 2. Current job title (67 titles)

Paste into «Current job title» (Boolean):

```
"Chief Underwriting Officer" OR "Chief Underwriter" OR "Head of Underwriting" OR "VP Underwriting" OR "SVP Underwriting" OR "Vice President of Underwriting" OR "Vice President, Underwriting" OR "AVP Underwriting" OR "Underwriting Director" OR "Director of Underwriting" OR "Director, Underwriting" OR "Head of Life Underwriting" OR "VP Life Underwriting" OR "President, Life Underwriting" OR "AVP Life Underwriting" OR "Director, Life Underwriting" OR "Underwriting Innovation" OR "Underwriting Strategy" OR "Underwriting Research" OR "Underwriting Rules" OR "Underwriting Philosophy" OR "Underwriting Analytics" OR "Accelerated Underwriting" OR "Automated Underwriting" OR "Algorithmic Underwriting" OR "Underwriting Solutions" OR "Client Underwriting" OR "Underwriting Manager" OR "Chief Medical Officer" OR "Medical Director" OR "Head of New Business" OR "VP New Business" OR "President, New Business" OR "AVP New Business" OR "Director, New Business" OR "Director of New Business" OR "Head of Individual Life" OR "President, Individual Life" OR "VP Individual Life" OR "SVP Individual Life" OR "AVP Individual Life" OR "Director, Individual Life" OR "Head of Term Life" OR "VP Term Life" OR "Director, Term Life" OR "Head of Individual Disability" OR "Head of Disability Income" OR "President, Individual Disability" OR "VP Individual Disability" OR "VP Disability Income" OR "AVP Disability Income" OR "Director, Disability Income" OR "Director, Individual Disability" OR "Head of Life Product" OR "VP Life Product" OR "Director, Life Product" OR "Head of Product" OR "Chief Product Officer" OR "Head of Life Pricing" OR "VP Life Pricing" OR "Director, Life Pricing" OR "Head of Innovation" OR "Digital Transformation" OR "Insurtech" OR "Chief Technology Officer" OR "Chief Information Security Officer" OR "Chief Privacy Officer"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Scrum Master" OR "QA" OR "Annuity" OR "Annuities" OR "Retirement" OR "Group" OR "Worksite" OR "Workplace" OR "Voluntary" OR "Dental" OR "Medicare" OR "Investment" OR "Wealth" OR "Asset" OR "Property" OR "Casualty" OR "P&C" OR "Personal Lines" OR "Commercial Lines" OR "Specialty" OR "Marine" OR "Cyber" OR "Surety" OR "Mortgage" OR "Liability" OR "Claims" OR "Distribution" OR "Sales" OR "Wholesaler" OR "Brokerage" OR "Business Development" OR "Marketing" OR "Compliance")
```

Campaign adjustments applied by the coordinator 2026-10-30 (hypothesis l.105): `Assistant` removed (it drops every spelled-out Assistant Vice President), line-of-business and function exclusions added for the whole search. If Sales Navigator rejects the length, run the same company list twice (titles down to `"Medical Director"`, then the rest) and save both exports in `sales-nav-raw/`; `extract-people` keeps one row per person. A company over 80 rows is re-run alone without `"Underwriting Manager"`, then without the function lines.

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-10-29-us-insurance-underwriting/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-10-29-us-insurance-underwriting
```
