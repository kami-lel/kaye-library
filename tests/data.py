"""
tests/data.py

wording the library's own skills must render, by canonical name
"""

FILE_CONTENT = {'coder-bash-script': ['## Bash',
                       'You write **Bash** targeting Debian GNU/Linux, '
                       'using only the standard GNU',
                       '### Coder Bash Script',
                       'open every script file with a **shebang** on the '
                       'first line',
                       '#### Function Header Comment'],
 'coder-bash-shell': ['## Bash',
                      'You write **Bash** targeting Debian GNU/Linux, '
                      'using only the standard GNU',
                      '### Coder Bash Shell',
                      'Return the command alone, with no surrounding '
                      'explanation.',
                      '`sudo` is allowed, and so are destructive commands '
                      'whenever they are what'],
 'coder-c': ['## Coder C',
             'Use **C99** standard',
             '## Brace Style',
             'opening `{` on the **same line**',
             'closing `}` on its **own line**'],
 'coder-c-sharp': ['## Coder C Sharp',
                   '## Brace Style',
                   'opening `{` on the **same line**',
                   'closing `}` on its **own line**',
                   '/// <summary>',
                   'Documentation: Use XML comments'],
 'coder-comment-banner-in-code-comment': ['## Comment Banner',
                                          '**Levels** — six ranks, highest '
                                          '(`CB0`) to lowest (`CB5`)',
                                          '### CB in Code Comment',
                                          'Use CB to mark sections of long '
                                          'source files.',
                                          '`CB0` boxes the file title, '
                                          '`CB1` marks top-level sections'],
 'coder-comment-banner-in-print-out': ['## Comment Banner',
                                       '**Levels** — six ranks, highest '
                                       '(`CB0`) to lowest (`CB5`)',
                                       '### CB in Print Out',
                                       'Use CB to divide logging / demo / '
                                       'test phases',
                                       '`CB0` boxes the run title, `CB1C` '
                                       '(`#`) marks each phase'],
 'coder-cpp': ['## Brace Style',
               'opening `{` on the **same line**',
               'closing `}` on its **own line**',
               '## Coder C',
               'Use **C99** standard',
               '## Coder CPP',
               'Use **C++17** standard'],
 'coder-gdscript': ['## Coder GDScript',
                    'Writing code based on [Coder](#coder)'],
 'coder-html': ['## Coder HTML', 'Version: **HTML5** standard'],
 'coder-javascript-and-typescript': ['## Brace Style',
                                     'opening `{` on the **same line**',
                                     'closing `}` on its **own line**',
                                     '## Coder JavaScript and TypeScript',
                                     'These standards are applicable '
                                     'exclusively',
                                     '**ES11** standard',
                                     '#### Naming Conventions',
                                     '- Use **camelCase** for naming '
                                     'variables',
                                     '### Documentation and Comments',
                                     '- Ensure the code is accompanied by',
                                     'Use **JSDoc**',
                                     '*Example of JSDoc documentation:*',
                                     'globalNS.method1 = function (a, b)'],
 'coder-python': ['## Coder Python',
                  'Adhere to the **PEP8** style guide, ensuring clarity '
                  'and consistency.',
                  '- do **not** use type hints anywhere (no variable '
                  'annotations,',
                  '- prefer `str.format()` for string formatting, dont '
                  'use'],
 'coder-python-docstring-style': ['### Coder Python Docstring Style',
                                  'Write all docstrings in Sphinx style '
                                  'using reStructuredText.',
                                  '#### Which Fields They Carry',
                                  '"""banned single-line docstring"""',
                                  '| public API function | S, D, A, R, E |',
                                  '| class function, public or private | '
                                  'S, A, R |',
                                  '| auxiliary / helper function | S *or* '
                                  'R, never Both |',
                                  'Never pad a docstring with an empty or '
                                  'placeholder field.',
                                  '`:param:` / `:type:` per argument',
                                  '#### Which Callables Carry a Docstring',
                                  'Public Functions and Methods: always '
                                  'carry One',
                                  '`__init__`: **never** carries one',
                                  '#### Module & Script Docstrings',
                                  'first line is the filename',
                                  '#### Field Rules',
                                  '- `Iterable(str)`',
                                  '- `dict{str: int}`',
                                  'Optional Arguments: for a parameter '
                                  'with a default',
                                  'Raises: one `:raises:` entry per '
                                  'distinct scenario',
                                  'Wrapping: when a field line runs long'],
 'coder-python-testing-guidelines': ['### Coder Python Testing Guidelines',
                                     'This section pertains specifically '
                                     'to Python test code',
                                     '`pytest` module',
                                     'test class names should start with '
                                     '`Test`',
                                     'test function names should begin '
                                     'with `test_`',
                                     'strive to create as many separate '
                                     'test functions',
                                     'do **not** require docstrings',
                                     '**Each test file**',
                                     '*Example of tests for the `add` '
                                     'function:*',
                                     'TestAdd',
                                     'class TestAdd:'],
 'coder-u3d': ['## Brace Style',
               'opening `{` on the **same line**',
               'closing `}` on its **own line**',
               '## Coder C Sharp',
               'Documentation: Use XML comments',
               '## Coder Unity Engine',
               'Follows [Coder C Sharp](#coder-c-sharp)',
               '##### Logging',
               'Open every message with the owning subsystem or module '
               'name',
               'Debug.isDebugBuild'],
 'coder-u3d-assets-management': ['### Assets Management',
                                 'Assets/_MyGame/Scripts/MinigameRacing/RacingSceneRoot.cs',
                                 '##### Type Folders'],
 'coder-u3d-mb': ['### MonoBehaviour',
                  'Section order, formatting, and accessors follow the '
                  'example exactly.',
                  'public class PlayerController: MonoBehaviour',
                  'public static PlayerController FindInScene()',
                  'private const string LOAD_TRIGGER_TAG',
                  '- guard **every** `[SerializeField] private` field '
                  'carrying no declaration default',
                  '// Public Members',
                  '// Inspector Fields',
                  '- **one block, at the top** of `Awake()`, under exactly '
                  'one `// Inspector Assignment Guard` line, never '
                  'scattered, never repeated',
                  'Inspector Assignment Guard:',
                  'if (nextSceneName == null) {',
                  '"MinigameRacing:\\tmust assign Inspector Field: '
                  'nextSceneName",'],
 'coder-u3d-so': ['### Scriptable Object'],
 'coder-ue': ['## Coder Unreal Engine',
              'Follows [Coder C](#coder-c) and [Coder CPP](#coder-cpp)',
              '## Brace Style',
              'opening `{` on the **same line**',
              'closing `}` on its **own line**',
              '## Coder C',
              'Use **C99** standard',
              '## Coder CPP',
              'Use **C++17** standard'],
 'commit-sense': ['### primary summary',
                  '### per-file change sigil',
                  '### per-file summary',
                  '### Perform Commit Sense',
                  'Commit the indexed changes: draw the message from the '
                  'conversation'],
 'condense-agents-and-context': ['## Condense AGENTS and CONTEXT',
                                 'You work from the **files alone**: no '
                                 'change set, no conversation to draw on, '
                                 'nothing new to add.',
                                 '### Repository AGENTS Writer',
                                 '## Repository CONTEXT Writer'],
 'condense-changelog': ['## Condense CHANGELOG',
                        'reword every `[Unreleased]` entry into changelog '
                        'style — concise, high-level, free of '
                        'implementation detail',
                        '## Repository CHANGELOG Writer'],
 'create-changelog': ['## Create CHANGELOG',
                      'reconstruct project history from git tags, '
                      'releases, and the commit log',
                      '## Repository CHANGELOG Writer',
                      '### Semantic Version Extended'],
 'create-project-agents': ['### Create Project AGENTS',
                           "ground the file in the project's own material "
                           'and the conversation; write only what they '
                           'support',
                           '### Project AGENTS Writer'],
 'create-project-docs': ['### Create Project Docs',
                         "ground each document in the project's own "
                         'material and the conversation; write only what '
                         'they support',
                         '### Project Doc Writer'],
 'create-readme': ['## Create README',
                   'inspect the repository for structure, then draw '
                   'material from its docs, config, manifests, and source',
                   'take intent and anything the repository has not '
                   'captured from the conversation',
                   'write a section only where project information '
                   'supports it, titled per [README Title](#readme-title)',
                   'create `README.md` at the project root, for a '
                   'repository that has none',
                   '## Repository README Writer'],
 'create-repo-agents': ['### Create Repository AGENTS',
                        'ground the file in the repository itself and the '
                        'conversation; write only what they support',
                        '### Repository AGENTS Writer'],
 'create-repo-docs': ['### Create Repository Docs',
                      "ground each document in the repository's code, "
                      'configurations, and the conversation; write only '
                      'what they support',
                      '### Repository Doc Writer'],
 'element-dt-month-day-format': ['### Month Day Format',
                                 'Write `MM-DD` when the date carries no '
                                 'year.',
                                 '`01-16`, `01-16`, `H 12-31`',
                                 'Day of week codes:'],
 'element-dt-time-format': ['### Time Format',
                            'On a 24-hour clock:',
                            '- `09:30`, minute precision, the hour padded '
                            'to two digits',
                            '- `00:00` is midnight and `12:00` is noon, '
                            'neither ever written with'],
 'element-dt-watch-day': ['### Watch Day',
                          'A Watch Day carries the small hours of the '
                          'following morning rather than ending at '
                          'midnight.',
                          '- 07-02 06:00 = 07-02 06:00, past the Cutoff, '
                          'so it takes the new date, not 07-01 30:00'],
 'element-dt-watch-week': ['### Watch Week',
                           'The terminal Sunday is this coming Sunday, or '
                           'the one after it when today falls Friday '
                           'through Sunday.',
                           '- Monday 08-17 to Sunday 08-23, 7 days'],
 'element-dt-year-month-day-format': ['### Year Month Day Format',
                                      'Write `0YYYY-MM-DD`, the year '
                                      'padded to five digits.',
                                      '`H 02015-01-15`, `02015-01-15`, `A '
                                      '01984-12-31`',
                                      'Day of week codes:'],
 'element-international-phonetic-alphabet': ['## International Phonetic '
                                             'Alphabet',
                                             'Always use slashes: /wɜːrd/',
                                             'Place the IPA directly after '
                                             'the word or phrase, inline'],
 'element-numerical-values-with-units': ['## Numerical Values with Units',
                                         '- Dual Unit Systems:',
                                         '- Distance: `8 848m (29 029ft)`',
                                         '- Unit Abbreviations:',
                                         '- Thousands Separator:',
                                         'Use a space character as the '
                                         'thousands separator'],
 'glossary-programming-language-codes': ['- bash:Bash',
                                         '- c:C language',
                                         '- cpp:C++',
                                         '- csharp:C Sharp',
                                         '- gdscript:GDScript used by '
                                         'Godot Engine',
                                         '- js:JavaScript',
                                         '- p4v:Perforce',
                                         '- py:Python',
                                         '- ts:TypeScript',
                                         '- u3d:Unity Engine code',
                                         '- ue:Unreal Engine code'],
 'glossary-units-of-measure': ['- b:bit',
                               '- B:byte',
                               '- ft:foot',
                               '- hr:hour',
                               '- lb:pound',
                               '- mi:mile',
                               '- min:minute',
                               '- s:second',
                               '- yd:yard',
                               '- nmi:nautical mile'],
 'land-feature': ['## Perform Feature Landing',
                  'tmp content for Perform Feature Landing'],
 'maintain-changelog': ['## Maintain CHANGELOG',
                        'take what to log from the conversation and recent '
                        'repository changes',
                        'file each entry under the right subsection of '
                        '`[Unreleased]`, the default target for new work',
                        'combine with existing entries rather than '
                        'duplicating; leave their wording as it stands',
                        'keep the links block current so every version '
                        'stays referenced',
                        'update the CHANGELOG in place, then return a '
                        'brief summary of the changes',
                        '## Repository CHANGELOG Writer'],
 'maintain-project-agents': ['### Maintain Project AGENTS',
                             'edit in place: fold new material into the '
                             'section it belongs to',
                             '### Project AGENTS Writer'],
 'maintain-project-docs': ['### Maintain Project Docs',
                           'edit in place: update what the change set '
                           'moved, fix references it broke',
                           '### Project Doc Writer'],
 'maintain-readme': ['## Maintain README',
                     'take what changed from the conversation, then diff '
                     'it against the current README to find stale, '
                     'missing, or inaccurate content',
                     '## Repository README Writer'],
 'maintain-repo-agents': ['### Maintain Repository AGENTS',
                          'edit in place: fold moved commands, '
                          'conventions, and constraints into the sections '
                          'already there',
                          '### Repository AGENTS Writer'],
 'maintain-repo-docs': ['### Maintain Repository Docs',
                        'edit in place: update what the change set moved, '
                        'fix references it broke',
                        '### Repository Doc Writer'],
 'maintenance-before-compact': ['## Maintenance Before Compact',
                                'Before context is compacted, capture this '
                                "session's durable changes so nothing is "
                                'lost',
                                '#### Instructions',
                                '- [Maintain '
                                'CHANGELOG](#maintain-changelog) → record '
                                'those changes',
                                '- [Maintain Repository '
                                'AGENTS](#maintain-repository-agents) → '
                                'update for any command, convention, or '
                                'constraint the session moved',
                                '- skip a step the session gives nothing '
                                'relevant to',
                                '#### Output',
                                'Update the affected files in place, '
                                'leaving unrelated files untouched.'],
 'plan-for-suite': ['## Plan for Suite',
                    'Do **not** start editing.',
                    '### Bar 1: Gather',
                    '### Bar 2: Write the Plan',
                    '##### Movement Heading',
                    '### Plan for Suite: Bar 3: Execution'],
 'plan-for-suite-execution': ['### Plan for Suite: Bar 3: Execution',
                              'Starts only after the user approves the '
                              'Plan.',
                              'ask whether to run under '
                              '`cascade-all-movements` or '
                              '`halt-each-movement`.',
                              '##### Movement Parties in '
                              'Execution',
                              '##### Reworking the Plan'],
 'proj-agents-writer': ['## agents writer',
                        '#### AGENTS Title & Preface',
                        '# Example Project AGENTS',
                        'Replace `Example Project` with the real project '
                        'name.',
                        '### Project AGENTS Writer',
                        '##### Suggested Sections',
                        '- Concept: what the project is and why it exists'],
 'proj-doc-writer': ['## doc writer',
                     '### Project Doc Writer',
                     "Draw from the project's own material, and verify "
                     'every claim against it.'],
 'proj-version': ['## Project Semantic Version',
                  'major.minor.patch',
                  'x.y.z',
                  '`x.y.z-alpha`, `x.y.z-alpha.2`',
                  '[0-9a-z-]',
                  '`x.y.z+build.1`',
                  '[0-9A-Za-z-]'],
 'proj-version-extended': ['## Project Semantic Version',
                           'major.minor.patch',
                           'x.y.z',
                           '### Semantic Version Extended',
                           'pre-releases types: `alpha`, `beta`, `rc`',
                           'start at `.2`, e.g. `1.0.0-alpha.2`, '
                           '`1.0.0-alpha.3`',
                           '`1.0.0+Win`, `1.0.0+mac`, `1.0.0+linux`',
                           'Vertical Slice (VS): `0.5.z`~`0.8.z`',
                           'Release Candidate (RC): `1.0.0-rc`'],
 'ready-land-feature': ['## Prepare for Feature Landing',
                        'Before merging the current [feature '
                        'branch](#feature-branch)',
                        '#### Movement 1~3: Sync Unit Test',
                        '#### Movement 4: Learn the Feature Branch',
                        '#### Movement 5: Record the Change Set in the '
                        'CHANGELOG',
                        'Run [Maintain CHANGELOG](#maintain-changelog), '
                        'recording the change set per [Repository '
                        'CHANGELOG Writer](#repository-changelog-writer).',
                        '#### Movement 6: Sync AGENTS and CONTEXT'],
 'ready-release-version': ['## Prepare for Version Release',
                           'Cut a new release: bring all docs current',
                           '#### Movement 1: Decide Release Version and '
                           'Date',
                           '- require both a version number and a release '
                           'date; if either is missing',
                           '#### Movement 2: Maintain the README',
                           '#### Movement 3: Condense AGENTS and CONTEXT',
                           '#### Movement 4: Maintain the Docs Directory',
                           '#### Movement 5: Condense the Changelog',
                           '#### Movement 6: Close Out the Changelog',
                           '#### Movement 7: Bump the Repository Version'],
 'release-version': ['## Perform Version Release',
                     'tmp content for Perform Version Release'],
 'repo-agents-writer': ['## agents writer',
                        '#### AGENTS Title & Preface',
                        '# Example Project AGENTS',
                        'Replace `Example Project` with the real project '
                        'name.',
                        '### Repository AGENTS Writer',
                        'Apply these rules to `AGENTS.md`, formatting it '
                        'per',
                        '##### Suggested Sections',
                        'Keep content command-oriented; descriptive '
                        'architecture',
                        '- Layout & Naming: where each kind of file goes',
                        '##### What to Include',
                        'Instruction budget is finite, and a wrong '
                        'instruction beats no instruction only in the '
                        'wrong direction.',
                        '##### Quality Expectations',
                        '- repository-specific, never generic',
                        '- behavioral and command-oriented — rules, '
                        'commands, constraints, not architecture '
                        'narration'],
 'repo-changelog-writer': ['## Repository CHANGELOG Writer',
                           'these guidelines define what a good '
                           '`CHANGELOG.md` (or CHANGELOG-style file) is',
                           '#### Guiding Principles',
                           '- keep every version and section linkable, '
                           'with a links block at the foot of the file '
                           'holding all of them',
                           '#### CHANGELOG Example',
                           '#### Types of Changes',
                           '- `Changed`: changes in existing functionality',
                           '- `Security`: in case of vulnerabilities',
                           '#### CHANGELOG Example',
                           '[unreleased]: '
                           'https://github.com/example-user/example-project/compare/v2.0.0...dev',
                           '> Drops support for Node 14; upgrade before '
                           'updating'],
 'repo-doc-writer': ['## doc writer',
                     '### Repository Doc Writer',
                     "Draw from the repository's code and configurations"],
 'repo-readme-writer': ['## Repository README Writer',
                        "You write and maintain a repository's "
                        '`README.md`: the landing page for the people who '
                        'use the project',
                        '#### Audience',
                        'Write for a first-time visitor and a returning '
                        'contributor, stating each capability as an '
                        'Outcome the reader gets rather than the mechanics '
                        'producing it',
                        '#### Sections',
                        '- Project Overview: what it does, who it serves, '
                        'why it is worth using',
                        '#### Style',
                        '- favor short Sections a visitor can scan in '
                        'seconds',
                        '#### Quality',
                        '- specific to this Repository, never generic'],
 'repo-structure': ['## Repository Structure',
                    'A repository keeps its readme, agent, context, and '
                    'doc files as set out in [Project Context '
                    'Engineering](#project-context-engineering), with one '
                    'addition: local layers are machine-specific, '
                    'gitignored, and never committed.',
                    'Place the following at the **top level** of the '
                    'repository when applicable, named consistently across '
                    'projects:',
                    '- `CHANGELOG.md`: full version history; each release '
                    'is documented here',
                    '- `CREDITS.md`: acknowledgements, contributors, and '
                    'third-party attributions',
                    '- `DEVLOG.md`: development journal, decisions, and '
                    'progress notes',
                    '- `src/` or package-name: primary source code folder',
                    '- `bin/`: compiled binaries or executable entry-point '
                    'scripts',
                    '- `examples/`: standalone usage examples and demos',
                    '- `scripts/`: utility and maintenance scripts not '
                    'part of the main codebase',
                    '- `tests/`: test suite, kept separate from source '
                    'code',
                    '- `tools/`: project-specific developer tooling, '
                    'distinct from `scripts/`'],
 'resolve-merge-conflict': ['## Resolve Merge Conflict',
                            'You resolve a **halted Git merge**.',
                            '#### Resolve',
                            '#### Output'],
 'review-gaps': ['## Gap Review',
                 'Inspect the repository and surface every inconsistency, '
                 'gap, or unfinished seam',
                 '#### Categories',
                 '#### Using Triage Tags',
                 '#### Findings'],
 'style-briefness-style': ['## Style Guide Briefness Style',
                           '- omit articles (a, an, the) and helper '
                           'verbs, ',
                           '- keep sentences short, direct, drop filler'],
 'style-good-writing': ['## Style Guide Good Writing',
                        '- Correct spelling, grammar, punctuation, '
                        'sentence structure, and',
                        '- Avoid generic filler when details are '
                        'unavailable',
                        '- Avoid dense prose, generic filler, and '
                        'unnecessary complexity'],
 'style-letter-case-commentary-case': ['### Letter Case Commentary Case',
                                       '- begin 1st sentence with a '
                                       'lowercase letter',
                                       '- the last sentence should not end '
                                       'with punctuation'],
 'style-letter-case-title-case': ['### Letter Case Title Case',
                                  '- capitalize major words: nouns, '
                                  'pronouns, verbs, adjectives, adverbs, '
                                  'numerals',
                                  '- keep proper nouns, acronyms, and '
                                  'brand styling as written']}

DESCRIPTION_CONTENT = {'coder-bash-script': 'writes Bash script files, functions, and sourced '
                      'libraries for Debian GNU/Linux under a fixed house '
                      'style.',
 'coder-bash-shell': 'answers Bash command requests for Debian GNU/Linux '
                     'with the bare terminal line',
 'coder-c': 'Writes, edits, and reviews all C code.',
 'coder-c-sharp': 'Writes, edits, and reviews all C# code.',
 'coder-comment-banner-in-code-comment': 'writes comment banners inside '
                                         'source code',
 'coder-comment-banner-in-print-out': 'writes banners into printed program '
                                      'output',
 'coder-cpp': 'Writes, edits, and reviews all C++ code.',
 'coder-gdscript': 'GDScript code for Godot 4',
 'coder-html': 'apply HTML5 standards for structure, semantics, and '
               'markup.',
 'coder-javascript-and-typescript': 'Writes, edits, and reviews all '
                                    'JavaScript and TypeScript code, '
                                    'targeting the ES11 standard with '
                                    'camelCase naming and JSDoc '
                                    'documentation conventions.',
 'coder-python': 'scripts, modules, packages, functions, classes, inline '
                 'snippets',
 'coder-python-docstring-style': 'writes, formats Python docstrings in '
                                 'Sphinx/reStructuredText',
 'coder-python-testing-guidelines': 'writes, reviews Python `pytest` test '
                                    'code per project conventions',
 'coder-u3d': 'Writes, edits & reviews all Unity 6 C# code under house '
              'conventions: class-role suffixes, singleton & event idioms, '
              'member order, subsystem-prefixed logging',
 'coder-ue': 'C++ code for Unreal Engine',
 'commit-sense': 'Commits the indexed diff',
 'condense-agents-and-context': 'Shrinks an existing AGENTS and CONTEXT '
                                'pair',
 'condense-changelog': 'rewords its entries into concise, high-level '
                       'changelog style and adds Admonitions for Breaks '
                       'and Hazards where warranted.',
 'create-project-agents': 'Creates `AGENTS.md` for a generic project that '
                          'has none',
 'create-project-docs': 'Creates topic-focused `docs/` files for a generic '
                        'project',
 'create-readme': 'Use this skill when the user wants to create a new '
                  '`README.md` from scratch — covering project overview, '
                  'setup, usage, configuration, and contributing '
                  'guidelines.',
 'create-repo-agents': 'Creates `AGENTS.md` for a repository that has none',
 'create-repo-docs': 'Creates topic-focused `docs/` files for a repository',
 'element-dt-month-day-format': 'Formats a date carrying no year, day of '
                                'week prefix optional',
 'element-dt-time-format': 'Formats a time of day on a 24-hour clock, '
                           'precision from minute down to sub-second',
 'element-dt-watch-day': 'Defines the Watch Day, a day kept on a 30-hour '
                         'clock that runs past midnight rather than ending '
                         'at it',
 'element-dt-watch-week': 'Defines the Watch Week, a forward planning '
                          'range of days closing on a terminal Sunday',
 'element-dt-year-month-day-format': 'Formats a date carrying a year, day '
                                     'of week prefix optional',
 'element-international-phonetic-alphabet': 'IPA transcription',
 'element-numerical-values-with-units': 'when physical quantities appear '
                                        'in output',
 'element-triage-tags': 'defect/note labels spanning code and docs across '
                        '3 case tiers (Loud/Steady/Quiet), with per-tag '
                        'meanings and raise/lower tier shifts',
 'glossary-programming-language-codes': 'Glossary '
                                        'programming-language-codes',
 'land-feature': 'tmp description Perform Feature Landing',
 'maintain-changelog': 'Use this skill when the user wants to add, fix, or '
                       'reorganize entries in an existing CHANGELOG — '
                       'logging new features, bug fixes, or breaking '
                       'changes without overwriting existing content.',
 'maintain-project-agents': 'Updates an existing project `AGENTS.md` '
                            'against what changed',
 'maintain-project-docs': 'Updates existing project `docs/` files against '
                          'what changed',
 'maintain-repo-agents': 'Updates an existing repository `AGENTS.md` '
                         'against what changed',
 'maintain-repo-docs': 'Updates existing repository `docs/` files against '
                       'what changed',
 'maintenance-before-compact': "Logs a session's durable changes before "
                               'context compaction',
 'plan-for-suite': 'Splits oversized task into ordered, numbered '
                   'Movements, then runs them under review',
 'proj-agents-writer': 'Writes & maintains `AGENTS.md` for generic '
                       'AI-ready projects: rules & constraints telling '
                       'agents how to work on project',
 'proj-doc-writer': 'Writes & maintains `docs/` topic files for generic '
                    'projects',
 'proj-version': 'defines semantic versioning scheme',
 'proj-version-extended': 'Extends semantic versioning with conventions '
                          'for `alpha`/`beta`/`rc` pre-release numbering, '
                          'OS/date build-metadata tags, and '
                          'version-to-dev-stage mapping',
 'ready-land-feature': 'Records a feature branch',
 'ready-release-version': 'Cuts a project release',
 'release-version': 'tmp description Perform Version Release',
 'repo-agents-writer': '**prescriptive** rules telling AI coding agents '
                       'how to work in repo, e.g. commands, code style, PR '
                       'rules, safety constraints',
 'repo-changelog-writer': 'dated version entries newest-first, grouped '
                          'change types, a persistent `[Unreleased]` '
                          'section, and linkable version references.',
 'repo-doc-writer': 'Writes & maintains `docs/` topic files for '
                    'repositories',
 'repo-readme-writer': 'Writes and maintains human-friendly README files — '
                       'scannable, visually clear landing pages covering a',
 'repo-structure': 'naming conventions and placement for top-level '
                   'documentation files and source, build, docs, test, and '
                   'tooling folders.',
 'resolve-merge-conflict': 'Resolves conflicts in a halted Git merge',
 'review-gaps': 'Audits whole repository for gaps, drift, unfinished seams',
 'sort-and-group-triage-tag': 'Reorders existing triage tags into grouped '
                              'blocks — tier from Loud to Quiet, then '
                              'meaning from bug to fixme, todo, hack.',
 'style-briefness-style': 'dropped articles and helper verbs, strong nouns '
                          'and verbs, active voice, numerals and '
                          'abbreviations, punctuation-compressed phrasing, '
                          'no terminal periods.',
 'style-good-writing': 'fixing spelling, grammar, punctuation, and clarity '
                       'while preserving the original meaning, voice, and '
                       'wording.',
 'style-letter-case-commentary-case': 'define Commentary Case',
 'style-letter-case-title-case': 'define Title Case'}

WHEN_TO_USE_CONTENT = {'coder-bash-script': 'fires on durable shell artifacts: `.sh`, `.bash`, '
                      '`bashrc`, function definitions',
 'coder-bash-shell': 'fires when the user wants something run now, not a '
                     'file kept',
 'coder-c': 'Use for any C code work, requests for C.',
 'coder-c-sharp': 'Use for any C# code work, requests for C#, mentions of '
                  '.NET.',
 'coder-comment-banner-in-code-comment': 'Any long source file needing '
                                         'structural markers: section '
                                         'dividers, boxed file-title '
                                         'blocks, or banner comments.',
 'coder-comment-banner-in-print-out': 'any script or program emitting '
                                      'multi-phase terminal output: run '
                                      'headers, stage separators, '
                                      'log-section dividers',
 'coder-cpp': 'Use for any C++ code work, requests for C++.',
 'coder-javascript-and-typescript': 'Use for any JavaScript or TypeScript '
                                    'work, inline JS/TS code blocks, '
                                    'requests for JavaScript, TypeScript, '
                                    'or Node.',
 'coder-python': 'files, code blocks, '
                 'writing/fixing/refactoring/optimizing/reviewing Python, '
                 'or bare code requests with no language stated in a '
                 'Python context. Not for docstring-only or test-only '
                 'requests, route those to the dedicated skills',
 'coder-python-docstring-style': 'trigger whenever a Python function, '
                                 'method, class, or module is written or '
                                 'edited',
 'coder-python-testing-guidelines': 'trigger on `test_*.py`/`*_test.py` '
                                    'files, pytest, fixtures, mocks, '
                                    'parametrize, assertions, or requests '
                                    'like write/add/fix a unit test or '
                                    'test case. Not for non-test Python '
                                    'code',
 'coder-u3d': 'Any C# in a Unity project, even when user never says '
              '"Unity": gameplay systems, managers, controllers, editor '
              'tools, UI, input, save/load, scene logic. Triggers: Unity, '
              '`UnityEngine`, `Debug.Log`, `.cs` under `Assets/`, '
              'singleton, manager, event. Load together w/ `coder-u3d-mb` '
              'for `MonoBehaviour` scripts, `coder-u3d-so` for '
              '`ScriptableObject` classes; asset placement & naming belong '
              'to `coder-u3d-assets-management`',
 'commit-sense': 'write a commit message',
 'element-dt-month-day-format': 'Any output date stated without a year: '
                                'anniversaries, birthdays, recurring '
                                'schedules, near-term plans, entries '
                                'inside the current year',
 'element-dt-time-format': 'Any output time of day: schedules, meetings, '
                           'alarms, timestamps, log entries, span '
                           'endpoints, any hour stated as 3pm or noon',
 'element-dt-watch-day': 'Any WD or SWD, any moment falling in the small '
                         'hours, and any reckoning of which day a '
                         'late-night task, log entry, or event belongs to',
 'element-dt-watch-week': 'Any horizon covering the days ahead: weekly '
                          'reviews, task ranges, plans and deadlines '
                          'stated as this week',
 'element-dt-year-month-day-format': 'Any output date whose year is known '
                                     'or matters: deadlines, timestamps, '
                                     'log entries, filenames, historical '
                                     'dates, spans crossing a year '
                                     'boundary',
 'proj-agents-writer': 'Creating, updating, reviewing `AGENTS.md` for '
                       'generic project',
 'proj-version-extended': 'Choosing or validating a version string for a '
                          'pre-release, tagged build, or dev-stage '
                          'milestone.',
 'repo-agents-writer': 'Not for **descriptive** architecture/domain '
                       'knowledge, which belongs in `CONTEXT.md`',
 'repo-changelog-writer': 'Use when creating, updating, or adding entries '
                          'to a CHANGELOG, or recording changes for a '
                          'release.',
 'repo-readme-writer': 'Use when creating, updating, or reviewing a README '
                       'or similar project landing page.',
 'repo-structure': 'Use when scaffolding a new repo, organizing an '
                   'existing one, or deciding where a file or folder '
                   'belongs.',
 'style-briefness-style': 'Use when the user asks for headlinese, '
                          'telegraphic, or ultra-condensed text',
 'style-good-writing': 'Use to proofread, copyedit, or correct writing '
                       'without rewriting. Not for heavy rewrites, '
                       'summarizing, or tone changes.',
 'style-letter-case-commentary-case': 'for list items, table cell content, '
                                      'code comment',
 'style-letter-case-title-case': 'for document titles and section headings'}

CLAUDE_TOOL_CONTENT = {'plan-for-suite': ['opens with `EnterPlanMode` tool, so all discovery '
                    'runs before any edit is possible',
                    'delivers the finished Plan through `ExitPlanMode` '
                    'tool, which is where the user approves it'],
 'ready-release-version': ['if version number or release date is '
                           '**missing**, use `AskUserQuestion` to ask user '
                           'before proceeding'],
 'resolve-merge-conflict': ['track resolution with the `TodoWrite` tool — '
                            'one todo per unmerged path',
                            '`git add` each path as soon as it is '
                            'resolved'],
 'write-llm-prompt': ['## Write Large Language Model Prompt',
                      'You draft new **textual prompts** and edit existing '
                      'ones, usually a system message',
                      '- Draft: build a complete prompt from any description, '
                      'however short',
                      'the prompt itself is the deliverable, never a '
                      'paraphrase or summary'],
 'write-skill-description': ['## Write Skill Description',
                             '`description` decides whether the skill is '
                             'selected at all, so treat it as the '
                             'highest-stakes text.',
                             'Label the heading literally `{description}`, '
                             "one level below the skill's own."]}
