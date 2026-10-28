# Log: clinical trials landing

## 2026-10-28: page-builder review of three drafts (Vadim: «в слаці маркетинг Ніка скинула драфт клінікал тріалс. почитай та запусти пейдж білдера з оцінкою»)

- Source: Slack #marketing (C0C0TBSM90E), thread 1793092031.104189, 2026-10-27 09:07 UTC. Nika: first draft of
  the clinical trials landing, two versions, no clinical trial clients in the CRM, "one of the weakest pages for
  me". Files `fitxpress-clinical-trials-landing-v3.html` (F0CC9DQFXLK) → `nika-v3-2026-10-27.html` and
  `fitxpress-clinical-trials-landing-v2.html` (F0CC9DQFN75) → `nika-v2-2026-10-27.html`.
- Same thread, 09:11 UTC: Vadim posted the hub article link.
- Same thread, 15:17 UTC: Asselya ran both through ChatGPT with the keyword map and guardrails, picked v2, ten
  changes. File `fitxpress-clinical-trials-landing-v4.html` (F0CCCQ1JMJP) → `asselya-v4-2026-10-27.html`.
- Text extracts: the `.txt` files beside each HTML.
- Checks run: kit word count, FAQ count, you/your, Yoast lengths, schema, detector `--channel page`, live
  `/pricing/` (still "scans" on 10-28), live hub title, form id, hero at 1280×800 and layout at 375 px (v2, v4),
  fact check against `proof-points.md`, `compliance.md`, `tech-spec.md`, content plan Hub 7, keyword map §8.
- `gate-reports.md`, `fact-sheet.md` written. Primary-source check of the third-party figures by a research
  subagent → `sources-problem-block.md`.
- Primary-source check done (`sources-problem-block.md`): FDA "not standardized" verbatim but only one of FDA's
  three reasons; DXA/MRI "expensive" correct but joined from two sections ("representative sample", "DXA or a
  suitable alternative"); "calibrated scale" not in the guidance; 30-45% attrition correct (Khera 2016, five older
  drugs) but not linked to visits, STEP 1 94.3% completed; BELIEVE 92.8 / 71.8 superseded by Nature Medicine 2026
  (92.3 / 71.1, DXA, phase 2); DHT guidance final Dec 2023 ("fit-for-purpose"); ICH E6(R3) adopted Jan 2025.
  Usable pain for the between-visits angle: home weight accepted with V&V (FDA DHT §IV.D.2), waist a secondary
  endpoint (EMA 2016), self-measured waist overestimated by 5.98 cm (Contardo Ayala 2014, n = 622).
- Blind judges round 1 (fresh subagents, one per draft): A (Nika v3) 48, B (Nika v2) 52, C (Asselya v4) 46.
  Hard fails: A and B unsourced iOS 15 / "2 cm" + placeholders; C placeholder + no "not a medical device".
  Lowest: sales argument (A, C), claims discipline (B). JSONs `judge-round-1-*.json`.
- Review for Nika in Russian: `review-2026-10-28-nika-ru.md` (base = B + Asselya's edits, new problem block in
  EN, structure to 1,100-1,600 words, 5 FAQ). Not sent: waits for Vadim's go and his calls on the hero buyer
  (DCT platform vs sponsor) and on rewriting `fx-clinical-trials.md`.
- 2026-10-28, Vadim's answers: «1. для платформ 2. ні 3. так». Hero for DCT platforms; `fx-clinical-trials.md`
  stays as is; send the review and commit. Review, `gate-reports.md` and the landing-map row updated.
