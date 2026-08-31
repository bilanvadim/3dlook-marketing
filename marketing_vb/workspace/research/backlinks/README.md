# Backlink Analysis Report — 3dlook.ai

**Source of truth:** Google Sheet «Backlink  Analysis Report» (owner: asselya@3dlook.me)
https://docs.google.com/spreadsheets/d/171n8SVk_MdlKa-1XChbf57LvRuCYtAKWSperfUTdQRg/edit

Ahrefs export. Snapshot pulled 2026-08-31 (sheet modifiedTime 2026-08-31T16:24Z).
This is a **general, site-wide report** — not article-specific. Reuse it for any SEO
planning that needs authority / internal-link-donor decisions.

Refresh with `./refresh.sh` (public export link, no auth needed).

## Files

| File | Tab | Rows | What it is |
|---|---|---|---|
| `pivot.csv` | Pivot | 34 non-empty | **Not a pivot** — hand-written content-strategy recommendations (P1 refresh winners, P2 BOFU pages, P3 comparison pages, effort split) |
| `links-by-segments.csv` | Links by Segments | 156 | Backlinks per target URL, tagged `General` / `Apparel` / `Health` |
| `all-links.csv` | All links | 14 680 | Every referring link. 37 cols: referring page URL/title, DR, UR, anchor, left/right context, target URL, nofollow/UGC/sponsored, first/last seen, lost |
| `links-dr-65.csv` | Links (DR 65+) | 4 519 | Same schema, filtered to DR ≥ 65 |
| `all-domains.csv` | All domains | 3 073 | Referring domains: DR, traffic, keywords, links to target, new/lost |
| `domains.csv` | Domains | 1 304 | Filtered subset of the above |

## Segment totals (backlinks by target URL)

- General 9 999 · Apparel 2 398 · **Health 1 005**

## Health-segment link equity (top donors for internal linking)

| Target URL | Backlinks |
|---|---|
| `/content-hub/ai-in-fitness-industry/` | 326 |
| `/content-hub/the-potential-of-ai-in-telehealth/` | 263 |
| `/content-hub/glp-1-market/` | 183 |
| `/mobile-tailor/` | 153 |
| `/content-hub/top-fitness-industry-trends/` | 36 |
| `/content-hub/weight-loss-industry-overview/` | 33 |

## Wellness-specific finding (2026-08-31)

- `/content-hub/beyond-bmi-business/` — **1 backlink**
- `/content-hub/wellness-rewards-verification-.../` — **0 backlinks** (absent from the report)

So a new Wellness Platforms hub inherits **no external authority** from either page.
It has to be powered by internal links from the Health winners above
(ai-in-fitness-industry, telehealth, glp-1-market, mobile-tailor), not by the two
pages it is meant to sit above.

## Strategy notes lifted from the Pivot tab

Priority 1 — refresh proven winners: AI in fashion, **AI in fitness (build a full Health
cluster around it)**, AI in telehealth, sustainable fashion trends, apparel return rates,
GLP-1 market (expand into GLP-1 tracking / body composition / patient progress).

Priority 2 — BOFU pages under high-performing informational topics: FitXpress for fitness
apps & digital coaching, FitXpress for telehealth, body tracking for GLP-1 programs,
ROI of virtual fitting, virtual fitting buyer guide.

Priority 3 — comparison / decision-support pages (good for GEO + AI answers), e.g.
"BMI vs Body Measurements: What Digital Health Programs Should Track".

Effort split: 40% apparel refresh + BOFU · 40% Health cluster expansion · 15% technical
cleanup / consolidation · 5% experiments.
