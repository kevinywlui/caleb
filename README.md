# caleb

[![PyPI version](https://badge.fury.io/py/caleb.svg)](https://badge.fury.io/py/caleb)
[![Coverage Status](https://coveralls.io/repos/github/kevinywlui/caleb/badge.svg?branch=master)](https://coveralls.io/github/kevinywlui/caleb?branch=master)
[![Build Status](https://travis-ci.org/kevinywlui/caleb.svg?branch=master)](https://travis-ci.org/kevinywlui/caleb)

**caleb** is a tool to automatically fill in your Latex citations.

## Usage examples

See the `examples` directory along with the `an_example.tex` file. The
following examples occur in the `examples` directory.

* First run `pdflatex an_example.tex ` to generate `an_example.aux`. `caleb`
  will now parse `an_example.aux` to generate the appropriate bibliography
  file.
```
caleb an_example
```

* The first important commandline option is `--take-first`. When making a
  query, it is possible that there are multiple result. By default, `caleb`
  will take no action here. However, if the `--take-first` flag is passed,
  `caleb` will take the first entry.
```
caleb --take-first an_example
```

* The next important commandline option is `--method`. By default, `caleb` uses
  `crossref.org`. However, we can also tell `caleb` to use
  <https://mathscinet.ams.org/mrlookup>.
```
caleb --method ams
```

## Workflow integration

### latexmk

* The best way is probably to integrate into `latexmk`. The `-pdflatex` flag
  allows us to run `caleb` after each `pdflatex` call.
```
latexmk -pdf -pdflatex='pdflatex %O %S; caleb -t -m ams %B' an_example
```

* We can set the `-pdflatex` flag in a `.latexmkrc` file. This can either go in
  the your tex project folder or in the home directory. So in the `.latexmkrc`
  file, include the following line (see examples directory for an example):
```
$pdflatex='pdflatex %O %S; caleb %B'
```

### Barebones

* The barebone approach is to run `caleb` before running bibtex.
```
pdflatex an_example
caleb an_example
bibtex an_example
pdflatex an_example
pdflatex an_example
```

### cocalc

<http://cocalc.com> contains a collaborative latex editor that allows you to use a
custom build command. We can use `caleb` by changing it to
```
latexmk -pdf -pdflatex='pdflatex %O %S; caleb -t -m ams %B' -f -g -bibtex -synctex=1 -interaction=nonstopmode an_example.tex
```


## Help

`caleb` comes with some command line arguments.
```
$ caleb --help
usage: caleb [-h] [-t] [-v] [--version] [-m {crossref,ams}] [input_name]

positional arguments:
  input_name

optional arguments:
  -h, --help            show this help message and exit
  -t, --take-first      Take first result if multiple results
  -v, --verbose         Increase verbosity of output
  --version             Outputs the version
  -m {crossref,ams}, --method {crossref,ams}
                        Specify a method for retrieving citations
```

## Installation

### Dependencies

* [crossref_commons_py](https://gitlab.com/crossref/crossref_commons_py)
* [requests](https://3.python-requests.org/)
* `python3`

### Testing and Development Dependencies

* [python-coveralls](https://github.com/z4r/python-coveralls)
* [pytest](https://pytest.org/en/latest/)
* [pytest-cov](https://github.com/pytest-dev/pytest-cov)
* [black](https://github.com/psf/black)

### `pip`

```
pip3 install caleb --user
```

### `setup.py`

```
python setup.py install --user
```


## Goal of project

* [ ] Reach feature parity with IRL [Caleb](https://sites.math.washington.edu/~geigerc/)

## Homepage

* https://github.com/kevinywlui/caleb
