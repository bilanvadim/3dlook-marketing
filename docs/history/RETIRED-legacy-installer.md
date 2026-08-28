# `install.sh` and `INSTALL.md` (root) — retired 2026-08-28

Two installers shipped side by side and disagreed with each other:

* `bootstrap/install.sh` — the current one. README's opening paragraph and its quick-start
  block both point here.
* `install.sh` (root) — the legacy one. README's own "Get started" section pointed HERE,
  and it still described "prepares Conductor (libSQL)" — a driver removed after it leaked a
  connection per transaction and OOM-killed the box. It also told the reader to overwrite a
  SYSTEM-scope `hermes-conductor.service`, which on this host belongs to the other account.

A reader following the README could land on either, depending on which section they read
first, and one of the two would put two conductors on one queue.

Only `bootstrap/install.sh` remains. `docs/INSTALL.md` is the installation document.
