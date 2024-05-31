class Solution {
    public int[] singleNumber(int[] nums) {
        // Step 1: XOR all numbers
        int xorResult = 0;
        for (int num : nums) {
            xorResult ^= num;
        }
        
        // Step 2: Find a differentiating bit (rightmost set bit)
        int differentiatingBit = xorResult & -xorResult;
        
        // Step 3: Partition the numbers and XOR within each partition
        int num1 = 0;
        int num2 = 0;
        for (int num : nums) {
            if ((num & differentiatingBit) != 0) {
                num1 ^= num;
            } else {
                num2 ^= num;
            }
        }
        
        return new int[]{num1, num2};
    }

    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] result1 = sol.singleNumber(new int[]{1, 2, 1, 3, 2, 5});
        System.out.println(Arrays.toString(result1));  // Output: [3, 5]

        int[] result2 = sol.singleNumber(new int[]{-1, 0});
        System.out.println(Arrays.toString(result2));  // Output: [-1, 0]

        int[] result3 = sol.singleNumber(new int[]{0, 1});
        System.out.println(Arrays.toString(result3));  // Output: [1, 0]
    }
}
