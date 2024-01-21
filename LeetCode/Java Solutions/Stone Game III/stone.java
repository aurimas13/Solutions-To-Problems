class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        int[] dp = new int[n + 1];

        // Dynamic programming approach
        for (int i = n - 1; i >= 0; i--) {
            dp[i] = Integer.MIN_VALUE;
            int take = 0;
            // Consider taking 1, 2, or 3 stones
            for (int k = 0; k < 3; k++) {
                if (i + k < n) {
                    take += stoneValue[i + k];
                    // Calculate the maximum score difference
                    dp[i] = Math.max(dp[i], take - dp[i + k + 1]);
                }
            }
        }

        // Determine the winner based on the score difference
        if (dp[0] > 0) {
            return "Alice";
        } else if (dp[0] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
