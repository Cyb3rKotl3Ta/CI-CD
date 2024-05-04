# test_my_module.py

import pytest
from src.my_module import add_numbers

def test_add_numbers():
    # Test with positive numbers
    assert add_numbers(3, 4) == 7, "Should be 7"

    # Test with negative numbers
    assert add_numbers(-1, -1) == -2, "Should be -2"

    # Test with zero
    assert add_numbers(0, 0) == 0, "Should be 0"

    # Test with positive and negative number
    assert add_numbers(-5, 10) == 5, "Should be 5"
