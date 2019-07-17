import argparse
import logging
from .file_handler import AuxHandler, BibHandler
from .amsmrlookup import AMSMRLookup


def launch():
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
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument(
        "-q",
        "--quiet",
        help="No output to stdout, overrides all other arguments",
        action="store_true",
    )
    parser.add_argument(
        "-b", "--bibfile", help="Location of .bib file", action="store", default=""
    )
    args = parser.parse_args()
    input_name = args.input_name
    bib_name = args.bibfile

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

    if bib_name:
        bib_file = bib_name + ".bib"
    else:
        bib_file = aux_h.bibdata() + ".bib"
    logging.info("aux file: {}".format(aux_file))
    logging.info("bib file: {}".format(bib_file))

    bib_h = BibHandler(bib_file)

    requested_citation_keys = aux_h.citation_keys()
    existing_bibs = bib_h.citation_keys()
    missing_cits = requested_citation_keys.difference(existing_bibs)

    for cit in missing_cits:
        logging.info("Working on: {}".format(cit))
        new_bib = AMSMRLookup(cit)
        bib_entry = new_bib.bib_entry()
        num_results = new_bib.num_results()
        if num_results == 0:
            logging.warning("No results found for: {}".format(cit))
        elif num_results > 1:
            logging.warning("Multiple results found for: {}".format(cit))
            if not args.take_first:
                continue
        bib_h.append_a_citation(bib_entry)
