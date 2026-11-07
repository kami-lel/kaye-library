# Perforce

## Working with Perforce

The user thinks in Git. When you explain, instruct, or act in Perforce, follow every Perforce term with its closest Git equivalent in `()`, so the user never translates alone. Keep the Perforce term as the main word: the user must still recognize it in P4V.

- parenthesize every occurrence, never only the first: the user may read any single line alone
- cover nouns, commands, flags, and P4V menu actions alike

> Shelve (stash) your changelist (index) first.

#### Examples

- depot (repo)
- workspace/client (worktree)
- changelist (index)
- submit (commit+push)
- sync (pull+checkout)
- stream (branch)
- integrate (merge)
- resolve (resolve merge conflict)
- revert (restore)
- shelve (stash)
- label (tag)
- head revision (branch tip)

For any term not listed, use its closest Git equivalent, consistently.

### {avoid}

Dropping the Perforce term for the Git one, or parenthesizing only the first mention.





### {description}

Pairs every Perforce term with its closest Git equivalent in parentheses, so a user who thinks in Git never translates alone.

### {when_to_use}

Trigger on any explanation or action in Perforce, P4, or P4V: changelists, shelves, streams, depots, submit, sync, integrate, resolve. Not for Git repositories (use `working-with-git`).
