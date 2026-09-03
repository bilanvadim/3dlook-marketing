---
article: 2026-08-31-ai-body-data-wellness-platforms-hub
text: final-google-doc.md (revision 6)
target_url: https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/
created: 2026-09-03
status: not started
owner: unassigned
---

# CMS tasks for the Wellness Platforms hub

Three tasks. All need WordPress access, none need a writer. Task 1 is the one that decides
whether the page ranks; tasks 2 and 3 are correctness.

**Order matters: publish the article first.** Every link below points at a URL that does not
exist yet, so doing task 1 before publication just creates five 404s.

---

## Task 1 — Inbound internal-link pass (~40 min, load-bearing)

### Why this is not optional

The hub inherits no external authority. Beyond BMI has 1 backlink; Wellness Rewards has 0 and is
absent from the Ahrefs export entirely. Meanwhile the primary keyword moved to `wellness
platform` at KD 36. A page with zero external links, targeting a KD 36 term, ranks on internal
equity or it does not rank. The Health segment holds 1,005 backlinks and roughly 92% of them sit
in the five pages below.

### What "doing it" means, per page

Open the page in WordPress, find the paragraph described under *where*, and add one contextual
in-body link to the hub. In-body means inside a sentence a reader is already reading, not a
"Related articles" block in the footer — footer link lists pass a fraction of the equity and are
frequently ignored by search engines as boilerplate.

Anchors are drafted below. They are deliberately not all the exact keyword: five pages all
linking with the identical anchor `wellness platform` reads as manipulation. Each one is
descriptive, varied, and reads as a sentence someone wrote on purpose.

| # | Donor page | Backlinks | Where to put the link |
|---|---|---|---|
| 1 | `/content-hub/ai-in-fitness-industry/` | 326 | Where it separates training outcomes from wellbeing and corporate wellness programs |
| 2 | `/content-hub/the-potential-of-ai-in-telehealth/` | 263 | Where it covers remote capture outside clinical care |
| 3 | `/content-hub/glp-1-market/` | 183 | Where it discusses progress tracking beyond weight for non-clinical programs |
| 4 | `/content-hub/top-fitness-industry-trends/` | 36 | The corporate and employee wellness trend mentions |
| 5 | `/content-hub/weight-loss-industry-overview/` | 33 | The employer and insurer wellness program mentions |

### Drafted anchor sentences

Adapt the wording to the surrounding paragraph; keep the link target and the anchor phrase.

1. **ai-in-fitness-industry** — "Programs built around wellbeing and participation rather than
   training load have a different set of requirements, covered in
   [AI body data for wellness platforms](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/)."

2. **the-potential-of-ai-in-telehealth** — "The same remote capture also runs outside clinical
   care, where the goal is member progress rather than patient monitoring:
   [how wellness platforms use body data](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/)."

3. **glp-1-market** — "Tracking change beyond scale weight is not specific to medicated programs.
   [Progress tracking for wellness platforms](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/)
   covers the non-clinical version of the same problem."

4. **top-fitness-industry-trends** — "For the corporate and employee side of this,
   [body data in wellness platforms](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/)
   covers progress tracking, personalization, and engagement."

5. **weight-loss-industry-overview** — "Employer and insurer programs sit next to this,
   and [what a wellness platform needs from body data](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/)
   sets out the requirements."

### Rules that apply to all five

- Canonical URL with the trailing slash, exactly as written above. The Ahrefs export shows
  parameterised and non-slash variants of 3dlook.ai URLs already circulating; do not add more.
- One link per donor page. A second link from the same page adds close to nothing.
- Do not remove existing links to make room.

---

## Task 2 — Architecture re-parenting (~20 min, approved at checkpoint 1)

`wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/` stops being the
Wellness hub and becomes the employer/insurer sub-hub under this page.

1. `brand-assets/content-strategy/published-articles-inventory.md` — three places: the Hub #8 row,
   the Wellness section, and the Internal Linking Map, which currently draws Wellness Rewards as
   the hub node. Repo edit, not CMS.
2. The Wellness Rewards page itself needs one link pointing **up** to the new hub, so the parent
   relationship exists in both directions. The new hub already links down to it.

---

## Task 3 — Illustrations (blocked on design)

Three images, planned and specified with alt text in `illustrations.md` §10. Not produced.
The article carries their positions as `(*cover*)`, `(*Image 1*)` and `(*Image 2*)`; those
markers must be replaced with the real images or removed before publication. Alt text is
published copy and ships with them.

---

## Not a CMS task, but do not lose it

The sentence *"the customer acts as the controller and 3DLOOK acts as the processor under the
General Data Protection Regulation (GDPR)"* in `Privacy and data handling` has no source line
anywhere in `brand-assets/`. Every other privacy claim in that section traces to
`product-info/compliance.md` or `how-it-works.md`; this one is a legal-role assertion that
arrived with the external revision. It needs confirming by whoever owns the DPA wording before
this publishes.
