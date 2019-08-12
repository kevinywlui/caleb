import argparse
import logging
import sys

from .__version__ import __version__
from .app import Application
from .reference import Reference


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_name", nargs="?")
    parser.add_argument(
        "-t",
        "--take-first",
        help="Take first result if multiple results",
        action="store_true",
    )
    parser.add_argument(
        "-v", "--verbose", help="Increase verbosity of output", action="count"
    )
    parser.add_argument("--version", help="Outputs the version", action="store_true")
    parser.add_argument(
        "-m",
        "--method",
        help="Specify a method for retrieving citations",
        choices=["crossref", "ams"],
        default="crossref",
    )
    parser.add_argument(
        "-g",
        "--get-this-key",
        help="Print the first entry with this key",
        action="store",
    )
    return parser


def launch() -> None:
    parser = make_parser()
    args = parser.parse_args(sys.argv[1:])

    # User is asking for version
    if args.version:
        print(__version__)
        sys.exit(0)
    elif args.get_this_key is not None:
        ref = Reference(key=args.get_this_key, method=args.method)
        print(ref.bibtex())
        sys.exit(0)
    elif args.input_name is None:
        print("Need input name")
        sys.exit(1)

    if args.verbose == 0:
        logging.disable(logging.CRITICAL)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.WARNING)
    elif args.verbose >= 2:
        logging.basicConfig(level=logging.INFO)

    app = Application(args.input_name, take_first=args.take_first, method=args.method)
    app.go()
