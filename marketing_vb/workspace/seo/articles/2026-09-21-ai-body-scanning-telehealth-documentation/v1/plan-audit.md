---
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
plan: plan.md
stage: plan
created: 2026-09-21
audience: seo-publisher, Vadim, external reviewer
---

# Plan audit, 2026-09-21-ai-body-scanning-telehealth-documentation

Why the plan looks the way it does. The writer does not need this file.

## 1. Keyword synthesis across three seeds

Three Ahrefs pulls, all with `seed_has_data: true`. They tell three different stories.

**Seed 1, "telehealth documentation" (40/mo, KD 10, TP 100).** This is the real, correctly targeted pool and the one the title already sits on. The usable cluster is small: "cms telehealth documentation requirements" 150/mo KD 22, "telehealth documentation requirements" 70/mo KD 0, the 2025 and 2026 dated variants at 50 and 40, "ai tools for telehealth visit documentation" 30/mo, then a long tail of 10/mo and 0/mo phrases. Roughly half the 40 returned ideas are 0/mo.

**Seed 2, "telemedicine documentation" (0/mo).** A finding, not a failed pull. The seed and nearly every idea under it measure zero. The one non-zero phrase, "telemedicine system documentation" (250/mo), is IT and EHR system documentation, a different subject. Conclusion carried into the plan: use "telehealth" throughout, and do not include "telemedicine" as a synonym anywhere in the draft or the meta.

**Seed 3, "clinical documentation" (1,000/mo head, KD 16, TP 2,900).** Big and almost entirely off-intent. Most of the volume is career demand: "clinical documentation specialist" 3,700/mo, "clinical documentation specialist jobs" 2,300/mo. The genuinely adjacent pocket is ambient and note-taking AI ("ambient clinical documentation" 450/KD 29, "ai clinical documentation" 700/KD 67, "chatgpt for clinical documentation" 1,600/KD 8). That is a different product category: it transcribes and drafts what was said in a consultation. Structured body-data capture is an input to the same record from a different point in the process. Decision: do not target any of it. Use it only as one clause of context in Section 3, and turn the category question into FAQ 2, where we can answer it cleanly instead of competing for it.

### Demand reality, stated for checkpoint 1

The largest single figure in the entire pool is 150/mo, and the primary keyword itself is 40/mo. This is a thin-demand BOFU supporting page. That is a legitimate choice here, because the page exists to be the documentation anchor for the Admin Panel and a landing point for sales and procurement conversations, not to bring traffic. Vadim should see that now, not in Search Console in six months.

### SERP risk worth recording

Ahrefs reports the parent topic of "telehealth documentation" as "medicare modifier for telehealth". The head SERP is therefore weighted toward billing, coding and payer-rule content, which we will not write. Expect the page to earn long-tail and AI-answer visibility rather than the head term. If a ranking check three months post-publish shows nothing but billing results on page one, that is the explanation, not a content defect.

## 2. Title decision

Working title: "How AI Body Scanning Supports More Consistent Telehealth Documentation". Kept as the social and outreach phrasing, not as H1, because the keyword falls at word seven and "supports" describes an effect without naming the artifact the page is about.

Chosen: "Telehealth Documentation: How AI Body Scanning Creates More Consistent Records". Keyword in the first two words, outcome named, "creates structured records" is on the approved operational-verb list in `about-me.md`, no em dash, no content-plan label. At 78 characters it sits in the same range as the live occupational-health H1 (79 characters), so length is in house style even though a meta title will need trimming.

Rejected, with the reason each one fails:

| Variant | Why not |
|---|---|
| Telehealth Documentation Requirements: Where Body Data Fits | Chases the 70/mo KD 0 term, but the title promises a requirements explainer. Writing it would put us on the wrong side of "no guaranteed compliance" and of the ban on regulatory advice |
| AI Tools for Telehealth Visit Documentation: What Body Scanning Adds | Matches a 30/mo phrase and files the product under ambient note-taking AI, which is the category confusion FAQ 2 exists to prevent |
| Structured Body Data for Telehealth Records: A Documentation Guide | Near-duplicate of the product page title at `/structured-body-data-for-telehealth-digital-health-programs/`. Competing with our own down-link target is the definition of self-inflicted cannibalization |
| More Consistent Telehealth Documentation: Structured Body Data for Remote Care | Keyword split across the phrase, and "remote care" pulls toward remote monitoring, a different cluster inside the same hub |

## 3. Cannibalization map

Five live or planned neighbours touch this territory. How each one is handled:

| Neighbour | Status | Rule applied in the plan |
|---|---|---|
| the-potential-of-ai-in-telehealth (live 2026-08-07) | Hub 2 anchor | Up-link once, in Section 4. The broad overview is never restated. Every section stays narrower than the hub |
| online-pharmacy-bmi-verification-a-2026-compliance-guide (live 2026-08-24) | Owns telehealth BMI verification and the eligibility-support workflow since the 2026-08-24 boundary update | Link only, one sentence, descriptive anchor. The workflow is never re-explained. No BMI-threshold logic and no eligibility framing anywhere in the outline. This page links there; it is not a route into that topic |
| mobile-body-scanning-patient-engagement (live 2026-08-14) | Canonical engagement asset | Sideways link in related reading only. Its progress-visibility and retention thesis is deliberately absent. Our Section 6 is about record shape, not about showing progress to the patient |
| "Progress Photos vs Structured Body Data in Virtual Weight-Loss Programs" (planned, P1, create net-new, content-plan.md:144) | Not yet written | The highest-risk neighbour, because the natural table for a documentation article is exactly that comparison. Mitigation is written into Section 6 as a boundary: the table compares record shape (fields, timestamp, format, availability, re-entry), and the draft makes no argument about photo credibility or manipulation risk. Reviewers should fail the draft if that argument appears |
| "GLP-1 Patient Progress Record" (planned, Hub 3, content-plan.md:163) | Not yet written, shares the Admin Panel anchor | Kept apart by vertical: that row owns GLP-1 clinic workflow, baseline data and medication-supported progress. This one stays general telehealth. No GLP-1 clinical framing, no medication context, no GLP-1 keyword weaving |

Also excluded by hub boundary: insurance-underwriting documentation claims and KPIs belong to Hub 4 and appear nowhere here.

## 4. Directions considered and dropped

- **A CMS and payer requirements explainer.** The biggest keyword in the pool (150/mo) points this way. Dropped: it would require us to interpret reimbursement and documentation rules, which collides with the ban on guaranteed compliance and with "3DLOOK does not assert whether a clearance applies to a given customer". FAQ 1 captures the query without taking on the liability.
- **A head-to-head against ambient documentation AI.** Interesting demand, wrong category, and a named-comparison risk. Reduced to one clause in Section 3 and one FAQ answer.
- **An accuracy-first opening.** The instinct is to lead with 96-97%. This page's claim is record consistency, not accuracy, and `accuracy_framing` in the pack says only to invoke the numbers if the draft genuinely discusses accuracy. Result: no accuracy figure in the body at all, one repeatability figure in FAQ 4 with its condition and the framework link attached.
- **A named customer example.** Yazen is not named by Vadim's 2026-09-19 decision, and UK Meds belongs to the BMI verification page. A generic telehealth-program scenario carries the article without either. No case study, no geography.
- **The market sizing table.** None of its five use cases match this topic.
- **A second table.** The live model article carries two tables and still reads dense. One is enough here, and the FAQ absorbs what the second would have said.

## 5. Claim handling decisions

**FX-001 is the anchor and the weakest-sourced claim in the set.** Its wording comes from a draft publish package for the telehealth hub, and no `published-live-*.md` capture exists for that page. The feature itself is confirmed independently by the live Admin Panel launch post. The plan therefore instructs a rewrite in plain words rather than a copy of the draft sentence. A prior editorial pass raised, as a non-blocking advisory, whether to say "FitXpress Admin Panel" or a softer "vendor console". There is no ban on the name, so the plan uses it and flags the question below.

**Export is the phrase most likely to drift.** The content-plan row says "records/export/workflow", but `approved_claims` covers delivery through the API and access through the Admin Panel, not export formats, audit logs, permission models or named integrations. Section 5 carries that as an explicit boundary. If Vadim wants the article to state a specific export capability, it needs a claim added to the pack first.

**"Audit-ready" is positioning language from `competitors_context`, not an approved claim.** The plan bans it in the voice guardrails and substitutes "records that can be retrieved and reviewed".

**Privacy stays section-first.** Section 8 is five or six sentences and a link to the trust FAQ, per the content-plan guardrail that vertical privacy rows link the central FAQ instead of restating it. The live occupational-health article does not link the trust FAQ, which its own `known_issues` block records as a defect to fix in new articles. This plan fixes it.

## 6. Word count reasoning

Target is 2,100 words of prose, inside the pack's 1,800 to 2,400 band. The reference model, `manual-vs-digital-intake-occupational-health-screening`, is about 1,877 words in the editor's final with 9 H2s. This outline carries 10 H2s plus a four-question FAQ, so 2,100 is the honest budget. Per-section budgets in `plan.md` sum to 2,100 exactly, which gives the editor room to cut without renegotiating the structure. If the draft arrives over 2,300, the first cuts should come from Section 3 and Section 9, not from the boundary sections.

## 7. Open items

1. **Admin Panel naming.** Use "FitXpress Admin Panel" as written, or the softer "vendor console"? Prior editorial advisory, still unresolved. Plan assumes the product name. Vadim decides.
2. **Export specifics.** Is there an approved claim for what a team can export from the Admin Panel, and in what form? Without one, the draft describes delivery and retrieval only.
3. **External citation in Section 3.** The plan suggests HHS telehealth best-practice material and instructs the writer to verify the live page before citing. If verification fails, the section ships with no external citation. Reviewer should not read a missing citation there as an oversight.
4. **Thin demand, acknowledged.** Primary keyword 40/mo, largest pool figure 150/mo, head SERP skewed to billing content. Confirm this is accepted as a sales-support page rather than a traffic page before the writer starts.
5. **Progress Photos article sequencing.** This page and the planned Progress Photos comparison share a theme. If that article moves up the queue, re-check Section 6 so the two do not converge.

## 8. What the external reviewer should look at on this outline

- Does Section 6 stay about record shape, or has it become the photos-versus-data comparison?
- Is the BMI verification mention one sentence and a link, with no workflow explanation?
- Does any section promise a capability outside `approved_claims`, especially in Section 5?
- Is there exactly one accuracy-family figure in the whole plan, in FAQ 4, with its condition and the framework link?
- Does any FAQ question duplicate a body section? Four are planned, and the editor cut one of four on the last comparison article for exactly this reason.
