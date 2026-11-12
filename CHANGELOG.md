# kaye-library CHANGELOG

<!--
todo support layered CONTEXT/AGENTS
-->

## [Unreleased]

### Added

- `commit-sense-branch-merging`: exportable skill for merging a branch with a typed primary summary; was the internal `git-sense-branch-merging`
- `docs/blueprint-doc.md`: the blueprint dependency and invocation graphs
- `proj-version-title`: version release title as bump word, release type, version; depends on the internal `proj-version-bump`
- `u3d-assets-management`: optional asset domain level between asset type and asset module (`Scripts/Mobs/Spider/`), with common domains (`Mobs`, `World`, `Cameras`, `Items`, `Player`, `UI`, `Combat`, `Interactables`) and audio-only `BGMs/`, `SFXs/`

### Changed

- Perforce corpus and registration moved to their own `registrations/p4v/` module; `working-with-p4v` unchanged
- README is rewritten as a pitch, with a Contributing path into the dev-side `kaye-engine` docs
- `u3d-assets-management`: rewritten around asset type, asset domain, and asset module; `Audio/BGM/`, `Audio/SFX/` renamed `Audio/BGMs/`, `Audio/SFXs/`
- `u3d-naming`: dev prefix `dev` → `DEV` (`DEVJohnMainScene.unity`), now also covering dev-only assets (`DEVSandboxScene.unity`)

### Deprecated

### Removed

- `Repositories` corpus root and `registrations/repo/`: merged into `registrations/git/` under the one `Git` root, split as `git.md`, `repo.md`, `workflow.md`, `branch.md`; `repo-*` slugs unchanged
- `docs/`: its content moved into `CONTEXT.md`, and the consumer guide became the Consumer documentation in `kaye-engine`

### Fixed

### Security

[unreleased]: https://github.com/kami-lel/kaye-library/compare/v1.2.1...dev













## [1.2.1] - 2026-11-09

### Added

- keybinding glossaries for controller, mouse & mouse movement (`amanuensis-config-keybinding-controller`, `-mouse`, `-keyboards`): buttons, bumpers & triggers, sticks, d-pad, clicks, wheel
- Keybinding Writer: stick press/push, stick axis (vertical ⇧Ⓛ⇩, horizontal ⇦Ⓛ⇨) & wheel direction modifiers, L/R prefix for modifier keys

##### Unity Engine

- standalone `u3d-*` skills, 1 per section: naming, type suffixes, coding, inspector fields, prefabs, owner-driven activation, game tuning
- naming: new role suffixes, asset naming rules
- coding rules: inspector fields, `ScriptableObject` shape, units, input via `InputAction`s
- game tuning: tunable values in data, curves for dependent values
- assets management: `Meshes/` & `Plugins/` folders

### Changed

- git-abbr: `icc` → `ig`, `cci` → `gi`, `cc` → `g`; "then continue" dropped
- "unknown" shorthand `??` → `⁇`, new alt `❓`
- keyboard-key glossary renamed `amanuensis-keybinding-writer-shorthand` → `amanuensis-config-keybinding-keyboards`
- arrow-key symbols ↑ → ← ↓ → black arrowheads ⮝ ⮞ ⮜ ⮟, no clash w/ increase/become/decrease shorthand

##### Unity Engine

- split out of Coder into own module; skills & glossaries `coder-u3d*` → `u3d*`
- corpus reorganized around naming, coding & game tuning
- assets management: type folders pluralized (`Inputs/`, `VFXs/`)

> [!WARNING]
> skills `coder-u3d`, `coder-u3d-mb`, `coder-u3d-so`, `coder-u3d-assets-management` and glossaries `coder-u3d-abbr`, `coder-u3d-identifier` are renamed; update every reference to the `u3d*` names before upgrading

[1.2.1]: https://github.com/kami-lel/kaye-library/compare/v1.2.0...v1.2.1













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
