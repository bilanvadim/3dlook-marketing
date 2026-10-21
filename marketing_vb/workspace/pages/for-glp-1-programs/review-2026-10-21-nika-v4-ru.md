---
product: fitxpress
type: review
vertical: glp-1-programs
date: 2026-10-21
source: nika-v4-2026-10-13.html (Slack #marketing, thread 1791887447.483839, file F0C8MH6MQLT)
status: sent 2026-10-21 (reply ts 1792578562.622949)
---

# Ответ Нике по v4 (отправлен в тред 2026-10-21)

Ника спросила: 1) подходит ли новая структура, 2) есть ли ошибки в стейтментах. 19.10 попросила финальный апрув.

Проверки: детектор `--channel page` (hard fail: en dash ×2; you/your 17,2 на 1 000), видимые слова ~1 800
(мок hero, мок progress view, мобильные карточки сравнения и форма не считались), FAQ 6 и JSON-LD совпадает
с видимым текстом, все 15 ссылок отвечают 200 (кроме самой страницы, она ещё не опубликована), живая
`/pricing/` 2026-10-21 («Up to 500 scans per month», «Personalized»), факты против `pricing.md`,
`accuracy-formulations.md`, `compliance.md`, `tech-spec.md`, `sources-problem-block.md`.

---

<@Ника> посмотрел v4.

*1. Структура.* Порядок Hero → Problem → Solution ок: для клинической программы боль и есть главный аргумент. Проблема в другом: после блока проблемы идут три блока с одной мыслью: карточки «Make progress visible», секция «Show changes across selected check-ins» и «Body data and progress capabilities». 3D Body Progress упоминается 6 раз, «your program controls/decides» 7 раз. Отсюда и длина: ~1 800 слов при потолке 1 600, «you/your» 17 на 1 000 слов при норме 12,5.
Предлагаю: карточки оставить, секцию «Show changes…» свернуть в одну фразу и мок под карточками, а outputs сделать таблицей на 5 строк «Returned output | What it changes for the program», как на фитнесе.

*2. Ошибки в стейтментах*
• *Мок в hero и в progress view.* Вес −0,3 кг при жире −1,0 п.п. значит, что пациент за 4 недели на GLP-1 набрал ~0,8 кг lean mass. Это спорит с нашим же блоком проблемы, где ~25% потерянного веса приходится на lean mass. Предлагаю вес 97,4 → 94,6 кг (−2,8 кг), жир и талию оставить. Тогда из 2,8 кг ~73% приходится на жир и ~27% на lean mass, как в SURMOUNT-1, и мок показывает ровно то, о чём H2: вес упал, а состав тела показывает, за счёт чего. Подпись «A small change in entered weight…» тоже поменять.
• *«Patients see the change the scale cannot show».* Спорит с таблицей сравнения: connected scale с биоимпедансом показывает состав тела (об этом была и правка Асель от 08.10). Замена: «the change that weight alone does not show».
• *64,8% в блоке проблемы.* H2 про то, что вес не показывает жир и lean mass, а цифра про отказ от терапии и теперь ничего не доказывает. Фразу про выручку убрали по правке Асель, и цифра повисла. Рекомендую убрать: связать отказ с тем, что пациент не видит прогресса, данные не позволяют (из-за недостаточной потери веса бросают 1,7%, из-за цены и страховки 47,6%). 25% и advisory остаются, они ровно про этот блок.
• *No integration fee* пропало из цены. Это публичное решение от 30.09, вернуть: «Both plans include guided implementation support, with no integration fee.»
• *96–97% и 1.5–2.0 cm*: в каноне через дефис, en dash детектор считает hard fail.
• *Peer review*: лучше дословно из канона: «3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study.»

*3. Мелочи*
• Пилот: вернуть одну фразу «A comparable cohort keeps the usual check-in flow.» Без сравнения «continued program participation» не с чем сопоставить.
• FAQ про DXA: начать ответ с «No.»
• Хлебные крошки: «FitXpress for weight management» → «GLP-1 programs» (запросы про weight loss держит telehealth).
• Smart Scales пишем просто Smart Scales, без «(beta)». На бариатрии тоже убираем.
• Форма такая же, как на insurance и бариатрии. Сейчас в HTML стоит заглушка с /contact-us/.
• Цены в «scans» совпадают с живой /pricing/. Когда выйдет новый прайсинг на запросах, меняем на обоих лендингах сразу.

С этими правками апрув, можно в дизайн.

---

## Арифметика мока (для проверки)

| | Неделя 8 | Неделя 12 (v4) | Неделя 12 (предложение) |
|---|---|---|---|
| Entered weight | 97,4 кг | 97,1 кг | 94,6 кг |
| Body-fat estimate | 39,6% | 38,6% | 38,6% |
| Fat mass | 38,57 кг | 37,48 кг (−1,09) | 36,52 кг (−2,05) |
| Lean mass | 58,83 кг | 59,62 кг (**+0,79**) | 58,08 кг (−0,75) |
| Доля lean в потере | | — (lean растёт) | 27% |

## Решения Вадима 2026-10-21

- Порядок блоков Ники (проблема сразу после hero) остаётся для этой страницы, хотя кит с 07.10 ставит карточки ценности первыми.
- Smart Scales без «(beta)» на страницах, бариатрия тоже.
- Форма та же, что на insurance и бариатрии (общая `FX | LP | Demo`, `11acb23a-…`).
- Остальные пункты приняты как есть.
