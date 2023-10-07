public class Solution {
    private static final int MOD = 1000000007;

    public int numOfArrays(int n, int m, int k) {
        int[][][] dp = new int[n + 1][m + 1][k + 1];

        // Base case
        for (int j = 1; j <= m; j++) {
            dp[1][j][1] = 1;
        }

        // Fill the dp array using the transition
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                for (int l = 1; l <= k; l++) {
                    dp[i][j][l] = (int) ((dp[i][j][l] + (long) j * dp[i - 1][j][l]) % MOD);
                    for (int p = 1; p < j; p++) {
                        dp[i][j][l] = (int) ((dp[i][j][l] + (long) dp[i - 1][p][l - 1]) % MOD);
                    }
                }
            }
        }

        // Calculate the answer
        int ans = 0;
        for (int j = 1; j <= m; j++) {
            ans = (ans + dp[n][j][k]) % MOD;
        }

        return ans;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.numOfArrays(50, 100, 25));  // Expected output: 34549172
    }
}
