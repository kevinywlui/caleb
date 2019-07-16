import argparse
from .file_handler import AuxHandler, BibHandler
from .amslookup import AMSMRLookup


def launch():
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

    requested_citations = aux_h.citations()
    existing_bibs = bib_h.citations()
    missing_cits = requested_citations.difference(existing_bibs)

    new_cits = AMSMRLookup(missing_cits)
    bib_h.append_citations(new_cits)
