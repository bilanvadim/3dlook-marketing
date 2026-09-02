---
slug: 2026-08-31-ai-body-data-wellness-platforms-hub
review: 1
decided: 2026-09-02
decided_by: Vadim
purpose: >
  How each Review 1 item is applied, and how the four conflicts between the review and
  brand-assets were resolved. seo-planner / seo-writer / seo-editor MUST read this alongside
  review-1.md. Where this file and review-1.md disagree, THIS FILE WINS.
---

# Review 1 — application decisions

## A. Vadim's two calls (2026-09-02)

### A1. Primary keyword broadens — review item 2 is executed in full

Checkpoint 1 approved `corporate wellness platform` (500/mo, KD 11) as primary. Review item 2 says
corporate wellness must stop being the dominant frame. Vadim's call: **broaden.**

| Role | Keyword | Volume / KD | Where it lives |
|---|---|---|---|
| **Primary** | `wellness platform` | 150 / KD 36 | First paragraph, meta title, one H2 |
| Support | `wellness app` | 1000 / KD 1 | Body prose, naturally, 2-3 times |
| Support | `corporate wellness` | 1000 / KD 3 | The employer/insurer subsection |
| **Secondary (demoted)** | `corporate wellness platform` | 500 / KD 11 | Meta description + the employer/insurer subsection only |

- **H1 does not change.** *AI Body Data for Wellness Platforms: Progress Tracking,
  Personalization, and Engagement* is the content-plan strategy row verbatim and stays.
- **Meta title changes** to carry the broadened head term: target
  `AI Body Data for Wellness Platforms | 3DLOOK` (44 chars; this file said 48 until 2026-09-02, which was my miscount, caught by seo-publisher). The checkpoint-1 note in `plan.md`
  said the H1 deliberately omits the head term and the meta title carries it. That split is now
  void: with `wellness platform` as primary, H1 and meta title both carry it.
- **Audience coverage is now plural and balanced.** Consumer wellness apps, lifestyle-change
  platforms, nutrition and habit-coaching products, digital wellbeing ecosystems, and human-led
  plus automated coaching get equal or greater weight than corporate wellness. Corporate wellness
  is one application in one subsection.
- `corporate wellness platform` keeps a real home so the 500/mo term is not abandoned, but it no
  longer sets the frame.

### A2. "positioned as" — review item 19 is executed, the guardrail is reverted

Review item 19 asks for **"It is not positioned as a medical device."** in place of the direct form.
That phrasing was banned by `terminology-guardrails.md` §2.10 (2026-08-13) and was a hard fail in
`detect-ai-tells.py`. Vadim's call on 2026-09-02: **execute the review, revert the guardrail.**

Three files were changed on 2026-09-02 so the article can pass its own lint gate:

| File | Change |
|---|---|
| `brand-assets/style-guides/scripts/detect-ai-tells.py` | `positioned_as` hard pattern narrowed with a lookahead. `not positioned as a medical device` is licensed; every other product / intended-use / regulatory "positioned as" still hard-fails. Verified against a 6-sentence test set. |
| `brand-assets/content-strategy/terminology-guardrails.md` | Supersession row rewritten, a dated re-reversal note added, §2.10 example and the Part 3 grep row updated. |
| `brand-assets/style-guides/editorial-guardrails.md` | #6 model sentence restored, dated re-amendment note added. #7 untouched. |

**Scope of the revert is exactly one sentence.** "Positioned as" is still banned for intended use,
scope, replacement, equivalence, and every other product or regulatory statement. Do not reintroduce
it anywhere else.

**Flag for the editorial owner:** Review 1 and terminology guardrail §2.10 come from the same
authority and point opposite ways. This is now the third state of the rule
(#6 2026-06-09 → superseded 2026-08-13 → partially restored 2026-09-02). Worth settling in the Doc.

## B. Conflicts between the review and brand-assets — resolved without asking

These three had a safe resolution, so they were not escalated. Each divergence is flagged.

### B1. Item 14, DEXA → DXA. **Applied in the article. Brand-assets diverge.**

DXA is the correct current term and the review states it flatly. Applied: every instance in this
article becomes `dual-energy X-ray absorptiometry (DXA)` on first use, `DXA` thereafter.

**Divergence flagged, not silently fixed:** `DEXA` is still the house spelling in
`terminology-guardrails.md` §1 (abbreviation example list), `editorial-guardrails.md` #7 (the model
boundary sentence), the Part 3 grep row, and ten-plus published articles. Fixing those retro-edits
other articles and changes a rule for all future content, which is the same class of decision as A2
and belongs to Vadim, not to this run. **Until it is taken, the next article regenerates `DEXA`.**
Recommendation: change the abbreviation lists to DXA, leave published articles alone.

### B2. Item 15, training-data paragraph. **Figure RESOLVED 2026-09-02. Detailed paragraph still cut.**

**Vadim's call, 2026-09-02: 150 to 220 cm is the correct figure.** The review was right that the
article's 150-205 cm was wrong. This closes a conflict that had been open since the insurance-page
work, and 150-220 cm has been propagated across every source and artifact in the repo:

| Where | Change |
|---|---|
| `brand-assets/product-info/proof-points.md` | Training-data height row → 150-220 cm. Source attribution changed: the figure is now credited to Vadim's 2026-09-02 confirmation, **not** to the Apr 2025 deck, which is where 150-205 cm came from |
| `brand-assets/product-info/how-it-works.md`, `faq.md` | → 150-220 cm |
| `workspace/seo/_context-packs/…wellness-platforms-hub.yaml` | **claim FX-011** → 150-220 cm |
| `workspace/pages/for-insurance-underwriting/` | `page.md` (x2), `fact-sheet.md`, `open-items.md` item 4 and `TODO.md` item 6 closed as resolved |
| `workspace/playbooks/` | `fitxpress-marketing-playbook-nika.md` (x2), `build_nika_deck.py` (x2, including the deck's own open-item slide) |
| `workspace/outbound/campaigns/2026-07-16-au-telehealth/` | `messaging-brief.md` and 7 generator scripts, so a re-run cannot emit the old figure |
| `about-me.md`, `workspace/seo/telehealth-hub-refresh/draft-v1.md` | Already carried 150-220 cm. No change |

**Labelling question also closed by Vadim, 2026-09-02: one figure for both.** `proof-points.md` had
filed 150-205 cm under *training data* demographic coverage while `about-me.md` filed 150-220 cm under
*internal validation population*. Vadim's ruling is that 150 to 220 cm covers both. There is no second
dataset and no second number, so nothing is lost by unifying.

**No CMS edit needed. The repo was the side that had drifted.** I first flagged the live accuracy
article as publishing the stale figure. That was wrong, and Vadim caught it. The live page
(<https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/>, fetched 2026-09-02) already states
150-220 cm in three places:

> The internal validation population included participants aged 16-78, heights of 150-220 cm, weights
> of 38-210 kg, and participants from the US and Europe.

What was stale was **our local copy of that article**, in
`workspace/seo/articles/2026-05-29-3dlook-accuracy-enterprise-evaluation/v2-asselya/`, which no longer
matched what shipped. Corrected there on 2026-09-02 in `final.md`, `draft-final.md` and
`phase-4-self-critique.md`, with a provenance note at `NOTE-height-range-2026-09-02.md`. The two
inbound `.txt` documents in that directory keep 150-205 cm deliberately: they are the record of what
was received for review, no agent cites them, and editing them would falsify that record.

So this hub and the accuracy page it links to now agree in public, and both agree with
`proof-points.md`.

**The detailed training-data paragraph is still cut**, on the review's other ground: item 15 also says
"the detailed training-data paragraph is not essential to this hub", and the cut serves the
2,650-word target. What goes is the enumeration (9+ years, 150,000 photographs, 30,000 3D scans,
430,000 measurements, gender split). What may stay, in one clause in the evaluation section, is the
population-coverage point now that a clean figure exists: ages 16 to 78, heights **150 to 220 cm**,
weights 38 to 210 kg, US and Europe (FX-011). Asking a provider what population its model was
validated on is good evaluation advice and now costs one sentence instead of a paragraph.

**The second half of item 15 is a non-issue in our sources.** The review says "the number of years of
data also varies across public materials". Checked: every internal source says `9+ years`
(`proof-points.md`, `how-it-works.md`, `overview.md`, `messaging.md`, `competitors.md`,
`tech-spec.md`). Any variation is on the public site, not in the repo.

### B3. Item 13, essential fat / beneficial fat. **Removed from the article. Proof-points diverge.**

The review asks to verify or remove them, and gives the documented output set as BMI, BMR, body fat
percentage, lean mass, fat mass, predicted weight, measurements, and a 3D model.

Our sources **do** list them: `proof-points.md` line 48, `how-it-works.md` line 25 and **approved
claim FX-009** all include `essential fat, beneficial fat`. But neither term earns space in a wellness
hub and the reviewer flagged them, so they are **removed from this article**.

**`predicted weight` is NOT added — corrected 2026-09-02.** The reviewer lists it in the documented
output set. Checked: it appears nowhere in `brand-assets/product-info/`, and **FX-009 does not contain
it.** What we do have is a *separate* proof-point, "weight estimation, ±3.5% average error margin"
(`proof-points.md` line 21, `overview.md` line 38), which belongs to Smart Scales mismatch flagging,
not to the body-composition output list. Citing "predicted weight" as a composition output would be
an unsupported claim, and this hub does not need it.

**Output list for this article, FX-009 minus the two flagged terms:** BMI, BMR, body fat percentage,
lean mass, fat mass, 80+ body measurements, 3D model. Nothing else. `seo-writer` must not add
`predicted weight`.

**Divergences flagged, both owner Vadim:**
1. `proof-points.md`, `how-it-works.md` and FX-009 still list essential and beneficial fat, which the
   reviewer wants gone. Either the sources are stale or the reviewer is wrong about the product.
2. The reviewer's documented set includes `predicted weight`, which no approved claim supports. If
   weight estimation really is a composition output, FX-009 and `proof-points.md` need the row added.

Also applied from item 13: **"body composition values" → "body composition estimates"** throughout.
This matches `compliance.md`, which already says "body measurements and composition estimates".

### B4. Item 16, number formatting. **Reviewer's format applied.**

v1 spelled these out ("96 to 97 percent", "between 1.5 and 2.0 cm"). The review asks for `96-97%`
and `1.5-2.0 cm`. Applied. **Hyphens, not en dashes** — the em/en dash ban is absolute and unchanged.

The approved repeatability formulation replaces v1's internal-validation prose:

> For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less
> than 1 cm.

The measurement-level figures v1 carried (chest 0.60 cm, waist 0.89 cm, ">95 percent repeatability
consistency", "detailed methodology available under NDA") are **cut** — too detailed for this hub,
per item 16.

## C. Item 20, the exact compliance wordings

The review asks to confirm the approved wording. Sourced from
`brand-assets/product-info/compliance.md`:

| Topic | Approved wording to use | Source line |
|---|---|---|
| GDPR roles | "In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under GDPR." | Review 1 item 20 (approved role formulation). Replaces the vague "follows GDPR principles" in `compliance.md`. |
| Photo deletion / retention | Photos are permanently removed immediately after processing, or within 30 days, depending on the client's configured policy. | `compliance.md`, Photo retention row + buyer Q |
| Face obfuscation | Photos are automatically blurred when stored. | `compliance.md`, Photo blur row |
| Regional storage | Amazon S3 in the client's region, with server-side encryption (SSE-S3) always on. | `compliance.md`, Storage + Encryption rows |
| Personal identifiers | No personal identifiers are processed; photos cannot be linked to individuals via 3DLOOK. | `compliance.md`, Personal identifier row |
| AI training | Photos are not used to train the model. | `compliance.md`, buyer Q |
| HIPAA | **Do not foreground.** Per item 20 a non-clinical wellness hub does not lead with healthcare compliance. One mention maximum, in the evaluation section, as something to ask about. | Review 1 item 20 |
| SOC 2 | **Never mention.** Not certified. | `compliance.md`, What we do NOT claim |

## D. Every review item, and where it lands

| # | Item | Disposition |
|---|---|---|
| 1 | Scope note after the intro | **Apply.** Section 1, with the three "belongs elsewhere" redirects as links. |
| 2 | Broaden beyond corporate wellness | **Apply in full.** See A1. |
| 3 | Cut the employer/insurer section | **Apply.** One short subsection inside section 10, three points, link out. Rewards FAQ question removed. |
| 4 | Rework the opening | **Apply.** New frame: limited visibility into physical progress between check-ins. All five flagged claims cut. |
| 5 | Remove "Why this matters now" | **Apply — remove.** No third-party evidence exists for the four claims, so the section goes. The one defensible point (smartphone capture removes the hardware constraint) folds into section 2 as a clause. Both dismissive budget claims cut. |
| 6 | Value-map table | **Apply.** Section 3, the reviewer's five rows verbatim. |
| 7 | Keep progress visibility strongest | **Apply.** Section 4. "The story the product tells is now accurate" → "a more complete view of progress". |
| 8 | Balance personalization | **Apply.** Section 5, the six combining inputs listed. Grouping by measured starting point is **retained** with aggregated reporting, purpose limitation and privacy controls attached. |
| 9 | Engagement claims supportive, not causal | **Apply.** Section 6, the reviewer's four formulations. No retention causality anywhere. No third-party source added — none is approved, and inventing a citation is worse than omitting one. **Flagged as an open item.** |
| 10 | Wellness-specific UX consideration | **Apply.** Section 6, five points. This is new material and the clearest differentiator from the fitness hub. |
| 11 | Merge workflow + implementation | **Apply.** Section 7, the reviewer's five steps. Both anxiety phrasings cut. |
| 12 | Shorten pilot metrics | **Apply.** The reviewer's five measures, inside section 7. No causal retention claim. |
| 13 | Output list | **Apply with one correction.** See B3: essential/beneficial fat removed, `predicted weight` NOT added (no approved claim supports it), "values" → "estimates". |
| 14 | DEXA → DXA | **Apply in the article.** See B1. |
| 15 | Training-data paragraph | **Figure resolved, detailed paragraph still cut.** Vadim confirmed 150-220 cm on 2026-09-02 and it is propagated repo-wide. See B2. |
| 16 | Accuracy discussion | **Apply.** See B4. All three absolute statements cut. |
| 17 | Integration wording | **Apply.** "API, web SDK, and mobile SDKs" replaces "API or camera SDK". |
| 18 | "It does not detect fraud" | **Apply.** Becomes: capture-quality and verification signals, no final fraud determinations. |
| 19 | Medical-device wording | **Apply.** See A2. Five-item limitations list compressed to one or two paragraphs. |
| 20 | Privacy and compliance language | **Apply.** See C. |
| — | Recommended 12-section structure | **Apply verbatim as the new outline.** |
| — | Target 2,500-2,800 words | **Apply.** From 4,035. Hard target: 2,650 ±150. |

## E. What does NOT change from checkpoint 1

- H1, verbatim from the content-plan strategy row
- Hub #8 placement, `create-net-new` action type, P0 priority
- The architecture re-parenting decision: `wellness-rewards-verification…` becomes the
  employer/insurer sub-hub. Still requires the `published-articles-inventory.md` update and the
  internal-link pass at publish.
- All four internal-link directions must survive the cut: up, sideways, down, trust
- The inbound internal-link pass from the five backlink donor pages. This is still the single
  thing that makes the page rankable and it survives the rewrite unchanged.
- No named vendors. No wellness proof points (none exist — argue from mechanism, never re-label
  Yazen or UK Meds as wellness).
- Privacy FAQ dependency: still an unpublished P0, so short inline answers stay, with
  `<!-- TODO(publish) -->` markers.

## F. Open items after this revision

1. **No third-party source on self-monitoring and feedback** (review item 9 asks for one). None is
   approved. The engagement section argues from mechanism only. If Vadim clears a source, it
   strengthens section 6.
2. **DEXA/DXA divergence in brand-assets.** See B1. Owner: Vadim.
3. ~~**Height range 150-205 vs 150-220.**~~ **CLOSED 2026-09-02 — 150 to 220 cm, one figure for
   both training data and the validation population.** No follow-ons: the labelling question was
   settled by the same ruling, and the live accuracy page already carried the correct figure, so the
   fix was to our stale local copy rather than to the CMS. Nothing left for Vadim here.
4. **essential/beneficial fat vs `predicted weight`.** Two separate divergences between the review
   and `proof-points.md` / FX-009. See B3. Owner: Vadim.
5. **"positioned as" is now in its third state.** See A2. Owner: editorial owner + Vadim.
6. **Images still not produced.** Unchanged from v1. Needs design.
