import logging
import os

from .file_handler import AuxHandler, BibHandler
from .reference import Reference


class Application:
    """Glues together all the functionality of this package.

    This class is intended to be called by the `cmdline` module. Afterwards, it
    uses the `reference` module to obtain the bibtex entries. Then it uses
    `file_handler` to append the entries to .bib file.

    Args:
        input_name (str): Path to tex file whose bib entries we need to add.
    """

    def __init__(
        self, input_name: str, take_first: bool = False, method: str = "crossref"
    ):
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

        logging.info(f"Using {method} for citations")
        self.method = method

        logging.info(f"Taking first citation found: {take_first}")
        self.take_first = take_first

    def go(self) -> None:
        """Fill in the bibtex entries.

        Args:
            take_first (bool): Whether to just take the first bibtex entry.
            method (str): Determines whether we use `ams` or `crossref`.
        """

        aux_h = AuxHandler(self.aux_file)
        bib_h = BibHandler(self.bib_file)

        requested_citation_keys = aux_h.citation_keys()
        existing_bibs = bib_h.citation_keys()
        missing_cits = requested_citation_keys.difference(existing_bibs)
        logging.info(f"List of missing citations: {missing_cits}")

        for cit in missing_cits:
            logging.info("Working on: {}".format(cit))
            new_bib = Reference(cit, method=self.method)
            if not new_bib.exists():
                logging.warning("No results found for: {}".format(cit))
                continue
            elif not new_bib.is_unique():
                logging.warning("Multiple results found for: {}".format(cit))
                if not self.take_first:
                    continue
            bibtex = new_bib.bibtex()
            logging.info("Appending: \n{}".format(bibtex))
            bib_h.append_a_citation(bibtex)
