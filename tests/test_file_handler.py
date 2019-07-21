"""Script used for testing the file handler module.
"""

import pytest
import subprocess
import os
from caleb.file_handler import FileHandler, AuxHandler, BibHandler
from .consts import aux_clean_keys


def test_file_handler():
    filename = 'mazur:eisenstein'
    FH = FileHandler(filename)
    assert FH.filename == filename
    with pytest.raises(NotImplementedError):
        FH.citation_keys()


def test_clean_tex():
    tex_file_path = 'tests/tex_files/'
    name = tex_file_path + 'test_clean'
    assert os.path.getsize('tests/tex_files/biblio_clean.bib') == 0
    subprocess.run(["latexmk", "-pdf", "-cd", name])
    aux_h = AuxHandler(name + '.aux')
    assert aux_clean_keys == aux_h.citation_keys()
    bib_h = BibHandler(aux_h.bibdata())
    assert bib_h.citation_keys() == set()
    subprocess.run(["git", "clean", "-xf", tex_file_path])
    subprocess.run(["git", "checkout", tex_file_path])
