from typing import List


class Solution:
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        Row, Col = len(grid), len(grid[0])
        if not grid or Row == 0:
            return 0
        for x in range(1, Row):
            grid[x][0] += grid[x - 1][0]
        for y in range(1, Col):
            grid[0][y] += grid[0][y - 1]

        for x in range(1, Row):
            for y in range(1, Col):
                grid[x][y] += min(grid[x - 1][y],
                                  grid[x][y - 1])
        return grid[-1][-1]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minPathSum(grid=[[1, 2, 3],[4, 5, 6]])  # grid = [[1,2,3],[4,5,6]] -> 12
    print(Solve)
