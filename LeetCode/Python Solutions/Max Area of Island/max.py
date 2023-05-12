from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        
        # Helper function to traverse an island using DFS
        def traverse_island(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            area = 1
            grid[i][j] = 0
            area += traverse_island(i+1, j)
            area += traverse_island(i-1, j)
            area += traverse_island(i, j+1)
            area += traverse_island(i, j-1)
            return area
        
        # Traverse each cell in the grid to find the maximum island area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = traverse_island(i, j)
                    max_area = max(max_area, area)
                    
        return max_area


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]])
    # Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
    # [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
    # [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    # [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]] -> 6
    # grid = [[0,0,0,0,0,0,0,0]] -> 0
    print(Solve)
