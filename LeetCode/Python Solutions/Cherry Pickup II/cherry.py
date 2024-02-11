class Solution {
    public int cherryPickup(int[][] grid) {
        int R = grid.length, C = grid[0].length;
        int[][][] dp = new int[R][C][C];
        
        // Initialize DP table for the bottom row
        for (int c1 = 0; c1 < C; ++c1) {
            for (int c2 = 0; c2 < C; ++c2) {
                dp[R-1][c1][c2] = c1 == c2 ? grid[R-1][c1] : grid[R-1][c1] + grid[R-1][c2];
            }
        }
        
        // Fill the DP table
        for (int r = R - 2; r >= 0; --r) {
            for (int c1 = 0; c1 < C; ++c1) {
                for (int c2 = 0; c2 < C; ++c2) {
                    int maxCherries = 0;
                    for (int dc1 = -1; dc1 <= 1; ++dc1) {
                        for (int dc2 = -1; dc2 <= 1; ++dc2) {
                            int nc1 = c1 + dc1, nc2 = c2 + dc2;
                            if (nc1 >= 0 && nc1 < C && nc2 >= 0 && nc2 < C) {
                                maxCherries = Math.max(maxCherries, dp[r+1][nc1][nc2]);
                            }
                        }
                    }
                    dp[r][c1][c2] = maxCherries + grid[r][c1] + (c1 != c2 ? grid[r][c2] : 0);
                }
            }
        }
        
        return dp[0][0][C-1];
    }
}
