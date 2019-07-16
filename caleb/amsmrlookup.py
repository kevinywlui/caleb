import requests


class AMSMRLookup():
    """Handles searches for AMS MR Lookup.
    """
    def __init__(self, key):
        self.key = key

        # replace underscore by space
        key = key.replace("_", " ")

        # Pad with colons to handle the case where the user did not specify all
        # entries
        key = key + ':::'
        # Separate entries by colon
        self.author, self.title, self.year, *_ = key.split(':')

    def _payload(self):
        entries = self.author, self.title, self.year
        payload = dict(zip(["au", "ti", "year"], entries))
        payload["format"] = "bibtex"
        return payload

    def bibtex(self):
        try:
            return self._bibtex
        except AttributeError:
            pass

        r = requests.get("https://mathscinet.ams.org/mrlookup",
                         params=self._payload)
        output = r.text
        self.num_results = output.count("<pre>")
        self._bibtex = output.split("<pre>")[1].split("</pre>")[0].strip("\n")
        return self._bibtex
