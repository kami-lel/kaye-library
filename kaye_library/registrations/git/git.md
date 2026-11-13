# Git

## Working with Git

Use these Git terms, no synonyms. Abbreviations are decode-only: never write them in a reply.

(((git-abbr)))

----

- edit in the workspace; index your own changes when done or partly done
- run `git status` or `git diff` only when the codebase differs from what you expect





#### Working Alongside the User

- the user may work in the same workspace or worktree at the same time. Treat any change you did not make as theirs: never revert, index, or commit it
- if a change you did not make blocks your work, stop and report





#### Actions Needing Explicit Approval

Run only when the user names the exact action in the same turn:

- Rewrite History: `git commit --amend`, `git rebase`, `git reset`, `git cherry-pick`
- Discard Work: `git reset --hard`, `git checkout .`, `git restore .`, `git clean -f`, `git stash drop`, `git branch -D`
- Publish: `git push`, `git push --force`, `git tag`, `gh pr create`
- Sweep or Bypass: `git add -A`, `git add .`, any command with `--no-verify`





### {[Claude:Skill] Usage}

To commit, invoke the `commit-sense` skill via the `Skill` tool.
Never devise your own commit message format, nor run `git commit` outside it.

### {[Hermes:skill_view] Usage}

To commit, load the `commit-sense` skill with `skill_view`.
Never devise your own commit message format, nor run `git commit` outside it.





### {description}

Sets the Git working terms and the actions that need explicit approval, so edits stay in the workspace beside the user.

### {when_to_use}

Trigger on any work in a Git repository: editing files, indexing, committing, branching, stashing, or running `git` commands. Not for writing the commit message itself (use `commit-sense`).



































## commit sensing

You are given the result of `git diff --cached` — read it as the changes staged for commit, and distill them into their **essential meaning**.

First, find the **intent** behind the edits — the direction they move in, the paradigm they shift toward, the theme they share. Then pick the **single most impactful change** carrying that intent; that change is the summary's substance.

Discard secondary, incidental, and repetitive edits. Report what the work was **for**, not an inventory of everything touched. Where a **pattern** spans the material, state the pattern rather than its instances; where none holds, state the one change that matters most.

Write strictly in [Briefness Style](#style-guide-briefness-style),
and apply [Commentary Case](#letter-case-commentary-case) to every line

Hold every line of a message to **72 characters at max**.

Aggressively replace each match with its listed entry:

(((commit-sense-shorthand)))



#### Co-author Trailer

If you helped write the changes for the current task, end the message with the trailer `Co-authored-by: Name <email>`. It is the **last line** of the message, nothing after.













### primary summary

summarize changes spanning **multiple files** as one whole, not file by file.

State the **unifying intent** the edits share; if none holds, the one change that most defines the set.

- Summary Line: required, and usually the whole message. Hold summary line to **72 characters at max**, one line that sums up the whole change
- Body: rare, after a blank line; write one only when a large pattern spans the change, eg a paradigm shift across many files, and neither the summary line nor the per-file summaries convey it, since the ledger already says what each file did; at the conceptual level, in up to 3 lines, every line within 72 characters, a longer point continuing onto the next line

Use [ASCII only](#ascii-only) for all content.

<primary-message-example>
introduce feature-flag framework; enable gradual rollout for search
</primary-message-example>

<primary-message-example>
introduce feature-flag framework

every new search path sits behind a flag, so rollout widens without a
redeploy; older paths stay untouched until the flag retires them
</primary-message-example>

#### {avoid}

A body that restates the ledger or inventories follow-on edits the summary line already implies, eg "docs, tests updated to match".












### per-file change sigil

A **change sigil** is one character classifying the change a one-file change set makes; it is the first line of a [Per-File Summary Task](#per-file-summary-task) result.

Output exactly **one character**: no word, label, quote, or empty line.

Evaluate the rules strictly in order. Take the **first** sigil that fully fits and stop. Never scan ahead or weigh two rules against each other.

(((commit-sense-sigil)))





#### No Fit Fallback Sigil

If nothing fits, or only loosely, output a single space ` ` as **fallback**.





#### Ordinary Edit Fallback Sigil

For an ordinary edit (no special nature an earlier rule names), pick by Lean and Size, so the reader sees at a glance whether the file grew, shrank, or merely changed:

- Lean: addition if added lines clearly outnumber deleted; deletion if deleted clearly outnumber added; else balanced
- Size: long if added plus deleted lines in this file total **100 or more**, else short

| Lean | Short | Long |
|---|---|---|
| addition | 🟢 | 🟩 |
| balanced | 🟡 | 🟨 |
| deletion | 🔴 | 🟥 |













### per-file summary

A **per-file summary** is the one-line message for a one-file change set: what the file is for, and its single most impactful change.

- Drop smaller edits rather than crowd the line
- Hold summary line to **72 characters at max**, one concise line, never wrapped onto a second
- Use [ASCII only](#ascii-only) for summary message












### Per-File Summary Task

**current task**: create a message summarizing change set touching **one file** — that file is whole set.

The result combines the [per-file change sigil](#per-file-change-sigil) and the [per-file summary](#per-file-summary): the sigil classifies the change, the summary describes it.

Return exactly **two lines**, nothing else — no heading, no blank line between, no surrounding text, no code fence.

- line 1 **change sigil**
- line 2 **summary** message line

<per-file-summary-example>
📖
document retry-budget behavior in scheduler README
</per-file-summary-example>













### Commit Sense

Commit the indexed changes: draw the message from the conversation so far, optionally confirmed against `git diff --cached --numstat`, whose added and deleted counts per file settle each sigil's Lean and Size, then run `git commit` once with the whole message as a single `-m` argument.

The message has up to three parts, in order, separated by blank lines:

1. Primary Message: follow [Primary Summary](#primary-summary) over the whole diff
2. File Ledger: per changed file, its [change sigil](#per-file-change-sigil), backticked filename with extension (eg `git.md`, never the directory path), a space, its [summary](#per-file-summary); for a single file, sigil and name only
3. Co-author Trailer: optional; per [Co-author Trailer](#co-author-trailer)

<commit-message-example>
restructure commit sense under Git hierarchy

🪧`CHANGELOG.md` remove stale TT
📖`http-api-doc.md` document commit-sense prompt nodes
🧪`__init__.py` update fixtures: heading levels

Co-authored-by: Example Bot <bot@example.com>
</commit-message-example>

<commit-message-example>
raise TT commit sense doc from todo => fixme & clarify relocation

🔖`CHANGELOG.md`
</commit-message-example>

##### Post Commit Output

Reply in one line with the short hash. If git rejects the commit, report its output and stop.

<post-commit-output-example>
🚩🐙 Commit `a3f9c21`
</post-commit-output-example>



#### {description}

Commits the indexed diff with a primary summary and a per-file ledger.

#### {when_to_use}

Trigger on "g" (git commit), the most common trigger; also "commit this", "write a commit message", or a handed-over `git diff --cached`.













### Commit Sense For Branch Merging

Write the commit message of a merge, usually mid-merge, where Git has already drafted one. Work on the message alone: leave the merge itself, its commit, and the index and working tree to the user.



##### message first line

The first line of a merge's commit message is decided by the merge's source and target branch types.

| From | Into | Message First Line |
|---|---|---|
| feature | dev | `Feature Landing: FEATURE_BRANCH` |
| dev | feature | `Catch Up: FEATURE_BRANCH` |
| dev | main | per [Semantic Version Title](#semantic-version-title) |
| hotfix | main | `BUMP Hotfix Release VERSION` |
| release | main | `BUMP Release Cut VERSION` |
| hotfix | dev | `Hotfix Backport from VERSION` |
| release | dev | `Release Backport from VERSION` |
| main | dev | `Sync Backport from VERSION` |

`BUMP` is the [bump word](#semantic-version-bump); `VERSION` comes from the source branch; `FEATURE_BRANCH` is the name of the feature branch.

If the branch pair is not in the table, or the source type is unclear, ask which types they are rather than guess a first line.



##### merge message example

Prepend the first line and append the [Co-author Trailer](#co-author-trailer), if any, to Git's auto-generated message, kept verbatim.

<merge-message-example>
Minor Release Cut 1.1.0

Merge branch 'release-1.1.0' into main

Co-authored-by: Example Bot <bot@example.com>
</merge-message-example>

<merge-message-example>
Feature Landing: add-search-filter

Merge branch 'add-search-filter' into dev

Co-authored-by: Example Bot <bot@example.com>
</merge-message-example>



##### post merge output

Reply in one line with the first line written. If no merge is in progress, report that and stop.

<post-merge-output-example>
🚩🐙 Feature Landing: add-search-filter
</post-merge-output-example>



#### {avoid}

Rewording, shortening, or dropping Git's auto-generated line.



#### {description}

Writes the message of a merge in progress: a typed first line prepended to Git's own message.

#### {when_to_use}

Trigger mid-merge, before the merge commit: "write the merge message", "message for this merge", "land the feature message", or any request to word a pending merge commit.



































## Resolve Merge Conflict

You resolve a **halted Git merge**. Leave the working tree and index correct so the *user* can finish the merge.





#### Resolve

- fix **only** files Git reports as unmerged; read both sides with context first, and disambiguate with `git log`, `git diff`, `git show :1:/:2:/:3:path`
- reconcile **semantically**: imports, signatures, config keys, and call sites must still agree
- preserve intent from both branches; never take "ours" or "theirs" wholesale
- name the surviving path for delete/modify and rename conflicts
- regenerate lock and generated files, never hand-merge
- stop and ask when a resolution needs a decision you cannot infer
- remove every conflict marker; grep for residuals, confirm each file parses or compiles, run tests if cheap
- `git add` each path as soon as it is resolved
- touch only the working tree and index: no `merge --continue`, `commit`, `merge --abort`, or branch/tag/stash/worktree changes, since finishing or abandoning the merge is the user's call





#### Output

Per file: what each side changed, how you reconciled it, what to double-check. End by stating the index is staged and ready for `git merge --continue`.





### {description}

Resolves conflicts in a halted Git merge — reconciles both sides of every hunk into correct working-tree files, markers removed.

### {when_to_use}

Triggers on a halted merge, rebase, cherry-pick, or pull; `<<<<<<<`/`=======`/`>>>>>>>` markers; or phrases like "resolve the conflicts," "fix the merge," "merge --continue is blocked." Not for branch strategy or merge commit messages.





### {[Claude:TodoWrite] Usage}

track resolution with the `TodoWrite` tool — one todo per unmerged path, marked complete only after its markers are gone and the file parses

### {[Hermes:todo_list] Usage}

track resolution with the `todo_list` tool — one todo per unmerged path, marked complete only after its markers are gone and the file parses

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.





### {[task-tracking] Fallback}

track resolution with a markdown task list — one item per unmerged path, checked off only after its markers are gone and the file parses


































## Tend Linked Worktree

Give each task its own linked worktree on the task's single [feature branch](#feature-branch), so work on the task leaves the main worktree untouched; never share a linked worktree across tasks or switch its branch, since one worktree per task keeps each task's edits apart.

A linked worktree sits inside the repository's workspace folder, named `REPO-WT-FEATURE`:

```text
WS-kaye-library/
├── kaye-library/                         # main worktree, on dev
└── kaye-library-WT-add-search-filter/    # linked worktree, on add-search-filter
```

- `WS-`: prefix of a workspace folder, which holds several worktrees
- `-WT-`: infix marking a linked worktree







### {description}

Places a feature branch's linked worktree, one per task, as `REPO-WT-FEATURE` inside the repository's `WS-` workspace folder, and removes it once its edits reach the main worktree.

### {when_to_use}

Trigger on starting, continuing, or finishing a task on a feature branch in a linked worktree, even when the user does not say so; also "new worktree for this feature", "work in a linked worktree", "don't touch main", "remove the worktree", `git worktree add`, `git worktree remove`.













### Plant the Linked Worktree

Plant the task's linked worktree as `REPO-WT-FEATURE` in the workspace folder, linked to the task's existing feature branch; if none exists, create the branch with the worktree.



#### {description}

Creates a task's linked worktree as `REPO-WT-FEATURE` in the repository's `WS-` workspace folder, on the task's feature branch, creating the branch if missing.

#### {when_to_use}

Trigger on starting a task on a feature branch, even when the user does not ask for a worktree; also "new worktree for this feature", "work in a linked worktree", "don't touch main", `git worktree add`. Not for removing a worktree.













### Uproot the Linked Worktree

Once the task is done, uproot its linked worktree, but only after every edit it holds has reached the main worktree, ie committed and merged into the main worktree's branch; if any edit has not, stop and report.



#### {description}

Removes a finished task's linked worktree once every edit in it is committed and merged into the main worktree's branch.

#### {when_to_use}

Trigger on finishing a task in a linked worktree or merging its branch, even when the user does not ask; also "remove the worktree", "clean up the worktree", `git worktree remove`. Not for deleting merged branches.
