class Solution {
    public int subsetXORSum(int[] nums) {
        return backtrack(nums, 0, 0);
    }
    
    private int backtrack(int[] nums, int index, int currentXOR) {
        // If we've considered all elements, add the current XOR to the total sum
        if (index == nums.length) {
            return currentXOR;
        }
        // Recursively calculate the XOR sum including the current element
        int include = backtrack(nums, index + 1, currentXOR ^ nums[index]);
        // Recursively calculate the XOR sum excluding the current element
        int exclude = backtrack(nums, index + 1, currentXOR);
        // Return the sum of both choices
        return include + exclude;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.subsetXORSum(new int[]{1, 3}));  // Output: 6
        System.out.println(sol.subsetXORSum(new int[]{5, 1, 6}));  // Output: 28
        System.out.println(sol.subsetXORSum(new int[]{3, 4, 5, 6, 7, 8}));  // Output: 480
    }
}
