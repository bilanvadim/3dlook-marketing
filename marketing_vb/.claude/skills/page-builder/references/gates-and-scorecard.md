# Gates and scorecard — 3DLOOK pages

Four gates and one scorecard. They exist because the expensive failures on a website are decided
before the writing starts and after it finishes, not during.

| Gate | When | Blocks |
|---|---|---|
| **G-I** | first, vertical pages only | the page existing at all |
| **G-A** | before the first word | writing |
| **G-T** | before publish | publishing, on technical grounds |
| **G-J** | after G-T | publishing, on quality — scored by a model that did not build the page |

---

## G-I · Should this page exist (vertical pages only)

Full detail in `kit-vertical-page.md`. Summary:

- [ ] Use-case file exists in `brand-assets/product-info/use-cases/`
- [ ] 2+ publishable case studies from this vertical in `product-info/case-studies/`
- [ ] Demand: content-plan row, Search Console volume, or ≥15% of outbound pipeline
- [ ] 5 facts absent from the parent product page
- [ ] The market's BD owner confirms the objections differ
- [ ] Parent and URL settled: homepage + `/for-{vertical}/` for FitXpress, `/mobile-tailor/` +
      `/mobile-tailor/for-{vertical}/` for Mobile Tailor (`site-inventory.md`)
- [ ] The 60% uniqueness rule can realistically be met

**Fail →** a section on the product page plus the vertical's hub article. Revisit when the second case
lands. A waiver is Vadim's call and gets recorded with its reason.

---

## G-A · Architecture gate — before the first word

- [ ] **Placed.** Parent, final URL and sibling set decided, per the two hierarchies in
      `site-inventory.md`. The in-body link down from the parent does not exist on either parent page
      today — request it in the handover and note it here rather than assuming it.
- [ ] **Cannibalisation checked** against both inventories — marketing pages
      (`site-inventory.md`) and articles (`published-articles-inventory.md`). If the vertical's hub
      article already targets these queries, the decision is a split of intent, not publish-alongside.
- [ ] **Inbound internal links named** — the specific existing pages that will link here, including
      the parent's link down.
- [ ] **Baseline captured** in Search Console if the URL already exists — impressions, position,
      clicks. Every rewrite of `/for-bmi-verification/` or a Mobile Tailor vertical page is this case.

**Why first:** a page that duplicates an existing one costs the whole writing cycle and drags down the
page it duplicates. Rewriting after publication is more expensive than deciding before.

---

## G-T · Technical gate — before publish

- [ ] Indexable, in the sitemap, canonical to self
- [ ] Schema validates: Service or Product with `audience` + `areaServed`, FAQPage, BreadcrumbList
- [ ] Yoast title ≤ 60 characters, description ≤ 155, both different from the parent's and the hub
      article's
- [ ] Performance and accessibility within threshold; checked at 375 / 768 / 1280 / 1440
- [ ] One primary conversion action; analytics events verified firing manually, not assumed
- [ ] Every `[marker]` replaced; alt text everywhere
- [ ] `fact-sheet.md` written — the sources behind every number, and everything the judge cannot see

---

## G-J · Blind judge — after G-T, before publish

Scored by a **fresh subagent that did not build the page**. The builder never marks its own work up:
after two hours inside a page every compromise has a reason attached, and reasons are exactly what a
scorecard is supposed to ignore.

Not `mvb-core:quality-controller` — that agent scores pipeline artifacts on the 20-point rubric with
full project context. Different job, and not blind. Run `/qc` afterwards if the pipeline wants the
artifact tracked; it does not replace this gate.

### What the judge receives

- The page draft in full
- The page type and the Kit's slot list
- The scorecard below
- `fact-sheet.md`: final URL, canonical target, schema types present, measured performance, viewports
  checked, contrast results, whether analytics events were verified manually, and **the source behind
  every number and client name on the page**. Anything unverified is labelled unverified.

### What the judge must NOT receive

- The intake answers and the reasoning behind them
- The gate justifications, including any G-I waiver
- Which slots were dropped and why — the dropped-slot excuse is how a self-scorer launders a gap into
  a decision
- Any opinion from the builder about how the page turned out

### What the judge returns

JSON only, no prose:

```json
{
  "scores": {"<axis>": 0},
  "total": 0,
  "hard_fails": [],
  "lowest": "<axis>",
  "one_fix": "<one concrete edit>"
}
```

Grade harshly. Partial credit per axis, with the lost points attributable.

### Hard fails — any one fails the gate regardless of total

- [ ] A figure on the page that `fact-sheet.md` cannot trace to `proof-points.md`, a case-study file,
      or the live `/pricing/` page
- [ ] A client name, logo or client metric without publication rights — any Mobile Tailor customer ARR
      is automatically this
- [ ] "independent", "validated", "third-party" or "clinically validated" without a named external
      party and a citable output (guardrail #3)
- [ ] Medical framing other than "not positioned as a medical device", or a claim that a regulatory
      framework "does not apply" (guardrail #6)
- [ ] A bare headline percentage with no methodology and no "available under NDA" (guardrail #4)
- [ ] Leading with "most accurate", "best-in-class" or equivalent — anti-positioning violation
- [ ] Negative parallelism ("not just X — it's Y") or a rule-of-three punch triad anywhere in the copy
- [ ] A CLAUDE.md §6 banned word: leverage, utilize, harness, robust, seamless, comprehensive,
      revolutionize, cutting-edge, game-changer, disrupt, delve, tapestry, realm
- [ ] More than one primary conversion action
- [ ] Zero or more than one `<h1>`
- [ ] A `[placeholder]` marker left in the page
- [ ] Contrast or keyboard operation failing
- [ ] Fewer than two case studies from this vertical on a vertical page

### The loop

**Gate = `total ≥ 85` AND `hard_fails` empty.**

Not taken → fix every hard fail first, then apply `one_fix` to the `lowest` axis, then rescore with a
**new** subagent. Never re-ask the same judge: a judge shown its own suggestion applied grades the
suggestion, not the page.

Stop after three rounds. Still short → hand over flagged "gate not taken — X/85, weakest axis =
`<axis>`" and let Vadim decide. Publishing below 85 without saying so is forbidden.

---

## Scorecard — vertical page

Threshold **85 / 100**. Below it, return to the axis that lost points. Do not average a failure away.

| Axis | Weight | What is checked |
|---|---|---|
| Proof of belonging to the vertical | 20 | context facts, regulators, 2+ vertical cases, integration and formats, quote |
| Claims discipline | 15 | every figure traced and identical everywhere, accuracy scoped with the four conditions, reserved words absent, medical framing correct, M1 acronyms, M2 negation |
| Uniqueness against the parent | 15 | 60% rule, different Yoast title and description, no cannibalisation of the hub article |
| Conversion | 15 | one action, soft alternative, short form, price signal, events working |
| Copy in the buyer's language | 10 | vertical vocabulary, verbatim pains, the segment's "what NOT to say" honoured |
| Human copy | 10 | no AI tells, varied rhythm, an opinion and a boundary present |
| Search and AI visibility | 10 | vertical queries, FAQ + FAQPage schema, quotable structured blocks |
| Place in the site | 5 | link up, two siblings, hub article, breadcrumbs, canonical |
| Design and technical layer | 5 | `DESIGN.md` tokens, mobile, performance, indexation |

Technical and placement carry only 5 each because G-T and G-A already block on them. Scoring them
heavily here would count the same check twice and let a page buy its way to 85 on plumbing.

**Why claims discipline carries 15:** it is the axis that ends deals. A diligence reader who finds two
different versions of the same number stops reading the page and starts doubting the product.

## Scoring the Human copy axis

Full rubric and the tell list are in `copy-humanisation.md`. Score it after running `brand-assets/style-guides/scripts/detect-ai-tells.py --channel page`: any `hard_fails` entry caps this axis at 5, and an unanswered "what still reads as machine-written?" self-check caps it at 8 no matter how clean the detector output is.

| Points | State |
|---|---|
| 9–10 | No banned tells. Rhythm varies. Specifics, an opinion and a stated boundary all present. |
| 6–8 | One or two isolated tells, or clean but flat — no opinion, uniform rhythm. |
| 3–5 | Tells recur across sections, or the page reads as a filled template. |
| 0–2 | Negative parallelism or punch triads present, brochure adjectives throughout. Hard fail. |

## How to score honestly

- **Blind, always.** A score produced by the builder is not a measurement.
- **Score before the fixes, not after.** The first number tells you where the process is weak across
  many pages.
- **Track the losing axis across pages.** If "proof of belonging" keeps losing points, the problem is
  not the writer — it is that nobody is collecting vertical case studies. If "human copy" keeps
  losing them, the drafting prompt is doing the damage upstream. That pattern is what
  `/improve-agents` is for.

---

## Post-launch review — 30 and 90 days

Against the baseline captured at G-A.

| Signal | What it means | Action |
|---|---|---|
| Impressions growing, position flat | Found but not chosen | Yoast title and description rewrite |
| Position growing, no demo requests | Traffic arrives, the offer does not land | Conversion and copy pass |
| Nothing at 90 days | Wrong place in the site, or no demand | Review placement, consider merging into the product page |
| The parent or the hub article dropped after this page launched | The new page is a duplicate | Fold it back into a section |

The last row is why uniqueness carries 15 points, and it is the specific risk on this site, where a
vertical page and its hub article can end up chasing the same query.
