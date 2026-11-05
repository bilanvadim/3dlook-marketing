---
product: fitxpress, mobile_tailor
type: pricing
status: live (2026-11-05)
---

# /pricing/ redesign — log

## 2026-10-14

- Trigger: FitXpress bills per API request, not per successful scan (Vadim's thread in #marketing). Proposals from Nika (requests wording, disclaimer) and Asselya (feature regrouping, Clarity dead clicks, mobile confusion).
- Data pull: `data/2026-10-14-analytics.md` (GA4, GSC, Clarity, Ahrefs, live page).
- Prototype: `page-2026-10-14.html` (text copy `page-2026-10-14.md`, screenshots `screenshot-*.jpeg`). Detector `--channel page`: no hard fails.
- Changes and reasons: `changes-2026-10-14.md`, also published as the Google Doc "3DLOOK Pricing page: proposed changes (2026-10-14)".
- Shared for review: Google Doc (edit) and the prototype HTML on Drive (view) to Asselya, Nika and Kristina; English summary, HTML and screenshots in the #marketing thread; a private review page of the prototype.

## Open (Doc section 6)

1. Feature gating: progress tracking and goal visualization Pro-only, or every feature on every plan (sales).
2. What happens at the request limit: overage at the plan rate or a blocked request.
3. One request per billable action; 2D progress on Pro; monthly pool on annual plans.
4. Failed scans stay off the page.
5. Smart Scales beta label; Mobile Tailor trial price; "respond within one business day".

## 2026-11-05

- The new /pricing/ is live (FitXpress, Mobile Tailor and Wrist tabs; requests as the FX unit). Snapshot of the live page: `live-2026-11-05/published-live-2026-11-05.{html,md}` (captured ~14:15 UTC, after someone changed the Yoast title to "3DLOOK Pricing | FitXpress, Mobile Tailor & Wrist").
- Technical audit: `live-2026-11-05/audit-2026-11-05.md`. P1: hero videos of 6.6–10 MB without faststart or poster; homepage hero images preloaded on /pricing/; `pricing_plan_click` sends the button text, so plans can't be told apart, and MT trial clicks aren't tracked; GA4 `form_start` fires 4–5 times per view because of hidden HubSpot forms. P2: Wrist form missing from the GTM map; MT form lacks 3 hidden fields; mtm signup returns 404; Request indexing; meta description and og:image.
