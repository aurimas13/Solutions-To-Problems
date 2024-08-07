class Solution {
    public int minSwaps(int[] nums) {
        int n = nums.length;
        int ones = 0;
        for (int num : nums) {
            ones += num;
        }
        
        if (ones == 0) {
            return 0;
        }
        
        // Double the array to handle circular property
        int[] doubledNums = new int[2 * n];
        System.arraycopy(nums, 0, doubledNums, 0, n);
        System.arraycopy(nums, 0, doubledNums, n, n);
        
        // Initialize the window
        int zerosInWindow = 0;
        for (int i = 0; i < ones; i++) {
            if (doubledNums[i] == 0) {
                zerosInWindow++;
            }
        }
        int minSwaps = zerosInWindow;
        
        // Slide the window
        for (int i = ones; i < 2 * n; i++) {
            zerosInWindow -= (1 - doubledNums[i - ones]);  // Remove the leftmost element
            zerosInWindow += (1 - doubledNums[i]);  // Add the new rightmost element
            minSwaps = Math.min(minSwaps, zerosInWindow);
        }
        
        return minSwaps;
    }
}