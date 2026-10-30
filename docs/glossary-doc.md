# Glossary Documentation

A **glossary** is a named group of abbreviation entries. Library text splices a glossary with a `(((name)))` placeholder, and an exportable glossary is also a skill named `glossary-<name>`. The library registers its glossaries in `kaye_library/registrations/<group>/<group>_glossary.py` and ships their entries in `kaye_library/abbrs.json`; the engine's glossary model is documented in [kaye-engine](https://github.com/kami-lel/kaye-engine), and the layering of entry files is in the [boundary document](boundary-doc.md#abbreviation-layers).

## Registered Glossaries

| glossary | group | skill | spliced by | entries |
|---|---|---|---|---|
| `briefness-shorthand` | Style | none | Briefness Style | 28 |
| `style-md-heading-abbr` | Style | none | Markdown Heading Format | 4 |
| `table-cell-values-shorthand` | Style | none | List Format | 5 |
| `units-of-measure` | Element | `glossary-units-of-measure` | Numerical Values with Units | 21 |
| `element-dt-days-of-week` | Element | `glossary-element-dt-days-of-week` | the `(element-dt-days-of-week)` dynamic node | 7 |
| `element-dt-watch-day-abbr` | Element | none | Watch Day | 2 |
| `element-dt-watch-week-abbr` | Element | none | Watch Week | 1 |
| `git-abbr` | Git | none | Working with Git | 6 |
| `commit-sense-shorthand` | Git | none | commit sense | 11 |
| `commit-sense-sigil` | Git | none | per-file change sigil | 21 |
| `agent-chat-turn-progress-dispatch-decorative` | Agent | none | Turn Progress Dispatch | 9 |
| `coder-abbr` | Coder | `glossary-coder-abbr` | Coder | 51 |
| `coder-identifier-shorthand` | Coder | none | variable naming | 55 |
| `coder-documentation-field-shorthand` | Coder | none | Coder Python Docstring Style | 7 |
| `coder-u3d-abbr` | Coder | none | Coder Unity Engine | 11 |
| `coder-u3d-identifier` | Coder | none | Coder Unity Engine | 10 |
| `amanuensis-config-writer-shorthand` | Amanuensis | none | Config Writer | 8 |
| `amanuensis-keybinding-writer-shorthand` | Amanuensis | none | Keybinding Writer | 18 |
| `secretary-common-shorthand` | Secretary | none | calendar and GTD push | 3 |
| `secretary-eisenhower-matrix-quadrant` | Secretary | none | the Secretary report skills | 10 |
| `secretary-eisenhower-matrix-quadrant-base` | Secretary | none | the Secretary report skills | 3 |
| `secretary-calendar-name` | Secretary | none | calendar push and pull | 8 |
| `secretary-gtd-project` | Secretary | none | GTD push | 9 |
| `secretary-email-category` | Secretary | none | Sweep Email Inbox | 9 |
| `programming-language-codes` | Coder | `glossary-programming-language-codes` | code format | 12 |

Counts are entries carrying the glossary in `abbrs.json`; an entry may carry several glossaries.

## Rendering Options

A registration states how entries render:

| option | effect |
|---|---|
| `is_exportable` | also registers the `glossary-<name>` skill |
| `is_dyn_substitution` | reachable as a `(((name)))` placeholder in text |
| `is_sorted` | entries ordered by priority instead of insertion order |
| `is_numbered_list` | `1.` markers instead of bullets |
| `is_remark_disabled` | no `(...)` remark suffix |

```python
from .._common import register_abbr_glossary

register_abbr_glossary("git-abbr", False, is_dyn_substitution=True)
```

## Naming

A glossary name follows its usage: `-abbr` for decode-only glossaries, `-shorthand` for glossaries the assistant may use to replace words, `-decorative` for glossaries the assistant accompanies text with. Register a glossary before any entry names it, or loading `abbrs.json` raises.

## Entries

`abbrs.json` maps a meaning to its abbreviations; each carries `priority`, `wrap`, `tags` (glossary names and rendering flags such as `single_character`), and optionally a `remark`. The library's file carries only entries of the glossaries above and loads standalone.

```json
{
  "bit": {
    "abbrs": {
      "b": {
        "priority": 5,
        "tags": ["letters_only", "single_character", "units-of-measure"],
        "wrap": "unit"
      }
    }
  }
}
```

Add an entry to the library file only when a glossary that library text splices needs it.
