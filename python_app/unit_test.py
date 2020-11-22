"""
Unit tests
"""

import app

def test_add_one_to_input():
    """
    Test function add_one_to_input
    """
    my_number = 5
    assert app.add_one_to_input(my_number) == 6

def test_subtract_one_to_input():
    """
    Test function subtract_one_to_input
    """
    my_number = 5
    assert app.subtract_one_to_input(my_number) == 4
