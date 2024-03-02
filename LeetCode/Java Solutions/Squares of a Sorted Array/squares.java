class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];  // Initialize the result array
        int left = 0, right = n - 1;  // Two pointers
        for (int i = n - 1; i >= 0; i--) {  // Fill the result array from the end
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                result[i] = nums[right] * nums[right];
                right--;
            } else {
                result[i] = nums[left] * nums[left];
                left++;
            }
        }
        return result;
    }
}
