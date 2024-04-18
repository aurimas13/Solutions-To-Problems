from typing import List
from collections import deque


from typing import List
from collections import deque


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # Check up
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # Check down
                    if i == rows - 1 or grid[i+1][j] == 0:
                        perimeter += 1
                    # Check left
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # Check right
                    if j == cols - 1 or grid[i][j+1] == 0:
                        perimeter += 1
        return perimeter


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] -> 16
    # grid = [[1]] -> 4
    # grid = [[1,0]] -> 4
    print(Solve)
