class Solution:
    # Constant variables for the 4 directions and the modulus
    DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    MOD = 10**9 + 7

    def countPaths(self, grid):
        m, n = len(grid), len(grid[0])  # Get the size of the grid
        dp = [[None] * n for _ in range(m)]  # Initialize the DP table
        res = 0  # Initialize the result

        # Iterate through each cell in the grid
        for i in range(m):
            for j in range(n):
                # Add the number of paths starting from the current cell to the result
                res = (res + self.dfs(i, j, m, n, grid, dp)) % self.MOD

        return res  # Return the result

    def dfs(self, x, y, m, n, grid, dp):
        # If the number of paths starting from the current cell has been calculated, return it
        if dp[x][y] is not None:
            return dp[x][y]

        res = 1  # Initialize the number of paths starting from the current cell

        # Iterate through each direction
        for dx, dy in self.DIRS:
            nx, ny = x + dx, y + dy  # Calculate the coordinates of the next cell

            # If the next cell is valid and its value is larger than the current cell
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                # Add the number of paths starting from the next cell to the result
                res = (res + self.dfs(nx, ny, m, n, grid, dp)) % self.MOD

        dp[x][y] = res  # Store the number of paths starting from the current cell
        return res  # Return the number of paths starting from the current cell
