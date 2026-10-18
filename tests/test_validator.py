import pytest
from utils.validator import validate

def test_validate_string():
    assert validate("  hello world  ") == "hello world"
