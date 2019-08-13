"""Script used for testing the reference module.
"""

import pytest

from caleb.reference import Reference

from .consts import mazur_eisenstein_citation


def test_when_exists_and_is_unique():
    # the crossref version yields a heisenbug
    ref = Reference("mazur:eisenstein", method="ams")
    assert ref.exists()
    assert ref.is_unique()
    assert ref.bibtex() == mazur_eisenstein_citation


def test_when_exists_and_not_is_unique():
    ref = Reference("mazur:modular", method="crossref")
    assert ref.exists()
    assert not ref.is_unique()

    ref = Reference("mazur:modular", method="ams")
    assert ref.exists()
    assert not ref.is_unique()


def test_when_exists_and_is_unique_with_year():
    ref = Reference("mazur:modular:2000", method="crossref")
    assert ref.exists()
    assert ref.is_unique()

    ref = Reference("mazur:modular:2000", method="ams")
    assert ref.exists()
    assert ref.is_unique()


def test_when_not_exists_and_not_is_unique():
    ref = Reference("fermat:marvelous", method="crossref")
    assert not ref.exists()
    with pytest.raises(ValueError):
        ref.is_unique()
    assert ref.bibtex() == ""

    ref = Reference("fermat:marvelous", method="ams")
    assert not ref.exists()
    with pytest.raises(ValueError):
        ref.is_unique()
    assert ref.bibtex() == ""
