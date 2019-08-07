"""This module is used obtaining citations from references. Currently, this
module can use both the crossref api and can scrape the AMS page. Eventually,
more sources will be available.
"""

import requests
from crossref_commons.iteration import iterate_publications_as_json
from crossref_commons.retrieval import get_publication_as_refstring


class Reference:
    """Given a search key, this class will be able to retrieve data relating to
    the corresponding bibtex entry.

    Note:
        The key is assumed to be the form `author:title:year` or
        `author:title`. Underscores are replaced with a space.
    """

    def __init__(self, key, method="crossref"):
        self.key = key

        # replace underscore by space
        spaced_key = key.replace("_", " ")

        # data for query
        self.pieces = spaced_key.split(":")

        self.method = method

    def _get_bibtex(self):
        """Calls the correct version of _get_bibtex_XXX given self.method

        Returns:
            str: A bibtex entry.
        """
        if self.method == "crossref":
            return self._get_bibtex_crossref()
        elif self.method == "ams":
            return self._get_bibtex_ams()
        else:
            raise NotImplementedError()

    def _get_bibtex_ams(self):
        """Fetch the bibtex entry from amsmrlookup.

        Note:
            Results are cached.

        Returns:
            str: A bibtex entry.
        """
        self.payload = dict(zip(["au", "ti", "year"], self.pieces))
        self.payload["format"] = "bibtex"
        r = requests.get("https://mathscinet.ams.org/mrlookup", params=self.payload)
        output = r.text

        # set existence and uniqueness
        num_results = output.count("<pre>")
        if num_results == 0:
            self._exists = False
        elif num_results == 1:
            self._exists = True
            self._is_unique = True
        else:
            self._exists = True
            self._is_unique = False

        # This is *almost* correct. We just have to fix the key.
        bibtex = output.split("<pre>")[1].split("</pre>")[0].strip("\n")

        # Here we assume the first line is always
        # @something {OLD_CITATION,\n
        # Replace OLD_CITATION with citation
        # Use { and ,\n to find and replace
        a, b = bibtex.split("{", 1)
        self._bibtex = a + "{" + self.key + ",\n" + b.split(",\n", 1)[1]

        return self._bibtex

    def _get_bibtex_crossref(self):
        """Internal function to fetch the bibtex entry and determine existence
        and uniqueness.

        Note:
            Results are cached.

        Returns:
            str: A bibtex entry.
        """
        queries = dict(
            zip(["query.author", "query.title", "query.bibliographic"], self.pieces)
        )
        queries["sort"] = "relevance"

        iter_pub = iterate_publications_as_json(queries=queries)
        try:
            doi = next(iter_pub)["DOI"]
            self._exists = True
        except StopIteration:
            self._exists = False
            return
        try:
            next(iter_pub)
            self._is_unique = False
        except StopIteration:
            self._is_unique = True

        # This is almost correct! We just need to change the citation key to
        # self.key
        raw_bibtex = get_publication_as_refstring(doi, "bibtex")

        # Here we assume the first line is always
        # @something {OLD_CITATION,
        # Replace OLD_CITATION with citation
        # Use { and , to find and replace
        a, b = raw_bibtex.split("{", 1)
        self._bibtex = a + "{" + self.key + "," + b.split(",", 1)[1]

        # Remove leading whitespace if necessary
        if self._bibtex[0] == " ":
            self._bibtex = self._bibtex[1:]
        return

    def bibtex(self):
        """Return the first bibtex entry found given the citation.

        Note:
            This calls _get_bibtex if it has not been ran already.

        Returns:
            str: bibtex entry
        """
        if not self.exists():
            return None
        return self._bibtex

    def exists(self):
        """Return whether a citation for this reference exists.

        Note:
            This calls _get_bibtex if it has not been ran already.

        Returns:
            bool: True if citations exists and False otherwise.
        """
        try:
            return self._exists
        except AttributeError:
            self._get_bibtex()
        return self._exists

    def is_unique(self):
        """Return whether a citation for this reference is unique.

        Note:
            Since self.exists() calls self._get_bibtex(), we don't need to make
            sure to call self._get_bibtex()

            Uniqueness only makes sense given existence.

        Returns:
            bool: True if citations is unique and False otherwise.
        """
        if not self.exists():
            raise ValueError("Determining uniqueness requires existence.")

        return self._is_unique
