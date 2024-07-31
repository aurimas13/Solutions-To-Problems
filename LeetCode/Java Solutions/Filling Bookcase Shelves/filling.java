class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int n = books.length;
        // dp[i] represents the minimum height for books[i:]
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[n] = 0;  // Base case: no books means 0 height

        for (int i = n - 1; i >= 0; i--) {
            int width = 0;
            int height = 0;
            for (int j = i; j < n && width + books[j][0] <= shelfWidth; j++) {
                width += books[j][0];
                height = Math.max(height, books[j][1]);
                dp[i] = Math.min(dp[i], height + dp[j + 1]);
            }
        }

        return dp[0];
    }
}
