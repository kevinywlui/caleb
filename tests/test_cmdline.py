import subprocess

from caleb.__version__ import __version__

from .consts import mazur_eisenstein_citation


def test_version_request():
    version = subprocess.check_output(["poetry", "run", "caleb", "--version"])
    assert version.decode("utf-8")[:-1] == __version__


def test_missing_argument():
    try:
        subprocess.check_output(["poetry", "run", "caleb"])
    except subprocess.CalledProcessError as e:
        assert e.output.decode("utf-8")[:-1] == "Need input name"


def test_get_this_key():
    mazur = subprocess.check_output(
        [
            "poetry",
            "run",
            "caleb",
            "--get-this-key",
            "mazur:eisenstein",
            "--method",
            "ams",
        ]
    )
    assert mazur.decode("utf-8")[:-1] == mazur_eisenstein_citation
