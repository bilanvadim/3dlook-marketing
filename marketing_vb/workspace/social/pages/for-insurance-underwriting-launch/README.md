# Company-page posts: insurance underwriting landing launch (2026-11-16)

Source: the live page https://3dlook.ai/for-insurance-underwriting/ (capture:
`workspace/pages/for-insurance-underwriting/published-live-2026-11-16.md`). Not an
article pack. Posts for the four company profiles, each with the launch video made by
/brag-slim (private repo: `3dlook-marketing-private/launch-videos/insurance-underwriting/brag-output/`).

| Profile | Video | Post |
|---|---|---|
| linkedin-company | `brag-feed.mp4` 4:5 | 225 words, page link in the post |
| facebook-company | `brag-feed.mp4` 4:5 | 1069 chars, page link in the post |
| instagram-company | `brag-reel.mp4` 9:16 Reel, cover `brag-reel.jpg` | 801 chars, link in bio |
| twitter-company | `brag.mp4` 16:9 | 268 chars, page link in the first reply |

**Gates:**
- `post-lint.py --gate` passes on all four. The only warning: `video` is not in the
  lint's seven design-tip formats.
- `post-brand-checker` ran on all four. Instagram and X passed. LinkedIn and Facebook
  failed on claims the page does not make: "That gap grows…" and "Most applications…".
  Those lines were fixed. The fixes also narrowed Munich Re to accelerated underwriting
  everywhere and removed "now" and "on screen".
- One flag was not adopted: "FitXpress for Life Insurance Underwriting is not on the
  page". The name is the hero eyebrow on the live page, but `capture-live.py` drops
  eyebrows. The post uses "FitXpress" anyway.

**Left out on purpose:** customer logos, the "HIPAA Compliant" badge, pricing and
accuracy figures.
