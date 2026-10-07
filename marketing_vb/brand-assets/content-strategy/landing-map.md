# FitXpress landing map: which page every article links down to

> **Decided by Vadim, 2026-09-29.** Articles bring the traffic, and each one links to its vertical's FitXpress landing page, where the reader converts. Each hub in `content-plan.md` has one landing. Every FX landing embeds one shared demo form (`FX | LP | Demo`, anchor `#demo`); GTM tags the lead with `fx_vertical`.
> **Read by:** `seo-planner` (plans the down link), `seo-writer` (places it), `seo-editor` (checks it), `seo-publisher` (checklist line `landing_link`).
> **Updated by:** the `page-builder` handoff, when a landing ships: its row flips to `live`, and "Link now" becomes the landing URL.
> **Sources:** keywords in `workspace/research/seo-fitxpress-2026-09/2026-09-29-landing-keywords.md`; tracking in `…/2026-09-27-tz-tracking-hubspot-ga4.md`.

## The map

"Link now" is the URL an article uses today. While a landing is `planned`, that column holds the closest live FitXpress page, and the article records the relink in its Open items. Never link a `planned` URL: it does not exist yet.

| Hub | Landing (target URL) | Status | Link now | Demo button now | Anchors (use one, as written or lightly inflected) |
|---|---|---|---|---|---|
| Hub 0 (Main Health) and FitXpress in general | `/fitxpress/` | planned (draft `workspace/pages/fitxpress/`) | `/` | none, link only | FitXpress · AI body scanner · body scanning API |
| BMI / weight verification, in any hub | `/fitxpress/bmi-verification/` | planned (live today at `/for-bmi-verification/`) | `/for-bmi-verification/` | `/for-bmi-verification/` | BMI verification · remote BMI verification · weight and BMI verification |
| Hub 1 Fitness, and proposed Hub 9 Body Composition | `/fitxpress/for-connected-and-digital-fitness/` | **live** | `/fitxpress/for-connected-and-digital-fitness/` | same page | body scanning for fitness apps · mobile alternative to a gym body scanner · body composition tracking for fitness apps |
| Hub 2 Telehealth | `/fitxpress/for-telehealth/` | planned (live today at `/structured-body-data-for-telehealth-digital-health-programs/`) | `/structured-body-data-for-telehealth-digital-health-programs/` | same page | remote patient monitoring for weight loss · body scanning API for telehealth platforms · remote body measurement for telehealth |
| Hub 3 GLP-1 | `/fitxpress/for-glp-1-programs/` | planned (URL and H1 "FitXpress for GLP-1 programs: body composition tracking between clinic visits" confirmed by Vadim 2026-10-07; draft v2 in `workspace/pages/for-glp-1-programs/`) | `/structured-body-data-for-telehealth-digital-health-programs/` | same page | body composition tracking for GLP-1 programs · remote progress tracking for GLP-1 clinics |
| Hub 4 Insurance underwriting | `/fitxpress/for-insurance-underwriting/` | planned (draft `workspace/pages/for-insurance-underwriting/`) | `/for-bmi-verification/` | same page | accelerated underwriting · build and BMI evidence for underwriting |
| Hub 5 Wellness | `/fitxpress/for-wellness-programs/` | planned; angle = remote biometric screening (Vadim, 2026-09-29) | `/fitxpress/for-connected-and-digital-fitness/` | same page | remote biometric screening · at-home biometric screening · body measurements for employee wellness programs |
| Hub 6 Bariatrics | `/fitxpress/for-bariatric-clinics/` | planned | `/for-bmi-verification/` | same page | bariatric pre-authorization documentation · body measurement records for bariatric programs |
| Hub 7 Clinical trials | `/fitxpress/for-clinical-trials/` | planned | `/` | none, link only | remote anthropometric measurement for clinical trials · body measurement for DCT platforms |
| Hub 8 Occupational health | `/fitxpress/for-occupational-health/` | planned | `/` | none, link only | occupational health screening software · occupational health software |

## Rules

1. **One down link to the hub's landing (the "Link now" column), placed within the first 30% of the article body.** Put it in the short answer, the first two H2 sections or the first "Where FitXpress fits" mention. Clarity shows health articles are read to only 5–35% depth, so a link placed near the end is never seen. Anything the article says about BMI or weight verification also links to the BMI verification row, whatever the hub.
2. **The anchor comes from the row's anchor list** and reads as part of the sentence. Never "click here", "learn more" or a bare URL. The anchor is a keyword the landing owns, which is how the landing holds its position.
3. **The article's title, H1 and meta title never use the landing's primary keyword** (the first anchor in the row, or the primary in the keyword map). The article takes the informational version: "what is…", "how to…", "…process". For example, a telehealth article may be titled "How remote weight checks work in telehealth programs", but not "Remote patient monitoring for weight loss".
4. **CTA by intent still decides whether a demo CTA appears** (TOFU soft, MOFU evaluation, BOFU direct). When it does, the "Book a demo" button links to `{landing}#demo` once the landing is `live` with the shared form. Until then it links to the "Demo button now" page. It never links to `/contact-us/` or a form made for the article, and there is no demo button where that column says "none". TOFU keeps its down link (rule 1) as a plain contextual link, not a demo push.
5. **A second conversion for readers who are not ready** is allowed: the eBook or a checklist, as the plan specifies. It is a different offer with its own form, and it never replaces the down link.
6. **Planned-landing debt.** When "Link now" is a stand-in, the publisher adds this line to Open items: `Relink when /fitxpress/for-{vertical}/ goes live: <anchor> → <current link>`. When a landing flips to `live`, the page-builder handoff lists the published articles of that hub that still point to the stand-in (SEO plan §1.5).
7. **Biometric screening boundary (Hub 5).** FitXpress covers the body-measurement part of a biometric screening: waist circumference is measured from two photos, BMI is calculated from height and weight (Smart Scales, in beta, cross-checks a self-reported weight), and body composition comes as estimates. Blood pressure, cholesterol, glucose and other blood tests are out of scope, and any article or landing says so plainly. It makes no ADA, GINA, EEOC or HIPAA wellness-program compliance claim: incentive design is the employer's call, made with counsel. The page does not interpret results or assign health risk.
