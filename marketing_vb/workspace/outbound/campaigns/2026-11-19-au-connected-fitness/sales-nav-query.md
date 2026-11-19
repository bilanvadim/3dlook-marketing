# Sales Navigator pull — 2026-11-19-au-connected-fitness

Profile: **vadim** · generated 2026-11-19 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (8)

- Les Mills International — https://www.linkedin.com/company/les-mills-international
- Les Mills New Zealand — https://www.linkedin.com/company/les-mills-new-zealand
- CityFitness — https://nz.linkedin.com/company/cityfitness
- Fluidform — https://www.linkedin.com/company/fluidform-pilates
- Studio Pilates International — https://www.linkedin.com/company/studio-pilates-international
- 28 by Sam Wood (now evvr.) — https://au.linkedin.com/company/28-sam-wood
- Michelle Bridges 12WBT — https://au.linkedin.com/company/12wbt
- Transform by Fitaz — https://www.linkedin.com/company/fitazfk

## 2. Current job title (31 titles)

Paste into «Current job title» (Boolean):

```
"Founder" OR "Co-Founder" OR "Chief Executive Officer" OR "Managing Director" OR "General Manager" OR "Chief Product Officer" OR "Chief Digital Officer" OR "Head of Product" OR "Director of Product" OR "Product Manager" OR "Senior Product Manager" OR "Product Owner" OR "Head of Digital" OR "Head of Digital Product" OR "Digital Product Manager" OR "Head of App" OR "Chief Technology Officer" OR "Head of Technology" OR "Head of Engineering" OR "Head of Programming" OR "Head of Training" OR "Head of Education" OR "Head of Fitness" OR "Fitness Director" OR "Head Coach" OR "National Fitness Manager" OR "Head of Member Experience" OR "Head of Partnerships" OR "Partnerships Manager" OR "Business Development Manager" OR "Franchise Business Manager"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-11-19-au-connected-fitness/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-11-19-au-connected-fitness
```
