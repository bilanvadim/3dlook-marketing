# Editorial rewrites: what the editor changes in our drafts

**Status:** canonical for sentence length, repetition and the comparison-article format. Read it
with `blog-style-guide.md` (voice, article types) and `ai-tells-sweep.md` (AI tells). Where an
older structure or voice rule disagrees, this file wins, because it records what the editor
actually shipped.

**Mechanical half:** `scripts/article_lint.py`, gate `sentence length` (§1). Everything else here
is judgment, owned by `seo-editor` Pass 3d.

**Add to this file** when the next editorial final teaches something new: a dated section with
its own pairs. Do not rewrite the evidence below.

---

## Where this comes from

`manual-vs-digital-intake-occupational-health-screening`, FitXpress, Hub 8 comparison cluster.

- Our revision 5 (`workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md`,
  uploaded as tab "Version 3" of the article's Google Doc) passed all nine gates of
  `article_lint.py` and scored CLEAN on `detect-ai-tells.py`, 0.86 markers per 1,000 words.
- Assel Sekerova on that revision, relayed by Vadim on 2026-09-11: *«в той версии мне не
  нравилась длинна предложений, были повторения и читалось это всё как явно AI»*. Long
  sentences, repetition, reads as obviously AI.
- Her final (tab "Final version", after two intermediate passes) is saved as
  `editorial-final-2026-09-11.md` in the article directory and as
  `brand-assets/past-articles/blog/manual-vs-digital-intake-occupational-health-screening.md`.
  The article-specific record is `editorial-delta-2026-09-11.md` in the article directory.

Our gates passed a text the editor rejected, so they were measuring the wrong things. The table
below is what they should have measured.

## The measurement

Prose sentences only (tables, headings, captions and image placeholders excluded), counted by
`prose_sentences()` in `article_lint.py`, the function the gate itself uses.

| Text | Mean words | p90 | Over 25 words | Over 35 words | Gate |
|---|---|---|---|---|---|
| Our revision 5 | 17.7 | 31 | 13 of 93 (14.0%) | 6 | FAIL |
| **Editorial final, 2026-09-11** | **14.7** | **23** | **3 of 94 (3.2%)** | **1** | PASS |
| `glp-1-market-hub`, live page 2026-08-28 | 15.2 | 23 | 5 of 120 (4.2%) | 0 | PASS |
| `remote-body-measurement-online-fitness-coaching`, live page 2026-09-04 | 13.6 | 22 | 6 of 146 (4.1%) | 0 | PASS |
| Our `2026-08-31-ai-body-data-wellness-platforms-hub/final.md` | 17.2 | 28 | 24 of 155 (15.5%) | 3 | FAIL |
| `online-pharmacy-bmi-verification`, live page 2026-08-24 | 16.9 | 28 | 24 of 124 (19.4%) | 2 | FAIL |
| `bariatric-hub-refresh`, live page 2026-07-27 | 16.6 | 31 | 51 of 233 (21.9%) | 10 | FAIL |

The three most recent editorial passes land on the same numbers independently. This is the house
standard, not one reviewer's taste. The two older live pages predate it and are not retro-edited.

Word count: 2,160 prose words in revision 5, 1,877 in the final, against a plan target of 2,050.
No claim, source or substantive section was lost. The 283 words came out of long sentences,
refrains, sentences about the page, and a table and an FAQ that repeated the body.

---

## 1. Sentence length (gated)

**Gate:** mean ≤ 16 words; at most 6% of sentences over 25 words; at most one sentence over 35,
and only for a quoted procedure or a list that loses its meaning when split. The finals sit at
14-15, so aim there, not at the ceiling.

What the editor did with our long sentences, most frequent move first.

**An inventory becomes several sentences.**

> **Ours (50 words):** FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts and signs Business Associate Agreements with HIPAA-covered customers, encrypts data at rest and in transit, processes no personal identifiers, and deletes photos immediately after processing or within 30 days, with the window set by client policy.
>
> **Final:** FitXpress encrypts data in transit and at rest, deletes photos after processing, and retains generated outputs in accordance with the deployment terms. In most enterprise deployments, the customer acts as the controller, and 3DLOOK acts as the processor under the General Data Protection Regulation (GDPR). A Business Associate Agreement under the Health Insurance Portability and Accountability Act (HIPAA) is available on request.

The wording of that paragraph changed along with its shape. Reuse the shape, not the wording:
`compliance.md` stays as it is for now (Vadim, 2026-09-11), so the BAA, retention and
personal-identifier facts keep its wording.
**Superseded 2026-09-18:** `compliance.md` was rebuilt from the live trust FAQ, and it now agrees
with this final on the substance (outputs retained per the deployment terms, BAA for qualifying
deployments, no "processes no personal identifiers"). The GDPR sentence adds "the data" before
controller and processor. Take the wording from `compliance.md`.

**A list of conditions becomes bullets under an H3.**

> **Ours (63 words):** Manual intake remains practical in several situations: single-site or low-volume programs where the appointment slot is not the constraint; populations without reliable smartphone or network access; intake dominated by history, symptom and functional content, where body measurement is a minor line item; workflows where the measurement is part of the examination; and programs with no downstream system able to receive a structured record.
>
> **Final:**
>
> ### Manual intake fits when
> - Appointment capacity is sufficient for the current volume.
> - Reliable smartphone or network access is limited.
> - Body measurement represents a small part of the intake workflow.
> - Measurement is intentionally completed during the examination.
> - The downstream system cannot receive structured records.

**A colon does not turn two ideas into one sentence.**

> **Ours (50 words):** One regulated context already routes the questionnaire for confidentiality: Appendix C to the Occupational Safety and Health Administration (OSHA) respiratory protection standard forbids the employer and the supervisor from reading a worker's answers, and obliges the employer to explain how to deliver the form to the reviewing health care professional.
>
> **Final:** The Occupational Safety and Health Administration (OSHA) respiratory protection standard illustrates how confidentiality requirements can shape the intake route. Appendix C requires employees to be able to complete the questionnaire privately and prevents employers and supervisors from reviewing their answers. The rule applies specifically to respirator medical evaluations, and the form must be submitted to the reviewing health care professional through an appropriate channel.

**Approved accuracy wording can be split too.** The canonical accuracy sentence runs 42 words. The
final carries the same figures, reference and hedge in two sentences plus the NDA line; those are
now approved short forms in `brand-assets/product-info/accuracy-formulations.md` §5.

**The one long sentence she kept** is the NHANES waist protocol, 51 words: a sequence of steps that
reads as one procedure. That is what the one-sentence allowance is for.

## 2. Repetition (judgment; the gate prints hints)

The gate prints `near_duplicate_pairs` and `repeated_phrases` without failing on them. The final
repeats topic phrases too: "testing and examination … on-site" appears several times, and that is
fine. What the editor did cut, counted on both texts:

| Phrase or pattern | Revision 5 | Final |
|---|---|---|
| "remote channel" | 5 | 0 |
| "digital channel" | 3 | 0 |
| "manual vs digital intake" (primary keyword) | 4 | 2, the H1 and one H2 |
| "at or around the" (appointment / visit) | 5 | 3 |
| "depends on" | 8 | 5 |
| "structured" | 9 | 6 |
| The same set of operational problems listed | intro, short answer, decision framework | once, as decision-framework bullets |
| Repeatability sentence in the body and again, near verbatim, in the FAQ | yes | no |

Rules drawn from it:

- **A phrase you liked is not a refrain.** "a remote channel can carry" three times is a verbal
  tic. The final says "can be completed remotely" and then names the steps.
- **List a set of problems once,** in the section that acts on it. The intro names the problem in
  a sentence; the decision framework carries the list.
- **The primary keyword lives in the H1 and one H2.** Prose uses the plain words.
- **An FAQ answer rephrases the body, shorter, and links.** It does not paste the body sentence.
  An FAQ whose question a body section already settles is cut: the EEOC question went, and its
  substance moved into the body.
- **Two consecutive paragraphs making one point become one.** Revision 5 had two paragraphs after
  the comparison table, one from each review round. The final has one paragraph of three
  sentences: what manual intake is good at, what digital intake is good at, what decides.

## 3. No sentences about the page

| Revision 5 | Final |
|---|---|
| Each row is a dimension a program can check for itself. | The capture method is one part of the comparison. Set-up, ongoing staff work, access, integration, and exception handling also affect the choice. |
| Side by side, the two models run the same steps in a different place and order. | The steps are similar; their timing and location change. |
| The operational difference sits in the fourth row: a structured pre-appointment path can surface exceptions before the visit instead of during it, while tests and the examination stay on site under both models. | Completing intake early gives the program time to identify missing information before the person arrives, provided the process includes the necessary validation rules. Testing and examination continue on site. |
| The comparison gets confusing when the occupational health intake process is treated as the whole of screening. | Occupational health screening consists of three phases. |
| Two diligence questions sit alongside the numbers: | Cut, together with the list and the metrics table. |

A lead-in to a table says something about the subject, never about the table.

## 4. No aphorisms, slogans or verdict headings

| Revision 5 | Final |
|---|---|
| H2: The intake step is where screening programs lose time | H2: Where manual intake can slow occupational health screening |
| Framed as manual vs digital intake, that sequence sounds like a software preference; inside a screening program it is an operations question about a fixed appointment slot. | Moving eligible steps online changes when the record becomes available and how much work remains inside the appointment. |
| Choosing between manual vs digital intake decides a method. It never decides a candidate. | Cut. The paragraph now ends on "Requirements in other jurisdictions vary." |
| **Neither method wins outright.** Manual intake combines data collection with the on-site visit. Digital intake moves eligible steps before the appointment. | **How the methods differ.** Manual intake provides immediate in-person support, while digital intake makes eligible information available before the appointment. |
| The useful question about any measurement method is: accurate enough for which decision? | What counts as adequate performance depends on how the measurements will be used. |
| Two questions decide the method: … | The choice turns on two questions: … |

- **The reframe move survives as a statement.** `about-me.md` (amended the same day) keeps the
  idea. The quoted question belongs only in a piece about accuracy itself.
- **A heading describes; it does not assert a finding.** Hedge it ("can slow") or make it plain.
- **End a paragraph on information.** A closing line written for rhythm is the first thing cut.

## 5. Plain subject, plain verb, hedge at the end

- **The system that does the work is the subject.** "The program's intake system handles
  questionnaire collection." "FitXpress provides remote body measurement within pre-appointment
  intake." "The reviewing provider assesses the record and makes any determination required by
  the program."
- **A boundary names who owns the decision.** "FitXpress supplies body-measurement data for
  clinician review; clearance, eligibility, and fitness-for-duty determinations remain with the
  responsible professionals." Revision 5: "…it does not make clearance, eligibility or
  fitness-for-duty determinations."
- **A hedge is one clause at the end of the sentence it qualifies.** "Moving eligible steps before
  the visit can reduce in-appointment collection and transcription, although the result varies
  with completion rates, fallback volume, integration quality, and the causes of existing
  rescreens." Revision 5 spent a separate sentence on it, "The effect depends on completion
  rates, …".
- **Fewer names for the same person.** Revision 5 used "candidate", "worker" and "the person". The
  final introduces "the candidate or employee" once and then mostly says "the individual".
- **A limitation gets its own short paragraph and its consequence.** Three sentences: the limit,
  when it matters, what the program needs. The disability limitation from the final is approved
  (Vadim, 2026-09-11): `accuracy-formulations.md` §5 and `proof-points.md`, Training data.

## 6. Punctuation

- **Serial comma, always.** Revision 5 had 3 lists with it and 23 without. The final has 24 with
  it and 2 without: "testing, examination, and clinical review".
- **A semicolon joins two short, parallel clauses** ("The steps are similar; their timing and
  location change."). Never a third clause, never inside an inventory.
- "therefore" as a parenthetical is fine: "The program, therefore, needs a documented manual
  alternative."

## 7. Format of a comparison or workflow cluster article

For `seo-planner`, FitXpress comparison and workflow clusters. Hubs and Type A use-case
deep-dives keep their templates in `blog-style-guide.md` §9.

1. **H1:** `<Topic>: A Workflow Comparison`. Keyword, then a plain descriptor; not "Which Method Fits Which Workflow".
2. **Opening H2,** hedged and descriptive, with `(Cover) - Concept` directly under it.
3. **Intro in four short paragraphs:** the concrete scene in two sentences; one sentence on what changes when steps move; what competes for the appointment time; "The choice turns on two questions: …" with the hub link.
4. **`**Scope note.**`** as a bold-label paragraph (not a blockquote, not italics), four or five short sentences. It carries the product boundary. A cluster article whose hub owns the "What FitXpress does not do" section has no such section of its own (Review 1 item 1 on this article); the scope note and one boundary sentence in "Where FitXpress fits" carry it.
5. **"Short answer" H2:** 4-5 bullets, each a bold label and one or two sentences. A label may be a question.
6. **Phases H2:** one sentence naming the phases, then bold-label bullets (not a numbered list), `(Image 1) - Concept`, then the external evidence paragraphs.
7. **One comparison table** with a bold header row, 11 rows at most. Merge rows that say the same thing. Revision 5 had 14: "Fallback availability" folded into "Exceptions and fallback", "Ongoing labor" into the set-up row, and "Relationship to the wider workflow" was cut because the phases section owns it. A two-sentence lead-in before it, a three-sentence reading after it.
8. **A second small table** only when it shows sequence ("How the workflows differ", five rows), with a one-line lead-in and a two-sentence reading.
9. **Decision framework H2** with three H3s, "Manual intake fits when" / "Digital intake fits when" / "A hybrid model fits when", 3-5 bullets each. Every bullet is a complete sentence of about ten words.
10. **The regulatory paragraph sits in the body,** in short sentences, ending on the jurisdiction caveat. Not an FAQ.
11. **A limitation paragraph, then how to pilot** in three sentences. No metrics table, no list of diligence questions.
12. **"Where FitXpress fits":** `(Image 2) - Concept`, three short sentences on what it provides, the evidence in the short forms of `accuracy-formulations.md` §5, then the privacy paragraph in four sentences.
13. **FAQ:** three H3 questions, answers of two or three sentences, none repeating a body section.
14. **Next steps:** two sentences. The second starts with "Then" and carries the CTA link.

**Visuals.** A cover and at most two inline images, marked in the text as `(Cover) - Concept` and
`(Image N) - Concept`, with an Illustrations table beside the plan: `Name | Placement | Concept`.
The editor cut four proposed visuals because each repeated a table or a list already on the page.
A visual shows something the text does not.

**Length.** About 1,900 prose words for this format, so plan the target there. The 2,200-4,200
range in `blog-style-guide.md` §2 is for Types A-C.

## 8. Reviewer text: verbatim fixes the claim, not the sentence

Revision 5 carried 22 scripted reviewer replacements, and its own editor's self-check called the
FitXpress section "assembled rather than written". Two cases show what that cost:

- Review 2 item 6 proposed the privacy paragraph as five short sentences. We declined two of its
  sub-points and, with them, the shape, and shipped one 50-word inventory. The final uses four
  short sentences. Declining part of a review's substance is no reason to keep a long shape.
- Review 2 item 4 supplied the hybrid-model paragraph, applied verbatim as two long sentences. The
  final turned it into three bullets under "A hybrid model fits when".

When a review row says verbatim, keep its **claim, figures, hedge and boundary** word for word. The
sentence shape is ours to fix: split a reviewer sentence over 25 words, and record the split in
`changes_summary`. Never merge two reviewer sentences into a longer one.

---

## Decided by Vadim, 2026-09-11

The final departed from repo canon on four points. Vadim's calls:

- **Medical device:** the final's direct form, **"FitXpress is not a medical device."**, everywhere.
  "Positioned as" has no licensed exception any more (`editorial-guardrails.md` #6,
  `detect-ai-tells.py`).
- **Compliance wording** (BAA "available on request", output retention, the dropped "processes no
  personal identifiers" and 30-day photo window): `compliance.md` is **not** changed for now. New
  drafts keep its wording. *Superseded 2026-09-18: `compliance.md` was rebuilt from the live trust
  FAQ (Vadim), and new drafts take that wording.*
- **Disability limitation:** approved and added to `proof-points.md` and
  `accuracy-formulations.md` §5.
- **Primary keyword in the first paragraph:** no longer required. `article_lint.py` gate 7 fails
  only on the H1 and the H2s, and reports the first paragraph as information.
