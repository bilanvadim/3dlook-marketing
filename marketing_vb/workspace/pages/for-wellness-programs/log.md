# Log: wellness landing

## 2026-10-28: page-builder review of three drafts (Vadim: «давай теперь все тоже по велнесу», after the clinical trials review)

- Source: Slack #marketing (C0C0TBSM90E), thread 1793092164.544279, 2026-10-27 09:09 UTC. Nika: "next page on the
  list was WELLNESS PLATFORMS", overlaps the fitness landing, the difference between the two ICPs is unclear. File
  `fitxpress-wellness-platforms.html` (F0CCK9BV2G4) → `nika-v1-2026-10-27.html`.
- 09:13 UTC: Vadim posted the wellness rewards article link. 09:24 UTC: Nika, "Updated version":
  `fitxpress-wellness-rewards.html` (F0CCDPARTV4) → `nika-v2-2026-10-27.html`.
- 15:42 UTC: Asselya, same approach as on clinical trials: repositioned on remote biometric screening for employee
  wellness programs, rewards as one use case, "use v3 as the new working version". `fitxpress-wellness-programs-v3.html`
  (F0CCP2LGC04) → `asselya-v3-2026-10-27.html`.
- Text extracts: the `.txt` files beside each HTML.
- Checks run: kit word count, FAQ, you/your, Yoast, schema, detector `--channel page`, form id, links, hero at 1280×800
  and layout at 375 px (v2, v3), live hub titles, fact check against `proof-points.md`, `accuracy-formulations.md`,
  `compliance.md`, `tech-spec.md`, use-case file, content plan Hub 5, keyword map §6, landing-map rule 7.
- `gate-reports.md`, `fact-sheet.md` written. Primary-source check of B's statistics by a research subagent →
  `sources-problem-block.md`. Blind judges on A and C launched first (no third-party figures), B after the check.
- Primary-source check done (`sources-problem-block.md`): CDC 40% = population prevalence gap and argues against
  entered height/weight → drop; KFF 2025 43% (200+ workers, offer screening) correct, "HR workload" not in source; KFF
  62% = incentives for completing, only 14% reward results; Gallup 78% = remote-capable only (May 2026); KFF 2025:
  50% of large firms with screening already allow remote completion; KFF defines screening as an in-person exam;
  Dekkers 2008: self-reported BMI −0.7, waist +1.1 cm; EEOC 30% limit vacated from 2019, no new rule.
- Blind judges round 1: A (Nika v1) 43, B (Nika v2) 41, C (Asselya v3) 46. Hard fails: A and B unsourced iOS 15 /
  "2 cm" / gender inputs (A also "4 to 12 weeks") + placeholders, B a punch triad; C none. Lowest: search (A), claims
  (B), sales argument (C). JSONs `judge-round-1-*.json`.
- Review for Nika in Russian: `review-2026-10-28-nika-ru.md`. Base = C on the approved URL and angle; from B: reward
  threshold above scan-to-scan variation, fraud block, pilot measures; A is the fitness buyer. New problem block in EN.
  Not sent yet: waits for Vadim's go.
- Side effect: Dekkers 2008 corrected the clinical trials problem card (5.98 cm → 1-6 cm range), see that log.
