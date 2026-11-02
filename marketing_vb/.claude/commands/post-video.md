---
description: Adds the short HyperFrames video to a social pack that already has its posts (copy from the final posts → lint → render → digest → Telegram)
argument-hint: "<pack-slug>"
model: sonnet
---

Add the pack's short video to `$1`. New packs get it inside `/post-batch` (step 7);
this command is for packs whose posts already exist.

## Model

This session runs on **sonnet**: every step here is dispatch. The words are written
by `post-drafter` (opus in its own frontmatter), the rest by
`scripts/social_video.py`. Do not write or edit `video.json` yourself, and do not
hand-edit the template's filled copies: the template is
`brand-assets/video/stat-reel.html`.

## Steps

1. **Is there anything to do?**

   ```bash
   python3 scripts/social_video.py status $1
   ```

   Both `reel` and `feed` under `formats` and `"stale": false` → the video is current:
   go to step 5 only if Vadim asked for it to be sent again, otherwise stop and say so.
   `copy` present but stale or unrendered → go to step 3.

2. **The copy.**

   ```bash
   python3 scripts/social_video.py prompt $1 --write
   ```

   Spawn `post-drafter` with exactly this prompt and WAIT for it:

   > Read the file `workspace/social/articles/$1/_video-prompt.md` and execute it
   > exactly. It is your complete assignment: the rules, the output shape and the
   > pack's final posts are inside it. Read nothing else first. Save the JSON to the
   > path its "## Output" section names, then reply with the one line it asks for.

3. **Gate and render.**

   ```bash
   python3 scripts/social_video.py lint $1
   python3 scripts/social_video.py render $1
   ```

   Lint exit 1 → one follow-up to the same `post-drafter` quoting the lint lines (two
   rounds maximum). `render` takes one to two minutes: foreground, wait for it. It
   commits and pushes the MP4s to the private repo itself (`private_repo` in its
   output); do not run git for them. A
   `check failed` result means a line does not fit its card: send the findings to the
   drafter once, then render again.

4. **Re-assemble the pack** so the digest and the report carry the video:

   ```bash
   python3 scripts/social_pack.py manifest $1 --write
   python3 scripts/social_pack.py digest   $1 --write
   python3 scripts/social_pack.py report   $1 --write
   ```

5. **Send it.**

   ```bash
   python3 scripts/social_video.py notify $1
   ```

6. **Commit.**

   ```bash
   python3 scripts/social_pack.py commit $1
   ```

   It commits and pushes this pack's folder and nothing else (never run `git add -A`
   or any git command yourself here: other jobs keep uncommitted work in the same
   checkout). `pushed` or `unchanged` is done; `committed, push failed` or any other
   status goes in the FIRST line of your summary. The commit hash goes in the summary.

7. **Summary:** the hook, which post's angle it came from, both durations, lint and
   render state, the commit hash. Read `_video/reel-sheet.jpg` (one frame per card) before you write it
   and say if any card looks wrong.
