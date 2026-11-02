---
description: Writes ALL missing social posts for a ready SEO article in ONE post-drafter session (batch mode), then assembles the pack
argument-hint: "<article-slug>"
model: sonnet
---

Write every missing post for article `$1` in one batch, then assemble the pack.

## Why this mode exists

Measured A/B (CLAUDE.md §9 protocol, `bariatric-hub-refresh`, 2026-09-20, commit
1f2aea5, full write-up in that pack's `_ab-batch/ab-comparison.md`): one opus
post-drafter session writing all nine posts scored **18.78/20 against the fan-out's
18.00** on a full blind QC set, linted 9/9 on the first pass, and cost **$8.65** of
drafting against ~$12.6 plus nine coordinator sessions. The angle map allocated by one
head beat the fan-out's "angles already taken" relay. Vadim accepted batch as the
default on 2026-09-20; the fan-out (`mvb-run.py posts` without `--batch`) remains for
targeted single-profile re-runs.

The batch's one measured weakness: on the two soft-register company accounts
(facebook, instagram) the batch posts read slightly more technical than their briefs
want. That is what step 5's brand-check sample is for — route those findings back.

## Model

This session runs on **sonnet** (frontmatter above): every step here is dispatch.
The text is written by `post-drafter`, which carries `model: opus` in its own
frontmatter and is untouched by this setting.

## The rule that governs every step

**Anything mechanical goes through a script.** `scripts/social_pack.py` and
`scripts/post-lint.py` own source resolution, prompt assembly, gating, manifest,
digest and report. Do not reimplement any of it, and do not "just check" with a
directory listing when a subcommand answers the same question.

## Steps

1. **Prepare the pack (idempotent).**

   ```bash
   python3 scripts/social_pack.py source $1
   python3 scripts/social_pack.py brief $1
   ```

   Stop only if: `source` exits non-zero, or the brief's HUMAN section is still the
   empty template on a fresh pack — in that case fill the two HUMAN sections first
   (claims discipline in the live wording, and the article's real visual assets),
   exactly as `/post-one-profile` step 1 describes. Do **not** refuse on the
   article's `status:` field.

2. **Build the batch assignment.**

   ```bash
   python3 scripts/social_pack.py batch-prompt $1 --write
   ```

   This writes `workspace/social/articles/$1/_batch-prompt.md` covering ONLY the
   profiles that have no `post.md` yet (first run = all active, re-run = the gaps),
   and prints which. If it says the pack is complete, skip to step 6.

3. **Run `post-drafter` ONCE, and wait for it.**

   Spawn the `post-drafter` subagent with exactly this prompt:

   > Read the file `workspace/social/articles/$1/_batch-prompt.md` and execute it
   > exactly. It is your complete assignment: the run brief, the article of record,
   > the house rules and every profile section are inside it. Read nothing else
   > first. Save every post to the "## Save to" path its section names. When every
   > file is saved, reply with the one-line-per-profile summary the assignment asks
   > for.

   **Do not end your session while ANY subagent is running — the drafter, a
   brand-checker, a QC run.** Three times on 2026-09-20 a posts job went `done`
   mid-flight: #136 and #158 "waiting for the drafter" with no post on disk, and
   #160 "kicked off 7 brand-checks in the background, I'll resume" — the session
   ended, every child died with it, and the queue recorded success over unfinished
   work. There is no "later" for this session: nothing resumes it. Spawn, WAIT for
   the result, act on it, and only then move on. Do not "schedule a check-in", do
   not describe work as continuing in the background. A Stop hook will refuse to
   let this session end while an expected `post.md` is missing or the pack's
   manifest is older than the newest post.

4. **Gate mechanically — ONLY the profiles this batch wrote.**

   For each profile listed in step 2's output (they are also the `===== PROFILE`
   sections of `_batch-prompt.md`):

   ```bash
   python3 scripts/post-lint.py $1 <profile> --summary --gate
   ```

   Exit 1 → send the failing profiles back to `post-drafter` in ONE follow-up call:
   quote the lint lines per profile, name the file paths to rewrite, do not rewrite
   the text yourself. Two rewrite rounds maximum, then record the remaining fails in
   your summary and continue. Warnings are informational.

   **Never `--all --gate` here.** On a top-up run the pack contains posts that
   shipped under OLDER rules; `--all` hard-fails them retroactively and sending
   those to the drafter rewrites published posts. Job #160 (2026-09-20) did exactly
   that to five shipped glp-1 LinkedIn posts before this rule existed. A shipped
   post is redrafted only when someone deliberately removes its post.md.

5. **Brand voice, sampled.**

   ```bash
   python3 scripts/social_pack.py qc-plan $1
   ```

   Run `post-brand-checker` on each profile in `qc`, plus every profile whose lint
   gate failed in step 4. FAIL → one rewrite round through `post-drafter` with the
   checker's reasons. Use `post-brand-checker` (mvb-social), never the bare
   `brand-checker`.

6. **Quality control, per the same plan.** For each profile in `qc`:

   ```bash
   python3 scripts/social_pack.py qc-prompt $1 <profile>
   ```

   Pass the output verbatim to `post-quality-controller` (mvb-social) — never the
   bare `quality-controller`. Then add your one-line `coordinator_review` to each
   report (agreement + top_issue), per CLAUDE.md §14.

7. **Video: one short HyperFrames clip for the pack** (added 2026-11-02). It is
   written from the FINAL posts, so it runs after steps 4-6. Skip this step when
   `python3 scripts/social_video.py status $1` shows both `reel` and `feed` under
   `formats` with `"stale": false`.

   ```bash
   python3 scripts/social_video.py prompt $1 --write
   ```

   Spawn `post-drafter` once more, with exactly this prompt, and WAIT for it:

   > Read the file `workspace/social/articles/$1/_video-prompt.md` and execute it
   > exactly. It is your complete assignment: the rules, the output shape and the
   > pack's final posts are inside it. Read nothing else first. Save the JSON to the
   > path its "## Output" section names, then reply with the one line it asks for.

   ```bash
   python3 scripts/social_video.py lint $1
   python3 scripts/social_video.py render $1
   ```

   Lint exit 1 → one follow-up to `post-drafter` quoting the lint lines (two rounds
   maximum). `render` takes one to two minutes: run it in the foreground and wait. It
   commits and pushes the two MP4s to the private repo itself (`private_repo` in its
   output); do not run git for them. A
   `check failed` result means a line does not fit its card: send the findings to the
   drafter once, then render again. The video never blocks the pack: after two failed
   rounds, record what failed in your summary and go on to step 8.

8. **Assemble.**

   ```bash
   python3 scripts/social_pack.py profiles $1
   ```

   `missing` must be empty — if it is not, something in steps 3-4 did not land;
   go back, do not assemble a partial pack. Then:

   ```bash
   python3 scripts/post-lint.py $1 --all --summary
   python3 scripts/social_pack.py manifest $1 --write
   python3 scripts/social_pack.py digest   $1 --write
   python3 scripts/social_pack.py report   $1 --write
   ```

   Do not write any of the three by hand. There is no visual-brief step (removed
   2026-09-20): the designer builds each visual from the post's Design tip in the
   digest. The digest and the report pick up the video from `_video/` on their own.

   When the report says `Video: rendered ✅`, send the two MP4s to Vadim:

   ```bash
   python3 scripts/social_video.py notify $1
   ```

9. **Commit** (Vadim, 2026-11-02: every pack ends in git, as articles do).

   ```bash
   python3 scripts/social_pack.py commit $1
   ```

   It commits and pushes this pack's folder and nothing else (never run `git add -A`
   or any git command yourself here: other jobs keep uncommitted work in the same
   checkout). `pushed` or `unchanged` is done; `committed, push failed` or any other
   status goes in the FIRST line of your summary. The commit hash goes in the summary.

10. **Final self-check before your summary** — the same check the Stop hook makes:
   every active profile has a `post.md` and `publish-report.md` says N/N. Report the
   angle map, lint state, QC scores, the video's hook and render state, the commit
   hash, and anything you left unresolved.
