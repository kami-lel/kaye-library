# kaye-library README

English | [简体中文](README.zh-CN.md)

📚 **100+ ready-made Agent Skills** that teach your AI assistant to write, code, commit, plan, and organize the way a careful professional would. Install once, and every conversation gets sharper. ✨

⚙️ **Powered by [kaye-engine](https://github.com/kami-lel/kaye-engine)**, its companion repository: the engine that renders and exports every skill.

⭐ **If kaye-library saves you a prompt or two, please [star it on GitHub](https://github.com/kami-lel/kaye-library)!** Every star helps more people find it. 🙏

## 💡 Why kaye-library?

Every time you explain your commit style, your Markdown taste, or how a README should look, you are rewriting a prompt someone already perfected. kaye-library collects those prompts into one curated library and hands them to your agent as skills it picks up on its own.

- 🧠 Write Once, Reuse Forever: each instruction lives in one place and ships everywhere your agent goes
- 🎯 Triggers on Its Own: say "commit this" or "write a README" and the right skill steps in
- 🧩 Built to Extend: layer your own package on top, override any skill, keep the rest, as the [Consumer documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) shows
- 📦 Ships Everywhere: Agent Skills folders, a Claude plugin, a plugin marketplace, or an upload-ready `.zip`

## 🗂️ What's Inside

100+ skills across 11 groups:

| | Group | What Your Agent Learns |
|---|---|---|
| 💻 | Coder | shared coding rules, plan and review workflows, test syncing, profiles for Bash, C, C++, C#, GDScript, HTML, JS/TS, PowerShell, Python, Unreal Engine |
| 📝 | Repository & Project | README, CHANGELOG, AGENTS, CONTEXT, and docs writers; feature landing and version release workflows |
| 🎨 | Style | Markdown, heading spacing, every letter case, briefness, good writing |
| 🗓️ | Secretary | email drafting and sweeping, calendar and task sync, event radar, daily recaps, morning and weekly check-ins, job hunt |
| 🎮 | Unity Engine | Unity 6 C# naming, inspector fields, input, activation, game tuning, asset placement |
| 🖋️ | Amanuensis | Chicago citations and bibliographies, redaction, notes, configs, keybindings, meeting minutes |
| 🧱 | Elements | date and time formats, units, triage tags, phonetic alphabet |
| 🐙 | Git | commit messages with a per-file ledger, merge conflict resolution, branch pruning, PRs, Git and Perforce terms |
| 🤖 | Agentic | chat rules, Movement and Suite planning: big tasks split into reviewable steps |
| 🪄 | Meta Prompt | writers for LLM system prompts and skill descriptions |
| 📖 | Glossaries | units, weekdays, language codes, coder abbreviations |

Start with the favorites:

- `/commit-sense`: 🐙 no more "fix stuff" commits: say "commit this" and get a sharp summary line plus a per-file ledger of what changed and why
- `/plan-for-suite`: 🤖 stops your agent from rewriting 30 files in one go: sprawling work becomes numbered, reviewable steps, each waiting for your approval
- `/repo-readme-writer`: 📝 a bare repository becomes a landing page people actually read, covering purpose, setup, and usage, like this one
- `/good-morning`: 🗓️ skip the morning tab-hopping: one report sweeps your inbox, recaps yesterday, and surfaces upcoming events and job openings

Then dig into the rest:

- `/coder-python`: 💻 no more cleaning up AI code by hand: PEP 8 Python, consistent names, Sphinx docstrings, and comments that explain intent
- `/sync-unit-test`: 💻 tests red after a refactor? stale assertions and fixtures realigned, and a flag wherever the code, not the test, went wrong
- `/review-gaps`: 💻 catch the half-finished seams before your users do, with a whole-repository audit before release
- `/release-version`: 📝 releases without the checklist dread: docs and changelog brought current, version bumped, merged to `main`, and tagged
- `/style-briefness-style`: 🎨 wordy drafts cut down to tight, headline-style notes
- `/draft-email`: 🗓️ emails that say exactly what you asked, nothing invented, revised as often as you like
- `/u3d-naming`: 🎮 ends the `Hero_final2` chaos with one naming rule for every Unity class, asset, folder, and GameObject
- `/amanuensis-chicago-note`: 🖋️ never hand-format a citation again: *Chicago Manual of Style* notes as native Markdown footnotes
- `/resolve-merge-conflict`: 🐙 a halted merge untangled: both sides of every hunk reconciled, conflict markers gone
- `/write-llm-prompt`: 🪄 turns a vague system prompt into one that delivers: drafted, graded, and sharpened

## 🚀 Getting Started

### Use with Claude

**Claude Desktop**: every release on the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases) carries the ready-made plugin `.zip`, named `kaye-library-claude-VERSION.zip`. Download it, then upload it in the app as shown in [Use in Claude Desktop](https://github.com/kami-lel/kaye-engine/blob/dev/docs/claude-doc.md#use-in-claude-desktop); no install is needed.

**Claude Code VS Code Extension**: follow [Use in the Claude Code VS Code Extension](https://github.com/kami-lel/kaye-engine/blob/dev/docs/claude-doc.md#use-in-the-claude-code-vs-code-extension), running `kaye-library` in place of `kaye-engine`.

### 📦 Install with pip

Requires Python 3.11 or newer. 🐍

```bash
pip install git+https://github.com/kami-lel/kaye-library.git
kaye-library skill --all ./skills   # export every skill into ./skills
```

## 🧭 Explore

```bash
kaye-library x ls                            # every skill
kaye-library blueprint render commit-sense   # preview one prompt
kaye-library --help                          # everything else
```

How the skills depend on and invoke each other is in the [blueprint documentation](docs/blueprint-doc.md).

## 🤝 Contributing

New skills and fixes are welcome! 🛠️ Install a working copy, then run the tests for the area you touch:

```bash
pip install -e '.[dev]'
pytest tests/skill_export_test.py
```

A path in, in order:

1. Find where a skill lives: each feature group has a folder under `kaye_library/registrations/`, its Markdown corpus beside the code that registers it, and the [blueprint documentation](docs/blueprint-doc.md) shows how the skills connect
2. Learn the engine underneath: the Markdown format a skill is written in is the [corpus documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/corpus-doc.md), its `{description}` and `{when_to_use}` sidecars are in the [sidecar documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/sidecar-doc.md), blueprints and the registry in the [prompt documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/prompt-doc.md), export flags in the [exportable registry documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/exportable-registry-doc.md), and glossaries in the [abbreviation documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/abbrs-doc.md)
3. Build on the library instead of changing it: the [Consumer documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) shows how to layer your own package and override a skill, with a working package in [examples/minimal-consumer](examples/minimal-consumer/example_consumer/__init__.py)

One rule to keep in mind: every prompt here stays free of personal data. The full set of conventions, commands, and constraints is in [AGENTS.md](AGENTS.md), and the architecture behind them in [CONTEXT.md](CONTEXT.md).

⭐ Enjoying it? A [star on GitHub](https://github.com/kami-lel/kaye-library) goes a long way!
