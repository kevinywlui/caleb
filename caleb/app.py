import logging
import os

from .file_handler import AuxHandler, BibHandler
from .reference import Reference


class Application:
    def __init__(self, input_name, verbose_level):
        if verbose_level == 0:
            logging.disable(logging.CRITICAL)
        elif verbose_level == 1:
            logging.basicConfig(level=logging.WARNING)
        elif verbose_level >= 2:
            logging.basicConfig(level=logging.INFO)

        # Normalize name by removing .tex and .aux, if necessary.
        filename, file_extension = os.path.splitext(input_name)
        if file_extension in [".tex", ".aux"]:
            input_name = filename

        # Set filenames
        aux_file = input_name + ".aux"
        aux_h = AuxHandler(aux_file)
        bib_file_name = aux_h.bibdata() + ".bib"

        dirname = os.path.dirname(aux_file)
        bib_file = os.path.join(dirname, bib_file_name)

        logging.info("aux file: {}".format(aux_file))
        logging.info("bib file: {}".format(bib_file))
        self.aux_file = aux_file
        self.bib_file = bib_file

    def go(self, take_first=False, method="crossref"):

        logging.info(f"Using {method} for citations")

        aux_h = AuxHandler(self.aux_file)
        bib_h = BibHandler(self.bib_file)

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
                if not take_first:
                    continue
            bibtex = new_bib.bibtex()
            logging.info("Appending: \n{}".format(bibtex))
            bib_h.append_a_citation(bibtex)
