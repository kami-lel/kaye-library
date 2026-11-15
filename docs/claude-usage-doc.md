# kaye-library: Claude Usage Documentation

Install `kaye-library` in Claude Desktop or the Claude Code VS Code Extension: pick any one of the methods below.

<!--
TODO zh version of claude usage doc
-->

## for Claude Desktop

### ⓐ Add the Marketplace by URL

1. Click *Customize* in the sidebar.

   ![Customize in the sidebar](assets/claude-desktop-step-1-customize.png)

2. Open the *Plugins* tab.

   ![Plugins tab](assets/claude-desktop-step-2-plugins-tab.png)

3. Click *Add* → *Add marketplace*.

   ![Add menu with Add marketplace](assets/claude-desktop-marketplace-step-3-add-marketplace.png)

4. Choose *Add from a repository*.

   ![Add marketplace dialog with Add from a repository](assets/claude-desktop-marketplace-step-4-add-from-repository.png)

5. Type this in the *URL* field, then choose *Use "kami-lel/kaye-library-marketplace"*:

   ```text
   kami-lel/kaye-library-marketplace
   ```

   ![URL field with the repository typed in](assets/claude-desktop-marketplace-step-5-repository.png)

6. Click *Sync*.

   ![Add marketplace dialog with the Sync button](assets/claude-desktop-marketplace-step-6-sync.png)





### ⓑ Upload the Release Zip

Download a ready-made plugin file, then upload it.

1. Download `kaye-library-VERSION-claude-desktop-plugin.zip` from the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases).
2. Upload it as in [Upload Plugin as Zip File](#upload-plugin-as-zip-file).





### ⓒ Build and Upload the Zip

Make the plugin file yourself, then upload it.

1. Build the zip:

   ```bash
   kaye-engine claude plugin -z
   ```

2. Upload `CONSUMER-claude-VERSION.zip` from the current directory, as in [Upload Plugin as Zip File](#upload-plugin-as-zip-file).





### Upload Plugin as Zip File

1. Click *Customize* in the sidebar.

   ![Customize in the sidebar](assets/claude-desktop-step-1-customize.png)

2. Open the *Plugins* tab.

   ![Plugins tab](assets/claude-desktop-step-2-plugins-tab.png)

3. Click *Add* → *Upload plugin*.

   ![Add menu with Upload plugin](assets/claude-desktop-step-3-add-upload-plugin.png)

4. Drop the zip into the dialog, or browse for it, then click *Upload*.

   ![Upload a plugin dialog](assets/claude-desktop-step-4-upload-dialog.png)













## for Claude Code VS Code Extension

### ⓐ Add the Marketplace by URL

<!-- TODO add screen caps of adding the marketplace by URL in the VS Code Extension -->

In the *Claude Code* panel, run:

```text
/plugin marketplace add kami-lel/kaye-library-marketplace
/plugin install kaye-library@kaye-library-marketplace
```

- Update: `/plugin marketplace update kaye-library-marketplace`
- Remove: `/plugin uninstall kaye-library@kaye-library-marketplace`

### ⓑ Run the One-Click Installer

1. Download the installer for your system from the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases), then run it:
   - Windows: extract `kaye-library-VERSION-claude-vsc-installer-Win.zip`, then double-click `Install.cmd`
   - Linux: run `bash kaye-library-VERSION-claude-vsc-installer-linux.run`
2. Restart VS Code.
3. Check the result, as in [Check the Result](#check-the-result).

- Update: run the new installer
- Remove: follow [Remove](#remove)

### ⓒ Run the Setup Command

1. Run:

   ```bash
   kaye-engine claude vs-code-extension
   ```

2. Restart VS Code.
3. Check the result, as in [Check the Result](#check-the-result).

- Update: run the command again
- Remove: follow [Remove](#remove)

### Check the Result

<!-- TODO replace w/ newer VS Code Extension screen caps if the panel UI changed -->

1. In the *Claude Code* panel, type `/` and choose *Manage plugins*.

   ![Manage plugins in the slash menu](assets/claude-vsc-step-1-manage-plugins.png)

2. Open the *Plugins* tab. Check that every plugin is listed under *Installed* as `PLUGIN@kaye-engine`, its toggle on.

   ![Plugins tab with installed plugins enabled](assets/claude-vsc-step-2-plugins-tab.png)

3. Open the *Marketplaces* tab. Check that the `kaye-engine` marketplace is listed.

   ![Marketplaces tab with the kaye-engine marketplace](assets/claude-vsc-step-3-marketplaces-tab.png)

### Remove

1. Delete the folder `~/.claude/kaye-engine/`.
2. In `~/.claude/settings.json`, delete the `kaye-engine` entries under `extraKnownMarketplaces` and `enabledPlugins`.
