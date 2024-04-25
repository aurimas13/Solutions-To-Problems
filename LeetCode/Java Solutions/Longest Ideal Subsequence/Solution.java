public class Solution {
    public int longestIdealString(String s, int k) {
        // dp array to store the longest ideal substring length ending with each character
        int[] dp = new int[128]; // ASCII size, considering lowercase letters

        // Iterate through each character in the string
        for (char ch : s.toCharArray()) {
            int idx = (int) ch; // ASCII index of the character
            
            // Determine the maximum subsequence length ending with this character
            int maxLen = 0;
            // Check potential characters from `ch - k` to `ch + k`
            for (int i = Math.max(97, idx - k); i <= Math.min(122, idx + k); i++) {  // 'a' to 'z'
                maxLen = Math.max(maxLen, dp[i]);
            }
            
            // Update the dp for the current character
            dp[idx] = maxLen + 1;
        }

        // Find the maximum value in dp for all characters 'a' to 'z'
        int maxResult = 0;
        for (int i = 97; i <= 122; i++) { // From 'a' to 'z'
            maxResult = Math.max(maxResult, dp[i]);
        }

        return maxResult;
    }
}
