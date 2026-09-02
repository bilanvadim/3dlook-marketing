---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
artifact: illustration plan
revision: 3
created: 2026-09-02
status: awaiting_design
blocked_on: Figma blog-banner exports (see section 6)
design_source: DESIGN.md (repo root) — the only source of truth for tokens
corpus_evidence: brand-assets/past-articles/blog/online-pharmacy-bmi-verification.md
---

# Illustration plan: AI Body Data for Wellness Platforms (Hub #8)

Review 2 closed with "ready for final proofreading and illustration planning". This is the
illustration half. It is a brief for a designer, not a visual.

## 1. What the published corpus actually does

Measured, not assumed. Of the nine articles in `brand-assets/past-articles/blog/`, **exactly
one carries images**: `online-pharmacy-bmi-verification`, 2,638 words, **2 images**.

| Property | What the corpus does |
|---|---|
| Count | 2 images for 2,638 words |
| Hero | **None.** The H1 leads; both banners sit inside body sections |
| Placement | One in the section making the problem argument, one in the section describing capability |
| Format | `.webp` at `https://3dlook.ai/wp-content/uploads/YYYY/MM/banner_N.webp` |
| Alt text | Literal description of what is in the frame, then a clause tying it to the article's topic |
| Overlay | Banner 1 carries a short editorial line inside the image; banner 2 carries none |

The house alt style, verbatim from that article:

> Three images show a woman standing with arms at her sides; the left and right images are
> labeled "AI-generated," and the center, "Original." Text above reads, "AI made fake evidence
> cheap", raising concerns for online pharmacy BMI verification.

Note what that does: it describes the frame first, quotes the overlay, and only then connects
to the keyword. It is written for someone who cannot see the image, not as a caption.

**So the house norm is two in-body banners and no hero.** This article is 2,790 words and is a
hub, so three is defensible. Section 5 names which one drops if capacity is short.

## 2. The three banners

### Banner 1 — Progress visibility beyond scale weight (`final.md` line 53)

**Why this one first.** It is the only image on the list that shows something the prose
physically cannot. The article's central claim is that a member can be succeeding while the
scale says nothing, and both reviewers named this section the strongest part of the article.
An image settles in one glance what the section spends 313 words establishing.

**Content.** A member-facing progress view comparing two check-ins. Bodyweight reads the same
in both. A body measurement has moved. The 3D model comparison sits alongside, baseline and
current.

**Pattern.** Device mockup with metric callouts (DESIGN.md §11), phone UI as the carrier asset
(§10).

**Alt text:**

> Wellness app progress view comparing two member check-ins, where bodyweight is unchanged and
> the waist measurement has moved, shown beside a baseline and current 3D body model.

### Banner 2 — Practical wellness-platform workflow (`final.md` line 87)

**Why.** Five ordered steps. A sequence is the one thing a diagram reliably beats prose at, and
the integration/architecture diagram is already a house component pattern (DESIGN.md §11).

**Content.** The five steps as a horizontal flow: consent and baseline capture, selection of
goal-relevant outputs, result presentation, recurring capture under the same conditions,
comparison and connection to the next step. Show the ownership split, because it is the part
teams get wrong: the platform owns program logic, the member relationship, content and
interpretation; the body-data layer owns capture, measurement extraction and the comparable
record.

**Alt text:**

> Five-step wellness platform workflow from consent and baseline capture through recurring
> check-ins to comparison, with platform responsibilities separated from the body-data layer.

### Banner 3 — the opening comparison (`final.md` line 23, inside the intro)

**Why.** Review 2 item 1 rebuilt this paragraph so that three kinds of record each carry a
*different* limitation, replacing a version that wrongly gave two of them the same one. That
correction is the article's frame and it is newly precise. Three columns make it land.

**Content.** Three columns, no winner-loser framing:

| Self-reported entry | Scale reading | Repeatable body data |
|---|---|---|
| Estimated, rounded, not always collected the same way twice | Compares cleanly against last month, but one number compresses every kind of body change | Measurements and visual context, same protocol each time, timestamped |

**Alt text:**

> Three ways a wellness platform can record physical progress, comparing a self-reported entry,
> a scale reading, and repeatable body data.

## 3. What NOT to illustrate, and why

This half matters as much as the list above. Each of these was considered and rejected.

| Candidate | Why not |
|---|---|
| **Hero / top-of-article banner** | The corpus does not use one. The H1 leads. Adding a hero here would be a new convention, not this article's decision to make. |
| **Section 2, the value map** | It is already a table. The article carries seven tables; rendering one as a graphic duplicates it and makes it harder to read on mobile. |
| **Section 7, evaluation criteria as a checklist card** | This was in the v1 suggestion list. It re-renders prose as graphics and adds nothing, and a "checklist" graphic invites being read as a spec or a certification, which is exactly the reading the accuracy section works to prevent. |
| **Section 8, Where FitXpress fits** | A product hero inside the product section would tip a hub page toward a product page. That is the failure the cannibalization guardrail exists to prevent, and the plan's Phase 0 gate is explicit about it. |
| **Section 9, boundaries** | Illustrating what the product does not do gives the boundary more visual weight than the capability. Review 1 item 19 already asked for that list to be shorter and less defensive. |

## 4. Hard constraints specific to this article

Generic brand rules are in section 7. These six come from this article's own claims, and
breaking any of them makes the illustration contradict the text.

1. **Nothing depicting a decision, score, diagnosis, eligibility or reward outcome.** The
   article states plainly that FitXpress does none of these. A wellness-score dial, a
   traffic-light state, an approved/declined badge or a risk band would contradict the boundary
   section visually. This is the single most likely way to get the illustration wrong.

2. **Numbers rendered inside an image must come from an approved claim or be visibly
   illustrative.** Usable claims: `96-97%` accuracy (FX-001), `1.5-2.0 cm` typical error
   (FX-002), under `1 cm` scan-to-scan (FX-003), under 45 seconds (FX-006), 80+ measurements
   (FX-008), ages 16 to 78 / 150 to 220 cm / 38 to 210 kg (FX-011). **Do not invent a precise
   change figure** for the progress mockup, for example "waist −3.2 cm over 8 weeks".

   **Verified 2026-09-02:** `scripts/article_lint.py` catches an invented figure in *alt text*
   and fails the build. It is **blind to a number rendered inside the image**. So this one
   cannot be automated and stays with the designer and with review.

3. **A stored photo is shown blurred; a live capture view is not a stored photo.**
   `compliance.md` and the article agree: blur is automatic *when photos are stored*. A guided
   capture screen showing a live camera view is consistent. A gallery or record of retained
   photos must be blurred. The 3D model is a mesh and carries no face at all.

4. **No named vendors in any UI mockup, and no customer logos.** There are zero wellness proof
   points on file, so nothing may imply a wellness reference customer. Yazen and UK Meds are
   GLP-1 and pharmacy, and must not be re-labelled as wellness in an image any more than in
   prose.

5. **Do not make it corporate-coded.** Corporate wellness is one application in one subsection,
   by Vadim's decision at Review 1 item 2. Office desks, lanyards, HR dashboards, boardrooms or
   benefits-portal styling would reintroduce through the artwork exactly the frame that revision
   2 removed from the text. The article's broad:corporate term balance is 4.3 to 1; the imagery
   should not invert it.

6. **Body representation.** The article's own UX paragraph asks for neutral, non-judgemental
   comparison language and says progress should not be reduced to appearance or weight loss. So:
   a range of body types across the set, no before/after weight-loss trope, no aspirational
   physique, no arrows implying a body should move in one direction.

## 5. If only two banners are possible

**Drop banner 3.** It illustrates a conceptual argument the prose already makes clearly.
Banners 1 and 2 show things prose cannot: a comparison the reader has to see, and a sequence
that reads better as a flow. Two banners also matches the corpus norm exactly.

## 6. Blocked on Vadim: the Figma exports are not on disk

The Figma file Vadim linked is <https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners>
(node `2088-4`). **It cannot be read from here.** Figma requires authentication and a fetch
returns nothing but the word "Figma", no design content.

The repo situation, checked 2026-09-02:

- `brand-assets/past-posts/_figma-exports/` **does not exist**
- `brand-assets/` contains **zero** image files of any kind
- `.claude/agents/social/visual-brief.md` step 3 already reads
  `brand-assets/past-posts/_figma-exports/blog-banners/` and is instructed to **STOP and ask
  Vadim** when it is missing. So this gap is known and already wired into the pipeline; it has
  simply never been filled.

**What to do:** export the banner frames from that file as PNG into
`brand-assets/past-posts/_figma-exports/blog-banners/`. That is the path the pipeline already
expects, so filling it fixes this for every future article, not just this one.

**Until then**, section 7 below is derived from `DESIGN.md` tokens rather than from the actual
banners. That is enough to keep a designer on-brand, and not enough to match the established
banner composition. The difference between "on-brand" and "looks like our other banners" is
what the export buys.

## 7. Design system, from `DESIGN.md`

Verbatim, because `DESIGN.md` is the single source of truth and the older
`brand-assets/color-palette/colors.md` (`#2962FF`) and `fonts.md` (Inter) are superseded stubs.

**Colour.** Navy `#050F40` takes 60 to 70% of the weight on a banner ground. Electric blue
`#143DFF` stays a *single sharp accent*: one callout, one key numeral, one line. Never a large
fill. White dominates on content areas.

**Ground.** Navy radial glow, never flat navy: brighter core `#4F6DFF` / `#0B2299`, through
`#08186B`, to `#050F40` at the edge, plus subtle grain or a faint measurement-grid texture.

**Type.** Satoshi only, headings and body. Nothing else. Use the eyebrow technique for a
section label and oversized numerals for a proof moment.

**Craft.** Soft believable shadows. Generous negative space. Device mockups with real scan
metrics. Product imagery over icons: the three carrier assets are the 3D body-scan render, the
guided-capture phone UI, and the Admin Panel in a laptop or browser frame.

**Don't** (DESIGN.md §14): spread `#143DFF` across large fills, use flat navy blocks, use an
icon where a product asset fits, invent sizes or radii off the scale, put light text on imagery
without a scrim, or introduce any font other than Satoshi. **No purple-pink AI gradients.**

**⚠ The brand mark.** DESIGN.md §10 states that logo files, exact triangle-mark geometry,
clearspace and minimum sizes are **not** in the design export. Request the brand-mark asset kit
before reproducing the mark at small sizes. Do not redraw it from a screenshot.

## 8. Production spec

| Item | Value | Confidence |
|---|---|---|
| Format | `.webp` | Matches the corpus exactly |
| Naming | `banner_1.webp`, `banner_2.webp`, `banner_3.webp` | Matches the corpus |
| Path | `/wp-content/uploads/2026/09/` | Matches the corpus pattern, month is this month |
| Body width | 1200 px, exported at 2x for retina | **Inferred**, not confirmed. DESIGN.md §4 sets the site container at `max-width: 1200px`, so 1200 matches it. Exact export sizes are not in the design export |
| Featured / OG image | Recommend banner 1 doubles as the featured image | **Open question.** The featured-image slot is separate from in-body banners and is what appears in a social share, but the corpus markdown does not show it, so the convention cannot be read from the repo. Confirm with whoever owns WordPress |

Alt text goes in the markdown as `![alt](url)`. It is published copy: `article_lint.py` reads it
as prose, counts it toward the word total and runs the claim gate over it.

## 9. What ships back into the article

Nothing yet. `final.md` carries no image markup, and it should not until the assets exist,
because a broken image reference is worse than no image. When the three files are produced:

1. Insert `![alt](url)` at the three named lines, using the alt text in section 2 verbatim.
2. Run `python3 scripts/article_lint.py workspace/seo/articles/<slug>/final.md`. It must stay
   `VERDICT: PASS`. Asset URLs are handled: they are counted separately from page links and are
   exempt from the canonical trailing-slash rule, and a figure in alt text will fail the claim
   gate.
3. Regenerate the publish package so its embedded copy matches.
