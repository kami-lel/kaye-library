# Kaye Library: Claude Usage Documentation

English | [简体中文](claude-usage-doc.zh-CN.md)

Install `kaye-library` in Claude Desktop or the Claude Code VS Code Extension: pick any one of the methods below.

## for Claude Desktop

There are 3 ways to install in Claude Desktop:

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

7. In the *Discover* view, click *Add* beside *Kaye Library*.

   ![Discover view with Kaye Library and its Add button](assets/claude-desktop-marketplace-step-7-add.png)





### ⓑ Upload the Release Zip

Download a ready-made plugin file, then upload it.

1. Download `kaye-library-VERSION-claude-desktop-plugin.zip` from the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases).
2. Upload it as in [Upload Plugin as Zip File](#upload-plugin-as-zip-file).





### ⓒ Build and Upload the Zip

Make the plugin file yourself, then upload it.

1. Build the zip:

   ```bash
   kaye-library claude plugin -z
   ```

2. Upload `kaye-library-claude-VERSION.zip` from the current directory, as in [Upload Plugin as Zip File](#upload-plugin-as-zip-file).





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

There are 4 ways to install in the Claude Code VS Code Extension: pick one, then verify it, as in [Check Installed Plugins](#check-installed-plugins).

### ⓐ Add the Marketplace by URL

1. In the *Claude Code* panel, type `/` and choose *Manage plugins*.

   ![Manage plugins in the slash menu](assets/claude-vsc-step-1-manage-plugins.png)

2. Open the *Marketplaces* tab. Type this in the field, then click *Add*:

   ```text
   kami-lel/kaye-library-marketplace
   ```

   ![Marketplaces tab with the repository typed in](assets/claude-vsc-marketplace-step-2-add.png)

3. Check that `kaye-library-marketplace` is listed.

   ![Marketplaces tab with kaye-library-marketplace listed](assets/claude-vsc-marketplace-step-3-listed.png)

4. Open the *Plugins* tab. Under *Available*, click *Install* beside `kaye-library`.

   ![Plugins tab with kaye-library and its Install button](assets/claude-vsc-marketplace-step-4-install.png)

5. Check that `kaye-library@kaye-library-marketplace` is listed under *Installed*.

   ![Plugins tab with kaye-library installed](assets/claude-vsc-marketplace-step-5-installed.png)

6. Restart VS Code.






### ⓑ Run the One-Click Installer on Windows

Download a ready-made installer, then run it.

1. Download `kaye-library-VERSION-claude-vsc-installer-Win.zip` from the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases).
2. Extract it, then double-click `install.cmd`.
3. Restart VS Code.
4. Check the result, as in [Check Installed Plugins](#check-installed-plugins).






### ⓒ Run the One-Click Installer on Linux

Download a ready-made installer, then run it.

1. Download `kaye-library-VERSION-claude-vsc-installer-linux.run` from the [GitHub Releases page](https://github.com/kami-lel/kaye-library/releases).
2. Run:

   ```bash
   bash kaye-library-VERSION-claude-vsc-installer-linux.run
   ```

3. Restart VS Code.
4. Check the result, as in [Check Installed Plugins](#check-installed-plugins).






### ⓓ Run the Setup Command

Install it yourself with one command.

1. Run:

   ```bash
   kaye-library claude vs-code-extension
   ```

2. Restart VS Code.
3. Check the result, as in [Check Installed Plugins](#check-installed-plugins).






### Check Installed Plugins

1. In the *Claude Code* panel, type `/` and choose *Manage plugins*.

   ![Manage plugins in the slash menu](assets/claude-vsc-step-1-manage-plugins.png)

2. Open the *Plugins* tab. Check that `kaye-library` is listed under *Installed*, its toggle on.

   ![Plugins tab with installed plugins enabled](assets/claude-vsc-step-2-plugins-tab.png)

3. Open the *Marketplaces* tab. Check that `kaye-library` is listed.

   ![Marketplaces tab with the kaye-library marketplace](assets/claude-vsc-step-3-marketplaces-tab.png)
