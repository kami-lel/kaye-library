# Consumer Guide Documentation

How a package of your own builds on `kaye-library`: its own corpus, its own values, and a library skill taken over. The working version of everything below is [examples/minimal-consumer](../examples/minimal-consumer/example_consumer/__init__.py), tested by `tests/example_consumer_test.py`.

## When to Build One

The library ships generic defaults and no persona. Build a consumer package when you want any of:

- your own prompts beside the library's
- your own values where the library holds a default: an email account, calendars, task projects
- a library skill changed, under the same name
- your own chat persona and `claude code` setup

The engine has no configuration file for any of this; a package is the mechanism. The rules for what may cross between the library and a package are in the [boundary document](boundary-doc.md).

## Layout

```text
minimal-consumer/
├── pyproject.toml            # depends on kaye-library, one console script
└── example_consumer/
    ├── __init__.py           # setup_example_consumer(): the six steps
    ├── __main__.py           # main(): setup, then the engine's CLI
    ├── example.md            # the package's own corpus
    └── abbrs.json            # the package's own abbreviation entries
```

`pyproject.toml` declares `kaye-library` as a dependency, the package data (`*.md`, `abbrs.json`), and a console script pointing at `main`.

## The Six Steps

A package runs the library's steps itself, in this order, and adds its own between them. It never calls `setup_kaye_library_for_kaye_engine()`: a process runs exactly one setup.

1. consumer records: `kaye_library.register_kaye_library_consumer()`, then `register_consumer(display, name, version)` for the package
2. glossaries: `kaye_library.register_kaye_library_abbr_glossaries()`
3. abbr data: `populate_abbr_data_with_json_file` for the library's path (`get_kaye_library_abbrs_json_path()`), then for the package's own `abbrs.json`
4. substitutions: `kaye_library.register_kaye_library_dynamic_substitutions()`, then the package's own values
5. corpus: `kaye_library.register_kaye_library_corpus()`, then `register_corpus_under_node` for the package's files, then `load_corpus_tree()` once
6. blueprints: `kaye_library.register_kaye_library_blueprints()`, then the package's own, then `set_entry_consumer(name)`

## Your Own Values

A value only you can know goes in a placeholder the library splices as `(((name)))`. The standalone setup registers a default for each; a package registers its own instead:

```python
register_dynamic_substitution(
    "secretary-email-authuser", StringDynamicSubstitution("1")
)
```

A glossary entry, such as one more calendar, goes in the package's `abbrs.json` with the glossary's name in `tags`; the library's glossaries are listed in the [glossary document](glossary-doc.md). A second registration of the same glossary or substitution name raises `ValueError`, so register only what the library leaves to a consumer.

## Your Own Corpus

Write a Markdown file, register it under the root or under a library node (see the [corpus registration document](corpus-registration-doc.md)), and register a blueprint over its node with `consumer=` your package name. A skill-backing section needs `{description}` and `{when_to_use}` sidecars.

## Taking a Skill Over

Build the new blueprint over the library skill's own blueprint object, taken before the override, then call `override_exportable(name, blueprint, consumer=...)`. A string dependency on the skill's own name would form a cycle. The skill keeps its name and moves to your package's plugin. The example takes `style-good-writing` over this way, adding its own house rules.

## Your Own Chat

The standalone chat base (`chat`, `chat-coder`) is registered only by the standalone setup, so a package supplies its own: register a blueprint named for the chat exportable, one merging it with `coder`, and call `setup_claude_cli(chat_name, coder_name)` and `setup_hermes_cli(soul_name)` as the last step. Until it does, the subcommands that need them exit 1 and say what is missing.

## Try It

```bash
pip install ./examples/minimal-consumer
example-consumer skill --all ./skills
```
