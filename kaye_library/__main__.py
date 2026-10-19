"""
kaye_library.__main__.py
"""

from argparse import ArgumentParser
from importlib.metadata import version

from kaye_library import PACKAGE_NAME, PROGRAM_NAME

# constants  ###################################################################
_DOC = (
    "entry point for kaye-library's console script: registers this"
    " package's corpus, abbr data, and blueprints, then hands off to"
    " kaye-engine's CLI dispatcher"
)


# auxiliaries  #################################################################
def main():
    # TODO run library setup, then kaye-engine's CLI subcommands
    cli_parser = ArgumentParser(prog=PROGRAM_NAME, description=_DOC)
    cli_parser.add_argument(
        "--version",
        action="version",
        version=str(version(PACKAGE_NAME)),
    )
    cli_parser.set_defaults(func=lambda _: cli_parser.print_help())

    parsed_args = cli_parser.parse_args()
    parsed_args.func(parsed_args)  # call respective main function


# Entry Point  #################################################################
if __name__ == "__main__":
    main()
