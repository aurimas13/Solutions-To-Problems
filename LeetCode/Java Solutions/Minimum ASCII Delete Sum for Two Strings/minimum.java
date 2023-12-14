class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        // length of the strings
        int len1 = s1.length(), len2 = s2.length();

        // create a 2D DP table, the size is (len1+1) * (len2+1)
        // dp[i][j] represents the minimum ASCII delete sum for s1[0..i) and s2[0..j)
        int[][] dp = new int[len1+1][len2+1];
        
        // Initialize the first column
        for (int i = 1; i <= len1; i++)
            dp[i][0] = dp[i-1][0] + (int)s1.charAt(i-1);
        
        // Initialize the first row
        for (int j = 1; j <= len2; j++)
            dp[0][j] = dp[0][j-1] + (int)s2.charAt(j-1);

        // Fill the DP table using the recursion formula
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                // If current characters of both strings are same, no need to delete
                if (s1.charAt(i-1) == s2.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1];
                // Otherwise, delete either the current character of s1 or s2,
                // choose the one which costs less
                else
                    dp[i][j] = Math.min(dp[i-1][j] + (int)s1.charAt(i-1), dp[i][j-1] + (int)s2.charAt(j-1));
            }
        }

        // Return the final result
        return dp[len1][len2];
    }
}

