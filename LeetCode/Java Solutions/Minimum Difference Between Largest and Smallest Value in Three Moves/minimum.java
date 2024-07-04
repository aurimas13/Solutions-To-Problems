import java.util.Arrays;

class Solution {
    public int minDifference(int[] nums) {
        if (nums.length <= 4) {
            return 0;
        }
        
        Arrays.sort(nums);
        
        int n = nums.length;
        return Math.min(Math.min(nums[n - 1] - nums[3], nums[n - 2] - nums[2]),
                        Math.min(nums[n - 3] - nums[1], nums[n - 4] - nums[0]));
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minDifference(new int[]{5, 3, 2, 4}));       // Output: 0
        System.out.println(sol.minDifference(new int[]{1, 5, 0, 10, 14}));  // Output: 1
        System.out.println(sol.minDifference(new int[]{3, 100, 20}));       // Output: 0
    }
}
