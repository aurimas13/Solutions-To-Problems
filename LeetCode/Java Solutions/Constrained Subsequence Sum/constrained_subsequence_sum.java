import java.util.Deque;
import java.util.LinkedList;

public class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];  // DP table representing the maximum sum ending at each element
        dp[0] = nums[0];

        Deque<Integer> maxDeque = new LinkedList<>();  // Deque to keep track of maximums
        maxDeque.offerFirst(0);  // Start with the first element

        for (int i = 1; i < n; i++) {
            // The front of the deque has the index of the maximum element for the last k entries
            dp[i] = nums[i] + Math.max(dp[maxDeque.peekFirst()], 0);

            // Maintain the deque: only keep elements that are in decreasing order of dp
            while (!maxDeque.isEmpty() && dp[i] >= dp[maxDeque.peekLast()]) {
                maxDeque.pollLast();
            }

            maxDeque.offerLast(i);

            // If the maximum element is out of the current window (k size), remove it
            if (i - k == maxDeque.peekFirst()) {
                maxDeque.pollFirst();
            }
        }

        // Find the maximum value in the dp table for the result
        int maxSum = dp[0];
        for (int i = 1; i < n; i++) {
            maxSum = Math.max(maxSum, dp[i]);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test cases
        int[] nums1 = {10, 2, -10, 5, 20};
        int k1 = 2;
        System.out.println(sol.constrainedSubsetSum(nums1, k1));  // Output: 37

        int[] nums2 = {-1, -2, -3};
        int k2 = 1;
        System.out.println(sol.constrainedSubsetSum(nums2, k2));  // Output: -1

        // Add more test cases as needed
    }
}
