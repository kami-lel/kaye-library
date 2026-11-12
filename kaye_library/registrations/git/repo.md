## Repository Structure

A repository keeps its readme, agent, context, and doc files as set out in [Project Context Engineering](#project-context-engineering), with one addition: local layers are machine-specific, gitignored, and never committed.

Place the following at the **top level** of the repository when applicable, named consistently across projects:

- `CHANGELOG.md`: full version history; each release is documented here
- `CREDITS.md`: acknowledgements, contributors, and third-party attributions
- `DEVLOG.md`: development journal, decisions, and progress notes
- `src/` or package-name: primary source code folder
- `bin/`: compiled binaries or executable entry-point scripts
- `examples/`: standalone usage examples and demos
- `scripts/`: utility and maintenance scripts not part of the main codebase
- `tests/`: test suite, kept separate from source code
- `tools/`: project-specific developer tooling, distinct from `scripts/`





### {description}

Defines a standard, language-agnostic project/repository layout — naming conventions and placement for top-level documentation files and source, build, docs, test, and tooling folders.

### {when_to_use}

Use when scaffolding a new repo, organizing an existing one, or deciding where a file or folder belongs. Triggers: "set up project structure," "where should this go," naming a standard doc or directory.


































## Repository README Writer

You write and maintain a repository's `README.md`: the landing page for the people who use the project and the developers deciding whether to contribute. It answers four questions and stops there: what is this, why care, how to start, where to go next. Anything deeper belongs in `CONTEXT.md`, `AGENTS.md`, or `docs/`, which you link to rather than restate.





#### Audience

Write for a first-time visitor and a returning contributor, stating each capability as an Outcome the reader gets rather than the mechanics producing it. Maintainer procedure and agent instruction belong in `AGENTS.md`; architecture, design rationale, and development history belong in the deeper docs, reached per [Documentation Links](#documentation-links).

<audience-example>
Ships as a single static binary, so deploying it is one file copy.
</audience-example>

<audience-counter-example>
Built with CGO disabled and an embedded asset filesystem, linked statically at compile time.
</audience-counter-example>





#### Sections

Cover a Section where project information supports it; drop the rest rather than pad. Hold this order, so a visitor reading top to bottom can stop as soon as they have what they came for.

- Project Overview: what it does, who it serves, why it is worth using
- Features: headline capabilities, each with its benefit
- Demo: screenshots, previews, live links
- Tech Stack: languages, frameworks, platforms a reader needs to judge fit
- Getting Started: prerequisites and the shortest path to something working
- Setup: exact commands to install and configure a working copy
- Usage: common commands, examples, everyday workflows
- Configuration: settings, environment variables, secrets the reader supplies
- Build & Test: exact commands to build, run, lint, test
- Contributing: how to propose a change, where the deeper docs live
- Security: responsible disclosure, sensitive-data warnings
- License: license terms
- Acknowledgments: credits, references, related projects





#### Documentation Links

Every reference document the repository carries earns a link from the README: each file under `docs/`, alongside root documents such as `CONTEXT.md` and `AGENTS.md`. Carry each link inside the sentence that explains its topic, in whichever Section already covers that topic, and gather the leftovers under Contributing.

<documentation-link-example>
Flags, exit codes, and piping behavior are set out in the [CLI reference](docs/cli-reference.md), and every error this tool raises is listed with its cause in [Troubleshooting](docs/troubleshooting.md).
</documentation-link-example>





#### Style

- format per [Style Guide Markdown Format](#style-guide-markdown-format)
- keep bullets and table cells terse per [Style Guide Briefness Style](#style-guide-briefness-style); prose stays in full sentences
- favor short Sections a visitor can scan in seconds
- use emoji, badges, and diagrams where they aid Navigation, not as decoration





#### Quality Expectations

- specific to this Repository, never generic
- backed by project information, never invented or padded
- honest about Status, limitations, and requirements
- command-oriented wherever install, build, run, and test flows are known
- complete on links: every reference document reachable from the README











### {description}

Writes and maintains human-friendly README files — scannable, visually clear landing pages covering a project's purpose, features, setup, usage, and contribution flow, linking every reference document inline within the explanation that names it, with a standard title format and tasteful use of headings, lists, badges, and emoji.

### {when_to_use}

Use when creating, updating, or reviewing a README or similar project landing page. Triggers: "write a README," "improve the README," documenting a repo's overview or quick-start.

### {globs}

```glob
**/{README,Readme,readme}{,.md,.txt}
```

































## Repository CHANGELOG Writer

these guidelines define what a good `CHANGELOG.md` (or CHANGELOG-style file) is





#### Guiding Principles

Changelogs are *for humans*, not machines.

- write entries a reader can act on, per [Style Guide Good Writing](#style-guide-good-writing)
- hold each entry to one terse line, per [Style Guide Briefness Style](#style-guide-briefness-style)
- format headings, lists, and callouts per [Style Guide Markdown Format](#style-guide-markdown-format)
Structure:
- group the same types of changes together
- keep every version and section linkable, with a links block at the foot of the file holding all of them
- keep an `[Unreleased]` section carrying all six subsections, even when empty
- omit empty subsections from released versions
Versions:
- carry every version, latest first, numbered per [Project Semantic Version](#project-semantic-version)
- show the release date beside each version




#### Types of Changes

- `Added`: new features
- `Changed`: changes in existing functionality
- `Deprecated`: soon-to-be removed features
- `Removed`: now removed features
- `Fixed`: any bug fixes
- `Security`: in case of vulnerabilities






#### CHANGELOG Example

```md
# Example Repository CHANGELOG

## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security

[unreleased]: https://github.com/example-user/example-project/compare/v2.0.0...dev

## [2.0.0] - 2024-01-15

### Removed

- Node 14 runtime support

> [!WARNING]
> Drops support for Node 14; upgrade before updating
[2.0.0]: https://github.com/example-user/example-project/compare/v1.5.7...v2.0.0

## [1.5.7] - 2023-12-04

### Fixed
- Profile picture not rendering correctly on Safari

[1.5.7]: https://github.com/example-user/example-project/compare/v1.5.6...v1.5.7

## [1.5.6] - 2023-11-02

### Added

- OAuth2 support for Google and GitHub providers

> [!CAUTION]
> Profile pictures fail to render on Safari; fixed in [1.5.7]

[1.5.6]: https://github.com/example-user/example-project/releases/tag/v1.5.6
```












### {description}

Writes and maintains CHANGELOG files per Keep a Changelog conventions — dated version entries newest-first, grouped change types, a persistent `[Unreleased]` section, and linkable version references.

### {when_to_use}

Use when creating, updating, or adding entries to a CHANGELOG, or recording changes for a release. Triggers: "update the changelog," "log this change," "document the release."

### {globs}

```glob
**/{CHANGELOG,Changelog,changelog}{,.md,.txt}
```

### {[Claude:Skill] Usage}

Invoke `sync-unit-test` skill via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `sync-unit-test` skill with `skill_view`.
































## Repository CONTEXT Writer

You write and maintain `CONTEXT.md` files for software repositories. Apply these rules to `CONTEXT.md` and to a personal `CONTEXT.local.md`, formatting both per [Style Guide Markdown Format](#style-guide-markdown-format).

#### CONTEXT Title & Preface

```markdown
# Example Repository CONTEXT

Descriptive knowledge of this repository for agents and developers.

- Belongs Here: what the system is, ie architecture, domain model, API surface, patterns, known gaps; only what the code cannot show, as it stands, never its history
- Size: stay lean for the context window; when the file grows, move detail to `docs/` or cut it
- Upkeep: update in the same change that moves architecture, patterns, commands, or environment variables
- Structure: follow the existing sections; keep every statement true for every contributor
- Belongs in `AGENTS.md`: prescriptive rules for agents, ie commands, conventions, constraints, do/don't
- Belongs in `docs/`: system documentation for users and agents alike; link it from here, never grow this file to hold it
- Local Layer: put machine-specific or personal context in `CONTEXT.local.md`; create it if missing, never commit it
```

Replace `Example Repository` with the real repository name. Copy the preface exactly, word for word.

The personal layer's title line, marked as local:

```markdown
# Example Repository local CONTEXT
```





#### Suggested Sections

Recommended, not mandatory — use what fits under clear `##` headings, and omit rather than pad. Humans and agents both parse structure faster than prose, so reach for tables, annotated trees, and ASCII diagrams wherever they carry more per token.

- Project Overview: what the app is, who it serves, major tech. A stack table works well
- Repository Layout: annotated tree of landmarks — what each key directory holds and why, not a raw `ls` dump
- Domain Model: entities, primary keys, key fields, foreign-key links. ASCII ERD plus a per-entity table
- API Surface: route prefixes, methods, request and response conventions. Saves reading every route file
- Patterns & Conventions: the highest-value section — where business logic lives, how data access and errors work, which naming to preserve
- Build, Run & Test Commands: exact commands, never descriptions. Lets an assistant verify its own work
- Environment Variables: a table of names, defaults, and descriptions
- Testing Strategy: tools, where tests live, fixture and test-database conventions
- Known Gaps & Constraints: underrated — flag mocked auth, a missing service layer, deliberately pinned-old libraries. Stops a reader building on absent infrastructure

Add any section carrying project-specific knowledge a newcomer or assistant needs — external services, migration flows, key abstractions, historical decisions. A starting point, not a ceiling.
In a monorepo, nest a `CONTEXT.md` per package for its own architecture and domain, the closest file being the most specific. In a large codebase, layer stack-specific patterns and anti-patterns beneath a base `CONTEXT.md`, keeping each file focused before instruction fatigue sets in. Local env quirks, workflow notes, and scratch understanding go in `CONTEXT.local.md`, which augments or overrides the committed shared source of truth without reaching teammates.





#### Living Document Maintenance

A stale briefing is worse than none. Instruct the reader to update the file when entities or services appear, patterns or boundaries shift, build and test workflows change, environment variables are introduced, or conventions are set.
Recommend in-file: update `CONTEXT.md` in the same pull request as the change; have the assistant that just made the change write it, as the final step; and keep the file on the pull-request checklist.





#### Quality Expectations

- repository-specific, never generic
- descriptive — a system map, not a command list
- structured for fast parsing, useful to humans and agents alike
- explicit on patterns, boundaries, and especially known gaps
- current, maintained alongside architecture changes
- complementary to `README.md` and `AGENTS.md`, duplicating neither













### {description}

`CONTEXT.md` is the **descriptive** knowledge layer: a dual-audience briefing for new developers and AI assistants on *what the codebase is* — architecture, data flow, domain model, API surface, patterns, conventions, known gaps. It goes deeper than the setup-focused `README.md` and is the foundational map other files build on; `CONTEXT.local.md` holds personal, gitignored context. This skill writes and maintains both.

### {when_to_use}

Use to create, update, or review `CONTEXT.md` or `CONTEXT.local.md`, or to capture durable codebase knowledge for AI across sessions. Triggers: "write a CONTEXT.md," "document the architecture for AI," "briefing doc for the repo." Difference from its sibling: `CONTEXT.md` is **descriptive** (what the system is — architecture, domain, patterns); `AGENTS.md` is **prescriptive** (commands, rules, constraints governing agent behavior). Route behavioral rules, commands-as-instructions, and do/don't constraints to `AGENTS.md`, not here.

### {globs}

```glob
**/{CONTEXT,Context,context}{,.local}{,.md}
```


































## Clean Up Branches

You delete **local** branches already merged into the current branch. Nothing else is in scope — no remote or remote-tracking refs, tags, stashes, worktrees, index, or working tree. Stop and say so if `HEAD` is detached or a merge, rebase, cherry-pick, or bisect is in progress.





#### Candidates

- take the set from `git branch --merged`, resolved against the current branch
- drop the current branch, protected branches (`main`, `master`, `develop`, `trunk`, `release/*`), and anything the user names
- a branch absent from that set is never a candidate, for any reason





#### Delete

`git branch -d` only. `-D` and `--delete --force` are forbidden, including as a retry; a refusal from `-d` stands — leave the branch and report it.

Present candidates and exclusions together and wait for an answer whenever the set is unclear: an unstated protected list, a candidate that looks like live work, or a current branch that is not the integration target. Deleting nothing is the correct outcome of an unanswered question. Once settled, pass every remaining name to a **single** `git branch -d` call — never loop, never one at a time.





#### Report

- each branch deleted, with the tip hash Git prints, so the user can recover it
- each branch skipped, and why
- if nothing qualified, say so in one line and stop













### {description}

Deletes local branches already merged into the current branch, with a report of what went and what stayed.

### {when_to_use}

Trigger on "clean up branches," "prune merged branches," or "delete old/stale branches."
## Open Pull Request

<!-- TODO create pull request skill -->

tmp content for Open Pull Request

### {description}

tmp description Open Pull Request

### {when_to_use}

tmp when_to_use Open Pull Request
