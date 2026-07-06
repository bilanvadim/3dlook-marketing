---
description: Creates posts for all active social profiles based on a ready SEO article
argument-hint: "<article-slug>"
---

Create posts for all active profiles based on article $1.

## Steps

1. **Find the publish-package.md** for the article:
   `workspace/seo/articles/$1/publish-package.md`
   If the file is not found — STOP, notify Vadim.
   If `status` in frontmatter is not `approved_for_publish` — STOP, notify that the article hasn't been approved yet.

2. **Get the profile list** from CLAUDE.md section 5. Only include profiles with `posts_per_week > 0`.

3. **For each profile sequentially** run the `post-drafter` subagent with:
   - `article_path`: `workspace/seo/articles/$1/publish-package.md`
   - `profile`: current profile

4. **If `AUTO_QC_ENABLED=true`** in CLAUDE.md section 14 — after each `post-drafter` run `quality-controller`:
   ```
   Use quality-controller to evaluate workspace/social/articles/$1/{profile}/post.md.
   Pass: agent_name=post-drafter, track=social, artifact_type=post.
   ```

5. **After all profiles** — confirm that `workspace/social/articles/$1/manifest.json` is updated with `ready_for_review: true` and QC scores.

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
