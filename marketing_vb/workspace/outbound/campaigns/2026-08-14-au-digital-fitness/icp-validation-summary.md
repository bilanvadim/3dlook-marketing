---
product: fitxpress
campaign: 2026-08-14-au-digital-fitness
profile: vadim
step: 4-validate
date: 2026-10-02
version: 2 (QC fixes applied; v1 kept as people-validated-v1-2026-10-02.csv)
source: Apollo (151 people, 16 of 18 IN companies)
---

# ICP Validation Summary — 2026-08-14-au-digital-fitness

## Stats

Из вывода `apply-decisions` (решения в `decisions.md`, таблица в `people-validated.csv`).

**Дополнение v3 (2026-10-02, поиск Apollo по seniority для Transform by Fitaz):** Aaron McAllister («Business Owner», Брисбен, headline «Founder of Transform by Fitaz», пустой профиль) → PASS P1 product. Итого 152 человека: PASS 123 (P1 47, P2 30, P3 6, P4 40; product 34), WEAK 16, FAIL 13. Transform by Fitaz — 1 PASS, Emily Skye FIT — по-прежнему 0. Таблицы ниже — состояние v2 (151 человек), к ним добавлен он один.

| | v1 | **v2 (сейчас)** |
|---|---|---|
| Всего | 151 | 151 |
| PASS (SEND) | 125 | **122**: P1 46 · P2 30 · P3 6 · P4 40 |
| WEAK (REVIEW) | 16 | **16**: 8 в AIA (7 сверх кепа + Gerald John), 8 с сомнением в личности или в том, что человек ещё в компании |
| FAIL | 10 | **13**: 11 коллизий имён или чужих компаний, 2 ушли из AIA |
| Исключены реестром | 0 | 0 (registry check: 151 clear) |

**По группам (PASS против `cap_per_group: 50`):**

| Группа | PASS | WEAK | FAIL | Доля SEND |
|---|---|---|---|---|
| AIA Australia | **50 (= кеп)** | 8 | 2 | 41% |
| Sonder | 12 | | 3 | 10% |
| Everlab | 11 | | | 9% |
| Sweat | 8 | | 1 | 7% |
| Hapana | 7 | 1 | | 6% |
| Fernwood Fitness | 7 | 2 | | 6% |
| Digital Wellness | 5 | | | 4% |
| Kic | 5 | 1 | 4 | 4% |
| Fitstop | 5 | 3 | 2 | 4% |
| Vively | 4 | | | 3% |
| Michelle Bridges 12WBT | 2 | | | 2% |
| Xyris | 2 | | | 2% |
| 28 by Sam Wood | 1 | | | 1% |
| Defeat Diabetes | 1 | | | 1% |
| VALD | 1 | 1 | | 1% |
| Springday | 1 | | 1 | 1% |
| Emily Skye FIT, Transform by Fitaz | 0 | | | Apollo никого не нашёл |

**По лейнам (PASS):** referral 40 (P4) · product 33 (P1 22, P2 11) · retention 19 (P1 14, P2 5) · wellbeing-programs 15 (P1 8, P2 7) · partnerships 7 (P2) · technical-integration 6 (P3) · clinical 2 (P1).

**Доля referral:** до исправления 1 — 32 из 125 (26%), из них 16 в AIA. После переноса 8 продуктовиков AIA — 40 из 125 (32%). Сейчас, после всех правок — 40 из 122 (33%), из них 24 в AIA.

**AIA по лейнам (50):** referral 24 · wellbeing-programs 8 · product 6 · retention 6 · partnerships 4 · technical-integration 2.

**Флаги `geo:` (14):** на другие профили никого не переводил (правило карточки: one company = one profile). 7 PASS остаются на `vadim`: Victor Garcia (Vively, Испания), Leo Bradshaw (Everlab, Лондон), Joe Golio, Scott Penn, Anna Crook (Digital Wellness, США), Travis Shannon (Hapana, США), Nick Matthews (Sonder, Лондон). 2 WEAK: Pete Hull, Drew Cooper. 5 FAIL как коллизии: Sweat Fitness, Tony Mante, Carole King, Audrey Gutfreund, Gabor Steinbacher.

## Что изменилось после QC (17/20)

- 8 продуктовиков AIA, которые ведут страховые полисы, перенесены из `product` в `referral` P4, ранг не изменился: Penny Sheppard, Raymond Cheng, Cate Menzies, Sheraden Bulsing, Simon Layne, Nicky Serret, Aakash Malhotra, Jo Moon. Их собственная причина была «can route», а карточка запрещает underwriting-подачу.
- PASS → WEAK: Giorgia Iacono, Pete Hull и Holly Brazier. Holly — сверх списка QC, по тому же тесту «ушёл ли» (см. Top concerns).
- WEAK → FAIL как коллизии: Gabor Steinbacher, Carole King, Audrey Gutfreund.
- В топ-15 AIA Peter Kelly (#15) и A/Prof Harris (#16) поменялись местами. Gerald John получил явный ранг 37, рядом с другими P3.
- Причины переписаны так, чтобы утверждать только то, что видно в строке. Поправлены Ryan Ansell, Harris, Carl Giammarco и ещё ряд «owns ...».
- В AIA по-прежнему 50 PASS, поэтому места из списка over cap не заполнялись.

## Proposed to SEND

AIA — в порядке ранга (соответствие программе AIA Vitality и персоне wellbeing program owner из карточки). Остальные группы — по приоритету.

| Группа | Человек | Title | P | Angle |
|---|---|---|---|---|
| AIA #1 | Alison McLean | General Manager Vitality and Shared Value | 1 | wellbeing-programs |
| AIA #2 | Danielle Williams | Head of Strategy & Innovation (AIA Vitality) | 1 | wellbeing-programs |
| AIA #3 | Luke Ashby | Head of Vitality Partnerships & Distribution | 1 | wellbeing-programs |
| AIA #4 | Stephanie Phillips | Chief Marketing & Propositions Officer | 1 | wellbeing-programs |
| AIA #5 | Margaret Awrey | General Manager, AIA Health | 1 | wellbeing-programs |
| AIA #6 | Alix Davison | Marketing Manager, AIA Vitality | 2 | wellbeing-programs |
| AIA #7 | Silipa Burgess | AIA Vitality Marketing Channels Manager | 2 | wellbeing-programs |
| AIA #8 | Arley Grey | Head of Customer Marketing and Engagement | 1 | retention |
| AIA #9 | Mark Broom | Head of Customer Retention | 1 | retention |
| AIA #10 | Theresa Brancatisano | Head of Digital | 1 | product |
| AIA #11 | Jeremy Simmons | General Manager Marketing Customer Digital | 1 | product |
| AIA #12 | Katherine McAuliffe | Marketing Manager - Customer Engagement & Retention | 2 | retention |
| AIA #13 | Fiona Tsang | Health Product Manager | 2 | product |
| AIA #14 | Matt Goodison | Digital Product Manager | 2 | product |
| AIA #15 | Peter Kelly | Head of Tender & Growth Propositions | 1 | product |
| | | **--- граница топ-15 (рекомендация июльского post-mortem, Open question 7) ---** | | |
| AIA #16 | A/Prof Harris | Chief Medical Officer | 2 | wellbeing-programs |
| AIA #17 | Sujan Yamunarajan | Executive General Manager Growth | 1 | retention |
| AIA #18 | Rochelle Evans | Head of Group & Retail Marketing | 1 | retention |
| AIA #19 | Craig Parker | General Manager, Retail Distribution & Retention | 1 | retention |
| AIA #20 | Chris Healey | Chief Executive - Group Insurance Officer | 1 | product |
| AIA #21 | Benjamin Martin | Head of Strategic Partnerships | 2 | partnerships |
| AIA #22 | Jordan Beasley | Head of Strategy & CEO Office | 4 | referral |
| AIA #23 | Penny Sheppard | Head of Retail Product | 4 | referral |
| AIA #24 | Marie Huong | General Manager Data Governance & Business Insights | 3 | technical-integration |
| AIA #25 | Raymond Cheng | Senior Product Manager | 4 | referral |
| AIA #26 | Cate Menzies | Senior Product Manager | 4 | referral |
| AIA #27 | Dave Evans | Head of Propositions & Direct Partnerships | 2 | partnerships |
| AIA #28 | Wanda Britton | General Manager Partnerships | 2 | partnerships |
| AIA #29 | Swapnil Kamankar | Regional Manager, Partnerships International Health | 2 | partnerships |
| AIA #30 | Tristan Oam | Senior Manager, Partnerships and General Advice | 4 | referral |
| AIA #31 | Kim Clough | GM Life Product and Pricing | 4 | referral |
| AIA #32 | Sheraden Bulsing | Product Manager | 4 | referral |
| AIA #33 | Simon Layne | Product Manager | 4 | referral |
| AIA #34 | Nicky Serret | National Product Manager - Group Insurance | 4 | referral |
| AIA #35 | Aakash Malhotra | Product Manager | 4 | referral |
| AIA #36 | Jo Moon | Product Manager | 4 | referral |
| AIA #37 | *Gerald John (WEAK, личность)* | *CTO* | *3* | *technical-integration* |
| AIA #38 | David O'Driscoll | Head of IT Strategy and Business Partnerships | 3 | technical-integration |
| AIA #39 | Alan Caputo | General Manager; Distribution (Advice, Banca, Health & AIA FW Marketing) | 4 | referral |
| AIA #40 | Paige Mathews | Marketing Manager | 4 | referral |
| AIA #41 | Phillip Klobucki | Marketing and Communications Manager | 4 | referral |
| AIA #42 | Karen Purcell | Head of New Business Development | 4 | referral |
| AIA #43 | George Stavliotis | General Manager Partnerships | 4 | referral |
| AIA #44 | Elke Reinstadler | Head of Group Partnerships | 4 | referral |
| AIA #45 | Trish Curry | General Manager Industry Funds and Government Partners | 4 | referral |
| AIA #46 | Vaibhav Sharma | Head of Master Trust Partnerships | 4 | referral |
| AIA #47 | Tim Billington | Business Delivery Manager - Propositions & Direct Partnerships | 4 | referral |
| AIA #48 | Sally Barnett | Senior Manager, Internal Communications & Strategy, CEO Office | 4 | referral |
| AIA #49 | Chris Freeman | Head of New Business Product and Pricing | 4 | referral |
| AIA #50 | Michelle Bennie | Head of Legal, Product and Partnerships | 4 | referral |
| AIA #51 | Tracey Crowe | Chief Customer Operations and Claims Officer | 4 | referral |
| | | **--- кеп: 50 PASS = ранги 1-51 без Gerald John; ранги 52-58 в WEAK «over cap». Если Gerald John подтвердится, в over cap уходит ранг 51 ---** | | |
| Everlab | Steven Lu | Cofounder, CMO | 1 | clinical |
| Everlab | Sam Kothari | Cofounder | 1 | product |
| Everlab | Marc Hermann | Founder | 1 | product |
| Everlab | Leo Bradshaw | General Manager, UK | 1 | product |
| Everlab | Dec Kickham | Product | 1 | product |
| Everlab | Matthew Kwong | Product Manager | 2 | product |
| Everlab | Khanh Nguyen | Product Manager | 2 | product |
| Everlab | Sharif Alvis | Head of Engineering | 3 | technical-integration |
| Everlab | Michael Reid | Founding Engineer | 3 | technical-integration |
| Everlab | Halla Dadouch | Corporate Lead & Founding AE - SME & Mid-Market | 4 | referral |
| Everlab | Jo Power | Marketing Manager | 4 | referral |
| Sonder | Craig Cowdrey | Co-founder & CEO | 1 | wellbeing-programs |
| Sonder | Nick Matthews | VP and General Manager UK | 1 | wellbeing-programs |
| Sonder | Kimi Powell | Director of Clinical Services | 1 | wellbeing-programs |
| Sonder | Jing Guo | Head of Product Design | 2 | wellbeing-programs |
| Sonder | Nemo Hu | Product Manager | 2 | wellbeing-programs |
| Sonder | Lena Morrison | Group Product Manager | 2 | wellbeing-programs |
| Sonder | Michael Conroy | Group Product Manager | 2 | wellbeing-programs |
| Sonder | Aimie Smith | Marketing | 4 | referral |
| Sonder | Duyen Nguyen | Marketing | 4 | referral |
| Sonder | Michaela Pigott | Customer Marketing Manager | 4 | referral |
| Sonder | David Badet | Manager, Growth Marketing | 4 | referral |
| Sonder | Robert Chasse | Education Partnerships | 4 | referral |
| Sweat | Adam Koch | Chief Executive Officer | 1 | product |
| Sweat | Chris Torcasio | Head of Product | 1 | product |
| Sweat | Steven Dent | Head of Marketing, Content and Partnerships | 1 | retention |
| Sweat | Sarah Macdougall | Head of Performance Marketing | 1 | retention |
| Sweat | Claudia Impedovo | Head of Go to Market (Marketing) | 1 | retention |
| Sweat | Becky Wallis | App Product Manager | 2 | product |
| Sweat | Jack Tuckerman | Senior Product Manager | 2 | product |
| Sweat | Rachel Murray | Affiliate Marketing Lead | 4 | referral |
| Hapana | Jarron Aizen | CEO & Founder | 1 | product |
| Hapana | Alan Sacharowitz | Chief Operating Officer | 1 | product |
| Hapana | Lakshmi Koppula | Head of Product | 1 | product |
| Hapana | Milena Zanini | Head of Marketing | 1 | retention |
| Hapana | Gopal Agrawal | Director of Product Operations | 2 | product |
| Hapana | Travis Shannon | Chief Technology Officer | 3 | technical-integration |
| Hapana | Rajan Csm | Product Test Manager | 4 | referral |
| Fernwood Fitness | Belinda Wheaton (Amis) | CEO | 1 | product |
| Fernwood Fitness | Elle Chai | CRM and Digital Marketing Manager | 2 | retention |
| Fernwood Fitness | Bianca Clements | Marketing Lead | 2 | retention |
| Fernwood Fitness | Kitty Robinson | Digital Content + Community Manager | 2 | retention |
| Fernwood Fitness | Ella Wheeler | National Campaign & Local Area Marketing Manager | 4 | referral |
| Fernwood Fitness | Ashleigh J | Sales & Marketing | 4 | referral |
| Fernwood Fitness | Zoe Kirby | Fernwood Morayfield | 4 | referral |
| Digital Wellness | Scott Penn | Global CEO | 1 | product |
| Digital Wellness | Joe Golio | Chief Operating Officer - US | 1 | product |
| Digital Wellness | Anna Crook | Director of Product Development | 1 | product |
| Digital Wellness | Claire Stephenson | Head of Partnerships | 2 | partnerships |
| Digital Wellness | Claire Brinkley | Performance Marketing Manager | 4 | referral |
| Kic | Steph Smith | Co-Founder | 1 | product |
| Kic | Laura Henshaw | Co-Founder | 1 | product |
| Kic | Natalie O'Heare | Head of Marketing | 1 | retention |
| Kic | Tom Grimshaw | Senior Product Manager | 2 | product |
| Kic | Tess Drobik | Marketing | 4 | referral |
| Fitstop | Carl Giammarco | Global Head of Growth | 1 | retention |
| Fitstop | Ryan Ansell | Head of Brand & Marketing | 1 | retention |
| Fitstop | Riley Woodcock | General Manager | 2 | retention |
| Fitstop | Olivia Houston | Managing Owner | 4 | referral |
| Fitstop | Sally Kubler | Head Coach | 4 | referral |
| Vively | Tim Veron | Founder | 1 | product |
| Vively | Michelle Woolhouse | Founding Medical Director: Vively Health | 1 | clinical |
| Vively | Kat Kawecki | Product Manager | 2 | product |
| Vively | Victor Garcia | Head of Engineering | 3 | technical-integration |
| Michelle Bridges 12WBT | Stephanie Clark | Head of Member Experience | 1 | retention |
| Michelle Bridges 12WBT | Jane Weston | Head of Corporate Partnerships | 2 | partnerships |
| Xyris | Declan Goodsell | CEO & Managing Director | 1 | product |
| Xyris | Shian Jordan | Product Manager | 2 | product |
| 28 by Sam Wood | Jess Darvell | Head of Growth Marketing | 1 | retention |
| Defeat Diabetes | Zoe Eaton | Chief Executive Officer | 1 | product |
| VALD | Kieran Harrison | Product | 2 | partnerships |
| Springday | Sarah Cahill | Product Manager | 2 | product |

## WEAK — нужно решение Вадима

Тир из карточки сохранён в `decisions.md` (в `people-validated.csv` скрипт оставляет `priority` у WEAK пустым).

| Человек | Title | Группа | Тир | Почему на грани |
|---|---|---|---|---|
| Gerald John | CTO | AIA Australia | P3 technical-integration | ранг 37 (внутри кепа): title CTO не вяжется с единственной ролью в записи (Account Manager в MLC Life). Если подтвердится, ранг 51 (Tracey Crowe) уходит в over cap |
| John Micallef | General Manager, Legal | AIA Australia | P4 referral | over cap, ранг 52 |
| Edmund Wong | Head of Risk - Marketing and Propositions | AIA Australia | P4 referral | over cap, ранг 53 |
| John Giannikos | Technical Product Training Manager | AIA Australia | P4 referral | over cap, ранг 54 |
| Justin Ca | Head of Risk, General Manager | AIA Australia | P4 referral | over cap, ранг 55 |
| Leigh Kobus | Head of Business Partnering Savings and Investments | AIA Australia | P4 referral | over cap, ранг 56 (group finance) |
| Paul Trigg | Claims and Reinsurance Consultant, Office of the CEO | AIA Australia | P4 referral | over cap, ранг 57 (claims) |
| David Shuvalov | General Manager, Reinsurance | AIA Australia | P4 referral | over cap, ранг 58 (reinsurance) |
| Pete Hull | CEO | Fitstop | P1 product | имя совпадает с founder-CEO из карточки, но запись — пустая заглушка из США без ролей, а Fitstop по карточке в Брисбене: сначала проверить URL профиля |
| Keiichi Niinuma | Managing Director | Kic | P1 product | пустой профиль, а CEO Kic по карточке — Jane Martino; локация Австралия, поэтому не FAIL |
| Holly Brazier | Product Manager | Hapana | P2 product | headline и обе прошлые роли — PadelWithHolly и JPMorgan, ничто, кроме title из Apollo, не связывает её с Hapana |
| Drew Cooper | Founder | VALD | P2 partnerships | роль в VALD в записи прошлая (PM ForceDecks), headline «Coach»: вероятно, ушёл |
| Giorgia Iacono | Digital Content and Community Manager | Fernwood Fitness | P2 retention | headline и обе прошлые роли — её собственные бизнесы (Market Me By G, макияж), с Fernwood её связывает только title |
| Erica Graham | Sales and Marketing Manager | Fernwood Fitness | P4 referral | headline «Founder and CEO of Dirty Mullet»; роль в Fernwood в записи стоит за более поздней ролью в TMJ Clinics |
| Jolyn Lee | Co-Owner & Head of Marketing | Fitstop | P4 referral | студия в Сингапуре; франшизы Fitstop в Сингапуре в карточке нет |
| Sharon Yeap | Head Coach | Fitstop | P4 referral | Сингапур, ex F45; франшизы Fitstop в Сингапуре в карточке нет |

## Кого оставили за бортом: пулы

Каждая функция в IN-компаниях получила лейн (стоящее решение 3), поэтому функциональных пулов нет. Не в рассылке 29 человек: 16 WEAK выше и 13 FAIL. В каждом пуле из `skipped` есть старшие роли. Промоутить можно только WEAK:

| Пул (`skipped`) | Людей | Кто (можно взять) | Предлагаемый angle | Что нужно поменять, чтобы их взять |
|---|---|---|---|---|
| executives (no function) | 13 (4 WEAK, 9 FAIL) | Pete Hull (Fitstop) · Keiichi Niinuma (Kic) · Drew Cooper (VALD) · David Shuvalov (AIA) | product (Hull, Niinuma), partnerships (Cooper), referral (Shuvalov) | Hull, Niinuma, Cooper: проверить профиль на LinkedIn. Shuvalov: кеп AIA ≥ 57 |
| marketing / UA / content | 4 (3 WEAK, 1 FAIL) | Giorgia Iacono, Erica Graham (Fernwood) · Jolyn Lee (Fitstop SG) | retention (Iacono), referral | подтвердить, что работают в Fernwood; что студия в Сингапуре — франшиза Fitstop |
| other | 4 (1 WEAK, 3 FAIL) | Leigh Kobus (AIA) | referral | кеп AIA |
| finance / legal | 3 WEAK | John Micallef, Edmund Wong, Justin Ca (AIA) | referral | кеп AIA ≥ 53 (ранги 52, 53, 55) или снять кого-то из рангов 22-51 |
| product | 2 WEAK (1 senior) | Holly Brazier (Hapana) · John Giannikos (AIA) | product · referral | подтвердить, что Holly в Hapana · кеп AIA |
| engineering / ML | 1 WEAK | Gerald John (AIA CTO) | technical-integration | проверка личности (ранг внутри кепа) |
| HR / office / support | 1 WEAK | Paul Trigg (AIA) | referral | кеп AIA |
| clinical / coaching | 1 WEAK | Sharon Yeap (Fitstop SG) | referral | франшиза Fitstop в Сингапуре |

Добавление по имени, без нового раунда:
`python3 scripts/outbound_pack.py promote --campaign 2026-08-14-au-digital-fitness --names "Имя Фамилия; person_id" --angle referral --pool X`

**FAIL (13), промоутить нельзя:**

| Человек | Группа | Причина |
|---|---|---|
| Greg Ballard | AIA Australia | ушёл: headline «open to fresh opportunities» |
| Sandra Gallagher | AIA Australia | ушла: title «Exploring new Opportunities» |
| Sweat Fitness | Sweat | коллизия: страница филадельфийского зала, не человек |
| Nilesh Patel | Kic | коллизия: «CEO» в Индии, а по карточке CEO Kic — Jane Martino |
| Tony Mante | Kic | коллизия: KIC Holdings Inc (США) |
| Carole King | Kic | коллизия: пустой профиль, «General Manager» в Калифорнии, тот же паттерн, что у KIC Holdings |
| Audrey Gutfreund | Kic | коллизия: пустой профиль, «Program Director» в Массачусетсе |
| Carlos Sumner | Fitstop | коллизия: «CEO» в Монголии, пустой профиль |
| Ana Chagas | Fitstop | другой бизнес: FitStop Personal Training Studio, Бразилия |
| Gabor Steinbacher | Springday | коллизия: вся запись — венгерская сеть залов Oxygen Wellness |
| Manav Desai | Sonder | коллизия: data scientist в Индии, «co-founder» другого Sonder |
| Clyzel Peralta | Sonder | коллизия: фрилансер media buyer, Филиппины |
| Neel Parekh | Sonder | коллизия: пустой профиль, Индия |

## Top concerns

- **AIA — 41% рассылки (50 из 122), и 24 из них referral.** Июльский post-mortem советовал не больше 15 человек на страховщика. Граница топ-15 проходит после Peter Kelly (ранг 15): 7 wellbeing-programs (Vitality и AIA Health), 3 retention, 5 product/digital. A/Prof Harris (CMO, в записи нет роли в AIA, это сторона медицинских рисков) — ранг 16. Решает Open question 7.
- **Доля referral выросла с 26% до 33%.** Было 32 из 125, после переноса 8 продуктовиков AIA, которые ведут страховые полисы, — 40 из 125 (32%), после всех правок — 40 из 122. 24 из 40 приходятся на AIA. Это честная цифра: этим людям нельзя слать build-versus-buy про API/SDK.
- **Sonder — самое слабое попадание по карточке («Weakest feature fit, kept as approved»), но вторая по размеру группа: 12 PASS, 10% рассылки.** 7 из них wellbeing-programs, 5 referral (B2B-маркетинг и продажи в образование). Если сократить Sonder до CEO, клинического директора, GM UK и продуктовиков, уйдёт 5 referral.
- **Один тест на каждый сигнал, применён к каждой строке:**
  - **Коллизия → FAIL:** нет ничего, что связывает человека с компанией, кроме title из Apollo, и при этом пустой профиль или чужая карьера плюс локация вне рынков компании либо title, противоречащий лидеру из карточки. Так прошли Carlos Sumner, Neel Parekh, Carole King, Audrey Gutfreund, Gabor Steinbacher.
  - **Сомнение в личности → WEAK:** что-то связывает или локация совпадает (Pete Hull, Keiichi Niinuma, Gerald John, Drew Cooper).
  - **Возможно ушёл → WEAK:** headline называет собственный бизнес, а компанию подтверждает только title из Apollo. Это Giorgia Iacono, Erica Graham и Holly Brazier.
  - **Пустой профиль с подходящей австралийской локацией и непротиворечивым title → PASS:** Kat Kawecki, Declan Goodsell, Zoe Kirby, Robert Chasse.
- **Коллизии имён Apollo.** Общие названия (Kic/KIC, Sonder, Sweat, Fitstop/FitStop, Springday) дали 11 FAIL-коллизий. Apollo сопоставляет по компании, которую человек указал сам.
- **Тонкие группы и пропуски.** У 28 by Sam Wood, Defeat Diabetes, VALD и Springday по одному PASS. Владельца партнёрств нет в Hapana (в персоне карточки он идёт первым), VALD и Springday. В Springday нет и владельца wellbeing-программы. Клинический лейн есть только в Vively и Everlab. CEO Kic Jane Martino и Kayla Itsines (Sweat) в выгрузку не попали. CEO-слот Fitstop ждёт проверки Pete Hull. Emily Skye FIT и Transform by Fitaz — 0 человек.
- **Решения на суждении:**
  - Steven Lu (Everlab, «Cofounder, CMO», Dr) → clinical: CMO прочитан как chief medical officer.
  - Stephanie Phillips (AIA CMO) → wellbeing-programs: прошлая роль — Chief Shared Value and Marketing Officer.
  - Riley Woodcock (Fitstop GM) → retention P2: в headline франшизный мульти-сайт.
  - Sonder целиком → wellbeing-programs (лейн компании в карточке), B2B-маркетинг → referral.
  - Kieran Harrison (VALD, product) → partnerships (лейн компании в карточке).
  - Chris Healey (Chief Executive Group Insurance) оставлен в product P1. Это пограничный случай по той же логике, что и страховой продукт.
- **Ограничения для копирайта:** у 5 PASS в Kic действует правило подачи (Open question 8). Fitstop работает на Hapana — одному про другого не писать. У Sweat, Everlab, Fernwood и AIA уже есть фото или измерения: подавать «как», не «что».
- **Люди вне Австралии без `geo:`-флага** (Индия, Сингапур — рынков без профиля): Gopal Agrawal (headline подтверждает Hapana) и Rajan Csm (Hapana) в PASS. Jolyn Lee и Sharon Yeap — WEAK.

## Vadim — please confirm

**А. Валідація**

1. Список SEND — 122 людини (P1 46, P2 30, P3 6, P4 40) одним файлом імпорту, без хвиль. Підтверджуєш?
2. WEAK (16): кого беремо? 7 людей в AIA понад кеп (ранги 52-58, усі referral P4) і Gerald John (ранг 37, якщо підтвердиться особа). Ще 8 — із сумнівом в особі або в тому, що людина ще в компанії: Pete Hull, Keiichi Niinuma, Holly Brazier, Drew Cooper, Giorgia Iacono, Erica Graham, Jolyn Lee, Sharon Yeap.
3. Пули: які беремо? Функціональних пулів немає (кожна функція має лейн); усі 16 WEAK додаються командою promote, без нового раунду. 13 FAIL — колізії й ті, хто пішов, їх не беремо.
4. Кепи: AIA впирається в 50 (знайдено 60, 2 FAIL, 8 WEAK). Лишаємо 50, піднімаємо або знижуємо до 15 (див. відкрите питання 7)? І Sonder: лишаємо 12 чи прибираємо 5 referral, бо це найслабше попадання в картці?

**Б. Відкриті питання гіпотези (номер і текст із картки)**

1. **B2B-платформи в цій кампанії** (Hapana, VALD і лейн partnerships у Digital Wellness та Springday)? За замовчуванням: так, лейн `partnerships`, той самий файл імпорту. (Збережено з 2026-08-17; Catapult і dorsaVi відтоді вийшли зі списку.) *Зараз у SEND: Hapana 7 (власника партнерств немає), VALD 1, partnerships у Digital Wellness 1, у Springday партнерського власника немає.*
2. **Конфлікт каналів із липневими акаунтами медичних фондів** (AIA Australia, Springday, Sonder; серед клієнтів Sonder є медичний фонд, а у Vively є венчурний інвестор медичного фонду)? За замовчуванням: конфлікту немає, надсилаємо й ніколи не називаємо фонди. (Збережено з 2026-08-17.)
3. **Eucalyptus — до `nick` разом із Hims & Hers?** За замовчуванням: тут OUT і не реєструється на `vadim`; `nick` може взяти Hims & Hers, включно з його міжнародним підрозділом, яким керують із Сіднея, у US-кампанії.
4. **Catapult — до `nick`?** За замовчуванням: тут OUT; його власний fact sheet називає головним офісом Бостон, хоча компанія котирується на ASX і заснована в Мельбурні.
5. **Sleepfit, HELD через неактивність.** За замовчуванням: не надсилаємо, не реєструємо; відпускаємо, лише якщо Apollo покаже чинних керівників і ти захочеш його взяти.
6. **Compliance-рядок в AU cold copy.** (a) без compliance-рядка; (b) похідне речення «We encrypt data in transit and at rest, and delete photos after processing or within 30 days.» (US-рядок `compliance.md` §9 без HIPAA-частини, сьогодні його в `compliance.md` немає); (c) щось інше, наприклад погоджене юристами речення про Australian Privacy Act / APP. **За замовчуванням: (a), без compliance-рядка в AU cold copy, доки не відповіси.** Питання про австралійську приватність у відповідях — на legal@3dlook.me з посиланням на FAQ.
7. **Обсяг AIA Australia.** Apollo знайшов в AIA 60 людей, це понад кеп. За замовчуванням: кеп 50 (постійне рішення), валідатор ранжує 60, топ-50 ідуть. Липневий post-mortem радив не більше 15 людей на страховика, через названих власників. Знижуємо кеп для AIA? *Межа топ-15 — після Peter Kelly (ранг 15): 7 wellbeing-programs, 3 retention, 5 product.*
8. **Відповідність бренду Kic.** За замовчуванням: IN із правилом подачі (сила, вибір учасниці, без ваги й зовнішності). *У SEND 5 людей із Kic.*
9. **Який профіль володіє The Fast 800?** Companies House показує британську операційну компанію (Healthlab Online Limited, Witney), Apollo ставить штаб-квартиру в Marlow, а CEO — у Лондоні; Dealroom каже Perth, і двоє директорів живуть в Австралії. За замовчуванням: HELD, не надсилаємо й не реєструємо на `vadim`; якщо скажеш `katerina`, компанія переходить в OUT і до її UK-списку; якщо `vadim`, її відпускають в IN з 5 людьми з Apollo. *Цих 5 людей у поточному списку немає: promote їх не додасть, потрібне окреме довантаження.*
10. **Аудит твого LinkedIn-профілю** (головна гіпотеза липневого post-mortem щодо 17,3% acceptance). За замовчуванням: не зроблено, ризик прийнято, надсилаємо як є.
