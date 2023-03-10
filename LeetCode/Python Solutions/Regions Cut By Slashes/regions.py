from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # create a 3*n x 3*n grid
        new_grid = [[0] * (3 * n) for _ in range(3 * n)]
        # fill in the new grid with slashes and spaces
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    new_grid[3*i][3*j+2] = 1
                    new_grid[3*i+1][3*j+1] = 1
                    new_grid[3*i+2][3*j] = 1
                elif grid[i][j] == '\\':
                    new_grid[3*i][3*j] = 1
                    new_grid[3*i+1][3*j+1] = 1
                    new_grid[3*i+2][3*j+2] = 1
        # count the number of regions using depth-first search
        count = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if new_grid[i][j] == 0:
                    self.dfs(new_grid, i, j)
                    count += 1
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 1:
            return
        grid[i][j] = 1
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.regionsBySlashes(grid = [" /","/ "])  
    # grid = [" /","/ "] -> 2
    # grid = [" /","  "] -> 1 
    print(Solve)
    