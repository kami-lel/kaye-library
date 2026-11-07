# kaye-library CHANGELOG

<!--
todo support layered CONTEXT/AGENTS
-->

## [Unreleased]

### Added

- `amanuensis-config-keybinding-controller` glossary: face buttons, bumpers & triggers as letter emoji 🄻 🅁 🅻 🆁, sticks, d-pad, view & menu symbols
- `amanuensis-config-keybinding-keyboards` glossary: mouse & mouse movement symbol 🖰, listed first
- `amanuensis-config-keybinding-mouse` glossary: left, right, middle click & wheel, buttons 4 & 5
- Keybinding Writer: stick press/push & wheel direction modifiers, L/R prefix for modifier keys

### Changed

- keyboard-key glossary renamed `amanuensis-keybinding-writer-shorthand` → `amanuensis-config-keybinding-keyboards`
- arrow-key symbols ↑ → ← ↓ → black arrowheads ⮝ ⮞ ⮜ ⮟, no clash w/ increase/become/decrease shorthand

### Deprecated

### Removed

### Fixed

### Security

[unreleased]: https://github.com/kami-lel/kaye-library/compare/v1.2.0...dev













## [1.2.0] - 2026-11-06

### Added

- GitHub Release workflow: a `v*` tag builds the plugin zip and attaches it to a release, a pre-release for `-alpha` and `-beta` tags
- Hermes tool usage nodes beside the Claude ones, so a `hermes` render carries Hermes tool instructions
- `working-with-git` and `working-with-p4v` skills: Git working terms and approval rules, Perforce terms paired with Git equivalents

### Changed

- `kaye-engine` dependency is a git reference at tag `v11.0.0`, as it is not on PyPI
- Claude tool sidecars take the single `Claude:` prefix; Chat and Cowork twins of the Gmail, TickTick, and Google Calendar usage nodes merge
- `commit-sense`: line counts from `git diff --cached --numstat` settle sigil Lean and Size
- `plan-for-suite`: Movement Heading is an `h3` marking a non-own party in `{}`

> [!WARNING]
> requires `kaye-engine` v11.0.0; packages building on the library must upgrade their engine pin before updating

[1.2.0]: https://github.com/kami-lel/kaye-library/compare/v1.1.1...v1.2.0

## [1.1.1] - 2026-10-30

### Changed

- `agent-unreachable-task-workaround`: the several-items example links the release page

[1.1.1]: https://github.com/kami-lel/kaye-library/compare/v1.1.0...v1.1.1














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
