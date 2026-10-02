---
campaign: 2026-10-02-us-virta-health
product: fitxpress
profile: nick
step: 4 (validate)
date: 2026-10-02
inputs: card-validate.md (hypothesis 8d5710479b811dba), people-compact.csv (68 rows: 38 Sales Navigator + 30 Apollo)
---

# ICP Validation Summary — 2026-10-02-us-virta-health

## Stats

Combined result from `apply-decisions` after the Apollo top-up (68 people in `people-compact.csv`: 38 from Sales Navigator, 30 from Apollo):

| | Combined | Round 1 (Sales Navigator, 38) | Round 2 (Apollo, 30) |
|---|---|---|---|
| PASS | 50 (P1: 9 · P2: 10 · P3: 4 · P4: 27) | 37 | 13 |
| WEAK | 14 | 0 | 14 |
| FAIL | 4 | 1 (Julia Julia) | 3 (Jamie Anderson, Wael Asano, Lola Morris) |
| Excluded by registry | 0 | 0 | 0 |
| To send | 50 | 37 | 13 |

No `registry:` flag on any of the 68 compact rows (round 1 registry check: 38 clear).

Distribution against the cap:

| Group | To send | cap_per_group | Status |
|---|---|---|---|
| Virta Health | 50 | 50 | at the cap; 6 of the 14 WEAK wait only on the cap |

Angle breakdown (50 PASS):

| Angle | People | Tiers |
|---|---|---|
| product | 5 | P1 ×4, P2 ×1 |
| clinical | 5 | P1 ×2, P2 ×3 |
| operations | 9 | P1 ×3, P2 ×6 |
| technical-integration | 4 | P3 ×4 |
| referral | 27 | P4 ×27 |

`wave` = 1 for everyone (no waves since 2026-09-29). Tiers only order the list; all 50 go in one import file. Round 1: the two former staff (Travis W., Everlaw; Jason Rebacz, LaborFirst) were dropped upstream and are not in this list, so the card's 37 + 3 = 40 reconciles as 37 PASS + 1 FAIL here + 2 dropped before step 4.

## Proposed to SEND

| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Virta Health | Dan Hang | Chief Product Officer | 1 | product |
| Virta Health | Liza Fryberger | Director of Product, Care Delivery | 1 | product |
| Virta Health | Kathryn Geskermann | Director of Product, Member Experience | 1 | product |
| Virta Health | Adam Wolfberg, MD, MPH | Chief Medical Officer | 1 | clinical |
| Virta Health | Kristin Bergethon | Associate Chief Medical Officer | 1 | clinical |
| Virta Health | Melissa Rondi | Senior Vice President Operations | 1 | operations |
| Virta Health | Rad Thie | Senior Director (Product Strategy & Positioning) | 2 | product |
| Virta Health | Caroline Roberts, MD | Medical Director of Research | 2 | clinical |
| Virta Health | Jeff Stanley, MD | Medical Director | 2 | clinical |
| Virta Health | Stephanie Drullinger, MSN, RN | Director of Nursing | 2 | clinical |
| Virta Health | Castle Hazzard | Director of Clinical Operations | 2 | operations |
| Virta Health | Holly Anderson, RD | Director, Enrollment Operations | 2 | operations |
| Virta Health | Adriana Lindsey, BSN, RN | Associate Director (leads Enrollment Nurses, per card) | 2 | operations |
| Virta Health | Shaila Chhibba | Senior Director, Implementation | 2 | operations |
| Virta Health | Karthik Prasad | Director of Engineering | 3 | technical-integration |
| Virta Health | Eric Paxton | Director of Engineering | 3 | technical-integration |
| Virta Health | Kristen Larson | VP Strategy and Business Development | 4 | referral |
| Virta Health | Leana Balasco | Vice President of Commercial Operations | 4 | referral |
| Virta Health | Amy Mengyun Zhang | Director of Actuarial Strategy | 4 | referral |
| Virta Health | Candi Buell | Associate Director of Client Success | 4 | referral |
| Virta Health | Andre Burkholder | Senior Director, Consultant Relations and Partnerships | 4 | referral |
| Virta Health | Emily (Summerville) Elter | Director, Partnerships | 4 | referral |
| Virta Health | Patrick Tumpane | ASO Partner Growth | 4 | referral |
| Virta Health | Tara Conboy | Solutions Architect | 4 | referral |
| Virta Health | Ryan Andrews | Head of Public Sector | 4 | referral |
| Virta Health | Danielle Ritter | Director of Sales, Public Sector | 4 | referral |
| Virta Health | Jack Rose | National Sales Director, Health Systems | 4 | referral |
| Virta Health | Jared Maruji | Director of Sales | 4 | referral |
| Virta Health | Taylor P. | Director of Sales | 4 | referral |
| Virta Health | Manu Diwakar | Chief Financial Officer | 4 | referral |
| Virta Health | Roger Kumar | SVP, Strategic Finance & IR | 4 | referral |
| Virta Health | Andrew Chen | Senior Director, Strategic Finance | 4 | referral |
| Virta Health | Alex Choi | Strategic Finance Director | 4 | referral |
| Virta Health | Sam Berklacich | Director, Strategic Finance | 4 | referral |
| Virta Health | Judy Huang | VP of Communications | 4 | referral |
| Virta Health | Dani LaSalvia | Director, Internal Communications | 4 | referral |
| Virta Health | Alexander (Xander) Jones, CPA | Director of Tax | 4 | referral |
| Virta Health | Sami Inkinen | CEO & Founder | 1 | product |
| Virta Health | Amit Shah | President | 1 | operations |
| Virta Health | Naomi Kincler | VP Care Operations and Content | 1 | operations |
| Virta Health | Colin Daw | VP of Growth | 2 | operations |
| Virta Health | Jennifer Arensdorf | Head of Clinical Quality and Training | 2 | operations |
| Virta Health | Neha Shevade | VP of Engineering | 3 | technical-integration |
| Virta Health | Christine Vonderach | VP Information Technology and Security | 3 | technical-integration |
| Virta Health | Laura Walmsley | Chief Commercial Officer (CCO) | 4 | referral |
| Virta Health | Kristen Weeks | Head of Customer Success and Partnerships | 4 | referral |
| Virta Health | Lindsay Johnson | Head of Partnerships With Unions, Labor and Trusts | 4 | referral |
| Virta Health | Jason Lee | Chief of Staff and Head of Commercial Ops | 4 | referral |
| Virta Health | Shravya Gupta | VP & Chief of Staff to COO | 4 | referral |
| Virta Health | Ryann Donohue | Vice President Marketing | 4 | referral |

P4 order follows the card: commercial and partnerships, then sales, finance, communications, tax last. The 13 rows after the Director of Tax are round 2 (Apollo).

## WEAK — нужно решение Вадима

Round 1: none. Every compact row matches the card's people table: all 38 rows sit on the Virta Health group, no row carries an `empty-profile`, `other-company-page` or `geo` flag, and no row shows a different current employer or a departure.

Round 2 (Apollo): 14 WEAK, listed in the "Apollo top-up" section below.

## FAIL

| Человек | Title | Группа | Reason |
|---|---|---|---|
| Julia Julia | Founder & Director of Probiotic Research | Virta Health (page only) | Identity collision. Compact row: headline "Head of Product R&D", no earlier roles, no Virta role of any kind. Virta's founders are Inkinen, Phinney and Volek, and nothing on Virta's site mentions probiotic research (card). FAIL, not referral. |

## Кого оставили за бортом: пулы

| Пул | Людей | Кто | Предлагаемый angle | Что нужно поменять в гипотезе, чтобы их взять |
|---|---|---|---|---|
| (none) | 0 promotable | `skipped` lists one person, Julia Julia, under "analytics / data / BI, senior". That is the identity collision above, not a pool: there is no Virta role to promote. | n/a | Nothing. Vadim takes every pool, and every other function in the export already has a lane. |

The people Vadim might want and does not have are outside the export, not skipped inside it (see Top concerns, first item, and question 5).

## Top concerns

- **Company export, not title export: no top owners above the directors.** The export has no CEO, President, CTO or VP Engineering, no VP or Head of Product beyond the CPO, no head of research (the *Obesity* paper's Virta author, Athinarayanan, is not in the list) and no member-experience or clinical-operations VP (card). P1 is six people; 21 of 37 (57%) go in the referral lane. The card's top-up title list (Open question 1) is the fix.
- **Displacement re-check.** The card says "The validator repeats the scan and vendor check before import (anti-case: displacement)." This step was limited to the card and the compact list, so the validator did not run it. The coordinator ran it on 2026-10-02 (note below the confirm list): no phone-camera body scan, body-composition device or scanning vendor found, not displacement.
- **Former employers: the card and the compact rows disagree for six people.** Current employer agrees (Virta) on all six, so each keeps the card's tier and lane. The coordinator is reconciling these in the hypothesis before messages. Former employers may be named in copy (decision 5), so until then message-sequencer names only an employer that is on the person's row.
  - Liza Fryberger: card says ex-Head of Product, Care System at Cityblock Health; row shows Product Consulting and Advising (self-employed) and Principal Product Manager at Pair Team.
  - Kristin Bergethon: card says ex-CMO at Physician Housecalls and Director of Product and Strategy at Novocardia; row shows Advisor, Regional Medical Director at Ennoble Care.
  - Shaila Chhibba: card says ex-payor contracting at HealthCare Partners; row shows only Implementation at Virta Health, Director.
  - Melissa Rondi: card says ex-ClassPass and Deloitte; row shows Senior Financial Planning & Analysis Manager at ClassPass and a truncated Business Development & Operations role, no Deloitte.
  - Tara Conboy: card cites a Skedulo, Castlight and Limeade history; row shows only Director, Solution Consulting at Skedulo.
  - Adam Wolfberg: card says ex-CMO at Current Health and Ovia Health; row shows Chief Medical Officer at Current Health and Physician-in-Chief at Ovia Health.
- **Adriana Lindsey rests on her bio.** Her compact title is only "Associate Director" and the compact row has no headline or bio; the card places her as the lead of Virta's Enrollment Nurses from her bio. Not a contradiction, so PASS P2 `operations` as the card gives it.
- **Flags missed the collision.** Julia Julia's `flags` cell is empty: the Virta company page on her row passed the `other-company-page` check. Caught by headline and the card, as the card expected.
- **Script hint is stale.** `skipped` prints a `promote ... --wave 2` example; there are no waves since 2026-09-29. Any promote for this campaign should not pass `--wave 2`.

## Vadim — please confirm

1. Список SEND: 37 людей, Virta Health, P1 6 · P2 8 · P3 2 · P4 21, усі в одному import-файлі?
2. WEAK: немає жодного (0). Підтверди, що вирішувати нічого.
3. Пули: брати нічого. Єдина, хто не йде в розсилку, Julia Julia, це колізія імен, а не пул.
4. Кеп: 37 із 50, група в кеп не вперлася, піднімати не треба.
5. **Відкрите питання 1 гіпотези, top-up pull:** запускаємо опціональний top-up у Sales Navigator всередині Virta Health за списком тайтлів із картки (CEO, President, CTO, VP / Head of Engineering, VP / Head of Product, Group і Principal PM, VP / Head of Clinical Operations, VP / Director of Research, Head of Data Science, VP / Head of Member Experience), щоб закрити відсутніх CEO, CTO, VP продукту, керівника досліджень і VP member experience або clinical operations? Нові люди йдуть через `check` → `compact` → validate, а не через `promote`.
6. **Відкрите питання 2 гіпотези, Julia Julia:** підтверди FAIL як колізію імен, а не referral. У її compact-рядку немає жодної ролі у Virta.
7. **Відкрите питання 3 гіпотези, Tara Conboy:** підтверди `referral` для Solutions Architect, а не `technical-integration`. Це pre-sales solution consulting: headline «Experienced Solution Consultant» і попередня роль Director, Solution Consulting у Skedulo. Стоїть як P4 `referral`.
8. Повторна перевірка на displacement (anti-case з картки): координатор зробив її 2026-10-02 (нотатка нижче), displacement немає. Підтверди, що імпорт іде без паузи.

**Coordinator: displacement re-check done 2026-10-02 (the validator has no web).** Virta's help center (BodyTrace / Virta Scale: weight over a cellular connection), its New Member FAQ, Google Play listing and how-it-works page show a connected scale and blood meters; no phone-camera body scan, body-composition device, circumference tracking or scanning vendor found. Consistent with the hypothesis's own check (114 help-center articles, App Store and Play, site, press). Not displacement.

## Apollo top-up (2026-10-02)

Round 2 of step 4: the 30 Apollo rows from Vadim's decision 2026-10-02 #2, judged against the same persona and lanes. The 38 round-1 rows are unchanged; every section above this one describes round 1. Apollo rows carry no bio or skills, so they were judged on title, headline and earlier roles.

**Combined, from `apply-decisions`:** 68 people · PASS 50 · WEAK 14 · FAIL 4 · excluded by registry 0 · to send 50, cap 50 (Virta Health at 100%).
Combined PASS by tier: P1 9 · P2 10 · P3 4 · P4 27. By lane: product 5 · clinical 5 · operations 9 · technical-integration 4 · referral 27.

**The 30 new rows:** PASS 13 · WEAK 14 · FAIL 3.

| Tier | New PASS | Lane |
|---|---|---|
| P1 | Sami Inkinen (CEO & Founder) · Amit Shah (President) · Naomi Kincler (VP Care Operations and Content) | product · operations · operations |
| P2 | Colin Daw (VP of Growth, ex-Sr. Director Enrollment Operations at Virta) · Jennifer Arensdorf (Head of Clinical Quality and Training) | operations · operations |
| P3 | Neha Shevade (VP of Engineering) · Christine Vonderach (VP Information Technology and Security) | technical-integration ×2 |
| P4 | Laura Walmsley (CCO) · Kristen Weeks (Head of Customer Success and Partnerships) · Lindsay Johnson (Head of Partnerships With Unions, Labor and Trusts) · Jason Lee (Chief of Staff and Head of Commercial Ops) · Shravya Gupta (VP & Chief of Staff to COO) · Ryann Donohue (VP Marketing) | referral ×6 |

**How the last cap seats were picked:** round 1 left 13 seats under the cap of 50. P1 to P3 took seven. The six P4 seats went first to profiles with a clean current Virta role: Lisa Chen and Meredith Loring moved to WEAK because theirs is unconfirmed. The rest followed the card's "commercial leaders first" order inside P4, which put the two commercial heads, Kristen Weeks and Lindsay Johnson, ahead of the remaining over-the-cap referrals. Shravya Gupta and Ryann Donohue keep their seats: VP level, with a clean current role.

**FAIL (3):**

| Person | Title on row | Reason |
|---|---|---|
| Jamie Anderson | General Counsel and Corporate Secretary | Not at Virta: headline "Chief Legal Officer at Midi Health", and the Virta GC role sits among earlier roles. The card says drop anyone who has left. |
| Wael Asano | Head of Commercial Innovation | Duplicate: same LinkedIn id suffix (028a9828b) and title as Wael Asfour, empty profile. Asfour is the row kept, since it carries a Virta role history. |
| Lola Morris | Chief Executive Officer | Identity collision: Virta's CEO and founder is Sami Inkinen (in this batch; on the card's founders list). Her row is an empty profile in Elk Grove Village, IL with no headline, no earlier roles and no Virta role. |

**WEAK (14), all kept at P4 `referral` in `decisions.md`, so `promote` keeps the tier:**

| Why on the edge | People |
|---|---|
| Over the cap: 37 + 13 fills 50. Valid referrals, ranked below the six new P4s kept. | Keenan Jarvis (Partner Growth) · Jannie Villiers (SVP Accounting and Finance Operations) · Amy Dalton (Head of Corporate Events and Community) · Lucia Guillory (Chief People Officer) · Marc Mooney (Head of People & HR) · Nina Beck (VP Total Rewards) |
| May have left: headline "New Opportunity Loading..." names no Virta role. | Michael Ahlberg (Head of Sales Development) |
| Junior roles that entered the leader pull on a title token ("CFO", "Partner", "Owner"); at Virta, referral possible. | Christina Pentz (Executive Support to the CFO & CCO) · Tyler Mayo-Frey (HR Business Partner) · Sean Moore (Human Resource Business Partner) · Magen Johnston (Associate Customer Success Manager; "Owner" matches her own business, Seat's Taken Concierge, not a Virta role) |
| Current Virta role unconfirmed. | Lisa Chen (Head of Commercial Innovation: one of three rows with that title, with both Wael rows, and her headline names no Virta role) · Meredith Loring (VP, Chief of Staff: the title also sits among her earlier roles and her headline targets 2025; per QC, the raw row's current role is Advisor at Virta Health) |
| Duplicate kept, current role unconfirmed: earlier Director of Customer Success, Employer Group at Virta, but located in Cairo and sharing Lisa Chen's title. | Wael Asfour (Head of Commercial Innovation) |

**Pools:** `skipped` sorts the 18 people not sent (14 WEAK + 4 FAIL) into seven pools, all marked senior. Every one of them is listed above; no pool holds anyone not already judged. Proposed angle for every WEAK: `referral`, P4. The hypothesis needs no change to take them, only the cap.

**Concerns:**
- The cap is full at 50 of 50. Any WEAK added needs the cap raised: 56 takes the six over-the-cap people, 64 takes all 14 WEAK.
- The top-up added no clinical-lane person. The Virta author of the *Obesity* lean-mass paper is still not in the list, so Open question 1's research-head gap stays open.
- Order inside P4 is not encoded beyond the tier number. In `decisions.md` the new P4 rows come after the Director of Tax, whom the card puts last. If import order matters, sort P4 as commercial, executive office and marketing, sales, finance, communications, tax.
- `promote` for this campaign: no `--wave` flag (the round-2 `skipped` hint no longer prints one).

**Peer groups for message-sequencer** (from the rows):

| Group | People | What it means for the messages |
|---|---|---|
| Ex-Personify Health | Laura Walmsley (ex-CCO, Personify Health; earlier CCO at Virgin Pulse) · Kristen Larson (ex-SVP Client Growth, Personify Health) · Leana Balasco (ex-VP Commercial Strategy & Operations, Personify Health) | Three former colleagues, now all in Virta's commercial team. Do not give all three the same former-employer hook, and keep the three referral asks distinct. |
| President and his chief of staff | Amit Shah (President, P1 `operations`) · Shravya Gupta (VP & Chief of Staff to COO, headline "to President", P4 `referral`) | Same office. Her referral ask should point to the President's decision, not repeat his pitch. |
| Also on the rows | Ex-Kaia Health: Manu Diwakar (CFO there), Andrew Chen (Head of Finance there). Ex-Elevance Health: Rad Thie (Staff VP), Ryann Donohue (VP, Health Benefits Marketing). Ex-Kaiser Permanente: Kathryn Geskermann, Jeff Stanley. | Same rule: one former-employer hook per pair, never copied. |

**Питання до Вадима (top-up):**
1. Кеп 50 заповнено (37 + 13). Піднімаємо? 56, щоб узяти шістьох «over the cap», або 64, щоб узяти всі 14 WEAK.
2. WEAK не через кеп (8): Michael Ahlberg (можливо, вже пішов), Christina Pentz, Tyler Mayo-Frey, Sean Moore, Magen Johnston (молодші ролі), Wael Asfour (залишений дубль, роль не підтверджена), Lisa Chen і Meredith Loring (поточна роль у Virta не підтверджена). Кого беремо?
3. Sami Inkinen (CEO & Founder) іде P1 у лейні `product`. Залишаємо чи переводимо в `referral`?
