from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Step 1: Ensure the first column has all 1s
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1

        # Step 2: Maximize the 1s in each column from the second column onwards
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] ^= 1

        # Calculate the final score
        score = 0
        for row in grid:
            num = 0
            for bit in row:
                num = (num << 1) | bit
            score += num

        return score
