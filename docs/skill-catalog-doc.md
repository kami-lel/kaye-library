# Kaye Library: Skill Catalog Documentation

<!-- Fixme manually update the catalog doc -->

English | [简体中文](skill-catalog-doc.zh-CN.md)

Meet all 148 skills in kaye-library. 📚 Grouped just like the [README](../README.md).

Use any skill two ways:

- Call It: type its name, eg `/commit-sense`
- Ask for It: just say what you want, eg "commit this"; your agent picks the right skill

New here? Start with the 🌟 top picks, then try the ⭐ favorites.

Jump to a group: [💻 Coder](#-coder), [📝 Repository & Project](#-repository--project), [🎨 Style](#-style), [🗓️ Secretary](#️-secretary), [🎮 Unity Engine](#-unity-engine), [🖋️ Amanuensis](#️-amanuensis), [🧱 Elements](#-elements), [🐙 Git](#-git), [🤖 Agentic](#-agentic), [🪄 Meta Prompt](#-meta-prompt), [📖 Glossaries](#-glossaries).


































## 💻 Coder

Clean, consistent code in every language. No more tidying up after your AI.

It all starts with `/coder`: the house rules for all code. Lines stay under 80 characters. Names stay consistent. Comments explain why, not how. Tests run only where the change lands, not the whole suite every time.

You rarely call `/coder` yourself. Every language profile calls it first, then adds its own rules. Python and C# share one set of habits, yet each reads like it was written by a native.













### Language Profiles

Pick your language. Most profiles even load themselves the moment your agent opens a matching file.

| Skill | Language | What You Get |
|---|---|---|
| `/coder-python` ⭐ | Python | PEP 8, consistent names, Sphinx docstrings, comments that explain intent |
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

Python gets two extras. `/coder-python-docstring-style` adds a Sphinx docstring to every function, class, and module, by default. `/coder-python-testing-guidelines` writes `pytest` tests that match your project.













### Keeping Code Healthy

Tests red after a refactor? `/sync-unit-test` 🌟 fixes stale assertions, fixtures, and snapshots. When the code is what broke, it says so. Real bugs never get papered over.

Shipping soon? `/review-gaps` ⭐ audits the whole repository first. It finds gaps, drift, and half-finished seams before your users do, and tags each one for you to fix.













### Output Helpers

Three small skills for the text your code prints:

- `/coder-command-usage-message`: a crisp usage message for `--help` and errors
- `/coder-comment-banner-in-code-comment`: ranked banner comments for file titles, sections, and subsections
- `/coder-comment-banner-in-print-out`: ranked banners that split logs, demos, and test runs into clear phases


































## 📝 Repository & Project

Every project file, written right and kept current.

A good project speaks to five readers. The README greets visitors. The CHANGELOG tells users what changed. `AGENTS.md` gives AI agents their rules. `CONTEXT.md` explains the architecture. `docs/` goes deep. Two optional files round it out: `CREDITS.md` credits every third-party asset, and `DEVLOG.md` keeps the team's journal. kaye-library has a writer for each.

Most writers come with two workflows. Create builds the file from nothing. Maintain updates it in place after the code moves on.

| File | Who Reads It | Writer | Create | Maintain |
|---|---|---|---|---|
| `README.md` | visitors | `/repo-readme-writer` ⭐ | `/create-readme` | `/maintain-readme` |
| `CHANGELOG.md` | users upgrading | `/repo-changelog-writer` | `/create-changelog` | `/maintain-changelog` |
| `AGENTS.md` in a repository | AI coding agents | `/repo-agents-writer` | `/create-repo-agents` | `/maintain-repo-agents` |
| `AGENTS.md` in any project | AI agents | `/proj-agents-writer` | `/create-project-agents` | `/maintain-project-agents` |
| `CONTEXT.md` | new developers and AI | `/repo-context-writer` | ➖ | ➖ |
| `CREDITS.md` | credited creators, license checkers | `/repo-credits-writer` | `/create-credits` | `/maintain-credits` |
| `DEVLOG.md` | the team, reviewers | `/repo-devlog-writer` | `/create-devlog` | `/maintain-devlog` |
| `docs/` in a repository | readers wanting depth | `/repo-doc-writer` | `/create-repo-docs` | `/maintain-repo-docs` |
| `docs/` in any project | readers wanting depth | `/proj-doc-writer` | `/create-project-docs` | `/maintain-project-docs` |

`repo-` skills are for code repositories. `proj-` skills fit any project: a game design, a research archive, a codebase.

A few highlights:

- `/repo-readme-writer` turns a bare repository into a landing page people actually read, like this library's own README
- `/repo-changelog-writer` follows Keep a Changelog, with an `[Unreleased]` section and version links; `/create-changelog` even rebuilds one from git history
- `/repo-agents-writer` and `/repo-context-writer` keep rules and knowledge apart: `AGENTS.md` says what to do, `CONTEXT.md` says how things work, and personal notes stay in a private `.local.md` file
- `/repo-credits-writer` gives every third-party asset a row: its path, source, author, and license, so nothing ships uncredited
- `/repo-devlog-writer` ties each change to the playtest, survey, or bug that prompted it, with captioned screenshots and honest leftovers













### Setting Up and Keeping Tidy

New repository? `/initialize-repo` 🌟 writes the whole starter set in one pass: README, CHANGELOG, AGENTS, CONTEXT, and `docs/`. No overlap, no gaps. Just need agent rules? `/equip-proj-for-agent` writes and keeps up `AGENTS.md`. Both follow `/repo-structure`, one standard layout for every folder and top-level file.

Files bloat. Two skills trim them:

- `/condense-agents-and-context`: cuts finished plans and stale detail from `AGENTS.md` and `CONTEXT.md`, adds nothing
- `/condense-changelog`: tightens `[Unreleased]` for release and flags breaking changes

Long session? `/maintenance-before-compact` ⭐ saves every lasting change to CHANGELOG, AGENTS, and CONTEXT before the context window compacts. Nothing learned gets lost.













### Landing Features and Shipping Releases

Two workflows, each with a ready half before the merge and a scrub half after it:

| Prepare | Clean Up | Prepare, Merge, and Clean Up | What Merging Adds |
|---|---|---|---|
| `/ready-land-feature` | `/scrub-landed-feature` | `/land-feature` | merge into `dev` with a clear message |
| `/ready-release-version` | `/scrub-released-version` | `/release-version` ⭐ | merge to `main` and tag the release |

The ready half logs changes in the CHANGELOG and syncs every doc. For releases, it also dates the version and bumps it in every metadata file. The scrub half pushes the result, then clears what the merge left behind: the merged branch and its linked worktree after a landing, merged branches and a lagging `dev` after a release, which then moves on to the next alpha version, each only once you approve. Prefer to merge by hand? Run the ready half, merge, then the scrub half. Want a pull request instead? See `/submit-pr` under [Git](#-git).













### Versioning

- `proj-version`: semantic versioning rules, ie when MAJOR, MINOR, and PATCH go up; loads on its own, stays out of the slash menu
- `/proj-version-extended`: `alpha`, `beta`, and `rc` numbering, build tags, and the right version for each stage of development
- `/proj-version-title`: a release title from the old and new versions


































## 🎨 Style

One voice, whatever your agent writes.













### Markdown

- `style-markdown`: clean GitHub Flavored Markdown with consistent bold and italics; applied automatically, stays out of the slash menu
- `/style-markdown-extended`: labeled lists, LaTeX math, Mermaid diagrams
- `/style-markdown-footnotes`: each footnote right beside the text that cites it
- `/style-markdown-endnotes`: every definition gathered in one block at the end
- `/style-markdown-file-assets`: each file's images in its own sibling folder, eg `CHANGELOG-assets/`, linked by relative path

Long documents need room to breathe. `/style-heading-separation` spaces headings by level and file length. `/style-heading-separation-medium` and `/style-heading-separation-long` lock in the spacing for medium and long files.













### Letter Case

One skill per convention, so any rule can point to exactly one.

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

Two skills, opposite jobs. `/style-briefness-style` ⭐ cuts wordy drafts down to tight, headline-style notes. Perfect for status lines, summaries, and comments. `/style-good-writing` proofreads with the lightest touch: spelling, grammar, punctuation, clarity. Your voice stays yours.


































## 🗓️ Secretary

A personal assistant for your inbox, calendar, to-do list, and job search. It works through the apps your agent is already connected to.













### Check-ins

`/good-morning` 🌟 is your daily briefing. One command sweeps your inbox, recaps yesterday, scans today's events, and finds job openings. You get one combined report. Each step also works alone.

`/good-week` looks ahead at the week's events and job openings. Need a lift? `/recap-yesterday` and `/recap-today` sum up what you got done in one warm, upbeat line.













### Email, Calendar, and Tasks

`/draft-email` ⭐ writes exactly what you asked. Nothing invented. Revised as often as you like. `/sweep-email-inbox` reads every unread message, marks it read, and files it by category.

Calendar and tasks come in push and pull pairs:

| Push into Your App | Pull into the Conversation |
|---|---|
| `/push-event-to-calendar`: one event, or a whole list from the chat | `/pull-event-from-calendar`: your real schedule |
| `/push-task-to-gtd`: tasks with a project and an Eisenhower quadrant | `/pull-task-from-gtd`: your real to-do list |

GTD stands for *Getting Things Done*, the task-management method.













### Events and Jobs

`/scan-event-radar-daily` finds today's events. `/scan-event-radar-weekly` covers the week ahead. Both use `/secretary-event-brief-format`: heading, key details, short overview. `/hunt-job-opportunity` pulls job openings from any source, one brief per job.


































## 🎮 Unity Engine

A complete house style for Unity 6 C#. `/u3d` sets the baseline, built on `/coder-c-sharp`. Every topic is its own skill, so your agent loads only what the task needs.

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


































## 🖋️ Amanuensis

Your scholarly scribe: citations, notes, minutes, and careful revision.













### Citations

Every citation follows the *Chicago Manual of Style*. Never hand-format one again.

- `/amanuensis-chicago-note` 🌟: citations as native Markdown footnotes
- `/amanuensis-chicago-bibliography`: bibliography entries, plain or annotated
- `/assemble-bibliography`: every source a document cites, gathered into one bibliography
- `/bibliographer`: runs all of the above together when a piece needs both notes and a bibliography













### Notes and Records

`/dispositor` is the base note-taker: structured notes, one filename, one layout. Four specialists build on it:

- `/scholiast`: paragraph-by-paragraph reading notes on academic texts, citations on request
- `/minutes-clerk` ⭐: meeting minutes that track every decision and action item to done
- `/config-writer`: an app's, game's, or system's settings, saved as a snapshot you can restore
- `/keybinding-writer`: keybindings recorded in compact key symbols

And `/redactor` revises your text, keeps your intent and style, and iterates until it reads right.


































## 🧱 Elements

The small, exact building blocks behind every other skill. Other skills call them for you. Call one directly when you want just that rule.

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


































## 🐙 Git

Commits worth reading. Clean merges. Parallel work without collisions.

`/working-with-git` sets the ground rules: your agent never pushes or rewrites history without your say-so. On Perforce? `/working-with-p4v` pairs every Perforce term with its Git equivalent. No translating in your head.













### Commits and Merges

`/commit-sense` 🌟 ends "fix stuff" commits. Say "commit this" and get a sharp summary line plus a per-file ledger of what changed and why. `/commit-sense-branch-merging` does the same for merge messages.

The rest of the branch lifecycle:

- `/resolve-merge-conflict` ⭐: a halted merge untangled, both sides reconciled, markers gone
- `/prune-merged-branches`: merged branches deleted, with a report of what went and what stayed
- `/submit-pr`: docs readied and a pull request into `dev` opened, title and body written for you













### Parallel Work in Worktrees

Run three features at once. None collide. A linked worktree is a second working folder on its own branch. `/tend-linked-wt` 🌟 handles its whole life: `/plant-linked-wt` creates it, `/uproot-linked-wt` removes it once the work is merged.


































## 🤖 Agentic

How your agent works with you, turn by turn. The conversation rules apply on their own, in Kaye's voice: reply language, shared terms for each step, and clearly marked questions you can't miss.













### Movements and Suites

Big tasks need structure. A Suite is the whole multi-round task. A Movement is one reviewable step, small enough to judge at a glance. `/agent-movement-and-suite` defines both. `/agent-movement-and-suite-with-count` splits Movements into Counts, so progress reads as a fraction.

`/plan-for-suite` 🌟 puts it to work. No more 30-file rewrites in one go. Your agent surveys the repository, writes a numbered plan, and waits for your approval.

- `/execute-plan-for-suite`: one Movement per turn; the plan file saves progress, so you pause tonight and resume tomorrow, even in a new session
- `/rework-plan-for-suite`: plan no longer fits reality? It halts, rewrites the plan, and waits for your approval again

You set the pace. `/halt-each-movement` stops after every step for your review. `/cascade-all-movements` runs everything left and stops only when done or when it needs you.


































## 🪄 Meta Prompt

Prompts that write prompts. `/write-llm-prompt` ⭐ turns a vague system prompt into one that delivers: drafted, graded, sharpened, with JSON schemas and structure left intact.

Three more write the metadata that tells an agent when to load a skill:

- `/write-skill-description`: what the skill does, main verb first
- `/write-skill-when-to-use`: trigger phrases, plus where the skill stops
- `/write-skill-description-and-when-to-use`: both at once


































## 📖 Glossaries

Type less. Your agent still understands. Each glossary decodes one family of shorthand.

| Skill | Decodes | Example |
|---|---|---|
| `/glossary-coder-abbr` | programming abbreviations | `ctor`, `iface`, `mpl` |
| `/glossary-programming-language-codes` | programming language codes | `py`, `ts`, `cpp` |
| `/glossary-natural-language-codes` | natural language codes | `en`, `zh`, `jp` |
| `/glossary-units-of-measure` | unit abbreviations | `ft`, `lb`, `mi` |
| `/glossary-element-dt-days-of-week` | single-letter weekday codes | days in dates and schedules |
| `/glossary-secretary-eisenhower-matrix-quadrant` | the four Eisenhower quadrants | Important and Urgent, with emoji |
