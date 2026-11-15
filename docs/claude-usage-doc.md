# kaye-library: Claude Usage Documentation

<!--
Fixme improve claude related docs
Todo zh version of claude usage doc
-->

How to put the library into Claude: the Claude Desktop app and the Claude Code VS Code Extension.

## Use in Claude Desktop

1. Create the plugin zip:

   ```bash
   kaye-engine claude plugin -z
   ```

   One zip per consumer lands in the current directory, named `CONSUMER-claude-VERSION.zip`, e.g. `my-corpus-claude-1.2.1.zip`.

2. Upload the zip in the Claude Desktop app:

   1. Click *Customize* in the sidebar.

      ![Customize in the sidebar](assets/claude-desktop-step-1-customize.png)

   2. Open the *Plugins* tab.

      ![Plugins tab](assets/claude-desktop-step-2-plugins-tab.png)

   3. Click *Add* → *Upload plugin*.

      ![Add menu with Upload plugin](assets/claude-desktop-step-3-add-upload-plugin.png)

   4. Drop the zip into the dialog, or browse for it, then click *Upload*.

      ![Upload a plugin dialog](assets/claude-desktop-step-4-upload-dialog.png)

To update, export again and upload the new zip.

## Use in the Claude Code VS Code Extension

1. Run the setup command:

   ```bash
   kaye-engine claude vs-code-extension
   ```

   It does 4 things in `~/.claude/`:

   - writes your `CLAUDE.md` system prompt; a different `CLAUDE.md` already there is first copied to `CLAUDE.md.YYYYMMDDHHMMSS.bak`
   - builds a marketplace folder `kaye-engine/` holding your plugins
   - registers that marketplace in `settings.json` (`extraKnownMarketplaces`)
   - enables each of its plugins in `settings.json` (`enabledPlugins`)

   `settings.json` only gains missing keys: anything already there, a plugin you turned off included, stays as it is. If it is not valid JSON, the command stops and writes nothing. Each step is specified in [Installer Algorithm](https://github.com/kami-lel/kaye-engine/blob/dev/docs/installer-algorithm-doc.md#claude-vs-code-plugin).

2. Restart VS Code, then check the result in the plugin manager. Nothing needs adding by hand.

   1. In the *Claude Code* panel, type `/` and choose *Manage plugins*.

      ![Manage plugins in the slash menu](assets/claude-vsc-step-1-manage-plugins.png)

   2. Open the *Plugins* tab. Every plugin is listed under *Installed* as `PLUGIN@kaye-engine`, with scope `user` and its toggle on.

      ![Plugins tab with installed plugins enabled](assets/claude-vsc-step-2-plugins-tab.png)

   3. Open the *Marketplaces* tab. The `kaye-engine` marketplace is listed, its directory pointing at `~/.claude/kaye-engine`.

      ![Marketplaces tab with the kaye-engine marketplace](assets/claude-vsc-step-3-marketplaces-tab.png)

To update, run the command again.
