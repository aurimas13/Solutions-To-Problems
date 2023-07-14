import java.util.HashMap;

class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        // Initialize a hashmap to keep track of the longest sequence ending at each number
        HashMap<Integer, Integer> dp = new HashMap<>();

        int res = 1;  // Initialize the result
        for (int num : arr) {  // Iterate over the input array
            // If num - difference is not in dp, set dp[num] to 1
            // Else set dp[num] to dp[num - difference] + 1
            dp.put(num, dp.getOrDefault(num - difference, 0) + 1);
            // Update the result if current sequence length is greater
            res = Math.max(res, dp.get(num));
        }
        
        // Return the result
        return res;
    }
}

