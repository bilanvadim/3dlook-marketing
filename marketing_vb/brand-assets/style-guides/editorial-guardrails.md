# Editorial Guardrails for 3DLOOK Materials

> **Append this block (or a link to this file) to the brief of any future 3DLOOK content/agent run** — blog, SEO, outbound, social, whitepaper, demo deck. These encode how the editorial team (Asselya, Whitney, Vadim) reviews 3DLOOK claims at publish time. Applying them up-front in the brief prevents rework.
>
> Established: 2026-06-09, from the FAQ-article review cycle (v2-asselya rewrite + Whitney/Asselya editorial pass).

---

## 1. Claim substantiation — cut what you can't back

If a statement ("this error is fine for X", "best in class", "lower end of the range") is not directly supported by an internal figure or a citable source, remove it or convert it to a qualitative dependency statement. Marketing-confident benefit claims get hedged: prefer **supports** / **may reduce** / **can help** over **faster** / **reduces** / **eliminates**.

## 2. One number, everywhere the same

Every quantitative claim must be byte-identical in all sections (body, question lists, FAQ, disclaimer). If two figures conflict, never average them — keep the single defensible one or replace both with a qualitative statement. Conflicting numbers are the first thing a diligence reader catches.

## 3. "Independent" / "validated" / "third-party" are reserved words

Never use them unless independence is provable with a named external party and a citable output. Default framings: **internal validation**, **benchmark participation**, **dataset enrichment**. State the negatives plainly and consistently: *not peer-reviewed, not third-party validated, not clinically certified*.

## 4. Drop hard headline percentages you can't precisely define

A bare ">95%" invites "of what, measured how, over how many sessions?" Replace with a qualitative claim + one concrete sub-figure + "detailed methodology available under NDA."

## 5. Honest caveats beat clean overclaims

Whenever you describe a control or safeguard, state its limit: controls **reduce** risk, they do not eliminate the need for capture instructions, retake logic, deployment-specific thresholds, etc.

## 6. Medical / regulatory framing: state the boundary directly, never "does not apply"

Use **"It is not positioned as a medical device."** Frame compliance as built on data-privacy frameworks (HIPAA, GDPR, SOC 2 where applicable) instead of medical-device frameworks. Do not assert that a regulatory framework categorically "does not apply."

For intended-use boundaries, the standard sentence is: **"FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility."** Where the boundary needs a supportive half, pair it: *"FitXpress supports clinician review; it is not a diagnostic tool."*

> **Amended 2026-08-25** — the original wording of this principle was *"not positioned as a medical device."* `brand-assets/content-strategy/terminology-guardrails.md` §2.10 (Asselya's Doc, 2026-08-13) bans **"positioned as"** for product, intended-use and regulatory statements: it makes the product's identity depend on external perception, and turns a factual boundary into a marketing choice. Say what the product is and is not. Articles published before this date keep the old sentence and are not retro-edited.

> **Re-amended 2026-09-02 — the 2026-08-25 amendment above is reverted for this sentence only.** Review 1 on the Wellness Platforms hub names *"It is not positioned as a medical device."* as the approved medical-device wording, and Vadim took that call on 2026-09-02. The medical-device boundary goes back to the original wording. The rest of terminology guardrail §2.10 stands: "positioned as" is still banned for intended use, scope, replacement or equivalence, and every other product or regulatory statement. Guardrail **#7** below is therefore unchanged. `detect-ai-tells.py` licenses the medical-device sentence and nothing else. Articles published under either earlier wording are not retro-edited.

## 7. Conditional language for boundaries

> "FitXpress is not equivalent to DXA, BIA, or a calibrated scale **when the workflow, protocol, or regulatory standard requires those methods**."

> **DXA, not DEXA** (Vadim, 2026-09-02). The live framework article still writes DEXA and needs a CMS edit; new copy uses DXA and `article_lint.py` fails the old spelling.

Conditions make the boundary defensible and non-absolute. (Model sentence updated 2026-08-25: it previously read *"should not be positioned as equivalent to…"*, which breaks terminology guardrail §2.10.)

## 8. Diligence register, not insider register

Title question sections as "diligence questions." Remove self-praising or editorializing adjectives ("honest framing", "genuine framing") and punchy aphorisms. Frame scope **constructively**: how should this be used (*a supporting data layer*) rather than a blunt list of what it is not.

## 9. Lead with the right question, with concrete verticals

For accuracy/validation topics, open by reframing "how accurate is it?" to **"accurate enough for which decision?"**, and ground it immediately in real verticals (apparel sizing, uniform allocation, GLP-1 progress, remote screening, underwriting support) plus the four conditions that make accuracy meaningful: **reference method, measurement protocol, population tested, intended workflow**.

## 10. Structure defaults

- Numbered list for the five evaluation dimensions
- Bulleted disclaimer with a purpose-first opening bullet
- Clean Markdown tables (never tab-exported blobs)
- Preserve internal content-hub links on their anchor phrases

## 11. When in doubt, flag — don't decide

Any unresolved trade-off (an asymmetry, a dropped number, a possible contradiction) goes into an **Open items** block for Asselya's review, not a silent edit. Editorial judgment defers to Asselya.

---

## Mechanical writing rules

> Added 2026-07-07 from the Clinical Trials use-case review (Vadim). Lower-level than the 11 principles above, but apply to **all** 3DLOOK content and are enforced in the writing and editing passes. These fix recurring drafting slips, not positioning.

### M1. Expand every abbreviation at first use, except the commonly known ones

Spell out each acronym the first time it appears in the body, then use the short form: *dual-energy X-ray absorptiometry (DXA)*, *glucagon-like peptide-1 (GLP-1)*, *Food and Drug Administration (FDA)*, *International Council for Harmonisation (ICH)*, *Contract Research Organization (CRO)*, *decentralized clinical trial (DCT)*, *Electronic Data Capture (EDC)*, *electronic Clinical Outcome Assessment (eCOA)*, *Quality Assurance (QA)*, *Digital Health Technology (DHT)*, *API / SDK* (spelled out on first use).

**Do not expand the commonly known ones:** AI, WWW, iOS, and **BMI, CEO, UK, US, EU**. Write *BMI*, never *Body Mass Index (BMI)*.

Outside that list, first-use expansion is **universal** — it does not depend on which section the term lands in, and it still applies to regulators or standards cited as authority (FDA, ICH, GCP), which are the ones most often left bare.

A term that appears only inside a cited document's italicized title still needs its own gloss at its first standalone use.

> **Amended 2026-08-25** — M1 originally required expanding *every* acronym and named BMI as the canonical example of a term that feels obvious but must still be expanded. `brand-assets/content-strategy/terminology-guardrails.md` §1 (Asselya's Doc, 2026-08-13) lists BMI, CEO, UK, US and EU as commonly known, so they are now used bare. Everything else in M1 stands.

### M2. Prefer positive scoping over stacked negation

Compliance-heavy copy tends to negate twice in one breath. State a boundary **once, clearly**, and prefer the positive framing where the meaning survives.

Avoid:
- chained negatives — *"It does not replace DXA… **nor does it** independently validate endpoints."*
- interrupted / parenthetical negation — *"the scope FitXpress **is — and is not —** designed for"*
- double-negative idioms — *"**necessary but not sufficient**"*, *"not uncommon"*, *"they **do not, on their own,** make a study compliant"*

Prefer:
- *"Endpoint validation stays with the sponsor; FitXpress standardizes and documents capture."*
- *"FitXpress supports pre-check workflows; eligibility remains the investigator's determination."*

Keep exactly one clear negative statement of scope where a boundary must be stated (per #6, *"It is not positioned as a medical device."*, restored 2026-09-02); do not chain a second negation onto it in the same sentence. (Repeating the scope disclaimer across sections, when each restatement fits its section, is acceptable — this rule is about negation density within a sentence, not about how often the disclaimer appears.)

### M3. Construction rules live in the terminology guardrails

`brand-assets/content-strategy/terminology-guardrails.md` Part 1 adds five construction rules at the same mechanical level as M1/M2, and they apply to all content: write relationships explicitly ("depends on", "varies by"); no presumed audience reaction ("what trips people up"); no behaviour attributed to concepts ("do the heavy lifting"); no corrective negation "X, not Y" outside a real boundary; no corrective "rather than". Part 2 holds the ten word-level bans. Run that file as its own pass, not from memory.

---

## How to apply

| Phase | Application |
|-------|-------------|
| Brief intake | Include this file (or a link to it) in the brief. Don't write a sentence without confirming none of the 11 are broken. |
| Phase 1 fact-check | Run the 11 as an explicit checklist. Flag every #1, #2, #3, #4, #6 risk before approving the brief. |
| Phase 3 writing | Enforce naскрізь — especially #1 (substantiation), #2 (one number everywhere), #3 (reserved words), #4 (no bare percentages without methodology), #6 (medical framing stated directly), and **M1 (expand acronyms except the commonly known ones) / M2 (no stacked negation) / M3 (terminology guardrails as its own pass)**. |
| Phase 4 self-critique | List any place a guardrail was bent. Per #11, surface to Open Items for Asselya, not a silent edit. Run a first-use scan for every acronym (M1), a stacked-negation scan (M2), and the terminology-guardrails pass plus the detector (M3). |
| Phase 5 metrics | Add a "Guardrails audit" subsection — pass/fail for each of the 11 principles + M1/M2/M3. |

## Related references

- `brand-assets/content-strategy/terminology-guardrails.md` — **word-level and sentence-construction rules (Asselya's Doc). Wins on wording; it amends #6 and M1 above.**
- `brand-assets/style-guides/ai-tells-sweep.md` + `scripts/detect-ai-tells.py` — AI-tell catalogue and mechanical detector
- `brand-assets/style-guides/blog-style-guide.md` — lower-level voice/structure spec for blog content
- `CLAUDE.md` §6 — tone of voice & banned phrases
- `CLAUDE.md` §15 — blog authoring standards
- `docs/quality-rubric.md` — QC rubric (if/when populated)
