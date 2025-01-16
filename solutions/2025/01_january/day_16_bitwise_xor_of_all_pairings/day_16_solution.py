from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = []

        for num1 in nums1:
            for num2 in nums2:
                nums3.append(num1 ^ num2)

        final_result = 0

        for num in nums3:
            final_result ^= num

        return final_result
