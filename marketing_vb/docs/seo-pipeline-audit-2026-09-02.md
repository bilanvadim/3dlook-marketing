# SEO article pipeline: what it costs, where the quality leaks, what to change

**Measured 2026-09-02** against one real run: revision 2 of the Wellness Platforms hub
(`2026-08-31-ai-body-data-wellness-platforms-hub`), driven by a 20-item external review.
Numbers come from `scripts/pack-cost.py`, which dedupes by message id and prices cache classes
separately, so they are list-price actuals and not estimates.

> **Status, 2026-09-02: items 1 to 7 are implemented. Item 8 was rejected by Vadim on quality
> grounds and is not done.** Regression suite: `scripts/test-pipeline-changes.sh`, 42 checks,
> all passing. What shipped:
>
> | # | Change | Where |
> |---|---|---|
> | 1 | `Bash` added to `seo-writer`; it now runs the gate instead of simulating it | 3 prompt copies |
> | 2 | External review moves to checkpoint 1, with a recovery order if it arrives late | `new-article.md`, `orchestrator.md` |
> | 3 | Nine mechanical gates in one call, including the claim audit | `scripts/article_lint.py` |
> | 4 | Hard-bans card generated from the detector's own patterns | `scripts/bans-card.py`, `hard-bans-card.md` |
> | 5 | Plan split into `plan.md` (writer) and `plan-audit.md` (publisher) | `seo-planner`, and the read rules in the other three |
> | 6 | `--report` gives the coordinator every descriptive number in one call | `scripts/article_lint.py` |
> | 7 | DEV is the source; the two derived copies are generated | `scripts/sync-agent-copies.py` |
>
> **Section 4a now carries measured-after numbers** for the two stages that ran again on
> revision 3. The per-stage estimates below held up in direction and roughly in magnitude.
> The MAIN estimate did not, and section 4a explains why: session length, not file reading,
> is what drives it.

---

## 1. What one revision actually cost

```
stage                    runs  reqs     cacheW       cacheR   output          ctx        $
MAIN session                1    88    218,408   14,788,967   95,288   15,007,551    33.43
seo-planner                 1    21    224,410    2,700,471  160,314    2,924,923    20.28
seo-writer                  1    34    188,262    4,802,899  110,755    4,991,229    19.04
seo-editor                  1    40    139,787    3,995,782   49,622    4,135,649    12.34
seo-publisher               1    33    152,875    3,238,651   44,855    3,391,592     2.22

TOTAL 30,911,778 tokens · ~$87.31
```

Three things this table says immediately:

- **MAIN is 48% of tokens and 38% of cost.** The coordinator, not the writers, is the biggest
  single line. The social pipeline hit the same wall in August (MAIN was 59% of a 42.8M pack).
- **Cost does not track token count.** `seo-publisher` moved 3.4M tokens for $2.22;
  `seo-editor` moved 4.1M for $12.34. The publisher runs on Sonnet. That is a 5.5x per-token
  difference on the same pipeline.
- **On Opus stages, output dominates.** The planner's 160,314 output tokens are ~$12 of its
  $20.28. It cost more to *write* the plan than to read everything it read.

Cost scales as `context size × request count`, and both compound. Every fix below attacks one
or the other.

---

## 2. Findings, ranked by value

### F1. `seo-writer` cannot run the linter its own prompt tells it to satisfy

**Severity: bug. Fix: one line.**

`seo-writer.md` declares `tools: Read, Write, WebSearch, WebFetch, Grep`. No Bash. But its
prompt says *"Проверь себя grep-ом, а не памятью"* and the whole pipeline gates on
`detect-ai-tells.py`.

So on 2026-09-02 the writer did the only thing it could: it read the detector's **40,702 B
(~11,300 tokens) of Python source** and hand-simulated every `HARD_EN` category with roughly
thirty ripgrep calls. It reported this honestly and refused to fabricate a verdict, which is
the right behaviour, but the work was waste, and a simulation of a regex engine is strictly
less reliable than the engine.

- **Fix:** add `Bash` to `seo-writer`'s tools line. `seo-editor` already has it.
- **Estimated saving:** ~11K tokens of source reading plus ~30 tool calls per run. At the
  writer's observed ~147K average context per request, 30 fewer round-trips is roughly
  **4.4M tokens, ~$8**, and it is the cheapest fix in this document.
- **Quality gain:** the writer's self-check becomes authoritative instead of approximate.

### F2. `plan.md` is the pipeline's cost multiplier

**Severity: structural. Fix: split the file by audience.**

| | v1 | revision 2 |
|---|---|---|
| `plan.md` | 37,931 B | **69,900 B (~19,400 tokens)** |

It is read by `seo-writer`, `seo-editor` and `seo-publisher`, and re-read by `seo-planner`.
Four reads of a 19.4K-token file is ~78K tokens of input, and writing it is most of the
planner's $12 output bill.

It is large because it serves three audiences in one file:

1. the writer's per-section brief (goal, must-cover, word budget, claims, keywords)
2. reviewer-facing audit tables (review coverage map, deletions ledger, open items)
3. the publisher's checklist source

Only audience 1 is needed to write the article.

- **Fix:** `plan.md` keeps the writer brief. Move the audit tables to `decisions.md`, read by
  the publisher only. Generate the coverage and closure tables with a script from
  `plan.md` + `final.md` + the review file, instead of having an Opus model retype them.
- **Estimated saving:** ~40-50K tokens of input across stages, plus a large share of the
  planner's output cost. Call it **$8-14**, mostly output.
- **Quality gain:** the writer stops reading 30K B of material about *why* decisions were
  made when it needs to know *what* to write. Less context to lose the brief inside.

### F3. Mechanical style rules are encoded four times and enforced once

**Severity: this is what bit us today. Fix: generate the rule card from the detector.**

Banned words and phrasings currently live in:

| Location | Size | Enforces? |
|---|---|---|
| `brand-assets/style-guides/ai-tells-sweep.md` | 18,166 B | no |
| `brand-assets/content-strategy/terminology-guardrails.md` | 16,345 B | no |
| `brand-assets/style-guides/scripts/detect-ai-tells.py` | 40,702 B | **yes** |
| `CLAUDE.md` §6 | inside 46,302 B | no |
| inline in each of the 4 SEO agent prompts | 2-3 hits each | no |

`seo-writer` and `seo-editor` are each told to read the first two in full: 34,511 B per stage.

**The cost of this duplication is not hypothetical.** When Vadim reverted the "positioned as"
rule on 2026-09-02, the change had to be made in the detector, both guardrail docs, and
**twelve agent-prompt files across three copies**. The agent prompts still said `DEXA`
after the review corrected it to `DXA`, so the writer had to be told to override its own
prompt. Four-way duplication guarantees that a rule change ships partially.

- **Fix:** the detector's pattern tables become the single source of truth for mechanical
  rules. A script emits a compact hard-bans card (~2K B) from those tables. Agents read the
  card; the prose docs stay for humans and for judgment rows no regex can decide.
- **Estimated saving:** ~32K B (~9K tokens) off writer and editor first-read each, so
  **~18K tokens**, plus the request-count reduction from not re-reading them.
- **Quality gain:** larger than the token gain. A rule changes in one place and every agent
  gets it, which removes the failure class we spent an hour on today.

### F4. Script verification outperformed the QC agent, and cost nothing

**Severity: opportunity. Fix: write `scripts/article_lint.py`.**

`orchestrator.md` specifies QC after key artifacts, and the August social baseline spent
**7.1M tokens / $36.35** on `quality-controller`. This run ran no QC agent. Verification was
the detector plus about fifteen targeted greps from the coordinator, and it caught:

- an unsupported `predicted weight` claim the *external reviewer* had asserted (FX-009 does
  not contain it; it appears nowhere in `product-info/`)
- the corporate-versus-broad framing ratio, 64:15, which is the article's main review item
- link-direction coverage, 14 links across 8 targets, all four directions
- **a real measurement bug:** the detector reports 3,055 words for a 2,691-word article,
  because its `\b\w+\b` count includes frontmatter, HTML comments and table pipes. Anyone
  gating on "±10% of target" from the detector's number is judging the wrong quantity.

- **Fix:** put those checks in `scripts/article_lint.py`: the seven grep gates, a real prose
  word count, claim traceability against the context pack, link-direction coverage, keyword
  placement counts. Then run `quality-controller` **only** on what a script cannot judge:
  whether the argument holds, whether a section earns its place.
- **Estimated saving:** most of a $36 stage, based on the social baseline. The remaining
  judgment-only QC pass would be far smaller because it reads a lint report instead of
  re-deriving the mechanics.
- **Quality gain:** the checks become repeatable instead of depending on which greps the
  coordinator thought to run.

### F5. Claim traceability has no adversarial check, and that is the one failure with business risk

**Severity: highest quality risk. Fix: extend `article_lint.py`.**

Every number in the article carries a `<!-- claim: FX-xxx -->` marker, and the publisher
checklist asserts traceability. But nothing *verifies* that the marker's claim actually
supports the sentence. The `predicted weight` error survived a 20-item expert review and was
caught only because someone happened to grep `product-info/`.

- **Fix:** extract every figure and product term from `final.md`, resolve each claim marker
  against `approved_claims` in the context pack, and fail on any unsourced number or any
  marker whose claim text does not contain the asserted value.
- **Quality gain:** unsupported product claims are the pipeline's only failure mode with real
  external consequence. This is the check worth building first on quality grounds alone.

### F6. MAIN is 48% of tokens, and round-trips are why

Eighty-eight requests at ~170K average context. The coordinator's context grows monotonically
and every Bash round-trip re-sends all of it.

- **Fix:** collapse the verification sweep into one `article_lint.py` call instead of ~15
  separate Bash calls. Stop reading agent outputs that the lint report already summarises.
- **Estimated saving:** ~13 fewer requests at ~170K context is **~2.2M tokens, ~$5**.
- **Note:** this is the same lever that took the social pipeline from 42.9M down, and it was
  the largest one there.

### F7. Three prompt copies are a tax on every rule change

`ROOTS` in `check-agent-copies.py` is DEV source, installed plugin, project copy: 3 copies of
29 agents. Today's one-sentence rule change touched 15 files.

`check-agent-copies.py` verifies they match but cannot prevent drift, and per the project's own
notes it was once blind to a *missing* copy.

- **Fix:** make DEV the only editable source and generate the other two, exactly as
  `split-linkedin-prompts.py` already generates the six LinkedIn briefs with a `--check` that
  exits 1 on divergence. The precedent and the pattern are already in this repo.
- **Quality gain:** rule changes stop shipping partially. No token saving; this one is
  correctness.

---

## 3. The process change that dwarfs all of the above

**External review currently arrives at checkpoint 2, after the article is finished.**

`.claude/commands/new-article.md` defines checkpoint 1 as Vadim approving title and outline,
and checkpoint 2 as final text plus meta. Review 1 arrived at checkpoint 2, and its item 2
overturned the **primary keyword**, a checkpoint-1 decision. That invalidated the frame of
every section.

The rewrite cost:

```
seo-planner  $20.28
seo-writer   $19.04
seo-editor   $12.34
seo-publisher $2.22
             ------
             $53.88   plus the coordinator time around it
```

Of the 20 review items, the ones that forced structural work (broaden beyond corporate
wellness (2), cut the employer section (3), rework the opening (4), remove "Why this matters
now" (5), add a value table (6), merge the workflow sections (11), and the whole 12-section
restructure) are **all outline-level judgments**. Every one was decidable from `plan.md`
alone, before a word was written.

**Proposal: route the outline through the external reviewer at checkpoint 1.** Send the
12-section outline with per-section goals, not the finished 3,400-word draft. Item 2 costs
one line to fix in an outline and a full pipeline run to fix in prose.

Five of the twenty items (13, 14, 15, 16, 20) were factual corrections about our own product,
three of which turned out to be **our sources being stale, not the article being wrong**:
DEXA/DXA, essential-versus-beneficial fat, and the 150-205 versus 150-220 height range that
had been sitting open across at least two deliverables. Those are also catchable before
writing, by F5's claim audit run against the sources rather than against the draft.

---

## 4. What to do first

Ordered by value per unit of effort, not by size of saving.

| # | Change | Effort | Est. saving | Main gain |
|---|---|---|---|---|
| 1 | Add `Bash` to `seo-writer` tools | one line | ~$8 | correctness of self-check |
| 2 | Review the **outline** at checkpoint 1, not the finished text | process | up to $54 per avoided rewrite | avoids whole rewrites |
| 3 | `scripts/article_lint.py` with the claim audit (F4 + F5) | ~250 lines | most of a $36 QC stage | catches unsupported claims |
| 4 | Generate the hard-bans card from the detector (F3) | ~80 lines | ~$5 | rule changes stop shipping partially |
| 5 | Split `plan.md` by audience (F2) | prompt edits | ~$8-14 | writer keeps the brief in focus |
| 6 | Collapse coordinator verification into one lint call (F6) | usage habit | ~$5 | shrinks the 48% line |
| 7 | Generate the two derived prompt copies from DEV (F7) | ~120 lines | none | correctness |
| 8 | ~~Try `seo-editor` on Sonnet~~ | **REJECTED by Vadim 2026-09-02** | ~$10 forgone | quality risk not worth it |

**#8 is closed as rejected.** Vadim declined it on 2026-09-02: quality would suffer. That
matches what this run showed anyway. The editor made three genuine judgment calls (where the
accuracy link belongs, whether to force long-tail keywords past a cap, what to cut to pay for
two oversized sections), argued each, and caught a reduction loss nobody had flagged. The
~$10 stays on the table and the editor stays on Opus. Do not reopen this without new evidence
about the editor's output, not about the price gap.

**Do not** cut the checkpoints, and do not merge writer and editor. Both were load-bearing
this run: the writer refused to fabricate a lint verdict, and the editor caught a real
reduction loss (the *reason* to ask about validation population, which had been flattened into
a bare checklist item).

---

## 4a. Measured after, on revision 3

The audit promised the savings were estimates until re-measured. Revision 3 of the same
article, driven by Review 2, is the first run with the tooling in place. Same script, same
session, `scripts/pack-cost.py`.

**The clean comparison is `seo-publisher`, because it did the identical job twice:** rebuild
the publish package for this article.

| Stage | Revision 2 (before) | Revision 3 (after) | Tokens | Cost |
|---|---|---|---|---|
| `seo-publisher`, same job | 3,391,592 tok / $2.22 / 33 reqs | 2,125,036 tok / $1.61 / 30 reqs | **-37%** | **-27%** |
| `seo-editor` | 4,135,649 tok / $12.34 / 40 reqs | 1,514,852 tok / $5.97 / 22 reqs | **-63%** | **-52%** |

The editor's number is the larger drop but the weaker evidence: revision 3 was a wording pass
and revision 2 was a restructure, so part of that -63% is simply less work. The publisher's
-37% is the figure to trust. Both stages also made fewer requests, which is the mechanism:
`article_lint.py` answers in one call what previously took a series of greps, and each saved
round-trip is a saved copy of the whole context.

Direction confirmed, magnitude roughly as estimated. What is NOT yet measured: a full net-new
article through `plan -> write -> edit -> publish` with the split plan and the bans card in
place. Run it and compare against the $53.88 four-stage figure from revision 2.

### The MAIN number went the wrong way, and that is the real finding

| | Requests | Context | Cost | Average context per request |
|---|---|---|---|---|
| Revision 2 window | 88 | 15.0M | $33.43 | 170,540 |
| Whole session, all of the above plus building the tooling | 191 | 51.2M | $118.46 | **268,239** |

**These two are not comparable and the second is not a per-article cost.** The 191-request
session carries the article revision, the guardrail revert, this audit, implementing seven
changes, and 42 tests. Reporting $179.91 as the price of an article would be wrong.

What it does show is the mechanism, and it is the one thing this audit under-weighted:
**average context per request grew 1.57x as the session went on.** MAIN's cost is not driven
by how many files it reads, it is driven by session length, because every request re-sends
everything that came before. Finding F6 said "collapse fifteen greps into one call", which is
right and now possible. The larger lever is next to it:

**Split the session at the natural boundary.** An article revision is one session. Auditing
the pipeline is another. Implementing the audit is a third. Running them in one session
charged the article work for the audit's context and the audit for the article's, on every
single request. That costs more than any prompt or file-reading change in this document, and
it is free to fix.

## 5. Honest limits of this audit

- One run, one article, one revision. A net-new article has no `v1/` to read and no review to
  carry, so its shape differs. The MAIN share in particular may be inflated here by the
  guardrail-revert work and by the measurement queries for this document, which ran in the
  same session and inside the same pack window.
- Savings are arithmetic from observed averages, not measured after a change. Re-measure each
  with `pack-cost.py` before believing any of them.
- `pack-cost.py` files SEO stages as `other:` because its stage matcher was written for the
  social pack. Worth teaching it the SEO openers so this table labels itself next time.
