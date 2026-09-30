---
product: fitxpress
type: page-review
vertical: insurance-underwriting
date: 2026-09-30
compares: page.md (08-31) · драфт Ніки (Drive, HTML, 09-30) · драфт Асселі (fitxpress-insurance-underwriting.hr-d114.chatgpt.site)
result: page-v2-short.md
---

# Рев'ю: три версії insurance-лендингу → коротка v2

Задача Вадима: лендинги юз-кейсів мають бути коротшими за наші й комерційнішими, щоб конвертувати
лідів. Глибина живе в статтях, лендинг на них посилається. Ключі беремо з
`2026-09-29-landing-keywords.md` §5. Дизайн не оцінюємо, тільки структуру й текст.

## 1. Порівняння

| | Наш `page.md` (08-31) | Ніка | Асселя | **v2 (`page-v2-short.md`)** |
|---|---|---|---|---|
| Обсяг | ~2 700 слів, 13 H2, 13 FAQ | ~2 050, 11 H2, 9 FAQ | ~1 160, 7 H2, 0 FAQ | **~1 250, 8 H2 + форма, 6 FAQ** |
| Хук у hero | опис продукту | вигода: «issue faster, cut rework» + результат за 45 с | опис продукту | результат за 45 с + «ваш поріг» |
| Проблема в цифрах | абзац (Munich Re, CDC) | **3 цифри: Gen Re 59%, Munich Re #1, LIMRA 9 vs 27** | немає | 3 цифри Ніки + лінк на хаб |
| Порівняння з paramed | таблиця 6 рядків | таблиця 8 рядків | 3 картки | таблиця 5 рядків |
| Шлях пілоту (shadow) | FAQ-відповідь із тріалом | є | **є, найчіткіше** | є + «з якими цифрами ви підете» |
| Ціна | тариф + тріал | $1,000 / 500 сканів | лише лінк | $1,000 / 500 сканів + лінк |
| FAQ (GEO) | 13 | 9 | немає | 6, GEO-фрази як H3 |
| Compliance | повний блок (~450 слів) | картки, без HIPAA/BAA | **правильні формулювання** | 5 рядків + лінк на trust-FAQ |
| Головний ключ `accelerated underwriting` у title / H1 | ні / частково | ні / ні («accelerated life underwriting») | ні / ні | **так / так** |
| Лінки на статті | 3 | 2 | 3 | 5 статей + фіча-сторінка |

**Висновок.** Найкраща основа — драфт Ніки: він говорить мовою вигоди покупця («your threshold», «you
get»), має блок проблеми в цифрах, ціну й FAQ. Але він довгий і має фактичні помилки (§2). У Асселі
найкоротша структура, найчистіші compliance-формулювання й найкращий пілотний блок. Зате в неї немає
цифр проблеми, ціни й FAQ, а регістр ближчий до procurement-документа, ніж до продажу. v2 бере скелет і
вигоди Ніки, стислість і пілот Асселі, ключі й лінки з нашої карти.

## 2. Що виправити в драфті Ніки (факти)

| # | Що в тексті | Проблема | Як у v2 |
|---|---|---|---|
| 1 | «heights 150 to 205 cm» | Застаріло. Вадим 2026-09-02: **150-220 cm**, 205 публікувати не можна | Популяцію перенесено в статтю про точність |
| 2 | «FitXpress is not *positioned as* a medical device» (×2, зокрема футер) | Hard ban з 09-11 | «FitXpress is not a medical device.» |
| 3 | Заголовок «Encrypted and short-lived» | Короткий строк зберігання стосується лише фото. Виміри й 3D-моделі зберігаються без обмеження строку | Окремо «Photos» і «Scan records» |
| 4 | «67 active customers in 2025», «112,100 scans» | Вадим 09-30: публічно всюди лише «100+ clients»; 67 і 112,100 на сторінки не йдуть | «100+ clients» у блоці пілоту |
| 5 | «with no integration fee» | ✅ Вадим 09-30: правда і наша перевага над конкурентами. Тепер записано в `pricing.md` | Залишено: у hero-стрічці й у рядку ціни |
| 6 | Hero-стат «No exam: no examiner, no appointment» | Читається як заміна paramed (ключова карта забороняє). До того ж тягне споживчий запит «no medical exam life insurance» | «Same session: no measurement appointment» |
| 7 | H1 «Verified build evidence…» | Вага передбачена (±3.5%), тож «verified» перебільшує. Точного ключа в H1 немає | «Remote build and BMI evidence for accelerated underwriting» |
| 8 | Власна форма (Role, «annual accelerated application volume») | Рішення 09-29: одна спільна форма `FX \| LP \| Demo` на всіх FX-сторінках | Спільна форма. **Поле обсягу — хороший кваліфікатор; пропоную додати його в спільну форму як необов'язкове (рішення Вадима)** |
| 9 | «Review the evidence-workflow checklist →» | Такого активу ще немає (чекліст — P2 у контент-плані) | Прибрано; м'який вихід веде на хаб |
| 10 | «30-minute walkthrough» | Обіцянка від імені sales, треба підтвердити | Без тривалості |
| 11 | Немає HIPAA/BAA | Для US-страховика це перше питання | Рядок BAA + FAQ-питання |

**Перевірено й залишено:** «#1: build/BMI попереду тютюну» (Munich Re) правильне. Munich Re пише:
«Build/BMI misclassification is the leading misclassification reason», тютюн другий у RHO і четвертий у PIA
([джерело](https://www.munichre.com/us-life/en/insights/future-of-risk/misclassification-driving-mortality-slippage-in-auw.html)).
**Помилка в нашій хаб-статті:** там build/BMI стоїть «#2 driver of misclassification after smoking».
Хаб змішав дві статті Munich Re: друге місце там належить *misrepresentation concern*, а не
*misclassification*. Виправити на рефреші хабу.

## 3. Що виправити в драфті Асселі

| # | Що | Проблема |
|---|---|---|
| 1 | Title «FitXpress for Insurance Underwriting \| Remote Build Evidence», H1 «…accelerated life insurance underwriting» | Точного головного ключа `accelerated underwriting` немає ні в title, ні в H1 |
| 2 | Немає FAQ | Втрачено GEO: «what is accelerated underwriting» (US 60) і «remote height and weight verification for life insurance» мають стояти як H3 |
| 3 | Немає ціни й цифр проблеми | Бракує комерційного аргументу: навіщо це зараз і скільки коштує |
| 4 | Регістр («The proof required for technical, security and legal review») | Мова procurement, а не вигоди для андеррайтингу |
| 5 | «currently at the pilot stage» відкриває розділ | Чесно, але в лоб. У v2 рамка «перевірено в регульованих флоу, готово до пілоту» |
| 6 | Дві назви CTA («Book a demo» / «Book an underwriting review») | Одна дія, одна назва |
| 7 | «96–97%» з en dash; «≈3.5% under documented validation conditions» | Формат `96-97%`; у `proof-points.md` вага ±3.5% «real-world conditions» |

## 4. Що з нашого `page.md` застаріло (v2 його замінює)

- «FitXpress maintains HIPAA compliance», «No names and no personal identifiers», «Images are excluded from
  model training and not shared with third parties»: усе це суперечить `compliance.md` від 09-18.
- Публічний тріал «200 requests»: рішення 09-27 — тріал публічно не обіцяємо, CTA завжди «Book a demo».
- SEO title «Body Data for Life Insurance Underwriting»: ключ `life insurance underwriting` належить хабу.
- URL `/for-insurance-underwriting/` → `/fitxpress/for-insurance-underwriting/`.

## 5. Куди пішла глибина (лендинг дає рядок і лінк)

| Прибрано з лендингу | Де живе |
|---|---|
| Етапи андеррайтингу, де AU гальмує, fraud-prevention support, NAIC | Хаб [`mobile-body-scanning-insurance-underwriting`](https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/) |
| Чотири умови точності, популяція валідації | [`mobile-body-scanning-accuracy`](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) |
| HIPAA, biometric/health data, хостинг, SOC 2, FDA, видалення | [Trust-FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) |
| Як працює перевірка ваги в інших регульованих флоу | `/for-bmi-verification/` |
| Wellness-linked insurance | [`wellness-rewards-verification-…`](https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/) |
| П'ятиетапна таблиця customer journey | Хаб, рядок контент-плану «expand the workflow table» (P2) |
| Self-report vs verified, глибоко (ключ `life insurance fraud`) | Запланована стаття «Self-Reported BMI vs Verified Body Data» (P1) |
| Чекліст вибору вендора | Лід-магніт «Insurance Buyer's Checklist» (P2). Коли з'явиться, стане м'якою конверсією |

## 6. Шаблон для всіх лендингів юз-кейсів (≈1 100-1 300 слів)

| # | Блок | Слів | Навіщо |
|---|---|---|---|
| 1 | Hero: H1 = головний ключ; 2-3 речення (результат + час); CTA `#demo` + якір на запис; стрічка з 4 фактів | 90 | Продати за 5 секунд |
| 2 | Проблема в 3 цифрах + лінк на хаб | 90 | Навіщо зараз |
| 3 | Як це працює, 3 кроки + рядок про налаштування + лінк на фіча-сторінку | 130 | Зняти страх інтеграції |
| 4 | Що ви отримуєте (таблиця на 5 рядків) + CTA «sample» | 150 | Конкретика для покупця |
| 5 | Порівняння з тим, як роблять зараз (таблиця на 5 рядків) | 120 | Позиціонування без атаки |
| 6 | Точність і дані на одному екрані: 3 цифри + 5 рядків + 2 лінки | 180 | Зняти заперечення diligence |
| 7 | Пілот і ціна: 3 кроки, «з якими цифрами ви підете», ціна від | 150 | Знизити ризик першого кроку |
| 8 | FAQ, 5-6 питань, GEO-фрази дослівно як H3 | 280 | GEO + заперечення |
| 9 | Форма `#demo` (спільна) + м'який вихід на хаб | 50 | Конверсія |

**Правило:** усе, що потребує більше одного абзацу пояснень, іде в статтю, а на лендингу лишаються рядок і лінк.
CTA стоїть на кожному другому екрані: hero, після запису, після пілоту, форма.

## 7. Кіт `page-builder` тягне сторінки в довжину. Пропоновані зміни (чекають на «так» Вадима)

`references/kit-vertical-page.md` зараз вимагає саме того, від чого ми хочемо піти:

1. Writer SOP §1: «Match its depth (~1,600 words)» → **ціль 1 100-1 300 слів**; телехелс-сторінка
   лишається еталоном лише для схеми й дисципліни claims, а не для обсягу.
2. Слот 13: «13-question FAQ» → **5-6 питань**, GEO-фрази як H3; решта відповідей живе в статтях.
3. Слот 9: чотири умови точності → **3 цифри + одне речення + лінк** на accuracy-статтю.
4. Слот 8: повний compliance-блок → **5 рядків + лінк** на trust-FAQ (так уже каже `compliance.md` і контент-план).
5. Слоти 4, 5 і 7 зливаються в «Проблема в цифрах» і «Як це працює, 3 кроки».
6. **Баг:** слот 6 досі диктує «FitXpress is not *positioned as* a medical device», хоча це hard ban з
   09-11. Звідси, найімовірніше, і формулювання в драфті Ніки. Правильно: «FitXpress is not a medical device.»
7. Скоркард сліпого судді (`gates-and-scorecard.md`) треба узгодити з пунктами 1-4, інакше короткі
   сторінки програватимуть за «глибину».

## 8. Рішення Вадима (2026-09-30)

1. **Кіт `page-builder` змінено за §7**, разом зі скоркардом судді, `docs/page-pipeline.md`, SKILL і
   `site-inventory.md`. Заодно виправлено «positioned as» у слоті 6.
2. **Поле обсягу додано в спільну форму** як необов'язкове: «Expected monthly scan volume», межі як у
   тарифах (ТЗ трекінгу B1).
3. **112,100 сканів і «not billable» на сторінках не використовуємо.**
4. **«No integration fee» публічно**: це правда і перевага (`pricing.md`).
5. **«100+ clients» всюди**, 67 — лише внутрішня цифра (`proof-points.md`, `CLAUDE.md` §1).
