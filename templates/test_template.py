from solution import Solution

def test_template():
    solution = Solution()
    test_cases = [
        # Add test cases here
        # (["pay", "attention", "practice", "attend"], "at", 2),
        # (["leetcode", "win", "loops", "success"], "code", 0)
    ]

    for test_case in test_cases:
        assert solution.testfunction(test_case[0], test_case[1]) == test_case[2]