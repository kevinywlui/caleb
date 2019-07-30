import subprocess
from caleb.__version__ import __version__


def test_version_request():
    version = subprocess.check_output(["poetry", "run", "caleb", "--version"])
    assert version.decode("utf-8")[:-1] == __version__
