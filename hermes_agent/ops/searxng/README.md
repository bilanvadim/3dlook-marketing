# SearXNG — веб-поиск для Хермеса

Без него тулсет `web` мёртв: `hermes doctor` пишет
`⚠ web (missing EXA_API_KEY, TAVILY_API_KEY, …)`, и агент не видит интернета.
SearXNG закрывает это бесплатно и без чужих ключей.

## Установка

```bash
mkdir -p ~/.hermes/searxng/config
cp docker-compose.yml apply-settings.sh ~/.hermes/searxng/
cp config/settings.yml.example ~/.hermes/searxng/config/settings.yml
# подставить секрет:
python3 -c "import secrets;print(secrets.token_hex(32))"
$EDITOR ~/.hermes/searxng/config/settings.yml     # secret_key: REPLACE_ME -> сгенерированный
docker volume create hermes-searxng-config
~/.hermes/searxng/apply-settings.sh               # заливает конфиг в volume и стартует
hermes config set SEARXNG_URL http://127.0.0.1:8888   # НЕ сработает: см. грабли
```

Затем **вручную** в `~/.hermes/.env`:

```
SEARXNG_URL=http://127.0.0.1:8888
```

Проверка: `hermes doctor` → `✓ web`.

## Грабли, на которые уже наступили

- **`hermes config set SEARXNG_URL …` не помогает.** Ключ уедет в `config.yaml`
  как custom top-level, а провайдер читает `get_env_value()` — то есть
  `os.environ` или `~/.hermes/.env`. Только `.env`.
- **Конфиг нельзя монтировать из `~/.hermes`.** Домашняя папка 700, контейнер
  (uid 977) в неё не пройдёт и упадёт с `Permission denied: /etc/searxng/settings.yml`.
  Поэтому конфиг живёт в именованном volume `hermes-searxng-config`.
- **Внутри volume файл обязан быть 644.** Под 600 (даже с владельцем 977) воркеры
  granian всё равно получают `Permission denied`. Volume лежит под `/var/lib/docker`,
  так что наружу секрет не светится.
- **`format: json` НЕ включён в дефолтах SearXNG**, а провайдер зовёт
  `/search?format=json`. Без него — пустая выдача.
- **`limiter: false` обязателен** для приватного инстанса, иначе штатный
  rate-limiter отдаёт 429 нашему же агенту.
- **`default_lang: "auto"`** — сервер в Германии, движки геолоцируют выдачу по IP,
  и на русский/французский запрос сыпались немецкие сниппеты.
- Движок `wikidata` в логе даёт `HTTP error 403` — он блокирует IP датацентра.
  Остальные ~20 движков работают, это не поломка.
