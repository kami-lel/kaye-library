# kaye-library CHANGELOG

<!--
todo add gh release script
-->

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

[unreleased]: https://github.com/kami-lel/kaye-library/compare/v1.1.0...dev














## [1.1.0] - 2026-10-30

### Added

- Secretary skills: email drafting and sweeping, daily and weekly event radar, calendar and GTD push and pull, daily recaps, job hunt, morning and weekly check-ins, with their report-field blueprints and glossaries; personal placeholders render literally until a consumer registers them
- Amanuensis writers: Chicago citation, bibliographer, bibliography assembly, redactor, dispositor, scholiast, config, keybinding, minutes clerk, with their glossaries
- Meta Prompt writers: LLM prompt and skill `description` / `when_to_use` writers
- `agent-unreachable-task-workaround` blueprint: one 🚧 line per blockage, closing 🙋 line asking for what clears it
- `plan-for-suite`: a Party per Movement and a Movement Heading format; `plan-for-suite-execution` guides the user through a user Movement
- `coder-u3d`: owner-driven activation pattern
- `p4v:Perforce` joins the programming language codes glossary

### Changed

- `commit-sense` and `coder`: one registration each, no `-core` blueprint; a package takes either over by building on the library blueprint object
- `coder-u3d` abbreviations extended for effects, hierarchy, and editor terms
- `plan-for-suite`: Bar 1 and Bar 2 headings rise from h4 to h3

> [!WARNING]
> `commit-sense-core` and `coder-core` blueprints are gone; packages building on them must take the library `commit-sense` / `coder` blueprint object instead

### Fixed

- `commit-sense`: file ledger names the file with its extension, not the directory path

[1.1.0]: https://github.com/kami-lel/kaye-library/compare/v1.0.0...v1.1.0













## [1.0.0] - 2026-10-19

### Added

- library package on kaye-engine: `kaye-library` command, standalone setup, no persona anywhere
- Style: Markdown format, heading separation, letter cases, briefness, good writing
- Elements: date-time formats, units, triage tags, ASCII only, phonetic alphabet, sequence numbering
- Git: `commit-sense` w/ per-file ledger & optional co-author trailer, `resolve-merge-conflict`, `prune-merged-branches`, `submit-pr` stub
- Repositories & Projects: README, CHANGELOG, AGENTS, CONTEXT, docs writers, `ready-land-feature`, `ready-release-version`, `land-feature` & `release-version` stubs
- Agentic: Movement & Suite, `halt-each-movement`, `cascade-all-movements`, Turn Progress Dispatch
- Coder: `# Coder` rules, `coder-core`, persona-free `coder` skill over it, plan, sync-test & `review-gaps` workflows, 12 language profiles
- `rapid` blueprint, `(today)` node, 10+ glossaries w/ own `abbrs.json`
- console command on engine main parser: shared `--help` text, own usage line & `--version`; `KAYE_LIBRARY_DISPLAY_NAME` names consumer record & comment line
- `claude plugin`, `claude marketplace`, `skill`, `blueprint` & other engine subcommands work standalone; chat-bound ones exit 1 w/ clear message
- tests: skill export as folders & zips, standalone setup, third-consumer registration, privacy scan, skill invocations resolve, doc links resolve
- docs: README, AGENTS, CONTEXT, blueprint, glossary, corpus registration & boundary documents

[1.0.0]: https://github.com/kami-lel/kaye-library/releases/tag/v1.0.0
