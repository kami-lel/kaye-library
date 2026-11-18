# Kaye Library: Skill Catalog Documentation

<!-- Fixme manually update the catalog doc -->

English | [简体中文](skill-catalog-doc.zh-CN.md)

Meet every skill in kaye-library. 📚 Grouped just like the [README](../README.md).

Use any skill two ways (eg in Claude Desktop):

- Call It: type its name, eg `/commit-sense`
- Ask for It: just say what you want, eg "commit this"; your agent picks the right skill

New here? Start with the 🌟 Top Picks, then try the ⭐ Favorites.


































## 🤖 Agentic

How your agent works with you, turn by turn. Chat rules apply on their own, in Kaye's voice: reply language, shared terms, clearly marked questions.













### Movements and Suites

Big tasks need structure. `/plan-for-suite` 🌟 is where to start.

Your agent first surveys the repository, then writes the work down as a numbered **plan file** and waits for your approval before touching anything.

That file is the **Suite**: the whole multi-round task, saved on disk. Each numbered step in it is a **Movement**, one reviewable unit small enough to judge at a glance.

> [!NOTE]
> When Git is available, each Movement is committed automatically.

No more 30-file rewrites in one go. You read the plan, adjust it, and only then does the work begin, one Movement at a time.

Plan the work, then run it:

| Skill | What You Get |
|---|---|
| `/plan-for-suite` 🌟 | a numbered, reviewable plan before any edit; nothing runs until you approve |
| `/execute-plan-for-suite` | one Movement per turn; the plan file saves progress, so you pause tonight and resume tomorrow, even in a new session |
| `/rework-plan-for-suite` | plan no longer fits reality? it halts, rewrites the plan, and waits for your approval again |

Then set the pace:

| Skill | What You Get |
|---|---|
| `/halt-each-movement` | stops after each Movement and waits for your review before the next |
| `/cascade-all-movements` | runs every remaining Movement in one go, stopping only when the Suite is done or when it needs you |

> [!TIP]
> When executing plans, pair `/execute-plan-for-suite` with `/tend-linked-wt` to work in parallel. Each plan gets its own linked worktree, so several Suites can run at once without colliding.

----

Supporting skills behind the vocabulary:

- `/agent-movement-and-suite`: defines Suite and Movement
- `/agent-movement-and-suite-with-count`: splits Movements into Counts, so progress reads as a fraction


































## 📝 Repository & Project

Every project file, written right and kept current.

A good project speaks to **five readers**: the README greets visitors, the CHANGELOG tells users what changed, `AGENTS.md` gives AI agents their rules, `CONTEXT.md` explains the architecture, and `docs/` goes deep. Optional `CREDITS.md` and `DEVLOG.md` cover third-party credits and a public development journal, a favorite for games. Each file has its own writer.

Most writers have two workflows: **Create** builds the file from nothing, **Maintain** updates it in place as the code moves on.

| File | Who Reads It | Writer | Create | Maintain |
|---|---|---|---|---|
| `README.md` | visitors | `/repo-readme-writer` ⭐ | `/create-readme` | `/maintain-readme` |
| `CHANGELOG.md` | users upgrading | `/repo-changelog-writer` | `/create-changelog` | `/maintain-changelog` |
| `AGENTS.md` in a repository | AI coding agents | `/repo-agents-writer` | `/create-repo-agents` | `/maintain-repo-agents` |
| `AGENTS.md` in any project | AI agents | `/proj-agents-writer` | `/create-project-agents` | `/maintain-project-agents` |
| `CONTEXT.md` | new developers and AI | `/repo-context-writer` | ➖ | ➖ |
| `CREDITS.md` | credited creators, license checkers | `/repo-credits-writer` | `/create-credits` | `/maintain-credits` |
| `DEVLOG.md` | followers of the dev process (eg players tracking a game or app in the making) | `/repo-devlog-writer` | `/create-devlog` | `/maintain-devlog` |
| `docs/` in a repository | readers wanting depth | `/repo-doc-writer` | `/create-repo-docs` | `/maintain-repo-docs` |
| `docs/` in any project | readers wanting depth | `/proj-doc-writer` | `/create-project-docs` | `/maintain-project-docs` |

`repo-` skills are for code repositories. `proj-` skills fit any project: a game design, a research archive, a codebase.

A few **highlights**:

- `/repo-readme-writer` turns a bare repository into a landing page people actually read, like this library's own README
- `/repo-changelog-writer` follows Keep a Changelog, with an `[Unreleased]` section and version links; `/create-changelog` even rebuilds one from git history
- `/repo-agents-writer` and `/repo-context-writer` keep rules and knowledge apart: `AGENTS.md` says what to do, `CONTEXT.md` says how things work, and personal notes stay in a private `.local.md` file
- `/repo-credits-writer` gives every third-party asset a row: its path, source, author, and license, so nothing ships uncredited
- `/repo-devlog-writer` ties each change to the playtest, survey, or bug that prompted it, with captioned screenshots and honest leftovers













### Setting Up and Keeping Tidy

Start a repository right, keep its files lean, and never lose what a long session learned. The two setup skills follow `/repo-structure`, one **standard layout** for every folder and top-level file.

| Skill | What You Get |
|---|---|
| `/initialize-repo` 🌟 | the whole **starter set** in one pass: README, CHANGELOG, AGENTS, CONTEXT, and `docs/`, no overlap, no gaps |
| `/equip-proj-for-agent` | just the **agent rules**: writes and keeps up `AGENTS.md` |
| `/condense-agents-and-context` | trims bloated files: cuts finished plans and stale detail from `AGENTS.md` and `CONTEXT.md`, adds nothing |
| `/condense-changelog` | tightens `[Unreleased]` for release and flags breaking changes |
| `/maintenance-before-compact` ⭐ | saves every lasting change to CHANGELOG, AGENTS, and CONTEXT **before the context window compacts**, so nothing learned is lost |













### Landing Features and Shipping Releases

Two workflows, each with a ready half before the merge and a scrub half after it:

| Prepare, Merge, and Clean Up | Prepare | Clean Up | What Merging Adds |
|---|---|---|---|
| `/land-feature` | `/ready-land-feature` | `/scrub-landed-feature` | merge into `dev` with a clear message |
| `/release-version` ⭐ | `/ready-release-version` | `/scrub-released-version` | merge to `main` and tag the release |

Each workflow has two halves:

- Ready Half: logs changes in the CHANGELOG and syncs every doc; for a release, it also dates the version and bumps it in every metadata file
- Scrub Half: pushes the result, then clears what the merge left behind, **each step only once you approve**:
  - after a landing: the merged branch and its linked worktree
  - after a release: merged branches and a lagging `dev`, then `dev` moves on to the next alpha version

Prefer to merge by hand? Run the ready half, merge, then run the scrub half. Want a **pull request** instead? See `/submit-pr` under [Git](#-git).













### Versioning

Supporting skills for the release workflows above:

- `/proj-version-extended`: numbers every pre-release for you, eg `1.0.0-beta.2` for the second beta and `1.0.0-rc.1` for the first release candidate, plus build tags
- `/proj-version-title`: titles a release from its old and new versions, eg going from `1.3.2` to `1.4.0` gives `Minor Stable Release 1.4.0`


































## 🐙 Git

Commits worth reading. Clean merges. Parallel work without collisions.













### Commits and Merges

`/commit-sense` 🌟 ends "fix stuff" commits. A commit is a saved snapshot of your work, and its message should say what changed. Say "commit this" and get:

- a sharp **summary line**: the one-line headline of the change
- a **per-file ledger**: what changed in each file, and why

`/commit-sense-branch-merging` does the same for merge messages. A merge joins one branch, a separate line of work, back into another.

The rest of the branch lifecycle:

- `/resolve-merge-conflict` ⭐: two branches edited the same lines and the merge stopped? this untangles it, keeping both sides' intent and clearing the conflict markers
- `/prune-merged-branches`: deletes branches whose work is already merged, with a report of what went and what stayed
- `/submit-pr`: readies the docs and opens a pull request into `dev`, a request to merge your branch, with title and body written for you













### Parallel Work in Worktrees

Run three features at once. None collide.

Normally one folder holds one branch at a time, so switching branches mid-task disturbs your files. A **linked worktree** is an extra working folder of the same repository, locked to its own branch. Each task gets its own folder, so edits in one never touch the others.

- `/tend-linked-wt` 🌟: handles a worktree's whole life, from creating it to removing it
- `/plant-linked-wt`: creates one for a new task
- `/uproot-linked-wt`: removes it once the work is merged













### Ground Rules

These apply on their own, so you rarely need to call them by hand:

- `/working-with-git`: your agent **never pushes or rewrites history** without your say-so
- `/working-with-p4v`: on Perforce? every term paired with its Git equivalent


































## 💻 Coder

Clean, consistent code in every language. No more tidying up after your AI.

It all starts with `/coder`: the house rules for all code, such as 80-character lines and consistent names. You rarely call it yourself. It **triggers on its own** whenever your agent writes code, and every language profile builds on it.













### Keeping Code Healthy

Tests red after a refactor? `/sync-unit-test` 🌟 fixes **stale assertions, fixtures, and snapshots**. When the code is what broke, it says so. Real bugs never get papered over.

Shipping soon? `/review-gaps` ⭐ audits the whole repository first. It finds **gaps, drift, and half-finished seams** before your users do, and tags each one for you to fix.













### Language Profiles

Pick your language. Most profiles even load themselves the moment your agent opens a matching file.

| Skill | Language | What You Get |
|---|---|---|
| `/coder-python` ⭐ | Python | PEP 8, consistent names, comments that explain intent |
| `/coder-python-docstring-style` | Python | a Sphinx docstring on every function, class, and module, by default |
| `/coder-python-testing-guidelines` | Python | `pytest` tests that match your project |
| `/coder-c` | C | C99 and clean brace placement |
| `/coder-cpp` | C++ | one house style, built on the C profile |
| `/coder-ue` | Unreal Engine C++ | Unreal conventions, built on the C++ profile |
| `/coder-c-sharp` | C# | clean braces and XML documentation comments |
| `/coder-javascript-and-typescript` | JavaScript, TypeScript | ES11, camelCase names, JSDoc comments |
| `/coder-html` | HTML | HTML5 structure and semantic markup |
| `/coder-gdscript` | GDScript | idiomatic Godot 4 code |
| `/coder-powershell` | PowerShell | one fixed code style |
| `/coder-bash-script` | Bash | scripts, functions, and libraries for Debian |
| `/coder-bash-shell` | Bash | the bare command line, ready to paste |













### Output Helpers

Three small skills for the text your code prints:

| Skill | What You Get |
|---|---|
| `/coder-command-usage-message` | a crisp usage message for `--help` and errors |
| `/coder-comment-banner-in-code-comment` | ranked banner comments for file titles, sections, and subsections |
| `/coder-comment-banner-in-print-out` | ranked banners that split logs, demos, and test runs into clear phases |


































## 🗓️ Secretary

A **personal assistant** for your inbox, calendar, to-do list, and job search. It works through the apps your agent is already connected to.













### Check-ins

`/good-morning` 🌟 is your **daily briefing**. One command sweeps your inbox, recaps yesterday, scans today's events, and finds job openings. You get one **combined report**. Each step also works alone.

`/good-week` looks ahead at the week's events and job openings. Need a lift? `/recap-yesterday` and `/recap-today` sum up what you got done in one warm, upbeat line.













### Email, Calendar, and Tasks

`/draft-email` ⭐ writes exactly what you asked. **Nothing invented.** Revised as often as you like. `/sweep-email-inbox` reads every unread message, marks it read, and files it by category.

Calendar and tasks come in push and pull pairs:

| Push into Your App | Pull into the Conversation |
|---|---|
| `/push-event-to-calendar`: one event, or a whole list from the chat | `/pull-event-from-calendar`: your real schedule |
| `/push-task-to-gtd`: tasks with a project and an Eisenhower quadrant | `/pull-task-from-gtd`: your real to-do list |

GTD stands for *Getting Things Done*, the task-management method.













### Events and Jobs

`/scan-event-radar-daily` finds today's events. `/scan-event-radar-weekly` covers the week ahead. Both use `/secretary-event-brief-format`: heading, key details, short overview. `/hunt-job-opportunity` pulls job openings from any source, **one brief per job**.


































## 🖋️ Amanuensis

Your **scholarly scribe**: citations, notes, minutes, and careful revision.













### Citations

Every citation follows the *Chicago Manual of Style*. **Never hand-format one again.**

- `/amanuensis-chicago-note` 🌟: citations as native Markdown footnotes
- `/amanuensis-chicago-bibliography`: bibliography entries, plain or annotated
- `/assemble-bibliography`: every source a document cites, gathered into one bibliography
- `/bibliographer`: runs all of the above together when a piece needs both notes and a bibliography













### Notes and Records

`/dispositor` is the **base note-taker**: structured notes, one filename, one layout. Four specialists build on it:

- `/scholiast`: paragraph-by-paragraph reading notes on academic texts, citations on request
- `/minutes-clerk` ⭐: meeting minutes that track every decision and action item to done
- `/config-writer`: an app's, game's, or system's settings, saved as a snapshot you can restore
- `/keybinding-writer`: keybindings recorded in compact key symbols

And `/redactor` revises your text, keeps your intent and style, and iterates until it reads right.


































## 🎮 Unity Engine

A complete **house style** for Unity 6 C#. `/u3d` sets the baseline, built on `/coder-c-sharp`. Every topic is its own skill, so your agent loads only what the task needs.

| Skill | What You Get |
|---|---|
| `/u3d-coding` | Unity C# in one house idiom; debug sessions read like a story |
| `/u3d-naming` ⭐ | one naming rule for every class, asset, folder, and GameObject; goodbye, `Hero_final2` |
| `/u3d-common-type-and-suffix` | one clear role per class, script, GameObject, and asset, named by its suffix |
| `/u3d-if` | Inspector fields designers can tune and rename without losing saved values |
| `/u3d-mb` | one layout for every `MonoBehaviour`; missing Inspector links caught at startup |
| `/u3d-so` | one layout for every `ScriptableObject`; data stays read-only and valid |
| `/u3d-pfb` | prefabs and variants early; one edit updates every copy |
| `/u3d-game-tuning` | gameplay numbers in designer-editable data; rebalance without a recompile |
| `/u3d-owner-driven-activation` | one owner spawns, shows, and hides each short-lived object; zero cost while idle |
| `/u3d-assets-management` | a home for every asset under `Assets/`; find anything without searching |


































## 🪄 Meta Prompt

**Prompts that write prompts.** `/write-llm-prompt` ⭐ turns a vague system prompt into one that delivers: drafted, graded, sharpened, with JSON schemas and structure left intact.

Three more write the metadata that tells an agent **when to load** a skill:

- `/write-skill-description`: what the skill does, main verb first
- `/write-skill-when-to-use`: trigger phrases, plus where the skill stops
- `/write-skill-description-and-when-to-use`: both at once


































## 🎨 Style

One **voice**, whatever your agent writes.

Most style skills are supporting: other skills load them for you, so one rule shapes every document. Call one directly only when you want just that rule.













### Markdown

- `/style-markdown-extended`: labeled lists, LaTeX math, Mermaid diagrams
- `/style-markdown-footnotes`: each footnote right beside the text that cites it
- `/style-markdown-endnotes`: every definition gathered in one block at the end
- `/style-markdown-file-assets`: each file's images in its own sibling folder, eg `CHANGELOG-assets/`, linked by relative path

Long documents need **room to breathe**. `/style-heading-separation` spaces headings by level and file length. `/style-heading-separation-medium` and `/style-heading-separation-long` lock in the spacing for medium and long files.













### Letter Case

One skill per **convention**, so any rule can point to exactly one.

| Skill | Convention | Example |
|---|---|---|
| `/style-letter-case-title-case` | major words capitalized, minor words lowercase | `The Lord of the Rings` |
| `/style-letter-case-commentary-case` | lowercase opening, no final period | `check the Config first` |
| `/style-letter-case-snake-case` | lowercase words joined by underscores | `total_price` |
| `/style-letter-case-kebab-case` | lowercase words joined by hyphens | `total-price` |
| `/style-letter-case-camel-case` | first word lowercase, later words capitalized | `totalPrice` |
| `/style-letter-case-pascal-case` | every word capitalized, no separators | `TotalPrice` |
| `/style-letter-case-all-caps` | uppercase words joined by underscores | `TOTAL_PRICE` |













### Prose

Two skills, opposite jobs. `/style-briefness-style` ⭐ cuts wordy drafts down to **tight, headline-style notes**. Perfect for status lines, summaries, and comments.

`/style-good-writing` proofreads with the **lightest touch**: spelling, grammar, punctuation, clarity. Your voice stays yours.


































## 🧱 Elements

The small, exact **building blocks** behind every other skill. They are all supporting: other skills call them for you, so one rule stays the same everywhere. Call one directly only when you want just that rule.

Dates and times look the same everywhere:

| Skill | What It Does |
|---|---|
| `/element-dt-year-month-day-format` | a date with a year, weekday optional |
| `/element-dt-month-day-format` | a date without a year, weekday optional |
| `/element-dt-time-format` | 24-hour time, from minutes to fractions of a second |
| `/element-dt-watch-day` ⭐ | a day that runs past midnight on a 30-hour clock, built for night owls |
| `/element-dt-watch-week` | a planning week that always ends on Sunday |

More building blocks:

- `/element-numerical-values-with-units`: metric and US units side by side, correctly abbreviated
- `/element-international-phonetic-alphabet`: IPA pronunciation after any tricky word, in any language
- `/element-alphabetical-sequence-numbering`: circled letters (ⓐ, ⓑ, ⓒ) for choices, so you answer with one letter
- `/element-triage-tags`: `BUG`, `FIXME`, `TODO`, and `HACK` in three loudness tiers
- `/sort-and-group-triage-tag`: sorts existing tags into tidy groups, changes nothing else


































## 📖 Glossaries

**Type less.** Your agent still understands. Each glossary decodes one family of shorthand.

They are all supporting: other skills load them for you, so shorthand means the same everywhere. Call one directly only when you want just that decoding.

| Skill | Decodes | Example |
|---|---|---|
| `/glossary-coder-abbr` | programming abbreviations | `ctor`, `iface`, `mpl` |
| `/glossary-programming-language-codes` | programming language codes | `py`, `ts`, `cpp` |
| `/glossary-natural-language-codes` | natural language codes | `en`, `zh`, `jp` |
| `/glossary-units-of-measure` | unit abbreviations | `ft`, `lb`, `mi` |
| `/glossary-element-dt-days-of-week` | single-letter weekday codes | days in dates and schedules |
| `/glossary-secretary-eisenhower-matrix-quadrant` | the four Eisenhower quadrants | Important and Urgent, with emoji |
