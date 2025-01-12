from ast import main
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        max_freq = [0] * 26

        for word in words2:
            print("word: ", word)
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            for i in range(len(max_freq)):
                max_freq[i] = max(max_freq[i], freq[i])
            print("freq: ", freq)

        print("max_freq: ", max_freq)

        res = []

        for word in words1:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            if all(freq[i] >= max_freq[i] for i in range(len(max_freq))):
                res.append(word)
        
        print("res: ", res)
        return res
        


if __name__ == "__main__":
    
    solution = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]

    solution.wordSubsets(words1, words2)

