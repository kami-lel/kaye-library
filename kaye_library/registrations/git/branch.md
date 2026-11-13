## feature branch

A **feature branch** is a branch cut from `dev` to build one feature in isolation, then merged back.

Name it starting with a verb, never with a `feature/` prefix, eg `add-search-filter`, `fix-token-refresh`.

Assume local `HEAD` is the feature branch. Observe it with `git log dev..HEAD`: the commits it holds that `dev` lacks.













### discover feature branch

Learn what the finished [feature branch](#feature-branch) delivers and why:

- read the current conversation for what was built and why
- understand the change set from both sources: `git log dev..HEAD` and the `[Unreleased]` entries of `CHANGELOG.md`; fold them together so nothing is stated twice
- if the two together leave the change unclear, read the change directly: `git diff dev...HEAD`













### feature branch summary

Only for a Feature Landing: the body of its merge message, per [Commit Sense For Branch Merging](#commit-sense-for-branch-merging), and the wording of its pull request, per [Submit Pull Request](#submit-pull-request).

Given [Discover Feature Branch](#discover-feature-branch), write the summary the reviewer merging into `dev` decides from, so lead with the outcome:

- headline: one verb-first sentence on what the branch delivers
- changes: 2~5 bullets grouped by purpose, each saying what changed and why it matters

Write strictly in [Briefness Style](#style-guide-briefness-style),
and apply [Commentary Case](#letter-case-commentary-case) to every line

example:

```md
add status filter to Search page

- filter results by status: no full-list scan for open items
- persist chosen filter in URL: reload/shared link keeps view
```

#### {avoid}

Retelling commits or listing files.



































## Ready for Feature Landing

Before merging the current [feature branch](#feature-branch), sync the docs it affects. Work in Movements; edit affected files in place and leave the rest untouched.





#### Movement 1~3: Sync Unit Test

If the project has unit tests, run [Sync Unit Test](#sync-unit-test) first.



##### {[Claude:Skill] Usage}

Invoke `sync-unit-test` skill via `Skill` tool.

##### {[Hermes:skill_view] Usage}

Load `sync-unit-test` skill with `skill_view`.






#### Movement 4: Learn the Feature Branch

Run [Discover Feature Branch](#discover-feature-branch), then use the change set it yields throughout Movement 5 & 6.





#### Movement 5: Record the Change Set in the CHANGELOG

Run [Maintain CHANGELOG](#maintain-changelog), recording the change set per [Repository CHANGELOG Writer](#repository-changelog-writer). The unreleased-only and deduplication rules come from that skill.






#### Movement 6: Sync AGENTS and CONTEXT

Run [Maintain Repository AGENTS](#maintain-repository-agents), updating any command, convention, or constraint the branch moved, per [Repository AGENTS Writer](#repository-agents-writer). Then update `CONTEXT.md` directly for any architecture the branch moved, per [Repository CONTEXT Writer](#repository-context-writer).





#### Movement 7: Commit the Work

Index the changes this work made, then run [Commit Sense](#commit-sense) to commit them.





### {description}

Records a feature branch's changes into `CHANGELOG.md` and updates `AGENTS.md` and `CONTEXT.md` to match, syncing all affected docs in one pass before a merge, then commits the work.

### {when_to_use}

Reach for this when wrapping up or merging a feature branch — "prep for merge," "finish this feature," "document what I changed," "update docs before merging." Not for cutting a versioned release (use the release skill) or general doc edits unrelated to a branch.





### {[Claude:Skill] Usage}

Invoke `sync-unit-test`, `maintain-changelog`, `maintain-repo-agents`, and `commit-sense` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `sync-unit-test`, `maintain-changelog`, `maintain-repo-agents`, and `commit-sense` skills with `skill_view`.


































## Perform Feature Landing

Land the current [feature branch](#feature-branch) on `dev`: ready it, then merge it, so `dev` never receives stale docs.



#### Movement 1~7: Ready the Feature Branch

Run [Ready for Feature Landing](#ready-for-feature-landing) whole. Continue only once its commit lands; keep its [feature branch summary](#feature-branch-summary) for Movement 8.



#### Movement 8: Merge into Dev

Merge per [Commit Sense For Branch Merging](#commit-sense-for-branch-merging) (feature into dev). When you work in a linked worktree, do every step in the main worktree, since it holds `dev`.

1. `git switch dev`, then `git merge --no-ff --no-commit FEATURE`: a merge commit records the landing, and the pause lets you word it
2. on conflicts, run [Resolve Merge Conflict](#resolve-merge-conflict), then go on
3. write the message, Git's drafted one read from `git rev-parse --git-path MERGE_MSG`, then `git commit` once

Stop at the merge commit: push and branch deletion wait for the approval of Movement 9.



#### Movement 9: Report and Ask Approval

Reply as below, asking up to 3 approvals: push `dev`; delete the feature branch (merged, so safe to drop); uproot its linked worktree, asked only when you work in a linked worktree. If any Movement halts, report where and why in one line, then stop.

<post-landing-output-example>
🚩🐙 Feature Landed: add status filter to Search page
✍️ ⓑ push `dev` to origin?
✍️ ⓒ delete feature branch `add-search-filter`?
✍️ ⓓ uproot linked worktree `kaye-library-WT-add-search-filter`?
ⓐ all of above
</post-landing-output-example>



#### Movement 10: Push and Delete

Run only the approved actions, in order ⓑ, ⓓ, ⓒ, since Git refuses to delete a branch while a worktree holds it; ⓐ approves all three:

- ⓑ `git push origin dev`
- ⓒ `git branch -d FEATURE`, never `-D`
- ⓓ invoke `uproot-linked-wt`

Reply once, after all are done:

<post-push-delete-output-example>
🚩🐙 pushed `dev` to origin
🚩🐙 uprooted `kaye-library-WT-add-search-filter`
🚩🐙 deleted `add-search-filter`
</post-push-delete-output-example>



### {description}

Lands a feature branch on `dev`: runs every Ready for Feature Landing movement, then merges the branch into `dev` with a typed Feature Landing message.

### {when_to_use}

Reach for this when a finished feature branch should be merged: "land this feature," "merge this into dev," "finish and merge." Not for prepping docs alone (use the ready-land-feature skill) or releasing a version.



### {[Claude:Skill] Usage}

Invoke `ready-land-feature`, `commit-sense-branch-merging`, `resolve-merge-conflict`, and `uproot-linked-wt` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `ready-land-feature`, `commit-sense-branch-merging`, `resolve-merge-conflict`, and `uproot-linked-wt` skills with `skill_view`.






## Ready for Version Release

Cut a new release: bring all docs current, finalize the changelog, and bump the project version.



#### Movement 1: Decide Release Version and Date

- require both a version number and a release date; if either is missing, ask the user before proceeding
- the version must match [Project Semantic Version](#project-semantic-version)



#### Movement 2: Maintain the README

Run [Maintain README](#maintain-readme): overview, features, setup, usage, version-dependent details.



#### Movement 3: Condense AGENTS and CONTEXT

Run [Condense AGENTS and CONTEXT](#condense-agents-and-context): changed commands, conventions, constraints, architecture.

While in `CONTEXT.md`, prune as well as update: keep only what describes the released state, and cut superseded plans, stale notes, and history no longer worth a reader's time. The file should end up smaller, not just newer.



#### Movement 4: Maintain the Docs Directory

Run [Maintain Repository Docs](#maintain-repository-docs): affected files under `docs/`.



#### Movement 5: Condense the Changelog

Run [Condense CHANGELOG](#condense-changelog) to reword `[Unreleased]` entries into changelog style and settle any Admonitions for Breaks and Hazards.



#### Movement 6: Close Out the Changelog

1. move every (now-condensed) `[Unreleased]` entry, admonitions included, into a new versioned section headed with the version and date from Movement 1, keeping only non-empty subsections
2. leave a fresh `[Unreleased]` section above it, carrying every standard subsection heading with no entries beneath
3. update the GitHub comparison links so every version, including the new tag, stays referenced



#### Movement 7: Bump the Repository Version

Set the version to match Movement 1 exactly, in whichever metadata files apply — `setup.cfg`, `pyproject.toml`, `package.json`, `Cargo.toml`, and the like.













### {description}

Cuts a project release: brings `README.md`, `CHANGELOG.md`, `AGENTS.md`, `CONTEXT.md`, and `docs/` current, moves `[Unreleased]` changelog entries into a dated versioned section, and bumps the version across metadata files like `package.json`, `pyproject.toml`, `Cargo.toml`, or `setup.cfg`.

### {when_to_use}

Reach for this on release requests — "ship v1.2.3," "cut a release," "tag a version," "bump the version," "prep the release." Not for logging a single in-progress change (use the changelog-maintain skill) or landing a feature branch before merge (use the feature-landing skill).





### {[Claude:Skill] Usage}

Invoke `maintain-readme`, `condense-changelog`, `condense-agents-and-context`, and `maintain-repo-docs` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `maintain-readme`, `condense-changelog`, `condense-agents-and-context`, and `maintain-repo-docs` skills with `skill_view`.

### {[Claude:AskUserQuestion] Usage}

- if version number or release date is **missing**, use `AskUserQuestion` to ask user before proceeding

### {[Hermes:clarify] Usage}

- if version number or release date is **missing**, use `clarify` to ask user before proceeding


































## Perform Version Release

Release the project: ready it, merge it into `main`, then tag the merge, so every tag marks a release with current docs.



#### Movement 1~7: Ready the Release

Run [Ready for Version Release](#ready-for-version-release) whole. Keep the version it settles for Movement 9~12.



#### Movement 8: Commit the Work

Index the changes Movement 1~7 made, then run [Commit Sense](#commit-sense) to commit them.



#### Movement 9: Merge into Main

Merge the current branch per [Commit Sense For Branch Merging](#commit-sense-for-branch-merging) (into main):

1. `git switch main`, then `git merge --no-ff --no-commit SOURCE`: a merge commit records the release, and the pause lets you word it
2. on conflicts, run [Resolve Merge Conflict](#resolve-merge-conflict), then go on
3. write the message, Git's drafted one read from `git rev-parse --git-path MERGE_MSG`, then `git commit` once



#### Movement 10: Tag the Release

Tag the merge commit with `v` plus the version: `git tag vVERSION`, eg `git tag v1.0.0`.



#### Movement 11: Report and Ask Approval

Reply as below, asking 3 approvals: push `main` and the tag, prune merged branches, naming each branch to prune (the candidates of [Prune Merged Branches](#prune-merged-branches)), and fast-forward `dev` to `main`, local and remote. If any Movement halts, report where and why in one line, then stop.

<post-release-output-example>
🚩🐙 Minor Release 1.1.0
✍️ ⓑ push `main` and `v1.1.0` to origin?
✍️ ⓒ prune merged branches `add-search-filter`, `fix-login-redirect`?
✍️ ⓓ fast-forward `dev` to `main`, local and origin?
ⓐ all of above
</post-release-output-example>



#### Movement 12: Push, Prune, and Sync Dev

Run only the approved actions, in order; ⓐ approves all three:

- ⓑ `git push origin main vVERSION`
- ⓒ invoke `prune-merged-branches`
- ⓓ fast-forward `dev` to `main`, local and origin; if it cannot fast-forward, report in one line and stop

Reply once, after all are done:

<post-push-prune-output-example>
🚩🐙 pushed `main` and `v1.1.0` to origin
🚩🐙 pruned `add-search-filter`, `fix-login-redirect`
🚩🐙 fast-forwarded `dev` to `main`, local and origin
</post-push-prune-output-example>



### {description}

Releases the project: runs every Ready for Version Release movement, merges the branch into `main` with a typed release message, and tags the merge with its `v` version.

### {when_to_use}

Reach for this when a release should go out: "release 1.2.0," "cut a release and tag it," "merge to main and tag." Not for prepping the release alone (use the ready-release-version skill) or landing a feature branch (use the land-feature skill).



### {[Claude:Skill] Usage}

Invoke `ready-release-version`, `commit-sense`, `commit-sense-branch-merging`, `resolve-merge-conflict`, and `prune-merged-branches` skills via `Skill` tool.

### {[Hermes:skill_view] Usage}

Load `ready-release-version`, `commit-sense`, `commit-sense-branch-merging`, `resolve-merge-conflict`, and `prune-merged-branches` skills with `skill_view`.
