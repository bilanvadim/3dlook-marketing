# Local rules for this machine (3DLOOK marketing VPS), set 2026-11-12

These override anything in AGENT_GUIDE.md / skills where they conflict.

1. **No Remotion.** `remotion-composer/node_modules` is intentionally NOT installed. 3DLOOK has more than 3 employees, so
   Remotion needs a paid Company License (Creators $25/seat/mo; Automators $0.01/render, $100/mo minimum). Do not run
   `npm install` in `remotion-composer/`, `npx remotion ...`, or any `render_demo.py` demo (they are all Remotion).
   Lock `render_runtime` to `hyperframes` or `ffmpeg` at proposal stage. Captions: `remotion_caption_burn` already
   falls back to FFmpeg (`method: ffmpeg_fallback`), or build them in HyperFrames. Only Vadim can lift this rule (if he
   buys a licence).
2. **Python env:** always `source .venv/bin/activate` first (piper, faster-whisper, yt-dlp, mediapipe live there).
   PyAV is pinned `av<17` because faster-whisper 1.2.1 breaks on av 19 (`metadata_errors`). Do not upgrade av blindly.
3. **Paid providers: none configured.** `.env` has no keys. Before adding a key or calling any paid API (fal, ElevenLabs,
   Kling, Veo, OpenAI, HeyGen, etc.), show the cost estimate and get Vadim's OK. The free path works: Piper TTS
   (`en_US-lessac-medium` in `~/.piper/models`), Pixabay music, stock/archive footage, HyperFrames, FFmpeg.
4. **HyperFrames telemetry stays off** (`HYPERFRAMES_NO_TELEMETRY=1` is set in `~/.claude/settings.json` env). Never post
   feedback, renders, or prompts to any public channel, discussion, or issue.
5. **3DLOOK claims rules apply to every script, caption and on-screen text:** client names only as
   `marketing_vb/CLAUDE.md` §1-2 and §6 allow (named live customers; not Generation Tux in new material); no
   wrist-measurement accuracy figures; accuracy wording only verbatim; never "HIPAA compliant"; no em dash. Canon: `~/3dlook-marketing/marketing_vb/brand-assets/product-info/`
   (`compliance.md`, `accuracy-formulations.md`, `proof-points.md`, `roadmap.md`). Do not let the research step invent
   product numbers: product facts come only from there.
6. **Shared VPS, limited RAM** (about 6 GB free; the Hermes gateway runs here and has crashed from RAM pressure). Use
   faster-whisper `small` (not large) on CPU, run one render at a time, and check `free -h` before heavy steps.
7. **Brand:** Satoshi is installed system-wide (`~/.local/share/fonts`) for web and video work; brand tokens are in
   `~/3dlook-marketing/marketing_vb/DESIGN.md`. Reply to Vadim in Ukrainian.
