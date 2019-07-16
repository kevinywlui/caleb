import argparse
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
    args = parser.parse_args()
    input_name = args.input_name

    aux_file = input_name + ".aux"
    aux_h = AuxHandler(aux_file)

    bib_file = input_name + ".bib"
    bib_h = BibHandler(bib_file)

    requested_citation_keys = aux_h.citation_keys()
    existing_bibs = bib_h.citation_keys()
    missing_cits = requested_citation_keys.difference(existing_bibs)

    for cit in missing_cits:
        new_bib = AMSMRLookup(cit)
        bib_h.append_a_citation(new_bib.bib_entry())
