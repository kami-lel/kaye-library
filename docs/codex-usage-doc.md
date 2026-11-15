# kaye-library: Codex Usage Documentation

How to put the library into OpenAI Codex: the published marketplace, added by URL, or a local export.

> [!NOTE]
> Codex installs plugins only from a marketplace, never from a zip, so there is no Codex release asset.

## Add the Marketplace by URL

Every stable release pushes the plugin to the [kaye-library-marketplace](https://github.com/kami-lel/kaye-library-marketplace) repository; no install of Python or Kaye Engine is needed.

```bash
codex plugin marketplace add kami-lel/kaye-library-marketplace
```

Then install the `kaye-library` plugin from the `kaye-library-marketplace` marketplace in Codex.

## Export Locally

Requires Python 3.11 or newer:

```bash
pip install git+https://github.com/kami-lel/kaye-library.git
```

`kaye-library codex` (alias `o`) then exports the library in 4 forms:

| Goal | Command |
| --- | --- |
| Personal marketplace Codex reads on its own | `kaye-library codex marketplace` |
| Every skill as its own folder, no plugin | `kaye-library codex skills` |
| Global prompt for `~/.codex/AGENTS.md` | `kaye-library codex usp` |
| One plugin folder, to place by hand | `kaye-library codex plugin FOLDER` |

Every command takes the render flags of [Render Flags](https://github.com/kami-lel/kaye-engine/blob/dev/docs/codex-doc.md#render-flags); pass `-n` to list every write without writing.

### Marketplace

```bash
kaye-library codex marketplace          # ~/.agents/plugins/marketplace.json, ~/plugins/
```

The default root, your home folder, is the personal marketplace Codex reads, named `kaye-engine`; install the `kaye-library` plugin from it. Given another root, add it by hand with `codex plugin marketplace add ROOT`.

### Skills

```bash
kaye-library codex skills               # ~/.agents/skills/
```

### Global Prompt

The command prints the Chat prompt and writes nothing unless you redirect it; `-c` also appends the Coder prompt.

```bash
kaye-library codex usp > ~/.codex/AGENTS.md
kaye-library codex usp -c > ~/.codex/AGENTS.md
```

> [!WARNING]
> The redirect replaces an existing `~/.codex/AGENTS.md`; back it up first.

To update any export, run its command again. The full reference is in the Kaye Engine [Codex documentation](https://github.com/kami-lel/kaye-engine/blob/dev/docs/codex-doc.md).

## Remove

- Marketplace: delete `~/plugins/kaye-library/` and the `kaye-library` entry in `~/.agents/plugins/marketplace.json`
- Skills: delete the skill folders under `~/.agents/skills/`
- Global Prompt: delete or restore `~/.codex/AGENTS.md`
