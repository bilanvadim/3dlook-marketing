# 3DLOOK — General Approach & Language Guardrails for Corporate Content

> **Source of truth:** Google Doc *"General Approach & Language Guardrails for Corporate Content — 3DLOOK"*
> (internal title: *Terminology & Language Guardrails*), owner **Asselya** (`asselya@3dlook.me`).
> Doc ID `1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214` ·
> [open](https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit) ·
> doc last modified **2026-08-13** · synced into the repo **2026-08-25**.
>
> **Scope:** ALL 3DLOOK corporate content. SEO and blog articles, website pages, social posts,
> outbound messages, whitepapers, decks, one-pagers. There is no channel exemption.
>
> **Precedence:** this file is the source of truth for **word-level choice and sentence construction**.
> `about-me.md` still governs voice and claims discipline; `editorial-guardrails.md` still governs
> whether a claim may be made at all; `brand-assets/product-info/` is still the only source of facts
> and numbers. Where this file and an older project rule disagree on *wording*, this file wins — see
> **Overrides** below, which records the two cases where that has happened, with dates.
>
> Re-sync when the Doc changes. Keep the row order and the wording of the "Reason" columns close to
> the Doc so a diff against it stays readable.

---

## Overrides of earlier project rules

The Doc (2026-08-13) is newer than both rules below and is owned by the editorial owner. Editorial
judgment defers to Asselya (editorial guardrail #11), so the Doc wins. Both are recorded here rather
than silently deleted, because published articles were written under the old rule.

| Earlier rule | Status | New rule |
|---|---|---|
| `editorial-guardrails.md` **M1** (2026-07-07): expand *every* abbreviation at first use, *including* BMI | **Amended** | BMI, CEO, UK, US, EU now count as commonly known and are **not** expanded. M1 stands for everything else, including the cited regulators (FDA, ICH, GCP). |
| `editorial-guardrails.md` **#6** (2026-06-09): medical framing is *"not positioned as a medical device"* | **Superseded 2026-08-13, then restored 2026-09-02** | The medical-device boundary sentence is **"It is not positioned as a medical device."** again — see the note directly below. Every *other* product, intended-use and regulatory use of "positioned as" stays banned by §2.10. |

Articles already published with `Body Mass Index (BMI)` on first use or with *"not positioned as a
medical device"* are historical and are not retro-edited. New drafts follow the rules above. If a
refresh touches such a sentence, bring it into line.

> **Partial re-reversal, 2026-09-02 — medical-device wording only.** Review 1 on the Wellness
> Platforms hub (Google Doc, tab "Review 1") names **"It is not positioned as a medical device."**
> as the approved medical-device wording and asks for the direct form to be replaced. Vadim took
> that call on 2026-09-02. So:
>
> - **Medical-device boundary:** use **"It is not positioned as a medical device."** The direct
>   form *"FitXpress is not a medical device."* stays acceptable in already-published articles and
>   is not a fail; new drafts use the reviewer's wording.
> - **Everything else in §2.10 is unchanged.** "Positioned as" remains banned for intended use,
>   scope, replacement/equivalence, and every other product or regulatory statement.
> - `detect-ai-tells.py` was narrowed to match: the `positioned_as` hard category now licenses
>   `not positioned as a medical device` and nothing else.
>
> This is the third state of this rule (#6 2026-06-09 → superseded 2026-08-13 → partially restored
> 2026-09-02). If the editorial owner disagrees, this is the row to argue about, because Review 1
> and terminology guardrail §2.10 came from the same authority and point opposite ways.

---

# Part 1 — General approaches

Nine construction rules. These are about how a sentence is built, not which word is banned.

### 1. Abbreviations

Give the full version first, then the abbreviation in brackets, at the **first** mention in the text:
*dual-energy X-ray absorptiometry (DEXA)*, *glucagon-like peptide-1 (GLP-1)*, *Food and Drug
Administration (FDA)*.

**Exception — commonly known concepts are used bare:** AI, WWW, iOS, and explicitly **BMI, CEO, UK,
US, EU**. Do not write "Body Mass Index (BMI)".

### 2. Internal and third-party linking

Integrate links **directly into the anchor text**, on the phrase that carries the meaning. No bare
URLs, no "click here", no footnote-style dumps. Applies wherever a source citation is needed.

### 3. Third-party source quality

Cite only **high-quality neutral websites**. Aim to avoid vendor blogs, including competitors and
adjacent vendors. Regulators, standards bodies, peer-reviewed journals, national statistics offices
and established trade press are the safe classes.

### 4. Write relationships explicitly

Avoid compressed business or technical phrasing that makes the reader decode the relationship. When
one requirement varies with another factor, say so with **"depends on"**, **"varies by"**, or
**"is determined by"**.

- Avoid: "The historical records the feature needs scale to what is being compared."
- Prefer: "The historical records required depend on the type of comparison."

### 5. No presumed audience reaction

Focus on the concept, not on what the audience is assumed to think or get wrong. Define the issue
directly and name its components. Banned shapes: *"what trips people up"*, *"the mistake buyers
make"*, *"what most teams misunderstand"*, and their variants.

- Avoid: "What trips up most procurement reviews is treating 'who owns the data' as one question, when it is really five."
- Prefer: "'Data ownership' involves several distinct rights: individual privacy rights, customer contractual rights, processing rights, intellectual-property rights, and rights to generated outputs."

### 6. No casual language for a healthcare-enterprise tone

Do not write about concepts by attributing behaviour, feelings, or effort to them.

- Avoid: "Two properties do the heavy lifting across all of these."
- Prefer: "Two properties matter across all of these workflows."

### 7. Em dashes

**Avoid, always.** No exceptions, in any channel. Use a comma, a full stop, or brackets. This is
stricter than a style preference: it is a hard fail at every gate.

### 8. Corrective negation

Avoid **"X, not Y"** constructions where they read as corrective, dismissive, or overly instructive.
Lead with the recommended approach and explain its purpose or benefit.

- Preferred: "This explanation should be included in the patient-facing flow, where patients can access it when needed. A policy document can provide supplementary detail."

**Licensed exception:** negation that communicates a necessary **product, clinical, legal, or
regulatory boundary**. Use it once, cleanly.

- Acceptable: "FitXpress supports clinician review; it is not a diagnostic tool."

### 9. Contrast using "rather than"

Do not use **"rather than"** to frame one format, capability, workflow, or outcome through corrective
contrast with another. State the primary characteristic directly, then put any limitation or
difference in a separate clause or sentence.

**Applies when** the contrast may sound dismissive, may imply the alternative is inherently inferior,
or requires the reader to interpret the intended relationship.

- Avoid: "Results typically arrive as a report rather than a live data feed."
- Prefer: "Results typically arrive as a PDF report or portal export. Live data-feed availability depends on the provider and integration."

**Licensed exception:** a necessary clinical, legal, regulatory, or product boundary, or a genuine
user choice that cannot be stated as clearly without the contrast.

---

# Part 2 — Word and phrase guardrails

Ten entries, in the Doc's order. "Condition" is when the rule is live; "Apply" is the narrow case
where the word is allowed.

### 2.1 "Objective" — near-ban

| | |
|---|---|
| **Condition** | In relation to 3DLOOK's technology and product outputs |
| **Apply** | Rarely |
| **Avoid** | Most cases |
| **Reason** | Too strong and subjective |
| **Use instead** | **standardized**, **timestamped**, **structured**, **repeatable** (pick by context) |

### 2.2 "We / our" — judgment call

| | |
|---|---|
| **Condition** | All content |
| **Apply** | When ownership matters: the company is making a clear claim, explaining its own product, or taking responsibility |
| **Avoid** | When the workflow or the buyer's needs should be the focus |
| **Reason** | If overused, the content feels like a company-centered sales deck |
| **Fix** | Reformulate the statement around the workflow or the buyer |

### 2.3 "You" — judgment call

| | |
|---|---|
| **Condition** | All content |
| **Apply** | When speaking to a clear decision-maker or operational owner: landing pages, conversion sections, product onboarding, practical guidance |
| **Avoid** | In neutral educational sections, which should feel authoritative |
| **Reason** | Creates a direct address |
| **Fix** | Reformulate the statement |

### 2.4 "Reader / audience / the following sections / below / …" — banned

| | |
|---|---|
| **Condition** | All content |
| **Apply** | Never |
| **Avoid** | Almost always |
| **Reason** | Reminds people that they are reading marketing content instead of focusing on the actual problem |
| **Fix** | Do not describe the reading experience. Describe the business reality. |

### 2.5 "This article / this guide / our article / our content" — banned

| | |
|---|---|
| **Condition** | All content |
| **Apply** | Only in a scope note, to define the document |
| **Avoid** | Preferably always elsewhere |
| **Reason** | Consumes the strongest part of the page without adding meaning |
| **Fix** | Reformulate the statement |

### 2.6 "By hand" — banned

| | |
|---|---|
| **Condition** | All content |
| **Apply** | Never |
| **Avoid** | Always |
| **Reason** | Too plain |
| **Use instead** | **manually** |

### 2.7 "Plus" — banned as a connector

| | |
|---|---|
| **Condition** | All content, and specifically when connecting product capabilities, outputs, benefits, or proof points |
| **Apply** | Never |
| **Avoid** | Always |
| **Reason** | "Plus" can make capabilities feel like informal add-ons or promotional feature stacking |
| **Use instead** | Structured phrasing that groups related outputs clearly: **"including"**, **"such as"**, **"along with"**, **"as well as"**, or a separate sentence when the list is long |

### 2.8 "Let" — banned

| | |
|---|---|
| **Condition** | All content |
| **Apply** | Never |
| **Avoid** | Always |
| **Reason** | Too plain |
| **Use instead** | **allow** |

### 2.9 "So" — banned as a result connector

| | |
|---|---|
| **Condition** | When "so" introduces a result, consequence, or business benefit in formal B2B content |
| **Apply** | Never |
| **Avoid** | Always |
| **Reason** | "So" can sound conversational and may present the stated benefit as an automatic consequence. More precise alternatives create a more formal tone and allow the outcome to be appropriately qualified. |
| **Use instead** | **reducing…**, **helping to reduce…**, **allowing…**, **which can reduce…**, **thereby reducing…** — select wording that reflects the certainty of the evidence |

### 2.10 "Positioned as" — banned for product and regulatory boundaries

| | |
|---|---|
| **Condition** | When describing 3DLOOK, its products, technology, outputs, intended use, or regulatory status |
| **Apply** | Only when discussing explicit market positioning, messaging strategy, or competitive positioning |
| **Avoid** | When defining what the product is, does, supports, replaces, or is intended to be used for |
| **Reason** | "Positioned as" suggests that the product's identity, intended use, or regulatory status depends on external perception rather than on 3DLOOK's defined product scope and claims. It can also make a factual product boundary sound like a marketing choice. |
| **Fix** | State the product scope or boundary directly |

- **Medical device is now the licensed exception (2026-09-02):** use **"It is not positioned as a medical device."** See the re-reversal note in the header table.
- Avoid: "FitXpress is positioned as a supporting tool for clinician review." → Prefer: **"FitXpress supports clinician review."**
- For intended-use boundaries: **"FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility."**

---

# Part 3 — Quick grep table

For the mechanical pass. The detector
(`brand-assets/style-guides/scripts/detect-ai-tells.py`) covers every row marked **auto**.

| Banned | Use instead | Auto |
|---|---|---|
| em dash (— –) | comma, full stop, brackets | auto |
| "objective" about our own output | standardized, timestamped, structured, repeatable | auto |
| "the reader", "the audience" | describe the business reality | auto |
| "the following sections", "see below" | restructure or cut | auto |
| "this article", "this guide", "our content" | cut, or confine to a scope note | auto |
| "by hand" | manually | auto |
| "plus" stacking capabilities | including, such as, along with, as well as | auto |
| "let" | allow | auto |
| "so" introducing a benefit | reducing…, helping to reduce…, which can reduce… | auto |
| "positioned as" a product or regulatory boundary, **except the medical-device sentence** | state the boundary directly; for medical device use "It is not positioned as a medical device." | auto |
| "what trips people up", "the mistake buyers make", "what most teams misunderstand" | name the components of the issue | auto |
| "do the heavy lifting" and other attributed behaviour | "matter", "apply", plain verbs | auto |
| corrective negation "X, not Y" | lead with the recommended approach | judgment |
| corrective "rather than" | state the characteristic, then the limitation separately | judgment |
| "Body Mass Index (BMI)" | "BMI" — commonly known, do not expand | judgment |
| unexpanded first-use acronym (DEXA, GLP-1, FDA, ICH, GCP, CRO, EDC, eCOA) | expand once, then use the short form | judgment |
| bare URL, "click here" | link on the meaningful anchor phrase | judgment |
| vendor blog as a citation | regulator, standards body, journal, trade press | judgment |
| compressed relationship ("records scale to what is compared") | "depends on", "varies by", "is determined by" | judgment |
| "we / our" beyond a claim of ownership | reframe on the workflow or buyer | judgment |
| "you" in a neutral educational block | reframe impersonally | judgment |

---

# Part 4 — Where this is enforced

| Stage | Owner | What runs |
|---|---|---|
| SEO planning | `seo-planner` | Reads this file with the strategy row; no wording work yet |
| SEO drafting | `seo-writer` | Hard bans only: em dash, banned words, "positioned as", presumed reaction, attributed behaviour. Judgment rows are the editor's. |
| SEO editing | `seo-editor` | Pass 3c runs the detector; Pass 4 runs Part 1 and Part 2 as a checklist |
| SEO publish | `seo-publisher` | Terminology line in the final checklist |
| Website pages | `page-builder` | Layer 0 detector, Layer 2 terminology, G-T gate, G-J scorecard |
| Social posts | `post-drafter` → `post-brand-checker` → `social-editor` | Self-check at draft, Pass 2b detector per post |
| Outbound | `message-sequencer` | `--channel dm` sweep before the CSV. The soft conversational ask in Message 1/2 is written to the outbound templates; "so" and "plus" are still replaced. |
| Any artefact | `brand-checker` | Check 3b (M1 with the commonly-known exception), 3c (detector), 4b (medical framing stated directly) |

---

## Related references

- `brand-assets/style-guides/editorial-guardrails.md` — the 11 claim-level principles + M1/M2
- `brand-assets/style-guides/ai-tells-sweep.md` — the 27-category AI-tell catalogue; these guardrails are its hard-fail terminology layer
- `brand-assets/style-guides/scripts/detect-ai-tells.py` — mechanical detector
- `brand-assets/style-guides/blog-style-guide.md` — voice and structure for blog content
- `about-me.md` — brand voice and claims discipline
- `CLAUDE.md` §6 — tone of voice, banned words, AI signatures
