import doctest
import unittest
from . import convert


def load_tests(loader, tests, ignore):
    """
    This function adds the doctests to the discovery process.
    """
    tests.addTests(doctest.DocTestSuite(convert))
    return tests


if __name__ == "__main__":
    unittest.main()