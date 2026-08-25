---
name: page-builder
description: >-
  Production line for 3DLOOK website pages on 3dlook.ai (WordPress + Yoast). Takes ONE page request —
  a FitXpress or Mobile Tailor use-case (vertical) page, a product page, a case study, a campaign
  landing — and runs it end to end: routes it to a Kit, runs the G-I existence gate and the G-A
  architecture gate BEFORE a word is written, drafts the structure, then runs copy, guardrails,
  humanisation, AI-visibility, UI/UX, conversion and technical passes, enforces the G-T technical
  gate, and hands the draft to a blind judge that did not build it (threshold 85/100).
  Use whenever someone says: "build a page for [vertical]", "we need a FitXpress page for insurance",
  "rewrite /for-bmi-verification/", "add a use-case page to the site", "campaign landing",
  "зроби сторінку під вертикаль", "сторінка на сайт", "лендинг під кампанію",
  "нужна страница под [вертикаль]", or when auditing an existing 3dlook.ai page against the standard.
  Do NOT use for blog / SEO articles — those belong to /new-article (mvb-seo) and this skill will send
  you there. Not for social posts (/post-from-article), not for outbound (/outbound), not for the
  homepage positioning rewrite.
---

# page-builder — the 3DLOOK website page production line

A repeatable line for pages on **3dlook.ai** (WordPress, Yoast SEO). The point is that page #10 comes
out as good as page #1, and that nothing ships carrying a number nobody can trace.

Three rules carry the whole thing:

1. **The site architecture is an input, not a step.** `references/site-inventory.md` holds the current
   page inventory, the URL logic and the known gaps. A page cannot be placed inside an architecture
   that does not exist. The two hierarchies here have different depths — the homepage is the FitXpress
   parent, `/mobile-tailor/` is the Mobile Tailor parent — so check the inventory rather than assuming
   a `/product/for-vertical/` shape. No agreed URL → stop and resolve it with Vadim first.
2. **Gates are stop-filters, not suggestions.** G-I blocks the page existing. G-A blocks writing.
   G-T blocks publishing. G-J — a blind judge that did not build the page — blocks it again on
   quality. A page that fails a gate goes back; it does not proceed with a note in the margin.
3. **Every number comes from `brand-assets/product-info/proof-points.md`.** A figure that is not
   there does not go on the page. Not "approximately", not "around" — it goes into Open items and
   the slot stays visibly empty. This is guardrail #1 and #2 from `editorial-guardrails.md`, and it
   is the fastest way this pipeline loses credibility.

## What this skill does not own

| Request | Where it goes |
|---|---|
| Blog / SEO article, hub, comparison, buyer guide | `/new-article` → mvb-seo (`seo-planner` Phase 0 resolves it against `content-plan.md`) |
| Social posts from a published article | `/post-from-article` → mvb-social |
| Outbound campaign copy | `/outbound` → mvb-outbound |
| Scoring a pipeline artifact on the 20-point rubric | `/qc` → `mvb-core:quality-controller` |
| Deep brand / fact check of a brief or article | `mvb-core:brand-checker` (the deep one — **not** `mvb-social:post-brand-checker`) |

The blog Kit is deliberately absent. Two article pipelines competing for the same page is how the
content plan gets contradicted. If a request is really an article, say so and route it.

---

## Phase 0 — Intake

Collect before anything else. Ask only for what is missing; never invent an answer.

| Field | Why it matters |
|---|---|
| Page type | Selects the Kit (`references/page-types.md`) |
| Product | `fitxpress` or `mobile_tailor` — they have different ICPs, verticals and case studies |
| Vertical / segment | Must match a file in `brand-assets/product-info/use-cases/` |
| Target buyer (title, seniority, market) | From the use-case file's ICP block and `audience.md` |
| Search + buying intent | Commercial / transactional — a use-case page is BOFU, not education |
| Place in the site | Parent page, URL, siblings, which pages link in (`references/site-inventory.md`) |
| One conversion action | The live site uses "Book a demo" / "Talk to sales" / "Start a trial" — pick one |
| Proof available | Which case studies from **this** vertical, which numbers, which approved quote |
| Language | English (the site is English-only) |

**Read before writing anything** (or request a pack from `mvb-core:context-pack-builder`):

- `CLAUDE.md` §2 (two products), §6 (tone + banned phrases), §10 (artifact rules), §12 (compliance)
- `about-me.md` — voice and claims discipline; `audience.md` — the segment's hook and its
  "what NOT to say" list
- `brand-assets/product-info/use-cases/{fx|mt}-{vertical}.md` — **mandatory input.** No use-case file
  → write it first (same rule `hypothesis-generator` follows) or stop
- `brand-assets/product-info/proof-points.md` — the only source of numbers
- `brand-assets/product-info/case-studies/` — the only source of client names and client metrics
- `brand-assets/product-info/compliance.md`, `messaging.md`, `faq.md`, `tech-spec.md`, `pricing.md`
- `brand-assets/style-guides/editorial-guardrails.md` — the 11 principles + M1/M2, non-negotiable
- `brand-assets/content-strategy/terminology-guardrails.md` — Asselya's word-level rules
- `DESIGN.md` — the design system. It outranks any generic UI recommendation
- `references/site-inventory.md` — where this page lives and what is already there

Artifacts go to `workspace/pages/{slug}/` (never into chat), frontmatter carrying
`product`, `type`, `vertical`, `status`, per CLAUDE.md §10. Log to `workspace/pages/{slug}/log.md`.

---

## Phase 1 — Route to the Kit

Read `references/page-types.md` and load **only** the Kit you need.

| Page type | Kit | Status |
|---|---|---|
| Use-case / vertical page (`/fitxpress/for-…/`, `/mobile-tailor/for-…/`) | `references/kit-vertical-page.md` | full Kit |
| Campaign landing (gated asset, paid, outbound) | `references/kit-vertical-page.md`, no nav, one action, no sibling block | adapted |
| Product page (FitXpress, Mobile Tailor, Technology) | no Kit yet — build from the vertical Kit, say so | gap |
| Case study page | no Kit yet — the site has no individual case-study pages at all | gap |
| Blog / hub / comparison | not this skill — `/new-article` | routed away |

Never silently substitute a Kit. When there is no Kit for the type, name the substitution in the
handover and record which slots you invented.

Two references apply to every page type: `references/copy-humanisation.md` (Phase 3, pass 3) and
`references/ux-pass.md` (Phase 3, pass 5). `references/gates-and-scorecard.md` is loaded at Phases 2,
4 and 5.

---

## Phase 2 — The gates before the first word

### G-I · Should this page exist (use-case / vertical pages only)

Runs first. Full checklist in `references/kit-vertical-page.md`. In short: a use-case file, **2+
publishable case studies from this vertical**, five facts that are not on the parent page, real
demand, and a realistic shot at the 60% uniqueness rule.

**Fail → no page.** A section on the product page plus the vertical's hub article carries it until a
second case exists. That is not a downgrade; it is what stops the site filling up with pages that
cannibalise each other.

### G-A · Architecture gate

- [ ] The page has a parent, a final URL and a decided sibling set
- [ ] Cannibalisation checked against `references/site-inventory.md` and the published article
      inventory — no existing page or hub already targets these queries
- [ ] Inbound internal links named: which existing pages will link here
- [ ] Search Console baseline captured if the URL already exists (rewrites always do)

**Placement on this site:** a FitXpress vertical page is a child of the homepage and lives at
`/for-{vertical}/`; a Mobile Tailor one is a child of `/mobile-tailor/` and lives underneath it. Do
not invent a `/fitxpress/` path level — it 301s to the homepage. The known debt is that neither parent
links down to its verticals in the body, only through the nav dropdown; ask for that block in the
handover. Details and the one page that needs normalising are in `references/site-inventory.md`.

Checkpoint: Vadim approves placement, URL and angle before Phase 3.

---

## Phase 3 — Build

Structure first. Passes 2–7 can run in any order; structure cannot move.

**1. Structure.** Fill every Kit slot top to bottom. A slot is dropped only deliberately, and the
reason goes in `gate-reports.md`. Mark visuals inline: `[HERO]`, `[CONTEXT]`, `[COMPLIANCE]`,
`[WORKFLOW]`, `[CASE CARD]`, `[QUOTE]`, `[INTEGRATION]`.

**2. Copy.** In the buyer's vocabulary, taken from the use-case file, `audience.md` and real calls.
Nouns for deliverables, numbers for claims, and every number traceable to `proof-points.md`. Outcomes
over features — the KPI block of the use-case file is the spine. A differentiator without proof is
deleted, not softened.

**3. Guardrails + humanisation — one mandatory pass, run after the draft is finished.**
Start with the detector (`brand-assets/style-guides/scripts/detect-ai-tells.py --channel page --summary`), then run `references/copy-humanisation.md`: the 11 editorial guardrails and M1/M2, the terminology
guardrails, CLAUDE.md §6 banned phrases, then the AI-tell sweep. Do not fold this into writing; a
drafter policing their own tells does neither job well. The pass ends with the honest question "what
here still reads as machine-written?" and a second round of fixes. Copy that skipped this pass does
not reach Phase 4.

**4. Search and AI visibility.** Primary query in H1 and the first 100 words. One H1, no skipped
levels. FAQ built from `faq.md` and real vertical objections, phrased the way a buyer asks. A
comparison or criteria table where the topic allows — structured blocks are what AI search quotes.
Schema per the Kit. **Only one page on this site ships FAQPage and Service schema today** — the
telehealth page — while `/mobile-tailor/for-uniforms/` has eleven visible answers and no markup at
all. Copy the telehealth page's graph; it is the cheapest win available here.

**5. UI/UX.** Run `references/ux-pass.md`. `DESIGN.md` decides tokens — Satoshi, `#143DFF` as the
single accent, navy `#050F40` surfaces, the 4/5/15/20/30–40 px radius scale, the 8-step spacing
rhythm. Accessibility first, then touch, then performance, then layout. Scannable in 60 seconds,
mobile first, tables scrolling inside their own container.

**6. Conversion.** One primary action matching the site's own language. Inline actions contextual to
their section. A soft alternative for buyers not ready to talk: the accuracy framework article, a
vertical checklist, the ebook. Short form. Analytics events on view, first input, submit and contact
clicks.

**7. Technical.** Indexable, in the sitemap, canonical to self, Yoast title ≤ 60 and description
≤ 155 characters, valid schema, images WebP and lazy-loaded, page weight controlled.

---

## Phase 4 — G-T · Technical gate (before publish)

- [ ] Indexable, in the sitemap, canonical points to self
- [ ] Schema validates: Service (or Product) with `audience` + `areaServed`, FAQPage, BreadcrumbList
- [ ] Performance and accessibility within threshold; checked at 375 / 768 / 1280 / 1440
- [ ] One primary conversion action; analytics events verified firing manually, not assumed
- [ ] Every `[marker]` replaced, alt text everywhere
- [ ] `fact-sheet.md` written for the judge — what it cannot see from the copy

---

## Phase 5 — G-J · Blind judge

Scored by a **fresh subagent that did not build the page**, against the scorecard in
`references/gates-and-scorecard.md`. Threshold **85 / 100**. The builder never marks its own work up.

1. **Spawn a blind judge** — a new general-purpose subagent with a clean context. Never a fork of
   this session, never the drafting agent, and **not** `mvb-core:quality-controller` (that one grades
   pipeline artifacts on the 20-point rubric with full project context — a different job, and not
   blind). Give it only: the page draft, the page type, the Kit's slot list, the scorecard, and
   `fact-sheet.md` (final URL, canonical, schema types present, measured performance, viewports
   checked, contrast results, whether analytics events were verified manually, and the sources behind
   every number on the page).
   **Do not give it** the intake reasoning, the gate justifications, which slots were dropped and
   why, or your own view of how the page turned out. The dropped-slot excuse is exactly what a
   self-scorer uses to mark itself up.
2. **It returns JSON only**, no prose:
   `{"scores": {<axis>: int}, "total": int, "hard_fails": [...], "lowest": "<axis>",
   "one_fix": "<one concrete edit>"}` — axes and weights from the scorecard, scored harshly.
3. **Gate = `total ≥ 85` AND `hard_fails` empty.** The hard-fail list is in the reference.
4. **Not taken →** fix every `hard_fail` first, then apply `one_fix` to the `lowest` axis, then
   **rescore with a NEW subagent**. Never re-ask the same judge; a judge shown its own note applied
   grades the note, not the page.
5. **Stop after 3 rounds.** Still short → hand over flagged "gate not taken — X/85, weakest axis =
   `<axis>`" and let Vadim decide. **Silent publishing below 85 is forbidden.**

Save every round as `workspace/pages/{slug}/judge-round-N.json`. Report the final score as a table
with the points lost and why. A scorecard that always returns 95 measures nothing.

Checkpoint: Vadim approves the final page and meta together, the way `/new-article` does it.

---

## Phase 6 — Handoff to whoever publishes it

3DLOOK does not publish from here — the page goes to whoever owns WordPress. Ship five things per
`references/handoff-kit.md`: the page, `README.md`, `TODO.md`, the WordPress notes (Yoast fields,
schema blocks, FAQ markup), and the assets folder.

- **Unfinished stays visibly unfinished.** One searchable pattern (`[PLACEHOLDER]`, `[QUOTE — needs
  client approval]`) in the markup and the same list in `TODO.md`. Plausible filler that looks
  finished never gets replaced.
- **Blockers first**, then placeholders, then claims that need Asselya's or Whitney's confirmation,
  then nice-to-have. Conflicting numbers in the source material go in as a conflict — guardrail #2
  forbids averaging them and forbids silently picking one.
- **Open items block** for every bent guardrail, per principle #11. No silent editorial decisions.
- **Say what you skipped**, in writing, in the README.

---

## Phase 7 — Post-launch review

30 and 90 days against the G-A baseline: impressions and position in Search Console, demo requests
attributed to the page, scroll depth.

- Zero demo requests at 90 days → back for a conversion and copy pass, or a review of the page's
  place in the site.
- Check separately whether the parent product page or the vertical's hub article lost ground. If it
  did, the new page is a duplicate — fold it back into a section.

---

## Working rules

- **Never fabricate proof.** No invented figures, clients, certifications or standards. Missing proof
  is flagged as missing: "to confirm with Vadim — not fabricated".
- **Publication rights are not a formality.** Mobile Tailor customer ARRs never appear publicly.
  Client names, logos and metrics only from `case-studies/`, and only where that specific use is
  approved.
- **Accuracy is scoped, never bragged.** Reframe to "accurate enough for which decision?" with the
  four conditions (reference method, protocol, population, workflow). Never lead with "most accurate"
  or "best-in-class" — that is an anti-positioning violation and an automatic hard fail.
- **Medical framing is fixed language.** "FitXpress is not a medical device." State the boundary
  directly; "positioned as" is banned for product, intended-use and regulatory statements
  (`terminology-guardrails.md` §2.10). Never assert that a regulatory framework "does not apply".
- **One page, one job.** A page serving two intents serves neither.
- **A price signal belongs on the page.** `/pricing/` is public with real tiers: link to it and name
  the entry tier. Never publish the internal per-request rates from `pricing.md` — they contradict
  the live page (see the conflict note in `references/site-inventory.md`).
- **Say what you skipped.** A slot dropped for missing input is stated in the handover, not quietly
  shipped as a thinner page.
- **Never grade your own page.** The Phase 5 score comes from a model that did not write the copy and
  does not know the reasoning behind it. Self-assessment is a mood, not a measurement.
- **Humanisation is a pass, not a habit.** It runs as its own step after the draft. Watching for
  tells while drafting produces cautious copy that still reads as generated.
