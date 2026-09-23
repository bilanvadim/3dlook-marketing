# Accuracy formulations — canonical, from the live framework article

**Source of truth:** <https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/>
**Fetched and transcribed verbatim: 2026-09-02.**

`about-me.md` §"Canonical figures" already says it plainly: *"Not the source of truth. The
'Body Scanning Accuracy' framework article is canonical."* This file is that article's accuracy
language, transcribed so agents do not have to fetch a web page mid-run and do not have to
reconstruct the wording from `proof-points.md` numbers.

**Everything in section 1 is quoted verbatim from the live page.** Do not improve it, do not
tighten it, do not re-punctuate it. If a formulation reads awkwardly, that is still the
formulation, because it is what is published and what legal and editorial signed off on.

**When the live page changes, this file is stale.** Re-fetch and re-transcribe. There is no
automated sync: the page is behind no auth, but a scraper that silently rewrites approved
wording is worse than a stale file with a date on it.

---

## 1. The formulations, verbatim

### 1.1 Accuracy

> Internal validation across multiple real-world scan events with five repeated scans per
> person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy
> of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per
> measurement, varying by body part.

> the typical absolute error is generally in the 1.5-2.0 cm range, depending on the measurement
> type and body part evaluated.

**Format is `96-97%` and `1.5-2.0 cm`, with hyphens.** Not en dashes, not "96 to 97 percent".
Review 1 item 16 confirmed this against the live page.

### 1.2 Repeatability

> Internal repeatability testing on a real-world customer dataset, using five repeated scans
> per participant, showed strong scan-to-scan consistency across the majority of evaluated
> measurements.

> For most evaluated measurements, repeated scans showed typical scan-to-scan differences of
> less than 1 cm.

> For most measurements, repeated scans produced typical differences of less than 1 cm.

The second and third are variants of one another. **Prefer the second**, which Review 1 item 16
named "the approved repeatability formulation".

### 1.3 The ISO benchmark, which is a SEPARATE study

> The ISO 8559-1:2017 benchmark, which uses 3D scanner averages as the reference (a different
> reference than the internal pattern-maker comparison), placed 3DLOOK's session-to-session
> repeatability at 0.40 cm.

> The numbers from the two studies should not be combined because the references differ.

**This is a hard rule, not a preference.** `0.40 cm` and the internal figures (`96-97%`,
`1.5-2.0 cm`, `< 1 cm`) answer different questions against different references. Quoting them
in one breath, one sentence or one paragraph misrepresents both. `article_lint.py` fails it.

### 1.4 Validation population and its scope

> The internal validation population included participants aged 16–78, heights of 150–220 cm,
> weights of 38–210 kg, and participants from the US and Europe.

> These ranges define the population scope to which the reported accuracy figures apply.

> 3DLOOK's internal validation dataset covers ages 16 to 78, heights 150 to 220 cm, weights 38
> to 210 kg, and participants across the US and Europe.

> Performance outside this scope has not been characterized.

**Height is 150 to 220 cm.** Confirmed by Vadim 2026-09-02 and by the live page, which carries
it in three places. The 150-205 cm figure from the Apr 2025 deck is superseded and
`article_lint.py` fails it.

### 1.5 What an accuracy figure means, and what it does not

> The same percentage can represent very different levels of performance depending on the
> reference method, test population, measurement protocol, and number of repeated scans.

> Every accuracy figure is really an accuracy relative to one specific reference.

> For most use cases, the important question is not the headline accuracy number alone, but
> whether the expected measurement error is acceptable for the workflow the data supports.

> Accurate enough for which decision?

> A measurement system used for apparel sizing, uniform allocation, GLP-1 progress tracking,
> remote screening, or underwriting support does not need to be evaluated against the same
> operational standard in every case.

### 1.6 The conditions that must qualify a figure

> the reference method, measurement protocol, population tested, and intended workflow are
> clearly defined

The five dimensions the article says must be evaluated together:

> 1. Measurement accuracy
> 2. Scan-to-scan repeatability
> 3. Real-world robustness
> 4. Output breadth and use-case fit
> 5. Validation strength

### 1.7 The diligence question to hand a buyer

> For any body-scanning solution, the key diligence question is whether the vendor clearly
> explains how repeatability was measured, how many repeated scans or sessions were included,
> which measurements were evaluated, and what level of variation was observed.

### 1.8 Methodology availability

> Detailed methodology, including sample size, measurement-level results, and the definition of
> repeatability used in the analysis, is available under NDA.

Use this sentence rather than a bare `>X%` with no method behind it. That is editorial guardrail
#4 and the detector's `bare_percentage` category.

### 1.9 What is NOT claimed. Quote these when scope comes up.

> 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a
> third-party clinical study.

> No peer-reviewed publication specific to 3DLOOK's accuracy claims is currently on record.

> It has not been clinically validated through peer-reviewed research or third-party clinical
> studies, and it is not positioned as a medical device.

> The NCSU partnership was dataset enrichment work, not independent validation of 3DLOOK's
> measurement claims.

> Where direct comparative validation against a specific reference method has not been
> completed, 3DLOOK should not be positioned as equivalent to that method.

> 3DLOOK should not be positioned as equivalent to DEXA, BIA, calibrated scales, or certified
> manual anthropometry methods when the workflow, protocol, or regulatory standard requires
> those methods.

**The NCSU line matters.** It is the only place on file that pre-empts "you partnered with a
university, so you are independently validated". Reach for it whenever a draft edges toward
implying external validation.

---

## 2. Where the live page and our current rules disagree

Two open, one closed. §2.1 and §2.3 are live: a writer copying those §1.9 sentences verbatim
will fail our own gate. §2.2 was decided by Vadim on 2026-09-02.

### 2.1 The live page uses "positioned as" for equivalence. Our detector fails that.

Three of the sentences in §1.9 use it, including two for **equivalence** rather than for the
medical-device boundary:

- "should not be positioned as equivalent to that method"
- "should not be positioned as equivalent to DEXA, BIA, calibrated scales..."

`terminology-guardrails.md` §2.10 bans "positioned as" for product, intended-use and regulatory
statements. Vadim's 2026-09-02 revert licensed **exactly one sentence**, the medical-device one, and that licence was withdrawn on 2026-09-11 (§2.3).
Equivalence is still a hard fail, and `editorial-guardrails.md` #7 was deliberately reworded on
2026-08-25 away from "should not be positioned as equivalent to" for that reason.

So the live canonical trust asset carries wording our own linter rejects. Three ways out, and
picking one is not this file's job:

1. License "positioned as" for equivalence, matching the live page (no sentence is licensed since 2026-09-11, see §2.3).
2. Keep the ban and use guardrail #7's replacement in new articles: *"FitXpress is not
   equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory
   standard requires those methods."* Same meaning, passes the gate. **This is what new drafts
   do today.**
3. Update the live page to match the guardrail.

**Current behaviour: option 2.** Quote §1.9 verbatim only in the two sentences that do not carry
"positioned as equivalent"; for equivalence, use guardrail #7's wording.

### 2.2 DXA is correct. RESOLVED 2026-09-02 by Vadim.

The three-way split is closed. **DXA is the spelling in all our own prose**, and it has been
propagated: `terminology-guardrails.md` §1 and its grep table, `editorial-guardrails.md` #7 and
M1, `about-me.md`, `product-info/faq.md`, `competitors.md`,
`content-strategy-guidelines.md`, `ai-tells-sweep.md`, the page-builder Kit, and
`context-pack-builder` in all three copies. `article_lint.py` fails the old spelling.

**One licensed exception, because otherwise the gate fights SEO.** `DEXA` carries real search
volume and one published slug already uses it (`ai-body-scanners-vs-dexa-scans/`). So `DEXA` is
allowed where it is a search term, written as **`DXA (also written DEXA)`**. The gate licenses
it by looking for `DXA` on the same line.

**Still needed, and it is a CMS edit, not a repo one:** the quoted sentences in §1.9 above are
verbatim from the live page, which writes DEXA. The live framework article needs updating to
DXA. Published articles are not retro-edited as a rule, but this one is Trust Asset #1 and
every new article links to it, so the two would disagree in public on the spelling. Owner:
whoever owns WordPress.

### 2.3 The live page writes "not positioned as a medical device". Our rule writes it directly.

The third §1.9 sentence ends "and it is not positioned as a medical device." Since 2026-09-11 the
rule is the direct form, **"FitXpress is not a medical device."** (Vadim's call on the editor's
final of the occupational-health intake article), and `detect-ai-tells.py` fails every "positioned
as" sentence, the medical-device one included. Quote the first half of that §1.9 sentence if you
need it, then state the boundary as its own sentence in the direct form. The live framework page
would need a CMS edit to match; same owner and same kind of debt as §2.2.

---

## 3. How to use this in a draft

1. **Never state an accuracy figure without a condition.** The figure alone is meaningless; §1.5
   is the reason, in the article's own words. Name the reference method, the population, the
   protocol, or the decision the number has to support.
2. **Link to the framework article** from the paragraph carrying the figure, not from a distant
   "further reading" block. A cited figure whose source is a scroll away is the weaker
   configuration.
3. **Never combine the two benchmarks.** §1.3.
4. **Repeatability outranks accuracy for longitudinal tracking, but say it conditionally.**
   Review 1 item 16 struck "repeatability outranks accuracy" as too absolute. The defensible
   form: the acceptable error depends on the expected magnitude of change and the workflow;
   repeatability is especially important for longitudinal tracking; accuracy and repeatability
   are evaluated separately.
5. **Reserved words stay off our own evidence:** `independent`, `third-party`, `validated`,
   `clinically validated`, `peer-reviewed`. The detector's `reserved_words` category fails them.
   §1.9 is how to say what we actually have.
6. **Measurement-level figures belong in technical material, not in a hub.** Review 1 item 16
   cut the per-site girth numbers (chest 0.60 cm, waist 0.89 cm) from the Wellness hub for that
   reason. `proof-points.md` keeps them as FX-016 for when a technical page needs them.

## 4. The gate

```
python3 scripts/article_lint.py <file>.md
```

The **accuracy discipline** gate checks what a script can check: that no unapproved accuracy
figure appears, that the two benchmarks are not combined in one paragraph, that a figure is not
left bare, and that a paragraph carrying a figure links to the framework article. It cannot
judge whether a condition is the *right* condition. That stays with the editor.

---

## 5. Approved short forms, from an editorial final. NOT from the live page

Section 1 is verbatim from the live framework page and stays exactly as it is. The sentences
below carry the **same claims**, in the words the editor used in her final of
`manual-vs-digital-intake-occupational-health-screening` (Assel Sekerova, 2026-09-11; saved as
`brand-assets/past-articles/blog/manual-vs-digital-intake-occupational-health-screening.md`).

They exist because the §1 sentences run 20-42 words, and pasting them whole was one cause of
the editor's verdict on our revision 5: long sentences, reads as AI
(`brand-assets/style-guides/editorial-rewrites.md`). Either §1 or §5 is fine; do not mix the
two inside one paragraph. Every condition §3 requires is still present: the reference, "most of
the evaluated measurements", the NDA line, and the framework link, which stays on the paragraph.

**Repeatability** (short form of §1.2):

> Repeatability testing used a real-world customer dataset with five scans per participant.
> For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm.

**Accuracy** (short form of §1.1 and §1.8), in its own paragraph, after repeatability:

> A separate validation compared FitXpress measurements with expert pattern-maker tape
> measurements. Across the evaluated body measurements, reported accuracy was approximately
> 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed
> methodology is available under a non-disclosure agreement.

**What the evidence does not show:**

> These findings establish performance relative to the selected reference; they do not
> demonstrate superiority over expert tape measurement.

**The reframe, as a statement** (§1.5 without the quoted question):

> What counts as adequate performance depends on how the measurements will be used.

**FAQ form:**

> 3DLOOK's published figures compare FitXpress with expert tape measurements, which serve as
> the reference. The relevant question is whether the reported error and repeatability are
> suitable for the intended workflow.

Two notes. `below 1 cm` is accepted by the accuracy gate alongside `less than 1 cm` and
`< 1 cm` (added 2026-09-11). The final drops the word "internal" from both studies; where the
surrounding copy could be read as implying outside validation, put it back ("Internal
repeatability testing…"), per editorial guardrail #3.

**Population limitation** (approved by Vadim 2026-09-11; the number-store row is in
`proof-points.md`, Training data). It complements §1.4, "Performance outside this scope has not
been characterized.", and uses the editor's three-sentence shape: the limit, when it matters,
what the program needs.

> FitXpress was not specifically trained on data representing people with physical
> disabilities, and its measurement performance has not been established for this population.
> This matters when a disability affects the standard standing pose or capture sequence. In
> those cases, the program needs a documented alternative measurement path.

**Scope note (Vadim, 2026-09-23):** this sentence stays canon. It was removed only from the capture-quality FAQ (Review 1, C9) because that page does not need it; that is not a precedent for removing it elsewhere.

The last sentence fits a workflow article. Elsewhere, keep the first two and say what the
workflow does instead.
