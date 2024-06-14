import java.util.Arrays;

class Solution {
    public int minIncrementForUnique(int[] nums) {
        Arrays.sort(nums);
        int moves = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                int increment = nums[i - 1] - nums[i] + 1;
                nums[i] += increment;
                moves += increment;
            }
        }
        return moves;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {3, 2, 1, 2, 1, 7};
        System.out.println(sol.minIncrementForUnique(nums));  // Output: 6
    }
}
