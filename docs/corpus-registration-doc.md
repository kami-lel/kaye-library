# Corpus Registration Documentation

The library's text lives in Markdown files under `kaye_library/registrations/`, registered into the engine's one corpus tree. This document covers how the files are listed, how a package adds its own beside them, and the rules for writing a source; the roots each source creates are in [CONTEXT.md](../CONTEXT.md#corpus-structure), and the engine's tree model is documented in [kaye-engine](https://github.com/kami-lel/kaye-engine).

## Listing

`_CORPUS_SOURCES` in `kaye_library/__init__.py` pairs a node path with a file, in registration order:

```python
_CORPUS_SOURCES = [
    ((), "dynamic_nodes/dynamic_nodes.md"),
    ((), "agent/agent.md"),
    # ... one entry per file
    ((), "coder/coder.md"),
    (("Coder",), "coder/coder-bash.md"),
]
```

`register_kaye_library_corpus()` records each pair with the engine's `register_corpus_under_node`; nothing is read until the host calls `load_corpus_tree()` once, after every package has registered.

## Node Paths

- `()` is the root: the file's `#` headings become root nodes
- `("Coder",)` is one heading below the root: the file's `##` headings become children of `Coder`, which is how every language file joins the Coder rules
- a bare `str` without `/` or `.md` means a one-heading path
- a source's top headings sit exactly one level below its target; a wrong level raises, naming the file
- registration order does not matter between targets; only the order of siblings under one node follows registration order

## Adding a Package's Own Sources

A package composing the library's steps registers its files between the corpus step and the load:

```python
import kaye_library
from kaye_engine import load_corpus_tree, register_corpus_under_node

kaye_library.register_kaye_library_corpus()
register_corpus_under_node((), "# My Root\nText.\n")
register_corpus_under_node(("My Root",), "## My Child\nText.\n")
load_corpus_tree()
```

Keep to the root and to the package's own nodes; a root name the library already uses raises as a duplicate sibling.

## Writing a Source

- a skill-backing section needs `{description}` and `{when_to_use}` sidecars; a conditional sidecar is spelled `{[Name] Usage}` or `{[Name] Fallback}`
- a `(name)` heading places a dynamic node, and `(((name)))` splices a glossary or substitution; the library authors only `(today)` and `(element-dt-days-of-week)`
- a link follows heading text, as `[Title Case](#letter-case-title-case)`; link only to text the library ships
- blank spacer lines between sections are deliberate; keep them
- a `<!-- ... -->` comment line never renders, so authoring notes may live in a source
- a heading deeper than one level below its parent is local: it stays text of its section, not a node

The boundary rules for what may enter a source are in the [boundary document](boundary-doc.md).
