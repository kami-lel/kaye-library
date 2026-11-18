# kaye-library README

English | [简体中文](README.zh-CN.md)

📚 **140+** ready-made **Agent Skills** that teach your AI assistant to write, code, commit, plan, and organize the way a careful professional would. 🪶 **Leaner** prompts, 🔁 **repeatable** results, ⚡ agents working in **parallel**: install once, and every conversation gets sharper. ✨

⚙️ Powered by **[kaye-engine](https://github.com/kami-lel/kaye-engine)**, its companion repository: the engine that renders and exports every skill.

⭐ If kaye-library saves you a prompt or two, please **[star it on GitHub](https://github.com/kami-lel/kaye-library)**! Every star helps more people find it. 🙏

## 💡 Why kaye-library?

Every time you explain your commit style, your Markdown taste, or how a README should look, you are rewriting a prompt someone already perfected, and paying for it in **tokens**. kaye-library collects those prompts into one curated library of small, sharp skills your agent picks up on its own.

- 🪶 **Lean on Tokens**: one bloated system prompt becomes 140+ **narrow skills**, each with one clear job; your agent loads **only** the skill the task calls for, so the **context window** stays free for your code, and terse house styles keep comments, notes, and commit messages short on the way out too
- 🔁 **Repeatable by Design**: the same request gets the **same treatment** every time, from commit messages to release checklists, so a workflow you approve once still holds on the hundredth run; a big task saves its progress in a **Plan file**, so it pauses tonight and resumes tomorrow exactly where it stopped
- ⚡ **Built for Parallel Work**: every subagent and every worktree loads the same skills, so five agents follow **one rulebook**, and `/tend-linked-wt` gives each task its own **worktree** so parallel branches never collide
- 🔗 **Skills That Team Up**: one skill calls the next, so `/good-morning` runs four reports in one go and `/release-version` updates the docs, bumps the version, merges, and tags; shared rules are written **once** and reused by dozens of skills, so one fix improves them all
- 🎯 **Triggers on Its Own**: say "commit this" or "write a README" and the right skill steps in
- 🧩 **Built to Extend**: layer your own package on top, override any skill, keep the rest, as the [Consumer documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/consumer-doc.md) shows
- 🔒 **Private by Default**: every prompt ships free of **personal data**, and a privacy test scans every shipped file on each change
- 📦 **Ships Everywhere**: Claude Code, Claude Desktop, and Codex plugins, a plugin marketplace, plain Agent Skills folders, an upload-ready `.zip`, even Continue rules, Hermes, and Open WebUI

## 🗂️ What's Inside

140+ skills across 11 groups:

| | Group | What Your Agent Learns |
|---|---|---|
| 🤖 | Agentic | chat rules, Movement and Suite planning: big tasks split into reviewable steps |
| 📝 | Repository & Project | README, CHANGELOG, AGENTS, CONTEXT, and docs writers; feature landing and version release workflows |
| 🐙 | Git | commit messages with a per-file ledger, merge conflict resolution, branch pruning, linked worktrees for parallel tasks, PRs, Git and Perforce terms |
| 💻 | Coder | shared coding rules, plan and review workflows, test syncing, profiles for Bash, C, C++, C#, GDScript, HTML, JS/TS, PowerShell, Python, Unreal Engine |
| 🗓️ | Secretary | email drafting and sweeping, calendar and task sync, event radar, daily recaps, morning and weekly check-ins, job hunt |
| 🖋️ | Amanuensis | Chicago citations and bibliographies, redaction, notes, configs, keybindings, meeting minutes |
| 🎮 | Unity Engine | Unity 6 C# naming, inspector fields, input, activation, game tuning, asset placement |
| 🪄 | Meta Prompt | writers for LLM system prompts and skill descriptions |
| 🎨 | Style | Markdown, heading spacing, every letter case, briefness, good writing |
| 🧱 | Elements | date and time formats, units, triage tags, phonetic alphabet |
| 📖 | Glossaries | units, weekdays, language codes, coder abbreviations |

#### 🌟 Start with the Top Picks

- `/commit-sense`: 🐙 no more "fix stuff" commits: say "commit this" and get a sharp **summary line** plus a **per-file ledger** of what changed and why
- `/plan-for-suite`: 🤖 stops your agent from rewriting 30 files in one go: sprawling work becomes numbered, **reviewable steps**, each waiting for your approval
- `/tend-linked-wt`: 🐙 three features at once without stepping on each other: each task gets its own **linked worktree**, removed once its work lands
- `/initialize-repo`: 📝 a new repository gets its whole **starter set** in one pass: README, CHANGELOG, AGENTS, CONTEXT, and docs, no overlap, no gaps
- `/sync-unit-test`: 💻 tests red after a refactor? **stale assertions** and fixtures realigned, and a **flag** wherever the code, not the test, went wrong
- `/good-morning`: 🗓️ skip the morning tab-hopping: **one report** sweeps your inbox, recaps yesterday, and surfaces upcoming events and job openings
- `/amanuensis-chicago-note`: 🖋️ never hand-format a citation again: *Chicago Manual of Style* notes as **native Markdown footnotes**

#### ⭐ Then Dig into the Favorites

- `/coder-python`: 💻 no more cleaning up AI code by hand: PEP 8 Python, consistent names, Sphinx docstrings, and comments that explain intent
- `/review-gaps`: 💻 catch the half-finished seams before your users do, with a whole-repository audit before release
- `/release-version`: 📝 releases without the checklist dread: docs and changelog brought current, version bumped, merged to `main`, and tagged
- `/repo-readme-writer`: 📝 a bare repository becomes a landing page people actually read, covering purpose, setup, and usage, like this one
- `/maintenance-before-compact`: 📝 a long session about to compact? every lasting change saved to CHANGELOG, AGENTS, and CONTEXT first, nothing learned lost
- `/style-briefness-style`: 🎨 wordy drafts cut down to tight, headline-style notes
- `/draft-email`: 🗓️ emails that say exactly what you asked, nothing invented, revised as often as you like
- `/u3d-naming`: 🎮 ends the `Hero_final2` chaos with one naming rule for every Unity class, asset, folder, and GameObject
- `/minutes-clerk`: 🖋️ meeting minutes that track every decision and action item to done
- `/element-dt-watch-day`: 🧱 a day that runs past midnight on a 30-hour clock, built for night owls
- `/resolve-merge-conflict`: 🐙 a halted merge untangled: both sides of every hunk reconciled, conflict markers gone
- `/write-llm-prompt`: 🪄 turns a vague system prompt into one that delivers: drafted, graded, and sharpened

📚 Want every skill by name? The **[Skill Catalog](docs/skill-catalog-doc.md)** is the complete list of **every skill**, with what each does and how to call it.

## 🚀 Getting Started

### Use with Anthropic Claude

Using Claude Desktop or the VS Code extension? [See the step-by-step guide](docs/claude-usage-doc.md), with one-click installers for Windows and Linux.

### Use with OpenAI Codex

Using Codex? [See how to install kaye-library for it](docs/codex-usage-doc.md).

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

----

⭐ Enjoying it? A [star on GitHub](https://github.com/kami-lel/kaye-library) goes a long way!
