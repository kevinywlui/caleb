import requests
import sys


def get_bibtex(**payload):
    r = requests.get('https://mathscinet.ams.org/mrlookup', params=payload)
    output = r.text
    return output.split('<pre>')[1].split('</pre>')[0].strip('\n')


def parse_string(s):
    pieces = s.split(':')
    payload = dict(zip(pieces, ['au', 'ti', 'year']))
    payload['format'] = 'bibtex'
    return payload


def parse_bib(filename):
    all_entries = set()
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith("@"):
                all_entries.add(line.split('{', 1)[1].split(',', 1)[0])
    return all_entries


def parse_aux(filename):
    with open(filename, "r") as f:
        citations = set()
        for line in f:
            if line.startswith("\\citation{"):
                citations.add(line[10:-2])
    return citations


def main():
    name = sys.argv[1]
    aux_file = name + ".aux"
    bib_file = name + ".bib"
    citations = parse_aux(aux_file)
    existing_bibs = parse_bib(bib_file)

    missing = citations.difference(existing_bibs)
    nikolas(missing, bib_file)


if __name__ == "__main__":
    main()
def add_to_bibfile(citations,bib_file):

	with  open(bib_file,"a+") as f:

	for citation in citations:

		f.write(get_bibtex(parse_string(citation))



