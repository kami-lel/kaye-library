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
| `commit-sense` | the `Perform Commit Sense` section's text, without any co-author persona; a package may replace it with `override_exportable` |
| `resolve-merge-conflict`, `prune-merged-branches` | called by the user only |
| `submit-pr` | stub awaiting text |

### Coder

| skill | depends on |
|---|---|
| `coder` | the Coder rules, glossaries, and triage tags, with no conversation rules; a package may replace it with `override_exportable` |
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

### Secretary

Every skill is called by the user only. The glossaries `secretary-calendar-name`, `secretary-gtd-project` and `secretary-email-category` ship with the library as generic defaults, so those placeholders resolve when a skill runs alone. A glossary or substitution that holds a value only a consumer can know (`secretary-work-color-legend`, `secretary-email-authuser`) is registered by that consumer; run alone, the library leaves that placeholder literal.

| skill | depends on |
|---|---|
| `draft-email` | none; drafts and processes emails and messages |
| `sweep-email-inbox` | the report info fields deadline, link, source; reads unread mail, marks it read, sorts it |
| `scan-event-radar-daily`, `scan-event-radar-weekly` | `secretary-event-brief-format`, `agent-unreachable-task-workaround`; format the day's or week's events |
| `secretary-event-brief-format` | `style-briefness-style`, the date-time, location, link, ticket fields; the shared event brief rules |
| `push-event-to-calendar`, `pull-event-from-calendar` | none; add or retrieve calendar events |
| `push-task-to-gtd`, `pull-task-from-gtd` | none; add or retrieve tasks in a GTD app |
| `hunt-job-opportunity` | `agent-unreachable-task-workaround`, `style-briefness-style`, the date-time, deadline, location, link, source fields; gathers job openings into per-job briefs |
| `good-morning`, `good-week` | none; the daily morning and weekly look-ahead check-ins that invoke the other Secretary skills |
| `recap-yesterday`, `recap-today` | `style-briefness-style`, `element-dt-watch-day`; one-line daily recaps |

### Meta Prompt

| skill | depends on |
|---|---|
| `write-llm-prompt` | `meta-prompt`; drafts and improves LLM system prompts, called by the user only |
| `write-skill-description` | `write-for-skill`; writes a skill's `description` field |
| `write-skill-when-to-use` | `write-for-skill`; writes a skill's `when_to_use` field |
| `write-skill-description-and-when-to-use` | `write-skill-description`, `write-skill-when-to-use` |

### Amanuensis

| skill | depends on |
|---|---|
| `amanuensis-chicago-note` | `style-markdown-footnotes`; Chicago-style notes-bibliography footnotes |
| `amanuensis-chicago-bibliography` | none; Chicago-style bibliography entries |
| `bibliographer` | `style-markdown-footnotes`; coordinates citation and bibliography assembly, called by the user only |
| `assemble-bibliography` | `amanuensis-chicago-bibliography`; gathers and creates a bibliography list |
| `dispositor` | `style-heading-separation`, `style-good-writing`; maintains structured, hierarchical notes |
| `scholiast`, `minutes-clerk` | `dispositor`; academic reading notes, meeting minutes |
| `config-writer` | `dispositor`, `style-briefness-style`; transcribes an app's or system's configuration into a structured note |
| `keybinding-writer` | `config-writer`; transcribes keybindings into a structured note |
| `redactor` | none; revises text while preserving intent and style |

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
| `agent-unreachable-task-workaround` | the procedure for a task whose needed information cannot be obtained |
| `git-sense-core`, `git-sense-primary-summary`, `git-sense-per-file-change-sigil`, `git-sense-per-file-summary` | building blocks of commit sense |
| `git-sense-dify-primary`, `git-sense-dify-per-file` | commit sense prompts split for a hosted workflow |
| `secretary-report-info-field-date-time`, `-deadline`, `-location`, `-link`, `-ticket`, `-source` | the Common Report Info Field leaves the Secretary reports merge |
| `meta-prompt`, `write-for-skill` | shared bases of the Meta Prompt writers and the skill-metadata writers |

A package builds its own skill over an internal blueprint by listing it as a dependency, or over an exportable's blueprint object for a skill it takes over, as in [the boundary document](boundary-doc.md#taking-a-skill-over).
