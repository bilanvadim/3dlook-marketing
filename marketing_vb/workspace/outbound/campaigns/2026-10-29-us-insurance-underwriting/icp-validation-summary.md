---
product: fitxpress
profile: nick
campaign: 2026-10-29-us-insurance-underwriting
created: 2026-11-05
stage: validate
status: approved
---

# ICP Validation Summary — 2026-10-29-us-insurance-underwriting

Источник людей: Apollo (не Sales Navigator), 393 человека в 32 группах, до 15 на компанию по выбору Вадима. Все в США. Флаг `empty-profile` (48 строк) здесь значит «у Apollo одна роль»: таких людей судил по title и группе, P1 никому из них не ставил.

Версия 2 (после QC 17/20): правило «линия не видна» применено к Mutual of Omaha и к медикам The Standard так же, как к Nationwide и перестраховщикам; выровнены тиры (new business, медики перестраховщиков, по одному P1 на перестраховщика, VP underwriting operations); все отступления от тиров перечислены ниже. Прошлые версии: `people-validated-v1-2026-11-05.csv` (первый прогон), `people-validated-v2-2026-11-05.csv` (промежуточный).

## Stats

| | Людей |
|---|---|
| PASS (в SEND) | **270** |
| из них P1 / P2 / P3 | 40 / 167 / 63 |
| WEAK (REVIEW, решает Вадим) | 42 |
| FAIL | 81 |
| исключены реестром `nick` | 0 |
| FAIL по локации (Канада, UK, EU) | 0 (всё US, проверено при отборе в Apollo) |

**FAIL по причинам (81):** другая линия бизнеса у IN-перевозчика (group, stop loss, annuity, retirement, PRT, кредитное underwriting) 27 · P&C у перестраховщиков и Nationwide 23 · ушли или на пенсии 8 · функции вне персоны внутри life (финансы, PMO, design, filings, data eng, ассистент, chief of staff) 11 · DI sales и distribution 6 · технологии ниже головы и CIO 6.

**Angle (PASS):** underwriting 80 · proposition 55 · reinsurance 44 · medical 37 · technical-integration 37 · partnership 11 · referral 6.

**Распределение против `cap_per_group: 50`:** максимум 14 (28% кепа), кеп не задет нигде.

| Группа | PASS | P1 | WEAK | FAIL | Всего |
|---|---|---|---|---|---|
| Penn Mutual | 14 | 3 | 1 | 0 | 15 |
| Protective Life | 14 | 2 | 0 | 1 | 15 |
| Sammons Financial | 14 | 1 | 0 | 1 | 15 |
| John Hancock | 13 | 0 | 1 | 0 | 14 |
| Northwestern Mutual | 13 | 3 | 1 | 0 | 14 |
| Pacific Life | 12 | 0 | 1 | 2 | 15 |
| RGA US | 12 | 1 | 1 | 2 | 15 |
| Ameritas | 11 | 2 | 1 | 2 | 14 |
| Corebridge Financial | 11 | 2 | 0 | 4 | 15 |
| Lincoln Financial | 11 | 1 | 0 | 4 | 15 |
| Prudential Financial | 11 | 0 | 1 | 3 | 15 |
| SCOR Life Americas | 11 | 0 | 1 | 3 | 15 |
| Transamerica | 11 | 1 | 1 | 3 | 15 |
| Guardian Life | 10 | 1 | 2 | 3 | 15 |
| MassMutual | 10 | 3 | 0 | 5 | 15 |
| Swiss Re Americas | 10 | 1 | 3 | 2 | 15 |
| Hannover Life Re America | 9 | 1 | 0 | 0 | 9 |
| Principal Financial | 8 | 2 | 1 | 6 | 15 |
| Thrivent | 8 | 2 | 1 | 2 | 11 |
| Gen Re US | 7 | 1 | 2 | 6 | 15 |
| Symetra | 7 | 2 | 1 | 5 | 13 |
| Securian Financial | 6 | 2 | 0 | 2 | 8 |
| Zinnia | 6 | 2 | 0 | 1 | 7 |
| Bestow | 5 | 2 | 0 | 1 | 6 |
| Nationwide | 5 | 0 | 3 | 7 | 15 |
| The Standard | 5 | 1 | 5 | 5 | 15 |
| Ethos | 4 | 1 | 0 | 0 | 4 |
| Munich Re Life US | 4 | 0 | 1 | 10 | 15 |
| Ladder Life | 3 | 1 | 0 | 0 | 3 |
| iPipeline US | 3 | 1 | 0 | 0 | 3 |
| Foresters Financial US | 1 | 1 | 0 | 1 | 2 |
| Mutual of Omaha | 1 | 0 | 14 | 0 | 15 |

**Группы B и D.** Ethos и Ladder Life — группа B по решению 5 карточки (там же TruStage, в выгрузке его нет). iPipeline, Zinnia и Bestow я посчитал группой D (платформы, lane `partnership`): карточка говорит «3 platforms», но не называет их.

### Отступления от тиров карточки

По одному правилу на случай, у каждого человека причина в `reason`.

1. **P1 только с подтверждением (PPL-1 и правило координатора про `empty-profile`).** P1-title без подтверждения в headline или прошлых ролях, или без видимой линии → P2: Matt Burrill (Prudential), Warner Shue (MassMutual, прошлое на уровне team lead), Helena Roberts (Lincoln), Shawn Fourez (Protective), Jeff Winkelmann (Corebridge), Rebecca Severson (Thrivent), Terry Huisman (Principal, региональный), Daniel Buchholz (Ameritas). P1-title с `empty-profile` → P2 (15): Bryan Flynn, Michael Farrell, Joel Larson, Kathleen Coughlin, Jennifer Black, Anthony Perez, Steve Donald, Terri Drahn, Nate Berns, Scott Corbett, Keith Beckman, Jacqueline Waas, Carl Holowaty, Michael Moore, Matt Webster.
2. **VP и Head в underwriting: владельцы правил P1, владельцы процесса P2.** В карточке есть и «SVP or VP Underwriting» (P1), и «innovation, strategy, research, rules, analytics leads» (P2). На уровне VP и Head я дал P1 тем, кто владеет правилами, стратегией, research, стандартами или accelerated/automated путём: Kari Turtinen (NM), Mary Bates (Symetra), Amy Rider (Sammons), Peter Rogers (MassMutual, Head of Accelerated UW), James Mayberry (Corebridge, Head of UW Automation). P2 получили operations, solutions, platform и data: Nicole Lund, Julia Oleson, Jaime Pulsfus (NM), Don Kidd (Guardian), **TJ Doan (Pacific Life, в этом раунде P1 → P2)**, Elizabeth Cloud (Corebridge), Brandon Smithhart и Dan Garant (MassMutual).
3. **New business: P1 только для «Head of» life, DI или protection new business в title, с подтверждением (место P1 по карточке).** P1: Alycia Bellody, Jason Paine (MassMutual), **Kenneth Byrd (Protective, P2 → P1)**. P2: **Courtney Falu (Sammons, AVP, P1 → P2)**, Jamie Lane, Carly Darnell, Melinda Marcotte, Brent Ricci, David McNamara, Michele Ohler, Jakki Velez, Eric Kaiser, Christopher Lintecum. Ниже карточки (P3): new-business titles без линии у перевозчиков, которые пишут и annuities: David Wexler, Frances Freeman, Pat Grashel, Beth Abbott, Lined Mason.
4. **Pricing без видимой линии → P3** (карточка: life pricing heads P2): Tasha Boland (MassMutual), Matt Winegar (Pacific Life).
5. **Главы бизнеса → P2** (в тирах карточки их нет; C-level редко принимает инвайты, PPL-1): Salene Hitchcock-Gear (President Individual Life, Prudential), Andy Gordon (Guardian), Mindi Work (Symetra), Jeremy Horner (The Standard IDI).
6. **Медики: P1 только у перевозчика (карточка).** **Gina Guzman (Munich Re, P1 → P2)**, как Carl Holowaty (RGA). Timothy Steffen (Ameritas) на P1 как «lead Medical Director»: в title VP and Medical Director, но он единственный медик Ameritas в выгрузке и бывший президент AAIM. Это толкование.
7. **Перестраховщики: один P1, самый старший глава US life underwriting.** Dave Rengachary (RGA), Frank Chechel (Gen Re), Bess Ganeff (Swiss Re), Susan Mayer (Hannover). **Bill Moore (Swiss Re, P1 → P2)**, как David Chien и Joe Curtin у Gen Re. У SCOR и Munich Re P1 нет. James McArdle (Hannover, Reflex AUW) на P2, хотя карточка допускает P1 для head of automated underwriting: его карьера в sales и marketing. Вне списков карточки, на P3: Kevin Bettis (fac), David Elias (in-force), Mark Brann (NB enablement), Renee McClintic (UW auditor), Braam Kruger (CRO US Individual Life: карточка называет CRO group-wide не-покупателями, у него место по линии, поэтому P3, а не FAIL).
8. **Группы B и D.** Ryan Mackillop (Ladder, Director of Underwriting) на P1 как head of underwriting группы B. Laura Hale (CPO Ladder) на P2, а не P1: в записи нет прошлой роли в продуктовом руководстве (у David Malenoir-Evans в Bestow есть прошлый CPO, он P1). Vipul Sharma (CTO Ethos, в title есть Product) на P2, а не P3. Michael Hogan (Zinnia, Head of Underwriting and Fulfillment) на P1 как «head of underwriting product at group D».
9. **Продукт с частичным life scope → P3:** Mike Hamilton (Lincoln MoneyGuard, гибрид life и long-term care).

## Proposed to SEND

270 человек, по группам, внутри группы по приоритету.

| Группа | Человек | Title | P | Angle |
|---|---|---|---|---|
| Penn Mutual | Gretchen Dinucci | VP, Chief Underwriter | 1 | underwriting |
| Penn Mutual | Marianne Cumming | Vice President, Chief Medical Director | 1 | medical |
| Penn Mutual | Michael Clark | Chief Medical Officer | 1 | medical |
| Penn Mutual | Bill Bell | Chief Product Officer | 2 | proposition |
| Penn Mutual | Brent Ricci | AVP, Life New Business & ACE at Penn Mutual | 2 | proposition |
| Penn Mutual | Chris Falu | Director of Underwriting | 2 | underwriting |
| Penn Mutual | Dean Galgano | Director, Underwriting Strategy and Governance | 2 | underwriting |
| Penn Mutual | Jack Nance | Director of Underwriting | 2 | underwriting |
| Penn Mutual | Jakki Velez | Director, Life New Business | 2 | proposition |
| Penn Mutual | Michele Ohler | Vice President of New Business | 2 | proposition |
| Penn Mutual | Sharon Garner | AVP, Associate Chief Underwriter | 2 | underwriting |
| Penn Mutual | Amzad Hossain | Chief Technology Officer | 3 | technical-integration |
| Penn Mutual | Jacqueline Fallon | VP, Product Management | 3 | proposition |
| Penn Mutual | Matthew Clark | Chief Information Security Officer | 3 | technical-integration |
| Protective Life | Brad Gabel | Vice President and Chief Underwriting Officer | 1 | underwriting |
| Protective Life | Kenneth Byrd | VP, Head of Protection New Business Operations | 1 | proposition |
| Protective Life | Alex Crawford | AVP Underwriting at Protective Life | 2 | underwriting |
| Protective Life | Jamie Lane | Vice President Head of New Business Operations and Enterprise Shared Services | 2 | proposition |
| Protective Life | Kristin Blake | 2nd VP Underwriting | 2 | underwriting |
| Protective Life | Lindsay Hackney | Vice President, Life Product Strategy | 2 | proposition |
| Protective Life | Mark Barnum | 2nd Vice President Underwriting | 2 | underwriting |
| Protective Life | Russell Kolmin | SVP, Chief Product Officer - Protection Division | 2 | proposition |
| Protective Life | Shawn Fourez | Vice President of Underwriting | 2 | underwriting |
| Protective Life | Stephen Lininger | 2nd Vice President, Underwriting | 2 | underwriting |
| Protective Life | Steve Donald | Chief Underwriter | 2 | underwriting |
| Protective Life | Susan Sucha | Medical Director | 2 | medical |
| Protective Life | Frances Freeman | 2nd Vice President, New Business Operations | 3 | proposition |
| Protective Life | Justin Allen | Chief Information Security Officer | 3 | technical-integration |
| Sammons Financial | Amy Rider | Vice President, Underwriting Strategy and Mortality Management | 1 | underwriting |
| Sammons Financial | Christie Brammer | Vice President - Life Product | 2 | proposition |
| Sammons Financial | Courtney Falu | AVP, Life New Business, Policy Change and Jet Underwriting | 2 | proposition |
| Sammons Financial | Elizabeth Alexander | AVP - Life Product Management | 2 | proposition |
| Sammons Financial | Katrisha Neisse | VP & Actuary, Life Insurance Product Development | 2 | proposition |
| Sammons Financial | Kory Petoske | Director, Underwriting Rules and Innovation | 2 | underwriting |
| Sammons Financial | Matt Rise | Director, Underwriting Operations | 2 | underwriting |
| Sammons Financial | Matt Webster | Chief Medical Director | 2 | medical |
| Sammons Financial | Nicole Duncan | Director, Underwriting Operations | 2 | underwriting |
| Sammons Financial | Norma Davis | Vice President and Medical Director | 2 | medical |
| Sammons Financial | Roger Hofer | Director, Mortality Management | 2 | underwriting |
| Sammons Financial | Beth Abbott | AVP New Business and Policy Change | 3 | proposition |
| Sammons Financial | Pat Grashel | AVP, New Business | 3 | proposition |
| Sammons Financial | Paul Mocarski | Chief Information Security Officer (CISO) and Vice President IT Infrastructure | 3 | technical-integration |
| John Hancock | Andrew Langemeier | Director, Underwriting Research & Development | 2 | underwriting |
| John Hancock | Christopher Lintecum | Assistant Vice President, Digital Operations - New Business | 2 | proposition |
| John Hancock | David Moon | General Director, Life Underwriting | 2 | underwriting |
| John Hancock | Elaine Szewc | Assistant Chief Medical Director | 2 | medical |
| John Hancock | Eric Kaiser | AVP, New Business Transformation | 2 | proposition |
| John Hancock | Helen Colberg | Director, Underwriting Research and Development | 2 | underwriting |
| John Hancock | Jordan Jonassen | General Director - Life Underwriting | 2 | underwriting |
| John Hancock | Katie Kermode | Medical Director | 2 | medical |
| John Hancock | Laurie Borowski | Director, Underwriting Research & Development | 2 | underwriting |
| John Hancock | Mike Link | Associate Chief Underwriter | 2 | underwriting |
| John Hancock | Sheila Macdonnell | AVP, Medical Director | 2 | medical |
| John Hancock | Jasvinder Khera | Chief Information Security Officer | 3 | technical-integration |
| John Hancock | Kevin Hill | VP, Product Management | 3 | proposition |
| Northwestern Mutual | Brandon May | Vice President - Chief Medical Officer | 1 | medical |
| Northwestern Mutual | Kari Turtinen | VP Underwriting Risk Analytics, Standards, and Partnerships | 1 | underwriting |
| Northwestern Mutual | Tim Ranfranz | VP Chief Life Underwriter (Underwriting Excellence) | 1 | underwriting |
| Northwestern Mutual | Chris Yiannias | VP, Medical Director | 2 | medical |
| Northwestern Mutual | Dupe Adewunmi | Vice President, Medical Director | 2 | medical |
| Northwestern Mutual | Gregory Soltner | Vice President - Medical Director | 2 | medical |
| Northwestern Mutual | Jaime Pulsfus | Vice President of Underwriting Operations | 2 | underwriting |
| Northwestern Mutual | Joel Weiner | VP, Medical Director | 2 | medical |
| Northwestern Mutual | Jonathan McAllister | VP, Medical Director | 2 | medical |
| Northwestern Mutual | Judy Finney | VP Medical Director | 2 | medical |
| Northwestern Mutual | Julia Oleson | Vice President, Underwriting Operations | 2 | underwriting |
| Northwestern Mutual | Nicole Lund | VP Underwriting Solutions | 2 | underwriting |
| Northwestern Mutual | Allyson Schrader | Chief Digital and Technology Officer | 3 | technical-integration |
| Pacific Life | David McNamara | AVP, Life New Business | 2 | proposition |
| Pacific Life | Ernest Armijos | AVP Life Pricing | 2 | proposition |
| Pacific Life | Jennifer Glessner | AVP Underwriting Transformation and Customer Journey | 2 | underwriting |
| Pacific Life | John Dieck | Senior Vice President & Chief Product Officer - Consumer Markets Division | 2 | proposition |
| Pacific Life | Mark Vincent | Medical Director | 2 | medical |
| Pacific Life | TJ Doan | VP, Head of Underwriting Operations and Assistant Chief Underwriter | 2 | underwriting |
| Pacific Life | Tristan Fontugne | Head of Product R&D and Analytics - Consumer Markets Division | 2 | proposition |
| Pacific Life | Victoria Liu | AVP Life Product Strategy, Product Development | 2 | proposition |
| Pacific Life | Alan Bub | Chief Technology Officer | 3 | technical-integration |
| Pacific Life | Christopher Hall | Chief Privacy Officer | 3 | technical-integration |
| Pacific Life | Matt Winegar | AVP Actuary, New Business Repricing & Regulatory | 3 | proposition |
| Pacific Life | Tee Sun | Assistant Vice President - New Business Model Development | 3 | referral |
| RGA US | Dave Rengachary | Senior Vice President, Head of Underwriting, U.S. Mortality Markets | 1 | reinsurance |
| RGA US | Carl Holowaty | SVP and Chief Medical Director | 2 | medical |
| RGA US | Caroline Specter | Vice President, Delivery - Automated Underwriting | 2 | reinsurance |
| RGA US | Colin Deforge | Vice President, Underwriting | 2 | reinsurance |
| RGA US | Jacqueline Waas | Vice President of Underwriting Research & Development | 2 | reinsurance |
| RGA US | Jennifer Johnson | Vice President of Underwriting Innovation | 2 | reinsurance |
| RGA US | Michael Hill | Vice President, Fac Underwriting Strategy and Data Analytics | 2 | reinsurance |
| RGA US | Nathan Hill | VP & Actuary, Individual Life Pricing | 2 | reinsurance |
| RGA US | Nick Sontheimer | VP & Managing Actuary, Pricing, US Individual Life | 2 | reinsurance |
| RGA US | Braam Kruger | Vice-President & Chief Risk Officer, US Individual Life | 3 | reinsurance |
| RGA US | Mark Brann | VP, New Business Enablement | 3 | reinsurance |
| RGA US | Ron Hollowell | SVP, Chief Technology Officer | 3 | technical-integration |
| Ameritas | Kelly Halverson | Senior Vice President, Chief Actuary and Underwriting, Individual | 1 | underwriting |
| Ameritas | Timothy Steffen | Vice President and Medical Director | 1 | medical |
| Ameritas | Al Barth | Director Life Underwriting | 2 | underwriting |
| Ameritas | Beverley Sloley | Director of Underwriting | 2 | underwriting |
| Ameritas | Daniel Buchholz | Managing Director, Underwriting | 2 | underwriting |
| Ameritas | Keith Flmi | Managing Director, Individual Life Underwriting | 2 | underwriting |
| Ameritas | Kyle O'Donnell | Vice President, Life Product Development | 2 | proposition |
| Ameritas | Michelle Visconti | 2nd VP, Individual Underwriting Operations | 2 | underwriting |
| Ameritas | Scott Corbett | Vice President and Chief Underwriter | 2 | underwriting |
| Ameritas | Lined Mason | 2nd VP of New Business | 3 | proposition |
| Ameritas | Lynn Saddoris | Director, Product Management, Underwriting & Exchange Solutions | 3 | proposition |
| Corebridge Financial | James Mayberry | Vice President and Head of Underwriting Automation Solutions | 1 | underwriting |
| Corebridge Financial | Joe Townsend | Vice President Life Underwriting | 1 | underwriting |
| Corebridge Financial | Carly Darnell | VP, Head of Retail New Business Operations | 2 | proposition |
| Corebridge Financial | Elizabeth Cloud | Head of Underwriting Solutions | 2 | underwriting |
| Corebridge Financial | Jeff Winkelmann | Vice President of Underwriting | 2 | underwriting |
| Corebridge Financial | Marjorie | Head of Product, Life Insurance | 2 | proposition |
| Corebridge Financial | Sakib Siddiqi | Head of Life Pricing | 2 | proposition |
| Corebridge Financial | David Russo | Chief Technology Officer | 3 | technical-integration |
| Corebridge Financial | Gopala Kuthethur | VP - Digital Transformation | 3 | referral |
| Corebridge Financial | Leigh Steffek | VP of Digital Transformation | 3 | referral |
| Corebridge Financial | Melissa Cozart | Vice President and Chief Privacy Officer | 3 | technical-integration |
| Lincoln Financial | Heather Milligan | SVP Underwriting & New Business Life Solutions | 1 | underwriting |
| Lincoln Financial | Eric Pahl | VP, Core Life Product Development | 2 | proposition |
| Lincoln Financial | Helena Roberts | Vice President, Underwriting & New Business | 2 | underwriting |
| Lincoln Financial | Jonathan Applewhite | VP, Core Life Product Development | 2 | proposition |
| Lincoln Financial | Deborah Lineberry | AVP, New Business Technology | 3 | technical-integration |
| Lincoln Financial | Ewelina Mroczek | VP, Digital Product Transformation | 3 | referral |
| Lincoln Financial | Katie Klod | AVP - Life Underwriting & New Business IT | 3 | technical-integration |
| Lincoln Financial | Mike Hamilton | VP, Head of MoneyGuard Product Solutions | 3 | proposition |
| Lincoln Financial | Nathan Brown | VP, New Business Technology | 3 | technical-integration |
| Lincoln Financial | Patrick Sullivan | VP, InsurTech / Strategy / Enablement | 3 | referral |
| Lincoln Financial | Rachael Maurer | VP, Chief Privacy Officer | 3 | technical-integration |
| Prudential Financial | Bryan Flynn | Vice President, Underwriting | 2 | underwriting |
| Prudential Financial | Jill Fallon | VP Medical Director | 2 | medical |
| Prudential Financial | Joel Larson | Vice President, Chief Underwriter | 2 | underwriting |
| Prudential Financial | Karna Trautman | Chief Product Officer - Simplified Solutions | 2 | proposition |
| Prudential Financial | Matt Burrill | Vice President, Underwriting | 2 | underwriting |
| Prudential Financial | Michael Farrell | Vice President, Underwriting | 2 | underwriting |
| Prudential Financial | Naishami Do | VP & Medical Director | 2 | medical |
| Prudential Financial | Salene Hitchcock-Gear | President, Individual Life Insurance, | 2 | proposition |
| Prudential Financial | Dan Manley | Chief Information Security Officer | 3 | technical-integration |
| Prudential Financial | David Wexler | Vice President, New Business Operations | 3 | proposition |
| Prudential Financial | Vikram Balwani | Chief Technology Officer at Simplified Solutions - Individual Life Insurance | 3 | technical-integration |
| SCOR Life Americas | Ashley Hunt | Director - Underwriting Partnerships | 2 | reinsurance |
| SCOR Life Americas | Brooke Morgan | Director, Underwriting Solutions | 2 | reinsurance |
| SCOR Life Americas | Ed Sheehan | AVP, Underwriting | 2 | reinsurance |
| SCOR Life Americas | James Flmi | AVP-Underwriting-Quality Assurance | 2 | reinsurance |
| SCOR Life Americas | Jessica Lenhard | SVP, Head of U.S. Client Solutions for Individual Life & Annuities | 2 | reinsurance |
| SCOR Life Americas | Laura Cutshall | Director / Velogica Underwriting and Configuration | 2 | reinsurance |
| SCOR Life Americas | Michelle Spevak | AVP, Underwriting Research | 2 | reinsurance |
| SCOR Life Americas | Patrick Scanlon | AVP, Underwriting Solutions, SCOR | 2 | reinsurance |
| SCOR Life Americas | Regina Rosace | VP Medical Director | 2 | medical |
| SCOR Life Americas | Stacy Stauffer | Director - Underwriting Partnerships | 2 | reinsurance |
| SCOR Life Americas | David Elias | VP and Deputy Head of Inforce Management, Pricing and Underwriting | 3 | reinsurance |
| Transamerica | Andrew Vigar | Head of Underwriting | 1 | underwriting |
| Transamerica | Aniton William | Director Underwriting | 2 | underwriting |
| Transamerica | Ben Wadsley | Head of Product Development & Pricing - Individual Solutions | 2 | proposition |
| Transamerica | Christine Kor-Aronski | Medical Director - Remote | 2 | medical |
| Transamerica | Michael K | Medical Director | 2 | medical |
| Transamerica | Neal Hasty | Director Life Underwriting | 2 | underwriting |
| Transamerica | Terri Drahn | VP Underwriting | 2 | underwriting |
| Transamerica | Tracy Regier | Director of Underwriting | 2 | underwriting |
| Transamerica | Virginia Greene | Medical Director | 2 | medical |
| Transamerica | Steve Jensen | Global Chief Information Security Officer | 3 | technical-integration |
| Transamerica | Tricia Wood | Chief Privacy Officer | 3 | technical-integration |
| Guardian Life | Robert Shourds | Head of Life Underwriting | 1 | underwriting |
| Guardian Life | Andy Gordon | Head of Individual Life Insurance | 2 | proposition |
| Guardian Life | Anthony Perez | Vice President and Chief Underwriting Officer | 2 | underwriting |
| Guardian Life | Beth Denning | VP, Life Product Developement | 2 | proposition |
| Guardian Life | Don Kidd | Head of Underwriting Operations | 2 | underwriting |
| Guardian Life | Greg Faux | Head of Life Product Development, Individual Life | 2 | proposition |
| Guardian Life | Jennifer Black | VP, Underwriting | 2 | underwriting |
| Guardian Life | Mark Woolley | Head of DI New Business and Underwriting Technology | 3 | technical-integration |
| Guardian Life | Smitha Jagalur | Head of Life New Business and Underwriting Technology-IM New Business | 3 | technical-integration |
| Guardian Life | Steve Rullo | Chief Digital and Technology Officer | 3 | technical-integration |
| MassMutual | Alycia Bellody | Head of Life New Business | 1 | proposition |
| MassMutual | Jason Paine | Head of Disability Underwriting and New Business | 1 | underwriting |
| MassMutual | Peter Rogers | Head of Accelerated Underwriting | 1 | underwriting |
| MassMutual | Brandon Smithhart | Underwriting Platform Head | 2 | underwriting |
| MassMutual | Dan Garant | Head of Data Science - Underwriting | 2 | underwriting |
| MassMutual | Kathleen Coughlin | DI Chief Underwriter, AVP | 2 | underwriting |
| MassMutual | Melinda Marcotte | Head of MMSD Life New Business | 2 | proposition |
| MassMutual | Warner Shue | Head of Underwriting | 2 | underwriting |
| MassMutual | Dhru Swadia | Head of New Business Technology | 3 | technical-integration |
| MassMutual | Tasha Boland | Head of New Business Analysis and Pricing Review | 3 | proposition |
| Swiss Re Americas | Bess Ganeff | Senior Vice President and Head of Underwriting Americas | 1 | reinsurance |
| Swiss Re Americas | Bill Moore | Chief Underwriter, Managing Director | 2 | reinsurance |
| Swiss Re Americas | Cynthia Landry | Vice President of Life Underwriting at Swiss Re Life and Health | 2 | reinsurance |
| Swiss Re Americas | Dave Loparco | Vice President, Head of U.S. Underwriting Risk Management | 2 | reinsurance |
| Swiss Re Americas | Eric Hoerr | Vice President, Underwriting | 2 | reinsurance |
| Swiss Re Americas | Kevin O'Hanlon | Vice President & Underwriting Client Relationship Lead | 2 | reinsurance |
| Swiss Re Americas | Kimberly Poulopoulos | Head Mortality Innovation & Transformation, Senior Vice President | 2 | reinsurance |
| Swiss Re Americas | Mandy Bovan | Vice President, Manager Underwriting Solutions | 2 | reinsurance |
| Swiss Re Americas | Vicki Garrett | Vice President, U.S. Facultative Underwriting Manager | 2 | reinsurance |
| Swiss Re Americas | Samrat Dua | Chief Digital & Technology Officer, Swiss Re Reinsurance | 3 | technical-integration |
| Hannover Life Re America | Susan Mayer | Vice President, Chief Underwriter | 1 | reinsurance |
| Hannover Life Re America | Brian Hiserote | VP Underwriting | 2 | reinsurance |
| Hannover Life Re America | Elena | Vice President, Medical Director | 2 | medical |
| Hannover Life Re America | Eric Flender | VP, Underwriting | 2 | reinsurance |
| Hannover Life Re America | James McArdle | Vice President- Reflex Underwriting Solutions at Hannover Life Reassurance Company | 2 | reinsurance |
| Hannover Life Re America | Jeremy Vest | Vice President, Underwriting | 2 | reinsurance |
| Hannover Life Re America | Sean Conrad | Senior Vice President, Head of Traditional Life Pricing and Data Analytics | 2 | reinsurance |
| Hannover Life Re America | Kevin Bettis | VP, Facultative Underwriting | 3 | reinsurance |
| Hannover Life Re America | Renee' McClintic | AVP Underwriting Auditor | 3 | reinsurance |
| Principal Financial | Jeff Kruger | AVP - Business Owner and Chief Underwriter | 1 | underwriting |
| Principal Financial | Kris Vanderkooy | Chief Medical Director | 1 | medical |
| Principal Financial | Cody Schiffer | Assistant Chief Underwriter | 2 | underwriting |
| Principal Financial | Josh Heidemann | Assistant Chief Underwriter | 2 | underwriting |
| Principal Financial | Nate Berns | AVP & Chief Underwriter Life | 2 | underwriting |
| Principal Financial | Terry Huisman | Regional Chief Underwriter | 2 | underwriting |
| Principal Financial | Bryant Fuller | MD, Head of Product for Individual Solutions | 3 | proposition |
| Principal Financial | Michele Ramsey | AVP - Chief Privacy Officer | 3 | technical-integration |
| Thrivent | Jean Pfundtner | Chief Life Underwriter | 1 | underwriting |
| Thrivent | Ronelle Moe | Chief Medical Director | 1 | medical |
| Thrivent | Rebecca Severson | Chief Underwriter | 2 | underwriting |
| Thrivent | Rhonda Steffel-Heling | Associate Medical Director | 2 | medical |
| Thrivent | Brett Brunick | Chief Digital & Technology Officer | 3 | technical-integration |
| Thrivent | Jeffrey Einhorn | Chief Technology Officer | 3 | technical-integration |
| Thrivent | Kenny Membreno | Chief Information Security & Privacy Officer | 3 | technical-integration |
| Thrivent | Ryan Hawkins | Chief Technology Officer | 3 | technical-integration |
| Gen Re US | Frank Chechel | SVP, Head of Individual Life | 1 | reinsurance |
| Gen Re US | Cecil Ramotar | Underwriting Vice President | 2 | reinsurance |
| Gen Re US | David Chien | Vice President, Chief Underwriter, Individual Life | 2 | reinsurance |
| Gen Re US | Georgette Chekiri | Vice President and Medical Director | 2 | medical |
| Gen Re US | Joe Curtin | VP Chief Underwriter - IL Production | 2 | reinsurance |
| Gen Re US | Michael Clift | Vice President, Underwriting Executive - Individual Products Division | 2 | reinsurance |
| Gen Re US | Sarah Fusco | VP, Underwriting Executive | 2 | reinsurance |
| Symetra | Mary Bates | SVP Underwriting Risk Management and Strategic Direction | 1 | underwriting |
| Symetra | Mike Derrig | Chief Underwriter | 1 | underwriting |
| Symetra | Harry Stanger | Medical Director | 2 | medical |
| Symetra | Mindi Work | EVP Individual Life Division and Emerging Solutions | 2 | proposition |
| Symetra | Silke Lavallee | VP, Life Product & Economics | 2 | proposition |
| Symetra | Dimitri Robert | Chief Technology Officer | 3 | technical-integration |
| Symetra | Jamal Bodey-Burks | Chief Information Security Officer | 3 | technical-integration |
| Securian Financial | John Helberg | Chief Underwriter, Individual Markets | 1 | underwriting |
| Securian Financial | Shona Murray | Chief Medical Director | 1 | medical |
| Securian Financial | Brian Rock | Director & Actuary, Life Product Development | 2 | proposition |
| Securian Financial | Gay Kemmis | 2nd VP, Life Underwriting Operations | 2 | underwriting |
| Securian Financial | Jeffrey Noren | Actuarial Director - Life Product Development | 2 | proposition |
| Securian Financial | Lara Shemtob | Medical Director | 2 | medical |
| Zinnia | Michael Celi | Chief Product Officer | 1 | partnership |
| Zinnia | Michael Hogan | Head of Underwriting & Fulfillment | 1 | partnership |
| Zinnia | Vikash Rai | VP, Head of Product, System of Record. | 2 | partnership |
| Zinnia | Brad Medd | Chief Technology Officer | 3 | technical-integration |
| Zinnia | Jennifer Abboud | Head of Product Operations | 3 | partnership |
| Zinnia | Timothy Nash | Chief Information Security Officer | 3 | technical-integration |
| Bestow | David Malenoir-Evans | Chief Product Officer | 1 | partnership |
| Bestow | Laura Boylan | VP, Underwriting Solutions | 1 | partnership |
| Bestow | Eric Lee | Vice President of Product Management | 2 | partnership |
| Bestow | Dave Belanger | Chief Security & Privacy Officer | 3 | technical-integration |
| Bestow | David Peters | Director of Underwriting | 3 | partnership |
| Nationwide | Matt Mylroie | AVP, Life Product Management | 2 | proposition |
| Nationwide | Michael Moore | Chief Medical Director | 2 | medical |
| Nationwide | Paulo Pinho | Senior Medical Director | 2 | medical |
| Nationwide | Tim Lyons | Vice President & Chief Information Security Officer | 3 | technical-integration |
| Nationwide | Todd Lukens | SVP, Chief Technology and Information Security Officer | 3 | technical-integration |
| The Standard | Michael Ash-Dollowitch | Director & Chief Underwriter, IDI | 1 | underwriting |
| The Standard | Jeremy Horner | Vice President, Individual Disability Insurance and Corporate Development | 2 | proposition |
| The Standard | Tony Fung | Assistant Vice President, IDI Underwriting and GSI | 2 | underwriting |
| The Standard | Jody Pfeifer | Chief Product Officer | 3 | proposition |
| The Standard | Rajesh Mondkar | AVP Digital Transformation | 3 | referral |
| Ethos | Nichole Myers | Chief Underwriter | 1 | underwriting |
| Ethos | Ashwath Muralidharan | Vice President of Product Management | 2 | proposition |
| Ethos | Sean Flanagan | Senior Director, Underwriting Automation | 2 | underwriting |
| Ethos | Vipul Sharma | Chief Technology Officer (Product, Engineering, Data/AI) | 2 | technical-integration |
| Munich Re Life US | Brad Heltemes | VP and Medical Director, R&D | 2 | medical |
| Munich Re Life US | Gina Guzman | Vice President & Chief Medical Director | 2 | medical |
| Munich Re Life US | Patti Arellano | Head of Individual Life New Business | 2 | reinsurance |
| Munich Re Life US | Robert Lund | Vice President and Medical Director | 2 | medical |
| Ladder Life | Ryan Mackillop | Director of Underwriting | 1 | underwriting |
| Ladder Life | Keerthi Mandala | Vice President of Product Management | 2 | proposition |
| Ladder Life | Laura Hale | Chief Product Officer | 2 | proposition |
| iPipeline US | Katie Kahl | Chief Product Officer | 1 | partnership |
| iPipeline US | Alex Tompkins | Vice President of Product Management | 2 | partnership |
| iPipeline US | Chris Cella | Vice President of Product Management | 2 | partnership |
| Foresters Financial US | Paul Greene | Chief Underwriting Officer | 1 | underwriting |
| Mutual of Omaha | Thomas Ferguson | Chief Underwriter | 3 | underwriting |

## WEAK — нужно решение Вадима

42 человека. Рекомендация по каждой группе стоит в начале причины:
- **Взять P3 (11): перевозчик, underwriting-функция ясна, линия не видна.** Erdahl, Foran, Nattis (The Standard), Rahmani, Allocco (Nationwide), Kaczmar (Ameritas), Dawson (Principal), Pemberton (Prudential), Pace (Guardian), Donna Rogers и Mike Bauer (supervising chief underwriters MoO). Внутри одного перевозчика человек из соседней линии знает, кто ведёт life underwriting.
- **Решение по функции (1):** TJ Clayton (Pacific Life). Если «New Business Acquisition» значит приём заявок, то P3 `proposition`, если M&A, то не брать.
- **Не брать (30):**
  - 8 по логике пула E: перестраховщики без видимой линии (Sirkar, Eberle, Bandele, Ospalik, Sawyer, Drabik) и две чужие линии (Cam Cook, long-term care; Teresa Loker, банковский кредит). P&C и life у перестраховщиков — разные команды, через них к life underwriting не попасть.
  - 11 «Chief Underwriter» MoO уровня team lead без линии. MoO пишет Medicare supplement, а маршрут внутрь компании уже дают Ferguson (PASS) и два supervising.
  - 2 associate medical directors The Standard (Ingram, Syna): похоже на DI claims, а claims карточка не берёт.
  - 3 с guaranteed или simplified issue (Knauss, Clu, Massey): anti-case.
  - 5, у кого headline спорит с Apollo (Donna Kim, Lori Wilt, Lou Desorbo, Frank Schmid, Susan Radford): похоже, ушли.
  - 1 дубль места: Valickus John (Symetra), life chief underwriter там Mike Derrig (P1). Если всё же брать, порядок имени неясен, приветствие «John» проверить до сообщений.

| Человек | Title | Группа | Почему на грани |
|---|---|---|---|
| Kevin Erdahl | Vice President, Underwriting | The Standard | **Взять P3.** VP Underwriting at The Standard, line not stated: most underwriting there is group, and IDI is the in-scope line. (angle: underwriting) |
| Tom Foran | Vice President, Underwriting and Product Development | The Standard | **Взять P3.** VP Underwriting and Product Development at The Standard, line not stated (group or individual DI). (angle: underwriting) |
| Jeffrey Nattis | Director of Medical Underwriting | The Standard | **Взять P3.** Director of Medical Underwriting at The Standard, earlier sales support at a health plan: line not stated, and much medical underwriting there is group evidence of insurability. (angle: underwriting) |
| Khalid Rahmani | Director of Underwriting | Nationwide | **Взять P3.** Director of Underwriting at Nationwide, line not stated: most Nationwide underwriting is P&C. (angle: underwriting) |
| Cathy Allocco | Vice President, Underwriting, Product, and Pricing | Nationwide | **Взять P3.** VP Underwriting, Product and Pricing at Nationwide, line not stated and earlier roles under the P&C brand. (angle: underwriting) |
| Pete Kaczmar | Director - Underwriting National Accounts & National Partners | Ameritas | **Взять P3.** Director of Underwriting for National Accounts and Partners: at Ameritas this may be group dental and vision (out) or individual partner channels (in). (angle: underwriting) |
| Heather Dawson | Head of Product Strategy, Income Solutions | Principal Financial | **Взять P3.** Head of Product Strategy, Income Solutions: may be retirement income (out) or income-protection DI (in); earlier roles are workplace. (angle: proposition) |
| Brian Pemberton | Vice President, New Business Underwriting | Prudential Financial | **Взять P3.** VP New Business Underwriting, but his career is group national-accounts underwriting, so the Prudential role may sit in Group Insurance (out). (angle: underwriting) |
| Micah Pace | Head of Underwriting Operations | Guardian Life | **Взять P3.** Head of Underwriting Operations, but earlier roles are group portfolio underwriting, so this may be Guardian's group benefits side (out). (angle: underwriting) |
| Donna Rogers | Supervising, Chief Underwriter | Mutual of Omaha | **Взять P3.** Supervising Chief Underwriter at MoO, earlier risk-management team lead and senior underwriter at a group and DI carrier: senior, but individual life not visible. (angle: underwriting) |
| Mike Bauer | Supervising Chief Underwriter | Mutual of Omaha | **Взять P3.** Supervising Chief Underwriter at MoO, promoted from chief underwriter there: senior enough to route internally, but no line in any role. (angle: underwriting) |
| TJ Clayton | VP, New Business Acquisition | Pacific Life | **По функции.** VP New Business Acquisition: unclear whether this is new-business intake (in) or acquiring blocks and partners (out). (angle: proposition) |
| Nabaneeta Sirkar | Deputy Global Chief Underwriting Officer- Pricing | Gen Re US | **Не брать (логика пула E).** Deputy Global CUO for pricing at Gen Re, line not stated: Gen Re CUO titles in this export are P&C. (angle: reinsurance) |
| Rachel Eberle | AVP, Underwriting Risk Management | Munich Re Life US | **Не брать (логика пула E).** AVP Underwriting Risk Management, line not stated: Munich Re's US underwriting in this export is mostly P&C. (angle: reinsurance) |
| Kwame Bandele | VP, Treaty Underwriting | SCOR Life Americas | **Не брать (логика пула E).** VP Treaty Underwriting at SCOR in Chicago, line not stated: treaty underwriting titles are usually P&C. (angle: reinsurance) |
| Craig Ospalik | Senior Vice President, Treaty Underwriting Leader | Swiss Re Americas | **Не брать (логика пула E).** SVP Treaty Underwriting Leader at Swiss Re in Schaumburg, earlier regional treaty underwriter at GE Reinsurance: line not stated, treaty titles are usually P&C. (angle: reinsurance) |
| Peter Sawyer | Vice President of Underwriting | Swiss Re Americas | **Не брать (логика пула E).** VP Underwriting at Swiss Re, one Apollo role and line not stated: Swiss Re US underwriting is P&C-heavy. (angle: reinsurance) |
| Dan Drabik | Vice President Underwriting | Swiss Re Americas | **Не брать (логика пула E).** VP Underwriting at Swiss Re, one Apollo role and line not stated: Swiss Re US underwriting is P&C-heavy. (angle: reinsurance) |
| Cam Cook | Vice President, Underwriting | Transamerica | **Не брать (логика пула E).** VP Underwriting, but the earlier role is VP claims and underwriting for long-term care, which is outside life or DI. (angle: underwriting) |
| Teresa Loker | Director of Underwriting | Thrivent | **Не брать (логика пула E).** Director of Underwriting at Thrivent, but her career is bank credit management: may be lending underwriting. (angle: underwriting) |
| Daren Hotham | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO Chief Underwriter whose past roles (Berkshire Hathaway underwriter, Unum analyst) show no individual life; MoO also writes Medicare supplement (out). (angle: underwriting) |
| Mike Markvicka | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** Omaha-based MoO Chief Underwriter with one Apollo role: life, DI or Medicare supplement cannot be told apart. (angle: underwriting) |
| Tony Consolo | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** Columbus-based MoO Chief Underwriter, earlier a Nationwide manager and VP underwriting at North American Benefits: no individual life line visible. (angle: underwriting) |
| Andrew Haynes | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO Chief Underwriter whose only earlier role is claims intake at Lincoln: no underwriting line visible. (angle: underwriting) |
| Kevin Dolezal | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO Chief Underwriter, earlier MoO underwriting consultant and HealthMarkets agent: health-insurance history makes Medicare supplement as likely as life. (angle: underwriting) |
| Steve Bauman | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO Chief Underwriter in Fort Calhoun, Nebraska, nothing in the row beyond the title: business line unknown. (angle: underwriting) |
| Andrew Andersen | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO Chief Underwriter in Blair, Nebraska; Apollo has only this role, so the line (life, DI, Medicare supplement) is unreadable. (angle: underwriting) |
| Thomas Andrews | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** One of the Omaha team-lead Chief Underwriters at MoO, with no headline or history to show which product line he underwrites. (angle: underwriting) |
| Sallie Larmon | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** Title only: Chief Underwriter at MoO in Omaha; nothing says individual life rather than Medicare supplement. (angle: underwriting) |
| Dave Wulf | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** MoO team-lead Chief Underwriter with an empty record: whether he underwrites individual life is unknown. (angle: underwriting) |
| Al Bruner | Chief Underwriter | Mutual of Omaha | **Не брать (MoO team lead).** Single Apollo role as MoO Chief Underwriter; no life, DI or Medicare supplement marker anywhere in the row. (angle: underwriting) |
| Shirley Ingram | Associate Medical Director | The Standard | **Не брать (claims?).** Associate Medical Director at The Standard who is also a rheumatology professor: reads like a part-time DI claims consultant, and claims are not pulled. (angle: medical) |
| Deborah Syna | Associate Medical Director | The Standard | **Не брать (claims?).** Associate Medical Director at The Standard, neurologist and script consultant by headline: underwriting or claims role unclear, likely part-time consulting. (angle: medical) |
| Vicki Knauss | Head of Risk Management Strategies & Underwriting Multi Life Disability | Guardian Life | **Не брать (guaranteed issue).** Heads underwriting for multi-life DI: individual DI line, but multi-life is mostly guaranteed standard issue (anti-case). (angle: underwriting) |
| Wade Clu | Director of Multi Life Underwriting | Penn Mutual | **Не брать (guaranteed issue).** Director of Multi-Life Underwriting: multi-life cases are mostly guaranteed or simplified issue, and his background is advanced marketing. (angle: underwriting) |
| Teresa Massey | VP, Underwriting & Operations - Institutional Life Insurance | Nationwide | **Не брать (guaranteed issue).** VP Underwriting for institutional (corporate-owned) life, which is mostly guaranteed or simplified issue. (angle: underwriting) |
| Donna Kim | VP Medical Director | Northwestern Mutual | **Не брать (headline).** Apollo says VP Medical Director at Northwestern Mutual, but her headline says medical consultant at Unum: current employer unclear. (angle: medical) |
| Lori Wilt | Medical Director | John Hancock | **Не брать (headline).** Apollo says Medical Director at John Hancock, but her headline says medical consultant at MassMutual: current employer unclear. (angle: medical) |
| Lou Desorbo | Global Chief Information Security Officer | RGA US | **Не брать (headline).** Global CISO per Apollo, but his headline reads as a portfolio of advisory and virtual-CSO roles: current RGA role uncertain. (angle: technical-integration) |
| Frank Schmid | Chief Technology Officer | Gen Re US | **Не брать (headline).** CTO per Apollo, but his headline says Senior Advisor: may have stepped back. (angle: technical-integration) |
| Susan Radford | Chief Underwriter | Mutual of Omaha | **Не брать (headline).** Chief Underwriter per Apollo, but her headline says Lead Crew Chief: the title may be wrong. (angle: underwriting) |
| Valickus John | Vice President/Chief Underwriter | Symetra | **Не брать (дубль места).** VP and Chief Underwriter at Symetra with no line stated: Symetra's individual life chief underwriter is Mike Derrig (P1) and its other big underwriting lines are group and stop loss; name order unclear (first_name Valickus), check the greeting before messages. (angle: underwriting) |

## Кого оставили за бортом: пулы

Полный список: `skipped-detail.md` (123 человека = 81 FAIL + 42 WEAK). Категории скрипта (other, executives) перемешивают причины, поэтому ниже пулы собраны по причине отказа. Только пулы со старшими ролями, WEAK разобраны выше.

| Пул | Людей | Кто (3-5 имён) | Предлагаемый angle | Что нужно поменять в гипотезе, чтобы их взять |
|---|---|---|---|---|
| A. Функции вне персоны внутри individual life | 11 | Ashley Destito (VP, Head of Individual Life FP&A, Prudential); Lynn Brown (Executive Liaison to Head of Protection New Business & Underwriting, MassMutual); Robert Reynolds (Director Individual Life Financial Management, Securian); Mike Beebe (Head of Product Design, Thrivent); Tyra Wheatley (VP Life Product Document Solutions, Corebridge) | `referral` | Lane `referral` для не-покупателей в relevant function внутри life (PPL-2: referral 21/475 против 21/958 у buyer lanes; решение Вадима 3 «lane для каждой функции»). **Рекомендую** Lynn Brown (прямой путь к head of protection NB and UW), Ashley Destito, Robert Reynolds |
| B. DI sales и distribution | 6 | Frank Mikalonis, Bob Herman, Marian Coffey, Mike Sir (DI Regional VPs, Principal); Scott Delisi (VP DI Distributions, Ameritas); Teague Jim (Regional Director IDI, The Standard) | `referral` | Снять «agent-facing sales» из Not the buyer для referral. PPL-3: partnerships, BD и sales ответили 6/83, лучше всех функций. Но эти люди продают агентам, правил underwriting у них нет. Брать только как referral на underwriting |
| C. Технологии ниже головы и CIO | 6 | Richard Leechow (CIO, Corebridge); Thomas Watson (SVP Divisional CIO, Lincoln); David Goodrich (SVP Deputy CTO, Corebridge); Eric Svalstad (Deputy CISO, Transamerica); Carolyn Stewart (SVP COO Global Technology, RGA) | `technical-integration` | Убрать CIO из исключений персоны. **Не рекомендую**: CTO и CISO этих компаний уже в SEND, engineering ответил 1/90 (PPL-3) |
| D. Другая линия бизнеса у IN-перевозчика | 27 | Chris Reed (SVP Group Protection Underwriting, Lincoln); Tina Haley (SVP Head of Product, Corebridge, retirement); Jessica Vanscavish (Head of Disability, Absence, Life and Supplemental Health Product, Guardian group); Jennifer Tabb (VP Institutional Markets NB, RGA, PRT); Nick Weber (VP Head of Annuity Product, Pacific Life) | `referral` | Снять бизнес-линейный фильтр (group, worksite, annuity, retirement, stop loss): это anti-case гипотезы. **Не рекомендую**. Если брать, то только SVP-уровень (Reed, Haley) как referral на коллег из individual life |
| E. P&C у перестраховщиков и Nationwide | 23 | Erin Kang (CUO North America Treaty, Gen Re); Catherine Smith (CUO, Munich Re); Julie Hespe (EVP Underwriting Performance, Nationwide E&S); Victor Min (SVP Head of Treaty Cat UW, Gen Re); Benjamin Skurek (SVP CUO Mutual Treaty, Gen Re) | `referral` | Снять правило «P&C staff at reinsurers». **Не рекомендую**: P&C и life у перестраховщиков — разные юрлица с разными командами, через них к life underwriting не попасть |
| F. Ушли или на пенсии | 8 | Denise Bates (ex Head of Life Underwriting, Guardian); Robert Anderegg (Former VP UW, Swiss Re); Kevin Smith (ушёл в Dual Re); Rob Tourt, Terry Feeney, Dick Byrne | — | Взять нельзя. Leaver становится referral, только если сам назвал преемника (PPL-5). Здесь не назвал никто |

Добавить по имени (пул A, рекомендованные трое): `python3 scripts/outbound_pack.py promote --campaign 2026-10-29-us-insurance-underwriting --names "Lynn Brown; Ashley Destito; Robert Reynolds" --angle referral --pool A`

## Top concerns

- **Выгрузка по компании у перестраховщиков принесла P&C.** Munich Re Life US: 10 из 15 человек — P&C из Munich Re America (property, casualty, treaty, E&S), прошли 4, и среди них нет ни одного head of underwriting и ни одного P1: только head of IL new business и три medical directors. У Gen Re 6 P&C, у SCOR 2, у Swiss Re treaty-лидер в WEAK. Apollo проверял домен (munichre.com, genre.com), а домен у life и P&C один. Если Munich Re нужен с главой underwriting, нужен отдельный Apollo-pull по title с «Life».
- **Mutual of Omaha: 1 PASS и 14 WEAK.** 13 человек с title «Chief Underwriter» (у MoO это team lead) и 2 supervising. Линия не видна ни у кого, а MoO пишет ещё и Medicare supplement (FAIL по карточке). Прошёл только Thomas Ferguson: у него в прошлом underwriting в Lincoln. VP underwriting MoO в выгрузке нет. Если MoO важен, нужен Apollo-pull по title с «Individual Life» или «Life Underwriting».
- **«VP Underwriting» без линии у мультилинейных перевозчиков.** У Prudential, Guardian, Transamerica и Protective такие люди прошли на P2 по title (часть из них с `empty-profile`), потому что у этих перевозчиков underwriting в основном life. Где карьера указывала на group (Pemberton, Pace, Anderson, Workman), я снял или поставил WEAK. Остальные — риск: небольшая доля может оказаться в group benefits.
- **Nationwide и The Standard — в основном не наша линия.** Nationwide: 6 FAIL за P&C, 1 FAIL за chief of staff CTO, 3 WEAK. Прошли life product, два medical director и двое из security и CTO. The Standard: 5 FAIL (group, retirement, sales, data engineering), 5 WEAK. Прошли Michael Ash-Dollowitch (P1, IDI chief underwriter), Tony Fung, Jeremy Horner, CPO и digital transformation (referral).
- **Ушедшие, несмотря на проверку Apollo.** 8 человек ушли или на пенсии по headline или title, ещё 5 WEAK, у кого headline спорит с работодателем из Apollo. Это то же, что PPL-5: проверка работодателя в Apollo не ловит тех, кто ушёл недавно.
- **Имена из Apollo.** У нескольких PASS в фамилии стоят credentials: Keith Flmi (Beckman), Chris Falu (Feldges), Courtney Falu (Jacobson), James Flmi (Atkins). Nick пишет по first name, так что приветствие верное, но фамилии в import-файле неверны. Valickus John (WEAK): порядок имени неясен.
- **Foresters Financial US — без пути ниже C-level.** В выгрузке только CUO Paul Greene (P1) и annuity VP (FAIL). PPL-1 просит хотя бы одного человека ниже C-level, а в экспорте такого нет.
- **Lane technical-integration: 37 PASS (14% SEND).** Карточка ставит CTO, CISO и privacy officers на P3, поэтому все они в SEND. Но PPL-3: engineering ответил 1/90. Больше всего у Thrivent: 4 tech из 8 PASS (две строки CTO, CDTO, CISO). Если Вадим хочет урезать, первыми кандидатами будут дубли CTO и CISO при живом CDTO (Thrivent, Nationwide).

## Vadim — please confirm

1. Список SEND (270 человек)?
2. WEAK (42): мой вариант — взять 11 «перевозчик, линия не видна» как P3 (Erdahl, Foran, Nattis, Rahmani, Allocco, Kaczmar, Dawson, Pemberton, Pace, Donna Rogers, Mike Bauer). TJ Clayton — по функции. Остальные 30 не брать: 8 перестраховщики без линии, LTC и кредит (логика пула E), 11 team-lead chief underwriters MoO, 2 associate MD The Standard (claims), 3 guaranteed issue, 5 со спорным headline, Valickus John.
3. Пулы: берём **A** (`referral`: Lynn Brown, Ashley Destito, Robert Reynolds, команда выше)? **B** (DI sales как `referral`)? C, D, E и F не рекомендую. Добавлю через `promote`, нового раунда не нужно.
4. Кеп: ни одна группа к 50 не подошла (максимум 14), менять нечего. Mutual of Omaha и Munich Re: делаем Apollo-pull по life-title или идём с тем, что есть (MoO 1 PASS, Munich Re 4 PASS)?

## Top-up 2026-11-05

После чекпоинта Вадим одобрил список (270 SEND, 11 рекомендованных WEAK как P3, пулы A и B как `referral`; `promote` запускает координатор) и Apollo-дотяжку двух тонких аккаунтов. Пришли 13 человек: 9 Mutual of Omaha и 4 Munich Re Life US. Правила те же, что во втором раунде. Цифры ниже — до `promote` координатора.

**Итог по 406 людям:** PASS 278 (P1 40 / P2 174 / P3 64) · WEAK 46 · FAIL 82. Angle: underwriting 83 · proposition 55 · reinsurance 47 · medical 39 · technical-integration 37 · partnership 11 · referral 6. Кеп не задет, максимум 14 на группу. Прошлая версия: `people-validated-v3-2026-11-05.csv`.

| Человек | Title | Группа | Решение | Почему |
|---|---|---|---|---|
| Kurtis Stewart | SVP, Underwriting | Mutual of Omaha | PASS P2 `underwriting` | Старший владелец underwriting, которого не было в первой выгрузке; раньше lead underwriter в Lincoln (по тому же правилу, что Ferguson). Линии нет в title, поэтому не P1 |
| Marty Johnson | VP Life Underwriting | Mutual of Omaha | PASS P2 `underwriting` | Линия в title; `empty-profile`, поэтому не P1 |
| Timothy Tse | VP & Medical Director | Mutual of Omaha | PASS P2 `medical` | VP-медик перевозчика, как у других перевозчиков |
| Anjali Masand | VP & Medical Director | Mutual of Omaha | PASS P2 `medical` | Раньше медик в New York Life |
| Tracey Schifferdecker | Chief Individual Life Underwriter | Mutual of Omaha | PASS P3 `underwriting` | Линия явная, но «chief» у MoO — уровень team lead (этот title у двоих), как у Ferguson |
| Jennifer Lingenfelter | VP of Underwriting | Mutual of Omaha | WEAK | Линии нет ни в одной роли |
| Jim Monahan | VP, Underwriting | Mutual of Omaha | WEAK | Линии нет, вся карьера внутри MoO |
| Joe Maginn | VP - Underwriting | Mutual of Omaha | WEAK | Линии нет, раньше supervisory chief underwriter |
| Lori Brown | Chief Individual Life Underwriter | Mutual of Omaha | FAIL | На пенсии по headline (это не Lynn Brown из пула A) |
| Jennifer Dalton | Director of Accelerated Underwriting | Munich Re Life US | PASS P2 `reinsurance` | Ведёт accelerated-программу; в прошлом life underwriting |
| Greg Dewey | 2nd VP, Underwriting Services | Munich Re Life US | PASS P2 `reinsurance` | Раньше AVP Underwriting Operations в John Hancock |
| Shane Banks | Director, Underwriting Pricing and Client Support | Munich Re Life US | PASS P2 `reinsurance` | Раньше technical underwriting на Velogica (SCOR) |
| Tim Rieder | Director Underwriting Risk | Munich Re Life US | WEAK | Линии нет, Чикаго: тот же случай, что Rachel Eberle |

**Что изменилось по аккаунтам.**
- **Mutual of Omaha:** 1 → 6 PASS (Stewart, Johnson, Tse, Masand, Schifferdecker и Ferguson), 17 WEAK, 1 FAIL. Life-цепочку теперь видно напрямую.
- **Munich Re Life US:** 4 → 7 PASS, 2 WEAK. P1 по-прежнему нет: в дотяжке нет главы US life underwriting, только директора.

**Новые WEAK (4) — нужно решение Вадима.** Я бы не брал никого из четырёх.
- Три VP Underwriting MoO без линии: life-цепочка MoO теперь в SEND напрямую, поэтому довод «человек из соседней линии подскажет, кто ведёт life» здесь больше не работает, а Medicare supplement исключить нельзя.
- Tim Rieder — по тому же правилу, что Eberle.

## Checkpoint 2026-11-05 (coordinator)

Vadim approved: every PASS (278 after the top-up), the 11 recommended WEAK as P3 (pool W), pool A (3) and pool B (6) as `referral`. The other WEAK and pools C-F stay out. After `promote`: **298 to send**, largest company 14, cap 50 untouched. Mike Sir (pool B) went in with `--force` (empty-profile, approved by name). **Before messages:** «Teague Jim» (pool B, The Standard) has the same reversed-name risk as «Valickus John»: check the LinkedIn display name and fix `first_name` before writing his pair.
