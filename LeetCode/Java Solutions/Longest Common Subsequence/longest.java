class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // Reverse the strings
        text1 = new StringBuilder(text1).reverse().toString();
        text2 = new StringBuilder(text2).reverse().toString();

        int m = text1.length();
        int n = text2.length();

        // Initialize memo array
        int[] memo = new int[n + 1];

        for (int i = 1; i <= m; i++) {
            int diag = 0;
            for (int j = 1; j <= n; j++) {
                int tmp = memo[j];
                // Update memo[j] based on whether characters match
                memo[j] = (text1.charAt(i - 1) == text2.charAt(j - 1)) ? diag + 1 : Math.max(memo[j], memo[j - 1]);
                diag = tmp;
            }
        }

        return memo[n];
    }
}
