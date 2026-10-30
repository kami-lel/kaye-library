# Perforce

## Working with Perforce

When you explain, instruct, or act in Perforce (P4, P4V), the user thinks in Git. Follow every Perforce-specific term with its closest Git equivalent in `[]`, so the user never translates alone. Keep the Perforce term as the main word, since the user must still recognize it in P4V.

- Bracket every occurrence of a term, never only the first
- Bracket commands, flags, and P4V menu actions as well as nouns

> Shelve [stash] your changelist [index] first.

#### Reference Pairs

- depot: [repo]
- workspace (client): [worktree]
- changelist: [index]
- submit: [commit+push]
- sync: [pull+checkout]
- stream: [branch]
- integrate: [merge]
- resolve: [resolve merge conflict]
- revert: [restore]
- shelve: [stash]
- label: [tag]
- head revision: [branch tip]
