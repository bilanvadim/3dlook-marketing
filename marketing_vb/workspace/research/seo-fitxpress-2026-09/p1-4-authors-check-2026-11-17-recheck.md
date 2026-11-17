---
type: live-check
task: P1-4 (authors + author schema) re-check after Asel's reply
date: 2026-11-17
source: Slack DM D0A1Q2E02P3 ts 1794906150.079519 («Всё, кроме изменения slugs и Reset indexables сделано»)
---

# P1-4: повторна перевірка (2026-11-17)

## Виправлено

- Тимчасовий `/for-connected-and-digital-fitness/` → 301 (Redirection, одна ланка) на `/fitxpress/for-connected-and-digital-fitness/`.
- **Canonical на всіх 8 сторінках авторів = сама сторінка**, `ProfilePage @id` і `Person.url` теж. Профілі пересохранено
  16.11–17.11 (lastmod у author-sitemap), тож Reset indexables не потрібен.
- Whitney: фото (`2026/06/whitney.webp`), біо, LinkedIn. Nadya: фото. Oleksii: біо + LinkedIn. Vitaliy: `sameAs` = лише
  LinkedIn (Website очищено). Те саме в schema постів (вибірка: Whitney, Oleksii, Vitaliy, Nadya).

## Лишилось

1. Службові акаунти: `/author/admin/`, `/developer/`, `/developers_ukraine/`, `/<slug з особистої gmail-адреси>/`, `/seo/` = 200 noindex;
   `?author=1,6,16,23` → 301 на них; `?author=7,9,17,19,20,24–26` = 200 (SEO, HR Department, Test Test …).
   **Сторінка цього акаунта має в `<title>` чужу особисту gmail-адресу** (display name = email).
2. Старі `/content-hub/author/{dana,luke,vitaliy,whitney}/` → 301 Yoast на файл фото (attachment); oleksii, vadim → 301
   на `/author/<slug>/`. Пропозиція: regex 301 `^/content-hub/author/(.*)$` → `/author/$1` у Redirection.
3. Slug не змінено (`oleksii-kaplanskyi3dlook-me`, `nadya`, `luke`, `dana`, `vitaliy`, `whitney`).
4. Дрібниці: Luke без LinkedIn; `jobTitle` немає лише в Nadya.
