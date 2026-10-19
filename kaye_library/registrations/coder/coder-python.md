## Coder Python

Adhere to the **PEP8** style guide, ensuring clarity and consistency.

- do **not** use type hints anywhere (no variable annotations, no function parameter or return type annotations).
- prefer `str.format()` for string formatting, dont use f-strings (`f""`).
- for every `try`/`except` block, bind the exception with `as e` (eg `except ValueError as e:`); if that block re-raises, the `raise` must include `from e`.
- writing code based on [Coder](#coder)

Common CBs:

- `constructor`, place before `__init__()`
- `magic methods`, eg for `__repr__()`
- `operators`, eg for `__or__()`













### {description}

writes, edits, reviews Python code: scripts, modules, packages, functions, classes, inline snippets

### {when_to_use}

trigger for any Python task — `.py` files, code blocks, writing/fixing/refactoring/optimizing/reviewing Python, or bare code requests with no language stated in a Python context. Not for docstring-only or test-only requests, route those to the dedicated skills

### {globs}

```glob
**/*.py
```

### {[ClaudeCode:Skill] Usage}

Invoke `coder` skill via `Skill` tool.













### Coder Python Docstring Style

Write all docstrings in Sphinx style using reStructuredText. Use no other style.

Used in combination with [Coder](#coder) and [Coder Python](#coder-python)




#### Which Callables Carry a Docstring

- Public Functions and Methods: always carry One
- Private Functions and Methods (`_` prefixed): carry one unless the name alone conveys the Purpose
- Classes: always carry one directly under the `class` statement
- `__init__`: **never** carries one — the class docstring documents it, so the class's A fields describe the `__init__` Arguments
- Dunder Methods (`__eq__`, `__repr__`, `__len__`): carry none unless the behaviour is Non-Obvious
- Modules: always carry one, following the separate rule Below




#### Which Fields They Carry

| callable | required fields |
| --- | --- |
| public API function | S, D, A, R, E |
| class function, public or private | S, A, R |
| auxiliary / helper function | S *or* R, never Both |

A required field is written only where it applies — a callable taking no arguments carries no A, and one that neither returns nor raises carries no R. Never pad a docstring with an empty or placeholder field.

For a helper, pick the single field that documents it fully: S when the work is the point, R when the returned value is.

Aggressively replace each docstring field name with its listed letter:

(((coder-documentation-field-shorthand)))




#### Layout

A docstring is **never** collapsed onto one physical line — the `"""` delimiters always sit on their own lines with content between them. Banned:

```python
"""banned single-line docstring"""
```

- Order: S, D, then the fields — A (`:param:` / `:type:` per argument), R (`:raises:` before `:return:` / `:rtype:`), then E (`:example:`)
- Spacing: one empty line between S and D; two empty lines before the First Field. A docstring carrying S alone, or fields alone, holds no Empty Lines

In the examples below, `(ONE EMPTY LINE)` / `(FIRST EMPTY LINE)` / `(SECOND EMPTY LINE)` mark where empty lines go; the markers themselves are not written.




#### Examples

*public API function — S, D, A, R, E:*

```python
def normalize_scores(scores, weights, ceiling=1.0):
    """
    normalize a set of weighted scores to a fixed range
    (ONE EMPTY LINE)
    each score is multiplied by its matching weight, then the
    whole set is rescaled so the largest value equals ``ceiling``
    (FIRST EMPTY LINE)
    (SECOND EMPTY LINE)
    :param scores: raw scores to normalize
    :type scores: list[float]
    :param weights: weight for each score, keyed by its index;
            every score must have a matching weight
    :type weights: dict{int: float}
    :param ceiling: value the largest score is scaled to; default=1.0
    :type ceiling: float, optional
    :raises KeyError: a score index has no matching weight
    :raises ValueError: scores is empty
    :raises ValueError: every weighted score is zero
    :return: normalized scores, in original order
    :rtype: list[float]
    :example:
    >>> normalize_scores([1.0, 3.0], {0: 1.0, 1: 1.0})
    [0.333, 1.0]
    """
```

*class docstring, object methods — S, A, R:*

```python
class Rectangle:
    """
    an axis-aligned rectangle defined by its size
    (FIRST EMPTY LINE)
    (SECOND EMPTY LINE)
    :param width: width of the rectangle;
            must be a positive number
    :type width: float
    :param height: height of the rectangle;
            must be a positive number
    :type height: float
    :raises ValueError: width is not positive
    :raises ValueError: height is not positive
    """
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self._width = width
        self._height = height
```

*helper — S only:*

```python
def _clear_cache(self):
    """
    remove every entry from the internal cache
    """
    self._cache.clear()
```

*helper — R only:*

```python
def add(a, b):
    """
    :return: sum of ``a`` and ``b``
    :rtype: int
    """
    return a + b
```




#### Module & Script Docstrings

Start every module with a docstring whose first line is the filename, then a brief description of what it defines. This follows its own rule and carries none of the fields above:

```python
"""
email_validator.py
(SINGLE EMPTY LINE)
define ``EmailValidator`` and ``validate_address``
"""
```

For `__init__.py`, `__main__.py`, and `conftest.py`, the bare filename is ambiguous — prefix it with the dotted path of the containing package or directory (eg `my_package/sub/__init__.py` → `my_package.sub.__init__.py`):

```python
"""
my_package.__init__.py
(SINGLE EMPTY LINE)
expose ``EmailValidator`` and ``validate_address`` as the public API
"""
```




#### Field Rules

- Types (`:type:` / `:rtype:`): follow these forms, nesting them for Compound Structures

  - `int`, `float`, `str`, `bool`
  - `Iterable`
  - `Iterable(str)`
  - `list[bool]`
  - `dict{str: int}`
  - `tuple(float, float)`
  - `list[dict{str: int}]`
  - `Iterable(tuple(str, bool))`

- Optional Arguments: for a parameter with a default, append `, optional` to its `:type:` and `; default=<value>` to the end of its `:param:` description; see `ceiling` Above
- Raises: one `:raises:` entry per distinct scenario, even when scenarios share an Exception Type. Never merge them, see the two `ValueError` entries above
- Return: when a callable exists mainly to return a value, describe that value in R, not in S
- Wrapping: when a field line runs long, break after a `;` and indent the continuation; see `:param weights:` Above






#### {description}

writes, formats Python docstrings in Sphinx/reStructuredText

#### {when_to_use}

trigger whenever a Python function, method, class, or module is written or edited — docstrings are near-mandatory, so add or update one by default, not just on explicit request. Also trigger on docstring, Sphinx, reST, `:param:`, `:return:`, `:raises:`, `:type:` mentions

#### {globs}

```glob
**/*.py
```













### Coder Python Testing Guidelines

This section pertains specifically to Python test code. Tests should be compatible with the `pytest` module.

- used in combination with [Coder](#coder) and [Coder Python](#coder-python)
- test class names should start with `Test`, and test function names should begin with `test_`
- strive to create as many separate test functions as possible, with each test case in individual functions
- group related test cases under a single test class for organization
- test classes and test functions do **not** require docstrings — the class and function names should be descriptive enough to convey their purpose

**Each test file** must begin with a module-level docstring that briefly describes what unit or component is being tested.

*Example of tests for the `add` function:*

```python math_utils_test.py
"""
math_utils_test.py

tests for the `add` function in `math_utils.py`
"""


class TestAdd:
    def test_addition_of_integers(_):
        assert add(1, 1) == 2

    def test_addition_with_different_operands(_):
        assert add(1, 2) == 3
        assert add(2, 1) == 3

    def test_negative_value_error(_):
        with pytest.raises(ValueError) as ei:
            add(1, -1)
        assert str(ei.value) == (
            "Addition of negative value is not supported. Please contact your "
            "admin for more information.")

    def test_invalid_type_error(_):
        with pytest.raises(ValueError) as ei:
            add('a', 5)
        assert str(ei.value) == (
            "Addition of a string and an integer is not supported. Please "
            "contact your admin for more information.")
```





#### {description}

writes, reviews Python `pytest` test code per project conventions

#### {when_to_use}

trigger on `test_*.py`/`*_test.py` files, pytest, fixtures, mocks, parametrize, assertions, or requests like write/add/fix a unit test or test case. Not for non-test Python code

#### {globs}

```glob
**/test_*.py
**/*_test.py
```
