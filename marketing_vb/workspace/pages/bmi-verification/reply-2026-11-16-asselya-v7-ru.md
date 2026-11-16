---
product: fitxpress
type: feature-page
vertical: bmi-verification
status: sent 2026-11-16 (thread reply ts 1794838086.310489)
for: Asselya
thread: C0C0TBSM90E / 1792656114.772339
draft_reviewed: 3dlook-bmi-verification-mockup-v7.html (Slack F0CHY5CT68G, 2026-11-12)
---

<@U0A0JTLHW2K> посмотрел v7. Почти всё из разбора учтено: FitXpress в H1, блок «What is BMI verification?» с определением и цифрой CDC, общий ряд логотипов с UK Meds и Yazen первыми, RTPV и Clothing Detector на подтверждённом уровне, 3.5% под predicted weight, «Under 45 seconds», пять строк про данные, «BMI verification methods compared» со строкой про видеоконсультацию, ссылки из карточек вертикалей. Осталось немного:

*Обязательно*
1. *Карточка Bariatric programs ведёт на 404.* `/fitxpress/for-bariatric-programs/` ещё не опубликован. Пока ставим статью: <https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/|Bariatric pre-qualification ↗>. Она уже на 1-й позиции по «mobile body scanning software remote bmi verification». Когда выйдет лендинг, поменяем ссылку.

*Стоит поправить*
2. *Блок «Pose and clothing information»*: в тексте только Clothing Detector. Добавь туда же строку про RTPV: «Real-Time Pose Validation (RTPV) gives pose and framing guidance during capture.» Пункт меню «Capture controls» ведёт сюда, и без RTPV в нём половина контролей.
3. *Логотипы*: в общем ряду на страховом и фитнес-лендингах есть Erakulis, здесь его нет. Добавь, порядок оставь (UK Meds и Yazen первыми).
4. *Meta description* 160 знаков, Google режет примерно на 155. Вариант на 148: «Cross-check self-reported weight with FitXpress Smart Scales. Two guided photos support remote BMI verification in clinical and insurance workflows.»
5. *Бренд.* По запросу «fitxpress» Google сейчас показывает только эту страницу, а что такое FitXpress, на ней нигде не сказано. В блок «What is BMI verification?» перед «FitXpress uses two guided smartphone photos…» одну фразу: «FitXpress is 3DLOOK's body-scanning software, available as web and mobile SDKs and an API.»
6. Два H2 подряд заканчиваются на «review process» («From guided capture to your review process» и «Weight and BMI, ready for your review process»). Второй можно просто «What FitXpress returns».
7. В карточке Bariatric «serve as a baseline» → «and becomes the baseline for follow-up».

*Перед публикацией (как договаривались)*
• Liveness: если релиз вышел, убираем «Coming soon» и пишем в настоящем времени; если нет, оставляем.
• Schema: Service + FAQPage (те же пять вопросов) + BreadcrumbList. Форма: общая `FX | LP | Demo` на `#demo`.
