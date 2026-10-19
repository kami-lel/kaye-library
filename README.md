# kaye-library README

Shareable prompt library for LLM agents: style guides, git workflows, repository documents, and coding rules, written once in Markdown and exported as Agent Skills, built on [kaye-engine](https://github.com/kami-lel/kaye-engine).

## Project Overview

`kaye-library` is a corpus of ready-to-use agent instructions plus the registrations that turn it into skills. Install it, run one command, and your agent gains reusable skills such as `commit-sense` or `coder-python`, with no persona attached: every prompt is written for any assistant and any project.

It also serves as a base layer. Other packages built on `kaye-engine` can register their own corpus beside it, even under its nodes, and take over any skill with their own version.

## Features

- Style: Markdown format, heading separation, every letter case, briefness, good writing
- Elements: date and time formats, units, triage tags, ASCII only, phonetic alphabet
- Git: commit messages with a per-file ledger, merge conflict resolution, branch pruning
- Repositories: README, CHANGELOG, AGENTS, CONTEXT, and docs writers, landing and release workflows
- Agentic: Movement and Suite workflows, Turn Progress Dispatch, file and folder naming
- Coder: shared coding rules, comment banners, plan and review workflows, and profiles for Bash, C, C++, C#, GDScript, HTML, JavaScript, TypeScript, PowerShell, Python, Unity, and Unreal Engine
- One command exports everything as Agent Skills, a Claude plugin, or a plugin marketplace

## Tech Stack

- Python 3.11 or newer
- [kaye-engine](https://github.com/kami-lel/kaye-engine): parses the corpus and renders prompts
- Markdown corpus, shipped as package data

## Getting Started

Install the engine and the library, then check that the command resolves:

```bash
pip install -e ../kaye-engine -e .
kaye-library --help
```

## Usage

List what the library registers, preview one prompt, and export:

```bash
kaye-library blueprint list                  # every registered blueprint
kaye-library blueprint render commit-sense   # print one prompt
kaye-library skill --all ./skills            # every skill into ./skills
kaye-library skill commit-sense ./skills     # one skill
kaye-library claude plugin                   # ~/.claude/plugins/kaye-library/
kaye-library claude plugin -z                # upload-ready .zip
kaye-library claude marketplace              # ~/.claude/kaye-engine/ marketplace
```

Once installed as a plugin, a skill is addressed as `kaye-library:<name>`, for example `kaye-library:commit-sense`; the `coder` skill carries the shared coding rules every language profile builds on; every skill and its dependencies are listed in the [blueprint document](docs/blueprint-doc.md), and the abbreviation glossaries behind them in the [glossary document](docs/glossary-doc.md).

Subcommands that need a chat persona, a coder profile, or a Hermes soul (`claude code`, `claude user-system-prompt`, `claude vs-code-extension`, `hermes`) exit with code 1 and say what is missing: the library names none of them.

## Build & Test

```bash
pip install -e '.[dev]'
pytest tests
```

The suite loads the library alone, exports every skill as a folder and as a `.zip`, and scans the shipped files for private strings.

## Contributing

Put new prompts in `kaye_library/registrations/<group>/`, one folder per feature group, holding the corpus `.md` beside the code that registers its blueprints. Keep every prompt free of personal data and of any persona.

Rules for agents are in [AGENTS.md](AGENTS.md) and the architecture in [CONTEXT.md](CONTEXT.md). How corpus files are listed and attached to the tree is in the [corpus registration document](docs/corpus-registration-doc.md); what may cross the boundary between the library and a package building on it, including taking a skill over, is in the [boundary document](docs/boundary-doc.md).

## Acknowledgments

Built on [kaye-engine](https://github.com/kami-lel/kaye-engine).
