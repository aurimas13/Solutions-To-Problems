class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int[] dp = new int[n + 1];  // Initialize DP array with 0's

        for (int i = 1; i <= n; i++) {
            int maxVal = 0;
            for (int j = 1; j <= Math.min(k, i); j++) {
                maxVal = Math.max(maxVal, arr[i - j]);  // Find max in the last j elements
                dp[i] = Math.max(dp[i], dp[i - j] + maxVal * j);  // Update dp[i]
            }
        }

        return dp[n];  // Return the maximum sum after partitioning
    }
}
