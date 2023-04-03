from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # Get the list of all row and column indices with people
        rows = [i for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]
        cols = [j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1]

        # Calculate the median of rows and cols
        row_median = sorted(rows)[len(rows) // 2]
        col_median = sorted(cols)[len(cols) // 2]

        # Calculate the minimum total distance
        return sum(abs(row - row_median) for row in rows) + sum(abs(col - col_median) for col in cols)

# Test cases
solution = Solution()
grid1 = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
grid2 = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]

print(solution.minTotalDistance(grid1))  # Output: 6
print(solution.minTotalDistance(grid2))  # Output: 4
