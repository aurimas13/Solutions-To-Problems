import java.util.*;

class Solution {
    /**
     * Computes the length of the longest arithmetic subsequence in an array. 
     * An arithmetic subsequence is a sequence of numbers in which the difference 
     * between any two consecutive elements is the same. The function takes an 
     * integer array `nums` as input and returns an integer representing the length 
     * of the longest arithmetic subsequence.
     *
     * @param  nums  an integer array representing the input sequence
     * @return       an integer representing the length of the longest arithmetic subsequence
     */
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer>[] dp = new HashMap[n];
        int max_length = 2;

        for (int i = 0; i < n; i++) {
            dp[i] = new HashMap<>();
            for (int j = 0; j < i; j++) {
                int diff = nums[i] - nums[j];
                dp[i].put(diff, dp[j].getOrDefault(diff, 1) + 1);
                max_length = Math.max(max_length, dp[i].get(diff));
            }
        }

        return max_length;
    }
}

