# Projects

## Project Semantic Version

- **core:** `major.minor.patch` / `x.y.z`
- pre-release: append `-` plus dot-separated identifiers, e.g. `x.y.z-alpha`, `x.y.z-alpha.2`. identifiers must use `[0-9a-z-]` only; no uppercase, no empty identifiers.
- build: append `+` plus dot-separated identifiers, e.g. `x.y.z+build.1`, `x.y.z-alpha+build.1`; identifiers must use `[0-9A-Za-z-]` only





### {description}

defines semantic versioning scheme













### Semantic Version Extended

##### common pre-releases

- pre-releases types: `alpha`, `beta`, `rc`
- first pre-release: use unnumbered form, e.g. `1.0.0-alpha`.
- next pre-releases: start at `.2`, e.g. `1.0.0-alpha.2`, `1.0.0-alpha.3`, **do not use:** `1.0.0-alpha.1`
- pre-release patch: e.g. `1.0.0-alpha.2.1`



##### common build metadata

- `1.0.0+Win`, `1.0.0+mac`, `1.0.0+linux`: builds for different OS
- `0.5.0+2026-01-01-1234`, `1.0.0-alpha.2+2026-01-01`: date / date-time builds



##### development stage examples

- toy/prototypes: `0.1.z`~`0.4.z`
- Vertical Slice (VS): `0.5.z`~`0.8.z`
- pre-alpha: `0.9.z`
- alpha: `1.0.0-alpha`, `1.0.0-alpha.2`, ~~
- beta: `1.0.0-beta`, `1.0.0-beta.2`, ~~
- Release Candidate (RC): `1.0.0-rc`, `1.0.0-rc.2`
- first Stable Release: `1.0.0`



#### {description}

Extends semantic versioning with conventions for `alpha`/`beta`/`rc` pre-release numbering, OS/date build-metadata tags, and version-to-dev-stage mapping (toy, vertical slice, pre-alpha, alpha, beta, rc, stable)

#### {when_to_use}

Choosing or validating a version string for a pre-release, tagged build, or dev-stage milestone. Not for the base `major.minor.patch` core format or general changelog entries

































## Project Context Engineering

- For Agents:

  - Agent File: `AGENTS.md`, prescriptive rules (commands, conventions, constraints)
  - Context File: `CONTEXT.md`, descriptive system knowledge (architecture, domain, patterns, known gaps)
  - Local Layer: `AGENTS.local.md`, `CONTEXT.local.md`, personal and private, over its file

- For Users First: agents may read too

  - Readme File: `README.md`, landing page (what the project is, how to start, where next); must sit at project root
  - Doc Files: `docs/`, in-depth topic documents beyond the readme

- Project-Specific Skill: reusable instructions for a task only this project performs

A scoped agent/context file is optional: it sits in a subfolder and covers only that folder and beneath with specific information; the root agent/context file holds generic, project-wide information.

Explore these before assuming, by default at the opening of a conversation and whenever a gap appears: the agent file, then the context file (each with its local layer over it), then only the doc files the topic names. When none answers, open the actual file, config, or schema and verify what is checkable rather than assume it.





#### Folder Structure Example

```text
ExampleProject/
├── .claude/
│   └── skills/
│       └── write-release-note/
│           └── SKILL.md
├── README.md
├── AGENTS.md
├── CONTEXT.md
├── docs/
│   └── setup-guide.md
└── Frontend/
    ├── AGENTS.md
    ├── AGENTS.local.md
    └── CONTEXT.md
```


































## agents writer

Apply these rules to `AGENTS.md`, formatting it per [Style Guide Markdown Format](#style-guide-markdown-format).

Suggested Sections go under clear `##` headings: use what fits, omit rather than pad, and add any section carrying a project-specific behavioral rule. Keep content to rules and constraints an agent acts on. Each writer below lists its own.

The root `AGENTS.md` links every file under `docs/`, per [Reference Link Format](#reference-link-format), each phrased to send an agent there when its topic arises.





#### AGENTS Title & Preface

```markdown
# Example Project AGENTS

Prescriptive rules for agents working in this project.

- Belongs Here: rules an agent must follow, ie commands, conventions, constraints, who decides; only what an agent cannot infer from the code
- Size: stay lean for the context window; when the file grows, move detail to `docs/` or cut it
- Upkeep: update in the same change that moves a command, convention, or constraint
- Structure: follow the existing sections; keep every rule true for every contributor
- Belongs in `CONTEXT.md`: descriptive knowledge of the system, ie architecture, domain model, patterns, known gaps
- Belongs in `docs/`: system documentation for users and agents alike; link it from here, never grow this file to hold it
- Local Layer: put machine-specific or personal rules in `AGENTS.local.md`; create it if missing, never commit it
```

Replace `Example Project` with the real project name. Copy the preface exactly, word for word.

The personal layer's title line, marked as local:

```markdown
# Example Project local AGENTS
```













### Project AGENTS Writer

##### Suggested Sections

Keep content to rules, constraints, and who decides.

- Concept: what the project is and why it exists (kind of project, e.g. software, event, research, creative work; goals, scope, explicit non-goals)
- Members: who takes part and in what capacity (roles, responsibilities, skill sets, whom to ask about what, handoff and approval rules)
- Design: how the concept takes concrete form (design docs, style guides, asset locations)
- Engineering: the technical means of building it (tools, standards, environments, technical constraints)
- Business: the commercial and legal frame (budget, contracts, legal constraints, confidentiality, decision authority)
- Marketing: how the project reaches its audience (marketing plan, market research, voice, channels, what needs approval before publishing)
- Production: how the work gets made and finished (workflows, tools, quality checks, naming and versioning rules)
- Operations: what follows completion (release, maintenance, steps for each recurring task)
- Logistics: practical support for the team so work can happen (supplies, venues, travel, who books or approves)
- Timeline: when things happen (milestones, deadlines, current phase, date format, which deadline wins on conflict)

Split content by topic, never by type: a tool or resource link tied to production sits under Production, not in a separate links section.



#### {description}

Writes & maintains `AGENTS.md` for generic AI-ready projects: rules & constraints telling agents how to work on project

#### {when_to_use}

Creating, updating, reviewing `AGENTS.md` for generic project













### Repository AGENTS Writer

##### Suggested Sections

Keep content command-oriented; descriptive architecture and domain knowledge belong in `CONTEXT.md`.

- Layout & Naming: where each kind of file goes and how it is named, wherever the repository departs from the standard repository structure or an agent would misplace a file
- Setup Commands: copy-pasteable commands to install, run, and build
- Code Style: conventions this repository actually enforces — typing strictness, quote and semicolon rules, linter and formatter
- Testing Instructions: per the dedicated requirement below
- PR & Commit Instructions: title format, required pre-commit checks, review conventions
- Security Considerations: secrets handling, files and commands never to touch, commands that need confirmation before they run, safety constraints
- Documentation Maintenance: which docs must move when code, commands, or conventions change
- Project Overview & Pointers: one short paragraph, then links to `CONTEXT.md` and the deeper docs. Never duplicate them

Typical additions: release process, migration commands, environment gotchas, do/don't constraints.
In a monorepo, place a nested `AGENTS.md` in each package and state that the file closest to an edited file wins, with chat instructions overriding every file.



##### What to Include

Instruction budget is finite, and a wrong instruction beats no instruction only in the wrong direction. Write for signal:

- document only what an agent cannot infer — skip framework defaults and anything readable from a config file. Pin versions and name non-obvious constraints outright
- favor anti-patterns and counterintuitive rules. "Never use `Y` here, because `Z`" carries signal; "write clean code" carries none
- stay lean and disclose progressively, pointing to nested files, `CONTEXT.md`, or skills rather than crowding the root. Compliance falls sharply past a few dozen rules
- show one real example instead of three paragraphs describing a convention



##### Quality Expectations

- repository-specific, never generic
- behavioral and command-oriented — rules, commands, constraints, not architecture narration
- lean enough to sit in context without crowding out what matters
- explicit about conventions, tooling, and safety constraints
- consistent with existing documentation and repository structure
- free of contributor-facing explanation, which belongs in `README.md`, and descriptive knowledge, which belongs in `CONTEXT.md`



#### {description}

Writes & maintains repository `AGENTS.md` & personal `AGENTS.local.md`: **prescriptive** rules telling AI coding agents how to work in repo, e.g. commands, code style, PR rules, safety constraints

#### {when_to_use}

Creating, updating, reviewing `AGENTS.md`, `AGENTS.local.md`, `CLAUDE.md`, similar agent-instruction files. Triggers: "write an AGENTS.md", "add agent instructions", "agent rules/conventions". Not for **descriptive** architecture/domain knowledge, which belongs in `CONTEXT.md`

#### {globs}

```glob
**/{AGENTS,Agents,agents}{,.local,.override}{,.md}
```













### Create Project AGENTS

1. ground the file in the project's own material and the conversation; write only what they support
2. keep the root file generic; add a scoped file only where a subfolder's rules differ
3. create `AGENTS.md` per [Project AGENTS Writer](#project-agents-writer), formatted per [Style Guide Markdown Format](#style-guide-markdown-format)



#### {description}

Creates `AGENTS.md` for a generic project that has none

#### {when_to_use}

Triggers: "write an AGENTS.md for this project", "add agent instructions", "set up agent rules"







### Maintain Project AGENTS

You work from a **change set**: what the conversation and the project have altered since the file was last written. A section the change set never reaches is left exactly as it reads.

1. edit in place: fold new material into the section it belongs to, correct what the change set falsified, delete only what it retired
2. leave sound wording, structure, and length alone
3. verify facts against the project; keep the root generic and scoped files scoped
4. create a missing file only where the change set requires it
5. follow [Project AGENTS Writer](#project-agents-writer) and [Style Guide Markdown Format](#style-guide-markdown-format), then return a brief summary of the changes



#### {description}

Updates an existing project `AGENTS.md` against what changed, editing in place

#### {when_to_use}

Triggers: "update AGENTS.md", "AGENTS.md is out of date", changed member, deadline, or decision













### Create Repository AGENTS

1. ground the file in the repository itself and the conversation; write only what they support
2. in a monorepo, nest a file per package; gitignore any `AGENTS.local.md` in the same pass
3. create `AGENTS.md` per [Repository AGENTS Writer](#repository-agents-writer), formatted per [Style Guide Markdown Format](#style-guide-markdown-format)



#### {description}

Creates `AGENTS.md` for a repository that has none

#### {when_to_use}

Triggers: "write an AGENTS.md", "add agent instructions", "make an agents file"







### Maintain Repository AGENTS

You work from a **change set**: what the conversation and the repository have altered since the file was last written. A section the change set never reaches is left exactly as it reads.

1. edit in place: fold moved commands, conventions, and constraints into the sections already there, correct what the change set falsified, delete only what it retired
2. leave sound wording, structure, and length alone; descriptive knowledge belongs in `CONTEXT.md`
3. verify facts against the codebase; keep the root file primary and nested files scoped to their package
4. create a missing file only where the change set requires it
5. follow [Repository AGENTS Writer](#repository-agents-writer) and [Style Guide Markdown Format](#style-guide-markdown-format), then return a brief summary of the changes



#### {description}

Updates an existing repository `AGENTS.md` against what changed, editing in place

#### {when_to_use}

Triggers: "update AGENTS.md", "CLAUDE.md still says the old path", changed build/test command or convention


































## doc writer

Apply these rules to the topic documents under `docs/`, formatting them per [Style Guide Markdown Format](#style-guide-markdown-format) and writing them per [Style Guide Good Writing](#style-guide-good-writing).

A single document focuses on one very specific topic, or one system with a clear boundary.













### Project Doc Writer

Draw from the project's own material, and verify every claim against it.



#### {description}

Writes & maintains `docs/` topic files for generic projects

#### {when_to_use}

Triggers: "write docs", "document this project", "update the docs"













### Repository Doc Writer

Draw from the repository's code and configurations, and verify every example against the source. Link every file written here from `README.md`, per [Documentation Links](#documentation-links).



#### {description}

Writes & maintains `docs/` topic files for repositories

#### {when_to_use}

Triggers: "write docs", "document this", "update the docs", undocumented command/API













### Create Project Docs

1. ground each document in the project's own material and the conversation; write only what they support
2. give each document one topic and one clear boundary, cross-linked to its neighbors
3. verify every claim against the project
4. create the files under `docs/` per [Project Doc Writer](#project-doc-writer), linking each from the root `AGENTS.md` per [agents writer](#agents-writer), formatted per [Style Guide Markdown Format](#style-guide-markdown-format) and written per [Style Guide Good Writing](#style-guide-good-writing)



#### {description}

Creates topic-focused `docs/` files for a generic project

#### {when_to_use}

Triggers: "write docs", "document this project", "add a doc for this topic"













### Maintain Project Docs

You work from a **change set**: what the conversation and the project have altered since the docs were written. A document the change set never reaches is left exactly as it reads.

1. edit in place: update what the change set moved, fix references it broke, cut what it made stale, duplicated, or unsupported
2. leave each document's audience, scope, and sound wording alone
3. verify facts against the project; keep links current
4. create a document only where the change set requires it
5. follow [Project Doc Writer](#project-doc-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing), then return a brief summary listing changed files



#### {description}

Updates existing project `docs/` files against what changed, editing in place

#### {when_to_use}

Triggers: "update the docs", "the docs are out of date", changed decision, tool, or process













### Create Repository Docs

1. ground each document in the repository's code, configurations, and the conversation; write only what they support
2. give each document one topic and one clear boundary, cross-linked to its neighbors
3. verify every example against the source
4. create the files under `docs/` per [Repository Doc Writer](#repository-doc-writer), linking each from the root `AGENTS.md` per [agents writer](#agents-writer), formatted per [Style Guide Markdown Format](#style-guide-markdown-format) and written per [Style Guide Good Writing](#style-guide-good-writing)



#### {description}

Creates topic-focused `docs/` files for a repository

#### {when_to_use}

Triggers: "write docs", "document this", "add API/setup docs", undocumented command/API













### Maintain Repository Docs

You work from a **change set**: what the conversation and the repository have altered since the docs were written. A document the change set never reaches is left exactly as it reads.

1. edit in place: update what the change set moved, fix references it broke, cut what it made stale, duplicated, or unsupported
2. leave each document's audience, scope, and sound wording alone
3. verify links, paths, commands, and examples against the codebase
4. create a document only where the change set requires it
5. follow [Repository Doc Writer](#repository-doc-writer), [Style Guide Markdown Format](#style-guide-markdown-format), and [Style Guide Good Writing](#style-guide-good-writing), then return a brief summary listing changed files



#### {description}

Updates existing repository `docs/` files against what changed, editing in place

#### {when_to_use}

Triggers: "update the docs", "docs still show the old command", renamed file, removed feature, changed command


































## Equip Project for Agent

Task: create or maintain the project's `AGENTS.md` per [Project AGENTS Writer](#project-agents-writer).





### {description}

Equips project for AI agents: writes & maintains its `AGENTS.md`

### {when_to_use}

Setting up or updating agent instructions for a generic project. Triggers: "equip project for agent", "make project AI-ready"





### {[ClaudeCode:Skill] Usage}

Invoke `proj-agents-writer` skill via `Skill` tool, asking it to create or maintain the project's `AGENTS.md`.
