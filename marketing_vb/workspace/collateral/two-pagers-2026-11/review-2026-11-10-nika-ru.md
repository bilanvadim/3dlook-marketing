---
product: fitxpress
type: review
artifact: two-pagers (Fitness, GLP-1, Bariatric)
date: 2026-11-10
source: Slack #marketing (C0C0TBSM90E), Nika, ts 1794306480.438679; files F0CGG2LDVED (Fitness), F0CFYQ1P51V (GLP-1), F0CGHSC1XDJ (Bariatric)
status: sent 2026-11-10 (reply ts 1794313232.362169)
---

# Ответ Нике по трём 2-pager (отправлен в тред 2026-11-10)

Ника отметила Асель и Вадима: «Сделала драфты 2-pager для: Fitness, GLP-1, Bariatric. Дайте фидбек».
PDF не коммитим: репо публичный, а на 2-й странице чужой SMS-экран с номером телефона. Здесь только
текст, вытащенный из PDF (`nika-draft-2026-11-10-*.txt`).

Что проверено:
- Тексты против `proof-points.md`, `accuracy-formulations.md` §1.2, `compliance.md`, `pricing.md`,
  `tech-spec.md`, `how-it-works.md`; источники проблемных блоков против
  `pages/for-glp-1-programs/sources-problem-block.md`, `pages/for-bariatric-programs/page-v2-2026-10-16.md`,
  `pages/for-connected-and-digital-fitness/page-final-2026-10-07.md`.
- `detect-ai-tells.py --channel page`: 0 hard bans, density 0.0 на всех трёх.
- Картинки на 80 и 200 dpi; `pdfinfo -url` (ссылок 0); `pdffonts` (Jost, Inter); формат 1080×1528,5 pt.
- Лендинги: `/fitxpress/for-connected-and-digital-fitness/` 200, GLP-1 и bariatric 404 (не вышли).

Что сходится с каноном: 80+ body measurements, under 45 seconds, «100+ clients have used 3DLOOK body
scanning since 2016» (подпись лого-ряда, Вадим 06.10), «including fitness teams» (Zing Coach, Verv),
«including weight management programs» (Yazen), No Integration Fee (30.09), HIPAA Support Under BAA,
«FitXpress is not a medical device.», Smart Scales без «(beta)» (Вадим 21.10), Admin Panel + CSV export
(канон: optional interface for monitoring and exporting results), SURMOUNT-1 ~25% lean (DXA-подисследование,
у плацебо та же пропорция, формулировка это не нарушает), MBSAQIP 30 дней / 6 мес / 1 год, NICE 2 года.

---

## Текст для треда (Slack, от Вадима)

<@U0BSD11QFFX> посмотрел все три. Тексты чистые: цифры (80+, under 45 seconds, 100+ clients since 2016, no integration fee), HIPAA under BAA и «FitXpress is not a medical device» по канону, детектор AI-штампов ничего не нашёл. Править в основном визуал и несколько формулировок.

*Общее для всех трёх*
1. *SMS на 2-й странице (шаг 1)* — это экран Mobile Tailor: «Welcome to …, your perfect wedding» (свадебный салон), ссылка 3dl.ink и номер телефона, похожий на настоящий. Нужен экран FitXpress (вход в скан в приложении или напоминание о чек-ине), без чужого названия и номера. На фитнесе подпись к нему ещё и «Member Starts a Scan in the App».
2. *Мок админки на ноутбуке не сходится.* Вес 143 lb, а lean 99 lb + fat 68,3 lb = 167 lb; при fat 26% жировая масса ~37 lb, lean ~106 lb. Справа «June 20th, 143 lb», а график заканчивается на ~175 lb. Даты в двух форматах (09/18/20 и 29.03.2026). «Trajectory» и «Next visible change in 2 weeks» — такого прогноза в продукте нет, лучше убрать. На GLP-1 читатель как раз смотрит на fat и lean, там это бросится в глаза первым.
3. *«Book a demo» и «3dlook.ai» не кликаются*: в PDF нет ни одной ссылки, и рядом нет ни адреса, ни почты. Эти PDF пойдут в ответы на аутбаунд, поэтому кнопку сделать ссылкой и добавить адрес текстом для печати: фитнес → 3dlook.ai/fitxpress/for-connected-and-digital-fitness/ (живая), GLP-1 и бариатрия → 3dlook.ai/contact-us/, пока их лендинги не вышли.
4. *«Scans Under Your Brand»*: экран съёмки в SDK сейчас не брендируется, меняется только язык (шрифты, цвета и кнопки нет; Whitney писала 28.10, что клиенты об этом спрашивают). «White-label» как термин ок, а эту плашку лучше заменить на «Results in Your Own App».
5. «3D Body Progress (Pro)» — убрать «(Pro)»: тарифы сейчас переделываются, а клинические программы всё равно на Personalized.
6. Дизайн: шрифт Jost + Inter, а бренд-шрифт по DESIGN.md — Satoshi (в PDF его нужно встроить). На GLP-1 и бариатрии та же стройная модель в спортивной форме, что на фитнесе; для клинической программы лучше другой кадр или продуктовый экран.

*Фитнес*
• В Challenge нет главной боли, удержания. На лендинге она есть, с проверенными цифрами: у health & fitness приложений 24% пользователей активны в первый день и 7% на 30-й (Adjust); медиана 70% пользователей бросают lifestyle-приложения в первые 100 дней (Kidman et al., JMIR 2024). Одну из них стоит поставить в Challenge.
• «GDPR Principles Applied»: по compliance.md «follows GDPR principles» как единственный ответ про GDPR не пишем. Замена: «GDPR: DPA with SCCs».

*GLP-1*
• Повторяемость: «repeat scans differed by less than 1 cm» → «repeated scans showed typical differences of less than 1 cm for most measurements». Без «typical» читается как «каждый повторный скан». На фитнесе формулировка правильная.
• SURMOUNT-1: цифра верная, но нужна сноска мелким шрифтом (Look et al., Diabetes, Obesity and Metabolism, 2025). Клинический читатель захочет источник.
• Шаг 1 «Patient Receives Scan Link» спорит с Solution, где скан «inside its own app». Либо «Patient Opens the Scan in Your App», либо убрать «inside its own app».

*Бариатрия*
• Повторяемость: та же правка.
• MBSAQIP и NICE: факты совпадают с лендингом, но тоже нужна сноска (MBSAQIP Standards, NICE NG246). «US-accredited programs» точнее как «MBSAQIP-accredited programs».
• Акцент на follow-up после операции и BMI-проверка вторым планом — так и договаривались, ок.
