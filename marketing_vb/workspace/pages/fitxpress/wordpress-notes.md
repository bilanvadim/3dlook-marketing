---
product: fitxpress
type: wordpress-notes
vertical: all
date: 2026-09-27
---

# WordPress notes: /fitxpress/

For whoever builds the page in WordPress (the developer, per the SEO plan §0). Nothing here is
published from this pipeline.

## 0. Before building

1. **Remove the 301** `/fitxpress/` → `/`. The page cannot be indexed while it is in place.
2. **Change the 301** `/fitxpress` (no slash) → `/content-hub/fitxpress-admin-panel-launch/` to point at `/fitxpress/`.
3. Save a Search Console snapshot for `/`, `/for-bmi-verification/` and "ai body scanner" / "fitxpress" before go-live (baseline rows in `gate-reports.md`).
4. Closest template to clone: `/structured-body-data-for-telehealth-digital-health-programs/` (the only page whose schema graph is already right). Delete its telehealth-specific blocks; keep hero, FAQ accordion, CTA band.

## 1. Yoast fields

| Field | Value | Length |
|---|---|---|
| SEO title | `FitXpress: AI body scanner and body measurement API | 3DLOOK` | 60 |
| Meta description | `FitXpress turns two smartphone photos into 80+ body measurements, BMI and body composition estimates via API and SDKs. Book a demo or see pricing.` | 146 |
| Canonical | `https://3dlook.ai/fitxpress/` (self) | |
| Slug | `fitxpress` | |
| Parent page | none (top level); breadcrumb Home → FitXpress | |
| Breadcrumb title | `FitXpress` | |
| Focus keyphrase | `AI body scanner` (secondary: fitxpress, body scanning software, body scanning API, body measurement API) | |
| Robots | index, follow | |
| Open Graph title / description | same as SEO title / meta description | |

Both title and description differ from the homepage (`3DLOOK - AI-powered 3D body scanning solution`)
and from every hub article. When the homepage is rewritten as the general 3DLOOK page, its title should
**drop "AI body scanner"** to stop the two URLs competing (homepage copy is out of this package).

## 2. Schema (JSON-LD)

Yoast outputs `WebPage`, `Organization`, `WebSite` and `BreadcrumbList` by default. Either disable
Yoast's page-level graph for this URL and paste the block below whole, or merge: keep Yoast's
`Organization` / `WebSite` nodes and add `SoftwareApplication` and `FAQPage` with the same `@id`s. The
FAQ answers are generated from the visible FAQ text; if the copy changes, change both. Valid JSON,
no HTML inside strings.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://3dlook.ai/fitxpress/#webpage",
      "url": "https://3dlook.ai/fitxpress/",
      "name": "FitXpress AI body scanner: body measurements your health program can act on",
      "description": "FitXpress turns two smartphone photos into 80+ body measurements, BMI and body composition estimates via API and SDKs. Book a demo or see pricing.",
      "isPartOf": {
        "@id": "https://3dlook.ai/#website"
      },
      "about": {
        "@id": "https://3dlook.ai/fitxpress/#software"
      },
      "mainEntity": {
        "@id": "https://3dlook.ai/fitxpress/#software"
      },
      "breadcrumb": {
        "@id": "https://3dlook.ai/fitxpress/#breadcrumb"
      },
      "hasPart": [
        {
          "@id": "https://3dlook.ai/fitxpress/#faq"
        }
      ],
      "inLanguage": "en-US"
    },
    {
      "@type": "SoftwareApplication",
      "@id": "https://3dlook.ai/fitxpress/#software",
      "name": "FitXpress",
      "alternateName": "FitXpress by 3DLOOK",
      "url": "https://3dlook.ai/fitxpress/",
      "applicationCategory": "BusinessApplication",
      "applicationSubCategory": "Mobile body scanning software and body measurement API",
      "operatingSystem": "iOS, Android, Web",
      "brand": {
        "@type": "Brand",
        "name": "FitXpress"
      },
      "publisher": {
        "@id": "https://3dlook.ai/#organization"
      },
      "provider": {
        "@id": "https://3dlook.ai/#organization"
      },
      "description": "FitXpress is body scanning software for digital health, insurance, wellness and fitness programs. Two guided smartphone photos return 80+ body measurements, calculated metrics such as BMI and BMR, body composition estimates and a 3D model through an API and web and mobile SDKs.",
      "featureList": [
        "80+ body measurements",
        "Calculated metrics: BMI and BMR",
        "Body composition estimates: body fat %, lean mass, fat mass",
        "3D body model",
        "Predicted weight (Smart Scales, beta)",
        "Scan-to-scan comparison of two selected scans",
        "Real-Time Pose Validation (RTPV)",
        "Clothing Detector",
        "Face obfuscation at capture",
        "API with web and mobile SDKs, including supported iOS and Android integrations",
        "Optional FitXpress Admin Panel for monitoring and exporting results"
      ],
      "audience": {
        "@type": "BusinessAudience",
        "audienceType": "Telehealth and GLP-1 weight-loss programs, online pharmacies, life insurers, employer wellness programs and health plans, occupational health providers, clinical trial sponsors and CROs, bariatric and metabolic clinics, connected and digital fitness platforms"
      },
      "areaServed": "Global",
      "offers": {
        "@type": "Offer",
        "name": "Starter",
        "price": "1000",
        "priceCurrency": "USD",
        "url": "https://3dlook.ai/pricing/",
        "description": "Up to 500 scans per month",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "1000",
          "priceCurrency": "USD",
          "unitText": "MONTH"
        }
      },
      "softwareHelp": {
        "@type": "CreativeWork",
        "url": "https://docs.fitxpress.3dlook.me"
      }
    },
    {
      "@type": "Organization",
      "@id": "https://3dlook.ai/#organization",
      "name": "3DLOOK",
      "url": "https://3dlook.ai/",
      "foundingDate": "2016",
      "logo": {
        "@type": "ImageObject",
        "url": "https://3dlook.ai/wp-content/themes/3dlook/assets/img/logo.svg"
      },
      "brand": [
        {
          "@type": "Brand",
          "name": "FitXpress"
        },
        {
          "@type": "Brand",
          "name": "Mobile Tailor"
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://3dlook.ai/fitxpress/#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://3dlook.ai/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "FitXpress",
          "item": "https://3dlook.ai/fitxpress/"
        }
      ]
    },
    {
      "@type": "FAQPage",
      "@id": "https://3dlook.ai/fitxpress/#faq",
      "url": "https://3dlook.ai/fitxpress/#faq",
      "isPartOf": {
        "@id": "https://3dlook.ai/fitxpress/#webpage"
      },
      "about": {
        "@id": "https://3dlook.ai/fitxpress/#software"
      },
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is FitXpress?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "FitXpress is 3DLOOK's AI body scanner for health, wellness, insurance and fitness programs. It turns two guided smartphone photos into 80+ body measurements, calculated metrics such as BMI, body composition estimates and a 3D model. Results are delivered through an API and SDKs."
          }
        },
        {
          "@type": "Question",
          "name": "What does each scan return?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Each scan returns 80+ body measurements, BMI and BMR, body composition estimates (body fat %, lean mass, fat mass), a 3D model and a predicted weight. Capture-quality flags come with the results. Programs can also compare two scans they select."
          }
        },
        {
          "@type": "Question",
          "name": "How long does a scan take?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The time is under 45 seconds from the photos to structured results. The person takes two photos, one from the front and one from the side."
          }
        },
        {
          "@type": "Question",
          "name": "Does FitXpress need special hardware?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. FitXpress works with a standard smartphone camera and needs no additional hardware."
          }
        },
        {
          "@type": "Question",
          "name": "How accurate is the FitXpress body scanner?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "3DLOOK's published figures use expert tape measurements as the reference. Reported accuracy is approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. The relevant question is whether the reported error and repeatability are suitable for the intended workflow. Detailed methodology is available under a non-disclosure agreement."
          }
        },
        {
          "@type": "Question",
          "name": "Is there a body measurement API and SDK?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. FitXpress is delivered through an API and web and mobile SDKs, including supported iOS and Android integrations. Access is set up after a demo call or under a non-disclosure agreement."
          }
        },
        {
          "@type": "Question",
          "name": "Can we use our own branding and keep results server-side?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes. Onboarding, consent wording and the results view are yours to design. Results can also stay server-side, with the person seeing only a confirmation screen. The photo capture layer stays fixed to protect measurement quality."
          }
        },
        {
          "@type": "Question",
          "name": "Where is data stored, and how long are photos kept?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Data is hosted on AWS, primarily in US-West-2 and partially in US-East-1. Photos are deleted immediately after processing, or within 30 days under the customer's policy. Retained photos are automatically blurred, and faces are obfuscated at capture."
          }
        },
        {
          "@type": "Question",
          "name": "Is FitXpress HIPAA compliant?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "HIPAA is a regulatory framework, not a certification. FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA. The BAA is available for qualifying enterprise deployments."
          }
        },
        {
          "@type": "Question",
          "name": "Is FitXpress a medical device, and what about the FDA?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "FitXpress is not a medical device. It is not cleared, authorized or approved by the FDA, and 3DLOOK makes no representation as to whether FDA clearance, authorization or approval is required for a particular use case. The UK and EU position is in the trust FAQ."
          }
        },
        {
          "@type": "Question",
          "name": "Does 3DLOOK train its models on our data?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "No. 3DLOOK does not use production customer data to train its models unless the customer gives explicit, documented authorization."
          }
        },
        {
          "@type": "Question",
          "name": "How much does FitXpress cost?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "The entry plan, Starter, is $1,000 per month for up to 500 scans. Custom plans cover larger volumes. Current plans are on the pricing page."
          }
        }
      ]
    }
  ]
}
```

Notes:
- `offers` names the Starter tier exactly as live `/pricing/` shows it on 2026-09-27 ($1,000 per month,
  up to 500 scans). Re-check before publishing; if the price changes, change the page and this node together.
- `operatingSystem` lists iOS, Android and Web because the public SDK wording is "web and mobile SDKs,
  including supported iOS and Android integrations" (`tech-spec.md`).
- No `aggregateRating`: the G2 rating on `/pricing/` is not in `proof-points.md` and was not used.
- Validate in Google's Rich Results Test and validator.schema.org after publishing.

## 2a. Documentation link

The integration section and the results section link to `https://docs.fitxpress.3dlook.me` as the API
documentation. Make both links **dofollow** (the subdomain currently gets one nofollow link from the
site, SEO plan §1). When `/developers/` ships, it becomes the link target and links on to the docs
(TODO item, not a page marker).

## 3. FAQ markup

- One accordion, 12 items, each question an `<h3>` inside a `<button aria-expanded>`; answer panel
  with `id` referenced by `aria-controls`. Answers present in the HTML on load (not fetched on click),
  otherwise FAQPage content does not match visible content.
- Section `id="faq"` to match `@id` `https://3dlook.ai/fitxpress/#faq`.
- Keyboard: Enter / Space toggles, focus ring `#B1BDFF` 3px, 2px offset (`DESIGN.md` §6).

## 4. Blocks and components

| Section | Component | Notes |
|---|---|---|
| Breadcrumbs | Theme breadcrumb | Home → FitXpress; do not insert a middle level |
| Hero `[HERO]` | Navy `#050F40` band with radial glow and grain (`DESIGN.md` §2) | H1 in Satoshi 700; white "Book a demo" button with dark text; text link to `#outputs`. Spec row as oversized numerals. Visual: guided-capture phone UI next to a 3D body render |
| `[LOGO STRIP]` | Grayscale logo row | UK Meds, Yazen, Healthyr. Label "Used by health programs including". No metrics, no links to case studies |
| Problem | Plain text block | White background |
| `[OUTPUTS]` table | Responsive table, scrolls inside its own container under 768px | `id="outputs"` |
| `[WORKFLOW]` | Numbered steps, 6 | Real product imagery (capture UI) over icons |
| `[INDUSTRIES]` | 8 cards, 20px radius, 2 columns desktop, 1 mobile | Whole card clickable; card title is the link text. This is the in-body link-down block |
| `[PAYLOAD]` | Text block + two-column table (program / destination), scrolls in its own container under 768px | Admin Panel in a browser frame as optional visual. No code sample: canon has no public field names |
| `[INTEGRATION]` | Diagram: your app (SDK capture) → your backend → FitXpress API → your backend / your UI | Admin Panel shown as optional side element in a browser frame |
| `[ACCURACY]` | Text block with numeral row (96-97%, 1.5-2.0 cm, below 1 cm) | Numerals must not appear without the paragraph that scopes them |
| `[COMPLIANCE]` | Two-column table on desktop, stacked on mobile | Link to trust FAQ at top of block |
| Pricing | Short text block | Link to `/pricing/` |
| FAQ | Accordion (section 3) | |
| Closing CTA | Footer-style navy band, white "Book a demo" button | Soft-alternative links under the button |

Namespace custom classes (`fx-parent-…`) to avoid theme collisions. If a prototype ships its own header
and footer, delete both; the theme supplies them.

## 5. Alt text

| Image | Alt |
|---|---|
| UK Meds logo | `UK Meds logo` |
| Yazen logo | `Yazen logo` |
| Healthyr logo | `Healthyr logo` (the current site asset is labelled "Reddit"; fix it) |
| Hero phone UI | `Smartphone screen guiding a person through a front photo for a body scan` |
| Hero 3D render | `3D body model generated from two smartphone photos` |
| Integration diagram | `Diagram of photos moving from an app to the FitXpress API and back as structured results` |
| Admin Panel frame | `FitXpress Admin Panel listing scans with filter and export controls` |

All alt texts are under 125 characters, no em dash, no borrowed keywords.

## 6. Demo form and analytics events

**Demo form, kept short:** first name, last name, work email, company, a required consent checkbox
linking to the Privacy Policy, and one optional free-text field ("What are you building?"). Real
`<label for>` on every field, errors next to the field, submit button disabled while sending, a
confirmation state after submit. Form name: `fitxpress_demo`.

The page has **one primary action** ("Book a demo", hero and closing band), **one soft alternative**
(the accuracy framework article in the closing section) and **one price signal** (Starter tier, link to
`/pricing/`). The trust FAQ and vertical links are navigation, not conversion actions.

| Event (GA4) | Trigger | Parameters |
|---|---|---|
| `demo_click` | Click on any "Book a demo" | `section`: hero / close |
| `generate_lead` | Successful demo form submit (mark as key event; mirror to HubSpot form submission) | `form_name`: `fitxpress_demo` |
| `docs_click` | Click on either API documentation link | `section`: integration / results |
| `pricing_click` | Click to `/pricing/` | `section` |
| `soft_alt_click` | Click on the accuracy framework link in the closing section | |
| `vertical_card_click` | Click on an industries card | `vertical` |
| `faq_open` | FAQ item expanded | `question` |

Tracking spec: `workspace/research/seo-fitxpress-2026-09/2026-09-27-tz-tracking-hubspot-ga4.md`. The
"Book a demo" buttons must be real `<a>` links, not JS-only handlers (SEO plan §1 item 3). **None of these
events is verified: they are specified pre-publish and must be checked firing manually after publish.**

## 7. Performance

WebP images with `srcset`, lazy-load everything below the hero, under 200KB each; preload Satoshi; honour
`prefers-reduced-motion`. Check at 375 / 768 / 1280 / 1440 and at 320 for horizontal scroll.

## 8. After publishing

Add to `page-sitemap.xml`; request indexing in Search Console; update `llms.txt`; replace FitXpress links
in nav, footer and articles; monitor GSC weekly for 3 months (SEO plan §9.0).
