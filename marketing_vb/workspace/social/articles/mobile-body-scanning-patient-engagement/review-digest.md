# Review Digest — How Mobile Body Scanning Improves Patient Engagement

**Article:** How Mobile Body Scanning Improves Patient Engagement
**Slug:** mobile-body-scanning-patient-engagement
**Stage:** Social-Editor (Stage 3/4) review digest
**Date:** 2026-08-17

---

## 1. Pass / Fail Summary

| Gate | Result |
|------|--------|
| Brand voice — hard bans (diagnoses, makes decisions, etc.) | ✅ PASS |
| Banned words (leverage, utilize, harness, robust, seamless, etc.) | ✅ PASS |
| Banned phrases (this article, reader, audience, it's no secret, etc.) | ✅ PASS |
| AI signatures (em-dash rhetoric, "it's not just X, it's Y", triple parallel) | ✅ PASS |
| Claim currency — Revision 1 only | ✅ PASS |
| Regional lens enforcement (UK, AU, US, Continental EU, Israel+Gulf) | ✅ PASS |
| POV enforcement (3rd person company / 1st person personal) | ✅ PASS |
| Length limits | ✅ PASS (7 of 9 exact; 2 off-by-one, both inside band) |
| Format distribution (max 3 carousels) | ✅ PASS (1 used) |
| Hashtags | ✅ PASS (0) |
| Emoji (max 2 per post) | ✅ PASS (1 total: 📈 on instagram-company) |
| No named customers / scan volumes | ✅ PASS |
| Cannibalization guardrail (no GLP-1 in posts) | ✅ PASS |
| Vertical boundary (no eligibility/underwriting/fraud claims) | ✅ PASS |

---

## 2. Open Items (judgment calls, not rule breaches)

### Item 1 — Unsourced retention curve in katya design tip
**File:** `linkedin-katya/post.md`
**Section:** Design tip

**Issue:** The design tip references a retention curve "dropping after week four" —
a shape the article no longer supports. The GLP-1 discontinuation statistic
(64.8%, JAMA Network Open) was removed in Review 1, and no replacement statistic
was introduced. The post **body** is clean, but the design brief would put an
unsourced curve in front of a designer.

**Recommendation:** Replace with a neutral "week six" marker on an unlabelled
timeline. Do **not** draw a drop-off curve without an approved data source.

---

### Item 2 — Phrase-level reuse across LinkedIn posts
**Files:**
- `linkedin-company/post.md`
- `linkedin-katerina/post.md`
- `linkedin-nick/post.md`
- `linkedin-katya/post.md`

**Issue:** Two article phrases appear verbatim in **two** and **three** posts
respectively:

1. "Motivation fades when progress stays invisible" — appears in linkedin-company §1 and linkedin-katerina §2 (verbatim, not paraphrased).
2. "30, 60, and 90-day cycles" — appears in linkedin-company §1, linkedin-katerina §2, and linkedin-nick §1.

**Context:** These posts are clean against uniqueness rules (distinct hooks,
distinct primary insights). The reuse is of the **article's own bridge framing**,
not headline copy. The overlap risk is company-page and CEO audiences
(linkedin-company + linkedin-katerina).

**Recommendation:** Option A (preferred for speed) — paraphrase one of the two
in linkedin-katerina to avoid verbatim repetition with the company page. Option
B — leave as-is; the overlap is defensible because the audiences are reached
at different cadences and the posts open on distinct hooks.

---

### Item 3 — Single emoji on instagram-company
**File:** `instagram-company/post.md`

**Issue:** One emoji 📈 is used. This is **within** the CLAUDE.md §6 ceiling
(1-2 per post), and the post is for Instagram where a progress glyph reads
naturally. Flagged for full transparency rather than edited.

**Recommendation:** Keep — no remedial change needed.

---

## 3. Pack-Hygiene Items

### Item 4 — Missing manifest.json field
**File:** `manifest.json`

**Issue:** `manifest.json` lists 1 of 9 drafts in the `source_drafts` field.
All 9 finalised post files exist on disk, but only one is referenced in the
manifest.

**Recommendation:** Add all 9 `post.md` paths to `source_drafts` in `manifest.json`.

### Item 5 — No staging date in manifest.json
**File:** `manifest.json`

**Issue:** No `staging_date` or `social_editor_completed` field.

**Recommendation:** Add `social_editor_completed: 2026-08-17` and leave
`staging_date` blank until Vadim approves.

---

## 4. Recommendation

**Status: READY for Stage 4 (Social-Publisher) / Vadim's Telegram review.**

The 9 posts are clean against every mechanical gate. The three open items above
are judgment calls — item 1 needs a design-tip fix before any designer hand-off,
items 2 and 3 are noted for awareness. No remedial copy edits required at this
stage.

Approval needed before scheduling: Vadim (per CLAUDE.md §9 §10).
