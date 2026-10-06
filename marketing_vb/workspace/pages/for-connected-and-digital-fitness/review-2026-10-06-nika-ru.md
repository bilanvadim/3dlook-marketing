---
product: fitxpress
type: page-review
vertical: connected-and-digital-fitness
language: ru
date: 2026-10-06
for: Nika (Slack #marketing, thread of 2026-10-06)
source: review-2026-10-06-nika.md (Ukrainian, full table) and page-v3-2026-10-06.md
---

# Фитнес-лендинг: разбор твоей версии и v3

Ника, прогнали твою версию фитнес-лендинга через page-builder: агенты, детектор и слепой судья. Прототип v3 (HTML) и текст v3 по блокам приложены отдельными файлами.

## Итог
v3 = твоя версия + новые правила для лендингов «Sell, not educate», которые приняли сегодня (H1 = продукт + аудитория + результат, сначала ценность, потом «как работает», выгода у каждой функции, blog test). Слепой судья: 69 → 71 → 73 из 100, порог 85 не взят. Оценку держат две вещи: на странице нет доказательств именно из фитнеса, а технические проверки (контраст, аналитика, 768 и 1440 px) можно сделать только на сборке в WordPress.

## Что взяли из твоей версии
- Блок выгод для участников. Теперь это колонка «What it changes for the app» в таблице того, что возвращает скан: у каждой функции своя выгода в той же строке.
- H2 «Each scan shows members the body changes a weight log does not record» вырос из твоего «Change the scale can't show».
- FAQ «Will adding a scan step reduce onboarding completion?». Ответ честный: место скана выбирает команда продукта, а пилот измеряет completion до полного запуска.
- Колонку «Standalone scanning app» в сравнении и строку про бренд, который видит участник.
- H2 пилота «Start with a member cohort, then scale on a fixed monthly plan».
- «100+ clients since 2016», теперь это подпись под рядом логотипов.
- Цены Starter и Pro: совпадают с живым /pricing/ (проверено 06.10).

## Решения по странице (06.10)
- H1 на языке приложений: «FitXpress for fitness apps: help retain members with in-app body scanning». Title: «In-App Body Scanning for Fitness Apps | FitXpress», ключ: body scanning for fitness apps. «Gym body scanner» остался вторичным ключом (сравнение и FAQ). Все «app»-ключи со спросом в Ahrefs (body scan app 200, body scanner app 100, body scanning app и body composition app по 50) потребительские: так ищут люди, которым нужно приложение для себя, а не CPO, который покупает SDK.
- «Help retain», а не «retain»: внутренней цифры по удержанию у нас нет (guardrail #1).
- Под hero идет ряд логотипов всех клиентов 3DLOOK. В прототипе пока заглушка, набор логотипов даст дизайн.

**Что пришлось убрать или исправить** (большая часть уже была в разборе 02.10)
1. «95%+ consistency»: жесткий запрет, в proof-points стоит «INTERNAL ONLY, DO NOT PUBLISH». Осталось < 1 cm.
2. Таблица точности по частям тела: только для внутренних материалов. На странице одна фраза о методе (под NDA) и ссылка на статью о точности.
3. Условия съемки («height entered within 2 cm…»): их нет в каноне точности.
4. React Native: в tech-spec прямо «не писать». Публичная формулировка: web and mobile SDKs, including supported iOS and Android integrations.
5. 99.5% uptime SLA, «2 days integration», iOS 15+, размер SDK (40/104 MB), вебхуки без ретраев: источника нет ни в одном нашем файле. Вынесено в вопросы к продукту.
6. «Dedicated customer success manager on every plan»: по живому /pricing/ dedicated support есть только на Personalized, на Starter и Pro guided implementation support.
7. RTPV «with no manual review on your side»: обещание без источника, стало «which helps avoid retakes».
8. «AWS US West (Oregon)»: неполно (основной регион US-West-2, частично US-East-1). Регионы закрывает ссылка на trust-FAQ.
9. GDPR: каноническое предложение дословно, хедж «in most enterprise deployments» не срезаем.
10. «A 30-minute demo»: длительность демо обещает sales, не страница.
11. «A 3D model per scan» (так было и в v2): на живом /pricing/ в Starter 3D-модели нет. 3D Body progress tracking и 3D Goal Visualization есть только в Pro, страница теперь так и пишет.
12. Вернули цифры оттока (Adjust 24% → 7%, JMIR 70%) и метрики пилота с контрольной группой: отток с первого драфта назван главной проблемой, а CPO покупает цифры, на которых можно принять решение.
13. Форма текста: было 22 «you/your» на 1 000 слов при лимите 12,5, en dash в 96–97%, нерасшифрованные SLA, API, TLS, AWS, JSON, CSV, ~1 700 слов при бюджете 1 100–1 300 и 7 FAQ при норме 4–6. Сейчас ~1 335 слов, 4 FAQ, детектор чистый.
14. Блок «Why 3DLOOK» разложили по местам: white-label в полосу фактов, SDK в шаги, поддержку в цены, «100+ clients» к логотипам. У 5 из 9 фактов в нем не было источника.

**Вопрос к тебе:** откуда 95%+, таблица по частям тела, 99.5% SLA, React Native и «2 days integration»? Если это из презентации или подтверждено продуктом, давай сначала внесем в tech-spec и proof-points, тогда сможем вернуть на страницу.
