"""
docs_test.py

Unit Tests (using pytest) for: every relative link in the repository's
documents resolves, anchors included
"""

import pathlib
import re

import pytest

_ROOT = pathlib.Path(__file__).resolve().parent.parent
_DOCS = sorted(
    [
        *_ROOT.glob("*.md"),
        *_ROOT.glob("docs/*.md"),
    ]
)
_LINK = re.compile(r"\]\(([^)\s]+)\)")
_FENCE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)


def _slug(heading):
    slug = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return slug.replace(" ", "-")


def _anchors(path):
    text = _FENCE.sub("", path.read_text(encoding="utf-8"))
    return {
        _slug(m.group(1)) for m in re.finditer(r"^#+ (.*)$", text, re.MULTILINE)
    }


@pytest.mark.parametrize("path", _DOCS, ids=lambda p: p.name)
def test_relative_links_resolve(path):
    text = _FENCE.sub("", path.read_text(encoding="utf-8"))

    for target in _LINK.findall(text):
        if re.match(r"[a-z]+://", target) or target.startswith("#"):
            continue
        file_part, _, anchor = target.partition("#")
        linked = (path.parent / file_part).resolve()
        assert linked.is_file(), f"{path.name}: {target}"
        if anchor:
            assert anchor in _anchors(linked), f"{path.name}: {target}"


def test_every_doc_is_linked_from_readme_and_agents():
    readme = (_ROOT / "README.md").read_text(encoding="utf-8")
    agents = (_ROOT / "AGENTS.md").read_text(encoding="utf-8")

    for doc in sorted((_ROOT / "docs").glob("*.md")):
        assert f"docs/{doc.name}" in readme, doc.name
        assert f"docs/{doc.name}" in agents, doc.name
