
caleb
=====


.. image:: https://badge.fury.io/py/caleb.svg
   :target: https://badge.fury.io/py/caleb
   :alt: PyPI version


.. image:: https://coveralls.io/repos/github/kevinywlui/caleb/badge.svg
   :target: https://coveralls.io/github/kevinywlui/caleb
   :alt: Coverage Status


.. image:: https://travis-ci.org/kevinywlui/caleb.svg?branch=master
   :target: https://travis-ci.org/kevinywlui/caleb
   :alt: Build Status


**caleb** is a tool to automatically fill in your Latex citations.

Usage examples
--------------

See the ``examples`` directory along with the ``an_example.tex`` file. The
following examples occur in the ``examples`` directory.


* 
  The best way is probably to integrate into ``latexmk``. The ``-pdflatex`` flag
  allows us to run ``caleb`` after each ``pdflatex`` call.

  .. code-block::

     latexmk -pdf -pdflatex='pdflatex %O %S; caleb %B' an_example

* 
  We can set the ``-pdflatex`` flag in a ``.latexmkrc`` file. This can either go in
  the your tex project folder or in the home directory. So in the ``.latexmkrc``
  file, include the following line (see examples directory for an example):

  .. code-block::

     $pdflatex='pdflatex %O %S; caleb %B'

* 
  The barebone approach is to run ``caleb`` before running bibtex.

  .. code-block::

     pdflatex an_example
     caleb an_example
     bibtex an_example
     pdflatex an_example
     pdflatex an_example

* 
  By default, ``caleb`` will ignore any citation where crossref.org returns
  multiple results. To take the first result ordered by relevance, pass the
  ``--take-first`` flag. For example,

  .. code-block::

     caleb --take-first an_example

Installation
------------

Dependencies
^^^^^^^^^^^^


* `crossref_commons_py <https://gitlab.com/crossref/crossref_commons_py>`_
* ``python3``

Testing and Development Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* `python-coveralls <https://github.com/z4r/python-coveralls>`_
* `pytest <https://pytest.org/en/latest/>`_ 
* `pytest-cov <https://github.com/pytest-dev/pytest-cov>`_
* `flake8 <http://flake8.pycqa.org/en/latest/>`_

``setup.py``
^^^^^^^^^^^^^^^^

.. code-block::

   python setup.py install --user

``pip``
^^^^^^^^^^^

.. code-block::

   pip3 install caleb --user

Goal of project
---------------


* [ ] Reach feature parity with IRL `Caleb <https://sites.math.washington.edu/~geigerc/>`_

Homepage
--------


* https://github.com/kevinywlui/caleb
