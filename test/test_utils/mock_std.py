"""
Utility functions for mocking stdin and stdout
"""

# pylint: disable=C

from unittest.mock import patch
from io import StringIO


def with_mock_in(string, func):
    with patch("sys.stdin", new=StringIO(string)):
        return func()


def with_mock_out(func, *args, **kwargs) -> str:
    with patch("sys.stdout", new=StringIO()) as mock_out:
        func(args, kwargs)
        return mock_out.getvalue()
