from pathlib import Path
from shutil import copy

from caleb.app import Application
from caleb.file_handler import AuxHandler

tex_dir = Path("tests/tex_files")
control_bib_dir = tex_dir / "control_bibs"


def cmp_files(f1, f2):
    with open(f1, "r") as fh1:
        s1 = set(fh1.read().splitlines()).difference(set([""]))
    with open(f2, "r") as fh2:
        s2 = set(fh2.read().splitlines()).difference(set([""]))
    return s1 == s2


def test_clean_take_all(tmp_path):
    """Test a tex file with an empty bib without the --take-first flag.
    """
    test_file = tex_dir / "test.aux"

    # Copy to tmp_path and work from there
    test_file = copy(test_file, tmp_path)

    # Run caleb
    app = Application(str(test_file), verbose_level=0)
    app.go(take_first=True)
    test_bib = (tmp_path / AuxHandler(str(test_file)).bibdata()).with_suffix(".bib")

    control_bib = control_bib_dir / "take_all.bib"

    # Compare with control
    assert cmp_files(test_bib, control_bib)


def test_dirty_not_take_all(tmp_path):
    """Test a tex file with an empty bib without the --take-first flag.
    """
    test_file = tex_dir / "test.aux"
    partial_file = tex_dir / "biblio.bib"

    # Copy to tmp_path and work from there
    test_file = copy(test_file, tmp_path)
    copy(partial_file, tmp_path)

    # Run caleb
    app = Application(str(test_file), verbose_level=0)
    app.go(take_first=False)
    test_bib = (tmp_path / AuxHandler(str(test_file)).bibdata()).with_suffix(".bib")

    control_bib = control_bib_dir / "not_take_all.bib"

    # Compare with control
    assert cmp_files(test_bib, control_bib)
