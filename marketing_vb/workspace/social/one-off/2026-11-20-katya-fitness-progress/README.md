# Katya · FitXpress progress post (one-off, 2026-11-20)

Hlib Hlazovyi wrote a LinkedIn post for Kateryna Boichuk (`linkedin-katya`) and sent it to Vadim in a Slack DM on
2026-11-20 («для Катерины Бойчук такой написал, что скажешь?», D0CC6GESJ90 ts 1795190743.617049). The image he
attached is the 4:5 visual made for Nick's post the day before
(`../2026-11-19-nick-fitness-retention/visual/fitxpress-post-4x5-1080x1350.png`). Vadim: «перевір. О і зроби
краще відео до нього». The post supports Katya's LatAm + MX connected-fitness outbound
(`workspace/outbound/campaigns/2026-11-19-latam-connected-fitness`).

Status: review + rewrite + video ready for Vadim. Not yet sent to Hlib.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's text as sent (140 words) |
| `post/post.md` | Rewrite: 140 words, post-lint PASS (only the one-off `design_tip` / `cta` warnings), avg sentence 9.3 words |
| `visual/hlib-image-as-sent.png` | The image Hlib attached (Nick's US visual, reused) |
| `video/composition/index.html` | HyperFrames composition, 1080×1350, 22 s (edit THIS) |
| `video/build.sh` | Copies the composition + product imagery to `~/.cache/mvb-social-video/oneoff-…/feed/`, runs `check`, renders with `hyperframes@0.9.1`, writes the MP4 to the private repo |
| `video/sound.py` | House sound rules on this composition's scene times: bed from the private library (beat-fitted), earshot effects, −14 LUFS |
| `video/sound.json` | Bed, licence, beat fit and mix levels of the sound version |
| `video/feed-sheet.jpg` | One frame per scene |
| `~/3dlook-marketing-private/social-video/2026-11-20-katya-fitness-progress/` | `…-feed.mp4` (silent) and `…-feed-sound.mp4` |

## Text review (what changed and why)

- **Units.** Inches and pounds → cm and kg. Katya's audiences (outbound LatAm + MX, social brief Israel + Gulf) are
  metric. Same illustrative member as Nick's visual: waist −2.5 cm (= 1 in), weight −0.3 kg (≈ the −0.6 lb card),
  body fat −2%.
- **Hook.** "Most fitness apps lose members between month one and month three because progress looks like noise"
  is an unsourced causal claim about "most" apps. The new hook keeps Hlib's idea as an opinion someone can argue
  with: "Weight alone makes real progress look like noise." (8 words.)
- **Sentence length.** Hlib's 29-word scenario sentence is split into four short lines. Average 17.5 → 9.3 words.
- **Dashes.** Two " - " used as dashes (house hard ban on dash rhetoric) are gone.
- **Rule of thumb.** "Stop asking users to track more often, and start showing…" is a corrective negation (terminology
  guardrails). The recommendation now comes first and the limitation is its own sentence, which ties back to the
  hook: "More frequent logging only adds more noise."
- **Canon.** "80+ body measurements" (guardrails term), "body composition estimates", "under 45 seconds". "Kept under
  your own brand" → "Members compare check-ins in your app, under your brand" (live page: white-label, compare
  between check-ins). The medical-device and coach line is kept as in Nick's approved post.
- **Kept from Hlib:** the scenario, the 4 to 12 week clock, the closing question, 💭, the link as the last line.
- **Overlap with Nick (11-19):** same scenario and product paragraph. Different angle (the logging rule of thumb),
  different audience and units, and a video instead of the shared static image.

## Video

Product story, one line per scene, every line taken from `post/post.md`:

1. Hook on screen from frame 0 (LinkedIn previews take the first frame); a jagged line draws under "noise."
2. Weight chart over 12 weeks: a flat, jittery line, counter to −0.3 kg, "On the scale, that reads as failure."
3. "Same 12 weeks, measured": 3D body models (real render) + progress card, bars for weight / waist / body fat,
   "Illustrative member", "Show the numbers that move on a 4 to 12 week clock."
4. "Two guided phone photos.": real capture UI with a scan sweep, chips 80+ body measurements · Body composition
   estimates · Under 45 seconds.
5. Close: "Members compare check-ins in your app, under your brand.", CTA, landing URL,
   "FitXpress is not a medical device. It doesn't replace a coach."

Imagery: `brand-assets/product-imagery/fitxpress/3d-body-models.webp` and `capture-person-and-phone.webp` (real UI,
INDEX.md). Art direction from the house stat-reel template (navy glow, measurement grid, Satoshi, one electric-blue
accent, no bounce). HyperFrames `check`: 0 errors. Sound: CC BY bed without credit (Vadim, 2026-11-16).
