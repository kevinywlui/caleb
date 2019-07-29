import pytest
from shutil import copyfile


# Here we test
def test_clean_tex(tmp_path):
    """Test a tex file with an empty bib without the --take-first flag.
    """
    # Copy over files to tmp_path
    copyfile(
