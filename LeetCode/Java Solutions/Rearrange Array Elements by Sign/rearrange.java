class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int posIndex = 0, negIndex = 0;  // Pointers for filling positive and negative numbers
        
        // Separate and fill positive and negative numbers in the result array
        for (int num : nums) {
            if (num > 0) {
                result[posIndex * 2] = num;  // Place positive number
                posIndex++;
            } else {
                result[negIndex * 2 + 1] = num;  // Place negative number
                negIndex++;
            }
        }
        
        return result;
    }
}
