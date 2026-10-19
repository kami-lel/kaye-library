"""
kaye_library.__main__.py
"""

from kaye_engine.cli.cli_main import register_cli_main_parser

from kaye_library import (
    PACKAGE_NAME,
    PROGRAM_NAME,
    setup_kaye_library_for_kaye_engine,
)


# auxiliaries  #################################################################
def main():
    setup_kaye_library_for_kaye_engine()

    cli_parser, _ = register_cli_main_parser(
        PACKAGE_NAME, PROGRAM_NAME
    )

    parsed_args = cli_parser.parse_args()
    parsed_args.func(parsed_args)  # call respective main function


# Entry Point  #################################################################
if __name__ == "__main__":
    main()
