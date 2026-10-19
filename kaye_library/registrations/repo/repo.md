# Repositories

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
- keep bullets and table cells terse per [Style Guide Briefness Style](#style-briefness-style); prose stays in full sentences
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
- hold each entry to one terse line, per [Style Guide Briefness Style](#style-briefness-style)
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

### {[ClaudeCode:Skill] Usage}

Invoke `sync-unit-test` skill via `Skill` tool.
































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


































## Initialize Repository

Bootstrap a repository's baseline documentation from nothing, in one pass. Write everything per [Style Guide Markdown Format](#style-guide-markdown-format) and [Style Guide Good Writing](#style-guide-good-writing).





#### Instructions

- inspect the repository once — layout, configs, manifests, scripts, tests — and take the rest from the conversation. Reuse those findings across every step below

- run each create skill in order, skipping any whose target file already exists:

  1. [Create README](#create-readme) → `README.md`, per [Repository README Writer](#repository-readme-writer)
  2. [Create CHANGELOG](#create-changelog) → `CHANGELOG.md`, per [Repository CHANGELOG Writer](#repository-changelog-writer)
  3. [Create Repository AGENTS](#create-repository-agents) → `AGENTS.md`, per [Repository AGENTS Writer](#repository-agents-writer)
  4. write `CONTEXT.md` directly, per [Repository CONTEXT Writer](#repository-context-writer)
  5. [Create Repository Docs](#create-repository-docs) → files under `docs/`

- split by purpose and never duplicate: human onboarding → README, release history → CHANGELOG, agent behavior → AGENTS, system knowledge → CONTEXT, topic deep-dives → `docs/`
- write a file or section only where project information supports it





#### Output
Create the documentation files at their standard locations.
Return a brief summary listing every file created.














### {description}

Bootstraps a repository's entire baseline documentation set in one pass — `README.md`, `CHANGELOG.md`, `AGENTS.md`, `CONTEXT.md`, and `docs/` — from a single repository inspection, splitting content by purpose with no duplication and skipping files that already exist.

### {when_to_use}

When a bare repo needs its documentation scaffolded all at once — "set up docs," "set up this project/repo," "document this project," "create the docs from scratch." Not for updating or fixing existing docs.

### {[ClaudeCode:Skill] Usage}

Invoke `create-readme`, `create-changelog`, `create-repo-agents`, and `create-repo-docs` skills via `Skill` tool.


































## Create README

1. inspect the repository for structure, then draw material from its docs, config, manifests, and source
2. take intent and anything the repository has not captured from the conversation
3. write a section only where project information supports it, titled per [README Title](#readme-title)
4. create `README.md` at the project root, for a repository that has none, per [Repository README Writer](#repository-readme-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)






#### README Title

```markdown
# <Repository Name> README
```

Replace `<Repository Name>` with the real repository name.





### {description}

Use this skill when the user wants to create a new `README.md` from scratch — covering project overview, setup, usage, configuration, and contributing guidelines. Trigger even for casual requests like "write a readme" or "document this project."


































## Maintain README

1. take what changed from the conversation, then diff it against the current README to find stale, missing, or inaccurate content
2. edit in place, preserving structure and scope that still hold
3. cut what is stale, misleading, duplicated, or obsolete
4. verify every link, path, command, config name, and example against the codebase
5. prioritize the root README, keeping secondary ones scoped to their own area
6. update the README in place, then return a brief summary of the changes, per [Repository README Writer](#repository-readme-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Updates an existing README to match the current project state — correcting stale overviews, commands, links, configuration names, and examples, pruning obsolete or duplicated content, and editing in place against the latest repository changes.


































## Create CHANGELOG

1. reconstruct project history from git tags, releases, and the commit log
2. take release dates and anything the repository has not captured from the conversation
3. write one versioned section per release, newest first, each carrying its date, titled per [CHANGELOG Title](#changelog-title)
4. open with an empty `[Unreleased]` section holding all six subsections
5. close with a links block referencing every version
6. create `CHANGELOG.md` at the project root, for a repository that has none, per [Repository CHANGELOG Writer](#repository-changelog-writer), numbering versions per [Project Semantic Version](#project-semantic-version). Format per [Style Guide Markdown Format](#style-guide-markdown-format), keep entries terse per [Style Guide Briefness Style](#style-briefness-style), and write per [Style Guide Good Writing](#style-guide-good-writing)





#### CHANGELOG Title

```markdown
# <Repository Name> CHANGELOG
```

Replace `<Repository Name>` with the real repository name.





### {description}

Bootstraps a `CHANGELOG.md` for a repo that has none — reconstructing dated, versioned sections from git history newest-first, with an `[Unreleased]` block and version links.


































## Maintain CHANGELOG

1. take what to log from the conversation and recent repository changes
2. file each entry under the right subsection of `[Unreleased]`, the default target for new work
3. combine with existing entries rather than duplicating; leave their wording as it stands
4. keep the links block current so every version stays referenced
5. edit in place
6. update the CHANGELOG in place, then return a brief summary of the changes, per [Repository CHANGELOG Writer](#repository-changelog-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Use this skill when the user wants to add, fix, or reorganize entries in an existing CHANGELOG — logging new features, bug fixes, or breaking changes without overwriting existing content. Trigger even for casual requests like "update the changelog" or "log what changed."



































## Condense CHANGELOG

1. reword every `[Unreleased]` entry into changelog style — concise, high-level, free of implementation detail
2. keep existing subsections and their grouping; drop nothing that still applies
3. for each entry, judge whether it warrants an [Admonition for Breaks or Hazards](#admonitions-for-breaks-and-hazards), and add it under the relevant `[Unreleased]` subsection when it does
4. update the CHANGELOG in place, then return a brief summary of the changes, per [Style Guide Markdown Format](#style-guide-markdown-format) and [Style Guide Good Writing](#style-guide-good-writing)




#### Admonitions for Breaks and Hazards

Two kinds, each placed under the relevant subsection. Both are exceptional — a changelog with nothing dangerous to say carries none.

- `> [!WARNING]`: a break in the **public** interface — removed or renamed api, changed signature or return, dropped runtime or platform. Name what broke and what the reader must do before upgrading
- `> [!CAUTION]`: a bug serious enough that staying on an affected version is a hazard. Name the symptom and, once known, the version that fixes it




### {description}

Condenses `CHANGELOG.md`'s `[Unreleased]` section for release: rewords its entries into concise, high-level changelog style and adds Admonitions for Breaks and Hazards where warranted.




































## Condense AGENTS and CONTEXT

You work from the **files alone**: no change set, no conversation to draw on, nothing new to add. Every line already there is read once and then kept, shortened, moved, or dropped.

1. read each file whole, judging every section on whether it still earns the space it takes
2. drop what has gone stale: a workflow nobody follows now, a plan already landed or abandoned, a migration finished, an implementation detail the code has since moved past
3. drop what the code already answers on its own — restated file trees, signatures, config values, anything a reader would check in the source before believing the document
4. merge what repeats within a file, and move anything sitting on the wrong side of the pair to its counterpart rather than restating it
5. shorten what survives: same meaning, fewer words, AGENTS directive and imperative, CONTEXT descriptive and explanatory
6. hold AGENTS lean enough to stay in context: the commands an agent must run and the rules it must obey, nothing more
7. hold CONTEXT to what explains the system as it stands, never to how it came to stand that way
8. add nothing the files did not already carry; name a gap you find in your summary rather than filling it
9. update the files in place, then return a brief summary of the changes, per [Repository AGENTS Writer](#repository-agents-writer), [Repository CONTEXT Writer](#repository-context-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)




### {description}

Shrinks an existing AGENTS and CONTEXT pair: reads both whole, drops finished plans, dead workflows, superseded detail, anything the code already answers, tightens the rest, adds nothing

### {when_to_use}

Fires when the pair has outgrown its content: an `AGENTS.md` too long to keep in context, a "Planned" or "In Progress" or "Migration" section describing finished work, a directory tree the source now contradicts, one rule stated in both files. Also "AGENTS.md is 600 lines", "cut CLAUDE.md down", "why is CONTEXT.md so long". Apply unasked before a release or handoff. Not when new work needs recording








































## Maintenance Before Compact

Before context is compacted, capture this session's durable changes so nothing is lost — log them and update the agent-facing docs. Format per [Style Guide Markdown Format](#style-guide-markdown-format) and write per [Style Guide Good Writing](#style-guide-good-writing).





#### Instructions

- identify the session's changes once, from the conversation, working diffs, and existing `[Unreleased]` entries, then reuse that set below
- [Maintain CHANGELOG](#maintain-changelog) → record those changes; the unreleased-only and deduplication rules come from that skill
- [Maintain Repository AGENTS](#maintain-repository-agents) → update for any command, convention, or constraint the session moved
- update `CONTEXT.md` directly for any architecture the session moved, per [Repository CONTEXT Writer](#repository-context-writer)
- skip a step the session gives nothing relevant to





#### Output

Update the affected files in place, leaving unrelated files untouched.












### {description}

Logs a session's durable changes before context compaction — recording them in `CHANGELOG.md` and syncing `AGENTS.md` and `CONTEXT.md` — identifying the change set once from the conversation, working diffs, and existing `[Unreleased]` entries.

### {[ClaudeCode:Skill] Usage}

Invoke `maintain-changelog` and `maintain-repo-agents` skills via `Skill` tool.


































## Prepare for Feature Landing

Before merging the current [feature branch](#feature-branch), sync the docs it affects. Work in Movements; edit affected files in place and leave the rest untouched.





#### Movement 1~3: Sync Unit Test

If the project has unit tests, run [Sync Unit Test](#sync-unit-test) first.



##### {[ClaudeCode:Skill] Usage}

Invoke `sync-unit-test` skill via `Skill` tool.






#### Movement 4: Learn the Feature Branch

Identify the change set, then use it throughout Movement 5 & 6:

- read the current conversation for what was built and why
- observe the [feature branch](#feature-branch) as the change set
- fold in existing `[Unreleased]` entries so nothing is recorded twice





#### Movement 5: Record the Change Set in the CHANGELOG

Run [Maintain CHANGELOG](#maintain-changelog), recording the change set per [Repository CHANGELOG Writer](#repository-changelog-writer). The unreleased-only and deduplication rules come from that skill.






#### Movement 6: Sync AGENTS and CONTEXT

Run [Maintain Repository AGENTS](#maintain-repository-agents), updating any command, convention, or constraint the branch moved, per [Repository AGENTS Writer](#repository-agents-writer). Then update `CONTEXT.md` directly for any architecture the branch moved, per [Repository CONTEXT Writer](#repository-context-writer).





### {description}

Records a feature branch's changes into `CHANGELOG.md` and updates `AGENTS.md` and `CONTEXT.md` to match, syncing all affected docs in one pass before a merge.

### {when_to_use}

Reach for this when wrapping up or merging a feature branch — "prep for merge," "finish this feature," "document what I changed," "update docs before merging." Not for cutting a versioned release (use the release skill) or general doc edits unrelated to a branch.





### {[ClaudeCode:Skill] Usage}

Invoke `sync-unit-test`, `maintain-changelog`, and `maintain-repo-agents` skills via `Skill` tool.


































## Perform Feature Landing

tmp content for Perform Feature Landing

### {description}

tmp description Perform Feature Landing

### {when_to_use}

tmp when_to_use Perform Feature Landing


































## Prepare for Version Release

Cut a new release: bring all docs current, finalize the changelog, and bump the project version.



#### Movement 1: Decide Release Version and Date

- require both a version number and a release date; if either is missing, ask the user before proceeding
- the version must match [Project Semantic Version](#project-semantic-version)



#### Movement 2: Maintain the README

Run [Maintain README](#maintain-readme): overview, features, setup, usage, version-dependent details.



#### Movement 3: Condense AGENTS and CONTEXT

Run [Condense AGENTS and CONTEXT](#condense-agents-and-context): changed commands, conventions, constraints, architecture.

While in `CONTEXT.md`, prune as well as update: keep only what describes the released state, and cut superseded plans, stale notes, and history no longer worth a reader's time. The file should end up smaller, not just newer.



#### Movement 4: Maintain the Docs Directory

Run [Maintain Repository Docs](#maintain-repository-docs): affected files under `docs/`.



#### Movement 5: Condense the Changelog

Run [Condense CHANGELOG](#condense-changelog) to reword `[Unreleased]` entries into changelog style and settle any Admonitions for Breaks and Hazards.



#### Movement 6: Close Out the Changelog

1. move every (now-condensed) `[Unreleased]` entry, admonitions included, into a new versioned section headed with the version and date from Movement 1, keeping only non-empty subsections
2. leave a fresh `[Unreleased]` section above it, carrying every standard subsection heading with no entries beneath
3. update the GitHub comparison links so every version, including the new tag, stays referenced



#### Movement 7: Bump the Repository Version

Set the version to match Movement 1 exactly, in whichever metadata files apply — `setup.cfg`, `pyproject.toml`, `package.json`, `Cargo.toml`, and the like.













### {description}

Cuts a project release: brings `README.md`, `CHANGELOG.md`, `AGENTS.md`, `CONTEXT.md`, and `docs/` current, moves `[Unreleased]` changelog entries into a dated versioned section, and bumps the version across metadata files like `package.json`, `pyproject.toml`, `Cargo.toml`, or `setup.cfg`.

### {when_to_use}

Reach for this on release requests — "ship v1.2.3," "cut a release," "tag a version," "bump the version," "prep the release." Not for logging a single in-progress change (use the changelog-maintain skill) or landing a feature branch before merge (use the feature-landing skill).





### {[ClaudeCode:Skill] Usage}

Invoke `maintain-readme`, `condense-changelog`, `condense-agents-and-context`, and `maintain-repo-docs` skills via `Skill` tool.

### {[ClaudeCode:AskUserQuestion] Usage}

- if version number or release date is **missing**, use `AskUserQuestion` to ask user before proceeding





### {[git] Usage}

Invoke `clean-up-branches` as Movement 5, if any branch needs pruning. Movements 5~7 renumber to 6~8


































## Perform Version Release

tmp content for Perform Version Release

### {description}

tmp description Perform Version Release

### {when_to_use}

tmp when_to_use Perform Version Release


































