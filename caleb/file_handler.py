class FileHandler():
    def __init__(self, filename):
        self.filename = filename

    def citations(self):
        return NotImplementedError("Override this")


class AuxHandler(FileHandler):
    def citations(self):
        with open(self.filename, "r") as f:
            citations = set()
            for line in f:
                if line.startswith("\\citation{"):
                    citation = line[10:-2]
                    if citation.count(":"):
                        citations.add(citation)
        return citations


class BibHandler(FileHandler):
    def citations(self):
        all_entries = set()
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if line.startswith("@"):
                        all_entries.add(line.split("{", 1)[1].split(",", 1)[0])
        except FileNotFoundError:
            pass
        return all_entries

    def append_citations(self, citations):
        with open(self.filename, "r") as f:
            for cit in citations:
                f.write("\n")
                f.write(cit)
                f.write("\n")
