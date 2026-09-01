#!/usr/bin/env bash
# Утренний выбор агентной модели: возвращает прокси на список «for agent AI»
# и прогревает цепочку, чтобы к первому разговору была известна живая модель.
#
# Зачем это нужно. Сильный список («for reasoning power») включается по просьбе
# в чате и остаётся активным до тех пор, пока его не сняли. Сильные модели —
# free с жёсткими суточными лимитами, держать их для обычной беседы нельзя.
# Поэтому в 07:00 система возвращается на агентный список сама.
#
# Сам выбор модели внутри списка делает прокси: конфиг Hermes всегда просит
# `auto`, и цепочка перебирается сверху вниз на каждом запросе. Прогревающий
# вызов ниже нужен, чтобы в логе было видно, кто именно отвечает сегодня.
#
# ПОЧЕМУ ЗДЕСЬ ПРОВЕРКА РЕЗУЛЬТАТА, А НЕ ПРОСТО `llmfp use` (правка 24.08.2026).
# `llmfp use <имя>` при незнакомом имени возвращает ненулевой код и НИЧЕГО не
# меняет — активным остаётся вчерашний список. Здесь имя пока верное и
# переключение проходит каждое утро; барьер поставлен ПРЕВЕНТИВНО, потому что на
# соседнем аккаунте ровно это и случилось: списки переименовали, дефолт в скрипте
# остался прежним, и пять дней подряд в лог писалось «не удалось переключить» —
# а лог никто не читает. Активным всё это время оставался список из моделей ОДНОГО
# провайдера, и когда его суточная free-квота выбилась, прокси стал отвечать 502
# на каждый запрос. Пользователю это пришло как «Response remained truncated after
# 4 continuation attempts» — сообщение про обрыв по длине и ни словом про квоту.
# Поэтому теперь: имя разрешается терпимо (точно → регистронезависимо → по
# подстроке), результат ПЕРЕЧИТЫВАЕТСЯ из конфига, одно-провайдерная цепочка
# считается аварией, и о любой аварии приходит сообщение в Telegram.
set -uo pipefail

CONFIG="${LLMFP_CONFIG:-$HOME/.config/llm-failover-proxy/agentic/config.json}"
LIST="${LLMFP_MORNING_LIST:-for agent AI}"
# ЛОГ ПАРАМЕТРИЗОВАН (01.09.2026). Раньше путь был жёстким, и второй инстанс
# (strong) писал бы в тот же файл вперемешку с агентным — а по этому логу
# разбирают утренние аварии. Умолчание прежнее, так что агентный юнит не менялся.
LOG="${LLMFP_MORNING_LOG:-$HOME/.hermes/llmfp-morning.log}"
ROUTER_LIB="${ROUTER_LIB:-$HOME/.hermes/model-router}"
# Ниже этого числа разных провайдеров в активном списке цепочка считается
# хрупкой: исчерпание квоты у одного провайдера убивает все запросы сразу.
MIN_PROVIDERS="${LLMFP_MIN_PROVIDERS:-2}"
# Файл статистики прокси лежит рядом с конфигом: config.json -> config.stats.json.
STATS="${CONFIG%.json}.stats.json"
# Сколько моделей в активной цепочке должны быть живыми и сколько РАЗНЫХ провайдеров
# среди живых. Второе важнее: три живые модели одного провайдера — это одна
# исчерпанная квота до 502 all_providers_failed.
MIN_HEALTHY="${LLMFP_MIN_HEALTHY:-3}"
MIN_HEALTHY_PROVIDERS="${LLMFP_MIN_HEALTHY_PROVIDERS:-2}"

llmfp_bin() {
    if [ -x "$HOME/.local/bin/llmfp" ]; then echo "$HOME/.local/bin/llmfp"; return; fi
    if [ -f "$HOME/.local/lib/node_modules/llm-failover-proxy/dist/index.js" ]; then
        echo "node $HOME/.local/lib/node_modules/llm-failover-proxy/dist/index.js"; return
    fi
    echo "node /usr/lib/node_modules/llm-failover-proxy/dist/index.js"
}

say() { printf '%s %s\n' "$(date '+%F %T')" "$*" >> "$LOG"; }

# Молчаливый сбой этого скрипта стоил пяти дней работы на мёртвой цепочке,
# поэтому об аварии сообщаем в тот же канал, что и авто-обновление.
notify() {
    # Запись в лог ОБЯЗАТЕЛЬНА, а не только отправка. Алерт, который существует лишь в
    # Telegram, невидим при разборе: 28.08.2026 негативный тест порога здоровья нельзя
    # было подтвердить по логу — там была только строка «здоровье: …», и отличить
    # «алерт ушёл» от «условие не сработало» было невозможно.
    say "АЛЕРТ: $(printf '%s' "$1" | tr '\n' ' ' | sed 's/<[^>]*>//g' | cut -c1-200)"
    python3 - "$1" <<'PY' >> "$LOG" 2>&1 || true
import sys, os
sys.path.insert(0, os.path.expanduser(os.environ.get("ROUTER_LIB", "~/.hermes/model-router")))
try:
    import router_lib as rl
    rl.telegram(sys.argv[1])
except Exception as exc:
    print("%s не смог отправить уведомление: %s" % (__import__("datetime").datetime.now(), str(exc)[:120]))
PY
}

# Разрешить имя списка в (id, имя, число_провайдеров). Терпимо к регистру и
# к неполному имени — иначе любое переименование списков снова тихо ломает утро.
resolve_list() {
    LLMFP_WANT="$1" python3 - "$CONFIG" <<'PY'
import json, os, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
want = os.environ["LLMFP_WANT"].strip().lower()
prov = {p["id"]: p.get("name", "?") for p in cfg.get("providers", [])}
lists = cfg.get("modelLists", [])

def providers(lst):
    return {prov.get(m["providerId"], "?") for m in lst.get("models", []) if m.get("enabled")}

hit = None
for pick in (
    lambda l: l.get("name", "").strip().lower() == want,
    lambda l: want in l.get("name", "").strip().lower(),
):
    matches = [l for l in lists if pick(l)]
    if len(matches) == 1:
        hit = matches[0]
        break
    if len(matches) > 1:
        print("AMBIGUOUS\t%s" % ", ".join(l.get("name", "?") for l in matches))
        sys.exit(3)
if hit is None:
    print("NOTFOUND\t%s" % ", ".join(l.get("name", "?") for l in lists))
    sys.exit(2)
print("OK\t%s\t%s\t%d" % (hit["id"], hit.get("name", "?"), len(providers(hit))))
PY
}

# Что активно ПРЯМО СЕЙЧАС — читаем из конфига, а не из кода возврата `use`.
active_list() {
    python3 - "$CONFIG" <<'PY'
import json, sys
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
act = cfg.get("activeListId")
prov = {p["id"]: p.get("name", "?") for p in cfg.get("providers", [])}
for l in cfg.get("modelLists", []):
    if l["id"] == act:
        names = {prov.get(m["providerId"], "?") for m in l.get("models", []) if m.get("enabled")}
        print("%s\t%s\t%d\t%s" % (l["id"], l.get("name", "?"), len(names), ",".join(sorted(names))))
        break
else:
    print("%s\t<неизвестный список>\t0\t" % act)
PY
}

# Здоровье активной цепочки по СТАТИСТИКЕ прокси, а не по флагу enabled.
#
# ЗАЧЕМ ЭТО ОТДЕЛЬНО ОТ MIN_PROVIDERS (правка 27.08.2026). Барьер считал провайдеров
# среди enabled-моделей и каждое утро честно писал «провайдеров: 3». Замер в тот день:
# слот 1 активной цепочки — 1 успех на 88 попыток и постоянный cooldown, слот 3 —
# 10 на 233, и он же был целью хеджа при hedgeDelayMs 5000, то есть почти каждый
# запрос сначала оплачивал 429. Живой моделью в цепочке была фактически одна.
# Флаг enabled не знает ничего о том, отвечает ли модель; статистика знает.
chain_health() {
    python3 - "$CONFIG" "$STATS" <<'PY'
import json, sys, time

cfg = json.load(open(sys.argv[1], encoding="utf-8"))
try:
    stats = json.load(open(sys.argv[2], encoding="utf-8")).get("entries", {}) or {}
except Exception:
    stats = {}

prov = {p["id"]: p.get("name", "?") for p in cfg.get("providers", [])}
act = next((l for l in cfg.get("modelLists", []) if l["id"] == cfg.get("activeListId")), None)
if act is None:
    print("0\t0\t\t<нет активного списка>")
    raise SystemExit

now_ms = time.time() * 1000
healthy, healthy_prov, sick = 0, set(), []
for m in act.get("models", []):
    if not m.get("enabled"):
        continue
    st = stats.get(m.get("id")) or {}
    ok = st.get("successes", st.get("ok", 0)) or 0
    bad = st.get("failures", st.get("fail", 0)) or 0
    try:
        benched = float(st.get("cooldownUntil") or 0) > now_ms
    except Exception:
        benched = False
    # Непробованная модель (0/0) считается живой: она ещё не падала, иначе свежий
    # список читался бы как полная авария.
    tried = ok + bad
    if benched or (tried >= 20 and bad > ok):
        sick.append("%s/%s %d/%d%s" % (prov.get(m["providerId"], "?"), m.get("model"),
                                       ok, bad, " [benched]" if benched else ""))
    else:
        healthy += 1
        healthy_prov.add(prov.get(m["providerId"], "?"))
print("%d\t%d\t%s\t%s" % (healthy, len(healthy_prov),
                           ",".join(sorted(healthy_prov)), "; ".join(sick[:6])))
PY
}

mkdir -p "$(dirname "$LOG")"
BIN="$(llmfp_bin)"
export ROUTER_LIB

# 1. Разрешить целевой список.
RESOLVED="$(resolve_list "$LIST")"; RC=$?
if [ "$RC" != 0 ]; then
    detail="$(printf '%s' "$RESOLVED" | cut -f2-)"
    say "ОШИБКА: список «$LIST» не разрешён ($(printf '%s' "$RESOLVED" | cut -f1)). Есть: $detail"
    notify "⚠️ <b>llmfp: утренний список не найден</b>
Искали «$LIST», прокси такого не знает.
Активная цепочка осталась прежней — проверьте <code>llmfp lists</code>."
    exit 1
fi
WANT_ID="$(printf '%s' "$RESOLVED" | cut -f2)"
WANT_NAME="$(printf '%s' "$RESOLVED" | cut -f3)"
WANT_PROVS="$(printf '%s' "$RESOLVED" | cut -f4)"

# 2. Переключить и ПЕРЕПРОВЕРИТЬ по конфигу (код возврата `use` тут не показатель).
$BIN use "$WANT_NAME" --config "$CONFIG" >/dev/null 2>&1
sleep 1
ACTIVE="$(active_list)"
ACT_ID="$(printf '%s' "$ACTIVE" | cut -f1)"
ACT_NAME="$(printf '%s' "$ACTIVE" | cut -f2)"
ACT_NPROV="$(printf '%s' "$ACTIVE" | cut -f3)"
ACT_PROVS="$(printf '%s' "$ACTIVE" | cut -f4)"

if [ "$ACT_ID" != "$WANT_ID" ]; then
    say "ОШИБКА: просили «$WANT_NAME», активным остался «$ACT_NAME»"
    notify "⚠️ <b>llmfp: список не переключился</b>
Просили «$WANT_NAME», активен «$ACT_NAME» ($ACT_PROVS).
Hermes весь день пойдёт по этой цепочке."
else
    say "список переключён на «$ACT_NAME» (провайдеров: $ACT_NPROV — $ACT_PROVS)"
fi

# 3. Барьер: цепочка на одном провайдере — авария, даже если переключение прошло.
# Именно так выглядел сбой 24.08: список жив, но у единственного провайдера
# кончилась суточная квота, и падали ВСЕ запросы сразу, без остатка.
if [ "${ACT_NPROV:-0}" -lt "$MIN_PROVIDERS" ]; then
    say "ВНИМАНИЕ: в активном списке «$ACT_NAME» всего $ACT_NPROV провайдер(ов) — цепочка хрупкая"
    notify "⚠️ <b>llmfp: цепочка на одном провайдере</b>
Активен «$ACT_NAME»: провайдеров $ACT_NPROV ($ACT_PROVS).
Исчерпание его квоты положит все ответы Hermes сразу — переключите список."
fi

# 3b. То же, но по здоровью, а не по флагам. Барьер выше отвечает на вопрос «сколько
# провайдеров ПЕРЕЧИСЛЕНО», этот — на вопрос «сколько из них сегодня отвечает».
HEALTH_RAW="$(chain_health 2>/dev/null || true)"
N_HEALTHY="$(printf '%s' "$HEALTH_RAW" | cut -f1)"
N_HPROV="$(printf '%s' "$HEALTH_RAW" | cut -f2)"
HPROVS="$(printf '%s' "$HEALTH_RAW" | cut -f3)"
SICK="$(printf '%s' "$HEALTH_RAW" | cut -f4)"
say "здоровье: живых моделей ${N_HEALTHY:-?}, живых провайдеров ${N_HPROV:-?} (${HPROVS:-—}); больные: ${SICK:-нет}"
if [ "${N_HEALTHY:-0}" -lt "$MIN_HEALTHY" ] || [ "${N_HPROV:-0}" -lt "$MIN_HEALTHY_PROVIDERS" ]; then
    notify "⚠️ <b>llmfp: цепочка выглядит полной, а живых моделей мало</b>
Активен «$ACT_NAME»: перечислено провайдеров $ACT_NPROV, но отвечают ${N_HEALTHY:-0} модел(ей) у ${N_HPROV:-0} провайдер(ов) (${HPROVS:-—}).
Не отвечают: <code>${SICK:-—}</code>
Порог: ${MIN_HEALTHY} модел(ей) и ${MIN_HEALTHY_PROVIDERS} провайдер(а). Это то состояние, которое заканчивается 502 all_providers_failed и обрывом ответа на середине."
fi

# 4. Прогреть цепочку и записать, какая модель отвечает сегодня.
PORT=$(python3 -c "import json,sys;print(json.load(open('$CONFIG'))['server']['port'])" 2>/dev/null)
KEY=$(python3 -c "import json,sys;print(json.load(open('$CONFIG'))['server']['apiKey'] or '')" 2>/dev/null)
if [ -n "${PORT:-}" ]; then
    ANSWER=$(curl -sS --max-time 120 -X POST "http://127.0.0.1:$PORT/v1/chat/completions" \
        -H "Authorization: Bearer $KEY" -H 'Content-Type: application/json' \
        -d '{"model":"auto","messages":[{"role":"user","content":"ping"}],"max_tokens":16}' \
        2>/dev/null | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    print(d.get('model','?') if 'choices' in d else 'ошибка: '+str(d.get('error'))[:80])
except Exception as exc:
    print('нет ответа: %s' % str(exc)[:60])
" 2>/dev/null)
    say "утренняя модель дня: ${ANSWER:-неизвестно}"
    case "${ANSWER:-}" in
        ошибка:*|"нет ответа:"*)
            notify "⚠️ <b>llmfp: прогрев не ответил</b>
Список «$ACT_NAME», ответ: <code>${ANSWER}</code>"
            ;;
    esac
fi

# Лог не должен расти без предела.
tail -n 200 "$LOG" > "$LOG.tmp" 2>/dev/null && mv "$LOG.tmp" "$LOG"
