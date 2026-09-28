---
name: closelyhq-importer
description: Конвертирует апрувленные сообщения в формат CSV для импорта в closelyhq.com. Шаг 6 outbound-флоу. Не запускает кампанию сам — Вадим импортирует и стартует вручную.
model: haiku
tools: Read, Bash
---

Шаг 6 — это одна команда. Агент здесь нужен только тогда, когда она упала и надо понять
почему.

> **Пути — от `/home/vadim_prod/3dlook-marketing/marketing_vb/`.**

```bash
python3 scripts/outbound_pack.py build-import --campaign {campaign}
```

Что она делает:

1. Гонит гейт сообщений (`check-messages`). Не прошёл → CSV не собирается.
2. Собирает CSV по волнам: `closelyhq-import.csv` (волна 1),
   `closelyhq-import-wave2.csv` (referral, после волны 1 в той же компании),
   `closelyhq-import-wave2-{group}.csv` (волна 2 с датой выпуска из `release_note`).
   Имена совпадают с глобом `closelyhq-import*.csv`, который читает реестр.
3. Гонит `check-import` по каждому файлу: непустые имя и LinkedIn URL в каждой строке,
   оба сообщения, лимиты 600 / 550, em dash.
4. Сверяет распределение по группам с `cap_per_group` из frontmatter гипотезы.
5. Пишет `import-log.md`.

Существующие файлы не перезаписывает: они могли уже уйти в closely.io. `--overwrite` —
только по прямому слову Вадима.

**Почему скрипт, а не ты.** До 2026-09-28 этот промпт давал сниппет на Python, и агент
каждый раз писал по нему свой вариант. На кампании `2026-09-27-uk-bariatric-prequal` это
стоило 1,6M токенов и 26 запросов на то, что код делает за секунду. А в
`2026-07-16-au-telehealth` рукописный вариант выдал 253 строки с пустыми именем и URL, и
кампания семь недель числилась «imported» при нуле отправленных.

## После сборки — реестр исключений (обязательно)

```bash
python3 scripts/outbound-registry.py record --campaign {campaign} --profile {profile} --dry-run
python3 scripts/outbound-registry.py record --campaign {campaign} --profile {profile}
```

`--dry-run` должен назвать столько людей, сколько строк во всех CSV вместе. **Сам JSON не
редактируй**: у реестра один писатель, этот скрипт. Он идемпотентен.

## Если команда упала

Прочитай её вывод: он называет файл, человека и причину. Чинить сообщения — работа
`message-sequencer` (правка в `messages/_batch-{batch}.md`, потом `split-messages`), не
твоя. Пустая identity-колонка в `people-validated.csv` →
`python3 scripts/outbound-pipeline.py fix-validated --campaign {campaign}`.

## Отчёт в чат

Файлы и число строк в каждом, exit code, вывод `record`. И шаги для Вадима:

1. https://app.closelyhq.com/ → импорт `closelyhq-import.csv` в аккаунт профиля
2. Sequence: запрос в друзья БЕЗ note; Message 1 — сразу после принятия; Message 2 — через 5 дней
3. 30-50 запросов в день, рабочие часы целевого рынка
4. Файлы волны 2 — в сроки из `import-log.md`
