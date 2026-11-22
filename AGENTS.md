# kaye-library AGENTS

Prescriptive rules for agents working in this project.

- Belongs Here: rules an agent must follow, ie commands, conventions, constraints, who decides; only what an agent cannot infer from the code
- Size: stay lean for the context window; when the file grows, move detail to [CONTEXT.md](CONTEXT.md) or cut it
- Upkeep: update in the same change that moves a command, convention, or constraint
- Structure: follow the existing sections; keep every rule true for every contributor
- Belongs in [CONTEXT.md](CONTEXT.md): descriptive knowledge of the system, ie architecture, domain model, patterns, known gaps
- Belongs in `kaye-engine`'s [docs/](https://github.com/kami-lel/kaye-engine/tree/dev/docs): developer-facing documentation of the engine and of consumers; this repository's `docs/` holds only library-specific topics
- Local Layer: put machine-specific or personal rules in `AGENTS.local.md`; create it if missing, never commit it

## Setup Commands

```bash
pip install -e '.[dev]'                     # engine installs from its pinned git tag
pip install -e ../kaye-engine               # then swap in the sibling checkout
kaye-library --help                         # verify the console script resolves
kaye-library blueprint list                 # every registered blueprint
```

Requires Python 3.11+. Importing `kaye_library` loads nothing: call `setup_kaye_library_for_kaye_engine()` (the console command and `tests/conftest.py` do) or compose the five steps in `kaye_library/__init__.py`.

## Layout & Naming

- `kaye_library/registrations/<group>/`: one folder per feature group, its corpus `.md` beside the `<group>_bp.py` and `<group>_glossary.py` that register it; `git/` holds four corpus files (`git.md`, `repo.md`, `workflow.md`, `branch.md`) under one `Git` root, each with its own `_bp.py`
- corpus files are listed in `_CORPUS_SOURCES` (`kaye_library/__init__.py`) with the node each registers under; a source's top headings sit one level below that node
- skill names carry no prefix; a workflow skill is `<verb>-<object>`, its verb unique among exportable names (`commit-sense`, `prune-merged-branches`); a reference skill keeps a noun lead (`style-`, `element-`, `coder-`, `glossary-`)
- register a skill under its final name; keep no alias

## Code Style

- follow PEP 8 within 80 characters; Sphinx docstrings; test files end `_test.py` under `tests/`
- `*_bp.py` imports of the corpus tree stay function-local: the tree loads after `kaye_library` is imported
- create a blueprint only in `registrations/`, through the helpers of `registrations/_common.py` (`register_exportable`, `register_prompt`, `register_internal`, `register_abbr_glossary`), which bind this package's consumer via the engine's `bind_registrars`; build node and leaf blueprints with the engine's `register_node`, `register_leaf`, `glossary_blueprint`, never a local copy; build a blueprint whole before registering, never assign `entry.blueprint` afterwards; never call `register_blueprint` with `is_exportable=True` elsewhere
- a skill-backing corpus section needs `{description}` and `{when_to_use}` sidecars; blank spacer lines between sections are deliberate, keep them

## Content Rules

- keep every prompt free of the user's personal data: no names, contact data, accounts, or schedules; a persona the library ships may carry its public identity (display name, bot account email) behind its `{for <persona>}` sidecar; a personal taste expressed as a rule ships as a default a consumer overrides with `override_exportable`; a generic default list (the Secretary calendar, GTD project, and email category glossaries) ships as a registered glossary; a value only a consumer can know, spliced by a `(((placeholder)))`, is registered by the consumer only, since a second registration of a glossary or substitution raises `ValueError`, so the library skill renders that placeholder literally when run alone
- the standalone setup alone registers a default for each such placeholder (`secretary-email-authuser` is `0`, in `registrations/chat/chat_bp.py`), so a standalone export leaves no `(((placeholder)))` behind; a composing host registers its own
- never name a downstream package in code, corpus, docs, tests, or commit messages
- an abbreviation entry belongs in `kaye_library/abbrs.json` only when a glossary that library text splices needs it; name only glossaries this package registers
- `tests/privacy_test.py` scans every shipped file for private strings: extend its generic list, never trim it; personal strings (names, emails, ids, domains) go in the gitignored `tests/privacy-forbidden.local.txt`, 1 per line, never in a committed file

## Testing Instructions

Scope each run to the area touched; run everything only before a merge.

| changed | run |
|---|---|
| a corpus `.md` or a `*_bp.py` | `pytest tests/skill_export_test.py` plus the group's test (`tests/coder_test.py`, `tests/u3d_test.py`, `tests/agent_test.py`, `tests/commit_sense_test.py`, `tests/general_test.py`, `tests/personality_test.py`) |
| a glossary or `abbrs.json` | `pytest tests/glossary_test.py tests/abbr` |
| setup, `__main__.py`, the consumer record | `pytest tests/library_setup_test.py tests/console_test.py tests/third_consumer_test.py` |
| any shipped file | `pytest tests/privacy_test.py` |
| an `Invoke ... skill` line in a corpus `.md` | `pytest tests/invocation_test.py` |
| a `#anchor` link or a linked heading in a corpus `.md` | `pytest tests/anchor_test.py` |
| `README.md`, `README.zh-CN.md`, `AGENTS.md`, `CONTEXT.md` | `pytest tests/docs_test.py` |
| `examples/minimal-consumer/`, the Consumer documentation, an override or step rule | `pytest tests/example_consumer_test.py tests/docs_test.py` (the example test installs the example and needs `setuptools`, else it skips) |
| before a merge | `pytest tests` |

- `tests/data.py` holds the wording each skill must render; update it in the same change as the text
- `tests/console_test.py` runs `kaye-library` as a subprocess: install the package first
- `tests/invocation_test.py` fails when library text tells the assistant to invoke a skill the library does not register: point it at a library skill, never at one a downstream package supplies
- `tests/docs_test.py` checks every relative link and anchor in the root documents
- never run `kaye-library claude code`, `vs-code-extension`, or `marketplace` without a folder argument while testing: they write into the real `~/.claude/`; `vs-code-extension` also edits its `settings.json`
- `kaye-library build-github-release-assets` takes one required `OUTPUT` folder and writes every release asset there: the plugin zip, 2 installers, 2 system prompt `.md` files
- `kaye-library build-github-marketplace OUTPUT` writes the marketplace repo root; `scripts/sync-marketplace-paths.sh SRC DEST` replaces only `.claude-plugin/`, `.agents/`, `plugins/` in DEST, so rehearse a push against a scratch `git init` folder, never the real repo

## PR & Commit Instructions

- branch from `dev`; work lands on `dev`
- record every notable change under `[Unreleased]` in [CHANGELOG.md](CHANGELOG.md)
- a pushed `v<version>` tag builds the release: the tag must equal `v` plus the `pyproject.toml` version, or the workflow fails; the engine tag named in `pyproject.toml` must exist first
- at every version release, check the `kaye-engine` pin in `pyproject.toml` is the newest engine tag; update it before releasing

## Security Considerations

- never commit secrets, tokens, or personal data
- exports write to `~/.claude/` by default: pass a folder when testing

## Documentation Maintenance

- [README.md](README.md): overview, install, commands; the canonical readme
- [README.zh-CN.md](README.zh-CN.md): Simplified Chinese translation of `README.md`; update it in the same change, mirroring its sections, links, and commands
- [CONTEXT.md](CONTEXT.md): architecture and the root node ownership; refresh its `Last updated` line
- [docs/blueprint-doc.md](docs/blueprint-doc.md): the blueprint dependency and invocation graphs; update it when a blueprint's `dependencies=[...]` or an `Invoke ... skill` line changes
- [docs/claude-usage-doc.md](docs/claude-usage-doc.md), [docs/codex-usage-doc.md](docs/codex-usage-doc.md): client install walkthroughs; update them when an install route, release asset, or marketplace step changes; mirror each in its `.zh-CN.md` sibling ([Claude](docs/claude-usage-doc.zh-CN.md), [Codex](docs/codex-usage-doc.zh-CN.md))
- [docs/skill-catalog-doc.md](docs/skill-catalog-doc.md): the complete skill list by group, with starred picks, its groups in the order of the README group table; update it when a skill is added, renamed, or removed; mirror it in [docs/skill-catalog-doc.zh-CN.md](docs/skill-catalog-doc.zh-CN.md)
- [Consumer documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) in `kaye-engine`: how a consumer is created on the library; update it, `examples/minimal-consumer/` and `tests/example_consumer_test.py` together whenever the steps or the override rule change
- `CHANGELOG.md`: notable changes per release
