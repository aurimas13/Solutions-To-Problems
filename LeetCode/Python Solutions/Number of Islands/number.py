from typing import List

class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        # Initialize the count of islands
        count = 0

        # Iterate through the rows in the grid
        for i in range(len(grid)):
            # Iterate through the columns in the grid
            for j in range(len(grid[0])):
                # Check if the current cell is a land
                if grid[i][j] == '1':
                    # Perform DFS on the current cell and increment the count
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid: List[List[str]], i: int, j: int) -> None:
        # Check if the current cell is out of bounds or not a land
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        # Mark the current cell as visited
        grid[i][j] = '#'

        # Perform DFS on the neighboring cells
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# Test the solution
if __name__ == '__main__':
    s = Solution()
    test_grid = [['1', '1', '0', '0', '0'],
                 ['1', '1', '0', '0', '0'],
                 ['0', '0', '1', '0', '0'],
                 ['0', '0', '0', '1', '1']]
    print(s.num_islands(test_grid))  # Output: 3
