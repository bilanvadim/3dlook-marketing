# DESIGN.md — 3DLOOK / FitXpress design system

> Read before building any marketing artifact (landing page, HTML prototype, 2-pager, deck, social, email). Single source of truth for brand tokens and art direction. Voice lives in `about-me.md`; audience in `audience.md`.
>
> **Rule for agents:** use tokens exactly as written. All values below are confirmed from the official Figma export (`Color / Typography / Buttons / Border Radius / Spacing / Header / Footer`) unless marked `⚠`. Never introduce fonts, colors, or radii not defined here. Never resurrect superseded values (§15).
>
> **Sources (2026-11-12):** tokens = Figma export above · logo rules, secondary font, icons, photography and deck rules = the 3DLOOK brand guideline, Google Slides «3DLOOK Branding» `1p1cW9pE-a4nvqlRRUzirIU6tvSksz7T20YxaFMAuEQ4` (Vadim's copy of Kristina's 2024 guideline) · files = `brand-assets/logos/` and `brand-assets/product-imagery/` (collected from the live site, each with its README / INDEX).

---

## 1. Brand essence
Clinical-grade precision meets consumer-app polish. Confident, spacious, technical but human. Every layout should read as **precision + trust + modern AI**.

**Design principles**
- **Restraint over density.** One or two big moments per page; generous negative space.
- **Product over icons.** Prefer real product imagery (3D body-scan render, guided-capture phone UI, Admin Panel in a laptop/browser frame) over generic icons.
- **Precision as a visual language.** Fine measurement lines, grids, keypoint dots, big exact numerals.
- **Depth, not flat fills.** Navy zones use a radial/mesh glow + subtle texture, never a dead flat block.
- **Evidence-forward.** Oversized numerals for stat/proof moments — the number is the hero.

---

## 2. Color system (confirmed)

### Brand
| Token | Hex | Role |
|---|---|---|
| `--black` | `#000000` | Pure black; dark buttons, high-contrast type |
| `--white` | `#FFFFFF` | Dominant background on content zones; text on dark |
| `--blue` | `#143DFF` | **Electric blue** — the single sharp accent: CTAs, key numbers, links, highlights |

### Blue scale (10 steps)
`#ECEFFF` · `#D8DEFF` · `#B1BDFF` · `#8A9CFF` · `#4F6DFF` · **`#143DFF`** · `#0F2ECD` · `#0B2299` · `#08186B` · `#050F40`
- Tints (`ECEFFF → B1BDFF`): soft cards, chips, captions on dark, focus ring (`#B1BDFF`).
- Mids (`8A9CFF / 4F6DFF`): accents, hovers, data-viz.
- Core `#143DFF`: primary accent. `#0F2ECD`: primary hover. `#0B2299`: gradient end.
- Deeps (`08186B / 050F40`): **navy surfaces** — hero, proof bands, CTA, footer.

### Gray scale (10 steps)
`#F9F9F9` · `#F2F2F2` · `#E5E5E5` · `#D1D1D1` · `#A8A8A8` · `#808080` · `#666666` · `#4C4C4C` · `#333333` · `#1A1A1A`
- `F9F9F9–E5E5E5`: backgrounds/surfaces. `D1D1D1–A8A8A8`: borders/lines. `808080–666666`: muted text. `4C4C4C–1A1A1A`: strong text / near-black.

### Neutral scale (blue-tinted navy family — pixel-read, unlabeled in source)
`#ECEFFF` · `#D8DEFF` · `#BABFDB` · `#7D89CF` · `#4D5DAC` · `#4756A0` · `#2B3772` · `#343A59` · `#232941` · `#0F1040`
Use for desaturated navy surfaces/gradients where the pure blue scale feels too saturated. Treat Brand/Blue/Gray as primary; Neutral is secondary.

**Usage weighting:** white dominant on content; navy `#050F40` takes 60–70% weight on hero/proof/CTA/footer; electric blue `#143DFF` stays a *single* sharp accent — never a large fill.

**Navy glow gradient (hero / CTA / footer):** radial glow, brighter blue upper-center → deep navy at edges. Stops: `#4F6DFF/#0B2299` glow core → `#08186B` → `#050F40` edge. Add subtle grain or a faint measurement-grid texture. Rounded top corners on the footer band (~30–40px).

**Print/collateral variant (2-pager):** print art direction used a marginally warmer navy `#0A1338`, ink `#0B0B0C`, muted `#5D6070`, same blue tints. For **web** use the canonical values above; `#0A1338` is acceptable for **print**. Electric blue `#143DFF` is identical everywhere.

`⚠` Semantic status colors (success/pending/error) are not defined in the palette. If a status UI is needed (e.g. scan Success/Pending), choose accessible green/amber and flag for confirmation — do not treat as brand tokens.

### Product colour coding (approved by Vadim, 2026-10-22)
Each product owns one hue. Use it on cross-product surfaces (homepage, product menus and cards, Content Hub tags) so a visitor can tell the products apart at a glance. Product pages keep their own art direction.

| Product | Token | Hex | Role |
|---|---|---|---|
| FitXpress | `--fx` / `--fx-l` | `#143DFF` / `#8A9CFF` | Electric blue; the light tint is for text and lines on dark |
| Wrist Measurement | `--wm-deep` / `--wm` / `--wm-l` | `#1B0942` / `#7A3CF0` / `#B89BEE` | Violet, as on the live `/wrist-measurement/` hero |
| Mobile Tailor | `--mt-paper` / `--mt-ink` | `#EEEBE5` / `#111111` | Strict monochrome for fashion: paper and ink |
| Homepage base | `--ink2` | `#070A1C` | Near-black navy behind the product colours |

Rules: one product colour per element, never mixed in one component; on dark use the light tints (`--fx-l`, `--wm-l`, `--mt-paper`); the electric-blue CTA stays the primary button everywhere.

---

## 3. Typography — Satoshi

**Typeface:** **Satoshi** for both headings and body (web, print, social, video). Decks use Jost (§3b).
**Weights:** Regular **400** · Medium **500** · Bold **700** (Light **300** and Black **900** exist for display accents). **Satoshi has no 600:** the guideline lists Light / Regular / Medium / Bold, the live site serves only 400 / 500 / 700, and the Figma org fonts are static styles. A `600` request renders as 700, so headings marked Semi Bold below are set in Bold.
**Import:** `https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,700,900&display=swap`
**Fallback:** `'Satoshi','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif`. Embed or outline Satoshi in print PDFs.

### Headings
| Token | Size | Weight |
|---|---|---|
| Display | 80px | Bold (700) |
| H1 | 65px | Bold (700) |
| H2 | 50px | Bold (700) |
| H3 | 40px | Bold (700) (Figma label «Semi Bold»; no 600 exists) |
| H4 | 35px | Bold (700) (same) |
| H5 | 27px | Medium (500) |

Heading treatment: line-height ~1.08, letter-spacing −0.02em. On web, scale headings responsively (e.g. `clamp()`) down from these desktop sizes.

### Body
| Token | Size | Weight |
|---|---|---|
| Body lg | 20px | Regular (400) |
| Body | 17px | Regular (400) |
| Body sm | 12px | Regular (400) |
| Body (medium) | 16px | Medium (500) |
| Body lg (medium) | 20px | Medium (500) |
| Body-menu | 16px | Medium (500) |

Body line-height 1.5. **Eyebrow technique** (signature): small uppercase label above section headings — 13px, weight 700, letter-spacing 0.14em, color `--blue` (muted variant `--g500`), margin-bottom 18px. **Hero stat numerals:** oversized (print 72–120pt; web large `clamp()`).

### 3b. Jost — secondary typeface (brand guideline, slide 12)
**Jost** is used **in presentations (Google Slides decks), in the Mobile Tailor widget, and wherever Satoshi is unavailable.** Weights: Light 300 · Regular 400 · Medium 500 · Semi Bold 600. Free on Google Fonts (`https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&display=swap`), so it works in Slides and in Claude artifacts where Fontshare can't load.

---

## 4. Spacing scale (confirmed)
`2 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 60 · 80 · 96 · 120` (px).
Use these steps only. Component rhythm favors 8/12/16/24; section padding favors 60/80/96/120.

**Layout:** container max-width `1200px` (Desktop 1440 frame) up to `1920`; horizontal padding `clamp(24px, 5vw, 80px)`; section vertical rhythm `clamp(56px, 8vw, 110px)`. Breakpoints in source: **Desktop 1920, Desktop 1440, Gadgets (mobile)**.

---

## 5. Border radius (confirmed)
Scale: `0 · 4 · 5 · 15 · 20 · 30 · 40 · 9999` (px).
- Buttons / inputs: **4–5px**
- Chips / small cards: **15px**
- Cards / panels: **20px**
- Large surfaces / footer band / feature blocks: **30–40px**
- Pills / avatars / circular: **9999px**

---

## 6. Buttons

Two shapes, four fills each. Base: Satoshi 700, 16px; padding ~`14px 26px`; transition transform/background/shadow; hover lift `translateY(-1px)`; focus-visible `outline: 3px solid #B1BDFF; outline-offset: 2px`.

**Rectangular** (radius 4–5px) — primary page actions, label like "Get in touch":
| Variant | Default | Hover |
|---|---|---|
| Black | bg `#000`, white text | slight lift |
| Blue (primary) | bg `#143DFF`, white text | bg `#0F2ECD`, lift |
| Outline / ghost | white bg, `--ink` text, `--ink` border | bg `--ink`, white text |
| Text-only | no fill, `--ink` text | underline / blue text |

**Pill** (radius 9999px) — content/nav actions, label like "Read Articles" with a trailing arrow icon (↗ diagonal for nav/external, ↘ down-right). Same four fills: Blue, Black, Outline, Text-only. On-navy variant: white or blue pill.

**Play button:** small rounded control (▶) for video, on dark.

On navy backgrounds, primary CTA is typically a **white** button with dark text (see footer).

---

## 7. Header (structure from live site — Figma frame is a placeholder)
The `Header.png` export contains only empty breakpoint frames, so use the production structure:
- **Left:** △ 3DLOOK logo (triangle mark + wordmark).
- **Nav (Body-menu, 16px Medium)** with dropdowns: **Use Cases** (Telehealth & Weight Loss · Connected & Digital Fitness · Weight & BMI Verification) · **Technology** · **Pricing** · **Resources** (Case Studies · Content Hub · Terms & Policies) · **Made-to-Measure** (Mobile Tailor · Pricing · Made-to-Measure · On-Demand Manufacturing · Uniform Fitting · Sign In) · **About 3DLOOK** (About Us · Partners · Careers · Contact Us).
- **Right:** "Let's talk" CTA button.

---

## 8. Footer (confirmed from export)
Full-width navy radial-glow band, rounded top corners (~30–40px). Three CTA-headline variants share one footer body:

**CTA band (centered):**
- Heading (Display/H1, Satoshi Bold, white): **"Let's talk"** / **"Request a Demo"** / **"Unlock Body Data"**.
- Subcopy (Body, light-muted): e.g. "Contact us today to learn how AI-powered body scanning technology can drive your revenue growth."
- CTA: white rectangular **"Get in touch"** button. *Unlock Body Data* variant uses two buttons: **"Book a Consultation"** (white) + **"Explore Technology"** (outline).

**Trust badges (centered, two outlined navy pills):** HIPAA Compliant (caduceus) · GDPR (stars circle).
> **The badge stays on the site as is (Vadim, 2026-09-18)**, so footer designs keep it. It is a site element, not copy: in text (articles, pages, posts, outbound, decks) "HIPAA compliant" is still banned and the wording comes from `brand-assets/product-info/compliance.md` (live trust FAQ: HIPAA is a framework, not a certification).
> **Confirmed 2026-10-19 (Vadim): the footer badge on every page is a given and stays**, `/fitxpress/` included. Audits and status checks don't list it as a defect. Everywhere else the approved wording applies.

**Link section:** △ 3DLOOK logo (left) · **What We Do** (FitXpress · Mobile Tailor · Technology · Case Studies) · **About 3DLOOK** (About Us · Content Hub · Careers) · **Ready to get started?** with social icons (Facebook · Instagram · X · LinkedIn · YouTube). Column headers in muted blue-gray; links in white.

**Legal row (muted small):** left — GDPR EU-representative notice ("3DLOOK INC. is a company located outside of the European Union… GDPR-Rep.eu… Our Public Privacy Dashboard"); right — Legal · Privacy Policy.

---

## 9. Motion
Scroll-reveal with stagger on section entry; `scroll-behavior: smooth`; always honor `@media (prefers-reduced-motion: reduce)`. Button hover lift `translateY(-1px)`; transitions ~0.15s ease. Keep motion subtle and precise — no bounce/overshoot.

---

## 10. Art direction & imagery
- **Hero/proof zones:** navy radial glow + subtle grain or measurement-grid texture; optional blue scan-line / keypoint dots over a body render.
- **Three carrier assets:** real 3D body-scan render, guided-capture phone UI, Admin Panel in a laptop/browser frame — prefer over icons.
- **Motif:** the 3DLOOK triangle mark + fine measurement-line accent, used sparingly (never edge stripes).
- Soft, believable shadows; generous negative space; device mockups with real scan metrics.

- **Product imagery library:** `brand-assets/product-imagery/` (34 images from the latest pages of the live site: 3D renders, capture UI on phones, dashboard on a laptop, API code card, Wrist and Mobile Tailor sets). Use these before generating anything; never generate fake product UI. `INDEX.md` says what each one shows and where it may be used.

### Logo (brand guideline, slides 6-9)
Files and full rules: `brand-assets/logos/README.md`. In short: the **horizontal lockup** (symbol + wordmark) is the primary logo; the symbol alone is for tight spaces. **Always black or white**, never blue, gradient, outlined, shadowed, 3D, stretched, rotated, mirrored or cropped. Minimum size: lockup **90 px wide**, symbol **20 px high**. Keep clearspace around it. On imagery, darken or lighten the image until the logo reads.

### Icons (slide 13)
Simple, light line icons with one consistent stroke weight across a set; keep lines as light as the surrounding type. Icons support, they don't replace product imagery (§1 "Product over icons"). No icon set is stored yet; draw new ones in that style.

### Photography (slides 14-15)
Always high quality (upscale if needed). Vibe: **aspirational, confident, elegant, clear.** The guideline's own examples are fashion editorials from the retail era; for FitXpress use real people in health, fitness and clinical settings in the same register (see `product-imagery/fitxpress/lifestyle-person-with-app.png`), and keep fashion imagery for Mobile Tailor.

### Presentations / decks (slides 16-21)
Decks are set in **Jost** (§3b) on black and white with electric blue as the single accent.
- **Cover:** an image, or just the logos (3DLOOK × partner) on a dark or light background.
- **Lines** are the main device: a **black** line above or beside the title, a **grey** line to separate text blocks. A line is always as long as the row it belongs to.
- **Title length:** on dense slides the title takes at most ⅓ of the slide width (½ at most); secondary text may sit to the right of the title.
- **Black rectangle** behind a short subtitle to label a visual.
- **Circles with numbers** for steps, agendas and numbered lists.
- Charts: §2 reserves the blue mids (`#8A9CFF` / `#4F6DFF`) for data-viz; the guideline's chart examples (slide 19) use multi-colour series for many categories. `⚠` No chart palette is defined beyond that.

---

## 11. Recurring component patterns
Comparison table (HTML, "compare by role not hype"), FAQ accordion, integration/architecture diagram, device mockup with metric callouts, stat rows with oversized numerals, status table, trust-badge pills, "OPTIONAL"-tagged subordinate modules, eyebrow-labelled sections.

---

## 12. Accessibility
Body text meets **AA contrast** minimum. Never place light text on light imagery without a **scrim**. Visible focus ring (`#B1BDFF`, 3px, 2px offset). Respect reduced-motion.

---

## 13. Copy-paste CSS `:root` (canonical web tokens)
```css
:root{
  /* brand */
  --black:#000; --white:#fff; --blue:#143DFF;
  /* blue scale */
  --blue-50:#ECEFFF; --blue-100:#D8DEFF; --blue-200:#B1BDFF; --blue-300:#8A9CFF;
  --blue-400:#4F6DFF; --blue-500:#143DFF; --blue-600:#0F2ECD; --blue-700:#0B2299;
  --blue-800:#08186B; --navy:#050F40;
  /* gray scale */
  --g50:#F9F9F9; --g100:#F2F2F2; --g200:#E5E5E5; --g300:#D1D1D1; --g400:#A8A8A8;
  --g500:#808080; --g600:#666666; --g700:#4C4C4C; --g800:#333333; --g900:#1A1A1A;
  --ink:#1A1A1A;
  /* radius */
  --r-0:0; --r-4:4px; --r-5:5px; --r-15:15px; --r-20:20px; --r-30:30px; --r-40:40px; --r-pill:9999px;
  /* spacing */
  --s-2:2px; --s-4:4px; --s-8:8px; --s-12:12px; --s-16:16px; --s-20:20px; --s-24:24px;
  --s-32:32px; --s-40:40px; --s-48:48px; --s-60:60px; --s-80:80px; --s-96:96px; --s-120:120px;
  /* layout + type */
  --maxw:1200px; --pad:clamp(24px,5vw,80px);
  --font:'Satoshi','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  /* product colour coding (§2, 2026-10-22) */
  --fx:#143DFF; --fx-l:#8A9CFF; --wm-deep:#1B0942; --wm:#7A3CF0; --wm-l:#B89BEE;
  --mt-paper:#EEEBE5; --mt-ink:#111111; --ink2:#070A1C;
}
/* @import url('https://api.fontshare.com/v2/css?f[]=satoshi@400,500,600,700,900&display=swap'); */
```

---

## 14. Do / Don't
**Do:** keep electric blue as one sharp accent · lead proof zones with oversized numerals · use navy radial glow + texture, never flat · prefer product imagery · use the type scale and spacing steps exactly · use the eyebrow technique · white CTA button on navy · honor reduced-motion.
**Don't:** spread `#143DFF` across large fills · use flat navy blocks · use icons where a product asset fits · invent sizes/radii off-scale · put light text on imagery without a scrim · introduce fonts other than Satoshi (web, print, social, video) and Jost (decks, Mobile Tailor widget) · colour the logo or use a 3D version of the symbol · request Satoshi 600.

---

## 15. Superseded — do NOT use
- **Bricolage Grotesque** and **IBM Plex Sans** appeared in the earliest telehealth prototype, built **before** this design system existed. They are **not** brand fonts. Canonical type is **Satoshi** only.
- Earlier ad-hoc radii (22/34/7px) and the smaller gray set — replaced by the confirmed scales above.
- **3D / extruded versions of the symbol** (the site favicon `uploads/2023/10/cropped-3dlook-black-logo-1-*.png`, Drive folders «3dlook_logo + mark» 2021 and «Logo-Fonts 2021») — outdated; the guideline says don't make the symbol 3D. Use `brand-assets/logos/`.
- **«Brand Guideline.pdf» on Drive (2026-10-22)** is the Activitis Education brand book, not 3DLOOK. The 2021 «3DLOOK Brand Identity Guidelines» PDF is superseded by the Slides guideline above.
- Guideline neutral `#F3F3F3` = the same role as `--g100` `#F2F2F2`; use the token on web, either is fine in Slides.
