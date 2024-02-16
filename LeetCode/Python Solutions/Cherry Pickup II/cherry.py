from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # dp[r][c1][c2] represents the max cherries collected when robot1 is at (r, c1) and robot2 is at (r, c2)
        dp = [[[0] * C for _ in range(C)] for _ in range(R)]
        
        # Initialize the DP table for the bottom row
        for c1 in range(C):
            for c2 in range(C):
                if c1 == c2:
                    dp[-1][c1][c2] = grid[-1][c1]
                else:
                    dp[-1][c1][c2] = grid[-1][c1] + grid[-1][c2]
        
        # Fill the DP table
        for r in range(R - 2, -1, -1):
            for c1 in range(C):
                for c2 in range(C):
                    maxCherries = 0
                    # Consider all movements for both robots
                    for dc1 in [-1, 0, 1]:
                        for dc2 in [-1, 0, 1]:
                            nc1, nc2 = c1 + dc1, c2 + dc2
                            if 0 <= nc1 < C and 0 <= nc2 < C:
                                maxCherries = max(maxCherries, dp[r+1][nc1][nc2])
                    dp[r][c1][c2] = maxCherries + grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)
        
        return dp[0][0][C-1]
