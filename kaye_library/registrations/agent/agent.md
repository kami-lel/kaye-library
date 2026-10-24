# Agentic

## {[ClaudeCode:Agent~] Usage}

Only invoke `Agent` skill on: explicit user request, explicit workflow call, or common agent use case. Avoid defaulting to `Agent` for ordinary task — delegating hides step-by-step progress from user.




## Turn Progress Dispatch

A Turn Progress Dispatch marks conversation/task progress at Turn Start, mid-Turn, or Turn Stop, so the user can monitor it at a glance. It is the only shape progress ever takes: no prose summary or recap accompanies it, and none stands in for it.

Syntax: 1~3 lines, each pairing 1~2 symbol prefixes with a short [Title Case](#letter-case-title-case) summary of that line's situation.

(((agent-chat-turn-progress-dispatch-decorative)))

Each example below runs across several Turns of one conversation. A line in parentheses names the situation around the decorative, never text to write in an actual response.

```markdown
(user asks for the schema migration)
(you backfill the new columns)
🚩 Migration Script Complete
(you wire the loader to the new columns)
🚩 Config Loader Reading New Columns
(you rebuild the entry point on the loader)
🎏 Schema Migration Wired End to End
🧭✍️ Open a PR, Awaiting Approval Next
(user approves; new Turn, you open the pull request)
```

```markdown
(two config keys claim one slot, and the loader cannot choose)
🙋 Which Key Should Win on Collision
(user answers: the environment key; new Turn, you apply the rule and extend the fixtures)
🎏 Config Movement Done
🔍 Fixture Diff Worth Reading Before the Next Movement
```

```markdown
(you start pushing the branch)
(user interrupts: run the linter first)
(the linter comes back clean)
🧭 Resume the Interrupted Push Next
(user: continue)
🥁 Resuming the Interrupted Push
(you push the branch, start the integration suite, and dispatch a subagent for the release notes)
💤 Awaiting the Integration Suite and the Notes Subagent
(both report back, the suite red on the migration test)
🥁 Resuming Once Both Reported
(you remove the migration script behind the failures)
🏁 Schema Migration Suite Complete
```





## Files & Folders

Files are assumed to be consistent between rounds. If you detect any changes, treat them as intentional user edits and continue working from the current state of the file.

----

When no specific naming format is required — for documents, resources, media, and other non-code files:

- respect a directory's existing naming convention for new entries within it
- otherwise, for a new file or folder:

  - Files: use [Kebab Case](#letter-case-kebab-case)
  - Folders: use [Pascal Case](#letter-case-pascal-case)

- if a file name must carry a date, the date leads it: `0YYYYMMDD` per [Date and Time Format](#date-and-time-format), then a hyphen, then the subject slug, eg `020260826-weekly-standup.md`. This sorts a directory chronologically on name alone



































## Movement and Suite

A **Suite** is a workflow for explicit, multi-round user tasks — not simple, implicit, or single-round work — made up of multiple **Movements**, each one a division of that Suite sized for when the whole cannot be held at once.

- design each Movement **reviewable**: one coherent unit user reads, judges, accepts or rejects on its own
- size to that end: worth a halt, small enough to grasp at a glance
- a Movement may build on prior work or stand apart; required is not independence but sharp boundary, so where one Movements Out and next Movements In is never in question
- number Movements from `1`, incrementing by 1 — `1`, `2`, `3`.





### {description}

Defines the **Suite** and its **Movement** divisions — a multi-round workflow and the reviewable units it's broken into

### {when_to_use}

When a task is broken into Movements, or a Suite or Movement is announced, numbered, or presented — including "break this up", "step by step", "next step"





### {[git] Usage}

A single Movement often corresponds to one git commit.





### {[ClaudeCode:TodoWrite] Usage}

One `TodoWrite` entry per Movement in the Suite — 1:1, never merged or split. Entry index gives Movement number `a`; array length gives total `b`.

- `content`: prefix + Movement imperative
- `activeForm`: prefix + present continuous

Status flow: `pending` at Seed (before Movement 1 opens) → `in_progress` on Open → `completed` on Close, once Working state is verified.

Rules:

- exactly 1 entry `in_progress` at a time
- Movement added or dropped mid-Suite: edit the array in the call that closes the current Movement, and rewrite every prefix to the new `b`

### {[task-tracking] Fallback}

One markdown task-list item per Movement in the Suite — 1:1, never merged or split. Item index gives Movement number `a`; list length gives total `b`.

- item text: prefix + Movement imperative

Status flow: unchecked, undecorated at Seed (before Movement 1 opens) → unchecked, marked current on Open → checked on Close, once Working state is verified.

Rules:

- exactly 1 item marked current at a time
- Movement added or dropped mid-Suite: edit the list in the same reply that closes the current Movement, and rewrite every prefix to the new `b`












### Movement Notation

```
🧩3\7 Rewrote the Entry Point
🧩5
```

Aggressively use one of these 2 forms for every mention of a Movement in your response: `🧩a\b SUMMARY` or `🧩a`:

- `a` current Movement number
- `b` total Movement count
- `SUMMARY` short description of the Movement, in [Title Case](#letter-case-title-case)

----

Except in a markdown heading: spell out `Movement a` instead, eg `## Movement 5`.



#### {[ClaudeCode:TodoWrite] Usage}

`TodoWrite` Examples, with prefix `🧩a\b SUMMARY`

Seed:

```json
{
  "todos": [
    {
      "content": "🧩1\\3 Rewrite the Entry Point",
      "status": "pending",
      "activeForm": "🧩1\\3 Rewriting the Entry Point"
    },
    {
      "content": "🧩2\\3 Move the Parser to Its Own Module",
      "status": "pending",
      "activeForm": "🧩2\\3 Moving the Parser to Its Own Module"
    },
    {
      "content": "🧩3\\3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "🧩3\\3 Updating the Test Fixtures"
    }
  ]
}
```

Open Movement 2 — resend whole array, 1 status changes:

```json
{
  "todos": [
    {
      "content": "🧩1\\3 Rewrite the Entry Point",
      "status": "completed",
      "activeForm": "🧩1\\3 Rewriting the Entry Point"
    },
    {
      "content": "🧩2\\3 🥁 Move the Parser to Its Own Module",
      "status": "in_progress",
      "activeForm": "🧩2\\3 🥁 Moving the Parser to Its Own Module"
    },
    {
      "content": "🧩3\\3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "🧩3\\3 Updating the Test Fixtures"
    }
  ]
}
```

#### {[task-tracking] Fallback}

Markdown task-list Examples, with prefix `🧩a\b SUMMARY`

Seed:

```markdown
- [ ] 🧩1\3 Rewrite the Entry Point
- [ ] 🧩2\3 Move the Parser to Its Own Module
- [ ] 🧩3\3 Update the Test Fixtures
```

Open Movement 2 — resend whole list, 1 item's marker changes:

```markdown
- [x] 🧩1\3 Rewrite the Entry Point
- [ ] 🧩2\3 🥁 Move the Parser to Its Own Module
- [ ] 🧩3\3 Update the Test Fixtures
```













### Movement with Count

A **Count** is any countable atomic unit that may exist within a Movement — files affected, bugs to fix, tests to implement. What a Count is depends on the usage. One Movement holds one or more Counts. Counts measure progress only: never halted at
individually, and a Movement of many Counts still closes as one Movement.

----

Every mention of a Movement takes the form `a\b🧩c\d SUMMARY`:

- `a` Counts closed to date — all Counts of prior Movements, plus this Movement's own
- `b` total Counts across all Movements
- `c` current Movement number
- `d` total Movement count
- `SUMMARY` short description of the Movement, in [Title Case](#letter-case-title-case)

*Example — 3 Movements holding 4, 5, 3 Counts, 12 total:*

```
4\12🧩1\3 Cleared First 4
9\12🧩2\3 5 More Closed
12\12🧩3\3 Last 3
```



#### {description}

Defines the **Movement** and its inner **Count** — reviewable division of large work, atomic action measuring progress — with naming, sizing, boundaries, and `a\b🧩c\d` prefix

#### {when_to_use}

When work is split into Movements or Counts, or either is announced, numbered, tallied, or sized — "break this up", "step by step", "how far along", or progress given as a fraction. Also whenever "phase", "stage", "task", or "part" would name a division of work



#### {[ClaudeCode:TodoWrite] Usage}

`TodoWrite` Examples, with prefix `a\b🧩c\d SUMMARY`

Seed:

```json
{
  "todos": [
    {
      "content": "4\\12🧩1\\3 Rewrite the Entry Point",
      "status": "pending",
      "activeForm": "4\\12🧩1\\3 Rewriting the Entry Point"
    },
    {
      "content": "9\\12🧩2\\3 Move the Parser to Its Own Module",
      "status": "pending",
      "activeForm": "9\\12🧩2\\3 Moving the Parser to Its Own Module"
    },
    {
      "content": "12\\12🧩3\\3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "12\\12🧩3\\3 Updating the Test Fixtures"
    }
  ]
}
```

Open Movement 2 — resend whole array, 1 status changes:

```json
{
  "todos": [
    {
      "content": "4\\12🧩1\\3 Rewrite the Entry Point",
      "status": "completed",
      "activeForm": "4\\12🧩1\\3 Rewriting the Entry Point"
    },
    {
      "content": "9\\12🧩2\\3 🥁 Move the Parser to Its Own Module",
      "status": "in_progress",
      "activeForm": "9\\12🧩2\\3 🥁 Moving the Parser to Its Own Module"
    },
    {
      "content": "12\\12🧩3\\3 Update the Test Fixtures",
      "status": "pending",
      "activeForm": "12\\12🧩3\\3 Updating the Test Fixtures"
    }
  ]
}
```

#### {[task-tracking] Fallback}

Markdown task-list Examples, with prefix `a\b🧩c\d SUMMARY`

Seed:

```markdown
- [ ] 4\12🧩1\3 Rewrite the Entry Point
- [ ] 9\12🧩2\3 Move the Parser to Its Own Module
- [ ] 12\12🧩3\3 Update the Test Fixtures
```

Open Movement 2 — resend whole list, 1 item's marker changes:

```markdown
- [x] 4\12🧩1\3 Rewrite the Entry Point
- [ ] 9\12🧩2\3 🥁 Move the Parser to Its Own Module
- [ ] 12\12🧩3\3 Update the Test Fixtures
```


































## Unreachable Task Workaround

A task is **unreachable** when you need information you cannot obtain, eg network down, connection refused, permission denied.

When a task is unreachable:

1. pause the work that depends on that information; continue any part that does not
2. ask the user for it, in the reply format below
3. once the user provides it, resume where you paused and finish the task





#### Reply Format

Reply with one line: 🙋🚧, then what is unreachable and what you need from the user.

```markdown
🙋🚧 Network Down, Please Paste the Page Text
```



































## Halt Each Movement

Stop the Turn once 1 Movement is done; the next Movement begins only when user opens a new Turn.

1. Turn start
2. perform tasks of Movement
3. **Movement-Turn Dispatch**
4. Turn stop
5. user says "continue" or "c"
6. next Turn start
7. repeat from step 2, one Movement per Turn, until no Movement remains

**Movement-Turn Dispatch**: end the Turn with a [Turn Progress Dispatch](#turn-progress-dispatch), each line prefixed per [Movement Notation](#movement-notation):

```
🎏 🧩3\7 Rewrote the Entry Point
🧭 🧩4\7 Wire Up the Config Loader
```

Except when the entire Suite is completed — then name the Suite instead:

```
🏁 Auth Refactor
```





### {description}

Stops after 1 Movement, waits for user to open next Turn






### {[git] Usage}

Index the Movement's edits before the Turn stop. Commit them at the next Turn start, once user approves (eg "git commit then continue" or "cc").





### {[ClaudeCode:TodoWrite] Usage}

Invoke `TodoWrite` when:

- when Turn start, before Movement start; often directly after user continue
- after Movement finished, before the Movement-Turn Dispatch

### {[task-tracking] Fallback}

Update the markdown task list when:

- when Turn start, before Movement start; often directly after user continue
- after Movement finished, before the Movement-Turn Dispatch





































## Cascade All Movements

Keep working across Movements until the whole Suite is done; stop only once no Movement remains and no Suite task remains.

If a Suite is already in progress, pick up from the leftover Movements and finish the Suite in this Turn.

1. Turn start
2. perform tasks of Movement 1
3. **Movement Dispatch**
4. perform tasks of Movement 2
5. repeat for remaining Movements

**Movement Dispatch**: mark each closed Movement with the [Movement Notation](#movement-notation) prefix:

```
🎏 🧩3\7 Rewrote the Entry Point
```

Once all Movements are done, **Suite Dispatch**: end the Turn with a [Turn Progress Dispatch](#turn-progress-dispatch) naming the Suite:

```
🏁 Auth Refactor
```





### {description}

Runs all remaining Movements in 1 Turn, stops only when the Suite is done





### {[git] Usage}

Index and commit at each Movement's close, before its Movement Dispatch: 1 commit per Movement.





### {[ClaudeCode:TodoWrite] Usage}

Invoke `TodoWrite` **every time** after Movement finished, before the Movement Dispatch

### {[task-tracking] Fallback}

Update the markdown task list **every time** after Movement finished, before the Movement Dispatch
