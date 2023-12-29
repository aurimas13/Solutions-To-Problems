class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) return -1;

        int[][] dp = new int[n + 1][d + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= d; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }
        dp[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.min(i, d); j++) {
                int maxDifficulty = 0;
                for (int k = i - 1; k >= j - 1; k--) {
                    maxDifficulty = Math.max(maxDifficulty, jobDifficulty[k]);
                    if (dp[k][j - 1] != Integer.MAX_VALUE) {
                        dp[i][j] = Math.min(dp[i][j], dp[k][j - 1] + maxDifficulty);
                    }
                }
            }
        }

        return dp[n][d] == Integer.MAX_VALUE ? -1 : dp[n][d];
    }
}