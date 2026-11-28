# Katya · FitXpress premium-tier post (one-off, 2026-11-27)

Hlib Hlazovyi wrote a LinkedIn post for Kateryna Boichuk (`linkedin-katya`, Israel + Gulf) and sent it to Vadim in
the Slack DM on 2026-11-27 (D0CC6GESJ90 ts 1795797379.267719, then «Для Кати Бойчук»), with no image. Vadim (11-28):
«треба перевірити та підготувати візуали або відео для них».

Status: draft. Video sent to Vadim's Telegram on 2026-11-28 (msg 6847) for review; nothing sent to Hlib yet.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's text as sent (106 words, post-lint PASS) |
| `post/post.md` | Edit: 149 words, post-lint PASS (only the one-off `design_tip` / `cta` warnings and the soft rhythm note) |
| `video/composition/index.html` | HyperFrames composition, 1080×1350, 25 s (edit THIS) |
| `video/build.sh` | Copies the composition + product imagery to `~/.cache/mvb-social-video/oneoff-…/feed/`, runs `check`, renders with `hyperframes@0.9.1`, writes the MP4 to the private repo |
| `video/sound.py` | House sound rules on this composition's scene times (bed from the private library, earshot effects, −14 LUFS) |
| `video/sound.json` | Bed, licence, beat fit and mix levels of the sound version |
| `video/feed-sheet.jpg` | One frame per scene, from the final MP4 |
| `~/3dlook-marketing-private/social-video/2026-11-27-katya-premium-tier/` | `…-feed.mp4` (silent) and `…-feed-sound.mp4` |

## Text review

The angle (what belongs in a paid tier) is new against Nick (retention), Katya 11-20 (progress noise), Vadim 11-20
(records) and Olena (consent), and it is the live landing's own block: "Features for your premium tier: Offer 3D
progress tracking and goal visualization within your premium tier." It fits Katya's brief (why it matters
commercially).

- **Hook.** "Putting basic weight tracking behind a paywall rarely convinces fitness members to upgrade" is a general
  claim about member behaviour with no source. Now an opinion: "A paid tier that only tracks weight is hard to sell."
- **"Members look for clear visual and measurement shifts over time instead of another number."** Unsourced claim
  about what members want, built as a corrective "instead of". Replaced by a usable rule (personal-profile rule 4):
  "My test for a premium feature: does it show something the free log can't? A side-by-side 3D view of two scans
  passes. Another weight chart doesn't."
- **Two different "plans".** "On the FitXpress Pro plan" sat next to "the paid tier" and read as if members buy a
  FitXpress plan. Now explicit: the Pro plan is what the app gets from 3DLOOK; the app puts the features in its own
  premium tier.
- **"Two guided smartphone photos return those results in under 45 seconds."** "Those results" included the 3D
  progress view, which needs two scans. Now the scan line comes first, then the two Pro features, each described in
  the `/pricing/` page's words: progress compares two scans as 3D models; goal visualization builds a 3D body model at
  a target weight from a scan.
- **"does not replace coaching"** → the house line "doesn't replace a coach".
- **Kept:** the premium/upgrade angle, the question (lightly shortened), the link as the last line. No emoji.

## Video

1. Hook from frame 0: "A paid tier that only tracks weight is hard to sell." A flat weight line draws under "only
   tracks weight".
2. "The upgrade screen": a phone with the app's own plan screen ("Your app", "Choose your plan"): workouts, weight
   log, weight chart, reminders, all ticked in Free and in Premium. The Premium column is ringed, "Same as free", the
   member taps "Not now" and the upgrade button greys out. Copy: "Premium repeats the free log." / "The same chart,
   behind a price." / "The upgrade feels thin."
3. "My test for premium": the plan screen slides away, the app's Premium screen shows the real 3D progress render
   ("3D Body Progress · Compare two scans") and "3D Goal Visualization · A 3D body model at a target weight". Copy:
   "Does it show what the free log can't?", the pass/fail line, "FitXpress Pro plan: 3D Body Progress tracking and 3D
   Goal Visualization."
4. "FitXpress · in your app": "Two guided phone photos." Real capture UI (`capture-skeleton-two-phones.webp`), chips
   80+ body measurements · Body composition estimates · Under 45 seconds.
5. Close: "Put in premium what the free log can't show.", CTA, landing URL, medical-device line.

No pounds or inches anywhere (Katya's audience is metric): the `/pricing/` cards with "150 lb / 35.4"" are left out;
the 3D renders used carry no units. The phone screens are drawn schematics of a customer app, not 3DLOOK UI. Scene 4
uses a different capture image from Katya's 11-20 video. HyperFrames `check`: 0 errors. Sound: CC BY bed without
credit (Vadim, 2026-11-16).
