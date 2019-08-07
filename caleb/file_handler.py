"""Module for handling files.

This module is used to interface with .aux and .bib files. The goal is to
eventually have it handle other formats.
"""
from typing import Set


class FileHandler:
    """Generic class for handling .aux and .bib files.
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename


class AuxHandler(FileHandler):
    """Class for handling .aux files.
    """

    def citation_keys(self) -> Set[str]:
        """Extract citation keys from this .aux file.

        Returns:
            set: Set of citation key found in this .aux file.
        """
        with open(self.filename, "r") as f:
            citation_keys = set()
            for line in f:
                if line.startswith("\\citation{"):
                    citation = line[10:-2]
                    if citation.count(":"):
                        citation_keys.add(citation)
        return citation_keys

    def bibdata(self) -> str:
        """Extract the location of user-specified .bib file from the .aux
        file.

        Returns:
            str: location of the user-specified .bib file.
        """
        with open(self.filename, "r") as f:
            for line in f:
                if line.startswith("\\bibdata{"):
                    bibdata = line[9:-2]
                    return bibdata
        assert False  # something went wrong


class BibHandler(FileHandler):
    """Class for handling .bib files.
    """

    def citation_keys(self) -> Set[str]:
        """Extract citation keys from this .bib file.

        Note:
            If `self.filename` is not a file, this will return an empty set.

        Returns:
            set: Set of citation key found in this .bib file.
        """
        all_entries = set()
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if line.startswith("@"):
                        all_entries.add(line.split("{", 1)[1].split(",", 1)[0])
        except FileNotFoundError:
            pass
        return all_entries

    def append_a_citation(self, citation: str) -> None:
        """Append a citation to this .bib file."

        Args:
            citation (str):  the citation to be appended.
        """
        with open(self.filename, "a") as f:
            f.write("\n")
            f.write(citation)
            f.write("\n")
