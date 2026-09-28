# Профили в социальных сетях — полный текст

> Вынесено из `CLAUDE.md` §5 2026-09-28 (токен-диета). `CLAUDE.md` грузится в контекст
> каждой сессии и каждого агента, который открыл файл в `marketing_vb/`; полный текст этой
> секции нужен не всем. В `CLAUDE.md` осталась выжимка с правилами, здесь — полный текст,
> дословно, с обоснованиями и историей. **Кто читает:** тот, кто меняет правила профилей или разбирает спорный пост. `post-drafter` получает правила своего профиля из `brand-assets/linkedin-prompts/{profile}.md`, а не отсюда.
> При расхождении выжимки и этого файла прав этот файл: поправь выжимку.

## 5. Профили в социальных сетях

**Детальная per-profile config: `brand-assets/social-profiles-config.md`** — posts_per_week, product_bias, tone, content_types, length, hashtags.

**`post-drafter` читает не весь этот файл, а свой профиль.**
`scripts/split-linkedin-prompts.py` разрезает мастер на
`brand-assets/linkedin-prompts/{profile}.md` (общие правила + секция профиля: ~4,9 КБ у
company, ~8 КБ у пяти личных вместо 17,6 КБ мастера). Эти шесть файлов **генерируются** —
правится мастер, потом скрипт; `--check` падает с exit 1 при расхождении. Мастер остаётся
источником правды. Секцию `Rules for the five personal profiles` скрипт кладёт **только**
пяти личным профилям — company-страница её не получает.

**Для 6 LinkedIn-профилей источник правды по промпту — `brand-assets/linkedin-post-prompts.md`** (офлайн-копия [Google Doc Вадима](https://docs.google.com/document/d/19KKWLtJv4Jx_hKbgxy0TCWnLXgnHe0-gxGuDj9vA2WQ/edit), синк 2026-08-07): аудитория, рынок, фокус-лист, тон, структура, word count и закрытие для каждого профиля. `post-drafter` обязан прочитать нужную секцию перед написанием любого `linkedin-*` поста. При конфликте с `social-profiles-config.md` выигрывает этот файл — кроме трёх house rules, которые выигрывают всегда: **хештегов нет ни на одном профиле**, **1-2 эмодзи максимум** и **100-170 слов на пяти личных профилях**. Twitter / Instagram / Facebook документ не затрагивает.

**Пять личных LinkedIn-профилей (Katerina · Katya · Nick · Olena · Vadim) с 2026-09-04 имеют свою секцию правил** в том же файле — `Rules for the five personal profiles`, решение Вадима: **100-170 слов, 170 — жёсткий потолок** (было 180-250), короткие предложения (ничего длиннее 30 слов), **локация не объявляется** — ни «Here in Australia…», ни «For US teams…» в первом предложении, ни строки о том, с кем автор говорит каждый день; пост учит одной конкретной вещи, а хук — утверждение, не вопрос. Рынок профиля — это **для кого** пост, а не про что. Механическую половину гейтит `scripts/post-lint.py` (потолок слов, длина предложений, геомаркер в первом предложении, клише «I speak with …»), судейскую — `post-brand-checker` пункты 14-15 (шкала для личных профилей — 15, PASS при 14+). `linkedin-company` этих правил **не** получает: у него свои 180-280 слов и корпоративный регистр.

**Активные профили (9 штук):**

| profile_id | Платформа | Owner | Рынок | Product bias |
|------------|-----------|-------|-------|--------------|
| `twitter-company` | Twitter / X | Vadim manages | — | 100% FX |
| `instagram-company` | Instagram | Vadim manages | — | 100% FX |
| `facebook-company` | Facebook | Vadim manages | — | 100% FX |
| `linkedin-company` | LinkedIn Company | Vadim manages | глобально | 100% FX |
| `linkedin-katerina` | LinkedIn Personal | Katerina Galich (CEO) | UK | 100% FX |
| `linkedin-vadim` | LinkedIn Personal | Vadim Bilan (Marketing) | **Australia** | 100% FX |
| `linkedin-nick` | LinkedIn Personal | Nick Omelchak (BD, USA) | USA | 100% FX |
| `linkedin-olena` | LinkedIn Personal | Olena Kudryavtseva (BD, Europe) | Continental Europe (без UK) | 100% FX |
| `linkedin-katya` | LinkedIn Personal | Kateryna Boichuk (BD, Israel) | Israel + Gulf | 100% FX |

Рынки social-профилей теперь совпадают с outbound-рынками из таблицы ниже.

**Вимкнені:** `linkedin-whitney` (Whitney Cathcart, CCO) — posts_per_week: 0.

**Активувати/вимкнути профіль:** зміни `posts_per_week` в `brand-assets/social-profiles-config.md`.
**Для outbound:** 5 профілів для рассылок, кожен прив'язаний до свого ринку (гео) + свій exclusion registry (`workspace/outbound/exclusions/`):

| profile | Owner | Ринок |
|---------|-------|-------|
| `katerina` | Katerina Galich (CEO) | UK |
| `nick` | Nick Omelchak (BD) | USA |
| `olena` | Olena Kudryavtseva (BD) | Europe / EU |
| `katya` | Kateryna Boichuk (BD) | Israel |
| `vadim` | Vadim Bilan (Marketing) | Australia |

Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна). Деталі — `runners/outbound-runner.md`.

