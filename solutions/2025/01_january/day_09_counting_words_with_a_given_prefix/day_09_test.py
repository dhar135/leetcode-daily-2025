# test_solution.py
from day_09_solution import Solution

def test_prefix_count():
    solution = Solution()
    test_cases = [
        (["pay", "attention", "practice", "attend"], "at", 2),
        (["leetcode", "win", "loops", "success"], "code", 0)
    ]
    
    for words, pref, expected in test_cases:
        assert solution.count_words_with_a_given_prefix(words, pref) == expected