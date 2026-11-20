# Vadim · FitXpress check-in records post (one-off, 2026-11-20)

Hlib Hlazovyi wrote a LinkedIn post for Vadim (`linkedin-vadim`) and sent it in the Slack DM on 2026-11-20
(«это для тебя пост», D0CC6GESJ90 ts 1795192781.239389). The image is again the 4:5 visual made for Nick on 11-19
(US units). Vadim asked for a review. The post supports the AU + NZ connected-fitness outbound from Vadim's profile
(`workspace/outbound/campaigns/2026-11-19-au-connected-fitness`).

Status: review sent to Hlib on 2026-11-20 (Vadim «давай»): DM ts 1795193566.255739 (ru review + «на будущее» rules + final text) and the metric visual F0CKNSB0TEW. Vadim publishes from his own account.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's text as sent (129 words). post-lint **FAIL (2)**: a 32-word sentence, an em dash |
| `post/post.md` | Rewrite: 164 words, post-lint PASS (only the one-off `design_tip` / `cta` warnings), avg sentence 10.9 words |
| `visual/hlib-image-as-sent.png` | The image Hlib attached (Nick's US visual) |
| `visual/fitxpress-post-4x5-metric-1080x1350.png` | **Feed version** (use this one): same design, metric units |
| `visual/fitxpress-post-metric-1800x942.png` | Same, original 1.91:1 layout (backup) |
| `visual/tools/` | Nick's build tools with metric values; `build.sh` rebuilds both from Hlib's original in the Nick folder |

## Text review

- **Kept:** the angle. Structured, comparable records fit Vadim's brief (reliability, implementation, operating at
  scale) and differ from Nick (retention) and Katya (logging cadence). Hook, link as the last line, the
  medical-device line.
- **Hard fails fixed:** the 32-word product sentence is split, the em dash is gone.
- **"…as a timestamped record rather than a loose note"** is a corrective contrast (guardrails). Now stated
  positively, in the live page's own words: one timestamped record per scan, same structure every time.
- **"and a 3D model"** dropped. On the live page 3D progress sits on the Pro plan; listing it with the base outputs
  overstates what every customer gets.
- **"80+ measurements" → "80+ body measurements"** (guardrails term).
- **The 12-week scenario** (weight flat, waist and body fat move) was the third use in two days (Nick, Katya). It's
  replaced by a concrete picture of inconsistent records: tape at the navel in week 1, a few centimetres higher in week
  6, a coach note "looks leaner" in week 12. Framed as "can look like", not as a customer story.
- **Question:** "How do you keep check-in records consistent…" → one that needs the reader's own number: "How many
  formats does one member's check-in history sit in on your platform today?"
- Australian spelling: "centimetres".

## Visual

Same design as Nick's fixed 4:5 visual, numbers in metric for an AU audience. One illustrative member, 168 cm,
63.5 kg: BMI 22.5 (63.5 / 1.68²), BMR 1,420 kcal (Katch-McArdle at 23% fat), progress over 3 months −0.3 kg weight,
−2.5 cm waist, −2% body fat. Everything else is unchanged from 11-19 (white logo, "Scan, measure, compare", Jost).
