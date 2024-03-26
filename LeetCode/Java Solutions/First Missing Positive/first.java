class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        // Mark numbers (num <= 0) and (num > n) with a special marker number (n + 1)
        for (int i = 0; i < n; ++i) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }
        
        // Use the index as a hash key and the sign as a presence detector
        for (int i = 0; i < n; ++i) {
            int num = Math.abs(nums[i]);
            if (num <= n) {
                nums[num - 1] = -Math.abs(nums[num - 1]);
            }
        }
        
        // Find the first cell which isn't negative (i.e. the smallest missing positive)
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }
        
        // If no cell was found, that means the answer is n + 1
        return n + 1;
    }
}
