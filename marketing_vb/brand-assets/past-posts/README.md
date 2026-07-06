# Past Posts — Stylistic Anchor for All Content

> **Самая важная папка для консистентности.** Без неё агенты пишут «AI-generic» материал.

## Что класть

### Per-profile (минимум 10, лучше 30)

```
past-posts/
├── linkedin-company/
│   ├── 2026-01-15-fitxpress-glp1-retention.md      # текст поста
│   ├── 2026-01-15-fitxpress-glp1-retention.png     # визуал
│   └── ...
├── linkedin-personal/
│   ├── katerina-galich/
│   │   ├── 2026-01-12-ai-risk-thoughts.md
│   │   └── ...
│   ├── whitney-cathcart/
│   │   └── ...
├── facebook/
└── instagram/
```

### Frontmatter формат для каждого поста

```markdown
---
profile: linkedin-company
date: 2026-01-15
product: fitxpress | mobile_tailor | mixed
format: single | carousel | video | infographic
metrics:
  impressions: 12500
  engagement_rate: 4.2
  clicks: 87
performance: top10 | mid | bottom10
---

[оригинальный текст поста as published]
```

### Визуалы

В той же папке, тот же slug, расширение .png/.jpg/.mp4.

## Дополнительно: Figma экспорты

3DLOOK имеет богатую визуальную базу в Figma:
- **Blog banners:** https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners
- **Website pages:** https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website

Положи в:
```
past-posts/_figma-exports/
├── blog-banners/
│   ├── banner-01-fitxpress-onboarding.png
│   ├── banner-02-bmi-verification.png
│   └── ...
└── website/
    ├── homepage-hero.png
    ├── fitxpress-page.png
    └── ...
```

Это **референс по визуальному стилю** для `visual-brief` агента.

## Сколько

- **Минимум:** 10 постов на каждый активный профиль
- **Идеал:** 30 постов на каждый профиль + 20 Figma экспортов
- **Без чего не работает:** меньше 5 постов = visual-brief не сможет дать качественный бриф

## Зачем агентам

| Агент | Использует для |
|-------|----------------|
| `post-drafter` | Стилевой эталон тона, длины, структуры |
| `visual-brief` | Визуальные паттерны, цвета, композиции |
| `social-analytics` | Базовые метрики для квартального отчёта |
| `quarterly-strategist` | Identifies какие темы заходили |
| `brand-checker` | Сравнивает новый текст с историей на консистентность |

## Workflow для Вадима (как заполнить)

1. **Экспорт LinkedIn:** скрипт или ручной экспорт последних 30 постов с метриками (LinkedIn Analytics дает CSV)
2. **Сохранение текстов:** скопировать в .md с frontmatter
3. **Сохранение визуалов:** скачать PNG из постов
4. **Figma экспорт:** все banners из Blog banners файла → PNG → в `_figma-exports/blog-banners/`
5. **Website экспорт:** ключевые страницы из 3DLOOK website Figma → PNG → в `_figma-exports/website/`

Если ручной экспорт — слишком много, начни с топ-10 постов по engagement и 5 топовых banner'ов из Figma. Это уже даст агентам нужный стилевой контекст.
