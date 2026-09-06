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


def _seam_file(basename):
    """Where a run.py seam lives in THIS upstream.

    0.21 split the 12k-line gateway runner into mixins — run_inbound.py (command
    dispatch, lobby, forward-picker), run_turn.py (the two turn intercepts),
    run_topics.py (Telegram topic recovery), run_busy.py (busy acknowledgements).
    Every seam this kit patches survived the split verbatim or near-verbatim; only
    its FILE changed, which is why 2026-09-05 reported eleven MISSING_ANCHORs at
    once while the code they point at was sitting untouched one module over.

    Probe per seam and fall back to run.py, so one kit installs on the split
    layout and on every release before it.
    """
    cand = os.path.join(GATEWAY, basename)
    return cand if os.path.exists(cand) else RUN_PY


RUN_INBOUND_PY = _seam_file("run_inbound.py")   # dispatch · lobby-topic · forward-picker
RUN_TURN_PY = _seam_file("run_turn.py")         # intercept-primary/followup · media recall
RUN_TOPICS_PY = _seam_file("run_topics.py")     # lobby-no-pin
RUN_BUSY_PY = _seam_file("run_busy.py")         # busy acknowledgements (cosmetic)


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
# 0.20.6 (main @ 89b38ed7) folded the plain slash handlers into a dict —
# `background` became the "bg" key of _gateway_plain_command_handlers() and the
# `if canonical == "background"` branch is gone. The switcher check has to sit
# ahead of that dict lookup, which is the first thing the chain does now.
DISPATCH_ANCHOR_0206 = (
    '        plain_handler = self._gateway_plain_command_handlers().get(canonical)\n'
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
# 0.21 moved the plain-command lookup into `_hm_dispatch_canonical_command` in
# gateway/run_inbound.py, and — the part that matters — changed the RETURN SHAPE:
# the method now answers `(handled, result)` instead of a bare reply string.
# Re-anchoring alone would have installed a handler returning a str where a tuple
# is unpacked, so the insert gets its own variant rather than sharing one.
DISPATCH_ANCHOR_021 = (
    "        plain_handler = (\n"
    "            self._gateway_plain_command_handlers().get(canonical)\n"
    "            or self._gateway_idle_command_handlers().get(canonical)\n"
    "        )\n"
)
DISPATCH_INSERT_021 = (
    '        # [hermes-switcher] route switcher commands to the sticky-mode handler\n'
    '        try:\n'
    '            from gateway import claude_switcher as _cs\n'
    '            if canonical in _cs.SWITCHER_COMMANDS:\n'
    '                return True, await _cs.handle_command(self, event, canonical, source, _quick_key)\n'
    '        except Exception:\n'
    '            logger.debug("claude-switcher command dispatch failed", exc_info=True)\n'
)
# Shared by every variant, so "already applied" survives a shape change.
DISPATCH_PRESENT = "[hermes-switcher] route switcher commands"


# --- run.py: DM lobby («УСІ») opens its own topic ---------------------------
# Placed BEFORE the first _quick_key computation on purpose: the session key, the
# topic-lane checks and the auto-rename lane must all see the NEW lane. Patch it
# after that line and the turn binds to the lobby and only the reply moves.
LOBBY_TOPIC_ANCHOR = (
    "        _quick_key = self._session_key_for_source(source)\n"
)
LOBBY_TOPIC_INSERT = (
    "        # [hermes-switcher] «УСІ» → новий чат: a plain message in the DM lobby\n"
    "        # opens its own topic, and this turn runs there instead of the lobby.\n"
    "        try:\n"
    "            from gateway import claude_switcher as _cs\n"
    "            await _cs.maybe_open_lobby_topic(self, event, source)\n"
    "        except Exception:\n"
    "            logger.debug(\"claude-switcher lobby topic open failed\", exc_info=True)\n"
)

# --- run.py: «Усі» must open a NEW chat, not continue the last one ----------
# Upstream _recover_telegram_topic_thread_id does exactly what its docstring says:
# "Pin DM-topic routing to the user's last-active topic" — a message that arrives
# with NO message_thread_id (which is what the «Усі» / All Messages view sends;
# measured 2026-08-30: raw=None is_topic_message=False) gets re-pointed at the most
# recently bound topic. It runs inside the ADAPTER, ahead of text batching and far
# ahead of the run.py turn hooks, so by the time anything else looks at the source
# the lobby is already gone. That single behaviour is what made every "new chat"
# attempt land in the previous conversation.
#
# Returning None here leaves the source in its lobby shape, which is what
# maybe_open_lobby_topic() needs in order to open a fresh lane.
#
# Trade-off, deliberate: the docstring also claims Telegram "can omit
# message_thread_id ... for some topic-mode DM replies". If that happens, such a
# reply now opens a new chat instead of continuing its own. The DIAG-thread log
# added the same day exists to catch it — every private inbound so far carried a
# real thread id whenever it was genuinely in a topic.
LOBBY_PIN_ANCHOR = (
    "        is_lobby = not inbound or inbound in self._TELEGRAM_GENERAL_TOPIC_IDS\n"
)
LOBBY_PIN_INSERT = (
    "        # [hermes-switcher] «Усі» opens a NEW chat instead of resuming the last\n"
    "        # one — see maybe_open_lobby_topic(). Without this the lobby message is\n"
    "        # pinned to the most recent topic before any hook can see it.\n"
    "        if is_lobby:\n"
    "            return None\n"
)
# 0.21 rewrote _recover_telegram_topic_thread_id (now in gateway/run_topics.py):
# the `is_lobby` name is gone and the test is inverted into an early return for
# the NON-lobby case. Everything past that guard IS the lobby case, so the old
# `if is_lobby: return None` becomes an unconditional one — same behaviour, and
# the guard above is what carries the condition now.
LOBBY_PIN_ANCHOR_021 = (
    '        inbound = str(source.thread_id or "")\n'
    "        if inbound and inbound not in self._TELEGRAM_GENERAL_TOPIC_IDS:\n"
    "            return None\n"
)
LOBBY_PIN_INSERT_021 = (
    "        # [hermes-switcher] «Усі» opens a NEW chat instead of resuming the last\n"
    "        # one — see maybe_open_lobby_topic(). Without this the lobby message is\n"
    "        # pinned to the most recent topic before any hook can see it. The guard\n"
    "        # above already returned for every non-lobby thread, so what remains is\n"
    "        # exactly the old `if is_lobby:` branch with its condition applied.\n"
    "        return None\n"
)
LOBBY_PIN_PRESENT = "[hermes-switcher] «Усі» opens a NEW chat"


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
# 0.21 pulled the turn assembly out of the message handler into
# `_hmwa_prepare_turn` (gateway/run_turn.py), which returns
# ``(_PreparedTurn | str | None, env_tokens)``; the caller drops the turn on any
# non-_PreparedTurn first element. So the intercept's "handled — stop here" is no
# longer a bare `return`: it must hand back upstream's own drop shape, exactly as
# the `if message_text is None` line right above it does. A bare `return` here
# would yield None and blow up unpacking at the call site.
S1_ANCHOR_021 = (
    "        message_text = await self._prepare_profile_scoped_inbound_message_text(\n"
    "            event=event, source=source, history=history, session_key=session_key,\n"
    "        )\n"
    "        if message_text is None:\n"
    "            return None, _session_env_tokens\n"
)
S1_INSERT_021 = (
    "        # [hermes-switcher] sticky Claude Code mode — route the turn to Claude\n"
    "        try:\n"
    "            from gateway import claude_switcher as _cs\n"
    "            if await _cs.maybe_handle_turn(self, event, source, session_key, message_text):\n"
    "                return None, _session_env_tokens\n"
    "        except Exception:\n"
    "            logger.debug(\"claude-switcher turn intercept failed\", exc_info=True)\n"
)
S1_PRESENT = "[hermes-switcher] sticky Claude Code mode — route the turn to Claude"


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
# 0.21 (gateway/run_inbound.py) hoisted the `not is_internal` test into an
# enclosing `if`, so the lobby branch sits one level deeper and the debounce
# comment was reworded. Deeper is the RIGHT place for the picker anyway: a
# self-injected internal event has no forward to offer buttons for.
FWD_ANCHOR_021 = (
    "            if await asyncio.to_thread(self._is_telegram_topic_root_lobby, source):\n"
    "                # Debounced so a user who forgets about topic mode doesn't get ten reminders.\n"
    "                if self._should_send_telegram_lobby_reminder(source):\n"
)
FWD_INSERT_021 = (
    "            # [hermes-switcher] forward-picker — a forwarded message in the topic\n"
    "            # lobby offers inline buttons to route it into a project tab.\n"
    "            try:\n"
    "                from gateway import claude_switcher as _cs\n"
    "                _fwd_reply = await _cs.maybe_handle_forward_in_lobby(self, event, source)\n"
    "                if _fwd_reply is not None:\n"
    "                    return _fwd_reply\n"
    "            except Exception:\n"
    "                logger.debug(\"claude-switcher forward-picker failed\", exc_info=True)\n"
    "\n"
)
FWD_PRESENT = "[hermes-switcher] forward-picker"


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
# 0.21: same seam, two levels shallower (the queued-follow-up block moved out of
# a nested `with` into the body of the turn method in gateway/run_turn.py) and the
# call args are line-folded. `return result` still means the same thing here.
S2_ANCHOR_021 = (
    "            next_message = await self._prepare_profile_scoped_inbound_message_text(\n"
    "                event=pending_event, source=next_source, history=updated_history, session_key=next_session_key,\n"
    "            )\n"
    "            if next_message is None:\n"
    "                return result\n"
)
S2_INSERT_021 = (
    "            # [hermes-switcher] sticky Claude Code mode (queued follow-up)\n"
    "            try:\n"
    "                from gateway import claude_switcher as _cs\n"
    "                if await _cs.maybe_handle_turn(self, pending_event, next_source, next_session_key, next_message):\n"
    "                    return result\n"
    "            except Exception:\n"
    "                logger.debug(\"claude-switcher followup intercept failed\", exc_info=True)\n"
)
S2_PRESENT = "[hermes-switcher] sticky Claude Code mode (queued follow-up)"



# --- run.py: media recall for the turns that DO fall through to Hermes -----
# The Claude paths append their own attachment hint inside claude_switcher, but a
# turn handled by the Hermes agent never passes through them: ask Hermes "изучи
# скриншоты" about a screenshot forwarded into the topic ten minutes ago and it
# has nothing — the pixels went to the routed Claude turn and the ephemeral topic
# they arrived in is deleted. This gives Hermes the paths (it can open one with
# vision_analyze). Applied in a SECOND _patch_file pass anchored on the intercept
# block above, so it lands on a fresh install and on an already-patched run.py
# alike — extending S1_INSERT itself would insert a duplicate intercept on every
# install that already has the old text.
AUG1_ANCHOR = S1_INSERT
AUG1_INSERT = (
    "        # [hermes-switcher] Hermes-bound turn asking about a picture it does not\n"
    "        # carry — hand it what this topic already received.\n"
    "        try:\n"
    "            from gateway import claude_switcher as _cs\n"
    "            message_text = _cs.augment_inbound_for_hermes(\n"
    "                self, event, source, session_key, message_text)\n"
    "        except Exception:\n"
    "            logger.debug(\"claude-switcher media recall failed\", exc_info=True)\n"
)
AUG2_ANCHOR = S2_INSERT
AUG2_INSERT = (
    "                    # [hermes-switcher] media recall for the queued Hermes turn\n"
    "                    try:\n"
    "                        from gateway import claude_switcher as _cs\n"
    "                        next_message = _cs.augment_inbound_for_hermes(\n"
    "                            self, pending_event, next_source, next_session_key, next_message)\n"
    "                    except Exception:\n"
    "                        logger.debug(\"claude-switcher media recall (followup) failed\", exc_info=True)\n"
)
# Both recalls hang off the intercept block the pass above just wrote, so each one
# needs the variant matching whichever intercept landed. The primary insert sits at
# the same indent in both shapes; only the follow-up moved.
AUG1_ANCHOR_021 = S1_INSERT_021
AUG1_PRESENT = "[hermes-switcher] Hermes-bound turn asking about a picture"
AUG2_ANCHOR_021 = S2_INSERT_021
AUG2_INSERT_021 = (
    "            # [hermes-switcher] media recall for the queued Hermes turn\n"
    "            try:\n"
    "                from gateway import claude_switcher as _cs\n"
    "                next_message = _cs.augment_inbound_for_hermes(\n"
    "                    self, pending_event, next_source, next_session_key, next_message)\n"
    "            except Exception:\n"
    "                logger.debug(\"claude-switcher media recall (followup) failed\", exc_info=True)\n"
)
AUG2_PRESENT = "[hermes-switcher] media recall for the queued Hermes turn"


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
# 0.21 replaced the if/elif callback chain with two prefix->handler TABLES. There
# is no longer a `cp:` branch to append to, so both switcher branches go where the
# chain begins — right after the callback context is built and before the first
# table is consulted. That is the same ordering guarantee the old anchor gave:
# csw: and ho: are tested ahead of every upstream prefix.
ADAPTER_ANCHOR_021 = (
    "        data = query.data\n"
    "        cb = self._callback_ctx(query)\n"
    "        # Model picker / generic choice picker (/reasoning, /fast) need a chat id.\n"
)


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

# 0.20 moved handler registration out of connect() into `_register_handlers(self,
# app)`: one indent level shallower, and the Application is a parameter (`app`)
# rather than `self._app`. Derive the variant instead of keeping a second copy —
# the two must never drift.
ADAPTER_IQ_ANCHOR_020 = (
    '        # Handle inline keyboard button callbacks (update prompts)\n'
    '        app.add_handler(CallbackQueryHandler(self._handle_callback_query))\n'
)


def _dedent_to_register_handlers(text):
    lines = [ln[4:] if ln.startswith("    ") else ln for ln in text.split("\n")]
    return "\n".join(lines).replace("self._app.add_handler", "app.add_handler")


ADAPTER_IQ_INSERT_020 = _dedent_to_register_handlers(ADAPTER_IQ_INSERT)
# Distinctive and identical in both variants — safe as the "already applied" test.
ADAPTER_IQ_PRESENT = "[hermes-switcher] inline-mode system launcher"
# 0.21 grew an inline picker OF ITS OWN — a searchable command/skill catalogue
# registered as InlineQueryHandler(self._handle_inline_query) in the default group.
# PTB stops a group at its first matching handler, so a second handler in group 0
# would simply never run; register in group -1 instead and answer ONLY the queries
# that carry a system keyword (which is all the launcher buttons ever produce, via
# switch_inline_query_current_chat), then stop the chain so the two cannot both
# answerInlineQuery for the same id. A bare "@bot …" now reaches upstream's
# catalogue untouched — a deliberate split of one seam that used to be ours alone.
ADAPTER_IQ_ANCHOR_021 = (
    "        app.add_handler(CallbackQueryHandler(self._handle_callback_query))\n"
    "        # Inline command picker; inert until the owner enables inline mode via BotFather /setinline.\n"
    "        app.add_handler(InlineQueryHandler(self._handle_inline_query))\n"
)
ADAPTER_IQ_INSERT_021 = (
    '\n'
    '        # [hermes-switcher] inline-mode system launcher (Dev/SEO/Marketing/Security).\n'
    '        # Group -1 so it is consulted before upstream\'s catalogue; it answers only\n'
    '        # when the query starts with a system keyword and then stops the chain, so\n'
    '        # the two handlers never answer the same inline query.\n'
    '        try:\n'
    '            from telegram.ext import InlineQueryHandler as _CswIQH\n'
    '            from telegram.ext import ApplicationHandlerStop as _CswStop\n'
    '            async def _csw_inline_query(update, _ctx):\n'
    '                _iq = getattr(update, "inline_query", None)\n'
    '                if _iq is None:\n'
    '                    return\n'
    '                try:\n'
    '                    from gateway import claude_switcher as _cs\n'
    '                    _q = (getattr(_iq, "query", "") or "").strip()\n'
    '                    if not _cs._match_system_prefix(_q)[0]:\n'
    '                        return\n'
    '                    await _cs.handle_inline_query(self, _iq)\n'
    '                except Exception:\n'
    '                    logger.debug("claude-switcher inline query failed", exc_info=True)\n'
    '                    return\n'
    '                raise _CswStop\n'
    '            app.add_handler(_CswIQH(_csw_inline_query), group=-1)\n'
    '        except Exception:\n'
    '            logger.debug("claude-switcher: inline handler registration failed", exc_info=True)\n'
    '\n'
    '        # [hermes-switcher] forward prefilter (group -1): note forwards on the\n'
    '        # RAW update BEFORE batching can strip forward_origin.\n'
    '        try:\n'
    '            from telegram.ext import MessageHandler as _CswMH, filters as _csw_filters\n'
    '            async def _csw_fwd_prefilter(update, _ctx):\n'
    '                try:\n'
    '                    from gateway import claude_switcher as _cs\n'
    '                    _cs.note_forward_from_update(self, update)\n'
    '                except Exception:\n'
    '                    logger.debug("claude-switcher fwd prefilter failed", exc_info=True)\n'
    '            app.add_handler(_CswMH(_csw_filters.ALL, _csw_fwd_prefilter), group=-1)\n'
    '        except Exception:\n'
    '            logger.debug("claude-switcher: fwd prefilter registration failed", exc_info=True)\n'
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

# 0.21 moved the text-batch MERGE itself down into gateway/platforms/base.py, where
# it is shared by every platform. Patching a shared base for a Telegram-only concern
# is the wrong blast radius, so hook the Telegram override instead: it already wraps
# super()._enqueue_text_event(), and after that call the merged batch is sitting in
# _pending_text_batches under this event's key. Same stash, same reader, one platform.
ADAPTER_FWD_ANCHOR_021 = (
    "    def _enqueue_text_event(self, event: MessageEvent) -> None:\n"
    '        """Buffer a text chunk, or hold it while delayed delivery must be dropped."""\n'
    "        if self._should_drop_delayed_delivery():\n"
    '            self._hold_inbound_event(event, where="text-enqueue")\n'
    "            return\n"
    "        super()._enqueue_text_event(event)\n"
)
ADAPTER_FWD_INSERT_021 = (
    "        # [hermes-switcher] preserve forward provenance across batching: the merge\n"
    "        # keeps only the FIRST chunk's raw_message, so a forward sent AFTER a typed\n"
    "        # comment loses its forward_origin and the forward-picker never fires. Stash\n"
    "        # the forwarded chunk's raw_message on the pending batch so the switcher can\n"
    "        # still detect it.\n"
    "        try:\n"
    '            _csw_er = getattr(event, "raw_message", None)\n'
    '            if _csw_er is not None and (getattr(_csw_er, "forward_origin", None)\n'
    '                                        or getattr(_csw_er, "forward_date", None)\n'
    '                                        or getattr(_csw_er, "forward_from", None)\n'
    '                                        or getattr(_csw_er, "forward_sender_name", None)):\n'
    "                _csw_pending = self._pending_text_batches.get(self._text_batch_key(event))\n"
    "                if _csw_pending is not None:\n"
    "                    _csw_pending._csw_fwd_raw = _csw_er  # type: ignore[attr-defined]\n"
    "        except Exception:\n"
    "            pass\n"
)
ADAPTER_FWD_PRESENT = "[hermes-switcher] preserve forward provenance across batching"


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

# 0.21 (gateway/run_busy.py) rebuilt this block: the six acknowledgements became
# `head, tail = ...` pairs joined as f"{head}{status_detail}{tail}", and two of the
# three status parts are now read straight off the summary dict. Same six strings,
# new shape — so they get their own edit list. Both lists are optional and their
# anchors are mutually exclusive, so whichever release is installed, the other
# list simply reports "seam absent" and nothing is written twice.
#
# The demoted pair used to share self._BUSY_DEMOTED_TAIL; each branch gets its own
# tail here because "waiting for the subagent" and "waiting for compression" do not
# read the same in Russian. The constant is left in place, just unused by these two.
BUSY_ACK_EDITS_021 = [
    ("busy-status-iteration",
     '                        f"iteration {summary.get(\'api_call_count\', 0)}/{summary.get(\'max_iterations\', 0)}"\n',
     '                        f"шаг {summary.get(\'api_call_count\', 0)}/{summary.get(\'max_iterations\', 0)}"\n'),
    ("busy-status-tool",
     'status_parts.append(f"running: {summary.get(\'current_tool\')}")',
     'status_parts.append(f"сейчас: {summary.get(\'current_tool\')}")'),
    ("busy-ack-steer",
     'head, tail = "⏩ Steered into current run", ". Your message arrives after the next tool call."',
     'head, tail = "⏩ `Подкинул это прямо в текущий прогон", " — подхвачу после ближайшего инструмента.`"'),
    ("busy-ack-redirect",
     'head, tail = "↪ Redirected current run", ". I\'ll adjust using your correction."',
     'head, tail = "↪ `Развернул текущий прогон", " — учту твою поправку.`"'),
    ("busy-ack-subagent",
     'head, tail = "⏳ Subagent working", self._BUSY_DEMOTED_TAIL',
     'head, tail = "⏳ `Подагент в мыле", " — твоё сообщение ждёт, пока он выдохнет. /stop — отменить всё.`"'),
    ("busy-ack-compression",
     'head, tail = "⏳ Compressing context", self._BUSY_DEMOTED_TAIL',
     'head, tail = "⏳ `Утрамбовываю контекст", " — твоё сообщение уже в очереди, займусь сразу после. /stop — отменить всё.`"'),
    ("busy-ack-queue",
     'head, tail = "⏳ Queued for the next turn", ". I\'ll respond once the current task finishes."',
     'head, tail = "⏳ `Твой запрос встал в очередь", " — отвечу, как только разгребу текущее.`"'),
    ("busy-ack-interrupt",
     'head, tail = "⚡ Interrupting current task", ". I\'ll respond to your message shortly."',
     'head, tail = "⚡ `Бросаю текущее дело", " — переключаюсь на твоё.`"'),
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

    A missing anchor fails the RUN (caller exits 2) but no longer discards the
    edits that DID resolve. It used to: ``if missing: return missing`` sat above
    the write, so 0.20 rewording the *inline-query* seam silently dropped the
    ``csw:`` panel branch and the ``ho:`` escalation branch too — every inline
    button in Telegram dead for two days while the reply-keyboard bar (plain
    text, patched in run.py) kept working and made it look installed. Landing
    what resolved keeps one cosmetic drift from taking the whole adapter with it;
    the loud exit 2 still says the install is incomplete.
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
    if skipped:
        print(f"  (skipped, seam absent in this upstream: {', '.join(skipped)})")
    if todo:
        for _name, hit, replacement in todo:
            s = s.replace(hit, replacement, 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
    if missing:
        if todo:
            print(f"  (partial: applied {', '.join(n for n, _, _ in todo)})")
        return missing
    return "patched" if todo else "already"


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

    # 3. run.py seams. 0.21 split the runner into mixins, so each seam is patched in
    # the file _seam_file() resolved for it; on every earlier release those all collapse
    # back to run.py and this is the same three passes it always was. _patch_file
    # re-reads per call, so repeated passes over one file are safe.
    for _target, _edits in (
        (RUN_INBOUND_PY, [
            ("dispatch", [DISPATCH_ANCHOR_021, DISPATCH_ANCHOR, DISPATCH_ANCHOR_0206],
             lambda a: (DISPATCH_INSERT_021 if a is DISPATCH_ANCHOR_021 else DISPATCH_INSERT) + a,
             DISPATCH_PRESENT),
            ("lobby-topic", LOBBY_TOPIC_ANCHOR, before(LOBBY_TOPIC_INSERT)),
            ("forward-picker", [FWD_ANCHOR_021, FWD_ANCHOR, FWD_ANCHOR_016],
             lambda a: (FWD_INSERT_021 if a is FWD_ANCHOR_021 else FWD_INSERT) + a,
             FWD_PRESENT),
        ]),
        (RUN_TOPICS_PY, [
            ("lobby-no-pin", [LOBBY_PIN_ANCHOR_021, LOBBY_PIN_ANCHOR],
             lambda a: a + (LOBBY_PIN_INSERT_021 if a is LOBBY_PIN_ANCHOR_021 else LOBBY_PIN_INSERT),
             LOBBY_PIN_PRESENT),
        ]),
        (RUN_TURN_PY, [
            ("intercept-primary", [S1_ANCHOR_021, S1_ANCHOR, S1_ANCHOR_016],
             lambda a: a + (S1_INSERT_021 if a is S1_ANCHOR_021 else S1_INSERT), S1_PRESENT),
            ("intercept-followup", [S2_ANCHOR_021, S2_ANCHOR, S2_ANCHOR_016],
             lambda a: a + (S2_INSERT_021 if a is S2_ANCHOR_021 else S2_INSERT), S2_PRESENT),
        ]),
        # Cosmetic: the gateway's own busy acknowledgements, in Russian. Both shape
        # variants are listed and both are optional — whichever release is installed,
        # the other list finds none of its anchors and says so instead of failing.
        (RUN_BUSY_PY, [(n, a, r_, r_, True) for (n, a, r_) in BUSY_ACK_EDITS]
                      + [(n, a, r_, r_, True) for (n, a, r_) in BUSY_ACK_EDITS_021]),
    ):
        r = _patch_file(_target, _edits)
        _label = os.path.basename(_target)
        if isinstance(r, list):
            problems += [f"{_label}:{m}" for m in r]
        else:
            print(f"{_label}: {r}")

    # 3b. Media recall for Hermes turns. Separate pass: it is anchored on the intercept
    # blocks the pass above just wrote, and _patch_file re-reads the file, so the same
    # code path works fresh and already-patched.
    r = _patch_file(RUN_TURN_PY, [
        ("media-recall-primary", [AUG1_ANCHOR_021, AUG1_ANCHOR], after(AUG1_INSERT), AUG1_PRESENT),
        ("media-recall-followup", [AUG2_ANCHOR_021, AUG2_ANCHOR],
         lambda a: a + (AUG2_INSERT_021 if a is AUG2_ANCHOR_021 else AUG2_INSERT), AUG2_PRESENT),
    ])
    if isinstance(r, list):
        problems += [f"{os.path.basename(RUN_TURN_PY)}:{m}" for m in r]
    else:
        print(f"{os.path.basename(RUN_TURN_PY)} (media recall): {r}")

    # 4. adapter.py — panel callback branch + ho: relay + inline-query handler + fwd
    # provenance. 0.19/0.21 anchors are complete blocks → append after them; 0.16's is
    # the head of the NEXT branch → insert before it. Hence the explicit builders.
    r = _patch_file(ADAPTER_PY, [
        ("panel-callback", [ADAPTER_ANCHOR_021, ADAPTER_ANCHOR, ADAPTER_ANCHOR_016],
         lambda a: (ADAPTER_INSERT + a) if a is ADAPTER_ANCHOR_016 else (a + ADAPTER_INSERT),
         'data.startswith("csw:")'),
        ("escalation-callback", [ADAPTER_ANCHOR_021, ADAPTER_ANCHOR, ADAPTER_ANCHOR_016],
         lambda a: (ADAPTER_HO_INSERT + a) if a is ADAPTER_ANCHOR_016 else (a + ADAPTER_HO_INSERT),
         ADAPTER_HO_PRESENT, True),
        ("inline-query", [ADAPTER_IQ_ANCHOR_021, ADAPTER_IQ_ANCHOR_020, ADAPTER_IQ_ANCHOR],
         lambda a: a + (ADAPTER_IQ_INSERT_021 if a is ADAPTER_IQ_ANCHOR_021
                        else ADAPTER_IQ_INSERT_020 if a is ADAPTER_IQ_ANCHOR_020
                        else ADAPTER_IQ_INSERT),
         ADAPTER_IQ_PRESENT),
        ("fwd-provenance", [ADAPTER_FWD_ANCHOR_021, ADAPTER_FWD_ANCHOR],
         lambda a: a + (ADAPTER_FWD_INSERT_021 if a is ADAPTER_FWD_ANCHOR_021 else ADAPTER_FWD_INSERT),
         ADAPTER_FWD_PRESENT),
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
