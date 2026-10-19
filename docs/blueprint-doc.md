# Blueprint Documentation

A **blueprint** selects the corpus nodes a skill renders. This document lists every blueprint the library registers and how to register one; how the corpus is organised is in the [corpus registration document](corpus-registration-doc.md), and the engine's blueprint model is documented in [kaye-engine](https://github.com/kami-lel/kaye-engine).

## Registration

Blueprints register only in `kaye_library/registrations/<group>/<group>_bp.py`, through the helpers of `registrations/_common.py`, which bind the `kaye-library` consumer:

| helper | registers |
|---|---|
| `register_exportable` | an exportable skill, invokable by the user and the assistant |
| `register_prompt` | an exportable skill the assistant does not surface on its own (`llm_invokable=False`) |
| `register_node` | a node (optionally recursive) under a slug, through any of the above |
| `register_leaf` | one leaf with its ancestor headings, descriptors included |
| `register_blueprint(..., is_exportable=False)` | an internal building block, never exported |

```python
from .._common import register_exportable, register_node

register_node(
    register_exportable,
    "style-good-writing",
    style_node,
    "Style Guide Good Writing",
)
```

Registration order lives in `kaye_library/registrations/__init__.py`: a blueprint is registered after every blueprint it depends on. A dependency name is checked at registration, so a missing one raises.

A skill-backing section carries `{description}` and `{when_to_use}` sidecars; a blueprint reads them as its descriptors.

## Exportable Skills

Each skill is addressed as `kaye-library:<name>` once installed as a plugin. These are called by the user only, the assistant never surfacing them on its own: `initialize-repo`, `maintenance-before-compact`, `ready-land-feature`, `ready-release-version`, `land-feature`, `release-version`, `prune-merged-branches`, `resolve-merge-conflict`, `submit-pr`, `plan-for-suite`, and `review-gaps`.

### Agentic

| skill | depends on |
|---|---|
| `agent-movement-and-suite` | none |
| `agent-movement-and-suite-with-count` | none |
| `halt-each-movement` | `agent-movement-and-suite` |
| `cascade-all-movements` | `agent-movement-and-suite` |

### Style Guide

`style-briefness-style`, `style-good-writing`, `style-markdown` (assistant only), `style-markdown-extended`, `style-markdown-footnotes`, `style-markdown-endnotes`, `style-heading-separation` with `-long` and `-medium`, and the letter cases `style-letter-case-snake-case`, `-kebab-case`, `-pascal-case`, `-camel-case`, `-all-caps`, `-title-case`, `-commentary-case`. None depends on another skill.

### Elements

`element-dt-year-month-day-format`, `element-dt-month-day-format`, `element-dt-time-format`, `element-dt-watch-day` (depends on `element-dt-time-format`), `element-dt-watch-week`, `element-numerical-values-with-units`, `element-triage-tags`, `sort-and-group-triage-tag`, `element-international-phonetic-alphabet`, `element-alphabetical-sequence-numbering`.

### Projects

| skill | depends on |
|---|---|
| `proj-version` (never invoked on its own), `proj-version-extended` | none |
| `proj-agents-writer`, `repo-agents-writer` | internal `proj-agents` |
| `proj-doc-writer`, `repo-doc-writer` | internal `proj-docs`, `style-good-writing` |
| `equip-proj-for-agent` | internal `proj-context-engineering` |
| `create-project-agents`, `maintain-project-agents` | `proj-agents-writer` |
| `create-project-docs`, `maintain-project-docs` | `proj-doc-writer` |

### Repositories

| skill | depends on |
|---|---|
| `repo-structure`, `repo-context-writer` | none |
| `repo-readme-writer` | `style-briefness-style` |
| `repo-changelog-writer` | `style-briefness-style`, `proj-version-extended`, `style-good-writing` |
| `create-readme`, `maintain-readme` | `repo-readme-writer`, `style-good-writing` |
| `create-changelog`, `maintain-changelog`, `condense-changelog` | `repo-changelog-writer` |
| `create-repo-agents`, `maintain-repo-agents` | `repo-agents-writer` |
| `condense-agents-and-context` | `repo-agents-writer`, `repo-context-writer` |
| `create-repo-docs`, `maintain-repo-docs` | `repo-doc-writer` |
| `initialize-repo`, `maintenance-before-compact` | `style-good-writing` |
| `ready-land-feature` | none |
| `ready-release-version` | `proj-version-extended` |
| `land-feature`, `release-version` | none, stubs awaiting text |

### Git

| skill | notes |
|---|---|
| `commit-sense` | over the internal `commit-sense-core`; a package may replace it with `override_exportable` |
| `resolve-merge-conflict`, `prune-merged-branches` | called by the user only |
| `submit-pr` | stub awaiting text |

### Coder

| skill | depends on |
|---|---|
| `plan-for-suite` | `agent-movement-and-suite` |
| `plan-for-suite-execution` | `agent-movement-and-suite` |
| `sync-unit-test` | `agent-movement-and-suite-with-count`, `element-triage-tags` |
| `review-gaps` | `element-triage-tags` |
| `coder-comment-banner-in-code-comment`, `coder-comment-banner-in-print-out` | none |
| `coder-command-usage-message` | `style-letter-case-all-caps` |
| `coder-bash-shell`, `coder-bash-script`, `coder-powershell`, `coder-c`, `coder-c-sharp`, `coder-gdscript`, `coder-html`, `coder-javascript-and-typescript`, `coder-python`, `coder-python-docstring-style`, `coder-python-testing-guidelines` | none |
| `coder-cpp` | `coder-c` |
| `coder-ue` | `coder-cpp` |
| `coder-u3d` | `coder-c-sharp` |
| `coder-u3d-mb` | `style-briefness-style` |
| `coder-u3d-assets-management`, `coder-u3d-so` | none |

### Glossary Groups

Each exportable glossary is also a skill named `glossary-<name>`; see the [glossary document](glossary-doc.md).

## Internal Blueprints

Never exported; they exist for a skill, or a package, to build on.

| blueprint | holds |
|---|---|
| `style` | the whole Style Guide |
| `rapid` | Markdown rules for quick, mechanical tasks with no persona or role |
| `proj-agents`, `proj-docs`, `proj-context-engineering` | text shared by the writers and workflows above |
| `element-alphabetical-sequence-numbering-in-chat` | the chat form of sequence numbering |
| `git-feature-branch` | the feature branch definition |
| `git-sense-core`, `git-sense-primary-summary`, `git-sense-per-file-change-sigil`, `git-sense-per-file-summary` | building blocks of commit sense |
| `commit-sense-core` | the commit sense skill's text, without any co-author persona |
| `git-sense-dify-primary`, `git-sense-dify-per-file` | commit sense prompts split for a hosted workflow |
| `coder-core` | the Coder rules, glossaries, and triage tags, with no conversation rules |

A package builds its own skill over an internal blueprint by listing it as a dependency, as in [the boundary document](boundary-doc.md#taking-a-skill-over).
