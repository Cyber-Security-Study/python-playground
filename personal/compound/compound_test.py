import pytest
from compound import convert_percentage

def test_convert_percentage():
    assert convert_percentage(1) == 0.01