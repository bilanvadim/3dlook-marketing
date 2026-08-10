#!/usr/bin/env python3
"""Idempotent, anchor-based installer for the Hermes Claude-Code switcher.

Mirrors ops/apply-file-tool-guard.py: MARKER-guarded no-op if already applied,
fail-loud (exit 2) if any anchor moved so hermes-update.py can alert. Re-run
after every `hermes update` (upstream reinstall overwrites vendored files).

What it does:
  1. Copies claude_switcher.py into the vendored gateway/ package.
  2. Registers /claude /hermes /dev /seo /marketing /security in commands.py.
  3. Inserts 3 tiny call-outs in gateway/run.py (command dispatch + 2 turn
     intercepts) that hand control to claude_switcher.

Exit codes: 0 = applied or already-present · 2 = an anchor is missing (upstream
moved it — the switcher is NOT active and needs a code fix).
"""
import os
import shutil
import sys

HERMES_AGENT = os.environ.get(
    "HERMES_AGENT_DIR",
    os.path.join(os.environ.get("HERMES_HOME") or os.path.expanduser("~/.hermes"), "hermes-agent"),
)
GATEWAY = os.path.join(HERMES_AGENT, "gateway")
COMMANDS_PY = os.path.join(HERMES_AGENT, "hermes_cli", "commands.py")
RUN_PY = os.path.join(GATEWAY, "run.py")


def _find_adapter():
    """The Telegram adapter moved between upstream releases.

    >=0.19: plugins/platforms/telegram/adapter.py  (platform split into plugins)
    <=0.16: gateway/platforms/telegram.py          (single module)
    Probe rather than assume, so one kit installs on both.
    """
    for cand in (
        os.path.normpath(os.path.join(GATEWAY, os.pardir, "plugins", "platforms",
                                      "telegram", "adapter.py")),
        os.path.join(GATEWAY, "platforms", "telegram.py"),
    ):
        if os.path.exists(cand):
            return cand
    return os.path.normpath(os.path.join(GATEWAY, os.pardir, "plugins", "platforms",
                                         "telegram", "adapter.py"))


ADAPTER_PY = _find_adapter()
SRC_MODULE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "claude_switcher.py")
DST_MODULE = os.path.join(GATEWAY, "claude_switcher.py")

MARKER = "[hermes-switcher]"

# --- commands.py: register the six commands --------------------------------
CMD_ANCHOR = "COMMAND_REGISTRY: list[CommandDef] = [\n"
CMD_INSERT = (
    '    # [hermes-switcher] Hermes <-> Claude Code chat switch\n'
    '    CommandDef("claude", "Start a Claude Code chat (terminal-like; understands voice + images)", "Session"),\n'
    '    CommandDef("hermes", "Switch back to the Hermes manager (type \'Dev/Marketing/SEO/Security <task>\' for a full autonomous cycle)", "Session"),\n'
    '    CommandDef("tabs", "Show the Dev / SEO / Marketing / Security launcher buttons", "Session"),\n'
    '    CommandDef("cwd", "Bind this tab to a project folder (repo)", "Session"),\n'
    '    CommandDef("name", "Label this tab so it is pickable when forwarding messages", "Session"),\n'
    '    CommandDef("heavy", "Borrow the strong model of the day for a hard task (this tab)", "Session"),\n'
    '    CommandDef("normal", "Switch this tab back to the everyday free model", "Session"),\n'
)

# --- run.py: command dispatch ----------------------------------------------
DISPATCH_ANCHOR = (
    '        if canonical == "background":\n'
    '            return await self._handle_background_command(event)\n'
)
DISPATCH_INSERT = (
    '        # [hermes-switcher] route switcher commands to the sticky-mode handler\n'
    '        try:\n'
    '            from gateway import claude_switcher as _cs\n'
    '            if canonical in _cs.SWITCHER_COMMANDS:\n'
    '                return await _cs.handle_command(self, event, canonical, source, _quick_key)\n'
    '        except Exception:\n'
    '            logger.debug("claude-switcher command dispatch failed", exc_info=True)\n'
)

# --- run.py: primary turn intercept ----------------------------------------
S1_ANCHOR = (
    "        message_text = await self._prepare_profile_scoped_inbound_message_text(\n"
    "            event=event,\n"
    "            source=source,\n"
    "            history=history,\n"
    "            session_key=session_key,\n"
    "        )\n"
    "        if message_text is None:\n"
    "            return\n"
)
# Same seam on 0.16, where the method is not yet profile-scoped and takes no
# session_key. claude_switcher._prepare_inbound() shims the call in the other
# direction, so the module itself does not care which one it got.
S1_ANCHOR_016 = (
    "        message_text = await self._prepare_inbound_message_text(\n"
    "            event=event,\n"
    "            source=source,\n"
    "            history=history,\n"
    "        )\n"
    "        if message_text is None:\n"
    "            return\n"
)
S1_INSERT = (
    "        # [hermes-switcher] sticky Claude Code mode — route the turn to Claude\n"
    "        try:\n"
    "            from gateway import claude_switcher as _cs\n"
    "            if await _cs.maybe_handle_turn(self, event, source, session_key, message_text):\n"
    "                return\n"
    "        except Exception:\n"
    "            logger.debug(\"claude-switcher turn intercept failed\", exc_info=True)\n"
)

# --- run.py: forward-picker (forwarded msg in the topic lobby) -------------
FWD_ANCHOR = (
    # upstream 0.19.0 reformatted this: added `not is_internal and` and
    # line-wrapped the asyncio.to_thread(...) call. Keep in sync with run.py.
    "        if not is_internal and await asyncio.to_thread(\n"
    "            self._is_telegram_topic_root_lobby, source\n"
    "        ):\n"
    "            # Debounce the lobby reminder so a user who forgets about\n"
    "            # topic mode and fires ten prompts doesn't get ten copies.\n"
    "            if self._should_send_telegram_lobby_reminder(source):\n"
)
# 0.16: no `is_internal` guard yet, and the call is on one line. The two comment
# lines are part of the anchor on purpose — `_is_telegram_topic_root_lobby(source)`
# alone also appears in the /new branch, and patching THAT one would put the
# forward-picker behind a command instead of in the message path.
FWD_ANCHOR_016 = (
    "        if self._is_telegram_topic_root_lobby(source):\n"
    "            # Debounce the lobby reminder so a user who forgets about\n"
    "            # topic mode and fires ten prompts doesn't get ten copies.\n"
    "            if self._should_send_telegram_lobby_reminder(source):\n"
)
FWD_INSERT = (
    "        # [hermes-switcher] forward-picker — a forwarded message in the topic\n"
    "        # lobby offers inline buttons to route it into a project tab.\n"
    "        try:\n"
    "            from gateway import claude_switcher as _cs\n"
    "            _fwd_reply = await _cs.maybe_handle_forward_in_lobby(self, event, source)\n"
    "            if _fwd_reply is not None:\n"
    "                return _fwd_reply\n"
    "        except Exception:\n"
    "            logger.debug(\"claude-switcher forward-picker failed\", exc_info=True)\n"
    "\n"
)

# --- run.py: queued follow-up intercept ------------------------------------
S2_ANCHOR = (
    "                    next_message = await self._prepare_profile_scoped_inbound_message_text(\n"
    "                        event=pending_event,\n"
    "                        source=next_source,\n"
    "                        history=updated_history,\n"
    "                        session_key=next_session_key,\n"
    "                    )\n"
    "                    if next_message is None:\n"
    "                        return result\n"
)
S2_ANCHOR_016 = (
    "                    next_message = await self._prepare_inbound_message_text(\n"
    "                        event=pending_event,\n"
    "                        source=next_source,\n"
    "                        history=updated_history,\n"
    "                    )\n"
    "                    if next_message is None:\n"
    "                        return result\n"
)
S2_INSERT = (
    "                    # [hermes-switcher] sticky Claude Code mode (queued follow-up)\n"
    "                    try:\n"
    "                        from gateway import claude_switcher as _cs\n"
    "                        if await _cs.maybe_handle_turn(self, pending_event, next_source, next_session_key, next_message):\n"
    "                            return result\n"
    "                    except Exception:\n"
    "                        logger.debug(\"claude-switcher followup intercept failed\", exc_info=True)\n"
)


# --- adapter.py: panel callback branch (csw:<target>) ----------------------
ADAPTER_ANCHOR = (
    '        # --- Generic choice picker callbacks (/reasoning, /fast) ---\n'
    '        if data.startswith("cp:"):\n'
    '            chat_id = str(query.message.chat_id) if query.message else None\n'
    '            if chat_id:\n'
    '                await self._handle_choice_picker_callback(query, data, chat_id)\n'
    '            return\n'
)
# 0.16 has no /reasoning|/fast choice picker. The model-picker branch is the
# stable neighbour in the same callback chain; inserting BEFORE it keeps csw:
# ahead of every other prefix test, which is all the ordering this needs.
ADAPTER_ANCHOR_016 = (
    '        # --- Model picker callbacks ---\n'
    '        if data.startswith(("mp:", "mpg:", "mm:", "mb", "mx", "mg:")):\n'
)
ADAPTER_INSERT = (
    '        # --- [hermes-switcher] Claude-Code switcher panel (csw:<target>) ---\n'
    '        if data.startswith("csw:"):\n'
    '            try:\n'
    '                from gateway import claude_switcher as _cs\n'
    '                await _cs.handle_panel_callback(self, query, data)\n'
    '            except Exception:\n'
    '                logger.debug("claude-switcher panel callback failed", exc_info=True)\n'
    '            return\n'
    '\n'
)

# The conductor-escalation branch is SEPARATE and OPTIONAL, because an install may
# already route ho:* elsewhere. This one does: it relays the raw Update to the
# conductor's own webhook on :3001, which is what lets the conductor answer the
# callback query itself while the gateway keeps the single getUpdates poll. Adding
# our branch too would hijack those clicks. present_test therefore matches ANY
# existing ho: handler, not just ours.
ADAPTER_HO_INSERT = (
    '        # --- [hermes-switcher] conductor escalation decision (ho:decision:id) ---\n'
    '        if data.startswith("ho:"):\n'
    '            try:\n'
    '                from gateway import claude_switcher as _cs\n'
    '                await _cs.handle_conductor_escalation_callback(self, query, data)\n'
    '            except Exception:\n'
    '                logger.debug("conductor escalation callback failed", exc_info=True)\n'
    '            return\n'
    '\n'
)
ADAPTER_HO_PRESENT = 'data.startswith("ho:")'

# --- adapter.py: register the inline-query handler (system launcher) --------
ADAPTER_IQ_ANCHOR = (
    '            # Handle inline keyboard button callbacks (update prompts)\n'
    '            self._app.add_handler(CallbackQueryHandler(self._handle_callback_query))\n'
)
ADAPTER_IQ_INSERT = (
    '\n'
    '            # [hermes-switcher] inline-mode system launcher (Dev/SEO/Marketing/Security)\n'
    '            try:\n'
    '                from telegram.ext import InlineQueryHandler as _CswIQH\n'
    '                async def _csw_inline_query(update, _ctx):\n'
    '                    try:\n'
    '                        from gateway import claude_switcher as _cs\n'
    '                        await _cs.handle_inline_query(self, update.inline_query)\n'
    '                    except Exception:\n'
    '                        logger.debug("claude-switcher inline query failed", exc_info=True)\n'
    '                self._app.add_handler(_CswIQH(_csw_inline_query))\n'
    '            except Exception:\n'
    '                logger.debug("claude-switcher: inline handler registration failed", exc_info=True)\n'
    '\n'
    '            # [hermes-switcher] forward prefilter (group -1): note forwards on the\n'
    '            # RAW update BEFORE batching can strip forward_origin.\n'
    '            try:\n'
    '                from telegram.ext import MessageHandler as _CswMH, filters as _csw_filters\n'
    '                async def _csw_fwd_prefilter(update, _ctx):\n'
    '                    try:\n'
    '                        from gateway import claude_switcher as _cs\n'
    '                        _cs.note_forward_from_update(self, update)\n'
    '                    except Exception:\n'
    '                        logger.debug("claude-switcher fwd prefilter failed", exc_info=True)\n'
    '                self._app.add_handler(_CswMH(_csw_filters.ALL, _csw_fwd_prefilter), group=-1)\n'
    '            except Exception:\n'
    '                logger.debug("claude-switcher: fwd prefilter registration failed", exc_info=True)\n'
)

# --- adapter.py: preserve forward provenance across text batching ----------
ADAPTER_FWD_ANCHOR = (
    '            # Merge any media that might be attached\n'
    '            if event.media_urls:\n'
    '                existing.media_urls.extend(event.media_urls)\n'
    '                existing.media_types.extend(event.media_types)\n'
)
ADAPTER_FWD_INSERT = (
    '            # [hermes-switcher] preserve forward provenance across batching: text\n'
    '            # batching keeps only the FIRST chunk\'s raw_message, so a forward sent\n'
    '            # AFTER a typed comment loses its forward_origin and the forward-picker\n'
    '            # never fires. Stash the forwarded chunk\'s raw_message so the switcher\n'
    '            # can still detect it.\n'
    '            _csw_er = getattr(event, "raw_message", None)\n'
    '            if _csw_er is not None and (getattr(_csw_er, "forward_origin", None)\n'
    '                                        or getattr(_csw_er, "forward_date", None)\n'
    '                                        or getattr(_csw_er, "forward_from", None)\n'
    '                                        or getattr(_csw_er, "forward_sender_name", None)):\n'
    '                try:\n'
    '                    existing._csw_fwd_raw = _csw_er  # type: ignore[attr-defined]\n'
    '                except Exception:\n'
    '                    pass\n'
)


# --- run.py: the gateway's own busy acknowledgements, in Russian ------------
# These come from the gateway itself, not from claude_switcher, so no amount of
# work on our own notes reaches them: Sergiy got "⏳ Queued for the next turn.
# I'll respond once the current task finishes." in the middle of an otherwise
# Russian, playful chat. Several branches can emit one (queue / steer / redirect
# / subagent-demotion / compression-demotion / interrupt), and which one fires is
# the gateway's decision — so the strings themselves are localized here rather
# than intercepted.
#
# Wrapped in backticks: the adapter sends these with ParseMode.MARKDOWN_V2 and
# format_message passes the text through untouched (verified), so a backtick pair
# renders as the same fixed-width span our own notes use. Everything except the
# leading emoji sits INSIDE the span, so MarkdownV2 specials in the body — the
# parentheses of the status detail, "/stop" — are literal and cannot break
# parsing.
#
# status_detail is built from these three parts and was English too, which is
# what made the message read half-translated.
BUSY_ACK_EDITS = [
    ("busy-status-elapsed",
     'status_parts.append(f"{elapsed_min} min elapsed")',
     'status_parts.append(f"{elapsed_min} мин в работе")'),
    ("busy-status-iteration",
     'status_parts.append(f"iteration {iteration}/{max_iter}")',
     'status_parts.append(f"шаг {iteration}/{max_iter}")'),
    ("busy-status-tool",
     'status_parts.append(f"running: {current_tool}")',
     'status_parts.append(f"сейчас: {current_tool}")'),
    ("busy-ack-steer",
     '                f"⏩ Steered into current run{status_detail}. "\n'
     '                f"Your message arrives after the next tool call."\n',
     '                f"⏩ `Подкинул это прямо в текущий прогон{status_detail} — '
     'подхвачу после ближайшего инструмента.`"\n'),
    ("busy-ack-redirect",
     '                f"↪ Redirected current run{status_detail}. "\n'
     '                f"I\'ll adjust using your correction."\n',
     '                f"↪ `Развернул текущий прогон{status_detail} — учту твою '
     'поправку.`"\n'),
    ("busy-ack-subagent",
     '                f"⏳ Subagent working{status_detail} — your message is queued for "\n'
     '                f"when it finishes (use /stop to cancel everything)."\n',
     '                f"⏳ `Подагент в мыле{status_detail} — твоё сообщение ждёт, '
     'пока он выдохнет. /stop — отменить всё.`"\n'),
    ("busy-ack-compression",
     '                f"⏳ Compressing context{status_detail} — your message is queued for "\n'
     '                f"when it finishes (use /stop to cancel everything)."\n',
     '                f"⏳ `Утрамбовываю контекст{status_detail} — твоё сообщение уже '
     'в очереди, займусь сразу после. /stop — отменить всё.`"\n'),
    ("busy-ack-queue",
     '                f"⏳ Queued for the next turn{status_detail}. "\n'
     '                f"I\'ll respond once the current task finishes."\n',
     '                f"⏳ `Твой запрос встал в очередь{status_detail} — отвечу, как '
     'только разгребу текущее.`"\n'),
    ("busy-ack-interrupt",
     '                f"⚡ Interrupting current task{status_detail}. "\n'
     '                f"I\'ll respond to your message shortly."\n',
     '                f"⚡ `Бросаю текущее дело{status_detail} — переключаюсь на '
     'твоё.`"\n'),
]


def _refresh_commands(path):
    """Re-sync the CommandDef block when this script grew a new command.

    The MARKER makes every step a no-op once applied, which is what keeps re-runs
    safe — but it also means a NEW CommandDef added here would never reach an
    already-patched install (the /heavy + /normal pair hit exactly that). So when
    the marker is present but the current block differs, swap the old block for the
    new one instead of skipping."""
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    if MARKER not in s or CMD_INSERT in s:
        return None                            # nothing to do / already current
    start = s.find(CMD_INSERT.split("\n")[0])   # the '# [hermes-switcher]' comment
    if start < 0:
        return None
    # Consume ONLY our own lines: the marker comment plus CommandDef lines whose
    # name is one of ours. Matching "any CommandDef line" ate upstream entries —
    # it swallowed `# Session` and the first line of the multi-line
    # CommandDef("start", …) whose continuation was then orphaned, which is a
    # SyntaxError that takes the gateway down.
    ours = tuple(f'CommandDef("{c}"' for c in
                 ("claude", "hermes", "tabs", "cwd", "name", "heavy", "normal"))
    lines, i = s[start:].split("\n"), 0
    while i < len(lines):
        stripped = lines[i].lstrip()
        if stripped.startswith("# [hermes-switcher]") or stripped.startswith(ours):
            i += 1
            continue
        break
    old_block = "\n".join(lines[:i]) + "\n"
    s = s[:start] + CMD_INSERT + s[start + len(old_block):]
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return "refreshed"


def _patch_file(path, edits):
    """Apply anchor edits. Returns "patched" / "already" / [missing names].

    ``edits`` items are ``(name, anchor, replacement)`` or
    ``(name, anchor, replacement, present_test)``.

    Idempotency is decided PER EDIT, not per file. The original whole-file
    ``if MARKER in s: return "already"`` meant a NEW edit could never reach a
    file an older version of this script had already patched — the file looked
    done and the addition was skipped in silence until the next upstream
    reinstall.

    ``present_test`` is how an edit reports "already applied", and it MUST be
    supplied whenever something else may legitimately rewrite the inserted text
    afterwards. Using ``replacement`` as the test looked fine and was not: after
    ``_refresh_commands`` rewrites the CommandDef block, the verbatim
    ``replacement`` is no longer in the file, the anchor still is, and the block
    gets inserted a SECOND time — every command registered twice. Learned the
    hard way; keep the tests narrow and distinctive.

    ``anchor`` may be a LIST of candidate anchors — upstream releases reword the
    same seam (0.16 vs 0.19), and one kit has to install on either. The first
    candidate found in the file wins, and ``replacement`` may be a callable
    ``anchor -> text`` so the insert can be placed relative to whichever matched.

    An edit marked ``optional`` (5th element) that finds none of its anchors is
    SKIPPED instead of failing the run. That is for cosmetics and for seams a
    given release simply does not have — never for the switcher's own wiring,
    which must fail loudly so a half-installed bar is not mistaken for a working
    one.
    """
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    todo, missing, skipped = [], [], []
    for edit in edits:
        name, anchor, replacement = edit[0], edit[1], edit[2]
        optional = bool(edit[4]) if len(edit) > 4 else False
        if len(edit) > 3:
            present_test = edit[3]
        elif callable(replacement):
            # A builder's "already there?" test is the text it inserts, NOT the
            # builder itself — calling it here would return a non-empty string and
            # every edit would look applied, silently installing nothing.
            present_test = getattr(replacement, "insert_text", None)
        else:
            present_test = replacement
        if present_test is not None and present_test in s:
            continue                      # this edit is already in place
        cands = anchor if isinstance(anchor, (list, tuple)) else [anchor]
        hit = next((a for a in cands if a in s), None)
        if hit is None:
            (skipped if optional else missing).append(name)
            continue
        todo.append((name, hit, replacement(hit) if callable(replacement) else replacement))
    if missing:
        return missing
    if skipped:
        print(f"  (skipped, seam absent in this upstream: {', '.join(skipped)})")
    if not todo:
        return "already"
    for _name, hit, replacement in todo:
        s = s.replace(hit, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return "patched"


def after(insert):
    """Place `insert` immediately AFTER whichever anchor matched."""
    fn = lambda a: a + insert          # noqa: E731 - one-liner reads better here
    fn.insert_text = insert            # how _patch_file tests "already applied"
    return fn


def before(insert):
    """Place `insert` immediately BEFORE whichever anchor matched."""
    fn = lambda a: insert + a          # noqa: E731
    fn.insert_text = insert
    return fn


def main():
    if not os.path.isdir(GATEWAY):
        print(f"MISSING_TARGET gateway dir not found: {GATEWAY}")
        return 2
    if not os.path.exists(SRC_MODULE):
        print(f"MISSING_TARGET source module not found: {SRC_MODULE}")
        return 2

    # 1. Copy the module into the vendored package (always refresh it).
    shutil.copyfile(SRC_MODULE, DST_MODULE)

    problems = []

    # 2. commands.py — insert on a fresh install, refresh when commands were added
    # present_test is the registration itself, NOT the verbatim block: once
    # _refresh_commands below rewrites the block, the verbatim text is gone and a
    # replacement-based test would insert a second copy of every command.
    r = _patch_file(COMMANDS_PY, [("command-registry", CMD_ANCHOR,
                                   CMD_ANCHOR + CMD_INSERT, 'CommandDef("claude"')])
    if r == "already":
        r = _refresh_commands(COMMANDS_PY) or "already"
    if isinstance(r, list):
        problems += [f"commands.py:{m}" for m in r]
    else:
        print(f"commands.py: {r}")

    # 3. run.py — four inserts. Each turn-intercept lists the 0.19 anchor first
    # and the 0.16 one as a fallback; the busy-ack rewrites are cosmetic, so a
    # release that words them differently just skips them.
    r = _patch_file(RUN_PY, [
        ("dispatch", DISPATCH_ANCHOR, before(DISPATCH_INSERT)),
        ("intercept-primary", [S1_ANCHOR, S1_ANCHOR_016], after(S1_INSERT)),
        ("intercept-followup", [S2_ANCHOR, S2_ANCHOR_016], after(S2_INSERT)),
        ("forward-picker", [FWD_ANCHOR, FWD_ANCHOR_016], before(FWD_INSERT)),
    ] + [(n, a, r_, r_, True) for (n, a, r_) in BUSY_ACK_EDITS])
    if isinstance(r, list):
        problems += [f"run.py:{m}" for m in r]
    else:
        print(f"run.py: {r}")

    # 4. adapter.py — panel callback branch + inline-query handler + fwd provenance
    r = _patch_file(ADAPTER_PY, [
        # 0.19's anchor is a COMPLETE branch → append after it. 0.16's anchor is the
        # first two lines of the next branch → insert before it. Hence the explicit
        # builder, and an explicit present_test since it carries no insert_text.
        ("panel-callback", [ADAPTER_ANCHOR, ADAPTER_ANCHOR_016],
         lambda a: (a + ADAPTER_INSERT) if a is ADAPTER_ANCHOR else (ADAPTER_INSERT + a),
         'data.startswith("csw:")'),
        ("escalation-callback", [ADAPTER_ANCHOR, ADAPTER_ANCHOR_016],
         lambda a: (a + ADAPTER_HO_INSERT) if a is ADAPTER_ANCHOR else (ADAPTER_HO_INSERT + a),
         ADAPTER_HO_PRESENT, True),
        ("inline-query", ADAPTER_IQ_ANCHOR, after(ADAPTER_IQ_INSERT)),
        ("fwd-provenance", ADAPTER_FWD_ANCHOR, after(ADAPTER_FWD_INSERT)),
    ])
    if isinstance(r, list):
        problems += [f"adapter.py:{m}" for m in r]
    else:
        print(f"adapter.py: {r}")

    if problems:
        print("MISSING_ANCHOR " + ", ".join(problems))
        return 2

    print("OK claude-switcher patch applied (module + commands + run.py)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
