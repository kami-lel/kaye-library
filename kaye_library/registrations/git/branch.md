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

Only for a Feature Landing: the body of its merge message, per [Commit Sense For Branch Merging](#commit-sense-for-branch-merging), and the wording of its pull request, per [Open Pull Request](#open-pull-request).

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

<!-- TODO write perform feature landing -->

tmp content for Perform Feature Landing

### {description}

tmp description Perform Feature Landing

### {when_to_use}

tmp when_to_use Perform Feature Landing











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





### {[git] Usage}

Invoke `prune-merged-branches` as Movement 5, if any branch needs pruning. Movements 5~7 renumber to 6~8


































## Perform Version Release

<!-- TODO write perform version release -->

tmp content for Perform Version Release

### {description}

tmp description Perform Version Release

### {when_to_use}

tmp when_to_use Perform Version Release
