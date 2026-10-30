# Git

<!--
todo git branch merge skill: handling landing/release/catch up ~
todo working w/ git worktree main & linked
-->

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





### {[ClaudeCode:Skill] Usage}

To commit, invoke the `commit-sense` skill via the `Skill` tool.
Never devise your own commit message format, nor run `git commit` outside it.



































## commit sense

You are given the result of `git diff --cached` — read it as the changes staged for commit, and distill them into their **essential meaning**.

First, find the **intent** behind the edits — the direction they move in, the paradigm they shift toward, the theme they share. Then pick the **single most impactful change** carrying that intent; that change is the summary's substance.

Discard secondary, incidental, and repetitive edits. Report what the work was **for**, not an inventory of everything touched. Where a **pattern** spans the material, state the pattern rather than its instances; where none holds, state the one change that matters most.

Write strictly in [Briefness Style](#style-briefness-style),
and apply [Commentary Case](#letter-case-commentary-case) to every line

Aggressively replace each match with its listed entry:

(((commit-sense-shorthand)))













### primary summary

summarize changes spanning **multiple files** as one whole, not file by file.

State the **unifying intent** the edits share; if none holds, the one change that most defines the set.

- Summary Line: required, may stand alone. Hold summary line to **72 characters at max**, one line that sums up the whole change
- Body: optional, after a blank line; covers only what the summary line leaves out, at the conceptual level, in up to 3 lines, every line within 72 characters, a longer point continuing onto the next line

Use [ASCII only](#ascii-only) for all content.

<primary-message-example>
introduce feature-flag framework; enable gradual rollout for search
</primary-message-example>

<primary-message-example>
introduce feature-flag framework

every new search path sits behind a flag, so rollout widens without a
redeploy; older paths stay untouched until the flag retires them
</primary-message-example>












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













### Perform Commit Sense

Commit the indexed changes: draw the message from the conversation so far, optionally confirmed against `git diff --cached`, then run `git commit` once with the whole message as a single `-m` argument.

The message has up to three parts, in order, separated by blank lines:

1. Primary Message: follow [Primary Summary](#primary-summary) over the whole diff
2. File Ledger: per changed file, its [change sigil](#per-file-change-sigil), backticked filename with extension (eg `git.md`, never the directory path), a space, its [summary](#per-file-summary); for a single file, sigil and name only
3. Co-author Trailer: optional; only when the project's instructions name a co-author, as `Co-authored-by: Name <email>`

Keep the trailer last.

Use ASCII only, except the sigil.

<commit-message-example>
restructure commit sense under Git hierarchy

blueprints, docs, tests updated to match new nesting and heading levels;
corpus source entry for commit sense dropped from init list

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





### Perform Commit Sense Personalized

#### {description}

Commits the indexed diff with a primary summary and a per-file ledger.

#### {when_to_use}

Trigger on "cc" (commit, then continue), the most common trigger; also "commit this", "write a commit message", or a handed-over `git diff --cached`.


































## feature branch

<!-- todo feature branch summary -->

A **feature branch** is a branch cut from `dev` to build one feature in isolation, then merged back.

Name it starting with a verb, never with a `feature/` prefix, eg `add-search-filter`, `fix-token-refresh`.

Assume local `HEAD` is the feature branch. Observe it with `git log dev..HEAD`: the commits it holds that `dev` lacks.




































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





### {[ClaudeCode:TodoWrite] Usage}

track resolution with the `TodoWrite` tool — one todo per unmerged path, marked complete only after its markers are gone and the file parses





### {[task-tracking] Fallback}

track resolution with a markdown task list — one item per unmerged path, checked off only after its markers are gone and the file parses



































## Open Pull Request

<!-- todo create pull request skill -->

tmp content for Open Pull Request

### {description}

tmp description Open Pull Request

### {when_to_use}

tmp when_to_use Open Pull Request




































## Clean Up Branches

You delete **local** branches already merged into the current branch. Nothing else is in scope — no remote or remote-tracking refs, tags, stashes, worktrees, index, or working tree. Stop and say so if `HEAD` is detached or a merge, rebase, cherry-pick, or bisect is in progress.





#### Candidates

- take the set from `git branch --merged`, resolved against the current branch
- drop the current branch, protected branches (`main`, `master`, `develop`, `trunk`, `release/*`), and anything the user names
- a branch absent from that set is never a candidate, for any reason





#### Delete

`git branch -d` only. `-D` and `--delete --force` are forbidden, including as a retry; a refusal from `-d` stands — leave the branch and report it.

Present candidates and exclusions together and wait for an answer whenever the set is unclear: an unstated protected list, a candidate that looks like live work, or a current branch that is not the integration target. Deleting nothing is the correct outcome of an unanswered question. Once settled, pass every remaining name to a **single** `git branch -d` call — never loop, never one at a time.





#### Report

- each branch deleted, with the tip hash Git prints, so the user can recover it
- each branch skipped, and why
- if nothing qualified, say so in one line and stop













### {description}

Checks prune repository's local branches

### {when_to_use}

Trigger on "clean up branches," "prune merged branches," or "delete old/stale branches."