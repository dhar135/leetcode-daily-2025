from typing import List


class Solution:
    
    def count_words_with_a_given_prefix(self, words: List[str], pref:str) -> int:
        """Returns the number of words in the list that start with the given prefix.

        Args:
            words (List[str]): List of words
            pref (str): prefix

        Returns:
            int: number of words in the list that start with the given prefix
        """

        count = 0

        for word in words:
            if word.startswith(pref):
                count += 1
        
        return count