# caleb

**caleb** is a tool to automatically fill in your Latex citations using https://mathscinet.ams.org/mrlookup.

## Usage

Here we will show off some ways to run `caleb`. All of these examples will
happen in the `test` directory. The goal is always to give `caleb` an `aux` to
parse.

* The barebone approach is to run
```
pdflatex test
caleb test
bibtex test
pdflatex test
pdflatex test
```

* In the previous example, we were missing the citations that yielded multiple
  entries. If we want to just take the first one, we can pass the
  `--take-first` flag.
```
pdflatex test
caleb --take-first test
bibtex test
pdflatex test
pdflatex test
```

* We can also integrate into `latexmk`:
```
latexmk -pdf -pdflatex='pdflatex %O %S; caleb %B'
```

* We can also set a `.latexmkrc`. This file will either go into the project
  directory or the home directory. In the `.latexmkrc` write:
```
$pdflatex='pdflatex %O %S; caleb %B'
``` 

## Installation


## Link

* https://github.com/kevinywlui/caleb
