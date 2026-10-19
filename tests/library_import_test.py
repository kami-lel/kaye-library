import importlib
import subprocess
import sys


class TestStructure:
    def test_import_loads_nothing(self):
        code = (
            "import kaye_library\n"
            "from kaye_engine.prompt.blueprint.registry import"
            " blueprint_registry\n"
            "from kaye_engine.abbr_collection import get_abbr_data\n"
            "assert not blueprint_registry\n"
            "assert not get_abbr_data()\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", code], capture_output=True, text=True
        )
        assert result.returncode == 0, result.stderr

    def test_package_name(self):
        module = importlib.import_module("kaye_library")
        assert module.PACKAGE_NAME == "kaye-library"


class TestContent:
    def test_help_runs(self):
        result = subprocess.run(
            ["kaye-library", "--help"], capture_output=True, text=True
        )
        assert result.returncode == 0
        assert "Kaye Engine CLI: " in result.stdout
