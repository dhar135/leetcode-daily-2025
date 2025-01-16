from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        len1 = len(nums1)
        len2 = len(nums2)

        freq = {}  # store the frequency of each number's appearances in the final XOR computations.

        for num in nums1:
            freq[num] = freq.get(num, 0) + len2

        for num in nums2:
            freq[num] = freq.get(num, 0) + len1

        ans = 0
        for num in freq:
            if freq[num] % 2:
                ans ^= num
        return ans


