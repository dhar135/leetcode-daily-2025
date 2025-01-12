import pytest
from solution import solution_function  # Replace with your function name

# Test cases for the problem
@pytest.mark.parametrize(
    "input_data, expected",
    [
        # Add your test cases here as tuples (input_data, expected_output)
        # Example format:
        # ({"words": ["pay", "attention", "practice", "attend"], "pref": "at"}, 2),
        # ({"words": ["leetcode", "win", "loops", "success"], "pref": "code"}, 0),
    ]
)
def test_solution_function(input_data, expected):
    """
    Test the solution function with various input and expected output pairs.
    """
    assert solution_function(**input_data) == expected
