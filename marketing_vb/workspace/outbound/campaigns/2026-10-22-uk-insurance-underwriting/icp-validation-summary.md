---
product: fitxpress
profile: katerina
campaign: 2026-10-22-uk-insurance-underwriting
created: 2026-10-23
stage: validate
status: awaiting_review
---

# ICP Validation Summary — 2026-10-22-uk-insurance-underwriting

Validated in five `icp-validator` batches: Aviva 449 · Legal & General 298 · other Sales Nav companies 259 · Apollo gap top-up 135 (the 11 companies Sales Nav left empty) · Apollo title top-up 142 (the 12 Sales Nav companies, by hypothesis titles). The coordinator merged the decision files into `decisions.md` and ran `apply-decisions` and `skipped`. Batch sections below are the validators' own tables (the title top-up section is built from its decisions file: that validator's session ended before its report).

## Stats

1,283 people (Sales Navigator 1,006 + Apollo 277, 23 of 23 companies; Vadim approved 135 + 144 Apollo credits) · **PASS 160** (P1 31 · P2 72 · P3 57) · **WEAK 136** · FAIL 987 · excluded by registry 0 · cap 50 per group, largest group 21 PASS.

PASS by angle: underwriting 57 · reinsurance 36 · proposition 23 · referral 19 · technical-integration 14 · partnership 9 · medical 2

| Group | PASS | WEAK | FAIL |
|---|---|---|---|
| Aviva | 21 | 29 | 447 |
| Legal & General | 19 | 27 | 279 |
| Royal London | 18 | 14 | 107 |
| Pacific Life Re | 12 | 9 | 25 |
| Scottish Widows | 10 | 1 | 13 |
| Zurich UK | 8 | 15 | 23 |
| VitalityLife | 8 | 14 | 8 |
| Swiss Re UK | 8 | 3 | 4 |
| UnderwriteMe | 8 | 6 | 0 |
| Munich Re UK Life Branch | 6 | 3 | 4 |
| RGA UK | 6 | 0 | 1 |
| LV= | 5 | 5 | 43 |
| The Exeter | 5 | 1 | 9 |
| SCOR UK | 5 | 1 | 3 |
| Guardian Financial Services | 5 | 0 | 0 |
| Shepherds Friendly | 4 | 2 | 7 |
| Cirencester Friendly Society | 4 | 0 | 4 |
| iPipeline UK | 3 | 0 | 0 |
| Hannover Re UK Life Branch | 2 | 2 | 0 |
| Holloway Friendly | 1 | 1 | 6 |
| British Friendly | 1 | 2 | 3 |
| Gen Re UK | 1 | 0 | 1 |
| Iress UK | 0 | 1 | 0 |

## Vadim — please confirm

1. **Group parents (decision 2).** Pravina Ladva, Swiss Re Group Chief Digital and Technology Officer: WEAK, held because the Swiss Re parent is open for Olena. Emma Jones and Rebecca Abayakoon, RGA global underwriting philosophy heads based in London: PASS P2 from katerina, while the RGA parent is open for Nick. Keep, move, or drop?
2. **P1 titles held as WEAK:** Louise Colley (Zurich, Protection Director, empty profile), Grace Flowers (Zurich, CUO, GI history), Szymon Marszalek and Paul Yarham (Vitality, Directors of Pricing and Underwriting, life or health not shown), Deborah Smith (Swiss Re, CMO, only trainee-grade history in the row). Take any of them?
3. **Vitality:** the 6 heads of product with no line shown: all as P3 `proposition`, or none? Zurich underwriting managers with empty profiles (Andy Penny, Mark Paxford): drop?
4. **Pools:** recommended first is CEOs and COOs of the single-line protection mutuals as `referral` (Holloway, Shepherds, The Exeter, Cirencester returned no other owner there). The rest are in each batch section.
5. **Royal London × LV=.** Two web searches found only the 2021-22 history (Bain vote failed, Royal London talks ended); QC could not verify either way. If a deal closed, LV= (5 PASS) falls under the recent-acquisition rule. Confirm before import.

### Vadim's answers, 2026-10-26

Every recommended option taken (`hypothesis.md`, «Vadim's decisions 2026-10-26»), applied through `decisions.md` + `apply-decisions`: **PASS 176** (+16) · WEAK 125 · FAIL 982.

1. Group parents as they are: Ladva WEAK; Emma Jones and Rebecca Abayakoon stay PASS P2.
2. Marszalek and Yarham (P1 `underwriting`), Deborah Smith (P1 `medical`) go out; Colley and Flowers stay WEAK.
3. The six VitalityLife heads of product go out as P3 `proposition`; Andy Penny and Mark Paxford FAIL.
4. Pool A1 only: CEOs/COOs of the single-line mutuals as P3 `referral` (Pears, Barrell, O'Dea, J. Sandell, Chivers, Esson, Howe). Every other pool stays out.
5. Royal London × LV=: no deal (talks ended February 2022; Royal London later bought only Wealth Wizards from LV=). LV= stays.

## Main finding: the Sales Navigator export was pulled by company, not by title

All three Sales Nav validators found it independently: the export is every senior person at each company (speechwriting, events, catering, PAs). Across the 12 companies it held no Chief Underwriter, CUO, CMO or development/philosophy/rules underwriter; the only P1 underwriting owner was Sue Hendry (Aviva, Head of Protection UW/Claims and Customer Services). Of 1,006 Sales Nav people 45 PASS. The two Apollo pulls by the hypothesis titles gave 52 of 135 and 63 of 142 (after the QC fix round), and brought in the underwriting and medical lanes: Royal London Chief Underwriter, L&G Underwriting & Claims Director and CMO, Aviva Head of Underwriting Strategy & Governance, heads of underwriting at British Friendly and Shepherds Friendly, the reinsurers' CUOs and CMOs.

## Data issues

- `compact` bug: `earlier_roles` split Experience on `, `, so a comma inside the current title leaked as a fake earlier role. **Fixed 2026-10-23, commit 40002e5** (`split_roles`, also used by `empty-profile` and the messages profiles card). The title top-up batch was compacted after the fix; earlier batches decided on the full title, so their decisions stand.
- Same person under two LinkedIn slugs: Fiona Wynn (Apollo) = Fi Wynn (Sales Nav), suffix `72936a4`; the Apollo row is FAIL as a duplicate. `extract-people` dedupes on the full URL only.
- Duplicates inside the export: Fiona Beale, Neil Southam (Aviva); Lee Taylor, Christina Nicolaou, Paul Lewis (L&G); Robin Crouch, Gavin Drescher, Lorraine Donald. Extra copies FAIL.
- Identity collisions: Valerie Edward ("LV Limited" joins the `lv` key), 丹丹 欧阳 (Chinese fintech), Nichola H (artist, Apollo), Alwyn Roberts (Wynn Resorts, Apollo). All FAIL. Apollo rows carry no `other-company-page` flag.
- Mixed company pages: LV= includes LV= GI (Allianz); Aviva includes Direct Line; VitalityLife includes VitalityHealth; Munich Re includes Great Lakes (P&C); Gen Re includes Faraday (P&C).
- Royal London × LV=: a validator recalled a 2025 deal. Two web searches found only 2021-22 (Bain vote failed, Royal London talks ended); no completed deal, so the acquisition rule does not apply.
- UnderwriteMe ↔ Pacific Life Re are linked (Andrew Doran ex PLRe Global Chief Underwriter): keep the partnership and reinsurance messages consistent.
- CMO titles to eyeball: Deborah Smith (Swiss Re, P1) thin history; Harpreet Sarna (Vitality, WEAK) no medical history.

## Batch: Apollo title top-up for the Sales Nav companies (142)

**Counts:** PASS 63 (P1 10 · P2 38 · P3 15) · WEAK 34 · FAIL 45 · registry 0.

| Group | n | P1 | P2 | P3 | WEAK | FAIL |
|---|---|---|---|---|---|---|
| Aviva | 48 | 2 | 4 | 3 | 10 | 29 |
| Legal & General | 27 | 3 | 4 | 5 | 10 | 5 |
| Royal London | 18 | 1 | 9 | 1 | 4 | 3 |
| Pacific Life Re | 11 | 2 | 4 | 1 | 4 | 0 |
| Scottish Widows | 10 | 0 | 7 | 1 | 1 | 1 |
| LV= | 9 | 0 | 3 | 0 | 3 | 3 |
| The Exeter | 4 | 0 | 2 | 1 | 0 | 1 |
| Holloway Friendly | 4 | 0 | 0 | 1 | 0 | 3 |
| UnderwriteMe | 4 | 0 | 3 | 1 | 0 | 0 |
| Cirencester Friendly Society | 3 | 0 | 2 | 1 | 0 | 0 |
| British Friendly | 2 | 1 | 0 | 0 | 1 | 0 |
| Shepherds Friendly | 2 | 1 | 0 | 0 | 1 | 0 |

#### Proposed to SEND
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Aviva | James Whitty | Head of Underwriting Strategy & Governance | 1 | underwriting |
| Aviva | Nick Austin | Protection Commercial Director | 1 | proposition |
| Aviva | Michelle Cross | Underwriting Philosophy Manager | 2 | underwriting |
| Aviva | Tom Parkinson | Underwriting Rules Developer | 2 | underwriting |
| Aviva | Daryl Warren | Head of Individual Protection Pricing | 2 | proposition |
| Aviva | Sally James | Senior Development Underwriter | 2 | underwriting |
| Aviva | Paul Welsh | Group Head of Innovation | 3 | referral |
| Aviva | Harriet Granville-Jones | Partnerships Manager - Group Innovation | 3 | referral |
| Aviva | Suzanne Lawson | Partnerships Manager - Group Innovation | 3 | referral |
| British Friendly | Alex Yates | Head of Underwriting | 1 | underwriting |
| Cirencester Friendly Society | Steve Betteridge | Senior Development Underwriter | 2 | underwriting |
| Cirencester Friendly Society | Samuel Njoroge | Underwriting Analytics & Development Manager | 2 | underwriting |
| Cirencester Friendly Society | Sue Kissane | Underwriting Manager | 3 | underwriting |
| Holloway Friendly | Jamie Welch | Underwriting and Claims Technical Manager | 3 | underwriting |
| LV= | Lucy Luscombe | Head of Protection Pricing at LV= | 2 | proposition |
| LV= | Gareth Hurst | Development Underwriter | 2 | underwriting |
| LV= | Rachel Haig | Development Underwriter | 2 | underwriting |
| Legal & General | David Banks | Underwriting & Claims Director | 1 | underwriting |
| Legal & General | Tarun Gupta | Chief Medical Officer | 1 | medical |
| Legal & General | Pippa Barber | Commercial Director, Retail Protection | 1 | proposition |
| Legal & General | Sara Denyer | Underwriting Rules User Business Analyst | 2 | underwriting |
| Legal & General | Jenni Phillips | Development Underwriter | 2 | underwriting |
| Legal & General | John Redmond | Claims & Underwriting Development Team Manager | 2 | underwriting |
| Legal & General | Hai Luc | Head of Actuarial Research, Retail Protection | 2 | proposition |
| Legal & General | Brian Kemp | Customer Underwriting Manager | 3 | underwriting |
| Legal & General | Scott Wallace | Customer Underwriting Team Manager | 3 | underwriting |
| Legal & General | Nicky McRae | Customer Underwriting Team Manager | 3 | underwriting |
| Legal & General | Bethan Shepherd | Medical Underwriting Team Manager | 3 | underwriting |
| Legal & General | Andrew Greatbanks | Customer Underwriting Service Delivery Manager | 3 | underwriting |
| Pacific Life Re | David Waters | Underwriting Director | 1 | reinsurance |
| Pacific Life Re | Febby Mulewa | Head of Underwriting and Claims, Protection, Europe | 1 | reinsurance |
| Pacific Life Re | Killian Farrelly | Director, Protection Pricing | 2 | reinsurance |
| Pacific Life Re | Nikolai Harrowing | Development Underwriter | 2 | reinsurance |
| Pacific Life Re | Caroline Smith | Underwriting and Claims Developer | 2 | reinsurance |
| Pacific Life Re | James Sims | Underwriting Developer | 2 | reinsurance |
| Pacific Life Re | Justin Farrow | Manager, Underwriting | 3 | reinsurance |
| Royal London | Craig Paterson | Chief Underwriter | 1 | underwriting |
| Royal London | Ceri Davies | Underwriting Rules and Philosophy Developer | 2 | underwriting |
| Royal London | Dominic Pagan | Underwriting Philosophy Manager | 2 | underwriting |
| Royal London | Robert Arbuckle | Underwriting Rules Developer | 2 | underwriting |
| Royal London | William Stratton | Underwriting Rules Developer | 2 | underwriting |
| Royal London | Damian Mapplebeck | Underwriting Rules Developer | 2 | underwriting |
| Royal London | Jane Lyle | Development Underwriter | 2 | underwriting |
| Royal London | Seb Bowden | Rules & Development Underwriter | 2 | underwriting |
| Royal London | Caitlin Stronach | Head of Protection Commercials and Business Quality | 2 | proposition |
| Royal London | Robin Goodwin | Underwriting Analytics Manager | 2 | underwriting |
| Royal London | James Blaney | Underwriting & Claims Quality Assurance Manager | 3 | underwriting |
| Scottish Widows | Simon Vooght | Protection Proposition Manager | 2 | proposition |
| Scottish Widows | Daniel Musty | Underwriting Development Manager | 2 | underwriting |
| Scottish Widows | Eric Walker | Development Underwriting Manager | 2 | underwriting |
| Scottish Widows | Kerrie Cross | Protection Underwriting Development Manager | 2 | underwriting |
| Scottish Widows | Paul Young | Development Underwriter | 2 | underwriting |
| Scottish Widows | Tom Green | Development Underwriter | 2 | underwriting |
| Scottish Widows | David Russell | Senior Manager Claims & Underwriting Strategy | 2 | underwriting |
| Scottish Widows | Scott Innes | Senior Technical Underwriting Manager | 3 | underwriting |
| Shepherds Friendly | Michael Jackson | Head of Underwriting | 1 | underwriting |
| The Exeter | David Piggin | Underwriting Rules Developer | 2 | underwriting |
| The Exeter | Ed Lyon | Head of Underwriting Operations | 2 | underwriting |
| The Exeter | Lara Harkins | Underwriting Team Manager | 3 | underwriting |
| UnderwriteMe | Helen Sutherland-Thomas | Lead Development Underwriter | 2 | partnership |
| UnderwriteMe | James Hetherington | Manager, Development Underwriting | 2 | partnership |
| UnderwriteMe | Pete Martin | Lead Development Underwriter (NA and UK&I) | 2 | partnership |
| UnderwriteMe | Will Miller | VP, Head of Legal and Risk and DPO | 3 | technical-integration |

#### WEAK
| Person | Title | Group | Angle | Why borderline |
|---|---|---|---|---|
| Stuart McKellar | Data Protection Officer | Aviva | technical-integration | Holds a data protection officer title after a paralegal role, which reads as one of several data protection staff at Aviva; whether he covers protection is not shown. |
| Robert Morrison | Chief Underwriting Officer | Aviva | underwriting | The CUO title would be P1 for protection, yet Apollo has no history for him and both other Aviva CUO titles in this batch sit in general insurance. |
| Dan Tinson | Head of Protection Reinsurance | Aviva | proposition | Manages protection reinsurance, so the treaty partners who must accept any evidence change deal with him, though the card gives reinsurance management no tier. |
| Simon Lloyd | Senior Technical Underwriting Manager | Aviva | underwriting | Senior technical underwriting manager in London; Aviva's head of technical underwriting comes from GI exposure management, but Scottish Widows and L&G use the same title in protection, so his line is open. |
| Tom Craven | Pricing Technician-Protection | Aviva | proposition | Junior pricing technician inside protection after bulk-annuity quotation work: the function has a lane, but he sits well below the pricing heads the card tiers. |
| David C | Head of Risk Business Partnering - Aviva Plc - UK Life, Health, Protection and Workplace… | Aviva | referral | Risk business partnering head whose remit names UK Life, Health and Protection, so protection is in scope, but risk owns no evidence decision and Apollo truncates his surname. |
| Mike Konstant | Underwriting Effectiveness Manager | Aviva | underwriting | Nothing in Apollo beyond the title; Jamie Lye, who heads underwriting effectiveness, comes from GI, so this is probably GI, though his own record does not prove it. |
| Kelly Mhasal | Interim Head of Governance & Assurance - Protection | Aviva | referral | Interim head of protection governance and assurance, so she sits inside protection and near post-issue audit findings, but governance is not a buying role and the post is interim. |
| Penny Jemison | Underwriting Quality Assurance Manager | Aviva | underwriting | Underwriting quality at Aviva shows up in this batch only inside the GI chief underwriting office (Grahame Clarke), and Apollo has no history for her, so protection is possible but unshown. |
| Adrian Nye | Health & Protection Procurement and Outsourcing Director | Aviva | referral | Runs procurement and outsourcing for Health and Protection and would hold the nurse-screening and GP-report contracts, but buying evidence is not owning it, and his headline puts him on the Aviva Health (PMI) side. |
| Debbie Elms | Head of Underwriting & Claims | British Friendly | underwriting | Head of Underwriting and Claims, but Alex Yates also holds Head of Underwriting at British Friendly and her career is claims-led, so one title is probably stale. |
| Scott Greenhill | Head of Underwriting | LV= | underwriting | Head of Underwriting would be P1, but Apollo has no history and LV= branding still covers the GI business Allianz owns, so line and person are unconfirmed. |
| Stephanie Richards | Head of Marketing (Protection) | LV= | referral | Heads protection marketing after marketing roles at Iress, an adviser software firm; inside protection, but marketing does not own underwriting evidence. |
| Adam Davison | Head of Distribution Quality - Protection | LV= | proposition | Owns the quality of business advisers submit for protection, which touches disclosure accuracy, but the job is adviser-facing and has no tier. |
| Matthew Wilton | Underwriting Development | Legal & General | underwriting | Works in underwriting development in London after contract life-assurance work, but L&G's London underwriting development head runs Retail Retirement, so he may be on annuities. |
| Richard Whaley | Development Underwriter | Legal & General | underwriting | His L&G record includes enhanced annuity underwriting, so this Cardiff development role could be on the retirement side, although his latest earlier role, senior medical underwriter, points to protection. |
| Ann Nuttall | Underwriting Development Specialist | Legal & General | underwriting | Underwriting development specialist with nothing else in Apollo, and L&G runs underwriting development in Retail Retirement as well as protection, so neither line nor person is confirmed. |
| Malcolm Cooper | Director, Pricing and Underwriting | Legal & General | proposition | His pricing-and-underwriting directorship would be P1, but the headline "Old, happy - not looking for work" and the same title among his past roles suggest he has retired. |
| John Graves | Head of Product Technical & Oversight | Legal & General | proposition | Heads product technical and oversight, a head-of-product post the card ranks P3, but his background is pensions product and the line he oversees now is not shown. |
| Jonathan Saggers | Head of Product and Commerical Risk | Legal & General | referral | Head of product and commercial risk with an HSBC insurance distribution past; the line is not shown and risk does not own evidence, though protection product could be in his remit. |
| Donna Cowell | Head of Reinsurance, Protection | Legal & General | proposition | Ex-head of pricing at Swiss Re iptiQ EMEA now running protection reinsurance, which puts her between pricing and the reinsurers who approve evidence changes; the card has no tier for that seat. |
| Sarah Holifield | Customer Underwriting Team Manager | Legal & General | underwriting | Customer underwriting team manager in Wales with no history in Apollo, so the person and the current role are unconfirmed. |
| Lindsey Samuel | Technical Underwriting Team Manager | Legal & General | underwriting | Apollo gives only a title, technical underwriting team manager, and a Cardiff location near L&G's protection development and medical underwriting teams; the person is unconfirmed. |
| Justin Choi | Group Head, Digital Channels & Innovation | Legal & General | referral | Holds the group digital channels and innovation post the card ranks P3 referral, yet his career is brand, content and channels at Rolls-Royce and elsewhere. |
| Alan Dott | Director of Underwriting | Pacific Life Re | reinsurance | No history at all in Apollo behind a director of underwriting title, so the person needs confirming before a P1 send. |
| Warren Copp | Chief Underwriter | Pacific Life Re | reinsurance | Chief Underwriter per Apollo, but with an empty record nothing confirms the person or that the title is current. |
| Paul Reddick | Head of Medical Underwriting & Claims | Pacific Life Re | reinsurance | Medical underwriting and claims head per Apollo; the blank profile leaves identity and tenure unverified. |
| Daragh Brady | Head of Risk, Global Protection & Capital Solutions | Pacific Life Re | reinsurance | Moved from finance and strategy to head of risk for global protection and capital solutions; the reinsurance lane covers him, but the card calls the CRO line not the buyer. |
| Daniel Smith | Underwriting Philosophy Developer | Royal London | underwriting | Apollo lists him as Royal London's underwriting philosophy developer, but his headline still names Aviva as his employer, so the current company needs checking. |
| Vikki Larkin | Protection Pricing Actuary | Royal London | proposition | Protection pricing actuary, a function with a proposition lane, but below the pricing-head tier and with no history in Apollo. |
| Robert Morrison | Head of Underwriting and Claims | Royal London | underwriting | Head of underwriting and claims would be P1, yet his Apollo record is blank and the same name carries a blank Aviva CUO record, so identity must be checked first. |
| Richard Basham-Jones | Customer Service Director - Pensions Protection & Customer Relations | Royal London | referral | Customer service director whose remit covers pensions and protection, so he is partly inside protection, but service does not own evidence and pensions leads his title. |
| Frances Heggie | Senior Underwriting Strategy Manager | Scottish Widows | underwriting | Senior underwriting strategy manager would be P2, but there is no history in Apollo to confirm the person or the protection line. |
| Val Brookes | Claims and Underwriting Manager | Shepherds Friendly | underwriting | Claims and underwriting manager whose title puts claims first and whose Apollo record is empty, so the role cannot be confirmed. |

Fiona Wynn (Apollo) = Fi Wynn (Sales Nav), renamed slug: the Apollo row is FAIL as a duplicate and does not appear above.

**After QC (fix round):** team managers judged on business line only (5 FAIL → PASS P3, 2 → WEAK on empty profile); the "team already covered" argument dropped (8 WEAK → PASS P2); protection governance / marketing and 6 more protection-side functions FAIL → WEAK; 3 Aviva underwriting titles whose GI line was only inferred FAIL → WEAK. Inference to know: L&G's "customer underwriting" desk is read as the protection tele-underwriting team (Kemp, Wallace, McRae, Greatbanks); no row says "protection" on its own.

#### Pools left out (seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| Protection distribution and sales | 4 | Mike Farrell (Director of Protection Sales, LV=), Daren Boys (Protection Portfolio Distribution Director, Aviva), Charlotte Dipfa (Head of Strategic Accounts, Protection Distribution, Aviva), Tony Silvester (L&G) | referral | lift the adviser-facing distribution exclusion for directors |
| Innovation / transformation, no protection scope | 6 | David Fleming, Laura Nicol, Juliet Fenton, Andrew Fisher, Ankur Singh (Aviva), James Trehane (Royal London) | referral | take innovation staff who are neither group-wide leads nor in protection |
| Group IT, data, CIO functions | 5 | David Debnam (Operational Risk & Innovation Director, Aviva), Luke Mepham (Aviva), Nikitas Mahmudi, Kalpesh Mistry, Jayant Maroo (L&G) | technical-integration | extend the lane below CTO and architecture |
| Claims | 1 | Natalie James (Holloway) | underwriting | Open question 4 |
| Not offered | 28 | GI 20 (19 Aviva incl. Michael Korner, CUO Aviva Retail; 1 LV= pet/travel), retirement / equity release 2, left or retired 5, individual underwriter 1 | none | — |

#### Data notes from the validator
Two blank Robert Morrison records; three blank senior titles at Pacific Life Re; two Heads of Underwriting at British Friendly; Daniel Smith's headline still names Aviva; some departures show in headlines while Apollo lists the role as current.

## Batch: Apollo gap top-up (135)

**Counts:** PASS 52 (P1 12 · P2 24 · P3 16) · WEAK 39 · FAIL 44 · registry 0.

| Group | n | P1 | P2 | P3 | WEAK | FAIL |
|---|---|---|---|---|---|---|
| Zurich UK | 46 | 1 | 3 | 4 | 15 | 23 |
| VitalityLife | 30 | 0 | 5 | 3 | 14 | 8 |
| Swiss Re UK | 15 | 2 | 5 | 1 | 3 | 4 |
| Munich Re UK Life Branch | 13 | 3 | 2 | 1 | 3 | 4 |
| SCOR UK | 9 | 1 | 3 | 1 | 1 | 3 |
| RGA UK | 7 | 2 | 3 | 1 | 0 | 1 |
| Guardian Financial Services | 5 | 1 | 3 | 1 | 0 | 0 |
| Hannover Re UK Life Branch | 4 | 1 | 0 | 1 | 2 | 0 |
| iPipeline UK | 3 | 0 | 0 | 3 | 0 | 0 |
| Gen Re UK | 2 | 1 | 0 | 0 | 0 | 1 |
| Iress UK | 1 | 0 | 0 | 0 | 1 | 0 |

#### Proposed to SEND
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Gen Re UK | Lynn Baillie | Chief Underwriting Officer | 1 | reinsurance |
| Guardian Financial Services | Nick Rice | Head of Underwriting and Claims | 1 | underwriting |
| Guardian Financial Services | Andrew Newton | Development Underwriting Manager | 2 | underwriting |
| Guardian Financial Services | Richard Stadon | Strategic Underwriting Manager | 2 | underwriting |
| Guardian Financial Services | Caroline Froude | Head of Technical Underwriting | 2 | underwriting |
| Guardian Financial Services | Jane Tarbuck | Operational Underwriting Team Manager | 3 | underwriting |
| Hannover Re UK Life Branch | Tim Smith | Head of Protection | 1 | reinsurance |
| Hannover Re UK Life Branch | Andrea Gregory | Underwriting and Claims Manager | 3 | reinsurance |
| Munich Re UK Life Branch | Adrian Stevenson | Head of Protection | 1 | reinsurance |
| Munich Re UK Life Branch | Matt Bone | Head of Underwriting & Claims | 1 | reinsurance |
| Munich Re UK Life Branch | Madhu Sridharan | CUO | 1 | reinsurance |
| Munich Re UK Life Branch | Lloyd Williams | Underwriting Development Manager | 2 | reinsurance |
| Munich Re UK Life Branch | Jonathan Carnell | Consultant Medical Officer | 2 | medical |
| Munich Re UK Life Branch | James Norton | Underwriting & Claims Operations Manager | 3 | reinsurance |
| RGA UK | Mike Evans | Chief Underwriter - Protection | 1 | reinsurance |
| RGA UK | Anna Graham | Head of Protection, UK and Ireland | 1 | reinsurance |
| RGA UK | Anna Currie | Underwriting Research and Development Manager | 2 | reinsurance |
| RGA UK | Emma Jones | Head of Global Underwriting Philosophy Delivery | 2 | reinsurance |
| RGA UK | Rebecca Abayakoon | Head of Global Underwriting Philosophy Design at Reinsurance Group of America, Incorporat… | 2 | reinsurance |
| RGA UK | Dean Scotson | DPO (emea) | 3 | technical-integration |
| SCOR UK | Helen Croft | Head of Life & Health Underwriting & Claims UK & Ireland | 1 | reinsurance |
| SCOR UK | Hannah Cook | Head of Protection Business Development | 2 | reinsurance |
| SCOR UK | Gill Salton | Underwriting & Claims Development Manager | 2 | reinsurance |
| SCOR UK | Ricky D'Gama | Head of Modelling & Innovation | 2 | reinsurance |
| SCOR UK | Anil Girdhari | Senior Underwriting Manager Life & Health | 3 | reinsurance |
| Swiss Re UK | Claire Nolan | Head of Claims & Underwriting | 1 | reinsurance |
| Swiss Re UK | Natalie Kelly | Head L&H Underwriting, Claims and R&D | 1 | reinsurance |
| Swiss Re UK | Denise Bates | Head of Income Protection Pricing UKI | 2 | reinsurance |
| Swiss Re UK | Alana Paterson-Barker | Head of Pricing, Life & Health, UK&I | 2 | reinsurance |
| Swiss Re UK | Vicki Livingstone | Underwriting Proposition Manager | 2 | reinsurance |
| Swiss Re UK | Andrew Graham | Underwriting Solution Manager | 2 | reinsurance |
| Swiss Re UK | Tim Knaust | L&H Underwriting & Claims Propositions Manager for UK & Ireland | 2 | reinsurance |
| Swiss Re UK | Dave Evans | Data Protection Officer | 3 | technical-integration |
| VitalityLife | Nicky Roux | Underwriting Research and Development Manager | 2 | underwriting |
| VitalityLife | Andrew Smith | Underwriting Philosophy and Automation Manager | 2 | underwriting |
| VitalityLife | Lorna Miller | Strategic Underwriting Manager | 2 | underwriting |
| VitalityLife | Kathryn Conniff | Life Underwriting Service Director | 2 | underwriting |
| VitalityLife | James Ayland | Director of Data Science - Life Pricing and Underwriting | 2 | underwriting |
| VitalityLife | Fareeha Brownless | Head of Product (Life) | 3 | proposition |
| VitalityLife | Catherine Bowen-Walker | Head of Data Protection and UK DPO | 3 | technical-integration |
| VitalityLife | Simon Evans | Chief Product & Delivery Officer UK - Vitality | 3 | proposition |
| Zurich UK | Sabrina Lane | Chief Underwriter | 1 | underwriting |
| Zurich UK | Adrian Hill | Life Development Underwriter | 2 | underwriting |
| Zurich UK | Ryan Parsons | Senior Development Underwriter | 2 | underwriting |
| Zurich UK | Scott Reid | Head of Propositions & Pricing, Digital Protection Hub | 2 | proposition |
| Zurich UK | Rebecca McGeoch | UK Data Protection Officer | 3 | technical-integration |
| Zurich UK | Steve Smith | Global Senior Underwriting Manager | 3 | underwriting |
| Zurich UK | Fraser Ballantine | Underwriting Quality & Risk Manager | 3 | underwriting |
| Zurich UK | Gareth Jenkins | Head of Life Product and Inforce | 3 | proposition |
| iPipeline UK | Danny Essam | Head of Product | 3 | partnership |
| iPipeline UK | Kaj Makaswaran | Underwriting Services Manager | 3 | partnership |
| iPipeline UK | Helena Mbcs | Director Data Protection | 3 | technical-integration |

#### WEAK
| Person | Title | Group | Angle | Why borderline |
|---|---|---|---|---|
| David Brownlow | Global Head of Life & Health Data Operations & Solutions | Hannover Re UK Life Branch | reinsurance | Global Head of L&H Data Operations and Solutions, ex CFO of the UK Life Branch: data and solutions could host an evaluation, but the lineage is finance. |
| Stuart Crichton | Underwriting & Claims Manager / Senior Underwriter | Hannover Re UK Life Branch | reinsurance | UK-based (Edinburgh), but his headline is Head of Life Underwriting and Claims for Ireland, which is not katerina's market. |
| Gideon Cheok | Head of Product Design (UK & RSA) | Iress UK | partnership | Head of Product Design (UX) across Iress UK and South Africa: design rather than product ownership, protection scope not shown. |
| Louis Pereira | Underwriting Manager | Munich Re UK Life Branch | reinsurance | Underwriting Manager with an empty profile; this group also returned Great Lakes UK (P&C), so life is not confirmed. |
| Armin Fox | Underwriting Manager | Munich Re UK Life Branch | reinsurance | Underwriting Manager, ex SVP and head of section at Munich Re; life or P&C not shown. |
| Rose Duffy | Interim Head of Underwriting Operations | Munich Re UK Life Branch | reinsurance | Interim Head of Underwriting Operations (headline: senior underwriting analyst); an operations role, life or P&C not shown. |
| Emma Denby | Underwriting Innovation & Data Strategy Manager | SCOR UK | reinsurance | Underwriting Innovation and Data Strategy Manager is a P2 title, but her headline is actuarial analyst and SCOR UK also runs P&C; life not shown. |
| Simon Jenner | CTO & CSO (Chief Technology & Security Officer) | Swiss Re UK | technical-integration | Chief Technology and Security Officer title, but Swiss Re's group technology chief is Pravina Ladva and his scope here is unclear (ex National Grid CISO). |
| Deborah Smith | Chief Medical Officer | Swiss Re UK | medical | Chief Medical Officer title at Swiss Re UK, but the only earlier roles are trainee-grade NHS posts (CT2 neurology, acute medicine specialty doctor); P1 needs the role confirmed before she goes out. |
| Pravina Ladva | Group Chief Digital and Technology Officer | Swiss Re UK | technical-integration | Swiss Re Group Chief Digital and Technology Officer, a parent-level executive; decision 2 sends only the UK team from katerina and leaves the Swiss Re parent open for Olena, so held for Vadim. |
| Louise Cowan | Head of Product - Innovation | VitalityLife | proposition | Head of Product (Innovation) at Vitality UK with a CRM product background; life or health side not shown. |
| Dave Roberts | Underwriting Manager | VitalityLife | underwriting | Underwriting Manager (P3) at Vitality, ex senior underwriter at Aviva; Vitality UK also underwrites health, and life is not confirmed. |
| Nick Telfer | Head of Protection Specialists | VitalityLife | proposition | Title is Head of Protection Specialists (an adviser-facing team), but his headline says Head of Protection Development and his background is protection product. |
| Neil Hartigan | Head of Underwriting & Claims Quality | VitalityLife | underwriting | Head of Underwriting and Claims Quality fits the post-issue audit KPI, but the profile is empty and life or health is not shown. |
| Szymon Marszalek | Director of Pricing and Underwriting | VitalityLife | underwriting | Director of Pricing and Underwriting is a P1 title, but Vitality UK has two such directors and life or health is not shown; James Ayland's title confirms a separate Life Pricing and Underwriting function. |
| Paul Yarham | Director of Pricing and Underwriting | VitalityLife | underwriting | Director of Pricing and Underwriting, P1 if life; his commercial and market pricing background reads like the health side. |
| Sharon Powell | Head of Product | VitalityLife | proposition | Head of Product at Vitality UK (ex digital product manager there); life or health side not shown. |
| Gareth Alan-Williams | Head of Product | VitalityLife | proposition | Head of Product at Vitality UK (ex portfolio management and VitalityCar change); life or health side not shown. |
| Becca Cooke | Head of Product | VitalityLife | proposition | Head of Product at Vitality UK with a customer-acquisition platform background; life or health side not shown. |
| Chris Puzey | Portfolio Underwriting Manager | VitalityLife | underwriting | Portfolio Underwriting Manager with an Aviva pricing background; portfolio underwriting is a corporate-health or GI term, life not shown. |
| Hannah Leech | Senior Underwriting Manager | VitalityLife | underwriting | Senior Underwriting Manager (P3), but her background is customer service at Vitality and PruHealth; life or health not shown. |
| Harpreet Sarna | Chief Medical Officer | VitalityLife | medical | Chief Medical Officer is a P1 title, but no earlier role is medical (charity trustee, WBS ambassador); check it is not Chief Marketing Officer. |
| Rachel Loudain | Head of Product Management | VitalityLife | proposition | Head of Product Management with an ASOS customer-experience background; life or health side not shown. |
| Stuart Jackson | Head of Product Management - Adviser, Employer & Servicing | VitalityLife | proposition | Head of Product for the adviser, employer and servicing platforms: the adviser portal carries life applications, but employer is health and servicing is post-sale. |
| Grace Flowers | Chief Underwriting Officer | Zurich UK | underwriting | CUO is a P1 title, but her earlier role was Head of Retail UW at Zurich Insurance plc (the GI carrier) and Zurich protection uses the Chief Underwriter title (Sabrina Lane), so she is probably the GI CUO. |
| Mike Lytheer | Data Protection Officer | Zurich UK | technical-integration | Data Protection Officer title, but his earlier role (senior operations assistant) points to a team-level role; Rebecca McGeoch is the UK DPO. |
| Louise Colley | Protection Director | Zurich UK | proposition | Protection Director is a P1 title, but the profile is empty: no role history to confirm she holds it now. |
| Shaun Beale | Claims & Underwriting Development | Zurich UK | underwriting | Claims and Underwriting Development in Swindon (Zurich's life office) fits P2, but the profile is empty and half the title is claims. |
| Sally Watford | Head of Underwriting Operations | Zurich UK | underwriting | Head of Underwriting Operations; the line is not shown and her reinsurance-services background reads GI. |
| Andy Penny | Underwriting Manager | Zurich UK | underwriting | Underwriting Manager (P3) with an empty profile: life or GI cannot be told, and most Zurich UK underwriting managers here are GI. |
| Mark Paxford | Underwriting Manager | Zurich UK | underwriting | Underwriting Manager (P3) with an empty profile; lives near Zurich's Swindon life office, but the line is not shown. |
| Emma Coleman | Life Development Underwriter | Zurich UK | underwriting | Life Development Underwriter in Swindon is a P2 fit, but the profile is empty and there is no second confirmation. |
| Paul Barker | Innovation Manager | Zurich UK | referral | Innovation Manager with an IT business-systems background; no protection scope shown, so P3 group-wide at best (referral lane). |
| Charlotte Hayes | Medical Underwriting Manager | Zurich UK | underwriting | Medical Underwriting Manager in Swindon, but her background is group risk underwriting (an anti-case); individual protection is not confirmed. |
| Pete Sanderson | Head of Operations - Retail Protection | Zurich UK | referral | Head of Operations for Retail Protection (ex Head of Automation and Robotics) runs protection new-business processing; operations is not a named function, so referral only if Vadim adds it. |
| John Lavender | Underwriting Business Manager | Zurich UK | underwriting | Underwriting Business Manager whose background is mortgage and protection advice, hinting at the life side; an operations role and the line is not confirmed. |
| Chloe Eggleton | Innovation Lead / Senior Project Manager | Zurich UK | referral | Innovation Lead combined with Senior Project Manager, procurement IT background; no protection scope shown. |
| Simon Guest | Head of Customer Solutions & Partnerships, Global Life Protection | Zurich UK | referral | Senior in Global Life Protection, but customer solutions and partnerships is distribution-facing and global; referral at most. |
| Kylie Maxam | Operational Transformation Underwriter Zurich | Zurich UK | underwriting | Operational Transformation Underwriter in Swindon, ex Guardian medical underwriter: life side and change work, but an individual underwriter title without development or rules. |

#### Pools left out (seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| GI / P&C underwriting leaders at multi-line groups | 8 | Sam Thomas (Zurich, interim CUO), Grant Thompson (Zurich, Head of UW), Scott Bailey (Zurich, Global CUO A&H), Tony Ayles (Great Lakes UK CUO), Marie Biggas (SCOR CUO), Paula Wolfenson, Lawrence Harper, Louise Martin | none | out of line: build is not rated in GI, a different campaign |
| L&H seniors at reinsurers outside underwriting | 5 | Andy Parkinson (Swiss Re, Head of L&H Claims EMEA), Paul Bevan (RGA, Annuities Chief UW & Head of Protection Claims), Colin Bannister (Swiss Re, L&H Valuation), Dean Galligan (Swiss Re, L&H Transactions), Doug Scott (Munich Re, Block Risk Transfer) | referral | Open question 4 (claims) = yes; valuation/capital as referral only |
| Vitality product marketing | 2 | Prema Sohun (Head of Product Marketing, VitalityLife), Sarah Squelch | referral | product marketing as a referral function |
| Vitality adviser-facing protection | 2 | Gary King (Head of Protection Specialists), Fergus Bescoby | referral | lift the adviser-facing exclusion for heads of specialist teams |
| Vitality claims / health product | 3 | Charles Nolan (claims & ops product), Jessica Jones, Jonathan Hubbard (PMI) | referral (Nolan only) | Nolan: Open question 4; the other two are VitalityHealth (anti-case) |
| Not offered | 24 | GI underwriters and managers 15, retired / identity collisions 4 (Nicky Bray, Graham Johnston, Nichola H, Alwyn Roberts), junior/admin 4, Zurich retirement 1 | none | — |

#### Data notes from the validator
- Apollo rows carry no `other-company-page` flag: two collisions caught by headline (Nichola H, artist; Alwyn Roberts, Wynn Resorts).
- VitalityLife's page mixes VitalityHealth; Munich Re includes Great Lakes (P&C); Gen Re includes Faraday (P&C). Lynn Baillie passed as the L&H CUO on her Gen Re career: inference, nothing in the row says L&H.
- Zurich: both CUOs (Grace Flowers, Sam Thomas) have GI histories; the protection lead is titled Chief Underwriter (Sabrina Lane). "Development Underwriter" at Zurich is mostly the GI broker-sales role.
- Validator's questions: the 6 Vitality heads of product with no line shown (all P3 or none?); the 2 Vitality Directors of Pricing and Underwriting (both P1?); Zurich underwriting managers with empty profiles (drop?).

## Batch: Royal London, LV=, Pacific Life Re, Scottish Widows, The Exeter, mutuals, UnderwriteMe (259)

**Counts:** PASS 26 (P1 7 · P2 7 · P3 12) · WEAK 27 · FAIL 206 · registry 0. No group near the cap.

| Group | n | P1 | P2 | P3 | PASS | WEAK | FAIL |
|---|---|---|---|---|---|---|---|
| Royal London | 121 | 1 | 1 | 5 | 7 | 10 | 104 |
| LV= | 44 | 0 | 1 | 1 | 2 | 2 | 40 |
| Pacific Life Re | 35 | 1 | 3 | 1 | 5 | 5 | 25 |
| Scottish Widows | 14 | 2 | 0 | 0 | 2 | 0 | 12 |
| The Exeter | 11 | 1 | 1 | 0 | 2 | 1 | 8 |
| Shepherds Friendly | 11 | 0 | 1 | 2 | 3 | 1 | 7 |
| UnderwriteMe | 10 | 2 | 0 | 2 | 4 | 6 | 0 |
| Cirencester | 5 | 0 | 0 | 1 | 1 | 0 | 4 |
| Holloway | 4 | 0 | 0 | 0 | 0 | 1 | 3 |
| British Friendly | 4 | 0 | 0 | 0 | 0 | 1 | 3 |

**Data note:** no underwriting title anywhere in the slice (not even Royal London's chief underwriter, whom the persona cites): the underwriting and medical lanes are empty. LV= rows include LV= GI staff (Allianz since 2019) → FAIL. Duplicates: robin-crouch, gavin-drescher, lorraine-donald. Retired: jon-glen, graham-nichol. valerie-edward = identity collision, FAIL. UnderwriteMe ↔ Pacific Life Re linked (Andrew Doran ex PLRe Global Chief Underwriter). To check: Royal London's 2025 deal for LV= (recent-acquisition rule?).

#### Proposed to SEND (rest)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Royal London | Carrie Johnson | Customer Lifestage Director - Protection and Build & Grow (Protection P&L) | 1 | proposition |
| Royal London | Fi Wynn | Head of Protection Propositions | 2 | proposition |
| Royal London | James Sandell | UK CIO / CTO | 3 | technical-integration |
| Royal London | Lee Ellis | Group Chief Digital Officer | 3 | referral |
| Royal London | Amy Higgs | Head of Strategic Transformation | 3 | referral |
| Royal London | Joshua Goodwin | Head of Transformation and Innovation | 3 | referral |
| Royal London | Myrto (Myrsini) A. | Head of Strategy & Innovation | 3 | referral |
| LV= | Gary Beyer | Protection Proposition Director | 2 | proposition |
| LV= | Karl Pickering | CTO | 3 | technical-integration |
| Pacific Life Re | Mala Thurston | Head of Protection, Europe | 1 | reinsurance |
| Pacific Life Re | Sandi Sohal | AVP, Basis Development, R&D | 2 | reinsurance |
| Pacific Life Re | Réka Halász | AVP, Basis Development, R&D | 2 | reinsurance |
| Pacific Life Re | Martin Boniface-Jones | AVP, R&D | 2 | reinsurance |
| Pacific Life Re | Caroline Burton | DPO - AVP | 3 | technical-integration |
| Scottish Widows | Kate Lyons | Protection Director | 1 | proposition |
| Scottish Widows | Laura Vaughan | Head of Protection (thin profile) | 1 | proposition |
| The Exeter | Toby Bainbridge | Head of Insurance Solutions (ex Director of Protection, LV=) | 1 | proposition |
| The Exeter | Jack Southcott | Head of Proposition (Protection) | 2 | proposition |
| Shepherds Friendly | Steve Smith | Head of Product (ex Head of Underwriting, CPD) | 2 | proposition |
| Shepherds Friendly | Michael Williams | Chief Change Officer | 3 | referral |
| Shepherds Friendly | Elizabeth Cook | Head of Business Innovations | 3 | referral |
| UnderwriteMe | Andrew Doran | CEO | 1 | partnership |
| UnderwriteMe | Kylie Irwin | CPO | 1 | partnership |
| UnderwriteMe | Sai Tejo Kiran | Director of Product Management | 3 | partnership |
| UnderwriteMe | Riccardo Rossi | Product Manager Director | 3 | partnership |
| Cirencester | John Underwood | Director of Technology | 3 | technical-integration |

#### WEAK (rest)
| Person | Title | Group | Why borderline |
|---|---|---|---|
| Jonathan Letham | Head of Proposition | Royal London | No line; earlier roles wealth |
| Daniel T. | Head of Proposition | Royal London | No line named |
| Sophie Hadfield | Head of Proposition | Royal London | No line; Deloitte audit background |
| Maureen Duckworth | Head of Product Management | Royal London | Multi-line, no profile |
| Sarah Farquharson | Head of Transformation and Performance | Royal London | Ops-efficiency background |
| Finlay Boyd | Head of Commercial Insight / Planning / E2E Transformation | Royal London | Reads as commercial planning |
| Ritwik Samsi | Group Corporate Development Director | Royal London | Owns no evidence; insurtech boards |
| Vicki Wharton | Group Customer Operations Director | Royal London | New-business processing may report to her |
| Kevin Milne | Case Management Consultant, New Business - Protection | Royal London | IC in protection new business; referral |
| Jones (Birmingham) | Head of Customer Experience (New Business) | Royal London | No first name |
| Martyn Luke | Head of Protection Change | LV= | Delivers, does not decide |
| Jonathan Manning | Head of Change (S&R) | LV= | Headline adds Protection; delivers |
| Charles King | Head of Digital Process | Pacific Life Re | Scope unclear |
| Richard Purcell | Client Solutions Director | Pacific Life Re | Underwriting solutions or capital/longevity? |
| Matthew Barclay | Director, Client Solutions | Pacific Life Re | Same question |
| Oliver Gingell | VP, Head of Client Solutions UK | Pacific Life Re | Same; longevity background |
| Ben Acheson-Gray | AVP, Technical Services, Europe & NA | Pacific Life Re | May be client underwriting support |
| Ali Law | CIO | The Exeter | Card excludes CIOs, but top technologist, no CTO |
| Darren Wing | Head of IT and Change | Holloway | Top technologist at a small IP mutual |
| Nic Herbert | Head of Technology & Change | British Friendly | Top technologist at a small IP mutual |
| Daniel Simpson | Chief Commercial Officer | Shepherds Friendly | Product/proposition/pricing background |
| Simon Coutts, Will Hutchinson, Sergey Kobzar, Alan Pich | Directors of Engineering | UnderwriteMe | Four, no CTO in the pull; pick one |
| Kristian Samuel-Camps | Director of Product Operations | UnderwriteMe | Runs product ops |
| Paul Mburu | Head of Strategy | UnderwriteMe | May own partnerships |

#### Pools left out (rest, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| A1. Executives at single-line protection mutuals | 7 | Ben Pears (CEO Holloway), Ann-Marie O'Dea (CEO Shepherds Group), Jonathan Sandell (CEO Shepherds Friendly), Suzy Esson (COO The Exeter), Ben Howe (COO Cirencester) … | referral | add CEO/COO at a single-line protection mutual as P3 referral — **recommended**: no underwriting owner returned there |
| A2. Executives at multi-line groups | 7 | Barry O'Dwyer, Peter Josse, Jo Kite, Bernie Hickman (RL); Anita Fernqvist, Richard Rowney (LV=) | referral | card says group CEO is not the buyer — not recommended |
| C. CIOs and heads of architecture | 11 | Ian Andrews (LV=); Lisa Bullock, Stuart R., Michael Hunter, Charul Scott (RL) … | technical-integration | lift the CIO rule or give architecture a tier |
| B. Protection distribution heads | 4 | Jon Fuller (RL), Catherine Trimble (SW), Jamie Page (Exeter), Alan Waddington (Cirencester) | proposition | exempt protection-named distribution heads |
| D. Data and AI | 20 | Chris Miller (Group Chief Data & AI Officer, RL), Lee Wilson (RL), Ian McNamara (PLRe), Annabel Banks (LV=), Russell Johnston (RL) … | technical-integration | group data/AI chiefs as P3 — Miller and Wilson only |
| E. Strategy / corporate development | 7 | Etienne B. (RL), Chris Walker (LV=), Hannah Rothery (PLRe), Minoka Radhakrishnan, Julie Clapperton (RL) … | referral | strategy heads as referral |
| F. Pacific Life Re ops / client services / actuarial | 7 | Myles Rix (SVP Global Head of Ops), Travis Short, Savita Rai, Akta Savla, Mark Howlett … | reinsurance | read "reinsurance lane = everyone at group B" literally |
| H. Operations and customer | 13 | Ian Wheat (RL), Claire Hird (Exeter), Lorraine Donald (BF), Valerie Rogerson, Gail Manchester … | referral | new-business ops owners, small mutuals only |
| G. Change / PMO / delivery | 17 | Hilary Jones, Caroline Edgar, Wayne Morris (RL); Kevin Buckland (LV=); Simon Trowbridge (Exeter) … | referral | not recommended |
| I. Claims | 2 | Ian Rowe (PLRe), Maxine Jannetta (BF) | none | open question 4 keeps claims out |

Not offered (111): out of line 26, general distribution/BD 17, IT below CIO/CTO 23, support 35, legacy/unclear 4, duplicates/retired/collision 6.

## Batch: Aviva (449)

**Counts:** PASS 12 (P1 2 · P2 2 · P3 8) · WEAK 19 · FAIL 418 · registry 0 · cap 50 not reached.
FAIL by reason (validator's tally): GI 104 · group support 95 · tech/data/AI 82 · transformation/change 40 · governance/audit/regulatory 29 · wealth/pensions 27 · empty/junk/left/duplicate 24 · claims 9 · Aviva Health 8.

**Data note:** company-wide pull, not by title (card: "never by company alone"). Of the P1 roles only Sue Hendry and Victoria Francis are present; no CUO, Chief Underwriter, CMO, development/philosophy underwriter, MD Protection, Head of New Business. Duplicates: Fiona Beale ×2, Neil Southam ×2. Junk/collisions: 丹丹-欧阳 (Chinese fintech), ma-ma (Landlord), darran-r (investigator), two retired, rob-fisher (other-company-page). Direct Line staff now under Aviva (GI, FAIL).

#### Proposed to SEND (Aviva)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Aviva | Sue Hendry | Head of Protection UW/Claims and Customer Services | 1 | underwriting |
| Aviva | Victoria Francis | Protection Propositions Director | 1 | proposition |
| Aviva | Lili Burdass | Head of Transformation, Protection | 2 | proposition |
| Aviva | Rachel Hannon | Chief Transformation Officer, UK Life (IWR) | 2 | proposition |
| Aviva | Jon O'Neal | Head of IT, Aviva Protection UK | 3 | technical-integration |
| Aviva | Steve Lister | Head of Architecture, Insurance, Wealth & Retirement | 3 | technical-integration |
| Aviva | Arslan Hannani | Chief Innovation Officer (group) | 3 | referral |
| Aviva | Marina Belezina | Group Director Strategy & Innovation | 3 | referral |
| Aviva | Hannah Spiro | Head of Innovation Engagement | 3 | referral |
| Aviva | Joel Manstoff | Group Head of Transformation | 3 | referral |
| Aviva | Aman Hayer | Group Transformation Director | 3 | referral |
| Aviva | Manju Devi | Head of Digital Portfolio, Group Strategy & Transformation | 3 | referral |

#### WEAK (Aviva)
| Person | Title | Group | Why borderline (angle) |
|---|---|---|---|
| Martin Felice | Head of Underwriting Governance | Aviva | Empty profile; GI or protection unknown (underwriting) |
| Gary Williams | Director of Product and Underwriting | Aviva | Buyer title, line not shown; GMAC motor background (underwriting) |
| Katriona Cunningham | Head of Underwriting Counter Fraud | Aviva | Owns application misrepresentation, but persona excludes fin-crime; Perth suggests GI (underwriting) |
| Dan Turner | Head of Change | Aviva | Ex Head of Change at AIG Life (now Aviva protection) (proposition) |
| Clare Mallion | Head of Transformation (headline: Head of Pricing) | Aviva | Protection pricing would be P2; line not shown (proposition) |
| Brian Spinks | Head of New Business Development, Propositions & Insights | Aviva | Reads as BD; line not shown (proposition) |
| Ashley Murray | Head of Retail Propositions & Change | Aviva | Retail includes direct protection and savings (proposition) |
| Louise M. | Head of Propositions | Aviva | Line not shown (proposition) |
| Mike Jackson | Head of Product | Aviva | Bare title, no detail (proposition) |
| Maria C. | Head of Digital Product | Aviva | Prior role commercial GI (proposition) |
| Jen Hobbs | Head of Digital Product (Interim) | Aviva | Line not shown (proposition) |
| Michael Sasaki | IT Director IWR | Aviva | Ex CIO AIG Life; card says CIO-level does not own evidence (technical-integration) |
| Juan Gómez-Reino Garrido | CIO IWR and Group Deputy CIO | Aviva | Same CIO rule (technical-integration) |
| Ashley Bevan | Head of Life and Group Data Platform | Aviva | Life-scoped data platform (technical-integration) |
| David Montgomery | COO, Insurance, Wealth & Retirement | Aviva | Runs protection ops among others; no COO lane (referral) |
| Amanda Weston | Head of Partnerships | Aviva | Ex AIG Life partnerships; distribution (referral) |
| Matt Rushbrooke | Customer Expert, Protection Operations | Aviva | Individual contributor in protection (referral) |
| James Appleton | Head of Innovation Delivery | Aviva | Probably group innovation (referral) |
| Ashley Stevens | Global Head of Transformation | Aviva | "Global" at Aviva often = GCS (GI) (referral) |

#### Pools left out (Aviva, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| Group executives and group technology | 9 | Amanda Blanc (Group CEO), Craig Fazzini-Jones (Group COO), John Cummings (Group CIO), Ajit Dhaliwal, Paul Shaw (Group CISO), Chris Cochrane, Martin Lamb, Andy Piper, Anna King | referral · technical-integration | allow group C-suite referral and group CIO/CISO |
| Life and protection support functions | 8 | Steve Bridger (Chief Claims Officer, ex-MD Group Protection), Richard English, Jackie Kerwood, Karen Howard, Tegan Gill, Eva Werry, Chris Wood, Michelle Mapplebeck | referral | open question 4 (claims) = yes; IWR-wide support as referral |
| AI and data leadership | 11 | Angela Luget (Chief AI Officer), Chris Thompson, Alberto Romero, Tom Spencer, David Young … | referral | add an AI/data referral lane |
| Group strategy / corporate development | 9 | Megumi Takenoshita, James Oram, Alistair Hargreaves (ex L&G digital proposition), Nathan Tomlinson, Charlotte Davey … | referral | treat group strategy as group-wide P3 |
| Transformation heads, scope not shown | 16 | Rachel Robinson, Paula Whitwell, Samantha Lacey, Radhika Kale, Jon Day … | referral | unscoped transformation = group-wide P3 |
| Architecture, scope not shown | 6 | Joshua Cruickshank, Luke Temple, Atanu B., Martin Copley, David McIntyre … | technical-integration | accept architecture heads without protection scope |
| Cross-line digital and customer | 5 | Kiran Bharucha, Alex Allen (MyAviva), Delia Todman, Jason Knowles, Chris Johnston | proposition | cross-line digital as P3 |
| Aviva Health (PMI) | 8 | Matthew McGill, Lisa Bartlett, Rob McKillop, Lucy Dearing, Charles McElroy … | none (anti-case) | a separate health campaign |

Not proposed: GI 104, wealth/pensions 27, distribution ~12, governance/HR/finance/comms, IT delivery, junk 24.

## Batch: Legal & General (298)

**Counts:** PASS 7 (P1 0, P2 1, P3 6) · WEAK 17 · FAIL 274 · registry 0. Under the cap (50).

**Data note:** the L&G export is a company-wide seniority pull, not a title pull: zero underwriting / Chief Underwriter / CMO titles, no Head of Protection. Only real protection buyer: Nicki Plews. Duplicates: Lee Taylor ×2, Christina Nicolaou ×2 (empty copies FAIL), Paul Lewis ×2 (both FAIL). Three "IT & Transformation Director" profiles (Siingh, Rautaray, Sundarraj) look like TCS account staff. Ruth Burgess has likely left. Group Protection (Yash Gupta, Chloe Carter, Jimmy Turrell) FAIL as group risk.

#### Proposed to SEND (L&G)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| L&G | Nicki Plews | Head of Product and Proposition (ex Head of Protection Strategy and Proposition, ex Munich Re) | 2 | proposition |
| L&G | Tariq Surty | Chief Technology Officer ("CTO - Retail") | 3 | technical-integration |
| L&G | Michael Spiteri | Group CTO | 3 | technical-integration |
| L&G | Jenny Reeve | Group Head of Transformation | 3 | referral |
| L&G | Steve Davis | Group Director of Transformation | 3 | referral |
| L&G | Gary M. | Transformation Director - Retail | 3 | referral |
| L&G | Cris Saunders | Head of Groupwide Digital Products | 3 | referral |

#### WEAK (L&G)
| Person | Title | Group | Why borderline |
|---|---|---|---|
| Laura Mason | CEO, Retail | L&G | Runs the division that holds protection; CEO-to-CEO referral fits, but the card has no insurer-CEO tier |
| Wayne Lancaster | Head of Clinical Operations | L&G | Could be the medical-evidence team behind underwriting or Group Protection rehab |
| Judit F. | Head of IT & InfoSec (LGRS), "L&G Retail" | L&G | Lane names InfoSec owners for new business, no tier names the title |
| Claire Toller | CTO, OneTech Services | L&G | Shared tech unit; protection scope not shown |
| Lee Taylor | CTO | L&G | Division not shown; Retail CTO already PASS |
| Cheryl Hinton | CTO Innovation | L&G | Board seats point to Workplace Savings |
| Emese Simoradik | Product Director | L&G | Life actuary (ex Prudential Financial); line not shown |
| Dave Butcher | Product Director | L&G | Line not shown; ex Aon |
| Aran Chamberlain-Clark | Product Director | L&G | Line not shown; pensions-consulting background |
| Steven Morrison | Head Of Product Management | L&G | No line, no history |
| Andy Bergin | Head of Product and Delivery | L&G | No line, no history |
| Dan Borrill | Head of Proposition and Implementation | L&G | Line not shown; advice/wealth background |
| Rachel Cude | Head of Product Proposition Development & Oversight | L&G | Last proposition role was workplace savings |
| Natalie Bentley | Head of Pricing Execution | L&G | Protection pricing = P2, but common PRT team name |
| Matt Kirwin | Digital Product Director & Head of App | L&G | App spans lines |
| Fraser Brough | Head of Onboarding Administration | L&G | Earlier role group risk: likely scheme onboarding |
| OPG One Piccadilly Gardens | Owner | L&G | Company-named profile (standing decision 4); recommend drop |

#### Pools left out (L&G, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| A. Executives / strategy above the buyer | 6 | António Simões (Group CEO), Gareth Mee, Kate Avery (empty), Sarah Spooner (CCO), Martin Todd (Head of Strategy, Retail), James McMillan (Group Strategy) | referral | allow insurer CEOs/strategy as referral; one at most |
| B. Protection distribution / partnerships | 6 | Adrian Riddleston, Sam T. (BD, Insurance), Brett Dexter, Natalie H., Nick Birdseye, Paul Maxwell | referral | lift the adviser-distribution ban for protection partnership heads; only Riddleston and Sam T. show protection |
| C. Transformation, scope not shown | 10 | Kate Smalley, Rich Dixon, Simon Sheldon, Nina Taylor, Paul Rogers, Liz Greenwood, Russell Evans + 3 TCS-looking profiles | referral | treat unscoped transformation heads as group-wide P3 |
| D. Data and analytics | 5 | James Jarman (CDAO, Retail), Henry Carman, Mark Bird, David Stewart, Michaela Finlayson | technical-integration | add Retail data leads |
| E. Architecture, other CTO, DPO | 6 | Christina N. (CTO Group Functions), Sonya Cerutti (Head of Data Protection), Dan Kaiserman, James Bull, Neil Workman, Nik Hart | technical-integration | give architecture heads P3 |
| F. Conduct / customer outcomes | 3 | Joanne Gregory, Kerrie Mitchener-Nissen, Thomas Lucas | referral | pull Consumer Duty owners (card excludes compliance) |
| G. Protection claims | 1 | Arnaud Carette (Head of Retail Protection Claims Operations) | referral | reverse open question 4 (claims) |

## Skipped pools (script)

`skipped-detail.md`: 1123 not sent. Pools with a proposed angle are in each batch section above; add by name with `outbound_pack.py promote --names "…" --angle … --pool …`.
