class Solution {
    public int kInversePairs(int n, int k) {
        final int MOD = 1000000007;  // Modulus for large numbers

        int[][] dp = new int[n + 1][k + 1];  // Initialize DP table
        dp[0][0] = 1;  // Base case: 1 way to form an empty array

        // Iterate over array sizes from 1 to n
        for (int i = 1; i <= n; i++) {
            int cumSum = 0;  // Initialize cumulative sum for the current row
            // Iterate over the number of inverse pairs from 0 to k
            for (int j = 0; j <= k; j++) {
                cumSum = (cumSum + dp[i - 1][j]) % MOD;  // Add the number of ways from the previous row
                if (j >= i)
                    cumSum = (cumSum - dp[i - 1][j - i] + MOD) % MOD;  // Subtract the number of ways exceeding the inverse pair limit
                dp[i][j] = cumSum;  // Update the DP table
            }
        }

        return dp[n][k];  // Return the number of ways for n elements and k inverse pairs
    }
}
