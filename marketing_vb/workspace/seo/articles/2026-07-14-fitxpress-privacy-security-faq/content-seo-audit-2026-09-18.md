---
slug: fitxpress-data-privacy-security-regulatory-faq
type: content-seo-audit
date: 2026-09-18
subject: https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/
text_of_record: published-live-2026-09-18.md
compared_with: v3-seo/final.md, v3-seo/plan.md, v3-seo/publish-package.md
rules_checked: about-me.md, blog-style-guide.md, editorial-guardrails.md, editorial-rewrites.md, terminology-guardrails.md, content-strategy-guidelines.md, content-plan.md, detect-ai-tells.py, article_lint.py
---

# Аудит контенту й SEO: Data, Privacy, Security & Regulatory FAQ for FitXpress

Живу сторінку прогнано через наші гейти (`article_lint.py`, `detect-ai-tells.py`), звірено з планом і пакетом публікації v3-seo, з правилами письма, з Search Console (URL Inspection + Search Analytics) і з вхідними посиланнями 20 сторінок сайту. Дата заміру: 2026-09-18.

## Коротко

Як trust-актив сторінка сильна: таблиця Quick answers «пряма відповідь + уточнення», питання в H3, FAQPage-schema на 14 питань, точні формулювання без маркетингових перебільшень. Щільність AI-маркерів 1,8 на 1000 слів при бюджеті 6,0, жодного em dash, жодного «positioned as». Редактор перетворив наш драфт на значно кращий текст: 21 жорстке порушення → 2, «HIPAA compliant» ×4 → 0.

Слабкі місця — не текст, а зв'язність і дрібна гігієна: на сторінку в тексті посилаються лише 4 сторінки сайту з 20 перевірених, сама вона веде лише на accuracy-статтю й головну, посеред тексту стоїть eBook про GLP-1, alt-тексти картинок напхані чужим ключовим словом. За нашими гейтами текст провалює довжину речень, розшифровку абревіатур і правило про коригувальні протиставлення, але частина цих правил не пасує до юридично-довідкового формату, і це вже питання до наших правил, а не до статті.

## 1. Технічне SEO

| Елемент | Стан | Оцінка |
|---|---|---|
| Title | «FitXpress Data Privacy & Security FAQ \| 3DLOOK», 46 символів | ✅ дослівно наша рекомендація |
| Meta description | 141 символ, HIPAA / GDPR / SOC 2 / FDA / procurement | ✅ наша рекомендація (дрібна правка «&») |
| H1 | «Data, Privacy, Security & Regulatory FAQ for FitXpress» | ✅ |
| Slug, canonical | `fitxpress-data-privacy-security-regulatory-faq`, self-canonical | ✅ |
| Індексація | GSC: «Submitted and indexed», просканована 16.09 | ✅ |
| Пошукові дані | GSC Search Analytics 14–18.09: 0 рядків | — зарано, сторінці 2 дні |
| Schema | Article + FAQPage (14 питань = 14 H3) + BreadcrumbList + Person | ✅ FAQPage покриває всі H3 |
| Article.articleSection / keywords | «Blog» / «Technology» | ⚠️ для trust-сторінки краще Health / Privacy / Security |
| Breadcrumbs | Home → стаття | ⚠️ без рівня Content Hub |
| TOC, якорі | TOC є; якорі `#data-rights`, `#ai-training`, `#security-assurance`, `#privacy-compliance`, `#regulatory-status`, `#fda-status` працюють | ✅ |
| Alt-тексти (3 банери) | «…all powered by a robust framework that enhances body scanning accuracy for precise enterprise decisions», em dash у першому | ❌ чуже ключове слово (accuracy-статті), «robust» із нашого стоп-списку, не описують зображення |
| Довжина | 3 810 слів прози (план: 2 500–3 500, ціль 3 200) | ⚠️ +9% понад верхню межу |

## 2. Посилання

**Вихідні.** План закладав 8 внутрішніх посилань у 4 напрямках (Main Health hub, три продуктові сторінки, insurance use case, two-photos, accuracy, Privacy Policy). На живій сторінці із запланованих лишилися 2 (accuracy ×3, Privacy Policy); додалися головна ×2, Terms, API docs, eBook ×2.
- Немає посилання **вгору** на Main Health hub (`ai-body-data-health-hub`). У плані стояв неправильний слаг `ai-body-data-for-health` — можливо, тому редактор його й прибрав.
- Немає посилань **вниз** на BOFU-сторінки (`/structured-body-data-for-telehealth-digital-health-programs/`, `/for-bmi-verification/`, `/fitxpress/for-connected-and-digital-fitness/`).
- Немає посилань **убік** на вертикальні хаби, хоча текст називає telehealth, weight management, insurance, research.

**Вхідні.** Контент-план (v2.0) вимагає посилання з кожного вертикального хабу та з кожного розділу про приватність. Посилання в тексті є лише з 4 сторінок: Main Health hub, GLP-1-хаб, bariatric-хаб, coaching-стаття. Решта ставлять FAQ тільки у віджет «останні пости».

Без посилання в тексті: accuracy framework · AI in Fitness · AI in Telehealth · patient engagement · online pharmacy BMI verification · GLP-1 tools listicle · insurance underwriting · Wellness Platforms hub · wellness rewards · clinical trials · occupational health · admin panel · `/structured-body-data-for-telehealth-digital-health-programs/` · `/for-bmi-verification/` · `/fitxpress/for-connected-and-digital-fitness/` · головна.

## 3. Структура і подача

- **Формат** — довідковий FAQ: вступ-застереження → Quick answers (Topic / Direct answer / Qualification) → 6 H2-груп → 14 питань у H3 → запит документів. Для GEO/AEO це правильна форма: кожне питання — окремий видобувний блок, таблиця дає короткі відповіді.
- **Пряма відповідь першим реченням** — у 9 з 14 секцій. Слабкі 5: «What data…» (починається з опису сканування), «Who controls and owns…» (мета-речення), «How does 3DLOOK protect…» («groups … into four areas»), «How does FitXpress support HIPAA, GDPR…» (починається з ярлика «HIPAA.»), «Is 3DLOOK SOC 2 certified?» (спершу визначення SOC 2, відповідь лише в другому реченні).
- **CTA.** Посеред тексту — банер eBook «The Digital Health Revolution» про GLP-1/telehealth. Порушує наше «один CTA, без банерів посеред тексту» і не збігається з наміром сторінки (procurement / objection handling). Фінальний CTA (запит документів через legal@3dlook.me) якраз правильний.
- **E-E-A-T.** Автор — «marketing professional with over 10 years…». Для сторінки про юридичні й безпекові питання немає рядка «Reviewed by legal / security» і видимої дати «Last reviewed».
- **Зовнішні авторитетні джерела.** Жодного посилання на HHS, ICO/EDPB, AICPA чи FDA, хоча about-me вимагає «neutral authority» — цитувати зовнішні органи.

## 4. Стиль і тон проти наших правил

| Правило (джерело) | Що на сторінці | Вердикт |
|---|---|---|
| Calm, specific, honest about limits (about-me) | Кожне «так» має умову, межі названі поруч із можливостями | ✅ сильна сторона |
| Reframe move на старті (about-me) | Починається з опису продукту й юридичного застереження | ⚠️ немає — для довідника допустимо |
| Actor framing, «customer» лише для юридичної ролі (terminology §2.12) | «customer» 104 рази (26 на 1000 слів), майже завжди юридична/договірна роль; «you» 2 рази в застереженні; «we» — 0 | ✅ формально, але монотонно |
| Довжина речень (article_lint gate 10: сер. ≤16, ≤6% >25, ≤1 >35) | 16,9 · 16% (25 з 155) · 3 (найдовше — застереження на 43 слова) | ❌ за гейтом |
| Коригувальні протиставлення «X, not Y», «rather than» (terminology) | 5: «HIPAA is a regulatory framework, not a certification» ×2, «…independent auditor, not a product certification», «operational rather than descriptive», «…rather than diagnosis» | ❌ за правилом, але перші три — головний зміст сторінки |
| Абревіатури M1 (editorial-guardrails) | GDPR і BIPA не розшифровано ніде; HIPAA і FDA вжито в таблиці до розшифровки | ❌ |
| Термінологія §2.13 | «80+ body measurements» ✅, «body metrics» як парасолька ✅, але «body composition values» ×1 (наш термін — estimates) | ⚠️ |
| Medical device (guardrail #6) | «does not meet the definition of a medical device under the UK MDR / EU MDR» — точніше за наше «FitXpress is not a medical device.» | ✅ сильніше за наше правило |
| Em dash, «positioned as», заборонені слова | 0 / 0 / 0 у тексті (але «robust» і em dash в alt) | ✅ текст, ❌ alt |
| Повтори (editorial-rewrites) | однакове речення про NDA-документи двічі; «applicable customer agreement» ×8; «qualified enterprise customers» ×6; список «does not determine a diagnosis, treatment…» у двох сусідніх секціях | ⚠️ |
| Речення про саму сторінку (editorial-rewrites; terminology «see below») | «explained under … section» / «described in …» ×10, «This FAQ …» ×2 | ⚠️ у довіднику це навігація, у статті ми б це різали |
| Регістр | пасив ~15 на 1000 слів, «applicable» 39 разів (~1 на 100 слів), «does not» 18 | ℹ️ юридично-документний регістр — доречний тут, не для маркетингових статей |
| Детектор, жорсткі збіги | «independent auditor» (reserved word) у визначенні SOC 2; «diagnosis» у гіпотетичному «functionality intended to support diagnosis … would require reassessment» | ℹ️ обидва виправдані контекстом |

## 5. Що редактор зробив з нашим драфтом

| | Наш v3-seo/final.md | Жива сторінка |
|---|---|---|
| Слова прози | 5 547 | 3 810 (−31%) |
| Жорсткі порушення детектора | 21 | 2 (обидва виправдані) |
| «HIPAA compliant» | 4 | 0 |
| «positioned as» | 4 | 0 |
| Em dash | 2 | 0 |
| «What trips up most…» (presumed reaction) | 3 | 0 |
| AI-маркерів на 1000 слів | 5,6 | 1,8 |
| Речень понад 35 слів | 8 | 3 |
| Частка речень понад 25 слів | 14% | 16% |
| Внутрішні посилання із запланованих | 8 | 2 |
| Структура | 6 частин, 14 нумерованих розділів + чекліст впровадження + окремий FAQ-блок на 11 питань | 6 H2 + 14 H3; чекліст і окремий FAQ прибрано (FAQPage зібрано з H3); додано розділ UK/EU MDR (у нас його не було), TOC, eBook |

**Висновок.** На trust-сторінці редактор ставив юридичну точність вище за довжину речень: речення не стали коротшими (частка довгих навіть зросла), зате зникли всі неправдиві compliance-статуси й маркетингові звороти. Наш пайплайн тоді писав неправильні факти («HIPAA compliant»), і з 2026-09-18 `compliance.md` і детектор це закривають.

## 6. Рекомендації

### На сайті (для редакторів, у порядку пріоритету)
1. **Вхідні посилання.** Додати в тексті коротку контекстну заметку про приватність + посилання на FAQ на 12 content-hub сторінках і 3 продуктових (список у §2). Це вимога контент-плану, і це найбільший SEO-важіль сторінки.
2. **Вихідні посилання.** Вгору — Main Health hub; вниз — telehealth BOFU-сторінка і `/for-bmi-verification/` у розділах, де згадано ці сценарії; убік — 2–3 вертикальні хаби.
3. **eBook-банер** замінити на procurement-CTA («Request security documentation») або прибрати.
4. **Три alt-тексти** переписати: описати зображення, без «body scanning accuracy», «robust», em dash.
5. **Пряма відповідь першим реченням** у 5 секціях (§3). Напр. SOC 2: «Not yet. 3DLOOK is working toward…»
6. **Дрібні правки:** розшифрувати GDPR і BIPA при першому вжитку; «body composition values» → «estimates»; прибрати дубль речення про NDA.
7. **Schema і breadcrumbs:** articleSection / keywords → Health, Privacy, Security; хлібні крихти з рівнем Content Hub.
8. **E-E-A-T:** рядок «Reviewed by 3DLOOK legal and security» і видима дата «Last reviewed».

### У наших правилах (потрібне рішення Вадима)
A. Додати в `blog-style-guide.md` **Type G — canonical trust FAQ** за зразком цієї сторінки: Quick answers (topic / direct answer / qualification), H2-групи + H3-питання, пряма відповідь першим реченням, FAQPage з H3, один procurement-CTA, юридичний регістр дозволений. Зараз такого типу немає, а чекліст гайду забороняє заголовки-питання поза типами B/C/D.
B. **Гейт довжини речень** для Type G: або окремі пороги, або виключити абзаци-застереження з підрахунку. Інакше кожна наступна trust-сторінка валиться на юридичних формулюваннях.
C. **Коригувальне протиставлення:** дозволити дефініційні уточнення в trust-контенті («HIPAA is a regulatory framework, not a certification») — або переписувати їх двома реченнями. Зараз правило забороняє головну думку сторінки.
D. **Детектор:** не рахувати «independent auditor» у визначенні SOC 2 та гіпотетичне «support diagnosis … would require reassessment».
E. **Alt-текст** — додати правило в чекліст `seo-publisher` і G-T `page-builder`: описує зображення, без ключових слів чужої сторінки, без слів зі стоп-списку.
F. **Регістр:** зафіксувати, що юридично-документний регістр — норма для Type G і не переноситься в маркетингові статті (там і далі правлять about-me та editorial-rewrites).

## Рішення (2026-09-18, Вадим: «внось зміни»)

Пропозиції A–F внесено того ж дня:
- **A** — `blog-style-guide.md` §9: Type G — canonical trust FAQ (структура, регістр, гейти, обов'язкові посилання, E-E-A-T); чекліст дозволяє заголовки-питання для G. Жива FAQ лежить у корпусі як `brand-assets/past-articles/blog/fitxpress-data-privacy-security-regulatory-faq.md` з `known_issues`; CLAUDE.md §15 п.2 посилається на неї.
- **B** — `article_lint.py`: для `article_type`, що містить «trust FAQ» / «Type G» / «canonical FAQ», пороги довжини речень 18 / 18% / 3 (заміряно на цьому фіналі, з тим самим запасом, що й основний гейт). Жива FAQ позначена `article_type` і проходить.
- **C** — `terminology-guardrails.md` (project note) і CLAUDE.md §6: дефініційне «HIPAA is a regulatory framework, not a certification» — це вже наявний виняток документа Ассель («legal or regulatory boundary»), а не порушення.
- **D** — `detect-ai-tells.py`: ліцензії на рівні речення (визначення SOC 2 з «independent auditor», гіпотетичне «support diagnosis … would require reassessment», «not a (product) certification»). Справжні твердження («validated by an independent auditor», «supports diagnosis») і далі падають — тести.
- **E** — alt-текст: чекліст `blog-style-guide.md` §10, `seo-publisher`, G-T `page-builder`.
- **F** — `about-me.md` «Register»: юридичний регістр лише для Type G.

Рекомендації для сайту (1–8) лишаються за редакторами.

