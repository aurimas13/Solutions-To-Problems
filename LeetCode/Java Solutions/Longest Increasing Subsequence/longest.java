import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums) {
        // Array to hold the smallest tail of all increasing subsequences with length i+1.
        int[] tails = new int[nums.length];
        int size = 0;
        
        for (int num : nums) {
            // Use binary search to find the insertion point
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < num) {
                    i = m + 1;
                } else {
                    j = m;
                }
            }
            // Update or extend the size of the 'tails' array
            tails[i] = num;
            if (i == size) {
                size++;
            }
        }
        return size;
    }
}
