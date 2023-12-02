# test_my_module.py
import pytest
from src.my_module import my_function

#def test_my_function():
#    # Setup (if necessary)
#    input_value = "expected_input"
#    expected_output = "expected_result"
#
#    # Exercise
#    result = my_function(input_value)
#
#    # Verify
#    assert result == expected_output
#
#    # Teardown (if necessary)

def test_my_function():
    assert my_function() == "Hello, World!"

