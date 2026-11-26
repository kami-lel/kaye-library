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

### {[Claude:Skill] Usage}

Invoke `create-readme`, `create-changelog`, `create-repo-agents`, and `create-repo-docs` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `create-readme`, `create-changelog`, `create-repo-agents`, and `create-repo-docs` skills with `skill_view`.


































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

### {when_to_use}

Trigger on "write a README", "create a README", "this repo has no README", or a new project needing a landing page.


































## Maintain README

1. take what changed from the conversation, then diff it against the current README to find stale, missing, or inaccurate content
2. edit in place, preserving structure and scope that still hold
3. cut what is stale, misleading, duplicated, or obsolete
4. verify every link, path, command, config name, and example against the codebase
5. prioritize the root README, keeping secondary ones scoped to their own area
6. update the README in place, then return a brief summary of the changes, per [Repository README Writer](#repository-readme-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Updates an existing README to match the current project state — correcting stale overviews, commands, links, configuration names, and examples, pruning obsolete or duplicated content, and editing in place against the latest repository changes.

### {when_to_use}

Trigger on "update the README", "the README is stale", "sync the README with the code", or a README showing old commands or names.


































## Create CHANGELOG

1. reconstruct project history from git tags, releases, and the commit log
2. take release dates and anything the repository has not captured from the conversation
3. write one versioned section per release, newest first, each carrying its date, titled per [CHANGELOG Title](#changelog-title)
4. open with an empty `[Unreleased]` section holding all six subsections
5. close with a links block referencing every version
6. create `CHANGELOG.md` at the project root, for a repository that has none, per [Repository CHANGELOG Writer](#repository-changelog-writer), numbering versions per [Project Semantic Version](#project-semantic-version). Format per [Style Guide Markdown Format](#style-guide-markdown-format), keep entries terse per [Style Guide Briefness Style](#style-guide-briefness-style), and write per [Style Guide Good Writing](#style-guide-good-writing)





#### CHANGELOG Title

```markdown
# <Repository Name> CHANGELOG
```

Replace `<Repository Name>` with the real repository name.





### {description}

Bootstraps a `CHANGELOG.md` for a repo that has none — reconstructing dated, versioned sections from git history newest-first, with an `[Unreleased]` block and version links.

### {when_to_use}

Trigger on "create a changelog", "start a CHANGELOG", "rebuild the changelog from git history", or a repository with no `CHANGELOG.md`.


































## Maintain CHANGELOG

1. take what to log from the conversation and recent repository changes
2. file each entry under the right subsection of `[Unreleased]`, the default target for new work
3. combine with existing entries rather than duplicating; leave their wording as it stands
4. keep the links block current so every version stays referenced
5. edit in place
6. update the CHANGELOG in place, then return a brief summary of the changes, per [Repository CHANGELOG Writer](#repository-changelog-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Use this skill when the user wants to add, fix, or reorganize entries in an existing CHANGELOG — logging new features, bug fixes, or breaking changes without overwriting existing content. Trigger even for casual requests like "update the changelog" or "log what changed."

### {when_to_use}

Trigger on "update the changelog", "log what changed", "add a changelog entry", or "fix a changelog entry".



































## Create CREDITS

1. inventory the third-party material the repository ships: asset folders, fonts, audio, vendored code, bundled libraries
2. read the license, readme, and attribution files shipped beside each, and any credits already in the README, DEVLOG, or build notes
3. take sources, authors, and licenses the repository has not captured from the conversation, and, when the user wants them, the contributors with their roles and the acknowledgments
4. write one row per asset under its section, marking every field nobody can confirm `unknown`
5. create `CREDITS.md` at the project root, for a repository that has none, per [Repository CREDITS Writer](#repository-credits-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing), then return a brief summary listing every `unknown` field





### {description}

Bootstraps a `CREDITS.md` for a repository that has none, inventorying every third-party asset, font, sound, and bundled library it ships, with each one's source, author, and license.

### {when_to_use}

Trigger on "create a credits file", "credit our assets", "list the third-party assets", or a repository shipping third-party material with no `CREDITS.md`.

































## Maintain CREDITS

1. take added, moved, replaced, and removed third-party material from the conversation and recent repository changes
2. add a row for each new asset under its section, opening the section when the kind is new; add or update a contributor or acknowledgment the conversation names
3. update a row whose path, role, or modification changed; remove a row whose asset has left the repository
4. leave rows that still hold as they stand
5. verify every path against the repository and every link
6. update the CREDITS in place, then return a brief summary of the changes, listing any `unknown` field, per [Repository CREDITS Writer](#repository-credits-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Updates an existing `CREDITS.md` against what changed: adds rows for new third-party assets, updates moved or modified ones, removes those the repository no longer ships.

### {when_to_use}

Trigger on "update the credits", "credit this new asset", "add attribution for", or a third-party asset added, moved, or removed.

































## Create DEVLOG

1. reconstruct the project's history from the commit log, tags, `CHANGELOG.md`, and any playtest, survey, or meeting notes in the repository
2. take the reporting cadence, the setting, and the reasons behind decisions from the conversation; ask for the cadence when neither gives it
3. group the history into periods, and write one entry per period worth telling, newest first
4. write a reason only where the record or the conversation gives one, never a guessed motive
5. create `DEVLOG.md` at the project root, for a repository that has none, per [Repository DEVLOG Writer](#repository-devlog-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing), then return a brief summary listing every entry written





### {description}

Bootstraps a `DEVLOG.md` for a repository that has none, reconstructing one entry per period, newest first, from the commit log, tags, CHANGELOG, and playtest notes.

### {when_to_use}

Trigger on "start a devlog", "create a DEVLOG", "write a dev diary from the history", or a repository with no `DEVLOG.md`.

































## Maintain DEVLOG

1. take the period's work from the conversation, the commits since the newest entry, `[Unreleased]` in the CHANGELOG, and any new playtest, survey, or review notes
2. add a new entry directly under the title, or extend the newest entry when it covers the current period
3. tie every fix to its finding and every change of approach to its reason; ask for a reason the record does not give, never invent one
4. save each screenshot the user supplies into `DEVLOG-assets/`, named and captioned per [Repository DEVLOG Writer](#repository-devlog-writer), leaving a Loud `TODO` wherever a needed screenshot is missing; chart the period's data in Mermaid where it fits
5. leave past entries as written, except to correct a factual error or point a leftover forward to the entry that takes it up
6. update the DEVLOG in place, then return a brief summary of the changes, per [Repository DEVLOG Writer](#repository-devlog-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing)





### {description}

Adds the current period's entry to an existing `DEVLOG.md`: findings, fixes tied to them, other work, leftovers, and captioned screenshots, leaving past entries as written.

### {when_to_use}

Trigger on "write this week's devlog", "add a devlog entry", "log the playtest findings", or a period's work ready to record.

































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

### {when_to_use}

Trigger on "condense the changelog", "tidy the Unreleased section", "reword the changelog for release", or "add Breaks and Hazards".




































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

### {when_to_use}

Trigger on "before compact", "context is about to compact", "save this session's progress", or "log the session's changes before the context fills".

### {[Claude:Skill] Usage}

Invoke `maintain-changelog` and `maintain-repo-agents` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `maintain-changelog` and `maintain-repo-agents` skills with `skill_view`.
