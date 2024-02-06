public class Solution {
    Integer[][] memo;
    public int getLengthOfOptimalCompression(String s, int k) {
        memo = new Integer[s.length()][k + 1];
        int result = dp(s, 0, k);
        return result == Integer.MAX_VALUE ? 0 : result; // Handle case where result is MAX_VALUE
    }

    private int dp(String s, int i, int k) {
        // Base cases
        if (k < 0) return Integer.MAX_VALUE;
        if (i >= s.length()) return 0;
        if (s.length() - i <= k) return 0; // Can delete all remaining characters

        if (memo[i][k] != null) return memo[i][k];

        int minLen = dp(s, i + 1, k - 1); // Try deleting this character

        int len = 0, same = 0, diff = 0;
        for (int j = i; j < s.length(); j++) {
            if (s.charAt(j) == s.charAt(i)) {
                same++;
                if (same == 1 || same == 2 || same == 10 || same == 100) len++; // Increase length when hitting 1, 2, 10, or 100
            } else {
                if (++diff > k) break; // If more deletions are needed than allowed, break
            }
            // Try keeping this character and calculate the minimum length
            minLen = Math.min(minLen, len + dp(s, j + 1, k - diff));
        }

        memo[i][k] = minLen;
        return minLen;
    }
}
