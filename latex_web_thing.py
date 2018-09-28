import requests


def get_bib(**payload):
    r = requests.get('https://mathscinet.ams.org/mrlookup', params=payload)
    output = r.text
    return output.split('<pre>')[1].split('</pre>')[0].strip('\n')
