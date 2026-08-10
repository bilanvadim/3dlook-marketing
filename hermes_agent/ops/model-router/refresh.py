#!/usr/bin/env python3
# ============================================================
# Daily model picker (07:00). Fully FREE — no paid tiers.
#   * Look at every live OpenCode Zen model that the catalog prices at $0.
#   * Rank them by strength (+ a context bonus) — cost is 0 for all, so the
#     old cost penalty is gone.
#   * Walk that ranking and take the STRONGEST one that answers — vision NOT
#     required. The everyday brain is the strongest thing available even when
#     it is blind; see ops/vision-switch for how images are still read.
#   * Also find the strongest model that PROVES it can see (it must answer a
#     real chat request AND name the colour of a red square) and write it to
#     auxiliary.vision. That is the model Hermes borrows for exactly the turn
#     that carries an image, and drops again the moment plain text arrives.
#   * Next strongest live model becomes the fallback.
#   * Write all three into Hermes config (model.default + fallback_providers +
#     auxiliary.vision), restart only if something changed, report to Telegram.
#
# If NOTHING free answers, config is left ALONE (yesterday's working model keeps
# running) and the report screams about it — better stale and working than fresh
# and dead. Same rule per-role: no proven reader today means auxiliary.vision is
# left exactly as it was rather than pointed at a guess.
#
# Run as vadim_prod. Costs $0: listing + $0 probes on free models only.
#   --dry-run  → probe and print, touch nothing (no config, no restart, no TG)
# ============================================================
import json, logging, re, sys, time, traceback
import free_providers as fp
from router_lib import OPENCODE_CFG as OPENCODE_CFG_PATH
from router_lib import (env, get_json, ids, load_catalog, telegram, restart_gateway,
                        set_model_default, set_fallback, set_opencode_model,
                        set_opencode_auth, free_ok, vision_ok, zen_key,
                        set_moa_council, set_auxiliary_vision, esc,
                        ROOT, ZEN_BASE)

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


DRY = "--dry-run" in sys.argv
PROVIDER = "opencode-zen"
# How many providers off the top of the repo's FREE section get evaluated. The list
# is ordered by how generous the free limits are, so the top few are the only ones
# worth spending probe time on.
TOP_N_PROVIDERS = 3

# --- bootstrap ---------------------------------------------------------------
# All of this used to run bare at module level. get_json has no retry, no cache
# and no except (unlike load_catalog, which does have a cache fallback), so an
# opencode.ai outage, a DNS hiccup or a rotated key at 07:00 killed the process
# before pick.json, before the coder pick and before any Telegram call. The unit
# is Type=oneshot with no OnFailure=, so the only symptom was the morning report
# never arriving — the exact opposite of the "config untouched, but the report
# SCREAMS" contract at the top of this file.
def _zen_models(key, attempts=3):
    last = None
    for i in range(attempts):
        try:
            return ids(get_json(f"{ZEN_BASE}/models", key))
        except Exception as e:
            last = e
            log(f"Zen /models недоступен ({e}) — попытка {i + 1}/{attempts}")
            if i + 1 < attempts:
                time.sleep(20)
    raise last

try:
    S   = json.load(open(f"{ROOT}/model-strength.json"))
    KEY = zen_key()
    cat = load_catalog()
    oc  = cat["opencode"]["models"]
    zen_live = _zen_models(KEY)
except Exception as _boot_exc:
    _why = f"{type(_boot_exc).__name__}: {_boot_exc}"
    log("СТАРТ НЕ УДАЛСЯ:\n" + traceback.format_exc())
    if "--dry-run" not in sys.argv:
        telegram("🚨 <b>Утренний выбор моделей не состоялся</b>\n"
                 f"   Не удалось получить список моделей Zen: <code>{esc(_why)}</code>\n"
                 "   config.yaml НЕ тронут — Hermes работает на вчерашней модели.\n"
                 "   Логи: <code>journalctl --user -u model-router-refresh</code>")
    sys.exit(1)

def strength(m):
    base = m[:-5] if m.endswith("-free") else m
    return S["strength"].get(base, S["default_strength"])

def meta(m):
    md = oc.get(m, {})
    ctx = (md.get("limit") or {}).get("context", 0) or 0
    # Two independent self-reported signals; either one claims vision.
    mods = (md.get("modalities") or {}).get("input") or []
    claims_vision = ("image" in mods) or (md.get("attachment") is True)
    return ctx, claims_vision

def score(m):
    ctx, _ = meta(m)
    return round(strength(m) + (S["ctx_bonus"] if ctx >= S["ctx_big"] else 0), 1)

# --- free candidates: live on Zen AND priced at $0 in the catalog -------------
free_live = [m for m in zen_live if (oc.get(m, {}).get("cost") or {}).get("input", 1) == 0]
ranked = sorted(free_live, key=score, reverse=True)

# --- walk the ranking once and fill three roles ------------------------------
# Vision USED to be a hard gate on the primary, and it cost real strength: the
# best image reader was 62 while the best text-only model was 82. Since the
# reader is now borrowed per-turn (ops/vision-switch) instead of being worn all
# day, the roles are separate:
#   * pick        — the strongest model that answers at all. Text-only is fine.
#   * fallback    — the next strongest that answers, for when the primary's
#                   limit resets. Vision is no longer preferred here either.
#   * best_vision — the strongest model that PROVES it sees (red-square probe).
#                   Goes to auxiliary.vision AND is what vision-switch borrows.
# Only models that CLAIM vision get the image probe: a text-only model answers
# the image part with HTTP 400, so probing them all would burn a minute every
# morning for a guaranteed rejection.
pick = fallback = best_vision = None
probes = []          # [{m, score, strength, ctx, claims, alive, vision, ms, answer, why}]
for m in ranked:
    ctx, claims = meta(m)
    row = {"m": m, "score": score(m), "strength": strength(m), "ctx": ctx,
           "claims_vision": claims, "alive": None, "vision": False, "ms": None,
           "answer": "", "why": "", "role": ""}
    # Stop paying for probes the moment a model can no longer win any role: it
    # is weaker than both text picks, and it cannot beat an already-proven
    # reader. Everything skipped still shows up in the report, marked as such.
    need_text = pick is None or fallback is None
    need_vision = best_vision is None and claims
    if not (need_text or need_vision):
        row["why"] = "слабее — роли уже закрыты, не проверяли"
        probes.append(row); continue

    row["alive"] = free_ok(KEY, m)
    if not row["alive"]:
        row["why"] = "не отвечает (промо закончилось?)"
        probes.append(row); continue

    vfail = ""
    if need_vision:
        v = vision_ok(KEY, m)
        row.update(vision=v["ok"], ms=v["ms"], answer=v["answer"])
        if not v["ok"]:
            vfail = f" · vision-проба провалена: {v['error'] or v['answer'] or '—'}"

    roles = []
    if pick is None:
        pick = m; roles.append("рабочая")
    elif fallback is None:
        fallback = m; roles.append("fallback")
    if best_vision is None and row["vision"]:
        best_vision = m; roles.append("читает картинки")
    row["role"] = " + ".join(roles)
    row["why"] = (("✓ " + row["role"]) if roles else "живая, но роли уже заняты") + vfail
    probes.append(row)

# --- previous pick (read BEFORE overwriting) --------------------------------
try:
    prev = json.load(open(f"{ROOT}/pick.json"))
except Exception:
    prev = {}
prev_primary = prev.get("primary") or prev.get("go")

# --- backup coding agent (OpenCode CLI) ------------------------------------
# Still a separate pick even though Hermes' primary is no longer handicapped by
# the vision gate: the coder looks WIDER than Zen and is judged on different
# evidence (measured speed and a real agent turn, not raw strength). The top free
# providers from cheahjs/free-llm-api-resources, whose order is re-read every
# morning because the maintainer keeps it sorted by how generous the free limits
# are. Zen stays as the safety net when no third-party provider is usable.
zen_coder = None
for m in ranked:
    if m == pick and pick is not None:
        zen_coder = m              # already proven alive above
        break
    if free_ok(KEY, m):
        zen_coder = m
        break

prov_results, missing_keys, provider_order = [], [], []
new_providers, not_reached, unsupported = [], [], []
coder = zen_coder
coder_provider = "opencode"
coder_base = None          # only set for providers whose base URL is templated
try:
    fp.ensure_secrets_file()
    repo_free = fp.parse_free_section(fp.fetch_readme())
    provider_order = [e["name"] for e in repo_free]

    # NEW provider in the repo → Sergiy has to register there before we can use it.
    # Announced only when the newcomer lands INSIDE the competing window: under the
    # top-N rule a provider appearing 20th changes nothing today, and asking him to
    # go register there would be busywork. (`load_seen` returns empty after a source
    # change, which suppresses the one-off wall of "new" providers.)
    seen = fp.load_seen()
    head = [e["name"] for e in repo_free[:TOP_N_PROVIDERS]]
    new_providers = [n for n in head if n not in seen] if seen else []
    # NOT in a dry-run: marking providers as seen is exactly what suppresses the
    # announcement, so a dry-run that wrote it would silently eat the one
    # notification the real run was supposed to send.
    # Only the WINDOW is remembered, not all 29. Recording the whole list would
    # mark a provider sitting at position 9 as "seen" today, so the day it climbs
    # into the top-3 — the day it finally matters — it would no longer count as new
    # and the "зарегистрируйся" block would never fire for it.
    if not DRY:
        fp.save_seen(set(head) | seen)

    # Only the TOP-N of the repo's permanently-free table compete (Sergiy's rule,
    # 2026-08-08). The new source orders providers by how wide their free catalogue
    # is, so the head of the table is where the choice actually lives; probing every
    # provider we happen to hold a key for would spend the morning budget on the
    # tail. Providers below the window keep their keys — they just do not run today.
    window = repo_free[:TOP_N_PROVIDERS]
    known = [e for e in window if e["name"] in fp.PROVIDERS]
    keyed, keyless = [], []
    for e in known:
        (keyed if fp.find_key(fp.PROVIDERS[e["name"]])[0] else keyless).append(e)
    top = keyed
    ask_list = keyless
    unsupported = [e["name"] for e in window if e["name"] not in fp.PROVIDERS]
    log(f"провайдеров в репо: {len(repo_free)} · в топ-{TOP_N_PROVIDERS}: "
        + ", ".join(e["name"] for e in window)
        + f" · с ключом: {len(keyed)} · без ключа: {len(keyless)} · "
        f"не поддержаны: {len(unsupported)}"
        + (f" · НОВЫЕ: {', '.join(new_providers)}" if new_providers else ""))

    hist = fp.load_history()
    stage_t0 = time.monotonic()
    not_reached = []
    for entry in top:
      # Global cap: whatever is left unprobed is named in the report instead of
      # quietly missing.
      if time.monotonic() - stage_t0 > fp.CODER_STAGE_BUDGET_S:
          not_reached.append(entry["name"]); continue
      # Per-provider guard: the whole block used to share ONE try, so a single
      # surprise (OpenRouter's percentile-dict stats) discarded every provider's
      # result and silently fell back to Zen.
      try:
        prov = fp.PROVIDERS[entry["name"]]
        key, src, var = fp.find_key(prov)
        # Progress goes to stdout as it happens (journalctl for the 07:00 run):
        # the whole report is one print at the end, so a stall or a raise in the
        # middle of a multi-minute race left no trace at all.
        log(f"provider {entry['name']}: ключ {'есть' if key else 'НЕТ'}")
        row = {"provider": entry["name"], "id": prov["id"],
               "limits": entry["limits"], "key_var": var, "model": None,
               "score": None, "score_src": None, "probe": None,
               "reference": None, "verdict": ""}
        if not key:
            row["verdict"] = "нет API-ключа"
            prov_results.append(row); continue
        # Cloudflare's base URL carries the account id, so it is only complete once
        # a key exists to look it up with. Failing here beats probing a URL with a
        # literal '{account_id}' in the path and reporting a mystery 404.
        try:
            fp.ensure_base(prov, key, persist=not DRY)
        except Exception as e:
            row["verdict"] = f"не собрать base URL: {str(e)[:50]}"
            prov_results.append(row); continue
        try:
            cands = fp.list_free_models(prov, key, entry, S["strength"],
                                        S["default_strength"])
        except Exception as e:
            row["verdict"] = f"каталог моделей недоступен: {str(e)[:40]}"
            prov_results.append(row); continue
        # The strongest model can be 503 under load — walk a couple down the list
        # rather than writing the whole provider off.
        log(f"  кандидатов {len(cands)}, пробую: "
            f"{', '.join(c['id'] for c in cands[:3]) or '—'}")
        prov_t0 = time.monotonic()
        # Three REAL attempts, plus any number of instant plan rejections. Cloudflare
        # lists models its free plan does not include and there is no flag in the
        # catalogue to tell them apart — the model 403s in 150 ms with "not available
        # on the Workers Free plan". Counting those as attempts meant a provider could
        # burn its whole allowance on three models it was never allowed to call, and
        # look dead. The walk is still bounded: by the provider time budget, and by
        # SKIP_CEILING so a provider that locks EVERYTHING cannot spin forever.
        SKIP_CEILING = 25
        attempts = walked = 0
        skipped_locked = []
        for cand in cands:
            if attempts >= 3 or walked >= SKIP_CEILING:
                break
            walked += 1
            if time.monotonic() - prov_t0 > fp.PROVIDER_BUDGET_S:
                log(f"  бюджет провайдера исчерпан — дальше не пробую")
                row["verdict"] = row["verdict"] or "бюджет времени исчерпан"
                break
            pr = fp.coding_probe(prov, key, cand["id"])
            if not pr["ok"] and fp.plan_locked(pr.get("error")):
                skipped_locked.append(cand["id"])
                log(f"  {cand['id']}: не входит в бесплатный план — пропускаю")
                continue
            attempts += 1
            # Pass or fail, it goes on the record: success_rate cannot come from a log
            # that only kept the wins.
            fp.record_probe(hist, f"{prov['id']}/{cand['id']}", pr)
            log(f"  {cand['id']}: ok={pr['ok']} {pr.get('ms')}мс "
                f"{pr.get('tps')}tok/s {pr.get('error') or ''}")
            row.update(model=cand["id"], score=cand["score"],
                       score_src=cand["score_src"], probe=pr,
                       limits=cand.get("limits") or entry["limits"],
                       rpd=cand.get("rpd"), limits_ok=cand.get("limits_ok", True))
            if pr["ok"]:
                ref = fp.declared_speed(prov, key, cand["id"])
                if not ref:
                    b = fp.baseline_tps(hist, f"{prov['id']}/{cand['id']}")
                    ref = {"tps": b, "source": "наш лучший замер ранее"} if b else {}
                row["reference"] = ref or None
                slow = (ref and ref.get("tps") and pr["tps"]
                        and pr["tps"] < 0.6 * ref["tps"])
                row["verdict"] = ("медленнее обычного — похоже на наплыв"
                                  if slow else "ок")
                break
            row["verdict"] = pr.get("error") or "проба не прошла"
        row["skipped_locked"] = skipped_locked
        # Every model walked was locked behind a paid plan — that is a plan problem,
        # not a broken provider, and the report should say which one it is.
        if skipped_locked and not row.get("probe"):
            row["verdict"] = (f"все проверенные модели ({len(skipped_locked)}) "
                              "недоступны на бесплатном плане")
        prov_results.append(row)
      except Exception as e:
        import traceback
        log(f"  провайдер {entry['name']} упал: {e}")
        logging.debug("provider failed", exc_info=True)
        prov_results.append({"provider": entry["name"],
                             "id": fp.PROVIDERS[entry["name"]]["id"],
                             "limits": entry.get("limits", ""), "key_var": None,
                             "model": None, "score": None, "score_src": None,
                             "probe": None, "reference": None,
                             "verdict": f"ошибка: {str(e)[:60]}"})
    fp.save_history(hist)
    for e in ask_list:
        pv = fp.PROVIDERS[e["name"]]
        missing_keys.append({"provider": e["name"], "var": pv["env"][0],
                             "signup": pv["signup"], "limits": e["limits"],
                             "is_new": e["name"] in new_providers})

    # All survivors are strong enough to write code, so SPEED decides.
    ok_rows = [r for r in prov_results if r["probe"] and r["probe"]["ok"]]
    # Limits gate the WINNER too, not just the pick inside a provider. OpenRouter
    # caps its whole free tier at 50 requests/day, so without this a morning where
    # it happened to be fastest would bind the backup coder to a model that runs out
    # inside one task. A limit-starved model is taken only if nothing else answered.
    ok_rows.sort(key=lambda r: (not r.get("limits_ok", True),
                                -(r["probe"]["tps"] or 0), r["probe"]["ms"]))
    # Walk the ranking and CONFIRM with the real CLI. A model can ace the API probe
    # and still be unusable: Groq's gpt-oss-120b measured 435 tok/s on a 30-token
    # prompt, then rejected every agent turn because the free tier caps at 8000
    # tokens per MINUTE and OpenCode's system prompt is ~38k. Writing the config and
    # walking away would have left the backup coder broken until someone tried it in
    # anger — which is exactly when it is needed.
    # Zen is the last resort, and it must be PROVEN too — falling back to an
    # unverified model would just move the breakage somewhere less visible.
    if zen_coder and not any(r["id"] == "opencode" for r in ok_rows):
        ok_rows.append({"provider": "OpenCode Zen", "id": "opencode",
                        "model": zen_coder, "score": strength(zen_coder),
                        "score_src": "zen fallback", "limits": "", "limits_ok": True,
                        "probe": {"ok": True, "ms": None, "tps": None},
                        "reference": None, "verdict": "подстраховка Zen"})
    # Yesterday's knowledge decides the ORDER of the live checks: a model that has
    # never managed an agent turn should not be retried before one that has, however
    # fast it looks on the API probe.
    # Quality over a window beats today's number: one sample ranks whose queue was
    # empty. Score = p25(tok/s) x success_rate x (1 - CV penalty).
    for r in prov_results:
        if r.get("probe") and r["probe"].get("ok"):
            ref_r = f"{r['id']}/{r['model']}"
            r["score_q"], r["stats"] = fp.quality_score(hist, ref_r, r["probe"].get("tps"))
        else:
            r["score_q"], r["stats"] = 0.0, None

    vmem = fp.load_verified()
    # Snapshot the CURRENT coder config: the loop rewrites it before each check, so if
    # nothing verifies the file would be left pointing at the last thing we tried
    # rather than at the coder that is actually working. Observed exactly that:
    # pick.json said groq while opencode.jsonc had been left on glm-5.2.
    try:
        cfg_before = open(OPENCODE_CFG_PATH).read()
    except Exception:
        cfg_before = None
    ok_rows.sort(key=lambda r: (fp.verify_rank(vmem, f"{r['id']}/{r['model']}"),
                                not r.get("limits_ok", True),
                                -(r.get("score_q") or 0)))
    # Hysteresis. Without it the pick wanders between providers on noise alone — we
    # watched it bounce Google↔Zen on runs minutes apart. The incumbent keeps the job
    # unless a challenger is clearly better (HYSTERESIS x) or the incumbent broke.
    cur_ref = prev.get("coder_ref")
    if cur_ref and len(ok_rows) > 1:
        cur = next((r for r in ok_rows if f"{r['id']}/{r['model']}" == cur_ref), None)
        if cur is not None and cur is not ok_rows[0]:
            best = ok_rows[0].get("score_q") or 0
            # Never promote an incumbent that yesterday's LIVE check disqualified.
            # The list was just sorted by verify_rank for exactly that reason, and
            # hysteresis compares score_q only — which comes from API probes, where
            # a structurally broken model still looks fast. So a coder known not to
            # work was pushed back to position 0 every morning, spending a full
            # agent turn (~38k tokens of system prompt) to fail again and pushing a
            # healthy candidate out of the VERIFY_TOP_N window.
            _cur_rank = fp.verify_rank(vmem, cur_ref)
            _best_rank = fp.verify_rank(vmem, f"{ok_rows[0]['id']}/{ok_rows[0]['model']}")
            if _cur_rank > _best_rank:
                log(f"гистерезис пропущен: {cur_ref} хуже по живой проверке "
                    f"(rank {_cur_rank} против {_best_rank})")
            elif best < (cur.get("score_q") or 0) * fp.HYSTERESIS:
                ok_rows.remove(cur); ok_rows.insert(0, cur)
                log(f"гистерезис: оставляю действующего {cur_ref} "
                    f"(претендент {best:.0f} < {cur.get('score_q', 0):.0f}×{fp.HYSTERESIS})")
    for cand_row in ok_rows[:fp.VERIFY_TOP_N]:
        ref = f"{cand_row['id']}/{cand_row['model']}"
        if DRY:
            coder, coder_provider = cand_row["model"], cand_row["id"]
            cand_row["verified"] = {"ok": None, "detail": "dry-run"}
            break
        _prov = fp.PROVIDERS[cand_row["provider"]]
        k, _, _ = fp.find_key(_prov)
        set_opencode_auth(cand_row["id"], k)
        # A templated base (Cloudflare) has to be written out explicitly — the CLI
        # would otherwise try to interpolate an env var it was never given.
        cand_row["base_url"] = _prov["base"] if _prov.get("_base_templated") else None
        set_opencode_model(cand_row["model"], provider=cand_row["id"],
                           base_url=cand_row["base_url"])
        # Most mornings the pick does not change. Re-proving a coder that is already
        # running and already proven costs a full agent turn for nothing — and those
        # turns are exactly what trips the providers' per-minute quotas.
        if ref == prev.get("coder_ref") and (vmem.get(ref) or {}).get("ok"):
            v = {"ok": True, "detail": "тот же кодер, уже подтверждён — не перепроверяю"}
        else:
            v = fp.verify_backup_agent()
        cand_row["verified"] = v
        if v["ok"] is not None:
            prior = vmem.get(ref) or {}
            # A structural verdict outlives a lucky success (see verify_rank).
            hard = bool(v.get("hard")) or (prior.get("hard") and fp._fresh(prior))
            vmem[ref] = {"ok": bool(v["ok"]) and not hard,
                         "hard": bool(hard),
                         "date": time.strftime("%Y-%m-%d"),
                         "detail": (v["detail"] or prior.get("detail", ""))[:120]}
            if v["ok"] and hard:
                log(f"  {ref}: ответил, но у него известный структурный лимит — не доверяю")
                v = {"ok": False, "detail": "разовый успех при структурном лимите"}
                cand_row["verified"] = v
        log(f"проверка живьём {ref}: {'ok' if v['ok'] else v['ok']} {v['detail']}")
        if v["ok"] is not False:          # True, or None when verification is skipped
            coder, coder_provider = cand_row["model"], cand_row["id"]
            coder_base = cand_row.get("base_url")
            break
        cand_row["verdict"] = f"проба ок, но агент не работает: {v['detail'][:60]}"
    fp.save_verified(vmem)
    # Asked over ok_rows, NOT prov_results — those are two different populations.
    # The Zen safety-net row is appended to ok_rows only (it is synthetic, it has
    # no provider probe behind it), so when Zen won the live check the question
    # "did anything verify?" was being asked of a list Zen was never in. Answer:
    # no. The rollback below then threw away the coder that had just proven
    # itself, restored yesterday's — possibly the broken one we were running from
    # — and reported "НИ ОДИН кандидат не прошёл живую проверку".
    if not any((r.get("verified") or {}).get("ok") for r in ok_rows) \
            and not DRY and ok_rows:
        # Put back exactly what was running, and report the SAME thing in pick.json.
        # Reverting to "the previous pick" is not enough — that pick may itself be
        # the broken one we are running away from.
        if cfg_before is not None:
            open(OPENCODE_CFG_PATH, "w").write(cfg_before)
        restored = None
        for ln in (cfg_before or "").splitlines():
            if '"model"' in ln:
                restored = ln.split('"')[3]
                break
        if restored and "/" in restored:
            coder_provider, coder = restored.split("/", 1)
        else:
            coder, coder_provider = prev.get("coder"), prev.get("coder_provider") or "opencode"
        log(f"НИ ОДИН кандидат не прошёл живую проверку — вернул рабочий конфиг: "
            f"{coder_provider}/{coder}")
except Exception:
    # Print the traceback to stdout too: piping the run through a filter used to
    # swallow the stderr traceback, leaving an empty provider table and no clue.
    import traceback
    log("ОШИБКА выбора кодера — остаюсь на Zen:\n" + traceback.format_exc())
    logging.exception("coder pick via free providers failed — оставляю Zen")

# Compare against what actually gets WRITTEN, not against today's raw pick. On a
# morning where nothing passes the vision probe, best_vision is None while the
# reader on disk stays yesterday's — comparing the two would report a change,
# restart the gateway (killing live sessions) and print "модель сменилась" while
# config.yaml was never touched. And it would do it again every such morning,
# because the carried-over value never converges on None.
vision_written = best_vision or prev.get("best_vision")
# Same trap as best_vision, and it was left open for `fallback`: on a morning
# where only ONE free model is alive, fallback is None, `if fallback:` skips the
# write, config keeps yesterday's — and comparing None against it declared a
# change. Gateway restarted (killing live sessions), report said "модель
# сменилась", and since pick.json carries the old value forward it repeated every
# single morning until a second model came back.
fallback_written = fallback or prev.get("fallback")
changed = bool(pick) and (pick != prev_primary
                          or fallback_written != prev.get("fallback")
                          or vision_written != prev.get("best_vision"))
kept_stale = pick is None

primary_written = False
if pick and not DRY:
    # The return value used to be discarded, while the function rewrites the file
    # either way. A `model:` block whose `default:` line was renamed or commented
    # out meant Hermes silently kept yesterday's model while the report announced
    # the new one — the one value in this whole run where a silent no-op matters
    # most was the only one not checked.
    primary_written = set_model_default(pick, provider=PROVIDER)
    if not primary_written:
        log("model.default НЕ записан: в config.yaml нет строки default: внутри model:")
    if fallback:
        set_fallback(fallback, provider=PROVIDER)

# The image reader, written whether or not the primary changed. A morning with
# no proven reader leaves the slot alone: yesterday's reader is a better guess
# than today's unverified one, and vision-switch checks liveness itself anyway.
aux_written = False
if best_vision and not DRY:
    try:
        aux_written = set_auxiliary_vision(best_vision, provider=PROVIDER)
        log(f"auxiliary.vision → {PROVIDER}/{best_vision}" if aux_written else
            "auxiliary.vision НЕ обновлён: в config нет блока auxiliary.vision")
    except Exception:
        log("auxiliary.vision не обновлён:\n" + traceback.format_exc())
        logging.exception("set_auxiliary_vision failed")

# Keep the MoA council pointed at today's line-up. The aggregator must be the
# primary that was just proven (that is the whole premise of the preset), and the
# advisors are the next live models behind it. Skipped entirely when the config
# has no `moa:` block — an absent preset is a choice, not a gap.
moa_advisors = []
if pick and not DRY:
    for m in ([fallback] if fallback else []) + ranked:
        if not m or m == pick or m in moa_advisors:
            continue
        # `fallback` was already proven alive above; only new candidates cost a ping.
        if m == fallback or free_ok(KEY, m):
            moa_advisors.append(m)
        if len(moa_advisors) == 2:
            break
    if moa_advisors:
        try:
            if not set_moa_council(pick, moa_advisors, provider=PROVIDER):
                moa_advisors = []          # no moa block in config — nothing written
        except Exception:
            moa_advisors = []
            log("MoA-пресет не обновлён:\n" + traceback.format_exc())
            logging.exception("set_moa_council failed")
# The winner's config was already written (and confirmed) inside the loop above.
# This only covers the Zen fallback path, where no third-party provider was usable.
if coder and not DRY and coder_provider == "opencode":
    set_opencode_model(coder, provider=coder_provider)

if not DRY:
    json.dump({"generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
               "primary": pick or prev_primary,
               "primary_provider": PROVIDER,
               # The model ops/vision-switch borrows for an image turn. Carried
               # over when nothing proved out today, so the switch keeps working
               # on yesterday's reader instead of falling back to a blind turn.
               # Same value `changed` was computed from — one variable, so the
               # restart decision and the record can never drift apart.
               "best_vision": vision_written,
               "best_vision_provider": PROVIDER,
               "best_vision_verified_today": bool(best_vision),
               # Kept for readers that predate the split: it now answers "is
               # there a proven image reader", not "is the primary one".
               "vision_verified": bool(best_vision),
               "primary_sees_images": bool(pick) and pick == best_vision,
               "fallback": fallback or prev.get("fallback"),
               "coder": coder or prev.get("coder"),
               "coder_provider": coder_provider,
               "coder_ref": f"{coder_provider}/{coder}" if coder else None,
               "coder_base_url": coder_base,
               "provider_order": provider_order,
               "provider_results": prov_results,
               "missing_keys": [m["var"] for m in missing_keys],
               # `go` is kept as an alias of the primary: the vps-orchestration
               # skill still reads pick.json['go'] for the OpenCode failover.
               "go": pick or prev_primary,
               "free": fallback or prev.get("fallback"),
               "moa_aggregator": pick if moa_advisors else None,
               "moa_advisors": moa_advisors,
               "kept_stale_pick": kept_stale,
               "candidates": probes},
              open(f"{ROOT}/pick.json", "w"), indent=2)

# Restart only on a real change — a no-op pick must not kill an active session.
restarted = None
if changed and not DRY:
    restarted = restart_gateway()

# --- Telegram report --------------------------------------------------------
def line(r):
    tag = ("✅" if r["vision"] else
           "👁️✖" if r["claims_vision"] else "📄")
    ms = f", {r['ms']} мс" if r["ms"] else ""
    return f"   {tag} <code>{r['m']}</code> — сила {r['strength']}, {esc(r['why'])}{ms}"

head = (f"🌅 <b>Модель дня</b> {time.strftime('%d.%m %a')} — только бесплатные\n\n")
if pick:
    top = next(r for r in probes if r["m"] == pick)
    ctx_note = f", контекст {top['ctx']//1000}k" if top["ctx"] else ""
    vis = next((r for r in probes if r["m"] == best_vision), None) if best_vision else None
    if best_vision and best_vision == pick:
        eye = ("👁️ <b>Картинки:</b> читает сама рабочая модель — переключаться "
               "не на кого и не нужно\n\n")
    elif best_vision:
        eye = (f"👁️ <b>Читает картинки:</b> <code>{best_vision}</code> "
               f"(сила {vis['strength'] if vis else '?'})\n"
               f"   на красный квадрат ответила «{esc(vis['answer']) if vis else '—'}» "
               f"за {vis['ms'] if vis else '?'} мс\n"
               f"   беру её ТОЛЬКО на тот ход, где пришла картинка, "
               f"и сразу возвращаюсь на рабочую\n\n"
               + ("" if aux_written or DRY else
                  "   ⚠️ в config.yaml нет блока auxiliary.vision — "
                  "записать её туда не удалось\n\n"))
    else:
        eye = ("🚨 <b>Ни одна бесплатная модель не прошла vision-пробу.</b>\n"
               f"   auxiliary.vision НЕ тронут — остаётся вчерашняя "
               f"<code>{prev.get('best_vision') or '?'}</code>.\n"
               "   Если и она умерла — скриншоты сегодня не прочитаются.\n\n")
    body = (f"⚙️ <b>Рабочая:</b> <code>{pick}</code>\n"
            f"   сильнейшая из живых бесплатных, сила {top['strength']}{ctx_note}"
            + ("" if top["vision"] else " — <b>text-only</b>, и это нормально") + "\n\n"
            + eye
            + f"🆓 <b>Fallback Hermes:</b> <code>{fallback or '—'}</code>\n\n")
else:
    body = (f"🚨 <b>Ни одна бесплатная модель не отвечает.</b>\n"
            f"   config.yaml НЕ тронут — работает вчерашняя "
            f"<code>{prev_primary or '?'}</code>.\n"
            f"   Проверь список ниже: похоже, промо-раздача на Zen закончилась.\n\n")

# Everything below the winner was never probed (we stop at the strongest proven
# one) — list it anyway so the report shows the whole free line-up rather than
# implying only three models exist.
seen = {r["m"] for r in probes}
rest = [m for m in ranked if m not in seen]
rest_line = ("\n   ⏭️ слабее, не проверяли: "
             + ", ".join(f"{m} ({score(m)}{'/👁️' if meta(m)[1] else ''})" for m in rest)
             if rest else "")

# --- backup-coder section: the three providers, measured side by side ---------
# Refusals that a key cannot fix — the account itself needs an action. Without
# this the report shows a raw 401 and reads as "wrong key", sending Sergiy to
# re-issue a token that was never the problem.
_ACCOUNT_ACTIONS = (
    ("bind your alibaba cloud",
     "нужно привязать аккаунт Alibaba Cloud → https://modelscope.ai/my/settings/account "
     "(ключ при этом ВАЛИДНЫЙ, просто бесплатная квота не включена)"),
    ("phone verification",
     "нужно подтвердить телефон в кабинете провайдера"),
)


def _account_hint(text):
    low = (text or "").lower()
    return next((h for sig, h in _ACCOUNT_ACTIONS if sig in low), "")


def _locked_note(r):
    n = r.get("skipped_locked") or []
    return (f"\n      ⏭️ вне бесплатного плана, пропущены: {', '.join(n[:4])}"
            + (f" и ещё {len(n) - 4}" if len(n) > 4 else "")) if n else ""


def prov_line(r):
    if not r["probe"]:
        return f"   ✖ <b>{r['provider']}</b> — {esc(r['verdict'])}{_locked_note(r)}"
    p = r["probe"]
    if not p["ok"]:
        hint = _account_hint(p.get("error") or r["verdict"])
        return (f"   ✖ <b>{r['provider']}</b> · <code>{r['model']}</code> — "
                f"{esc(r['verdict'])} ({p['ms']} мс)"
                + (f"\n      ⚠️ {hint}" if hint else ""))
    ref = r.get("reference") or {}
    refs = (f", заявлено ~{ref['tps']} tok/s ({ref['source']})"
            if ref.get("tps") else ", эталона скорости нет — первый замер")
    mark = "🥇" if f"{r['id']}/{r['model']}" == f"{coder_provider}/{coder}" else "  "
    v = r.get("verified") or {}
    live = ("" if v.get("ok") is None else
            "\n      ✅ проверен живым запуском OpenCode" if v.get("ok") else
            f"\n      ❌ агент НЕ работает: {esc(v.get('detail','')[:90])}")
    rpd = fp.rpd(r["limits"])
    lim = (f"{rpd}/сутки" + ("" if r.get("limits_ok", True) else " ⚠️ мало для агента")
           if rpd else "суточный лимит не заявлен")
    # Otherwise a top-quality row that lost to a structural ban looks arbitrary.
    banned = ""
    try:
        _vm = fp.load_verified().get(f"{r['id']}/{r['model']}") or {}
        if _vm.get("hard"):
            banned = f"\n      ⛔ структурно непригоден: {esc(_vm.get('detail','')[:70])}"
    except Exception:
        banned = ""
    st = r.get("stats") or {}
    q = (f"\n      качество {r.get('score_q', 0):.0f} = p25 {st.get('p25', 0):.0f} tok/s"
         f" × успех {st.get('success_rate', 1):.0%} × разброс {st.get('cv', 0):.0%}"
         f" (замеров {st.get('n', 1)})" if st.get("n") else
         f"\n      качество {r.get('score_q', 0):.0f} (первый замер — со скидкой)")
    return (f"   {mark} <b>{r['provider']}</b> · <code>{r['model']}</code> — сила "
            f"{r['score']} ({r['score_src']}), {lim}\n"
            f"      {p['ms']} мс, {p['tps']} tok/s{refs} → {esc(r['verdict'])}"
            f"{_locked_note(r)}{q}{banned}{live}")

coder_block = ""
if provider_order:
    tested = [r["provider"] for r in prov_results if r.get("probe")]
    coder_block = ("🛠 <b>Запасной кодинг-агент (OpenCode)</b>\n"
                   f"   в репозитории провайдеров: {len(provider_order)}, "
                   f"проверено с ключами: {len(tested)}\n"
                   "   одна и та же задача «форма из 10 полей»; решает КАЧЕСТВО "
                   "(p25 скорости × доля успехов × штраф за разброс), "
                   "при равных — у кого лимиты рабочие:\n"
                   + "\n".join(prov_line(r) for r in prov_results) + "\n\n"
                   f"   ➡️ выбран: <code>{coder_provider}/{coder}</code>\n\n")
    if not_reached:
        coder_block += (f"⏳ не успели в бюджет времени: {', '.join(not_reached)}\n"
                        "   (проверятся завтра первыми — порядок из репозитория)\n\n")
    # A brand-new provider is the one thing that genuinely needs Sergiy TODAY: it
    # landed high in the list because its free limits are good, and we cannot touch
    # it without an account.
    fresh = [m for m in missing_keys if m.get("is_new")]
    rest = [m for m in missing_keys if not m.get("is_new")]
    if fresh:
        coder_block += ("🆕 <b>В репозитории ПОЯВИЛСЯ новый провайдер</b> — "
                        "зарегистрируйся, и он войдёт в отбор:\n"
                        + "\n".join(f"   • <b>{m['provider']}</b> → {m['signup']}\n"
                                    f"     ключ в <code>~/.hermes/ai-models.env</code> "
                                    f"как <code>{m['var']}=…</code>\n"
                                    f"     (лимиты: {m['limits'][:60]})"
                                    for m in fresh) + "\n\n")
    if rest:
        coder_block += ("🔑 <b>Ещё нет ключей</b> (проверить их не можем):\n"
                        + "\n".join(f"   • <b>{m['provider']}</b> → {m['signup']} → "
                                    f"<code>{m['var']}=…</code>"
                                    for m in rest) + "\n\n")
else:
    coder_block = (f"🛠 <b>Запасной кодинг-агент:</b> <code>opencode/{zen_coder}</code> "
                   "(репозиторий провайдеров недоступен — остался Zen)\n\n")

msg = (head + body + coder_block
       + f"📋 <b>Все бесплатные на Zen ({len(ranked)}), по силе:</b>\n"
       + "\n".join(line(r) for r in probes) + rest_line + "\n\n"
       + (f"🎛 совет: {' + '.join(moa_advisors)} → {pick}\n" if moa_advisors else "")
       # Report what HAPPENED, not what was attempted: this line used to claim a
       # restart unconditionally, so a unit that refused to come back looked
       # identical to a clean switch.
       + ("🔄 модель сменилась — gateway перезапущен" if changed and restarted else
          "🔄 модель сменилась, но <b>gateway НЕ перезапустился</b> — "
          "Hermes до сих пор на старой модели, см. journalctl" if changed and restarted is False else
          "🔄 модель сменилась (dry-run — gateway не трогали)" if changed else
          "➖ модель та же — gateway не трогали")
       + ("" if primary_written or not pick or DRY else
          "\n⚠️ <b>model.default НЕ записан</b> в config.yaml — проверь блок model:"))

if DRY:
    print("[dry-run] ничего не записано\n")
    print(msg.replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", ""))
else:
    # telegram() swallows its own failures and returns False, and the return value
    # was dropped — so a rejected message (bad markup, too long, chat gone) looked
    # exactly like a delivered one. Retry once as PLAIN TEXT: a report that arrives
    # ugly beats a morning with no report at all.
    if not telegram(msg):
        plain = re.sub(r"</?(?:b|code|i|u|s|a|pre)(?:\s[^>]*)?>", "", msg)
        log("Telegram отверг HTML-отчёт — отправляю простым текстом")
        if not telegram(plain, parse_mode=None):
            log("Telegram НЕ ПРИНЯЛ отчёт даже простым текстом — смотри вывод выше")
    print(msg.replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", ""))
