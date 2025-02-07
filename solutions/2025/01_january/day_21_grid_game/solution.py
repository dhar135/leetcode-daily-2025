from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        # First we need to find the number of rows and columns
        # We know grix is 2xn, so n is the length of each row
        n = len(grid[0])

        # Create prefix sums for both rows 
        # We add a leading 0 to make calculation easier
        # top_prefix[i] will give us sum of grid[0][0] to grid[0][i-1]
        top_prefix = [0]

        bottom_prefix = [0]

        for i in range(n):
            top_prefix.append(top_prefix[-1] + grid[0][i])
            bottom_prefix.append(bottom_prefix[-1] + grid[1][i])



        # Initialize robot2's best possible score
        # We'll try to minimize this
        robot2_best_score = 0

        # Try each possible column where robot 1 could move down
        for k in range(n):
            # When robot1 moves down at column k:
            # 1. It takes all points from top row from 0 to k-1
            # 2. Then takes all points from bottom row from k to n-1
            # 3. These cells become 0
            
            # Calculate what's left for robot2:
            # - In top row: sum from k+1 to n-1
            remaining_top = top_prefix[n] - top_prefix[k + 1]

            remaining_bottom = bottom_prefix[k]

             # Robot2 will choose the maximum between:
            # 1. Going down early and getting remaining bottom points
            # 2. Going down late and getting remaining top points
            robot2_score = max(remaining_top, remaining_bottom)
            
            # Robot1 wants to minimize robot2's best possible score
            robot2_best_score = min(robot2_best_score, robot2_score)

        return robot2_best_score






if __name__ == "__main__":
    grid = [[2, 5, 4], [1, 5, 1]]
    solution = Solution()
    print(solution.gridGame(grid))