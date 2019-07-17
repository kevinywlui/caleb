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
        "--show_warnings",
        help="Show warnings when there is not a unique result in a search",
        action="store_true",
    )
    parser.add_argument(
        "-t",
        "--take-first",
        help="Take first result if multiple results",
        action="store_true",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="No output to stdout, overrides all other arguments",
        action="store_true",
    )
    parser.add_argument(
        "-b",
        "--bibfile",
        help="Location of .bib file",
        action="store",
        default=''
    )
    args = parser.parse_args()
    input_name = args.input_name
    bib_name = args.bibfile

    if args.quiet:
        logging.disable()
    elif args.show_warning:
        logging.basicConfig(level=logging.WARNING)

    aux_file = input_name + ".aux"
    aux_h = AuxHandler(aux_file)

    if bib_name:
        bib_file = bib_name + ".bib"
    else:
        bib_file = aux_h.bibdata() + ".bib"

    bib_h = BibHandler(bib_file)

    requested_citation_keys = aux_h.citation_keys()
    existing_bibs = bib_h.citation_keys()
    missing_cits = requested_citation_keys.difference(existing_bibs)

    for cit in missing_cits:
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
