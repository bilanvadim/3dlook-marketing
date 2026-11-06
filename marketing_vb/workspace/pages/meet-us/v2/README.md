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
  (`route`: foyer|west), `map_replay`.
- **WordPress.** The block is plain HTML + inline SVG + ~3 KB JS, classes `.mu-find*`, `.m-*`. Copy the
  `<section id="find">` from `out/page-v2.html`, its CSS and the first `<script>`.

## Videos

Square 1080×1080 MP4, H.264, no sound: overview → zoom to the start → the camera walks the route with
the step caption → zoom on the booth → "See you at booth 55630" end card. For LinkedIn posts, invite
emails (as a GIF or a link), WhatsApp to guests on the day, the booth team's phones.

## Before launch

1. **Re-check every route point against the final floor plan** (December), especially which doors are
   entrances during show hours. The plan of Oct 5, 2026 marks "Hall D Entrance" and "Hall C Entrance".
2. The directory link placeholder (v1 TODO 4) now sits in the note under the map.
