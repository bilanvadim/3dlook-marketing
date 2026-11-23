# Sales Navigator pull — 2026-11-22-uk-connected-fitness

Profile: **katerina** · generated 2026-11-23 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (34)

- PureGym
- The Gym Group
- Virgin Active (UK)
- Fitness First UK
- Bannatyne Group
- Everyone Active (SLM)
- Places Leisure
- Serco Leisure (MORE)
- Fusion Lifestyle
- Better (GLL)
- Ultimate Performance
- Xercise4Less
- Nuffield Health (clubs)
- David Lloyd Leisure
- Gymbox
- énergie Fitness (Empowered Brands)
- Freedom Leisure
- Total Fitness
- Buzz Gym
- My PT Hub
- PT Distinction
- Fitr
- Kahunas
- PT Minder (Software Minder Limited)
- Coach Catalyst
- Fisikal
- ClubRight
- myFitApp (vendor of Places Leisure app)
- Shreddy (Rose Appellations Limited)
- EvolveYou (EvolveYou App Ltd)
- The Body Coach
- Nutracheck
- Coopah
- 10XU (formerly WithU Group)

## 2. Current job title (37 titles)

Paste into «Current job title» (Boolean):

```
"Chief Product Officer" OR "Chief Digital Officer" OR "VP Product" OR "Head of Product" OR "Director of Product" OR "Product Director" OR "Head of Digital" OR "Digital Director" OR "Head of Digital Product" OR "Head of App" OR "Product Owner" OR "Senior Product Manager" OR "Lead Product Manager" OR "Product Manager" OR "Head of Member Experience" OR "Director of Member Experience" OR "Head of Digital Experience" OR "Digital Experience Manager" OR "Head of Innovation" OR "Head of Training" OR "Head of Fitness" OR "Fitness Director" OR "Head of Personal Training" OR "Head of Coaching" OR "Head Coach" OR "Head of Programming" OR "Head of Wellbeing" OR "Head of Partnerships" OR "Partnerships Director" OR "Partnerships Manager" OR "Head of Business Development" OR "Head of Integrations" OR "Chief Technology Officer" OR "Chief Executive Officer" OR "Managing Director" OR "Founder" OR "Co-Founder"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-11-22-uk-connected-fitness/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-11-22-uk-connected-fitness
```
