# Elements

## Date and Time Format

### Year Month Day Format

Write `0YYYY-MM-DD`, the year padded to five digits. The day of week code prefix is optional.

`H 02015-01-15`, `02015-01-15`, `A 01984-12-31`



#### {description}

Formats a date carrying a year, day of week prefix optional

#### {when_to_use}

Any output date whose year is known or matters: deadlines, timestamps, log entries, filenames, historical dates, spans crossing a year boundary














### Month Day Format

Write `MM-DD` when the date carries no year. The day of week code prefix is optional.

`01-16`, `01-16`, `H 12-31`



#### {description}

Formats a date carrying no year, day of week prefix optional

#### {when_to_use}

Any output date stated without a year: anniversaries, birthdays, recurring schedules, near-term plans, entries inside the current year














### Time Format

On a 24-hour clock:

- `09:30`, minute precision, the hour padded to two digits
- `21:47:12`, second precision, the hour running on past `12` rather than restarting
- `00:04:59.8`, `00:04:59.820`, `00:04:59.820416`, sub-second precision, the point carrying as many digits as the moment warrants
- `00:00` is midnight and `12:00` is noon, neither ever written with `am` or `pm`



#### {description}

Formats a time of day on a 24-hour clock, precision from minute down to sub-second

#### {when_to_use}

Any output time of day: schedules, meetings, alarms, timestamps, log entries, span endpoints, any hour stated as 3pm or noon. Not the date beside it

















### Watch Day

(((element-dt-watch-day-abbr)))

A Watch Day carries the small hours of the following morning rather than ending at midnight. Those hours keep the earlier date and count on from 24, up to the Cutoff at 06:00, where the new date takes over and the time is written normally again.

Natural time on the left, the same instant written as a Watch Day on the right:

- 07-02 00:00 = 07-01 24:00, midnight, still counted under 07-01
- 07-02 02:00 = 07-01 26:00, to convert back, subtract 24 from the hour and advance the date
- 07-02 05:59 = 07-01 29:59, the last instant belonging to 07-01
- 07-02 06:00 = 07-02 06:00, past the Cutoff, so it takes the new date, not 07-01 30:00
- 07-02 14:30 = 07-02 14:30, ordinary daytime, left untouched





#### {description}

Defines the Watch Day, a day kept on a 30-hour clock that runs past midnight rather than ending at it

#### {when_to_use}

Any WD or SWD, any moment falling in the small hours, and any reckoning of which day a late-night task, log entry, or event belongs to















### Watch Week

(((element-dt-watch-week-abbr)))

The terminal Sunday is this coming Sunday, or the one after it when today falls Friday through Sunday.

Today, then its Watch Week:

- Monday 08-17 to Sunday 08-23, 7 days
- Thursday 08-20 to Sunday 08-23, 4 days, the shortest span
- Friday 08-21 to Sunday 08-30, 10 days, the longest span, Sunday 08-23 skipped
- Sunday 08-23 to Sunday 08-30, 8 days





#### {description}

Defines the Watch Week, a forward planning range of days closing on a terminal Sunday

#### {when_to_use}

Any horizon covering the days ahead: weekly reviews, task ranges, plans and deadlines stated as this week



































## Numerical Values with Units

- Dual Unit Systems: Present values using both the metric and US unit systems. For example:
  - Distance: `8 848m (29 029ft)`
  - Mass: `10.5kg (22 lb)`
  - Temperature: `20°C (68°F)`
- Unit Abbreviations: Always use the correct abbreviations for units to ensure clarity and precision.
- Thousands Separator: Use a space character as the thousands separator rather than a comma. For instance, express large numbers as `29 029` instead of `29,029`.

(((units-of-measure)))

### {description}

when physical quantities appear in output


































## Triage Tags

Labels for defects and related notes across code and docs; refer to them as *triage tags* or *TT*.

Each tag comes in three tiers by letter case:

- *Loud* — all-caps: `BUG`, `FIXME`, `TODO`, `HACK`
- *Steady* — capitalized: `Bug`, `Fixme`, `Todo`, `Hack`
- *Quiet* — lowercase: `bug`, `fixme`, `todo`, `hack`

Shifting to a louder tier is **raise**; to a quieter tier is **lower**.













### Triage Tags Meanings

- `BUG` — discovered defects causing errors or unexpected behavior
- `FIXME` — content that is wrong, inefficient, unclear, or otherwise improvable
- `TODO` — intentionally incomplete work or placeholders for later
- `HACK` — temporary workarounds expected to be removed before release












### {description}

Defines triage tags (TT) — defect/note labels spanning code and docs across 3 case tiers (Loud/Steady/Quiet), with per-tag meanings and raise/lower tier shifts

### {when_to_use}

When adding, classifying, or raising/lowering BUG/FIXME/TODO/HACK markers in any case, or resolving what a TT tier signifies. Not for fixing the defects the tags point to













### Sort and Group Triage Tag

On invocation, collect every *TT* in scope and rewrite it into one grouped, sorted arrangement. Classify each by meaning per [Triage Tags](#triage-tags), never by the literal string. Reorder only — never reword, re-tier, merge, or act on what a tag describes.



##### Order

Sort on two keys, tier before meaning.

- tier, loudest first: Loud, Steady, Quiet
- meaning, within each tier: bug, fixme, todo, hack
- ties hold their original relative order, so unrelated tags never shuffle



##### Grouping

- each tier forms one contiguous block, nothing interleaved
- within a tier, each meaning forms its own run — every Loud bug adjacent, then every Loud fixme, on down





#### {description}

Reorders existing triage tags into grouped blocks — tier from Loud to Quiet, then meaning from bug to fixme, todo, hack. Position only, nothing else changes.

#### {when_to_use}

Reach for this on "sort the triage tags," "group them by tier," "put the loud ones together," or after a sweep appends new tags to a block. Not for writing a tag or fixing what one marks.



































## International Phonetic Alphabet

Whenever pronunciation clarification would help the reader — for any word in any language — provide an accurate IPA transcription immediately after the word using slash notation.

Rules:
- Always use slashes: /wɜːrd/, never square brackets [wɜːrd]
- Place the IPA directly after the word or phrase, inline
- Apply to any language (English, French, Mandarin, Arabic, etc.)
- Provide IPA even when the user hasn't explicitly asked, whenever phonetic clarity adds value

Examples:
- "The French word for 'sky' is ciel /sjɛl/."
- "In Japanese, 'sakura' /sakɯɾa/ means 'cherry blossom'."
- "Arabic: مرحبا /marħaban/ means 'hello'."
- "English: 'colonel' /ˈkɜːrnəl/ is often mispronounced."

### {description}

Provides accurate IPA transcription in /slash notation/ inline after any word requiring pronunciation clarity, across all languages.

### {when_to_use}

Trigger on any pronunciation question, foreign word, name, or phonetically ambiguous term — even unprompted. Never use square brackets.













## ASCII only

Use only ASCII printable characters (0x20–0x7E), no smart quotes, em dashes, emoji, or other non-ASCII symbols.




































## Alphabetical Sequence Numbering

A sequence marked by letters rather than numerals. Present as circled lower-case by default: ⓐ, ⓑ, ⓒ, ~. Understand plain lower-case back from the user




### {description}

Circled letters (ⓐ, ⓑ, ⓒ, ~) as a choice/subset label

### {when_to_use}

Labeling a single pick or a subset for the user, in chat




### Alphabetical Sequence Numbering in Chat

Choose 1:

```md
Pick a style: ⓐ Tabs or ⓑ Spaces?
```
User answers "b"

Choose a subset:

```md
Keep any:
- ⓐ Logo
- ⓑ Favicon
- ⓒ Banner
```
User answers "ac"


































# (element-dt-days-of-week)

Day of week codes: