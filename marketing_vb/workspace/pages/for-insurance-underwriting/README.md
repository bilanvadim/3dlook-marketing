---
product: fitxpress
type: handoff-readme
vertical: insurance-underwriting
status: draft-awaiting-vadim
date: 2026-08-31
---

# Handoff — FitXpress for insurance underwriting

A new FitXpress vertical page for 3dlook.ai. WordPress with Yoast. Nothing in this pipeline has
publishing credentials, so this folder is the whole package.

**Read first:** the page is **blocked on a G-I waiver**. The insurance vertical has zero case studies, so
by the Kit's own rule the page should not exist yet. `gate-reports.md` sets out the waiver request and
the fallback. Do not build until Vadim answers.

## What is in the box

| File | What it is |
|---|---|
| `page.md` | The page copy, slot by slot, with visual markers |
| `fact-sheet.md` | The source behind every figure, and what was measured versus specified |
| `gate-reports.md` | G-I, G-A and G-T results, dropped slots, the waiver request |
| `open-items.md` | Eleven items for Asselya, Vadim and Whitney |
| `TODO.md` | Blockers first, then everything else |
| `judge-round-N.json` | Blind-judge rounds, including failed ones |
| `assets/` | Empty. No images have been produced |
| `log.md` | The run log |

## The page in one line

A bottom-of-funnel commercial page for life and group carriers, reinsurers and digital distribution
partners running accelerated underwriting. Its job is to convert a buyer who already understands the
category, which the hub article at `/content-hub/mobile-body-scanning-insurance-underwriting/` teaches.

## Placement

| | |
|---|---|
| URL | `https://3dlook.ai/for-insurance-underwriting/` (confirmed free, HTTP 404 on 2026-08-31) |
| Parent | `/` (the homepage is the FitXpress parent, `/fitxpress/` 301s to it) |
| Breadcrumb | Home → FitXpress for Insurance Underwriting |
| Canonical | Self |
| Siblings | `/for-bmi-verification/`, `/structured-body-data-for-telehealth-digital-health-programs/` |
| Closest template to clone | `/structured-body-data-for-telehealth-digital-health-programs/`, the only page on the site whose schema is already right |

**No redirects to set.** The URL is new. No Search Console baseline is needed for the same reason.

## Yoast fields

| Field | Value | Length |
|---|---|---|
| SEO title | `Body Data for Life Insurance Underwriting \| FitXpress` | 53 / 60 |
| Meta description | `A guided smartphone scan captures structured build and BMI data remotely, supporting underwriter review in accelerated life insurance programs.` | 143 / 155 |
| Breadcrumb title | `FitXpress for Insurance Underwriting` | 36 |
| Canonical | `https://3dlook.ai/for-insurance-underwriting/` | |
| Index | Yes, in `page-sitemap.xml` | |

Both fields differ from the homepage's and from the hub article's. Do not reuse the hub article's title.

## Structure, in build order

| # | Section | Block | Visual |
|---|---|---|---|
| 1 | Hero | Navy band with radial glow, H1, sub, three oversized numerals, one button | `[HERO]` |
| 2 | The evidence gap accelerated underwriting created | White, two paragraphs, then a four-card row | `[CONTEXT]` |
| 3 | What an underwriting team receives | Light surface `#F9F9F9`, five-row definition table | `[CONTEXT]` |
| 4 | Where underwriting changes the workflow | White, three numbered blocks | `[WORKFLOW]` |
| 5 | Accuracy, scoped to the decision it supports | Navy proof band, four conditions, then a three-row figure table | `[ACCURACY]` |
| 6 | Compliance and data governance | White, six cards at 20px radius | `[COMPLIANCE]` |
| 7 | Integration and the boundary you control | Light surface, architecture diagram, two lists | `[INTEGRATION]` |
| 8 | Where the scan sits in the underwriting journey | White, five-stage horizontal flow, scrolls on mobile | `[WORKFLOW]` |
| 9 | Where FitXpress runs today | Light surface, short text block with two stat numerals | `[CASE CARD]` |
| 10 | Compare by role | White, three-column comparison table in its own scroll container | `[ACCURACY]` |
| 11 | What it costs | White, one paragraph, link to `/pricing/` | none |
| 12 | Questions underwriting teams ask | White accordion, 13 items, H3 per question | none |
| 13 | See the evidence a scan puts in the case file | Navy band with radial glow, form, one button | `[HERO]` |
| 14 | Keep reading | Light surface, three link groups | none |

## Designer briefs and alt text

Tokens come from `DESIGN.md` §13. Satoshi only. `#143DFF` stays a single sharp accent and never a large
fill. Navy `#050F40` with the radial glow on sections 1, 5 and 13, never a flat block.

| Marker | Brief | Alt text |
|---|---|---|
| `[HERO]` | Guided-capture phone UI in a frame against the navy glow, with fine measurement lines over the body render. The three numerals are the hero, not the image | "Guided body scan capture on a smartphone, with measurement points marked on the body outline" |
| `[CONTEXT]` ×2 | Section 2: four chips at 15px radius, one per method, muted until the cost line. Section 3: a plain definition table, no illustration | Decorative, empty alt |
| `[WORKFLOW]` ×2 | Section 4: the three diverging steps highlighted against a greyed base flow. Section 8: a five-stage horizontal flow with the scan marked at stages 1 to 3 | "Where the body scan runs across five stages of the accelerated underwriting workflow, from pre-screening to program insight" |
| `[ACCURACY]` | Oversized numerals for 96-97%, `< 1 cm` and ±3.5%, each with its reference underneath in small caps | Decorative, empty alt |
| `[COMPLIANCE]` | Six cards at 20px radius: encryption, retention, blur, identifiers, logging, privacy contact. No padlock icons, use the numbers and the words | Decorative, empty alt |
| `[INTEGRATION]` | The we-provide / you-build architecture diagram, same shape as the telehealth page's: your app, your backend, the FitXpress API, your backend, your output UI, with the customer environment boundary drawn | "Integration diagram showing guided capture inside the carrier's application, processing by the FitXpress API, and structured results returning to the carrier's underwriting platform" |
| `[CASE CARD]` | No card. Two stat numerals, 112,100 and 67, with the sentence underneath | Decorative, empty alt |

Real product imagery over icon grids, per `DESIGN.md` §10. No stock photography of people in offices.

## Schema to add on top of Yoast

Yoast supplies `WebPage`, `Organization`, `WebSite` and `BreadcrumbList`. `Service` and `FAQPage` have to
be added. The working example is the JSON-LD already live on the telehealth page; copy its shape.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "@id": "https://3dlook.ai/for-insurance-underwriting/#fitxpress-insurance-service",
      "name": "FitXpress for Insurance Underwriting",
      "alternateName": "FitXpress Underwriting Evidence",
      "url": "https://3dlook.ai/for-insurance-underwriting/",
      "provider": { "@id": "https://3dlook.ai/#organization" },
      "brand": { "@type": "Brand", "name": "FitXpress" },
      "serviceType": "Mobile body scanning and structured body data API for life insurance underwriting evidence collection",
      "category": [
        "Mobile body scanning",
        "Life insurance underwriting",
        "Accelerated underwriting",
        "BMI and build verification",
        "Remote evidence collection",
        "Applicant verification",
        "Body measurements"
      ],
      "description": "FitXpress allows life and group insurers to collect structured build and BMI data remotely through a guided two-photo smartphone scan, returning timestamped measurements and a disclosed-versus-captured comparison signal as supporting evidence for underwriter review.",
      "audience": {
        "@type": "BusinessAudience",
        "audienceType": "Life and group insurance carriers, reinsurers, insurtech platforms, digital distribution partners, accelerated underwriting teams, underwriting operations and new business teams"
      },
      "areaServed": "Global",
      "serviceOutput": [
        "80+ body measurements",
        "Body Mass Index (BMI)",
        "Basal Metabolic Rate (BMR)",
        "Body fat percentage",
        "Lean mass and fat mass",
        "3D body model",
        "Disclosed versus captured comparison signal",
        "Timestamped structured record",
        "Structured JSON payload"
      ],
      "termsOfService": "https://3dlook.ai/legal/"
    },
    {
      "@type": "FAQPage",
      "@id": "https://3dlook.ai/for-insurance-underwriting/#faq",
      "url": "https://3dlook.ai/for-insurance-underwriting/",
      "name": "Questions underwriting teams ask",
      "isPartOf": { "@id": "https://3dlook.ai/for-insurance-underwriting/#webpage" },
      "about": { "@id": "https://3dlook.ai/for-insurance-underwriting/#fitxpress-insurance-service" },
      "mainEntity": "ALL 13 QUESTIONS FROM page.md, each as {\"@type\":\"Question\",\"name\":...,\"acceptedAnswer\":{\"@type\":\"Answer\",\"text\":...}}"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://3dlook.ai/for-insurance-underwriting/#breadcrumb",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://3dlook.ai/" },
        { "@type": "ListItem", "position": 2, "name": "FitXpress for Insurance Underwriting", "item": "https://3dlook.ai/for-insurance-underwriting/" }
      ]
    }
  ]
}
```

Wire `WebPage` to the service the same way the telehealth page does: `about` and `mainEntity` pointing at
the `Service` node, `hasPart` pointing at the `FAQPage`. The FAQ answers in the JSON-LD must be
byte-identical to the answers rendered on the page.

## Internal links

**Out of the page:** `/` (up), `/for-bmi-verification/` and
`/structured-body-data-for-telehealth-digital-health-programs/` (siblings),
`/content-hub/mobile-body-scanning-insurance-underwriting/` (hub),
`/content-hub/mobile-body-scanning-accuracy/` (supporting), `/pricing/`, `/case-studies/`,
`/ebook-the-next-big-leap-in-health/`.

**Into the page, and someone else has to do these:**

1. A vertical block on the homepage linking down to all four FitXpress vertical pages. No parent page on
   this site does this today, and without it the page is reachable only through the nav dropdown.
2. The hub article's "Where FitXpress Fits" and "Next Steps" sections, which currently point at `/` and
   `/for-bmi-verification/`.
3. The sibling blocks on `/for-bmi-verification/` and the telehealth page.

## Analytics

Four events, all to be **verified firing manually** after publish, never assumed:

| Event | Fires on |
|---|---|
| `page_form_view` | The demo form enters the viewport |
| `page_form_first_input` | First keystroke in any field |
| `page_form_submit` | Successful submission |
| `page_demo_click` | Any "Book a demo" button, hero and closing band tagged separately |

## WordPress notes

- **Duplicate chrome.** The theme supplies header and footer. Nothing in `page.md` includes them.
- **Class collisions.** Namespace anything new as `.fx-iu-*`. Short names collide with the theme.
- **Tables.** The comparison table and the journey table each need their own `overflow-x: auto`
  container. The page body must never scroll sideways.
- **FAQ accordion.** Must open on tap, be operable by keyboard, and announce its state. Thirteen items.
- **Images.** WebP, `srcset`, lazy-loaded below the fold, under 200KB. None exist yet.
- **No asset paths to fix.** No prototype was built, so there is nothing relative to find and replace.

## Blind judge

**Gate not taken. 69 / 85. Weakest axis: proof of belonging to the vertical, 10 / 20.**

One round was run, in a fresh subagent that saw only the draft, the fact sheet, the scorecard and the
slot list.

| Axis | Score | Weight |
|---|---|---|
| Proof of belonging to the vertical | 10 | 20 |
| Claims discipline | 11 | 15 |
| Uniqueness against the parent | 9 | 15 |
| Conversion | 10 | 15 |
| Copy in the buyer's language | 9 | 10 |
| Human copy | 7 | 10 |
| Search and AI visibility | 7 | 10 |
| Place in the site | 4 | 5 |
| Design and technical layer | 2 | 5 |
| **Total** | **69** | **100** |

**One hard fail: fewer than two case studies from this vertical.** It is the same fact that failed G-I
before a word was written, and no edit to the copy clears it. The judge's suggested fix asks for pilot
figures that do not exist, and inventing them would be a worse hard fail. Rounds 2 and 3 were not run for
that reason.

Two axes lost points to things that only a built page can fix. **Design and technical, 2 / 5**: nothing
has been rendered, so performance, contrast, keyboard operation, viewports and schema validation are all
reported as unverified in `fact-sheet.md`, and the judge scored them as unverified rather than assumed.
**Place in the site, 4 / 5**: the parent does not link down, which is a WordPress task nobody has done for
any vertical page on this site.

**Publishing below 85 without saying so is forbidden.** This flag travels with the page.
