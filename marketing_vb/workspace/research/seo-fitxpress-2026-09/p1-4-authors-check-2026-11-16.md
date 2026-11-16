---
type: live-check
task: P1-4 (authors + author schema), 2026-09-27-tz-dev-site.md
date: 2026-11-16
---

# P1-4: перевірка сторінок авторів на живому сайті (2026-11-16)

Архіви авторів увімкнули 13.11 (lastmod у `author-sitemap.xml`). Обійдено 164 пости з `post-sitemap.xml`,
8 сторінок авторів і `?author=1…40`.

## Виконано

- Посты переназначено: в schema немає «admin», email чи одного імені. Підпис «By …» = `Person.name` і веде на
  `/author/<slug>/` = `Person.url` у 161 пості (3 ebook-пости без підпису: schema Vadim / Vitaliy).
- `author-sitemap.xml`: 8 авторів з постами (Asselya 54, Vadim 33, Luke 26, Oleksii 13, Nadya 13, Vitaliy 13,
  Dana 11, Whitney 1). `/author/admin/` у sitemap немає.
- Сторінки авторів: фото, ім'я, біо, LinkedIn, статті. Фото в schema = завантажене (не `d=mm`) у 6 з 8.

## Не так

1. **Canonical 6 з 8 сторінок** (Dana, Luke, Vitaliy, Whitney, Oleksii, Vadim) = `/content-hub/author/<slug>/`, а не
   сама сторінка. Для Dana, Luke, Vitaliy, Whitney ця адреса — 301 від Yoast на файл фото (attachment), для Oleksii
   і Vadim — 301 на `/author/<slug>/`. Asselya, Nadya — canonical на себе (профілі збережені пізніше, 13.11 15:53 і
   16:07). Ймовірно, Yoast тримає старий URL з часу, коли автори жили під `/content-hub/author/`. Фікс:
   пересохранити профілі; не допоможе — Yoast Test Helper → Reset indexables.
2. **Slug:** `oleksii-kaplanskyi3dlook-me` зібраний з email; `nadya`, `luke`, `dana`, `vitaliy`, `whitney` — лише ім'я.
   За ТЗ — ім'я-прізвище. Сторінки живуть з 13.11, міняти зараз найдешевше; підписи оновляться самі, старі → 301.
3. **Службові облікові записи відкриті** (200, noindex, не в sitemap): `/author/admin/`, `/author/developer/`,
   `/author/developers_ukraine/`, `/author/<slug з чиєїсь особистої gmail-адреси>/` (повний slug видно через `?author=N`); `?author=N` редиректить на них.
   Ще `?author=7` (SEO), `9` (HR Department), 17, 19, 20, 24–26 рендерять порожню сторінку автора. Для SEO не
   шкодить, але світить логіни. Змінити slug; сторінки авторів без статей → 404 (розробник).
4. **Профілі:** Whitney — без фото, біо, LinkedIn; Nadya — без фото; Oleksii — без біо й LinkedIn; Luke — без
   LinkedIn. Vitaliy: у `sameAs` потрапив `http://3dlook.ai/` (поле Website у профілі) — очистити.

## Дрібниці

- Сторінка автора показує 6 статей + «Show More» (JS), `/page/2/` → 301. Як на /content-hub/, свідомо (P1-6).
- `jobTitle` у schema лише в Asselya.
- Репо: `brand-assets/team/assel-sekerova.md` = «Assel Sekerova», сайт = «Asselya Sekerova».
- Schema aggregation endpoint — вмикати після пп. 1–3.
