def parsing(filename):

	with open(filename,"r") as f:

		citations = set()

		for line in f:

			if line.startswith("\\citation{"):
				
				citations.add(line[10:-2])
				
		return citations




