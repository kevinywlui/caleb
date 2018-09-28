def add_to_bibfile(citations,bib_file):

	with  open(bib_file,"a+") as f:

	for citation in citations:

		f.write(get_bibtex(parse_string(citation))



