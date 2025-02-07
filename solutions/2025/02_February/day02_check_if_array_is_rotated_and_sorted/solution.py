from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 1

        for i in range(1, N * 2):
            if nums[(i - 1) % N] <= nums[i % N]:
                count += 1
            else:
                count = 1
            
            if count == N:
                return True

        return False
    
if __name__ == "__main__":
    solution = Solution()

    nums = [3, 4, 5, 1, 2]
    print(solution.check(nums))