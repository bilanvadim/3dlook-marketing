# Olena · FitXpress consent-screen post (one-off, 2026-11-24)

Hlib Hlazovyi wrote a LinkedIn post for Olena Kudryavtseva (`linkedin-olena`, Continental Europe) and sent it to
Vadim in the Slack DM on 2026-11-24 («Пост для Лены», D0CC6GESJ90 ts 1795464272.818539), with no image. Vadim:
«подивись і підготуй візуал або відео до нього». The angle (consent, GDPR, photo retention) fits Olena's EU brief
and is new against Nick (retention), Katya (logging cadence) and Vadim (check-in records).

Status: video built and sent to Vadim; nothing sent to Hlib yet.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's text as sent (146 words, post-lint PASS) |
| `post/post.md` | Light edit: 169 words, post-lint PASS (only the one-off `design_tip` / `cta` warnings and the soft rhythm note Hlib's text also has) |
| `video/composition/index.html` | HyperFrames composition, 1080×1350, 23.5 s (edit THIS) |
| `video/build.sh` | Copies the composition + product imagery to `~/.cache/mvb-social-video/oneoff-…/feed/`, runs `check`, renders with `hyperframes@0.9.1`, writes the MP4 to the private repo |
| `video/sound.py` | House sound rules on this composition's scene times: bed from the private library (beat-fitted), earshot effects, −14 LUFS |
| `video/sound.json` | Bed, licence, beat fit and mix levels of the sound version |
| `video/feed-sheet.jpg` | One frame per scene, taken from the final MP4 |
| `~/3dlook-marketing-private/social-video/2026-11-24-olena-fitness-consent/` | `…-feed.mp4` (silent) and `…-feed-sound.mp4` |

## Text review

Hlib's draft already follows the 11-20 rules (no dashes, short sentences, only what the landing says). Checked
against the live landing (curl 2026-11-24) and `compliance.md`:

- **GDPR hedge.** "Under GDPR, your app acts as data controller" drops "in most enterprise deployments", which the
  canon (`compliance.md` §2, CLAUDE.md §12) says must stay: the allocation is contractual. Now: "Under GDPR, in most
  enterprise deployments, your app acts as the data controller." "Owns that clarity" went to make room.
- **Photo lifecycle order.** "Photos are blurred automatically and deleted after processing" reads as if every photo
  is blurred and then deleted. Canon: faces are obfuscated at capture; photos are deleted after processing or kept up
  to 30 days, and kept photos are blurred. Two sentences now, in that order.
- **"members close the screen" → "many members close the screen".** A general claim about behaviour with no source;
  hedged, the point stays.
- **Added one usable rule** (personal-profile rule 4, teach one thing): "Say there, in plain words, where the photos
  go and when they are deleted." It names what the consent screen should hold.
- **Kept:** hook, the SDK/API + white-label line, "Your team controls the consent wording and results view" (landing:
  the platform designs the onboarding, consent and results screens), product canon, medical-device line, the
  question, the link as the last line. No emoji, as Hlib had it.

## Video

1. Hook on screen from frame 0: "If members can't see where the photos go, the scan fails." A dotted route draws
   under "where the photos go".
2. The consent step: a phone opens "another app", a wall of legal text, the retention line ringed in blue
   ("Photo retention: see section 14.3"), the member taps ✕, "Scan closed". Copy: "Another brand. Retention terms
   hidden in legal text. Many members close the screen."
3. Under your brand: the same phone, the app's own consent screen with three plain lines (two guided phone photos ·
   faces obscured at capture · deleted after processing, or kept up to 30 days, blurred) and "Start scan". Copy: the
   post's rule + the GDPR line with the hedge.
4. FitXpress · SDK and API: "Runs inside your app." Real capture UI (`capture-person-and-phone.webp`) with a scan
   sweep, chips 80+ body measurements · Body composition estimates · Under 45 seconds.
5. Close: "Trust starts on the consent screen.", CTA, landing URL, "FitXpress is not a medical device. It doesn't
   replace a coach."

The phone screens in scenes 2-3 are drawn schematics, not product UI: the "other app" carries no brand, and "Your
app" stands for the customer's app. Real product UI is only in scene 4. HyperFrames `check`: 0 errors (overlap of the
two stacked phone screens is marked as intended). Sound: CC BY bed without credit (Vadim, 2026-11-16).
