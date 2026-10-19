"""
tests/support.py

helpers shared by the skill export tests
"""

import re

__all__ = (
    "VERSION_LINE_PATTERN",
    "split_frontmatter_md_file",
    "is_frontmatter_md_file_basic_structure",
)

VERSION_LINE_PATTERN = re.compile(r"^  version: [a-z0-9.\-]+$")

_BASIC_FORMAT_RE = re.compile(r"^---\n(.+?)---\n(.+)", re.DOTALL)


def split_frontmatter_md_file(content):
    """
    split a markdown file with YAML frontmatter into frontmatter and body


    :param content: full markdown file content
    :type content: str
    :return: tuple of (frontmatter_lines, body_text)
    :rtype: tuple[list[str], str]
    """
    parts = content.split("---", 2)
    frontmatter = parts[1].strip("\n").splitlines()
    body = parts[2].strip("\n")
    return frontmatter, body


def is_frontmatter_md_file_basic_structure(content):
    """
    :param content: full markdown file content
    :type content: str
    :return: whether it matches ``---\\nfrontmatter\\n---\\nbody`` with a
            non-empty frontmatter and body
    :rtype: bool
    """
    match = _BASIC_FORMAT_RE.match(content)
    if not match:
        return False
    return bool(match.group(1).strip()) and bool(match.group(2).strip())
