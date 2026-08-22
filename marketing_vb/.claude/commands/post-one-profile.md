---
description: Writes ONE social profile's post for a ready SEO article, then assembles the digest if it is the last profile left
argument-hint: "<article-slug> <profile-id>"
---

Write the post for profile `$2` from article `$1`.

## Why this command exists (do not "helpfully" widen it)

`/post-from-article` does all active profiles in a single run. On 2026-08-21 that was job
#90: one run, 206 turns, 29 minutes — and it exhausted the Claude usage window that the
conductor shares with Vadim's own interactive sessions. Every retry afterwards got 2 turns
before hitting the wall again, so the last 3 posts were finished by a fallback coder.

This command is the one-profile unit that `mvb-run.py posts <slug>` now enqueues as N
separate conductor jobs. The point is that each job is small, ends, and BANKS its post —
so an exhausted window costs you the profiles not yet started, never a half-finished run.

So: **write exactly one profile — `$2` — and nothing else.** Do not loop over the other
profiles because it would "save a run". That is the behaviour this command exists to undo.

## Steps

1. **Find the article source** — follow step 1 of `.claude/commands/post-from-article.md`
   verbatim, including its note about not refusing on `status:`. Report which file you took.

2. **Confirm `$2` is actually active** — read `brand-assets/social-profiles-config.md` and
   check that `$2` appears there with `posts_per_week > 0`. If it is missing or disabled,
   STOP and say so; do not substitute a different profile.

3. **Run the `post-drafter` subagent once**, with:
   - `article_path`: the source file resolved in step 1
   - `profile`: `$2`

   For any `linkedin-*` profile, `post-drafter` must read the matching section of
   `brand-assets/linkedin-post-prompts.md` first — that file wins over the config summary,
   except the two house rules that always win: **no hashtags anywhere** and **1–2 emoji max**.

4. **If `AUTO_QC_ENABLED=true`** in CLAUDE.md section 14 — run `quality-controller`:
   ```
   Use quality-controller to evaluate workspace/social/articles/$1/$2/post.md.
   Pass: agent_name=post-drafter, track=social, artifact_type=post.
   ```

5. **Assemble only if you are the last profile.** Re-read
   `brand-assets/social-profiles-config.md` for the full active list, then check which of them
   already have `workspace/social/articles/$1/<profile>/post.md` on disk.

   - **Some are still missing** → STOP here. Report: this profile is done, and list exactly
     which profiles remain. Do NOT write `review-digest.md` and do NOT touch `manifest.json` —
     a partial digest read as a finished one is how job #90's manifest ended up listing 3
     profiles while 9 posts existed on disk.
   - **All active profiles have a `post.md`** → you are last. Now do steps 5, 6 and 7 of
     `.claude/commands/post-from-article.md` verbatim (manifest, review digest, final report).
     They are deliberately not restated here so the digest format lives in exactly one file.

## Rules

- One profile per run. No parallel `post-drafter`.
- Facts come only from the article source file resolved in step 1. Invent nothing.
- `visual-brief` is **not** triggered here — only after Vadim approves the text in Telegram.
- Everything goes to files, not into the chat. Publish nothing outward.
