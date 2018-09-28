import requests


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
