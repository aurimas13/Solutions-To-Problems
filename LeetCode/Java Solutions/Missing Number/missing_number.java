class Solution {
    public int missingNumber(int[] nums) {
        int missing = nums.length; // Initialize missing to n for the same reason
        for (int i = 0; i < nums.length; i++) {
            missing ^= i ^ nums[i];
        }
        return missing;
    }
}
