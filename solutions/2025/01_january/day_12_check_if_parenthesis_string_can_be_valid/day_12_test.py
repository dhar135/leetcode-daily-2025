from day_12_solution import Solution

def test_template():
    solution = Solution()
    test_cases = [
        ("))()))", "010100", True),
        ("()()", "0000", True),
        (")", "0", False),
        ("()", "11", True),
        ("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", "100011110110011011010111100111011101111110000101001101001111", False),
        ("))))(())((()))))((()((((((())())((()))((((())()()))(()", "101100101111110000000101000101001010110001110000000101", False),
    ]

    for test_case in test_cases:
        assert solution.canBeValid(test_case[0], test_case[1]) == test_case[2]