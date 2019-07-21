"""This module is used obtaining citations from references. We mainly use the
crossref api but it'll be good to add more sources in the future.
"""

from crossref_commons.iteration import iterate_publications_as_json
from crossref_commons.retrieval import get_publication_as_refstring


class Reference:
    """This class handles things you would want to do with a reference.

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
        self.queries = dict(
            zip(["query.author", "query.title", "query.bibliographic"], pieces)
        )
        self.queries["sort"] = "relevance"

    def _get_bibtex(self):
        """Internal function to fetch the bibtex entry and determine existence
        and uniqueness.

        Note:
            Results are cached.
        """
        iter_pub = iterate_publications_as_json(queries=self.queries)
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

        Returns:
            bool: True if citations is unique and False otherwise.
        """
        if not self.exists():
            raise ValueError("Determining uniqueness requires existence.")

        return self._is_unique
