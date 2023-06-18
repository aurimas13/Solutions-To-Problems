class Solution {
    private static final int MOD = 1_000_000_007;
    private static final int[][] DIRS = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int countPaths(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        Integer[][] dp = new Integer[m][n];
        int res = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                res = (res + dfs(i, j, m, n, grid, dp)) % MOD;
            }
        }

        return res;
    }

    private int dfs(int x, int y, int m, int n, int[][] grid, Integer[][] dp) {
        if (dp[x][y] != null) {
            return dp[x][y];
        }

        int res = 1;
        for (int[] dir : DIRS) {
            int nx = x + dir[0], ny = y + dir[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] > grid[x][y]) {
                res = (res + dfs(nx, ny, m, n, grid, dp)) % MOD;
            }
        }

        dp[x][y] = res;
        return res;
    }
}
