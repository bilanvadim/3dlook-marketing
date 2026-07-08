# QUICKSTART — для Вадима

> Самый быстрый путь от «zip распаковал» до «первая outbound кампания запущена».
> Цель: 90 минут.

## 0. Распакуй и открой

```bash
unzip marketing-claude-code.zip
cd marketing-claude-code
code .  # или открой в твоём IDE / Cursor / VS Code
```

## 1. Установи Claude Code (если нет)

```bash
npm install -g @anthropic-ai/claude-code
```

Заведи аккаунт на claude.com, авторизуйся в claude code.

## 2. Прочитай главный контекст (5 минут)

Открой `CLAUDE.md` — там уже всё про 3DLOOK. Проверь что:
- секция 5 (профили в соцсетях) — реальный список твоих профилей. Подредактируй если что-то не так.
- секция 6 (tone of voice) — согласен ли ты с тоном.
- секция 8 (конкуренты) — нужно ли добавить кого-то.

Если что-то поменял — сохрани файл.

## 3. Telegram бот (15 минут)

```bash
cd telegram-bot
cp .env.example .env
# открой .env, впиши:
# TELEGRAM_BOT_TOKEN=xxx (из @BotFather)
# WORKSPACE_PATH=/абсолютный/путь/к/marketing-claude-code
# (запустишь бота, напишешь /start, узнаешь свой chat_id, потом)
# AUTHORIZED_CHAT_IDS=твой_chat_id

pip install -r requirements.txt
python bot.py
# В Telegram написать боту /start — он покажет твой chat_id
# Останови бота (Ctrl+C), допиши AUTHORIZED_CHAT_IDS в .env
# Снова запусти python bot.py
```

Проверь: бот отвечает на /start, не отвечает другим людям.

## 4. Первая outbound кампания (60 минут)

**Это самый быстрый ROI — экономит твоё время на outbound.**

### 4.1 Запусти трек
```bash
# в корне проекта
claude
```
В интерактивном режиме claude code:
```
/outbound
```

Или сразу:
```
/outbound для FitXpress, целимся в life insurance underwriting в США
```

### 4.2 Что произойдёт

1. **hypothesis-generator** напишет гипотезу (~5 минут). Получишь в Telegram. ✅ Approve / ✏️ Edit.

2. **company-researcher** найдёт топ-30 компаний. Получишь список в Telegram. ✅ Approve.

3. **СТОП — твоя работа** (~10 минут): открой Sales Navigator, выгрузи контакты по этим компаниям с фильтрами:
   - Title: «VP Underwriting», «Chief Underwriting Officer», «Head of Digital Innovation»
   - Company: список из шага 2
   - Сохрани CSV → положи в `workspace/outbound/campaigns/{дата}-{slug}/people-raw.csv`
   - В Telegram нажми «Sales Nav готов»

4. **people-extractor** нормализует CSV (~2 мин).

5. **icp-validator** прогонит каждого через ICP — каждый получит метку PASS / WEAK / FAIL. Получишь сводку. ✅ Approve финальный список.

6. **message-sequencer** напишет 4-шаговую цепочку под каждого человека (~10-30 минут в зависимости от числа). Получишь sample в Telegram. ✅ Approve все.

7. **closelyhq-importer** соберёт CSV для closely.io → лежит в `workspace/outbound/campaigns/.../closely-import.csv`.

8. **СТОП — твоя работа**: импортируешь CSV в closely.io, запускаешь кампанию.

9. (Через 2 недели) **response-classifier** + **campaign-analyzer** обработают результаты.

## 5. Что после первой кампании

Когда первая кампания на ходу — добавь:

- **past-posts** в `brand-assets/past-posts/{profile}/` — иначе post-drafter не сможет писать в твоём стиле
- **logos** в `brand-assets/logos/`
- **Figma экспорты** в `brand-assets/past-posts/_figma-exports/`

Тогда можно запускать `/quarterly-review` и `/weekly-posts`.

## Если что-то идёт не так

| Проблема | Решение |
|----------|---------|
| Агент пишет общими словами | Не дочитал product-info. Спроси его явно: «прочитай brand-assets/product-info/proof-points.md и перепиши» |
| Агент придумывает числа | Это критическая ошибка. Реджектни в Telegram, попроси переписать опираясь только на proof-points.md |
| Бот не отвечает | Проверь `AUTHORIZED_CHAT_IDS` в .env, перезапусти |
| В Telegram длинные сообщения обрезаны | Это нормально, текст лежит полностью в файле в `workspace/...` — открой его |
| Сообщения от агентов слишком общие | Добавь больше past-posts, агент опирается на стиль истории |

## Контакты для вопросов

Если что-то непонятно — пингани Серёгу. Архитектуру всей системы он знает.
