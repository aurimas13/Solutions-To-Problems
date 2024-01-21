class Solution {
    public double knightProbability(int n, int k, int row, int column) {
        // Directions for the knight's move
        int[][] dirs = {{2, 1}, {2, -1}, {-2, 1}, {-2, -1}, {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};
        
        // Initialize the dp table with 0s
        double[][] dp = new double[n][n];
        dp[row][column] = 1;  // At start, probability of being inside the board is 1

        // Compute probabilities
        for (; k > 0; k--) {
            double[][] dp2 = new double[n][n];
            for (int r = 0; r < n; r++)
                for (int c = 0; c < n; c++)
                    for (int[] dir : dirs)
                        if (r + dir[0] >= 0 && r + dir[0] < n && c + dir[1] >= 0 && c + dir[1] < n)
                            dp2[r+dir[0]][c+dir[1]] += dp[r][c] / 8.0;  // Add up probabilities
            dp = dp2;
        }

        double res = 0.0;
        for (double[] dpRow : dp)
            for (double x : dpRow) res += x;  // Sum of all probabilities
        return res;
    }
}

