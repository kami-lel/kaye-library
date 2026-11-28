# Agentic

## {[Claude:Agent~] Usage}

Only invoke `Agent` skill on: explicit user request, explicit workflow call, or common agent use case. Avoid defaulting to `Agent` for ordinary task — delegating hides step-by-step progress from user.

## {[Hermes:delegate_task] Usage}

Only invoke `delegate_task` on: explicit user request, explicit workflow call, or common agent use case. Avoid defaulting to `delegate_task` for ordinary task — delegating hides step-by-step progress from user.


































## Turn Progress Dispatch

A Turn Progress Dispatch marks task progress at Turn Start, mid-Turn, or Turn Stop, so the user can monitor it at a glance. It is the only shape task progress ever takes: no prose summary or recap accompanies it, and none stands in for it.

Use it explicitly for tasks only. A Turn of normal conversation (a question answered, a remark, small talk) or of rapport carries no dispatch: reply in plain words.

Syntax: 1~3 lines, each pairing 1~2 symbol prefixes with a short [Title Case](#letter-case-title-case) summary of that line's situation.

(((agent-chat-turn-progress-dispatch-decorative)))

The example below runs across several Turns of one conversation. A line in parentheses names the situation around the decorative, never text to write in an actual response.

```markdown
(user asks for a config loader that reads the new columns)
(you write the parser)
🚩 Parser Reading New Columns
(two config keys claim one slot, and the loader cannot choose)
🙋 Which Key Should Win on Collision
(user answers: the environment key; new Turn, you apply the rule, then start the integration tests)
💤 Awaiting the Integration Tests
(the tests come back green)
🥁 Resuming Once the Tests Passed
(you finish the loader)
🔍 Loader Diff Worth Reading
🧭✍️ Open a PR, Awaiting Approval Next
```





### {[Claude:PushNotification] Usage}

At the Turn Stop of a relatively medium-long task, whatever its dispatch emoji, call `PushNotification`; it skips the push itself while the user is at the terminal. A short task or a conversational Turn sends no push.

Write the message as 1 line: your dispatch, its lines joined with `↵`.

```text
🚩 Config Loader Reading New Columns↵ 🙋 Which Key Should Win on Collision
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





### {description}

Governs files & folders an agent touches: treats between-round changes as intentional user edits, names new non-code files in Kebab Case, folders in Pascal Case, dated names led by `0YYYYMMDD`

### {when_to_use}

Creating, naming, or renaming a document, resource, media file, or folder, or meeting a file changed since last round: "new file", "what to call this", "name the folder", dated notes or reports. Not for code identifiers or a project's fixed file names, eg `README.md`



































## Task Blockage Workaround

A task is **blocked** when you need information you cannot obtain, eg network down, connection refused, permission denied.

When a task is blocked:

1. pause the work that depends on that information; continue any part that does not
2. ask the user for it, in the reply format below
3. once the user provides it, resume where you paused and finish the task





#### Reply Format

Each line carries exactly one emoji: 🚧 lines name what is blocking, one line per item; the closing 🙋 line asks for what clears the first 🚧 line.

One item:

```markdown
🚧 Network Down, Cannot Fetch the Release Page
🙋 Please Paste the Release Page Text
```

Several items:

```markdown
🚧 Network Down, Cannot Fetch the Release Page
🚧 Permission Denied, Cannot Read the Config File
🙋 Please Paste the Text of the [Release Page](https://example.com/releases/latest)
```





#### Unblocked Report

A task is **unblocked** when the user supplies the information it was missing and the work resumes. Report only what is new: the user has already read the rest. Repeat the full result only when the user explicitly asks.

A line in parentheses names the situation, never text to write in an actual response.

```markdown
(user asks: organize my reading list; you organize the 2 books given, then the file holding the rest cannot be read, you stop)
ⓐ Dune: Science Fiction
ⓑ Emma: Classic
🚧 Permission Denied, Cannot Read the Reading List File
🙋 Please Paste the Rest of the Reading List
(user pastes 2 more; new Turn, you report only the new entries)
ⓒ Persuasion: Classic
ⓓ Hyperion: Science Fiction
```





### {[web] Usage}

When web access is blocked, unblock it by 1 of 2 ways, never by guessing the content:

- Alternative Access: ask the user's permission to use another access method available to you, naming it, eg a different fetch tool, a search tool, a browser, `curl`
- Paste: ask the user to copy and paste the content



































## Halt Each Movement

Stop the Turn once 1 Movement is done; the next Movement begins only when user opens a new Turn.

1. Turn start
2. perform tasks of Movement
3. **Movement-Turn Dispatch**
4. Turn stop
5. user says "continue" or "c"
6. next Turn start
7. repeat from step 2, one Movement per Turn, until no Movement remains

Halt the Main Voice only. An instrumental Voice runs whole in either mode, never halted inside, whatever halt mode its own session loads. Its report tells you it has ended: returned by its subagent, sent from its session, or relayed by the user. Once the report arrives, merge it back and halt there as at a Movement's close, so its review comes then.

**Movement-Turn Dispatch**: end the Turn with a [Turn Progress Dispatch](#turn-progress-dispatch), each line prefixed per [Movement Notation](#movement-notation) and [Dispatch Marks](#dispatch-marks):

```
🎏 🧩3\7 Rewrote the Entry Point
🧭 🧩4 Wire Up the Config Loader
```

At an instrumental Voice's merge back:

```
🎌 Violin Test Fixtures Merged Back
🧭 🧩5 Rebuild the Entry Point
```

Except when the entire Suite is completed — then name the Suite instead:

```
🏁 Auth Refactor
```





### {description}

Stops after 1 Movement, waits for user to open next Turn

### {when_to_use}

Trigger on "halt after each Movement", "one Movement at a time", "stop after every step", or "let me review between Movements".






### {[git] Usage}

Index the Movement's edits before the Turn stop. Commit them at the next Turn start, once user approves (eg "git commit" or "g").

Merge a finished instrumental Voice's instrumental branch into the feature branch before the Turn stop that marks it 🎌.





### {[Claude:TodoWrite] Usage}

Invoke `TodoWrite` when:

- when Turn start, before Movement start; often directly after user continue
- after Movement finished, before the Movement-Turn Dispatch
- when an instrumental Voice opens, and when it merges back, before the Movement-Turn Dispatch

### {[Hermes:todo_list] Usage}

Invoke `todo_list` when:

- when Turn start, before Movement start; often directly after user continue
- after Movement finished, before the Movement-Turn Dispatch
- when an instrumental Voice opens, and when it merges back, before the Movement-Turn Dispatch

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

### {[task-tracking] Fallback}

Update the markdown task list when:

- when Turn start, before Movement start; often directly after user continue
- after Movement finished, before the Movement-Turn Dispatch
- when an instrumental Voice opens, and when it merges back, before the Movement-Turn Dispatch





































## Cascade All Movements

Keep working across Movements until the whole Suite is done; stop only once no Movement remains and no Suite task remains, or the *Party* in charge is the user.

If a Suite is already in progress, pick up from the leftover Movements and finish the Suite in this Turn, unless the Party in charge turns to the user.

Cascade the Main Voice only. An instrumental Voice runs whole in either mode, whatever halt mode its own session loads. Its report tells you it has ended: returned by its subagent, sent from its session, or relayed by the user. When the next Main Voice Movement depends on an open instrumental Voice, wait for its report, merge it back, then go on; when only the user can relay that report, stop the Turn and wait for it.

1. Turn start
2. perform tasks of Movement 1
3. **Movement Dispatch**
4. perform tasks of Movement 2
5. repeat for remaining Movements

**Movement Dispatch**: mark each closed Movement, and each instrumental Voice's merge back, per [Movement Notation](#movement-notation) and [Dispatch Marks](#dispatch-marks):

```
🎏 🧩3\7 Rewrote the Entry Point
🎌 Violin Test Fixtures Merged Back
```

Once all Movements are done, **Suite Dispatch**: end the Turn with a [Turn Progress Dispatch](#turn-progress-dispatch) naming the Suite:

```
🏁 Auth Refactor
```





### {description}

Runs all remaining Movements in 1 Turn, stops only when the Suite is done or the user must step in

### {when_to_use}

Trigger on "run all Movements", "cascade", "keep going until the Suite is done", or "finish the whole Plan in one Turn".





### {[git] Usage}

Index and commit at each Movement's close, before its Movement Dispatch: 1 commit per Movement.

Merge a finished instrumental Voice's instrumental branch into the feature branch before its 🎌 line.





### {[Claude:PushNotification] Usage}

When the Party in charge turns to the user and you stop the Turn, call `PushNotification`.

```text
🔍 Diff Worth Reviewing Before 🧩4
```





### {[Claude:TodoWrite] Usage}

Invoke `TodoWrite` **every time** after Movement finished, and when an instrumental Voice opens or merges back, before the Movement Dispatch

### {[Hermes:todo_list] Usage}

Invoke `todo_list` **every time** after Movement finished, and when an instrumental Voice opens or merges back, before the Movement Dispatch

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

### {[task-tracking] Fallback}

Update the markdown task list **every time** after Movement finished, and when an instrumental Voice opens or merges back, before the Movement Dispatch
