# 3DLOOK — General Approach & Language Guardrails for Corporate Content

> **Source of truth:** Google Doc *"General Approach & Language Guardrails for Corporate Content — 3DLOOK"*
> (internal title: *Terminology & Language Guardrails*), owner **Asselya** (`asselya@3dlook.me`).
> Doc ID `1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214` ·
> [open](https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit) ·
> doc last modified **after 2026-08-13** (the export exposes no date; the change was first seen on
> 2026-09-14) · synced into the repo **2026-09-14** · previous sync 2026-08-25, against the
> 2026-08-13 version.
>
> **Raw export:** `terminology-guardrails.source.txt` next to this file is the Doc's plain-text
> export (`/export?format=txt`), byte for byte, as of the last sync. It is not a guard and no agent
> reads it. The weekly sync diffs a fresh export against it, so a change in the Doc shows up as a
> diff instead of being re-derived from this translation.
>
> **Scope:** ALL 3DLOOK corporate content. SEO and blog articles, website pages, social posts,
> outbound messages, whitepapers, decks, one-pagers. There is no channel exemption.
>
> **Precedence:** this file is the source of truth for **word-level choice and sentence construction**.
> `about-me.md` still governs voice and claims discipline; `editorial-guardrails.md` still governs
> whether a claim may be made at all; `brand-assets/product-info/` is still the only source of facts
> and numbers. Where this file and an older project rule disagree on *wording*, this file wins — see
> **Overrides** below, which records every case where that has happened, with dates.
>
> Re-sync when the Doc changes. Keep the row order and the wording of the "Reason" columns close to
> the Doc so a diff against it stays readable.

---

## Overrides of earlier project rules

The Doc is newer than every rule below and is owned by the editorial owner. Editorial judgment
defers to Asselya (editorial guardrail #11), so the Doc wins. Each override is recorded here rather
than silently deleted, because published content was written under the old rule.

| Earlier rule | Status | New rule |
|---|---|---|
| `editorial-guardrails.md` **M1** (2026-07-07): expand *every* abbreviation at first use, *including* BMI | **Amended 2026-08-25** | BMI, CEO, UK, US, EU now count as commonly known and are **not** expanded. M1 stands for everything else, including the cited regulators (FDA, ICH, GCP). |
| `editorial-guardrails.md` **#6** (2026-06-09): medical framing is *"not positioned as a medical device"* | **Superseded 2026-08-13, restored 2026-09-02, superseded again 2026-09-11, confirmed by the Doc 2026-09-14** | The medical-device boundary sentence is **"FitXpress is not a medical device."** — see the notes directly below. "Positioned as" is banned by §2.10 for every product, intended-use and regulatory statement, the medical-device sentence included. |
| `about-me.md` **"Buyer framing"** (2026-07-06): *prefer "enterprise teams," "buyers," "insurers," "programs," "care teams"* | **Amended 2026-09-14** | §2.12: **buyer** only when the sentence is about procurement, buying criteria or vendor evaluation; **customer** only for an established contract, deployment responsibility or legal role. Otherwise name the actor. |
| `proof-points.md` and `overview.md` IEEE rows: *"Winner, Retail Digital Transformation Grand Challenge"*, *"Member of Mobile Body Scanning Standards"* | **Corrected 2026-09-14** | §2.11: IEEE appears only in the Doc's two approved sentences, verbatim. |

Articles already published with `Body Mass Index (BMI)` on first use or with *"not positioned as a
medical device"* are historical and are not retro-edited. New drafts follow the rules above. If a
refresh touches such a sentence, bring it into line. The same applies to published pages carrying
the old IEEE wording (the Feb 2021 news post
`3dlook-is-a-member-of-the-mobile-body-scanning-standards-developed-by-ieee/`) or "80+ body metrics":
they are flagged, not rewritten from here, and the decision on a live page is Vadim's.

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

> **Reversed again, 2026-09-11 — the direct form, with no exception.** The editor's final of the
> occupational-health intake article writes **"FitXpress is not a medical device."**, and Vadim
> made it the rule everywhere on 2026-09-11. The 2026-09-02 note above is withdrawn:
>
> - **Medical-device boundary:** write **"FitXpress is not a medical device."**
> - **"Positioned as"** is banned for the medical-device sentence too. §2.10 applies without a
>   carve-out, which is what this Doc said on 2026-08-13.
> - `detect-ai-tells.py` no longer licenses `not positioned as a medical device`; that sentence is
>   a hard fail like every other product use of "positioned as".
>
> Fourth state of the rule (prescribed 2026-06-09 → banned 2026-08-13 → restored for medical
> device 2026-09-02 → direct form 2026-09-11). Published articles are not retro-edited.

> **Confirmed by the Doc, 2026-09-14.** The Doc's §2.10 now carries the medical-device pair itself:
> Avoid *"FitXpress is not positioned as a medical device."*, Prefer *"FitXpress is not a medical
> device."* The project rule of 2026-09-11 and its source agree, so the conflict recorded in the
> 2026-09-02 note is closed. Nothing changes in the detector.

---

# Part 1 — General approaches

Ten construction rules. These are about how a sentence is built, not which word is banned.

### 1. Abbreviations

Give the full version first, then the abbreviation in brackets, at the **first** mention in the text:
*dual-energy X-ray absorptiometry (DXA)*, *glucagon-like peptide-1 (GLP-1)*, *Food and Drug
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

### 10. Internal content-cluster labels *(new in the Doc, synced 2026-09-14)*

Replace internal planning terms with reader-facing language that identifies the **concrete topic,
question, workflow, or decision** the section covers.

**Applies when** terms such as **bridge**, **hub**, **pillar**, **cluster**, or **supporting
content** describe the page's role in the content architecture, not a concept the intended audience
uses. In this repo those labels live in `content-plan.md` and in article plans (hub, cluster, "the
GLP-1 bridge"). They are planning vocabulary and stop at the plan: they do not become H1/H2/H3 text,
meta titles, anchor text or body copy.

**Licensed exception:** keep the term when it has an established meaning within the relevant
industry, or when it accurately describes a visible website feature (the site's **Content Hub**).

- Avoid: "The GLP-1 bridge: current BMI, historical BMI, and documentation continuity"
- Prefer: "How does prior GLP-1 treatment affect BMI documentation at bariatric intake?"

---

# Part 2 — Word and phrase guardrails

Thirteen entries, in the Doc's order. "Condition" is when the rule is live; "Apply" is the narrow case
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

- **Medical device** (the Doc's own pair since the 2026-09-14 sync; the project rule since 2026-09-11): Avoid "FitXpress is not positioned as a medical device." → Prefer **"FitXpress is not a medical device."** There is no licensed exception; the notes under the header table record the rule's history.
- Avoid: "FitXpress is positioned as a supporting tool for clinician review." → Prefer: **"FitXpress supports clinician review."**
- For intended-use boundaries: **"FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility."**

### 2.11 IEEE — the approved wording only *(new, synced 2026-09-14)*

| | |
|---|---|
| **Condition** | Any mention of IEEE: copy, award and recognition lists, bios, decks, page trust strips |
| **Apply** | Only these two sentences, verbatim: **"Winner, 2019 Retail Digital Transformation Grand Challenge, run by the 3D Retail Coalition with Kalypso and IEEE."** · **"Participant in the IEEE 3D Body Processing working group, which is developing standards for mobile body scanning."** |
| **Avoid** | IEEE-certified · Certified by IEEE · IEEE-recognized · Recognized or acknowledged by IEEE · IEEE-validated · IEEE Grand Challenge · Member of IEEE standards · IEEE-backed accuracy, ISO compliance or clinical-grade performance · standalone IEEE logos in award, certification, validation or recognition strips |
| **Reason** | IEEE has raised an issue with the incorrect claims 3DLOOK was making |
| **Use instead** | The two approved sentences. They are also the IEEE rows of `brand-assets/product-info/proof-points.md`. |

- Read "IEEE-backed accuracy, ISO compliance or clinical-grade performance" as any claim that IEEE
  backs our accuracy, our ISO compliance or a clinical-grade performance level, in either word order
  ("accuracy validated by IEEE" is the same claim).
- "IEEE Grand Challenge" and "IEEE Retail Digital Transformation Grand Challenge" credit the
  challenge to IEEE alone. The approved sentence names the 3D Retail Coalition as the organiser.
- The logo ban is visual, so no detector can see it. It belongs to `page-builder`'s judge and to
  whoever briefs a deck or a one-pager.

### 2.12 "Buyer" / "customer" — name the actor *(new, synced 2026-09-14)*

| | |
|---|---|
| **Condition** | All corporate content |
| **Apply** | **buyer** only when discussing procurement, buying criteria, or vendor evaluation. **customer** when referring to an established contractual relationship, deployment responsibility, or legal role. |
| **Avoid** | When either term merely labels the intended audience, assumes an existing commercial relationship, or replaces the specific organization responsible for an action |
| **Reason** | These terms can expose the marketing framework instead of describing the operational reality. "Customer" can also imply that the organization has already selected 3DLOOK. |
| **Use instead** | Name the actual actor or context: **organization, program, provider, clinic, employer, operator, procurement team, decision-maker, person being screened** |

- The canonical GDPR sentence (CLAUDE.md §12) stays valid, because "customer" there names a legal
  role: *"In most enterprise deployments, the customer acts as controller and 3DLOOK acts as
  processor under GDPR."*
- "Buyer's guide" as an article type and "buying criteria" sections are procurement contexts, so
  "buyer" is allowed there.

### 2.13 "Body metrics" / "body measurements" — use the precise category *(new, synced 2026-09-14)*

| | |
|---|---|
| **Condition** | Whenever describing numerical body-related data or FitXpress outputs |
| **Apply** | **body metrics** as the umbrella category for numerical body-related outputs. **body measurements** specifically for anthropometric dimensions, such as circumferences, lengths, and widths. BMI, basal metabolic rate, and body composition estimates are **metrics** or **calculated / estimated outputs**. |
| **Avoid** | Using "body metrics" and "body measurements" interchangeably; describing BMI, body composition, or basal metabolic rate as body measurements; replacing the approved **"80+ body measurements"** claim with "80+ body metrics" |
| **Reason** | The terms represent different levels of classification. Conflating them obscures which outputs are anthropometric dimensions and which are calculated or estimated values. |
| **Use instead** | The precise category: **body measurements**, **calculated metrics**, **body composition estimates**, or the umbrella **body metrics** when referring to multiple output types |

- A shape that already passed review (Review 2 on the occupational-health intake article,
  2026-09-11): *"80+ body measurements and calculated metrics such as BMI"*.
- **Open item for Vadim and Asselya, not a rule change:** the canonical accuracy sentence in
  `brand-assets/product-info/accuracy-formulations.md` reads *"approximately 96-97% across body
  metrics, with a typical absolute error of 1.5-2.0 cm per measurement"*. An error in centimetres
  describes body measurements, so under §2.13 "across body metrics" is arguably the wrong category.
  That sentence is verbatim from the live framework article and is not changed from here.

---

# Part 3 — Quick grep table

For the mechanical pass. The detector
(`brand-assets/style-guides/scripts/detect-ai-tells.py`) covers every row marked **auto**; rows
marked **soft** are reported by the detector as soft markers for the editor to judge.

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
| "positioned as" a product or regulatory boundary, **the medical-device sentence included** | state the boundary directly; for medical device use "FitXpress is not a medical device." | auto |
| "what trips people up", "the mistake buyers make", "what most teams misunderstand" | name the components of the issue | auto |
| "do the heavy lifting" and other attributed behaviour | "matter", "apply", plain verbs | auto |
| "IEEE-certified / -recognized / -validated / -backed", "certified / recognized / validated by IEEE", "IEEE Grand Challenge", "member of IEEE standards" | the two approved sentences in §2.11, verbatim | auto |
| standalone IEEE logo in an award, certification, validation or recognition strip | remove the logo; the approved sentence carries the fact | judgment |
| "80+ body metrics"; BMI, BMR or body composition listed as body measurements | "80+ body measurements"; calculated metrics; body composition estimates | auto |
| "body metrics" and "body measurements" swapped anywhere else | the precise category (§2.13) | judgment |
| "buyer" / "customer" as an audience label or an assumed relationship | name the actor: organization, program, provider, clinic, employer, operator, procurement team, decision-maker, person being screened | judgment |
| "bridge", "hub", "pillar", "cluster", "supporting content" as a page-role label in a heading, anchor or sentence | the concrete topic, question, workflow or decision; "Content Hub" as the visible site section stays | soft |
| corrective negation "X, not Y" | lead with the recommended approach | judgment |
| corrective "rather than" | state the characteristic, then the limitation separately | judgment |
| "Body Mass Index (BMI)" | "BMI" — commonly known, do not expand | judgment |
| unexpanded first-use acronym (DXA, GLP-1, FDA, ICH, GCP, CRO, EDC, eCOA) | expand once, then use the short form | judgment |
| `DEXA` in our own prose | **`DXA`** (Vadim, 2026-09-02). `DEXA` stays legitimate only where it is a search term or a published slug, written as `DXA (also written DEXA)` | auto |
| bare URL, "click here" | link on the meaningful anchor phrase | judgment |
| vendor blog as a citation | regulator, standards body, journal, trade press | judgment |
| compressed relationship ("records scale to what is compared") | "depends on", "varies by", "is determined by" | judgment |
| "we / our" beyond a claim of ownership | reframe on the workflow or buyer | judgment |
| "you" in a neutral educational block | reframe impersonally | judgment |

---

# Part 4 — Where this is enforced

| Stage | Owner | What runs |
|---|---|---|
| SEO planning | `seo-planner` | Reads this file with the strategy row. H2 titles name the topic or question, never the content-plan label (§1.10) |
| SEO drafting | `seo-writer` | Hard bans only: em dash, banned words, "positioned as", presumed reaction, attributed behaviour, IEEE wording, "80+ body metrics". Judgment rows are the editor's. |
| SEO editing | `seo-editor` | Pass 3c runs the detector; Pass 4 runs Part 1 and Part 2 as a checklist, including the `cluster_labels` soft markers and buyer / customer |
| SEO publish | `seo-publisher` | Terminology line in the final checklist |
| Website pages | `page-builder` | Layer 0 detector, Layer 2 terminology, G-T gate, G-J scorecard (IEEE logo strips are a hard fail at the judge) |
| Social posts | `post-drafter` → `post-brand-checker` → `social-editor` | Self-check at draft, Pass 2b detector per post |
| Outbound | `message-sequencer` | `--channel dm` sweep before the CSV. The soft conversational ask in Message 1/2 is written to the outbound templates; "so" and "plus" are still replaced. |
| Any artefact | `brand-checker` | Check 3b (M1 with the commonly-known exception), 3c (detector), 4b (medical framing stated directly), 4d (IEEE wording, output vocabulary, actor naming, content-plan labels) |

---

## Related references

- `brand-assets/style-guides/editorial-guardrails.md` — the 11 claim-level principles + M1/M2/M3
- `brand-assets/style-guides/ai-tells-sweep.md` — the 27-category AI-tell catalogue; these guardrails are its hard-fail terminology layer
- `brand-assets/style-guides/scripts/detect-ai-tells.py` — mechanical detector
- `brand-assets/product-info/proof-points.md` — the IEEE rows, in the §2.11 wording
- `brand-assets/content-strategy/terminology-guardrails.source.txt` — raw export of the Doc at the last sync, for the next diff
- `brand-assets/style-guides/blog-style-guide.md` — voice and structure for blog content
- `about-me.md` — brand voice and claims discipline
- `CLAUDE.md` §6 — tone of voice, banned words, AI signatures
