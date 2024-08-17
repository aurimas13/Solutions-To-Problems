class Solution {
    public long maxPoints(int[][] points) {
        int m = points.length;
        int n = points[0].length;
        long[] dp = new long[n];
        
        // Initialize dp with the first row
        for (int j = 0; j < n; j++) {
            dp[j] = points[0][j];
        }
        
        for (int i = 1; i < m; i++) {
            long[] newDp = new long[n];
            long leftMax = 0;
            
            // Left to right
            for (int j = 0; j < n; j++) {
                leftMax = Math.max(leftMax - 1, dp[j]);
                newDp[j] = leftMax + points[i][j];
            }
            
            long rightMax = 0;
            // Right to left
            for (int j = n - 1; j >= 0; j--) {
                rightMax = Math.max(rightMax - 1, dp[j]);
                newDp[j] = Math.max(newDp[j], rightMax + points[i][j]);
            }
            
            dp = newDp;
        }
        
        long maxPoints = 0;
        for (long value : dp) {  // Changed 'points' to 'value'
            maxPoints = Math.max(maxPoints, value);
        }
        
        return maxPoints;
    }
}