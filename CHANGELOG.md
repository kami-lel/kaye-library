# kaye-library CHANGELOG

<!--
Fixme email category: Commercial, Entertainment

Todo workaround: how to deal w/ mux items
Todo add p4v instruction, use git terms

todo add gh release script
-->

## [Unreleased]

### Added

- `hunt-job-opportunity`, `good-morning`, `good-week`: the job hunt and the daily and weekly check-ins join the Secretary skills
- Secretary skills: `draft-email`, `sweep-email-inbox`, `scan-event-radar-daily`/`-weekly`, `secretary-event-brief-format`, calendar and GTD push/pull, `recap-yesterday`/`-today`, with the Common Report Info Field leaves and the `secretary-common-shorthand`, `secretary-eisenhower-matrix-quadrant`, `secretary-eisenhower-matrix-quadrant-base` glossaries; a skill that splices a personal glossary or substitution renders that placeholder literally until a consumer registers it
- Amanuensis writers: Chicago Citation, `bibliographer`, `assemble-bibliography`, `redactor`, `dispositor`, `scholiast`, `config-writer`, `keybinding-writer`, `minutes-clerk`, with the `amanuensis-config-writer-shorthand` and `amanuensis-keybinding-writer-shorthand` glossaries and their abbreviation entries
- Meta Prompt: `write-llm-prompt` and the `write-skill-description`, `write-skill-when-to-use`, `write-skill-description-and-when-to-use` writers, with the internal `meta-prompt` and `write-for-skill` bases
- internal `agent-unreachable-task-workaround` blueprint: the procedure for a task whose needed information cannot be obtained
- `plan-for-suite`: a Party per Movement, so a Movement can belong to the user or another party, and a `Movement Heading` format for the Plan file
- `plan-for-suite-execution`: guides the user step by step through a user Movement before it closes
- `coder-u3d`: owner-driven activation pattern, with apply and don't-apply cases and rules

### Changed

- `Perform Commit Sense Core` corpus section: the persona-free commit procedure body; `Perform Commit Sense` keeps only the skill sidecars, and the rendered skill heading reads `Perform Commit Sense Core`
- `commit-sense` and `coder`: each registered once under its own name, with no separate `-core` blueprint; a package takes a skill over by building on the library blueprint object
- `coder-u3d-abbr` and `coder-u3d-identifier` gain abbreviations for effects, hierarchy, and editor terms
- `plan-for-suite`: Bar 1 and Bar 2 headings rise from h4 to h3

### Deprecated

### Removed

### Fixed

- `commit-sense`: file ledger names file w/ extension, not directory path

### Security

[unreleased]: https://github.com/kami-lel/kaye-library/compare/v1.0.0...dev













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
