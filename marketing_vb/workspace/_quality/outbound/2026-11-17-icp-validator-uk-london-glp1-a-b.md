---
qc_date: 2026-11-17
agent: icp-validator
artifact: 2026-11-17-uk-london-glp1-connections + 2026-11-17-uk-london-glp1-pharmacies (people-validated.csv, icp-validation-summary.md, decisions.md)
track: outbound
artifact_type: validation
total_score: 16/20
status: good
coordinator_review: done
---

# QC — icp-validator — A (connections) + B (pharmacies), 2026-11-17

Scores: Adherence 4/5 · Factual accuracy 4/5 · Brand & tone 3/3 · Format 2/3 · Output quality 3/4 = **16/20**.

Top issues: (1) concentration across A+B not managed (Reset Health 11, DCA 13, SheMed 7, Numan 7); (2) `compact` drops headlines whose company differs from the group (Hyatt → Reset Health, Ravech → Rapid Health; A's connection export has no company-page column) — code fix candidate; (3) big-retail / logistics rule applied inconsistently (Lepley, Halsall, Rizwan Ali PASS vs Caplan, Lodge WEAK; coordinator's pool D promotions against its own rule).

## Coordinator review
- agreement: agree; applied every must-drop, every trim and both promotions.
- top_issue: wrong-company rows in SEND (Hyatt, Ravech, Wilkinson, Kamran Raja).
- dropped (A): Catherine Hyatt, David Ravech, Adrian Wilkinson, Rizwan Ali, Andrew Caplan, Matt Webster, Jamaal Khan, Duncan Ross, Will Lunt, Darren Jalink, Rachel Dreycroft, Kelly Morrall, Laura Newson, Raquel Sanchez Windt, Zoe Sullivan, Deepali (Gambhir) Dixon, Kamran Iqbal, Biran Pankhania, Ifrah Asmat, Paulet Chika Adimonye, Tatjana K., Hina Sarwar.
- dropped (B): Kamran Raja, Jennifer Kaur, Paul Halsall, David Lepley, Ling Chow.
- promoted (A): Sophie Kanani (Acharya), Alyza Gines.
- follow-ups: Well Pharmacy has nobody in SEND → Hlib's Sales Nav pull; `compact` headline/company mismatch flag → proposal for Vadim, not changed tonight.
