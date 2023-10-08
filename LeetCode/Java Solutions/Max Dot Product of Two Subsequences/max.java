public class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;

        // Initialize the dp table
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = -100000 * 100000;  // As a large negative value to ensure no overflow
            }
        }

        // Iterate through both arrays
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // Current dot product
                int curr = nums1[i - 1] * nums2[j - 1];

                // Update dp value based on the four options discussed above
                dp[i][j] = Math.max(dp[i][j], curr);
                dp[i][j] = Math.max(dp[i][j], dp[i - 1][j]);
                dp[i][j] = Math.max(dp[i][j], dp[i][j - 1]);
                if (dp[i - 1][j - 1] > 0) {  // Only add if the value is positive to avoid getting smaller dot product
                    dp[i][j] = Math.max(dp[i][j], dp[i - 1][j - 1] + curr);
                }
            }
        }

        // Return the result from the bottom-right corner of the dp table
        return dp[n][m];
    }
}
