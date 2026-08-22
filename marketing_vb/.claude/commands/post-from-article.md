---
description: Creates posts for all active social profiles based on a ready SEO article
argument-hint: "<article-slug>"
---

Create posts for all active profiles based on article $1.

## Steps

1. **Find the article source** in `workspace/seo/articles/$1/`, in this order:
   - `publish-package.md` — the canonical source when it exists;
   - otherwise the newest final draft: `draft-v5-revision1.md` → `draft-v4-publisher-final.md` → `draft-v3-final.md` → `draft-v3-edited.md`.

   Nothing usable in the directory (or no directory) — STOP, notify Vadim.

   **On approval — read this before refusing.** This step used to say «if `status` is not
   `approved_for_publish` — STOP». That check could never pass: the SEO pipeline never writes
   that value. Every `publish-package.md` in the workspace carries `ready_for_review`,
   `revision_ready_for_review` or `awaiting_final_approval` (verified across all of them
   2026-08-17), so the rule refused every article that has ever existed here — which is part of
   why social runs got briefed as free-form prose instead of through this command.
   The approval gate is Vadim asking for the run (Telegram «Пости &lt;slug&gt;», or a manual
   `/post-from-article`) plus his approval of the finished digest — see CLAUDE.md §9. So:
   **report** the article's `status:` and the file you took as the source in your final message,
   and do not refuse on status. Two cases still STOP and ask: the source has no article body
   (a stub under ~3000 chars), or its frontmatter says the text is mid-rewrite with no readable
   version on disk.

2. **Get the profile list** from `brand-assets/social-profiles-config.md` (CLAUDE.md section 5
   summarises it). Only include profiles with `posts_per_week > 0`.

3. **For each profile sequentially** run the `post-drafter` subagent with:
   - `article_path`: `workspace/seo/articles/$1/publish-package.md`
   - `profile`: current profile

4. **If `AUTO_QC_ENABLED=true`** in CLAUDE.md section 14 — after each `post-drafter` run `quality-controller`:
   ```
   Use quality-controller to evaluate workspace/social/articles/$1/{profile}/post.md.
   Pass: agent_name=post-drafter, track=social, artifact_type=post.
   ```

5. **After all profiles** — finalise `workspace/social/articles/$1/manifest.json`.

   **The schema is not defined here.** It is defined once, in the "Manifest — КАНОНІЧНА СХЕМА"
   section of the `social-publisher` agent. Read it and conform to it — do not infer the shape
   from a neighbouring article's manifest. This step used to say only "confirm it is updated
   with `ready_for_review: true` and QC scores", which defined nothing, so each run copied
   whatever a nearby file happened to look like while `post-drafter` and `social-publisher`
   wrote a different, older shape. That is how the 2026-08-21 run ended up with a manifest in
   the obsolete `drafts:` form listing 3 profiles while 9 posts sat on disk.

   Concretely: every active profile present in `profiles` with the required fields, anything
   skipped in `profiles_skipped` with a reason, QC scores where QC actually ran, and
   `ready_for_review: true` **only** once every active profile is `status: ready`.

6. **Assemble the review digest** — read all finished `post.md` files and write to `workspace/social/articles/$1/review-digest.md`:

   ```markdown
   # Review digest — {slug}

   Article: `workspace/seo/articles/{slug}/publish-package.md`
   Date: {YYYY-MM-DD}
   Profiles: N

   ---

   ## twitter-company

   {full post text}

   **CTA:** ...

   > **Design tip**
   > Article visual: ...
   > Format: [text | text + photo | carousel | infographic | lead magnet | poll | screenshot]
   > Adaptation: ...
   > Keep: ...

   ---

   ## {profile}

   {full post text}

   **CTA:** ...

   > **Design tip**
   > Article visual: ...
   > Format: [text | text + photo | carousel | infographic | lead magnet | poll | screenshot]
   > Adaptation: ...
   > Keep: ...

   ---
   ```

   Order: company accounts first (twitter → instagram → facebook → linkedin-company), then personal LinkedIn alphabetically.
   Include only profiles with a finished `post.md`.
   Copy the design tip verbatim from the `### Design tip` block in each `post.md`.

7. Report: "N posts ready for article $1. Digest: `workspace/social/articles/$1/review-digest.md`. Telegram bot will send to Vadim for approval."

## Rules

- **Do not run post-drafter in parallel** — one profile at a time, clean context.
- If a profile has `posts_per_week = 0` or is disabled — skip it, note it in the final report.
- `visual-brief` **is not triggered here** — only after Vadim approves the text in Telegram.
