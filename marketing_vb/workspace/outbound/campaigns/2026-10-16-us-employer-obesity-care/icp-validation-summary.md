---
product: fitxpress
profile: nick
campaign: 2026-10-16-us-employer-obesity-care
created: 2026-10-16
stage: validate
status: awaiting_review
---

# ICP Validation Summary — 2026-10-16-us-employer-obesity-care

Входы: `card-validate.md` и `people-compact.csv` (384 человека: 359 из выгрузки Вадима, 25 из добора через Apollo). Из `people-raw.csv` смотрел только строки 7 conditional-людей и двух профилей Patrick Lawrence. Решения: `decisions.md`, итоговый файл: `people-validated.csv`.

## Stats

| | Людей |
|---|---|
| Оценено | 384 (359 export + 25 Apollo) |
| **PASS (SEND)** | **367**: P1 43 · P2 107 · P3 43 · P4 174 |
| WEAK (REVIEW) | 7 (5 conditional без подтверждения роли, 2 eMed в Лондоне) |
| FAIL | 10 (7 identity collisions из карточки, 3 придержанных дубликата) |
| Исключены реестром (`nick`) | 0 |

Сверка с карточкой: в карточке 349 sendable (342 IN + 7 conditional). Из выгрузки прошли 344: все 342 IN и 2 из 7 conditional, у которых роль подтверждается (Kristin Grunzweig, Robyn Guillen). Плюс 23 из 25 человек Apollo.

**Распределение по группам против кепа 100** (вывод `apply-decisions`). До кепа не дошла ни одна группа:

| Группа | SEND | P1 | P2 | P3 | P4 | product | clinical | operations | tech-int | referral |
|---|---|---|---|---|---|---|---|---|---|---|
| Included Health | 96 | 7 | 31 | 10 | 48 | 3 | 18 | 17 | 10 | 48 |
| Omada Health | 68 | 7 | 15 | 11 | 35 | 8 | 7 | 7 | 11 | 35 |
| Vida Health | 47 | 6 | 13 | 4 | 24 | 6 | 5 | 8 | 4 | 24 |
| Crossover Health | 41 | 6 | 19 | 5 | 11 | 3 | 12 | 10 | 5 | 11 |
| eMed | 37 | 4 | 6 | 3 | 24 | 3 | 1 | 6 | 3 | 24 |
| MDLIVE | 32 | 4 | 11 | 4 | 13 | 4 | 4 | 7 | 4 | 13 |
| Wondr Health | 23 | 4 | 6 | 4 | 9 | 5 | 2 | 3 | 4 | 9 |
| Goodpath | 13 | 2 | 4 | 1 | 6 | 2 | 3 | 1 | 1 | 6 |
| Digbi Health | 10 | 3 | 2 | 1 | 4 | 3 | 2 | 0 | 1 | 4 |
| **Итого** | **367** | 43 | 107 | 43 | 174 | 37 | 54 | 59 | 43 | 174 |

**По angle:** `referral` 174 · `operations` 59 · `clinical` 54 · `technical-integration` 43 · `product` 37. Волна у всех 1.

**Как раздавал Apollo-людей** (в карточке для них назначений не было, тир и лейн по правилам персоны): CMO и CPO = P1 (Thomas Tsang в Omada, Richard Frank и David Osborne в Vida, Dyan Hes в eMed, Tim Church в Wondr). Head of Product в Goodpath Jason Trees и VP Product & Engineering в Digbi Sangeet Saurabh = P1 `product`. Медицинские директора, clinical leads и продакт-менеджеры = P2. Инженерный лид Digbi Rajan Bhuyan = P3.

**Где разошёлся с раскладкой карточки** (тиры только упорядочивают список, но для сверки): Brittani Hahn (eMed, Delivery Director) идёт в `operations` как внедрение у работодателя. Alicia Anderson (Growth & Product Operations) и Whitney Murphy (Chief of Staff) в Omada идут в `referral`. Claudia Ryan (Vida, Therapy and Care Navigation) идёт в `operations`. Sonia Lorbeski (IH, Advocacy Enablement) идёт в `referral`. Customer service и customer experience везде `referral`, как в карточке.

## Proposed to SEND

367 человек, отсортированы по группе, приоритету и angle. Полная строка с причиной по каждому лежит в `people-validated.csv`.

| Группа | Человек | Title | P | Angle |
|---|---|---|---|---|
| Included Health | Mary Reynolds | Senior Director of Product Management | 1 | product |
| Included Health | Owen Tripp | Chief Executive Officer | 1 | product |
| Included Health | Alexandra Yurkovic | Chief Medical Officer and Senior Vice President, Clinical Services and Delivery | 1 | clinical |
| Included Health | Vibin Roy, MD MBA | Vice President of Virtual Care | 1 | clinical |
| Included Health | Heather Johnson | Vice President, Practice Operations | 1 | operations |
| Included Health | Katie Robinson | Senior Director, Virtual Care Strategy & Operations | 1 | operations |
| Included Health | Meher Iqbal | Senior Director & GM, Care Delivery | 1 | operations |
| Included Health | Sara T. | Director, Product | 2 | product |
| Included Health | Adedamola Solawon, DNP, APRN,FNP-BC | Associate Clinical Director | 2 | clinical |
| Included Health | Akin Oyalowo | Medical Director, Clinical Affairs | 2 | clinical |
| Included Health | Anish Mehta, MD, MPP | Senior Medical Director, Complex Care | 2 | clinical |
| Included Health | Diana Malone | Director of Urgent Care | 2 | clinical |
| Included Health | Heather Hockenberry | Associate Medical Director | 2 | clinical |
| Included Health | Heather W. | Associate Medical Director, Primary Care | 2 | clinical |
| Included Health | Jeanette Carpenter | Associate Medical Director | 2 | clinical |
| Included Health | Jensen Campbell, PhD | Associate Clinical Director | 2 | clinical |
| Included Health | Jesse Michel | Associate Clinical Director, Care and Case Management | 2 | clinical |
| Included Health | Jordana Blair | Associate Medical Director, Specialty Care | 2 | clinical |
| Included Health | Megan White | Associate Clincal Director, Triage | 2 | clinical |
| Included Health | Phil Z. | Senior Medical Director, Clinical Affairs | 2 | clinical |
| Included Health | Sharon Johnson | Utilization Management Director | 2 | clinical |
| Included Health | Tamera Brandon MBA, MSN, RN | Clinical Director | 2 | clinical |
| Included Health | Tony Yuan, MD | Senior Medical Director, Urgent Care | 2 | clinical |
| Included Health | Yvette Young, MD, MBA | Associate Medical Director, Clinical Affairs | 2 | clinical |
| Included Health | Arvella W. | Director, Client Onboarding & Implementation | 2 | operations |
| Included Health | Bonnie Grenis | Vice President, Member Care - The Advocacy Team | 2 | operations |
| Included Health | Courtney Ortiz | Director, Pop Health Operations & Partnerships | 2 | operations |
| Included Health | Erin LaBarge | Director, Client Implementation | 2 | operations |
| Included Health | Jaclyn Karlen Marshall | Senior Health Economics and Outcomes Research Director | 2 | operations |
| Included Health | Kayla Cooper | Director, Member Care | 2 | operations |
| Included Health | Kyle Hughes | Vice President, Data Insights | 2 | operations |
| Included Health | Lauren Martinez | Senior Director, Population Health Strategy & Operations | 2 | operations |
| Included Health | Leah Brooke | Director, Performance Analytics | 2 | operations |
| Included Health | Melody Burns Msiska, MD | Director, Care Navigation | 2 | operations |
| Included Health | Meryl Fogg | Sr. Vice President, Member Care & Operations | 2 | operations |
| Included Health | Michael Starkey | Senior Director, Analytics | 2 | operations |
| Included Health | Susan Clune, CRNP | Director of Clinical Navigation | 2 | operations |
| Included Health | Tracy Wong | Vice President, Member Care Operations | 2 | operations |
| Included Health | Amyn Remtulla | Vice President, Technology Services | 3 | technical-integration |
| Included Health | Annabel Liu | Senior Vice President of Engineering | 3 | technical-integration |
| Included Health | Arjita Ghosh | Director of Engineering | 3 | technical-integration |
| Included Health | Geoff Janjua | Chief Information Security Officer | 3 | technical-integration |
| Included Health | Jeremiah B. | Director, Digital Workplace | 3 | technical-integration |
| Included Health | Kunal Sahu | Director of Engineering, Client Growth | 3 | technical-integration |
| Included Health | Mona Farhangi | Director of Engineering, Care Platform | 3 | technical-integration |
| Included Health | Pujita Mathur | Senior Director of Engineering | 3 | technical-integration |
| Included Health | Srdjan Perisic | Director, Healthcare Compliance | 3 | technical-integration |
| Included Health | Timothy Springer | Chief Compliance Officer | 3 | technical-integration |
| Included Health | Alessandra Henderson | Head of Strategic Growth Partnerships | 4 | referral |
| Included Health | Allison Treftz | Director, Client Success | 4 | referral |
| Included Health | Amanda Singleterry, PHR,CCP,GRP | Director, G&A Systems | 4 | referral |
| Included Health | Austin Aldrich | Division Vice President Consultant Strategy & Relations | 4 | referral |
| Included Health | Austin Kipp | Senior Director Corporate Development | 4 | referral |
| Included Health | Brad Edwards | Director - Operational Transformation & Enablement | 4 | referral |
| Included Health | Chelsea Joseph | Division Vice President, Growth & Partnerships | 4 | referral |
| Included Health | Christine Walanka | Director, Client Success | 4 | referral |
| Included Health | Cody Yashinsky | Proposal Management & AI Director | 4 | referral |
| Included Health | Colin Quinn | President, Included Health Communities | 4 | referral |
| Included Health | Craig Root | Chief Commercial Officer | 4 | referral |
| Included Health | David Scott | Director Growth Operations, Policy and Commercial Process | 4 | referral |
| Included Health | Dustin Bruggman | VP of Finance | 4 | referral |
| Included Health | Emma Schaffer (Sheldon) | Senior Director, Sales Performance | 4 | referral |
| Included Health | Emma Spiegel | Sr. Director FP&A | 4 | referral |
| Included Health | Hannah Bowen, RHU®, CSFS®, FAHM®, REBC® | Director of Sales, Channel Partnerships | 4 | referral |
| Included Health | Hannah Sivwright | Director, Client Success | 4 | referral |
| Included Health | Heather Conroy | Director, Claims, Communities and Referrals | 4 | referral |
| Included Health | Hillary Livengood | System Optimization Director | 4 | referral |
| Included Health | Jacqueline Poli | Solutions Consulting Director | 4 | referral |
| Included Health | Jaimie Kennedy, CPA (Inactive) | FP&A Business Partner | 4 | referral |
| Included Health | Jeni Klein | Director of Client Success | 4 | referral |
| Included Health | Jennifer Stanley | Director, Proposals | 4 | referral |
| Included Health | Jennifer Ullig, MBA | Director of FP&A | 4 | referral |
| Included Health | Jeremy Gross | Director, Group Health Strategy | 4 | referral |
| Included Health | Kerri K. Leigh | Senior Vice President, Customer Organization | 4 | referral |
| Included Health | Kim Seifi, MBA | FP&A Business Partner | 4 | referral |
| Included Health | Laura Eckhardt | Vice President of Strategy | 4 | referral |
| Included Health | Lauren Boneta Pierce | Client Success Director | 4 | referral |
| Included Health | Laurie Hinton | Vice President, Enterprise Client Success | 4 | referral |
| Included Health | Maggie Ohrt | Client Success Director- Navigation | 4 | referral |
| Included Health | Mark Flakne | Chief Financial Officer | 4 | referral |
| Included Health | Mary Melvin (she/her) | Senior Director, Ecosystem & Channel Partner Success | 4 | referral |
| Included Health | Mary-Helen Holland | VP, Growth Operations & Effectiveness | 4 | referral |
| Included Health | Mia Farrell (She/Her) | Sales Director, Communities | 4 | referral |
| Included Health | Mike Schirmers | Senior Vice President - Finance & Analytics | 4 | referral |
| Included Health | Nancye Smith | Director of GTM Enablement | 4 | referral |
| Included Health | Nick Boyd | Director, Growth Operations | 4 | referral |
| Included Health | Rachel Urbis | Vice President, Enterprise Sales | 4 | referral |
| Included Health | Ramon Torres | Director, Finance Systems | 4 | referral |
| Included Health | Shreya Gupta | Director Business Acceleration | 4 | referral |
| Included Health | Sonia Lorbeski | Director of Advocacy Enablement | 4 | referral |
| Included Health | Stefanie Isley | Client Success Senior Director (Since 2023)   /   Director, Client Success (2020 to 2022) | 4 | referral |
| Included Health | Stuart Gillespy | Director - Client Delivery Excellence | 4 | referral |
| Included Health | Suzanne Schmidt | Client Success Director | 4 | referral |
| Included Health | Tia Echeverria | Client Success Director | 4 | referral |
| Included Health | Travis Pierce | Solutions Consulting Director | 4 | referral |
| Included Health | Vincent Chang | Sr. Director, VBC Commercialization | 4 | referral |
| Omada Health | Britt Buntman | VP, GLP-1 and Cardiometabolic Health | 1 | product |
| Omada Health | Danika Harrison | Chief Product and Growth Officer | 1 | product |
| Omada Health | Ellery Cook | VP Product Management, Medical | 1 | product |
| Omada Health | Sean Duffy | Co-Founder & CEO | 1 | product |
| Omada Health | Wei-Li Shao | President | 1 | product |
| Omada Health | Thomas Tsang | Chief Medical Officer | 1 | clinical |
| Omada Health | Jennifer Becker | Chief Care Delivery Operations Officer | 1 | operations |
| Omada Health | Brandon Piechowski | Senior Director of Product Management | 2 | product |
| Omada Health | Spencer Cross | Senior Director of Product Management, Data, AI & Platform Services | 2 | product |
| Omada Health | Thuy Le | Director of Product | 2 | product |
| Omada Health | Alison Megliola, MS, RD, CDCES | Director, Clinical Product - Cardiometabolic | 2 | clinical |
| Omada Health | Amanda McGuill, NP-C, CDCES | Director, Clinical Product | 2 | clinical |
| Omada Health | Crystal Onwu, PharmD, RPh | Director Clinical Affairs | 2 | clinical |
| Omada Health | Hope Chang, PharmD | Director of Clinical Affairs, Clinical Writing and Translation | 2 | clinical |
| Omada Health | Kevin Masci, Pharm D | Sr. Director of Clinical Strategy | 2 | clinical |
| Omada Health | Todd Norwood, PT, DPT, FACHE | Senior Director, Clinical Services | 2 | clinical |
| Omada Health | Alex Chun | Senior Director, Member Operations | 2 | operations |
| Omada Health | Amber Boyd | Sr. Director of Clnical Operations & Practice | 2 | operations |
| Omada Health | Dani Burns | Sr Director, Data Analytics | 2 | operations |
| Omada Health | Karli Greene | Director, Client Operations | 2 | operations |
| Omada Health | Kathryn Wintermantel | Senior Director, Client Reporting & Analytics | 2 | operations |
| Omada Health | Lindsey Arnold | Director, Care Teams Optimization & Analytics | 2 | operations |
| Omada Health | Anna Nelson | Senior Director of Engineering | 3 | technical-integration |
| Omada Health | Ashok Kallarakuzhi | Director of Engineering, Data & AI | 3 | technical-integration |
| Omada Health | Franck Verrot | Vice President of Engineering | 3 | technical-integration |
| Omada Health | Kalika Kekkar | Director, Data | 3 | technical-integration |
| Omada Health | Marty Lynch | Director, Applied AI & Applied Statistics | 3 | technical-integration |
| Omada Health | Patrick Curry | Vice President, Compliance | 3 | technical-integration |
| Omada Health | Stanislav B. | Vice President Information Technology | 3 | technical-integration |
| Omada Health | Sunil Kayiti | Chief Technology Officer | 3 | technical-integration |
| Omada Health | Terry Miller | Vice President AI & Machine Learning | 3 | technical-integration |
| Omada Health | Tessa Morse | Director of Engineering, Member Experience | 3 | technical-integration |
| Omada Health | Veronica S. | Privacy and Compliance Director | 3 | technical-integration |
| Omada Health | Abdullah Nasir | Vice President Customer Experience | 4 | referral |
| Omada Health | Alicia Anderson | Director, Growth & Product Operations | 4 | referral |
| Omada Health | Arvind Stokes | Senior Vice President, Enterprise Sales & Customer Experience | 4 | referral |
| Omada Health | Brandon Hendricks | National Vice President, GLP-1 Sales | 4 | referral |
| Omada Health | Bridgette Bazant | Director Strategic Alliances | 4 | referral |
| Omada Health | Dane Woodley | Director, Commercial Enablement | 4 | referral |
| Omada Health | Emily Carbonara | Director, Alliance Delivery | 4 | referral |
| Omada Health | Garrett Halls | Senior Director, Strategic Finance | 4 | referral |
| Omada Health | Gerald Holt | National Vice President, GLP-1 Sales | 4 | referral |
| Omada Health | Hana Putman | Creative Director | 4 | referral |
| Omada Health | Heidi Chang | Sr. Director, Global Supply Chain | 4 | referral |
| Omada Health | Holly Morganti | Vice President, Head of Channel Sales, Consultant Relations & Reseller Growth | 4 | referral |
| Omada Health | Holly Scholl, MPH | Director, Strategic Alliance Management | 4 | referral |
| Omada Health | Jenny Sproull | Director Corporate Strategic Planning and Business Development | 4 | referral |
| Omada Health | Jerad Martin | National Vice President- Employer Sales | 4 | referral |
| Omada Health | Jessica Marr | Sr Director, Commercial Effectiveness | 4 | referral |
| Omada Health | Jill Belinky | Director of Partnership Growth | 4 | referral |
| Omada Health | Julie Mulcahy, PT, DPT, FACHE | Director, MSK Program | 4 | referral |
| Omada Health | Lily Orn | Senior Director, Customer Experience | 4 | referral |
| Omada Health | Mark G. Munsell | Vice President, Commercial Operations | 4 | referral |
| Omada Health | May Wu | Director, SOX Compliance | 4 | referral |
| Omada Health | Michael Becker | National Vice President, GLP-1 Strategy | 4 | referral |
| Omada Health | Michelle Percia | Senior Manager Partner Enablement | 4 | referral |
| Omada Health | Muhammad H. | VP | 4 | referral |
| Omada Health | Nicki Nieman | Senior Director, Corporate Strategy, Planning, and Business Development | 4 | referral |
| Omada Health | Nicole Hayes | National Vice President, Jumbo Sales and Strategy | 4 | referral |
| Omada Health | Ryan Minekime | Vice President, Head of Strategic Finance | 4 | referral |
| Omada Health | Sarah Hadburg | Director, Revenue Cycle | 4 | referral |
| Omada Health | Sean Milligan | Director, Strategic Accounts | 4 | referral |
| Omada Health | Shariyar Zarea | Director, Strategic Operations | 4 | referral |
| Omada Health | Steve Cook | Chief Financial Officer | 4 | referral |
| Omada Health | Steven Purta | Director of Sales Forecasting and Analytics | 4 | referral |
| Omada Health | Tanya Bellard | Director of Partnership Growth | 4 | referral |
| Omada Health | Tanya Lamp | Sr Director / Head of Customer Service | 4 | referral |
| Omada Health | Whitney Murphy | Vice President, Operational Excellence and Chief of Staff | 4 | referral |
| Vida Health | Ashish Nag | Director of Product Management | 1 | product |
| Vida Health | David Osborne | Chief Product Officer | 1 | product |
| Vida Health | Joe M. | President & CEO, Board Member | 1 | product |
| Vida Health | Richard Frank | Chief Medical Officer | 1 | clinical |
| Vida Health | Amy Mushlin | SVP Clinical Operations and Strategy | 1 | operations |
| Vida Health | Shane Giuliani | Chief Operating Officer | 1 | operations |
| Vida Health | Alen Tersakyan | Product Manager | 2 | product |
| Vida Health | Hersh Ranpura | Product Manager | 2 | product |
| Vida Health | Tom Kazer | Senior Group Product Manager, Client Experience | 2 | product |
| Vida Health | Annie Braun Gazda | Director Clinical Solutions | 2 | clinical |
| Vida Health | Jennifer Moreno | Clinical Dietetics Lead | 2 | clinical |
| Vida Health | Laura Isaacson MS, RD, CDCES, CSOWM, FAND, CD | Senior Director, Clinical Dietetics | 2 | clinical |
| Vida Health | Letal Yerganjiev | Clinical Dietetics Lead | 2 | clinical |
| Vida Health | Christina Bowens | Senior Director of Operations | 2 | operations |
| Vida Health | Christina Labib | Senior Director Clinical Operations | 2 | operations |
| Vida Health | Claudia Ryan, LCSW | Senior Director of Therapy and Care Navigation | 2 | operations |
| Vida Health | Erin Mynaugh | VP - Operations | 2 | operations |
| Vida Health | Mollie M. | Director, Member Experience | 2 | operations |
| Vida Health | Tara Fiano | Clinical Lead, Healthcare Operations | 2 | operations |
| Vida Health | Christopher Knaplund | Senior Director of AI & Data Engineering | 3 | technical-integration |
| Vida Health | Jorge Pérez Martínez | Director of Frontend Engineering | 3 | technical-integration |
| Vida Health | Joshua Stevens | Director Of Engineering | 3 | technical-integration |
| Vida Health | W. Bryan Smith | Chief Technology Officer | 3 | technical-integration |
| Vida Health | Alyssa Chafe, RD, MBA | Sales Director - Mid Market | 4 | referral |
| Vida Health | Angela Brennan, MPH | Vice President, Client Success | 4 | referral |
| Vida Health | Bill Campbell | VP of Sales, Taft-Hartley & Labor Markets | 4 | referral |
| Vida Health | Brent Hartman | Consultant Relations Director | 4 | referral |
| Vida Health | Colleen Reagan | Director, Sales Enablement | 4 | referral |
| Vida Health | David Carlson | Vice President of Finance | 4 | referral |
| Vida Health | Erica Terry | Vice President, Payer | 4 | referral |
| Vida Health | Gary Earl | Member Of The Board Of Advisors | 4 | referral |
| Vida Health | Hannah Porter | Director, Growth Strategy & Revenue Operations | 4 | referral |
| Vida Health | Jason Macaleer | Chief Strategy Officer (CSO) | 4 | referral |
| Vida Health | Jeff Schoenbauer | Vice President Sales, Enterprise - Central Region | 4 | referral |
| Vida Health | Jennifer Rice | Director, Client Success | 4 | referral |
| Vida Health | Jerry Jarvis | VP of Sales | 4 | referral |
| Vida Health | Jessica Vollendorf | Creative Director | 4 | referral |
| Vida Health | Julie Feneis | Director of Strategy & Operations, Client Success | 4 | referral |
| Vida Health | Kerryanne Shuler | Client Success Director | 4 | referral |
| Vida Health | Kristin Grunzweig | Director of Client Success | 4 | referral |
| Vida Health | Makara Fairman, MSW | Senior Director, Proposals | 4 | referral |
| Vida Health | Meredith Sparrow | Vice President Sales, Enterprise - Southeast Region | 4 | referral |
| Vida Health | Meredith Velan | Senior Vice President, Partnerships | 4 | referral |
| Vida Health | Michael Elassy | Sales Director, Mid-Market, East | 4 | referral |
| Vida Health | Pamela Babington | Client Success Director | 4 | referral |
| Vida Health | Ravi Guha | Chief Financial Officer | 4 | referral |
| Vida Health | Tracy Rodriguez, MBA | Director, Client Success | 4 | referral |
| Crossover Health | Anna Nachamie | Senior Director, Head of Product | 1 | product |
| Crossover Health | Scott Shreeve, MD | Chief Executive Officer, Founder | 1 | product |
| Crossover Health | Sally Larwood | Chief Nursing Officer | 1 | clinical |
| Crossover Health | Sumeet Batra, MD, MPH, FACOEM | National Medical Director of Occupational Medicine & Employee Health | 1 | clinical |
| Crossover Health | Sarah Lord | Chief Operating Officer | 1 | operations |
| Crossover Health | Sarah Pickell | Director, Medical Group Operations | 1 | operations |
| Crossover Health | Clifton Pait, MBA | Director of Product Management | 2 | product |
| Crossover Health | Amy Esposito, MD | Medical Director, Market Physician Manager | 2 | clinical |
| Crossover Health | Barry Giglio, M.D., MS | Site Medical Director | 2 | clinical |
| Crossover Health | Guido Macchiavello | Physician Lead | 2 | clinical |
| Crossover Health | Hari Athreya | Market Physician Director | 2 | clinical |
| Crossover Health | Josh Bruce | Onsite Medical DIrector | 2 | clinical |
| Crossover Health | Natalie Wilhelm | Medical Director | 2 | clinical |
| Crossover Health | Sreelata Kintala | Medical Director | 2 | clinical |
| Crossover Health | Steve Roey | National Division Medical Director | 2 | clinical |
| Crossover Health | Steven Chang, MD | Primary Care Program Director | 2 | clinical |
| Crossover Health | Steven Watts, MD, MPH | Medical Director, Roche and Genentech Account | 2 | clinical |
| Crossover Health | Cheryl Becerra | Practice Director | 2 | operations |
| Crossover Health | Christina Borduz | Practice Director | 2 | operations |
| Crossover Health | Cristy D. | Practice Director | 2 | operations |
| Crossover Health | Daniel Lord, DC | National Clinic Director | 2 | operations |
| Crossover Health | Jaclyn Hiura | Senior Practice Director | 2 | operations |
| Crossover Health | Jill Galvez, BSN, RN, NE-BC | National Practice Director | 2 | operations |
| Crossover Health | Laurel Lefler | Director Process and Implementations | 2 | operations |
| Crossover Health | Robyn Guillen | National Practice Director | 2 | operations |
| Crossover Health | Brady Mackey | Director of Engineering | 3 | technical-integration |
| Crossover Health | Kendra Mulvey | Vice President of Technology | 3 | technical-integration |
| Crossover Health | Maitreyi Gunye | Director of Data Science, Analytics, and Engineering | 3 | technical-integration |
| Crossover Health | Maria Popow | Director of Security | 3 | technical-integration |
| Crossover Health | Megan Stanfield | Director of IT Operations | 3 | technical-integration |
| Crossover Health | Burkie Smith | Director | 4 | referral |
| Crossover Health | Christine Wessel | Vice President, Deputy General Counsel | 4 | referral |
| Crossover Health | Elizabeth Chavez | Vice President of Account Management | 4 | referral |
| Crossover Health | Hanna Arch | Director of Capital Projects and Facilities Development | 4 | referral |
| Crossover Health | Jason M. Blote | VP, Enterprise & Capital Projects | 4 | referral |
| Crossover Health | Jeff Crichton | Senior Director of Finance | 4 | referral |
| Crossover Health | Jeff Shumer | Director, Project Management | 4 | referral |
| Crossover Health | Jessica Catelani | Director of Client Success Program | 4 | referral |
| Crossover Health | Kristoffer Dean | Senior Director of Facilities and Capital Projects | 4 | referral |
| Crossover Health | Rebecca Carbajal | Director | 4 | referral |
| Crossover Health | Ted Cancio | VP of Finance | 4 | referral |
| eMed | Alex C. | Director, Consumer Product | 1 | product |
| eMed | Linda Yaccarino | Chief Executive Officer | 1 | product |
| eMed | Dyan Hes | Chief Medical Officer | 1 | clinical |
| eMed | Duane Kingston | Vice President Operations | 1 | operations |
| eMed | Bahar Mohamadi | Product & Marketing Manager | 2 | product |
| eMed | Brittani Hahn | Delivery Director | 2 | operations |
| eMed | Eric Ebanks, Jr. | Director of Data and Analytics | 2 | operations |
| eMed | Maria Pugliese | Senior Director, Regulatory and Clinical Operations | 2 | operations |
| eMed | Phillip Whitman | Director of Pharmacy | 2 | operations |
| eMed | Ryan Adams | Pharmacist in Charge/Site Director | 2 | operations |
| eMed | Cassie Simko, CISA, CRISC | Director or Information Security | 3 | technical-integration |
| eMed | Jim Heising | Chief Technology Officer | 3 | technical-integration |
| eMed | Justin Wilson | Vice President Information Technology | 3 | technical-integration |
| eMed | Ally Wright | Director Of Business Development | 4 | referral |
| eMed | Annette Rivera | Senior Vice President Business Development | 4 | referral |
| eMed | Bryan Stokes | Director of Accounts | 4 | referral |
| eMed | Carlos Alvarez, MBA | Director of Accounts | 4 | referral |
| eMed | Chase Dujenski | Account Director | 4 | referral |
| eMed | David Isquith | Director of Client Success | 4 | referral |
| eMed | Doug Mee | Chief Financial Officer | 4 | referral |
| eMed | Eddie Maria | VP of Sales Health Plans | 4 | referral |
| eMed | Federico Castro | Vice President, Delivery & Client Success | 4 | referral |
| eMed | Gino Villani, MBA | Director | 4 | referral |
| eMed | Jason Steckler | Director, Sales Operations | 4 | referral |
| eMed | Jeremy Carr | Vice President, Enterprise Strategy | 4 | referral |
| eMed | John A. Pabich | VP, Strategic Partnerships | 4 | referral |
| eMed | Logan Sweet | Account Director | 4 | referral |
| eMed | Luis Aranguren Jr, MBA | Director, Customer Experience | 4 | referral |
| eMed | Maria Funkhouser | Head of Go To Market Business Operations | 4 | referral |
| eMed | Michael P. | Account Director | 4 | referral |
| eMed | Mike Davis | Account Director | 4 | referral |
| eMed | Missy Hunter | Vice President, Strategic Partnership Sales | 4 | referral |
| eMed | Reid Noah | Senior Vice President- Sales & Strategic Partnerships | 4 | referral |
| eMed | Robin K. | Senior Director, Client Success | 4 | referral |
| eMed | Scott Brendamour | Vice President of Sales & Strategic Partnerships | 4 | referral |
| eMed | Sheldon Allen | Vice President of Sales & Strategic Partnerships | 4 | referral |
| eMed | Sonia Ramsey | Senior Vice President, Public Sector & Channel Sales | 4 | referral |
| MDLIVE | Ali Krafft | Head of New Product Development & AI Strategy, Virtual and Emerging Care | 1 | product |
| MDLIVE | Rachel Rhodes, MPH | Head of New Product Development, AI Strategy, and Provider Experiences | 1 | product |
| MDLIVE | Jennifer Lord | Vice President Clinical and Operations | 1 | operations |
| MDLIVE | Mac Davis | Vice President Clinical Operations | 1 | operations |
| MDLIVE | Ariana Viale | Director of Product Management | 2 | product |
| MDLIVE | Asim Ilyas | Director Product Strategy | 2 | product |
| MDLIVE | Abhishek Mehra. M.D.  DFAPA | Medical Director | 2 | clinical |
| MDLIVE | Christina Chen | Medical Director of Asynchronous Care for Primary+ | 2 | clinical |
| MDLIVE | Maggie Williams | Medical Director | 2 | clinical |
| MDLIVE | Traci French | Associate Director | 2 | clinical |
| MDLIVE | Alex Soltesz | Director of Analytics | 2 | operations |
| MDLIVE | Brett Foster | Director of Member Engagement | 2 | operations |
| MDLIVE | Derek M. | Director of Implementation | 2 | operations |
| MDLIVE | Kimberly Brzezinski | Senior Director Network Operations | 2 | operations |
| MDLIVE | Sara Keyes | Director of Provider Development | 2 | operations |
| MDLIVE | Axel Hadida | Director of Platform Development | 3 | technical-integration |
| MDLIVE | Patrick Lawrence | Senior Director of Information Technology | 3 | technical-integration |
| MDLIVE | Stan Hebert | Director of Software Engineering | 3 | technical-integration |
| MDLIVE | Tony Belthrop | Chief Information Security Officer | 3 | technical-integration |
| MDLIVE | Antonio Moreno | Director of Account Management | 4 | referral |
| MDLIVE | Ayana Wong Wing, MBA | Sr. Director, Client Success | 4 | referral |
| MDLIVE | Dave Minns | Senior Director, Enterprise - West (acquisition of Bright.md Inc.) | 4 | referral |
| MDLIVE | Karen Olenski, MBA | Director, Client Success | 4 | referral |
| MDLIVE | Karen Palmer | Senior Director, Client Success MDLIVE Inc. | 4 | referral |
| MDLIVE | Kelly Serwer | Senior Director, Client Success | 4 | referral |
| MDLIVE | Michael Fernandez | Vice President, Account Management & Client Operations | 4 | referral |
| MDLIVE | Perry Ankney | Director | 4 | referral |
| MDLIVE | Rachel French | Chief Strategy and Partnerships Officer | 4 | referral |
| MDLIVE | Renee Rosica | Senior Director, Client Success | 4 | referral |
| MDLIVE | Shannon Abel, MBA | Senior Director - Sales | 4 | referral |
| MDLIVE | Sharon Heimbaugh | Sr. Director, Client Success | 4 | referral |
| MDLIVE | Shaundra Goding | Financial Analysis Director | 4 | referral |
| Wondr Health | Jeff Serrano | Chief Product & Experience Officer | 1 | product |
| Wondr Health | Scott Paddock | Council Member | 1 | product |
| Wondr Health | Lisa Talamini | Senior Vice President, Clinical Solutions | 1 | clinical |
| Wondr Health | Tim Church | Chief Medical Officer | 1 | clinical |
| Wondr Health | Annie Reed | Senior Product Manager | 2 | product |
| Wondr Health | Caitlin Dufresne | Senior Product Manager | 2 | product |
| Wondr Health | Matthew Frank | Director of Product - Platform | 2 | product |
| Wondr Health | Michael D. | Senior Director Data Analytics | 2 | operations |
| Wondr Health | Robin Patton, LMSW | Vice President, Live Services & Participant Success | 2 | operations |
| Wondr Health | Ruben Rodarte | Vice President of Operating Excellence | 2 | operations |
| Wondr Health | Cody Dufour | Sr. Director of Data Engineering | 3 | technical-integration |
| Wondr Health | Greg Shapley | SVP Information Technology & Security | 3 | technical-integration |
| Wondr Health | Greg Tracy | Chief Technology Officer | 3 | technical-integration |
| Wondr Health | Michael Mrnak | Director Software Engineering | 3 | technical-integration |
| Wondr Health | Alexander M. Schwarze | Director of Financial Planning and Analysis | 4 | referral |
| Wondr Health | Cindy Woods | Director of Cash | 4 | referral |
| Wondr Health | Deborah O'Connor | VP Health Plan Partnerships | 4 | referral |
| Wondr Health | Eric Frost | Senior Vice President of Sales | 4 | referral |
| Wondr Health | Joe Childress | Executive Producer | 4 | referral |
| Wondr Health | Kirstie van der Spuy | Creative Director | 4 | referral |
| Wondr Health | Nicolette Thaden Zelenovich | Chief Client Success Officer | 4 | referral |
| Wondr Health | Pauline Beaudoin | Director Sales Operations | 4 | referral |
| Wondr Health | Rob Sutton, CPA | Chief Financial Officer | 4 | referral |
| Goodpath | Bill Gianoukos | CEO & CoFounder | 1 | product |
| Goodpath | Jason Trees | Head of Product | 1 | product |
| Goodpath | Christelle Younes | Associate Medical Director | 2 | clinical |
| Goodpath | Nishant Uppal | Medical Director | 2 | clinical |
| Goodpath | Samantha Wu | Medical Director - Clinical Development | 2 | clinical |
| Goodpath | Joanna Gholmie | Director Of Pharmacy Services | 2 | operations |
| Goodpath | Joe Bondi | Chief Technology Officer | 3 | technical-integration |
| Goodpath | Allie Taikowski | Director of Business Operations | 4 | referral |
| Goodpath | Brett Olshan | Vice President of Sales | 4 | referral |
| Goodpath | Brian Harrigan | Senior Vice President, Sales | 4 | referral |
| Goodpath | Dustin Armitage | Vice President of Sales | 4 | referral |
| Goodpath | Patrick Wheelock | Vice President of Sales | 4 | referral |
| Goodpath | TJ Snediker, PT, DPT, TPI | Associate Director, Musculoskeletal Health | 4 | referral |
| Digbi Health | Ranjan Sinha | Founder  & CEO | 1 | product |
| Digbi Health | Sangeet Saurabh | VP Product & Engineering | 1 | product |
| Digbi Health | Dr. Garima Sharma | Chief of Care | 1 | clinical |
| Digbi Health | Varun Thakur | Associate Product Manager | 2 | product |
| Digbi Health | Madison Green | Health And Wellness Director | 2 | clinical |
| Digbi Health | Rajan Bhuyan | Leading Engineering | 3 | technical-integration |
| Digbi Health | Aksha S | Director Sales Operations | 4 | referral |
| Digbi Health | Forrest Knox | Vice President of Sales | 4 | referral |
| Digbi Health | Rob Matthews II | Senior Vice President | 4 | referral |
| Digbi Health | Sam Smith | Vice President of Sales, U.S. Enterprise/Mid-Market | 4 | referral |

## WEAK — нужно решение Вадима

| Человек | Title | Группа | Почему на грани |
|---|---|---|---|
| Joe Ennesser | Chief Operations Officer | Crossover Health | Conditional. Профиль из одной строки «Chief Operations Officer», а COO Crossover на сайте Sarah Lord, и она в этом списке (P1). Похоже на коллизию, роль не подтверждается. |
| Stephanie Anderson | Operations Executive | MDLIVE | Conditional. Компания «MDLive» набрана текстом, без страницы. Headline общий и MDLIVE не называет. Прошлая роль VP в Express Scripts (родитель MDLIVE), так что переход правдоподобен, но не подтверждён. |
| Marcia Upson | President | Wondr Health | Conditional. Одна строка «President at Naturally Slim», без страницы. От этого имени Wondr отказался в 2021, а CEO с 2022 Scott Paddock. Скорее всего, профиль устарел. |
| Elyzabeth Gonzalez | Vice President | Wondr Health | Conditional. Одна строка «Vice President at Naturally Slim», без страницы. Текущая роль в Wondr не подтверждается. |
| Candice Burgess, MSSW | Executive Vice President | Wondr Health | Conditional. Позиция привязана к странице Wondr, но вся история состоит из выпускных стажировок, что не вяжется с EVP. Роль не подтверждается. |
| Matthew Noble | Chief Medical Officer (Global Clinical Services) | eMed | Apollo, Лондон, `geo:katerina`. Роли в headline британские (Caldicott Guardian, Responsible Officer), так что это, скорее всего, британский бизнес eMed. Правила гео в карточке нет: решить, пишет ли nick (одна компания = один профиль) или человек уходит к Katerina. US-клинику eMed закрывает Dyan Hes (P1). |
| Cameron Pugh | Clinical Operations Lead | eMed | Apollo, Лондон, `geo:katerina`. Вопрос тот же, что у Noble: британская операционка eMed. |

## Кого оставили за бортом: пулы

Пулов по функции нет. Карточка даёт лейн каждой функции в девяти компаниях (standing decision 3, подтверждено 2026-10-16), так что ни одного человека с подходящей компании по функции не отсеивал. `skipped` показывает 17 человек, все senior: 7 WEAK выше и 10 FAIL по карточке.

| Пул | Людей | Кто | Предлагаемый angle | Что нужно поменять в гипотезе, чтобы их взять |
|---|---|---|---|---|
| G: гео, eMed в Лондоне | 2 | Matthew Noble (CMO, Global Clinical Services), Cameron Pugh (Clinical Operations Lead) | `clinical` (Noble), `operations` (Pugh) | Добавить правило гео: «одна компания = один профиль» (eMed целиком за nick) или роутинг британского бизнеса eMed к Katerina |
| C: conditional без подтверждения | 5 | Joe Ennesser, Stephanie Anderson, Marcia Upson, Elyzabeth Gonzalez, Candice Burgess | `operations` (Ennesser, Anderson), `referral` (три строки Naturally Slim) | Снять условие «только при подтверждённой роли» или подтвердить роль проверкой по имени вне этих файлов |
| Не предлагаю | 10 | celianny C., Clayton Martin, Seth Taylor, Stephanie Tilenius, Jose Moreno, Allan Voss, Will Wes (коллизии), дубликаты Kathryn Wintermantel, Patrick Lawrence, Elizabeth Chavez | n/a | Ничего: это OUT из карточки |

Добавить по имени (без нового раунда):

```bash
python3 scripts/outbound_pack.py promote --campaign 2026-10-16-us-employer-obesity-care \
    --names "matthew-noble-gp" --angle clinical --pool G
python3 scripts/outbound_pack.py promote --campaign 2026-10-16-us-employer-obesity-care \
    --names "cameron-pugh-b746101a2; stephanie-anderson-7a02016; joe-ennesser-335259317" --angle operations --pool C
python3 scripts/outbound_pack.py promote --campaign 2026-10-16-us-employer-obesity-care \
    --names "marcia-upson-3661b311; elyzabeth-gonzalez-4035031a; candice-burgess-mssw-53492927" --angle referral --pool C
```

## Top concerns

- **Повторный поиск вытеснения (displacement) не сделан.** Карточка: «The validator repeats it before import». У меня были только два файла и не было веба, поэтому проверку на phone-camera body scan по девяти компаниям нужно повторить до импорта.
- **Job-change check по имени не сделан.** У тонких профилей с company page карточка требует проверить по имени, не сменили ли они работу. Для этого нужен поиск вне входных файлов. Все такие люди оставлены PASS, потому что карточка считает их IN: Muhammad H., Perry Ankney, Madison Green, Cindy Woods, Burkie Smith, Rebecca Carbajal. Сюда же пустые профили, которых карточка отдельно не называла: Ally Wright, Heather Hockenberry, Jeanette Carpenter, Brady Mackey, Eric Frost. Цена ошибки: инвайт в устаревший профиль.
- **Два conditional подтвердил по собственным строкам профиля:** Kristin Grunzweig (свой headline «Director of Client Success @ Vida Health») и Robyn Guillen (текущая позиция «National Practice Director at Crossover Health», это фирменный тайтл Crossover, такой же у Jill Galvez). Если Вадиму этого мало, оба уходят в WEAK.
- **Правила гео в карточке нет.** Применил гео на уровне компании: американскую компанию ведёт nick, где бы ни сидел человек. Исключение — если человек работает в бизнесе на рынке другого профиля. Поэтому Samantha Wu (Goodpath, Лондон, `geo:katerina`), Christelle Younes (Goodpath, Монреаль) и Rajan Bhuyan (Digbi, Бенгалуру) идут как PASS: работают на американскую программу. Noble и Pugh из eMed идут в WEAK.
- **Половина списка referral (174 из 367).** Это по замыслу (лейн для каждой функции), но владельцев и лидов программ (P1+P2) 150. Message-sequencer должен держать разные вопросы для подролей referral: sales, client success, finance, partnerships.
- **137 из 367 (37%) в двух компаниях после сделок:** Included Health 96, Crossover 41. Banned terms должны держать: в копи ни слияния, ни поглощения, ни Premise, ни Firefly.
- **Имена клиентов в профилях Crossover:** Steven Watts (в тайтле аккаунт Roche and Genentech), Barry Giglio (в headline Applied Materials), Steven Chang (раньше Medical Director at Applied Materials). Карточка называет только Watts. В копи ни одного из них не называть.
- **Пробелы покрытия после Apollo:** у Digbi нет медицинского директора (Apollo не нашёл, клинику закрывает Chief of Care Garima Sharma, P1). У Goodpath нет CMO, старший клиницист Medical Director Nishant Uppal (P2).
- **Patrick Lawrence:** два профиля почти наверняка один человек. Оба в IT MDLIVE, у обоих в прошлом Director of IT в софтверной компании для ED (ProMed / veEDIS Clinical Systems). Придержан `patrick-lawrence-4550659`, как в карточке.

## Vadim — please confirm

1. Список SEND (367 человек)?
2. WEAK: кого берём? Пять conditional (Ennesser, Anderson, Upson, Gonzalez, Burgess) и два человека eMed из Лондона (Noble, Pugh), с решением по гео: nick или Katerina.
3. Пулы: пулов по функции нет. G и C выше добавляются командой `promote`, без нового раунда.
4. Кеп: ни одна группа не упёрлась в 100 (максимум Included Health, 96). Поднимать не нужно. Среди WEAK никого из Included Health нет.
5. До импорта: повторить поиск вытеснения и job-change check по 11 тонким профилям (или принять риск как есть)?
