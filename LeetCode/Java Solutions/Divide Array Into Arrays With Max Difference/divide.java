import java.util.Arrays;

class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);  // Sort the array first
        int n = nums.length / 3;
        int[][] result = new int[n][3];
        
        for (int i = 0, j = 0; i < nums.length; i += 3, j++) {
            if (nums[i + 2] - nums[i] <= k) {
                result[j] = new int[]{nums[i], nums[i + 1], nums[i + 2]};
            } else {
                return new int[0][];  // Condition not met, return an empty array
            }
        }
        
        return result;
    }
}
