"""Script used for testing the file handler module.
"""

from pathlib import Path

import pytest

from caleb.file_handler import AuxHandler

tex_dir = Path("tests/tex_files")


def test_no_bibdata():
    test_file = tex_dir / "bad.aux"
    auxh = AuxHandler(str(test_file))
    with pytest.raises(LookupError):
        auxh.bibdata()
