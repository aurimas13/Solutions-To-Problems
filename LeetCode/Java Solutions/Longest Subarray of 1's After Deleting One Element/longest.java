class Solution {
    public int longestSubarray(int[] nums) {
        // Keep track of the number of zeros seen
        int zeros = 0;
        
        // Keep track of the current length of subarray of ones
        int curr = 0;
        
        // Keep track of the maximum length of subarray of ones
        int maxLen = 0;
        
        // Keep track of the length of subarray just before the last zero
        int prev = 0;
        
        // Loop through each number in the array
        for (int num : nums) {
            // If the number is 1
            if (num == 1) {
                // Increment the current length
                curr++;
            // If the number is 0
            } else {
                // Increment the number of zeros seen
                zeros++;
                // Move the length of subarray just before the last zero
                // to prev, and reset current length
                prev = curr;
                curr = 0;
            }
            
            // Update the maximum length
            maxLen = Math.max(maxLen, prev + curr);
        }
        
        // If the array has at least one zero, then we can get the maximum
        // length by deleting one element. Otherwise, we should reduce
        // the length by 1 as we have to delete one element
        return zeros > 0 ? maxLen : maxLen - 1;
    }
}

// Time complexity: O(n), where n is the number of elements in the input array.
// Space complexity: O(1), as we are using only a constant amount of space.

