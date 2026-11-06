# Sales Navigator pull — 2026-11-05-latam-insurance-underwriting

Profile: **katya** · generated 2026-11-05 from the hypothesis (```titles block).

**Pull by TITLE inside the company list, never by company alone.** A company-only
pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export
and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of
Product, brand GMs) were missing from both.

## 1. Current company (16)

- Icatu Seguros
- MAG Seguros
- Bradesco Vida e Previdência (Bradesco Seguros)
- Brasilseg (BB Seguros)
- Allianz Brasil
- Azos
- AXA Seguros México
- Seguros Banorte
- HSBC Seguros México
- BBVA Seguros México
- MAPFRE México
- RGA Mexico (Reinsurance Group of America)
- SCOR Mexico
- Swiss Re Brasil
- Swiss Re Mexico
- Hannover Re Mexico (Hannover Re)

## 2. Current job title (47 titles)

Paste into «Current job title» (Boolean):

```
"Chief Underwriter" OR "Underwriting" OR "Chief Medical Officer" OR "Medical Director" OR "Head of Life" OR "Individual Life" OR "Life Products" OR "Life & Health" OR "Life and Health" OR "Chief Product Officer" OR "Head of Product" OR "Bancassurance" OR "Actuarial" OR "Innovation" OR "Chief Technology Officer" OR "Chief Information Security Officer" OR "Data Protection Officer" OR "Subscrição" OR "Aceitação" OR "Diretor Médico" OR "Diretora Médica" OR "Consultoria Médica" OR "Diretor Técnico" OR "Diretora Técnica" OR "Superintendente Técnico" OR "Vida Individual" OR "Seguros de Pessoas" OR "Produtos Vida" OR "Produtos de Vida" OR "Prestamista" OR "Habitacional" OR "Atuária" OR "Atuarial" OR "Inovação" OR "Proteção de Dados" OR "Suscripción" OR "Selección de Riesgos" OR "Dictaminación" OR "Dictamen Médico" OR "Director Médico" OR "Directora Médica" OR "Seguros de Personas" OR "Producto Vida" OR "Productos de Vida" OR "Actuaría" OR "Innovación" OR "Protección de Datos"
```

Exclude:

```
NOT ("Engineer" OR "Developer" OR "Designer" OR "Recruiter" OR "Accountant" OR "Support" OR "Intern" OR "Assistant" OR "Scrum Master" OR "QA")
```

## 3. Export

Save the CSV into `workspace/outbound/campaigns/2026-11-05-latam-insurance-underwriting/sales-nav-raw/`, then:

```
scripts/outbound_pack.py next --campaign 2026-11-05-latam-insurance-underwriting
```
