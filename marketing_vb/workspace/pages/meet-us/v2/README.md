---
product: company
type: readme
vertical: none
status: draft-awaiting-vadim
date: 2026-11-06
---

# /meet-us/ v2: Figma handoff + "find us" map

Vadim, 2026-11-06: a separate Figma file for the CES landing, prepared the way Kristina hands pages to
developers (every breakpoint), and an interactive map with arrows from the entrance to our booth.

v1 (`../page.md`, `../page.html`) stays the copy source. v2 adds one block, **"How do you find booth
55630?"**, a hero text link and a "See the route" link in the Where card. Everything else is v1 copy.

## Files

| File | What |
|---|---|
| `map_data.py` | Map geometry, routes, step copy. Units of the CTA/Freeman plan (1 unit ≈ 0.416 m) |
| `build.py` | One source for every output below |
| `out/page-v2.html` | Live responsive prototype, variant A, with the animated map |
| `out/page-v2-variant-b.html` | Variant B (after the show) |
| `out/figma/{A,B}-{1920,1440,744,375}.html` | Static pages per Figma frame (media queries unwrapped, final map state) |
| `out/video/*.mp4` | 1080×1080 route videos, one per entrance (≈17 s) |
| `tools/shot.js`, `tools/render_video.js` | Screenshots and video render (system Chrome + Playwright) |

## Breakpoints (Kristina's grid in the «Website» file)

| Figma frame | CSS range | Grid | Content width |
|---|---|---|---|
| 1920 | ≥1600 px | 12 col, gutter 20, margin 370 | 1180 |
| 1440 | 1280-1599 px | 12 col, gutter 17, margin 165 | 1110 |
| (no frame) | 1024-1279 px | 1440 layout, margins 48 | fluid |
| iPad mini 744 | 600-1023 px | 8 col, gutter 16, margin 48 | 648 |
| iPhone 13 375 | <600 px | 4 col, gutter 25, margin 30 | 315 |

## The map block

- **What it is.** Our own schematic of Level 2, Halls A-D around booth 55630: halls, the Venetian
  Ballroom, the foyer, the west concourse, the Health area, anonymous booth blocks, the Health Hub,
  the two entrances, the escalators. **No exhibitor names** (CES contract §37c, courtesy). Not a copy of
  the Freeman plan, drawn from its coordinates.
- **Two routes** (tabs): from the Venetian Foyer via the Hall D entrance (≈230 m from the escalators,
  ≈85 m from the Hall D door) and from the west concourse via the Hall C entrance (≈200 m).
- **Motion.** When the block is 35% in view the route draws itself: blue line with white chevrons, a
  walker dot, the current step lights up in the list (`is-upcoming` → `is-current` → `is-done`).
  Timing: 0.7 s intro, 7.5 s walk, 1.4 s arrival. Tabs restart the walk; **Replay the route** too.
  Desktop and tablet keep the whole map in view. Under 600 px the camera follows the walker
  (150 units wide) and ends on the booth window (`FINAL_MOBILE`).
- **Reduced motion / no JS.** Full route drawn, no camera moves, no pulse. The numbered steps are the
  text alternative; the SVG has `title` + `desc`.
- **Tabs.** `role=tablist/tab/tabpanel`, arrow keys move between tabs, focus ring `#B1BDFF` 3 px.
- **Analytics (GTM, add to README v1 list):** `cta_find_hero` (hero text link), `map_route_select`
  (`route`: foyer|west), `map_replay`, `video_play` (`video`).
- **WordPress.** The block is plain HTML + inline SVG + ~3 KB JS, classes `.mu-find*`, `.m-*`. Copy the
  `<section id="find">` from `out/page-v2.html`, its CSS and the first `<script>`.

## Figma (dev handoff)

https://www.figma.com/design/W6J8FtviwHjRejXnFKfJvN (3Dlook inc, Vadim's drafts). Pages: Cover, Landing ·
Variant A, Landing · Variant B, Find-us map · motion (Smart Animate flows + motion spec), Components
(all states), Handoff notes. Local variables «3DLOOK web tokens» with CSS code syntax, Satoshi text styles
per breakpoint. Built with `use_figma` from the same copy and map data as this folder.

## Hero and About videos (Vadim, 2026-11-06)

Kristina's booth video (B7) comes closer to the show, the page is needed now. Hero = YouTube
«FitXpress - AI-Powered Body Scanning» `452QOv0O2Hw` (2024) until B7 is ready; the 10-year video
`UVrdZlhAkeo` (team montage) sits in a new «Ten years of 3DLOOK» block next to the about line. Both are
click-to-load facades (thumbnail + play, `youtube-nocookie` iframe after the click, GTM `video_play`).
Vadim checks the FitXpress video for old claims (e.g. «HIPAA compliant») before launch.

## Videos

- **Loop, both routes at once** (Vadim: «декілька роутів одночасно… зациклим»): 1080×1350, 12 s,
  seamless (routes fade back to the first frame), route A blue, route B navy, two lanes on the shared
  aisle. `out/video-loop.html`. MP4 + 480 px GIF (388 KB, for emails) in Drive «CES 2027 Marketing».
- Single routes, 1080×1080, 16 s, captions + end card: one per entrance.

## Before launch

1. **Re-check every route point against the final floor plan** (December), especially which doors are
   entrances during show hours. The plan of Oct 5, 2026 marks "Hall D Entrance" and "Hall C Entrance".
2. The directory link placeholder (v1 TODO 4) now sits in the note under the map.
