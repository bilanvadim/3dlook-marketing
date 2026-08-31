---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/instagram-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
coordinator_review: |
  agreement: ✅ agree
  top_issue: None blocking; the M1 and M2 items were already fixed before QC ran.
  notes: |
    No action needed on claims. The two mechanical items QC would have caught were already
    corrected pre-QC: GLP-1 expanded at first use, and the stacked-negation disclaimer split into
    two sentences. post-brand-checker scored this 10/10 independently.
    Agreed on design-tip verbosity and the missing past-posts corpus; both are pack-wide, not
    per-post defects. brand-assets/past-posts/instagram-company/ has never been seeded.
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/instagram-company/post.md`
**Total: 16/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5

- Correct source. Lines 16-17 cite `published-live-2026-08-28.md` and the live URL, not a superseded `draft-v*`. Every claim in the body traces to that file.
- Two corrections from the twitter QC landed: `article_slug: glp-1-market` (line 5) now matches publish-package frontmatter and the live URL, and the design tip names `cover-3.webp` as the article visual with an alt-faithful description (line 41), instead of promoting an in-body banner to hero. Anchoring on the live 2026 assets rather than publish-package §4 is the coordinator's brief, so it is not scored as a missing input.
- IG config block applied on the mechanical dimensions: 982 chars (600-1000), hook line 111 chars (under the 125 cut), zero hashtags, one emoji, `carousel` is a legal IG format, product bias 100% FitXpress.
- **The one shallow step: the profile's tone line was read but only half applied.** `social-profiles-config.md` line 51 defines instagram-company as *"Visual storytelling. Human angle — technology through the lens of real outcomes. Less corporate, more brand."* The `Angle` field (line 18) commits to exactly that: *"The human moment inside the article's cover image: a patient's body stats..."*. The caption then contains no person, no patient, no outcome — the grammatical subject throughout is records, dates and methods. The declared angle and the delivered copy are different posts.
- `brand-assets/past-posts/instagram-company/` does not exist (the whole folder is absent; the 2026-08-21 report described it as empty). Per step 4 the correct behaviour is to continue, which the artifact did, but it does not flag the missing corpus either. Infrastructure gap, not an artifact defect — same as the twitter run.
- One angle, not a summary, and distinct from its pack siblings (twitter = documentation gap, facebook = delivery-model split, this = cross-date comparability). No internal cannibalization.

### B. Factual accuracy — 4/5

- Every product number traces to `proof-points.md` **and** to the live article: "80+ measurements" (proof-points line 47; article line 145), "less than 1 cm" (proof-points line 28 `< 1 cm`; article line 147), "body fat percentage, lean mass and fat mass" (proof-points line 48), "two photos, front and side, about 30 to 45 seconds, no specialized hardware" (article line 145). The 2024 lean-mass review is article line 119, reproduced without distortion.
- Claims discipline clean against `about-me.md`: repeatability is used (the correct frame for longitudinal GLP-1 use), accuracy is never reduced to a universal number because accuracy is never claimed at all. Line 31 states the boundary in the required post-2026-08-25 form — "FitXpress is not a medical device", not "is not positioned as". No diagnosis, no decisioning, no DEXA/scale-replacement, no eligibility claim. `audience.md` segment 1 "Don't" list respected, and no bleed into UK pharmacy compliance.
- No invented clients, no invented capability, correct product (`fitxpress`), no anti-positioning lead.
- **Line 27 hardens a deliberately hedged source claim:** "a check-in **is often** a single number on a scale". The article says programs "**may rely on** scale weight, patient-reported information, and manually captured progress photos" (line 105). Review 2 softened claims across this article on purpose. This is the second post in the pack to do it (the twitter post wrote "check-ins often run on a scale number"), so it is a pack-level pattern rather than a one-off.
- **Design tip asserts an asset detail the source does not evidence.** Line 43 instructs slide 1 to crop the cover "to a single date column with only a weight figure on it". The live alt text for `cover-3.webp` (article line 38) describes "body stats ... highlighting changes in body **fat and mass**" — no weight figure is documented. Same class of error as the twitter post's "no patient photography", one degree milder because it reads as an instruction rather than a description.
- Minor: "no special equipment" (line 29) widens the article's "without specialized scanning **hardware**" — a smartphone is still required. Not scored separately.

### C. Brand & tone — 2/3

- **Two em dashes, both in metadata fields.** Line 35: `**CTA:** Soft — "link in bio"...`. Line 41: `**Article visual:** The live cover \`cover-3.webp\` — a woman at a desk...`. CLAUDE.md §6 and `terminology-guardrails.md` ban the em dash "always, without exceptions". Line 14's dashes are the template's own heading form (`## Post — {profile} — {article_slug}`) and are not counted against the drafter. The 2026-08-21 instagram report deducted C to 2/3 for a single em dash in the `Angle` field; the pattern has repeated, and the facebook post in this same pack has it on lines 37 and 43 too.
- Everything else clean. Grep over the file: zero banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/tapestry/realm/unlock/unleash/game-changing/cutting-edge), no `positioned as`, no `objective` about our output, no `by hand`. No `plus` stacking, no `so` introducing a benefit, no presumed-reaction opener, no "not just X, it's Y", no adjectival punch triad. Zero hashtags, one emoji (📈).
- Voice matches `about-me.md` cadence: "It keeps the record consistent between appointments. The care team reads it." is the short-verdict pattern, and the limits are stated in the same breath as the capability rather than bolted on. Rule 6c satisfied — the post takes a position.
- Watch item, not scored: "That number is real, it just doesn't say what changed" (line 27) sits near the banned corrective-contrast shape. It reads as concession plus consequence, not "X, not Y", so it passes.
- Social override could not be run: the 3-post style comparison needs `past-posts/instagram-company/`, which does not exist. `detect-ai-tells.py` also not run — this QC pass has no Bash.

### D. Format & structure — 3/3

- Frontmatter complete and correct: all six template fields present including `product: fitxpress`, plus useful extras (`handle`, `article_url`, `vertical`, `format`). `article_slug: glp-1-market` is right.
- Correct path. All template sections present (Source article, Angle, Goal, body, CTA, Design tip with all four fields). The extra `Claims used` and `Length` fields are pack convention, shared with the facebook post, and cost nothing.
- Length self-report verified by manual count: body is 982 chars, inside 600-1000. Hook first line 111 chars, under the 125 cut.
- `manifest.json` correct: only the `instagram-company` entry touched, canonical schema (`profile_id`/`platform`/`handle`/`post_file`/`status`/`format`), exactly one length field and the right unit for the platform (`character_count_body: 982`), `profiles_skipped: []`, `ready_for_review: false` despite all nine profiles reading `ready`.
- Minor, not deducted (consistent with the two prior reports): `Angle` runs two sentences where the template asks for one.

### E. Output quality — 3/4

- Hook works. "Month one, month three, month six." is stoppable, sets the whole post up in seven words, and clears the "see more" cut with room to spare.
- **The profile's reason for existing is missing from the copy.** instagram-company is the one profile briefed for human storytelling, the drafter's own `Angle` promised the human moment from the cover, and the caption delivers a mechanism explainer. Removing the first line, this could be published as-is on facebook-company. The 19/20 instagram precedent (2026-08-21) put a person in the caption; this one does not.
- **Paragraph 2 opens with clinical friction.** "On a glucagon-like peptide-1 (GLP-1) program..." is a 30-character expansion in line 2 of an Instagram caption, and the profile's `avoid` list is "занадто технічні деталі, API-talk, pricing, jargon". M1 requires the expansion, so the drafter is caught between two rules rather than careless — but the resolution shipped here favours the guardrail over the channel. The same paragraph then cites "a 2024 review ... found substantial variation across studies", an unlinkable academic reference on the one platform that has no links. Flag for the improver: the abbreviation rule has no Instagram carve-out and probably needs one.
- **Design tip costs the designer two questions.** Slide 1 asks for "a weight figure" on a cover whose documented stats are body fat and mass. Slide 3 asks for a "two-photo capture glyph, front and side" that appears in none of the three 2026 assets (`cover-3.webp` is a photograph, `banner_1-3.webp` is the market-figures infographic, `banner_2-2.webp` is the five-requirements infographic), so it is a net-new element rather than an adaptation. Slide 2 is faithful and needs nothing.
- Design tokens correct per `DESIGN.md`: `#143DFF` (not `#2962FF`), `#050F40`, Satoshi (not Inter). "No body-exposure imagery in any slide" is a good instinct for this vertical.
- Estimate: 5-10 minutes of Vadim's editing — two dashes, and a call on whether the caption needs a person in it.

## Top 3 issues (приоритет для improver)

1. **Em dashes on lines 35 and 41**, both in metadata fields, body clean. Identical finding to the 2026-08-21 instagram report, and present in the facebook sibling too. The drafter has learned to keep the post body clean and the checker sweeps the body, so the metadata fields are an unswept surface. The sweep needs to cover the whole file.
2. **The declared angle is not the delivered post.** Line 18 promises "the human moment inside the article's cover image: a patient's body stats"; the caption contains no person. For the profile whose entire tone spec is "human angle, technology through the lens of real outcomes", this is the substantive miss, and it is invisible to any mechanical check.
3. **Design tip asserts asset details that the live assets do not evidence** — a weight figure on `cover-3.webp` (alt text says body fat and mass) and a two-photo capture glyph that exists in none of the three 2026 files. The twitter post made the same class of error about the same asset set, so the drafter is describing images it cannot see without marking which details are inferred.

## Coordinator review

