from solution import Solution

def test_word_subsets():
    solution = Solution()
    test_cases = [
        (["amazon","apple","facebook","google","leetcode"], ["e","o"], ["facebook","google","leetcode"]),
        (["amazon","apple","facebook","google","leetcode"], ["lc","eo"], ["leetcode"]),
        (["acaac","cccbb","aacbb","caacc","bcbbb"], ["c","cc","b"], ["cccbb"])
    ]
    
    for words1, words2, expected in test_cases:
        assert solution.wordSubsets(words1, words2) == expected