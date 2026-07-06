#!/usr/bin/env python3
# ============================================================
# Daily model picker (07:00). Simple & formula-driven.
#   * Look at all live OpenCode Go models + free Zen models.
#   * Pick ONE Go model that balances STRENGTH vs Go-limit headroom:
#       score = strength - cost_weight*output_cost + ctx_bonus*(context>=ctx_big)
#   * Pick the best FREE model (same formula, cost=0) as the fallback.
#   * Write both into Hermes config (primary + fallback_providers), restart, report.
# Run as sergiy_prod. Spends 0 Go requests (uses /models + catalog only).
# ============================================================
import json, time
from router_lib import (env, get_json, ids, load_catalog, telegram, restart_gateway,
                        set_model_default, set_fallback, free_ok, probe_go,
                        ROOT, HOME, GO_BASE, ZEN_BASE)

S   = json.load(open(f"{ROOT}/model-strength.json"))
KEY = env("OPENCODE_GO_API_KEY")
cat = load_catalog()

go_live  = ids(get_json(f"{GO_BASE}/models",  KEY))
zen_live = ids(get_json(f"{ZEN_BASE}/models", KEY))

def strength(m):
    base = m[:-5] if m.endswith("-free") else m
    return S["strength"].get(base, S["default_strength"])

def cost_ctx(provider_key, m):
    md = cat.get(provider_key, {}).get("models", {}).get(m, {})
    return ((md.get("cost") or {}).get("output", 0) or 0), ((md.get("limit") or {}).get("context", 0) or 0)

def go_score(m):
    cost, ctx = cost_ctx("opencode-go", m)
    sc = strength(m) - S["cost_weight"] * cost + (S["ctx_bonus"] if ctx >= S["ctx_big"] else 0)
    return round(sc, 1), strength(m), cost, ctx

# --- rank Go models ---
go_ranked = sorted(((go_score(m)[0], m, go_score(m)) for m in go_live), reverse=True)
go_pick = go_ranked[0][1]
gp = dict(zip(("score", "strength", "cost", "ctx"), go_ranked[0][2]))

# --- free candidates: live Zen ∩ catalog cost.input==0 ---
free_cat  = {k for k, v in cat["opencode"]["models"].items() if (v.get("cost") or {}).get("input", 1) == 0}
free_live = [m for m in zen_live if m in free_cat]
def free_score(m):
    _, ctx = cost_ctx("opencode", m)
    return round(strength(m) + (S["ctx_bonus"] if ctx >= S["ctx_big"] else 0), 1), ctx
free_ranked = sorted(((free_score(m)[0], m, free_score(m)[1]) for m in free_live), reverse=True)
# catalog lists ended promotions as "free" -> verify each actually answers ($0 pings)
free_working = [m for _, m, _ in free_ranked if free_ok(KEY, m)]
free_pick = free_working[0] if free_working else None

# --- write config: primary Go model + native free fallback ---
set_model_default(go_pick)
if free_pick:
    set_fallback(free_pick, provider="opencode-zen")

# --- write pick.json (read by the hourly Go check) ---
json.dump({"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
           "go": go_pick, "free": free_pick,
           "go_score": gp, "go_runners": [{"m": m, "s": s} for s, m, _ in go_ranked[1:4]],
           "free_available": free_working},
          open(f"{ROOT}/pick.json", "w"), indent=2)

restart_gateway()

# --- once-a-day Go health probe (1 request) for the status line ---
go_alive = probe_go(KEY, GO_BASE, go_pick)
go_status = ("доступен ✅" if go_alive is True else
             "в лимите/ошибка ⛔ — Hermes отвечает через free" if go_alive is False else
             "проверить не удалось (сеть) ⚠️")

# --- Telegram report ---
runners = ", ".join(f"{m} ({s})" for s, m, _ in go_ranked[1:4])
bonus = f" + {S['ctx_bonus']}(1M)" if gp["ctx"] >= S["ctx_big"] else ""
msg = (f"🌅 <b>Модель дня</b> {time.strftime('%d.%m %a')}\n\n"
       f"⚙️ <b>Рабочая (Go):</b> <code>{go_pick}</code>\n"
       f"   формула: сила {gp['strength']} − {S['cost_weight']}×{gp['cost']}{bonus} = <b>{gp['score']}</b>\n"
       f"   рядом: {runners}\n\n"
       f"🆓 <b>Fallback при лимите Go:</b> <code>{free_pick or '—'}</code>\n"
       f"   (Hermes сам переключится на неё, если Go упрётся в лимит)\n\n"
       f"📡 <b>Go сейчас:</b> {go_status}\n\n"
       f"free сегодня (рабочие): {', '.join(free_working) or '—'}")
telegram(msg)

print(msg.replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", ""))
