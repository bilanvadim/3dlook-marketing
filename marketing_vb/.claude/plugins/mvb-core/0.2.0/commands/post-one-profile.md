---
description: Writes ONE social profile's post for a ready SEO article, then assembles the pack if it is the last profile left
argument-hint: "<article-slug> <profile-id>"
---

Write the post for profile `$2` from article `$1`.

## Why this command exists (do not "helpfully" widen it)

`/post-from-article` does all active profiles in a single run. On 2026-08-21 that was job
#90: one run, 206 turns, 29 minutes — and it exhausted the Claude usage window that the
conductor shares with Vadim's own interactive sessions.

The measurement behind the split, taken on the 2026-08-28 pack (`glp-1-market-hub`, nine
posts, session `1ee1d21a`, deduplicated by message id): 42.9M context tokens and about
$133 in total, of which the **coordinator session alone was 25.5M tokens and $55.66** —
151 requests at a median context of 206K. Not the writing. The coordination: 165 Bash
calls, 27 subagent reports, a hand-written run brief and a hand-assembled 27KB digest,
all piling into one session where every later request pays for every earlier one.

So this command is the one-profile unit that `mvb-run.py posts <slug>` enqueues as N
separate conductor jobs, four minutes apart. Each job starts from a fresh ~15K context,
ends, and BANKS its post.

**Write exactly one profile — `$2` — and nothing else.** Do not loop over the others
because it would "save a run". That is the behaviour this command exists to undo.

## The rule that governs every step below

**Anything mechanical goes through a script, not through you.** Every Bash call you make
and every file you read lands in your context and is re-billed on every later request in
this job. `scripts/social_pack.py` and `scripts/post-lint.py` exist so that resolving the
source, listing profiles, building the drafter prompt, checking the post and writing the
manifest, digest and report cost zero tokens. Do not reimplement any of it by hand, and
do not "just check" with a directory listing when a subcommand answers the same question.

## Steps

1. **Prepare the pack (idempotent, safe to re-run).**

   ```bash
   python3 scripts/social_pack.py source $1
   python3 scripts/social_pack.py brief $1
   ```

   `source` reports the article of record, its status, the **published slug** and the live
   URL. `brief` writes `workspace/social/articles/$1/_run-brief.md` if it does not exist
   and leaves it alone if it does.

   Two things stop the run here, and only these two: `source` exits non-zero (no article
   directory, or nothing in it with an article body), or the brief's HUMAN section is still
   the empty template on a **first** profile of a pack. Do **not** refuse on the article's
   `status:` field — report it and continue. That gate used to say "if not
   `approved_for_publish`, STOP", the SEO pipeline never writes that value, so it refused
   every article that has ever existed here. The approval in this system is Vadim asking
   for the run plus his approval of the finished digest (CLAUDE.md §9).

   **If you are the first profile in the pack**, fill in the two HUMAN sections of the run
   brief before drafting: the claims discipline (every number and boundary the posts may
   state, in the live wording) and the article's real visual assets. This is the one part
   of the brief that needs a reader, it is shared by all nine profiles, and getting it
   right once is what keeps the other eight from inventing figures. Everything else in
   that file is generated — do not hand-edit it.

2. **Confirm `$2` is active.**

   ```bash
   python3 scripts/social_pack.py profiles $1
   ```

   `$2` must appear in `active`. If it is missing, STOP and say so; never substitute a
   different profile.

3. **Run `post-drafter` once, with the generated prompt.**

   ```bash
   python3 scripts/social_pack.py prompt $1 $2
   ```

   Pass that output to the `post-drafter` subagent **verbatim**. Do not summarise it, do
   not reorder it, do not prepend a note of your own.

   This matters beyond convenience. The first section of that output is byte-identical for
   all nine profiles, and prompt caching keys on the exact prefix: the first drafter in the
   pack writes the cache, the other eight read it. With
   `subagentPromptCacheTtl: "1h"` in `.claude/settings.json` the prefix survives the whole
   pack. On 2026-08-28, before this existed, each of the nine drafters paid 70-95K
   cache-creation tokens for substantially the same text in a different order, and shared
   nothing — the subagent cache TTL default is five minutes and the profiles ran four to
   six minutes apart. Any edit you make to the head of that prompt breaks the sharing for
   every profile after you.

   `python3 scripts/social_pack.py prompt $1 --check-prefix` confirms the nine prefixes
   still hash the same, if you want to verify.

4. **Gate the saved post mechanically.**

   ```bash
   python3 scripts/post-lint.py $1 $2 --summary --gate
   ```

   Exit 1 means hard fails. Send them back to `post-drafter` — quote the lint lines, do
   not rewrite the post yourself. Warnings are informational; do not spend a rewrite round
   on them.

   The lint covers length per platform (per tweet in a thread), 0 hashtags, max 2 emoji,
   em dash, banned words and phrasings, `positioned as`, presumed-reaction openers,
   placeholders, the published slug, the design-tip fields, and every number in the post
   against the article of record and `proof-points.md`. That last one is the check that
   caught "under a minute" against a sourced "Under 45 seconds".

5. **Brand voice.** Run `post-brand-checker` on the saved file. FAIL → back to
   `post-drafter` with the reasons. Two rewrite rounds maximum, then note it and move on.

6. **Quality control, only if this profile is sampled.**

   ```bash
   python3 scripts/social_pack.py qc-plan $1
   ```

   If `$2` is in `qc`, build the input and run `post-quality-controller` with it verbatim:

   ```bash
   python3 scripts/social_pack.py qc-prompt $1 $2
   ```

   If `$2` is in `skip`, run no QC. Three of nine profiles are sampled per pack — the
   angle-setter, the least recently inspected company account and the least recently
   inspected personal account — plus, unconditionally, any profile whose lint gate failed.
   The rationale is in CLAUDE.md §14: QC exists to feed `agent-improver`, and the gate on
   the pack is Vadim approving the digest.

   Use `post-quality-controller` (mvb-social), **not** the bare name `quality-controller`
   — that is the deep mvb-core inspector for articles, briefs and outbound, and pointing it
   at a 250-word post is how QC came to cost as much as the writing.

7. **Assemble only if you are the last profile.**

   ```bash
   python3 scripts/social_pack.py profiles $1
   ```

   - `missing` is non-empty → STOP. Report this profile as done and list what remains. Do
     **not** write the digest or the manifest. A partial digest read as a finished one is
     how job #90 shipped a manifest listing 3 profiles while 9 posts sat on disk.
   - `missing` is empty → you are last:

     ```bash
     python3 scripts/post-lint.py $1 --all --summary
     python3 scripts/social_pack.py manifest $1 --write
     python3 scripts/social_pack.py digest   $1 --write
     python3 scripts/social_pack.py report   $1 --write
     ```

     All three files are generated from what is on disk, in the canonical shapes. Do not
     write or edit them by hand, and do not reformat what the scripts produce: the manifest
     schema is owned by `social-publisher`, and the reason it is generated is that three
     agents used to each carry their own copy of it.

8. **Report** the profile, the source file and its status, the lint verdict, whether QC
   ran, and either what remains or the digest path.

## Rules

- One profile per run. No parallel `post-drafter`.
- Facts come only from the article of record resolved in step 1. Invent nothing.
- `visual-brief` is **not** triggered here — only after Vadim approves the text in Telegram.
- Everything goes to files, not into the chat. Publish nothing outward.
