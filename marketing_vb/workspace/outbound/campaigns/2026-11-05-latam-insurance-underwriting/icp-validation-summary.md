---
product: fitxpress
profile: katya
campaign: 2026-11-05-latam-insurance-underwriting
created: 2026-11-09
stage: validate
status: approved
---

# ICP Validation Summary — 2026-11-05-latam-insurance-underwriting

**Checkpoint 2026-11-09 (Vadim; `hypothesis.md` → `Vadim's decisions 2026-11-09 (step 4 checkpoint)`):** all WEAK taken except the six company-named profiles; pools A, B, C, D and F taken as `referral` P3 (A opens the country rows `Hannover Re Brasil` and `SCOR Brasil`, where research found no L&H team); no second Sales Navigator pull, an Apollo top-up for the gap accounts instead («добери з аполо якщо треба»): 11 new people, judged by a fresh validator (PASS 6, WEAK 3 taken, FAIL 2). Brasilseg's President (Júlio Cezar Oliveira, FAIL for an empty profile, now confirmed by Apollo) joins pool B; BBVA Seguros' President from Apollo FAILs as a probable name collision (headline "Cobol Developer").

## Stats

**After Vadim's checkpoint (2026-11-09): 489 people · SEND 122 (P1 9 · P2 37 · P3 76) · WEAK left 6 · FAIL 361 · excluded by registry 0.** No group is near `cap_per_group: 50` (largest: Bradesco Vida e Previdência 21).

SEND by origin: validator PASS 68 · WEAK taken 31 · pool A 3 · pool B 7 · pool C 5 · pool D 3 · pool F 5

Angles: referral 40 · proposition 32 · technical-integration 19 · underwriting 16 · reinsurance 14 · medical 1

Sources of the SEND list: Sales Navigator 73, Apollo 49 (Apollo credits 78 in total).

Location: 5 FAIL by location before the checkpoint; the Brazil-located reinsurer heads now sit in the new Brazil rows (pool A). **US-located 0, Spain-located 0, other Latin America 0**: all 489 are in Brazil or Mexico.

| Group | People | SEND (P1/P2/P3) | WEAK | FAIL |
|---|---|---|---|---|
| BBVA Seguros México | 251 | 13 (0/4/9) | 0 | 238 |
| Bradesco Vida e Previdência | 57 | 21 (0/5/16) | 1 | 35 |
| Icatu Seguros | 35 | 20 (0/8/12) | 0 | 15 |
| AXA Seguros México | 28 | 7 (1/1/5) | 0 | 21 |
| MAPFRE México | 25 | 7 (0/2/5) | 2 | 16 |
| Allianz Brasil | 22 | 7 (1/1/5) | 1 | 14 |
| MAG Seguros | 20 | 9 (0/3/6) | 1 | 10 |
| Azos | 12 | 12 (4/3/5) | 0 | 0 |
| Seguros Banorte | 8 | 4 (0/1/3) | 0 | 4 |
| RGA Mexico | 7 | 6 (3/0/3) | 0 | 1 |
| Swiss Re Mexico | 6 | 3 (0/2/1) | 1 | 2 |
| Brasilseg | 5 | 3 (0/0/3) | 0 | 2 |
| Swiss Re Brasil | 3 | 1 (0/1/0) | 0 | 2 |
| SCOR Mexico | 3 | 3 (0/3/0) | 0 | 0 |
| Hannover Re Brasil | 2 | 2 (0/0/2) | 0 | 0 |
| HSBC Seguros México | 2 | 1 (0/1/0) | 0 | 1 |
| Hannover Re Mexico | 2 | 2 (0/2/0) | 0 | 0 |
| SCOR Brasil | 1 | 1 (0/0/1) | 0 | 0 |

FAIL breakdown: 225 BBVA bank staff or bank-side data roles with no insurance scope; about 40 empty, stale or not-an-employee profiles (freelancers, a restaurant owner, a taqueria owner); 5 location FAILs; the rest by the card's line rules (P&C, auto, health, pensions, claims, sales and distribution) and function rules (IT below the owners, deputies whose chief is in the export).

## How this list was built (coordinator, 2026-11-09)

- **Hlib's sheet** (Google Sheet `1xr160xq…`, tab Data, 452 rows) is a company-wide **seniority** pull, not the title Boolean from `sales-nav-query.md`. For BBVA it took the bank pages (BBVA en México, BBVA Bancomer): 250 rows, about 10 with any insurance scope. Saved as `sales-nav-raw/export-1.csv`.
- **Aliases** added to `companies.csv` and `companies-verified.csv` for the export spellings (`norm_company` turns "México" into `m-xico`, so both spellings are needed): AXA México / AXA Mexico / AXA Seguros, MAPFRE MEXICO / MAPFRE México S.A. / MAPFRE Seguros, the BBVA bank and Seguros pages, Grupo MAG / Mongeral Aegon, Bradesco Seguros / Bradesco Insurance, Allianz Seguros, Reinsurance Group of America (Incorporated), SCOR.
- **Relabels in the raw export before `extract-people`:** bare "Swiss Re" cells became Swiss Re Brasil or Swiss Re Mexico by the person's location (7 rows); two "Grupo MAG" rows located in Mexico with no company page (a Mexican car-dealer group, "Director automotriz") were renamed so they do not join MAG Seguros.
- **Apollo top-up:** of the 70 pre-selected title candidates from 2026-11-06, 12 were already in Hlib's sheet; the other 58 were enriched. The 8 Banorte rows were first skipped by the literal domain check (`segurosbanorte.com.mx` against `segurosbanorte.com`, same employer) and re-enriched. **66 credits in total** (Apollo charged the 8 twice). Logged in `apollo-log.md`.
- **Validator in two parallel batches** (BBVA 247, the rest 231) with eight shared rulings (bank staff without insurance scope FAIL; reinsurer location; Bradesco lines; MAG's former name; stale profiles; multi-line life scope; tech owners P3; empty profiles), merged by the coordinator into `decisions.md`.
- **QC reconciliation (opus QC 14/20, 2026-11-09):** the two batches read "life scope must be visible" and the tech lane differently. 19 rows were brought to one ruling each, marked "(QC reconciliation 2026-11-09)" in `decisions.md`; the earlier list is `people-validated-v1-2026-11-09.csv`:
  - insurer-wide product or actuarial director at a multi-line insurer, no line shown → WEAK (Liliana R., BBVA, as MAPFRE's Director Actuarial);
  - Director Técnico with no line shown → WEAK (Felipe Orozco, BBVA, as Bradesco's Superintendente Técnico; his earlier role was commercial);
  - data operations below the tech owners → FAIL (Javier Camacho, BBVA, as AXA's Subdirector de datos);
  - data, engineering or infrastructure heads outside the card's tech list → WEAK (Guilherme Lissandre, André Oliva Carneiro, Alejandro D., Raul Lobo, Luan Noé, Felipe Octavio Gutierrez);
  - actuarial at the life-and-pensions specialists → P2 (Leonardo Hijino, Icatu, as Ligia Abreu and MAG's actuaries);
  - multi-line group CEO → FAIL (Ney Ferraz Dias, as Allianz's and MAPFRE's C-suite; he joins pool B);
  - coordinators → P3 (Victor Reis, Azos, as Icatu's Jimmy Monte);
  - MAG's COO fallback (Marco Giorgetti) → `referral` lane, not `underwriting`;
  - six company-named profiles → WEAK, held for Vadim by standing decision 4 (coordinator recommends FAIL: a broker, a branch, a music production firm, two outside consultancies, a "Swiss Re Owner").

- **Apollo top-up after the checkpoint:** free located search with other domains (`hsbc.com.mx`, `bbva.com`, BB Seguros) and the keywords seguros/vida for HSBC Seguros, BBVA Seguros, Brasilseg, Bradesco Vida e Previdência, SCOR Mexico and Banorte; 216 rows, 12 picked by title, enriched (12 credits; one was already in the sheet). Fresh validator, same reconciled rulings: PASS Jose Antonio Palacio Junco (HSBC, Director de Seguros Protection, P2 proposition), Hector Juarez Lara (BBVA, SD Técnico Global Vida, P2 underwriting), Daniel Oliva Becerra (BBVA Seguros y Pensiones CTO, P3), Bernardo Castello (CEO Bradesco Vida e Previdência, P3 referral), Francisco Majos and Yolanda Gutierrez (SCOR Mexico L&H, P2 reinsurance); WEAK taken Xabier Beroiz Ripa (BBVA), Estevao Scripilliti and Alessandro Malavazi (BVP); FAIL Juan Pablo Gonzalez Castro (HSBC insurance sales), Moises Arenas (collision).

## Proposed to SEND (122, after the checkpoint)

| Group | Person | Title | P | Angle | From | Source |
|---|---|---|---|---|---|---|
| AXA Seguros México | Beltrando Pini | Executive Vice President Health and Life | 1 | proposition | PASS | Apollo |
| AXA Seguros México | Tonantzin Tapia Garduno | Actuary Life Insurance Reserves Manager | 2 | proposition | PASS | Apollo |
| AXA Seguros México | Efrain Baldenebro Ortiz | CISO | 3 | technical-integration | PASS | SN |
| AXA Seguros México | Estelle Hascoët | Chief Customer Officer, Member of the Executive Committee | 3 | referral | pool B | SN |
| AXA Seguros México | Jose de Jesus Luna Cabrera | Director de Tecnología, Datos e IA | 3 | technical-integration | PASS | SN |
| AXA Seguros México | Maritere Torcida Rodríguez | Head of Customer Innovation | 3 | referral | PASS | SN |
| AXA Seguros México | Oscar Ruiz César | Chief Transformation Officer | 3 | referral | PASS | SN |
| Allianz Brasil | Fábio Ohara Morita | Vice-presidente executivo | 1 | underwriting | PASS | SN |
| Allianz Brasil | Alexandra Rossini Ruz | Superintendente de Resseguro, Produto, Governança de Subscrição e Programas Glob | 2 | underwriting | PASS | SN |
| Allianz Brasil | Eduard Folch Rue | Chief Executive Officer | 3 | referral | pool B | SN |
| Allianz Brasil | Guilherme Lissandre | Chief Data and Analytics Officer - Executive Director of Data Office | 3 | technical-integration | WEAK taken | SN |
| Allianz Brasil | Javier Bernat | CEO Latin America Region - Brazil, Mexico, Argentina and Colombia | 3 | referral | pool B | SN |
| Allianz Brasil | Josemilson Silva | CIO | 3 | technical-integration | PASS | SN |
| Allianz Brasil | Maria Fernanda Piccolo Rossi | Diretora de Transformação | 3 | referral | PASS | SN |
| Azos | Bernardo Correa Ribeiro | Co-founder | 1 | proposition | PASS | SN |
| Azos | Heloisa Falcão, MIBA | Diretora de Produtos de Seguros na Azos | 1 | proposition | PASS | SN |
| Azos | Rafael Cló | Co-Founder & CEO | 1 | proposition | PASS | SN |
| Azos | Renato Farias | Co-Founder | 1 | proposition | PASS | SN |
| Azos | Ana Bobis | Head Atuarial | 2 | proposition | PASS | SN |
| Azos | Julia Wajs | Group Product Manager | 2 | proposition | PASS | Apollo |
| Azos | Rodrigo Teixeira | Head of Product | 2 | proposition | PASS | SN |
| Azos | Julia Martins | Product Manager | 3 | proposition | PASS | Apollo |
| Azos | Luan Noé | Head of Engineering & Infrastructure | 3 | technical-integration | WEAK taken | SN |
| Azos | Raul Lobo | Head of Data | 3 | technical-integration | WEAK taken | SN |
| Azos | Thais Nakahira | Product Manager | 3 | proposition | PASS | Apollo |
| Azos | Victor Reis | Coordenador de Subscrição | 3 | underwriting | PASS | Apollo |
| BBVA Seguros México | Felipe Orozco | Director Técnico | 2 | underwriting | WEAK taken | SN |
| BBVA Seguros México | Hector Juarez Lara | SD Técnico Global Vida | 2 | underwriting | PASS | Apollo |
| BBVA Seguros México | Liliana R. | Directora de Producto de Seguros y Función Actuarial | 2 | proposition | WEAK taken | SN |
| BBVA Seguros México | Sandra Nacul Méndez | Subdirector de Productos de Vida | 2 | proposition | PASS | SN |
| BBVA Seguros México | Daniel Oliva Becerra | Director de Tecnología, Seguros y Pensiones | 3 | technical-integration | PASS | Apollo |
| BBVA Seguros México | Daniel Ordaz Palacios | Head of Data & CX | 3 | referral | pool F | SN |
| BBVA Seguros México | Fernando Campos García | Head of Data Portfolio Management & AI Factory | 3 | referral | pool F | SN |
| BBVA Seguros México | Hunibert Tuch | Director Proyectos e Innovación | 3 | referral | pool F | SN |
| BBVA Seguros México | Isaac Flores Lira | Director Business Process Architecture & Artificial Intelligence Technologies | 3 | referral | pool F | SN |
| BBVA Seguros México | LUIS HIDALGO | CIO BBVA SEGUROS | 3 | technical-integration | WEAK taken | SN |
| BBVA Seguros México | Nacho García Cantón | Head AI Solutions | 3 | referral | pool F | SN |
| BBVA Seguros México | Pedro Lopez Comision de Honor | Director Técnico | 3 | underwriting | WEAK taken | SN |
| BBVA Seguros México | Xabier Beroiz Ripa | Director Estrategia y Portafolio de Seguros | 3 | proposition | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Abelardo Filho | Superintende Tecnico | 2 | underwriting | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Gabriel Soares | Gerente de Subscrição de Risco | 2 | underwriting | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Marcio Gliosci | Gerente de Subscrição | 2 | underwriting | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Pedro Figueiredo | Gerente Atuarial de Pricing e Subscrição | 2 | proposition | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Thiago Sousa | Superintendente de Subscrição | 2 | underwriting | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Alessandro Malavazi | Superintendente Sênior na Bradesco Vida e Previdência | 3 | proposition | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Almir Ximenes | superintendente executivo | 3 | referral | pool C | SN |
| Bradesco Vida e Previdência | Bernardo Castello | Diretor-Presidente na Bradesco Vida e Previdência | 3 | referral | PASS | Apollo |
| Bradesco Vida e Previdência | Caio Mastronell | Diretor Executivo | 3 | referral | WEAK taken | SN |
| Bradesco Vida e Previdência | Carlos Rogoginsky Junior | Superintendente Executivo | 3 | referral | pool C | SN |
| Bradesco Vida e Previdência | Denis Nesi | CISO / Information Security, Cybersecurity, Privacy & Digital Fraud Prevention | 3 | technical-integration | PASS | Apollo |
| Bradesco Vida e Previdência | Dirlei Jordão | Superintendente Executivo | 3 | referral | WEAK taken | SN |
| Bradesco Vida e Previdência | Edilson Reis | Chief Information Officer, Executive Director | 3 | technical-integration | PASS | SN |
| Bradesco Vida e Previdência | Estevao Scripilliti | Diretor na Bradesco Vida e Previdência | 3 | referral | WEAK taken | Apollo |
| Bradesco Vida e Previdência | Felipe Szuster | Head Inovação | 3 | referral | PASS | SN |
| Bradesco Vida e Previdência | Fernando Mendonca | Gerente Sr. Inovação e Transformação Ágil | 3 | referral | PASS | Apollo |
| Bradesco Vida e Previdência | Guilherme Haraguchi | Superintendente Executivo | 3 | referral | WEAK taken | SN |
| Bradesco Vida e Previdência | Jose Loureiro | Diretor de Inovação & Digital & Dados | 3 | referral | PASS | SN |
| Bradesco Vida e Previdência | Marcos Scherer | Superintendente Executivo | 3 | referral | pool C | SN |
| Bradesco Vida e Previdência | Ney Ferraz Dias | Diretor-Presidente da Bradesco Auto/RE | 3 | referral | pool B | SN |
| Bradesco Vida e Previdência | Thais Polegato | Executive Director | 3 | referral | pool C | SN |
| Brasilseg | Gustavo Oliveira (Guga) | Superintendente Geral | 3 | referral | WEAK taken | SN |
| Brasilseg | Júlio Cezar Oliveira Oliveira | Presidente | 3 | referral | pool B | Apollo |
| Brasilseg | Thiago Affonso Borsari | Diretor de TI, Portfólio e IA | 3 | technical-integration | PASS | SN |
| HSBC Seguros México | Jose Antonio Palacio Junco | Director de Seguros Protection | 2 | proposition | PASS | Apollo |
| Hannover Re Brasil | João Caproni | Diretor Presidente, Representante, GM | 3 | referral | pool A | SN |
| Hannover Re Brasil | ivan passos | CEO Brazil | 3 | referral | pool A | SN |
| Hannover Re Mexico | Bryan Urbano | L&H Actuarial Manager | 2 | reinsurance | PASS | Apollo |
| Hannover Re Mexico | Julio Ponce De Leon | Underwriting Manager | 2 | reinsurance | WEAK taken | Apollo |
| Icatu Seguros | Ingrid Pereira | Product Manager | 2 | proposition | PASS | Apollo |
| Icatu Seguros | Leonardo Hijino | Gerente Atuarial | 2 | proposition | PASS | Apollo |
| Icatu Seguros | Ligia Abreu | Superintendente Executiva Atuarial | 2 | proposition | PASS | Apollo |
| Icatu Seguros | Luciana Bastos | Diretora de Desenvolvimento de Produtos - Vida | 2 | proposition | PASS | SN |
| Icatu Seguros | Marcela Gueiros | Gerente de Produtos Senior / GPM / Produtos Vida | 2 | proposition | PASS | Apollo |
| Icatu Seguros | Pier Ietto | Gerente de Subscrição/Precificação Vida / Icatu Seguros | 2 | underwriting | PASS | Apollo |
| Icatu Seguros | Priscilla Teixeira | Gerente Atuarial de Vida e Previdência | 2 | proposition | PASS | Apollo |
| Icatu Seguros | Rafael Saile | Gerente de Subscrição e Aceitação Vida | 2 | underwriting | PASS | Apollo |
| Icatu Seguros | André Oliva Carneiro | Executive Director of Data & AI | 3 | technical-integration | WEAK taken | SN |
| Icatu Seguros | Antonio Carlos Almeida Braga | Diretor de Produtos | 3 | proposition | PASS | SN |
| Icatu Seguros | Beatriz Helena | Coordenador de Produtos Vida | 3 | proposition | PASS | Apollo |
| Icatu Seguros | Bernardo Carneiro | CTO | 3 | technical-integration | PASS | SN |
| Icatu Seguros | César Saut | Vice-presidente corporativo | 3 | referral | WEAK taken | SN |
| Icatu Seguros | Eduardo Correa | Executive Director | 3 | referral | WEAK taken | SN |
| Icatu Seguros | Humberto Sardenberg | Head of Digital Experience / Digital Transformation / UX / Product Manager | 3 | proposition | PASS | Apollo |
| Icatu Seguros | Iago Duarte Simões | Head de Parcerias MG | 3 | referral | pool D | SN |
| Icatu Seguros | Jimmy Monte | Underwriting Coordinator | 3 | underwriting | PASS | Apollo |
| Icatu Seguros | Rachel Ferreira Bonel | Diretora de Controles Internos e Dados | 3 | technical-integration | PASS | SN |
| Icatu Seguros | Rodrigo Pádova | Head de Produtos Digitais, PM | 3 | proposition | PASS | SN |
| Icatu Seguros | Sergio Egidio | Diretor Executivo | 3 | referral | pool C | SN |
| MAG Seguros | Carlos Figueiredo | Gerente Atuarial | 2 | proposition | PASS | Apollo |
| MAG Seguros | Rafael Franco | Diretor Atuarial/ Chief Actuary | 2 | proposition | PASS | Apollo |
| MAG Seguros | Rodrigo Cunha | Gerente de Produtos e Inteligência de Mercado | 2 | proposition | PASS | Apollo |
| MAG Seguros | Dayana Mello | Coordenadora de Produtos Vida | 3 | proposition | PASS | Apollo |
| MAG Seguros | Eugenio Guerim Jr | Diretor de Parcerias Estratégicas | 3 | referral | pool D | SN |
| MAG Seguros | Larissa Althoff | Diretora de Parcerias Estratégicas | 3 | referral | pool D | SN |
| MAG Seguros | Luís Henrique Fontes de Oliveira | Diretor de tecnologia | 3 | technical-integration | PASS | SN |
| MAG Seguros | Marco Giorgetti | Diretor Executivo de Operações | 3 | referral | PASS | SN |
| MAG Seguros | Paula Cristiane Hernandes da Silva | Superintendente de Arquitetura e Transformação Digital | 3 | technical-integration | PASS | SN |
| MAPFRE México | Juan Ortiz Perez | Director Actuarial | 2 | proposition | WEAK taken | Apollo |
| MAPFRE México | Mario Gonzalez Mendez | Subdirector Suscripción Vida | 2 | underwriting | PASS | Apollo |
| MAPFRE México | Alejandro D. | Transformation Management Office / Data & AI Head | 3 | technical-integration | WEAK taken | SN |
| MAPFRE México | Felipe Octavio Gutierrez Manjarrez | Director de Infraestructura TI | 3 | technical-integration | WEAK taken | SN |
| MAPFRE México | Manuel Matamoros Arreguin | Director Planeación Estratégica | 3 | referral | pool B | SN |
| MAPFRE México | Miguel Angel C. | Chief Operating Officer | 3 | referral | pool B | SN |
| MAPFRE México | Ricardo Endo | Head of Transformation | 3 | referral | PASS | SN |
| RGA Mexico | Carolyn Pritchard | Head of Underwriting, Latin America | 1 | reinsurance | PASS | Apollo |
| RGA Mexico | Jesus Spinola Grandio | CEO Latin America | 1 | reinsurance | PASS | SN |
| RGA Mexico | Keiko Imuro | Chief Underwriter | 1 | reinsurance | WEAK taken | Apollo |
| RGA Mexico | Cesar Castillo | Strategy & PMO Leader, Latin America Chief of Staff | 3 | reinsurance | PASS | SN |
| RGA Mexico | Dominique Hierro | General Manager | 3 | reinsurance | WEAK taken | SN |
| RGA Mexico | Lorena Cruz Vega | Business Development Director, Health | 3 | reinsurance | PASS | SN |
| SCOR Brasil | Rafael Zimmer | CUO - Head of Program Business Latam | 3 | referral | pool A | SN |
| SCOR Mexico | Claudia Rodríguez  Gomez | Director | 2 | reinsurance | WEAK taken | SN |
| SCOR Mexico | Francisco Majos | Head of L&H Business Development Latin America | 2 | reinsurance | PASS | Apollo |
| SCOR Mexico | Yolanda Gutierrez | Senior Client Manager - Mexico, Central America & Caribbean L&H | 2 | reinsurance | PASS | Apollo |
| Seguros Banorte | Susana Granados | Gerente de Suscripcion de Seguros de Personas | 2 | underwriting | WEAK taken | Apollo |
| Seguros Banorte | Andres Martinez Sarmiento | Coordinador de Protección de Datos Personales | 3 | technical-integration | PASS | Apollo |
| Seguros Banorte | Eduardo Gutierrez Rojo | Subdirector Digital Attacker / Innovación y Producto | 3 | referral | PASS | Apollo |
| Seguros Banorte | Luis Pinon | Regional Underwriting Manager | 3 | underwriting | WEAK taken | Apollo |
| Swiss Re Brasil | Juliana Alves | Market Head for South Cone (P&C and L&H) and President for Swiss Re Brazil | 2 | reinsurance | PASS | SN |
| Swiss Re Mexico | Antonio F | Assistant Medical Director, Latam | 2 | medical | PASS | Apollo |
| Swiss Re Mexico | Gabriela Martinez Fentanez | Senior Client Manager Life and Health | 2 | reinsurance | PASS | Apollo |
| Swiss Re Mexico | Paulina Noyola | Head Business Operations Latin America & Caribbean | 3 | reinsurance | PASS | SN |

## WEAK — left after the checkpoint (6)

The six company-named profiles, held by standing decision 4 and not taken (the option Vadim chose excluded them). Before the checkpoint 34 WEAK; the 28 others are in SEND with pool `W`. The `empty-profile` note: 6 of the 58 first Apollo rows carry it (Susana Granados, Keiko Imuro, Julio Ponce De Leon, Marcio Gliosci, Mario Gonzalez Mendez, Ricardo Sosa); for them Apollo's 2026 title is the second source. Taken without a second source and re-checked on the web in the Account facts round: Pedro Lopez "Comision de Honor" (BBVA), César Saut (Icatu), Ivan Passos (Hannover Re Brasil).

| Person | Title | Group | Why |
|---|---|---|---|
| Swiss Re | Owner | Swiss Re Mexico | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |
| Filial Brasilia | Chefe de filial | Allianz Brasil | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |
| BBF ASOCIADOS | CEO de BBF y Asociados | MAPFRE México | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |
| Mais Proteção Consultoria e Corretora de Seguros | CEO | MAG Seguros | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |
| All Music Produções | Diretor musical | Bradesco Vida e Previdência | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |
| INDE Consultores de Riesgo | Consejero delegado | MAPFRE México | Company-named profile, held for Vadim by standing decision 4; not a person at the insurer, coordinator recommends FAIL (QC reconciliation 2026-11-09) |

## Кого оставили за бортом: пулы

**Taken at the checkpoint: A, B, C, D, F** (people in SEND with that pool letter). E, G, H stay out. Full lists in `skipped-detail.md` (367 not sent, 198 of them senior).

| Pool | People | Who (3-5 names) | Proposed angle | What would change to take them |
|---|---|---|---|---|
| A. Reinsurer Brazil country rows | 3 | João Caproni (GM, Hannover Re Brazil), Ivan Passos (CEO Brazil, Hannover Re, empty profile), Rafael Zimmer (SCOR, CUO Program Business LatAm, likely P&C) | reinsurance | New rows Hannover Re Brasil and SCOR Brasil; Open question 3 says only if an L&H team exists there |
| B. C-suite at multi-line insurers | 6 | Eduard Folch (CEO Allianz Brasil), Javier Bernat (Allianz CEO LatAm, former chief actuary), Ney Ferraz Dias (CEO Bradesco Seguros group), Miguel Angel C. (COO MAPFRE México), Estelle Hascoët (CCO AXA México), Manuel Matamoros (strategy director, MAPFRE México) | referral | Tiers keep a multi-line CEO/COO out; referral lane by your word |
| C. Group executives whose visible line is excluded | 5 | Almir Ximenes (earlier Auto/RE), Carlos Rogoginsky (earlier OdontoPrev), Thais Polegato (earlier investment banking) at Bradesco; Marcos Scherer, Sergio Egidio (Icatu, commercial histories) | referral | Referral lane by your word |
| D. Partnerships heads | 3 | Eugenio Guerim, Larissa Althoff (MAG, Parcerias Estratégicas), Iago Duarte (Icatu) | referral | Card takes partnerships heads only with digital scope; learnings PPL-3: partnerships replied 6/83 |
| E. Actuarial without visible life scope | 1 | Francisco Cerdeira (Gerente Actuarial, Banorte, multi-line) | proposition | Accept company-wide actuarial managers at multi-line insurers |
| F. BBVA bank-wide AI, data and innovation heads | 5+ | Daniel Ordaz Palacios (Head of Data & CX), Isaac Flores Lira (Head of AI Banking Platform), Nacho García Cantón (Head AI Solutions), Fernando Campos García (Head of Data Portfolio & AI Factory), Hunibert Tuch (Director Proyectos e Innovación) | referral | Bank staff as referral into BBVA Seguros (ruling R1 FAILs them now) |
| G. BBVA privacy and security | 2 | Jesus Andres Gomez Guerra (Director Protección de Datos Personales, empty profile), Victor Manuel C. (CISO) | technical-integration | Only if their scope covers Seguros |
| H. BBVA Seguros roles outside life | 2 | Jorge David Moncada Córdova (Director Seguros Contact Center), Hector Hugo Rodriguez Venegas (Subdirector de producción, Seguros Bancomer) | referral | Referral into the life team |

## Top concerns

- **The sheet was a seniority pull, not the title pull from the brief;** the buyer functions stay thin after the top-up: 16 `underwriting`, 14 `reinsurance` and 1 `medical` of 122, against 40 `referral`. P1 sits at Azos (4), RGA (3 with Keiko Imuro), AXA and Allianz Brasil (1 each); no Brazilian incumbent has a P1.
- **Accounts:** HSBC Seguros México now has one person (Director de Seguros Protection). BBVA Seguros has a life products head and a Subdirector Técnico Global Vida, both P2. Bradesco Vida e Previdência has its CEO (P3 referral) and the Rio-based underwriting rows taken from WEAK, whose line (life or Auto/RE) is still not confirmed. Brasilseg: IT director, the President (pool B) and a general superintendent. SCOR Mexico: three, two of them L&H.
- **Pool A has no L&H team behind it** (research 2026-11-05): Hannover Re Brasil and SCOR Brasil people go as `referral`, and Rafael Zimmer's Program Business is likely P&C.
- **Technology:** 19 of 122 are `technical-integration` (11 validator PASS, 7 data/engineering heads and BBVA's CIO Seguros taken from WEAK, 1 from the top-up). Learnings PPL-3: engineering replied 1/90.
- **Export noise:** about 40 empty, stale or fake profiles; 4 duplicate pairs at BBVA (both copies FAIL); two Jose Loureiro profiles (the Bradesco innovation director in SEND, an empty Icatu "governance director" FAIL, probably his old profile); two MAPFRE México COOs (one in pool B).

## Next (step 5 prep)

1. Fresh `hypothesis-generator` round writes `### Account facts` (one bullet per group with SEND, 18 groups incl. the two new Brazil rows and HSBC) and re-checks on the web every P1, the 28 WEAK taken (current role, life line) and the three no-second-source profiles above.
2. `card --for messages` → `profiles` → `message-sequencer` batches → `check-messages` → opus QC → Vadim.
3. The referral share is high (40 of 122): the card's referral themes per company need care against the M1 skeleton (learnings 2026-10-06).
