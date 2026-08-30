# Run brief — social pack for `glp-1-market-hub`

Shared context for every `post-drafter` run in this pack. Written 2026-08-28 by the coordinator.
Read this first, then your own profile prompt.

## Repo root
`/home/vadim_prod/3dlook-marketing/marketing_vb` — your cwd is `/home/vadim_prod`, so use absolute paths.

## The article

Published **today, 2026-08-28**, at <https://3dlook.ai/content-hub/glp-1-market/> — a hub refresh
republished in place at the same URL.

**Text of record:**
`/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/seo/articles/glp-1-market-hub/published-live-2026-08-28.md`

Two traps in that folder:

1. **`publish-package.md` has NO article body** — meta and checklist sections only. Do not use it
   for the article text.
2. **The `draft-v*.md` files no longer match the live page.** The article got a further editorial
   pass after `draft-v6-revision2.md` left the pipeline: ~500 words shorter, a new market-structure
   section, a market-indicator table, and materially harder hedging. **Ignore the drafts.** Every
   claim you make must be traceable to `published-live-2026-08-28.md`.

## Claims discipline — stricter than usual

This is regulated-adjacent health content and the live text is deliberately hedged. Respect the
live wording exactly:

- The **~$200B by 2030** figure is the **global incretin market** — explicitly *"a broader category
  than GLP-1 receptor agonists alone."* Never state it as "the GLP-1 market will be $200B."
- **~25 million** US users projected by 2030, per J.P. Morgan. The drafts' "25 to 30 million" and
  the "6M in 2024 → 10M in 2025" trajectory are **not on the live page** — do not use them.
- **KFF figures** (43% vs 28% coverage, 59% higher-than-expected use, 66% spending effect) apply
  **only to surveyed firms with 5,000+ workers.** Never generalise to "employers".
- **Scale weight** does not distinguish **fat mass, lean mass and fluid balance**. A 2024 review
  found substantial variation in lean-mass change during GLP-1 treatment; that review also notes
  lean mass and muscle mass are related but distinct.
- **FitXpress:** two photos (front and side), ~30–45 seconds, no specialised hardware, 80+
  measurements, plus body-fat-percentage / lean-mass / fat-mass estimates. Repeatability is
  *"typical scan-to-scan differences of less than 1 cm for most evaluated measurements"* —
  **never a single universal accuracy number.**
- **FitXpress is not a medical device.** It does not diagnose, decide, prescribe, or determine
  eligibility. It complements DXA, BIA and calibrated scales. Say "is not a medical device",
  never "is not positioned as".
- Delivery models on the live page: telehealth, in-person/hybrid clinic, pharmacy-led,
  employer-supported. Data-access and reporting requirements vary by structure and contract.

## MANDATORY — expand `GLP-1` at first use

Write **`glucagon-like peptide-1 (GLP-1)`** on the first mention, then `GLP-1` thereafter.

This is rule M1 in `brand-assets/content-strategy/terminology-guardrails.md` §Part 1.1, which names
`glucagon-like peptide-1 (GLP-1)` as its worked example. The commonly-known exception list is closed
— **AI, WWW, iOS, BMI, CEO, UK, US, EU** — and GLP-1 is not on it. The file's scope line says
explicitly: *"ALL 3DLOOK corporate content … social posts … There is no channel exemption."*

The `twitter-company` and `instagram-company` posts in this pack were both drafted without the
expansion and had to be corrected. Do not repeat it. `BMI` is never expanded.

## You cannot call `post-brand-checker`

Your agent definition grants only Read, Write, Grep, Glob — no Task tool — so hard rule #6 is not
executable in your context. Do not spend turns trying. Run the 10-point checklist, the Part 2
terminology guardrails and the ai-tells hard fails yourself, and report your self-check. The
coordinator runs the independent `post-brand-checker` on your saved file afterwards.

## Past-posts map — your spec's path is wrong for one profile

Step 4 of your spec says read 5+ past posts from `brand-assets/past-posts/{profile}/`. That path only
resolves for one profile. What actually exists:

| Profile | Past posts | Where |
|---|---|---|
| `linkedin-company` | 15 | `brand-assets/past-posts/linkedin-company/` — the path works |
| `linkedin-katerina` | 9 | **`brand-assets/past-posts/linkedin-personal/katerina-galich/`** — NOT `past-posts/linkedin-katerina/`, which does not exist. Read the real path; do not silently continue without them. |
| everyone else | 0 | No folder. Per your spec, continue without them — do not STOP. |

Note on the two GLP-1 posts that do exist in Katerina's folder
(`2025-09-10-glp-1-hype-vs-healthcare-reality.md`, and `2026-04-09-bmi-checks-not-just-glp1-thing.md`
under her folder): both **predate** rule M1 (2026-07-07) and the terminology sync (2026-08-25). They
ship bare `GLP-1`/`GLP1`, heavy emoji and other now-banned patterns. Use them for **voice and
cadence only** — they are not precedent for current rules.

## Article visuals for your Design tip

`publish-package.md` section 4 is **stale** — it says no OG image was commissioned, which is no
longer true. The live page ships three 2026 assets. Anchor your Design tip on one of these:

| Asset | What it shows |
|---|---|
| `cover-3.webp` | A woman at a desk with a laptop, her body stats shown across three dates, highlighting changes in body fat and mass, under headline text on GLP-1 market growth and progress tracking. |
| `banner_1-3.webp` | Market projections: $200B by 2030, 25M US users, 43% large-employer coverage, 59% higher-than-expected use, 66% higher spending. Credited to J.P. Morgan and KFF. |
| `banner_2-2.webp` | The five requirements for scalable progress tracking: baseline, remote capture, records, context, professional review. 3DLOOK logo upper right. |

Brand tokens (from `DESIGN.md`): navy `#050F40`, electric blue `#143DFF` as a single sharp accent,
Satoshi type. No body-exposure imagery.

**Do not write that the article assets avoid photography.** `cover-3.webp` *is* a photograph of a
woman at a desk; only the two `banner_*` files are abstract data cards. QC flagged exactly this
false statement in the `twitter-company` design tip. Describe whichever asset you actually anchor on.

**Already claimed:** `twitter-company` took `banner_1-3.webp` (cropped to the 25M panel);
`instagram-company` took `cover-3.webp` (3-slide carousel). Prefer a different asset or a clearly
different treatment.

## Angles already used — diverge from these

| Profile | Angle taken |
|---|---|
| `twitter-company` | Market scale vs documentation: volume is growing faster than how programs document progress, built on the ~25M US users projection. Closes on "same capture method every time, or records aren't comparable." |
| `instagram-company` | The individual check-in record: three dates only compare if captured the same way; scale weight can't say *what* changed (fat vs lean vs fluid). No market-size figures at all. |

Read the sibling `post.md` files in this folder before writing, and pick a genuinely different
entry point.

## Output

- Save to `workspace/social/articles/glp-1-market-hub/{profile}/post.md`.
- **`article_slug: glp-1-market`** — the real published slug, NOT the folder name. The folder is
  `glp-1-market-hub` because it mirrors the SEO working directory, but the slug field must match
  `publish-package.md` frontmatter and the live URL, both of which say `glp-1-market`. QC caught
  this on the first two posts: a social artifact carrying the folder name cannot be joined to the
  published URL.
- Then **append only your own entry** to the existing `profiles` array in
  `workspace/social/articles/glp-1-market-hub/manifest.json`. Leave every other entry and field
  untouched. **Never** set `ready_for_review: true` — that is the coordinator's call.
- Length field in the manifest: `word_count_body` for `linkedin-*`, `character_count_body` for the
  three non-LinkedIn company accounts. Exactly one, not both.

CTA link target: <https://3dlook.ai/content-hub/glp-1-market/>
