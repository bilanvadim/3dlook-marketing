---
product: company
type: gate-report
vertical: none
status: g-t-blocked-on-inputs
date: 2026-11-02
---

# Gate reports — /meet-us/

## Kit

Event page is a **gap** in `references/page-types.md`. Built from the campaign landing variant of
`kit-vertical-page.md`: no navigation, one action, no sibling block. Slots kept: hero, conversion,
soft alternative. Slots replaced: vertical context → event facts (when, where, booth) and "what you
can see"; case cards, compliance, accuracy, FAQ, pricing → dropped (see below). Invented slots: event
facts row, map link, free-pass block, about line.

## G-I · Should this page exist

Not applicable: G-I covers vertical pages. Decision recorded instead: Vadim, 2026-11-02, after a
pros-and-cons review, chose a one-screen event page over a full landing and over a bare redirect.

## G-A · Architecture

| Check | Result |
|---|---|
| Placed | `/meet-us/`, standalone, no parent, no breadcrumbs. Not in the header (five items, approved 2026-10-22) and not in the Company menu. Event-agnostic slug, so the page can carry later events, and no "CES" in the path (CTA contract §37) |
| Cannibalisation | None: noindex, and no page or article targets CES queries |
| Inbound internal links | Top bar on all pages (December 1 to January 9) and one line on `/contact-us/` (task D3). Off-site: QR codes, emails, LinkedIn, email signatures, CES directory listing |
| Baseline | Not needed: the URL returns 404 today |
| Vadim approved placement, URL and angle | Yes, 2026-11-02 ("да, обнови") |

## Deliberate deviations from the vertical rules

| Rule | Deviation | Why |
|---|---|---|
| H1 = product + audience + outcome; product in the lede (detector house rule) | H1 is event + booth; no product name | Event page. Vadim, 2026-10-27: CES presence is company-level, no product names (same rule as the CES directory text) |
| Acronyms expanded at first use (detector flags CES) | CES not expanded | The event's official name is CES |
| Indexable, in the sitemap, Service + FAQPage + BreadcrumbList schema | noindex, no sitemap, no schema | Temporary page with no search intent; Vadim, 2026-11-02 |
| 1,100-1,600 words, 4-6 FAQ, price signal, compliance lines, accuracy block | about 250 words, none of these | One-screen event page by decision; depth stays on the product pages and the trust FAQ |
| Shared form `FX · LP · Demo` | HubSpot Meetings embed | The action is a time slot at the booth, not a demo request |

## G-T · Technical gate

**Not passed. Blocked on inputs** (TODO.md, blockers): promo code, registration link, directory
listing URL, HubSpot Meetings links, hero visual. Prototype checks done: one `<h1>`, 375/768/1280
without horizontal scroll, contrast ≥ 5.7 everywhere, focus ring present. Analytics not verifiable
until the embed exists.

## G-J · Blind judge — event-page scorecard (adapted 2026-11-02)

The vertical scorecard scores search, uniqueness against a parent and vertical proof, which an event
page does not have. Adapted axes, same threshold and the same hard-fail list:

| Axis | Weight | What is checked |
|---|---|---|
| Event facts | 20 | when, where, booth, how to find it, what is shown; all correct and consistent |
| Claims discipline | 15 | every figure traced to fact-sheet sources and identical everywhere, approved wordings, banned words absent |
| Conversion | 20 | one primary action, low friction, its place on mobile, pass path, soft alternative, a CTA on every second screen |
| One screen, one job | 15 | scannable in 30 seconds, nothing that belongs on a product page |
| Human copy | 10 | no AI tells, varied rhythm, concrete detail |
| Register and vocabulary | 10 | US English, enterprise register, terminology guardrails |
| Technical and placement | 10 | noindex, no nav, URL, `DESIGN.md` tokens, mobile, accessibility |

Rounds: see `judge-round-N.json`.

| Round | Total | Hard fails | Lowest | Status |
|---|---|---|---|---|
| 1 (2026-11-02) | 71 / 100 | placeholders left (inputs pending) | human_copy 6/10 | gate not taken; round 2 after TODO blockers 1-4 and 6 are filled |
