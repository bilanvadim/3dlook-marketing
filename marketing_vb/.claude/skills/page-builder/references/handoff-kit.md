# Handoff kit — shipping a page someone else publishes

3DLOOK marketing pages are not published from this pipeline. The page goes to whoever owns WordPress
on 3dlook.ai, and per `CLAUDE.md` §10 rule 2 nothing here has publishing credentials. The handoff kit
is what makes that state honest and workable instead of a folder of files in a chat.

---

## What ships

Everything under `workspace/pages/{slug}/`:

| Artifact | Purpose |
|---|---|
| `page.md` | The page itself: every slot in order, visuals marked, frontmatter with `product`, `type`, `vertical`, `status` |
| `README.md` | What is in the box, the page structure, the WordPress and Yoast instructions, tokens used |
| `TODO.md` | Everything unfinished, ordered: blocking → placeholders → claims to confirm → nice to have |
| `fact-sheet.md` | The source behind every number and customer name, plus what was measured versus assumed |
| `gate-reports.md` | G-I / G-A / G-T results, dropped slots and why, waivers with dates |
| `judge-round-N.json` | Every blind-judge round, including the failed ones |
| `assets/` | Images actually referenced, at the sizes used, WebP, alt text listed |
| `open-items.md` | Every bent guardrail, for Asselya — principle #11, never a silent edit |

A `page.html` prototype is optional. Build one when the layout itself needs approving, using the
`:root` block from `DESIGN.md` §13 so tokens are exact — self-contained, openable with a double click,
no build step.

---

## The placeholder registry

Every unfinished thing is visible **in the markup** and **in `TODO.md`**, using one searchable
pattern: `[PLACEHOLDER]`, `[QUOTE — needs client approval]`, `[NUMBER — confirm with Vadim]`.

- **A placeholder never looks finished.** An invented case with plausible numbers is worse than an
  empty block, because nobody removes it. On this project it is also a hard fail at the judge.
- **Mocks are labelled on the artifact itself**, not only in the README. A sample report or dashboard
  screenshot carries a visible "Illustrative example" line.
- **Each placeholder has an exit** — either the real content, or "delete this section and its link".
- **Named humans and quotes are never invented.** Role and context without a name is acceptable
  ("Operations lead, distributed uniform programme"); invented names, faces and testimonials stay out
  even as filler.

## The blocker list

`TODO.md` opens with what blocks launch, and nothing else lives in that section. Typical blockers here:

- **URL and redirects.** For any FitXpress vertical page: which option from `site-inventory.md` was
  chosen, the final slug, and the 301s to set. This is the most common blocker on this site.
- **Parent link down.** The product page must link to the new vertical page. That edit is on someone
  else's plate and the page is orphaned until it happens.
- **Form destination.** Which plugin or endpoint receives the demo request, and where it lands.
- **Customer approval** on any name, logo, metric or quote from `case-studies/`.
- **Conflicting numbers** in the source material — put the conflict in the list. Guardrail #2 forbids
  averaging and forbids silently picking one. The `pricing.md` versus `/pricing/` mismatch is a live
  example.

Then, separately: claims needing Asselya's or Whitney's confirmation — anything touching medical,
clinical or regulatory framing, and any accuracy statement that had to be scoped.

## WordPress and Yoast notes for the README

- **Yoast fields**, written out: SEO title ≤ 60 characters, meta description ≤ 155, canonical to self,
  breadcrumb title. Say explicitly that they must differ from the parent page's and from the vertical's
  hub article's.
- **Schema.** Yoast supplies `WebPage`, `Organization` and `BreadcrumbList`. Service or Product with
  `audienceType` and `areaServed`, plus **FAQPage on the FAQ block**, have to be added on top. One page
  already does this — `/structured-body-data-for-telehealth-digital-health-programs/` — so point the
  receiving team at its JSON-LD as the working example instead of describing the markup from scratch.
- **Blocks and page builder.** Say which sections are plain blocks and which need the page builder,
  and which existing page to clone as the closest template —
  `/structured-body-data-for-telehealth-digital-health-programs/` is the best-built vertical page on
  the site today, and the only one whose schema is already right.
- **Asset paths.** Anything relative in a prototype breaks in WordPress. Name the exact string to
  find and replace.
- **Class collisions.** Short names (`.btn`, `.card`, `.wrap`) collide with the theme. Namespace them.
- **Duplicate chrome.** A prototype ships its own header and footer; the theme supplies those. Say
  which two blocks to delete, or the page goes live with two headers and the page gets blamed.
- **Analytics.** Name every event the page expects on form view, first input, submit and demo-link
  clicks, and say they must be verified firing manually after publish.
- **Third-party embeds.** Any widget or video: name the network dependency, what the block looks like
  when it fails, and that consent tooling can block it.

## Preflight before you send

- [ ] Every slot either filled or listed as a deliberate drop in `gate-reports.md`
- [ ] Every placeholder appears in `TODO.md`, and every `TODO.md` entry exists in the page
- [ ] Every number in `fact-sheet.md` with its source; nothing traced to "internal estimate"
- [ ] No confidential material in the package: Mobile Tailor ARRs, unapproved customer names,
      internal deck figures, staging URLs
- [ ] Yoast fields written out and within limits
- [ ] All internal links resolve, all four linking directions present
- [ ] Alt text on every asset; images WebP and sized
- [ ] Open items block written for Asselya
- [ ] The blind-judge score stated in the README, including a "gate not taken" flag if it applies
