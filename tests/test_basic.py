"""Basic tests to verify CI pipeline setup."""
import sys


def test_python_version():
    """Verify Python version is 3.10 or higher."""
    assert sys.version_info >= (3, 12), "Python 3.10+ required"


# def test_imports():
#     """Verify core dependencies can be imported."""
#     try:
#         import fastapi
#         import pandas
#         import numpy
#         import scipy
#         assert True
#     except ImportError as e:
#         raise AssertionError()
