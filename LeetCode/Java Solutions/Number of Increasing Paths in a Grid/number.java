class Solution {
    // Constant variables for the 4 directions and the modulus
    private static final int MOD = 1_000_000_007;
    private static final int[][] DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int countPaths(int[][] grid) {
        int m = grid.length, n = grid[0].length;  // Get the size of the grid
        Integer[][] dp = new Integer[m][n];  // Initialize the DP table
        int res = 0;  // Initialize the result

        // Iterate through each cell in the grid
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                // Add the number of paths starting from the current cell to the result
                res = (res + dfs(i, j, m, n, grid, dp)) % MOD;
            }
        }

        return res;  // Return the result
    }

    private int dfs(int x, int y, int m, int n, int[][] grid, Integer[][] dp) {
        // If the number of paths starting from the current cell has been calculated, return it
        if (dp[x][y] != null) {
            return dp[x][y];
        }

        int res = 1;  // Initialize the number of paths starting from the current cell

        // Iterate through each direction
        for (int[] dir : DIRS) {
            int nx = x + dir[0], ny = y + dir[1];  // Calculate the coordinates of the next cell

            // If the next cell is valid and its value is larger than the current cell
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] > grid[x][y]) {
                // Add the number of paths starting from the next cell to the result
                res = (res + dfs(nx, ny, m, n, grid, dp)) % MOD;
            }
        }

        dp[x][y] = res;  // Store the number of paths starting from the current cell
        return res;  // Return the number of paths starting from the current cell
    }
}

