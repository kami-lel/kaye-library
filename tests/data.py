"""
tests/data.py

wording the library's own skills must render, by canonical name
"""

FILE_CONTENT = {'element-dt-month-day-format': ['### Month Day Format',
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

DESCRIPTION_CONTENT = {'element-dt-month-day-format': 'Formats a date carrying no year, day of '
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

WHEN_TO_USE_CONTENT = {'element-dt-month-day-format': 'Any output date stated without a year: '
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
 'style-briefness-style': 'Use when the user asks for headlinese, '
                          'telegraphic, or ultra-condensed text',
 'style-good-writing': 'Use to proofread, copyedit, or correct writing '
                       'without rewriting. Not for heavy rewrites, '
                       'summarizing, or tone changes.',
 'style-letter-case-commentary-case': 'for list items, table cell content, '
                                      'code comment',
 'style-letter-case-title-case': 'for document titles and section headings'}

CLAUDE_TOOL_CONTENT = {}
