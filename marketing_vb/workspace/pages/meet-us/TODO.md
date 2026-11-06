---
product: company
type: todo
vertical: none
status: open
date: 2026-11-02
---

# TODO — /meet-us/

Search for `[PLACEHOLDER` in page.md and page.html: every hit below has one.

## Blockers (the page does not go live without these)

| # | What | Who | By | Exit |
|---|---|---|---|---|
| 1 | Customer promo code for free CES registration | Vadim (Exhibitor Dashboard) | Nov 10 | Paste into the pass block. No code by launch → remove the pass block (judge round 1) |
| 2 | CES registration link that accepts the code | Vadim | Nov 10 | Link in the pass block |
| 3 | HubSpot Meetings: check whether our plan allows a team (round robin) link. Yes → one link for CEO and sales; no → two host links side by side. Only January 6-9, Las Vegas time set explicitly, 30 minutes, 10-minute buffer, at most 5-6 a day per person, location "Booth 55630, Venetian Expo, Level 2", questions: company, role, topic | Asel | Nov 13 | Embed at `#book` |
| 4 | URL of the 3DLOOK listing in the CES exhibitor directory (shows the booth on the floor plan) | Vadim | Nov 10 | Link under the facts row; if there is none, delete the line |
| 5 | Exhibit hours for 2027 on ces.tech: confirm the link target, then the booking slots | Asel | Nov 13 | Keep the generic link or point to the hours page |

## Placeholders (can go live with a fallback)

| # | What | Who | By | Fallback |
|---|---|---|---|---|
| 6 | Hero visual: still from the booth video, guided capture on a phone | Kristina | Nov 23 | An existing guided-capture UI image from the site |
| 7 | OG image for link previews (LinkedIn, email) | Kristina | Nov 23 | Same as hero |

## Claims to confirm

| # | What | Who |
|---|---|---|
| 8 | Badge pick-up locations were cut from the page (unverified for 2027, judge round 1). Add back only from the 2027 registration guide | Asel |
| 9 | Demo decision (Nov 20): if the booth shows wrist sizing live, the "What is new" card may say so; until then it stays the approved platform sentence | Vadim after Katerina and Whitney |

## Launch steps

| # | What | Who | When |
|---|---|---|---|
| 10 | Build in WordPress from page.html, Yoast `noindex, follow`, no menu | Asel | by Nov 24 |
| 11 | GTM: events `cta_book_hero` (button), `soft_online_demo` (link) and the HubSpot booking success message → GA4 `meeting_booked` with page path. Verify each by hand | Asel | by Nov 24 |
| 12 | UTM links and QR codes from README.md for every off-site placement | Asel | by Nov 20 (QR goes to print on Dec 2) |
| 13 | Top bar and the `/contact-us/` line (copy in page.md), December 1 → January 9. No UTM on internal links | Asel | Dec 1 |
| 14 | Variant B on January 11: swap the hero, remove the facts row and the pass block, point the embed at the sales demo link; top bar off | Asel, Nika | Jan 11-12 |
| 15 | After January 31: next event on the same URL, or 301 to the demo booking page | Vadim | Feb 1 |

## v2 additions (2026-11-06): map block and Figma handoff (`v2/README.md`)

| # | What | Who | When |
|---|---|---|---|
| 16 | Re-check the two routes in `v2/map_data.py` against the final CES floor plan: doors open as entrances during show hours, booth position, aisle widths. Rebuild (`python3 v2/build.py`), re-render the videos | Vadim | Dec 10 |
| 17 | GTM: add `cta_find_hero`, `map_route_select` (route), `map_replay` to the event list in item 11 | Asel | by Nov 24 |
| 18 | Ring is part of the booth demo (Vadim, 11-03), but ring sizing is not built per claims registry CLM-CAP-017 and is never named on the site before launch. The "What is new" card keeps the approved wrist sentence | Vadim | n/a |
