---
product: fitxpress
profile: olena
campaign: 2026-10-29-eu-insurance-underwriting
created: 2026-11-02
stage: validate
status: approved
---

# ICP Validation Summary — 2026-10-29-eu-insurance-underwriting

Sources: Hlib's Sales Navigator sheet (`1-h7TxJuwFPO0-hEBvrVxZQdQq3y1qtd9l3eNRAmf2sc`, 685 rows → `sales-nav-raw/export-1.csv`) and an Apollo title top-up (`apollo-log.md`). Validated in four parallel `icp-validator` batches (Swiss Re 178, Munich Re 166, SCOR + Hannover Re + Gen Re 145, insurers + platforms 245) under one shared rulings sheet; merged by the coordinator into `decisions.md`. Coordinator changes after the merge: Ross Mayne relabelled from bare "Munich Re (Group)" to Munich Re Automation Solutions (CEO since 2008 per the MRAS leadership page) and WEAK → PASS P1 `partnership`; Jason Stone (Swiss Re, BD L&H "EMEA UK&I") PASS → WEAK, the coordinator's own call because UK is katerina's market (Vadim decides).

**QC fix round 2026-11-02** (opus QC 15/20, `workspace/_quality/outbound/2026-11-02-icp-validator-eu-insurance-underwriting.md`), 22 rows edited in `decisions.md` by the coordinator, marked "(QC fix 2026-11-02)": one P1 rule (Binswanger → WEAK, line not in the title; reinsurer CMOs Schoonbee and Senn → P2 like Hannover Re's Teichmann; Margot Wilson → P2 like the other L&H business heads); one CIO rule (a single-line life insurer's company IT head counts as its CTO: Fattah LV 1871, Clinton AXA Life Europe, Eivers New Ireland → P3 `technical-integration`; CosmosDirekt is multi-line, Roehrs stays FAIL); data architecture out on both sides (Braun FAIL like Rodgers); medisch adviseurs with no line shown → WEAK (8 at a.s.r., Steenks at Achmea; Middelbos, Inkomen, and Angelique R, registered insurance physician, stay P2); one DPO per account (Forrester, Ferguson, Juillard → WEAK). Before the round: PASS 138 · WEAK 44 · FAIL 552; after it: PASS 127 · WEAK 57 · FAIL 550.

**Checkpoint 2026-11-02 (Vadim, all recommended options; `hypothesis.md` → `Vadim's decisions 2026-11-02`):** five WEAK taken (Guthoerl, Langenstrass, Woltmann, Rozemuller, Betz); country rows `Swiss Re Germany`, `SCOR Germany`, `SCOR Ireland`, `Hannover Re Ireland` opened (29 people relabelled by location, 6 of them new; judged by the same two batches: PASS 8, WEAK 6, FAIL 15); five group architects/CTO and four Irish Life referral trimmed; Plisson and Schilling P1 → P2 by the same P1 rule; no title re-pull by Hlib. **Final: PASS 131 · WEAK 58 · FAIL 551.**

## Stats

740 people checked (Sales Navigator 657 after aliases and relabels, Apollo title top-up 83 new of 87 enriched, 96 credits) · **PASS 131** (P1 21 · P2 57 · P3 53) · **WEAK 58** · **FAIL 551** · excluded by registry 0 (bare `Aviva` ×18 waived, decision 3) · person overlap with katerina's registry and UK `people-approved.csv`: 0.

PASS by angle: underwriting 31 · reinsurance 28 · technical-integration 21 · proposition 19 · referral 19 · medical 8 · partnership 5

| Group | People in list | PASS | vs cap 50 |
|---|---|---|---|
| Swiss Re Switzerland | 166 | 15 | ok |
| Munich Re Germany | 161 | 15 | ok |
| Irish Life Assurance | 51 | 10 | ok |
| SCOR France | 75 | 8 | ok |
| Aviva Ireland | 23 | 7 | ok |
| Gen Re Germany | 16 | 7 | ok |
| LV 1871 | 8 | 6 | ok |
| Hannover Re Germany | 43 | 5 | ok |
| Volkswohl Bund | 7 | 5 | ok |
| Zurich Life Ireland | 6 | 5 | ok |
| New Ireland Assurance | 20 | 4 | ok |
| a.s.r. | 14 | 4 | ok |
| Allianz Lebensversicherungs-AG | 8 | 4 | ok |
| Nationale-Nederlanden | 31 | 3 | ok |
| Achmea | 19 | 3 | ok |
| SCOR Ireland | 7 | 3 | ok |
| Munich Re Automation Solutions | 5 | 3 | ok |
| Morgen & Morgen | 5 | 3 | ok |
| AXA Life Europe | 4 | 3 | ok |
| Hannoversche Lebensversicherung | 4 | 3 | ok |
| Alte Leipziger Lebensversicherung | 13 | 2 | ok |
| Swiss Re Germany | 12 | 2 | ok |
| Swiss Life Deutschland | 9 | 2 | ok |
| SCOR Germany | 8 | 2 | ok |
| Royal London Ireland | 5 | 2 | ok |
| CosmosDirekt | 5 | 2 | ok |
| Hannover Re Ireland | 2 | 1 | ok |
| vers.diagnose | 1 | 1 | ok |
| Acorn Life | 1 | 1 | ok |
| Die Bayerische | 10 | 0 | ok |
| Scildon | 1 | 0 | ok |

No people at all (Sales Navigator and Apollo): Allianz Nederland Leven, Dialog, Europa Lebensversicherung, HDI Lebensversicherung, RGA Ireland. People but no PASS: Scildon, Die Bayerische.

## SEND (approved by Vadim 2026-11-02)

| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| AXA Life Europe | John McCormack | Chief Operating Officer | 3 | referral |
| AXA Life Europe | Eoin Lynam | Chief Executive Officer | 3 | referral |
| AXA Life Europe | Caroline Clinton | Head of Information Technology | 3 | technical-integration |
| Achmea | Claudia Stewart-Duijndam | Directeur Transformation Management Office | 3 | referral |
| Achmea | Emilie Gale | Head of Transformation | 3 | referral |
| Achmea | Tom Verhoeven | Head of Intelligence Lab | 3 | referral |
| Acorn Life | Elaine Glynn | Underwriting Manager | 3 | underwriting |
| Allianz Lebensversicherungs-AG | Thomas Lay | Leiter Produktmanagement und Underwriting | 1 | underwriting |
| Allianz Lebensversicherungs-AG | Marc Schanbacher | Chief Data Officer | 2 | proposition |
| Allianz Lebensversicherungs-AG | Annette Seitz | Head of International Development Life | 2 | proposition |
| Allianz Lebensversicherungs-AG | Marcel Beißer | Referatsleiter Produktentwicklung und Aktuariat | 2 | proposition |
| Alte Leipziger Lebensversicherung | Holger Krebs | Bereichsleiter Produktgestaltung Leben | 2 | proposition |
| Alte Leipziger Lebensversicherung | Karsten Vogel | Zentralbereichsleiter Digitalisierung und Innovationsmanagement, Prokurist | 3 | referral |
| Aviva Ireland | Jean Larkin | Head of Underwriting | 1 | underwriting |
| Aviva Ireland | Karen O'Flaherty | Individual Protection Proposition Lead | 2 | proposition |
| Aviva Ireland | Mark Cree | Underwriting Manager Philosophy & Innovation | 2 | underwriting |
| Aviva Ireland | Brian O'Malley | Head of Propositions | 3 | proposition |
| Aviva Ireland | Caroline Doory | Head of Customer Experience Transformation | 3 | referral |
| Aviva Ireland | Claire Donohoe, FCA | Head of Transformation | 3 | referral |
| Aviva Ireland | Michelle Lyons | Data Protection Officer | 3 | technical-integration |
| CosmosDirekt | Erik Guthoerl | Head of Underwriting Leben | 2 | underwriting |
| CosmosDirekt | Nicole Heidemeyer | Chief Operating Officer | 3 | referral |
| Gen Re Germany | Andres Webersinke | Global Chief Underwriting Officer - Life/Health | 1 | underwriting |
| Gen Re Germany | Carsten Giese | Stellv. Direktor Leben/Kranken Deutschland | 2 | reinsurance |
| Gen Re Germany | Tim Eppert | Head of Life/Health Products & Analytics | 2 | reinsurance |
| Gen Re Germany | Ulrich Pasdika | Head of Life/Health Europe / Latin America / Middle East / North Africa | 2 | reinsurance |
| Gen Re Germany | Annika Schilling | Head of Underwriting Research | 2 | underwriting |
| Gen Re Germany | Simon Fallais | Medical Research Specialist / Underwriting Research | 3 | underwriting |
| Gen Re Germany | Carina Betz | Underwriting Manager Life/Health | 3 | underwriting |
| Hannover Re Germany | Dr. Gabriele Teichmann | General Manager | 2 | medical |
| Hannover Re Germany | Margot Wilson | Managing Director, Life & Health Global Services | 2 | reinsurance |
| Hannover Re Germany | Henning Von Kielpinski | Head of IT Underwriting Solutions Life & Health | 2 | technical-integration |
| Hannover Re Germany | Susanne Buchholz | Chief Medical Underwriter | 2 | underwriting |
| Hannover Re Germany | Rolf Kulemann | Team Manager L&H Underwriting Solutions | 2 | underwriting |
| Hannover Re Ireland | Steven Hardy | Director, Head of L&H Ireland & Canada | 1 | reinsurance |
| Hannoversche Lebensversicherung | Florian Kreutzkam | Abteilungsleiter Leben Risikoprüfung und Leistung | 1 | underwriting |
| Hannoversche Lebensversicherung | Christian Langenstrass | Leiter Underwriting | 2 | underwriting |
| Hannoversche Lebensversicherung | Mathias Schniebs | Leiter Services und Schnittstellen | 3 | technical-integration |
| Irish Life Assurance | Lauren McCormack | Head of Health & Protection Proposition | 1 | proposition |
| Irish Life Assurance | Siobhan Buckley | Head of Product and Proposition - Health and Protection Lines | 2 | proposition |
| Irish Life Assurance | Laura Mongan | Head of Products & Propositions | 3 | proposition |
| Irish Life Assurance | Patricia Smith | Head of Proposition Development | 3 | proposition |
| Irish Life Assurance | Christopher Curran | Head of Research and Innovation Partnerships | 3 | referral |
| Irish Life Assurance | Kelvin Gillen | Director of Innovation (ExO) | 3 | referral |
| Irish Life Assurance | Shay Browne | Director of Innovation & Change, Retail Division | 3 | referral |
| Irish Life Assurance | Alan Q. | Head of Digital Innovation | 3 | referral |
| Irish Life Assurance | Richard L. | Head of Strategy and Architecture | 3 | technical-integration |
| Irish Life Assurance | Brendan Lambe | Head of Architecture and Cloud | 3 | technical-integration |
| LV 1871 | Sandra John | Leiterin Risikoprüfung/Leistungsprüfung | 1 | underwriting |
| LV 1871 | Ralf Woltmann | Gesellschaftsarzt | 2 | medical |
| LV 1871 | Jakob Limbach | Produktmanager Biometrie | 2 | proposition |
| LV 1871 | David Ibl | Head of Process Optimization & Digitalization | 3 | referral |
| LV 1871 | Dr. Georg Bechler | Head of Digital Platforms & Services | 3 | referral |
| LV 1871 | Dr. Amir Fattah | CIO | 3 | technical-integration |
| Morgen & Morgen | Klaus Strumberger | Geschäftsführer | 1 | partnership |
| Morgen & Morgen | Benjamin Brummer | Senior Mathematiker, Stellvertr. Bereichsleiter Mathematik | 3 | partnership |
| Morgen & Morgen | Gabriela Heyne | Bereichsleiterin IT | 3 | technical-integration |
| Munich Re Automation Solutions | Ross Mayne | CEO | 1 | partnership |
| Munich Re Automation Solutions | George Fox | Product Director | 2 | partnership |
| Munich Re Automation Solutions | Darren Dempsey | Chief Technology Officer | 3 | technical-integration |
| Munich Re Germany | Luis Jimenez | Head of Corporate Underwriting and Claims Life&Health Section | 1 | underwriting |
| Munich Re Germany | Thomas Geissler | Chief Underwriter Germany Life/Health | 1 | underwriting |
| Munich Re Germany | Alban Senn | Chief Medical Officer | 2 | medical |
| Munich Re Germany | Steven Wiseman | Senior Medical Consultant/Senior Medical Officer | 2 | medical |
| Munich Re Germany | Christoph Henschel | Head of Biometric Analysis and Insights | 2 | reinsurance |
| Munich Re Germany | Keyvan Izadi | Head of Digital Services, Life & Health | 2 | reinsurance |
| Munich Re Germany | Roland Schneider | Head of Life&Health Data and Digital - Group Technology | 2 | reinsurance |
| Munich Re Germany | Volker Homola | Head of Business Development Life/Health for Continental Europe | 2 | reinsurance |
| Munich Re Germany | Fabian Schmitt | Chief Executive Officer, Life & Health, Continental Europe (excl. Italy, Spain,  | 2 | reinsurance |
| Munich Re Germany | Cosima Escher | Head of Client Management Life & Health | 2 | reinsurance |
| Munich Re Germany | Kshiti A. | REGIONAL HEAD OF IT SOLUTION DELIVERY LIFE&HEALTH, EMEA) | 3 | technical-integration |
| Munich Re Germany | Christian Helmes | Head of Subsection Enterprise Architecture - Reinsurance & Corporate Functions | 3 | technical-integration |
| Munich Re Germany | Wolfgang Mörlein | Chief Data Protection Officer | 3 | technical-integration |
| Munich Re Germany | Michael Ewers | CTO | 3 | technical-integration |
| Munich Re Germany | Mirjam Jonker-Heidolph | Life Underwriting Manager | 3 | underwriting |
| Nationale-Nederlanden | Rens Engelen | Head of Transformation | 3 | referral |
| Nationale-Nederlanden | Remco De Mol | Head of Data & AI Hub | 3 | referral |
| Nationale-Nederlanden | Koos van der Veen | Chief Information Officer Life&Pension Nationale Nederlanden | 3 | technical-integration |
| New Ireland Assurance | Noel Finnegan | Chief Underwriter | 1 | underwriting |
| New Ireland Assurance | Paul Courtney | Head of Product | 3 | proposition |
| New Ireland Assurance | Denis Eivers | Head of Company Wide Technology | 3 | technical-integration |
| New Ireland Assurance | Ronan Scully | Head of Operational Risk and Data Protection Officer | 3 | technical-integration |
| Royal London Ireland | Matthew Tinney | Head of Underwriting | 1 | underwriting |
| Royal London Ireland | Joe Charles | Proposition Director | 2 | proposition |
| SCOR France | Elsa Renouf-Helfen | L&H Chief Pricing & Underwriting Officer | 1 | underwriting |
| SCOR France | Antoine Moll | Head of Medical Underwriting Modelling | 1 | underwriting |
| SCOR France | Lucie Aubry | Head of L&H Advanced Analytics and Artificial Intelligence | 2 | reinsurance |
| SCOR France | Roberto Castellini | Head of Data Science - Life&Health | 2 | reinsurance |
| SCOR France | Stephanie Maret | Head of Life & Health UW Risk Management | 2 | underwriting |
| SCOR France | Manuel Plisson | Chief Underwriting Transformation Officer | 2 | underwriting |
| SCOR France | Marvin Dewkurun | Group Data Protection Officer | 3 | technical-integration |
| SCOR France | Adrien Givaudan | Senior Life Underwriting Risk Manager | 3 | underwriting |
| SCOR Germany | Thomas Trompetter | Head Of Client Services Central Europe, Nordics, Middle East | 2 | reinsurance |
| SCOR Germany | Fouzia Boussetta | Global Head of In-force Management for non-US markets | 3 | reinsurance |
| SCOR Ireland | Redmond Murphy | Deputy CEO, SCOR Life & Health | 2 | reinsurance |
| SCOR Ireland | Jenny McDonnell | Head of Business Acceptance | 2 | underwriting |
| SCOR Ireland | Jennifer Coleman | Chief Executive Officer - SCOR Ireland | 3 | reinsurance |
| Swiss Life Deutschland | Diana Glenewinkel | Abteilungsleiterin Service, Projects & Innovation | 3 | referral |
| Swiss Life Deutschland | Lars Kietzer | Head of Core Insurance Platform | 3 | technical-integration |
| Swiss Re Germany | Markus Unterkofler | Head Life & Health Germany, ACEE & Nordics | 2 | reinsurance |
| Swiss Re Germany | Sebastian Strasser | Head Business Advisory L&H, Managing Director | 2 | reinsurance |
| Swiss Re Switzerland | Carl Christensen | Head L&H Platforms & Data Solutions | 1 | reinsurance |
| Swiss Re Switzerland | Julien Descombes | Chief Underwriting Officer Life & Health Reinsurance | 1 | underwriting |
| Swiss Re Switzerland | John Schoonbee | Global Chief Medical Officer | 2 | medical |
| Swiss Re Switzerland | Velina Peneva | CEO Life & Health Reinsurance, Member of Group EC | 2 | reinsurance |
| Swiss Re Switzerland | Ian Long | Head of Data and Operational Excellence, Life & Health Reinsurance | 2 | reinsurance |
| Swiss Re Switzerland | Ginger Turner | Head Data & Systems, Life & Health Reinsurance COO | 2 | reinsurance |
| Swiss Re Switzerland | Anna Mazerant | Head Transformation & Initatives Reinsurance L&H | 2 | reinsurance |
| Swiss Re Switzerland | Sergio Lopez Jimenez | Head L&H Research and Forecasting | 2 | reinsurance |
| Swiss Re Switzerland | Rainer Helfenstein | Market Head L&H Netherlands | 2 | reinsurance |
| Swiss Re Switzerland | Augusto Diaz-Leante | Managing Director at Swiss Re, Head of Life & Health Continental Europe | 2 | reinsurance |
| Swiss Re Switzerland | Ashish Agarwal | Head of Technology and Data L&H Solutions | 2 | technical-integration |
| Swiss Re Switzerland | Dan Lacurezeanu | Product & Delivery Director Magnum | 2 | technical-integration |
| Swiss Re Switzerland | Claude Schwarz | Head Global Experience Studies | 2 | underwriting |
| Swiss Re Switzerland | Charpentier Carole | Magnum Underwriting Rules Manager | 2 | underwriting |
| Swiss Re Switzerland | Francesca Tamma | Head of Behavioural Research | 3 | reinsurance |
| Volkswohl Bund | Carina Gervens | Teamleiterin Produktmanagement Biometrie | 1 | proposition |
| Volkswohl Bund | Erik Schwarz | Produktmanager Biometrie | 2 | proposition |
| Volkswohl Bund | Finja Dumstorff | Product Owner Vergleichsrechner Biometrie | 3 | proposition |
| Volkswohl Bund | Jan Müller | Abteilungsleiter Daten, KI & Automatisierung | 3 | referral |
| Volkswohl Bund | Dana Rienhoefer | Gruppenleiterin Privatkunden Leben / Antragsprüfung und -entscheidung | 3 | underwriting |
| Zurich Life Ireland | Michael Vesey | Head of Protection Proposition | 1 | proposition |
| Zurich Life Ireland | Colette Houton | Head of Underwriting at Zurich Life Assurance plc (Ireland) | 1 | underwriting |
| Zurich Life Ireland | Laura Corrigan | Head of New Business | 2 | proposition |
| Zurich Life Ireland | Niall Walsh | Head of Business Innovation | 2 | proposition |
| Zurich Life Ireland | Cormac Frawley | Head of Data Protection | 3 | technical-integration |
| a.s.r. | Angelique R | Medisch Adviseur | 2 | medical |
| a.s.r. | Marno Middelbos | Medisch Adviseur Inkomen bij ASR | 2 | medical |
| a.s.r. | Andre Rozemuller | Teammanager Managed Care en AOV Medisch Acceptatie | 2 | medical |
| a.s.r. | Gert Lokhorst | Teammanager Inkomen Acceptatie Individueel | 3 | underwriting |
| vers.diagnose | Fabian Van Lancker | Geschäftsführer | 1 | partnership |

## WEAK — not taken (Vadim 2026-11-02)

| Person | Title | Group | Why on the edge |
|---|---|---|---|
| Arthur van der Wal | Directievoorzitter / CEO | Achmea | CEO at Achmea with a Life sector-board seat (likely the pensions and life arm): C-level at a multi-line group, which ruling 8 excludes; Vadim decides. |
| Rene Steenks | Medisch Adviseur | Achmea | Medisch adviseur at Achmea, line not shown: Achmea also runs Zilveren Kruis health and verzuim, so acceptance is not confirmed (QC fix 2026-11-02) |
| Alf Neumann | Chief Operating Officer | Allianz Lebensversicherungs-AG | COO of Allianz Leben, earlier head of life product development: owns operations including new business, but C-level at a multi-line group with the UW head already P1. |
| Juliane Kania | Bereichsleiterin | Alte Leipziger Lebensversicherung | Bereichsleiterin FO Privatkundengeschäft Leben at Alte Leipziger, earlier at MDK: retail life operations that may include application and risk check, not shown. |
| Stephanie Forrester | Data Protection Officer | Aviva Ireland | second DPO at Aviva Ireland; Michelle Lyons (ex Aviva Life & Pensions) carries the account (QC fix 2026-11-02) |
| Klaus Künzel | Head of Client Applications | Gen Re Germany | Head of Client Applications at Gen Re Cologne, the European L&H unit: may own the client-facing underwriting tools, but L&H scope is not shown. |
| David Zimmermann-Kollenda | Head Of Analytics | Gen Re Germany | Head of Analytics (global analytics) at Gen Re Cologne, the European L&H unit: likely L&H data, but the scope is not shown. |
| Maximilian Fischer | Entwickler Risikoprüfung | Gen Re Germany | Entwickler Risikoprüfung at Gen Re Cologne: builds the underwriting software, but an individual developer, not an owner. |
| Holger Schmarowski | Chief Underwriter | Gen Re Germany | Chief Underwriter at Gen Re in Germany, but the profile is empty and the line is not shown. |
| Konstantin Lofink | Director | Hannover Re Germany | Director at Hannover Re in Germany with a life product-development past at HDI-Gerling Leben, but the current scope is not shown. |
| Karsten Koch | Data Protection Officer | Hannover Re Germany | Hannover Re's Datenschutzbeauftragter in Hanover fits the technical-integration lane, but the profile is empty. |
| Marian Conway | Head of Protection and Health Propositions at Irish Life Employer Solu | Irish Life Assurance | Heads protection propositions for Irish Life employer schemes: group cover is an anti-case, but she sits next to retail protection and could refer. |
| Greg Ward | Chief Operating Officer | Irish Life Assurance | COO and MD of Customer Solutions at Irish Life, which has no underwriting owner in the export; Irish Life is not on the ruling 8 list and the profile is empty. |
| Glenn Lambkin | Director of Engineering | Munich Re Automation Solutions | Director of Engineering at Munich Re Automation Solutions (in-scope platform): engineering below the CTO, who is already in, and engineering rarely replies (PPL-3). |
| Sean Doyle | Head Of Customer Service | Munich Re Automation Solutions | Head of Customer Service at Munich Re Automation Solutions in Ireland: in-scope platform, but service operations with no product or underwriting role (PPL-3). |
| Jennifer H. | Head of section Data Maintenance and Processing Life&Health | Munich Re Germany | Heads L&H data maintenance and processing: inside the life business, but back-office data operations with no underwriting role. |
| Katja Rettig | Executive Director | Munich Re Germany | Executive Director with no scope shown; earlier strategic projects at AXA Life Europe point to L&H, but the current line is not confirmed. |
| Sabine Ottmann | Partner - Consulting, Digital Solutions | Munich Re Germany | Consulting partner for digital solutions with a digital-health headline: may be L&H client consulting, but the line is not shown. |
| Sebastian Soika | Head of Client Management | Munich Re Germany | Head of Client Management, ex board of MedNet Greece (Munich Re health): L&H likely, but the market is not shown and may be Southern Europe. |
| Florian Fuchsbrunner | Head of UW Data & Analytics | Munich Re Germany | Head of UW Data & Analytics with no background shown: underwriting analytics is P2, but L&H or P&C is not visible. |
| Rodrigo Belloube | Chief Underwriting Officer | Munich Re Germany | Chief Underwriting Officer with no line shown; ex CEO Munich Re Brazil suggests P&C or LatAm, P1 only if the role is L&H Europe. |
| Lisa Plunkett | Head of Individual Business | New Ireland Assurance | Head of Individual Business at New Ireland: may own individual new business (P2) or only servicing; scope not shown, earlier customer service. |
| Marie Murphy | Head of Actuarial & Product Services | New Ireland Assurance | Head of Actuarial and Product Services at New Ireland: may own protection pricing (P2), but empty profile. |
| Shane Ferguson | Deputy Data Protection Officer | New Ireland Assurance | deputy DPO at New Ireland; Ronan Scully (Head of Operational Risk and DPO) carries the account (QC fix 2026-11-02) |
| Yosra JEMAI | Head of French Multichannel Distribution Market & African Markets | SCOR France | SCOR L&H partnerships market head in Paris, but her markets are France and Africa, outside the cut (card: offered to Vadim). |
| Maria Brohmi | Chief Underwriting Officer | SCOR France | Chief Underwriting Officer title at SCOR in Paris, but the profile is empty and the line (L&H or P&C) is not shown. |
| Claire Juillard | Group Data Protection Officer (DPO) | SCOR France | second group DPO at SCOR; Marvin Dewkurun (ex legal counsel EMEA Life) carries the account (QC fix 2026-11-02) |
| Sophie Chapelain | Responsable Sélection des Risques et Sinistres / Head of Medical Under | SCOR France | Head of medical underwriting (and claims) at SCOR in France, but the French-language title points to the French market team, outside the cut. |
| Domenico Semeraro | Head of DACH & CEE | SCOR Germany | SCOR's DACH and CEE market head in Germany, but L&H or P&C is not shown and the Gen Re treaty and Aon broker past may point to P&C. (OQ12 country row, Vadim 2026-11-02) |
| Aisling Bradfield | Head of Behavioural Science at SCOR Global Life | SCOR Ireland | Head of behavioural science at SCOR Global Life in Ireland, the team behind application question design, but the profile is empty. (OQ12 country row, Vadim 2026-11-02) |
| Brent Engelke | Chief Executive Officer | SCOR Ireland | Second Chief Executive Officer title at SCOR Ireland with a finance past: no L&H scope shown, and one of the two CEO profiles may be stale or head another entity. (OQ12 country row, Vadim 2026-11-02) |
| Michael Haas | Head Life & Health Austria & CEE, Nordics | Swiss Re Germany | L&H, serves Austria, CEE and the Nordics: Munich-based L&H head for markets outside the cut; Germany sits with Markus Unterkofler. (OQ12 country row, Vadim 2026-11-02) |
| Roman Lerch | Head Client Management ACEE / L&H Reinsurance | Swiss Re Germany | L&H, serves Austria and CEE: client management head for ACEE, which excludes Germany (Unterkofler's title lists Germany separately). (OQ12 country row, Vadim 2026-11-02) |
| Claudia Szwillus | Head of UW and Claims L&H NACEE( Nordics Austria Central and Eastern E | Swiss Re Germany | L&H, serves Nordics, Austria and CEE: heads L&H underwriting and claims for NACEE, which excludes Germany; former Risikoprüfer at Continentale. (OQ12 country row, Vadim 2026-11-02) |
| Ueli Konrad | Head Data-Driven Underwriting & Analytics | Swiss Re Switzerland | Heads data-driven underwriting and analytics at head office, but the line (L&H or P&C) is not shown; if L&H he is P2 underwriting. |
| Jason Stone | Head of Business Development Life & Health Solutions EMEA UK&I | Swiss Re Switzerland | L&H Solutions BD whose title scope reads EMEA UK&I; the coordinator holds him because UK is katerina's market, Vadim decides (Volker Homola at Munich Re, Continental Europe, is P2) (QC fix 2026-11-02) |
| Enzo Vitale | Head of Life&Health Pricing Tools Development | Swiss Re Switzerland | Heads L&H pricing tools development: builds actuarial tooling rather than owning pricing or underwriting, so the P2 pricing-head tier fits only loosely. |
| Klemens Binswanger | Head UW & Claims Continental Europe | Swiss Re Switzerland | Head UW & Claims Continental Europe: L&H is inferred from board roles, the line is not in the title (ruling 12) (QC fix 2026-11-02) |
| Paul Murray | CEO Life & Health Reinsurance | Swiss Re Switzerland | Lists CEO L&H Reinsurance, the same title as Velina Peneva (Group EC); one of the two is stale, check before sending. |
| Aline Avedikian | Head A&H Product & Strategy, Global | Swiss Re Switzerland | Heads global accident and health product and strategy in L&H: a product owner, but A&H is not the individual life and disability business with build questions, and no market in the cut is named. |
| Marco Spagnuolo | Head of Conversational AI Solution | Swiss Re Switzerland | Heads a conversational AI solution with an L&H in-force management background: L&H scope visible, but in-force retention, not new-business underwriting. |
| Dominik Renggli | Head of Product Management | Swiss Re Switzerland | Head of Product Management with no line shown: the card's P3 head-of-product tier, but at a reinsurer it may be P&C or IT product, which FAIL. |
| Pia Burghartz, PhD | Global Head Behavioral Consulting Practice | Swiss Re Switzerland | Heads the global behavioural consulting practice that sells behavioural science to insurers, but the headline frames it as topline growth, not underwriting evidence. |
| Ariane Ehlers | Market Head L&H Belgium & Luxembourg | Swiss Re Switzerland | L&H, serves Belgium and Luxembourg: head-office L&H market head for a market outside the cut (Belgium is second wave). |
| Daniel Meier | Head Life & Health Risk Modelling | Swiss Re Switzerland | Heads L&H risk modelling: L&H scope visible, but risk modelling likely means the capital model rather than underwriting or biometric research. |
| Luiz Bueno | Market Head Life & Health Italy, Iberia | Swiss Re Switzerland | L&H, serves Italy and Iberia: head-office L&H market head for markets outside the cut. |
| Brian Gray | Group Chief Underwriting Officer | Swiss Re Switzerland | Group Chief Underwriting Officer with an empty profile and group-wide (P&C and L&H) scope; Julien Descombes holds the L&H CUO seat (ruling 10). |
| Michael Kamm | L&H Underwriting Manager CH & MENA | Swiss Re Switzerland | L&H, serves Switzerland and MENA: L&H underwriting manager (P3 by tier) for markets outside the cut. |
| Pavel Cerny | Manager L&H Underwriting, Central & Eastern Europe at Swiss Re | Swiss Re Switzerland | L&H, serves Central and Eastern Europe: L&H underwriting manager (P3 by tier) for a market outside the cut. |
| Shane Farrelly | Head of Underwriting Analytics | Zurich Life Ireland | Head of Underwriting Analytics (P2 by ruling 6), but earlier Head of Personal Property at Zurich Insurance: may sit in Zurich GI, not Life. |
| Katie Linstra | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Marlot Linstra | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Caroline Yntema | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Constance Koevoets | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Mattanja Dirks | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Hans Balk | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Evelien Groot | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |
| Marga Van Liere | Medisch Adviseur | a.s.r. | Medisch adviseur at a.s.r., line not shown: acceptance (the buyer) or AOV claims and personal injury (not) (QC fix 2026-11-02) |

## Left out: pools

Full list by function in `skipped-detail.md` (596 not sent, 537 senior). Only the pools worth a decision:

| Pool | People | Who (examples) | Proposed angle | What changes to take them |
|---|---|---|---|---|
| A. L&H market teams outside the head-office country (Open question 12) | ~16 (11 in the list, FAIL by location; 5 Irish branch rows left out at extract) | Swiss Re in Munich: Markus Unterkofler (Head L&H Germany, ACEE & Nordics), Claudia Szwillus (Head UW & Claims L&H NACEE), Sebastian Strasser (Head Business Advisory L&H), Roman Lerch (Client Mgmt ACEE L&H) · SCOR in Cologne: Thomas Trompetter, Domenico Semeraro · SCOR Ireland: Redmond Murphy (Deputy CEO SCOR L&H), Aisling Bradfield; extract-time rows SCOR Global Life Reinsurance Ireland (Head of Business Acceptance), SCOR Ireland CEO · Hannover Re Ireland: Head of L&H Ireland & Canada · Munich Re Dublin: Declan O'Neill (Head Digital & Innovation Strategy L&H Europe) · SCOR NL: Martijn Reijerse (CTO L&H) | `reinsurance` (`technical-integration` for Reijerse) | **Taken 2026-11-02** for `Swiss Re Germany`, `SCOR Germany`, `SCOR Ireland`, `Hannover Re Ireland` (PASS 8). Munich Re Dublin (O'Neill) and SCOR NL (Reijerse) stay FAIL. |
| B. Group data, AI, digital and IT heads at reinsurers without L&H scope | ~30 | Fabian Winter (Munich Re Chief Data & AI Officer), Thibault Antoine (SCOR Group Chief AI Officer), Mark W. (Swiss Re Group CDAO) | `referral` | P3 referral for group-wide digital heads at reinsurers. Not recommended (PPL-3: engineering 1 reply in 90). |
| C. CIOs and heads of IT at multi-line insurers | ~7 | Ashling Cunningham (Irish Life), Dennis Roehrs (CosmosDirekt) | `technical-integration` | Extend the single-line CIO rule to multi-line groups. Not recommended: technical-integration is already 26 of 127. |
| D. Insurer CEOs where an underwriting head is already in | 2 | Barry Cudmore (CEO Aviva Life & Pensions Ireland), Noel Freeley (CEO Royal London Ireland) | `referral` | Extend decision 5 to insurers that already have a P1. Optional. |
| E. Strategy, change and programme heads at insurers | ~9 | Alan Brady, Denis McManus, Eimear Saul | `referral` | Not recommended: Irish Life already carries 8 referral PASSes. |

Claims heads (decision 8), P&C at reinsurers, private health, pensions and investments stay out by the card.

## Top concerns

- **Hlib's sheet is again a seniority pull by company, not a title pull** (11 persona titles in 685 rows; the UK twin had the same problem). About 85% of the reinsurer rows are P&C, IT, finance or corporate. The Apollo title top-up found the L&H owners (Swiss Re CUO L&H, Gen Re Global CUO L/H, Zurich Life IE Head of UW, Royal London IE Head of UW, Volkswohl Biometrie). Gaps neither source closes: **no people** at Allianz Nederland, Dialog, Europa, HDI, RGA Ireland; **no PASS** at Die Bayerische (10 rows, sales/IT/motor) and Scildon; **no ORV/AOV owner** at NN (31 rows) and none at Achmea or Irish Life underwriting (Irish Life has 51 rows, no chief underwriter). Vadim decided against a title re-pull: the campaign runs on this list.
- **technical-integration is 21 of 131 PASS** after Vadim trimmed the five group architects/CTO without L&H scope (PPL: engineering answered 1 in 90).
- **referral is 19**; Irish Life capped at 4 by Vadim (Shay Browne, Christopher Curran, Kelvin Gillen, Alan Q.).
- **Medisch adviseurs:** 8 at a.s.r. and 1 at Achmea are now WEAK because the profile does not show acceptance (the buyer) versus AOV claims or personal injury (not). The Netherlands then rests on Middelbos and Angelique R (a.s.r.), Lokhorst (a.s.r. income acceptance) and NN/Achmea referral and IT rows: the Dutch buyers are mostly missing from the export.
- Hannover Re serves German cedants through E+S Rück, which is not on the company list.
- **Data quirk, harmless:** `location_country` in `people-raw.csv` is the company HQ for Sales Navigator rows (Aviva → United Kingdom, Gen Re → United States); the validator judged the person's own location from `people-compact.csv`.

## Next

1. Fresh `hypothesis-generator` writes `### Account facts` for the 31 groups with PASS (four new country rows included) from `companies.md`, under Message angle.
2. `outbound_pack.py card --for messages` → `profiles` → `message-sequencer` batches with `_grid-<batch>.md` up front → `check-messages` → opus QC → Vadim's second checkpoint.
