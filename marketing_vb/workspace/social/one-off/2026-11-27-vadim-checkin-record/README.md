# Vadim · FitXpress check-in post (one-off, 2026-11-27)

Hlib Hlazovyi wrote a LinkedIn post for Vadim (`linkedin-vadim`, Australia) and sent it in the Slack DM on 2026-11-27
(«Привет, вот пост для Вадима», D0CC6GESJ90 ts 1795796463.709559), with no image. Vadim (11-28): «треба перевірити та
підготувати візуали або відео для них».

Status: draft. Video sent to Vadim's Telegram on 2026-11-28 (msg 6846) for review; nothing sent to Hlib yet.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's text as sent (129 words, post-lint PASS) |
| `post/post.md` | Re-angled edit: 143 words, post-lint PASS (only the one-off `design_tip` / `cta` warnings and the soft rhythm note) |
| `video/composition/index.html` | HyperFrames composition, 1080×1350, 25 s (edit THIS) |
| `video/build.sh` | Copies the composition + logo to `~/.cache/mvb-social-video/oneoff-…/feed/`, runs `check`, renders with `hyperframes@0.9.1`, writes the MP4 to the private repo |
| `video/sound.py` | House sound rules on this composition's scene times (bed from the private library, earshot effects, −14 LUFS) |
| `video/sound.json` | Bed, licence, beat fit and mix levels of the sound version |
| `video/feed-sheet.jpg` | One frame per scene, from the final MP4 |
| `~/3dlook-marketing-private/social-video/2026-11-27-vadim-checkin-record/` | `…-feed.mp4` (silent) and `…-feed-sound.mp4` |

## Text review

**Main issue: the same idea as Vadim's own post of 11-20** (`../2026-11-20-vadim-fitness-records`): "a progress view
is only as reliable as the records behind it", "the fix I'd push for", "one timestamped record". Hlib's draft repeats
the thesis, the "fix I would push for" line and the product sentence a week later on the same profile. If the 11-20
post is live, a second one with the same point reads as a rerun.

The edit keeps Hlib's material (gaps, a note added later, the coach or member looking back, one record on the
member profile, his eight-week question) and moves the lesson to something the 11-20 post doesn't say: **the order
of two steps** (personal-profile rule 4). Design the review first, then make each check-in capture exactly what the
review needs. That fits Vadim's brief (implementation, operating a program).

- **Hook:** "A progress log … only stays clear when check-ins follow one consistent record" → "I'd design a fitness
  app's check-in backwards, starting from the progress review." An opinion someone can argue with, and new against
  11-20.
- **"Keep every check-in in one structured record tied to the member profile" + "Each scan creates one timestamped
  record in the app".** Read together they suggest FitXpress ties scans to a member. Canon (CLAUDE.md §12): 3DLOOK
  doesn't track people, scan records sit on random IDs. Now the app keeps the fields on the member profile, and the
  product line uses the live landing's wording: "Each scan comes back as one timestamped record, and your platform
  chooses what the member and the coach see."
- **Kept:** Hlib's scenario sentence, the coach-or-member review, the product canon line, the medical-device line,
  his question, the link as the last line. No emoji, as Hlib had it.

## Video

1. Hook from frame 0: "Design the check-in backwards. Start from the review." An arrow draws right to left under
   "backwards".
2. "One member, eight weeks": a check-in log, metric (Australia): weight 72.4 kg, no check-in, a note "felt lighter"
   tagged "added later", weight 72.1 kg, no check-in, an unmeasured progress photo, "waist about 86 cm, tape", and
   week 8 "Review: what changed?". Copy: "Weight some weeks. Gaps. A note added later." / "At week eight, the review
   is hard to read."
3. "Start at the review": week 8 turns into the review with four fields (weight, waist, hips, body fat), then weeks
   7 → 1 rebuild backwards into the same fields. Copy: "Decide what the week-eight review needs." / "Every check-in
   captures exactly that, in the same fields."
4. "FitXpress · SDK and API": "One timestamped record per scan." A code card of one scan result with
   `created_at` / `completed_at` ringed (36 s apart), chips 80+ body measurements · Body composition estimates ·
   Under 45 seconds.
5. Close: "Start from the review.", "Your platform chooses what the member and the coach see.", CTA, landing URL,
   medical-device line.

The log is a drawn schematic of a customer app, "Illustrative member" on screen. The code card uses field names from
the live API image (`api-json-response.webp`); that image itself isn't used because its BMI (24.6 at 168 cm / 62 kg)
and timestamps (47 s apart, against "under 45 seconds") don't add up. Values on the card match the member in
scenes 2-3 (174 cm, 72.0 kg). HyperFrames `check`: 0 errors. Sound: CC BY bed without credit (Vadim, 2026-11-16).
