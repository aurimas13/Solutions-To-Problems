import java.util.*;

class Solution {
    public int findRotateSteps(String ring, String key) {
        int n = ring.length(), m = key.length();
        List<Integer>[] pos = new List[26];
        for (int i = 0; i < 26; i++) pos[i] = new ArrayList<>();
        
        // Collect positions for each character in the ring
        for (int i = 0; i < n; i++) {
            pos[ring.charAt(i) - 'a'].add(i);
        }
        
        // dp[i][j]: minimum steps to process up to i-th character in key, ending with j-th character in ring
        int[][] dp = new int[m + 1][n];
        for (int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);
        dp[0][0] = 0; // Start at position 0 in ring
        
        for (int i = 1; i <= m; i++) {
            char ch = key.charAt(i - 1);
            for (int curPos : pos[ch - 'a']) {
                for (int k = 0; k < n; k++) {
                    if (dp[i - 1][k] != Integer.MAX_VALUE) {
                        int dist = Math.min(Math.abs(curPos - k), n - Math.abs(curPos - k));
                        dp[i][curPos] = Math.min(dp[i][curPos], dp[i - 1][k] + dist + 1);
                    }
                }
            }
        }
        
        // Find the minimal steps to complete the last character in key
        int minSteps = Integer.MAX_VALUE;
        for (int j = 0; j < n; j++) {
            minSteps = Math.min(minSteps, dp[m][j]);
        }
        
        return minSteps;
    }
}
