from day_12_solution import Solution

def test_template():
    solution = Solution()
    test_cases = [
        ("))()))", "010100", True),
        ("()()", "0000", True),
        (")", "0", False),
    ]

    for test_case in test_cases:
        assert solution.canBeValid(test_case[0], test_case[1]) == test_case[2]