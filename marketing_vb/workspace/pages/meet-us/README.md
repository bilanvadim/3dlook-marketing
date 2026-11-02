---
product: company
type: readme
vertical: none
status: draft-awaiting-vadim
date: 2026-11-02
---

# /meet-us/ — CES 2027 event page

One-screen page for CES 2027 (booth 55630, Venetian Expo, January 6-9, 2027). Not a full landing:
booth facts, what we show, booking, the free-pass code. Event-agnostic URL so it can carry the next
event. Plan context: Google Doc «CES 2027: план подготовки маркетинга», tasks D1, D3, D5.

## Files

| File | What |
|---|---|
| `page.md` | Copy: variant A (now → January 9), variant B (January 11 → 31), top bar and Contact line |
| `page.html` | Self-contained prototype of variant A, `DESIGN.md` tokens, classes `.mu-*` |
| `TODO.md` | Blockers first; every `[PLACEHOLDER` in the files is listed there |
| `fact-sheet.md` | Source of every figure, checks done, what is unverified |
| `gate-reports.md` | Kit substitution, G-A, deliberate deviations, G-T status, event scorecard |
| `open-items.md` | Bent rules for Asselya |
| `judge-round-N.json` | Blind judge rounds |

## Structure

1. Hero (navy): eyebrow, H1, lede with the two approved figures, **Book a meeting at the booth** → `#book`, micro line. `[HERO]` visual on desktop only.
2. Facts row: When · Where · Booth (oversized 55630). Directory link under it.
3. "What can you see at booth 55630?": three cards.
4. `#book`: heading and one line, HubSpot Meetings embed, pass block with the code, soft link to `/contact-us/`.
5. About line.

On mobile the order is hero → facts → cards → heading → embed → pass → soft link.

## WordPress and Yoast

- Build from `page.html`: delete the two `data-prototype-chrome` blocks; the theme supplies header and footer.
- Yoast: SEO title `Meet 3DLOOK at CES 2027 · Booth 55630`; meta description as in `page.html`; Advanced → `noindex`, follow. The page leaves the Yoast sitemap on its own. Add it to no menu.
- No schema on purpose.
- OG image: Kristina (TODO 7).

## Tracking

UTM on every off-site link, none on internal links (top bar, Contact line), because internal UTMs
restart GA4 sessions.

| Placement | Link |
|---|---|
| Booth back wall QR | `https://3dlook.ai/meet-us/?utm_source=ces2027&utm_medium=qr&utm_campaign=ces2027&utm_content=booth-wall` |
| Flyer QR | same, `utm_content=flyer` |
| Business cards | same, `utm_content=card-katerina` / `card-whitney` / `card-ihor` |
| Invitation emails | `utm_source=hubspot&utm_medium=email&utm_campaign=ces2027&utm_content=invite-1` (2, 3) |
| LinkedIn outreach | `utm_source=linkedin&utm_medium=outreach&utm_campaign=ces2027&utm_content={sender}` |
| Email signatures | `utm_source=signature&utm_medium=email&utm_campaign=ces2027` |
| CES directory listing | `utm_source=ces-directory&utm_medium=referral&utm_campaign=ces2027` |

GTM events: `cta_book_hero`, `soft_online_demo`, `meeting_booked` (HubSpot Meetings success message).
Verify each by hand before launch.

## Tokens used

Navy hero with radial glow and a 40px measurement grid, white primary button with navy text, `#143DFF`
only as an accent (pass block edge), radii 5 / 15 / 20 / 30, spacing from the `DESIGN.md` scale,
Satoshi, focus ring `#B1BDFF` 3px.

## Skipped, in writing

Variant B has no HTML prototype (copy only). 1440 viewport not checked. Performance not measured.
Analytics not verified (no embed yet).
