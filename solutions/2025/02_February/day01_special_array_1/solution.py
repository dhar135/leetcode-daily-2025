from typing import List
from venv import logger

import pytest


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(1, len(nums)):
            if (nums[i] % 2 == nums[i - 1] % 2):
                return False
        return True
        


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 10]
    print(solution.isArraySpecial(nums))

        