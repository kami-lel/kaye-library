"""
tests/data.py

wording the library's own skills must render, by canonical name
"""

FILE_CONTENT = {'glossary-units-of-measure': ['- b:bit',
                               '- B:byte',
                               '- ft:foot',
                               '- hr:hour',
                               '- lb:pound',
                               '- mi:mile',
                               '- min:minute',
                               '- s:second',
                               '- yd:yard',
                               '- nmi:nautical mile'],
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

DESCRIPTION_CONTENT = {'style-briefness-style': 'dropped articles and helper verbs, strong nouns '
                          'and verbs, active voice, numerals and '
                          'abbreviations, punctuation-compressed phrasing, '
                          'no terminal periods.',
 'style-good-writing': 'fixing spelling, grammar, punctuation, and clarity '
                       'while preserving the original meaning, voice, and '
                       'wording.',
 'style-letter-case-commentary-case': 'define Commentary Case',
 'style-letter-case-title-case': 'define Title Case'}

WHEN_TO_USE_CONTENT = {'style-briefness-style': 'Use when the user asks for headlinese, '
                          'telegraphic, or ultra-condensed text',
 'style-good-writing': 'Use to proofread, copyedit, or correct writing '
                       'without rewriting. Not for heavy rewrites, '
                       'summarizing, or tone changes.',
 'style-letter-case-commentary-case': 'for list items, table cell content, '
                                      'code comment',
 'style-letter-case-title-case': 'for document titles and section headings'}

CLAUDE_TOOL_CONTENT = {}
