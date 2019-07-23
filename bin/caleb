#! /usr/bin/env python3

import argparse
import logging
import os
from caleb.file_handler import AuxHandler, BibHandler
from caleb.reference import Reference


def main():
    """Parse the command line arguments. Fill in the bibtex entries.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input_name")
    parser.add_argument(
        "-w",
        "--show-warnings",
        help="Show warnings when there is not a unique result in a search",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--take-first",
        help="Take first result if multiple results",
        action="store_true",
    )
    parser.add_argument("-v",
                        "--verbose",
                        help="Increase verbosity of output",
                        action="store_true")
    parser.add_argument(
        "-q",
        "--quiet",
        help="No output to stdout, overrides all other arguments",
        action="store_true",
    )
    args = parser.parse_args()
    input_name = args.input_name

    if args.quiet:
        logging.disable()
    elif args.verbose:
        logging.basicConfig(level=logging.INFO)
    elif args.show_warnings:
        logging.basicConfig(level=logging.WARNING)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    aux_file = input_name + ".aux"
    aux_h = AuxHandler(aux_file)
    bib_file_name = aux_h.bibdata() + ".bib"

    dirname = os.path.dirname(aux_file)
    bib_file = os.path.join(dirname, bib_file_name)

    logging.info("aux file: {}".format(aux_file))
    logging.info("bib file: {}".format(bib_file))

    bib_h = BibHandler(bib_file)

    requested_citation_keys = aux_h.citation_keys()
    existing_bibs = bib_h.citation_keys()
    missing_cits = requested_citation_keys.difference(existing_bibs)

    for cit in missing_cits:
        logging.info("Working on: {}".format(cit))
        new_bib = Reference(cit)
        if not new_bib.exists():
            logging.warning("No results found for: {}".format(cit))
            continue
        elif not new_bib.is_unique():
            logging.warning("Multiple results found for: {}".format(cit))
            if not args.take_first:
                continue
        bibtex = new_bib.bibtex()
        logging.info("Appending: \n{}".format(bibtex))
        bib_h.append_a_citation(bibtex)


if __name__ == "__main__":
    main()
