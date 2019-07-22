# caleb

[![Coverage Status](https://coveralls.io/repos/github/kevinywlui/caleb/badge.svg)](https://coveralls.io/github/kevinywlui/caleb)

**caleb** is a tool to automatically fill in your Latex citations.

## Usage examples

* The best way is probably to integrate into `latexmk`.
```
latexmk -pdf -pdflatex='pdflatex %O %S; caleb %B'
```

* We can also set a `.latexmkrc`. This file will either go into the project
  directory or the home directory. In the `.latexmkrc` write:
```
$pdflatex='pdflatex %O %S; caleb %B'
``` 

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


## Installation

### Dependency

* [crossref_commons_py](https://gitlab.com/crossref/crossref_commons_py)
* `python3`

### `setup.py`

```
python setup.py install --user
```

### `pip`

```
pip3 install caleb --user
```

## Goal of project

* [ ] Reach feature parity with IRL [Caleb](https://sites.math.washington.edu/~geigerc/)

## Homepage

* https://github.com/kevinywlui/caleb
