public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        
        // Fill the array with the maximum value
        for (int i = 0; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        
        // Base case
        dp[0] = 0;
        
        // Build up the dp table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        
        return dp[n];
    }
}
