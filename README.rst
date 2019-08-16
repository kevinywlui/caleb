
caleb
=====


.. image:: https://badge.fury.io/py/caleb.svg
   :target: https://badge.fury.io/py/caleb
   :alt: PyPI version


.. image:: https://coveralls.io/repos/github/kevinywlui/caleb/badge.svg?branch=master
   :target: https://coveralls.io/github/kevinywlui/caleb?branch=master
   :alt: Coverage Status


.. image:: https://travis-ci.org/kevinywlui/caleb.svg?branch=master
   :target: https://travis-ci.org/kevinywlui/caleb
   :alt: Build Status


.. image:: https://img.shields.io/lgtm/grade/python/g/kevinywlui/caleb.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/kevinywlui/caleb/context:python
   :alt: Language grade: Python


.. image:: https://img.shields.io/github/license/kevinywlui/caleb
   :target: https://img.shields.io/github/license/kevinywlui/caleb
   :alt: GitHub


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: code style


Overview
--------

``caleb`` is a tool for automatically filling in your Latex citations. It assumes
that the citations in your tex files are of the form ``\cite{author:title:year}``
or ``\cite{author:title}``. ``caleb`` then extracts the citation keys from the aux
file and will retrieve bibliographic data from either
https://www.crossref.org/ (default) or https://mathscinet.ams.org/mrlookup.
By default, these entries are then appending to the bib file. If the
``--dry-run`` option is passed, then the entries are printed instead.

Usage examples
--------------

The quickest way to see what ``caleb`` is doing is to use the ``--get-this-key``
flag.

.. code-block::

   $ caleb --get-this-key 'mazur:eisenstein' --method 'ams'
   @article {mazur:eisenstein,
       AUTHOR = {Mazur, B.},
        TITLE = {Modular curves and the {E}isenstein ideal},
         NOTE = {With an appendix by Mazur and M. Rapoport},
      JOURNAL = {Inst. Hautes \'{E}tudes Sci. Publ. Math.},
     FJOURNAL = {Institut des Hautes \'{E}tudes Scientifiques. Publications
                 Math\'{e}matiques},
       NUMBER = {47},
         YEAR = {1977},
        PAGES = {33--186 (1978)},
         ISSN = {0073-8301},
      MRCLASS = {14G25 (10D05)},
     MRNUMBER = {488287},
   MRREVIEWER = {M. Ohta},
          URL = {http://www.numdam.org/item?id=PMIHES_1977__47__33_0},
   }

The following examples occur in the ``examples`` directory.


* 
  First run ``pdflatex an_example.tex`` to generate ``an_example.aux``. ``caleb``
  will now parse ``an_example.aux`` to generate the appropriate bibliography
  file.

  .. code-block::

     $ caleb an_example

* 
  The first important commandline option is ``--take-first``. When making a
  query, it is possible that there are multiple result. By default, ``caleb``
  will take no action here. However, if the ``--take-first`` flag is passed,
  ``caleb`` will take the first entry.

  .. code-block::

     $ caleb --take-first an_example

* 
  The next important commandline option is ``--method``. By default, ``caleb`` uses
  ``crossref.org``. However, we can also tell ``caleb`` to use
  https://mathscinet.ams.org/mrlookup.

  .. code-block::

     $ caleb --method ams an_example

Workflow integration
--------------------

latexmk
^^^^^^^


* 
  The best way is probably to integrate into ``latexmk``. The ``-pdflatex`` flag
  allows us to run ``caleb`` after each ``pdflatex`` call.

  .. code-block::

     latexmk -pdf -pdflatex='pdflatex %O %S; caleb -t -m ams %B' an_example

* 
  We can set the ``-pdflatex`` flag in a ``.latexmkrc`` file. This can either go in
  the your tex project folder or in the home directory. So in the ``.latexmkrc``
  file, include the following line (see examples directory for an example):

  .. code-block::

     $pdflatex='pdflatex %O %S; caleb %B'

Barebones
^^^^^^^^^


* The barebone approach is to run ``caleb`` before running bibtex.
  .. code-block::

     pdflatex an_example
     caleb an_example
     bibtex an_example
     pdflatex an_example
     pdflatex an_example

cocalc
^^^^^^

http://cocalc.com contains a collaborative latex editor that allows you to use a
custom build command. We can use ``caleb`` by changing it to

.. code-block::

   latexmk -pdf -pdflatex='pdflatex %O %S; caleb -t -m ams %B' -f -g -bibtex -synctex=1 -interaction=nonstopmode an_example.tex

Help
----

``caleb`` comes with some command line arguments.

.. code-block::

   $ caleb --help
   usage: caleb [-h] [-t] [-v] [--version] [-m {crossref,ams}] [-g GET_THIS_KEY]
                [-dr]
                [input_name]

   positional arguments:
     input_name

   optional arguments:
     -h, --help            show this help message and exit
     -t, --take-first      Take first result if multiple results
     -v, --verbose         Increase verbosity of output
     --version             Outputs the version
     -m {crossref,ams}, --method {crossref,ams}
                           Specify a method for retrieving citations
     -g GET_THIS_KEY, --get-this-key GET_THIS_KEY
                           Print the first entry with this key
     -dr, --dry-run        Write the changes to stdout instead of the bibtex

Installation
------------

Dependencies
^^^^^^^^^^^^


* `crossref_commons_py <https://gitlab.com/crossref/crossref_commons_py>`_
* `requests <https://3.python-requests.org/>`_
* ``python3`` (tested with >=3.6)

Testing and Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* `poetry <https://github.com/sdispater/poetry>`_
* `python-coveralls <https://github.com/z4r/python-coveralls>`_
* `pytest <https://pytest.org/en/latest/>`_
* `pytest-cov <https://github.com/pytest-dev/pytest-cov>`_
* `black <https://github.com/psf/black>`_
* `isort <https://github.com/timothycrosley/isort>`_
* `mypy <https://github.com/python/mypy>`_

``pip``
^^^^^^^^^^^

The recommended method is to get ``caleb`` from its `PyPI
repository <https://pypi.org/project/caleb/>`_.

.. code-block::

   pip3 install caleb --user

``setup.py``
^^^^^^^^^^^^^^^^

Alternatively, a ``setup.py`` file is auto-generated using
`dephell <https://github.com/dephell/dephell>`_. Let me know if something goes
wrong!

.. code-block::

   python setup.py install --user

Goal of project
---------------


* [ ] Reach feature parity with IRL
  `Caleb <https://sites.math.washington.edu/~geigerc/>`_ by version 2.13.1995.

Homepage
--------


* https://github.com/kevinywlui/caleb
