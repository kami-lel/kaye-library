## Plan for Suite

This uses the [Movement, Voice, and Suite](#movement-voice-and-suite) concepts on a Plan file — a Plan is a Suite, so it holds multiple Movements.

Two *Bars*, then Execution:













### Bar 1: Gather

Do **not** start editing. Read before you plan.

Resolve the task's scope from the repository itself — entry points, existing conventions, the files the task will touch, and anything the description leaves ambiguous. Prefer reading the actual code over assuming its shape.

Establish where the project stands **now**: what already exists, what is partially done, what is missing. The Plan starts from the real state, never from a clean slate.

Where the reading leaves intent unclear — scope, priorities, trade-offs, which of several readings is meant — ask the user rather than deciding yourself.





#### {[Claude:Enter/ExitPlanMode] Usage}

- opens with `EnterPlanMode` tool, so all discovery runs before any edit is possible

#### {[Claude:AskUserQuestion] Usage}

- use `AskUserQuestion` tool to ask user

#### {[Hermes:clarify] Usage}

- use `clarify` tool to ask user













### Bar 2: Write the Plan

The Plan divides the task into Movements.

The Plan is a **deliverable** and lives in a **Plan file**, so later Movements can revise it in place.

Lay the file out per [Plan File](#plan-file).

Hand the Plan to the user and **stop**. The codebase stays exactly as it is until they approve.





#### Movement Record

The Plan must be **readable at a glance** and **workable in order**. Any layout serving both is fine. Record for each Movement:

- Scope: the files it touches, all named, and few
- Statement: what changes and why, in a line or two — never a code dump
- **End State**: what *Working* means once the Movement closes, so review can stop there
- Party (who performs it): you, the user, or another party by name; give the user what lies beyond your reach, eg a GUI step, a login, a device, an approval
- Status: always write `Pending` when first writing the Plan

Record no Order field. With only the Main Voice, the Movement numbers give the order; with instrumental Voices, `## Order` holds every dependency.





#### Plan File

- Name: [Kebab Case](#letter-case-kebab-case) slug of the task, ending `-suite-plan.md`, eg `auth-refactor-suite-plan.md`
- Location: first available of workspace root, repository root, your own temporary location
- 1 Plan file holds the whole Suite, every Voice included

Open the file with the preface below, *verbatim* and ahead of all Plan content, so whoever executes it reads the terms before the first Movement.

<plan-for-suite-preface>
Before working from this file, invoke the skill for the Voice you run: `play-suite` if you run the Main Voice, `solo-voice` if you run an instrumental Voice.

If you run the Main Voice, ask the user whether to run under `cascade-all-movements` or `halt-each-movement`, then follow the chosen skill.
</plan-for-suite-preface>

Top-level headings, all `##`, in this order after the preface:

- `## Context`: what a reader needs to grasp the Plan at a glance, high level, as an indented outline: the goal, the state it starts from, each [Housekeeping Movements](#housekeeping-movements) decision that came out yes with a one-line reason (the feature branch with its name, the linked worktree with its path, each instrumental Voice with its instrumental branch name)
- `## Terrain`: what belongs to this Plan alone, in detail: technical particulars, where to find the relevant files, constraints, anything a Movement leans on
- `## Design`: optional, only when the Plan brings a complicated new design, eg an API or a data shape; where the design replaces something, compare new against old side by side
- `## Order`: optional, only with instrumental Voices: a Mermaid graph of every Movement's dependencies, each instrumental Voice a subgraph, per [Diagrams](#diagrams); it holds every dependency, so the Movement record carries no Order field
- `## Rework`: optional, absent from a first draft; the history of every [rework](#plan-for-suite-rework), oldest first: append 1 numbered entry per rework, never edit or drop an earlier one, even when a later rework reverses it; each entry holds the finding (the Plan's assumption, the reality, the cost) and the Movements it revised, removed, added, or split
- `## Main Voice`: the Main Voice's Movements
- `## 🎻 Violin Voice`: 1 per instrumental Voice, in instrument order, each holding its Movements


###### Movement Heading

In the Plan file, head each Movement `🧩a: Title` in the Main Voice and `🎻a: Title` in an instrumental Voice, with its Voice's own emoji, as an `h3` under its Voice's `h2`. Between number and colon, add, in order and only when they apply:

- `{party}`: for a Movement that is not yours, never for your own
- `[workspace]`: when the task spans several workspaces or repositories

The user is a party too, by their own name, eg `{John}`.

```
### 🧩5 [api]: Wire Up the Config Loader
### 🧩6 {John} [api]: Approve the Staging Deploy
### 🎻2 [api]: Add the Retry Wrapper
```





##### {[Claude:Skill] Usage}

Invoke the skill chosen for this run — `cascade-all-movements` or `halt-each-movement` — via `Skill` tool.

##### {[Hermes:skill_view] Usage}

Load the skill chosen for this run — `cascade-all-movements` or `halt-each-movement` — with `skill_view`.

##### {[Claude:Enter/ExitPlanMode] Usage}

delivers the finished Plan through `ExitPlanMode` tool, which is where the user approves it

If the Plan File is finished while already out of plan mode, never assume the user approved it: still seek approval, by `EnterPlanMode` then `ExitPlanMode`

##### {[git] Usage}

Never index or commit the [Plan File](#plan-file), unless the user explicitly asks: it is run scratch, not project history.





#### Housekeeping Movements

Housekeeping Movements set up and tear down the Suite's branches and worktrees: cutting, planting, merging, uprooting, pushing. Write one only if the Suite needs it, as an ordinary Movement of the Main Voice, decided from the repository state gathered in Bar 1, without asking; a Suite that needs none gets none.


###### Opening Movement

If the Suite needs a [feature branch](#feature-branch), open with a Movement that cuts it. It is needed when the repository uses git, the Suite's commits should land together, and some Movement edits a tracked file; it is not needed when the user said to work on the current branch.

If the main worktree is busy, or the user asked to leave it untouched, that Movement also plants the linked worktree per [Plant the Linked Worktree](#plant-the-linked-worktree), which cuts the feature branch when missing.


###### Closing Movement

If the Suite has a feature branch, close with a Movement that lands it per [Perform Feature Landing](#perform-feature-landing), then scrubs up per [Scrub After Feature Landing](#scrub-after-feature-landing).

If stale merged branches are in the way, add 1 Movement that prunes them per [Prune Merged Branches](#prune-merged-branches).


###### Instrumental Voice Movements

Form an instrumental [Voice](#movement-voice-and-suite) only if the Suite has a feature branch and a stretch of 3+ Movements you perform alone whose Scopes share no file with the Main Voice or any other Voice. Otherwise keep the work in the Main Voice; favor the Main Voice and keep the Voice count low.

Each Voice formed adds 2 housekeeping Movements:

- opening, in the instrumental Voice: plant its linked worktree per [Plant the Linked Worktree](#plant-the-linked-worktree), cutting its instrumental branch from the feature branch
- closing, in the Main Voice: after the Voice's report, merge its instrumental branch into the feature branch, uproot its linked worktree per [Uproot the Linked Worktree](#uproot-the-linked-worktree), and prune the merged branch per [Prune Merged Branches](#prune-merged-branches); place any Movement that depends on the Voice after it, and record the dependency in `## Order`



##### {[Claude:Skill] Usage}

Name in each Housekeeping Movement's Statement the skill that performs it, to invoke via `Skill` tool: `plant-linked-wt` to plant a linked worktree, `uproot-linked-wt` to uproot it, `land-feature` to land, `scrub-landed-feature` to scrub up after landing, `prune-merged-branches` to prune.

##### {[Hermes:skill_view] Usage}

Name in each Housekeeping Movement's Statement the skill that performs it, to load with `skill_view`: `plant-linked-wt` to plant a linked worktree, `uproot-linked-wt` to uproot it, `land-feature` to land, `scrub-landed-feature` to scrub up after landing, `prune-merged-branches` to prune.





### {description}

Splits oversized task into ordered, numbered Movements, then runs them under review — survey repository, write Plan file, hold for approval, execute 1 Movement per turn

### {when_to_use}

On large, multi-file, multi-concern work wanted reviewable, not 1 pass. Triggers: plan this, break into Movements, go step by step. Start before any edit, so survey precedes Plan, Plan precedes 1st change. Not for 1-turn tasks













### Plan for Suite: Execution

Starts only after the user approves the Plan. Follow Plan order — nothing skipped, nothing combined.

The Plan file holds the context and Terrain: start from it, read your Movements there, and explore the repository only when a Movement needs more. Leave the Plan file untouched unless a rule says to write it.

Never work around a mismatch with the Plan, an End State that will not hold, or anything a Movement cannot settle alone.

Each Voice works only on its own branch and in its own worktree, and never touches another Voice's.

Housekeeping splits by Voice: the instrumental Voice cuts its instrumental branch and plants its linked worktree, as its own opening Movement; the Main Voice merges, uproots, and prunes, as its own closing Movement. Any other housekeeping Movement is an ordinary Movement.

Each Movement runs these steps in order:

1. Movement In: enter the Movement next in order
2. Task: do its work, touching nothing outside the Movement's boundary, until its End State holds




#### {[Claude:Skill] Usage}

For each Movement's git commit, invoke `commit-sense` via `Skill` tool.

Run a housekeeping Movement through the skill its Statement names, invoked via `Skill` tool: `plant-linked-wt` to plant a linked worktree, `uproot-linked-wt` to uproot it, `land-feature` to land, `scrub-landed-feature` to scrub up after landing, `prune-merged-branches` to prune.

#### {[Hermes:skill_view] Usage}

For each Movement's git commit, load `commit-sense` with `skill_view`.

Run a housekeeping Movement through the skill its Statement names, loaded with `skill_view`: `plant-linked-wt` to plant a linked worktree, `uproot-linked-wt` to uproot it, `land-feature` to land, `scrub-landed-feature` to scrub up after landing, `prune-merged-branches` to prune.

#### {[git] Usage}

1 Movement = 1 commit. A Movement that edits no workspace file, such as a user Movement, commits nothing.












### Play Suite

You play the Main Voice of an approved Plan.

If not already answered, ask whether the Main Voice runs under `cascade-all-movements` or `halt-each-movement`.

Run each Movement's steps per [Plan for Suite: Execution](#plan-for-suite-execution), then close it:

3. [Movement Recap](#movement-recap)
4. Movement Out: return control to user

On resume, Movement In to the Movement its Status names, per [Saved State](#saved-state).

Check the Movement's Party at Movement In. Your own Movements run as above; any other party follows [Movement Parties in Execution](#movement-parties-in-execution).

Movement order binds your judgement, not the user's. Out of sequence, several at once, one skipped, the Plan set aside — obey without protest, noting which Movements are left.



##### Instrumental Voices

Start each instrumental Voice once every Movement it depends on is done:

1. choose its mode: a subagent by default, wherever a subagent tool exists; its own session when the Voice outgrows a subagent's budget, when the user wants to watch it, or when no subagent tool exists
2. start it with 1 prompt naming the Plan file and the Voice, and nothing else: the Voice reads the Plan and starts on its own with `solo-voice`; in session mode, ask the user to open a new session and give it that prompt
3. go on with the Main Voice on the feature branch; a Main Voice Movement that depends on the Voice waits for its closing Movement

On the Voice's report:

- every End State met: run the Voice's closing Movement, merging its instrumental branch into the feature branch, uprooting its linked worktree, and pruning the merged branch, then mark the merge back with 🎌 in the Movement Recap
- a stop or a mismatch: halt per [Plan for Suite: Rework](#plan-for-suite-rework)



##### Saved State

The Plan file doubles as the run's saved state, so a run survives the end of a session:

- Pause: only when the user explicitly states "pause", never on a halt; then set each Movement's Status keyword to where the run stands
- Resume: read each Movement's Status, Movement In to the earliest not `Done` or `Dropped`; check that the feature branch, each open instrumental branch, and their linked worktrees still exist; on a mismatch with the workspace, halt per [Plan for Suite: Rework](#plan-for-suite-rework)

Status keywords, written only on a pause or a rework. Each Movement carries exactly one keyword at any moment:

- `Pending`: not entered yet, the starting keyword
- `Done`: closed Working
- `Halted`: stopped, awaiting rework
- `Dropped`: removed by rework



##### Movement Parties in Execution

For a user Movement, never do the work yourself. Guide interactively:

1. Movement In: say the Movement is theirs and its goal
2. give one step at a time; wait for their report before the next
3. halt per [Plan for Suite: Rework](#plan-for-suite-rework) if a report contradicts the Plan
4. settle the End State by their confirmation or your check, and say which
5. Movement Out once it holds

For another party, hand over steps and End State, await its report, then verify.



#### Movement Recap

Always end the Turn with a 2-line [Turn Progress Dispatch](#turn-progress-dispatch), each line prefixed per [Movement Notation](#movement-notation) and [Dispatch Marks](#dispatch-marks):

```
🎏 🧩3\7 Rewrote the Entry Point
🧭 🧩4 Wire Up the Config Loader
```

At an instrumental Voice's merge back, add its line:

```
🎌 Violin Test Fixtures Merged Back
```

Except when the entire Plan is completed — then end with a 1-line Turn Progress Dispatch naming the Plan instead:

```
🏁 Auth Refactor
```

##### {[for Claude VSC]}

Link each line to the Plan file, at the line number of that Movement's heading — or to the Plan file itself when naming a completed Plan:

```markdown
🎏 [🧩3\7 Rewrote the Entry Point](file:///path/to/plan-file.md#L42)
🧭 [🧩4 Wire Up the Config Loader](file:///path/to/plan-file.md#L58)
```

```markdown
🏁 [Auth Refactor](file:///path/to/plan-file.md)
```



#### {[Claude:Skill] Usage}

Invoke the skill chosen for this run — `cascade-all-movements` or `halt-each-movement` — via `Skill` tool.

When halting for [Plan for Suite: Rework](#plan-for-suite-rework), invoke `rework-plan-for-suite` via `Skill` tool.

#### {[Hermes:skill_view] Usage}

Load the skill chosen for this run — `cascade-all-movements` or `halt-each-movement` — with `skill_view`.

When halting for [Plan for Suite: Rework](#plan-for-suite-rework), load `rework-plan-for-suite` with `skill_view`.




#### {[Claude:Agent~] Usage}

Start a subagent-mode Voice with 1 `Agent` call in the background, its prompt naming the Plan file and the Voice, and carrying nothing else.

#### {[Hermes:delegate_task] Usage}

Start a subagent-mode Voice with 1 `delegate_task` call: `goal` names the Voice, `context` names the Plan file, and nothing else goes in. A child shares your working directory, so the Voice enters its own linked worktree by absolute path.

#### {[agent] Fallback}

With no subagent tool, run every instrumental Voice in session mode.




#### {[Claude:AskUserQuestion] Usage}

use `AskUserQuestion` tool to confirm each step or the End State of a user Movement, carrying likely replies as options

#### {[Claude:PushNotification] Usage}

Call `PushNotification` when the entire Suite is completed.

Write 1 line: emoji + Suite name

```text
🏁 Auth Refactor
```

#### {[Hermes:clarify] Usage}

use `clarify` tool to confirm each step or the End State of a user Movement, carrying likely replies as options



#### {description}

Plays approved Plan file's Main Voice, 1 Movement per turn — Movement In, work, present with link back, Movement Out. Plan file doubles as saved state, so pause and resume carry across sessions

#### {when_to_use}

On Plan file preface; on instruction to begin, continue, pause, or resume; on any *continue* shorthand. Not for drafting Plans (`plan-for-suite`), reworking them (`rework-plan-for-suite`), or running an instrumental Voice (`solo-voice`)













### Solo Voice

You run 1 instrumental Voice of a Suite whole. The main session names the Plan file and the Voice, and nothing else.

- run the Voice's Movements per [Plan for Suite: Execution](#plan-for-suite-execution), its opening Movement first
- work only in the Voice's linked worktree, on its instrumental branch
- never merge or prune the instrumental branch: the main session merges the Voice back
- never ask the user anything, nor wait for an approval
- on a mismatch with the Plan, an End State that will not hold, or anything a Movement cannot settle alone, stop and report

End with 1 report, nothing after it: per Movement, its short commit hash and its End State (met, or why not), then where you stopped and what remains unrun.





#### {[Claude:Agent~] Usage}

Send the report to the main session: find it with `ListAgents`, then send the report with `SendMessage`; end your final reply with the same report.

#### {[Claude:Agent~] Lack}

End your final reply with the report, for the user to carry back to the main session.





#### {description}

Runs 1 instrumental Voice of a Suite whole, agent only, as a subagent or in its own session: its Movements in order on its instrumental branch, 1 commit each, then 1 report to the main session

#### {when_to_use}

When dispatched to run an instrumental Voice (🎻 Violin, 🎺 Trumpet, ~) of a Suite, by a subagent prompt or in a session that names the Plan file and the Voice. Not for the Main Voice (`play-suite`) or drafting Plans (`plan-for-suite`)













### Plan for Suite: Rework

Halt the moment reality stops matching the Plan — a bug, a false assumption, a wrong or unnecessary Movement, unaccounted-for work, a user redirect, anything unanticipated. Never work around it.

1. present the finding: the Plan's assumption, the reality, and the cost to the Movements still ahead
2. rewrite the Plan whole — edit it in place, or author an entirely new file — never a diff, excerpt, or the rework alone. Keep completed Movements untouched and numbered; revise, remove, or add the rest as the finding demands, and append the rework to the history in `## Rework`
3. set every Movement's Status keyword per [Bar 2: Write the Plan](#bar-2-write-the-plan), so the file reads cold as exactly how far the run got and what the finding cost
4. never renumber to make room. A split Movement keeps its number and gains sub-Movements beneath it — `Movement 1` becomes `Movement 1.1` and `Movement 1.2`
5. present the revised Plan and hold for approval, as in [Bar 2: Write the Plan](#bar-2-write-the-plan)
6. once approved, Movement In to the earliest unfinished Movement, and not sooner



#### {description}

Reworks running Plan file when reality stops matching it: halts, rewrites Plan, holds for approval before work resumes

#### {when_to_use}

Mid-run on bug, false assumption, wrong or unnecessary Movement, unaccounted-for work, user redirect, workspace mismatch on resume — even unprompted. Triggers: rework the Plan, replan, Plan no longer fits. Not for drafting Plans (`plan-for-suite`) or running Movements (`play-suite`)




#### {[Claude:Enter/ExitPlanMode] Usage}

Immediate `EnterPlanMode` tool on halt,
and present the revised plan to user thru `ExitPlanMode` tool

If the revised Plan File is finished while already out of plan mode, never assume the user approved it: still seek approval, by `EnterPlanMode` then `ExitPlanMode`

#### {[Claude:AskUserQuestion] Usage}

use `AskUserQuestion` tool to ask user during the rework

#### {[Hermes:clarify] Usage}

use `clarify` tool to ask user during the rework
