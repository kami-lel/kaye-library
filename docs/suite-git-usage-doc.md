# Kaye Library: Suite and Git Usage Documentation

English | [简体中文](suite-git-usage-doc.zh-CN.md)

Run a big task as a **Suite**: planned first, built in small reviewable steps, safe to pause. Read *Why*, then see *Example* at the end for a worked session.

Every skill involved, the Suite skills and every Git skill, is explained in the [Skill Reference](#skill-reference) below; the [Skill Catalog](skill-catalog-doc.md#movements-and-suites) lists them in brief.

## Why

An agent asked for a large change tends to do it all in 1 pass: 30 files edited, 1 giant diff, nothing you can accept in part, and a lost session loses everything.

A Suite fixes that by splitting **thinking** from **doing**:

- **Plan first**: the agent reads your repository and writes a plan file. You approve it before any edit.
- **Small steps**: each step (a **Movement**) is 1 reviewable unit and 1 git commit, so you accept, reject, or redirect piece by piece.
- **Saved state**: the plan file records progress, so you pause tonight and resume tomorrow, even in a new session.
- **Parallel lines**: independent stretches of work can run at once as agent-only **Voices**.

Use it for explicit, multi-file, multi-round work. For a one-turn task, just ask.

## The Vocabulary

These words mean something specific here, not their everyday sense.

| Term | Meaning here |
|---|---|
| **Suite** | the whole big task, kept in 1 plan file; not a test suite. Often 1 Suite = 1 feature branch |
| **Movement** | 1 numbered step of a Suite, sized to be judged and accepted or rejected on its own; not a UI motion. 1 Movement = 1 git commit |
| **Voice** | 1 ordered line of Movements. The **Main Voice** (🧩) is the one you review; an **instrumental Voice** (🎻 Violin, 🎺 Trumpet, ~) is agent only and runs in parallel on its own branch |
| **Plan file** | the Suite written down as `<task>-suite-plan.md`: the plan **and** the saved progress, which is what lets a run pause and resume |
| **Halt / Cascade** | the 2 paces: stop after every Movement and wait for you, or keep going until the Suite is done |
| **Rework** | when reality stops matching the plan, the agent stops, rewrites the plan, and asks you again; it never works around it |
| **Linked worktree** | a second checkout of the repo in its own folder, 1 per task, so your main folder stays untouched |

## Shorthand

Single letters you can type in chat instead of whole sentences:

| Type | Means | Does |
|---|---|---|
| `c` | continue | resume the run; under halt, opens the next Movement |
| `n` | next | move on to the next one: the next Movement or the next item |
| `g` | git commit | commit **only the changes made in this conversation**, through `/commit-sense`; changes the agent did not make are left alone, and it asks when unsure |
| `gi` | git commit indexed | commit **only what is already indexed**, changes the agent does not know about included; the workspace is untouched |
| `ig` | index all, commit | index **every** workspace change, unknown ones included, then commit |

*Indexed* means queued for the next commit (what Git calls staged). Pick `g` for "commit my agent's work", `gi` when you indexed files by hand and want exactly those, `ig` for "commit everything in the folder".

## Skill Reference

Every skill in the Suite workflow, what it does, and when it fires. Call one by name (`/play-suite`) or just describe the need; your agent picks it. Most fire on their own once a Suite is running.

### Plan It

#### `/plan-for-suite` 🌟

Turns an oversized task into a Plan file, then holds for your approval. Runs in 2 phases:

- **Gather**: read-only. The agent reads entry points, conventions, and the files the task touches, establishes what already exists, is half done, or is missing, and asks you about anything ambiguous (scope, priorities, trade-offs). In Claude Code this runs in plan mode, so no edit is possible.
- **Write the Plan**: the agent splits the task into numbered Movements and saves them to `<task>-suite-plan.md` (workspace root, else repository root). Each Movement records its **Scope** (files, all named, few), **Statement** (what and why, in a line or two), **End State**, **Party** (who performs it: the agent, you, or another party by name), and **Status** (`Pending`).

The file opens with a fixed preface telling whoever runs it which skill to load first, then `## Context`, `## Terrain` (technical particulars, relevant files, constraints), and, when needed, `## Design`, `## Order` (a dependency graph, only with Voices), and `## Rework`. Movements sit under `## Main Voice` and one `## 🎻 Violin Voice`-style heading per instrumental Voice.

The agent also decides the housekeeping on its own from the repository state: a Movement that cuts a **feature branch** (when git is in use and some Movement edits a tracked file), one that plants a **linked worktree** (when the main worktree is busy or you asked to leave it untouched), a closing Movement that **lands** the branch, and an instrumental **Voice** only when 3+ Movements of agent-only work share no file with any other Voice. Voice count favors few and large: each Voice holds at least 5 Movements.

Fires on "plan this", "break into Movements", "go step by step". Not for one-turn tasks.

#### `/rework-plan-for-suite`

Handles a plan that stopped matching reality: a bug, a false assumption, a wrong or unnecessary Movement, unaccounted-for work, a redirect from you, or a workspace that no longer matches on resume. The agent **halts at once and never works around it**, then:

1. presents the finding: the Plan's assumption, the reality, the cost to the Movements ahead
2. rewrites the whole plan (never a diff); finished Movements stay untouched and numbered
3. marks every Movement's Status (`Pending`, `Done`, `Halted`, `Dropped`)
4. never renumbers: a split Movement keeps its number and gains sub-Movements (`Movement 1.1`, `Movement 1.2`)
5. appends the finding to `## Rework`, oldest first, never editing an earlier entry
6. holds for your approval, then resumes at the earliest unfinished Movement

Fires mid-run, even unprompted. You can call it yourself: "replan", "the plan no longer fits".

### Run It

#### `/play-suite`

Plays the approved Plan's **Main Voice**. The agent enters each Movement in order, does its work inside the Movement's boundary until its End State holds, commits it, recaps, and hands control back. Nothing is skipped or combined; **your word overrides the order**, so skipping ahead, doing several at once, or setting the plan aside is obeyed without protest.

- **Saved state**: the plan file is the run's memory. Say "pause" and each Status is written down; on resume the agent enters the earliest Movement not `Done` or `Dropped` and first checks that the feature branch, instrumental branches, and linked worktrees still exist.
- **Your own Movements**: for a Movement whose Party is you, the agent never does the work: it states the goal, gives 1 step at a time, waits for your report, then settles the End State by your confirmation or its own check, and says which.
- **Other parties** get the steps and End State handed over, then the agent verifies their report.
- **Progress tracking**: the agent's todo list holds 1 entry per Movement, every Voice included, with the current one marked.

Fires on a Plan file's preface, on "begin", "continue", "pause", "resume", or `c`.

#### `/halt-each-movement` and `/cascade-all-movements`

The two paces for the Main Voice; the agent asks which at the start of a run.

| | `/halt-each-movement` | `/cascade-all-movements` |
|---|---|---|
| Turn | 1 Movement per Turn | all remaining Movements in 1 Turn |
| Next step | you say `c` or "continue" | automatic |
| Stops when | each Movement closes | the Suite is done, or a Movement's Party is you |
| Commit | edits are **indexed** at Turn stop, committed when you approve (`g`) | committed at every Movement's close |
| Ends with | `🎏` closed line + `🧭` next line | one `🎏` line per Movement, then `🏁` |

Both mark progress with the same dispatch marks: `🎏 🧩3\7 …` closes Movement 3 of 7, `🧭 🧩4 …` names the next, `🎌 …` marks an instrumental Voice merged back, `🏁 …` closes the Suite. In Claude Code a cascade also sends a push notification when it must stop for you. An instrumental Voice is never halted inside, in either mode.

Triggers: "one Movement at a time", "let me review between Movements" (halt); "run all Movements", "keep going until the Suite is done" (cascade).

### Voices

#### `/solo-voice`

Runs 1 **instrumental Voice** whole, agent only, as a subagent or in its own session. The main session names the Plan file and the Voice, and nothing else; the Voice reads the Plan itself. It works only in its own linked worktree on its own instrumental branch, commits 1 per Movement, **never asks you anything and never merges its branch**. On a mismatch with the Plan or an End State that will not hold, it stops and reports.

It ends with 1 report: per Movement, its commit hash and End State (met, or why not), where it stopped, and what remains. The main session then merges the branch back into the feature branch, uproots the worktree, prunes the branch, and marks `🎌`. A subagent is the default mode; its own session is for a Voice too large for a subagent, or one you want to watch.

Fires only when dispatched; not for the Main Voice.

### Git: Rules and Commits

The Suite schedules the worktree, landing, and pruning skills as ordinary Movements and names the skill in the Movement's Statement; the rest fire on their own. You rarely call any of them by hand during a Suite.

#### `/working-with-git`

Sets the working terms and the limits, so edits stay in the workspace beside you. It loads on its own whenever the agent works in a Git repository.

- edits go in the workspace; the agent indexes its own changes when done or partly done, and runs `git status` or `git diff` only when the codebase differs from what it expects
- **you may be working in the same folder**: a change the agent did not make is yours, so it never reverts, indexes, or commits it, and stops to report if it blocks the work
- **needs your exact word, in the same Turn**: rewriting history (`commit --amend`, `rebase`, `reset`, `cherry-pick`), discarding work (`reset --hard`, `checkout .`, `restore .`, `clean -f`, `stash drop`, `branch -D`), publishing (`push`, `push --force`, `tag`, `gh pr create`), sweeping or bypassing (`add -A`, `add .`, `--no-verify`)
- every commit goes through `/commit-sense`, never a message format of its own

#### `/commit-sense` 🌟

Commits the indexed diff. The message is drawn from the conversation, optionally checked against `git diff --cached --numstat`, then committed once. It has up to 3 parts: a **primary message** over the whole diff, a **file ledger** (per file: a change sigil, the filename, a short summary; a single file gets sigil and name only), and an optional co-author trailer.

```text
restructure commit sense under Git hierarchy
🪧`CHANGELOG.md` remove stale TT
📖`http-api-doc.md` document commit-sense prompt nodes
🧪`__init__.py` update fixtures: heading levels
```

The reply is 1 line, eg `🚩🐙 Commit a3f9c21`; if Git rejects the commit, the agent reports its output and stops. Fires on `g`, "commit this", "write a commit message".

#### `/commit-sense-branch-merging`

Writes the message of a merge in progress, working on the message alone: the merge, its commit, the index, and the working tree stay yours. It prepends a typed first line to Git's own message, kept verbatim, and appends the co-author trailer. The first line follows the branches involved:

| From | Into | First line |
|---|---|---|
| feature | `dev` | `Feature Landing: BRANCH` |
| `dev` | feature | `Catch Up: BRANCH` |
| `dev` | `main` | the version title, eg `Minor Release 1.1.0` |
| hotfix or release | `main` | `BUMP Hotfix Release VERSION` or `BUMP Release Cut VERSION` |
| hotfix, release, or `main` | `dev` | `Hotfix Backport from VERSION` and its siblings |

An unknown branch pair is asked about, never guessed. Fires mid-merge: "write the merge message".

#### `/resolve-merge-conflict` ⭐

Untangles a halted merge, rebase, cherry-pick, or pull. It fixes only the files Git reports as unmerged, reads both sides with context first, and reconciles them **semantically**: imports, signatures, config keys, and call sites must still agree, and intent from both branches survives, never "ours" or "theirs" wholesale. Lock and generated files are regenerated, not hand-merged; every conflict marker is removed and each file checked; each path is indexed as soon as it is resolved. A decision it cannot infer goes to you.

It touches only the working tree and index: finishing or aborting the merge is your call. The report lists, per file, what each side changed, how it was reconciled, and what to double-check, then says the index is ready for `git merge --continue`.

### Git: Worktrees

A **linked worktree** is an extra working folder of the same repository, locked to its own branch, so edits in one task never touch another. Each task, often a Suite, gets 1 worktree on its single branch, never shared across tasks, never switched to another branch. The 1 split allowed: each instrumental Voice gets its own.

```text
WS-kaye-library/
├── kaye-library/                              # main worktree, on dev
├── kaye-library-WT-add-search-filter/         # linked worktree, feature branch
└── kaye-library-WT-add-search-filter-violin/  # linked worktree, instrumental branch
```

`WS-` marks the workspace folder holding several worktrees; `-WT-` marks a linked one, named `REPO-WT-BRANCH`.

#### `/tend-linked-wt` 🌟

A worktree's whole life, from placing it to removing it. It routes to the 2 skills below, and fires on starting, continuing, or finishing a task in a linked worktree, or on "don't touch main".

#### `/plant-linked-wt`

Creates the worktree for a task's existing branch, or cuts the branch with it when missing: a feature branch from the branch it will merge into (`dev`), an instrumental branch from the feature branch.

#### `/uproot-linked-wt`

Removes the worktree **only after every edit in it is committed and merged** into the branch it merges back into (the main worktree's branch for a feature branch, the feature branch for an instrumental branch). If any edit is not, it stops and reports.

### Git: Landing a Feature

A **feature branch** is cut from `dev` to build 1 feature in isolation, then merged back. It is named verb-first, never with a `feature/` prefix: `add-search-filter`, `fix-token-refresh`. Landing is 3 skills in a row; the Suite's closing Movement runs `/land-feature`, which runs the other 2.

#### `/ready-land-feature`

Syncs the docs the branch affects before a merge, in 7 Movements: sync the unit tests (if any), learn what the branch delivers (the conversation, `git log dev..HEAD`, the `[Unreleased]` entries, the diff if still unclear), record it in `CHANGELOG.md`, update `AGENTS.md` and `CONTEXT.md` to match, then commit the work. Files the branch does not affect stay untouched. Fires on "prep for merge", "document what I changed".

#### `/land-feature`

Readies the branch (all 7 Movements above), then merges it into `dev` with `--no-ff --no-commit`, so a merge commit records the landing and the pause lets the message be worded: `Feature Landing: BRANCH` plus a short branch summary. A linked worktree does the merge in the main worktree, which holds `dev`. Conflicts go to `/resolve-merge-conflict`. It stops at the merge commit: pushing and deleting wait for your approval, through `/scrub-landed-feature`.

#### `/scrub-landed-feature`

Reports the landing, then asks up to 3 approvals, each separate because a push publishes and a deletion cannot be undone:

```text
🚩🐙 Feature Landed: add status filter to Search page
✍️ ⓑ push `dev` to origin?
✍️ ⓒ delete feature branch `add-search-filter`?
✍️ ⓓ uproot linked worktree `kaye-library-WT-add-search-filter`?
ⓐ all of above
```

Answer `a` for all, or letters such as `bd`. It runs the approved actions in the order ⓑ, ⓓ, ⓒ (Git refuses to delete a branch a worktree still holds), and deletes with `git branch -d`, never `-D`.

#### `/submit-pr`

The review-first alternative: readies the docs the same 7 Movements, pushes the branch if the remote lacks it, then runs `gh pr create --base dev`, titled with the branch summary's headline and bodied with its changes. The pull request is left unmerged for the reviewer, and the agent replies with its URL.

#### `/prune-merged-branches`

Deletes local branches already merged into the current branch, using `git branch -d` only: a refusal stands, and the branch stays. It lists candidates and exclusions together and waits whenever the set is unclear (an unstated protected list, a branch that looks like live work). The report names each branch deleted with its tip hash, so you can recover it, and each skipped with the reason.

### Git: Releasing a Version

#### `/ready-release-version`

Prepares a release in 6 Movements: settle the version and date (both required; asked for if missing), bring the README and CREDITS current, update `docs/`, condense `AGENTS.md` and `CONTEXT.md` (pruned smaller, not just newer), close out the changelog (condense `[Unreleased]`, move it into a dated versioned section, leave a fresh `[Unreleased]`, update the comparison links), and bump the version in every metadata file (`pyproject.toml`, `package.json`, `Cargo.toml`, ~).

#### `/release-version` ⭐

Readies the release (the 6 Movements), commits the work, merges into `main` with `--no-ff --no-commit` and a typed message (`Minor Release 1.1.0`, ~), tags the merge `v` plus the version, then hands over to the scrub. Fires on "release 1.2.0", "cut a release and tag it".

#### `/scrub-released-version`

Reports the release, then asks up to 4 approvals:

```text
🚩🐙 Minor Release 1.1.0
✍️ ⓑ push `main` and `v1.1.0` to origin?
✍️ ⓒ prune merged branches `add-search-filter`, `fix-login-redirect`?
✍️ ⓓ fast-forward `dev` to `main`, local and origin?
✍️ ⓔ bump `dev` to `1.1.1-alpha`, local and origin?
ⓐ all of above
```

The next alpha raises the released patch by 1 and appends `-alpha`, so `dev` never claims a released version. The bump runs only after the fast-forward succeeds, and is committed through `/commit-sense`.

### Vocabulary

Supporting skills that carry the terms and notation. They load themselves whenever a Suite is announced or presented.

- `/agent-movement-and-suite`: defines **Suite**, **Voice**, and **Movement**, the sizing rules (each Movement reviewable and sharply bounded, numbered from 1 within its Voice), the instrument order for Voices, the 1-to-1 todo-list tracking, and the dispatch marks
- `/agent-movement-and-suite-with-count`: adds **Counts**, any countable atom inside a Movement (files affected, bugs fixed, tests written). A Movement then reads `a\b🧩c`: `a` Counts closed so far, `b` total Counts, `c` the Movement number, eg `9\12🧩2` is 9 of 12 Counts done, in Movement 2. Counts measure progress only and are never halted at
- `/agent-files-and-folders`: names new files in kebab case, folders in Pascal case, dated names led by the date; the Plan file's name comes from it

## Example: Adding a Search Filter

One session that touches everything: plan, review, parallel Voice, your own step, rework, pause, resume, finish. Swap in your own task. Quotes marked `You` are what you type; quotes marked `Kaye` (the agent) are what comes back.

#### Ask for a Plan

You describe the outcome; Kaye reads the repository and asks before guessing.

> You: /plan-for-suite Add a search filter to the product list: API param,\
> UI control, tests. Keep existing queries working.

> Kaye: Filter by name only, or by category too?

> You: both

> [!TIP]
> Name the outcome, not the steps, and answer its questions: they are the cheapest fixes of the whole run.

#### Review and Approve

Kaye writes the plan file and stops. Nothing is edited yet.

> Kaye: Plan ready: `search-filter-suite-plan.md`
>
> Approve, or tell me what to change.

This plan has 5 Movements in the Main Voice and a parallel Violin Voice. Each Movement lists its files and an **End State**, what *working* means when it closes: check those first. Movement 3's says only "UI works", so tighten it. Movement 4 is yours because only you can reach staging; Kaye will guide you, never do it.

> You: Movement 3 should end with "control filters live, empty result\
> shows a message". Otherwise approved.

#### Pick a Pace

Kaye asks how fast to run. Halt means 1 Movement per Turn, the safe choice for a first run.

> Kaye: Plan updated. Run under halt-each-movement or cascade-all-movements?

> You: halt

#### Run, Then Commit

Kaye does a Movement and stops. Under halt it indexes the edits and waits for you to commit them: `g` commits, `c` opens the next Movement.

> Kaye: 🎏 🧩1\5 Feature Branch Cut\
> 🧭 🧩2 Add the Filter Param to the API

> You: g

> Kaye: 🚩🐙 Commit `a3f9c21`

> You: c

Next, Kaye plants a linked worktree for the Violin Voice and starts it as a subagent, in parallel on its own branch, then does Movement 2.

> Kaye: 🎏 🧩2\5 Filter Param Added to the API\
> 🧭 🧩3 Wire the UI Control to the API

#### Fix a Movement

You read the diff and spot a gap. Say so: because 1 Movement = 1 commit, the fix touches nothing else.

> You: Movement 2 should skip empty strings

> Kaye: Fixed as a new commit.\
> 🎏 🧩2\5 Filter Param Skips Empty Strings\
> 🧭 🧩3 Wire the UI Control to the API

> You: c

#### Rework the Plan

Partway through Movement 3, reality stops matching the plan. Kaye halts instead of working around it and runs `/rework-plan-for-suite`: finding, rewritten plan, your approval.

> Kaye: 🛑 Halted. Plan assumed: the API already suggests values.\
> Reality: no suggestions endpoint exists. Cost: Movement 3 and 5.\
> Plan rewritten with 🧩3.1 Add the Suggestions Endpoint, logged\
> under ## Rework. Approve to continue.

> You: approved

#### Merge a Voice Back

The Violin Voice reports done. Kaye merges its branch back, removes its worktree, and marks it 🎌. Merging a Voice back halts like any Movement's close; `n` goes on to the next one.

> Kaye: 🎌 Violin Filter Tests Merged Back\
> 🧭 🧩3.1 Add the Suggestions Endpoint

> You: n

#### Pause and Resume

It is late, so you stop. The plan file carries the state, so a new session picks up where this one left off.

> You: pause

> Kaye: Status written to search-filter-suite-plan.md.

Next morning, in a new session:

> You: /play-suite search-filter-suite-plan.md

> Kaye: Branch and worktrees found. Resuming at 🧩3.1.

#### Cascade to the Finish

Trusting the pattern now, switch pace. The cascade runs on by itself and stops only at Movement 4, which is yours.

> You: /cascade-all-movements

> Kaye: 🎏 🧩3.1 Suggestions Endpoint Added\
> 🎏 🧩3 UI Control Wired to the API\
> 🔍 🧩4 Your Turn: Approve the Staging Deploy\
> Step 1: open the staging dashboard and ...

> You: done, it works

Kaye finishes, lands the feature, and closes the Suite with 🏁.

> Kaye: 🎏 🧩4 Staging Deploy Approved\
> 🎏 🧩5 Feature Landed on dev\
> 🏁 Search Filter
