class Solution {
    public boolean PredictTheWinner(int[] nums) {
        // Create a memoization table
        int[][] memo = new int[nums.length][nums.length];
        // Fill the table with a default value
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                memo[i][j] = Integer.MIN_VALUE;
            }
        }
        return dp(nums, 0, nums.length - 1, memo) >= 0;
    }

    private int dp(int[] nums, int i, int j, int[][] memo) {
        // If this subproblem has been solved before, return the result
        if (memo[i][j] != Integer.MIN_VALUE) {
            return memo[i][j];
        }
        // If we are at the end of the array, return the last element
        if (i == j) {
            return nums[i];
        }
        // Calculate the maximum difference the first player can get over the second player
        // Either pick the first element and subtract the result of the rest array
        // Or pick the last element and subtract the result of the rest array
        memo[i][j] = Math.max(nums[i] - dp(nums, i+1, j, memo), nums[j] - dp(nums, i, j-1, memo));
        return memo[i][j];
    }
}
