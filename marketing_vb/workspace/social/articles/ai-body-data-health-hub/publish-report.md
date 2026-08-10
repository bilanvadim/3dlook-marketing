# Publish Report — AI Body Data for Health Hub

**Date:** 2026-07-20
**Article:** AI Body Data in Healthcare: A Guide to Verified Body Measurement Across Health Programs
**Product:** FitXpress (100%)
**Pipeline:** social-planner → post-drafter (×9) → social-editor → social-publisher

---

## Status Table

| # | Profile | Platform | Status | Body Chars | Format | Regional Check | Brand Check |
|---|---------|----------|--------|------------|--------|----------------|-------------|
| 1 | twitter-company | Twitter | ✅ Ready | ~256 | Text | N/A (global) | ✅ |
| 2 | instagram-company | Instagram | ✅ Ready | ~950 | Text+photo | N/A (global) | ✅ |
| 3 | facebook-company | Facebook | ✅ Ready | ~1,120 | Text+photo | N/A (global) | ✅ |
| 4 | linkedin-company | LinkedIn | ✅ Ready | ~1,680 | Text+photo | N/A (global) | ✅ |
| 5 | linkedin-katerina | LinkedIn | ✅ Ready | ~1,280 | Text+photo | UK-only ✅ | ✅ |
| 6 | linkedin-vadim | LinkedIn | ✅ Ready | ~1,380 | Text+photo | N/A (global) | ✅ |
| 7 | linkedin-nick | LinkedIn | ✅ Ready | ~1,240 | Text+photo | US-only ✅ | ✅ |
| 8 | linkedin-olena | LinkedIn | ✅ Ready | ~1,290 | Text+photo | EU/GDPR ✅ | ✅ |
| 9 | linkedin-katya | LinkedIn | ✅ Ready | ~1,400 | Text+photo | Israel-only ✅ | ✅ |

---

## Validation Results

### 1. File Completeness — PASS ✅
- All 9 profile directories have `post.md` ✅
- All files have correct YAML frontmatter (`profile`, `platform`, `date`, `product`) ✅
- No missing files ✅

### 2. Length Validation — PASS ✅
- All posts within platform-specific character limits ✅
- Shortest: twitter-company (~256 chars, target 240-260) ✅
- Longest: linkedin-company (~1,680 chars, target 1200-1800) ✅

### 3. Brand Hard Bans — PASS ✅
- Zero claims of: diagnoses, makes decisions, replaces clinician, guarantees compliance ✅
- Zero banned words: leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm, groundbreaking, cutting-edge, game-changer ✅
- Zero banned phrases: "In today's fast-paced world", "Have you ever wondered", triple parallelisms, em-dash rhetoric ✅
- Zero references to: "reader/audience/below", "this article/guide", "by hand" → manually, "plus" as connector ✅

### 4. Regional Lens — PASS ✅
- Katerina: UK-only (MHRA, NHS, UK Meds), no US/EU references ✅
- Nick: US health-tech, no EU regulatory ✅
- Olena: GDPR/EU, no US context ✅
- Katya: Israeli ecosystem, no EU/US specifics ✅

### 5. Format Distribution — PASS ✅
- 0 carousels (max 3 allowed) ✅
- 9 text+photo posts ✅
- No format conflicts ✅

### 6. Cross-Profile Uniqueness — PASS ✅
- All 9 hooks are distinct ✅
- All 9 primary insights are distinct ✅
- No duplicate opening lines ✅
- No duplicate central claim ✅

### 7. POV Enforcement — PASS ✅
- Company accounts: 3rd person or "we" ✅
- Personal accounts: 1st person ✅

---

## Artifacts Produced

| File | Stage | Description |
|------|-------|-------------|
| `posting-plan.md` | Stage 1 | Claims table + profile assignments + angle map |
| `{profile}/post.md` ×9 | Stage 2 | Individual posts with design tips |
| `all-posts-compiled.md` | Stage 3 | All posts compiled + cross-profile audit |
| `manifest.json` | Stage 4 | Machine-readable publish manifest |
| `publish-report.md` | Stage 4 | This file — human-readable status report |

---

## Ready for Review

**ready_for_review:** ✅ true

All 9 posts have passed brand checks, regional enforcement, length validation, and cross-profile deduplication. No issues remain.

**Next step:** Visual brief for design team (9 design tips ready per post).
