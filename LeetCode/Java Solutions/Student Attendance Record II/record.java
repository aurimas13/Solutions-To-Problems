class Solution {
    public int checkRecord(int n) {
        int MOD = 1000000007;

        int[][][] dp = new int[n + 1][2][3];
        dp[0][0][0] = 1;  // Base case: One way to have an empty string

        for (int i = 1; i <= n; i++) {
            for (int A = 0; A < 2; A++) {
                for (int L = 0; L < 3; L++) {
                    // Add 'P': No restriction on L, and A remains the same
                    dp[i][A][0] = (dp[i][A][0] + dp[i - 1][A][L]) % MOD;
                    // Add 'A': Can only add if A is less than 1
                    if (A > 0) {
                        dp[i][A][0] = (dp[i][A][0] + dp[i - 1][A - 1][L]) % MOD;
                    }
                    // Add 'L': Can only add if L is less than 2
                    if (L > 0) {
                        dp[i][A][L] = (dp[i][A][L] + dp[i - 1][A][L - 1]) % MOD;
                    }
                }
            }
        }

        int result = 0;
        for (int A = 0; A < 2; A++) {
            for (int L = 0; L < 3; L++) {
                result = (result + dp[n][A][L]) % MOD;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkRecord(2));  // Output: 8
        System.out.println(sol.checkRecord(1));  // Output: 3
        System.out.println(sol.checkRecord(10101));  // Output: 183236316
    }
}
