# kaye-library AGENTS

Prescriptive rules for agents working in this project.

- Belongs Here: rules an agent must follow, ie commands, conventions, constraints, who decides; only what an agent cannot infer from the code
- Size: stay lean for the context window; when the file grows, move detail to `docs/` or cut it
- Upkeep: update in the same change that moves a command, convention, or constraint
- Structure: follow the existing sections; keep every rule true for every contributor
- Belongs in `CONTEXT.md`: descriptive knowledge of the system, ie architecture, domain model, patterns, known gaps
- Belongs in `docs/`: system documentation for users and agents alike; link it from here, never grow this file to hold it
- Local Layer: put machine-specific or personal rules in `AGENTS.local.md`; create it if missing, never commit it

## Setup Commands

```bash
pip install -e ../kaye-engine -e '.[dev]'   # engine from the sibling checkout
kaye-library --help                         # verify the console script resolves
kaye-library blueprint list                 # every registered blueprint
```

Requires Python 3.11+. Importing `kaye_library` loads nothing: call `setup_kaye_library_for_kaye_engine()` (the console command and `tests/conftest.py` do) or compose the six steps in `kaye_library/__init__.py`.

## Layout & Naming

- `kaye_library/registrations/<group>/`: one folder per feature group, its corpus `.md` beside the `<group>_bp.py` and `<group>_glossary.py` that register it
- corpus files are listed in `_CORPUS_SOURCES` (`kaye_library/__init__.py`) with the node each registers under; a source's top headings sit one level below that node
- skill names carry no prefix; a workflow skill is `<verb>-<object>`, its verb unique among exportable names (`commit-sense`, `prune-merged-branches`); a reference skill keeps a noun lead (`style-`, `element-`, `coder-`, `glossary-`)
- register a skill under its final name; keep no alias

## Code Style

- follow PEP 8 within 80 characters; Sphinx docstrings; test files end `_test.py` under `tests/`
- `*_bp.py` imports of the corpus tree stay function-local: the tree loads after `kaye_library` is imported
- create a blueprint only in `registrations/`, through the helpers of `registrations/_common.py` (`register_exportable`, `register_prompt`, `register_abbr_glossary`), which bind this package's consumer; never call `register_blueprint` with `is_exportable=True` elsewhere
- a skill-backing corpus section needs `{description}` and `{when_to_use}` sidecars; blank spacer lines between sections are deliberate, keep them

## Content Rules

- keep every prompt persona-free and free of personal data: no names, contact data, accounts, or schedules; a personal taste expressed as a rule ships as a default a consumer overrides with `override_exportable`; a personal value spliced by a `(((placeholder)))` is registered by the consumer only, since a second registration of a glossary or substitution raises `ValueError`, so the library skill renders that placeholder literally when run alone
- a skill that splices such a consumer-registered placeholder is listed in `_PERSONAL_PLACEHOLDER_SKILLS` (`tests/skill_export_test.py`), which exempts it from the unresolved-placeholder check
- never name a downstream package in code, corpus, docs, tests, or commit messages
- an abbreviation entry belongs in `kaye_library/abbrs.json` only when a glossary that library text splices needs it; name only glossaries this package registers
- `tests/privacy_test.py` scans every shipped file for private strings: extend its list, never trim it

## Testing Instructions

Scope each run to the area touched; run everything only before a merge.

| changed | run |
|---|---|
| a corpus `.md` or a `*_bp.py` | `pytest tests/skill_export_test.py` plus the group's test (`tests/coder_test.py`, `tests/agent_test.py`, `tests/commit_sense_test.py`, `tests/general_test.py`) |
| a glossary or `abbrs.json` | `pytest tests/glossary_test.py tests/abbr` |
| setup, `__main__.py`, the consumer record | `pytest tests/library_setup_test.py tests/console_test.py tests/third_consumer_test.py` |
| any shipped file | `pytest tests/privacy_test.py` |
| an `Invoke ... skill` line in a corpus `.md` | `pytest tests/invocation_test.py` |
| `README.md`, `AGENTS.md`, `CONTEXT.md`, `docs/` | `pytest tests/docs_test.py` |
| before a merge | `pytest tests` |

- `tests/data.py` holds the wording each skill must render; update it in the same change as the text
- `tests/console_test.py` runs `kaye-library` as a subprocess: install the package first
- `tests/invocation_test.py` fails when library text tells the assistant to invoke a skill the library does not register: point it at a library skill, never at one a downstream package supplies
- `tests/docs_test.py` checks every relative link and anchor in the root documents and `docs/`
- never run `kaye-library claude code`, `vs-code-extension`, or `marketplace` without a folder argument while testing: they write into the real `~/.claude/`

## PR & Commit Instructions

- branch from `dev`; work lands on `dev`
- record every notable change under `[Unreleased]` in `CHANGELOG.md`

## Security Considerations

- never commit secrets, tokens, or personal data
- exports write to `~/.claude/` by default: pass a folder when testing

## Documentation Maintenance

- [README.md](README.md): overview, install, commands
- [CONTEXT.md](CONTEXT.md): architecture and the root node ownership; refresh its `Last updated` line
- [docs/blueprint-doc.md](docs/blueprint-doc.md): every skill and internal blueprint; update on any blueprint added, renamed, or re-wired
- [docs/glossary-doc.md](docs/glossary-doc.md): every glossary and its usage; update on any glossary added or re-wired
- [docs/corpus-registration-doc.md](docs/corpus-registration-doc.md): how sources attach to the tree; update when `_CORPUS_SOURCES` or the registration rules change
- [docs/boundary-doc.md](docs/boundary-doc.md): what crosses the boundary; update when a rule about consumers, overrides, or abbreviation layers changes
- `CHANGELOG.md`: notable changes per release
