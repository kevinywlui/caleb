import argparse
import sys
from .app import Application
from .__version__ import __version__


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_name", nargs="?")
    parser.add_argument(
        "-t",
        "--take-first",
        help="Take first result if multiple results",
        action="store_true",
    )
    parser.add_argument(
        "-v", "--verbose", help="Increase verbosity of output", action="store_true"
    )
    parser.add_argument("--version", help="Outputs the version", action="store_true")
    return parser


def launch():
    parser = make_parser()
    args = parser.parse_args(sys.argv[1:])

    # User is asking for version
    if args.version:
        print(__version__)
        sys.exit(0)
    elif args.input_name is None:
        print("Need input name")
        sys.exit(1)

    app = Application(args.input, args.verbose_level)
    app.go(take_first=args.take_first)
