"""This module is used for interfacing with
https://mathscinet.ams.org/mrlookup. In addition to retrieving the bibtex
entries, this module will also normalize the names.
"""
import requests


class AMSMRLookup:
    """Handles searches for AMS MR Lookup.

    Note:
        It is possible to initialize without the year.

    Args:
        key (str): A citation key assumed to be of the form author:title:year.

    """

    def __init__(self, key):
        self.key = key

        # replace underscore by space
        spaced_key = key.replace("_", " ")

        pieces = spaced_key.split(":")
        self.payload = dict(zip(["au", "ti", "year"], pieces))
        self.payload["format"] = "bibtex"

    def bib_entry(self):
        """Fetch the bibtex entry from amsmrlookup.

        Returns:
            str: A string ready to append to the bibtex file.
        """
        try:
            return self._bibtex
        except AttributeError:
            pass

        r = requests.get("https://mathscinet.ams.org/mrlookup", params=self.payload)
        output = r.text
        self._num_results = output.count("<pre>")

        # This is *almost* correct. We just have to fix the key.
        bib_entry = output.split("<pre>")[1].split("</pre>")[0].strip("\n")

        # Here we assume the first line is always
        # @something {OLD_CITATION,\n
        # Replace OLD_CITATION with citation
        # Use { and ,\n to find and replace
        a, b = bib_entry.split("{", 1)
        self._bib_entry = a + "{" + self.key + ",\n" + b.split(",\n", 1)[1]

        return self._bib_entry

    def num_results(self):
        """Return the number of results returned from the search.

        Note:
            This method will run `bib_entry` if it has not been ran already.
        Returns:
            int: the number of results.
        """
        try:
            return self._num_results
        except AttributeError:
            pass
        # call bibtex to get number of results
        self.bibtex()
        return self._num_results
