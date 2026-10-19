"""
tests/conftest.py

load the library standalone, once per session, before any test module
is imported
"""

import kaye_library

kaye_library.setup_kaye_library_for_kaye_engine()
