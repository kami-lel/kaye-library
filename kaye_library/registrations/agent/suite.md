## Movement, Voice, and Suite

An explicit, multi-round user task runs as 3 nested units: Suite, Voice, and Movement. Never use them for simple, implicit, or single-round work.

**Suite**: the whole workflow for 1 such task

- holds 1+ Voices, the Main Voice always among them
- works on its feature branch, often 1 Suite = 1 feature branch, which every instrumental branch merges back into
- completes once every Voice has merged back and no Movement remains

**Voice**: 1 line of Movements within a Suite, run in order

- the **Main Voice** is the Suite's own line, marked 🧩: every Movement outside the other Voices, user Movements included; the main session runs it, never a subagent or another session
- every other Voice is an **instrumental Voice**: agent only, with no user Movement, approval, or question inside it
- an instrumental Voice runs in 1 of 2 modes, both following `solo-voice`: soloed by a subagent of the main session, or run in its own session
- each instrumental Voice runs in parallel with the Main Voice and the rest, on its own instrumental branch and linked worktree; its instrumental branch is cut from the feature branch and merges back into it once its Movements are done
- an instrument emoji therefore always marks an instrumental Voice

**Movement**: 1 division of a Voice, sized for when the whole cannot be held at once

- design each Movement **reviewable**: one coherent unit user reads, judges, accepts or rejects on its own
- size to that end: worth a halt, small enough to grasp at a glance
- a Movement may build on prior work or stand apart; required is not independence but sharp boundary, so where one Movements Out and next Movements In is never in question
- number each Voice's Movements from `1`, incrementing by 1 — `1`, `2`, `3`.

Name each instrumental Voice after an instrument, and mark it with that instrument's emoji, taken in this order:

(((agent-movement-and-suite-voice-instrument)))

These extend the discourse units with the Suite's own terms. Abbreviations are decode-only: always use the full term in your response:

(((agent-movement-and-suite-discourse-unit)))

in general: Round < Movement < Voice < Suite





### {description}

Defines the **Suite**, its **Voices**, and their **Movement** divisions — a multi-round workflow, its parallel lines, and the reviewable units it's broken into

### {when_to_use}

When a task is broken into Movements, or a Suite or Movement is announced, numbered, or presented — including "break this up", "step by step", "next step"





### {[git] Usage}

Commit each Movement's edits as exactly one git commit: 1 Movement = 1 commit.

Often 1 Suite = 1 feature branch. 1 Voice = 1 instrumental branch, cut from the feature branch and merged back into it.





### {[Claude:TodoWrite] Usage}

One `TodoWrite` entry per Movement in the Suite, every Voice included — 1:1, never merged or split. List the Main Voice's entries first, then each instrumental Voice's in instrument order, each Voice's in Movement order.

- `content`: prefix + Movement imperative
- `activeForm`: prefix + present continuous

Status flow: `pending` at Seed (before Movement 1 opens) → `in_progress` on Open → `completed` on Close, once Working state is verified.

Rules:

- exactly 1 entry `in_progress` in the Main Voice, plus 1 per open instrumental Voice
- Movement added or dropped mid-Suite: edit the array in the call that closes the current Movement

### {[Hermes:todo_list] Usage}

One `todo_list` item per Movement in the Suite, every Voice included — 1:1, never merged or split. List the Main Voice's items first, then each instrumental Voice's in instrument order, each Voice's in Movement order.

- item text: prefix + Movement imperative

Status flow: not started at Seed (before Movement 1 opens) → in progress on Open → done on Close, once Working state is verified.

Rules:

- exactly 1 item in progress in the Main Voice, plus 1 per open instrumental Voice
- Movement added or dropped mid-Suite: edit the list in the call that closes the current Movement

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

### {[task-tracking] Fallback}

One markdown task-list item per Movement in the Suite, every Voice included — 1:1, never merged or split. List the Main Voice's items first, then each instrumental Voice's in instrument order, each Voice's in Movement order.

- item text: prefix + Movement imperative

Status flow: unchecked, undecorated at Seed (before Movement 1 opens) → unchecked, marked current on Open → checked on Close, once Working state is verified.

Rules:

- exactly 1 item marked current in the Main Voice, plus 1 per open instrumental Voice
- Movement added or dropped mid-Suite: edit the list in the same reply that closes the current Movement












### Dispatch Marks

Mark a Movement's close, an instrumental Voice's merge back, or the whole Suite's close in a [Turn Progress Dispatch](#turn-progress-dispatch) with:

(((agent-movement-and-suite-decorative)))

On a 🎏 line closing a Main Voice Movement, and only there, write the Movement prefix as `🧩a\b`, `b` the Main Voice's total Movement count. Every other line, 🧭 included, keeps its usual Movement prefix, with no total.

Only the main session writes these marks. An instrumental Voice, in either mode, writes none of them, neither 🎏 nor a `\b` total; the main session marks it once, with 🎌, at its merge back.

The example below runs across several Turns of one conversation. A line in parentheses names the situation around the decorative, never text to write in an actual response.

```markdown
(you wire the loader to the new columns, closing Movement 1 of 2)
🎏 🧩1\2 Config Loader Reading New Columns
🧭 🧩2 Rebuild the Entry Point
(the Violin Voice reports its fixtures rewritten, and you merge it back)
🎌 Violin Test Fixtures Merged Back
(new Turn, you rebuild the entry point on the loader, the last Movement)
🎏 🧩2\2 Entry Point Rebuilt on the Loader
🏁 Schema Migration Suite Complete
```












### Movement Notation

```
🧩3 Rewrote the Entry Point
🧩5
🎻2 Added Parser Tests
```

Aggressively use one of these 2 forms for every mention of a Movement in your response: `🧩a SUMMARY` or `🧩a`:

- `a` Movement number, counted within its own Voice
- `SUMMARY` short description of the Movement, in [Title Case](#letter-case-title-case)
- in a Voice other than the Main Voice, put that Voice's instrument emoji in place of 🧩, eg `🎻2`

Write no total Movement count unless a rule names one.

----

Except in a markdown heading: spell out `Movement a` instead, eg `## Movement 5`.



#### {[Claude:TodoWrite] Usage}

`TodoWrite` Examples, with prefix `🧩a SUMMARY` or `🎻a SUMMARY`

Seed:

```json
{
  "todos": [
    {
      "content": "🧩1 Rewrite the Entry Point",
      "status": "pending",
      "activeForm": "🧩1 Rewriting the Entry Point"
    },
    {
      "content": "🧩2 Move the Parser to Its Own Module",
      "status": "pending",
      "activeForm": "🧩2 Moving the Parser to Its Own Module"
    },
    {
      "content": "🧩3 Wire the Parser Into the Entry Point",
      "status": "pending",
      "activeForm": "🧩3 Wiring the Parser Into the Entry Point"
    },
    {
      "content": "🎻1 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "🎻1 Updating the Test Fixtures"
    },
    {
      "content": "🎻2 Add Parser Tests",
      "status": "pending",
      "activeForm": "🎻2 Adding Parser Tests"
    }
  ]
}
```

Open Movement 2 while the Violin Voice runs — resend whole array, 2 statuses change:

```json
{
  "todos": [
    {
      "content": "🧩1 Rewrite the Entry Point",
      "status": "completed",
      "activeForm": "🧩1 Rewriting the Entry Point"
    },
    {
      "content": "🧩2 🥁 Move the Parser to Its Own Module",
      "status": "in_progress",
      "activeForm": "🧩2 🥁 Moving the Parser to Its Own Module"
    },
    {
      "content": "🧩3 Wire the Parser Into the Entry Point",
      "status": "pending",
      "activeForm": "🧩3 Wiring the Parser Into the Entry Point"
    },
    {
      "content": "🎻1 Update the Test Fixtures",
      "status": "in_progress",
      "activeForm": "🎻1 Updating the Test Fixtures"
    },
    {
      "content": "🎻2 Add Parser Tests",
      "status": "pending",
      "activeForm": "🎻2 Adding Parser Tests"
    }
  ]
}
```

#### {[Hermes:todo_list] Usage}

`todo_list` Examples, with prefix `🧩a SUMMARY` or `🎻a SUMMARY`

Seed:

- 🧩1 Rewrite the Entry Point
- 🧩2 Move the Parser to Its Own Module
- 🧩3 Wire the Parser Into the Entry Point
- 🎻1 Update the Test Fixtures
- 🎻2 Add Parser Tests

Open Movement 2 while the Violin Voice runs — resend whole list, 2 items' statuses change (Movement 1 done, Movement 2 and Violin Movement 1 in progress):

- 🧩1 Rewrite the Entry Point (done)
- 🧩2 🥁 Move the Parser to Its Own Module (in progress)
- 🧩3 Wire the Parser Into the Entry Point
- 🎻1 Update the Test Fixtures (in progress)
- 🎻2 Add Parser Tests

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

#### {[task-tracking] Fallback}

Markdown task-list Examples, with prefix `🧩a SUMMARY` or `🎻a SUMMARY`

Seed:

```markdown
- [ ] 🧩1 Rewrite the Entry Point
- [ ] 🧩2 Move the Parser to Its Own Module
- [ ] 🧩3 Wire the Parser Into the Entry Point
- [ ] 🎻1 Update the Test Fixtures
- [ ] 🎻2 Add Parser Tests
```

Open Movement 2 while the Violin Voice runs — resend whole list, 3 items' markers change:

```markdown
- [x] 🧩1 Rewrite the Entry Point
- [ ] 🧩2 🥁 Move the Parser to Its Own Module
- [ ] 🧩3 Wire the Parser Into the Entry Point
- [ ] 🎻1 🥁 Update the Test Fixtures
- [ ] 🎻2 Add Parser Tests
```













### Movement with Count

A **Count** is any countable atomic unit that may exist within a Movement — files affected, bugs to fix, tests to implement. What a Count is depends on the usage. One Movement holds one or more Counts. Counts measure progress only: never halted at
individually, and a Movement of many Counts still closes as one Movement.

----

Every mention of a Movement takes the form `a\b🧩c SUMMARY`:

- `a` Counts closed to date — all Counts of prior Movements, plus this Movement's own
- `b` total Counts across all Movements
- `c` Movement number, counted within its own Voice; in a Voice other than the Main Voice, its instrument emoji replaces 🧩, eg `4\12🎻1`
- `SUMMARY` short description of the Movement, in [Title Case](#letter-case-title-case)

*Example — 3 Movements holding 4, 5, 3 Counts, 12 total:*

```
4\12🧩1 Cleared First 4
9\12🧩2 5 More Closed
12\12🧩3 Last 3
```



#### {description}

Defines the **Movement** and its inner **Count** — reviewable division of large work, atomic action measuring progress — with naming, sizing, boundaries, and `a\b🧩c` prefix

#### {when_to_use}

When work is split into Movements or Counts, or either is announced, numbered, tallied, or sized — "break this up", "step by step", "how far along", or progress given as a fraction. Also whenever "phase", "stage", "task", or "part" would name a division of work



#### {[Claude:TodoWrite] Usage}

`TodoWrite` Examples, with prefix `a\b🧩c SUMMARY`

Seed:

```json
{
  "todos": [
    {
      "content": "4\\12🧩1 Rewrite the Entry Point",
      "status": "pending",
      "activeForm": "4\\12🧩1 Rewriting the Entry Point"
    },
    {
      "content": "9\\12🧩2 Move the Parser to Its Own Module",
      "status": "pending",
      "activeForm": "9\\12🧩2 Moving the Parser to Its Own Module"
    },
    {
      "content": "12\\12🧩3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "12\\12🧩3 Updating the Test Fixtures"
    }
  ]
}
```

Open Movement 2 — resend whole array, 1 status changes:

```json
{
  "todos": [
    {
      "content": "4\\12🧩1 Rewrite the Entry Point",
      "status": "completed",
      "activeForm": "4\\12🧩1 Rewriting the Entry Point"
    },
    {
      "content": "9\\12🧩2 🥁 Move the Parser to Its Own Module",
      "status": "in_progress",
      "activeForm": "9\\12🧩2 🥁 Moving the Parser to Its Own Module"
    },
    {
      "content": "12\\12🧩3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "12\\12🧩3 Updating the Test Fixtures"
    }
  ]
}
```

#### {[Hermes:todo_list] Usage}

`todo_list` Examples, with prefix `a\b🧩c SUMMARY`

Seed:

- 4\12🧩1 Rewrite the Entry Point
- 9\12🧩2 Move the Parser to Its Own Module
- 12\12🧩3 Update the Test Fixtures

Open Movement 2 — resend whole list, 1 item's status changes (Movement 1 done, Movement 2 in progress):

- 4\12🧩1 Rewrite the Entry Point (done)
- 9\12🧩2 🥁 Move the Parser to Its Own Module (in progress)
- 12\12🧩3 Update the Test Fixtures

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

#### {[task-tracking] Fallback}

Markdown task-list Examples, with prefix `a\b🧩c SUMMARY`

Seed:

```markdown
- [ ] 4\12🧩1 Rewrite the Entry Point
- [ ] 9\12🧩2 Move the Parser to Its Own Module
- [ ] 12\12🧩3 Update the Test Fixtures
```

Open Movement 2 — resend whole list, 1 item's marker changes:

```markdown
- [x] 4\12🧩1 Rewrite the Entry Point
- [ ] 9\12🧩2 🥁 Move the Parser to Its Own Module
- [ ] 12\12🧩3 Update the Test Fixtures
```
