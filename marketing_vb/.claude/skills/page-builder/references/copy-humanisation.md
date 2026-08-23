# Guardrails and humanisation — the pass that runs after the draft

Phase 3, pass 3. It runs **after** the copy is drafted, as its own step, never as a mental note while
writing. Writing and editing pull in opposite directions; a drafter policing their own tells does
neither job well.

Why it exists: a page that reads as machine-written loses the buyer before the offer lands. The reader
rarely thinks "this is AI". They think "this is a template" and close the tab. On a vertical page that
costs a demo request. And on 3DLOOK pages there is a second cost — a diligence reader who catches an
unsourced number stops evaluating the product and starts evaluating whether anything on the page is
true.

Four layers, in this order. Do not fix while sweeping; mark first, then rewrite.

---

## Layer 1 — Editorial guardrails audit (`brand-assets/style-guides/editorial-guardrails.md`)

Run the 11 principles as an explicit checklist. The five that break pages most often:

- **#1 Substantiation.** A claim with no internal figure or citable source is removed or converted to a
  qualitative dependency statement. Marketing-confident verbs get hedged: **supports**, **may reduce**,
  **can help** rather than **faster**, **reduces**, **eliminates**.
- **#2 One number, everywhere the same.** Every figure byte-identical across hero, body, FAQ and
  disclaimer. Two conflicting figures are never averaged: keep the defensible one or go qualitative.
- **#3 Reserved words.** "independent", "validated", "third-party" only with a named external party and
  a citable output. Defaults: **internal validation**, **benchmark participation**, **dataset
  enrichment**. State the negatives plainly: not peer-reviewed, not third-party validated, not
  clinically certified.
- **#4 No bare headline percentages.** ">95%" invites "of what, measured how, over how many sessions?"
  Replace with a qualitative claim plus one concrete sub-figure plus "detailed methodology available
  under NDA".
- **#6 Medical framing.** "FitXpress is not positioned as a medical device." Never assert that a
  framework "does not apply". Compliance is framed on data-privacy frameworks, not medical-device ones.

Then the mechanical rules:

- **M1 — expand every acronym at first use.** Universal, including the obvious ones (BMI) and the
  authorities (FDA, ICH, GCP). Run a first-use scan over the finished page, not from memory.
- **M2 — no stacked negation.** One clear boundary sentence. No chained negatives, no parenthetical
  "is — and is not —", no "necessary but not sufficient".

Anything bent goes to the **Open items** block for Asselya, per principle #11. No silent editorial
decisions.

---

## Layer 2 — Terminology (`brand-assets/content-strategy/terminology-guardrails.md`)

Asselya's word-level rules. Grep the page for each of these:

| Banned | Use instead |
|---|---|
| em dash (—) | comma, full stop, or brackets. Banned in all contexts, no exceptions |
| "objective" (about our output) | standardized, timestamped, structured, repeatable |
| "reader", "audience", "the following sections", "below" | describe the business reality, never the reading experience |
| "this article", "this guide", "our content" | cut, or define scope in a scope note |
| "by hand" | manually |
| "plus" (stacking capabilities) | including, such as, along with, as well as |
| "let" | allow |
| "so" (introducing a benefit) | reducing…, helping to reduce…, which can reduce… |
| corrective negation "X, not Y" | lead with the recommended approach and its purpose |

Two judgement calls rather than bans: **we / our** — only where ownership matters, otherwise reframe
around the buyer's workflow; **you** — acceptable on a vertical page's conversion sections and
practical guidance, avoided in the educational blocks, which stay authoritative.

The one licensed negation: a product, clinical, legal or regulatory boundary. *"FitXpress supports
clinician review; it is not a diagnostic tool."* That is the exception, and it is used once.

---

## Layer 3 — Tone and AI signatures (`CLAUDE.md` §6, `about-me.md`)

Banned words: **leverage, utilize, harness, robust, seamless, comprehensive, revolutionize,
cutting-edge, game-changer, disrupt, delve, navigate** (figurative), **tapestry, realm**.

Banned phrasings: "In today's fast-paced world…", "Unlock the power of…", "Are you struggling
with…?", "It's no secret that…", "AI-powered" as a standalone value claim, "Furthermore / Moreover /
Additionally" opening sentences.

Banned constructions: **"not just X — it's Y"** and any negative-parallelism variant. **Rule-of-three
punch triads** ("fast, reliable, scalable"). Both are the most reliable AI signature in English
marketing copy and both are hard fails at the judge.

Anti-positioning: never lead with "most accurate", "best-in-class" or "industry-leading". 3DLOOK sells
a trusted workflow layer, and accuracy is scoped, not claimed. Never position the product as "just an
API" either.

---

## Layer 4 — AI tells sweep

### Content

- **Inflated significance** — "a key milestone", "a new era". Say what it does.
- **Borrowed authority** — "experts agree", "studies suggest" with no study named. Name the source or
  cut the claim. On this site that is also guardrail #1 and #3.
- **Empty participial tails** — "…, underscoring our commitment", "…, highlighting the importance of".
  No information. Delete the whole clause; the sentence is finished without it.
- **Brochure adjectives** — "vibrant", "state-of-the-art", "bespoke". Replace with the specific fact
  that made you reach for the adjective, or cut.
- **The challenges-and-opportunities template** — "While challenges remain, the outlook is promising."

### Language

- **Avoiding the plain verb** — "serves as", "represents", "constitutes" where "is" would do.
- **False ranges** — "from strategy to execution", "from startups to enterprises". Poles chosen for
  rhythm, not meaning.
- **Elegant variation** — calling the same thing "the platform", "the solution", "the system" across
  four paragraphs. Repeat the word.
- **Latinate padding** — "in order to" for to, "prior to" for before, "facilitate" for help.

### Structure and formatting

- **Bold-headed vertical lists** where prose would carry the argument. A list is for genuinely parallel
  items, not for making three sentences look organised.
- **Title Case In Every Heading.** Sentence case reads as written by a person.
- **Emoji** in headings or bullets on a B2B page.
- **Uniform paragraph length.** Three-sentence blocks all the way down is the clearest structural tell
  there is. Vary deliberately: a one-line paragraph, then a long one that takes its time.

### Voice

- **Assistant residue** — "Let's dive in", "In this article, we will explore", "Here's everything you
  need to know".
- **Hedging stacks** — "It could potentially be argued that in some cases…". Commit or cut. This is
  distinct from guardrail #1 hedging, which is one deliberate verb ("may reduce"), not a pile of them.
- **Slogan endings** — a closing line that resolves everything neatly. Real pages end on the next
  action.
- **No opinion anywhere.** A page that only states and never judges reads as compiled rather than
  written. Somewhere 3DLOOK should say plainly what the right way to run this workflow is, and be
  willing to be disagreed with.

---

## Positive checks — copy with a person behind it

Stripping tells produces sterile copy, which is its own tell. The pass finishes only when these are
also true:

- [ ] **Specific over abstract.** "15,500 scans a year across a distributed uniform programme" beats
      "significant deployment experience".
- [ ] **Varied rhythm.** Short sentences next to long ones, on purpose.
- [ ] **The buyer's own words**, from the use-case file, `audience.md` and real calls — not internal
      vocabulary.
- [ ] **Complexity admitted.** "Repeatability holds under a controlled capture protocol; it degrades
      with loose clothing" is more credible than a page where everything is a fit.
- [ ] **A boundary stated.** What the product does not cover, said once, plainly. Nothing reads more
      human than a limit — and on this site it is also guardrail #6.
- [ ] **Numbers that are real**, traced to `proof-points.md`, and flagged as pending where they are
      not.

---

## Closing question

Ask once, honestly: **"what here still reads as machine-written?"** Give 2–4 answers and fix those.
That second round is what separates technically clean copy from copy with a person behind it.

## Related agents

`mvb-core:brand-checker` is the deep check — it verifies numbers against `proof-points.md`, tokens
against `DESIGN.md`, and the M1/M2 rules. Use it on the finished page before the blind judge if the
page carries a lot of figures. Do not use `mvb-social:post-brand-checker` — that is a 10-point social
post check, not a page check. Neither replaces this pass, and neither replaces the blind judge.

## Scoring the axis

**Human copy** is worth 10 points on the scorecard. Rubric in `gates-and-scorecard.md`. Score before
fixing, not after: across many pages, the first number tells you whether the problem is one draft or
the drafting prompt.
