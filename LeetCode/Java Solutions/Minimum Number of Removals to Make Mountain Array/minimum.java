class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int n = nums.length;
        
        // Find longest increasing subsequence from left to right
        int[] left = new int[n];
        Arrays.fill(left, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    left[i] = Math.max(left[i], left[j] + 1);
                }
            }
        }
        
        // Find longest increasing subsequence from right to left
        int[] right = new int[n];
        Arrays.fill(right, 1);
        for (int i = n - 2; i >= 0; i--) {
            for (int j = n - 1; j > i; j--) {
                if (nums[i] > nums[j]) {
                    right[i] = Math.max(right[i], right[j] + 1);
                }
            }
        }
        
        // Find minimum removals needed
        int maxLen = 0;
        for (int i = 1; i < n - 1; i++) {
            if (left[i] > 1 && right[i] > 1) {
                maxLen = Math.max(maxLen, left[i] + right[i] - 1);
            }
        }
        
        return n - maxLen;
    }
}