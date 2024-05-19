import java.util.*;

class Solution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        int n = nums.length;
        Integer[] diff = new Integer[n];
        long totalSum = 0;
        
        // Calculate the total sum and differences
        for (int i = 0; i < n; i++) {
            diff[i] = (nums[i] ^ k) - nums[i];
            totalSum += nums[i];
        }
        
        // Sort the differences in descending order
        Arrays.sort(diff, Collections.reverseOrder());
        
        // Sum the pairs of the differences
        for (int i = 0; i < n; i += 2) {
            if (i + 1 == n) return totalSum;
            int pairSum = diff[i] + diff[i + 1];
            if (pairSum > 0) totalSum += pairSum;
        }
        
        return totalSum;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {24, 78, 1, 97, 44};
        int k = 6;
        int[][] edges = {{0, 2}, {1, 2}, {4, 2}, {3, 4}};
        System.out.println(sol.maximumValueSum(nums, k, edges));  // Expected output: 260
    }
}
