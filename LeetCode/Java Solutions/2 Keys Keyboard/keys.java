class Solution {
    public int minSteps(int n) {
        int[] dp = new int[n + 1];
        
        for (int i = 2; i <= n; i++) {
            dp[i] = i;  // Worst case: i copy-paste operations
            for (int j = i - 1; j > 1; j--) {
                if (i % j == 0) {
                    dp[i] = Math.min(dp[i], dp[j] + i / j);
                    break;  // We only need the largest factor
                }
            }
        }
        
        return dp[n];
    }
}