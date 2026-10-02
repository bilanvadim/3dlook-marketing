---
product: fitxpress
type: page-review
vertical: insurance-underwriting
date: 2026-10-02
compares: page-v2-short.md (09-30) · page-final-2026-10-02.html (передано в дизайн 10-02)
result: правки в page-builder (кіт, humanisation, скоркард, детектор)
---

# Фінал insurance vs наша v2: що змінилося і що пішло в білдер

Вадим 10-02: фінал передано в дизайн, «вивчи текст і внеси правки в білдер». Коментарі Асселі (21 правка з
причинами) лежать у `comments-asselya-2026-10-02.md`, транскрипт фіналу в `page-final-2026-10-02.md`.

## 1. Цифри

| | v2 (09-30) | Фінал (10-02) |
|---|---|---|
| Видимий текст (з макетом форми) | ~1 395 слів | ~1 480 слів |
| «you / your» на 1 000 слів | **23,7** | **12,1** |
| FAQ | 6 | 4 |
| Неголошені акроніми при першій згадці | SDK, API, NDA, BAA, SOC 2, FDA | жодного (HIPAA і GDPR лишились голими) |
| Блок «Keep reading» | є | прибрано, м'який вихід лише біля форми |

## 2. Зміни поза списком Асселі

Ці правки є у фіналі, але в її 21 пункті їх немає. Хтось вніс їх окремо, тому записую:

| # | v2 | Фінал | Що це означає для білдера |
|---|---|---|---|
| 1 | H1 «Remote build and BMI evidence…» | «Second-source build and BMI evidence…» | H1 називає роль продукту в процесі покупця, не канал |
| 2 | Hero: три речення про те, як AU прибрав paramed | «Check disclosed build inside the application, without adding an appointment.» + результат за 45 с | Hero коротший, дія першим словом |
| 3 | H2 проблеми «…got faster. Build evidence got weaker.» | «Why does accelerated underwriting need a second source of build evidence?» | Питальний H2 і в блоці проблеми |
| 4 | «The build field is where it leaks.» | «The remaining gap is independent build evidence.» | Без метафор |
| 5 | «live pose, framing and clothing checks»; FAQ «clothing detector asks for a retake» | «Clothing-related information can be surfaced for review… it does not trigger a retake»; «RTPV pauses capture until…» | **Факт змінився.** Записано в `tech-spec.md` як відкрите питання до продукту: там досі «can prompt corrective action» |
| 6 | Вага «±3.5% average error» | «approximately 3.5% mean absolute error under evaluated conditions» | **Формулювання змінилось.** `proof-points.md` досі каже «real-world conditions». Відкрите питання до Вадима: одне формулювання для всіх каналів |
| 7 | Пілот: «already runs BMI verification inside a UK online-pharmacy order flow… 100+ clients» | «production infrastructure already deployed in remote BMI-verification and weight-management workflows» | Без ринку клієнта і без кількості клієнтів у пілотному блоці |
| 8 | Ціна після кроків пілоту | Ціна одразу під першим абзацом пілоту | Ціна вище в блоці |
| 9 | FAQ «What is accelerated underwriting?» (GEO, US 60) | прибрано | Втрачено GEO-H3 з карти ключів. Якщо це свідомо, наступні лендинги теж не тримають визначальних FAQ; якщо ні, повернути |
| 10 | Фото: «Deleted after processing, or within 30 days under your policy» | «Deleted immediately after processing or retained for up to 30 days under a customer-specific policy» | Формулювання trust-FAQ дослівно, без «your» |
| 11 | Hero без макета | Макет запису з цифрами + підпис «Illustrative example» | Ілюстративний макет дозволений, якщо підписаний |

## 3. Що змінено в білдері (2026-10-02)

- `references/kit-vertical-page.md`: еталон форми → `page-final-2026-10-02.md`; таблиця блоків
  (питальні H2, лінки на першоджерела, «compared with», нейтральні заголовки таблиць, FAQ 4-6 без
  повторів, без «keep reading»); новий розділ **«Register for an enterprise reader»**; слоти 8, 9, 13 і
  чекліст оновлено.
- `references/copy-humanisation.md`: у Layer 0 три нові перевірки детектора; число для «you» (≤ 12,5 на
  1 000); новий **Layer 2b**: дедуплікація і явна конструкція речення.
- `references/gates-and-scorecard.md`: осі Claims discipline, Copy in the buyer's language, Search and AI
  visibility перевіряють нові правила.
- `SKILL.md`, `docs/page-pipeline.md`: FAQ 4-6, еталон, правило регістру.
- `detect-ai-tells.py --channel page`: щільність «you/your», акроніми без розшифрування при першій
  згадці, «vs» у заголовках (м'які house-rule порушення, не hard fail).

## 4. Відкриті питання

1. **HIPAA і GDPR без розшифрування.** Асселя пише, що HIPAA є в списку загальновідомих, але в її Doc
   (перевірено 10-02, змін з 09-28 немає) список такий: AI, WWW, iOS, BMI, CEO, UK, US, EU. Або додати
   HIPAA і GDPR у Doc, або розшифровувати. Детектор поки пропускає їх як на фіналі.
2. **Clothing Detector:** «does not trigger a retake» (фінал) проти «can prompt corrective action»
   (`tech-spec.md`, 09-23). Підтвердити в продукту.
3. **Вага:** «under evaluated conditions» (фінал) проти «real-world conditions» (`proof-points.md`).
4. **FAQ «What is accelerated underwriting?»** прибрано разом із GEO-фразою з карти ключів. Свідомо?
