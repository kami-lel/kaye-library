## Bash

You write **Bash** targeting Debian GNU/Linux, using only the standard GNU
and Debian toolset.

- use `printf` for output, adding `%b` when escape sequences must expand

Expand variables in these forms:

- `"${VAR}"`: the default form, brace every expansion and quote it, never
  a bare `$VAR`
- `"${VAR:-default}"`: supply a fallback for a value the script cannot run
  without
- `"${VAR-}"`: permit an intentionally empty setting, so that "unset" and
  "deliberately blank" mean the same thing













### Coder Bash Shell

A **command request** asks for a terminal one-liner or a short pipeline.

Return the command alone, with no surrounding explanation.

`sudo` is allowed, and so are destructive commands whenever they are what
the request actually calls for.





#### {description}

answers Bash command requests for Debian GNU/Linux with the bare terminal line

#### {when_to_use}

fires when the user wants something run now, not a file kept: "give me a command", "one-liner", ad hoc `grep`, `sed`, `awk`, `find`, `apt`, `systemctl`. Hands off to Coder Bash Script once the deliverable is a `.sh` file, function, or sourced library

#### {[ClaudeCode:Skill] Usage}

Invoke `coder` skill via `Skill` tool.














### Coder Bash Script

A **script request** asks for a script file, a function, or a sourced library. Everything below governs it.

Writing code based on [Coder](#coder)

- open every script file with a **shebang** on the first line, eg `#!/bin/bash`
- prefer **strict mode**, ie `set -euo pipefail`, unless the script has a specific reason to avoid it
- indent with **four spaces**
- keep every line within **80 characters**

  - continue a long line with a trailing `\`
  - break a `[[ ... ]]` test after its `&&` or `||`

- declare every local variable with `local`; add `-i` for integers and `-r` for values assigned exactly once
- keep the declaration on its own line, separate from any command substitution, so the exit status is not masked: `local message` first, then `message=$(cat -)` on the next line
- align `case` patterns at the same indentation as `case` itself, and end a one-line branch with `;;` on that same line
- close every non-predicate function with an explicit `return 0`, or with `return "$?"` when it ends by delegating to another function





#### Function Header Comment

Every function is preceded by a header comment block sitting directly above the declaration, with **no blank line** between the two. Six forms exist; pick the leanest that still documents the function fully.

###### Anatomy

| section | remark |
| --- | --- |
| name line | fully qualified name with `()`, and nothing else |
| summary | one-line brief of what the function does |
| description | multi-line detail beyond the summary |
| `PREREQUISITE:` | a bullet list, one condition per `# - item` line |
| `USAGE:` | one call signature per supported spelling; notation follows [Command Usage Message](#command-usage-message) |
| `ARGUMENT:` | positional operands, name then description |
| `OPTION:` | flag letters, one per line |
| `OUTPUT:` | what reaches standard output and standard error |
| `RETURN:` | exit statuses, one per line |
| `EXAMPLE:` | one call per line; repeat the whole label for a second example of a different shape — a bare call and a conditional call are two blocks, not two lines |
| declaration | `name() { ... }` line, directly below the header comment with no blank line between; precede it with the appropriate Comment Banner |

- **section necessity**: only the name line and summary are
  required; every other section, including every label, is optional,
  but an optional section must appear when the function actually
  demands it — eg omit `OPTION:` when the function takes no flags,
  but include it the moment one is added
- **label casing**: labels are all caps, singular, and end with a
  colon; their content is indented three spaces past the leader
- **label alignment**: in a two-column label, pad the name column so
  every description in that block starts at the same column — the
  longest name plus two spaces, never less than column 13;
  continuation lines align to the description column
- **label order**: emit only the labels that have something to say,
  always in the order given in the table above

###### full header comment example:

```bash
# array_binary_search()
#
# locate VALUE inside a sorted array via binary search
#
# halve the search range every iteration until VALUE is found or the
# range is empty; the array named by ARRAY_NAME must already be
# sorted ascending, or the result is undefined
#
# PREREQUISITE:
#   - array_utility_init() must have already run, to populate the
#     ARRAY_UTILITY_CACHE associative array this function reads from
#   - caller holds the lock on file descriptor
#     "${ARRAY_UTILITY_LOCK_FD}", to keep the cache read consistent
#     under parallel jobs
#
# USAGE:
#   array_binary_search [-n] ARRAY_NAME VALUE [START_INDEX]
#
# ARGUMENT:
#   ARRAY_NAME     name of the variable holding the sorted array
#   VALUE          target value to locate
#   [START_INDEX]  index to begin the search from, instead of 0
#
# OPTION:
#   -n  compare numerically instead of lexicographically
#
# OUTPUT:
#   print the matching index to stdout; print nothing on a miss
#
# RETURN:
#   0  found, VALUE exists in the array
#   1  not found
#
# EXAMPLE:
#   fruit=('apple' 'grape' 'lemon' 'plum')
#   array_binary_search fruit 'lemon'
#
# EXAMPLE:
#   score=(12 47 68 90 103)
#   if array_binary_search -n score 68; then
#       printf 'found\n'
#   fi
array_binary_search() {  # -----------------------------------------------------
    ~~
}
```





#### {description}

writes Bash script files, functions, and sourced libraries for Debian GNU/Linux under a fixed house style.

#### {when_to_use}

fires on durable shell artifacts: `.sh`, `.bash`, `bashrc`, function definitions, scripts to extend, refactor, or document. Cues: "write a script", "add a function", header comment, exit status. Not for throwaway terminal lines — those go to Coder Bash Shell

#### {[ClaudeCode:Skill] Usage}

Invoke `coder` skill via `Skill` tool.
