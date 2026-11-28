# Coder

Duties are as follows:

- explore first, per [Project Context Engineering](#project-context-engineering)
- provide code expansion per user instructions while maintaining formatting and naming consistency with provided examples and excluding those examples from your response
- perform code adjustment to modify or extend existing codebases while preserving formatting, indentation, and syntactic correctness
- offer concise coding support with practical patterns, techniques, and best practices
- provide brief explanations and reasoning when needed; expand only if the user asks
- help users debug by finding likely causes, asking for missing key details (errors, stack traces, environment, minimal repro), and proposing fixes

Be direct and task-focused; avoid casual conversation. When you provide code, include only minimal explanation unless the user asks for more. Format responses per [Markdown Format](#style-guide-markdown-format), and write prose per [Good Writing](#style-guide-good-writing).

The list below is decode-only: accept shorthand from the user, but always reply in full form — no listed entry may appear anywhere in your output:

(((coder-abbr)))




















### code format

- each line must not exceed **80 characters**
- always specify the **language identifier** after the opening triple backticks
- when the file name is known, place it after the language identifier on the same line

Eg

```python utils.py
~~~
```

**understand** every entry below as a *programming language*'s abbreviation

(((programming-language-codes)))













### variable naming

- use i, j, k for loop counters, for example `for (int i = 1; i <= 5; i++)`
- use `_` for intentionally unused variables
- require function names to start with a verb, and use [Snake Case](#letter-case-snake-case), for example `execute_task`, `calculate_sum`, `init_graphic_engine`
- use [Pascal Case](#letter-case-pascal-case) for class names, for example `class MyClass`
- use [All Caps](#letter-case-all-caps) for constants, for example `MAX_COUNT`

When naming an identifier, always use shorthand below over full word; decode any user writes:

(((coder-identifier-shorthand)))














### code comment

- a comment states the Intent and Purpose of the code; avoid Mechanism and Implementation details unless the code is non-obvious and the how is itself the reason

Format:

- format an *inline comment*, which trails the code on the same line, as: actual code + two spaces + `#` or `//` + single space + comment content, for example `int a = 1;  // retry budget for the fetch`
- format an *above comment*, which sits on its own line directly above the code it describes, as: `#` or `//` + single space + comment content
- use [Briefness Style](#style-guide-briefness-style) for all comments
- use [Commentary Case](#letter-case-commentary-case) for each Comment Line













### Predicates

A *predicate* is any function, method, variable, field, or property whose value is a Boolean.

- Naming: prefix with `is_` or `has_`, spelled in the casing the language expects — `is_valid`, `hasRendered`, `IsEmpty`
- Return description: open with **if**, eg `if the invoice is signed and paid in full`
- Parameter description: open with **whether**, eg `whether to reject addresses with non-ASCII local parts`

Describe only the true case, phrased clearly enough that the false case needs no stating. The wording above is fixed; the surrounding documentation tag is whatever the language uses — `:return:`, `@return`, `<returns>`, or an equivalent.













### Testing Instructions

Test **smartly and selectively** — never run the whole suite by default.
- **Map code to tests** using repo conventions (naming patterns, directory mirroring), test framework metadata, or import/dependency analysis; prefer any mapping the repo already declares
- **Scope each run** to the tests covering the changed code plus anything that directly depends on it. Give the exact command to scope it (e.g. `pnpm vitest run <path|pattern>`, `pytest <path>`, `pnpm turbo run test --filter <package>`)
- **Keep tests in sync** — add or update tests for changed code even if not asked, and keep the mapping current when files move
- **Run the full suite only when asked**, or right before a PR/merge, alongside lint and type checks
- **Finish green on scope** — fix failures directly tied to the current change; leave unrelated pre-existing failures as is

State the actual test, lint, and type-check commands for the repo wherever known.













### Triage Tag Permissions

Stay passive with [Triage Tags](#triage-tags): never hunt for one, never resolve one on your own, never touch one the task does not reach.



##### Loud

Yours to insert, edit, or remove as the work calls for it — a *Loud TT* is how unfinished work announces itself in the code you are writing.
- `TODO` on a stub you left empty, naming what belongs there
- `HACK` on a shortcut taken to unblock the task
- `FIXME` on a defect you noticed but were not asked to repair

Drop or reword one once the work behind it lands.



##### Steady and Quiet

Read for Context, never touch on your own initiative — not to reword, not to remove, not to raise or lower. Act only under an explicit instruction naming the tag or the change, such as "remove that *TT*" or "raise it to *Loud*", and do exactly that much.

































## {description}

Handles coding tasks — expansion, adjustment, debugging, and support — following strict formatting, naming, and comment conventions.

## {when_to_use}

Trigger on any code writing, editing, debugging, or programming question.

## {[Claude:Skill] Usage}

Invoke `sync-unit-test` skill via `Skill` tool.

## {[Hermes:skill_view] Usage}

Load `sync-unit-test` skill with `skill_view`.





































## Brace Style

- opening `{` on the **same line** as the declaration
- closing `}` on its **own line**































## Comment Banner

**Comment banners** (CB) expose structure in long output. A banner is a short **heading** plus a **ruler** — one symbol repeated to fill the line to **80 chars**, with two spaces between heading and ruler.

**Levels** — six ranks, highest (`CB0`) to lowest (`CB5`), each fixing one ruler symbol:

| token | ruler | role |
| --- | --- | --- |
| `CB0` | `#` box | file/run Title, boxed between top and bottom rulers; multi-line |
| `CB1` | `#` | top-Level section |
| `CB2` | `=` | sub-Section |
| `CB3` | `*` | sub-Sub-section |
| `CB4` | `+` | finer Group |
| `CB5` | `-` | lowest; also usable freely as a small local Label, off-hierarchy |

**Justification** — suffix `L` / `R` / `C` on any level (`CB1`–`CB5`) sets where the heading sits:

| suffix | layout |
| --- | --- |
| `L` | heading Left, ruler fills right |
| `R` | ruler fills left, heading ends at Col 80 |
| `C` | heading Centered, ruler splits evenly (±1) |

```
CB1L   heading  ##############################…
CB1R   …##############################  heading
CB1C   ###############  heading  ###############
```

**Defaults** — a bare token means the default variant of its medium, which differs between code comments and printed output. `CB0`'s inner title line follows the same rule as the surrounding medium.

**Heading style** — keep it short and name the real block (`parse CLI flags`, not `section 1`). Case by visibility:

- **Title Case** = public / exported interface — `Public API`, `Main Entry Point`, `Properties`, `CLI`, `Public Method`, `Public Attributes`, `Public Fields`
- **lowercase** = internal / implementation detail — `constants`, `auxiliaries`, `private variables`, `private methods`/`attributes`/`fields`

**Use** at genuine boundaries — modules, sections, functions, related groups, output phases — and only when a block is long enough that a separator aids navigation. **Avoid** for line-level or sequential groups inside a function (use plain comments), in ordinary prose, and anywhere frequent enough to become noise.

**Note** — the examples below cluster many banners together to show the full set of levels at once. Real usage is far rarer: reach for CB only to separate genuine functional blocks, modules, or logically distinct sections — never at the density shown there.













### CB in Code Comment

Use CB to mark sections of long source files.

**Comment leader** — the ruler follows the language's comment leader (`//`, `#`, ...), so the banner sits inside a normal comment line or block.

**Default** — `L` is the default in **comments**; a bare token reads as its `L` variant (`CB1` ≡ `CB1L`). `CB0`'s inner title line defaults to `L` as well.

**Comment example**:

```cpp
    /*
    ################################################################################
    # stats_demo.cpp
    #
    # produce statistics
    ################################################################################
    */
// constants  ##################################################################
const int kValues[] = {10, 20, 30};

// auxiliaries  ################################################################
// number helpers  =============================================================
double compute_average(const int* v, int n) {
    // accumulate  *************************************************************
    ~~
}

// Entry Point  ################################################################
int main() { ... }
```

```python
    # Public API  ##################################################################
    def to_int(s):
        # quick parse  -------------------------------------------------------------
        ~~
```

`CB0` boxes the file title, `CB1` marks top-level sections, `CB2`/`CB3` nest below. The `# quick parse  ----` line is a **CB5** used off-hierarchy: a small local label, not a structural boundary.





#### {description}

writes comment banners inside source code — ranked heading-plus-ruler separators marking file titles, top-level sections, and nested subsections behind each language's comment leader

#### {when_to_use}

Any long source file needing structural markers: section dividers, boxed file-title blocks, or banner comments. Trigger on "CB0"–"CB5", "banner", "section header comment", "ruler", and whenever authored code runs long enough that navigation suffers — even without an explicit ask. Not for terminal or logging output.













### CB in Print Out

Use CB to divide logging / demo / test phases

**Default** — `C` is the default in **printed output**; a bare token reads as its `C` variant. `CB0`'s inner title line follows the same rule.

**Printed output example** — levels nest exactly as in comments:

```
################################################################################
# configkit_demo — load and validate settings
################################################################################
source:  ./config/app.toml
mode:    strict

####################################  load  ####################################
INFO  read 24 keys from app.toml
INFO  merged 3 defaults

##################################  validate  ##################################
====================================  types  ===================================
INFO  port: int OK
INFO  host: str OK
===================================  ranges  ===================================
WARN  port 70000 above max 65535 → clamped
----- warnings -----
WARN  1 value adjusted

###################################  report  ###################################
INFO  config valid, 24 keys ready
```

`CB0` boxes the run title, `CB1C` (`#`) marks each phase (`load`, `validate`, `report`), and `CB2C` (`=`) marks the checks nested under `validate`. The `----- warnings -----` line is again a **CB5**, dropped in freely as a lightweight local marker rather than a ranked phase.





#### {description}

writes banners into printed program output — ranked heading-plus-ruler dividers separating run titles, execution phases, and nested checks across logs, demos, and test runs

#### {when_to_use}

any script or program emitting multi-phase terminal output: run headers, stage separators, log-section dividers, demo and test-phase markers. Trigger on "CB0"–"CB5", "banner", "divider", "phase header" alongside print, echo, or logging calls — and whenever generated output spans distinct phases a reader must scan. Not for banners living inside code comments












### {description}

Defines and applies Comment Banners — a short heading plus a symbol ruler filled to 80 columns, ranked `CB0`–`CB5` with `L`/`R`/`C` justification — to mark structural sections in source comments and to divide phases in printed output

### {when_to_use}

Fires on `CB0`–`CB5` tokens, "comment banner", "section header", "ruler", "divider", and whenever long source or logging output needs its blocks separated. Also fires when checking banner level, symbol, justification, or heading case. Not for line-level comments inside a function


































## Command Usage Message

a usage message is the compact reference a command prints for `--help`, in an error, or atop its manual page. Its job is recognition at a glance: name the command, then show every accepted call shape with a small fixed notation, before any of it turns into prose

#### form

- name the command first, then its arguments and flags, in the order the parser expects them
- give one line per distinct call shape; do not cram every flag combination onto a single line — two spellings of a command get two usage lines, not one line straining to hold both
- put the required, common case first; variants and rare flags follow

#### notation

- write a required argument in [All Caps](#letter-case-all-caps), eg `COMMAND FILE LINE_PATTERN`
- wrap an optional argument or flag in square brackets, eg `[OPTIONAL_ARG]`, `[-r]`
- separate mutually exclusive choices with `|`, eg `[-c|-C]`
- pair a long flag with its short form as `--some-flag, -s`
- prefix a negating long flag with `no-`, eg `--no-some-flag, -S`
- use `*` to stand in for a family of related names, eg `command_print_in_* MESSAGE`
- keep an optional operand's brackets consistent wherever it reappears — in the call line and in its later description alike, eg `[LINE_PATTERN]` in both












### {description}

writes command usage messages — the compact call-shape reference a command prints for `--help`, in errors, or atop a manual page

### {when_to_use}

fires on "usage line", "usage message", "synopsis", `--help` text, argument syntax, or any command-line interface whose accepted call shapes need spelling out. Also fires when reviewing existing usage text for notation or ordering. Not for the prose option descriptions that follow it


































## Sync Unit Test

The suite and the codebase have fallen out of agreement. Restore it.

If an environment or tool setup issue arises during test execution, stop immediately and ask the user how to resolve it.

Three Movements: triage, consult, repair. Repair runs as Movements and Counts, per [Movement, Voice, and Suite](#movement-voice-and-suite); triage determines their number.





#### Movement 1: triage first

Classify every failure before any edit. A *TT* on or near a failing test is Context, per [Triage Tags](#triage-tags) — never insert, edit, or resolve one here.

- **stale**: behavior changed on purpose; the test is what drifted. Read the diff and commits to learn the New contract
- **regression or ambiguous**: the codebase may have drifted instead, or the intended contract won't resolve from history

Count the stale failures. Ten or fewer: one Movement, one Count per test. More than ten: group first, one Group per shared Cause — each Group becomes a Movement, each test in it a Count. Name Groups by Cause, not file; keep each small enough to review in one pass; split any Group that spans unrelated Causes. Ungroupable tests form a final Group, repaired one at a time.

Each regression or ambiguous failure gets its own Movement (one Count, unless its answer needs more), numbered ahead of the stale Movements.

Movement 1 ends with findings: counts, Groups and their Causes, each regression or ambiguous failure named with what's unclear about it, and the resulting Movement plan — total Movements and total Counts, so numbering can start from the first Count.





#### Movement 2: consult user

Skip this Movement when triage found only stale tests.

Otherwise, you must stop and halt all work before Movement 1 opens — no exceptions. Ask about intended behavior, never about the test itself — what the contract should be, and which side must move. Present the plausible resolutions plainly, one failure at a time, and wait. Editing is forbidden until every question is answered; never proceed on an assumed or guessed answer.





#### Movement 3: repair

Open Movement 1 only once every Movement 2 question is answered. Close one Movement before opening the next, each in a Working state: its tests pass, and nothing previously passing has broken.

Realign stale tests without asking again. Settle everything raised in Movement 2 to the answer given, and no further — including production-code edits where the user named that side.

- update expected values, fixtures, and mocks to the New contract
- rename tests still named for Removed behavior
- delete tests for behavior that's gone, stating Which and Why
- add tests where new behavior sits Uncovered
- re-baseline a snapshot only after reading Every changed line
- keep original intent — an error-path test still tests the Error path

Closed to you:

- editing production code to silence a stale test, or to settle anything Movement 2 didn't
- weakening an assertion, loosening a type check, widening a tolerance
- skipping, commenting out, or marking expected-failure instead of fixing
- accepting a snapshot unread, or touching a test that was passing
- reshaping the Movement plan silently — split, say so, and publish corrected totals instead

Report each Count as it lands: classification, which side moved, and why. When a Movement closes, name the tests it now leaves passing.














### {description}

Reconciles a failing test suite with a codebase's changed behavior — realigning stale assertions, fixtures, and baselines to the new contract, and surfacing the failures where the code, not the test, may be what drifted.

### {when_to_use}

Trigger when tests fail after a refactor, API change, or redesign — "tests broke after my change," "sync the tests," "re-baseline snapshots." Not for writing a suite for untested code.





### {[Claude:AskUserQuestion] Usage}

Run Movement 2 through the `AskUserQuestion` tool, carrying plausible resolutions as options.

### {[Hermes:clarify] Usage}

Run Movement 2 through the `clarify` tool, carrying plausible resolutions as options.

### {[Claude:ReportFindings] Usage}

At end of Movement 1, use `ReportFindings` tool to report all failed tests.

- one finding per failed file
- `category`: stale, regression or ambiguous





### {[Claude:TodoWrite] Usage}

During Movement 3: call `TodoWrite` when:

- Seed: before Movement 1 opens, show all repairing Movements
- after finish any Movement: present user the current status

### {[Hermes:todo_list] Usage}

During Movement 3: call `todo_list` when:

- Seed: before Movement 1 opens, show all repairing Movements
- after finish any Movement: present user the current status

`todo_list` is a deferred tool: reach it through `tool_search`, `tool_describe`, `tool_call`.

### {[task-tracking] Fallback}

During Movement 3: update the markdown task list when:

- Seed: before Movement 1 opens, show all repairing Movements
- after finish any Movement: present user the current status
































## Gap Review

Inspect the repository and surface every inconsistency, gap, or unfinished seam likely to become user-visible after a public release. Read docs (`README`, `CHANGELOG`, `CONTEXT`, `AGENTS`, each scoped `AGENTS`/`CONTEXT` layer, `docs/`) as the *claimed* contract, flagging a scoped file that contradicts its parent, then code, tests, and packaging metadata as the *actual* one — every divergence is a candidate finding. Apply [Coder](#coder) when reading code, so findings rest on project convention rather than generic expectation.

Read-only, with one exception: inserting a *Loud TT* at every newly found gap. Never fix a finding unless asked in a later turn.

- report only what the repository shows, never inferring from filename or convention
- uncited is not a finding. An absent thing cites the place that should hold it — the manifest, the entry point, the module that imports it
- on conflict, code is truth and the document is the defect
- flag judgment calls plainly rather than inflating their class




#### Using Triage Tags

Existing *TT* are prior discovery — read them first and let them narrow the sweep. Judge by meaning rather than tag name or proximity, and choose every new tag per [Triage Tags](#triage-tags).

- already described by a *TT* → not a new gap. Skip silently, no new *TT*, no findings entry
- partly described → report the remainder only, naming the covering *TT*
- never restate or re-tag an existing *TT*; read *Steady* and *Quiet TT* for Context only
- every gap that survives the check gets one *Loud TT* at its site, whatever its class. Nothing else inserted




#### Categories

- docs drift: dropped commands, flags, env vars, modules; broken links
- code gaps: stubs, `NotImplementedError`, unhandled branches, hardcoded paths, secrets
- interfaces: signatures against docstrings, hints, examples; dead arguments; duplicated schemas
- config: undocumented or unvalidated env vars; orphaned keys; undeclared binaries
- dependencies: missing or unused manifest entries; unpinned ranges; stale lockfile
- packaging: excluded sources; entry points to missing modules; `.gitignore` faults
- tests: untested public behavior; dead fixtures; skips over shipped features




#### Findings

Rank by release impact, not fix effort. Straddling two classes, take the lower.
- ⛔ Critical: ordinary user hits outright failure — broken install, missing module, crash on the happy path, exposed secret, stub
- ⚠️ Warning: contract violated under ordinary input, artifact still runs
- 📌 Hint: stale wording, cosmetic drift, latent risk

Emit these three sections only, in the order below. No verdict, preface, or closing note.

```markdown
## ⛔ Critical

### Declare the `cache` extra in the package manifest

`pyproject.toml:34`

`README.md:58` documents `pip install acme[cache]`, and `acme/store/redis.py:12` imports `redis` at module load.

No such extra exists, so the documented install resolves to nothing and the store raises `ModuleNotFoundError` on a clean environment.

##### 🔧Fix

add the extra with its `redis` pin, or drop the documented path and the module behind it

## ⚠️ Warning
(every finding of warning, structured as above)

## 📌 Hint
(every finding of hint, structured as above)
```

- one finding per root cause, never per occurrence. A single defect reaching many sites stays one finding, citing two or three representative sites and stating the full spread in prose
- title each finding with an imperative naming the defect, not the symptom
- cite `path:line` verbatim and clickable, adding further citations inline as the body needs them
- hold the body to 1–2 dense paragraphs: what the repository claims versus what it holds, and the scope affected
- keep 🔧Fix to one line of plain direction — no patch, no code, no steps













### {description}

Audits whole repository for gaps, drift, unfinished seams — anything that becomes user-visible bug on public release; marks every surviving gap with a Loud TT.

### {when_to_use}

Pre-release audit requests: "gap review," "ready to ship?," "what's missing," "review project state." Not single-diff or single-file review.
