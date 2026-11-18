---
qc_date: 2026-11-17
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-17-uk-london-glp1-connections/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-17 (London GLP-1, A + twin B)

Scores: Adherence 4/5 · Factual accuracy 3/5 · Brand & tone 3/3 · Format 3/3 · Output quality 3/4 = **15/20**.

## Top 3 (QC)
1. M1 order (company's own weight-check line, then the GPhC expectation) reads as implied non-compliance for questionnaire / self-entered / photo-step accounts; GPhC point must be optional/off for accounts with a named GPhC/MHRA/ASA matter (HeliosX, SheMed/eMed, Superdrug, HealthExpress, Rightangled, PPRX, Day Lewis, TribElle).
2. Liveness and clothing checks described as available, against roadmap.md l.17/l.19 (liveness "coming soon", Clothing Detector Q4 2026) and CLAUDE.md claims gate; 3.5% vs roadmap.md l.21 "no weight-accuracy numbers until R&D publishes the baseline" not raised.
3. No send window for A; "at your office" asks for accounts whose London office is unconfirmed; ongoing-conversation rules clash (describe the scan / never new / never imply a conversation); PillTime deal data conflicts (Closed lost new deal vs Demo 1).
Lower: DCA 47 connections → soft cap ~12; deal markers and the active-deal list are pipeline disclosure in a public repo (CLAUDE.md l.215); B tone line vs tagged accounts.

## Coordinator review
- agreement: agree with all three; QC is right that the GPhC juxtaposition is the main copy risk.
- top_issue: GPhC line next to the account's own method.
- decisions taken by the coordinator (Vadim waived checkpoints): no liveness, no clothing checks and no weight-accuracy number in copy (roadmap.md wins over the brief); all contact markers and the active-deal list removed from both public hypotheses, replaced by one rule for every account (never a first-contact frame, never a reference to a previous conversation); A gets a timing guard (no M1 after Mon 23 Nov; any M2 on/after Tue 24 Nov drops the London link and dates); "30 minutes in London" instead of "at your office" where the office is unconfirmed; DCA soft cap 12 at validation.
- fixes sent back to hypothesis-generator (same agent) on 2026-11-17.
