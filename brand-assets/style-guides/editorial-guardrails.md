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

## 6. Medical / regulatory framing: "not positioned as," never "does not apply"

Use **"FitXpress is not positioned as a medical device."** Frame compliance as built on data-privacy frameworks (HIPAA, GDPR, SOC 2 where applicable) rather than medical-device frameworks — do not assert that a regulatory framework categorically "does not apply."

## 7. Conditional language for boundaries

> "…should not be positioned as equivalent to DEXA/BIA/calibrated scale **when the workflow, protocol, or regulatory standard requires those methods**."

Conditions make the boundary defensible and non-absolute.

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

## How to apply

| Phase | Application |
|-------|-------------|
| Brief intake | Include this file (or a link to it) in the brief. Don't write a sentence without confirming none of the 11 are broken. |
| Phase 1 fact-check | Run the 11 as an explicit checklist. Flag every #1, #2, #3, #4, #6 risk before approving the brief. |
| Phase 3 writing | Enforce naскрізь — especially #1 (substantiation), #2 (one number everywhere), #3 (reserved words), #4 (no bare percentages without methodology), #6 (medical framing). |
| Phase 4 self-critique | List any place a guardrail was bent. Per #11, surface to Open Items for Asselya, not a silent edit. |
| Phase 5 metrics | Add a "Guardrails audit" subsection — pass/fail for each of the 11. |

## Related references

- `brand-assets/style-guides/blog-style-guide.md` — lower-level voice/structure spec for blog content
- `CLAUDE.md` §6 — tone of voice & banned phrases
- `CLAUDE.md` §15 — blog authoring standards
- `docs/quality-rubric.md` — QC rubric (if/when populated)
