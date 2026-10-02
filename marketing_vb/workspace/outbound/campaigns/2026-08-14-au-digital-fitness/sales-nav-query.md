# Sales Navigator pull — 2026-08-14-au-digital-fitness

Profile: **vadim** · generated 2026-10-02 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (19)

- Vively (Vively Health Pty Ltd)
- Everlab
- Digital Wellness (CSIRO Total Wellbeing Diet Online)
- Hapana
- AIA Australia (AIA Vitality)
- Sweat (The Bikini Body Training Company Pty Ltd)
- Kic (Kic App Pty Ltd)
- 28 by Sam Wood
- Emily Skye FIT (Loup Pty Ltd)
- Michelle Bridges 12WBT
- Transform by Fitaz (FitazFK Health Pty Ltd)
- The Fast 800
- Defeat Diabetes
- VALD
- Springday
- Fernwood Fitness
- Fitstop
- Xyris (Easy Diet Diary, FoodWorks)
- Sonder

## 2. Current job title (39 titles)

Paste into «Current job title» (Boolean):

```
"Founder" OR "Co-Founder" OR "Chief Executive Officer" OR "Managing Director" OR "General Manager" OR "Chief Operating Officer" OR "Chief Product Officer" OR "Head of Product" OR "Product Director" OR "Product Manager" OR "Head of Digital" OR "Chief Technology Officer" OR "Head of Engineering" OR "Chief Marketing Officer" OR "Head of Growth" OR "Head of Marketing" OR "Head of Retention" OR "Head of CRM" OR "Head of Member Experience" OR "Head of Customer Experience" OR "Head of Community" OR "Head of Coaching" OR "Chief Medical Officer" OR "Medical Director" OR "Clinical Director" OR "Head of Clinical Services" OR "Head of Nutrition" OR "Lead Dietitian" OR "Head of Research" OR "Head of Health and Wellbeing" OR "Head of Wellbeing" OR "Head of Vitality" OR "Program Director" OR "Head of Partnerships" OR "Partnerships Manager" OR "Head of Business Development" OR "Head of Integrations" OR "Head of Fitness" OR "Head of Training"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-08-14-au-digital-fitness/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-08-14-au-digital-fitness
```
