from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 0
        dec = 0

        highest_count = 0

        count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                highest_count = max(inc, highest_count)
                dec = 0
            elif nums[i] < nums[i - 1]:
                dec += 1
                highest_count = max(dec, highest_count)
                inc = 0
            else:
                inc = 0
                dec = 0

        return highest_count + count
    
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 4, 3, 3, 2]
    print(f"{nums}: " + str(solution.longestMonotonicSubarray(nums)))

    nums = [3, 3, 3, 3]
    print(f"{nums}: " + str(solution.longestMonotonicSubarray(nums)))

    nums = [3, 2, 1]
    print(f"{nums}: " + str(solution.longestMonotonicSubarray(nums)))