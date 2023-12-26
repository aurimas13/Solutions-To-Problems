public class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        int MOD = 1000000007;

        // Initialize the dp array.
        int[][] dp = new int[n + 1][target + 1];
        dp[0][0] = 1;  // Base case: 1 way to achieve sum 0 with 0 dice

        for (int dice = 1; dice <= n; dice++) {
            for (int t = 1; t <= target; t++) {
                for (int face = 1; face <= k && face <= t; face++) {
                    dp[dice][t] = (dp[dice][t] + dp[dice - 1][t - face]) % MOD;
                }
            }
        }

        return dp[n][target];
    }
}


