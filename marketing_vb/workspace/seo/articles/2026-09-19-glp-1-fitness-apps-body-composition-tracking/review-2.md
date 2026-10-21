---
article: 2026-09-19-glp-1-fitness-apps-body-composition-tracking
published_slug: glp-1-muscle-loss-fitness-apps
review: 2
source: "Google Doc 1zRxKobn-1C5APcwhqZFX6T4qysxOhv62pwbyW9PKYb4, tab «Review 2» (t.5ivw4tehz9p5); sent by Assel in Slack DM 2026-10-20 15:00 UTC"
extracted: 2026-10-21 by coordinator via oo googledocs get_document_by_id (include_tabs_content=true)
reviewed_text: "Doc tab «Version 2» = v2/final.md (the 19.09 text, 128/128 sentences match), NOT the Review 1 rewrite (commit 93c4d79, now snapshotted in v3/). About half of the items below quote lines that the Review 1 rewrite already changed — see review-2-decisions.md."
extraction_notes: "Verbatim text. Link chips kept as markdown links; the trailing `?utm_source=chatgpt.com` on every reviewer link was stripped (never copy it into the article). Soft line breaks (\\x0b) converted to newlines. Tables rebuilt as markdown tables."
authority: "review-2-decisions.md WINS over this file wherever the two differ."
---

## Evaluation of the revised article
The revision is more accurate, but I would make one more substantive edit before publication. It now handles the late baseline well, states more clearly that the accuracy figures apply to body measurements, and avoids implying that FitXpress outperforms expert tape measurement. The central gap remains: the article promises a fitness app perspective but gives readers little detail about what the app should display or do with the data. The existing [AI in Fitness hub](https://3dlook.ai/content-hub/ai-in-fitness-industry/) and [online coaching article](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/) already cover much of its general workflow and method comparison. [3dlook.ai](https://3dlook.ai/content-hub/ai-in-fitness-industry/)
| Earlier recommendation | Status in this version |
|---|---|
| Clarify what a late baseline means | Resolved. “The baseline marks where the app’s record begins” is precise and useful. |
| Distinguish body-measurement validation from muscle or composition validation | Largely resolved. The revised performance section and first FAQ make this distinction. |
| Explain how composition estimates are produced | Partly resolved. The FitXpress section adds inputs, but the short answer still says estimates “split” weight change into fat and lean components. |
| Give the article a distinctive app-level example | Open. The progress view is still a four-word bullet followed by an image placeholder. |
| Reduce overlap with existing articles | Partly resolved. Links are better placed, but the separate roles, method-selection, best-fit, and implementation sections remain repetitive. |
| Verify the 34,000-scan example | Open. The claim remains without a supporting source in the draft. |
| Clarify privacy and sharing requirements | Open. The text still presents member consent and agreements as the complete explanation. |
| Align the headline with what scanning can establish | Open. “Muscle Loss” leads the H1, while the answer that FitXpress cannot measure muscle loss appears near the end. |
### Priority edits
1. Put the muscle-loss limitation near the beginning. The research section makes a valid distinction: lean mass is broader than muscle, and the cited review reports a wide range of lean-mass changes across studies. Readers arriving for “GLP-1 muscle loss” should see the direct answer before the workflow and product sections. [PubMed](https://pubmed.ncbi.nlm.nih.gov/38937282/)
I would keep the search topic but make the promise more exact:
GLP-1 Muscle Loss: What Fitness Apps Can Track Beyond Scale Weight
Then place a short answer after the opening:
A fitness app can show weight, body measurements, body composition estimates, and strength-training history together. A mobile body scan cannot determine whether a member has lost muscle or establish the cause of a change in lean mass.
2. Replace “split that change” in the short answer. It implies that the estimate identifies the actual fat and lean components of weight loss. FitXpress derives composition outputs from scan-generated measurements and relevant inputs; the outputs have their own methods and limitations. [3dlook.ai](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)
Suggested wording:
Body composition estimates provide modeled fat and lean mass values alongside weight. They can support review of trends, but they do not establish how much muscle a member gained or lost.
The FitXpress section should also specify which weight input the proposed app workflow uses, rather than leaving “optional weight” unexplained.
3. Build the article around a concrete progress view. This is the clearest way to make the piece distinct from the existing coaching article. Replace the generic “One progress view” bullet and Image 1 – Concept placeholder with a brief, labeled example:
| App displays | Source | Interpretation shown to the member |
|---|---|---|
| Weight trend | Member-entered or synced scale reading | Total weight change |
| Waist and other circumferences | Guided scans | Measurement changes, subject to capture variation |
| Fat and lean mass estimates | FitXpress calculation | Estimated trends; lean mass is not muscle mass |
| Completed strength sessions and performance | Fitness app | Training context alongside the body-data trends |
Follow it with one paragraph on what happens when signals disagree: review capture conditions and prior readings, avoid assigning a cause from one scan, and route clinical concerns to the prescribing team. Image 1 can then be an annotated mockup of this exact view. Label any numbers as illustrative.
4. Condense the middle. The sections “What the app, the prescribing program, and FitXpress each handle,” “Scale weight, body composition estimates, and DXA or professional BIA,” and “Fitness apps and GLP-1 programs this workflow fits” repeat the boundary and method discussion. Keep the useful distinction that scans and DXA/BIA records should each be compared with earlier results obtained by the same method. Move that point into the progress-view section, retain a short responsibilities paragraph, and link to the existing method comparison. This will give the article a clearer path from evidence → app design → implementation → FitXpress.
5. Correct two operational statements.
- “Scans spaced closer than the change they are meant to show add records without adding information” is too absolute. A short interval can still provide information about variability or capture quality. Say: “Set the check-in interval according to the program schedule, expected changes, member burden, and variation in the specific measurements being compared.” The published repeatability figure is for evaluated body measurements and is not a universal change threshold for composition estimates. [3dlook.ai](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)
- “An alternative measurement path” stops after identifying a limitation for people with physical disabilities. Complete the thought: the app should offer an appropriate alternative when someone cannot perform the standard capture, identify the method used, and avoid treating results from different methods as one continuous measurement trend.
6. Resolve the evidence and sharing claims. The linked FitXpress fitness page does not substantiate the 34,000 scans in 2025 figure. Keep it if there is an approved internal source confirming the count, period, customer description, and permitted public wording; otherwise remove it. [3DLOOK](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)
For separate app and prescribing services, replace “sharing depends on the member’s consent and on agreements between the two” with “any sharing requires an applicable lawful basis, appropriate notices and permissions, and agreements governing the exchange.” The privacy FAQ specifies consent where applicable, rather than as the sole basis in every workflow. Also replace “two organizations hold parts of the progress record” with “the fitness app company and prescribing provider may each hold different records.” [3DLOOK](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)
### Smaller editorial fixes
- Use the approved sentence exactly: “For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.” [3dlook.ai](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/)
- Specify that the integrating company associates and selects the two scan IDs for Body Progress; FitXpress does not track which scans belong to a person. [3DLOOK](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)
- The KFF statistic is correctly framed as a US adult poll, but it does not establish the share of fitness app members taking GLP-1 medication. Consider removing the poll paragraph: the opening member scenario establishes relevance more directly.
- Turn Image 2 into a defined brief: guided two-photo capture → scan-derived outputs → app-controlled progress view. Avoid a visual that labels lean mass as muscle.
- After publication, add contextual links to this article from the fitness hub and GLP-1 market article. Its outgoing links already establish the cluster relationship.
Overall: the factual revisions are moving in the right direction. The remaining work is mainly structural: give product teams a specific progress-view example, tighten repeated sections, and clear the unsupported proof point. Those changes would make this a valuable bridge article rather than another general explanation of body scanning.


