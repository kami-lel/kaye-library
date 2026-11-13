"""
example_consumer.__main__.py
"""

from kaye_engine.cli.cli_main import register_cli_main_parser

from example_consumer import (
    PACKAGE_NAME,
    PROGRAM_NAME,
    setup_example_consumer,
)


def main():
    setup_example_consumer()

    cli_parser, _ = register_cli_main_parser(PACKAGE_NAME, PROGRAM_NAME)

    parsed_args = cli_parser.parse_args()
    parsed_args.func(parsed_args)


if __name__ == "__main__":
    main()
