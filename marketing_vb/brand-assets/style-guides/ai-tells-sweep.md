# AI-tells sweep — the pass that makes copy read as written, not generated

**Status:** canonical. One copy, in `brand-assets/style-guides/`. Every content pipeline references
this file; none of them restates it.

Adapted from Victor Shulga's public [`anticopywriting-ai`](https://victorshulga.com/skills/outbound-agents/anticopywriting-ai/)
skill ([source](https://github.com/victor-shulga/gtm-skills/tree/main/anticopywriting-ai)), which
adapts [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(WikiProject AI Cleanup) via Georgiy Rivera's Russian version. Same lineage as `page-builder`, which
is adapted from the same author's `page-builder`.

**Detector:** `brand-assets/style-guides/scripts/detect-ai-tells.py`. Run it before you sweep by
hand — it finds the mechanical hits in a second and stops you missing the obvious.

---

## Why this exists, and what it is not

A reader almost never thinks "this is AI". They think "this is a template" and stop reading. On a
blog article that costs the ranking's whole point; in a LinkedIn DM it costs the reply; on a vertical
page it costs the demo request.

Three things this pass is **not**:

1. **Not "lower the AI score."** Optimising against a detector produces text that is odd in a new
   way. The target is copy a practitioner would recognise as written by another practitioner.
2. **Not a substitute for the guardrails.** `editorial-guardrails.md` (11 principles) governs
   whether a claim may be made at all; `terminology-guardrails.md` governs word choice. This sweep
   runs *after* them and catches a different failure: prose that is factually defensible and still
   reads as generated.
3. **Not a writing-time checklist.** Writing and editing pull against each other. A drafter policing
   their own tells does neither job well. Draft, then sweep as its own step.

---

## The order of operations

```
1. Run the detector            → mechanical hits, density, house-rule violations
2. Fix every hard fail          → non-negotiable, listed below
3. Sweep the soft categories    → judgment, weighted by channel
4. Positive checks              → is there a person behind this?
5. THE SELF-CHECK               → "what here still reads as machine-written?" (2-4 answers)
6. Fix what step 5 found        → this second pass is the whole point
```

Step 5 is the step that gets skipped and the step that matters most. Technically-clean copy and copy
with a voice are different things, and only the second pass gets you the second one.

Do not fix while sweeping. Mark first, then rewrite — otherwise you lose the thread of the argument
halfway through and the result reads patched.

---

## Running the detector

```bash
python3 brand-assets/style-guides/scripts/detect-ai-tells.py <file> --channel <channel> --summary
```

`--channel` is one of `article` · `post` · `dm` · `page` · `any`. It changes which categories apply
and how strict the density budget is; a 600-character DM and a 4,000-word article cannot share a
threshold. Add `--profile linkedin-vadim` to label the report. Drop `--summary` for JSON.

Read three fields first:

| Field | What to do with it |
|---|---|
| `hard_fails` | Fix every entry. Not judgment calls. Line numbers point at the original file. |
| `house_rule_violations` | Fix every entry: hashtags, emoji, Title Case, monotone rhythm, wall of text. |
| `verdict` | `CLEAN` / `SPOT FIXES` / `HARD FAILS` / `REWRITE`. `REWRITE` means redraft the section, not patch it. |

Then `markers_by_category` and `top_offenders` for the soft sweep.

**On the density number.** Markers per 1,000 words. Budgets: 6 for articles and pages, 10 for social
posts, 12 for DMs. Below 250 words the detector counts markers instead of scoring density, because
one marker in an 84-word post is 11.9/1,000 and that is noise, not a signal.

**em dashes are excluded from the density score** and reported separately. They are banned outright
(see below), but they are a global find-and-replace — 50 of them in one article would swamp the
number and hide everything the score is for. Still a hard fail; just counted on its own line.

**The detector is a floor, not the sweep.** It cannot see inflated significance carried by sentence
shape, an argument that never commits, or an ending that resolves too neatly. It reports zero on
plenty of copy that still reads generated. Run it, then read.

---

## Hard fails — fix at any density, any channel

These are already 3DLOOK policy; this section is the consolidated list, not a new rule set.

**Banned words** (CLAUDE.md §6) — leverage, utilize, harness, robust, seamless, comprehensive,
revolutionize, revolutionary, cutting-edge, state-of-the-art, game-changer, disrupt, delve, tapestry,
realm, groundbreaking, best-in-class, industry-leading, world-class, unparalleled, and *navigate* in
its figurative sense ("navigate the regulatory landscape"; navigating to a settings screen is fine).

**Banned phrasings** (CLAUDE.md §6) — "In today's fast-paced / rapidly evolving …", "Unlock the power
of …", "Are you struggling with …?", "It's no secret that …", "Have you ever wondered …", "In this
article we will …", "Let's dive in", "Here's everything you need to know", and "AI-powered" standing
alone as a value claim.

**Negative parallelism** — "It's not just X, it's Y", "not only X but also Y", "This isn't only X,
but …", "It's not about X, it's about Y". The most reliable AI signature in English marketing copy.
Note the trap: it is *also* the shape people reach for when they want to sound emphatic, so it
survives casual editing. Kill it every time.

**Punch triads** — three adjectives in series landing at a clause end: "fast, reliable, scalable",
"quick, visual, and data-backed". A three-item list of real things ("positioning, posture, and
equipment") is a list, not a triad, and is fine. The detector distinguishes them; it flags only
adjectival series.

**em dash (— and –) — banned in all contexts, no exceptions** (`terminology-guardrails.md`). This is
stricter than the upstream skill, which treats em dashes as an overuse problem. Here: comma, full
stop, or brackets. Every occurrence.

**Terminology guardrails** (`terminology-guardrails.md`) — "objective" about our own output, "the
reader / the audience", "the following sections", "see below", "this article / this guide", "by
hand", "let" for allow, "plus" as a capability connector, "so" introducing a benefit, corrective
negation "X, not Y".

**Reserved words** (editorial guardrail #3) — "independent(ly) validated", "third-party verified",
"clinically validated", "peer-reviewed" without a named external party and a citable output. The
compliant forms are internal validation, benchmark participation, dataset enrichment. The detector
suppresses these when the sentence is disclaiming them ("not independently validated" is the correct
phrasing, not a violation) and when they appear inside an FAQ question.

**Bare headline percentages** (editorial guardrail #4) — ">95%", "up to 90%" with no methodology.
Qualitative claim + one concrete sub-figure + "detailed methodology available under NDA".

**Claims discipline** — diagnoses, replaces a clinician / DEXA / reference method, guarantees
compliance, detects fraud, makes decisions, "most accurate", "just an API". Negated and
interrogative forms are the *required* framing and are not violations.

---

## Soft categories — judgment, by channel

Full before/after examples for each: the upstream skill's `references/patterns_en.md`
(and `patterns_uk.md` for Ukrainian). Here is what each looks like and what to do.

### Content

1. **Inflated significance** — "a key milestone", "a new era of", "plays a crucial role",
   "paradigm-shifting", "cornerstone of". Say what the thing does instead. 3DLOOK sells a workflow
   layer; nothing in the product line is a watershed.
2. **Borrowed authority** — "experts agree", "studies have shown", "research suggests" with nothing
   named. Name the source or cut the claim. Also editorial guardrail #1.
3. **Empty participial tails** — "…, underscoring our commitment", "…, highlighting the importance
   of", "…, ultimately driving better outcomes". Zero information. Delete the clause; the sentence
   was finished before it.
4. **Brochure adjectives** — vibrant, bustling, breathtaking, stunning, bespoke, "truly unique",
   boasts, "in the heart of". Replace with the specific fact that made you reach for the adjective.
5. **The challenges-and-opportunities template** — "While challenges remain, the outlook is
   promising", "continues to thrive", "the future is bright".

### Language

6. **AI vocabulary** — intricate, multifaceted, foster, underscore, encompass, pivotal, paramount,
   profound, holistic, nuanced, resonate, "the intersection of", "in line with", "dive deeper", and
   *landscape* in its abstract sense ("the regulatory landscape").
7. **Avoiding the plain verb** — "serves as", "stands as", "embodies", "constitutes", "represents an
   opportunity" where **is** would do.
8. **Elegant variation** — the same thing called "the platform", "the solution", "the system" across
   four paragraphs, because repetition felt wrong. Repeat the word. This one is invisible to the
   detector and common in our drafts.
9. **False ranges** — "from strategy to execution", "from startups to enterprises". Poles picked for
   rhythm, not meaning.
10. **Latinate padding** — "in order to" (to), "prior to" (before), "facilitate" (help), "has the
    ability to" (can), "due to the fact that" (because), "in terms of" (usually cut).
11. **Connective openers** — Furthermore / Moreover / Additionally / In addition. Minimise, and never
    as a transition between H2 sections; use a thematic bridge.

### Structure and formatting

12. **Bold-headed vertical lists** where prose would carry the argument. A list is for genuinely
    parallel items, not for making three sentences look organised. Detector flags 3+ such items.
13. **Bold overuse** — mechanically bolding every term. It stops meaning emphasis at about the fourth
    instance.
14. **Title Case in headings** — sentence case reads as written by a person. H1 is exempt: 3DLOOK
    blog titles are Title Case by convention, so the detector only checks H2 and below.
15. **Emoji in headings or bullets** on a B2B page or article. On social, house rules cap them
    (below).
16. **Uniform paragraph and sentence length** — the clearest structural tell there is. Three-sentence
    blocks all the way down. Vary on purpose: a one-line paragraph, then a long one that takes its
    time. The detector reports sentence-length variation; below 0.35 is monotone.
17. **Mixed straight and curly quotes** in one document. Pick one.

### Voice

18. **Assistant residue** — "Let's dive in", "In this article we will explore", "I hope this helps",
    "Here's an overview", "Great question".
19. **Hedging stacks** — "It could potentially be argued that in some cases…". Commit or cut.
    Distinct from guardrail #1's deliberate single hedge ("may reduce"), which is required.
20. **Slogan endings** — a closing line that resolves everything neatly. "Exciting times ahead", "a
    step in the right direction", "and that changes everything". Real copy ends on the next action or
    the open question.
21. **No opinion anywhere** — copy that only states and never judges reads as compiled rather than
    written. Somewhere, say plainly what the right way to run this workflow is, and be willing to be
    disagreed with.

### Outbound-specific (DMs only)

22. **Opener clichés** — "hope this message finds you well", "I came across your profile", "I admire
    your mission", "excited about your journey", "quick question for you", "I help companies like
    yours", "just following up", "circling back". In a 600-character message one of these burns the
    first line, which is the only line that gets read.

---

## Positive checks — is there a person behind this?

Stripping tells produces sterile copy, which is its own tell. The pass finishes only when these are
true as well:

- [ ] **Specific over abstract.** "15,500 scans a year across a distributed uniform programme" beats
      "significant deployment experience".
- [ ] **Varied rhythm.** Short sentences next to long ones, deliberately.
- [ ] **An opinion exists.** Not just facts arranged in order — a position on what teams should
      actually do.
- [ ] **Complexity admitted.** "Repeatability holds under a controlled capture protocol; it degrades
      with loose clothing" is more credible than a page where everything is a fit.
- [ ] **A boundary stated,** once, plainly. Nothing reads more human than a limit, and on this site
      it is also guardrail #6.
- [ ] **The buyer's own words** from `audience.md`, the use-case files and real calls — not internal
      vocabulary.
- [ ] **Numbers that are real,** traced to `proof-points.md`, flagged as pending where they are not.

---

## The self-check (step 5)

Stop after the first rewrite and answer honestly, in 2–4 short bullets: **"what here still reads as
machine-written?"** Then fix those.

Common residue, and none of it is detectable by script:

- Rhythm is still even; every sentence lands the same way.
- The ending is a slogan.
- The structure is textbook: thesis → three supports → conclusion.
- No first person where it would have carried more.
- No position taken, only description.
- Every paragraph opens with the same grammatical move ("The…", "This…", "The…").

Write the answers down in the artefact's `changes_summary` or the pass log. An unwritten self-check
does not happen.

---

## Channel profiles

| | Article / page | Social post | Outbound DM |
|---|---|---|---|
| Detector channel | `article` / `page` | `post` | `dm` |
| Density budget | 6 / 1,000 words | 10 / 1,000 | 12 / 1,000 |
| Hard fails | all | all | all |
| Structure checks | em dash, bold, Title Case, emoji, rhythm, list ratio | em dash, emoji, hashtags, rhythm | em dash, emoji, wall of text |
| House rules | 0 emoji | **0 hashtags, max 2 emoji** (LinkedIn) | 0 hashtags, 0 emoji, no single dense block |
| Muted | outbound clichés | outbound clichés, filler | Title Case, bold, participial tails, challenges template, slogan endings, bare percentages |
| Self-check | mandatory, written down | mandatory, 2 bullets | mandatory, 1 line |

The DM column mutes most structure categories because a 600-character message has no headings to
Title Case and no room for a participial tail. What it does not mute is the hard fails: a single
"leverage" in message 1 is the whole message.

---

## Who runs this, and where

| Pipeline | Agent | When |
|---|---|---|
| SEO / blog | `mvb-seo:seo-writer` | Draft-time: the hard fails only, from memory. No sweep while writing. |
| SEO / blog | `mvb-seo:seo-editor` | **Pass 3c** — the full sweep and the self-check loop. This is the real gate. |
| Social | `mvb-social:post-drafter` | Draft-time hard fails + a one-line self-check before handing off. |
| Social | `mvb-social:post-brand-checker` | Verdict only, per post. Does not edit. |
| Social | `mvb-social:social-editor` | **Pass 2b** — sweep across all 9 posts, detector per post. |
| Outbound | `mvb-outbound:message-sequencer` | Per message, `dm` channel, before writing the CSV. |
| Pages | `page-builder` | Phase 3 pass 3, layer 4 — see `references/copy-humanisation.md`, which owns the page-shaped version of this and adds the terminology and guardrail layers. |
| Any artefact | `mvb-core:brand-checker` | Deep check: numbers against `proof-points.md`, tokens against `DESIGN.md`, M1/M2, plus this sweep. |
| Ad hoc | `/humanize` | Vadim pastes text or a path; full skill treatment. |

`mvb-social:post-brand-checker` is the fast 13-point social check. It is not this sweep and does not
replace it — `social-editor` Pass 2b does the sweep for the social track.

---

## Related

- `brand-assets/style-guides/editorial-guardrails.md` — the 11 principles. Claims, not prose.
- `brand-assets/content-strategy/terminology-guardrails.md` — Asselya's word-level rules.
- `brand-assets/style-guides/blog-style-guide.md` — voice and structure for articles.
- `.claude/skills/page-builder/references/copy-humanisation.md` — the page-shaped four-layer version.
- `about-me.md`, `audience.md` — voice and audience, canonical.
- `~/.claude/skills/anticopywriting-ai/` — the interactive skill, with the full upstream
  before/after pattern references for both English and Ukrainian.
